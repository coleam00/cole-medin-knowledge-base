---
type: raw-transcript
title: "GitHub is the Future of AI Coding (Here's Why)"
youtube_id: upwbqZ67UBA
url: https://www.youtube.com/watch?v=upwbqZ67UBA
slug: github-is-the-future-of-ai-coding-heres-why
published: 2025-11-12
duration: "0:24:01"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** The future of software is leaving most, if not all, coding up to AI, and I will die on that hill. But also, it's not that simple. We're never going to have this magic box, this single chat input where we can tell AI what we want it to build and it's going to get it right

**[0:00:16]** every single time. That is just never going to exist. And the main reason for that is we are always going to have a need for what I like to call the orchestration layer. It's a place for us to perform task management, track changes in our codebase, version control

**[0:00:33]** it, even make a different assignments to different coding agents we have on our AI dev team. And GitHub or something similar like GitLab is the perfect solution for this. That's why I'm saying GitHub is the future of AI coding. And so in this video, I'm going to be giving

**[0:00:49]** you a glimpse into the future of AI coding and how you can get started with this right now because we're going to be integrating three different AI coding assistants into a GitHub repo. And I'll link to the workflows in the description. So you can take them, customize them to your project, and then

**[0:01:05]** incorporate them literally anywhere. And so we've got cloud code, codeex, and cursor. We can even run all these at the exact same time, handling different issues and pull requests. We can extend this to work with other coding agents like Klein. It's really powerful stuff. And yeah, call me crazy for building

**[0:01:23]** this many coding assistants into our workflow here, but I'm doing this for two reasons. First is I want to show you that we can do more than just use cloud code. I know I cover it all the time on my channel, but I want to show that really any AI coding assistant can work

**[0:01:37]** with what I'm showing you here. And then the second reason, and these are the workflows that I'll cover with you in this video, each one of them is structured a little bit differently. So, I'm using three coding assistants to demonstrate three different approaches for building our coding agents into our

**[0:01:52]** GitHub repos. And so, we'll get all into that because really I want this to not just show you how to build an AI coding assistant into a GitHub repo, but help you think about the different approaches and which one would work best for you. So, let's get right into it. I'll show

**[0:02:06]** you how the sausage was made and then we'll get into the different structures for our workflows here. And so for all of these coding assistant integrations, I'm using GitHub actions. It's the tooling for CI and CD built right into GitHub, which is freaking awesome. And it's actually so easy to build these

**[0:02:23]** workflows. Like once I dive into each one of these with you, I think you'll be pleasantly surprised how simple they really are. So each one of these workflows has a trigger. So I make a specific comment in an issue or a pull request and then it starts this flow

**[0:02:38]** that invokes one of my AI coding assistants. So let me show you this right now. So I'll go to the root of my repository. I'm just using a Pantic AI agent I built in a previous video as a demo and let's go to the one issue here. I've got uh something set up ahead of

**[0:02:53]** time to show you how this all works. And so this is an issue that I actually did notice for real in my GitHub repository. And the technical details of this don't matter. I just found some problem and I created an issue in my GitHub repo to report this. And now what I can do, take

**[0:03:08]** a look at this. I can do at@claude-fix. This is the trigger keyword that invokes this workflow where claude code. It's going to analyze the issue and then start digging into the codebase, doing a root cause analysis, and then implementing a fix, and even making it so I can click a button right here to

**[0:03:28]** create a pull request for the fix that it's done. It's so cool. And it's very similar for our other coding assistants. I can do at codeex fix, at cursor fix, and boom. Both of these, I made this simpler on purpose, but they create a pull request as well, and they even link

**[0:03:43]** to it. So now I can go to my pull requests and I have two right here cuz I didn't click on that button to create one for cloud code but for codeex and cursor I have the fix implemented from each of them. And then the other thing that I can do is have my coding

**[0:03:57]** assistants review my PRs as well. So at claude-review. So I'm having Claude review a poll request made from cursor. And I'm doing this all within just minutes. It's so cool. And so it does the full review here. And then going to the poll request from Codeex. I just had

**[0:04:12]** cursor review it at cursor review and there we go. And everything is really well formatted. Everything is super fast going into the workflow runs in the actions tab right here for GitHub. It's also really easy to like look at the progress of things. So I can filter for

**[0:04:26]** the tasks that are in progress, the ones that are successful. So I can look at past runs as well. So we have a lot of like logging and observability into this, but it's still just like really convenient and built right into GitHub. The beautiful thing with this is I'm not

