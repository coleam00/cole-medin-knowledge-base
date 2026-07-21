---
type: raw-transcript
title: "I Built My Claude Code Subagents DREAM TEAM to Create Any AI Agent"
youtube_id: HJ9VvIG3Rps
url: https://www.youtube.com/watch?v=HJ9VvIG3Rps
slug: i-built-my-claude-code-subagents-dream-team-to-create-any-ai-agent
published: 2025-08-27
duration: "0:26:36"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** It is no secret that Claude code sub agents have changed the game for AI coding. And today I'll show you how I use them along with Archon to build an AI agent factory. All I have to do is describe at a high level the agent I want to create. And then Claude Code

**[0:00:15]** spins up an entire agentic workflow with specialists to help me plan, create, and validate my agent. It's a template that I have available for you. And right now I'll show you how it works. Now sub agents are really just prompts. So it's not anything new, but the highly

**[0:00:29]** structured approach that we have to define and execute them in cloud code is a thing of beauty. With sub agents, we get specialized agentic coders to handle different parts of our development workflow. And then with archon, we use it to give knowledge to these sub aents and to split the tasks between them. We

**[0:00:47]** become the project manager of our agents. And that my friend is the future of agentic coding. So here is the sub agent Asian factory template that I have available for you in GitHub linked below. You can take this and run with it right now to build any agent that you

**[0:01:01]** want. And the reason that I'm jumping into this right now is because there is a really helpful diagram in the readme here to help us understand this agentic workflow that I've created. And so very simply, we have all of our sub aents that we're using in this workflow

**[0:01:15]** defined in ourcloud agents folder. These are all markdown documents. I'll show you how we create these in a little bit. So that defines each of our sub aents and then in our global rules and claw.md I define the workflow exactly what order we want to invoke these sub aents how we

**[0:01:30]** want to do it like we want to invoke some of them in parallel also speaking to how we can use archon to help us manage our knowledge and tasks if you have the archon mcp server connected to cloud code so we start with our user request that goes into our primary cloud

**[0:01:44]** code agent so no sub aents at this point that's going to ask some clarifying questions understand our requirements and then set up all the tasks in archon, distributing it between our different sub aents and then it'll immediately start prompting our planner. So we have our podantic AI planner because pyantic

**[0:02:00]** AI is the framework that I'm using for this factory and it's going to based on the requirements given from our primary cloud code agent. That's the prompt coming into our sub agent. It's going to do some web research, look at the Pantic AI documentation in Archon, use all of

**[0:02:15]** that to help it create architecture and best practices around the agent we want to create, and then it'll output a markdown document with its plan. We definitely need to have a markdown document outputed, and I'll show you we have that in our planning folder right here. So, it's going to create this uh

**[0:02:30]** initial MD because remember sub aents have their own context window. We don't share conversation history between our sub agents and our primary cloud code agent. So we use these markdown files to allow these sub aents to communicate with each other and with our primary cloud code agent. And so after we go

**[0:02:49]** through the planning, then our primary cloud code agent is going to kick off three parallel sub aents. We're going to plan the system prompt for our agent. We're going to plan the different tools that we need. And then we're also going to plan the package dependencies and also the agent dependencies, things like

**[0:03:06]** API keys and database connections. And so it's going to output, again going back here, these three markdown documents with its plan for building out each of those. And so now at this point, we've done a lot of context engineering. We have the initial plan for our agent. We know its system prompt. We know the

**[0:03:22]** tools that we need and generally how we're going to implement them, typically with some pseudo code and the dependencies that we have. So we really do have this rich set of context to now dive into the implementation. Now we don't have an implementation specific sub agent. This just goes to the primary

**[0:03:37]** cloud code agent to write out all the code for us. Then we prompt the validator agent. And this is so crucial. You always want to allow cloud code in some way to validate its own work and iterate on the things that it creates like unit tests. And so our validator

**[0:03:53]** sub agent is responsible for that. And then after it creates all of its tests, it's going to output a validation report. We're going to make sure we're good there. And then we will deliver the final agent. So that is the workflow that we have. And like I said,

**[0:04:06]** everything here is orchestrated within the global rules that we have defined in our claw.md. So I speak to the trigger here like this is when you should invoke the sub agent workflow. I talk about using archon and then I have the complete workflow built here in the different phases that I was just showing

