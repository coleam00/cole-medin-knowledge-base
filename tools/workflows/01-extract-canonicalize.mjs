export const meta = {
  name: 'okf-extract-canonicalize',
  description: 'Mine concepts/entities from every channel transcript, then dedupe into one canonical OKF taxonomy + manifest',
  phases: [
    { title: 'Extract', detail: 'one agent per transcript -> extractions/<slug>.json' },
    { title: 'Aggregate', detail: 'merge extractions -> candidates.json, cluster by topic' },
    { title: 'Canonicalize', detail: 'per-cluster slug dedup into canonical pages' },
    { title: 'Merge', detail: 'cross-cluster merge -> manifest.json + taxonomy.json' },
  ],
}

// args = { bundle: absPath }.  (Workflow args reliably carry only one key, so count is fixed here.)
const BUNDLE = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'
const N = 198  // number of transcripts in raw/ (see scripts/slugs.txt)

// Canonical slugs from the proven 20-video build of this same channel (taxonomy seed).
const POC = {
  concepts: ['adversarial-agents','agentic-coding','agentic-rag','agentic-search','agentic-workflow-engineering','agent-teams','ai-coding-harness','chunking','clarifying-questions','claude-code-hooks','codebase-indexing','code-execution','code-review','commandify-everything','context-aware-chunking','context-engineering','context-isolation','context-reset','context-rot','contextual-retrieval','contract-first','deterministic-workflows','end-to-end-validation','fine-tuned-embeddings','git-as-long-term-memory','global-rules','heartbeat','hierarchical-rag','human-in-the-loop','hybrid-search','issue-is-the-spec','keyword-search','knowledge-bases','knowledge-graphs','late-chunking','lethal-trifecta','mcp-problems','memory-systems','model-selection','multi-query-rag','parallel-agentic-coding','phases-of-work','planning-with-ai','prd-first-development','prime-command','progressive-disclosure','provider-independence','query-expansion','rag','reciprocal-rank-fusion','reduce-assumptions','reranking','second-brain','self-evolving-memory','self-reflective-rag','semantic-search','separate-reviewer','skills','slash-commands','spec-driven-development','strategy-stacking','structured-vs-unstructured-data','subagents-pattern','sycophancy','system-evolution','the-ai-layer','the-evolution-of-ai-coding','the-llm-wiki','the-piv-loop','the-whisk-framework','traditional-rag','two-layer-planning','validation','vector-embeddings','vibe-coding','when-rag-is-dead'],
  tools: ['agent-browser','aider','arcade','archon','claude-agent-sdk','claude-code','cline','codex','docling','github','git-worktree','graphiti','jira','linear','mcp','mongodb','neon','obsidian','openclaw','pi-coding-agent','postgres-pgvector','pydantic-ai','qa-tech','ripgrep'],
  people: ['andrej-karpathy','boris-cherny','cole-medin','lior-weinstein','mario-zechner','nick-baumann'],
  orgs: ['anthropic','cto-ai','dynamous','earendil-works','openai','stripe'],
}
const seed = `For consistency, these canonical slugs already exist from a 20-video build of this SAME channel — reuse them when a candidate matches: CONCEPTS=[${POC.concepts.join(', ')}]; TOOLS=[${POC.tools.join(', ')}]; PEOPLE=[${POC.people.join(', ')}]; ORGS=[${POC.orgs.join(', ')}].`

log(`Extracting from ${N} transcripts under ${BUNDLE}`)

// ---------------------------------------------------------------- EXTRACT
// Each agent resolves its own slug from line i of scripts/slugs.txt (avoids moving the list into JS).
const extractPrompt = (i) => `You are mining ONE YouTube video transcript for an Open Knowledge Format (OKF) knowledge base of Cole Medin's channel.

STEP 1 — resolve your slug: Use the Read tool on ${BUNDLE}/scripts/slugs.txt. Your assigned slug is the entry on LINE ${i + 1} (1-indexed, one slug per line). Call it SLUG.
STEP 2 — read the transcript in full: ${BUNDLE}/raw/<SLUG>.md
STEP 3 — extract the durable CONCEPTS (ideas, techniques, patterns, mental models) and ENTITIES (tools, people, organizations) this video teaches, with timestamped supporting quotes.
STEP 4 — WRITE (Write tool) the result as JSON to: ${BUNDLE}/scripts/extractions/<SLUG>.json

JSON schema:
{
  "slug": "<SLUG>",
  "thesis": "one-sentence thesis of the video",
  "summary": "2-3 paragraph synthesized summary of what the video teaches (not a transcript dump)",
  "tags": ["3-7 lowercase topic tags"],
  "key_moments": [{"ts":"H:MM:SS","note":"what happens here"}],
  "concepts": [
    {"slug":"kebab-stable-id","name":"Display Name","one_liner":"one sentence definition","tags":["..."],
     "quotes":[{"ts":"H:MM:SS","text":"verbatim quote <=240 chars supporting this concept"}],
     "related":["other-concept-or-entity-slugs"]}
  ],
  "entities": [
    {"slug":"kebab","name":"Display Name","subtype":"tool|person|organization","one_liner":"what it is / why it matters here",
     "resource":"canonical URL if clearly known else omit","quotes":[{"ts":"H:MM:SS","text":"verbatim quote"}]}
  ]
}

Rules:
- Use STABLE, GENERAL slugs so the same idea across videos collapses later ("the-piv-loop" not "plan-implement-validate-loop"; "context-engineering" not "engineering-the-context"). ${seed}
- Only extract what the video ACTUALLY teaches substantively. Aim for 5-20 concepts and 3-15 entities by density. Older/off-topic videos may yield fewer — that is fine.
- Quotes must be verbatim from THIS transcript with real timestamps. 1-3 per concept.
- Include Cole Medin once as an entity (slug "cole-medin", person) if natural.
- Output ONLY the file write, then return a tiny ack: "<SLUG>: <n_concepts>c/<n_entities>e".`

