---
type: raw-transcript
title: "The Next Evolution of AI Coding Is Harnesses - Here's How to Build Them"
youtube_id: qMnClynCAmM
url: https://www.youtube.com/watch?v=qMnClynCAmM
slug: the-next-evolution-of-ai-coding-is-harnesses-heres-how-to-build-them
published: 2026-04-08
duration: "0:30:49"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Finally, after months and months of hard work behind the scenes, I am unveiling the new Archon, a massive overhaul of the AI command center that I was working on last year. It is now the first open-source harness builder for AI coding. So, similar vision, but a very different and powerful use case.

**[0:00:20]** Harnesses are the future. It's the layer on top of your coding agents that orchestrates the different sessions. It's what makes AI coding deterministic and repeatable. We'll talk about what that means. And now with Archon, you can build your own custom harnesses very easily. No matter how you work with AI

**[0:00:39]** coding agents right now, you can take that process and bundle it up into an Archon workflow that you can run across all your code bases, even handling different tasks in parallel. Archon handles all of the messy logic behind the scenes to make that possible. And so in this video, I want to talk about what

**[0:00:57]** makes Archon so powerful. I want to show you how to get started with it and even give you some inspiration for the kinds of things you can do with it. It's a very powerful tool. It's actually hard for me to explain everything in just one video, but a lot more content coming on

**[0:01:11]** Archon soon as well. So, the main idea with Archon is you can encode your development process as a workflow, no matter what it is. And so I will link to this repo in the description. I highly encourage you to try Archon today. It's very easy to get up and running. I'll show you that in a

**[0:01:27]** little bit. But I have an example here at the top of the readme for what an Archon workflow looks like. And so every single workflow is just a combination of nodes, where a node is either a prompt that we send into a coding agent session, or it is a deterministic

**[0:01:42]** command that we want to invoke. Because sometimes we want to enforce certain things to happen, like context creation or validation, that we don't want to leave up to the coding agent cuz it might forget to do so. So we want to plan, implement tasks in a loop, run the

**[0:01:55]** tests, have it do a review, even adding in a human approval gate so we can address our feedback. We can build ourselves into Archon workflows if we want as well, and then ending with a pull request. And Archon comes with a skill that I'll cover with you in a bit

**[0:02:08]** as well. So we just say like use Archon to build this feature, it knows automatically the workflow to use, it'll invoke it for us, and we have the logs so we can monitor the workflow along the way. Archon also comes with a ton of pre-packaged workflows that will

**[0:02:23]** immediately level up your agentic coding workflow. Fixing GitHub issues, creating pull requests from ideas. We have pull request validation and review commands, even one to help you create full PRDs with human in the loop. So, ton of things for you to use and very easy to create your own custom workflows as

**[0:02:40]** well. We're going to cover all of that in this video. I'm going to give you enough of a starting point for you to dive right into Archon. And then if you want a super deep dive, I'm also doing a live stream this Saturday, 9:00 a.m. Central Time. So come be a part of this

**[0:02:53]** as well cuz we're going to get really deep into building workflows and running them in parallel, doing a lot of fancy things. But for now, I want to give you a good overview of Archon, why it's important, where we're heading with agent harnesses, and then we'll get into

**[0:03:06]** the setup guide. So I want to start by talking about the evolution that we've seen that has brought us to harness engineering. So prompt engineering, that was all the rage back in 2022 through 2024. It was all about how can we prompt LLMs to get the single best output? And

**[0:03:23]** then that evolved into context engineering, which is all about how can we curate the perfect context for a single agent so it can handle a larger set of work. We give it all the context it needs and nothing more. And now that has evolved into harness engineering, where we're dealing with

**[0:03:39]** many different coding agent sessions, all tying that together through a harness. And so up until this point, everything we've done here is dealing with a single LLM or a single agent. Now we are stringing coding agent sessions together to handle much larger sets of work. And so maybe you've heard of the

**[0:03:57]** Ralph loop before, or Anthropic has built a couple open-source harnesses. There are a lot of harnesses out there, but the problem is that they're not custom to you. Maybe it's a good starting point or helpful to create a proof of concept, but what Archon unlocks for you is being able to create

