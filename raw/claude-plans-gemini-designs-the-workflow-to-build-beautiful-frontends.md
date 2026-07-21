---
type: raw-transcript
title: "Claude Plans, Gemini Designs: The Workflow to Build BEAUTIFUL Frontends"
youtube_id: iICZTWcryac
url: https://www.youtube.com/watch?v=iICZTWcryac
slug: claude-plans-gemini-designs-the-workflow-to-build-beautiful-frontends
published: 2026-06-03
duration: "0:18:05"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A couple weeks ago Google released Gemini 3.5 flash, an LLM that's cheap, insanely fast, and a lot of people are finding builds beautiful front-ends, user interfaces that actually look like they're handcrafted by a human. And trust me, LLMs are usually pretty bad at that. And then just a week later,

**[0:00:18]** Anthropic drops Opus 4.8, a reasoning powerhouse that just generally does really well on longer running agentic engineering tasks. And so now we have these two new models that have their strengths and weaknesses. And you might think for your AI coding workflow you have to pick one. But what I'm really

**[0:00:35]** excited to show you today is a workflow that I built. GitHub linked in the description, you can use this today, that mixes providers. So it's a workflow using both Opus and Gemini 3.5 flash to build beautiful full-stack web applications. And so we're using the new Gemini to design the user interface, but

**[0:00:54]** then Opus is still doing all the planning for things like the page copy and any of the integrations to really make it a full-stack. And what really inspired me to build this workflow, and I'll show you how it works and how to use it in this video, is I've been doing a lot of testing

**[0:01:09]** recently with Gemini 3.5 flash both in the new version of antigravity and in Pi as my coding agent harness. And it's been able to build user interfaces that look like this. This was a one-shot in the new antigravity. Insanely impressive. I mean, this looks way better than what you'd usually make with

**[0:01:28]** Claude code lovable bull. Not new at least for a one-shot. A lot less obvious that this is made by a coding agent. I mean, there's still a couple of things here that make it obvious like this header at the top you see way too much in LLM sites, but overall this is a

**[0:01:42]** really, really good starting point. And so yeah, Gemini crushes the UI. But one thing that I noticed as I was building these sites is the UI looks good, but the information itself, the page copy, was often pretty hallucinated. And so like like looking at the benchmarks here, Gemini 3.5 Flash seems pretty good

**[0:02:01]** compared to other models like Opus and Sonnet. But like in the end, Opus 4.8 benchmarks in my own experience and a lot of people's experiences is just way better at reasoning overall. And so, this workflow combines the best of both worlds. Opus isn't as good as building front ends, but it sure is better

**[0:02:18]** designing the page copy, making sure it doesn't hallucinate the actual information and integrations for the front end. And then sort of the secondary benefit here is Gemini 3.5 Flash being a lot cheaper. We can spend a ton of tokens designing the actual UI while still paying a lot less. Like the

**[0:02:34]** price here $1.50 for every 1 million input tokens. It is a lot more expensive using Opus 4.8. So, mixing providers for the sake of cost and because we're leaning on the strengths for different parts of our workflow. So, I want to explain the workflow with you at a high level, each one of the

**[0:02:52]** nodes that we have here and how we're mixing providers. I know it's a longer workflow, but we can use this to one-shot some pretty impressive websites like this one I built right here, a deep space catalog. I built just for a demonstration for this video. But yeah, the UI looks really good and the page

**[0:03:09]** copy is perfect. It has a full back end that Opus built as well. This is the kind of thing we can build with this workflow in a single shot. And then I also just want to cover how you can use this workflow and just generally some best practices that I built into this

**[0:03:24]** that you can have as a takeaway no matter the harness you're building, mixing providers in any way. And then in the repository for this workflow that I have linked in the description, I have a read me here that you can point your coding agent at to set up everything. So, it'll copy the

**[0:03:38]** skills over into whatever folder you want to create your application. And then it'll help you set up Pi with OpenRouter to have access to Gemini 3.5 Flash. And later I'll show how you could use Anti-Gravity as well. So, I just used open router as my way to work with

**[0:03:54]** Gemini. And so, we have all of the skills really for each one of the steps in the workflow that we have here. And then, if you want to run everything as a one-shot, I also have the Archon workflow. So, I'm not going to focus on this in this video, but Archon is my

