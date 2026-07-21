---
type: raw-transcript
title: "This Completely Changes the Way We Build Production AI Agents (Vercel Eve)"
youtube_id: m8VC2SV2igM
url: https://www.youtube.com/watch?v=m8VC2SV2igM
slug: this-completely-changes-the-way-we-build-production-ai-agents-vercel-eve
published: 2026-07-15
duration: "0:16:25"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A new open-source AI agent framework was just released by Vercel called Eve. And man, this is worth a look. They're calling it a file system first framework, which is fascinating to me. I haven't seen something like this before. Because traditionally, when you make an AI agent more file system based, it's

**[0:00:17]** more for a personal agent or a second brain. It's not the kind of agent that you're going to deploy to a production environment to be used by thousands or millions of users like your customers. But Eve makes that possible. And so, you get the ease and the flexibility that

**[0:00:31]** comes with file system based agents, but you also have that strong foundation for production-grade reliability when it comes time to deploy your agent. And that's the kind of thing you usually don't have when your agent looks something like this. If you've built personal agents in the past, you're

**[0:00:47]** familiar with this kind of structure, where really your entire AI agent is just a collection of files in a single folder, right? And that's the idea with Eve is your AI agent is just a folder. That's what makes it so easy to build, making everything composable. And so,

**[0:01:02]** within your folder, you have your instructions. That's your system prompt, your global rules. You have your agent definition, where you're defining the model that you want to use, your skills, all the capabilities you want to give your agent, your tools, your sandbox for reliable code execution, your channels,

**[0:01:19]** so you can connect your agent to something like Slack or Discord, your connections, which includes your MCP servers, and your sub-agents, and then also your schedules, so you can run the agent on a scheduled basis for it to do things autonomously. And so, pretty much all the core primitives that we see with

**[0:01:36]** agents these days, you define them each in their own individual folder, and then you have the main parent folder that wraps everything together. That's what makes it so composable and easy to build. Now, the biggest reason that this caught my eye in the first place is because I'm seeing a lot of

**[0:01:51]** organizations build this kind of thing for themselves internally. And so, they have their own sort of structure, right? Like you have the agent at the top level and then they have their way of defining the model and packaging up the skills and bringing in the system prompt. And

**[0:02:05]** so what Eve gives us here is a standard, right? A way to define this in the most simplest way possible. And then they also take care of a lot of the plumbing under the hood. Things you wouldn't really think you would have to take care of, but when it comes [snorts] to like

**[0:02:19]** building this kind of agent as a folder architecture, there's a lot that has to happen to get it to the point where the agent is really hooked up into the skills and hooks and everything that you define. And so really this compilation step is the most impressive part of Eve.

**[0:02:35]** Because when you're creating your skills and sub-agents and everything in the folders here, you don't have to import or link anything together yourself. Like looking at the main TypeScript file for an agent, which I'll show you an example of this in a little bit, there's nothing that has to import or call out the

**[0:02:50]** specific things that we have in all of the other folders. That's the compilation step. When you run your agent and when you deploy it, Eve takes care of traversing through your single folder, finding all your skills and MCP servers and things like that, and then creating a single manifest that has

**[0:03:07]** everything hooked together. So you essentially have your output here of a compiled agent that takes care of all the connections so that it's as easy as possible for you to build the agent. And this is very similar to how primitives like skills work in coding agents like Claude code. Like in Claude code, as

**[0:03:22]** long as you dump a skill.md file in a folder within skills, Claude code magically understands it and you can now invoke that skill with a slash command. Same kind of thing here, but also Eve takes things a lot further than coding agents when it comes to production deployments and reliability. And this is

**[0:03:41]** what really makes it so that Eve agents can scale all the way to production and be reliable enough because we're relying on a lot of the infrastructure that Vercel gives us. I mean, Vercel has always been one of my favorite platforms to deploy things. And it makes sense

**[0:03:54]** that they're pushing for Vercel here. I mean, Vercel made this open-source framework, so yeah, fair enough. They want you to deploy to Vercel as well. And so, first of all, we have durable sessions. So, every session is a checkpointed workflow that survives crashes and redeploys. So, essentially, under the hood, every single turn and

