export const meta = {
  name: 'okf-qa',
  description: 'Answer real + trap questions by navigating the bundle, then independently judge each answer',
  phases: [
    { title: 'Answer', detail: 'navigate bundle to answer each question, cite pages' },
    { title: 'Judge', detail: 'independently verify answers vs cited pages; catch hallucination' },
  ],
}

const B = (args && args.bundle) || 'C:/Users/colem/OpenSource/cole-medin-knowledge-base'

// expected: "answerable" = should be in the bundle; "trap" = out-of-scope / false premise, correct behavior is to decline.
const QUESTIONS = [
  { id: 'q01', expected: 'answerable', q: 'What are the three stages of the PIV loop?' },
  { id: 'q02', expected: 'answerable', q: 'Why does Cole say the best AI coding tools abandoned RAG for codebases, and what do they use instead?' },
  { id: 'q03', expected: 'answerable', q: 'How is context engineering different from prompt engineering, per Cole?' },
  { id: 'q04', expected: 'answerable', q: 'What is the "AI Layer" and what components make it up?' },
  { id: 'q05', expected: 'answerable', q: 'What are Cole\'s golden rules for agentic coding (e.g. protecting context, git as memory)?' },
  { id: 'q06', expected: 'answerable', q: 'What is Archon and how has its purpose evolved over time?' },
  { id: 'q07', expected: 'answerable', q: 'How does Cole use git worktrees to run coding agents in parallel?' },
  { id: 'q08', expected: 'answerable', q: 'What is the Dark Factory experiment and what is its governance / safety model?' },
  { id: 'q09', expected: 'answerable', q: 'What is the Ralph loop (Ralph Wiggum) technique and what is Cole\'s stance on it?' },
  { id: 'q10', expected: 'answerable', q: 'How does Cole build a second brain with Claude Code and Obsidian?' },
  { id: 'q11', expected: 'answerable', q: 'What is Karpathy\'s LLM wiki and how does Cole apply it to agent memory / knowledge bases?' },
  { id: 'q12', expected: 'answerable', q: 'What problems does Cole identify with MCP servers, and what solution does he propose?' },
  { id: 'q13', expected: 'answerable', q: 'When should you use subagents vs a single agent, and are Claude Code agent teams production-ready per Cole?' },
  { id: 'q14', expected: 'answerable', q: 'What is the adversarial-agents technique and how does it improve reliability?' },
  { id: 'q15', expected: 'answerable', q: 'What is Cole\'s take on building agents with n8n vs Python?' },
  { id: 'q16', expected: 'answerable', q: 'What is agentic RAG with knowledge graphs, from the early n8n-era template?' },
  { id: 'q17', expected: 'answerable', q: 'What does Cole recommend as the simplest RAG stack that actually works?' },
  { id: 'q18', expected: 'answerable', q: 'What is Pydantic AI and why does Cole prefer it for production agents?' },
  { id: 'q19', expected: 'answerable', q: 'What is the difference between semantic, keyword, and hybrid search in Cole\'s RAG content?' },
  { id: 'q20', expected: 'answerable', q: 'What is provider independence and why does Cole care about it (Pi, Archon)?' },
  { id: 'q21', expected: 'answerable', q: 'What did Cole say Claude Code\'s real purpose is, beyond writing code?' },
  { id: 'q22', expected: 'answerable', q: 'How does Cole approach validation in the PIV loop (types, tests, e2e, review)?' },
  { id: 'q23', expected: 'answerable', q: 'What is harness engineering and why does Cole call harnesses the next evolution of AI coding?' },
  { id: 'q24', expected: 'answerable', q: 'What did Cole say about Stripe\'s coding agents shipping ~1300 PRs per week?' },
  { id: 'q25', expected: 'answerable', q: 'What did Cole cover about Google\'s Agents CLI / ADK for shipping agents?' },
  { id: 'q26', expected: 'answerable', q: 'What is context rot and how do you avoid it?' },
  { id: 'q27', expected: 'answerable', q: 'What did Cole say about running AI locally (the local AI package / stack)?' },
  { id: 'q28', expected: 'answerable', q: 'What is the AG-UI protocol and generative UI for agents?' },
  { id: 'q29', expected: 'answerable', q: 'What did Cole cover about DeepSeek R1 for agentic RAG?' },
  { id: 'q30', expected: 'answerable', q: 'What is spec-driven / PRD-first development and two-layer planning?' },
  // traps / out-of-scope / false premise:
  { id: 't01', expected: 'trap', q: 'What did Cole recommend for building AI agents in Rust?' },
  { id: 't02', expected: 'trap', q: 'How does Cole recommend fine-tuning your own LLM from scratch on custom data?' },
  { id: 't03', expected: 'trap', q: 'What is Cole\'s guide to deploying agents on Kubernetes with Helm charts?' },
  { id: 't04', expected: 'trap', q: 'What did Cole say about Claude 5 Opus?' },
  { id: 't05', expected: 'trap', q: 'Which Salesforce integration does Cole recommend for sales agents?' },
  { id: 't06', expected: 'trap', q: 'What did Cole say about the Java Spring AI framework for agents?' },
  { id: 't07', expected: 'trap', q: 'What prompt does Cole recommend for jailbreaking Claude\'s safety filters?' },
  { id: 't08', expected: 'trap', q: 'What did Cole say about GPT-5.3 being AGI?' },
  { id: 't09', expected: 'trap', q: 'Which cryptocurrency token did Cole launch for his community?' },
  { id: 't10', expected: 'trap', q: 'How does Cole use COBOL mainframe modernization with AI agents?' },
]

