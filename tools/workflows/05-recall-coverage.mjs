export const meta = {
  name: 'okf-recall',
  description: 'Sample videos, extract core ideas, check whether each durable idea has a page (coverage/recall test)',
  phases: [{ title: 'Recall', detail: 'per-video: extract ideas -> check page coverage -> flag genuine gaps' }],
}

const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'
const N = 25

const schema = { type: 'object', additionalProperties: false,
  properties: {
    slug: { type: 'string' },
    total_core_ideas: { type: 'integer' },
    covered: { type: 'integer' },
    gaps: { type: 'array', items: { type: 'object', additionalProperties: false,
      properties: { idea: { type: 'string' }, kind: { type: 'string', enum: ['concept', 'entity'] }, why_durable: { type: 'string' } },
      required: ['idea', 'kind', 'why_durable'] } },
  }, required: ['slug', 'total_core_ideas', 'covered', 'gaps'] }

const prompt = (i) => `You are testing RECALL (coverage completeness) of an OKF knowledge base built from Cole Medin's YouTube channel. For ONE video, find any DURABLE, link-worthy idea/tool it teaches that is MISSING a page.

STEP 1: Read ${B}/scripts/sample_slugs.txt; your video is the slug on LINE ${i + 1} (1-indexed). Call it SLUG.
STEP 2: Read the transcript ${B}/raw/<SLUG>.md and identify the 4-8 CORE ideas, techniques, and tools/entities the video actually teaches (ignore trivial asides).
STEP 3: For each core idea, check whether the bundle already covers it as a page. Look in:
   - ${B}/concepts/index.md (all concept pages, grouped)
   - ${B}/entities/tools/index.md , ${B}/entities/people/index.md , ${B}/entities/organizations/index.md
   Match by MEANING, not exact string (e.g. "planning before coding" == concepts/planning-with-ai). A page can be named differently than the video's phrasing.
STEP 4: Decide coverage. An idea is a GAP only if BOTH: (a) it is durable/link-worthy (a real concept or a named tool/company that recurs or is central, NOT a one-off remark), AND (b) there is NO existing concept/entity page that reasonably covers it. Do not flag minor mentions, and do not flag ideas that are folded into a broader existing page.

Return via schema: slug, total_core_ideas (how many core ideas you assessed), covered (how many were already covered), and gaps[] (each with the missing idea, kind concept|entity, and one line on why it is durable/link-worthy). If nothing is genuinely missing, return gaps: [].`

phase('Recall')
const results = await parallel(
  Array.from({ length: N }, (_, i) => () =>
    agent(prompt(i), { label: `recall:${i}`, phase: 'Recall', agentType: 'general-purpose', schema })
      .catch(() => null)
  )
)
const rows = results.filter(Boolean)
const allGaps = rows.flatMap((r) => (r.gaps || []).map((g) => ({ ...g, slug: r.slug })))
const totalIdeas = rows.reduce((a, r) => a + (r.total_core_ideas || 0), 0)
const totalCovered = rows.reduce((a, r) => a + (r.covered || 0), 0)
return {
  videos_checked: rows.length,
  total_core_ideas: totalIdeas,
  covered: totalCovered,
  coverage_pct: totalIdeas ? Math.round((100 * totalCovered) / totalIdeas) : 0,
  gap_count: allGaps.length,
  gaps: allGaps,
}