**[0:04:39]** running anything on my own infrastructure. This is all just environments that are spun up in the GitHub infrastructure whenever we invoke one of our coding assistants. So with that, let's get into the details of things more. I want to show you what these different processes look like, even get into the workflow code a little

**[0:04:57]** bit. And so I'll show you how these all work, then I'll do a full-blown demo at the end. And again, all these workflows are available for you to download and build into your own repositories. And so starting with cloud code, it's my example for you of a hybrid approach.

**[0:05:12]** And what I mean by hybrid is there are some parts of the process that we prompt the coding assistant to do. And there are other parts that we have built directly into the workflow like deterministic code or we handle as the user. And so for cloud code, going back

**[0:05:26]** to the issue here, instead of creating the pull request autonomously like cursor and codeex did, and I'll show you that in a little bit as well, it just makes a comment here in the issue with a button for us to click. So we are still in the loop. We get to decide when we

**[0:05:40]** create the pull request and we can even iterate with cloud code on the issue in the comments right here. And so the way this flow looks is we open up a GitHub issue. This could be a bug or even a feature that we want it to build. And

**[0:05:52]** then we at cloudfix mention it, right? And then we can even add any extra context here that we want like how we want to go about fixing the issue. And so we're not limited to just including this in our comment like I showed earlier. And then at this point, Cloud

**[0:06:06]** Code is going to create a feature branch to do its implementation. It'll analyze the codebase and fix whatever it needs to fix. And so it'll actually like clone the repository in this little Docker environment that it creates to handle things as a one-off implementation. And then once it does its fix, then it'll

**[0:06:22]** create that comment that we saw with the button for us to create the poll request. And then if we're good with its changes, we can click that button and boom, the pull request is ready. So it's pretty end to end, but also we still get to be in the loop. And so definitely

**[0:06:35]** like it isn't as quick going through this process because we have to be a part of it. But if you want to validate things, then the hybrid approach is very powerful. So now with the codebase opened up, I want to show you these workflows, at least give you a nice

**[0:06:49]** overview of how the sections are pieced together. And so I'll link in the description to the workflow folder directly so you have access to all of these. You can bring them right into your GitHub repos and even ask an AI coding assistant to help you customize it to your project. And I'll also link

**[0:07:04]** to the video right here where I built this Pantic AI research agent. It's a pretty cool agent, but not the focus of this video because I want to talk about our workflows. And so let's actually open up the first one here. This is claude fix. And so whenever we have a

**[0:07:19]** comment on an issue, then we're going to run this workflow. And I have security in place immediately where only certain users are allowed to invoke Claude in an issue. And so this way I can actually have this workflow in a public repository and not everyone can just go

**[0:07:36]** and and use my Cloud subscription and have Claude make edits on my codebase. And so I actually took inspiration from the workflows that I have in archon for what I'm showing you right now. So we have this exact same thing but we just protect so that only maintainers are

**[0:07:51]** allowed to invoke cloud code with this command. We give it the necessary permissions that it needs and then we start by checking out the repository. So we create this isolated environment for this GitHub action run. We bring the codebase into it and that is where cloud code is going to implement its fix. And

**[0:08:08]** so everything that we're doing right here is just loading this preconfigured prompt that I have describing how it can fix this issue. And so you can think of this like a slash command. It's a reusable prompt that we're actually using between all of our different coding assistants. And so if we're

**[0:08:24]** fixing with claude, codeex, cursor, it doesn't matter. They're all going to reference this specific prompt to go through the process, which also includes reading our agents.md for example. So we're bringing in global rules that's standard for every coding assistant as a part of this process as well. And then

**[0:08:41]** we also have some parameters that we replace as a part of our workflow for things like the name of the AI assistant. So that way all of our branches are named with a suffix representing the coding assistant that's actually operating on that branch. So we're keeping things very organized and

**[0:08:56]** being able to distinguish between the different dev team members that we have our different AI dev team members. So after we load the instructions, then the actual part of the workflow to trigger cloud code is super super simple because we have this preconfigured action that we're able to bring into our flow. So

**[0:09:17]** Anthropic has their official cloud code action for GitHub actions. We just have to pass in our GitHub token so it can do things like make comments on our issue. And then I'm passing in my Claude code ooth token, which if you didn't know, you can just go into your terminal and

