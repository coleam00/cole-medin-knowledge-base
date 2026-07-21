---
type: raw-transcript
title: "Pi Coding Agent + Archon: Build ANY AI Coding Workflow (No Claude Code Bloat)"
youtube_id: XSmI7OYd7iM
url: https://www.youtube.com/watch?v=XSmI7OYd7iM
slug: pi-coding-agent-archon-build-any-ai-coding-workflow-no-claude-code-bloat
published: 2026-04-20
duration: "0:17:48"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** If you haven't tried the Pi coding agent yet, it is time, my friend, to give it a shot. Pi is a minimalistic open-source coding agent, and minimalistic is really important here because Pi is fighting the bloat that we see with so many other coding agents right now, especially

**[0:00:17]** Claude Code. Now, don't get me wrong, I still love Claude Code, but especially recently, there have been a lot of problems with insane token usage and just bugs in the platform because they're shipping things so quickly. So, I really can resonate with the philosophy behind Pi, which is create

**[0:00:34]** the foundational harness and then make it very easy to extend. And so, I've been using Pi a lot recently, and I'm super excited to say that we've officially added it as the third coding agent supported in Archon. Archon is my open-source harness builder for AI coding. It allows you to take your

**[0:00:52]** entire agentic engineering process, no matter what it is, and package it up into reusable workflows that you can execute in parallel to handle all of your AI coding tasks at scale. And as far as the coding agents that you can use directly in these archon workflows in the harnesses that you build, we

**[0:01:08]** initially shipped with support for claude and codecs and now we've added in PI. And I have been loving the pi and archon combination especially because if we go back to the readme for pi here and go to the supported models, you can pretty much use any large language model

**[0:01:26]** that you want in pi. So pi also makes it super easy to build workflows. We are using different models, different providers. We have all that wrapped up in archon now. And so in this video right now, I want to cover how to get started with pi, why it's so important,

**[0:01:39]** especially right now. And then I want to get into how you can use it with Archon. Give you some inspiration for some workflows I've been building. There's so many cool things that I've been experimenting with taking advantage of the whole Pi extension ecosystem. All right, so let's start by talking about

**[0:01:55]** why Pi is so important right now. Quickly becoming my best friend might be the case for you soon as well. So here we have Mario Zechner. He's the creator of Pi and he gave a talk at the AI engineer conference recently called Building Pi in a world of slop. And so

**[0:02:11]** he gives this narrative here of why he ended up building his own tool even though we already have very powerful solutions out there like claude code. And in the beginning there was claude code. He like many of us used this as the first coding agent where it felt

**[0:02:25]** powerful enough to like really handle complex agentic engineering tasks end to end. And one of the biggest value propositions for claude code initially is that it was simple, predictable and easy to mold to fit our own workflows. That's one of the reasons they shipped it as a very simplistic CLI fighting

**[0:02:44]** against what they used to call the slop for other IDE tools like wind surf and cursor everything that came before. But the problem is Enthropic has not stopped shipping features. And so it's gotten to the point where this is what claude code looks like now. There's so many

**[0:02:59]** features, bugs being introduced all the time. The platform is just very bloated now because there's so much to maintain. And so they've definitely deviated from their initial mission for the tool. And I get it. It's important to ship features for any platform to remain relevant, but it seems like they're just

**[0:03:14]** doing too much right now. And then we have other problems that are honestly even bigger. Like your context is not really your context. It's difficult and in some ways impossible to control the system prompt for cloud code and it's changing constantly throughout their releases. And so you're relying on this

**[0:03:29]** harness where the underlying prompting is something that is always changing, hard to manage, and it's going to affect the results that you get. And you're not even going to know why. You're probably experiencing this yourself. Now, of course, before Mario just went and built Pi, built his own thing, he explored a

**[0:03:44]** lot of options that are already out there. And so, you know, AMP, codeex, factory, open code, he tried open code a lot because it is open source as well, fits a very similar ecosystem, but he found issues with that, right? He wanted to create something so foundational and

**[0:03:59]** easy to extend because the codebase itself would be small and very unopenated. And so, that's what led him to building his own. And so he decided, let's just strip away everything, build a minimal extensible core and make the agent modify itself. This is the kicker here with Pi. For any feature that you