**[0:04:21]** you in the diagram. And a lot of this could be a slash command as well. Slash commands are your way to have packaged up workflows in cloud code, but I just wanted to keep this simple and have it in the global rules here along with some best practices that I have for building

**[0:04:35]** agents with Pantic AI. So that's everything that we have set up here. Now I want to dive into sub agents with cloud code a bit more with you. Then we'll see this all in action and really have things come together. And also I just want to say here even if you aren't

**[0:04:48]** interested in building AI agents with cloud code specifically this kind of workflow will apply no matter what you want to create. And so going back to our diagram here let's say you wanted to build a front-end application for example. Well there's still going to be different components of your front end

**[0:05:03]** that you can split up the planning and execution between these different sub aents building a similar kind of workflow. So I hope this kind of can inspire you to just think about how you can take a problem like let's build a front-end app and let's split it into

**[0:05:16]** well we got our dependencies and then we have our components and then we have our CSS right like you can split into these different things and plan separately just like I'm doing with the system prompts tools and dependencies for our agents. So as I dive into how we can set

**[0:05:29]** up these sub aents and coordinate them together with global rules or slash commands think about how this will apply no matter what you want to make. All right, so let's dive more into the specifics of sub aents now. So I've got the sub aents page of the cloud code

**[0:05:43]** docs open right here. It's a great resource that I'll also have linked below. They got a quick start and they also cover the key benefits of sub aents which are really important to know. And so we've talked about some of this a bit already, but we have the specialized

**[0:05:55]** expertise through the fine-tuned prompts that we give each agent in the markdown files. We have reusability, like literally what I'm doing in this video, I'm packaging up these sub aents to give to you as a workflow. flexible permissions. We can define the tools that each sub agent has, even the model

**[0:06:10]** that it uses like Opus, Sonnet or Haiku. And then last but not least, we have the whole idea of context preservation. There's definitely pros and cons to this, but these sub agents do not share the conversation history with our primary claude code agent. So, we have to make sure that we're passing in all

**[0:06:26]** the context the sub agent needs and then outputting everything that our primary agent needs. That's why we're working with markdown files as output here. But it's also very nice because we're preventing pollution of the main conversation. For example, all of the web research and calls to the Archon MCP

**[0:06:41]** for knowledge that our sub agents are doing, that doesn't have to pollute the primary conversation for our cloud code instance. It's really nice to prevent us getting to that point where we have to autocompact the conversation in cloud code, which is never a good thing and leads to a lot of hallucinations. And

**[0:06:58]** so, we're just keeping our conversation very concise and directed. That's what sub aents help us with. And to get started, there's a couple of different ways that we can create our first sub agent. The easiest way to do so is with the slash agents command. And so going

**[0:07:13]** back to my IDE here, I have Cloud Code open up and I'll just do slash agents. So I'll go ahead and create a new agent. I'll put it in the current project. You can also make it global with this second option. And then I will have Claude help

**[0:07:24]** me generate this agent. So just like with my agent factory that I have for you, we can describe at a high level what we want for the sub agent. and it'll generate the full markdown that it'll put within thecloud/ aents folder. And so I can say I want to build a sub

**[0:07:40]** agent that helps me define system prompts for my AI agents in Python. So I'll send this in. And now it'll go ahead and generate the description, the system prompt that we have within our sub aents. Like for the validator, for example, it's about to generate all of this right here. And then there are just

**[0:07:57]** a couple of other things that we get to select once it's done there. So, I will come back once we have this generated. Next, we get to define the tools that we want our sub agent to have access to. I'll just do all just to keep it simple

**[0:08:08]** here. And then we get to pick the model, which is another really awesome thing with sub aents. If there is a certain part of your development workflow handled by a sub aent that doesn't need as much power in the LLM, you can save tokens by using Haiku, for example. So,

**[0:08:21]** I'll just have a balance here with sonnet. Then, I'll pick the color that it shows in the CLI when we invoke it. Pink looks good here. So, there we go. And now this is our system prompt engineer. So it's going to create this markdown file right here in the agents

**[0:08:33]** folder. So I'll do enter to save. And boom, there we go. We have our system prompt engineer. And take a look at this. We have everything at the top describing our agent. We got the name. We have the description, which by the way, the description is how our primary

