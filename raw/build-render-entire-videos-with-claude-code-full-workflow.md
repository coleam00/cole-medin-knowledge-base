---
type: raw-transcript
title: "Build + Render ENTIRE Videos with Claude Code (Full Workflow)"
youtube_id: Ya51a1EJPZk
url: https://www.youtube.com/watch?v=Ya51a1EJPZk
slug: build-render-entire-videos-with-claude-code-full-workflow
published: 2026-05-13
duration: "0:15:14"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** If you were to ask me even a few months ago if LLMs are able to generate full videos with animation and audio end to end, I would have said not yet. It's theoretically possible, but you're not going to get the best output. But just like everything else in the AI space,

**[0:00:16]** this is changing very quickly. This is what I'm going to show you how to do in this video. But this YouTube short that I'm showing you right here is generated entirely by AI, including audio that I just have muted right now that syncs with all the transitions, everything

**[0:00:30]** that you're seeing on the screen. And there's a few different technologies that I've stitched together to make this happen. It's super cool. And the biggest kit on the block here is HyperFrames. This is what lets our AI agents render these scenes and have that editor that I was just showing you. So, this is kind

**[0:00:47]** of like Remotion. It went viral a couple of months ago for really the first tool that had a skill giving Claude code the ability to generate videos wasn't really the most reliable in my experience. Hyperframes is definitely a step up and so I've taken hyperframes and I have

**[0:01:03]** combined it with a couple of things. So obviously Claude Code and then I'm using 11 Labs for my voice, Kokoro if you want something free and then I'm using Archon as the workflow manager to orchestrate everything. And so I have this as an open- source repository. You can

**[0:01:20]** download and try this right now. Literally just ask your coding agent to set it up and you can have your own AI generated video up and running in less than 10 minutes. I'm going to show you how to do that and exactly how this workflow works. It's pretty cool how we

**[0:01:33]** do the scripting and then we sync the audio with the different scenes. A lot of customizations you can do for this as well. So I want to start by saying that AI generated videos are not perfect yet, but man are they getting good. There are still some issues with voice inflection,

**[0:01:48]** slightly awkward renderings or transitions, but it is getting to the point very quickly where there are some real use cases for AI generated videos, especially just creating explainers for your team or a community, whatever. Even just creating YouTube shorts like that's what this repository is specialized in right here. And so I would consider this

**[0:02:08]** more an ongoing experiment versus something that you can use and expect to get production quality right out of the box. But I have also made it really easy for you to not just try this quickly, but also customize it to your own needs. And that's what I'll talk about in this

**[0:02:21]** video as well. And so literally once you have it set up, and you can ask your coding agent to do so, all you have to do is give it an idea. This can also be a URL, like if you wanted to create an explainer for a blog post, for example,

**[0:02:33]** and it's going to go through the full workflow of scripting it out, generating the audio, rendering the visuals, and syncing everything together, giving you the final video ready for you to review. and iterate on and then post once you are ready. And so all you have to do is

**[0:02:47]** start by cloning this repository. So I'll grab the URL here. And then you'll just run a get clone with that URL. I'm not going to do it here cuz I already have it cloned. Change your directory into there. And then open up cloud code in the repository. And then like I show

**[0:03:00]** in the readme, all you have to do to get everything set up and generating your first video is send in this prompt. Just two sentences. Read the readme. Set up everything so I can generate my first video. and then you give it the idea or the URL that you want to generate the

**[0:03:14]** video around. It is that easy. Now, obviously, this is a bit of an oversimplification. You're probably going to want to customize the style and the theme and the scenes. That's what the second prompt is for, but either one you send it in and now the rest of the

**[0:03:28]** readme, I know it's pretty long here, but it's really just instructions for your agent to walk you through everything. It'll install all of the dependencies and everything is free unless you want to use 11 Labs, which it'll walk you through setting up your API key and everything. If you do want

**[0:03:42]** to use 11 Labs, but if you want to use Cocoaro to make it completely free, you definitely can because Hyperframes for the rendering and then Archon, which is my harness builder. This gives us the workflow engine. All of this completely free to get up and running. So, very

**[0:03:58]** easy to get started. I'll talk about how you can customize things in a little bit as well. So, for example, with the video that I showed you at the start, I just said read the read me to set up everything. The topic is Claude Code agent view. This is the latest edition

**[0:04:10]** of Cloud Code. It's pretty powerful. So, I thought it'd be a good demo for our video here. And then I'm telling it to use the anthropic template. So, obviously, we need some kind of template that dictates the length and the content, what's rendered, and the style. So, there's three that I have shipped by

**[0:04:26]** default that you can use. I would also highly encourage you to just point your coding agent to look at these for inspiration and tell it to make one that is styled in the way you want it with the length and the content that you want. Very easy to do that. So I just

