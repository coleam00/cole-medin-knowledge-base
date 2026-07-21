export const meta = {
  name: 'okf-polish',
  description: 'ASR proper-noun cleanup across all authored pages, then enrich entity ## Related sections',
  phases: [
    { title: 'ASR', detail: 'fix transcription errors of names/terms in quotes + prose (528 pages)' },
    { title: 'Related', detail: 'rewrite entity ## Related into typed, described links (144 pages)' },
  ],
}

const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'
const N_AUTHORED = 528
const N_ENTITIES = 144
const A_BATCH = 7
const E_BATCH = 6
const chunkCount = (n, size) => Math.ceil(n / size)

const GLOSSARY = `CANONICAL NAMES (correct spellings to normalize toward):
Anthropic, Claude, Claude Code, Claude Agent SDK, Claude Desktop, Claude 3.5 Sonnet, Sonnet, Opus, Haiku, OpenAI, ChatGPT, Codex, GPT-4, GPT-4o, OpenAI Swarm, OpenAI Agents SDK, Google, Gemini, Gemini CLI, Meta, Llama, DeepSeek, DeepSeek R1, DeepSeek V3, Qwen, Nvidia, Groq, Cohere, Hugging Face, Mistral, OpenRouter, Ollama,
Cursor, Windsurf, Cline, Aider, Kiro, OpenClaw, Pi, Gemini CLI, Agent Zero, Manus, Lovable, Bolt.new, bolt.diy, Flowise, Voiceflow, n8n, Archon, Vercel, Vercel AI SDK, Netlify, Render, RunPod, Docker, Caddy, FastAPI, Uvicorn, Streamlit, Next.js, React, Python,
Pydantic AI, LangChain, LangGraph, LangSmith, LangServe, Langfuse, Logfire, CrewAI, CopilotKit, AG-UI, A2UI, Arcade, MCP (Model Context Protocol), Model Context Protocol,
Supabase, Postgres, Neon, MongoDB, Redis, Firebase, Neo4j, Qdrant, Pinecone, Chroma, Weaviate, Graphiti, Mem0, LightRAG, Context7, Crawl4AI, Docling, nomic-embed-text,
Playwright, Browserbase, Sentry, CodeRabbit, Snyk, Sonar, QA Tech, GitHub, Git, Git Worktrees, Jira, Linear, Asana, Slack, Telegram, Zapier, Obsidian, ElevenLabs, Cartesia, Vapi, Aqua Voice, Karpathy, Andrej Karpathy, Cole Medin, Boris Cherny, Dan Shapiro,
techniques: RAG, agentic RAG, agentic search, subagent, subagents, agent teams, context engineering, Kanban board, no-code, vibe coding, the PIV loop, knowledge graph, vector database, reranking, chunking.

KNOWN ASR ERRORS -> CORRECTION (examples of the kind of thing to fix):
"Enthropic"->"Anthropic"; "clae"/"clod"/"cloud 3.5"->"Claude"; "Sonet"->"Sonnet"; "pantic AI"/"pedantic AI"->"Pydantic AI"; "Lang graph"->"LangGraph"; "Lang chain"->"LangChain"; "Lang smith"->"LangSmith"; "canban"->"Kanban"; "noode"/"no code"->"no-code" (as adjective); "Kira"/"Kirao"->"Kiro"; "sub aents"/"subaents"/"sub agents"->"subagents"; "Codeex"->"Codex"; "Sue Bass"/"supabbase"->"Supabase"; "N8N"/"n8 n"->"n8n"; "post gres"->"Postgres"; "Neo forj"->"Neo4j"; "Quadrant"->"Qdrant" (when it means the vector DB); "graphi tea"->"Graphiti".`

const RULES = `STRICT RULES:
- Fix ONLY clear transcription errors of PROPER NOUNS and TECHNICAL TERMS (names of tools, companies, people, models, protocols, techniques) to their canonical spelling from the glossary.
- PRESERVE timestamps exactly ([H:MM:SS]). PRESERVE meaning, sentence structure, and all other wording. Do NOT paraphrase, do NOT fix grammar/filler, do NOT rewrite quotes beyond the specific misspelled name/term.
- Do NOT touch YAML frontmatter. Do NOT change slugs or link paths. Do NOT add or remove sentences.
- If you are not confident a token is an ASR error of a known name/term, LEAVE IT. Conservative is correct.
- Keep the source-citation format exact: '- [Title](../sources/<slug>.md) - "[H:MM:SS] quote"'.
- Use the Edit tool for surgical find/replace. Make each replacement specific enough to be unique.`

