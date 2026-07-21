---
type: raw-transcript
title: "Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship"
youtube_id: rFGlJ4oIlhw
url: https://www.youtube.com/watch?v=rFGlJ4oIlhw
slug: parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship
published: 2026-04-22
duration: "0:23:55"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** All right. What I have for you today is a playbook to help you 10x your AI coding with parallel agentic development. I'm going to get into all of the strategies that I use on a daily basis to run many cloud code sessions at the exact same time. And of course, I'll

**[0:00:17]** cover how these strategies will work no matter the coding agent that you're using or the applications that you are building. I would highly encourage you when you're trying to get the most output possible to run more than a single coding agent session at a time. I mean, sure, it's a good start. It'll at

**[0:00:32]** least 2x your output using AI coding assistance, but why stop there? Why not go for parallel agents to 10x your output or even beyond that? And by the way, this 10x versus 2x framing is very inspired by this book, 10x is easier than 2x Dan Sullivan and Dr. Benjamin

**[0:00:50]** Hardy. is a very good read by the way and I'm applying it here because the main argument in the book is that when you go 10x over 2x or that's your goal it actually is easier because it forces you to think differently for AI coding it forces us to think about building a

**[0:01:05]** system to make our coding agents more self- sustainable because otherwise there's no way that it would scale and of course there are features already built into these coding agents to support parallel agentic development like claude code has claude agent teams for example but honestly That's not very reliable and it's not a true system to

**[0:01:23]** give agents self- sustainability to make parallel agents really realistic and it's also definitely not enough to just spin up five instances of cloud code or codecs or whatever because sure I can give multiple different feature requests to these different agents but they're going to step on each other's toes

**[0:01:39]** constantly override each other's changes we need a system especially centered around work trees and so that's the system that I want to cover with you right now this video is really two parts I want to start with the five pillars and this is really simple to understand. I just want to cover the five things

**[0:01:54]** that we need for parallel agentic development to really work and a lot of it is going to center around git work trees and then the second part of the video goes a little bit deeper for real engineering. This is the good stuff here because there are some common problems

**[0:02:08]** that come up whenever you have your agents do end toend validation in parallel port conflicts installing dependencies token blowout. I want to talk about how we address all of these things to make it so that you can really scale your work, 10x your agentic development and beyond. Now, before we

**[0:02:24]** get into the five pillars, I want to just really quickly address the elephant in the room here, which is Archon. If you've been following my open-source harness builder, you know that I've built support for a lot of these things like isolation and workre. So, it's a system that ships ready for you to do

**[0:02:39]** parallel agentic development at extreme scale. And so a lot of the things that we'll cover in this video, Archon takes care of for you, but it's still important to understand how Archon works, how to use it effectively, and then some of the strategies that we'll talk about in the second part of the

**[0:02:54]** video are things that you'd actually want to build in your Archon workflows. And so even if you are using Archon, it's still really good to know how this works. And also, I don't want to always expect you to use my tool even though it is free and open source. And so that's

**[0:03:06]** why I want to cover these things with you, my system for parallel agentic development. So with that, let's get into the five pillars. All right, so pillar number one is that issue is the spec. Pretty much all of my agenda coding. Now, my input into any implementation is always a GitHub issue.

**[0:03:22]** And of course, if you're using some kind of task management platform like Linear or Jira, the ticket is going to be the input into the implementation. And then for validation, the input is always the pull request. We'll talk about that in a little bit as well, but let me go to the

**[0:03:35]** GitHub repository for this video to show you exactly what I mean. So, by the way, for this video, I built a very simple GitHub issue triager dashboard. So, it's not like it's some crazy powerful application I built or anything. I just built it to have a demonstration for

**[0:03:50]** this video. It helps us classify GitHub issues, managing a repo, and then everything is stored in the back end in a Postgress database using Neon. So, we have our issues, plans for the issues, and classifications. I might actually keep working on this. But anyway, the point here going back to the repository

**[0:04:05]** is that I have five open issues. And so I am ready to spin up five agents in parallel to handle each one of them. The power of having the issue or the ticket as the input is we already have the individual pieces of work scoped out. And so usually what I'll do is I'll

**[0:04:22]** create a bunch of issues in batch and I'll use a coding agent to help me do that because generally when you're working on an application you move in sprints where you have a bunch of bugs and features that you want to implement at the same time. And so usually I'll

