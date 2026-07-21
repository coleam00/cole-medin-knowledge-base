# Concepts

Ideas, techniques, patterns, and mental models mined from the videos. Grouped by theme.

## AI agent fundamentals
- [The Core Components of an Agent](agent-core-components.md) - Every AI agent reduces to four parts: the LLM (brain), tools (actions), the system prompt (instructions), and memory (context).
- [Agent Development Lifecycle](agent-development-lifecycle.md) - A repeatable blueprint for taking an agent from planning and a minimal proof-of-concept through database, code, UI, testing, deployment, and evaluation.
- [The Agent Loop (Reason-Act-Observe)](agent-loop.md) - The core agentic cycle where the LLM reasons, calls a tool, observes the result, and loops an unknown number of times until it decides to respond.
- [Agents vs. Workflows](agents-vs-workflows.md) - An agent lets the LLM non-deterministically control which tools run and how often to reach a goal, whereas a workflow chains a fixed sequence of steps.
- [Computer Use](computer-use.md) - Giving an agent control of a computer (mouse, keyboard, screen) so it can operate real software the way a person would.
- [SDK vs. Framework Decision](sdk-vs-framework-decision.md) - Choosing between a batteries-included coding-agent SDK and a from-scratch agent framework based on who uses the agent and tolerance for speed, cost, and determinism.
- [Structured Outputs](structured-outputs.md) - Constraining LLM output to a validated schema (with retries on failure) so downstream code can rely on its shape.
- [Tool Design](tool-design.md) - Designing agent tools to be few, single-purpose, and well-described (often via docstrings) so the model uses them reliably.
- [Tool Calling](tool-use.md) - Letting an LLM invoke external functions and APIs so it can take actions and fetch data beyond its parametric knowledge.
- [What Is an AI Agent](what-is-an-ai-agent.md) - An AI agent is a large language model given tools to interact with the outside world and take actions, making it far more capable than the LLM alone.

## Agent architecture & multi-agent systems
- [Agent Architecture Patterns](agent-architecture-patterns.md) - Reusable agent design patterns like prompt chaining, routing, parallelization, orchestrator-workers, and evaluator loops for structuring agentic systems.
- [Agent Dependency Injection](agent-dependencies.md) - Passing runtime dependencies (clients, config, connections) into an agent and its tools via dependency injection (as in Pydantic AI) for cleaner, testable, decoupled agent code.
- [Agent Graphs](agent-graphs.md) - Modeling agents as stateful graphs of nodes and conditional edges with persisted checkpoints, as in LangGraph.
- [Agent Teams](agent-teams.md) - Coordinating multiple specialized agents, via orchestrators, routers, and handoffs, to solve a task no single agent handles well.
- [Graph-Based Agent Workflows](langgraph-nodes-edges-state.md) - Model an agent as a directed graph of nodes, edges, and shared state (LangGraph) with routing between steps, giving explicit control over branching, loops, and serving of complex agent workflows.
- [Local LLMs as Agents](local-llms-as-agents.md) - Using openly downloadable, self-hosted models for agentic work, which hinges on the model's ability to do reliable function calling.
- [Multi-Model Agents](multi-model-agent.md) - Running an agent across more than one LLM, or combining several models together, to leverage each model's distinct strengths at runtime.
- [Multi-Tenant Agents](multi-tenant-agents.md) - Building a single agent that serves many users, each with personalized tools, memory, and securely authorized access to their own accounts.
- [Parallel Agent Execution](parallel-agent-execution.md) - Running multiple agents (or agent steps) concurrently to cut wall-clock time on a task.
- [Production-Grade Agents](production-grade-agents.md) - Real agents need validation, error handling, testing, logging, observability, and monitoring rather than just an LLM plus tools stitched together.
- [Production vs. Personal Agents](production-vs-personal-agents.md) - The architectural divide between quick personal-use agents and systems built to scale in production, and what has to change (structure, storage, reliability) to cross that line.
- [Single vs. Multi-Agent Architecture](single-vs-multi-agent.md) - The core architectural decision between one capable agent and a coordinated system of specialized agents with handoffs, and when the added complexity of multi-agent orchestration is actually worth it.
- [Subagents Pattern](subagents-pattern.md) - Delegating scoped tasks to isolated subagents to parallelize work and protect the main agent's context window.

