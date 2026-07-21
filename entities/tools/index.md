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

## MCP & agent UI protocols
- [MCP (Model Context Protocol)](mcp.md) - The protocol used to connect Claude Code to external tools and servers.
- [AG-UI](ag-ui.md) - Open protocol (by the CopilotKit team) that standardizes connecting AI agents to front ends via emitted events; ~16 event types.
- [A2UI](a2ui.md) - Google's generative-UI specification for how an agent defines the components (id, name, children, props) the front end renders.
- [CopilotKit](copilotkit.md) - Open-source front-end library for building agentic applications; the team that built AG-UI, providing React components to wire agents into a UI.

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

## Observability, testing & code quality
- [Langfuse](langfuse.md) - The platform Cole uses specifically to monitor AI agents in production, distinct from Sentry which he uses for backend/RAG infrastructure.
- [LangSmith](langsmith.md) - A competing observability platform Cole contrasts against Langfuse, faulting it for not being fully open-source.
- [Logfire](logfire.md) - Observability tool by the Pydantic team that instruments Pydantic AI agents to send traces, token usage, and cost as telemetry for local and production debugging.
- [Sentry](sentry.md) - Application monitoring platform (the video sponsor) that makes it easy to add tracing, logs, and error alerting to MCP servers in production.
- [CodeRabbit](code-rabbit.md) - AI code review tool that automatically and thoroughly reviews every pull request, free for open-source repos, with security vulnerability detection.
- [QA Tech](qa-tech.md) - AI testing platform whose agents crawl your deployed site and generate/evolve regression test cases as the codebase grows (has a free tier).
- [Playwright](playwright.md) - Cole's deterministic multi-browser web automation tool, whose MCP server lets coding assistants visually validate frontend changes.
- [Browserbase](browserbase.md) - Browser-automation company Cole partnered with; its Stagehand framework and Director platform bring self-correcting web automation on top of Playwright.

## Voice & media
- [ElevenLabs](elevenlabs.md) - The paid text-to-speech provider used for high-quality narration and voice cloning (though cloning takes work to make reliable).
- [Aqua Voice](aqua-voice.md) - Speech-to-text platform Cole uses to dictate into any text box, especially for communicating with LLMs.
- [Vapi](vapi.md) - No-code voice AI platform cited as easy but a black box, which Cole and clients have moved off of for custom solutions.
- [Remotion](remotion.md) - The earlier tool that first gave Claude Code a skill to generate videos; Cole found it less reliable than HyperFrames.

## Productivity & integrations
- [Asana](asana.md) - Task-management platform the agent integrates with; the chatbot creates real Asana tasks with due dates from natural-language requests.
- [Jira](jira.md) - Example issue tracker whose scoped tickets tell the engineer (and agent) which slice of the codebase to work in.
- [Linear](linear.md) - Project/issue tracker Cole used in place of the local file system to track a harness's feature list and progress, adding human-in-the-loop where teams already work.
- [Slack](slack.md) - Messaging platform used as an alerting destination for error workflows and scheduled report notifications, and as the chat surface for talking to agents.
- [Telegram](telegram.md) - The messaging app Cole integrates Codex into via the Telegraf library, letting him trigger remote coding jobs from his phone.
- [Zapier](zapier.md) - Automation platform whose MCP server connects agents to 8,000+ apps (video sponsor).
- [Google Drive](google-drive.md) - Used as a trigger/source node whose file outputs feed the RAG ingestion pipeline and illustrate multi-item looping.
- [Postman](postman.md) - API platform (video sponsor) that became git-native, syncing collections/specs/tests as local YAML with an agent mode across the API lifecycle.

## Search & retrieval tools
- [Brave Search API](brave-search.md) - Web search API wired up as the single example tool giving the template agent the ability to search the web.
- [SearXNG](searxng.md) - Local, private metasearch engine added for web search (with Redis for caching); kept private since it isn't password protected.
- [grep (command-line search)](ripgrep.md) - The default CLI search Claude Code uses for agentic navigation; the video argues it becomes slow and token-inefficient past six-figure line counts, motivating LSP.