**[0:04:11]** tool call, all of that is stored so that whenever there's any kind of breaking point, you can resume from that naturally. They also offer isolated sandboxing for code execution. So, your agent can write and execute code, but do it in a secure way. And then we have human in the loop. So, pausing at risky

**[0:04:27]** steps for approval. So, that way we can have our agent do real things, but not uh just have that risk of it running wild. And then they also have evals as a deploy gate. So, evals is another thing you can just have a folder for in your agent. And so, you can test certain

**[0:04:41]** behavior of your agent, making sure that you get green check marks across the board before you deploy that update of your agent to production. And then, of course, Vercel can also handle the entire infrastructure of hosting your agent, scaling that to thousands or millions of users. So, you also don't

**[0:04:54]** have to worry about hooking into some other infrastructure or hosting it on your own machine. And last but not least, we also have very easy connections into other platforms, like our own custom UI through an API, something like Slack. I'll show you an example of that in a little bit. But

**[0:05:10]** before I get into the agent I want to demo for you and uh showing you how to really easily build these Eve agents yourself. There's one more thing I want to cover. I just want to say that I absolutely love the standard that Eve is giving us here for file system-based

**[0:05:25]** agents. The structure for our agent and how we compile it. If you've watched my content in the past, you know that I'm a very big fan of standards, like MCP and A2A and OKF, all these three-letter acronyms. It's standards are what move the industry forward. Because when everyone has the same approach, we're

**[0:05:43]** able to learn from each other and build on top of each other. That's what moves the industry forward, especially open-source AI. And Eve being open-source is why it fits directly into my ethos. And the other thing I always say with these standards is I don't know if Eve is going to be the standard for

**[0:05:59]** file system-based agents in the future, but they are setting a precedent here. And whatever that standard is going to look like in the end, it's going to be something like this. In fact, you can sort of think of it like Eve is the standard for how we structure our agent,

**[0:06:13]** and then OKF is the standard for how we structure the knowledge bases that we attach the agents to. So, I think there's also a really cool combination that we can do here with Eve plus OKF. Because one thing I want to be very clear on here is when I say Eve can

**[0:06:25]** scale file system-based agents to production, I'm not talking about scaling knowledge bases of markdown, like LLM wikis for example. I've said in the past that they don't necessarily scale, especially once you get to tens of thousands of documents. And so, yeah, the knowledge base is a separate thing.

**[0:06:40]** This is just talking about scaling the core primitives of an agent. So, the agent connected to things like the skills and MCP servers. All right, so the question you might have at this point is how do we actually go about building Eve agents? Well, luckily for you, it's as straightforward as it

**[0:06:57]** possibly can be because Vercel ships a plugin for you to bring into your coding agents like Claude Code to make it incredibly easy to both build and deploy these agents. So, we have the Vercel plugin. I use this to build everything in the agent that I'll show you in a

**[0:07:12]** little bit. We can see we have the Vercel MCP for deploying connected here, so it makes it really easy to bring our agent into production. And then if I do /skills, we can see that as a part of the plugin, we also have all these Vercel skills, including Vercel Eve. And

**[0:07:26]** so, thanks to this skill, our coding agent like Claude Code knows exactly the structure of our agent, how we build our channels and incorporate our skills, and build out the schedules and the sandbox environment. So, you don't have to be a master at Eve and the whole structure

**[0:07:42]** here in order to build fully production ready agents. And I'll also link to this article in the description that has the instructions for installing the plugin, the exact command for you to copy and paste. And so it's just a single command you have to run in a coding agent like

**[0:07:56]** Claude Code or Cursor to bring in the whole suite of skills and the MCP server that comes with the plugin. And the other thing that I'll link to in the description is also the Eve analyst agent. This is the demo that I want to get into with you now to really make

**[0:08:09]** things concrete. So I built out a full agent that takes advantage of all the different capabilities that we have with Eve. And so I just want to walk you through this at a high level and even show you what it looks like to deploy and talk to the agent in Slack. So here

