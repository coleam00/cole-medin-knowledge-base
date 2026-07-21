---
type: raw-transcript
title: "I've Used Claude Code for 2,000+ Hours - Here's How I Build Anything With It"
youtube_id: nxHKBq5ZU9U
url: https://www.youtube.com/watch?v=nxHKBq5ZU9U
slug: ive-used-claude-code-for-2000-hours-heres-how-i-build-anything-with-it
published: 2026-03-16
duration: "0:22:49"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Claude Code was made generally available May 22nd of last year along with the release of Claude 4, but there was also a research preview before this and so I've been using the tool for a bit over a year now and I actually did the math. If you count all the time it took for me

**[0:00:16]** to prompt claude, review the code, monitor it. I have used the tool for over 2,000 hours now. So yeah, I have a thing or two to teach you. That's what I want to do in this video. So, right now, I want to share with you all of my

**[0:00:30]** battle tested strategies that will take you from a basic Cloud Code user all the way to a power user. I've bundled everything up together into what I call the Whisk framework. And here's the thing, these strategies are legit. I am not one of those AI content creators that has just jumped on the Cloud Code

**[0:00:47]** bandwagon the past few months. I've been using this tool, like I said, daily for over a year now. And so these strategies are going to work on any codebase, even massive ones, even projects that have multiple code bases. I've seen all of this applied at an enterprise level. And

**[0:01:03]** so no matter what you're working on, this is for you. This also really works for any AI coding assistant. I'm just focused on cloud code because it is the best right now. And so I am assuming here that you have at least a basic understanding of cloud code and now you

**[0:01:16]** want to take things to the next level. If you want the basics of building a system for AI coding, I'll have a video that I'll link to right here. All of these strategies, this is when we want to work on real code bases that get messy because we have a bunch of

**[0:01:30]** strategies here around context management. This is important because context rot is the biggest problem with AI coding assistance right now. It doesn't matter that we have the new 1 million token limit for clawed code. We still need to treat our context as the most precious resource that has to be

**[0:01:48]** engineered very carefully with our AI coding assistants. And so the WIS and C for the framework, all these strategies apply to that. And these are all things that you can take and apply to your projects immediately. So I'm going to break it down nice and simple for you

**[0:02:04]** here. Now the question you might be asking yourself is, Cole, why are we focusing so much on context management? Over 2,000 hours of using cloud code. this is what you want to focus on. And my answer is yes. I know this is very specific, but we need to lean right now

**[0:02:19]** into context rot and how to avoid this. I would go so far as to say that about 80% of the time when your coding agent messes up in your codebase, it's because you aren't managing your context well enough. And so I want to start with the problem of context rot and then we'll

**[0:02:34]** very quickly get practical diving into every part of the whisk framework. But I want to start with context rot as a precursor so you can really see why once you apply the whisk framework you're going to immediately see jumps in reliability with your AI coding even on messier code bases and I keep

**[0:02:52]** emphasizing larger messier code bases because that's where we see context rot becoming more and more of a problem. Now, there has been a lot of research in the industry on context rod, but my favorite, this is the most practical and probably most popular as well, is the Chroma technical report covering how

**[0:03:09]** increasing input tokens impacts LLM performance. And the main idea here is just because you can fit a certain amount of tokens into an LLM's context window doesn't mean that you should. And yes, it supplies the cloud code with the new 1 million token limit as well because large language models get

**[0:03:26]** overwhelmed with information just like people do. It is called the needle in the haystack problem. So when you have a very specific piece of information or with coding agents a specific file that it's read that you need it to recall, it will do a good job recalling that

**[0:03:42]** information in its short-term memory, but only if you don't have a superfilled context window. When you start to have a massive amount of contacts loaded, you start to get what are called distractors. And so these are pieces of information that are close or similar to what you need the LLM to recall, but not

**[0:04:00]** quite right. And we see this a lot with AI coding, especially with larger code bases. We are following the same patterns for things throughout our codebase. We have a lot of similarity in how different parts of our codebase are implemented. And so large language models will pull the wrong information

