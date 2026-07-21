---
type: raw-transcript
title: "Omnigent: The New Meta-Harness for EVERY Coding Agent - Claude Code, Codex, Pi, More"
youtube_id: oGE_Dwz-rMk
url: https://www.youtube.com/watch?v=oGE_Dwz-rMk
slug: omnigent-the-new-meta-harness-for-every-coding-agent-claude-code-codex-pi-more
published: 2026-06-15
duration: "0:14:51"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** There is a new open- source tool that was released just over the weekend. It's called Omni Agent. And we're going to unpack this today because it is a very powerful and free-touse meta harness. A meta harness is a tool that allows you to run longer AI coding workflows,

**[0:00:17]** mixing AI coding assistance. And so the most classic example that people really like right now is using cloud code for the implementation in a workflow and then reviewing that code with codecs. All of the top engineers right now, they're not relying on a single model or even a single harness for their

**[0:00:34]** workflows anymore because we want to lean on the different strengths of the different AI coding assistants and also have these different sessions for the sake of context and token optimization which is more important than ever right now. An Omni agent is the layer above the AI coding assistance that makes this

**[0:00:51]** orchestration really straightforward. Because if we don't have a tool like this, just one session to manage all of our coding agents and we can build custom agents. We'll get into all of this here. If we don't have something like this, we have to go between different terminals, create all these

**[0:01:04]** handoff documents. It really isn't straightforward. And so the idea of a meta harness, it really is peak harness engineering. And so I want to talk about why meta harnesses are so important right now. Then we'll get into how easy it is to use Omni Agent to drive your AI

**[0:01:19]** coding workflows, even building a custom setup in the platform. Cool. So, let's start by talking about why meta harnesses are so important right now. And so, first things first, if there's one lesson we can learn this year for AI coding, it's that the harness matters as much as or maybe even more than the

**[0:01:36]** model. And it's even more apparent right now with the recent ban of Fable 5. We can't even rely on having the best LLMs for our AI coding workflows or getting better ones. And so if we want to make our AI coding more reliable, that brings us back to the harness. If the LLM can't

**[0:01:52]** get better, then we better make the system around the LLM more powerful. See, your harness is everything like your system prompt, tools, skills, workflows, rules, all of that together packaged up is our harness for making a single AI coding assistant more reliable for us. and the meta harness. This is

**[0:02:10]** what a lot of people are really starting to lean into right now. This is the next big thing for AI coding. Instead of making one coding agent better, what if we have the layer above that orchestrates many AI coding assistants working together on larger tasks? That's exactly what a metah harness is. I'm

**[0:02:26]** building something kind of around meta harness engineering with archon. And there's actually a lot of ideas from Omni Agent that I'm going to be bringing into my tool that working on as well. This is just so powerful right now. And Omni Agent has made it so easy for us to

**[0:02:40]** run this meta harness pretty much right out of the box. Like we'll see in this video here, you can get this up and running in just minutes. You can also work on it across different devices in the same environment. We of course can connect all of the most popular AI

**[0:02:53]** coding assistants like Cloud Code, Codeex, and Pi using a bunch of different models. We can share our sessions with other people, which is another thing that coding agents don't really have right now. And then of course they have a lot around policies and guardrails and running agents and

**[0:03:08]** sandboxes. So this is really set up for a production environment as well. I'm really impressed with everything that they built here. And I'm just ecstatic that all this is open source for us to try right now. So to get started with Omni Agent, literally all you have to do

**[0:03:22]** is take a link to this GitHub repo, give it to your AI coding assistant, and tell it to set up everything. And of course, I'll have a link to this repo in the description. And even if you want to do it yourself, it's just a single command to set up everything. It's so easy. I

**[0:03:35]** would encourage you like just try this right now. You don't even have to reauthenticate because using Claude or Codeex or even Pi, it's just going to use the credentials from the CLI you're already signed into because Omni Agent just runs right on your machine. And so it even ships with Poly and Debbie a

**[0:03:52]** couple of example orchestrator agents that go between Claude and Codeex. I'll show you how these work and even how you can create your own agents and orchestrators in this video. And so before we dive in, just a little bit of context. I find this quite interesting. Omni agent is open source from the

**[0:04:08]** company data bricks. And so massive company, this is a project driven by their CTO. They're already using this very extensively internally, right? They're they're dog feeding their own platform. They're using it for their everyday engineering. And of course, they're having great success with it. It really is an impressive tool cuz you can

**[0:04:27]** pick any agent. You can build the custom ones like I will show you in a bit. And then you run it in a sandbox. So it's it's reliable, it's secure, and then you have the main orchestrator that has your history, all of your policies like the guardrails, your MCP servers and skills.