**[0:04:17]** want to build, you literally just ask Pi to build it into itself. And so anything that ships to cloud code like the slash by the way feature for example, you can just go into PI and say, "Hey, Claude Code just shipped this. I like this feature. Build it for myself." And it's

**[0:04:31]** going to do that. So you don't lose out on any of the features that cloud code is shipping, but you also don't have to bring in all the bloat and the system prompt changing all the time. So there are purposely a lot of things that are not built into PI like MCP, sub aents,

**[0:04:44]** plan mode, things that Mario doesn't use himself. And I mean I use plan mode, I use sub agents, but you can just build that right in. And there's an entire extension ecosystem with skills and prompts and themes and extensions. We'll talk about this today. So pretty much anything that you want, you can build it

**[0:05:00]** yourself or even use thirdparty implementations that you can bring into your Pi coding agent with a single command. And I have been playing around with so many of these extensions in Pi. There's this entire thirdparty marketplace that I'll link to in the description. Amazing things here. And of

**[0:05:16]** course, it's very easy to build your own in Pi, like I was just saying. So pretty much no matter the capability, skill, or prompt template that you want, you'll find it here. Or it's super easy to build yourself. One of the archon plus pi workflows I've been playing around

**[0:05:30]** with is a plan implement validate workflow using the planotator extension for pi. And so when your codeex or miniax or glm or whatever in pi creates a plan, it gives you this website where it renders everything out and you can make your comments in line and it'll address everything automatically once

**[0:05:50]** you send in your feedback. So we have this whole iteration just happening right within a website and it's so easy to just mention individual things instead of having to go into a separate session and say this line number change this thing this line number change this thing we have to explain a lot less so

**[0:06:05]** this is really cool I'll show you this more in a little bit but first I want to talk about how easy it is to get pi up and running. So scrolling down in the readme here it is a single npm command to install pi. So I'll run this and show

**[0:06:17]** you installing it from scratch on my computer right now. So I uninstall it. I'm going to reinstall it. All right. And then once you have it installed, you just have to run the pi command to open the coding agent terminal just like you do with claude or codeex. And then you

**[0:06:28]** do /log to set up any one of your subscriptions. They got anthropic, github copilot, anti-gravity, codeex. That's the one that I'm using. So my model is GPT 5.3 spark. Uh be aware that I believe it's against Anthropic's terms of service to use your subscription with Pi. It's the

**[0:06:46]** same thing that Pi actually runs OpenClaw under the hood. So be aware of that. But you can use codecs. That's what I'm using. And then of course, if you want to use your API keys for anything, they have instructions for that. So you can pretty much use any

**[0:06:58]** model that you could dream of like Mistl or Grock or Kimmy K2 or Miniaxm 2.7. The world is your oyster. And then once you have your API key set or your subscription logged in, then you just do /model to pick from the ones that are available based on what you have

**[0:07:12]** configured. So right now based on what I have set up, I can use Gemini models or I can use GPT. It is that easy to get started. And then as far as extending Pi, that's the main thing, right? We have the foundation that we build on top of for the coding agent. I have some of

**[0:07:27]** my favorite extensions already installed. And so I just found these from the extension marketplace here. It's a single command. You can click into any one of these, a single command to install them. The other thing you can do is literally just ask it to search the web for XYZ extension and install

**[0:07:43]** it. So it can run the single command itself to bring these extensions in. And of course, if you don't find what you're looking for or you want to build something custom cuz you don't trust a third party marketplace, then it is as easy as saying like, hey, we don't have

**[0:07:57]** MCP support right now. Build this into PI, right? Like that is literally how easy it is to extend PI. You don't have to do a lot of context engineering because it understands its own framework under the hood because it's so simple. So very easy to build on top. So again,

**[0:08:13]** no matter what you want, you can build it into Pi. Otherwise, Pi is just like any other coding agent. It's going to be just as powerful. Mario actually proves that with benchmarks in his conference talk. It supports skills out of the box, global rules, like you can see, it

**[0:08:27]** loaded myclaw.md automatically. So, it has that compatibility if you're coming over from cloud code. Very, very cool stuff. All right, so with that, let's get into using Archon and Pi together. This is quickly becoming my favorite AI coding combination. So, if you haven't used or heard of Archon before,