**[0:04:12]** your own custom harness wrapping up your own software development life cycle. And harnesses are a big deal. It's the tooling, the prompting, chaining different coding agents together, everything to elevate the capabilities of a single large language model. And this is really important right now cuz Claude is about to release Mythos, but

**[0:04:29]** it's more enterprise use. Like us consumers, there's no way we're going to be able to afford using Mythos for everything. But what we can do is build a harness around Opus to make it more powerful than Mythos by itself. And this is proven. There have been studies that

**[0:04:42]** have been done that if we take a large language model and we just use it to create some code, the PR acceptance rate is only 6.7%. But if we create a harness, like the Ralph loop but probably more custom and better, we can get even as high as like almost 70% for

**[0:04:58]** a PR acceptance. And I don't want to get like super deep into the study here, but the point is we can elevate models a drastic amount by creating a harness where we build in validation, we build in a special kind of context curation. And that's exactly what Stripe did with

**[0:05:13]** Stripe Minion. So I covered this on my channel already actually, but Stripe, they ship 1,300 AI only generated pull requests every single week. And they did this by building their AI coding workflow, their context curation, their validation, enforcing that at different steps of the way in their workflow. So

**[0:05:32]** they actually built something kind of like Archon, but it's not open-source, right? You can't use it like you can use Archon. And with the Claude code source code leak, we found that even Anthropic is leaning a lot more into harnesses with agent teams and features they're building around sub-agents. 40% of their

**[0:05:48]** code base is just code for harnesses right now. And so that just is a signal for how much it's a big deal right now. And Archon, it wraps above Claude code and Codex. So the old Archon was more of a tool built into coding agents. That's kind of why it became irrelevant because

**[0:06:04]** these coding agents, they built all that themselves for rag and task management. You know what I'm talking about if you've used the old Archon. But now the new Archon, it sits above the coding agents and it orchestrates them. So the problem is before, you're dealing with AI shepherding. Like yes, you have

**[0:06:20]** your skills and commands and you're running workflows there, but you still have your entire process where you're running different skills and different commands, and you have to remember what comes next, and you have to kick off the code review after the implementation. But now your entire process, you can

**[0:06:35]** bundle as an Archon workflow. Define once, run forever, reusable across projects. You also get to pick where you're injecting context. Like maybe you have a skill that you only need during the validation step, or you have an MCP server that you only want during planning. We have that level of control

**[0:06:51]** per node with Archon. And kind of like the example I gave in the readme, here's an example of going from plan all the way to open a pull request. This is the kind of thing you can build with Archon. And I think you really see here how we're building in reliability through

**[0:07:06]** deterministic steps, enforcing validation at certain steps of the way, and human approvals. So we have our plan here. We can even like build this into a loop where we have the agent create the plan and then we give feedback, and we go in a loop until we go to the coding step. And we

**[0:07:21]** do that in a fresh context window. You always want to do your planning and implementation in different coding sessions to remove bias. And then after the coding, we go into the tests, and we run this every single time. Again, we don't want to rely on the coding agent

**[0:07:35]** to remember to do the tests all the time. And then we retry and have it fix issues if they come up. Otherwise, we go to the final human approval gate. When things look good, we then open the pull request. Just one example of how you can take I mean this is a more basic example

**[0:07:51]** of what your agentic coding workflow might look like, but there's going to be different things depending on if you're fixing bugs or refactoring or building a new feature. All of those things you can build into Archon. And the big secret here is the hybrid secret. This is what

**[0:08:04]** makes Stripe Minion so powerful. There are certain steps of the workflow that we don't want the coding agent to decide. Like sometimes we want to curate context in a specific way, or run our tests in a specific way. We have nodes for that that we can build into Archon

**[0:08:18]** workflows. But then of course, most of the workflow is still going to be driven by our commands and skills, just sending prompts into our coding agents. We have of course support for all of that so you can take your existing commands and skills, everything, and build it right

**[0:08:33]** into Archon. So I hope you can see why this is so powerful, building these kinds of harnesses for yourself. And so with that, I now want to get into the guide for you, how you can get Archon up and running using these workflows in less than 5 minutes. Now, installing

