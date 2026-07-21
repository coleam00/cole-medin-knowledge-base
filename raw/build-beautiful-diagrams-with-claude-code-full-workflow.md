---
type: raw-transcript
title: "Build BEAUTIFUL Diagrams with Claude Code (Full Workflow)"
youtube_id: m3fqyXZ4k4I
url: https://www.youtube.com/watch?v=m3fqyXZ4k4I
slug: build-beautiful-diagrams-with-claude-code-full-workflow
published: 2026-03-02
duration: "0:09:54"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Most people are visual learners. I am myself. You probably are watching this video. The problem is coding agents like Claude Code are not very visual tools. When you want it to explain something to you visually or even just help you explain something to someone else, they really don't do a good job unless you do

**[0:00:18]** a lot of prompting and give it the right abilities. And that is what I have been working on. So, I love using Excaladrop for all of my diagrams. You've seen this before if you've been on my channel or in the Dynamis community. I build dozens of these every single month. And so I've

**[0:00:35]** taken my entire workflow and I've packaged it up into a skill so I can use Claude code or any coding agent to help me build all these beautiful and practical diagrams. And so giving my coding agent the ability to argue visually. And so right now I want to

**[0:00:50]** share this skill with you, my entire process packaged up so you can use it right now. So I will have a link in the description to this GitHub repository that says everything for the Excal diagram skill. It is pretty simple overall. So you just clone this repository and then you create a new

**[0:01:06]** folder in your do.cloud/skills or whatever it is for your coding agent and then you just copy over everything from this and it is going to work no matter your coding agent. So I'll show you my setup really quickly. Here I have my doclaude skills directory. I created a

**[0:01:20]** new folder called Excal diagram and then I just dumped in everything from the repo including the skill.md. This is the primary instruction set that guides claude code how to argue visually creating the JSON files for these Excal diagrams. And I know this is super meta, but I use the Excal diagram skill to

**[0:01:40]** create this diagram to explain the workflow to you so you understand how it works. And I iterated a couple of times to get to this point, but this is the kind of thing that you can generate with this skill. All you have to do, I'll show you a really quick demo of this

**[0:01:52]** right now, is go into cloud code and just say, "Hey, I want to create a diagram to explain." And then I could just like give the path to this file for example. You could also give it the path to maybe like a YouTube script. I do that all the time to help with my

**[0:02:06]** YouTube videos. You can have it build a diagram based on a PDF document. Like it can be literally anything. And so you just send in this prompt and then claude code or whatever coding agent is going to be smart enough to know like okay let me go ahead and load in the skill and

**[0:02:20]** that brings in the entire workflow. So basically we're giving it a very articulate prompt how to generate the diagram and validate it as well. And once your coding agent outputs the JSON for the Excal diagram, you can just go to excalraw.com and load it from your local file system or you can use the

**[0:02:40]** Excal plugin in Obsidian. Both are very valid and excal.com is entirely free. So very easy to render these diagrams once you have them. And my favorite part about this workflow is not only does it create the Excal diagram, but it also validates it visually. So it will render

**[0:02:56]** the diagram, take a screenshot, look at the PNG, and then iterate on any of the imperfections. And I just get insane results with this workflow when we have this self- validation. Cuz like I said earlier, coding agents are not the best at visual tasks. they need the ability

**[0:03:12]** to check their own work and we can do that with Excal. So I'll show you an example really quick of an image that it rendered after it built the diagram. So it's looking at this directly to see if there's anything off with the visual flow, the hierarchy of information, all

**[0:03:26]** the things that I have prompted into the skill.md and it uses a Python script in order to do this rendering which that's really the only setup that we have for this skill. So, I cover that in the readme here, but honestly, the easiest thing is you can just ask your coding

**[0:03:40]** agent to help you set up the Excalra diagram skill because then it knows to read the readme and it'll pretty much just go through the manual steps on its own so that by the time it's your turn to use the skill, everything is all good to go and you can just simply ask it to

**[0:03:56]** build any kind of diagram like I showed in the simple demo earlier. Now, one very important thing to keep in mind, no matter how well-designed this Excala draw skill is, and I have been iterating on it constantly, it is not going to be perfect. For example, this meta diagram

**[0:04:13]** here that explains the workflow. It took me two or three iterations to get to this point. This is the original diagram that the skill with claude code produced for me, which it still looks pretty good, but you can see there are a couple of imperfections here. Like I feel like

**[0:04:26]** the arrows look a little jank, for lack of better words. This arrow is too short. I don't quite like the colors. I feel like there's not enough information displayed here. So, I have my critiques. And it's very easy though to iterate on this. Just a couple of directed updates