**[0:08:43]** definitely check out this video I'll link to right here. I give a full introduction uh setup guide how to use it and build workflows. It is an open- source harness builder, right? So, you're taking your process for planning and implementing and validating whatever you do with coding agents and you're

**[0:08:58]** packaging up into a harness that you're creating yourself. And this really is the evolution we've seen recently for AI coding. It's not just about context engineering anymore. It's about how do we string together multiple coding agent sessions so that we can have longer running tasks and we don't have to just

**[0:09:17]** bog down a single coding agent. That is what we're doing with Archon. And I've been having a blast using Pi to run everything, even bringing a lot of these extensions into Archon workflows. So earlier I teased this planotator workflow that I built with Pi and Archon. This is the YAML for it. So I'll

**[0:09:35]** link to this in the description. If you want to use PI and Archon and use my exact workflow that I've been building recently, you can do that. You can bring this into your Archon environment and just tell your coding agent, hey, here's a new archon workflow. I want you to

**[0:09:49]** help me set everything up with pi, bring in the planotator extension, and then run it on whatever repository to build out anything. So, it goes through an entire piv loop as I call it. So, you do some planning for a new feature or a bug fix. Then, you go into implementation

**[0:10:03]** and validation with the coding agent. It has human in the loop for the plan with planotator. So it walks you through the entire process but also keeps you in the loop. And so as far as how I actually built this workflow, it is so simple in archon. So wherever you have archon

**[0:10:19]** configured and of course I have the installation instructions in the readme or just right within the archon repository. You open up your coding agent and you just say I want to build a new archon workflow. Specifically, I want to build a plan implement validate workflow around the planotator extension

**[0:10:36]** for PI. So, I want to use the PI coding agent for all of my nodes. I have my codec subscription already set up. I ran the login in PI and so I want to use GPT 5.4 for my model for everything. I want to use the planotator extension. So,

**[0:10:50]** make sure that's installed for me if it isn't already. I want to have a node where I can go through the iterations on the plan in the web UI and then it goes into implementation in the next node. And so yeah, obviously this is a little bit of a simplification for what I

**[0:11:05]** actually did, but you get the idea here. Uh so by the way, it said Python coding agent instead of pi. So just make sure if you're using a speech to text tool, it spells that right. It gets pi wrong all the time for me. But yeah, this is

**[0:11:16]** just generally all you have to do to build an archon workflow because it has the claude code skill for archon. It knows how to build and run workflows and guide you through that process of defining everything. And so all this together is what led to this workflow that we're looking at right here. All

**[0:11:32]** right, so let me show you really quick how this works. Then of course I'll show it to you in action. And so the first thing that I'm doing here is I'm actually setting cloud code as a primary provider. I'm using this workflow to show you that in archon we can mix

**[0:11:45]** providers between different nodes. A lot of people love using claude for implementation, then codeex for validation or here we're using PI for planning. So we can mix and match to our heart's content with both models and providers. So I start with a clarification phase. And so we just want

**[0:12:00]** to have the coding agent ask us a few questions, make sure it understands our request going into this piv loop here. So we're doing claude for that. And then we go into the PI session. So we change the provider to PI. We're overriding this at the individual node level. And

**[0:12:14]** then we're using OpenAI codecs with GPT 5.4 Mini. There's no separate authentication you have to do with PI in Archon. If you installed PI and you ran SLOG and go through that process like I showed earlier, then Archon can use those same credentials. So nothing else that we have to set up here. And so I'm

**[0:12:31]** just saying you're in Planotater plan mode. Your only job right now is to write a good plan.mmd and submit it for a human approval via this tool that comes with the planotator extension for pi. So, I did a little bit of research to craft this prompt here with the help

**[0:12:44]** of Claude code, but yeah, pretty much it's going to create this markdown document and then render that in the website here. So, we can provide the feedback in real time. I'll show you this in action in a little bit. And so, it's going to create these tasks here

**[0:12:57]** and it'll iterate on the plan when we give feedback. Once we approve, then we go into implementation with Claude again. And so it's going to essentially do a RA loop knocking off the tasks one by one creating a commit for each and then we have the validation at the end

**[0:13:11]** here just sort of doing like a full sweep kind of like a pull request review right like now that we have all the commits let's do a review on everything so pretty simple workflow overall but it's showing using PI and extensions and different providers and the piv loop