**[0:04:35]** work with my coding agent here to create these bugs and feature requests as issues in GitHub and then I'll go into my parallel development. So it's sort of like a fano pattern, right? like you start with one coding agent session to split your work into these different issues. Then you send them all out to be

**[0:04:53]** implemented at the same time. Then going to pillars two and three. Once we have the bug fix or feature scoped out in an issue or ticket, then we're going to go through the stages of planning, building, and validating, but each one of the coding agents working with their

**[0:05:07]** own local copy of the codebase so they aren't overwriting each other's changes. That is what git work trees gives us. And by the way, work trees are supported natively in claude code. So I can do claude and then it's d-worktree or you can just do dashw and then you

**[0:05:24]** give the name of the work tree. Like it can just be the issue number like issue-10 or you can give a description of the feature whatever it is. And so I'm going to send this in. You can see here that the path that we're operating in is a work tree created in the

**[0:05:38]** do.cloud folder. So this is my main codebase right here. But then if I go into doclaude work trees, we can see that we have the folder issue 10. That's the name of our workree. And then we have the exact same codebase duplicated here. That is the beauty of work trees

**[0:05:52]** is now when our coding agent works on the feature here, it's not going to be overriding other features that other coding agents are building. Each one of them has their own environment. And by the way, later on in the video when I show you my system to handle the more

**[0:06:06]** trickier parts of parallel development, I'll talk about how we can create work trees for any coding agent, even ones that don't support it natively like Claude Code. But this is the starting point. It's very easy to do work trees with Claude like I just showed you. All right. Now, what I did off camera is I

**[0:06:21]** created five git work trees to work on each of the issues in parallel. So, I essentially did a claude-w, but I'm using a custom script here because it takes care of some of the fancier stuff that we'll get to in a little bit in the video, like installing the dependencies

**[0:06:36]** up front, creating a database branch. We'll get into all that. It's very powerful. But essentially, I have five work trees ready to go. And so, at this point, this is where we point each work tree, each cloud code in the work tree to a GitHub issue as our input. And you

**[0:06:52]** can use whatever your agent coding process usually is to plan, build, and validate. So maybe you have a set of skills or commands. Maybe you're using a framework like GitHub specit or BMAD. It doesn't matter. You can use your usual process. It's just instead of you typing what you want up front, you're just

**[0:07:08]** going to point it right to the issue. So take a look at this. We'll look at our issue list here. We'll say for the first work tree, we want to work on issue number one. All I have to say is use the GitHub CLI to view issue one and help me

**[0:07:20]** make a plan for it. It is that simple. And so for the sake of simplicity here, I'm not going through my usual, you know, more elaborate process with my planning command and implementing command. I'm just kind of doing free form text here. Uh if you want to see my

**[0:07:34]** full process for building with AI coding assistance, I'll link to a video right here where I show more intricately what I do for planning and building and validating. The point here is more to focus on the parallel side of things. And so I sent this off. I'll literally

**[0:07:48]** just copy this prompt. Check this out. I'll go into this one and say I'll use the GitHub CLI to view issue number two. Very cool. And then go on to this one and we'll do issue number three. It's a little bit redundant here, but I'm keeping this in the video on purpose

**[0:08:01]** just to show you how easy it is to start up the session because we're going to use our exact same process of planning. Maybe it's a command or whatever. Literally the only thing we have to change is the underlying issue number. And so now it's going to create a plan

**[0:08:15]** for each one of these all in parallel. And so I'll come back once we have that. All right. So the plan is back for each one of our issues now. And so I'm not going to get into the weeds with exactly what it's planning for each issue. That's not the point of this video. The

**[0:08:28]** point is now we have all these plans. I can just say go ahead and implement. And we can do it all at the same time because they're not going to be overriding each other's changes since we have the separate code bases. And so again, usually my plan and implement

**[0:08:40]** process is more elaborate. I'm going to be reviewing on the plan and iterating it with the agent, but for the sake of demo here, I'm just going to say go with what you recommend and implement all the way to a pull request. I'm just going to say this for each one of our work trees.

**[0:08:53]** And so it's important here that the output of the implementation is a pull request. Like I said, the issue is input into the implementation and then the pull request is going to be the input into the validation. And so I'll let it go through the implementation for each