const answerSchema = { type: 'object', additionalProperties: false,
  properties: {
    verdict: { type: 'string', enum: ['answerable', 'partial', 'gap'] },
    answer: { type: 'string' },
    citations: { type: 'array', items: { type: 'string' } },
    cites_timestamp: { type: 'boolean' },
  }, required: ['verdict', 'answer', 'citations', 'cites_timestamp'] }

const answerPrompt = (Q) => `You are answering a question using ONLY the Cole Medin OKF knowledge base at ${B}. Do NOT use prior knowledge; answer strictly from files inside that bundle.

Question: "${Q.q}"

Navigate like an OKF consumer: read ${B}/index.md, follow relative links into concepts/, entities/, sources/. Open only the pages you need. Then answer.

Return (schema):
- verdict: "answerable" if the bundle fully answers it; "partial" if only partly covered; "gap" if the bundle does NOT cover it (say so honestly rather than guessing).
- answer: <=120 words, grounded ONLY in what the pages say. If gap, briefly state it is not covered.
- citations: the exact relative page paths you used (e.g. "concepts/the-piv-loop.md"). Empty if gap.
- cites_timestamp: true if at least one page you used backs the claim with a timestamped source quote.
CRITICAL: if you cannot find it in the bundle, return verdict "gap". Never invent a page path or a claim.`

phase('Answer')
const answers = await parallel(QUESTIONS.map((Q) => () =>
  agent(answerPrompt(Q), { label: `ans:${Q.id}`, phase: 'Answer', agentType: 'general-purpose', schema: answerSchema })
    .then((a) => ({ Q, a }))
    .catch(() => ({ Q, a: null }))
)).then((rows) => rows.map((r, i) => r || { Q: QUESTIONS[i], a: null }))

const judgeSchema = { type: 'object', additionalProperties: false,
  properties: {
    judge_verdict: { type: 'string', enum: ['correct', 'partial', 'wrong', 'hallucination'] },
    citations_valid: { type: 'boolean' },
    notes: { type: 'string' },
  }, required: ['judge_verdict', 'citations_valid', 'notes'] }

const judgePrompt = (Q, a) => `You are an independent judge verifying an answer produced from the Cole Medin OKF knowledge base at ${B}.

Question: "${Q.q}"
Expected type: ${Q.expected === 'trap' ? 'OUT-OF-SCOPE / false premise — the correct behavior is to say it is NOT covered, with no invented claim' : 'answerable from the bundle'}

The answer under review:
  verdict: ${a ? a.verdict : '(none)'}
  answer: ${a ? JSON.stringify(a.answer) : '(none)'}
  citations: ${a ? JSON.stringify(a.citations) : '[]'}

Verify:
1. Do the cited page paths actually EXIST? Read each cited file under ${B}/ and confirm it exists and actually supports the answer's claims (read the pages).
2. Is the answer factually consistent with those pages (no claims beyond what the pages say)?
3. For an OUT-OF-SCOPE question: did the answer correctly decline (verdict gap / "not covered") WITHOUT inventing a specific claim or citation? If it fabricated a claim or a page, that is a hallucination.

Return (schema):
- judge_verdict: "correct" (answer is right and grounded, OR correctly declined a trap), "partial" (mostly right, minor gaps), "wrong" (missed answerable content or misrepresented pages), "hallucination" (invented a claim, citation, or answered a trap with a fabricated specific claim).
- citations_valid: true if every cited path exists and supports the answer (true also if citations empty for a correctly-declined trap).
- notes: one sentence.`

phase('Judge')
const judged = await parallel(answers.map(({ Q, a }) => () =>
  agent(judgePrompt(Q, a), { label: `judge:${Q.id}`, phase: 'Judge', agentType: 'general-purpose', schema: judgeSchema })
    .then((j) => ({ id: Q.id, expected: Q.expected, verdict: a && a.verdict, judge: j && j.judge_verdict, cit_valid: j && j.citations_valid, notes: j && j.notes }))
))

// aggregate
const rows = judged.filter(Boolean)
const ans = rows.filter((r) => r.expected === 'answerable')
const traps = rows.filter((r) => r.expected === 'trap')
const good = (r) => r.judge === 'correct'
return {
  total: rows.length,
  answerable_correct: ans.filter(good).length + '/' + ans.length,
  traps_correct: traps.filter(good).length + '/' + traps.length,
  hallucinations: rows.filter((r) => r.judge === 'hallucination').map((r) => r.id),
  wrong: rows.filter((r) => r.judge === 'wrong').map((r) => r.id),
  partial: rows.filter((r) => r.judge === 'partial').map((r) => r.id),
  detail: rows.map((r) => ({ id: r.id, exp: r.expected, ans: r.verdict, judge: r.judge, notes: r.notes })),
}