**[0:04:10]** open source harness builder. This is a workflow that takes all of these skills, and it combines it together into a single execution. So, the agent will go through every single one of these steps autonomously. So, really, really cool. But, I want to more focus on the skills here so that you aren't, you know,

**[0:04:26]** forced to use my tool. And then, also it's better to just kind of explain things step-by-step in that way. So, I'll go through the workflow and then show you running the skills simultaneously. So, at a high level, the most important thing to understand for this workflow is every step is a

**[0:04:40]** separate coding agent session. And the way that they communicate with each other is by passing off a handoff documents. So, every single step is going to output a markdown document that is immediately read at the start of the next node. And so, for example, with our first step here, we kind of just survey

**[0:04:58]** the repo and the spec initially with Sonnet. And so, all that initial exploration, we summarize it in context.md, and then that is read in our plan step. So, there are two big reasons that we designed the workflow in this way. The first and more obvious one is that there's not really a way to mix

**[0:05:15]** providers in a single conversation, right? Like, I can't really just start with open assistant Claude code, and then transition that same context window into Gemini with either Pi or anti-gravity. It's just not possible to do that really. And so, that's why we designed the workflow first to be each

**[0:05:32]** step is a separate session. It also makes it very easy for us to experiment. Like, I can try in just a couple minutes, I can swap exploration to use Gemini with Pi as well. Or, I could have integrate use Pi with Kimmy K 2.6. Like, I can can this workflow and really

**[0:05:46]** experiment and find the best mix of providers. And the other equally important reason is we want to have every step of this workflow focused on a single task. Large language models, even the best ones like Opus right now, get overwhelmed when you try to have them do too much at once. Like there's no way

**[0:06:04]** for a larger workflow like this, I'm going to try to have Opus handle the whole thing, like exploration and then planning and then building the UI and then doing the integrations for full stack. I can guarantee it will fall flat on its face for anything more than a

**[0:06:16]** trivial web application. That's why we want to split things up. As long as we have a good process for hand-offs here, we're going to get the best results when every step, every coding agent session, is focused on one particular thing. And so, yes, there is a lot of prompt and

**[0:06:33]** context engineering that went into the skills for the hand-off process. We really have to make sure they're communicating effectively, and that's why I'm excited to give this as a resource for you cuz there's a lot of effort I put into it. But assuming you have that taken care of and designed

**[0:06:47]** well, this is going to give you the best results. Now, for a larger workflow like this, it's not like you can one-shot every web application. Like I want to be clear up front, but it's going to be great for building any kind of proof of concept or MVP for even non-trivial

**[0:07:01]** full-stack applications. The sponsor of today's video is Sonar, specifically their SonarQube advanced security product. The reality right now is that 30 to 40% of code is already being written by AI at a lot of companies, and that number is only going up. But what most companies aren't solving for fast

**[0:07:19]** enough is verification. If your AI is going to write code at machine speed, you also need verification that runs at machine speed. And that matters nowhere more than security. Case in point, just a couple of months ago we had the big Axios NPM package vulnerability. There was a version that shipped with a remote

**[0:07:36]** access Trojan. That, my friend, is bad news. And the The is if you're using Cloud Code or whatever coding agent, it might have brought that malicious version into your codebase without you even realizing. And so, your machine is infected before you even know it. Really, what it comes down to is we need

**[0:07:53]** our coding agents to have a way to verify the security of dependencies as they're bringing them into our codebases. And that is what SonarQube's advanced security gives us. You can think of it like a circuit breaker. When your coding agent wants to bring in an unverified dependency, it can lean on

**[0:08:09]** SonarQube advanced security and the real-time database here so that we know if there's any kind of vulnerability in the package and we can stop it from ever making its way in our codebase. It's also more than vulnerability detection and package scanning. We have unified SCA, SAST, and secrets detection all in

**[0:08:26]** one platform. Your unified verification layer built on the SonarQube you're already familiar with for code quality and SAST, just extended now for dependencies and AI-generated code, too. It's genuinely the platform that I lean on because I have everything I need for verification in one place. So, if you're

**[0:08:43]** writing code at machine speed now, this is your ticket to also verify at machine speed. I'd highly recommend checking it out. Link in the description. Also, if you want to get started for free, standard SonarQube is free for private projects up to 50,000 lines of code. I'll link to that as well. Cool. So,

