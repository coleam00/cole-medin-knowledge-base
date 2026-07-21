---
type: raw-transcript
title: "Harness Engineering: What Separates Top Agentic Engineers Right Now"
youtube_id: ulNsa0sD8N0
url: https://www.youtube.com/watch?v=ulNsa0sD8N0
slug: harness-engineering-what-separates-top-agentic-engineers-right-now
published: 2026-05-27
duration: "0:17:10"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A term that's popping up more and more in the AI space right now is harness engineering. It's the next big thing for this year, just like context engineering was for last year, and it is really important. But just like context engineering, it's starting to turn into this buzzword that people are throwing

**[0:00:17]** around without really knowing what it means. And so that begs the question, is this skill or even mindset, like I'll get into in a little bit, worth learning or adopting? And the answer is yes. And so I want to get into that with you today, helping you understand what

**[0:00:32]** harness engineering is. There are a couple of layers to it that are really worth knowing. And so I'm going to break this down nice and simple for you in less than 15 minutes. And of course, like usual, I've got some examples and demos to really make it concrete. All

**[0:00:46]** right, so let's get right into it. Harness engineering is all about building the wrapper around the model. So any agent is the combination of the underlying large language model like GPT or claude and then the wrapper around it that gives it the context and defines your processes. And so I'm mostly going

**[0:01:03]** to be focusing on AI coding assistance for this video. But really this idea of harness engineering can be extrapolated out to any agent that you build for anything. And there are really two parts of harness engineering. we have within an individual AI coding assistant session. And then we have really the

**[0:01:21]** real evolution here that I'm more focused on right now. This is combining multiple coding agent sessions in a larger workflow to handle a larger task. And so we'll get there, but I want to start more foundational here. And one really important thing to understand is that this first idea of harness

**[0:01:38]** engineering within a single session, a lot of the ideas here are very similar to context engineering. This is a direct evolution of context engineering. How do we give the right ecosystem of context to our coding agent? But there are some important differences here that I want to key in on. But first of all, I think

**[0:01:56]** this diagram explains it really well. We start with the underlying large language model. This is the reasoning for our agent. And then the first wrapper around it is not something you build yourself. It's actually the tool that you use, the coding agent that you choose. And so Claude Code, Codeex, Pi, you name the

**[0:02:14]** millions of coding agents out there. All of them are actually harnesses that a company has engineered around their model. And so this might not feel like harness engineering because you're not defining anything, but you're picking the harness when you choose the tool. Some people think Claude Code is the

**[0:02:29]** best harness for coding. Some people think Codeex is. There's a lot of debate right now. But what's even more important than the coding agent you pick is the AI layer. This is the ultimate wrapper around any coding agent session. And this is what you get to actually build. And so when we think about what

**[0:02:46]** goes into the AI layer, it's really defining all of our context and processes for our coding agents. So our global rules, our skills and MCP servers, all the capabilities we give, codebased searching like LSP or knowledge graphs, our hooks, and our sub aents. really like these six components

**[0:03:05]** that are pretty much built into every single AI coding assistant now makes up your AI layer. So no matter how you want to inject your process or your rules, you're going to do it through one of these six things. So there are a couple of articles I really want to lean into

**[0:03:19]** here to help you understand harness engineering. I'll link to them in the description. This first one has an analogy that I want to zoom in on here. I love this. So on the left hand side we have a representation of what the model can do by itself like claude or GPT. And

**[0:03:33]** spoiler it's not that much. We take for granted all of the capabilities that AI coding assistants like cloud code and codecs give to the model out of the box. An LLM by itself. It doesn't have any way to access a file system or get or run any commands. That's everything that

**[0:03:48]** comes with that first harness layer built into the tools that we download and use out of the box. And so that's what these top bridges represent here. It's all of the capabilities that these tools give to the model to make it so it can really act as an AI coding