// ---------------------------------------------------------------- ASR
log(`ASR cleanup over ${N_AUTHORED} authored pages`)
const asrBatches = chunkCount(N_AUTHORED, A_BATCH)
const asrAcks = await parallel(
  Array.from({ length: asrBatches }, (_, i) => () =>
    agent(
      `Normalize ASR (auto-transcript) proper-noun and technical-term errors in a batch of OKF wiki pages.

STEP 1: Use the Read tool on ${B}/scripts/authored_pages.txt. Your batch is the lines from index ${i * A_BATCH + 1} through ${i * A_BATCH + A_BATCH} (1-indexed; some may not exist at the tail, skip those). Each line is a relative page path.
STEP 2: For each page path, read ${B}/<path>, scan the BODY (quotes under '## Sources', '## Key moments', and prose) for garbled names/terms, and apply surgical Edits to correct them.

${GLOSSARY}

${RULES}

Return a tiny ack: "batch ${i}: <n_pages> pages, <n_fixes> fixes".`,
      { label: `asr:${i}`, phase: 'ASR', agentType: 'general-purpose' }
    )
  )
)
log(`ASR done: ${asrAcks.filter(Boolean).length}/${asrBatches} batches`)

// ---------------------------------------------------------------- RELATED (barrier: after ASR)
phase('Related')
log(`Enriching ## Related on ${N_ENTITIES} entity pages`)
const relBatches = chunkCount(N_ENTITIES, E_BATCH)
const relAcks = await parallel(
  Array.from({ length: relBatches }, (_, i) => () =>
    agent(
      `Improve the '## Related' section of a batch of OKF ENTITY pages so they read as richly as the concept pages (typed subheadings + one-line descriptions), instead of a bare list of undescribed links.

STEP 1: Use the Read tool on ${B}/scripts/entity_pages.txt. Your batch is lines ${i * E_BATCH + 1} through ${i * E_BATCH + E_BATCH} (1-indexed; skip any past the end). Each line is a relative entity page path (entities/tools|people|organizations/<slug>.md).
STEP 2: For each entity page:
  a. Read the page ${B}/<path>.
  b. Read its spec ${B}/scripts/pages/entities/<slug>.json for the 'related' slug list (the canonical concepts/entities it connects to).
  c. Read ${B}/scripts/slug_index.json to resolve correct RELATIVE link paths (use rel_from_entity_tool for sibling tools when the page is a tool; concepts are ../../concepts/<slug>.md; sibling tools ../tools/<slug>.md; people ../people/<slug>.md; orgs ../organizations/<slug>.md; sources ../../sources/<slug>.md). Only link slugs that exist in slug_index.
  d. To get the one-line description for each linked target, read that target page's frontmatter 'description' (or the concept/entity spec) and use it verbatim (trim to one line).
STEP 3: REPLACE ONLY the '## Related' section (and, where it improves clarity, split it into typed subheadings) with descriptive bullets. Use these headings by meaning, matching the concept pages:
  '## Implemented by' or '## Realizes' - concepts this tool/entity implements or embodies
  '## Contrasts with' - competing/alternative tools
  '## Works with' - tools it composes with
  '## Related' - everything else worth a hop
Each bullet: '- [Title](rel-path) - one-line description.' Keep the mandatory '## Sources' section and ALL other content EXACTLY as-is. Do not touch frontmatter or quotes.
- NEVER use em dashes; use ' - ' (hyphen) as the separator, matching the rest of the bundle.
- Every link MUST resolve (only slug_index slugs). Aim for 4-10 well-described links per page where the related list supports it.

Return a tiny ack: "rel batch ${i}: <n_pages> pages".`,
      { label: `related:${i}`, phase: 'Related', agentType: 'general-purpose' }
    )
  )
)
log(`Related done: ${relAcks.filter(Boolean).length}/${relBatches} batches`)

return { asrBatches, asrOk: asrAcks.filter(Boolean).length, relBatches, relOk: relAcks.filter(Boolean).length }