**[0:09:08]** of these and then I'll talk about the fourth pillar for how we can do better validation. Okay, so our implementation is done for each of our work trees. As you can see here, we now have a poll request open up for every single one of our issues. And so that my friend takes

**[0:09:25]** us to the fourth pillar. And so the interesting thing about pillars number four and five is they're not directly related to parallel agentic development like the first three, but it's all about the reliability of the validation to make it so that you can really scale your parallel agentic development.

**[0:09:41]** Because the thing is, if you don't have a lot built into your system for self- validation, then you're going to become such a big bottleneck for your system that you can't have that many agents going at the same time. So that's why I'm so focused on these two things to

**[0:09:55]** make the whole process more reliable. So one of the most important strategies for honestly working with large language models in general is you don't want it to validate its own work in the same context window where it did the implementation. There is so much bias that the agent builds up within the

**[0:10:13]** conversation that if you tell it to review the code in the same context window, it's like asking a kid to grade their own homework. they're going to sweep a lot of things under the rug and say it looks good because they just did the work. And so what we want to do is

**[0:10:28]** start a fresh context window. The reviewer should never see the writer's chat. So now going back to our cloud code sessions, there is a specialized command that I have created for this called review PR. So it automatically data mines the poll request associated with the current branch and it does a

**[0:10:46]** comprehensive review. But the important thing is we want to do this in a separate session. So I'm actually going to run a slashclear completely wipe the context window. Then I will do a review PR. So I don't need to get super deep into what the workflow looks like here,

**[0:11:01]** but essentially it's going to based on the git diffs analyze the code changes, compare it to the issue to make sure we're really addressing the issue and then spin up specialized sub aents just to make sure that the implementation is ideal. And of course this command will be linked in the description. this

**[0:11:17]** entire repository will be because also there's a lot of references that I have here getting into some of the fancier stuff we'll talk about in a little bit. So I'm going to go ahead and run review PR here and then I'm just going to keep going through all of these sessions

**[0:11:29]** clearing doing the review PR. I'll come back once we have the reviews for each one of them. Our reviews are done. Looks like this one says approve ship as is. We got uh one with approve with changes, approve with changes, approve with changes. So couple of little things to

**[0:11:43]** fix here. And then uh this one, oh actually request changes. So this one it found two critical issues. So it's good we're doing the review here. Always important to do the review with the coding agent and then yourself after before you're merging any pull requests into production. And then one other

**[0:11:58]** thing I want to show you here, just another cool golden nugget to include is I love also using other coding agents to review the work of Claude Code. So for example, using the codeex plugin for Claude Code. Very powerful. I'll link to this GitHub repo in the description.

**[0:12:13]** very easy to get installed through the anthropic plug-in marketplace. And so then what we can do is run a command called /codex adversarial review. And so it's going to review this current branch as it relates to the changes from main. I'm going to send this off on each one

**[0:12:29]** of them. Not that you always have to do this comprehensive of a review where you have both Claude and Codeex doing the review in separate sessions, but it can be pretty helpful if you want to be really thorough making sure that again the agent takes care of as much

**[0:12:42]** validation as possible so that you don't have to be the bottleneck for your system. And there we go. We got our codeex reviews back for all of our pull requests. And it ripped apart my code. It says I need attention for this one. Uh this one it actually approved, but

**[0:12:56]** then for the other three I checked off camera. They all need attention. So, it's good that we're doing these very comprehensive reviews. We're definitely finding things. And so, the goal here is for the agent to address as many things as possible. So, by the time it's our turn to review, we don't have to be as

**[0:13:11]** much of a bottleneck. There's less for us to address. And so, at this point, we now have our coding agent address these problems, review things ourselves, and then merge the pull requests. And then we just move on to the next batch of issues or tickets. That's the loop that

**[0:13:26]** we go through here with parallel agentic development. Very cool. And so the last thing that I want to cover here as far as the pillars go is the self-healing layer. This is pillar number five. The big mental model here is whenever we encounter a bug in a pull request, we

**[0:13:43]** don't just fix the bug and move on, but we fix the underlying system that allowed for the bug. And so this is where we evolve what I like to call the AI layer. all of the context engineering for our coding agent like our global rules, our workflows, our skills,