**[0:04:02]** assistant. Right? It's the capabilities plus the system prompt built into these tools. And then as we get to the lower bridges here, this is where we start to get into that higher level AI layer where we get to define things like the MCP servers we use, the skills that we

**[0:04:18]** build or incorporate, rules, things like that. even going down to Ralph loops like we'll talk about towards the end of this video when we get into stringing multiple coding agent sessions together. The ultimate kind of harness engineering. So stay tuned for that. But the point here is that each of these

**[0:04:32]** bridges are tools that allow the large language model to function and act as an AI coding assistant. All right, cool. So with that definition, I now want to address the elephant in the room. The question you might be asking yourself is, Cole, isn't a lot of this here just

**[0:04:48]** context engineering? like I thought we were covering this in 2025 and the answer is actually yes to an extent and that's why I think that harness engineering is becoming such a buzzword right now most people don't really understand how this is truly an evolution from context engineering that's what I want to argue with you

**[0:05:06]** right now and so there are two important distinctions so first of all most of the harness around the model like this article outlines it is just context engineering your context injection your actions through tools and MCPs, persistence, observability. The one thing that really is different is control. Like Ralph loops, orchestrating

**[0:05:26]** different coding agent sessions and sub aents. I think that is a true evolution from sub agents. And so we'll talk about that next. But the other really important distinction that this article outlines is the skill issue reframe. So I alluded to at the start of the video the fact that hardness engineering is

**[0:05:43]** not just a skill, it's also sort of a a mindset, right? A a reframe. So, the author here says, "There's a pattern I watch engineers fall into. The agent does something dumb, the engineer blames the model, and the blame gets filed under wait for the next version." As in,

**[0:05:58]** you know, Claude screws up here. Well, we better wait for Opus 5 or GPT messes up. Let's wait for GPT6. And, you know, personally, I see this all the time as well. I'm also tempted to think this myself, and you probably are as well. But the harness engineering mindset

**[0:06:13]** rejects that default. And by the way, I call this system evolution. It's very in line with something that I've been focusing on a lot recently. So here's what he says. The failure is usually legible. The agent didn't know about a convention, so you add it to agents.mmd. Or the agent ran a destructive command,

**[0:06:29]** so you add a hook that blocks it. Basically, the idea here is every mistake becomes a rule. Or the way I like to put it is every mistake becomes an opportunity to improve your harness. improving the security through your hooks, your processes through updating your skills, anything in your harness so

**[0:06:47]** that the next coding agent session that issue you encountered is less likely to come up. And that is super powerful. That system evolution means that you are taking ownership and improving the performance of your coding agent over time with the AI layer that you control over the coding assistant that you

**[0:07:04]** chose. And so really harness engineering is all about claiming that agency, taking ownership of your system so that when something goes wrong, you're not just blaming your AI coding assistant and feeling helpless because things will come up just like working with human developers. There are going to be

**[0:07:19]** issues. But we need to make sure that we have a way to learn from that and not just be at the mercies of the next session not encountering that problem again. We want to be the human steering the system feeding forward. So the initial generation we have our

**[0:07:33]** principles and other kinds of context we feed in and then we have our sensors for feedback our hooks our review agents the skills that we give it for that selfcorrection evolving our AI layer over time the sponsor of today's video is Google Cloud specifically their new agent CLI and I'm excited for this

**[0:07:52]** because nowadays it's optimal to build your agents with other agents right using your AI coding assistants like cloud code and codeex now the easy part is getting the idea for an agent, but actually building it out and deploying it to production, that is a different beast. But Google has made this so

**[0:08:10]** incredibly easy now with their agent CLI. It's a collection of skills that I can bring into my coding agent that give it full clear instructions on how to build agents with the Google agent SDK and even deploy them to production and monitor them. And so right here in my

**[0:08:24]** cloud code, for example, I can say use the agent CLI to build a research agent that searches the web. Obviously a simple example, but it's going to use the instructions really help you build any agent that you want. Then with the help of the skills, your coding agent