**[0:08:59]** let's zoom in now and see more how this workflow actually works, how you can use this for yourself. So, we start with the exploration step, and the input here, really the input to the entire workflow, is a spec document. So, either you'll craft this by hand or work with a coding

**[0:09:14]** agent to build it. This outlines the full-stack application that you want to create. And so, going over to the repo here, we have all the skills for each step of the workflow. Again, you can use your coding agent to help you set up everything with Pi, with CloudCode,

**[0:09:27]** bringing in all the skills. Our first one here is the front-end mix explorer. And so, I'll do command J to open up the terminal where I have CloudCode already open in VS Code. And then, since we want to use Sonnet for this, what we can do in Claude Code is just do {slash} model.

**[0:09:42]** I can change it to the default, which is Sonnet. And so, I recommend doing this for any kind of exploration step in a workflow cuz you really don't need the most reasoning capabilities, so we can make it more token efficient and faster as well. And then to invoke the skill,

**[0:09:56]** it's just front end mix explore. And then we can either give it the path to a spec file like I showed in the diagram, or it just in quotes here we can do a free form, you know, like build XYZ if we want to be more informal. I

**[0:10:11]** would recommend a spec file for a larger workflow like this building an entire application, you want to be pretty specific up front. And so, as far as the spec file goes, I do actually have a full example in this repository. So, this is the exact spec for this

**[0:10:26]** application, the deep space catalog that I showed earlier. And so, I have the spec.md here so that we can see the starting point for the application that I And then I also have the artifacts, we can see the full run. Every single one of the handoff documents produced every

**[0:10:41]** step of the way, I have that documented so we can look at that really quick as well. And so, in VS Code, I'll just right click the spec.md, copy the path, paste it in here, and then I don't want to watch paint dry with you, so we're not going to run this right now. But I'm

**[0:10:55]** just showing you how you would get started with the workflow for yourself. You can use this example spec if you want, or you know, obviously I'd encourage you to build your own. So, we'd send that off, and then what we get out of this skill once the full thing

**[0:11:07]** runs is we have our context.md file. This is what we then send into the next planning node. So, we have the repo state, like here it's actually green field. Maybe you have some kind of starter template you want to build on top of. We have the framework recommendations, brand assets,

**[0:11:22]** environment variables, data layer. We're not doing the full planning yet, but we're just doing the initial surveying of the spec in the repo, so we have a good starting point going into the planning step, so the planning doesn't have to do as much and we don't have to

**[0:11:35]** spend as many tokens with Opus. Okay, so back to the diagram now, we have our context MD and it's time for the plan step. And again, we do this in a separate coding agent session. And so back in Claude Code, we can start up a new terminal if we want to or we can

**[0:11:51]** just do a slash clear right here. It really doesn't matter that much. And so let me open up Claude Code again in a new session. And this time the skill that we're going to use is the plan one. So just slash front-end mix plan. You can see it, it's really easy here. Like

**[0:12:04]** yes, there's quite a few steps that I have in this workflow. It'll take a while to get through it, but you can chug through this pretty quickly. And also, it's nice to have different sessions and different handoff documents because we can also verify each one. We can put ourselves in the loop wherever

**[0:12:17]** we want to really make sure the coding agent is on track. Or if if we want to just trust it, we can just kind of rip through these. So we just wait for one to finish and do the next and then give the path to the handoff document, right?

**[0:12:28]** So like right here, I'll go back in the artifacts folder, copy the path to context.md. That is the one parameter here. So now we have Opus for our planning. And I guess before we run this, we would actually have to do slash model, right? And switch it back to

**[0:12:41]** Opus. So just make sure you're using the right model for the right task. And there's also a lot of work that I put into engineering the kinds of plans that are created here. It's a three-section spec because we have to describe the information in the UI, how we're going

**[0:12:56]** to do any kinds of integrations like a back-end or authentication. And then also, how we're going to deploy the application. Like if you wanted to hook up the Digital Ocean or Vercel MCP so you deploy it automatically, the workflow can even take care of that for you. And it's very general, so it works

**[0:13:11]** really no matter the deployment platform or the back-end you're building, whatever you're working with. And so going to the plan here just to keep following this example of the website I showed earlier. Section A, the site content and intent. So this is building Cosmic Explorer. We describe the voice