**[0:08:49]** Archon is actually incredibly easy because we can use our coding agent to guide us through the entire process. All you have to do is clone the repository, open up Claude, and then ask it to set up Archon. Because it will automatically load in a skill that we have in the code

**[0:09:06]** base here that guides you through the entire process. And I'll do this right now with you just to show how easy it is. We can do this in less than 5 minutes. So I'll take this first command here to clone the repository, and then obviously we want to open up our coding

**[0:09:18]** agent in this repo so we can load the skill. So we'll change our directory, and then we'll open up Claude. There we go. So now in Claude code, I just say set up Archon. That is all you have to do. And take a look at this. We'll see

**[0:09:29]** in just a second, it'll load the Archon skill, and then it'll kick off this process where it'll ask us all the questions we need in order to help us get our credentials set up and then validate that Archon is working on our machine. So first, Archon is going to

**[0:09:42]** check to make sure that we have the prerequisites in place, including Bun, and it'll install it if we don't have it already. Then it asks what repository we first want to use Archon with. So it's important that you add in your own project, not the Archon repo, because we

**[0:09:56]** want to use the Archon workflows on a target repository. And don't worry, it's super easy to add more projects into Archon after. And so, just for this demonstration here, I have a reg YouTube chat application that I'm going to be running some Archon workflows in. And so, I have the path to this repo cloned

**[0:10:15]** locally copied here. And so, I'll just go to option number two, specify a local path. And so, then it's going to ask me, you know, like what is the path? Please paste it. So, I'll paste it in here. And then, it'll register this as our first Archon registered project. And then,

**[0:10:29]** going forward, we can add any project into Archon by just running a workflow there for the first time or right within the web UI. I'll show you that in a little bit. Then, it asks what platforms do I want to set up. So, the CLI is included by default. You can run Archon

**[0:10:43]** through the CLI, ask your coding agent to do so. But, we can also run in GitHub. And then, we could run through Telegram, through Slack. I'm actually going to set up quite a few of these right now. There are a lot of different interfaces to interact with Archon.

**[0:10:55]** Then, I will submit my answer here. There we go. And now, it's going to walk us through setting up the credentials for each one of our platforms. Then, after Archon installs the global CLI, like it did right here, then it's going to walk us through a setup wizard to set

**[0:11:10]** our credentials for any other platforms we chose, like GitHub or Slack. We need to do this in a different window, because we don't want to send our API keys directly into Claude Code. So, it's going to spin up another terminal process for us to enter our keys, not

**[0:11:24]** going to a coding agent. And so, it should spin up the wizard automatically and bring up another terminal automatically. But, for certain operating systems, or if you're trying to run Archon in a VPS, you will probably have to open up a new session yourself. So, you just open up a new

**[0:11:38]** terminal, and you run the Archon setup command. So, Archon is now a globally recognized command, because we installed the CLI. So, this is going to work automatically. In my case, I'm just going to go back to the terminal that it popped up for me automatically. So, we can pick our database. SQLite by

**[0:11:55]** default, this is the easiest. Or, you can set up Postgres if you like. So, I'm going to do SQLite. And then, it asks which AI coding assistant you want to use. So, right now, we mostly support Claude. We're almost done with Codex support, and then we want to add in

**[0:12:08]** other coding assistants later, like the Pi Agent SDK and Open Code. And so, I'll go with Claude right here. So, I'll just do space to select, and then enter to confirm. And then, how do I want to authenticate with Claude? Well, I just want to use my Anthropic subscription.

**[0:12:22]** We are allowed to use our Anthropic subscription as long as it's an application running locally using the Claude Agent SDK. And that is the case for Archon. So, I'm going to use my global auth. Just going to hit enter here. What platforms do I want to connect? So, I'll

**[0:12:37]** just select GitHub, Telegram, and Slack. So, then it'll ask me for the credentials for those. And this is where it's going to guide you through getting the API keys for each of them. So, for each one of the platforms you select, there are instructions to walk you through getting your keys for each

**[0:12:53]** application. So, I'm just going to go through this quickly. You can take your time to get the keys yourself on your own. All right. Then, after you set all of your credentials, it's going to ask, do you want to install the Archon skill in your project? And I would highly