**[0:09:32]** do claude space setup- token. It'll give you this permanent token or at least it doesn't expire for an entire year. And so that way I can use my anthropic subscription. So I don't have to use an API key that is a lot more expensive. We have our trigger phase. Then we have the

**[0:09:47]** custom instructions where I'm just passing in the prompt that I loaded in from the markdown document. and then just an unauthorized message that I share if the user is not in that list of approved people at the top. And like that's literally it. It's barely over a hundred lines of code. Really simple.

**[0:10:04]** But this is all of the power of Cloud Code operating on any issue that we call upon its help for. And something interesting about the Cloud Code integration is that nothing in our workflow actually creates the branch or makes the comment on the issue. That is all done by Claude Code itself. And so

**[0:10:22]** it's pretty much autonomous in that way besides the hybrid thing there where we get to create the pull request. But sometimes you don't want the coding assistant to be responsible for creating the branch or creating the pull request or commenting on the issue. You want that to be built into the workflow and

**[0:10:38]** then you only want to use the coding assistant for the actual coding. So if you want the most control while still having the coding assistant do its thing, that's when I'd recommend the deterministic approach. And we're using codeex for this example. And so the flow starts the same. We open up an issue and

**[0:10:54]** we mention codeex. But then right away it deviates from what we saw from cloud code because claude code was the one that created the the feature branch to make the implementation that ultimately leads to the pull request. But here we're actually doing it in the YAML for the workflow. So we define the process

**[0:11:11]** and then the coding assistant only comes in to do the code changes and then after the code changes are done we return the control right back to our GitHub action workflow to create the pull request based on a summary uh that the codeex outputs and then also make the comment

**[0:11:28]** on the issue pointing to the PR as well and at this point the PR is ready and so it is more autonomous in the sense that we don't approve creating the poll request but it's a lot more deterministic stick because the coding assistant isn't doing anything in GitHub

**[0:11:42]** itself. It's only working on the code. So going to the code for this workflow, it looks pretty similar to our cloud fix one. We have the permissions at first. We're going to check out the repository in our isolated environment for the run. And then we pull our instructions from

**[0:11:57]** that template, that markdown document, and then we run codeex fix. And so it's very similar to what Enthropic has released where OpenAI has this codeex action that we can call upon. So it's barely any code for the call to the assistant itself. We just have to pass the OpenAI API key. And I believe you

**[0:12:13]** can use your codec subscription as well, but I just wanted to show you one example of using a subscription with claude. And then another example using an API key with codeex. And then we have this output file. And this is actually really important because when we create the pull request, since the coding

**[0:12:29]** assistant itself is not doing it, we need to have some kind of summary of what it did. And so we have it output to this file. And then you'll see here that we're referencing this when we are preparing the PR body. So now this is something we did not see in cloudfix

**[0:12:43]** because we are taking care of this deterministically. So we prepare the pull request body with our own code just leveraging the summary that codeex outputed and then we create the pull request and then we also manually comment on the issue as well. So we use our GitHub token which by the way the

**[0:13:01]** GitHub token is automatically available as one of the secrets that we have in our repo and so yeah we create the comment on the issue that points to the pull request and then we are good to go. That's literally it. We just have the unauthorized message handling here and

**[0:13:16]** that's the end of the workflow. So a little bit more than cloud because we're taking care of more things here. This gives us more control if that is important to you. And then cursor is definitely the final boss for the most autonomous agent. And it's not like you

**[0:13:28]** have to use cursor when you want to be fully autonomous. I just picked one coding assistant for each example. But here we create the GitHub issue. We mention cursor. And now we have the purple boxes for everything here because we're doing nothing in the workflow itself. We're just sending a prompt off

**[0:13:45]** to cursor telling it to make the branch with the GitHub CLI to analyze the code and make the fix. And then still within cursor, we are asking it to use the GitHub CLI to create the pull request and comment on the issue. And so at this point, the pull request is ready. And

**[0:13:59]** cursor did everything. And the really cool part with this workflow is it is both the simplest and the most custom. And what I mean by that, scrolling past all the stuff that we've already covered, is we install the cursor CLI ourself. And then we invoke the cursor agent in headless mode. You might have

**[0:14:17]** done this before locally on your computer. So if you're not using the cursor IDE, you can just do like a one-off request with the -p flag. And so with both codeex and cloud code, we were using that officially supported GitHub action. We weren't installing the CLI ourself or running it in headless mode