**[0:08:38]** will create all of the code. It's oneshotted a lot of different tests that I've given it here. And then we also have our local development environment. We can spin up the agent here so that we can test everything locally with a full chat application before we deploy our

**[0:08:51]** agent. And then when you're ready to take your agent to production, it is a single command to deploy your Google agent SDK agent to the Google Cloud. super easy and your agent gets its own identity in the cloud. You have the playground here to test it live and you

**[0:09:05]** have traces full observability. So everything you need for a production deployment, but it's not extremely difficult to get all this set up like it used to be. And the best part is the agent CLI is free and open- source. You can take these skills, bring it into any

**[0:09:18]** coding agent, and see how easy it is right now to build any AI agent. I'll have a link in the description. I'd highly recommend checking it out. So I also have this companion repo for our video giving you a super concrete idea of what an AI layer can look like. And

**[0:09:32]** this is a really good representation everything here of the AI layer that I'll bring into and evolve in each of my code bases. So I want to cover this quick before we get into the last evolution of harness engineering the really powerful stuff building workflows where we are bringing together and

**[0:09:47]** orchestrating many coding agent sessions and I have examples for that like with the Ralph loop in this repo as well. And so I did promise that this video is going to be shorter. So I'm not going to dive extremely deep into each one of the components of the AI layer, but I do

**[0:10:01]** have a video that I'll link to right here where I cover in more detail the rules and skills and LSP and hooks, each one of the components. I want to stay just really high level, give you some golden nuggets here, and then you can of course just give this repo to your

**[0:10:14]** coding agent and have it help you implement things and understand everything here. So really the foundation of your AI layer is all of the rules, the constraints and conventions that you want your coding agent to follow, your patterns. And so that's your global rules and any other kinds of on demand context that you have

**[0:10:30]** as markdown confluence documents, that kind of thing. And then your skills, these are the workflows that you have for your coding agent. Like here's how you wanted to plan, implement, and validate. And I have a separate skill for each because what I really want to do and I highly highly recommend this is

**[0:10:46]** you want to do your planning, implementation, and validation all in separate coding agent sessions to keep each one of them token efficient and focused. And so each one of these skills is going to output some kind of artifact so you can use it as a handoff to the

**[0:11:00]** next session. And so this is kind of getting into stringing coding agent sessions together, but we're still talking about doing this manually, right? like you'll run the plan and you'll create the plan with the coding agent with one skill and then you'll take this markdown and then you'll give

**[0:11:15]** it to the next coding agent session for the implement skill, right? You go through that systematically yourself. And so we'll talk about in a little bit how we can really bring all that together. And then as far as hooks go, these are honestly pretty underused. I love using hooks for a few different

**[0:11:30]** things. First of all, for security. So a pre-tool use hook. Basically, this is a piece of code that's going to trigger before the coding agent executes any tool call like writing out to a file, running any kind of command. And so, this is where we can build in security

**[0:11:43]** things like not reading files because we really don't want that in the LLM's context or removing directories in a very destructive way, for example. I also like having some kind of stop validation hook. So when the coding agent says it's done with the implementation, I want to deterministically run a set of tests

**[0:12:02]** like are the unit tests, the linting, the type checking, is all that really passing? Cuz if it's not, I want to force the coding agent to iterate on it until it is. And that's what this hook does. And then last but not least, just running a quick lint after every single

**[0:12:15]** file edit is really good just to keep your code base nice and clean, which also helps make your coding agents more reliable in the future. So there you go. Just a couple of golden nuggets for the AI layer that we have here. And I even have instructions in the readme for just

**[0:12:28]** running a super basic pit. This is the foundational approach to agentic engineering. So you plan with the plan skill just sending in the feature that you want. You iterate on the plan. You produce that markdown document that you then hand off to the implement skill in a separate coding agent session. You

**[0:12:43]** also have your validation strategy for the agent to check its own work in the markdown as well. So feel free to try that out for yourself. But now finally I want to get to the peak evolution of harness engineering. So I'm going to jump back to the diagram here. Let's