**[0:13:15]** recommend doing this, because then, if we open up Claude Code in our other code base, we can use the Archon CLI to kick off workflows automatically. Cuz then, if we have Claude open there, we can just say, "Use the Archon CLI to invoke whatever workflow to handle a pull

**[0:13:29]** request or an issue or something." And it'll know right away to load the skill, and it'll know exactly how to use the Archon CLI. Again, it's important for any CLI to have a skill paired with it, so that our coding agent knows how to use it. So, I will bring this over. It

**[0:13:43]** asks for the path. So, I'm just going to take the path that I copied earlier for the repo. Just paste it in right here, so it knows where to copy it. And then, it'll ask if you want a non-default docs directory. If you have other documentation you want to load into

**[0:13:55]** Archon, probably don't worry about that right now. That's something that we're working on currently. So, I'll do no there. And there we go. Our setup is complete. And so, what we do here is we actually go back to the first session where we first said, "Set up Archon."

**[0:14:08]** And it tells you this here. So, it says, you know, come back here, complete the configuration there, let me know when you are done. So, I'm I'll just say, "Done." And then, what it's going to do now, that I've set all my credentials, is verify that everything is working.

**[0:14:21]** So, it'll test the connections. It'll even test running a workflow through the Archon CLI. I'll come back once that is done. All right. So, it confirms that our credentials are good to go, without actually reading them, of course. Then, we list out all of the default Archon workflows to make sure they're

**[0:14:35]** available. Those are all the workflows that we have bundled ready for you to use immediately to fix GitHub issues, run a rough loop, create a PRD. There is a lot of value that we have built into this right away. And then, it of course runs a workflow as well. So, it runs our

**[0:14:50]** basic Archon assist one just to make sure that the Archon CLI is functioning, and we're ready to use it on any repository that we want. And then, it gives us a summary at the end. And look at how easy it is for us to just start using Archon right now.

**[0:15:04]** So, we just open up Claude Code in our target repository. You can really do this in any repo you want, because remember, when we run the Archon CLI in a repo for the first time, it automatically registers it with Archon. So, we just copy over the Archon skill

**[0:15:18]** into whatever repo, launch Claude there, and then we can just say, "Use Archon to, for example, fix this issue number." Or, "Help me create a PRD." Whatever workflow you want to use, and you can build your own, like I'll show you in a little bit. So, because I chose my reg

**[0:15:32]** YouTube chat application as my onboarding repo, I copied over the Archon skill. So, it knows how to use the Archon CLI when I ask it to. And so, I'm going to open up Claude Code right within this repository, and we are already ready to use a workflow. And so,

**[0:15:48]** I'm going to use Archon to help me fix a GitHub issue. And so, going into the issue list for my repo, you can see there is quite a few options that I have to work with here. Well, let's say I just want to deal with issue number one.

**[0:16:00]** And so, all I have to do is say, "Use Archon to fix issue number one in GitHub." That is it. I don't have to provide any more context, because it'll know to load the Archon skill, find the right workflow for the job, and then invoke it. And then, our Claude

**[0:16:17]** Code can just monitor it in the background. So, there we go. It used the GitHub CLI to view the issue to get context, loaded the Archon skill, and it decided, "Okay, I should use the Archon fix GitHub issue workflow." It's one of the defaults that we have bundled. It is

**[0:16:30]** a very powerful workflow, by the way, because it does full investigation, fixing, and validation before it creates the pull request. And that is the end result is we'll have a pull request that has the final implementation from the Archon workflow. So, we can see right here that in Claude Code, it is running

**[0:16:46]** as a background process. So, we can track the logs here. We can always ask Claude Code to give us an update for how the workflow is running, or we can view the workflow in the web UI as it is running. Okay. So, right here, we are focusing on using the CLI to run an

**[0:17:02]** Archon workflow. That is the most convenient way. But, we also have a web interface. If you want to more visualize what's happening with your workflows, we can also view the logs for the workflows more easily that we run through the CLI. So, I'm going to go back to the terminal

**[0:17:16]** where I had the Archon repository open with Claude Code. So, all I have to do, if I want to start the back end and front end of Archon, is I just have to ask my coding agent to do so. It is that easy. So, I can say, "Spin up the front