**[0:13:59]** anything that's context to the coding agent, we might want to make it better. And the easiest way to start this process is for any of the issues that we identified here, we just say like, hey, uh, issue XYZ came up. What could we fix in our rules, skills, workflows, etc. so

**[0:14:20]** that this doesn't happen again. Now, obviously, this is an oversimplification, but the point is you can work with the coding agent. It has full context from the reviews to help you identify like these are the core problems. Like maybe your validate skill doesn't have enough of a process laid

**[0:14:37]** out or your planning isn't elaborate enough or your rules need to specify something new so that the coding agent understands your codebase properly. Just kind of spitballing a couple examples here to give you the idea that usually there's something that we need to change in, you know, for cloud code, our claude

**[0:14:52]** layer, like we have our commands, we have our skills, or maybe it's something we'd have to change in our claw.md. Whatever it is, it's good to make those improvements cuz then we're evolving not just our code base over time, but also the reliability of our coding agents. And again, that's very important so that

**[0:15:07]** over time we reduce how much we have to be a bottleneck because we're making our coding agents more self-sufficient. And the last thing that I'll point out here is it's also very powerful since we have the issue going in and the pull request coming out of our implementation. We can

**[0:15:23]** actually do a comparison here. So like I can open up this pull request and I can go to the issues. It's related to issue number one, right? So like pull request number 12 closes issue number one. And we can identify any discrepancies here. So, we can look at the git diffs and

**[0:15:40]** obviously have our coding agent help us do this, especially if you're not quite as technical. We can compare what was done for the actual work compared to the scope that we had laid out in the issue. If the coding agent deviated in any kind of way from planning to implementation,

**[0:15:55]** it'll be obvious just comparing the poll request to the issue. So, it's yet another reason that I love using issues and pull requests as the artifacts to drive everything for my AI coding because then it's very easy to, you know, look back retroactively and see if there's anything in our process that

**[0:16:09]** needs to be adjusted because we deviate from our plans frequently. That happens a lot with coding agents. Really good to do this after you have a set of pull requests. All right, so if you have made it this far, congratulations. You now know the core workflow for parallel

**[0:16:24]** agentic development. But now I want to get into some of the trickier stuff that you're going to encounter if you really set up your agents for success by allowing them to do end-to-end validation. Static code analysis is not enough. You need your agents to actually start your application and use it as a

**[0:16:41]** user would to make sure you're really ready for the pull request merge. But there are these core problems that come up that we need to address for our agents to really be able to handle issues and pull requests completely end to end. So we can have five issues at

**[0:16:55]** breakfast and then five poll requests ready for us to review and merge before lunch. And so these are the five problems. And by the way, I'm going to go pretty quickly through these things because in the repository that I have here, of course linked in the description, all of this is a reference

**[0:17:10]** for you to point your coding agent at. And so I literally say that at the top of the readme here. If you want to incorporate these ideas for handling port conflicts and database branching and all of that into your own AI coding systems, then just point your coding

**[0:17:23]** agent here and say, "Hey, take these ideas from Cole. I love them." That's the goal that I have for you here. And so the first problem is port conflicts. If you're starting many versions of your application up on your computer, they're going to try taking the same port and

**[0:17:36]** that's going to confuse your coding agent a lot. Also, we have to reinstall dependencies for every single work tree because it is a new local copy of our codebase. So, how do we make that fast? And then we also have the issue of if different feature implementations are

**[0:17:50]** changing the database, we will actually break different work trees if they're all pointing to the same database. So, not only do we need a work tree for the codebase, but we need something like a work tree for the database as well. We'll talk about what that looks like

**[0:18:04]** with neon branching and how you can do something similar with SQLite as well. And then of course we have scaling issues with token blowouts and PR pileup. But I want to focus on these three to start. Okay. So going back to our cloud sessions here. This is the

**[0:18:19]** script that I teased earlier. I'm not just running claude-w issues. And so the first thing that I'm doing is I am installing all of the node modules up front. So that way my agent doesn't have to take care of that when it goes from implementation to validation. That also keeps the agent

**[0:18:40]** focused and it makes the process not take as long when I'm actually having the agent run. And then the other thing that I'm doing here is I am creating a what is called a neon branch. And so okay this this is like a really cool feature. So within neon and most