**[0:04:39]** ran this with one of the default ones and it goes through the entire workflow. Simple request leads to this entire workflow being executed here. All the steps that I'll explain after our quick demo here. And so it's going to generate all of the assets just self-contained in a single folder. So, it's really easy to

**[0:04:57]** manage everything per run. So, we have all the web research going into the script. Then, it creates the audio and the assets and composition. It syncs everything together with transitions. Very comprehensive workflow here. Definitely needs a harness to guide everything. And so, that's where Archon comes in. It's my open- source harness

**[0:05:14]** builder. I've covered a lot on my YouTube channel. It's not really the point of this video, but it is an important part of the tech stack here. So, this is one of the things that your coding agent will install for you. Very easy. and has a light footprint as well.

**[0:05:29]** Just an important part of the stack here. And then for the database that manages all the workflow runs, you can use SQLite or if you want something a bit more reliable, you can also use Postgress like I'm using neon here. So every single video that I generate the

**[0:05:41]** workflow state and everything is persisted into my neon database. You can see all of my individual runs. And also because we're using archon here, it supports parallel workflow execution. And so I can also generate a lot of different videos at the exact same time if I wanted to do so. But anyway, right

**[0:06:00]** here I'm just generating one video. So let me go ahead and just shut up play this for you so you can see the 25 seconds that Claude Code generated with this workflow. All right, here we go. >> Claude Code just went async. Agent view manages all your running sessions from

**[0:06:14]** one terminal. >> One command, Claude agents. Track all six session states at a glance. See every agent status in real time. Send sessions to the background and return when needed. Use /Gal for fully autonomous runs. Try it now at anthropic.com. Follow for more Claude Code updates. All right, that is not bad at all,

**[0:06:36]** especially cuz I did no iteration on it and I really didn't give much guidance for the actual content that I wanted and so I could have taken that a lot further as well to make it more concrete. But that's good. Like the audio was perfect. The transitions were great. Everything

**[0:06:50]** was synced phenomenally. That's part of the validation that's built into the workflow as well. So pretty much the entire workflow can be boiled down into this claude code skill that's wrapped in the archon workflow for parallel execution and durability. And so this accepts as input what you want to

**[0:07:06]** generate the video on. We have our core mission here. And then we have the playbook. This is what tells cloud code how we're going to use cocooro or 11labs, how we're going to use hyperframes, how we're going to stitch everything together. And this is custom to the template that I'm using. And so

**[0:07:22]** this is one of the files that you'll customize when you want to change the scenes and the length of the video, everything like that. So this is for the classic template that I used to generate that claude agent view video. And so of course I got an Excal diagram just to

**[0:07:36]** really quickly explain everything that goes into this. I think you'll really appreciate the workflow when you see how much prompting and you know step-by-step process that we have laid out here. And so we're going to start by creating a unique identifier for the video. This is so we can create an isolated environment

**[0:07:52]** to manage everything in the archon workflow also so that we can have the execution saved in our neon database here. So we create the ID and then we're going to copy the template in the isolated folder for this workflow run because remember we're managing all the assets and the output and everything in

**[0:08:11]** a single place. So we copy the template as a starting point, set the video metadata, and then we're going to research the topic. We don't want to assume that cloud code knows everything about the topic we're going to generate the video on. So it needs to do research. We have an anti-fabrication

**[0:08:25]** gate as well. So it's not just hallucinating everything. And then from the research, it's going to create the script. And the cool part here is the script is more than just the text that we're going to say. There is a lot of prompt engineering that goes into adding

**[0:08:39]** in tags and breaks and natural abbreviations to really optimize for our text to speech once we pass things into 11 Labs or Cocoaro. And so once we have everything ready, then we're going to make a single call to 11 Labs, send in the full script, get the audio out, and

**[0:08:56]** then we're going to sync the animation timing to the video. And so before we really start rendering things, we're going to decide, okay, based on the audio here, how do we have to paste the different scenes that we want to create with Hyperframes? And so then we create

**[0:09:12]** this index.html. This is what I love about hyperframes. It's literally just HTML. It's super easy to create and mold. So we build the composition based on the audio. We do some linting, so just making sure that our audio is good, the transitions are good, everything like that. We inspect for the layout

**[0:09:30]** overflow just to make sure that there are no text or visual elements that bust out of their containers. So basically we have Cloud Code look at it frame by frame to make sure everything looks good for the entire video. And then we open up the preview. And so this is what I

**[0:09:44]** was showing in the browser earlier. I'll pop back over to that. We have this preview mode that's built right into Hyperframes. This is not a dashboard that I had to build myself. This allows us to see you can see the sound effects here and the audio. And then we can