**[0:04:16]** and be very confident about their fix or implementation. I'm sure you've seen this all of the time. We have this needle in the haststack problem applying all of the time to AI coding. This is the idea of context rot. The larger our window gets, the more the large language

**[0:04:31]** model has a hard time pulling out exactly what we need for the current turn with our coding agent. So going back to the diagram, let me get super specific for you. What we're addressing with all of these strategies is the question, how do we keep our context window as lean as possible while still

**[0:04:49]** giving the coding agent all of the context it needs? That is the context engineering that we are doing here. And so I'm going to go through every single strategy. And I even have an example for each of them that I'll go through live with you on a complicated codebase. And

**[0:05:02]** all the commands and rules and docs that I use as an example, I have in this folder that I'll link to in the description. So you can use all of these strategies conceptually but also with these commands as an example that I have in the dotcloud folder right here. All

**[0:05:16]** right. So let's get into the individual strategies now. So W stands for write, I for isolate, S for select and C for compress. And of course we will start with the W here, which is writing, externalizing our agents memory as much as possible. We want to capture key

**[0:05:33]** decisions and what the agent has been working on so that in future sessions we can catch our agent up to speed a lot faster and have to spend less tokens up front having the agent understand what we really needed to do. And so the first strategy here is to use the git log as

**[0:05:49]** long-term memory. And I absolutely love this because there are so many people that love to overengineer and have super complicated memory frameworks for their coding agents, but really everyone's already using Git and GitHub for version control. And so we can take advantage of a tool that we're already using to

**[0:06:04]** provide long-term memory to our agent. Let's go into our codebase and I'll show you what I mean. So the codebase I'm going to be using for all the examples here is the new archon. And I've been working my butt off on this the last few months behind the scenes. This is your

**[0:06:20]** AI command center where you can create, manage, and execute longer running AI coding workflows. And we're even working on a workflow builder. It's going to be like the N8 for AI coding. And so we can kick off workflows. We can view the logs and monitor them in our mission control.

**[0:06:35]** We can look at past runs to see exactly what happened. Like this is a a very long workflow that I have to validate entire pull requests in my codebase. So yeah, you can tell from looking at this and a lot more in Archon coming soon, by the way. Okay, but you can tell from

**[0:06:48]** looking at this that there are a lot of moving parts. This is a very complicated codebase. So, it makes for a good example for everything I'm going to cover with you here, all of the strategies. And so, going to get as long-term memory, I'll show you an example right here of a oneliner for all

**[0:07:04]** of my recent commit messages. And what I want to point out here is that we have a very standard way of creating these commit messages. So, we have our merges, but we also have all these feature implementations and fixes. And so I have things very standard because that way I

**[0:07:19]** can rely on the commit messages to tell my coding agent what I've worked on recently because a lot of the time that will guide us for what we want to work on next. And the reason I have this so standard is because there is a commit command that I run. Now running a git

**[0:07:35]** commit is very easy. But if we want to standardize the message and have the coding agent help us with that having a specific command is very powerful. So I have this full implementation that I did here in a single context window with the coding agent. I'm at the end now where

**[0:07:50]** I'm ready to run my commit. And so if I just run / commit. That's all I have to do. It's running this command that has the standardization for how I document any work that I did and then also anything I did to improve my rules or command. So it's a twopart command.

**[0:08:05]** Here's what we built. Here's how we improve the AI layer. And so it's going to make this commit and I'll show you what it looks like after. All right. All right. So now looking at our commit message, we can see that we made some test improvements to the CLI. So a

**[0:08:16]** really nice prefix then getting into the details and then also so the coding agent knows how its own rules and commands are evolving over time. We include that in the commit message whenever we find an opportunity to improve let's say our plan command for example. And of course this commit

**[0:08:30]** command is one of the resources that I have for you in the repository if you want to use this as a starting point. But I also encourage you to customize what your commit messages look like. The important thing here is we standardize the messages. We make them very detailed

**[0:08:42]** so we can use it as long-term memory. All right. So the second right strategy is to always start a brand new context window whenever you are writing any code. No matter what I'm working on, my workflow is always I have one conversation to plan with the coding agent. I'll create some kind of markdown

