---
type: raw-transcript
title: "Turn Claude Code into Your Full Engineering Team with Subagents"
youtube_id: -GyX21BL1Nw
url: https://www.youtube.com/watch?v=-GyX21BL1Nw
slug: turn-claude-code-into-your-full-engineering-team-with-subagents
published: 2026-02-01
duration: "0:20:26"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Last month, I covered agent harnesses and why they're the next evolution for AI agents, especially for agentic coding. The idea here is simple. If we give too large of a request to our coding agent, even if we have a lot of context engineering, the agent is going to completely fall on its face. And it's

**[0:00:18]** all about context management. Agents don't do that well when you start to fill their context window. It is the most precious resource when we are engineering with them. And so that's what brings us to the idea of an agent harness. It's really a wrapper that we build of persistence and progress

**[0:00:36]** tracking over our coding agent. So that way we're able to string together multiple different sessions with state management, a git workflow. It can get pretty elaborate, but it allows us to extend how much we're able to send into a system at once. And this really is the future of AI coding. If we're going to

**[0:00:55]** push the boundaries of what is possible with our coding agents, it's going to be with a harness as a wrapper. But there is a big problem here because if we're building this harness like this is anthropics one that we'll talk about in this video, we're trying to push the

**[0:01:10]** boundaries of our coding agent turning it essentially into a full-on engineer. But engineers do a lot more than just coding. They also communicate in a platform like Slack, giving us updates on the progress. They manage the tasks in something like Linear or Jira. They're maintaining the GitHub repository. We need all of these things

**[0:01:30]** in the tool belt for our agent for it to be a true AI engineer. And this diagram, what you're looking at right here is actually what I've built to show you right now. I've been experimenting with some ideas here. How can we take an agent harness and build a tool belt into

**[0:01:45]** it so that it can really be a full engineer? So, I'll show you how this works right now, how you can extend this for yourself. and stick around to the end of the video as well because I'll talk about how this really is the future of Agentic Coding. Some big things that

**[0:01:57]** I'm working on personally as well. And of course, this entire harness I have as a GitHub repository for you, which I'll link to in the description. So, I encourage you to try it out and even extend it yourself. I made it super easy to tweak all the different sub aents

**[0:02:12]** that we'll talk about in a little bit to connect to the different services. In the read me here, there's a really quick setup guide. I'm also using Arcade. This is the platform to make it super easy for us to connect to Linear, GitHub, and Slack through MCP. So, I'll talk about

**[0:02:25]** that a bit more as well. Once you have this all set up, all you have to do to send the context into the harness to begin is create an appspec. You can think of this like a PRD. It's all of the features that you want it to build

**[0:02:39]** autonomously in the harness loop. And so, you want to take this appspec and use it as an example. So give it to your coding agent because there is a specific format that works best for this harness. The biggest thing here is we have our task list in a special JSON format. This

**[0:02:56]** is the official recommendation from Anthropic because I've built my harness on top of Anthropic's harness for longunning tasks that they open sourced at the end of last year. And of course that does mean that I am using the Claude agents SDK to run this harness, but you can use your Anthropic

**[0:03:13]** subscription. So really cost effective and the Cloud Agent SDK is powering all of the harness experimentation I'm doing right now. So for this app specifically, just to give you a really cool example what this harness can build, I'm extending my second brain. It's yet another thing I've covered on my channel

**[0:03:29]** recently. I want to build a dashboard where I can paste in a bunch of research that my second brain has done and then it'll in real time generate a layout that's unique to the specific research that I gave it. So, I can glean insights really quickly. And boom, take a look at

**[0:03:44]** that. We have a beautiful TLDDR for this pretty extensive research document. I It's like 2,000 words in total. We can view the full thing as well. And this is not a simple application. There is an agent behind the scenes deciding the components to generate in real time to

**[0:04:00]** customize the dashboard based on what we pasted in. And so using the harness to build this, it decided to create 44 tasks in total in linear. And so I ran all of this already. So everything is done. So we can see all the tasks here. And then we also have the progress

**[0:04:18]** tracker meta task. And so we need to hand off to the next agent session every time we go through that loop in the harness. And so we need to let the next agent know what did we do right now so that it can pick up where we left off.

**[0:04:32]** It's also managing the GitHub repository. We got pull requests. It's making a commit for every single feature that it built. That's really cool. You can tweak this to your heart's content as well. And we're providing updates in Slack. And so, for the sake of simplicity, I just have it message me

**[0:04:48]** after the first and second sessions. And then when my application is fully complete, so then I can come back to my computer to test everything myself, just like you would do when you're reviewing the output from a real engineer. So we have everything managed in linear everything in GitHub and then letting us