**[0:08:21]** is my cloned copy of the Eve analyst agent. And again, I use Claude Code with the plugin to build everything here. And so your agent starts with a simple agent.ts file. So within the agent folder, this is everything I have for my Eve agent, it is all just a collection

**[0:08:37]** of markdown and TypeScript. And don't worry, all the TypeScript is really simple. And so when we define our agent, we really just have to specify the model. And then within our environment variables, we'd set the Anthropic API key. And yet another thing that your coding agent can help walk you through.

**[0:08:52]** And so once you have the agent.ts, everything else is optional. I mean, obviously to make a truly useful agent, we have to add in other things like skills and tools, but right now we could run this agent right out of the gate. And so I'll do control J in VS Code to

**[0:09:06]** open up a another terminal here. And once you have the agent.ts, all you have to do to run it is the Eve command. And you can also have your coding agent run this and test out the agent itself as it's checking its own work. And so there we go. We have the agent running

**[0:09:21]** locally. I can say hi and I have this connected to Claude Sonnet 5 through the Anthropic API. And there we go. We get our answers streamed out to us. So that's how easy it is to start with an agent. And then it's not that much more difficult to start adding in all of the

**[0:09:33]** capabilities. So for For let's take a look at the skills. And so, we have a revenue rule skill. And so, we have a description just like you give to your coding agents at the start of a conversation that tells it what the capability is. So, load this before

**[0:09:46]** answering any revenue, sales, or growth questions. And then, for the sake of demo, I mean, everything is pretty simple that I've built here. We just have a couple of rules just to enhance the output, make sure the output is repeatable when the agent answers these kinds of questions. We have our channels

**[0:10:00]** like this is Eve, so we can talk to it locally like we just saw. We have the Slack one, and again, you can use your coding agent to help you set up the credentials for the agent. We have a subagent, an investigator. So, when we have a, you know, why did this metric

**[0:10:13]** change kind of question, and it's going to take more tokens, we want to dispatch that to a worker. We got a subagent for that. We have our core system prompt, you know, you are Eve analyst, careful data analyst, etc. We have that in our instructions.md. I mean, I don't need to

**[0:10:26]** go through everything here like the sandboxing, the evals. You get the point, you can explore those things if you want, but the cool thing to see here is that it is just a collection of markdown and title script, so incredibly easy. And then, once we want to run this

**[0:10:38]** to test things locally, we go back to our terminal here. We run that Eve command, and now I can ask it some questions that need to rely on some of the capabilities that we built in. And again, these capabilities, like I just drop the skill in the skills folder,

**[0:10:50]** drop the subagent in the subagents folder. I don't have to do any connection to the agents.ts. So, the entire time I'm adding these capabilities, this core file, that's sort of like the entry point to the agent, like I have to build nothing else into this. That's way different than

**[0:11:04]** what you see in other AI agent frameworks. And so, let's see this in action. So, back over here, let's paste in a question. What tables are in the warehouse, and how many rows does each have? So, this doesn't need a subagent or a skill, but it's going to use some

**[0:11:17]** of the tools that we gave it here to interact with our database. So, I guess this is a basic question, so just a single tool call, but it listed tables. Nice and fast, got exactly the information we needed. Boom. And each one of these tools here is just a simple

**[0:11:30]** TypeScript file. Like this is the tool that we just ran to list the contents of our table. So, it's really just a single operation to our database. We're using Zod here for typing to make it so that the inputs the agent gives to the function is reliable in what it really

**[0:11:44]** needs. I love how simple this is. And again, there's no hooking up into the agent here. We just define it as a function in the tools folder, and it's loaded automatically when we compile the agent with the Eve command or the deploy command we'll cover in a bit. And so,

**[0:11:57]** let me ask another question now. This one is going to have to leverage our skill because we're asking a revenue-based question. And so, sure enough, it loads the skill, the instructions for how we want to receive our answer, and then it's making the tool calls here to get the actual data.

**[0:12:11]** And then, it's running some SQL, and then we'll get the answer in just a second here. All right, so it takes a little bit because it does have to do a quite a bit of information processing here, but we can see that we have the final number, and it's giving us