**[0:17:29]** end and back end of Archon." And it's going to, based on the review, understand the commands to run, and then get everything running for us as background processes. And so, take a look at this. If I go into the browser and go to port 5178, right? Cuz that's

**[0:17:43]** where it says it's running right now, I can see my conversations. I can see the workflows that are currently active. So, if I go into the dashboard here, I can see that it's using the Archon fix GitHub issue workflow. I can view the logs for it to see what is currently

**[0:17:56]** happening. So, this is the node that we just completed. Now, we're currently investigating the issue. So, we started with web research, then now we're investigating. We can see all the tool calls. So, all the logs from Claude Code, if you want to dig into all the individual actions that it's doing as

**[0:18:12]** it's going through this Archon workflow. And so, every single one of the nodes here is either a deterministic action, like a bash command, or it's a session with Claude Code. And again, in our Archon workflows, we can determine when we go from node to node, do we want to

**[0:18:26]** start a brand new session with Claude Code or continue the conversation? We have a lot of flexibility for token management, making sure we keep our context lean when we're dealing with our coding agents. One of the big things that Archon gives us that we were missing before. All right. And while we

**[0:18:41]** wait for this workflow to finish, it's going to create a pull request at the end, I want to show you what it actually looks like in the YAML. Cuz remember, all of the workflows in Archon are simply defined as YAML files. It is so easy to improve the existing ones that

**[0:18:56]** we have in Archon, and even create your own. That's one of the last things I'll show you in this video. And so, within the .archon folder in the Archon repository, we have all of the default workflows. These are also bundled into the CLI. So, when you run the CLI from

**[0:19:11]** any other repository, it'll automatically have access to these. So, take a look at this. We have all of these different workflows. The one that we're running right now is Archon fix GitHub issue. And [snorts] so, we have a description for the workflow. And this is important, because this is just like

**[0:19:26]** Claude Code's skills, where the description is what we first give to Claude Code. Like, "Hey, here's a workflow from Archon that you want to use when the user is specifically asking for you to fix a GitHub issue." Right? We don't want to load the entire workflow into context for the coding

**[0:19:44]** agent. That's way too much. It only needs this brief description up front. So, it uses this to determine if it should analyze and run this entire workflow. We can define the provider up front. Again, we're supporting more in the near future, the default model used for each of the nodes, and then we have

**[0:20:00]** the list of nodes. This is the step-by-step that we're going through. So, exactly what I have defined in the YAML document, we can see right here in the web UI. We see the full execution, all the different nodes that we have, the different branches and decisions that can be made. All of this is a

**[0:20:15]** direct visualization of what we have in the YAML right here. So, for this workflow specifically, we are going to first extract the issue number. So, based on the prompt that is fed into this workflow, it's kind of like running a sub agent in Claude Code, we're going to grab the issue number,

**[0:20:31]** and then we're going to classify the issue. Is this a bug that needs to be fixed or a feature that we need to build? Because that's going to determine what comes next, right? Do we have to investigate the issue or plan for a new feature? And we have the prompt here

**[0:20:45]** that we're sending into the model for this step specifically. And one of the most powerful things, I know that token consumption is a big deal right now, especially because of rate limits with Anthropic. One of the powerful things we can do with Archon is specify the model we want to use for the individual nodes.

**[0:21:01]** So, certain nodes, like classification, they don't need a lot of reasoning power. So, we can make it a lot more token efficient, a lot cheaper by just using Haiku for our model. And then we go into the research phase. In this one, we're just going to use the

**[0:21:14]** default model. So, we don't specify it here, it just means that it'll use the default model of Sonnet. And we don't have the prompt in line, we're actually using a command. And so, for every single workflow that's in this folder, and then the commands are sort of like

**[0:21:27]** the extensions that we run in certain nodes. So, for example, we have the Archon web research command right here. So, I'll just open this really quickly. It's just like commands or skills in Claude, where it's just a longer prompt that we're going to invoke for this node specifically. So, we do our web

**[0:21:45]** research, and then we investigate if it is a bug or we plan if it is a feature request. That's the the first decision that we can see right here. So, in the case of the workflow we just invoked, it went down the path of investigation because looking at our issue here, it's

