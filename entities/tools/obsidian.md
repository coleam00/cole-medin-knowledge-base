---
type: entity
subtype: tool
title: "Obsidian"
description: "Free, local, markdown-based knowledge app Cole uses as the storage layer and canvas for his AI second brain; also renders Excalidraw diagram JSON."
resource: "https://obsidian.md"
tags: [knowledge-management, markdown, second-brain, local]
videos: [i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does, finally-an-open-standard-for-the-karpathy-llm-wiki-is-here, i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases, full-guide-build-your-own-ai-second-brain-with-claude-code, build-beautiful-diagrams-with-claude-code-full-workflow, i-built-a-safer-openclaw-alternative-using-claude-code, i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how, claude-codes-real-purpose-its-bigger-than-you-think, docker-just-made-using-mcp-servers-100x-easier-one-click-installs, the-true-power-of-ai-coding-build-your-own-workflows-full-guide]
created: 2026-07-21
updated: 2026-07-21
---

# Obsidian

Obsidian is the free, local, markdown-based app Cole uses as the storage layer and canvas for his AI [Second Brain](../../concepts/second-brain.md). His plain definition: "Obsidian is our local and private knowledge base. All of our files are simply stored as markdown docs on our computer" - ["I Built My Second Brain with Claude Code + Obsidian + Skills"](../../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) [0:06:35]. That everything-is-plain-markdown-on-disk property is the entire reason it fits his stack: an agent can read and evolve the vault directly. "I integrate with Obsidian because it's where I store all of my knowledge and have my agent evolve it over time" - ["Full Guide - Build Your Own AI Second Brain with Claude Code"](../../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) [0:02:06].

## How Cole uses it

Obsidian is the persistent knowledge substrate under most of Cole's memory work. His memory system is nothing more than markdown documents living in the vault: "I'm syncing my memory system. All these markdown documents, I'm storing it in Obsidian. And so my tech stack is Obsidian for storage, Markdown obviously for the memory system" - ["I Built a Safer OpenClaw Alternative Using Claude Code"](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) [0:09:26]. He calls it "my canvas for working with things with my second brain" and singles out the graph view as "one of the coolest parts of Obsidian" - ["I Built Self-Evolving Claude Code Memory..."](../../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) [0:00:48], [0:03:58], which visualizes the wiki-link structure the same way a [Knowledge Graph](../../concepts/knowledge-graphs.md) does.

The decisive advantage over Notion is direct file-system access, which removes an integration layer: "it's also much better than something like notion because then we have to use an MCP server. We can't just have Claude Code work directly in our file system like we can with Obsidian" [0:07:19]. That said, when Cole wants programmatic access he does use the community-plugin ecosystem, enabling the local REST API plugin: "when you go into the settings for Obsidian, you can install community plugins. And one of these plugins... is called the local rest API" - ["Docker Just Made Using MCP Servers 100x Easier"](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) [0:09:53], and a Copilot plugin for in-app chat. For his LLM-wiki work he treats Obsidian as the ideal home for the compiled bundle: "LLM Wiki, if using Hermes or Claude code or whatever with Obsidian, like that's actually ideal to keep things simple and flexible" - ["I Love the Karpathy LLM Wiki but it Doesn't Scale"](../../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) [0:18:20]. Separately, its Excalidraw plugin is one of the two supported ways to render the diagram JSON his workflow generates: "putting that all together to then build the JSON file that we can render with the Obsidian Excalidraw plugin or an excalidraw.com" - ["Build BEAUTIFUL Diagrams with Claude Code"](../../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) [0:07:29].

## Realizes

- [Second Brain](../../concepts/second-brain.md) - A personal, always-on AI system that captures, recalls, and acts on your knowledge and daily context.
- [The LLM Wiki](../../concepts/the-llm-wiki.md) - An LLM-maintained knowledge base of plain markdown pages that compiles sources into a navigable, self-referential wiki.

## Works with

