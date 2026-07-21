export const meta = {
  name: 'okf-notability-triage',
  description: 'Score single-video entity candidates for notability; produce a filtered add-list',
  phases: [{ title: 'Triage', detail: 'rubric-score single-video entities KEEP/DROP' }],
}

const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'
const SLICES = 5
const PER = 25 // covers up to 125 single-video entities

const schema = { type: 'object', additionalProperties: false,
  properties: {
    decisions: { type: 'array', items: { type: 'object', additionalProperties: false,
      properties: {
        slug: { type: 'string' },
        decision: { type: 'string', enum: ['keep', 'drop'] },
        reason: { type: 'string' },
      }, required: ['slug', 'decision', 'reason'] } },
  }, required: ['decisions'] }

const prompt = (i) => `You are triaging candidate ENTITY pages for an OKF knowledge base built from Cole Medin's YouTube channel. Each candidate appeared in only ONE video. Decide which deserve their own page.

STEP 1: Read ${B}/scripts/add_manifest.json. Take its "entities" array, FILTER to those with 1 or fewer supporting_videos, keep file order, and work ONLY on items at 0-indexed positions ${i * PER} through ${i * PER + PER - 1} of that filtered list. If that range is past the end, return an empty decisions array.

STEP 2: For each candidate in your range, decide KEEP or DROP using this rubric.

KEEP if ANY of these is true:
- It is a widely-known product, model, company, framework, or person in the AI/dev ecosystem that a reader would plausibly look up (e.g. a major LLM release, a well-known coding tool, a major cloud/company, a notable public figure).
- It is central to the video's subject (the thing the video is ABOUT), not a passing mention.
- It is a durable piece of infrastructure/tooling that recurs in the broader ecosystem even if Cole covered it once (e.g. a standard protocol, a common language/runtime/database, a popular editor).

DROP if ANY of these is true:
- It appears only as a SPONSOR read / advertisement with no substantive teaching.
- It is a tiny, obscure, or short-lived micro-tool, a one-off demo dependency, or a personal side project with little external significance.
- It is so generic that an existing page already covers the idea better, or it adds noise rather than knowledge.
- It is a private/internal thing unlikely to be asked about.

Be discriminating: a knowledge base is degraded by thin pages about things nobody will ask about. When genuinely torn, prefer DROP for obscure tools and KEEP for well-known named models/companies.

Return via schema: decisions[] with {slug, decision, reason (max 12 words)} for every candidate in your range.`

phase('Triage')
const results = await parallel(
  Array.from({ length: SLICES }, (_, i) => () =>
    agent(prompt(i), { label: `triage:${i}`, phase: 'Triage', agentType: 'general-purpose', schema })
      .catch(() => null)
  )
)
const decisions = results.filter(Boolean).flatMap((r) => r.decisions || [])
const keep = decisions.filter((d) => d.decision === 'keep')
const drop = decisions.filter((d) => d.decision === 'drop')
return {
  scored: decisions.length,
  keep: keep.length,
  drop: drop.length,
  keep_slugs: keep.map((d) => d.slug),
  drop_slugs: drop.map((d) => d.slug),
  drop_reasons: drop.slice(0, 40).map((d) => `${d.slug}: ${d.reason}`),
}