**[0:13:25]** which is my core methodology for AI coding. So yeah this is a great workflow. Okay so time to wrap things up by showing you this workflow in action. So I'm just going to be very brief here. So I have this sample application that I built for the sake of demo. GitHub issue

**[0:13:39]** triager. So just a dashboard that helps me manage my issues in a repository. One thing I don't have here is a theme toggle. There's no light theme, no way to switch to a light theme. So we can build that with this PI planot piv loop workflow. So I'm going to send in this

**[0:13:54]** prompt right here. And so I'm telling it to use the archon CLI to run this workflow. Giving it the path to the repository so it can run the CLI there. And I'm just describing very quickly what I want to build a light dark theme toggle. And so you can run this wherever

**[0:14:09]** you have archon set up. It's going to use the archon skill so it knows how to run the archon CLI to start this workflow. And so the first step here is going to be the clarification questions. We'll see that pop up in a little bit. All right. So here are our three

**[0:14:24]** clarifying questions. We'll just answer these really quick. Then we'll get into the planotator step. So for number one, sure, let's migrate to CSS custom properties. For the light theme colors, I want you to just figure out what's reasonable. And then for the toggle UI, let's do a sun moon icon button. There

**[0:14:40]** we go. So speech text for the win. Send this in. Now it's going to resume the archon workflow. So this is a human approval gate essentially, right, for these clarifying questions. Now we go into the planning process. So I'll come back again once we have that planator UI

**[0:14:54]** for us to review the plan and iterate. All right, so here we are. I just asked it to give me a status update and it gives me the URL saying that's ready for me to now review the plan. So because everything runs internally in that PI node, it's not like it reports to us

**[0:15:07]** automatically once the website is up. So we could just ask it for a status update or check this every once in a while. So here we are with our plan rendered. And now we can give feedback freely throughout the entire thing. So just for the sake of the demo, I'm going to say

**[0:15:20]** that most this is good. But let's say for example, we want to do more validation here. So I can highlight this entire thing. I can add a comment here and say validation isn't quite good enough. I also want to do browser automation testing with the agent browser CLI. I love using this as a tool

**[0:15:38]** to navigate through website just as a user would to make sure that we can you know for example toggle the theme view the light theme make sure that all looks good. So I can add my comment I can add any more if I want as well and then I

**[0:15:49]** send in my feedback. And so now the Archon Pi node will resume. It will produce a new plan or I should say an updated plan and then I can review again. All right. So I asked for another status update and now it picked up my feedback and revised the plan. So now

**[0:16:05]** going to the browser. Sure enough, invalidation. We have a new bullet point now to use the agent browser CLI for browser automation testing against the running application. So all right, I think this is really good. So now what I'm going to do is click on approve. And you could go through more iterations if

**[0:16:19]** you want, but I'm going to approve it. And then the archon workflow is going to continue going into the implementation and then validation steps. All right. And then after the plan, obviously, there's no more human in the loop. So the workflow goes through all of the implementation and validation, knocking

**[0:16:34]** out all of the tasks. We have our work done in a work tree. So then in order for me to actually test it myself, I just had it copy over the ENV into my work tree for the environment variables and then spin up the front end. and then

**[0:16:46]** going into our browser. Sure enough, take a look at this. We now have the theme toggle and the light theme is looking really good. So, we used Pi for the planning with the Planator extension. It's so cool how easy it is to bring extensions from Pi into the

**[0:17:00]** ecosystem and then plug it right into our Archon workflows. So, there you go. That is Archon and Pi. I love using Pi as a foundation and building things on top. And of course, you could always use the plug-in marketplace for cloud code to add more features there. But my

**[0:17:15]** question for you is why do you want to keep adding more features onto something that's already bloated? That's why I like using Pi as a minimalistic starting point, adding in the capabilities that I need. And I love doing that, adding these extensions and then wrapping everything in these archon workflows. So

**[0:17:31]** I'd encourage you to do this yourself. I will link to the workflow in the description that I just ran through with you as well if you want to try. And so if you appreciated this video and you're looking forward to more things on AI coding and archon, I would really

**[0:17:44]** appreciate a like and a subscribe.
