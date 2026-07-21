export const meta = {
  name: 'okf-gap-detect',
  description: 'Detect durable coverage gaps across all videos, then canonicalize into a deduped add-list',
  phases: [
    { title: 'Detect', detail: 'per-video: which mined ideas lack a covering page' },
    { title: 'Merge', detail: 'dedupe gaps -> add_manifest.json (new concept/entity pages)' },
  ],
}

const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'
const N = 198

const gapSchema = { type: 'object', additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    gaps: { type: 'array', items: { type: 'object', additionalProperties: false,
      properties: {
        idea: { type: 'string' },
        kind: { type: 'string', enum: ['concept', 'entity'] },
        subtype: { type: 'string', enum: ['tool', 'person', 'organization', 'none'] },
        one_liner: { type: 'string' },
      }, required: ['idea', 'kind', 'subtype', 'one_liner'] } },
  }, required: ['slug', 'gaps'] }

const detectPrompt = (i) => `You are finding COVERAGE GAPS in an OKF knowledge base of Cole Medin's channel: durable, link-worthy ideas/tools a video teaches that have NO page yet.

STEP 1: Read ${B}/scripts/slugs.txt; your video is the slug on LINE ${i + 1} (1-indexed). Call it SLUG.
STEP 2: Read ${B}/scripts/extractions/<SLUG>.json — it lists the concepts[] and entities[] this video teaches (each with name + one_liner + quotes).
STEP 3: Read the current coverage: ${B}/concepts/index.md and ${B}/entities/tools/index.md , ${B}/entities/people/index.md , ${B}/entities/organizations/index.md.
STEP 4: For each idea the video teaches, decide if it is a GENUINE GAP. It is a gap only if BOTH:
  (a) it is durable / link-worthy — a real concept, or a NAMED tool/company/person/model that is central to the video or recurs (well-known named products count even from one video), AND
  (b) NO existing page reasonably covers it (match by MEANING against the indexes, not exact string; if it is adequately folded into a broader existing page, it is NOT a gap).
Be conservative but do flag notable NAMED products/models/companies that clearly lack their own page (e.g. a specific model release, a specific framework/product).

Write nothing. Return via schema: slug=SLUG, gaps=[{idea (canonical Title Case name), kind (concept|entity), subtype (tool|person|organization for entities, else "none"), one_liner}]. Empty gaps if the video is fully covered.`

phase('Detect')
const detected = await parallel(
  Array.from({ length: N }, (_, i) => () =>
    agent(detectPrompt(i), { label: `detect:${i}`, phase: 'Detect', agentType: 'general-purpose', schema: gapSchema })
      .catch(() => null)
  )
)
const rows = detected.filter(Boolean)
const rawGaps = rows.flatMap((r) => (r.gaps || []).map((g) => ({ ...g, video: r.slug })))
log(`Detect: ${rows.length}/${N} videos scanned, ${rawGaps.length} raw gap mentions`)

// Persist raw gaps so the merge agent can work from disk (via one writer agent).
await agent(
  `Write this JSON array verbatim to ${B}/scripts/gaps/raw_gaps.json (create the file). It is a list of gap mentions across videos:\n\n${JSON.stringify(rawGaps)}`,
  { label: 'persist-gaps', phase: 'Detect', agentType: 'general-purpose' }
)

// ---- Merge ----
phase('Merge')
const merge = await agent(
  `Deduplicate raw coverage-gap mentions into a canonical ADD-LIST of new pages for the OKF knowledge base. Use Python for grouping and your judgment for merging + thresholds.

Inputs:
- ${B}/scripts/gaps/raw_gaps.json  — list of {idea, kind, subtype, one_liner, video} across all videos.
- ${B}/scripts/extractions/*.json  — per-video mined data (name, one_liner, quotes[{ts,text}]) to gather supporting quotes.
- ${B}/raw/manifest.json           — video metadata (slug,title,url,published,recency_rank).
- Existing pages: ${B}/concepts/*.md and ${B}/entities/**/*.md (to AVOID re-proposing anything already covered).

Steps:
1. Group gap mentions that refer to the same idea (fuzzy: "Meta-Harness"=="Meta Harness"=="meta harness"). Count how many videos mention each; collect the video slugs.
2. DROP any gap whose idea is actually already a page (check against existing concept/entity slugs + titles). Keep only genuinely-new ideas.
3. Threshold: keep a new CONCEPT if >=2 videos mention it OR it is clearly central/durable; keep a new ENTITY if it is a notable named product/model/company/person (even 1 video is fine for a well-known named entity). Drop weak/vague singletons.
4. Assign each kept new page: a canonical kebab slug (not colliding with existing files), Title Case title, one-sentence description, kind (concept|entity), subtype (for entities), a theme label (reuse the bundle's existing concept themes / tool groups where possible), and supporting_videos = list of {slug, up to 3 quotes {ts,text}} gathered from those videos' extractions.
5. WRITE ${B}/scripts/add_manifest.json:
   {"concepts":[{slug,title,description,theme,tags,supporting_videos:[{slug,quotes:[{ts,text}]}]}],
    "entities":[{slug,title,subtype,description,theme,resource?,tags,supporting_videos:[{slug,quotes:[{ts,text}]}]}]}

Validate: no slug collides with an existing page; every supporting quote is copied from a real extraction. RETURN via schema: n_new_concepts, n_new_entities (by subtype), and a short list of the new page titles.`,
  { label: 'merge-gaps', phase: 'Merge', agentType: 'general-purpose', effort: 'high',
    schema: { type: 'object', additionalProperties: true,
      properties: {
        n_new_concepts: { type: 'integer' }, n_new_entities: { type: 'integer' },
        n_new_tools: { type: 'integer' }, n_new_people: { type: 'integer' }, n_new_orgs: { type: 'integer' },
        new_titles: { type: 'array', items: { type: 'string' } },
      }, required: ['n_new_concepts', 'n_new_entities', 'new_titles'] } }
)

return { videos: rows.length, rawGaps: rawGaps.length, merge }
