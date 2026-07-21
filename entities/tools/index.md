# Tools & Products

Tools, products, and frameworks referenced across the videos.

## Coding agents & IDEs
- [Claude Code](claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.
- [Codex](codex.md) - OpenAI's cloud-based software-engineering agent integrated with GitHub, plus a Codex CLI.
- [Cursor](cursor.md) - AI coding assistant that can consume AG-UI's llms.txt docs to help build with the protocol.
- [Windsurf](windsurf.md) - AI coding IDE Cole used to build the Python AG-UI backend and consume the protocol docs.
- [Cline](cline.md) - An early AI coding driver alongside Aider; PRP was inspired by the Cline community's memory-prompting framework.
- [Aider](aider.md) - An early AI coding driver Rasmus used when first developing the PRP framework.
- [Kiro](kiro.md) - Amazon's AI coding assistant, drawing growing enterprise interest after re:Invent.
- [OpenClaw](openclaw.md) - The agent project (formerly Claudebot) that Cole's second brain was researching; that research is the demo's input document.
- [Pi](pi-coding-agent.md) - A minimalistic, open-source coding agent cited as another example of a company-built harness around a model.
- [Gemini CLI](gemini-cli.md) - Google's coding CLI, where subagent support is experimental and which has a direct integration with the Agent Client Protocol.
- [Vercel Agent Browser CLI](agent-browser.md) - Browser-automation skill used for the final smoke test so the agent verifies the deployed site as a user would.
- [Git Worktrees](git-worktree.md) - Git feature that duplicates the codebase across isolated branches so multiple coding agents can run in parallel without collisions.
- [Archon](archon.md) - Cole's free, open-source AI command center and harness builder for AI coding; started as an AI agent that builds other AI agents.
- [Google Antigravity](google-antigravity.md) - Google's agentic coding environment pairing a traditional IDE with an agent-manager surface and Chrome integration, used as an alternative harness for running Gemini models.
- [GitHub Copilot](github-copilot.md) - GitHub's AI coding agent, which recently added subagent support for research, code analysis, and code review (distinct from the gh CLI tool already covered).
- [BMAD Method](bmad-method.md) - An open-source context-engineering framework (installed via npx bmad-method install) that ships expert sub-agent personas (analyst, PM, architect, scrum master, dev, QA) as markdown prompts driving separate greenfield and brownfield planning and development workflows.
- [GitHub Spec Kit](github-spec-kit.md) - GitHub's spec-driven development toolkit, providing slash commands for vibe planning, initial requirements, and plan creation, cited alongside PRP and BMAD as another expression of the same plan-implement-validate philosophy.
- [Omnigent](omnigent.md) - Open-source meta-harness from Databricks that orchestrates multiple AI coding agents (Claude Code, Codex, Pi) from one customizable AI layer with sandboxing, guardrails, and cross-device collaboration.
- [Stripe Minions](stripe-minions.md) - Stripe's internal agent harness that runs 'blueprints' interweaving agent nodes with deterministic code steps, shipping 1,300+ fully AI-written PRs every week.
- [Claw Hub](claw-hub.md) - OpenClaw's public skills marketplace, where research found hundreds of malicious packages stealing API keys and SSH credentials, the canonical example of untrusted third-party agent capabilities.
- [Ask Gordon](ask-gordon.md) - The AI agent built directly into Docker Desktop and wired to the MCP Toolkit by default, useful as a quick smoke test for MCP servers before connecting an external client (though its small model gets overwhelmed by large tool lists).
- [Zed](zed.md) - A free, open-source code editor from the team that created the Agent Client Protocol, shipping the first beta ACP implementation with native Gemini CLI and adapter-based Claude Code support.
- [Visual Studio Code](vs-code.md) - Microsoft's editor where Cole drops LLM-generated Python, fills in placeholders, and runs the app from the integrated terminal.
- [Tabnine](tabnine.md) - An AI code-completion assistant that fills in large blocks of code, inferring things like a full database schema from just the name you type.

## Agent frameworks & SDKs
- [Pydantic AI](pydantic-ai.md) - Cole's framework for the individual agents, structured around three parts: dependencies, the agent definition, and tools.
- [LangChain](langchain.md) - The framework used in prior masterclass videos to build the Asana agent; its message objects and invoke/stream methods underpin the chatbot logic.
- [LangGraph](langgraph.md) - The orchestration framework wiring agents into a stateful graph of nodes and edges, used here to run agents in parallel and add human-in-the-loop.
- [LangServe](langserve.md) - LangChain's library that wraps any chain or LangGraph runnable in a FastAPI web server via a single add_routes call, plus a RemoteRunnable client.
- [CrewAI](crewai.md) - Multi-agent framework named as one of the interchangeable backends AG-UI supports.
- [OpenAI Swarm](openai-swarm.md) - OpenAI's experimental multi-agent framework for building teams of agents that hand off to each other; defaults to OpenAI models but accepts a custom client.
- [OpenAI Agents SDK](openai-agents-sdk.md) - OpenAI's agent framework, which their guide leans on heavily with code examples.
- [Claude Agent SDK](claude-agent-sdk.md) - The engine that powers Claude Code, exposed as a library so you can invoke Claude Code programmatically and build custom agents on top of the same harness.
- [Vercel AI SDK](vercel-ai-sdk.md) - The front-end AI library whose llms.txt documentation Cole crawls as the demo knowledge base and uses to build a Claude 4 chat UI.
- [Arcade](arcade.md) - Platform for agent authorization and tool security, enabling secure OAuth flows and MCP servers so agents can act on a user's accounts.
- [Live Agent Studio](live-agent-studio.md) - Cole's community-driven open-source AI agent platform, host of a $5,000 agent hackathon in partnership with Voiceflow and n8n.
- [Eve (Vercel)](eve.md) - Vercel's open-source 'file-system first' agent framework where an entire agent is a single folder of markdown/TypeScript, compiled and deployed to production with durable sessions, sandboxing, human-in-the-loop, and evals.
- [Zod](zod.md) - A TypeScript schema/validation library used to type agent tool inputs so the arguments the model passes to a function are reliable.
- [Google Agents CLI](google-agents-cli.md) - Google's free open-source CLI and skill collection that instructs a coding agent to build, evaluate, deploy, and monitor agents on the ADK.
- [Google ADK (Agent Development Kit)](google-adk.md) - Google's minimalistic agent framework giving full control over prompting and tooling, with sandboxed code execution and one-command deployment to Google Cloud.
- [Roast](roast.md) - Shopify's open-source structured AI workflow engine that combines deterministic and agentic nodes, Cole's recommended starting point for building your own harness.
- [LangChain Deep Agents](langchain-deep-agents.md) - LangChain's harness implementation for long-running (not just coding) agents that manages context by offloading to file-system tools.
- [TypeScript](typescript.md) - The go-to language for building MCP servers, especially remote ones deployed to Cloudflare.
- [smolagents](smolagents.md) - Hugging Face's minimal agent framework whose base agent executes actions through generated code, used here to build an entire agentic RAG workflow in very little code.
- [Pydantic](pydantic.md) - Python's de facto data-validation library (also the foundation of FastAPI), used as the validation layer by OpenAI, Anthropic, LangChain, and LlamaIndex, and the reason Pydantic AI puts validation at an agent framework's core.
- [Node.js](nodejs.md) - JavaScript runtime used as an install prerequisite, whose npm scripts act as optional convenience wrappers around the underlying Docker build and run commands.
- [Express.js](express.md) - Minimal JavaScript web framework used to stand up the small backend API that holds the OpenAI key and proxies chat-completion requests for the browser client.
- [Auto-GPT](auto-gpt.md) - Open-source experiment that wraps GPT-4 in an autonomous goal-decomposition-and-execution loop with tool use and optional vector-database memory; the first widely known autonomous agent.

## No-code & app builders
- [n8n](n8n.md) - A no-code AI automation platform for building agents and workflows that integrate with 500+ applications.
- [Flowise](flowise.md) - Low-code LLM app / agent builder included and exposed in the stack.
- [Voiceflow](voiceflow.md) - A conversational-AI builder cited as a comparable node-based workflow platform.
- [bolt.new](bolt-new.md) - StackBlitz's commercial AI coding platform that generates entire full-stack applications; the stable product bolt.DIY forks from.
- [bolt.diy](bolt-diy.md) - Front-end build tools cited as examples of domains that already have strong built-in self-correction, so the knowledge-graph MCP isn't needed there.
- [oTToDev (autod Dev)](ottodev.md) - Community fork of bolt.new that adds support for any LLM, including local models via Ollama; the tool this video is built around.
- [autodev (bolt.new fork)](autodev.md) - Cole's community-built fork of bolt.new, used to generate the front-end wrapper (vanilla JS/HTML) that embeds the Voiceflow chat widget.
- [Lovable](lovable.md) - AI app builder optimized for Claude 3.5 Sonnet; Cole's earlier lovable build is the comparison baseline for the R1 build.
- [GoHighLevel](gohighlevel.md) - The CRM/calendar the lead-nurturing agent interacts with to check availability and book meetings.
- [Lindy](lindy.md) - The video's sponsor; an AI automation platform whose 'agent swarms' feature spins up many parallel agents for tasks like deep research.
- [Lutra](lutra.md) - Sponsor: a natural-language AI agent that writes and saves reusable code (playbooks) to take actions across services like Slack, Gmail, GitHub and Google Sheets.
- [Manus](manus.md) - First-of-its-kind general AI agent that pioneered context-engineering strategies; reportedly being acquired by Meta.
- [Vector Shift](vector-shift.md) - A visual AI-workflow builder cited as a comparable node-based platform.
- [Agent Zero](agent-zero.md) - A front-end Cole hooks the agent army into (as an API endpoint) to get chat and conversation history.
- [v0](v0.md) - Vercel's AI front-end generator that builds Next.js/shadcn UI components and whole front ends from natural-language prompts, with an npx install command to pull the generated component into a local project.
- [Make.com](make.md) - No-code integration and automation platform, alongside Zapier, that a no-code agent can bridge to for services it doesn't natively integrate.
- [Retool](retool.md) - Internal-app platform that imports React code and connects to a database to deploy dashboards with a governed, permissioned, audit-trailed path to production.
- [Gradio](gradio.md) - Python UI framework for ML/LLM apps, integrated directly into smolagents so an agent gets a full chat interface in a single line of code.
- [Bubble](bubble.md) - Popular no-code app builder Cole criticizes for 'workload unit' usage-based pricing that makes AI app costs unpredictable and ruinous at scale.
- [shadcn/ui](shadcn-ui.md) - The copy-in React component library that v0 emits, so generated UI lands as standard, fully-owned components you can import and customize in your own Next.js project.
- [Builder.io](builder-io.md) - Figma-to-code product Cole cites as the canonical case where training a custom model beat general GPT, then used GPT to refine the generated code.

## LLMs & model access
- [Claude](claude.md) - Named as an example of a large language model that can be turned into an agent.
- [ChatGPT](chatgpt.md) - The AI chat model used throughout as the example interface for prompting.
- [Google Gemini 2.0 Flash](gemini.md) - Google's LLM line; Gemini 2.5 led general-purpose models for months and Gemini 3 is considered the most powerful general LLM at year-end.
- [Qwen 2.5 Coder 32B](qwen.md) - Alibaba's open-source LLM family Cole cites as among his favorites that stood the test of time.
- [Llama](llama.md) - The open LLM model powering the agent, served via Groq in the current build.
- [DeepSeek R1](deepseek-r1.md) - Open-source MIT-licensed reasoning LLM that rivals OpenAI o1, ships in distilled sizes, and is far cheaper to run.
- [DeepSeek V3](deepseek-v3.md) - New open model Cole cites as evidence the local-vs-closed gap is closing fast; he's using it heavily in his own stack and it's performing great.
- [GPT-4](gpt-4.md) - OpenAI's model cited as strong enough that it reasons step by step without being told to.
- [GPT-4o](gpt-4o.md) - Cited as the more expensive, more powerful model to route complicated requests to in a cost-routing setup.
- [GPT-4o mini](gpt-4o-mini.md) - A fast, cheap OpenAI model cited as a speed benchmark; Quasar Alpha runs the MCP agent army even faster than it.
- [OpenRouter](openrouter.md) - Unified API gateway to many LLMs; here it hosts Quasar Alpha, its first stealth/cloaked pre-release Foundation model, free to use.
- [Ollama](ollama.md) - Local LLM runtime; works with a locally-run bolt.diy but can't be reached by a self-hosted (remote) instance.
- [Local AI Package](local-ai-package.md) - Cole's bundled collection of self-hosted AI services (database, n8n, Ollama, Open Web UI) that installs the whole stack together for free.
- [Claude Desktop](claude-desktop.md) - The MCP client used to demo connecting to the server, configured via developer settings and mcp-remote pointed at the streamable HTTP endpoint.
- [Open Web UI](open-web-ui.md) - Free, open-source, self-hostable ChatGPT-style chat interface; the frontend used to give n8n agents a polished UI with history, functions, and voice.
- [OpenAI o1](o1.md) - OpenAI's reasoning model line that thinks before answering via inference-time compute, cited as the leading example of reasoning LLMs that reduce hallucinations and bad agent decisions.
- [OpenAI o3-mini](o3-mini.md) - OpenAI's small reasoning model, used as Archon's reasoner to write the scope document before the coder agent builds, and the head-to-head rival to DeepSeek R1 for coding.
- [DeepSeek Coder V2](deepseek-coder-v2.md) - Open-source 236B-parameter coding model available via OpenRouter or the DeepSeek API, recommended as roughly 20x cheaper than Claude while remaining highly capable for AI coding.
- [LM Studio](lm-studio.md) - Desktop app for downloading and running open-weight LLMs locally, the main alternative to Ollama and a requested provider integration for the bolt.new fork.
- [Kimi K2](kimi-k2.md) - Moonshot's Kimi model (K2.7), used as a cheap driver and exploration model in Cole's harness via a Kimi subscription to control per-token cost.
- [Gemini 3.5 Flash](gemini-3-5-flash.md) - Google's cheap, fast LLM that builds unusually beautiful, handcrafted-looking frontends; the design half of Cole's provider-mixing workflow, paired with Opus 4.8 for planning and integrations.
- [Claude Opus 4.8](claude-opus-4-8.md) - Anthropic's reasoning-heavy Claude release that owns planning, page copy, integrations, and fixes in Cole's mixed-provider frontend workflow.
- [MiniMax M2.7](minimax-m2.md) - A cheap, fast, capable LLM that Cole routes Claude Code to (via environment variables) to drive the entire dark factory economically at high throughput instead of Anthropic models.
- [GPT-5.4 Mini & Nano](gpt-5-4-mini-nano.md) - OpenAI's small/fast model releases marketed explicitly for subagents and AI coding; nano reportedly beats Claude Haiku 4.5 at a fifth the price and ~188 tok/s, anchoring the 'subagent era' thesis.
- [Gemini 3](gemini-3.md) - Google's flagship LLM release, genuinely strong on abstract reasoning (a large ARC-AGI-2 jump) and especially good at frontend and design work, though its real-world edge is hard to separate from the tooling layered on top of it.
- [Claude Sonnet 4.5](claude-sonnet-4-5.md) - Anthropic's coding-focused model release that topped the coding and agentic-tool-use benchmarks over Opus 4.1 and shipped as the default model in Claude Code 2.0.
- [GPT-5 Codex](gpt-5-codex.md) - OpenAI's coding-specialized GPT-5 model, the head-to-head opponent Cole benchmarks against Sonnet 4.5 on an identical real-world Stripe integration task.
- [GPT-4.1 Nano](gpt-4-1-nano.md) - OpenAI's smallest, cheapest model in the GPT-4.1 line, used for the per-chunk context-generation call in contextual retrieval because the task needs almost no reasoning power.
- [QwQ](qwq.md) - Alibaba's open reasoning model, cited as the kind of model that could draft a plan or README before any code is generated.
- [Code Llama](code-llama.md) - Meta's open-source code-specialized LLM family whose larger 34B variant fails builds that the smaller Qwen 2.5 Coder 32B handles, showing capability beats parameter count.
- [Claude 3.5 Sonnet](claude-3-5-sonnet.md) - Anthropic's mid-2024 flagship model and the only LLM Cole could not break in his agentic stress test, making it his clear winner for multi-step tool-using workflows.
- [GPT-3.5 Turbo](gpt-3-5-turbo.md) - OpenAI's ChatGPT-era chat-completion model called by the proxy server to generate the text that replaces the user's selection in place.

## RAG, embeddings & knowledge
- [Crawl4AI](crawl4ai.md) - The open-source crawling library powering Cole's RAG MCP server, handling llms.txt, sitemaps, and recursive scraping.
- [Crawl4AI RAG MCP Server](crawl4ai-rag-mcp.md) - Cole's open-source MCP server that gives coding assistants external knowledge via RAG and now knowledge-graph hallucination detection.
- [Docling](docling.md) - The open-source Python data-extraction/chunking tool that is the subject of the video summarized and integrated into Archon during the workflow demo.
- [Graphiti](graphiti.md) - A knowledge-graph tool Cole names as a candidate for a future agentic-RAG-with-knowledge-graphs strategy.
- [Neo4j](neo4j.md) - The graph database used to store and visualize the repository knowledge graph.
- [Qdrant](qdrant.md) - Vector database with an MCP server that lets agents do RAG without implementing custom retrieval tools.
- [Pinecone](pinecone.md) - Vector database used optionally by Auto-GPT to provide long-term memory.
- [Chroma](chroma.md) - Publisher of the technical report on context rot that Cole cites as the most practical treatment of how input tokens degrade LLM performance.
- [Mem0](mem0.md) - Open-source Python library for building per-user long-term memory for AI agents via memory extraction, vector storage, and retrieval; the core tool of the video.
- [LightRAG](lightrag.md) - A knowledge-graph RAG solution Cole previously covered; suited to static document summarization but slower to build and query than Graphiti.
- [Context7](context7.md) - A hosted MCP RAG server for 8,000+ library docs; impressive but too broad, can't include private repos, and its core logic is closed-source.
- [nomic-embed-text](nomic-embed-text.md) - Embedding model added to the Ollama container pull so RAG embeddings are available in the workflows.
- [Obsidian](obsidian.md) - Free, local, markdown-based knowledge app Cole uses as the storage layer and canvas for his AI second brain; also renders Excalidraw diagram JSON.
- [GraphRAG](graphrag.md) - A popular knowledge-graph RAG implementation Cole groups with LightRAG as built for static, rarely-changing document summarization rather than dynamic incrementally-updated data.

## Databases & backend
- [Supabase](supabase.md) - A single platform providing Postgres for scalable chat memory plus the pgvector store for RAG embeddings, recommended over in-memory alternatives.
- [Postgres](postgres-pgvector.md) - A Postgres extension for storing vector embeddings, used within Supabase as a production-ready vector store for RAG.
- [Neon](neon.md) - Serverless Postgres platform Cole favors, acquired by Databricks in 2025.
- [Redis](redis.md) - In-memory cache bundled alongside SearXNG for caching web-search results.
- [MongoDB](mongodb.md) - NoSQL database used here as both the document store and vector database, with aggregation pipelines and preview Rank Fusion features that make it optimal for hybrid search.
- [Firebase](firebase.md) - Underlies the Google Cloud Functions project structure Cole uses for the agent backend.
- [FastAPI](fastapi.md) - Python web framework used to serve the swapped-in Python agent endpoint that streams AG-UI events.
- [Python](python.md) - Language Auto-GPT is built in; requires Python 3.8+ to run.
- [Next.js](nextjs.md) - React framework hosting the demo's CopilotKit runtime API route for the agent.
- [React](react.md) - Front-end library used for the AG-UI demo application connecting to the agent.
- [Redis Iris](redis-iris.md) - A preview Redis product that wraps the database with a Context Retriever (auto-generated MCP tools over defined entities/schema) and Agent Memory (short/long-term with background promotion to vector-indexed memory), demoed as the production-agent substitute for markdown second brains.
- [Oracle AI Database](oracle-ai-database.md) - The video's sponsor; a unified AI database with built-in embeddings and semantic, keyword, and knowledge-graph search in one place, used for Cole's agentic RAG demo.
- [Clerk](clerk.md) - Drop-in authentication and user-management provider for web apps; Cole seeds a Clerk test account so an autonomous agent can sign in and self-validate the real running app.
- [SQLite](sqlite.md) - Embedded, file-based SQL database that lets example projects run with zero external database setup.

## MCP & agent UI protocols
- [MCP (Model Context Protocol)](mcp.md) - The protocol used to connect Claude Code to external tools and servers.
- [AG-UI](ag-ui.md) - Open protocol (by the CopilotKit team) that standardizes connecting AI agents to front ends via emitted events; ~16 event types.
- [A2UI](a2ui.md) - Google's generative-UI specification for how an agent defines the components (id, name, children, props) the front end renders.
- [CopilotKit](copilotkit.md) - Open-source front-end library for building agentic applications; the team that built AG-UI, providing React components to wire agents into a UI.
- [Coinbase x402](x402.md) - Coinbase's payment protocol for exposing AI agents over the internet that charge other agents per use, settled in stablecoins like USDC.
- [Sequential Thinking MCP Server](sequential-thinking-mcp.md) - A stdio MCP server that instructs a model to reason step by step, used to buy extra thinking tokens and attached to custom Claude Agent SDK agents via JSON config.
- [Docker MCP Toolkit](docker-mcp-toolkit.md) - Docker Desktop's MCP feature set: a curated catalog of hundreds of servers, a toolkit that runs each tool as an ephemeral container, and an open-source gateway for orchestrating them.
- [FastMCP](fastmcp.md) - Anthropic's high-level Python interface in the MCP SDK for spinning up an MCP server in one line (name, description, lifespan, host, port) and registering tools with the @mcp.tool decorator.

## Deployment & infrastructure
- [Docker](docker.md) - Containerization prerequisite; a single docker compose command spins up Archon's four containers (agents, MCP server, UI, API server).
- [Caddy](caddy.md) - Reverse proxy providing managed HTTPS/TLS via Let's Encrypt so each service gets a secure subdomain endpoint.
- [Render](render.md) - The cloud deployment platform (used on its free tier) that auto-builds and deploys staging on push and production on commit to main.
- [Netlify](netlify.md) - Deployment target on the roadmap for a one-click deploy from bolt.diy.
- [RunPod](runpod.md) - GPU cloud recommended when you need a powerful high-VRAM machine to run large language models like Llama 3.2 90B.
- [Uvicorn](uvicorn.md) - The ASGI server used to host the FastAPI app, running on 0.0.0.0:8000.
- [Streamlit](streamlit.md) - Used to build the travel-planner's chat UI, where users set preferences and watch the streamed synthesizer output.
- [Git](git.md) - Version control used as a core part of harness memory: commits and the git log let fresh sessions reconstruct progress, and enable automatic rollback.
- [GitHub](github.md) - The gh command-line tool that lets Claude Code manage issues and pull requests directly on a remote GitHub repository.
- [ngrok](ngrok.md) - Tunneling tool that exposes a local dev server on a public HTTPS URL so third-party webhooks (here ChargeBee's) can reach a local endpoint during development.
- [GitHub Actions](github-actions.md) - GitHub's built-in CI/CD system that runs trigger-based workflows to invoke coding assistants in isolated, GitHub-hosted environments.
- [Vertex AI](vertex-ai.md) - Google's cloud AI platform offering powerful agent capabilities out of the box, recommended in Google's agent white paper.
- [Nginx](nginx.md) - Open-source web server used as the reverse proxy that maps a public URL and domain to a local app's port, with configs symlinked from sites-available to sites-enabled and validated with nginx -t.
- [Certbot](certbot.md) - EFF tool that obtains and installs free Let's Encrypt SSL certificates and rewrites the web-server config so a deployed site is served over HTTPS.
- [n8n Self-Hosted AI Starter Kit](n8n-self-hosted-ai-starter-kit.md) - n8n's official Docker Compose package bundling Ollama, Qdrant, Postgres, and n8n so a fully local AI stack (LLMs, vector DB, SQL DB, orchestration) starts with one command.
- [Google Cloud Functions](google-cloud-functions.md) - Google's serverless function platform, used as the HTTP endpoint that receives the GoHighLevel webhook and hosts the agent's request-handling backend.

## Observability, testing & code quality
- [Langfuse](langfuse.md) - The platform Cole uses specifically to monitor AI agents in production, distinct from Sentry which he uses for backend/RAG infrastructure.
- [LangSmith](langsmith.md) - A competing observability platform Cole contrasts against Langfuse, faulting it for not being fully open-source.
- [Logfire](logfire.md) - Observability tool by the Pydantic team that instruments Pydantic AI agents to send traces, token usage, and cost as telemetry for local and production debugging.
- [Sentry](sentry.md) - Application monitoring platform (the video sponsor) that makes it easy to add tracing, logs, and error alerting to MCP servers in production.
- [CodeRabbit](code-rabbit.md) - AI code review tool that automatically and thoroughly reviews every pull request, free for open-source repos, with security vulnerability detection.
- [QA Tech](qa-tech.md) - AI testing platform whose agents crawl your deployed site and generate/evolve regression test cases as the codebase grows (has a free tier).
- [Playwright](playwright.md) - Cole's deterministic multi-browser web automation tool, whose MCP server lets coding assistants visually validate frontend changes.
- [Browserbase](browserbase.md) - Browser-automation company Cole partnered with; its Stagehand framework and Director platform bring self-correcting web automation on top of Playwright.
- [Puppeteer](puppeteer.md) - Browser-automation MCP server that lets a coding agent load pages, click, and screenshot to visually validate that a feature actually works before marking it passed.
- [Guardrails AI](guardrails-ai.md) - Open-source Python framework Cole leans on for agent input/output guardrails, blocking things like PII entering a prompt or unsafe content leaving the LLM.
- [Stagehand](stagehand.md) - Browserbase's open-source browser-automation framework, exposed as an MCP server so a coding agent can navigate a deployed site and validate its own work.
- [OpenTelemetry](opentelemetry.md) - The open telemetry standard that agent frameworks (Pydantic AI via Logfire) emit traces through, letting any compatible backend such as Langfuse ingest them without vendor lock-in.
- [Berkeley Function Calling Leaderboard](berkeley-function-calling-leaderboard.md) - A public benchmark that ranks LLMs on function-calling accuracy using tasks meant to represent real agent and enterprise workflows.

## Voice & media
- [ElevenLabs](elevenlabs.md) - The paid text-to-speech provider used for high-quality narration and voice cloning (though cloning takes work to make reliable).
- [Aqua Voice](aqua-voice.md) - Speech-to-text platform Cole uses to dictate into any text box, especially for communicating with LLMs.
- [Vapi](vapi.md) - No-code voice AI platform cited as easy but a black box, which Cole and clients have moved off of for custom solutions.
- [Remotion](remotion.md) - The earlier tool that first gave Claude Code a skill to generate videos; Cole found it less reliable than HyperFrames.
- [OpenAI Whisper](whisper.md) - OpenAI's open-source speech-to-text model; Whisper Turbo runs fully locally as Docling's ASR pipeline to transcribe audio and video into timestamped text.
- [Higgsfield](higgsfield.md) - A video-generation platform with a CLI used to create marketing videos and UGC-style ads from prompts and branded reference images, driven from inside the coding agent's terminal.
- [HyperFrames](hyperframes.md) - An HTML-based video rendering tool with a built-in preview editor that lets AI agents generate and mold animated scenes, positioned as a more reliable step up from Remotion.
- [Kokoro](kokoro.md) - A free, open-source text-to-speech model that lets you run the entire AI video-generation workflow at no cost.
- [Sora 2](sora-2.md) - OpenAI's video-plus-audio generation model that took the world by storm in 2025 and drew a $1B Disney investment.
- [LiveKit](livekit.md) - Open-source Python framework for building customizable, self-hostable voice AI agents with a swappable STT/LLM/TTS pipeline, tool calling, MCP server support, and a CLI deploy path to LiveKit Cloud.
- [Deepgram](deepgram.md) - Speech-to-text provider (with a free tier) used as the transcription stage of the deployed LiveKit voice pipeline.

## Productivity & integrations
- [Asana](asana.md) - Task-management platform the agent integrates with; the chatbot creates real Asana tasks with due dates from natural-language requests.
- [Jira](jira.md) - Example issue tracker whose scoped tickets tell the engineer (and agent) which slice of the codebase to work in.
- [Linear](linear.md) - Project/issue tracker Cole used in place of the local file system to track a harness's feature list and progress, adding human-in-the-loop where teams already work.
- [Slack](slack.md) - Messaging platform used as an alerting destination for error workflows and scheduled report notifications, and as the chat surface for talking to agents.
- [Telegram](telegram.md) - The messaging app Cole integrates Codex into via the Telegraf library, letting him trigger remote coding jobs from his phone.
- [Zapier](zapier.md) - Automation platform whose MCP server connects agents to 8,000+ apps (video sponsor).
- [Google Drive](google-drive.md) - Used as a trigger/source node whose file outputs feed the RAG ingestion pipeline and illustrate multi-item looping.
- [Postman](postman.md) - API platform (video sponsor) that became git-native, syncing collections/specs/tests as local YAML with an agent mode across the API lifecycle.
- [Gmail](gmail.md) - Google's email service, the canonical per-user integration in this video: hardcoded Gmail credentials illustrate the scaling problem, and a Gmail toolkit is what the agent authorizes per user.
- [Excalidraw](excalidraw.md) - Free, open-source hand-drawn-style diagramming tool whose JSON format coding agents can generate directly, rendered at excalidraw.com or through the Obsidian Excalidraw plugin.
- [tmux](tmux.md) - Terminal multiplexer (Cole's recommended option) that Claude Code drives to create the split-pane windows showing each agent-team teammate working in real time.
- [iTerm2](iterm2.md) - macOS terminal application with split-pane support; one of only two terminals Claude Code can drive to display agent teams live.
- [Airtable](airtable.md) - Spreadsheet-database platform wired to an agent via its MCP server, backing the 'AI research base' where the agent army writes and reads structured records.
- [Confluence](confluence.md) - Atlassian's team documentation wiki, connected via API key as the ingested knowledge-base source that grounds a RAG assistant's answers.
- [Notion](notion.md) - All-in-one docs and workspace app, supported alongside Confluence and Google Drive as a knowledge-base source for chat assistants.
- [Google Calendar](google-calendar.md) - Google's calendar service, integrated via API as the action target for agents that turn extracted meeting action items into scheduled events.
- [Prompt Engineering Guide](prompting-guide.md) - promptingguide.ai, the free resource Cole names as the single prompt-engineering guide worth studying end to end.

## Search & retrieval tools
- [Brave Search API](brave-search.md) - Web search API wired up as the single example tool giving the template agent the ability to search the web.
- [SearXNG](searxng.md) - Local, private metasearch engine added for web search (with Redis for caching); kept private since it isn't password protected.
- [grep (command-line search)](ripgrep.md) - The default CLI search Claude Code uses for agentic navigation; the video argues it becomes slow and token-inefficient past six-figure line counts, motivating LSP.
- [Serena](serena.md) - An open-source MCP server for semantic code retrieval and editing that outperforms a coding agent's built-in codebase search as the codebase grows.
- [Perplexity](perplexity.md) - AI-powered deep research search engine Cole uses daily to research new LLMs, frameworks, and AI tech.