- [Claude Code](./claude-code.md) - Anthropic's terminal-based agentic coding assistant that is the subject of this complete-guide walkthrough.

## Related

- [Memory Systems](../../concepts/memory-systems.md) - Giving agents durable short- and long-term memory so conversations, user context, and facts persist across sessions and users.
- [Progressive Disclosure](../../concepts/progressive-disclosure.md) - Loading context, skills, and tools on demand only when a task needs them instead of front-loading everything into the context window.
- [Context Engineering](../../concepts/context-engineering.md) - The deliberate practice of curating exactly what goes into an LLM's limited context window - system messages, schemas, chat history, and dynamic variables - to avoid overload and keep outputs sharp.
- [Skills](../../concepts/skills.md) - Reusable, model-invoked capability packages that load specialized instructions and tools on demand to extend an agent.
- [Knowledge Graphs](../../concepts/knowledge-graphs.md) - Structuring knowledge as entities and relationships (often temporal) so agents can traverse connections a vector store can't express.

## Sources

- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:06:35] Obsidian is our local and private knowledge base. All of our files are simply stored as markdown docs on our computer"
- [I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)](../../sources/i-built-my-second-brain-with-claude-code-obsidian-skills-heres-how.md) - "[0:07:19] it's also much better than something like notion because then we have to use an MCP server. We can't just have Claude Code work directly in our file system like we can with Obsidian"
- [Full Guide - Build Your Own AI Second Brain with Claude Code](../../sources/full-guide-build-your-own-ai-second-brain-with-claude-code.md) - "[0:02:06] I integrate with Obsidian because it's where I store all of my knowledge and have my agent evolve it over time"
- [I Built a Safer OpenClaw Alternative Using Claude Code](../../sources/i-built-a-safer-openclaw-alternative-using-claude-code.md) - "[0:09:26] I'm syncing my memory system. All these markdown documents, I'm storing it in Obsidian. And so my tech stack is Obsidian for storage, Markdown obviously for the memory system."
- [I Built Self-Evolving Claude Code Memory w/ Karpathy's LLM Knowledge Bases](../../sources/i-built-self-evolving-claude-code-memory-w-karpathys-llm-knowledge-bases.md) - "[0:00:48] I love seeing that he's using Obsidian as a core part of his stack. I always call it my canvas for working with things with my second brain"
- [Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)](../../sources/build-beautiful-diagrams-with-claude-code-full-workflow.md) - "[0:07:29] putting that all together to then build the JSON file that we can render with the Obsidian Excalidraw plugin or an excalidraw.com."
- [Claude Code's Real Purpose (It's Bigger Than You Think)](../../sources/claude-codes-real-purpose-its-bigger-than-you-think.md) - "[0:09:50] Obsidian, it is a completely free and local solution for knowledge management and note-taking. It's kind of like my second brain."
- [Docker Just Made Using MCP Servers 100x Easier (One Click Installs!)](../../sources/docker-just-made-using-mcp-servers-100x-easier-one-click-installs.md) - "[0:09:53] when you go into the settings for Obsidian, you can install community plugins. And one of these plugins... is called the local rest API."
- [I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.](../../sources/i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does.md) - "[0:18:20] LLM Wiki, if using Hermes or Claude code or whatever with Obsidian, like that's actually ideal to keep things simple and flexible."
- [Finally, an Open Standard for the Karpathy LLM Wiki is HERE](../../sources/finally-an-open-standard-for-the-karpathy-llm-wiki-is-here.md) - "[0:11:55] Brings the bundle into your local Obsidian or Notion or whatever you're managing your knowledge. And then boom, you can instantly start asking questions."
- [The True Power of AI Coding - Build Your OWN Workflows (Full Guide)](../../sources/the-true-power-of-ai-coding-build-your-own-workflows-full-guide.md) - "[0:03:09] switching to an app called Obsidian. It is a free and local knowledge management platform... there's also a ton of open source plugins"