**[0:09:58]** obviously scroll through this and see the different slides and animations. And so we have the opportunity here to review things and make adjustments before we actually have it render the full MP4. So we can even like change things in line here in the dashboard. It's really really cool. So this is a

**[0:10:15]** big part of the workflow as well. That's why I love hyperframes. And so we have the preview URL. So this is just like a local host browser page that we can open. And then once we're happy with everything and maybe we've iterated with claw code, then we can create the MP4.

**[0:10:29]** And so this is our opportunity here to say like, hey, the audio has a weird inflection at this point or the sound effect is really awkward for the transition here. Like whatever we want, we don't have to rerun the entire render cloud code with this whole workflow that

**[0:10:43]** I have set up for you and the skill. It's able to make those granular adjustments because the video is probably not going to be perfect on its first pass. the information, the transitions, the scenes, whatever. You're probably going to have to make some adjustments, but you can do all

**[0:10:57]** that and then render the final MP4 when you are happy. Cool. And just for fun, let me show you another video that I generated with a custom template that I created. And I'll show you at the end here how to create templates as well. So, this is a template for Archon. And

**[0:11:12]** this video is just a 30- secondond explainer for what Archon is. I also tried to use one of my clone voices in 11 Labs, but it actually takes a lot of work to make that reliable. So, just to show you something more fleshed out here, I have one of the more generic

**[0:11:27]** voices. But take a look at this. It's actually really good. Archon is an open- source AI coding harness built with Claude Code. A genic workflows isolated running in parallel. 21,000 GitHub stars and counting. One isolated Git work tree per task. Clean, safe, and fast. Three core workflows out of the box.

**[0:11:46]** PIV plan implement validate fix. Turn GitHub issues into a PR. Review with five parallel agents. Start free at archon.diy. One command and your AI dev team is ready. All right. Pretty good. A little slow paced overall, but I like the explanation quite a bit. So there you go. A couple of examples there. Now the

**[0:12:07]** last thing that I want to show you just so you can really take this as your own, I want to talk about how you can build your own templates. So, I want to reiterate that the three templates that ship with this repo for you are really just examples to get you started when

**[0:12:21]** you want to build your own videos. Really, what you do is you have Cloud Code read the readme, but instead of helping you with this setup now, it's going to help us build our own template. And then just for an example here, I'm saying that I want a template for

**[0:12:33]** explaining tougher AI concepts or tougher to understand concepts. And so now this is going to really kick off a process where Claude is going to go through a set of questions to understand what we're going for here and then build that custom template for us. And so first it asks like, you know, out of the

**[0:12:50]** ones that shipped, what are the ones that match what we're looking for the most? I'm really saying I want something pretty new here. I need a new explainer style video and I want diagrams before and after analogy panels for the brand. I just want something clean and educational. And then for the topic

**[0:13:06]** scope, let's just say that I want to cover uh architectures and techniques in the AI space. So, so I'll submit this. Maybe it'll ask me some more questions. Maybe it'll get right to creating the template. Just take your time, go through this process. I'll come back once this is done and I have a new

**[0:13:20]** template to show you. And boom, there we go. After quite a bit of work, cuz there's a lot that goes into creating these templates, Cloud Code has created the new concept short template for me. So now I can ask it to create videos to explain things like rag attention MCP

**[0:13:36]** and it'll know to use this template out of all of the other ones. And so if I go to like even a brand new cloud code session here and I say create a video on MCP, it'll know because of the project we're in right now like okay, we got to

**[0:13:49]** read the read me. Then let's look at the templates that are available and pick the right one. And it will pick the one that we just created here. And so now we have a template that's customized to these kinds of videos. Like for example, we're defaulting to the 50 second range

**[0:14:04]** instead of like 25 to 30 seconds like the other templates. So we can change style composition length everything to fit the exact kind of video that you want to generate. So just trying to show you at the end here how you can really take this and run with it to create any

**[0:14:18]** kinds of videos that you want with Archon, hyperframes, and clawed code. So there you go. That is how you can generate videos pretty reliably now with Claude code audio animations everything. And one really cool use case I didn't talk about earlier is you can even use this to generate explainer videos for

**[0:14:37]** just yourself like when a new Cloud Code feature comes out like agent view for example. Just have it explain it to you in a minute or 30 seconds instead of watching a longer YouTube video or going to the claude code docs. Of course, that's useful as well, but it's just a

**[0:14:51]** really cool use case for something like this. And it's so easy to get this up and running. I would highly encourage you just try this. It's free. Get it up and running in 15 minutes or less. Generate some videos and just have fun with this. And so, if you appreciated

**[0:15:04]** this video and you're looking forward to more things on cloud code and AI coding, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