**[0:04:42]** with my help to get to the point where we have something more like this. Now, the reason that it's never perfect at first, it actually makes sense when you think about how much the large language model has to produce for this diagram. Cuz think about this. It has to decide

**[0:04:57]** every color, every shape, the entire layout, the position of everything. There's so many micro decisions going into creating just this single rather simple diagram. And so it's always going to be imperfect, but it's easy to get to this point. That's the important thing is getting the starting point with this

**[0:05:12]** skill for you to apply your own reasoning for how you want it to evolve and the exact information that you want to display. Cool. Cool. So, the last thing that I want to cover with you is the workflow, at least at a high level, especially so you know how to customize

**[0:05:27]** it to your own liking. We'll also talk about the color palette. That's one of the most important things to make the diagrams on brand to you or just the color scheme that you like using. So, the core philosophy that I have built a lot of prompting around in the skill.md

**[0:05:42]** is teaching the coding agent how to argue visually. So explaining that like we don't just want to put things in a bunch of blocks because when it generates Excal diagrams without this skill, it's very blocky for lack of better words. But instead, we want to argue visually, we want the structure

**[0:05:58]** and labels to explain the entire concept. So even if we strip out all of the explanatory text from the diagram like this, we would still be able to understand what we are arguing visually in the diagram. And so there are two main questions that I have the coding

**[0:06:14]** agent ask itself in the workflow. First, does the visual structure mirror the concepts behavior? And then also, could someone learn something concrete from this diagram? I'm very educational focused on my YouTube channel as you probably know. So I want these diagrams to be very complimentary to exactly what

**[0:06:31]** I'm trying to explain in the content. And then for the workflow itself, it just starts with your idea. So this skill is assuming that you already have a good idea what you want to create a diagram for. So you can iterate with your coding agent before you load this

**[0:06:44]** skill and then have it first assess the depth of the diagram. And the reason this is important is because we have very simple diagrams like this and then we have more complicated ones like this. Maybe this is a better example as well. And the reason we need to assess the

**[0:07:00]** depth is because for more complicated diagrams we have to build them section by section. Otherwise, you'll get an error with clawed code where it's trying to output more than 32,000 tokens. There's a limit there. So, we have to build it section by section because these diagrams, they take quite a few

**[0:07:15]** tokens. It's definitely worth it, but it does take a while to generate these. And so, after it assesses, do I need to build it all at once or in chunks? Then, it's going to map the pattern. So taking our idea and thinking about what shapes do we need, what text do we need in the

**[0:07:29]** diagram, putting that all together to then build the JSON file that we can render with the Obsidian Excalibraw plugin or an excalraw.com. But after before it comes back to us, it goes through the validation loop. This is what I was talking about earlier where it renders the PNG, views the

**[0:07:45]** image, finds any imperfections, and then it'll just make direct edits to the JSON file it already created. So it's not like it has to spend all the time to create a duplicate or anything. Usually, it'll iterate like two to four times. Not that it's going to fix everything by

**[0:07:59]** the time control passes back to us, but it is going to be a fantastic starting point. I also have all of my design patterns laid out in the skill.md giving it examples of visual patterns, telling it to not do boxes and boxes and boxes. These are the kinds of things that

**[0:08:15]** coding agents will do without guidance because they generate excal diagrams that are always way too simple and look the same every single time when we don't have this kind of workflow. Multi-isoom architecture again just things for variety. We have the color system so I can be consistent in the colors for my

**[0:08:32]** diagrams. And then also the evidence artifacts. So being really specific for the kinds of elements that I want to really make my diagrams educational. And these are all the things that you can tune for yourself, especially the color palette. So I'll go back to my skill here and show you that one of the files

**[0:08:48]** that I referenced in the reference folder of the skill. This is in the GitHub repo as well is the color palette. And so you can just ask your coding agent like, hey, I want to use purples and yellows instead of blues or whatever, right? And it can create the

**[0:09:01]** hex codes and like put all this in the color palette so that way when you are generating diagrams going forward, it's your brand and the color scheme that you want to use. And so you can edit this, you can change the different element templates that it can bring in. All of

**[0:09:15]** this you can tune yourself, but also it all works out of the box if you just want to use it right away. So a very flexible skill that I have built for you. So there you go. That is the Excaladra diagram skill. And I encourage you to clone this repo, bring in the

**[0:09:29]** skill, and just try it right now on a PDF, even a code base. You could do research you do with an agent or just raw text. The possibilities are endless. And it does such a good job creating a starting point. literally saving me hours and hours every single week. And

**[0:09:42]** so, if you appreciated this video and you're looking forward to more things on skills and agentic engineering, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