**[0:08:58]** that has my structured plan and then I will send that in as the only context to a new session going into the implementation. And so it's very important here that your spec has all of the context the agent needs to write the code and do the validation. So for

**[0:09:13]** example in this conversation I am just doing planning. So I run my prime to start. I'll talk about this in a little bit. I load in context and then I create my plan with this command. So it's another one that I have as the resource for you. This essentially walks through

**[0:09:26]** for the coding agent. Here's the exact structure that we want to create for our single markdown document. So going from our short-term memory into a single document. And then we end the session here. We go to a brand new context window and we go with our implementation. So I have my execute

**[0:09:41]** command and then this is where I can specify the path to my structure plan. No other context because this should have everything that it needs. This is very important because it keeps our coding agent extremely focused on the task at hand. There can be a lot of research and other things that just

**[0:09:56]** muddles the context window if we implement in the same place that we plan. So, the last W strategy that I have for externalizing agent memory is progress files and decision logs. You'll see this all the time with more elaborate AI coding frameworks where you have like a handoff.md or a to-do.md

**[0:10:13]** communicating between different sub aents or agent teams, even just between different agent sessions when you're running low on context. A lot of times you want to create this summary of what was just done so you can go to a fresh session because you're starting to see that context rot with the agent

**[0:10:27]** hallucinating as you have these longer conversations. Now, obviously it's ideal to just avoid these longer conversations, but sometimes you need to have them. For example, something I do with Archon a lot is I'll have it use the Verscell agent browser CLI to perform endto-end testing within the browser. And so I have it go through a

**[0:10:46]** bunch of different user journeys and testing edge cases. It takes a lot of context. You can see at the bottom here, I ran a slashcontext and we're already at 200,000 out of the new 1 million limit. This fills up so quickly. And once you start to have a few hundred,000

**[0:11:01]** tokens in the context window, that's when you see the performance start to degrade for the agent. So, I can simply run a slash handoff. This command is going to create a summary that I can now pass into another session. So that agent can continue the work, but now it

**[0:11:15]** doesn't have hundreds of thousands of tokens of tool calls and things like that sitting in its window. And this handoff command is really just walking through a process of here's exactly what we want to put in this document so the next agent has what it needs. All right,

**[0:11:28]** so that wraps up our W. And each one of these strategies is very important because we are logging key decisions for future agent sessions to quickly pick up on. And I know I'm going quick here, so let me know in the comments if there's any one of these strategies that you

**[0:11:41]** want me to make an entire video on because I definitely could for each of these. And so now we get into the I for isolate using sub agents. I love using sub aents for all things research, using them pretty much every single session. The important thing here is keeping your

**[0:11:57]** main context clean. We can use sub aents to perform tens or even hundreds of thousands of tokens of research across our codebase or the web and then just giving the needed summary to our main claude code context window. So instead of loading in tens of thousands of tokens of research into our main context

**[0:12:17]** window, it is now only something like 500 tokens. So we still get the core information that we need, but we have a 90.2% 2% improvement according to some enthropic research using sub agents to load in context upfront for our research instead of having our main agent taking care of everything. So let me give you

**[0:12:36]** an example of this really quick. It's always at the start of the conversation or before that structure plan I covered earlier like I'm in the planning process that is when I use sub agents very heavily. Watch this. I want to build a workflow builder into Archon. So I want

**[0:12:51]** you to spin up two sub agents. one to do extensive research in the codebase to see how we would build in a workflow builder and what that means for archon and then spin up another sub agent to do web research on best practices for the text stack like if I want to use react

**[0:13:06]** what library should we use and generally how do we build workflow builders like diffy or nadn so I'm just using my texttospech tool here send off the prompt there we go and so not only do we get the benefit of isolation but also speed because it's going to use these sub aents in parallel

**[0:13:22]** come back with the summary and then my main agent will synthesize all that and give me the final say. So there we go. Both of the sub aents are running in parallel behind the scenes. We can go and view the logs for each of them as well. And then it'll come back at the

