---
type: raw-transcript
title: "Context Engineering is the New Vibe Coding (Learn this Now)"
youtube_id: Egeuql3Lrzg
url: https://www.youtube.com/watch?v=Egeuql3Lrzg
slug: context-engineering-is-the-new-vibe-coding-learn-this-now
published: 2025-07-02
duration: "0:22:57"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** The honeymoon phase for vibe coding is over and the new paradigm for AI coding is context engineering. I truly believe this is going to be the next big thing for AI as a whole. And let me show you why. So starting off earlier this year, Andre Karpathy coined the term vibe

**[0:00:17]** coding. It's all about relying 100% on your AI coding assistant to build applications for you with barely any input and no validation. And this concept completely blew up. We all fell for this trap because of the dopamine hit of instant code generation and also because vibe coding is great for

**[0:00:35]** weakened hacks and prototypes. Basically, you rely on intuition and repetition until your code seemingly works, at least until you try to productionize and scale it and then suddenly it doesn't. And you can read these statistics all over the internet. One article that I appreciate in particular is the state of AI code

**[0:00:52]** quality from Codto. They did a massive survey across the developer landscape. You can see in the bottom purple quadrant here, 76.4 of real developers have low confidence shipping AI code without human review. And they encounter a lot of hallucinations. And it's not like AI coding itself is bad. I mean, I

**[0:01:11]** love it myself. It's vibe coding. AI code without human review that is the problem. Because here's the thing, intuition does not scale. Structure does. I heard that recently. I thought it was so beautifully put. Because the biggest problem that we have with AI coding assistants right now is around

**[0:01:28]** context. Often times they miss or lack it entirely. So they don't have the necessary context to get the job done. We need better context. We need structure. That is where context engineering comes in. So let's kick things off right now by diving into what context engineering is. Then after we'll

**[0:01:46]** get into the lab with claude code. I'll show you how it works for real with a practical example that you can use as a template to instantly improve your AI coding. This is not theoretical. For some reason, YouTube has been obsessed with the Gemini CLI recently. Meanwhile, context engineering has been blowing up

**[0:02:03]** everywhere else on the internet, and context engineering is definitely a lot more important. Like I always say, capabilities over tools. The Gemini CLI is a tool. Context engineering is a very important capability that should really dictate the way that you work with AI as a whole. And context engineering was

**[0:02:21]** even condoned by Andre who originally coined Vibe coding. This is his response to a tweet from Toby, the CEO of Shopify, where he's comparing context engineering to prompt engineering. We'll talk about that in a second, but I really love his definition here. It is the art of providing all the context for

**[0:02:37]** the task to be plausibly solvable by the LLM. Here's a paradigm shift with this context which is our instructions and rules, documentation, so on that deserves the respect to be treated as an engineered resource requiring careful architecture just like everything else in software. When AI coding assistants fail, it's most often because they just

**[0:03:00]** don't have the information they need. And no, I'm not just talking about prompt engineering. Context engineering is very much a step up. Like Toby is saying, prompt engineering is all about tweaking wording, phrasing things in a specific way to get a single good answer from the LLM. But context engineering,

**[0:03:17]** supplying all relevant facts, rules, documents, plans, tools. So the LLM has a whole ecosystem of context. That is the paradigm shift from basic prompting and vibe coding. Prompting is just one piece of the bigger picture that we have here. And one last thing in X, I thought this was really funny. The top comment

**[0:03:35]** from Andre's reply to Toby is saying context engineering is the new vibe coding. And then Andre replied by saying he's not trying to coin a new word. But Andre, if you're watching this, I think it is too late. I'm sorry. There is a reason that people hang on to every word

**[0:03:50]** that you say. Thank you for everything that you do in the AI space. But anyway, if you are a visual learner, I also found this beautiful diagram in GitHub on context engineering. So all the different components that we have in here together make up what context engineering is. So we have prompt

**[0:04:06]** engineering as a part of it like we already talked about. We have structured output. It's a way to make the output of AI agents and coding assistants more reliable. We have state history and memory. So agents and coding assistants be able to remember what they built in the past. We can do things like provide