**[0:13:28]** and mood, the content and messaging. I specifically don't want Opus though to describe the structure of the site in any way. Like we're going to have grids in these columns. Like we have none of that at all because I want to rely on the strength of Gemini to do that. And

**[0:13:41]** so when I first built this workflow, Opus tried way too hard. It basically steamrolled Gemini and told it how to design the site and it did look significantly worse. Like it proves that Gemini is better at building front ends because when Opus described everything in the plan, the sites didn't look as

**[0:13:57]** good. And then we have section B here, so the integration scope. If we want to build any kind of API for example, which we do, we have the Cosmic Explorer back end. So we have the database for different planets and things like that. We have the database model. And then we

**[0:14:11]** also have the deployment plan. And so right for this example, I don't have any kind of cloud deployment, but I did do some testing with it automatically deploying to Vercel earlier and that actually worked really really well. So pretty cool. So that is our plan there. And so we take the plan.md. We pass it

**[0:14:28]** now into Gemini. This is the fun part where we get to use Pi or anti-gravity. And so we have it read the plan, but specifically just pay attention to section A. So now we're only building the UI. So now back over to my VS Code, I have Pi open in a terminal now instead of

**[0:14:45]** Claude Code. And so the read me will guide you through the open router configuration and the symlink for the skill and everything. So you can do /model to switch to Gemini 3.5 flash if you aren't there already. And then just /frontend mix design. It's the exact same as invoking skills in Claude Code.

**[0:15:02]** So even if you're just trying out Pi now cuz you're interested in this workflow, very straightforward, it will feel very similar to you. And so we just have to give it now the path to our plan.md. So copy the path here, paste it in, again just the same. Arguments work the same

**[0:15:17]** with skills in Pi and Claude Code. And if If want to use anti-gravity instead, using Gemini 3.5 flash here, you can just start up a new project in whatever codebase you're creating this front end, and then we can just give the path to the skill. So, I could say, you know,

**[0:15:34]** read the skill here, and then I'll go back to VS Code, and I'll I'll actually copy that. So, front end mix design, and copy the path to the skill, and I can say, uh, go through these instructions now. So, we can literally use a skill as a prompt, even if you're

**[0:15:51]** using a coding agent that doesn't support skills in the same way. And then obviously, we need the path to the plan as well. Path to the plan is, and then I can just do the same thing that I did earlier, copying the path there. And so, yeah, this might be my ignorance. Maybe

**[0:16:04]** there is a way to do like {slash} front end mix design, but like even if you have to tell it to read the skill and execute the instructions, you can literally do it this way as well. So, super easy to invoke this skill, and then it's going to create the user

**[0:16:16]** interface, and then produce the UI summary. So, then we can use this to then go into the integrations and the rest of the workflow, continuing back with Claude again. So now, the rest of the workflow, you really are just repeating the same process here. You have the handoff

**[0:16:31]** document that you give as a parameter to the next node. Just keep in mind that some of these nodes also might need both the plan and the previous handoff. And so, there might be a couple of arguments, but really everything else is the exact same. So, I'm not going to go

**[0:16:45]** through and and run through every single node in this video. I don't think that's a good use of your time, and I want to encourage you to just try this out yourself right now. But, the process is straightforward all the way to the end with a smoke test. So, we do the

**[0:16:58]** integrations, like building out any kind of back end. We do the validation, so just having Sonic go through our unit tests and linting and things like that. We fix any issues that come up with Opus, and then we have the deployment, whatever you have in your spec for that.

**[0:17:11]** And then we even do a smoke test. So, using the agent browser skill, I use this all of the time. It's browser automation, so the agent can verify the website testing it as a user actually would. So, we do that at the end, and then we end with a deployed app that as

**[0:17:27]** long as it's not like some really, really complicated full-stack app, you're going to have a nice one-shot. Like, this workflow works incredibly well from quite a few different tests that I did with different front ends, including the one that I showed you right here that I'm pretty impressed

**[0:17:40]** with overall. So, yeah, I mean, really, I'm just going to go ahead and leave it there. I'd encourage you to try this harness yourself. Even if you just want to take ideas that I've taught here and apply it to your own harnesses, of course, I would encourage you to do that

**[0:17:52]** as well. And so, if you appreciate this video, you're looking forward to more on harnesses and agentic engineering, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
