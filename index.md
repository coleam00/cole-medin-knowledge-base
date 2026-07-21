---
okf_version: "0.1"
---

# Cole Medin - AI Knowledge Base

> **Coverage: 198 long-form videos** (2023-04-05 to 2026-07-15), the full channel back catalog, compiled into **243 concept pages** and **242 entity pages** (198 tools, 13 people, 31 organizations) with **198 source summaries** over 925k words of transcript. This is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog) (OKF v0.1) bundle and a Karpathy-style LLM wiki: a synthesized, cross-linked graph of everything Cole teaches on [his channel](https://www.youtube.com/@ColeMedin), navigable with no database and no embeddings.

**If you are an agent:** read [SCHEMA.md](SCHEMA.md) for how this bundle is structured, then use this index to navigate. Follow the relative links into the pages a question needs, do not load the whole bundle. Every page ends with a `## Sources` section citing the video(s) and timestamps it came from, so you can always trace a claim back to the transcript. When you cannot answer from a page, say so rather than guessing. How-to for querying: [docs/query-guide.md](docs/query-guide.md).

**If you are a human:** start with the [README](README.md), then browse by theme below.

---

## Navigate

- **[Concepts](concepts/index.md)** - the ideas, techniques, patterns, and mental models.
- **[Entities](entities/index.md)** - the tools, people, and organizations.
  - [Tools & products](entities/tools/index.md) - [People](entities/people/index.md) - [Organizations](entities/organizations/index.md)
- **[Sources](sources/index.md)** - one summary page per video, with provenance to the raw transcript.
- **[Raw transcripts](raw/index.md)** - the immutable, timestamped source of truth.

## Themes

Pick the theme your question is about and open the hub concepts; each links onward to everything related. For the full list use the [concepts index](concepts/index.md).

- **AI agent fundamentals** - [The Core Components of an Agent](concepts/agent-core-components.md) - [Agent Development Lifecycle](concepts/agent-development-lifecycle.md) - [The Agent Loop (Reason-Act-Observe)](concepts/agent-loop.md) - [Agents vs. Workflows](concepts/agents-vs-workflows.md) - [Computer Use](concepts/computer-use.md) - [SDK vs. Framework Decision](concepts/sdk-vs-framework-decision.md)
- **Agent architecture & multi-agent systems** - [Agent Architecture Patterns](concepts/agent-architecture-patterns.md) - [Agent Dependency Injection](concepts/agent-dependencies.md) - [Agent Graphs](concepts/agent-graphs.md) - [Agent Teams](concepts/agent-teams.md) - [Graph-Based Agent Workflows](concepts/langgraph-nodes-edges-state.md) - [Local LLMs as Agents](concepts/local-llms-as-agents.md)
- **Agent reliability, safety & evaluation** - [Adversarial Agents](concepts/adversarial-agents.md) - [Agent Evaluation](concepts/agent-evaluation.md) - [Agent Observability](concepts/agent-observability.md) - [Agent Security](concepts/agent-security.md) - [Guardrails](concepts/guardrails.md) - [Human in the Loop](concepts/human-in-the-loop.md)
- **Context engineering** - [Context Engineering](concepts/context-engineering.md) - [Context Isolation](concepts/context-isolation.md) - [Context Reset](concepts/context-reset.md) - [Context Rot](concepts/context-rot.md) - [Context Window Limits](concepts/context-window-limits.md) - [Docs and Templates as Coding-Assistant Context](concepts/docs-as-agent-context.md)
- **Prompt engineering** - [Agent Prompting Techniques](concepts/agent-prompting.md) - [Prompting Techniques for AI Coding](concepts/ai-coding-prompting.md) - [Avoid Negative Instructions](concepts/avoid-negative-instructions.md) - [Chain-of-Thought Prompting](concepts/chain-of-thought.md) - [Docstrings as Tool Descriptions](concepts/docstrings-as-tool-descriptions.md) - [Effective Prompting](concepts/effective-prompting.md)
- **RAG & retrieval** - [Agentic RAG](concepts/agentic-rag.md) - [Agentic Search](concepts/agentic-search.md) - [Contextual Retrieval](concepts/contextual-retrieval.md) - [Hierarchical RAG](concepts/hierarchical-rag.md) - [Hybrid Search](concepts/hybrid-search.md) - [Keyword Search](concepts/keyword-search.md)
- **Chunking, embeddings & data** - [Chunking](concepts/chunking.md) - [Context-Aware Chunking](concepts/context-aware-chunking.md) - [Fine-Tuned Embeddings](concepts/fine-tuned-embeddings.md) - [Late Chunking](concepts/late-chunking.md) - [Structured vs Unstructured Data](concepts/structured-vs-unstructured-data.md) - [Vector Embeddings](concepts/vector-embeddings.md)
- **Knowledge bases & memory** - [Git as Long-Term Memory](concepts/git-as-long-term-memory.md) - [Heartbeat](concepts/heartbeat.md) - [Knowledge Bases](concepts/knowledge-bases.md) - [Knowledge Graphs](concepts/knowledge-graphs.md) - [Memory Systems](concepts/memory-systems.md) - [Second Brain](concepts/second-brain.md)
- **Agentic coding workflow** - [Agentic Coding](concepts/agentic-coding.md) - [Agentic Workflow Engineering](concepts/agentic-workflow-engineering.md) - [Clarifying Questions](concepts/clarifying-questions.md) - [Contract-First Development](concepts/contract-first.md) - [Reverting and Forking Conversations](concepts/conversation-checkpointing.md) - [Deterministic Workflows](concepts/deterministic-workflows.md)
- **AI coding landscape & tooling** - [AI Coding Assistant](concepts/ai-coding-assistant.md) - [AI Coding Harness](concepts/ai-coding-harness.md) - [Limitations of AI Coding Models](concepts/ai-coding-limitations.md) - [Everyday AI Coding Use Cases](concepts/ai-coding-use-cases.md) - [AI Coding Assistant UX Patterns](concepts/ai-coding-ux.md) - [Browser-Based AI Coding Tools](concepts/browser-based-ai-coding.md)
- **Commands, skills & self-evolving systems** - [Abstraction Distraction](concepts/abstraction-distraction.md) - [Capabilities Over Tools](concepts/capabilities-over-tools.md) - [Claude Code Hooks](concepts/claude-code-hooks.md) - [Commandify Everything](concepts/commandify-everything.md) - [Community-Driven Development](concepts/community-driven-development.md) - [Dark Factory](concepts/dark-factory.md)
- **Validation & code review** - [Code Review](concepts/code-review.md) - [End-to-End Validation](concepts/end-to-end-validation.md) - [Separate Reviewer](concepts/separate-reviewer.md) - [Test-Driven Development](concepts/test-driven-development.md) - [Validation](concepts/validation.md)
- **MCP & agent protocols** - [Agent Client Protocol (ACP)](concepts/agent-client-protocol.md) - [Agent Protocols](concepts/agent-protocols.md) - [Build Your Own MCP Server](concepts/build-your-own-mcp-server.md) - [Model Context Protocol (MCP)](concepts/mcp.md) - [MCP Server & Client Architecture](concepts/mcp-architecture.md) - [The Problems With MCP Servers](concepts/mcp-problems.md)
- **Deployment & production APIs** - [Agent as an API Endpoint](concepts/agent-as-api-endpoint.md) - [Agent Deployment](concepts/agent-deployment.md) - [Securing Agent APIs](concepts/api-security.md) - [Containerization & Docker Networking](concepts/containerization.md) - [Custom Domain via DNS A Record](concepts/custom-domain-dns.md) - [Embeddable Agent Widget](concepts/embeddable-agent-widget.md)
- **Agent UX & interfaces** - [Agentic Experiences](concepts/agentic-experiences.md) - [Chat Interfaces](concepts/chat-interfaces.md) - [Generative UI](concepts/generative-ui.md) - [Streaming Responses](concepts/streaming-responses.md) - [Voice Agents](concepts/voice-agents.md) - [Voice Agent Pipeline](concepts/voice-pipeline.md)
- **No-code agent building** - [Agentic Automation](concepts/agentic-automation.md) - [AI Agent Business Niches](concepts/ai-agent-business-niches.md) - [Buy vs. Build](concepts/buy-vs-build.md) - [Intents and Entities](concepts/intents-and-entities.md) - [No-Code AI Agents](concepts/no-code-agents.md) - [No-Code Automation](concepts/no-code-automation.md)
- **Local & self-hosted models** - [Fine-Tuning](concepts/fine-tuning.md) - [Local & Self-Hosted AI](concepts/local-ai.md) - [Model Quantization](concepts/model-quantization.md) - [Model Selection](concepts/model-selection.md) - [Reasoning Models](concepts/reasoning-models.md)

---

_Maintained per [SCHEMA.md](SCHEMA.md). Validate with `python lint.py`. Ingestion history in [log.md](log.md); scope in [roadmap.md](roadmap.md). How this was built: [docs/MAKING-OF.md](docs/MAKING-OF.md)._
