---
type: raw-transcript
title: "The BIG Problem with MCP Servers (and the Solution!)"
youtube_id: 1_z3h2r93OY
url: https://www.youtube.com/watch?v=1_z3h2r93OY
slug: the-big-problem-with-mcp-servers-and-the-solution
published: 2025-11-09
duration: "0:10:22"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Over the last year, MCP has really become the go-to way for us to connect our agents to our tools and data. But as the protocol has gained popularity, it's also become more and more obvious that we have a major flaw with the protocol. It is all about token consumption and context rot, which are very much hot topics right now. And Enthropic admitted to this problem themselves, and they literally built the protocol. So they published this blog post recently covering the main issue with MCP and

**[0:00:30]** then their proposed solution to build more efficient agents. That's what I want to cover with you today in a very practical way. So this video is going to be a quick breakdown. I'm going to do it very clearly for you. I want to cover the problem we have with MCP with a full example. Then we'll get into the proposed solution. And I really think that this is powerful stuff. And then I know I'm being a little cheeky here hiding this, but I want to cover the final question. Is this the end of MCP

**[0:00:58]** as we know it? The problem with MCP servers is that they are incredibly token inefficient and rigid. And starting with the token inefficiency. We've got a really nice diagram in the anthropic article that I want to show you quick. So every single tool definition like the when and the Y for the tool and the parameters and also every single time we leverage the tool both are going to fill our context window. And so the more capabilities we give our agent the more we are going to

**[0:01:25]** bloat its context. And I've got a scary example just to show you how quickly this can get seriously out of hand. Cuz right here I just have five very standard MCP servers for AI coding. And I've used these all a lot in the past, but I would never, and I repeat, never use them all in the same session with my coding assistant because they each take thousands of tokens just to describe their capabilities to the AI agent. And so these tokens are consumed at the start of a conversation before we even

**[0:01:55]** send our first message. And sure, modern LLMs can handle this many tokens. But just because the LLM can fit the tokens doesn't mean it can handle it gracefully. If we try to give this many tools to our coding assistant right out the gate, we're going to completely overwhelm it and make it feel like we're back in the stone age in 2022 running our LLMs with GPT 3.5. And I've been there. I've built agents back then. I know how they could only handle a couple of tools back then. And so, it's a lot

**[0:02:23]** better now, but still, this is way too much. And I'll prove to you that it really is this bad. It's actually bonkers. So, I'll go to my coding assistant. I have all the same servers connected. I'll go inside of Cloud Code now. And then I'll run slashcontext to show me how many tokens each of my capabilities are taking. And wow, look at this. We have a ton of tools here. And overall, the MCP tools alone are taking 97,000 tokens. That is 48% of the context available for Claude Sonnet 4.5. And

**[0:02:53]** even if you have an LLM that can take 1 million or 2 million tokens, this is still just going to overwhelm with capabilities. Okay, so that really sucks. So the big question now is what is the solution to this? What if I do want all these capabilities given to my agent at the exact same time? Well, what we need to consider here is that we need a way to give these capabilities to our agent but only when they need to leverage them. So we want more of a real time discovery of the tools that are

**[0:03:19]** available only loading in the content and the context of the specific capabilities when we want to use them. So real time discovery or even creating the capabilities on the fly. This is code execution what Anthropic talks about a lot in the article. We'll come back to this in a second. So, first think about this. Most MCP servers are really just API wrappers for agents. Like with my open source project archon, just to give you an example, but a lot of them work like this is we have all

**[0:03:47]** these API endpoints to work with our knowledge and our projects and our tasks. And the code for the MCP server itself, there's not actually much to it because it's just an instruction set to the agent. Here's a couple of functions you can call to interact with our API endpoints. And so the big question here, let me zoom in on this. What if we just allowed the agent to write the code directly to interact with the Archon API endpoints instead of having the MCP

**[0:04:11]** server as the middleman that is loading dozens of tools up front. So, not only is this going to be way less tokens, but it's also going to be a lot more flexible because the agent gets to decide how to interact with our API instead of the MCP kind of forcing these specific tools. Plus, the agent can save the generated code to reuse later. So, at first, the AI agent will generate the scripts on demand and then maybe even some instructions for how to use those

**[0:04:37]** going forward. This is very related to Claude skills that we'll talk about in a second. And then when the agent needs to leverage the capabilities later, it'll load the instruction set plus the code context and execute it. But it's only going to be doing this when it needs to. And so going back to our Enthropic article, instead of all the MCP servers being loaded right up front, we have something kind of like this. It's a folder that the agent can search through in real time, discovering the