**[0:14:33]** ourself. But here this is just like straight up command line. We're installing the CLI, running it, and we're just supplying the GitHub token and then also the cursor API key. And then we have the unauthorized message handling. We're pulling in the the issue fix prompt in pretty much the same way

**[0:14:49]** like that. That's literally it. It's so simple to have cursor handle this completely end to end because as a part of this prompt and what we're injecting here we're telling it like here's the details of the issue I want you to create the branch analyze the code make

**[0:15:04]** the fix make the pull request and comment on the issue and coding assistants these days can definitely handle that much in a single request the sponsor of today's video is Sonar and their platform Sonar Cube and it's really appropriate for this video since I'm covering more of an introduction to

**[0:15:20]** AI coding workflows. For the rest of the content here, I don't really have a chance to talk about security, but it is super important. You always want to run code quality and security scans on your code, especially AI generated code. And they have an MCP server so we can

**[0:15:35]** connect Sonar Cube directly into our AI coding assistance. So, it can run the security scans itself. Literally, I could take this MCP server, build it into the GitHub workflows I was just showing you. So we could run the security scans before we make a pull request. And I'm not going to show that

**[0:15:51]** here cuz it's actually hard to see MCP usage in GitHub action logs, but we can see it very beautifully in Cloud Desktop. So I've got my repository that we've been working on in this video. I have that connected to my Sonar Cube cloud instance. And then I have the MCP

**[0:16:08]** server connected to Cloud Desktop just following their documentation. So my request can be as simple as, "Hey Claude, can you analyze the security of my podant AAI research agent with the Sonar Cube MCP server?" So I'll send this off and it's going to do quite a bit here. I'll come back once it's done.

**[0:16:25]** And there we go. We get all of our issues listed out. It even does some more research for us on the specific problems that we have. And then it gives me a final report, which this is an educational repo. That's why I have this many issues. But it even finds one big

**[0:16:38]** blocker that it gives a lot more details on. And this kind of thing is just so powerful to build right into an AI coding workflow. So I'll have a link in the description to Sonar Cube and their MCP. I'd highly recommend checking them out if you are serious about code

**[0:16:51]** quality and security. And then for all of our poll request review workflows, they're pretty simple. Actually, a lot more than the fixed ones. Like I'll just go to the cloud review one. So same kind of setup with the permissions. Check out the repository. And then we're loading the instructions where we're just

**[0:17:06]** loading the PR review prompt instead of the issue fix. So, same kind of thing where it's basically just a slash command that we're taking in as the prompt to send in that also specifies how to pull our global rules. So, we got global rules, we've got our commands,

**[0:17:18]** and then we run cloud code in the same exact way. It's going to be the same thing for codeex and for cursor, but this time it's just a different set of instructions and we're operating on a pull request instead of an issue. So, that's why I didn't cover these in a lot

**[0:17:31]** of detail here because it is a very similar setup. Like if you understand how to use Claude with the fixing or codeex with the fixing, you'll know how to do the exact same thing for the review as well. And another really important thing I don't want to forget

**[0:17:44]** to share with you is how I figured out how to build all of this. And I'm never flying blind. I'm always relying on documentation. That's the same right here. So I have a link in the description to each of the different documentation pages for the different coding assistants. Like here's Cloud

**[0:17:59]** Code and GitHub actions. They lay it out really nice and clearly in their docs here. And then for the codeex SDK, they have an example workflow. That's this one right here that I worked on top of. And then for cursor, since I was using the cursor CLI directly, I reference to

**[0:18:15]** CLI docs and they actually have an example here of a GitHub action. So literally like direct GitHub action documentation for each of the coding assistants that I'm using. And then I poked around with some other ones as well like Klein also has GitHub action integration documentation. And so

**[0:18:31]** really, no matter the coding assistant you want to use, there's going to be a way for you to incorporate it pretty much the same way that I'm showing you with these core three uh in this video here. And then the way that you set up the credentials for each of these

**[0:18:44]** services in your repo is you just go to the settings for your repository, go down to secrets and variables, click on actions, and then you set up your token or your API key. So it's pretty obvious for cursor and openai. You just go into the dashboard. But then for the claude

**[0:19:00]** code ooth token, the way you do that, I mentioned that briefly earlier, but just to show you the command visually, it's claude setup token. So you don't have to use your anthropic API key in GitHub actions. You can use your subscription, which is a lot more cost-effective. And