**[0:05:03]** know when things are done. This is just beautiful to me. And by the way, I just want you to know that like this is just the starting point for a harness. A lot more work that I'm doing on top of this. A lot of ways you could extend this as

**[0:05:14]** well. Another really good example is you could build the harness to just watch 24/7 for any issues that you create in linear and then it would pick those up automatically. And so you can change the way that you interact with this harness. The sky is really the limit for the way

**[0:05:28]** that you build it into these tools. You could even have it work with GitHub issues, add in some other platform you have like Aana or Jira. It's entirely up to you. All right, so with that, let's now get into running this harness. We'll even do a live demo on a simpler

**[0:05:41]** application and then of course I'll show you how this all works. I want you to learn from this and see how you can extend it yourself. And so like I said earlier, the readme is really easy to follow. You just set up your virtual environment. Make sure you have Cloud

**[0:05:53]** Code installed and that you've logged in because this harness is going to use the same subscription that you have with Cloud Code. So, really easy there. The main thing that I want to cover right now is setting up your env. So, Arcade is our ticket here to connect super

**[0:06:08]** easily to linear Slack and GitHub. That's why I wanted to include it because then we don't have to set up all of the individual MCP servers. And so, you could change this harness to use those directly if you want. But Arcade has a free tier. They also implement

**[0:06:21]** what's called agent authorization. So they walk us through the OOTH flows really easily with these different services. So we could even share this harness with our team members with our Arcade MCP gateway. And they don't have to create a new linear API key and a new Slack app, but we also don't have to

**[0:06:36]** share those credentials with them. So it's a really really powerful platform. And so once you're signed in on the free tier, you just create your MCP gateway. You give it a name, description, LLM instructions. For the authentication, set it to arcade headers. And then for the allowed tools, look at this. Boom.

**[0:06:51]** We got GitHub. I'll search for linear. And then we got linear. And then finally, Slack. It is that easy to add in all 91 tools. And by the way, we are using the new tool discovery for MCP and Cloud Code. So, it's not like we're just dumping 91 tool definitions directly

**[0:07:07]** into our coding agent. That would not be contexts efficient. And so, there we go. You can create this. I'm just going to use the one that I already have. copy your URL because you set that as one of your environment variables and then you get your API key from the dashboard as

**[0:07:20]** well. That easy to get everything set up. Then just use your email here. We can also configure the specific GitHub repo that the harness leverages. So generally what I do is I'll create a empty repo and then add it in here. And then you can define a slack channel for

**[0:07:35]** updates too. And you can even change the model that each of our sub aents are using for coding linear GitHub. And so we can make things really cost effective or just really fast, right? Like we just want to really quickly create things in linear. So let's just use haiku for the

**[0:07:49]** model. So do all that configuration and then you'll run the authorize arcade script. So you just have to do this one time because then it'll go through the OOTH flow. So the harness now has access to your linear project, your Slack channel, and the GitHub repo that you're

**[0:08:06]** working in. And then with all of that taken care of, we can run our harness. Just a single command that we need to run to send our appspec into the harness. And so make sure that you have your appspec fully fleshed out with the help of your coding agent because

**[0:08:21]** looking at the first prompt here that's sent to our initializer agent is going to read the appspec to understand what we're building. So this is the single source of truth initially before we have everything set up in linear. And now I'm using WSL here because sub aents don't

**[0:08:36]** actually work that well in Windows with the cloud agent SDK. So use WSL Mac or Linux to run this. And so I'm going to activate my virtual environment here if I can type. There we go. All right. And then I'll run the command to kick off the agent. And then I'm just going to

**[0:08:51]** specify the directory here. So it's going to create this from scratch in the generations folder. So this is the default location for all of the projects that it creates. And so I'll send this off and it's going to kick off the initializer agent to scaffold everything for our project linear the GitHub repo

**[0:09:08]** the initial configuration for our codebase. I'll come back once it's done some of that. All right, take a look. So it delegated to the linear agent to get things set up for us. So it starts the project initially and now it's building all of these tasks. And so if I go to my

**[0:09:23]** projects here, we got our new Pomodoro timer task or project. So if I go to the issues here, there's six right now. And it's going to create more and more. Maybe actually probably only need six for this cuz it's a really simple application. So it created the five to

**[0:09:37]** build out the app. And then we have the meta project progress tracker as well. So this is where we're going to update things with our progress over time as we're handing off between the different sessions for the harness. So all the setup is done in linear. And now it's

