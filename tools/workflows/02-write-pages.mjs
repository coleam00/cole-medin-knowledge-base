export const meta = {
  name: 'okf-write-pages',
  description: 'Write all source/concept/entity pages against the frozen manifest, cross-linked per SCHEMA',
  phases: [
    { title: 'Prep', detail: 'split manifest -> per-page specs + slug_index' },
    { title: 'Sources', detail: 'one summary page per video (batched)' },
    { title: 'Concepts', detail: 'concept pages, batched by theme' },
    { title: 'Entities', detail: 'tool/person/org pages, batched' },
  ],
}

// args = { bundle: absPath }
const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'

// ---------------------------------------------------------------- PREP
const prep = await agent(
  `Split the frozen manifest into per-page spec files and a compact slug index, using Python, then RETURN the fan-out lists. This makes the page-writing agents cheap (each reads only its own specs + the slug index, never the whole manifest).

Inputs: ${B}/scripts/manifest.json , ${B}/scripts/taxonomy.json
Write:
1. ${B}/scripts/pages/concepts/<slug>.json  — one file per concept (the concept's manifest object).
2. ${B}/scripts/pages/entities/<slug>.json   — one file per entity (include its subtype).
3. ${B}/scripts/pages/sources/<slug>.json     — one file per source video.
4. ${B}/scripts/slug_index.json — compact link-resolution index:
   {
     "concepts": [{"slug":"...","title":"...","rel_from_concept":"./<slug>.md","rel_from_entity":"../../concepts/<slug>.md","rel_from_source":"../concepts/<slug>.md"}],
     "tools":    [{"slug":"...","title":"...","subtype":"tool","rel_from_concept":"../entities/tools/<slug>.md","rel_from_entity_tool":"./<slug>.md"}],
     "people":   [ ... under entities/people/ ... ],
     "orgs":     [ ... under entities/organizations/ ... ],
     "sources":  [{"slug":"...","title":"...","rel_from_concept":"../sources/<slug>.md","rel_from_entity":"../../sources/<slug>.md","rel_from_source":"./<slug>.md"}]
   }
   Precompute the correct RELATIVE path from each page-location so writers never miscompute a link. (Concepts live at concepts/<slug>.md; tools at entities/tools/<slug>.md; people at entities/people/<slug>.md; orgs at entities/organizations/<slug>.md; sources at sources/<slug>.md.)

Then RETURN, in the structured schema: concept_themes (from taxonomy.json concept_themes, as {theme, slugs}), tool_themes (from taxonomy.json tool_themes, as {group, slugs}), source_slugs (every source slug in manifest.json), people_slugs (every entity with subtype person), and org_slugs (every entity with subtype organization).`,
  { label: 'prep-split', phase: 'Prep', agentType: 'general-purpose',
    schema: { type: 'object', additionalProperties: true,
      properties: {
        concept_themes: { type: 'array', items: { type: 'object', additionalProperties: false,
          properties: { theme: { type: 'string' }, slugs: { type: 'array', items: { type: 'string' } } },
          required: ['theme', 'slugs'] } },
        tool_themes: { type: 'array', items: { type: 'object', additionalProperties: false,
          properties: { group: { type: 'string' }, slugs: { type: 'array', items: { type: 'string' } } },
          required: ['group', 'slugs'] } },
        source_slugs: { type: 'array', items: { type: 'string' } },
        people_slugs: { type: 'array', items: { type: 'string' } },
        org_slugs: { type: 'array', items: { type: 'string' } },
      },
      required: ['concept_themes', 'tool_themes', 'source_slugs', 'people_slugs', 'org_slugs'] } }
)
const conceptThemes = (prep.concept_themes || []).map((t) => [t.theme, t.slugs])
const toolThemes = (prep.tool_themes || []).map((t) => [t.group, t.slugs])
const sourceSlugs = prep.source_slugs || []
const peopleSlugs = prep.people_slugs || []
const orgSlugs = prep.org_slugs || []
log(`Writing: ${conceptThemes.length} concept themes, ${toolThemes.length} tool groups, ${sourceSlugs.length} sources`)