**[0:04:21]** examples. And then also rag is a huge component of context engineering. not something that I'm going to be focusing on a ton in this video, but that's actually because I have a lot more coming soon for you for rag and context engineering, being able to supply external documentation and knowledge to

**[0:04:38]** our AI coding assistants. And I will say there is a lot that is going on here. If you want to really do context engineering, well, you have to put a lot of time up front creating this context for your AI coding assistant. It's a lot different than vibe coding where you

**[0:04:51]** generally dive right into the actual coding. But I always love to quote Abraham Lincoln here. He said, "If you give me six hours to chop down a tree, I'm going to spend the first four sharpening my axe." And that is exactly what we are doing here. And it is well

**[0:05:06]** worth your time to invest upfront into creating this context because you're going to get infinitely better results versus diving straight into the implementation. You're going to have better code. You're going to actually save a lot of time in the end and then just not have to go through as much

**[0:05:20]** pain. That is the whole point. That is what I want to show you in action in a little bit here. And the very last article that I want to show you is the rise of context engineering from lang chain. This is definitely worth a read. So I'll link to this in the description

**[0:05:32]** of the video. And actually everything that I shared with you here I'll link in the description. I've definitely been doing a deep dive into context engineering. I hope that's very obvious to you. And so their definition of context engineering is pretty cool because it aligns very very closely with

**[0:05:47]** what we've seen already. But this is the key paragraph that I want to focus on here. LLM applications are evolving from single prompts to more complex dynamic agentic systems. And then here is the real kicker. As such, context engineering is becoming the most important skill an AI engineer can

**[0:06:05]** develop. That is a bold claim. Maybe it's a bit of an exaggeration. I don't really know if it's the most important skill, but yeah, this just shows the theme that's starting to emerge here where context engineering certainly feels like the thing to focus on right now. And so with that, let's now dive

**[0:06:20]** into cloud code. I'll show you how we can implement this for real to get some insane results with AI coding assistance. So here is my template for you in a GitHub repository that I'll have linked in the description. My introduction to context engineering. Now you can get very very deep with context

**[0:06:38]** engineering, diving into rag and memory, things that I'll cover a lot more in the near future here. What I want to do with this is introduce you to the idea of using AI coding assistance to create a super comprehensive plan for a new project and then implement that. And

**[0:06:54]** we're going to be using cloud code. This is going to work for really any AI coding assistant, but I'm focusing on cloud code here because it is the most agentic and widely considered the most powerful AI coding assistant right now. And we're going to use cloud code to

**[0:07:06]** plan, create the tasks, code, write tests, and iterate on that all end to end so that after just a few prompts, we have a full project implemented for us. That is the power that we have with context engineering. And by the way, a lot of what I'm about to dive into with

**[0:07:21]** you here is inspired by someone in the Dynamis community, Raasmus. He did a workshop last month in our community and it was an absolute killer. It was so awesome. He covered his agentic coding process focusing a lot on cloud code. He did a lot of things related to context

**[0:07:38]** engineering and he actually open sourced a lot of the resources that he shared with us in the workshop. So I'll link to this in the description as well. So credit where credit is due. Raasmus has inspired a lot of my ideas. And also if you want to dive a lot more into

**[0:07:52]** building AI agents using AI coding assistance, things like context engineering, definitely check out dynamis.ai. It is the place to be. We're constantly pushing the limit of what's possible with workshops like this. And so with that, back into my template that I have for you in the readme here, I

**[0:08:08]** have a quick start. You can follow along with this in just like 10 minutes and level up your AI coding game that fast with context engineering. But then also, I have this repo cloned locally. I'm just going to walk you through exactly what we're doing here. And then we'll

**[0:08:20]** see a demo in action. Now, before we move on, I just want to mention really quickly that there are definitely a lot of security risks when using AI coding assistance that are super important for you to keep in mind. It doesn't matter if you're using Cloud Code or Windsurf

**[0:08:34]** or something else like GitHub Copilot. These risks crop up that you might not even be aware of. Things like prompt injection, model poisoning, data leakage, these aren't theoretical threats anymore. That is why Sneak, a company that is trusted for securing AI generated code, is hosting a free live