**[0:13:35]** end once they're done with the final report. All right, our sub agents finished and instead of using hundreds of thousands of tokens in our main context window, which that is how much the sub agents did with their research, we only used 44,000 tokens, only 4% of our window so far. That is the power of

**[0:13:52]** sub aents. I don't recommend them for implementation because usually you want all the context of what you did, but for research it is very powerful. So yeah, isolation and sub aents are very important for your planning process. The other way that we can use sub agents is with what I like to call the scout

**[0:14:09]** pattern. We want to send scouts ahead before you commit your main context. There might be parts of your codebase or documentation that you want sub agents to explore to see if it is relevant to load into your main cloud code session. So it can kind of make the decision

**[0:14:24]** ahead of time like yes, we should bring this in for our larger planning or no, we should skip it. It isn't relevant. For example, with archon, I have a few markdown documents that are very deep dives into certain parts of the codebase. Not the kind of context we

**[0:14:38]** want in our rules because we don't need it all the time, but sometimes we might want to load this. And you can imagine this being something in Confluence or Google Drive like wherever you store your context. And so going back to this main conversation, I can just say spin

**[0:14:50]** up a sub agent to research everything in my do.cloud/docs. Are there any pieces of documentation here that we would care about loading into our main context for planning and I can send this in. It'll make the decision and then load in what I care about. So right here we kicked off an

**[0:15:06]** explore sub agent. It found all of our documentation recommended loading one and then I said, "Yep, go ahead and load it." This is really important for what we're planning here. So instead of just doing sub agents for research, sometimes we have entire pieces of documentation that we think are crucial for our main

**[0:15:21]** context window. That's we want to use the scouting pattern. So that is everything for isolation. Remember to use sub agents for your research and planning very extensively. And now that brings us into the S4 select. Load your context just in time, not just in case. And what I mean by that is if you're not

**[0:15:39]** 100% confident that a piece of information is important to your coding agent right now, then you shouldn't bother loading it. And we have a layered approach to help with this. And so we start with our global rules. These are our constraints and conventions that we always want our coding agent to be aware

**[0:15:56]** of. And so you want this file to be pretty concise. Usually between 500 and 700 lines long is what I go for. A lot of people advocate for even less. But you have things like your architecture, the commands to run, things like your testing and logging strategy. This is my

**[0:16:10]** example from Archon. But these are the things that you want your coding agent to be aware of all of the time. And then we have our layer 2. So our ondemand context as I call it. These are rules that apply only to specific parts of the codebase. Like if we're working on the

**[0:16:25]** front end, which you aren't always, but if you are, here are the global rules for the front end or here are the global rules for building API endpoints. So we add this onto our global rules for specific task types because we aren't always going to be working on the front

**[0:16:39]** end. For example, to show you one example of this, we have the workflow YAML reference that I pulled just a little bit ago with the explorer sub agent. So when we are working on the workflows, then we care about this, but we don't want this in our global rules

**[0:16:52]** because most of the time when we're working on archon, we're not actually working on this specific part of the codebase. And so it's on demand context. Then the third layer that we have here is skills. This is very popular with cloud code and beyond. Right now we have

**[0:17:08]** the different stages here where the agent is going to explore the instructions and capabilities in the skill as it deems that it actually needs it. So we start with the description. This is a very small amount of tokens loaded in up front with our global rules. If the agent decides it wants to

**[0:17:23]** use this skill, then it'll load the full skill.md which can also point to other scripts or reference documents that we'd want to load. if we're going even deeper into the skill. And so as an example of that, I have my agent browser skill. This is what I use for my browser

**[0:17:37]** automation for all my endto-end testing I was showing earlier. I use this every single day. And so whenever I am doing my end toend testing, then I want to load this instruction set so the agent understands how to use the agent browser. And then finally for the fourth

**[0:17:52]** layer here, I have prime commands. So everything else I've covered here is static documentation that we're going to update every once in a while. But sometimes we need our agent to do exploration of our live codebase. We need to make sure that all of its information is completely up to date and