**[0:08:47]** Claude code agent knows when to call upon this sub aent. So it's important to have things like examples here as well. That's why Claude adds these automatically. We define our model and the color. And then the rest of this is the system prompt. This is where we have

**[0:09:00]** the specialized instructions for our sub agent. And so this is generally what I followed when I created all of these other sub aents. I've got the name, description, tools, and color. We got our system prompt. That's our dependency manager. Same kind of thing with our planner, the tool integrator, the

**[0:09:16]** validator. So I'm not going to go into all these sub aents in great detail here, but definitely dive in and take a look at these if you want. I put a lot of time into kind of iterating on these sub agents after I created them with slash agents. So I didn't just go with

**[0:09:30]** whatever it spit out initially. I cleaned things up, made it more concise, made it fit more into the workflow that I also have defined in the claw.md. So yeah, really dive into this if you're curious how I set up this workflow and you want to see how you could adapt this

**[0:09:44]** to whatever kind of software you want to build with the help of cloud code. So that's the primary way that you can set up your sub agents. It's slash agent for each one of them and then iterate on them with the help of cloud code after. Another strategy that I just want to

**[0:09:58]** call out really quickly here and I tried with this as well and it worked extremely well. Just take the URL right here for the sub aents docs. Go into your archon and I'll have a link right here to the intro video where I show you how to set up archon if you want this

**[0:10:12]** for yourself. Go add knowledge and then paste in this link. This is going to give the entire documentation for cloud code including sub aents to our archon knowledge base. So now cloud code connected to the archon mcp server is able to search through the sub aent docs. It'll understand how to build

**[0:10:30]** these markdown files and so that way we can actually instruct claude code to create all of these sub aents at once. So we don't have to do slash agents for each one of these and iterate on it. And so yeah two approaches here. One of them is more simple getting started with how

**[0:10:45]** cloud code recommends creating your sub aents and then another one is specifically leveraging archon to build all this at once. You can build all these sub aents and even help you craft the cloud.md basically defining how we orchestrate all of these agents in a workflow. And so that's the key thing here is each of

**[0:11:03]** these sub aents the system prompt and description really describes how this agent operates in isolation. When do you want to use it? How does it work? And then our global rules here, which again, this could be a slash command. This defines how we use all of these sub

**[0:11:17]** agents together. The sponsor of today's video is Lindy, a noode AI agent builder that isn't just extremely powerful, but it's also very easy to use. Plus, they just dropped a massive update. Now, Lindy has an agent builder, they have team accounts, and now we have autopilot. So, Lindy agents have access

**[0:11:36]** to a computer and a web browser. First up, we've got the agent builder. Think of it like cursor but for building AI agents specifically in Lindy. And so we just prompt the agent that we want and then it creates the full workflow for us as a Lindy automation. So just as an

**[0:11:52]** example right here I had it build an AI agent that performs research on a lead and drafts an email in Gmail. So this is my conversation just super super simple. It was so easy to build this and it creates the full agent. So, it has these skills here, the tools that it has to

**[0:12:06]** search the lead with Replexity and draft an email for the outreach with Gmail. And just as an example here, I'm having him research Mark Cuban and draft an outreach email. So, it's going to start with Replexity, then go to the Gmail skill, and then we'll see our draft. And

**[0:12:19]** boom, there we go. Our conversation is done, and we have a draft Mark Cuban. Obviously, I'm not going to send this, but yeah, this automation is working perfectly, and I didn't have to build it myself. Next up, we've got Autopilot, which gives Lindy the ability to actually control your computer just like

**[0:12:34]** a human would. It unlocks literally every integration imaginable. Here you can see a Lindy agent monitoring Twitter for spam, identifying spammer patterns, and automatically blocking without any intervention from me. And finally, we have team accounts in Lindy now, so I can invite people in to collaborate on these agents with me and deploy them

**[0:12:53]** companywide. The automation possibilities with Lindy really are limitless, especially after their recent updates. So, definitely check them out. Link in the description to get started for free, $20 worth of credits, which is definitely enough to experience having a full AI agent factory working for your team. Now, the last thing that's really

**[0:13:10]** important to hit on before we dive into a demo, is how we are using markdown files to efficiently communicate between these different sub aents because none of them share the same context. And so phase zero after we ask for requirements we're going to create a folder within here. So when we do a third