**[0:22:00]** definitely a problem that we're addressing, not a new feature that we are adding. And so, not like I need to go like in super deep detail for every single node here, but I'm just trying to show you the idea of like how we can take a pretty comprehensive workflow and turn

**[0:22:16]** it into this single process that we run with Archon. It's more than just writing some code. It's doing classification, it's doing investigation or planning, it's implementing, validating, and then creating the pull request at the end as well, and even doing further review after that point. And so, we have a lot

**[0:22:32]** more faith by the time this workflow finishes that the pull request is really ready for us to review and merge. And yes, it takes a good number of tokens to go through this many steps, but that's why we lean on being able to specify the model at each step of the way. We're

**[0:22:48]** able to use Haiku for a lot of this here. So, we're just kind of giving more of a set of guidance around the coding agent. That's why we're calling it a harness, right? Like, this is sort of a harness wrapping many different Claude Code sessions to work together to fix a

**[0:23:03]** GitHub issue. And there are so many amazing workflows that we have available for you that you can use out of the box, and then anything that's not here, you can just create by yourself. So, we have the adversarial dev harness as an Archon workflow. I showed this in a live stream

**[0:23:18]** that I'll link to right here. We have a comprehensive PR review workflow. We have one to help you create issues. So, like investigating a problem creating a GitHub issue, idea to PR, this is a very comprehensive one. We have one with human in the loop. We actually have human in the loop with

**[0:23:34]** Archon. So, we can pause at any given node to ask for your input. So, we have this interactive PRD, where it'll have you sort of ideate with a coding agent to create that initial spec for a new application you want to create. We have the Ralph loop built as an Archon

**[0:23:50]** workflow. Uh man, there's just so many things that are here already. We even have an Archon workflow to help you build more workflows. We'll use this in just a second here. So, yeah, literally like no matter what you want to do with your AI coding assistants, it doesn't matter how

**[0:24:06]** many coding agent sessions you need, you can bundle it together into an Archon workflow, adding in reliability through deterministic nodes, like you always want to run validation at some point, or you always want to curate context in this way. The sky's the limit for what you can build with Archon. All right, so

**[0:24:22]** I'm just going to keep showing you some really cool ways to use Archon. I'm going to keep using the GitHub issue fix workflow because that is my most used, but there are so many amazing workflows you can use. And by the way, you can just ask it in the web UI here, what

**[0:24:34]** projects and workflows do you have? And so, the Archon agent in the UI is actually kind of special. It has all of the context around Archon, like our registered projects and workflows injected in at the start of the conversation. And by the way, in the web UI here, you can just click add project

**[0:24:53]** to give a GitHub URL or local path if you want to register more. So, right now, this is my only registered project, as you can see from the drop-down here. And then here are all of the available workflows, which this will also include any that you build on top yourself, but

**[0:25:06]** these are all of the default ones shipped with Archon. So, now, for example, I can say fix GitHub issue, and then if I go to the issue list here, we're currently handling this one and the other screen. So, we'll just do number three. So, I'll do number three

**[0:25:19]** for uh the rag YouTube chat project. So, we don't even have to call out the exact repo name, it can reason based on what we said and what context it has loaded to know which workflow to kick off. So, take a look at that. It invoked the Archon fix GitHub issue workflow

**[0:25:36]** specifically in our rag YouTube chat application. So, it does all of the routing for us from the web UI. And we can go into the logs, the beautiful screen. This is the exact same view we saw earlier, but this time we actually invoked it from the web UI. Very cool.

**[0:25:52]** And another really powerful thing I want to show you really quickly is that we can invoke a ton of workflows in parallel. And so, for example, I'm back here with Claude open in my rag YouTube chat application, and I can just say use Archon to fix GitHub issues 5 7 8 9 10

**[0:26:08]** and 11. So, the last six in that list there that we haven't touched yet, I just want to rip through all of these at the exact same time. And so, we can invoke Archon directly from our project, or we can have Claude Code open within our Archon repository, and we can point