## Agent reliability, safety & evaluation
- [Adversarial Agents](adversarial-agents.md) - Pitting a generator against an adversarial critic so an agent's output is stress-tested before it's accepted.
- [Agent Evaluation](agent-evaluation.md) - Systematically scoring agent behavior with evals and benchmarks, including as a gate before deployment.
- [Agent Observability](agent-observability.md) - Instrumenting agents with tracing, logging, and cost/token metrics so you can see and debug what they actually did.
- [Agent Security](agent-security.md) - Sandboxing agents, scoping permissions, and keeping secrets out of the model to limit blast radius and prevent abuse.
- [Guardrails](guardrails.md) - Constraints and checks that keep agents from hallucinating, going off the rails, or emitting unsafe output.
- [Human in the Loop](human-in-the-loop.md) - Keeping a human as the approver and steerer of agentic work rather than fully automating, so AI augments engineers instead of replacing them.
- [The Lethal Trifecta](lethal-trifecta.md) - The dangerous combination of private data access, untrusted content, and external communication that enables prompt-injection exfiltration.
- [Self-Correcting Agents](self-correction.md) - Feeding tool errors and results back to the model so it can reason about mistakes, avoid repeating calls, and retry until it gets the action right.
- [Sycophancy](sycophancy.md) - LLMs' tendency to agree with and flatter the user, which can mask real problems in their output.

## Context engineering
- [Context Engineering](context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Context Isolation](context-isolation.md) - Giving each agent or subagent its own clean context window so unrelated tokens never dilute the task at hand.
- [Context Reset](context-reset.md) - Clearing or compacting an agent's context window between phases of work to avoid context rot and keep reasoning sharp.
- [Context Rot](context-rot.md) - The degradation of an agent's output quality as its context window fills with stale, irrelevant, or accumulated information over a long session.
- [Context Window Limits](context-window-limits.md) - Managing finite context by summarizing, compacting, and sizing what you load so the model stays sharp on long tasks.
- [Docs and Templates as Coding-Assistant Context](docs-as-agent-context.md) - Feeding llms.txt docs and proven reference templates to an AI coding assistant so it builds from real context instead of hallucinating.
- [Global Rules](global-rules.md) - Persistent project- or user-level rule files that inject standing context and conventions into every agent run.
- [Intent Engineering](intent-engineering.md) - Shifting the engineer's job from writing code to precisely expressing intent that an AI agent implements.
- [Prime Command](prime-command.md) - A reusable slash command that primes an agent with focused codebase understanding at the start of a session.
- [Progressive Disclosure](progressive-disclosure.md) - Loading context, skills, and tools on demand only when a task needs them instead of front-loading everything into the context window.
- [PRP Framework](prp-framework.md) - The Product Requirements Prompt pattern: a structured, context-rich prompt blueprint that hands an agent everything it needs to one-pass a feature.
- [Stacking Context-Engineering Strategies](strategy-stacking.md) - Composing complementary methods (e.g. BMAD for planning, PRP for execution) rather than replacing one with another.
- [The WHISK Framework](the-whisk-framework.md) - Cole's mnemonic framework for structuring the context you feed an agent to reliably build anything with it.