**[0:18:56]** databases support this but neon just does this so well. We have the idea of database branching. Take a look at this. We have our main production database and then we have a special branch for each one of the work trees. So we essentially have not just codebase isolation with

**[0:19:12]** work trees but now we have database isolation as well. And the beautiful thing here if I click into one of the branches and I look at the tables we have all of the tables and data copied over from the main production instance. So it carries everything over and now I

**[0:19:28]** can test database updates and inserting records for testing and everything and it's not going to go right to my production data or conflict with the other branches that I'm working in with other pull requests. This is so important if you're doing anything with a database which is most applications

**[0:19:43]** you need something like database branching with ne which neon offers. Another solution if you just want something free and local is you can have like a SQLite database that you spin up in each workree. You can certainly have cloud code help you set that up as well. And the script for all of this, the w.sh

**[0:19:59]** or PS1 if you are on Windows, it runs this workree setup command and that is what creates the workree and then also the branch in Neon. And this is also really cool by the way because you can use this script in any coding agent. This is how you're able to add workree

**[0:20:13]** support automatically without having it built right into the tool like we have with cloud code. We don't have that luxury with every single coding agent. And then the other cool thing I want to show you here is our startup command. I have this separate command that handles startup as well. And what this does is

**[0:20:29]** it assigns a unique port based on the name of the work tree. So it uses the work tree name to create a random port. So that way when we start up the application, it has a unique port that isn't going to conflict with the other branches. So my base port is port 4000

**[0:20:45]** and then it's 4161 for this one. And then going to the bottom of this one, the port is 4107. So going to the browser here, you can see this is the main application that's running on main right now. And then I have all of the instances running on

**[0:20:59]** different ports in our workree. So our agents are able to start all these up in parallel and test everything in parallel. And you can see that we have different features like this one has classify all pending. That's not currently in main because that's what we implemented for this pull request. And

**[0:21:13]** so everything that I've covered here that hits on these first three things. And I know I'm going through it pretty quickly, but you can just point your coding agent at the repo and bring these commands into your own ecosystem if you'd like to. All right, so the last

**[0:21:24]** two things I'm going to cover very briefly here, just a couple of recommendations that I have for you. We got token blowout and PR pileup. And so for token blowout, the main thing we have to be aware of here is if we want our coding agents to be reliable, yes,

**[0:21:38]** we need to give it a very endto-end process, including a lot of validation and review. But it also means it's going to take more tokens. But the cool thing is with really any AI coding agent, you can switch between models. You aren't stuck always using the highest capability model. You can go to

**[0:21:54]** something lower like Haiku or Sonnet and Claude Code for example when you're doing something that you want to be cheap and fast and doesn't need as much reasoning power like codebased analysis, web research, even using something like Sonnet for code review. And so within cloud code and it works the same with

**[0:22:09]** other coding agents as well. You can just do slashmodel and then you're able to pick between the different models. Like let me just run it. I'll do this in another session here because I already ran it. So slashmodel I can pick between the different models depending on the

**[0:22:21]** task that I know I'm about to do. And the other cool thing that you can do is when you invoke skills in sub aents you can give a specialized model to those as well. So I can say use Haiku for a sub agent and do uh research for XYZ, right?

**[0:22:36]** Like use this model for this sub agent to do this thing. So I highly recommend doing that a lot to manage the tokens as you're doing these longer workflows. And then really for the last thing with PR pileup, the main thing is to reduce yourself being the human bottleneck,

**[0:22:53]** right? So, like anytime that you feel like you're slowing down on these code reviews and you just want to get over to that next batch of issues, if there's any issues that come up where it feels like you're spending a lot of time fixing, that is your signal to do the

**[0:23:07]** self-healing layer. You definitely need to add in more validation, something in the AI layer to make it so that there's not so much of a burden on you to do the reviews of the code and fixing all of those things. So, there you go, my friend. That is your playbook to 10X

**[0:23:20]** your AI coding with Parallel Agents. And remember to use this repository as a reference. My entire system packaged up here that you can have your coding agent steal for yourself. So I hope that you found this really useful. Even just the mental models here that you can apply no

**[0:23:35]** matter what your process is for parallel agentic development. And so with that, if you appreciated this video and you're looking forward to more things on agentic engineering and building harnesses and my open source harness builder archon, I would really appreciate a like and a subscribe. And with that, I will see you in the next

**[0:23:52]** video.