**[0:09:51]** moving on to initializing the Git repository, calling the GitHub sub agent for this. And so remember, we're using sub aents for context isolation. So we're not bloating the main context window for our primary orchestrator here. And so yeah, there's going to be a lot that it does here. It'll go on for a

**[0:10:07]** while. And so while we wait for this, I'm going to go back to our diagrams here because I want to show you exactly how this works. I think the diagrams are a lot better of a visual than just watching the longs as it's running. And of course, I'll show you the project

**[0:10:21]** once it's done, but let's cover this in the meantime. So, going to the original harness here, I want to talk about what Anthropic built to set the stage for how I've improved it to create our full AI engineer. And so, we start with the appsp spec as the primary context that

**[0:10:36]** goes into our initializer agent. And most of the harnesses that I've seen over the past few months, they always start with an initializer. Because before we get into the main loop of implementing all of the features that we have in linear or in this case our local feature list, we need to set the stage

**[0:10:52]** for our project. We need something to create those features in the first place. And I don't know if you saw that blip there for a sec, but it actually popped up the browser because it was validating our code behind the scenes with Playright. So anyway, with our initializer agent here, it creates the

**[0:11:07]** feature list. It's everything we have to knock out that we laid out in our appspec. It creates a way to initialize the project and it scaffolds the project and the git repository. And so these are the core artifacts that we have after the initializer runs. We have the source

**[0:11:22]** of truth for everything that has to be built. And our coding agents when it knocks out all the features, it'll go back here and update things. And so this is our place to keep track of what have we built already, what do we still have to build. And then for the session

**[0:11:36]** handoff, we have a simple text file, which I appreciate the simplicity of this harness. But I think there really is a a big use case to have the agent work where we actually work, which is why I wanted to build this. But anyway, I'll wrap up here with the coding agent

**[0:11:52]** loop. Every single time the agent runs, we're running in a fresh context window. The whole point of this agent being able to go for a longer time is that we're stringing together different agent sessions and each one of them we want to start over so that we have fresh

**[0:12:07]** context. So it starts by getting its bearings on the codebase and so reading the feature listing like okay what should we build next? It'll do regression testing. This is important for reliability of the harness because a lot of times one agent is going to break what a different agent worked on

**[0:12:21]** earlier. And then after it validates that then it'll pick the next feature implement it update and commit which includes making the get commit and then updating these two files as well. And so what I've built is very similar. I mean you can even see that I I purposely have

**[0:12:35]** a the same architecture for the diagram here but there are some big differences because of the service integrations and how I'm using sub aents to orchestrate everything. So we still start with the appspec going into an initializer agent. But now like we saw in the logs earlier, it's delegating to the linear agent to

**[0:12:54]** set up the project in linear and all of the issues. And then just so that we know for our codebase like what linear project are we tied to? We also have a single local file. So for the most part, I'm avoiding local files. I don't have all of these files, but we need at least

**[0:13:10]** one file to point us to the right project ID. And then we'll also create the meta linear issue. So this is replacing our cloud progress. And then we'll create that git repo with our GitHub sub agent. And so now linear is our source of truth instead of these

**[0:13:25]** local files. And so now when each agent runs, it's going to start by reading the linear project. So that way it knows what is our project in linear. It'll call the linear agent to then find, okay, what are the features that we should validate? What should we pick up

**[0:13:39]** next? And we're using Arcade for authentication. So the agent has access to all of these services. And so then it'll do that implementation, use the GitHub agent to push, and then we can also use the Slack sub agent to give a progress update. And we're just going to

**[0:13:54]** loop over and over and over again until every single task in linear is done. And I've set it up in a way for most of the time it's going to just do one task at a time. But if the agent figures out it's simple enough, it might actually just

**[0:14:09]** try to knock out multiple of them in a single session. And this is all configurable in the prompts that we'll get into as well. So the last thing I want to cover while we wait for our harness to complete is the architecture and how you can tweak things for

**[0:14:22]** yourself. Every single agent that we have in this harness for coding the different services, they are controlled by these prompts that we have in the prompts folder. And so when we create our agent, we're using the cloud agents SDK. So we're defining everything in code. We're not using our cloud folder

**[0:14:39]** like you would with cloud code. We have our system prompt loaded in right here. So we're loading in from this file. And so our orchestrator, this is our system prompt where we're describing. We're building from the appspec. Here are the sub aents that we have access to. Here's

**[0:14:55]** what our workflow looks like. All that's defined in the system prompt. And then when we are in our very first session, that's when we use the initializer task. And so I'll show you here in the code. I I promise I'll stay pretty high level with the code here. We're seeing is this