**[0:04:42]** So the AI layer that you customize lives in the server and then that can apply to any of the AI coding assistants that you run. So it's not like you have to have a specific setup for PI and then a specific one for cloud code. Everything runs at the top level and then we can

**[0:04:56]** access it through a lot of different ways. They have their native app. We have the REST API if you want to do things programmatically. The terminal if you're comfortable with that like cloud code, a web UI that we already saw. So many different ways to access it. So

**[0:05:10]** once you have Omni Agent up and running, you'll have a web UI that looks like this. It's nice, simple, and elegant. It reminds me a lot of the codeex app. So it's just agent first. You have your chat session here and you tell it what you want to build. We can go between the

**[0:05:23]** different coding agents and the example ones for orchestrating that they gave and then also a couple of custom ones that I'll cover with you here. And then for the custom one, we can go between the different harnesses. So if I even wanted to use PI with Olama for some

**[0:05:36]** local development, I can even do that with Omni Agent. So it's very flexible. I can pick my working directory like my AI tutor application and I can even do work trees which are very important for parallel development. And then I just send off my request. Obviously, we're not going to watch Paint Dry here. So,

**[0:05:52]** I'm going to go to a conversation that is already complete. So, I selected Poly as my orchestrator here. It has skills for how to run these larger workflows between different coding agents. And then it has access to call upon the different harnesses. And so, you can give it a GitHub issue or just a free

**[0:06:09]** form request like I did right here. And I'm specifically saying to delegate the implementation to Cloud Code and the review to Codeex. And so it loads context on our work and then it loads the skill that Pauly has. So it knows our workflow, our repeatable workflow for this specific flow and then we kick

**[0:06:28]** off cloud code for implementation. So we have the prompt that we're sending into cloud code. This is a subprocess that you can have run in sandbox or not whatever you can configure all of this and we'll talk about that as well. And so then Poly is going to monitor, make

**[0:06:42]** sure that Claude code goes through the implementation and then it'll send off the review to Codeex. So I didn't even have to set up authentication again. It just used the codeex and cla code credentials I already had. So I had this up and running in like literally less

**[0:06:56]** than 10 minutes. I was able to run this workflow going between cloud and codec so easily. And I know this is a pretty simple example of orchestrating a larger AI coding workflow, but it is very important, at least at a very fundamental level, to do your code review in a separate coding agent

**[0:07:13]** session from your implementation. Otherwise, the LLM builds up way too much bias. And this isn't like a absolute truth, but a lot of people feel like Codeex is best at reviewing and Claude is best at implementing. So if you're not doing a workflow like this, I would encourage you to just try it,

**[0:07:29]** especially because of how easy it is with Omni Agent to run this kind of thing now. And so we end with the implementation just local in our work tree. And of course, we can follow up just like any AI coding assistant and say make a PR for this just for example.

**[0:07:42]** So, however we want to then get this to the point where we review it and ship it, you can do all that with Omni Agent. It has all of the capabilities that any AI coding assistant would have, plus the ability to also call upon individual coding agents. So, I don't want to spend

**[0:07:58]** too much time in the config here, but I at least want to show you how this works at a high level. They've done a really good job making simple primitives for us to build all of the custom agents and orchestrators in Omni Agent. And of course, it's really set up for our AI

**[0:08:13]** coding assistants to help us build our own custom agents if we want to in the platform. And so every single orchestrator comprises of three parts. We have the configuration and then we have all the skills like the cross review one that we saw being used in the web UI and then we have the agents that

**[0:08:31]** it can call upon as it is orchestrating a larger workflow. So cloud code and codeex like we saw and then if we wanted to use like our Kimmy subscription or miniax or local modama poly the default one here can even run pi as well and so within our configuration we have the

**[0:08:48]** executor like for our orchestrator when it's not calling upon an agent what is the actual coding assistant we're using so it's using claude at the highest level we have its system prompt which is quite long but system prompts can be pretty long these days we have the sandboxing configuration so we can run

**[0:09:04]** unsandboxed or run in something like Docker or one of those more production platforms like E2B for example. Uh yeah, there's a lot of different configuration here around like the guard rails. And so there's a whole capability in omni agent I'll show in a little bit where we can

**[0:09:18]** have certain actions where we as a human have to approve. And so we have human in the loop where it'll wait for us to approve something before it continues in the workflow like force pushes to get for example. And then we have the tools that it has access to. And so this is

**[0:09:32]** where we tell it that these are the agents that you can delegate work to when you're orchestrating things at a high level. And then skills, I mean these are like just the classic skills that we have with claude codeex every AI coding assistant. This is the workflow that it can walk itself through. And