**[0:26:25]** it to any code base if we just give it the path. And remember, it will automatically register Archon at that point. So, now it used the Archon CLI. Boom, look at that. Six times in a row, all of them are running as background processes, so we can see that right

**[0:26:37]** here, and we can continue to have it monitor for us, or even just ask us along the way, like, you know, like give us a status update. So, we can view it in the user interface. Like, if I wanted to go back to the UI now, we can see

**[0:26:49]** that we have all of these workflows currently running, or we can just have Claude Code constantly check for us. We could, for example, use the slash loop command in Claude Code to say, you know, like every 10 minutes, check on the workflows and restart if there's a failure or something, which there

**[0:27:03]** usually isn't. But yeah, so all six workflows are running, progressing through the early DAG stages. So, yeah, most of them are on the classify step right now, figuring out is the issue a new feature or a problem that has to be addressed. Super cool. All right, so I'm

**[0:27:16]** back, and we have the pull requests for all of our Archon workflow runs. So, we can see them all complete in the web UI as well. We can click into the logs just see what happened every step of the way. And of course, we can go see our final

**[0:27:29]** result. Going to the repository for the first time here, I'll click on pull requests, and boom, there we go. We have eight new open pull requests handling each of the issues that we handled with an Archon workflow. All right, the last thing that I want to show you really

**[0:27:42]** quickly here, and I'm going to expand upon this a lot more in the Archon live stream, is how we can build our own custom Archon workflows. Because yes, there are a lot of very powerful workflows that we have as the defaults for you, like some of that I already

**[0:27:55]** showed you in this video, but there's always going to be an opportunity to build your own, something very custom to you, or if you want to take another framework like GSD or B-MAD and bring it into Archon, or take a strategy like beads for memory, like anything you want

**[0:28:09]** to do, you can build it as a custom workflow for yourself. And you can take advantage of this workflow builder workflow that we have. I know it's very meta, but all you have to do is open up Claude Code in the Archon repository and just say, use the workflow builder

**[0:28:23]** workflow to help me make an Archon workflow. If I had a dime for every time I said workflow in this video, I would be a rich man. But that is all you have to say, and it's going to automatically load the Archon skill, and then ask you questions. It'll give you a chance to

**[0:28:39]** obviously describe the workflow you want to build, and then it'll run this full builder afterwards to create the YAML structure, and then you will immediately be able to run the workflow on any code base. So, for example, something fun that I thought I would try right now for

**[0:28:54]** this video is creating an Archon workflow that essentially takes the idea from beads. So, beads, it's pretty cool. It's an open source repo that gives persistent structured memory for coding agents. And so, I want to essentially build the idea that we have here into an Archon workflow. So, I'm just going to

**[0:29:10]** copy this repo, paste it in here, go into my speech-to-text tool and say, I want to build an Archon workflow that incorporates beads. Basically, just taking all the ideas from beads in a simple sense. So, I want you to search through this repository, understand how it works, and then build this as an

**[0:29:27]** Archon workflow so that we can use beads to create any new feature on any code base. So, there we go. I'll send that off, and it's going to do some research and thinking for me, and then obviously invoke this workflow to create the final YAML. So, I'll show you that when it's

**[0:29:42]** done. And there we go. We have our full workflow created. It starts with exploration, then it decomposes the feature request into individual tasks. and We implement them in a loop with progress tracking, validating everything at the end as well. So, taking a lot of ideas from Beads and building a full

**[0:29:59]** Archon harness around it. So cool. We can also view the full workflow within the user interface. We're working on a workflow builder, so it's like N8N but for AI coding. Super cool. A ton of awesome things that we're actively working on right now with Archon. It's just in beta. Probably going to be some

**[0:30:14]** bugs that you'll find when you try it. A lot of new things that we're going to be adding over the next couple of months here. It is my biggest passion project. And so, please give it a shot. I think you'll really like it. And also, I would love to see you at the Archon livestream

**[0:30:27]** this Saturday at 9:00 a.m. Central Time. Going to be diving a lot deeper into building workflows and running them and showing you all these really cool features in Archon. So, I hope to see you there. Otherwise, if you appreciate this video and you're looking forward to more things on Archon and AI coding and

**[0:30:41]** agent harnesses, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