**[0:13:27]** implementation there'll be a third folder that's created here. And all of the planning documents are going to be outputed there. And so going to our planner to start things off. We're specifically having it output a file called initial.md within the planning folder of the new agent that we're

**[0:13:43]** creating. And so just to go to my rag agent as the example for you, we have this planning folder and this is where we're outputting the initial MD. So that's a part of our process defining the inputs and outputs. And we also specify some of this in the markdown

**[0:13:56]** files for the sub aents themselves but also having it here because it's orchestrating the full workflow. And then going into the parallel agents for example with the prompt engineer we're telling it your input is the initial MD and then your output is going to be again within the planning folder a

**[0:14:11]** prompts.md. So we have the prompt come into our engineer agent from the primary cloud code instance and we're telling it to look in initial MD. So those two things together is the context for that sub agent. So it reads this as its first operation and then it's la the last

**[0:14:28]** thing that it does is it outputs a prompts.mmd and it's the same kind of thing for the tool development agent. It's got the similar inputs and outputs and our dependency configuration agent. So that is our way to bring in just the context that we need for each sub agent

**[0:14:43]** and then output just the context that we need for the rest of the workflow keeping our conversation compact and very directed and focused on what we need to get done. And then also throughout this workflow we're describing how we can use archon to manage the knowledge and tasks that we

**[0:14:58]** need for our implementation which also I did make that optional because I don't want to be one of those people that says you have to use my tool. And so I am describing what it's like to use archon, but only if it is available. And so we have that managing the whole workflow as

**[0:15:11]** well, even assigning different tasks to the different sub aents that we have in each of our phases here. All right. So now that we understand how sub agents work and how I've set up this workflow, now let's get into a demo. Let's see this in action. And so what we're going

**[0:15:24]** to be building here is the full example that I have referenced at the top of this readme, which by the way, this is the readme in GitHub. This is what I'll have linked in the description. It's a part of the whole context engineering intro repository that I've been doing a

**[0:15:37]** lot of things around context engineering for you with recently. So yeah, going back here, we're just going to follow the instructions in the getting started. So we simply have a prompt to request our agent. What do we want to build? We'll answer some clarifying questions that it asks for us. That's a part of

**[0:15:52]** the workflow in phase zero. And then we'll watch the magic. I'll show you in real time these different sub aents operating. We got the planner, then we go into our parallel agents, then the implementation, then the validation. We'll see it all in action. We'll see how it works with Archon as well. It's

**[0:16:06]** really exciting. And then we'll get our agent at the end. Like that's it. It is really simple to work with this whole template. And it all starts with a super simple prompt. And I even have the sample prompt as a part of this repository for you if you want to see

**[0:16:20]** the exact prompt that I'm about to execute to build the agent that I have in the demo here. So, this reference is what we're about to build. So, I'll copy this prompt. I'll do Ctrl J to open up my terminal where I already have Cloud Code opened up. And then I'll paste this

**[0:16:35]** bad boy in. Now, before we run this, I do want to set up a couple of things in Archon. If you want to be using Archon to make your implementation even more reliable. And so, going back into the browser here, the one thing that I'll say is it helps a lot because this

**[0:16:50]** factory is using Pyantic AI for our AI agent framework. It's very helpful to have the Pyantic AI documentation. And so we have the LLM's-Lful.ext. This is all of the Pyantic AI docs curated into a single file to give to LLM. And so I'll have this linked in the

**[0:17:06]** description as well. If you want to set up Archon, copy this URL, go in and add the knowledge and crawl everything for Pantic AI. I'm not going to do it now because obviously it takes a good amount of time to chunk and crawl everything. But then you'll have the Pantic AI

**[0:17:19]** crawled. You'll have about 430 code examples if things are looking good. Now through MCP, Cloud Code is able to use Archon to search through the Pyantic AI documentation just to make the implementation more reliable. And then we also want to create a project here. So I'm going to go into my projects tab.

**[0:17:36]** I already have one project created just as I was prepping this for you. So I'm going to create a brand new one with a kind of a similar name. So new project. I'll call this uh hybrid search rag agent. And then for the description here, I'm just going to

**[0:17:50]** leave this nice and simple and do the same thing as the title. But yeah, I'll create this project. And now I'm specifically going to tell Cloud Code in my prompt to reference this new project. So I want it to create all the tasks for me. We can even have it so that it

