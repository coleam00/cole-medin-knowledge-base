export const meta = {
  name: 'okf-gap-fill',
  description: 'Write the new concept/entity pages from the add-list, wire links both directions, update taxonomy',
  phases: [
    { title: 'Prep', detail: 'split add_manifest -> per-page specs; return fan-out lists' },
    { title: 'Write', detail: 'write new pages (batched), cited + typed-edge linked' },
    { title: 'Backlink', detail: 'add inbound links from existing related pages so nothing is orphaned' },
  ],
}

const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'
const chunk = (arr, n) => (arr.length ? Array.from({ length: Math.ceil(arr.length / n) }, (_, i) => arr.slice(i * n, i * n + n)) : [])

// ---------------------------------------------------------------- PREP
const prep = await agent(
  `Prepare the gap-fill. Using Python:

1. Read ${B}/scripts/add_manifest.json (new pages to create: concepts[] and entities[]).
2. Read the existing ${B}/scripts/manifest.json and ${B}/scripts/slug_index.json.
3. SAFETY: drop any add_manifest entry whose slug already exists as a file under ${B}/concepts/ or ${B}/entities/**. Report how many were dropped.
4. Write per-page specs to ${B}/scripts/pages/new/<slug>.json (one per NEW page, containing its full add_manifest object PLUS a "video_meta" map of its supporting video slugs -> {title,url} pulled from ${B}/raw/manifest.json).
5. Write an UPDATED ${B}/scripts/slug_index_new.json = the existing slug_index PLUS entries for all new pages (same rel_from_* precomputed-path shape), so writers can link to both old and new pages.

Then RETURN via schema: new_concepts (array of slugs), new_tools, new_people, new_orgs (arrays of slugs), dropped (integer).`,
  { label: 'prep-fill', phase: 'Prep', agentType: 'general-purpose',
    schema: { type: 'object', additionalProperties: true,
      properties: {
        new_concepts: { type: 'array', items: { type: 'string' } },
        new_tools: { type: 'array', items: { type: 'string' } },
        new_people: { type: 'array', items: { type: 'string' } },
        new_orgs: { type: 'array', items: { type: 'string' } },
        dropped: { type: 'integer' },
      }, required: ['new_concepts', 'new_tools', 'new_people', 'new_orgs'] } }
)
const newConcepts = prep.new_concepts || []
const newTools = prep.new_tools || []
const newPeople = prep.new_people || []
const newOrgs = prep.new_orgs || []
const allNew = [...newConcepts, ...newTools, ...newPeople, ...newOrgs]
log(`Filling ${allNew.length} new pages (${newConcepts.length} concepts, ${newTools.length} tools, ${newPeople.length} people, ${newOrgs.length} orgs); dropped ${prep.dropped || 0} collisions`)

const SCHEMA_NOTE = `Follow ${B}/SCHEMA.md EXACTLY (read it first) and match the style of existing pages.
- Frontmatter: type + title + description + tags + videos (the supporting video slugs) + created: 2026-07-21 + updated: 2026-07-21. Entities also: subtype and resource (only if genuinely known).
- Body: open by DEFINING the thing (lead with a verbatim timestamped quote where it sharpens the definition), then typed-edge sections ('## Prerequisites', '## Builds on' / '## Part of', '## Contrasts with', '## Implemented by' / '## Tools' / '## Works with', '## Related'), and a MANDATORY final '## Sources'.
- '## Sources' style EXACTLY: '- [Video Title](<rel>/sources/<slug>.md) - "[H:MM:SS] quote"' using the spec's supporting_videos quotes and video_meta titles. From a concept: ../sources/<slug>.md ; from an entity: ../../sources/<slug>.md.
- LINKS: resolve ONLY via ${B}/scripts/slug_index_new.json rel_from_* fields. Never invent a slug. Every internal link MUST resolve.
- NEVER use em dashes; use ' - '. No curly quotes, no ellipsis characters.
- ~250-550 words, dense and synthesized. Link generously to related existing pages.`