**[0:12:22]** everything in the exact format that we specified in our skill. Awesome. And so, I did build a pretty simple agent for the sake of demo, but let's assume that we're happy with the capabilities we've hooked into our agent, and we're ready to deploy it. All you have to do, again,

**[0:12:35]** thanks to the Vercel plugin, is we just have to tell our agent, "Deploy this Eve agent." That's it. Now, it's going to take care of everything using the MCP server. And by the way, as it's running, let me open up a new Claude code instance cuz I also just want to show

**[0:12:50]** you how easy it is to build an agent from scratch. This is literally what I did to build the demo here. Take a look at this prompt. I just said, "Scaffold a new Eve agent called hello agent." just give it a name, you tell it to use Eve,

**[0:13:02]** so it knows to leverage the skill, and that is all it takes. And then, you can also describe, you know, any kind of sub-agents or skills you'd want it to build. It has full understanding of that, so it'll create everything. And so, I'm not exaggerating when I say that

**[0:13:15]** it could not be easier. All right, and then going back to our coding agent, our deployment is complete, and it even ran a smoke test to make sure we are good to go. You could also run the evals at this point, just telling the agent to run the

**[0:13:26]** eval suite. So, it's yet another thing in the skill that it can leverage to run that for you. And so at this point, if you have your credentials set up for a platform like Slack, you can immediately start talking to it. And if there's any other setup that you need to finish,

**[0:13:40]** just have the agent guide you through that. And so let me show you what it looks like now talking to the agent in Slack. So I will say that there are a good number of steps to get your Slack app created and get everything hooked up. I had my Claude code walk me through

**[0:13:53]** it, but there are good number of manual things you have to do. But anyway, once you have it set up, then you can just do @eveanalyst, and I can say hi, for example. And you'll see immediately that it says that the analyst is thinking, the Eve agent is thinking, and then in a

**[0:14:06]** little bit we'll see our reply in a thread. There we go. Boom, clicking to this and awesome. And so we can also continue the conversation here, like I can say, you know, Eve analyst, what did I just say? Just to prove that we have the short-term memory within a thread,

**[0:14:19]** and we can also have many conversations going in parallel because we have things scaled up in Vercel. We can have thousands of people interacting with this agent at the same time. So we got the conversation history, and then let me also show you one more thing here. I'll show you the human in the loop. And

**[0:14:34]** so this is kind of a silly prompt because I'm telling it explicitly to run a SQL query. You're never going to talk to an agent like this for real. But just so I can make sure that we trick the human approval here. I'm asking it to run an operation that's considered risky

**[0:14:47]** because we're doing something that could be a massive select. And so I'll click into this here and take a look at that. I have to approve or deny. So we have the integration right in Slack where we have the buttons that are open here. So I will click allow, and then it'll run

**[0:14:59]** the query and give me the final answer. And there we go. We got our answer, nice and simple. Only took a couple of seconds. And so this is one of the most important things for reliability, bringing an agent into production, especially if it's used more by an internal team in a platform like Slack.

**[0:15:13]** You got to have those human approvals for these kinds of actions. Now, of course, we could just make it so the agent can't do any of these things in the first place, but then it's just going to be less useful. The good balance here is given more power, but

**[0:15:25]** make it so you have to approve certain things. And Eve makes that so easy to set up. So, that's everything that I have to cover for Eve, the new framework and standard for file-system-based agents. So, I hope that you found this interesting, even just to think about how we are shifting the standard for

**[0:15:39]** building AI agents. Getting to the point now where we have a single folder that's just a collection of organized markdown and TypeScript. I love it. If you would have told me even half a year ago that agents are coming to this, I would have told you you're crazy. But here we are,

**[0:15:54]** and I'm loving it because it's we're not losing any power of production-grade agents, but it's a lot simpler to get there now. And so, I also want to say that I worked with Vercel on this video just to make sure that I framed everything right for you. So, thanks to

**[0:16:06]** them for working with me on that. I wanted to reach out to them because I really think this framework is incredible. So, I'll have a link to it in the description. So, with that, if you appreciate this video, you're looking forward to more things on building agents and AI coding, I would

**[0:16:19]** really appreciate a like and a subscribe. And with that, I will see you in the next video.