**[0:18:03]** stores the documents for our different sub aents here as well. And I actually did that as I was testing my implementation earlier. So like we have the output from the different sub aents, these markdown documents. I actually have them outputed and stored in Archon, which is just a really cool way to store

**[0:18:20]** all of the context in a database. So even other people that want to use archon along with us can reference these same things. It's really cool. So yeah. All right, we got our project set up now. So I'm going to go back into claw and I'm actually going to tell it to use

**[0:18:32]** this project. I'll say use the hybrid search rag agent project in archon. So I'm just going to be explicit here creating the project ahead of time. I mean it also will just create it for you if you don't have one, but yeah, I just wanted to define that since I already

**[0:18:46]** have a similar project in Archon. So there we go. Now we're kicking off the build. And because we're saying we want to build an agent, that's going to trigger the full workflow here. So there we go. We're starting with our clarifying questions. So off camera, I just really quickly typed out answers to

**[0:18:59]** each of its questions. It just wanted to know a couple of things like what kind of knowledge are we searching through and how exactly do we want the agent to output its findings? And so I'll send this in. And then it's going to start by creating some tasks for us in Archon to

**[0:19:13]** help us orchestrate the usage of our sub agent. So there we go. It's starting by checking Archon. We are successfully connected to the Archon MCP. And then after it creates some tasks, we'll dive into our first sub agent, the planner, where it's going to output that initial MD file. Once it does its planning and

**[0:19:29]** because we're doing the web research and all the Archon knowledge lookups within that sub agent, it's not going to pollute our conversation. And so I'll actually show you really quickly. Uh, something I want to call out that's really interesting is this workflow is actually very similar to the agent tier

**[0:19:46]** that I had with the original version of Archon. So, I turned it more now into something where it's like task management and knowledge for coding assistance. Like this is the layer between humans and coding assistants. But the old Archon was an AI agent that builds other agents. But really, it was

**[0:20:01]** just a bunch of specialized sub aents that I had to find through Langraph and Pideantic AI. And so we start with the planner and then we have our specialized agents for the tools and dependencies and prompt. Like this really is a a version maybe a bit more of a complex

**[0:20:16]** version of what we have now with sub aents in cloud code. So just a little interesting tidbit that I wanted to give you there. But yeah, look at this. Now we're setting up the tasks in archon. And so I'll actually show this here. I'll bring back over archon. We have

**[0:20:29]** requirement analysis and system prompt design as the two tasks that's created so far. And take a look at this. It even has it assigned to the right sub agent. So the requirement analysis is done by the podantic AI planner and then the prompt engineer is doing the system

**[0:20:41]** prompt design. Absolutely beautiful. And it's just going to keep creating more and more tasks here. Like I'll show you that we have it updated here. Like there's even more tasks now. And each one is assigned to the right agent. Like when we do the actual implementation, it's correct here that it's using cloud

**[0:20:55]** code, the primary coding. We're not using a sub agent in this case. So yeah, it's creating all the tasks and then we'll move on to the planner. So I'll skip ahead once we got to that point. All right. So it moved the task to doing for the planning. So if we go back into

**[0:21:09]** archon here, we can see that yep, we are about to execute the pyantic AI planner for requirements analysis. And there we go. We got the blue popup here. We're calling into this sub agent. And by the way, the planner agent is where you could integrate the PRP framework or

**[0:21:26]** something like BMAD if you wanted. I'm keeping this simple by just using sub aents. So not using a more advanced context engineering strategy like PRP, but I'm not just ditching PRP. I'm only excluding it to keep things simple here. But you could definitely like generate a PRP as a part of your planner sub agent.

**[0:21:42]** So yeah, I'll let this go for a while. It's going to do a lot of web search. It's going to look at the Pantic AI documentation through Archon. So it'll take its time. I'll pause and come back once we move on to the next phase. There we go. We completed our planner agent.

**[0:21:57]** Took 1 minute. Took almost 30,000 tokens. a lot of research that it did for us. And then it updated the task, marked it as done in Archon, and now it's moving on to invoking our parallel agents. So, it's updating all three of these tasks to doing. And then in a