**[0:15:10]** our first run? Do we have things initialized in linear or not? If it is our first run, then this function is going to load in the prompt from this file. So we're controlling with markdown files just like you would with sub aents in cloud code. And then otherwise we're

**[0:15:24]** going to load the continuation task. And so this is what we run every single loop when we're going to build that next feature. So we read that linear project. We know what linear project we're working with. We delegate [snorts] to the linear agent to figure out what we

**[0:15:39]** should work on next. everything that I've already explained in the diagram. I'm now just showing you how this maps to the prompts that we have for all the sub aents here so that you can tweak all this for yourself. You can connect more services, change how often it

**[0:15:51]** communicates in Slack, anything that you want to do. And so the last thing that I want to show you here is that instead of defining our MCP servers and our sub agents in thecloud folder, we're doing it here in our cloud agent SDK definition. And so we're connecting to

**[0:16:07]** obviously our arcade MCP gateway and then the Playright MCP server. Same kind of way that you configure the configuration with something like claw desktop for example. And then we have all of our agent definitions right here. So this is being imported from this file. It is super easy to add on more

**[0:16:25]** sub agents if you want because for every agent we just give it the description. This is how our orchestrator knows when to call upon the sub aent. We are loading the prompt from the file. Like for our linear agent, we're loading it directly from the linear agent prompt

**[0:16:39]** right here. Just speaking to like how we manage issues and projects and things like that, we have the tools, the tools that are it's allowed to use with the arcade mcp. And then finally, the model. So this is from ourv. We can use haiku, sonnet or opus. And so we just build up

**[0:16:55]** these agent definitions here. So you can change the prompts, change the description, add in another one. Very easy to configure. And that's all just brought into our agent automatically. And so it really is all of these markdown documents that define the entire flow. Really just using the Claude agent SDK as the wrapper around

**[0:17:13]** these different prompts, connecting everything together into this pretty elaborate system that's able to handle a lot. Like going back here, we're not done quite yet, but we finished three out of the five issues for this simple Pomodoro timer app. I'll come back once everything is done so we can see the

**[0:17:29]** full example now that you know how it all works and how you can extend this yourself. And here we go. The big reveal. The application that we've been creating throughout this video is complete. And interestingly enough, because this application was so incredibly simple, it decided to build everything in the initializer session,

**[0:17:46]** which I actually prompted it to do so if it determined it was simple enough just to show you how dynamic this system can be. And of course, I showed you the more complex app earlier where it did have to do many different sessions for 44 tasks. But yeah, our application looks really

**[0:18:01]** good. We can start it here. We can pause it, skip to our break. The Pomodoro technique is really awesome for productivity, by the way. But yeah, we got our update in Slack that the project is complete. It links to our GitHub repository here where we have six commits, one for the initialization and

**[0:18:16]** then one for each of our tasks. And of course, they're all marked as done with our progress tracking filled out as well. So we started the initialization and then this is the project complete status at the end. Super super cool. We built this entire thing just during this

**[0:18:31]** video as I was covering the code and our diagrams. So I want to end this video by talking about the future of AI coding with these harnesses and some things that I'm working on myself because here's the thing. I hope that in following this video you're inspired to

**[0:18:46]** try this harness yourself, even build on top of it. And I hope I made that clear enough for you. But in the end, what's most powerful is building AI coding workflows and harnesses that are specific to your use case, exactly how you want to manage tasks, how you want

**[0:19:01]** to share context between different sessions. I I really believe that if you build your own optimized workflow, it's going to be way better than anything that's off the shelf. But there's nothing that really helps you build that right now. And it's such a powerful concept. And so that's what I'm going to

**[0:19:16]** be working on. So, my open source project, Archon, I worked on this a lot last year. This is my command center for AI coding. It gained a lot of traction. I know it's not as many stars as something like OpenClaw, but I was really happy with the traction that it

**[0:19:30]** gained, but it's really not as relevant of a tool right now because it was all about task management and rag for AI coding. But task management is getting built into all these tools like cloud code and coding agents these days are so good at looking up documentation that

**[0:19:44]** rag just isn't as important for coding specifically. And so I want to keep the vision of archon being the command center for AI coding but I want to turn it into the N8N for AI coding being able to define and orchestrate your own AI coding workflows and harnesses so you

**[0:20:02]** can build something like this really easily but actually make it custom to you. So, that's what I'm working on behind the scenes right now. I know there hasn't been a lot of updates with Archon because I've been shifting the vision, but I'm super excited for that. And so, if you appreciate this video and

**[0:20:16]** you're looking forward to more things on AI coding and these harnesses, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