**[0:08:51]** webinar Tuesday, July 15th at 11:00 a.m. Eastern time covering the OASP top 10 for LLMs. This is an event that you don't want to miss. A clear breakdown of these critical vulnerabilities. You get to see live defenses against these attacks like model poisoning and prompt injection and learn best practices for

**[0:09:11]** avoiding these security issues with AI code. Vendanna Verma from Sneak is going to be walking us through best practices for handling AI generated code and showing us real world examples that you can apply immediately. Plus, if you're an ISC2 member, you get one CPE credit just for attending. It doesn't matter

**[0:09:28]** where you're at with your technical ability. If you are using AI coding assistance, you have to understand these risks. So, I have a link in the description to register. Again, this is Tuesday, July 15th at 11:00 a.m. Eastern, and I'm definitely going to be there myself. So I have the repo cloned

**[0:09:44]** locally. Now let's dive into creating a super comprehensive plan for a new project and implementing it end to end with cloud code. And like I said, context engineering can be decently involved up front. So there are quite a few different files that I want to cover here. Markdown files for all the

**[0:09:59]** instructions, the different parts of our context. And so the first file that I want to cover is our claude.md. These are the global rules for our AI coding assistant. similar to, you know, winds surf rules or cursor rules if you've used those AI idees before. This is the highest level information that we

**[0:10:17]** want to give to our AI coding assistant. Things like best practices that we want it to follow, the way that we want it to write tests for our project, um the way that we want it to manage tasks, the style and convention guides, like all of this highle information we want to put

**[0:10:31]** in claw.md. And then going back to the readme here, the next file that I want to cover is our initial MD. This is where we describe the feature that we wanted to implement as it kicks off the project for us. And so going into this, I very much have it as a template for you. It's

**[0:10:48]** just a few different sections for you to fill out. So first, you want to describe at a high level the feature that you want implemented by cloud code or your AI coding assistant. So something like I want to build an AI agent that does ABC built with XYZ. And it's worth being

**[0:11:02]** pretty detailed in this section. And then second, it's so so important whenever you can provide examples to the AI coding assistant. This just helps so much. And so this could be from past projects that you've worked on that have some similar implementations for what you want to build now. It could be code

**[0:11:18]** examples or snippets that you found online. You just want to put that in this examples folder. And so I have this in the repo specifically to call out like this is your place to add examples for your AI coding assistant. And then also getting into the rag part of

**[0:11:32]** context engineering, we have documentation. So listing out any online docs that you want the AI coding assistant to reference or any MCP servers for rag that you wanted to use like my crawl for AAI rag for example. I'm not going to be focusing on this too much right now, but it still is a very

**[0:11:47]** crucial part of context engineering. And then last but not least, a place for any other kinds of considerations that you have for your AI coding assistant. And this is a really good place to include any gotchas, things that AI coding assistants mess up on a lot in your

**[0:12:01]** experience, just specifying how to avoid that right here. And so what I'm going to do for this build, because I am going to show you a full example here, is I'm actually going to delete initial.md and I'm going to rename the example that I have in the repo because we're going to

**[0:12:14]** use this to build out an AI agent here. And so going to initial.md, I'm building an AI agent with pideantic AI. I have some examples that I'll add into the folder off camera. For the documentation, I'm just going to have it reference Pantic AI. And usually I'd want to use an MCP server for rag, but

**[0:12:30]** I'm just keeping it simple here. Um, and then just for some other considerations here, some things that I haven't messed up on quite a bit is the use of environment variables. I'm telling it to make sure that it has a project structure in a readme. So, just little

**[0:12:42]** things like that. Just a couple of examples that I wanted to give here. So, that is my initial MD. And so now going back to the readme, we have our global rule set up. We have our initial prompt. Now it is time to generate a full plan for our implementation. And this is

**[0:12:58]** where we get into two of my favorite things for context engineering. Cloud code/comands and PRPS, which is short for product requirements prompts. And so they're similar to product requirements documents, PRDs. You've probably heard of this before if you've been diving into AI coding, but they are specifically designed to instruct an AI

**[0:13:18]** coding assistant. So, we're not creating like an architecture document. We're actually creating a prompt that we're going to run with cloud code. So, we use cloud code to build a prompt which is part of the project plan and then we use that to actually do the implementation end to end. It's so so powerful and