**[0:19:15]** I've heard a lot of people say it's not possible, but I'm doing it right here, literally. So very, very cost-ffective. And I have the security in place so that only I can be the one to call into any of my coding assistants on my repo here. So let me give you a full demo of this.

**[0:19:30]** You can see things working live. So I'm going to go to issues here. Make a new simple issue. I'll just say the readme is too long. I just want a really basic demo that can go pretty fast here for each coding assistant. So I'll say the read me is way too long. Needs to be a

**[0:19:47]** lot more concise. All right, cool. And yeah, I'll make sure everything is spelled correctly. Create the issue. Boom. We are good to go. So now we could typically like hand this off to a human to handle this. But right now, I want to let my coding assistants have a stab at

**[0:20:00]** this. I have my AI dev team. I want to orchestrate the future of AI coding. And so I'll go into the comments here. I'll say atcla-fix, handle this issue for me, please. And I could be a lot more descriptive in the issue, my comment, but again, just a

**[0:20:15]** quick demonstration here. So I'll send this off. And then I can do all of these in parallel. So I can also do codeex fix. Send in a comment here. And then I'll do at cursor fix. And so all three of these workflows are going to be kicked off at the same time. And because

**[0:20:30]** each of them suffix the branch with their name like claude or cursor or codeex, there's going to be no conflicts. We can have them all running at the same time. And so I can click on the actions tab here. And then I'll go to the status and sort by the ones that

**[0:20:43]** are in progress. And there we go. We got the yellow indicator here that cursor is fixing codeex and claw code. They are all fixing. And so I'll come back once these are all green across the board. All right, the poll requests are ready. They just took a couple of minutes each.

**[0:20:58]** And so I'll go back to the repo here. Go to our issues and let's take a look. We should have a comment for each one of our coding assistants. There we go. Claude code readme is too long completed issue and then we've got our codeex pull request and our cursor pull request.

**[0:21:15]** really really nice. I'll go ahead and click on this button here to make the pull request from Claude Code as well. So now we're up to five pull requests, the two that I had at the start of this video and then one from each of our coding assistants. And obviously it's

**[0:21:28]** probably a bit of overengineering having all of them work in parallel, but it's cool to see. And I just wanted, like I said, to show you multiple coding assistant options. And then you never want to merge a pull request without a review as well. So again, I could have a

**[0:21:40]** human do this, but I'm going to go ahead and have the coding assistants review each other. So this is our one from codeex. Let's have Claude code do this one. So atclude- review. I could add more details, but I'm just going to send that in and then go on to the next one

**[0:21:55]** here. So next up, we have the one from cursor. And so let's have Codeex review this one at codeex-review. All right, looking really good. And then you know the drill. We're going to go to the last one here and we're going to have cursor review the one from claude

**[0:22:10]** code at cursor-review. So we got this nice little triangle here of all the coding assistants reviewing each other's work. So awesome. Going back to the workflows here. If I refresh so I just see the ones that are in progress. We have two right here and then the one for

**[0:22:24]** cursor will show up in a second. There we go. All right, we got all three running. So I'll come back again once we got green check marks across the board. And there we go. The latest three poll request reviews are now complete. we can just open them up really quickly. And

**[0:22:37]** overall, the review process is pretty simple. All of these workflows are pretty simple because I just want to use this as a starting point for you. So, you can take it, you can customize the rules, you can customize the commands, really whatever you want your coding assistants to do in your repos. You can

**[0:22:52]** do a lot more than just handling issues and pull requests as well. And so, here's one review. Really, really nice and structured. Just found a couple of minor things. And it's going to look the same for all of them for codeex and then also claude as well. But I just love the

**[0:23:07]** formatting that we have here. Having AI for code review and being able to like fully customize the code review process is a beautiful thing. So that's everything that I have for you on integrating our coding assistance with our repositories. And I know this was more of a basic introduction, but I hope

**[0:23:22]** it can really help you see why GitHub is the future of AI coding. And please feel free to use these workflows for yourself. I'll link to all them in the description. You really just have to change the permissions and then you can change up the prompts that are loaded in

**[0:23:38]** anything that you're sending into the coding assistant. You can customize this to pretty much anything you want to do within your GitHub repos. And so also let me know if you want me to cover more content on this kind of thing. And so with that, if you appreciated this video

**[0:23:51]** and you're looking forward to more things on AI coding and AI agents, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