const extractAcks = await parallel(
  Array.from({ length: N }, (_, i) => () =>
    agent(extractPrompt(i), { label: `extract:${i}`, phase: 'Extract', agentType: 'general-purpose' })
  )
)
const okExtracts = extractAcks.filter(Boolean).length
log(`Extract done: ${okExtracts}/${N} transcripts produced extractions`)

// ---------------------------------------------------------------- AGGREGATE
phase('Aggregate')
const agg = await agent(
  `Aggregate all per-video extraction JSON files into a single deduplicated candidate list, using Python.

Input dir: ${BUNDLE}/scripts/extractions/  (one <slug>.json per video)
Each has: slug, thesis, summary, tags, key_moments, concepts[{slug,name,one_liner,tags,quotes[{ts,text}],related[]}], entities[{slug,name,subtype,one_liner,resource?,quotes[{ts,text}]}].

Write a Python script that:
1. Loads every extractions/*.json.
2. Groups CONCEPT candidates by normalized slug (lowercase; keep the most common full slug as display; trim; collapse hyphens). Per group: slug, name variants, video_count (distinct videos), videos:[slugs], one_liners (up to 5), tags (union top 10), total_quotes.
3. Same for ENTITY candidates (also subtype by majority vote, resource = first non-empty).
4. Assign each concept candidate a rough "cluster" = its single most common tag; merge tiny clusters (<3 concepts) into "other"; aim for 6-14 clusters.
5. Write ${BUNDLE}/scripts/candidates.json:
   {"clusters":["..."],"concepts":[{slug,names,video_count,videos,one_liners,tags,cluster}...sorted by video_count desc],"entities":[{slug,subtype,names,video_count,videos,one_liners,resource,tags}...]}
6. Also write ${BUNDLE}/scripts/clusters.txt (one cluster name per line, same order as candidates.json "clusters").

Do NOT drop anything yet (keep singletons). Then RETURN via the schema: n_clusters, n_concept_candidates, n_entity_candidates. Also print a short human summary (cluster list with counts + top 15 concepts by video_count).`,
  { label: 'aggregate', phase: 'Aggregate', agentType: 'general-purpose',
    schema: { type: 'object', additionalProperties: true,
      properties: { n_clusters: { type: 'integer' }, n_concept_candidates: { type: 'integer' }, n_entity_candidates: { type: 'integer' } },
      required: ['n_clusters'] } }
)
const nClusters = agg.n_clusters
log(`Aggregate: ${nClusters} clusters, ${agg.n_concept_candidates} concept candidates, ${agg.n_entity_candidates} entity candidates`)

// ---------------------------------------------------------------- CANONICALIZE (per cluster index)
phase('Canonicalize')
const canonPrompt = (i) => `You are canonicalizing ONE topic cluster of candidate concepts for an OKF knowledge base mined from Cole Medin's channel.

STEP 1: Use the Read tool on ${BUNDLE}/scripts/clusters.txt. Your cluster is the name on LINE ${i + 1} (1-indexed). Call it CLUSTER.
STEP 2: Read ${BUNDLE}/scripts/candidates.json and work ONLY on concepts whose "cluster" == CLUSTER.
STEP 3: Deduplicate near-identical candidates into canonical concept pages by MERGING (e.g. "piv-loop"+"the-piv-loop"+"plan-implement-validate" -> one "the-piv-loop"). ${seed}
Rules:
- KEEP a concept as its own page if it appears in >=2 videos OR is a substantial, clearly link-worthy idea even in 1 deep-dive video. Otherwise fold its videos into the concept it belongs under.
- Choose the clearest canonical slug + Title Case name + a crisp one-sentence description.
- Assign each canonical concept a human-readable THEME label (a few words, e.g. "Context engineering", "RAG & retrieval", "Planning").
STEP 4: WRITE (Write tool) to ${BUNDLE}/scripts/canon/concepts-cluster-${i}.json:
{"cluster":"<CLUSTER>","concepts":[{"slug":"the-piv-loop","title":"The PIV Loop","description":"one sentence","theme":"Agentic coding foundations","tags":["..."],"members":["piv-loop","the-piv-loop"],"videos":["slugA","slugB"]}]}
Return a tiny ack: "<CLUSTER>: <n_canonical> from <n_candidates>".`