**[0:09:47]** then each of the individual agents has the exact same configuration. So same system prompt executor like this one is using claude. Obviously the codeex one is using codeex pi is using pi. The tools it has access to the guard rails. And so we can make things very custom

**[0:10:02]** for each individual agent that we're orchestrating as well. Very cool. And so I have a cool example here showing you both how to build custom agents in Omnien and then also how we can do policies and guard rails. And so this agent right here, I made something very

**[0:10:17]** simple, right? Like super simple system prompt using cloud code. No sandboxing or anything, but I have a custom guardrail here where I'm allowing cloud code to really run any command autonomously except any sort of get push that is using the force flag, right? Like that is one of those more dangerous

**[0:10:34]** actions you want to be careful of your agent running because it can override changes in your repo. And so the policy here just lives right next to the config for the agent. And it's just Python code which also I didn't write this either, right? Like this entire thing, I had my

**[0:10:47]** AI coding assistant build this custom agent for me just based on my request. Like I literally just told it to look at Paulie and Debbie for an example of how all the config is set up and then just build this for me. And so it's going to ask for my approval whenever I run any

**[0:11:03]** kind of forced get push. And so let me actually show you that here. So I'm going to go back to Omnigent here. I'm going to switch to my guarded custom agent that I have loaded up. And then I'll just paste in a prompt. I'm just telling it to run this command. Get push

**[0:11:16]** origin feature login. And also another thing I didn't show you cuz I didn't show you a live run yet. It's really cool how uh once it loads the repo, we can see like all the files in the workspace. We can see the agents that we're using if we're orchestrating many

**[0:11:29]** of them. It's really neat the the UX and the UI that we have here in the platform. And here you can see that I told it to run the command and now it's asking for my approval. And so we can get really custom here with the capabilities we allow our coding agent

**[0:11:43]** to just run with versus when we have to approve. And yeah, you can do this with hooks and claw code for example. But the benefit here is that we can apply this no matter the coding agent that we're using or orchestrating in Omnien. And we can use Omnien for more than just AI

**[0:11:58]** coding as well. Debbie, their other example they ship along with Paulie is a great example for this because this is an orchestrator that pits two coding agents against each other to argue on a question or a topic and then come to a conclusion together with Debbie orchestrating everything. And so I ask

**[0:12:16]** my question and then it lets Claude reason about it and take on one perspective and then GPT take on the other perspective. We can also click into the view to see their reasoning and all the tokens for each of the individual agents and then back to Debbie to see how everything is being

**[0:12:31]** orchestrated. And so basically it goes through two rounds here or at least that's what I prompted it to do. So then it sends the GPT feedback into Claude and vice versa for one more round. And then we sort of conclude the debate with Debbie synthesizing what both agents

**[0:12:46]** have said, giving us a final answer. So again, just like my test with Poly, it's a rather simple example, but I just want to quickly show what these workflows can look like. And I'm sure your imagination can really start to run wild here with the kinds of ways that you can build

**[0:13:03]** these larger workflows, combining coding agents when it becomes so incredibly easy to do so, even setting up your own custom orchestrators like I showed earlier. All right. So, at this point, I've showed you every feature at least at a high level for Omnigen except for the collaboration. So, what I want to

**[0:13:20]** show you really quickly is how we can work in the same session both on our phones and on our computer. And you can do this across the internet. So, you can work with people across the globe as well. But the easiest setup is to be working with different devices on the

**[0:13:33]** same Wi-Fi network. And so, if you scroll down in the read me here, they have instructions for doing that, deploying to a server using it from your phone. And so, personally, I didn't really do this myself. I just had my coding agent set up everything for me. That's obviously a theme that runs

**[0:13:48]** through any kind of setup these days. But, yeah, very easy to get this up and running. And so, if we go back over to Omnagent here, just over to this other conversation that I showed you earlier with the human in the loop. I'm going to go ahead and send a message on my phone.

**[0:14:01]** So, I'll just say hi right here. Send it in. And boom, there we go. You can see it immediately pop up on our desktop here. So very cool that just between different devices I can keep the conversation going as I'm going between different rooms in my house. And like I

**[0:14:15]** said, you can host this as well. So you can even work with it with other people. So there's everything you need to know to get started with Omniant. And meta harnesses are just so important now. You don't want to be stuck with just one model or provider for your entire AI

**[0:14:30]** coding workflow. It's just not the best way to do things these days. And so I would highly encourage you to try out Omnigen. so easy to get up and running. And so that's everything I got for you. Now, if you appreciated this video and you're looking forward to more things on

**[0:14:43]** harness engineering and AI coding, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