const SCHEMA_NOTE = `Follow the bundle's SCHEMA.md EXACTLY. Read ${B}/SCHEMA.md and ${B}/scripts/slug_index.json first. Hard rules:
- Frontmatter: type + title + description + tags + videos (source slugs) + created: 2026-07-21 + updated: 2026-07-21. Entities also: subtype and (if known) resource.
- Body: an opening paragraph that DEFINES the thing (lead with a verbatim timestamped quote where it sharpens the definition), then typed-edge sections using ONLY these headings when relevant: '## Prerequisites', '## Builds on' / '## Part of', '## Contrasts with', '## Implemented by' / '## Tools', '## Related', and a MANDATORY final '## Sources'.
- '## Sources' lists each source video page with a relative link and, for the important ones, a verbatim timestamped quote in this exact style: '- [Video Title](../sources/<slug>.md) — "[H:MM:SS] quote text"'. Use the quotes from the page spec.
- LINKS: use ONLY relative paths from slug_index.json (the precomputed rel_from_* fields). Never invent a slug or link to a page not in slug_index.json. Every internal link MUST resolve.
- Bidirectional intent: link generously to related concepts/entities that exist in slug_index.json.
- NEVER use em dashes (—) as sentence punctuation in prose; use commas/periods/hyphens. (The quote-citation style above with ' — ' before a quote is the ONE allowed exception, matching the existing bundle.)
- Synthesis, not transcript dump. ~250-600 words of dense, correct prose per page. If sources conflict, add '> **Contradiction:**' citing both.`

// ---------------------------------------------------------------- SOURCES
phase('Sources')
const chunk = (arr, n) => arr.length ? Array.from({length: Math.ceil(arr.length/n)}, (_,i)=>arr.slice(i*n,i*n+n)) : []
const sourceBatches = chunk(sourceSlugs, 10)
const srcAcks = await parallel(sourceBatches.map((batch, bi) => () =>
  agent(
    `Write the OKF SOURCE page for each of these videos: ${batch.join(', ')}.
For each slug, read ${B}/scripts/pages/sources/<slug>.json (thesis, summary, key_moments, url, published, duration, recency_rank, concepts[], entities[]) and write ${B}/sources/<slug>.md.

${SCHEMA_NOTE}

SOURCE page shape specifically:
- Frontmatter: type: source, title, description (the thesis), youtube_id, url, slug, published, duration, recency_rank, raw: "../raw/<slug>.md", tags, created, updated.
- Body: the 2-3 paragraph synthesized summary. Then '## Concepts covered' (relative links to concepts[] via slug_index rel_from_source), '## Entities' (links to entities[]), '## Key moments' (the timestamped key_moments as '- **[H:MM:SS]** note'), and '## Transcript' with a single link '[Raw transcript](../raw/<slug>.md)'.
- The youtube_id/url/published/duration come from the spec; recency_rank too.
Return a tiny ack: "sources batch ${bi}: <n> pages".`,
    { label: `sources:${bi}`, phase: 'Sources', agentType: 'general-purpose' }
  )
))
log(`Sources done: ${srcAcks.filter(Boolean).length}/${sourceBatches.length} batches`)