## Prompt engineering
- [Agent Prompting Techniques](agent-prompting.md) - Prompt-level techniques that shape agent behavior: a system/goal/do/don't template, dynamic runtime injection, internal thought messages, current-date grounding, and intent inference.
- [Prompting Techniques for AI Coding](ai-coding-prompting.md) - Structuring build prompts: precise on functionality, general on UI, a catch-all requirements section, and image-to-code inputs.
- [Avoid Negative Instructions](avoid-negative-instructions.md) - Tell the model what to do rather than what not to do, since positive, concrete instructions are far more reliable than prohibitions.
- [Chain-of-Thought Prompting](chain-of-thought.md) - Prompting the model to reason step by step before answering, optionally sampling multiple reasoning paths and taking the most consistent answer (self-consistency) to improve reliability.
- [Docstrings as Tool Descriptions](docstrings-as-tool-descriptions.md) - Writing clear function docstrings that double as the tool descriptions an agent reads, so the LLM knows exactly when and how to call each tool.
- [Effective Prompting](effective-prompting.md) - Keeping prompts simple, specific, and high-quality, and knowing when prompt tricks matter versus when they're overrated.
- [Few-Shot Prompting](few-shot-prompting.md) - Including a handful of concrete input/output examples in the prompt so the model infers the desired pattern instead of relying on instructions alone.
- [Prompt Engineering](prompt-engineering.md) - The craft of wording, structuring, and constraining a prompt so an LLM reliably produces the answer you want, one piece of the larger context-engineering picture that Cole considers mostly over-hyped with only a small transferable core worth learning.
- [Prompt Versioning](prompt-versioning.md) - Treating prompts as versioned artifacts so changes can be tracked, compared, and rolled back as the agent evolves.
- [Reduce Assumptions](reduce-assumptions.md) - Write explicit, unambiguous, non-contradictory prompts so the LLM has to guess as little as possible, which is the single biggest driver of accurate and predictable output.
- [Role Prompting](role-prompting.md) - Assigning the model a specific role or persona (e.g. 'an expert at growing Twitter accounts') to set the tone and expectations for its response, which Cole calls the overarching concept behind all prompt engineering.
- [Self-Criticism Prompting](self-criticism-prompting.md) - Having the model critique and revise its own output in the prompt loop so it catches errors and improves the answer before returning it.
- [System Prompt Engineering](system-prompt-engineering.md) - Crafting an agent's system prompt (persona, rules, output shape, routing logic, reusable templates) to steer its behavior consistently across turns.