**[0:05:02]** capabilities as it needs. Like maybe it decides I should be doing something with Google Drive now. And so it'll look at this highle file to see the capabilities there. And then maybe it'll load the code specifically to get a document. So it can look kind of something like this. The sort of thing that would be loaded right away with MCP, but now we're only calling this once we want to do things related to Google Drive. That's all just based off of the user query. So the user

**[0:05:24]** says something related to Google Drive. Then we know we should load in these capabilities. and having agents write code to create their capabilities, reusing code, like that all makes a lot of sense because the LLMs these days are really good at writing code and developers should take advantage of this to build agents that interact with MCP servers or just API endpoints a lot more efficiently. And when we think about giving our agent the ability to execute code and reuse code, it's not really

**[0:05:52]** obvious how to do that. I mean, that's one of the benefits of MCP. It's just really easy to plug the MCP servers in and instantly give these new capabilities to our agents. But that is where agent skills comes in. Enthropic released this pretty recently and it does embody the solution that we have to the MCP problem because it gives us and our AI agents the ability to generate these scripts to do things like interact with our API endpoints and generate instructions for how to use these

**[0:06:19]** scripts or create code on the fly. So code execution at its finest. And this is fantastic because the description for this skill, this little bit of text right here is the only thing that is given to our AI agent at the start of a conversation. So instead of thousands of tokens defining tools and MCP instructions, we just have a couple of sentences here. And then when the agent decides it wants to leverage the skill, then we load the full instruction set and the code that we want to execute.

**[0:06:46]** And it doesn't even have to load all the code, by the way. It can't just describe like here are the functions you can call and here's how you call them. And so this is very very token efficient like 2 to 3% of the token usage compared to MCP at the start of a conversation. So let me know in the comments if you want me to cover cla skills in a dedicated video. There is so much to go over here and it's so powerful and right now this is just in the anthropic ecosystem. But

**[0:07:11]** I think it's going to go way beyond that very quickly here just like MCP did because we can have dozens of skills given to our agents at the same time since it's a fraction of the token cost upfront compared to MCP. And I don't know if you noticed this yet, but the skill that I'm using here as an example is the one for Archon, my very own open- source project. So, I took the Archon MCP server, transformed it into a skill to prove to myself and to you that we

**[0:07:37]** have all the same functionality, and now it is way more token efficient and honestly flexible because the coding assistant can now generate its own code to interact with the Archon API. It is fantastic. And so now we can pair this with a ton of other different skills and not worry about getting to that 90,000 tokens up front. Oh, and by the way, I'll link to this in the description with the Archon skill. I did a full demonstration of this in the Dynamus community and so I I proved it out like

**[0:08:02]** this works as well as the MCP server and it takes just a couple of hundred tokens up front so you can try this out for yourself if you want. So the last question you're probably asking yourself is is this the end of MCP? I mean the picture that I laid out here is looking pretty grim. But my short answer is no. This is definitely not the end. And the reason for this is MCP is actually pretty great because what you see is what you get. And what I mean by that is

**[0:08:25]** when I build an MCP server, I define the tools that people leverage when they're using my service through MCP. And so I have a lot more control and predictability. So code execution is flexible and very efficient like we saw, but it's also risky and complicated. There's a lot of security considerations. We have to think about a code sandbox environment that also makes it more complicated. And so there is really a big trade-off here between control and flexibility. And so for MCP

**[0:08:53]** servers, we get to control how the agent leverages the tools because it's not generating arbitrary code. More control for things like credential setup, like how do you even manage environment variables in skills? I don't think that's figured out yet. And there's less risk of capabilities being missed. So if you're totally overwhelmed LLM, yes, it will still miss capabilities, but in general, since everything is given up front, there is no search and discovery

**[0:09:16]** like with code execution or skills, and so it'll miss things less. But then for this side of the coin, we got the flexibility here. So we can have dozens of capabilities available to our agent because we're not overwhelming with context. We have our instructions for how we reuse code or generate code and the capabilities like the scripts that we want to reuse loaded only when we need it. And then also our agent can also define workflows that are fit for the task like combining different API

**[0:09:41]** calls together. It's very flexible in that way. So when you're thinking about adding capabilities to your agents, I want you to think about this trade-off. But honestly, I think flexibility is going to win over control more and more over time because LLMs keep getting more powerful. So, we trust them more with code execution, searching, and discovering capabilities. And AI agents are meant to be autonomous after all. So, we're just making them more autonomous by upping the flexibility.

**[0:10:07]** And so, that's everything that I have for you here with the problem with MCP and the solution with skills and code execution. If you appreciated this video and you're looking forward to more things on AI agents and AI coding, I would really appreciate a like and a subscribe.