**[0:12:57]** talk about orchestrating coding agent sessions. This is when we can really scale the amount of work that we get done with coding agents. So the main idea here is you don't just want to take a massive task or PRD and hand it to a single coding agent session. It's not

**[0:13:13]** going to be token efficient and the underlying large language model in the harness is going to be completely overwhelmed. It does not matter how good the AI layer is that you created here with things like your skills and rules. If you send too much into the LLM at

**[0:13:28]** once, it is going to fall flat on its face. And so what we're doing here, orchestrating many coding agent sessions together, is we're giving each coding agent a very focused task. And so these can be sub agents as well, but like you'll see in the real loop, it's actual

**[0:13:42]** coding agent sessions that are handing things off to each other. So we can explore the implementation that comes in from a user requirement. Have one agent that writes the plan. Send that plan artifact into an implementation. And then for example, this is just an example harness, but we could have many

**[0:13:58]** code review agents running in parallel. This one focuses on security. This one correctness of the implementation. And this one making sure it's as simple as it can be. And then if everything passes, you create the pull request. Otherwise, you would iterate and keep working on the implementation. And you

**[0:14:13]** can do all this manually like I was talking about earlier. We can go to cloud code once and create the plan and then open up another cloud code and do the implementation. But the real power with harness engineering here is we can automate all of this. We can create a

**[0:14:27]** system that automatically hooks together all these coding agent sessions with the handoff documents and creating the poll requests and everything like that. And that's what the RA loop does. So let's go back to our example repo here. I want to show you what this actually looks like. So the Ralph loop is just one

**[0:14:42]** example of an agent harness. But Jeffrey Huntley, the creator of Ralph, he really is one of the pioneers here. This is one of the first examples showing in a very basic sense how we can automate stringing together many instances of cloud code, codecs. I mean you could do

**[0:14:57]** this with any coding assistant because basically all it is, I'm not going to get too technical here, but I just want to show you a little bit is we have a simple script. This can be a Python script, it can be a bash script. I'm not going to go into the code here, but

**[0:15:09]** essentially you give it a larger scope of work, like a massive PRD, and it's going to be responsible for splitting that up into individual tasks and then running coding agent sessions to handle them one at a time until everything is done. And so you give it a prompt. This

**[0:15:24]** is the user input here, like these are the different items that I want to build in the spec. And then it's going to produce a plan here. This is the fix plan. So like this is what it's going to do in iteration one of the loop, iteration two, iteration three. It's

**[0:15:36]** going to keep working and kind of like build up a log as the different cloud code sessions here are running. And then when it decides it's done, it's going to produce some kind of indicator of that. Like here I'm using a done.ext. And so this is where it decides like all right,

**[0:15:49]** all eight spec items from the original prompt are done. We are satisfied. We can now exit the loop. And that's the only condition. The only way that we can exit the main while loop here is if we have this done.ext text and the coding agent is confident that the

**[0:16:03]** implementation is done and all the validation is there. And so just trying to show you real loop to give you one example of a harness. But you can see the idea here of we are using many coding agent sessions to keep each one very very focused but also we're

**[0:16:18]** automating it so we don't have to babysit our coding agent as we're handling these longer tasks. This really is the future of agentic engineering. Building these harnesses to handle larger scopes of work as the models and the underlying tools are getting more powerful. Like this is the way. And so

**[0:16:35]** lean into this here. I mean there's so many resources out there for harness engineering. And then there's Archon, my open-source harness builder. Free to use. This is the easiest way to get started with Agentic Engineering. Building your own harnesses like the Ral Flute, but more custom to you, your

**[0:16:50]** exact process and software development life cycle. So, I'd highly recommend checking this out. Otherwise, I hope this video was helpful for you in general, just understanding what is harness engineering, what's the fluff, what's really worth knowing. If you found this useful in any way, I would really appreciate a like and a

**[0:17:05]** subscribe. And with that, I will see you in the next