**[0:22:10]** second here, we'll see the fancy colors pop up for these three agents all running in parallel. And in the meantime, oh, there we go. All right. Now, it's popping up. So, we got orange for our prompt engineer. And so, it's taking its time crafting the prompt to send into the sub agent. So, it finishes

**[0:22:23]** that. Now, it moves on to our tool integrator. And we can see that these these dots right here are not blinking yet because it's waiting for all three. There we go. Now they're all invoked at the exact same time once we have the prompts sent into each of them. And now

**[0:22:36]** they are off doing their own thing each rep starting by reading the initial MD exactly as we planned. And they're going to output markdown files in the end. So if we go in the agents folder, go into no not rag agent hybrid search agent and into the planning folder. Right now

**[0:22:50]** we've got our initial MD. So this is what our planner agent outputed. and then each of our parallel agents red. And so, yeah, the last thing I'll show you really quick is if I go back into Archon for task management. Just a beautiful thing. So, we completed our

**[0:23:03]** requirements analysis. Now, we're in progress for all three of our sub aents that each have a task assigned to them. This is a thing of beauty. So, all right, I will come back again once our parallel agents are done and we've got all the files in planning. Okay, this is

**[0:23:18]** actually blazing fast. like it only took a minute here because we just had to wait for the slowest parallel agent. And now we're already moving on to the main implementation. So I'm going to close out of the terminal here and show you. We got our dependencies. We've got our

**[0:23:31]** initial MD. We have our prompts. So our the system prompt for our agent. And then we have the general tools that we need for our semantic search and then also our hybrid search. So this is looking fantastic. This is all the context we need now. So going back to

**[0:23:46]** our primary claude agent and we can see this going back into archon here that now the current agent cla code is doing the implementation. This is not a sub agent right now and it's going to be reading in all these files. This is our complete context engineering. And so

**[0:23:59]** going back to my terminal, let me scroll down. Okay. Yep. So now we're doing some rag searches with archon to understand padantic AI. How to specifically implement the agent that we requested. Searching some code examples as well. So this is just so cool how we're seeing Archon in action, all these other parts

**[0:24:16]** of context engineering coming into the fold with sub aents. So yeah, I'm going to come back again once we're done with the implementation and we move on to that last sub agent for our validator. And there we go. We have our complete AI agent built for us now. Our hybrid

**[0:24:30]** search rag agent. So we had the validator that ran here actually for quite a while because it takes some time to iterate on the unit tests to make sure everything's polished for us. But then it updated everything in archon and wrote out some documentation. So you can see here that we have all the tasks

**[0:24:43]** complete now in archon. Take a look at that. And so what we built just now that actually is the full hybrid search rag agent that I linked to at the top of the readme. So you can check this out if you want. You can look into how it was

**[0:24:55]** built, learn from it, try the thing yourself. It's a fully working AI agent. I only had to iterate two times to fix it up. So I'll save you the boring details of having to iterate on this. I'll just show screenshots right here really quickly of the things that

**[0:25:09]** weren't working immediately. Just some database type issues that I fixed up in two more prompts. So, we threehotted this hybrid search agent and the rag pipeline already came. But yeah, it's super super cool. So, I'll go over and show you a demo really quickly. Now, I've got my environment already set up.

**[0:25:23]** So, I'll just run the CLI command like we have in the readme here and we can just do a quick demo of this thing. So, I can say for example, how are AWS and Anthropic partnered up? So this is just one of the documents that I have in my

**[0:25:35]** knowledge base from that rag pipeline. And yeah, if you guys didn't know, AWS is where all of the cloud LLM inference is run. It's run on AWS infrastructure. Super cool. So yeah, we can just ask another question as well. Uh like tell me about the cloud wars. Just another

**[0:25:50]** thing I know is in my knowledge base. So yeah, just a quick demo to show you what we were able to create thanks to the power of this agentic workflow using sub agents to have all these specialized agents operating in different stages of our development. Super super cool. We

**[0:26:06]** use archon to give all the knowledge around pyantic AI and also for the task management. So we are project manager throughout this entire thing too. Super super cool. So, that's everything that I've got for this sub aent template available for you to try right now. I hope that you enjoyed this, got a lot

**[0:26:24]** out of it. If you appreciated this video and you're looking forward to more things on AI agents and AI coding, I would appreciate a like and a subscribe. And with that, I will see you in the next video.