const canonAcks = await parallel(
  Array.from({ length: nClusters }, (_, i) => () =>
    agent(canonPrompt(i), { label: `canon:${i}`, phase: 'Canonicalize', agentType: 'general-purpose' })
  )
)
log(`Cluster canonicalization done: ${canonAcks.filter(Boolean).length}/${nClusters}`)

// ---------------------------------------------------------------- MERGE
phase('Merge')
const merge = await agent(
  `Build the FINAL frozen manifest + taxonomy for the OKF knowledge base. This is the contract the page-writing phase follows, so be careful and complete. Use Python for deterministic assembly and your judgment for cross-cluster merges + entity canonicalization + theme ordering.

Inputs:
- ${BUNDLE}/scripts/candidates.json                (all candidates + videos/quotes refs)
- ${BUNDLE}/scripts/canon/concepts-cluster-*.json  (per-cluster canonical concepts with member candidate slugs)
- ${BUNDLE}/scripts/extractions/*.json             (per-video actual quotes {ts,text} per candidate, + source thesis/summary/key_moments)
- ${BUNDLE}/raw/manifest.json                      (video metadata: slug,title,url,published,duration,recency_rank)

${seed}

Steps:
1. CONCEPTS: union all per-cluster canonical concepts; detect+merge cross-cluster duplicates into one (clearest slug); build a member->canonical map.
2. ENTITIES: canonicalize entity candidates the same way (merge near-dupes; subtype by majority; keep a resource if any had one). Keep an entity if it appears in >=2 videos OR is a well-known tool/person/org even at 1 video. Give tools a theme group (e.g. "Coding agents","RAG & data"); people/orgs are flat.
3. For each kept CONCEPT and ENTITY, gather evidence by walking member candidate slugs back through extractions/*.json: up to 3 timestamped quotes {ts,text} per source video. Sort a page's videos by manifest recency_rank.
4. SOURCES: one per video from manifest.json + the extraction's thesis/summary/key_moments; map each video's extracted candidate slugs THROUGH the canonical maps to canonical slugs (dedup) for linking.
5. WRITE ${BUNDLE}/scripts/manifest.json:
   {"concepts":[{slug,title,description,theme,tags,related:[canonical_slugs],videos:[{slug,title,url,quotes:[{ts,text}]}]}],
    "entities":[{slug,title,subtype,description,theme,resource,tags,related:[canonical_slugs],videos:[{slug,title,url,quotes:[{ts,text}]}]}],
    "sources":[{slug,title,url,published,duration,recency_rank,thesis,summary,key_moments:[{ts,note}],concepts:[canonical_slugs],entities:[canonical_slugs]}]}
   (a concept's related[] = canonicalized union of its members' "related" refs, limited to slugs that exist in the final sets.)
6. WRITE ${BUNDLE}/scripts/taxonomy.json:
   {"concept_themes":[["Theme",[concept_slugs in order]],...],   // every kept concept exactly once
    "tool_themes":[["Group",[tool_slugs]],...],
    "source_clusters":[["Cluster",[source_slugs]],...]}          // group videos into 6-12 thematic clusters; every source exactly once

Validate before finishing: every concept/entity slug in taxonomy.json exists in manifest.json and vice-versa; every related[]/concepts[]/entities[] slug resolves to a real page; every source in manifest appears in exactly one source_cluster. Fix mismatches.

RETURN via the schema: n_concepts, n_entities, n_tools, n_people, n_orgs, n_sources, and themes (array of {name, size} for concept themes in order). Also print any deliberately-dropped candidate count.`,
  { label: 'merge-manifest', phase: 'Merge', agentType: 'general-purpose', effort: 'high',
    schema: { type: 'object', additionalProperties: true,
      properties: {
        n_concepts: { type: 'integer' }, n_entities: { type: 'integer' },
        n_tools: { type: 'integer' }, n_people: { type: 'integer' }, n_orgs: { type: 'integer' },
        n_sources: { type: 'integer' },
        themes: { type: 'array', items: { type: 'object', additionalProperties: false,
          properties: { name: { type: 'string' }, size: { type: 'integer' } }, required: ['name', 'size'] } },
      },
      required: ['n_concepts', 'n_entities', 'n_sources', 'themes'] } }
)

return { extracts: okExtracts, nClusters, aggregate: agg, merge }