**[0:13:35]** we're using slash commands to take care of this. So we don't have to prompt a lot of things from scratch every time we're using this process to begin a project. And so in thecloud folder, if you have a folder called commands, any of the markdown files that you have here

**[0:13:50]** can be executed as custom commands for cloud code. It is a beautiful thing. And so our first command here is generate PRP. This is a prompt to create a very comprehensive plan as another prompt for cloud code. So there's a multi-step process here. We're getting a little bit

**[0:14:09]** more involved here now with context engineering. And so I'm not going to go through the details of this entire document, but we're walking it through what it looks like to take in a feature requirements. We're going to actually pass in initial MD and then do a bunch of research on our behalf, some

**[0:14:25]** architectural planning. We're having it really think through the problem step by step here to create a comprehensive plan for implementation. This is the engineered context that I'm really getting at with context engineering. And so the way this works and I'm going to go into my terminal here and I'm going

**[0:14:41]** to open up claude. When we have our commands within the commands folder now, I can do slashgenerate PRP and then the argument that I want to pass in here. This is just anything that I enter after a space. This is what's going to be given and it's going to replace the

**[0:14:58]** arguments placeholder here. So if I say initial.m MD, I'm now telling this command that the feature file is going to be initial.md. So now cloud code is going to look at initial.m MD, use that to guide the feature that it is then going to plan. So I'm going to go ahead and

**[0:15:15]** run this right now. And this will take a good amount of time because cloud code really goes through this in a comprehensive way, making sure that it generates a complete PRP for us. And by the way, it is also using a PRP template that I have available in the PRPS

**[0:15:32]** folder. So this is kind of its starting point. This is the template that it bases the whole document off of that it produces after we are done with this command. And so I'm going to pause and come back once it's generated the PRP. Then we'll take a look at what that

**[0:15:46]** looks like and use it to build our project. All right. So I'm coming back just for a second here to show you the process in action. The thing that I love about using PRPs and just context engineering in general is watching these relatively large to-do lists that it

**[0:15:59]** builds autonomously and knocks out one at a time. And so what it's doing is researching different APIs on my behalf to really make sure that the PRP we generate for implementation has all the details necessary to not hallucinate the usage of APIs. And that's one of the biggest things that AI coding assistants

**[0:16:16]** mess up on a lot. And so it's doing research, analyzing the existing codebase and then the examples that we're giving it, reviewing documentation, pantic AI, creating the PRP based on that, writing it all, and then it is done. There's so much that it's taking care of here. Not just

**[0:16:31]** creating one markdown file, but all of the research and planning that it does beforehand. And so yeah, now I will come back once it is complete. And there we go. Our PRP has now been implemented. It's in research emailagent.mmd in the PRPS folder. So it gives us a summary of

**[0:16:46]** its research and analysis, some things it did for the environment setup to get things ready to implement the project, and then it describes the content at a high level. And so I definitely don't want to dive in and explain everything that it creates here. And this is like

**[0:17:00]** brand new for me too. Um, but just going through this, it describes core principles, the primary goal for this project, and success criteria. A lot of specifics here that make a huge difference. And a lot of this is based off of the PRP base template that I uh

**[0:17:16]** used from Raasmus. And then talks about all the different documentation referencing both websites and things that I have in the examples folder that I included off camera like I said I would do. And man, this is just so powerful because now that we list these things and we instruct it in the PRP to

**[0:17:32]** look at each of these files and websites, we're going to have that all in the context as it's coding everything. And that's going to reduce hallucinations a lot. Even just this part alone is so powerful. And then another thing that I really like is we describe the current code base, what it

**[0:17:48]** looks like right now, and then our desired code bases. So we're laying out every single file that we want to have created ahead of time. And we're still flexible enough where like it can change the structure if it deems that worth doing in the middle of implementing. But

**[0:18:02]** yeah, this just shows the kind of architecture planning that we're doing ahead of time. It's so powerful. And so with that, going back to the readme here, there's really just one last step that I want to show you. We already did a lot of context engineering. This PRP,