**[0:18:08]** we're willing to spend some tokens with sub agents up front making that happen. That's what the prime command does is we are exploring our codebase at the start of our planning process. So it understands our codebase going into what we want to build next. And as you can

**[0:18:22]** see in my commands folder, I have many different prime commands because there are different parts of the codebase I want the agent to understand depending on what I want to build. And so my generic prime command is this one we're looking at right here. I just tell it to

**[0:18:35]** get an understanding of the archon codebase at a high level. And so step by step here is what I want it to read through including the git log because that is important for using our git log as longterm memory. I also have a specialized one, prime workflows, for

**[0:18:49]** when I know that I'm working on the workflow engine in Archon. So, a very similar command, but just more specialized. So, I use this at the start of the conversation so that my agent can quickly load everything it needs. I can confirm it understands my codebase. Then, I get into the planning process

**[0:19:05]** that I was showing you earlier. So, as a super quick summary, global rules are always loaded on demand context when you know you're about to work on a part of a codebase that is documented separately. skills when you need different capabilities like okay it's time to do endto-end testing let's load the skill

**[0:19:20]** for the agent browser and then prime commands I will usually run at the very start of a conversation to set the stage for my planning so that is everything for select now we will go to compress and this is actually the fastest section to cover because you shouldn't need to

**[0:19:37]** compress often if you're doing the right isolate and select well if we are doing all the other strategies to keep our context lean we are avoiding this and this is good because you want to avoid compressing as much as possible. If you must compress then there are a couple of

**[0:19:53]** strategies to cover here and those two strategies are the handoff and a focus compaction. So let's get into cloud code and take a look at this. So the handoff we already covered. It's one of our write strategies. We summarize everything that we just did to hand off to another agent or the same agent after

**[0:20:09]** memory compaction. And then we have the built-in compact command in claude code. This is going to summarize our conversation, then wipe the conversation and put the summary at the top of our context window. Now, the handoff is really powerful because that's where we get to define our own workflow for how

**[0:20:27]** we remember information. But the slashcompact is very useful as well, especially because we can optionally provide summarization instructions. When I absolutely have to compact, I will use this every single time. for example, focus on the edge cases that we just tested. Right? So now it's going to when

**[0:20:48]** it creates that summary pay more attention to that part of its shortterm memory. I didn't spell it right. That's totally good. It'll run the compaction here. And so the handoff and slashcompact are kind of either or. But I definitely find times where I want to use both. The handoff, especially when

**[0:21:03]** you run into a compaction more than twice. Usually that conversation is getting way too bloated. So you want to start a fresh session with the handoff. But if I'm just doing it once, a lot of times I am okay running a slashcompact once. But usually after a compact, I

**[0:21:17]** will still ask the agent to summarize what it remembers so I can make sure that it truly understands, right? Like what do you remember here? Something like that. And so yeah, it really isn't ideal. Avoid compaction as much as possible. The best compression strategy is not needing compression. All right.

**[0:21:35]** So that is the whisk framework. I know it was a lot. So, I hope that you found this helpful. And let me know if there's any one strategy that you want me to dive into deeper cuz I could make an entire video on any one of these strategies. But this is the Whisk

**[0:21:50]** framework. I hope that you can use this to take you to the next level of cloud code or really any AI coding assistant. And so if you found this video helpful and you're looking forward to more content on AI coding and being able to apply these kinds of frameworks in

**[0:22:06]** practice, I would really appreciate a like and a subscribe. And with that, I will see you in the next video. I've got one last thing for you really quick that you don't want to miss. On April 2nd, I am hosting a free AI transformation workshop live on my YouTube channel

**[0:22:21]** along with Leor Weinstein, the founder of CTOX. And this is a big deal. Leor is going to teach us how to restructure our entire organization for AI. And then I'll teach you how to master the AI coding methodology that I use to build reliable and repeatable systems for my

**[0:22:37]** coding agents. And so I'll have a link in the description to this page. It's going to be live on my YouTube channel, so you can enable notifications for it by clicking on this button right here. I will see you there.