// ---------------------------------------------------------------- CONCEPTS (by theme, sub-batched)
phase('Concepts')
const conceptBatches = []
for (const [theme, slugs] of conceptThemes) {
  const parts = chunk(slugs, 7)
  parts.forEach((part, k) => conceptBatches.push({ theme, part, k, kn: parts.length, siblings: slugs }))
}
const conAcks = await parallel(conceptBatches.map((batch) => () =>
  agent(
    `Write the OKF CONCEPT page for each concept in this batch (theme "${batch.theme}"${batch.kn > 1 ? `, part ${batch.k + 1}/${batch.kn}` : ''}): ${batch.part.join(', ')}.
For each slug, read ${B}/scripts/pages/concepts/<slug>.json (title, description, tags, related[], videos[] with per-video timestamped quotes) and write ${B}/concepts/<slug>.md.

${SCHEMA_NOTE}

CONCEPT page shape: frontmatter type: concept (title, description, tags, videos = the source slugs from the spec, created/updated). Body: open by DEFINING the concept (lead with a verbatim timestamped quote where it sharpens the definition), explain how it works / why it matters, then typed-edge sections linking to related concepts and to the entities that implement it (use '## Implemented by' / '## Tools' for entity links), and the mandatory '## Sources'. Use the spec's related[] to drive '## Related' / '## Builds on' / '## Prerequisites' / '## Contrasts with' (pick the heading by meaning). These concepts share the theme "${batch.theme}" (full set: ${batch.siblings.join(', ')}) — cross-link them where related.
Return a tiny ack: "concepts ${batch.theme} p${batch.k + 1}: <n> pages".`,
    { label: `concepts:${batch.theme}#${batch.k + 1}`, phase: 'Concepts', agentType: 'general-purpose' }
  )
))
log(`Concepts done: ${conAcks.filter(Boolean).length}/${conceptBatches.length} batches`)

// ---------------------------------------------------------------- ENTITIES
phase('Entities')
const entityTasks = []
for (const [group, slugs] of toolThemes) {
  const parts = chunk(slugs, 8)
  parts.forEach((part, k) => entityTasks.push(() => agent(
    `Write the OKF ENTITY page (subtype tool) for each tool in the group "${group}"${parts.length > 1 ? `, part ${k + 1}/${parts.length}` : ''}: ${part.join(', ')}.
For each slug read ${B}/scripts/pages/entities/<slug>.json and write ${B}/entities/tools/<slug>.md.
${SCHEMA_NOTE}
ENTITY page shape: frontmatter type: entity, subtype: tool, plus resource if known (a real homepage/repo URL; omit if unsure rather than guessing). Body: what it is, how Cole uses it / why it matters across the videos, then '## Related' linking the concepts it realizes and sibling tools, and the mandatory '## Sources'. Resolve links via slug_index rel_from_entity fields (tools link to concepts via '../../concepts/<slug>.md').
Return: "tools ${group} p${k + 1}: <n> pages".`,
    { label: `tools:${group}#${k + 1}`, phase: 'Entities', agentType: 'general-purpose' }
  )))
}
chunk(peopleSlugs, 8).forEach((part, k) => entityTasks.push(() => agent(
  `Write the OKF ENTITY page (subtype person) for each of these people: ${part.join(', ')}.
For each slug read ${B}/scripts/pages/entities/<slug>.json and write ${B}/entities/people/<slug>.md.
${SCHEMA_NOTE}
Frontmatter type: entity, subtype: person, resource (homepage/X/GitHub if genuinely known, else omit). Body: who they are, their relevance across the videos, '## Related' (tools/concepts they connect to, via ../../concepts/ and ../tools/ paths from slug_index), mandatory '## Sources'.
Return: "people p${k + 1}: <n> pages".`,
  { label: `people#${k + 1}`, phase: 'Entities', agentType: 'general-purpose' }
)))
chunk(orgSlugs, 8).forEach((part, k) => entityTasks.push(() => agent(
  `Write the OKF ENTITY page (subtype organization) for each of these orgs: ${part.join(', ')}.
For each slug read ${B}/scripts/pages/entities/<slug>.json and write ${B}/entities/organizations/<slug>.md.
${SCHEMA_NOTE}
Frontmatter type: entity, subtype: organization, resource (homepage if genuinely known, else omit). Body: what the org is, its role across the videos, '## Related', mandatory '## Sources'.
Return: "orgs p${k + 1}: <n> pages".`,
  { label: `orgs#${k + 1}`, phase: 'Entities', agentType: 'general-purpose' }
)))
const entAcks = await parallel(entityTasks)
log(`Entities done: ${entAcks.filter(Boolean).length}/${entityTasks.length} batches`)

return { prep, sources: srcAcks.filter(Boolean).length, conceptThemes: conceptThemes.length, entityBatches: entityTasks.length }