**[0:18:17]** this is the pinnacle of context engineering, at least what I want to introduce you to right now. And so going back to the readme, if I go down to the bottom, now that we have the command run for generate PRP, now we just want to execute the PRP. It's very, very simple.

**[0:18:33]** There's not much that we have to type within cloud code itself because we are doing all the planning in these markdown files. We have our initial planning and initial MD. We're generating a PRP with this command and then executing it with this one. And all the prompting just

**[0:18:47]** lives in those files. And so now I can literally do slashexecute PRP and then if I open up my full terminal here, then what I can do is reference PRPS slash and then research email agent.m MD. So just calling out where that exists in my codebase. And then I'll send that in and

**[0:19:06]** it's going to go ahead and create another decently long task list. This is going to be very very end to end. And so I'm going to pause in a second and come back once it is done implementing. But I'll show a screenshot right here of the task list that it creates. It's very

**[0:19:21]** very comprehensive. That's the goal that we have with this. It's so cool how agentic our AI coding assistance can be when we give it the right context and how much we can reduce hallucinations as well. And so I will come back once we have the first version of our agent

**[0:19:36]** created. And there we go. After more than 30 minutes, Claude code has completed and tested our agent end to end. That is the power of agent coding with cloud code and context engineering. And it did take quite a few tokens to do this to say the least. So I'll have a

**[0:19:54]** screenshot right here of the token usage in the middle of the development towards the end. But I'm not bringing my own API key. I'm taking advantage of the max plan for Claude. And so I didn't have to pay anything more for it to do all this work for me. It is a beautiful thing.

**[0:20:08]** And so yeah, this is the output here at the end describing what it did for us. There is one bit of iterating that I had to do here. There's some weirdness for how the tools were set up for the agent. like it was creating these functions as dependencies for the agent which isn't

**[0:20:22]** really how you're supposed to do it with padantic AI. So I did one round of iterating but that was it and everything is working really really well. And so I do like I just did I highly recommend not vive coding actually validating the output but if you validate the output

**[0:20:37]** have your context engineering set up you are set. And so yeah we can go into the terminal here. I can run pi test. So we can see all of the tests that it created and used to iterate on our agent. Everything is passing. Just a couple of warnings that we can ignore. And then

**[0:20:52]** also we can run our CLI. So, I followed the instructions that it created in the readme for me to set things up and I implemented my environment variables. And so, now I can run Python CLI.py. We're connected to our agent running gbt4.1 mini for our model. And you could

**[0:21:06]** really use any model that you want. Actually, one of the things that I had in my examples was showing how to make it. So, you can set up different providers for your podantic AI agent like Gemini or Olama or OpenAI. So, we can actually do that as well. It's

**[0:21:19]** really cool. And so, within here, I can just say hello. We can test a basic message to our agent. Looking really good. We got our output here. Our terminal is looking really beautiful. And I can say something like search the web for the latest on clawed code. So we can have it use

**[0:21:35]** the web search tool because that's our research agent. I'm not going to test this out a ton right here. I'm just showing you right now that like everything is working. We're using the Brave API. We're using the OpenAI API. We got some results here. It's going to spit out a response for us in a second.

**[0:21:49]** It's just doing a lot of web searching for us, I guess. And there we go. All right, we got our response from our agent. So, this is working really, really well. Like I said, I just had to iterate once. So, I just kicked off this build and I set up all the permissions

**[0:22:02]** ahead of time. So, I just went and, you know, took my dog on a walk, came back, and the agent was it done. And that's what I'm showing you guys right here. So, really, really cool. That is the power of context engineering. And this is just getting your feet wet. I very

**[0:22:14]** much encourage you to use this template that I have for you. dive into creating these comprehensive plans and using them with an AI coding assistant like cloud code and then just take it from there. There's so much more you can do with context engineering with memory and state and rag a lot of things that I

**[0:22:30]** want to cover soon on my channel as well. So you can really go down the rabbit hole of context engineering and like we talked about at the start of this video it is really the thing to focus on right now and so dive deep have fun with it. I hope this helps as a

**[0:22:43]** starting point for you as well. And so if you appreciated this video and you're looking forward to more things AI coding, AI agents, and context engineering, definitely give me a like and a subscribe. And with that, I will see you in the next