// ---------------------------------------------------------------- WRITE
phase('Write')
const tasks = []
chunk(newConcepts, 5).forEach((part, k) => tasks.push(() => agent(
  `Write NEW OKF CONCEPT pages: ${part.join(', ')}.
For each slug read ${B}/scripts/pages/new/<slug>.json and write ${B}/concepts/<slug>.md.
${SCHEMA_NOTE}
Frontmatter type: concept.
Return: "concepts p${k + 1}: <n> pages".`,
  { label: `new-concepts#${k + 1}`, phase: 'Write', agentType: 'general-purpose' }
)))
chunk(newTools, 5).forEach((part, k) => tasks.push(() => agent(
  `Write NEW OKF ENTITY pages (subtype tool): ${part.join(', ')}.
For each slug read ${B}/scripts/pages/new/<slug>.json and write ${B}/entities/tools/<slug>.md.
${SCHEMA_NOTE}
Frontmatter type: entity, subtype: tool. Use typed sections ('## Realizes', '## Contrasts with', '## Works with', '## Related') with one-line descriptions, matching the other tool pages.
Return: "tools p${k + 1}: <n> pages".`,
  { label: `new-tools#${k + 1}`, phase: 'Write', agentType: 'general-purpose' }
)))
chunk(newPeople, 6).forEach((part, k) => tasks.push(() => agent(
  `Write NEW OKF ENTITY pages (subtype person): ${part.join(', ')}.
For each slug read ${B}/scripts/pages/new/<slug>.json and write ${B}/entities/people/<slug>.md.
${SCHEMA_NOTE}
Frontmatter type: entity, subtype: person.
Return: "people p${k + 1}: <n> pages".`,
  { label: `new-people#${k + 1}`, phase: 'Write', agentType: 'general-purpose' }
)))
chunk(newOrgs, 6).forEach((part, k) => tasks.push(() => agent(
  `Write NEW OKF ENTITY pages (subtype organization): ${part.join(', ')}.
For each slug read ${B}/scripts/pages/new/<slug>.json and write ${B}/entities/organizations/<slug>.md.
${SCHEMA_NOTE}
Frontmatter type: entity, subtype: organization.
Return: "orgs p${k + 1}: <n> pages".`,
  { label: `new-orgs#${k + 1}`, phase: 'Write', agentType: 'general-purpose' }
)))
const writeAcks = await parallel(tasks)
log(`Write done: ${writeAcks.filter(Boolean).length}/${tasks.length} batches`)

// ---------------------------------------------------------------- BACKLINK
phase('Backlink')
const backAcks = await parallel(chunk(allNew, 6).map((part, k) => () => agent(
  `Ensure each NEW page has INBOUND links so it is not an orphan (SCHEMA §5 bidirectionality).
New pages in this batch: ${part.join(', ')}.

For EACH new slug:
1. Determine its path (concepts/<slug>.md, or entities/tools|people|organizations/<slug>.md - check which exists).
2. Read the new page's '## Related'/typed sections to see which EXISTING pages it links OUT to.
3. For 2-4 of those existing target pages, ADD a reciprocal bullet linking BACK to the new page, under the appropriate typed heading (or '## Related' if none fits). Use a correct relative path and append ' - <one-line description>' copied from the new page's frontmatter description.
4. Use the Edit tool; insert the bullet into the existing section (do NOT create duplicate headings, do NOT touch '## Sources' or frontmatter, do NOT duplicate a link that is already there).
- NEVER use em dashes; use ' - '. Every link MUST resolve.

Return: "backlink p${k + 1}: <n> new pages wired".`,
  { label: `backlink#${k + 1}`, phase: 'Backlink', agentType: 'general-purpose' }
)))
log(`Backlink done: ${backAcks.filter(Boolean).length} batches`)

return { newPages: allNew.length, concepts: newConcepts.length, tools: newTools.length, people: newPeople.length, orgs: newOrgs.length, dropped: prep.dropped || 0 }