## RAG & retrieval
- [Agentic RAG](agentic-rag.md) - Giving an agent retrieval as a tool so it decides when and how to search a knowledge base, picking strategies and issuing follow-up queries instead of a single static lookup.
- [Agentic Search](agentic-search.md) - An agent answering a question by reasoning across multiple search tools and full-document fallbacks instead of relying on a single retrieval call.
- [Contextual Retrieval](contextual-retrieval.md) - Prepending LLM-generated context to each chunk before embedding so retrieval understands where the chunk sits in the larger document.
- [Hierarchical RAG](hierarchical-rag.md) - A multi-level retrieval scheme that first narrows to the right documents or sections, then retrieves fine-grained chunks within them.
- [Hybrid Search](hybrid-search.md) - Combining keyword (BM25) and semantic vector search so retrieval catches both exact-term and meaning-based matches.
- [Keyword Search](keyword-search.md) - Exact-term (lexical) search that complements semantic search, especially for identifiers and rare tokens.
- [Multi-Query RAG](multi-query-rag.md) - Issuing several reformulated queries for a single question and merging their results to get broader, more complete retrieval coverage.
- [Query Expansion](query-expansion.md) - Rewriting or enriching a user's query with an LLM before retrieval to improve recall and match how source documents are phrased.
- [Retrieval-Augmented Generation (RAG)](rag.md) - Grounding an LLM's answers by retrieving relevant documents from an external knowledge base and injecting them into the prompt at query time.
- [Reciprocal Rank Fusion](reciprocal-rank-fusion.md) - A ranking method that merges results from multiple retrievers (e.g. keyword + semantic) into one fused ordering.
- [Reranking](reranking.md) - Applying a second, more precise model to reorder an initial candidate set so the most relevant chunks land at the top of the context.
- [Self-Reflective RAG](self-reflective-rag.md) - A RAG pattern where the agent evaluates its own retrieved context and re-queries or researches further until it has what it needs to answer well.
- [Semantic Search](semantic-search.md) - Retrieving content by embedding-based similarity so results match on meaning rather than exact keywords.
- [Traditional RAG](traditional-rag.md) - The classic one-shot, static RAG pipeline that embeds a query, runs a single vector similarity search, and stuffs the top chunks into the prompt.
- [When RAG Is (and Isn't) Dead](when-rag-is-dead.md) - The argument that for code, agents navigating files directly often beats indexed RAG, and when traditional retrieval still earns its place.

## Chunking, embeddings & data
- [Chunking](chunking.md) - Splitting source documents into appropriately sized, embeddable segments, the foundational preprocessing step that determines RAG retrieval quality.
- [Context-Aware Chunking](context-aware-chunking.md) - Splitting documents along semantic boundaries and enriching chunks with surrounding context to improve retrieval quality.
- [Fine-Tuned Embeddings](fine-tuned-embeddings.md) - Training embedding models on domain data so semantic search retrieves the right chunks for a specific corpus.
- [Late Chunking](late-chunking.md) - Embedding a full document first and only then splitting it, so each chunk carries whole-document context.
- [Structured vs Unstructured Data](structured-vs-unstructured-data.md) - Choosing the right representation for RAG, keeping tabular data queryable as SQL while formatting prose as markdown, rather than forcing everything through vector search.
- [Vector Embeddings](vector-embeddings.md) - Numeric representations of text that enable semantic similarity search, stored and managed in a vector database for retrieval.

## Knowledge bases & memory
- [Git as Long-Term Memory](git-as-long-term-memory.md) - Treating the git history and versioned files as durable, inspectable memory for agents instead of opaque model state.
- [Heartbeat](heartbeat.md) - A scheduled proactive loop that lets an AI system check in and act on its own without being prompted.
- [Knowledge Bases](knowledge-bases.md) - Curated bodies of knowledge an agent can retrieve from, distinct from raw model weights, that ground responses in trusted source material.
- [Knowledge Graphs](knowledge-graphs.md) - Structuring knowledge as entities and relationships (often temporal) so agents can traverse connections a vector store can't express.
- [Memory Systems](memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Second Brain](second-brain.md) - A personal, always-on AI system that captures, recalls, and acts on your knowledge and daily context.
- [Self-Evolving Memory](self-evolving-memory.md) - A memory system that reflects on and rewrites its own notes over time, promoting and pruning what it stores.
- [The LLM Wiki](the-llm-wiki.md) - An LLM-maintained knowledge base of plain markdown pages that compiles sources into a navigable, self-referential wiki.
- [Web Crawling & Ingestion](web-crawling.md) - Crawling sites and documentation (sitemaps, recursion, parallelism) and converting them to clean markdown for a knowledge base.

## Agentic coding workflow
- [Agentic Coding](agentic-coding.md) - Letting an AI agent drive software development end-to-end, from planning through implementation and validation, with human steering.
- [Agentic Workflow Engineering](agentic-workflow-engineering.md) - Designing repeatable AI workflows as engineered systems with defined steps, orchestration, and background execution rather than ad-hoc prompting.
- [Clarifying Questions](clarifying-questions.md) - Having the agent ask targeted questions up front to infer intent and reduce assumptions before it plans or builds.
- [Contract-First Development](contract-first.md) - Define the shared interface or data contract between an agent's frontend, backend, and collaborating agents before building either side, so components can be developed independently and wired together reliably.
- [Reverting and Forking Conversations](conversation-checkpointing.md) - Rolling a coding session back to an earlier message or forking from it to undo bad AI changes and explore alternatives.
- [Deterministic Workflows](deterministic-workflows.md) - Encoding known steps as fixed code paths and reserving the LLM for the genuinely fuzzy decisions, trading autonomy for reliability.
- [The Issue Is the Spec](issue-is-the-spec.md) - Treating a well-written ticket or issue as the complete specification the agent implements against.
- [Iterative Prompting](iterative-prompting.md) - Build complex software by prompting for a minimal baseline first and adding one change at a time to minimize hallucination.
- [One Feature Per Prompt](one-feature-per-prompt.md) - Scoping each AI coding prompt to a single feature so the model stays focused and produces smaller, reviewable, higher-quality changes.
- [Phases of Work](phases-of-work.md) - Breaking a build into ordered phases so the agent completes and validates one coherent chunk before starting the next.
- [Planning with AI](planning-with-ai.md) - Using the AI to produce a detailed plan before implementation so execution follows a reviewed blueprint instead of improvising.
- [PRD-First Development](prd-first-development.md) - Starting every build from a written product requirements document that becomes the contract the agent implements against.
- [Prototype as a Coding Blueprint](prototype-as-blueprint.md) - Using a finished no-code workflow as a visual reference (exportable as JSON) that directly guides the coding phase.
- [Spec-Driven Development](spec-driven-development.md) - Anchoring the build to an explicit written spec that the agent implements and validates against.
- [The PIV Loop](the-piv-loop.md) - Cole's core agentic-coding cycle of Plan, Implement, Validate that structures every unit of AI-driven work.
- [The Ralph Loop](the-ralph-loop.md) - Re-running an agent against the same prompt/state in a tight loop, letting each pass fix errors and compound reliability.
- [Two-Layer Planning](two-layer-planning.md) - Separating high-level strategic planning from detailed task planning, using a stronger model for the former.
- [Vibe Coding](vibe-coding.md) - Building software by conversationally prompting an AI without closely reading the code, useful for prototypes but risky for production.

## AI coding landscape & tooling
- [AI Coding Assistant](ai-coding-assistant.md) - A tool that generates or completes code from short prompts, applying targeted edits and offloading low-leverage software work.
- [AI Coding Harness](ai-coding-harness.md) - The surrounding scaffolding (prompts, tools, rules, validation) that turns a raw model into a reliable coding system.
- [Limitations of AI Coding Models](ai-coding-limitations.md) - General coding models stay too general and hallucinate, and silently generate stale library code because of the training cutoff.
- [Everyday AI Coding Use Cases](ai-coding-use-cases.md) - Delegating tedious, low-satisfaction dev work - debugging, documentation, tests, and infra config - to an AI assistant.
- [AI Coding Assistant UX Patterns](ai-coding-ux.md) - Interaction patterns of coding assistants: streamed code output, inline vs manual suggestions, and schema inference from a name.
- [Browser-Based AI Coding Tools](browser-based-ai-coding.md) - In-browser coding tools that import git repos and local projects to get you started fast, but stall on directed refinement vs AI IDEs.
- [Code Execution](code-execution.md) - Giving agents a sandbox to write and run code as a general-purpose tool rather than exposing many narrow tools.
- [Codebase Indexing](codebase-indexing.md) - Building a searchable index or map of a codebase so the agent can retrieve the right files instead of scanning everything.
- [Real-World Coding Benchmarks](coding-benchmarks.md) - Evaluating coding models on real engineering tasks, and the gap between exploding benchmark scores and flat developer productivity.
- [Language Server Protocol](language-server-protocol.md) - Using LSP to give agents precise code navigation (definitions, references, symbols) instead of guessing from text.
- [Open-Source & Local AI Coding](open-source-ai-coding.md) - Community-maintained, self-hostable AI coding tools and local models that dodge API costs and rate limits.
- [Parallel Agentic Coding](parallel-agentic-coding.md) - Dispatching agents to background tasks in isolated git worktrees, each fed repo context and returning a reviewable PR.
- [Prompt Caching](prompt-caching.md) - Caching repeated portions of prompts to cut cost and latency across an AI coding session.
- [The Evolution of AI Coding](the-evolution-of-ai-coding.md) - How AI coding assistants moved from novelty to daily driver, and where the landscape, adoption, and commentary are heading.

## Commands, skills & self-evolving systems
- [Abstraction Distraction](abstraction-distraction.md) - The trap of reaching for heavy frameworks and abstractions that get in the way instead of writing simple, direct code.
- [Capabilities Over Tools](capabilities-over-tools.md) - Framing skills as composable capabilities the model can combine, rather than a flat list of rigid tools.
- [Claude Code Hooks](claude-code-hooks.md) - Lifecycle hooks that run deterministic code at defined points in a Claude Code session to enforce behavior the model can't be trusted to.
- [Commandify Everything](commandify-everything.md) - Turning repeated agent workflows into reusable slash commands so complex processes run with a single invocation.
- [Community-Driven Development](community-driven-development.md) - Building products and open source in public with a community, using a public roadmap and shared learning.
- [Dark Factory](dark-factory.md) - A self-evolving codebase where autonomous workflows build and improve a product with minimal human touch.
- [Learn by Building](learn-by-building.md) - Learning AI engineering by building real projects, forking open source, and rebuilding from docs rather than passive study.
- [Provider Independence](provider-independence.md) - Architecting agents so the underlying model, framework, or client can be swapped without a rewrite, avoiding lock-in through low-level abstractions.
- [Rapid Prototyping](rapid-prototyping.md) - Building a fast proof of concept with managed services first, then hardening only what proves out, instead of over-engineering up front.
- [Skills](skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.
- [Slash Commands](slash-commands.md) - User-defined command files that package a prompt and arguments into a callable shortcut inside the coding agent.
- [System Evolution](system-evolution.md) - Building systems that improve themselves over time, including agents that generate and refine other agents.
- [The AI Layer](the-ai-layer.md) - The layer of rules, commands, skills, and context you own on top of a codebase that makes AI coding effective and portable.

## Validation & code review
- [Code Review](code-review.md) - Using AI to review diffs for bugs and quality as a gate before merging, ideally with a reviewer separate from the author.
- [End-to-End Validation](end-to-end-validation.md) - Validating the whole system through its real interface (not just unit-level checks) so the agent proves the feature actually works.
- [Separate Reviewer](separate-reviewer.md) - Splitting authoring and grading across different agents so the reviewer isn't biased by having written the code.
- [Test-Driven Development](test-driven-development.md) - Writing tests first so the agent has an objective target and a validation signal to code against.
- [Validation](validation.md) - Building explicit checks into agentic workflows so the AI verifies its own output against real success criteria before moving on.

## MCP & agent protocols
- [Agent Client Protocol (ACP)](agent-client-protocol.md) - An open standard for connecting any coding agent to any code editor, the agent-to-editor analog of MCP.
- [Agent Protocols](agent-protocols.md) - Emerging standards (A2A, agent cards, discovery) that let agents interoperate and be called across clients.
- [Build Your Own MCP Server](build-your-own-mcp-server.md) - Standing up custom MCP servers (often with LLM help) to expose tools to any client over a standard transport.
- [Model Context Protocol (MCP)](mcp.md) - An open protocol for packaging tools, data, and RAG capabilities as servers that any AI coding assistant or agent can connect to and call with a standard interface.
- [MCP Server & Client Architecture](mcp-architecture.md) - The structural foundations of the Model Context Protocol: how servers expose tools to clients, server lifespan and state management, containerized one-click installs, aggregating many servers, and registering tools dynamically.
- [The Problems With MCP Servers](mcp-problems.md) - MCP's practical failure modes, tool overload and context/token bloat that overwhelm LLMs, JSON setup friction, and early production gaps like missing built-in auth and security.
- [MCP with Custom Agents](mcp-with-custom-agents.md) - Integrating MCP servers directly into agents you build yourself, so you control the front end, tool selection, and how the tools are used.
- [Tool Standardization (USB-C for AI)](tool-standardization.md) - MCP standardizes how tools are exposed to LLMs, like a USB-C port for AI, so the same tools can be reused identically across any agent framework or host instead of hand-coding every capability.

## Deployment & production APIs
- [Agent as an API Endpoint](agent-as-api-endpoint.md) - Wrapping an AI agent in a web API (typically FastAPI) turns it from a terminal-bound script into a deployable, scalable service any frontend, SaaS, or client can call remotely.
- [Agent Deployment](agent-deployment.md) - Getting agents to production, containerizing, networking, reverse-proxying, and choosing a provider-agnostic, cost-predictable host.
- [Securing Agent APIs](api-security.md) - Protecting agent endpoints and secrets: bearer-token header auth stops strangers from calling a public agent webhook and draining LLM credits, while a small backend proxy holds the secret API key so a browser client never has to.
- [Containerization & Docker Networking](containerization.md) - Running each service and your own agent as Docker containers in one stack so they communicate over a private network by service name, and exposing a tool as a Dockerized HTTP API when it can't be installed natively.
- [Custom Domain via DNS A Record](custom-domain-dns.md) - Pointing a subdomain at your server's IP by adding an A record at your DNS provider so users reach the app by name instead of a raw IP address.
- [Embeddable Agent Widget](embeddable-agent-widget.md) - Deploying an agent onto any website with a single script tag - as a floating chat bubble, inline element, iframe, or full-screen page - independent of the site builder.
- [Extending a Platform via API + Marketplace](extend-the-platform.md) - A strong developer-first API plus an app marketplace (webhooks, auth, permissions) creates a profitable niche: extend an existing SaaS platform's functionality with AI instead of building from scratch.
- [Extensible Plugin Architecture](extension-marketplace.md) - Designing an AI coding assistant around an extension/marketplace model so third-party plugins can expand its capabilities without forking the core (e.g. oTToDev/bolt.diy).
- [Firewall Configuration](firewall-configuration.md) - Enabling the server firewall (UFW) and opening the necessary ports - HTTP/HTTPS (80/443) or the app's port - so external machines can reach the deployed app before proxy and SSL setup can succeed.
- [Frontend-Agnostic Agents](frontend-agnostic-agent.md) - Decouple the agent backend from any specific UI by emitting standardized events and subscribing to real-time messages (AG-UI, agentic experiences), so the same agent can power any frontend.
- [Full-Stack AI Application](full-stack-ai-application.md) - Combining an AI agent with a real front end, database, and API integrations, with the agent acting as the brain connecting the UI to back-end services.
- [HTTP Request Extensibility](http-request-extensibility.md) - An HTTP request block lets a no-code workflow call any external API mid-conversation (with custom headers, body, and keys), an escape hatch to hook into custom agents hosted elsewhere without losing the platform's convenience.
- [Machines Paying Machines](machines-paying-machines.md) - The near-future pattern where autonomous agents transact and pay each other for services with little human involvement.
- [Agent Request/Response Schema](request-response-schema.md) - Standardizing how any agent plugs in by fixing a strict input payload (query, user_id, request_id, session_id) and a minimal output (a success boolean), so agents become interchangeable behind a common contract.
- [Reverse Proxy](reverse-proxy.md) - A server (Nginx or Caddy) that receives requests at a public URL and routes them behind the scenes to internal services by port or subdomain, keeping backend services private and centralizing HTTPS.
- [HTTPS via Certbot / Let's Encrypt](ssl-tls.md) - Using Certbot to obtain and install a free Let's Encrypt SSL certificate so the deployed site is served securely over HTTPS.
- [Webhook-Driven Agents](webhook-driven-agent.md) - Triggering agents from external events via webhooks so they run reactively as part of automated workflows rather than only through direct chat.
- [Webhook Tool Pattern](webhook-tool-pattern.md) - Exposing and wiring no-code agents through webhooks: an n8n workflow starts with a webhook trigger and ends with respond-to-webhook, gets a public URL any frontend can call, and a reusable Python wrapper makes adding new webhook-backed tools nearly free.

## Agent UX & interfaces
- [Agentic Experiences](agentic-experiences.md) - Building apps where the agent drives a live, generative UI and front-end/back-end state stay in sync, instead of a static chat box.
- [Chat Interfaces](chat-interfaces.md) - Wrapping agents in chat surfaces (websites, DMs, platforms) with adapters, a shared message format, and durable history.
- [Generative UI](generative-ui.md) - Interfaces the agent generates or drives at runtime, streaming tool activity and reasoning into a live, stateful UI.
- [Streaming Responses](streaming-responses.md) - Streaming tokens and intermediate agent output to the user in real time instead of waiting for the full response.
- [Voice Agents](voice-agents.md) - Real-time voice-to-voice agents built from speech-to-text and text-to-speech pipelines, where latency is the key constraint.
- [Voice Agent Pipeline](voice-pipeline.md) - The speech-to-text, LLM reasoning, and text-to-speech pipeline architecture that turns an agent into a real-time voice assistant (e.g. with LiveKit).

## No-code agent building
- [Agentic Automation](agentic-automation.md) - Building practical, configurable AI automations that take grunt work off people - per-client agent setups, multi-trigger n8n flows, and friction-reducing workflows.
- [AI Agent Business Niches](ai-agent-business-niches.md) - Productizing AI agents for concrete business use cases such as lead-generation and nurturing chatbots, underserved platforms, and reusable open-source agents.
- [Buy vs. Build](buy-vs-build.md) - For a classic, well-solved use case, leaning on a robust existing platform beats building it yourself, since wiring up all the tools and integrations is real work even for a technical builder.
- [Intents and Entities](intents-and-entities.md) - The no-code tool-definition mechanism where an intent (name, description, and example utterances) tells the agent when to fire a tool, and entities are the required input variables it must collect first.
- [No-Code AI Agents](no-code-agents.md) - Building functional AI agents by wiring nodes on a visual canvas instead of writing code, trading some control for much faster build and debug time.
- [No-Code Automation](no-code-automation.md) - Building agent workflows visually in tools like n8n, trading raw flexibility for speed and accessibility.
- [No-Code vs. Code](no-code-vs-code.md) - The use-case-by-use-case decision to build agents visually or in code, often starting no-code for speed then migrating to Python when hitting a feature ceiling.
- [Prompt Variable Templating](prompt-templating.md) - Defining named variables (e.g. {{prompt}}, {{context}}) inside a node's prompt to create typed inputs the workflow can wire data into.
- [Reusable Components and Variables](reusable-components.md) - Packaging sub-workflows as reusable components and storing conversation state in variables so context can be referenced later in prompts and tool calls.
- [Usage-Based Pricing Trap](usage-based-pricing-trap.md) - Metering a no-code app per database or API operation makes costs unpredictable and explode at scale, since every page load spends multiple billable units.
- [Visual Workflow Builder](visual-workflow-builder.md) - A drag-and-drop canvas of nodes (triggers, messages, AI responses, logic, API calls, and typed audio/text I/O) wired together to define how a conversation or automation flows.

## Local & self-hosted models
- [Fine-Tuning](fine-tuning.md) - Adapting a base model to a task or domain via additional training, weighed against just prompting a stronger general model.
- [Local & Self-Hosted AI](local-ai.md) - Running open-weight models on your own hardware or cloud for privacy, cost control, and independence from API providers.
- [Model Quantization](model-quantization.md) - Compressing model weights to lower precision so large models fit and run on limited local hardware.
- [Model Selection](model-selection.md) - Choosing the right LLM per task by trading off quality, speed, and cost, often routing easy requests to cheap models and hard ones to expensive models.
- [Reasoning Models](reasoning-models.md) - Models that produce explicit reasoning before answering, and when that extra thinking helps versus hurts.
