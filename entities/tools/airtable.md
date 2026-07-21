---
type: entity
subtype: tool
title: "Airtable"
description: "Spreadsheet-database platform wired to an agent via its MCP server, backing the 'AI research base' where the agent army writes and reads structured records."
resource: "https://airtable.com"
tags: [integration, productivity]
videos: [build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how]
created: 2026-07-21
updated: 2026-07-21
---

# Airtable

Airtable is a spreadsheet-database hybrid: bases made of tables with typed fields and records, editable like a spreadsheet but queryable like a database. In Cole's catalog it plays exactly one role, and plays it well - it is the **structured store an agent writes into** when the output of research needs to be rows rather than prose. It reaches the agent through its MCP server, so the agent never touches the Airtable API directly; it just calls tools like "list records" and "create record."

The canonical demo is the Archon agent army. A primary [Pydantic AI](./pydantic-ai.md) agent decomposes a request and delegates each leg to a specialized sub-agent, each bound to one MCP server. Asked to research the top AI agent frameworks, it first calls the [Brave Search API](./brave-search.md) sub-agent to gather candidates, then hands off: "now it's calling the Air Table agent to list all the entries that are available in the framework table" [0:07:02]. Note the order - the agent reads the table *before* writing to it, checking what already exists so it does not duplicate records, then creates one record per framework. A follow-up turn has the Airtable sub-agent fetch the base URL for the AI research base and a [Slack](./slack.md) sub-agent post the link to a research channel, which is the whole point of putting structured data behind MCP: the record store becomes one interchangeable capability among many.

Cole's note about model economics matters here too. The Airtable sub-agent runs on [GPT-4o mini](./gpt-4o-mini.md), not a frontier model, because a sub-agent with a narrow tool list and a tight system prompt does not need one.

## Realizes

- [Structured vs Unstructured Data](../../concepts/structured-vs-unstructured-data.md) - Airtable is where the agent puts the structured half, as typed records rather than free text in a document.
- [Knowledge Bases](../../concepts/knowledge-bases.md) - the base functions as the durable, queryable memory the agent army accumulates research into.
- [Tool Calling](../../concepts/tool-use.md) - every read and write is a tool call, list records then create records, not custom API glue.

## Works with

- [MCP (Model Context Protocol)](./mcp.md) - the Airtable MCP server is the only integration surface the agent sees.
- [Archon](./archon.md) - Cole builds the agent army that drives Airtable inside Archon.
- [Pydantic AI](./pydantic-ai.md) - the framework the primary agent and every sub-agent are written in.
- [Brave Search API](./brave-search.md) - supplies the research that becomes Airtable records.
- [Slack](./slack.md) - the delivery channel for the base link once the records are written.
- [GitHub](./github.md) - another MCP-backed sub-agent in the same fleet.

## Contrasts with

- [Notion](./notion.md) - the document-first workspace for the same job when the output is prose rather than rows.
- [Supabase](./supabase.md) - a real Postgres backend when the structured store needs to serve an application, not a human browsing a grid.

## Related

- [Agent Teams](../../concepts/agent-teams.md) - the primary-plus-sub-agent structure Airtable is one leaf of.
- [Subagents Pattern](../../concepts/subagents-pattern.md) - why the Airtable tools live behind their own agent instead of bloating one prompt.
- [Agents That Build Agents](../../concepts/agents-that-build-agents.md) - the Archon vision the demo is showcasing.
- [No-Code Automation](../../concepts/no-code-automation.md) - the world Airtable came from before agents started writing to it.
- [Agentic Automation](../../concepts/agentic-automation.md) - research-to-record-to-notification as an autonomous chain.

## Sources

- [Build an ARMY of AI Agents on Autopilot with Archon, Here's How](../../sources/build-an-army-of-ai-agents-on-autopilot-with-archon-heres-how.md) - "[0:07:02] now it's calling the Air Table agent to list all the entries that are available in the framework table"
