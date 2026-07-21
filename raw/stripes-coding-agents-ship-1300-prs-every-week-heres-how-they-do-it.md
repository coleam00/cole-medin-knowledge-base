---
type: raw-transcript
title: "Stripe's Coding Agents Ship 1,300 PRs EVERY Week - Here's How They Do It"
youtube_id: NMWgXvm--to
url: https://www.youtube.com/watch?v=NMWgXvm--to
slug: stripes-coding-agents-ship-1300-prs-every-week-heres-how-they-do-it
published: 2026-03-11
duration: "0:18:51"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A few weeks ago, Stripe dropped a bombshell for us. They are now shipping over 1,300 poll requests every single week that are completely AI written. So, humans review the code still, but they don't write a single line of it. And for an organization at this scale, they have

**[0:00:17]** to have a lot of reliability to make that possible. So, they built their own internal agent harness called Minions. And they published a couple of blog posts covering exactly how this works. And so, yeah, it's a flashy headline, but when we get into these blog posts, and that's what we're going to do today,

**[0:00:33]** there are a ton of super valuable lessons. And so, think about this. Stripe, it has a very complicated codebase. They have a backend written in Ruby. It's an uncommon stack. They have a vast number of homegrown libraries that are generally unfamiliar to large language models. And on top of that,

**[0:00:51]** being Stripe, they have very high stakes because they're moving over $1 trillion in payment volume per year. And so complicated codebase, everything has to be perfect. And so if they've built a system that's reliable enough to ship at scale for them, really any company, you would be able to do this. And so that's

**[0:01:09]** what I want to get into today. How Stripe has made this possible. How you can take these ideas that we'll get into and apply them for yourself. And this is even more important than you would think because a lot of these larger companies are starting to build their own agent

**[0:01:22]** harnesses to make AI coding more deterministic, more reliable. So Shopify, they created their own structured AI workflow engine as well called Roast. They actually open sourced this. I'll link to this in the description. Airbnb is doing the same thing, especially for helping with their test migrations. And then AWS has their

**[0:01:40]** own internal tooling as well that they've started to share about in a blog post. So all these companies are building structured AI workflow engines. But what does this mean exactly? Let's get more specific now. And of course, to make this super clear for you, I have a handy dandy diagram. So, we'll start

**[0:01:55]** with the highlevel pattern. How do all of these structured AI workflow harnesses work? Then, we'll get into Stripe Minions specifically. I'll refer back to the blog post and pick out a lot of the key information there as I go through this. And then, honestly, most importantly, I want to cover how you can

**[0:02:12]** extrapolate these ideas to build your own workflow. How can you take these ideas? You can build something like Stripe Minions for yourself honestly very quickly. Having this combination of agent nodes and more deterministic nodes, this is what defines our workflow to make things more reliable for our coding agents. And I'll get a lot more

**[0:02:30]** specific on this as we explain the pattern here. So just like any agentic engineering task, we have some kind of entry point. This could be the cloud code or any coding agent like you would normally use. We'll talk about this, but in Stripe, they use Slack as the way to

**[0:02:44]** talk to their minions pretty often. Whatever that is, we have some entry point that is going to kick off a larger workflow. The important thing here is that we have steps of the workflow that we don't want the agent to do. And so, the AI coding assistant is only running

**[0:03:00]** for parts of the workflow. Otherwise, we have certain steps that we're going to run deterministically. like we are going to guarantee that after the coding agent writes some set of code, we are going to run the linting and the type checking, the unit testing. If there are any

**[0:03:14]** failures, then we loop back to the agent and have it fix these things and retry. And so the important thing here is that the agent isn't controlling the system. The system is controlling the agent. We have these guarantees and we force the agent to retry whenever there are any

**[0:03:31]** issues that come up. And this is so powerful and it honestly it's fundamentally different from a lot of the ways that we typically use our coding assistants cuz a lot of times we just have the agent. We don't have any other parts to the workflow. So we'll have the agent do the planning, do the

**[0:03:47]** implementation, do the validation like creating the unit tests and iterating on those. But the problem with that is it's not a guarantee that the agent will run all the validation that we want and in the way that we want. And so we enforce that by building these workflows that

**[0:04:02]** combine these non-deterministic agentic and deterministic nodes. And that is exactly what you need when you have a lot of very complicated code bases with high stakes. And so that brings us into minions. Now, and one really important caveat here is Stripe does have over 3,400 engineers. They are shipping over

**[0:04:21]** 8,000 pull requests every week. And so this is only a small percentage of PRs right now that are completely AI written. But this number is growing rapidly. Minions is becoming a critical part of their engineering stack. And the goal with minions is to allow unattended agents to oneshot tasks. And so this is

**[0:04:41]** fundamentally different from an engineer working with their coding assistant. So they still are using claw code and cursor for their daily work, but for anything that they want to just try to have the agent knock out like a GitHub issue, they just want to send off some requests in Slack. That is what Stripe

**[0:04:57]** Minions is for. And it's cool because in their blog post, they even show an example of what it looks like to talk to a minion in Slack. So they start a thread here. So they mention the dev box. We'll talk about the dev box in a little bit. and they're giving a ton of

**[0:05:09]** context around this issue and even parts of the codebase that the agent can go and look at right away. So something I really appreciate about this is just how much context is included up front so that the agent isn't making assumptions about the work that it's about to

**[0:05:23]** oneshot here. Okay, so the core idea behind Stripe Minions that I'll show in my diagram as well is blueprints. This is how we create our workflows that combine agent and deterministic nodes. And I want to hone in on this here for a bit because there are some great lessons

**[0:05:40]** to pick out of even just this section of the blog post. And so first of all, they say the most common primitive for orchestrating an LLM flow is either a workflow or an agent. And there is a big big difference here. A workflow is an LLM system that operates via a fixed

**[0:05:58]** graph of steps. And so we are building the model into the system versus having the system be the agent. kind of like what I was saying earlier. And so we're still using a large language model at certain steps of the way, but we are still defining the exact process that we

**[0:06:13]** go through every single time. It's more deterministic. On the other hand, with agents, it's more of a simpler loop with tools orchestration pattern. You can think of it like the agent is defining the workflow in real time because it decides what tool calls to make, how many to make, if it should make any at

**[0:06:29]** all. This is how we usually work with our AI coding assistants where we send in instructions for maybe a workflow or a skill that we want it to go through, but it still has to use its reasoning power to figure out how to make all those tool calls to build that workflow

**[0:06:43]** in real time. And that is really powerful, but it's also dangerous, especially when you're a company like Stripe and you need to guarantee that we have certain context creation and certain validation that takes place. So within these workflows, a given node can run either deterministic code or an

**[0:06:59]** agent loop focused on a task. And this is what I really love. In essence, a blueprint is like a collection of agent skills interwoven with deterministic code so that particular subtasks can be handled more appropriately. A little bit of a mouthful, but this is so powerful. And they even have a diagram here that

**[0:07:16]** shows what these workflows look like. So everything with the in the cloud here, this is an agent task. And then everything in the squares is a deterministic task. And this is a lot like what I have in my diagram for you here. So let's get into this right now.

**[0:07:29]** So we start with our entry point like Slack is the most common one, but they support the CLI as well. And then before we even send the engineers request to the agent, we already have a deterministic node at the start of the workflow for context curation. So there

**[0:07:43]** are two things that we do here. We are going to curate documentation and the tools that the agent needs. And so we're going to use MCP tools deterministically here. So, not giving it to an agent, but right within code, we're going to search through tickets and documentation. Basically, combining relevant

**[0:08:00]** information with the Slack prompt to send in as context to the agent. And then, not only are we going to use MCP tools for context curation, we're also going to pick out a subset of them that we want to give into the agent. So, it has these capabilities. And so this

**[0:08:17]** massive set of MCP tools, this is a single stripe MCP server that they call tool shed. And so it has over 400, actually around 500 MCP tools for all of the internal systems and SAS platforms that they use. And so we need to pull documentation, look at build statuses,

**[0:08:37]** run some external testing, whatever that might be. There's this massive set of tools, but we don't want to overwhelm the agent with tools. And so we need some kind of way to figure out at first based on the request, what smaller subset of capabilities do we need to

**[0:08:51]** give into our agent. And so that's the other part of the context curation that we're doing here. The sponsor of today's video is Postman. And I am genuinely excited about this because I've been using Postman for almost a decade now. And they just had a massive update making them the AI native API platform.

**[0:09:08]** Until now, Postman has always been a tool that you just run alongside your IDE. You have your specs and collections for your APIs running in the Postman cloud like we're looking at right here. And then you have your code base locally. So it's very very separated. And on top of that, you have to figure

**[0:09:25]** out how to run your tests in your CI. So three different workflows for the same API. But the new Postman solves this because it's now git native, which is very powerful. Let me show you what I mean. Take a look at this. I can now manage all of my Postman collections and

**[0:09:41]** environments, everything directly in my codebase locally. And it's all very simple YAML files that sync with the changes that I make in the Postman desktop app. So I have this set up locally right now. I can also switch to the Postman cloud where things are being synced and any changes that I make here

**[0:09:58]** like I'll just make a super simple one. It is automatically reflected in version control. So now I can go into my terminal, run a git diff, and you can see that it's super easy to track the changes to our API tests. We can version control them just like our codebase. And

**[0:10:12]** here's the best part. Watch this. Because everything is now just local files on our disk, their agent mode can actually coordinate across your entire API life cycle. So you describe what you need in natural language and it can create entire collections, generate specs, write tests, set up mocks, keep

**[0:10:28]** them all in sync. It can even scan your codebase and autodiscocover every endpoint. Plus, you can pick the AI model claw GPT self-hosted whatever fits your stack. And the same collection that runs on your machine will run in your CI pipeline. Pre-commit hooks, GitHub actions, no rewriting tests for

**[0:10:44]** different environments. One workflow everywhere. So, Postman has definitely stepped it up a notch recently. I would highly recommend checking them out. I will have a link to Postman and my example GitHub repository in the description. And then after our context curation, that is when we run the agent

**[0:11:00]** for the first time. And so the agent does the implementation. We have a deterministic step for linting and type-cheing with sorbet. And then we address any of those issues that come up with another agent node. And this entire step, everything that runs the agent is running in an isolated dev box. And so

**[0:11:16]** they specifically say that using work trees and containers running on the developer's laptop, it's really hard to get the permissioning right and to make that scale. And so what they do is every single time a minion runs, it runs in an isolated AWS EC2 instance running in the

**[0:11:31]** cloud. And these instances are spun up very quickly. They come preloaded with the Stripe code bases, the lint caching, everything they need to make it blazing fast. And they call it cattle, not pets, as in these instances are not important. We can spin them up and tear them down

**[0:11:46]** willy-nilly just based on the demand that we have right now for the engineers working with minions. And so everything runs with full permissions in a secure isolated environment that also scales really well for parallel execution. A single engineer, they say this in the blog post as well, oftentimes has many

**[0:12:03]** of these minions running at the exact same time. And so all actual development goes on right here in the box. And then also we have a deterministic step at the end where we're going to pull a part of the test suite to run against the change that was just made. So this is crazy to

**[0:12:18]** me, but Stripe has over three million tests in their CI. So we're going to pick out just a small portion of them, kind of like the MCP server. We just need a small portion that we're going to run and then give feedback to the agent for anything that is failing. So we

**[0:12:32]** iterate here a maximum of two times before we escalate to a human because we don't want infinite loops with unit test errors. Otherwise, once the agent is done with its fixes and the tests are passing, then we go to the human review. So important to say here again, we are

**[0:12:46]** never vibe coding here at Stripe, right? They are always doing human review at the end of every stripe run. But the point is with a much more reliable workflow curating the right context for the agent with exactly the validation it needs, we can be more confident that by

**[0:13:00]** the time the review comes to us or I should say comes to a Stripe engineer, they can be a lot more confident. The review is going to be faster, the code is going to be more reliable and it leads to emerge very quickly. All right, so I want to finish off by talking more

**[0:13:14]** about why we care about adding determinism into our AI coding workflows and how you can build this yourself. So the big question you might have right now is why do we care about not having agents do everything? I mean theoretically they can through skills and commands we can have it do the

**[0:13:29]** context curation implementation and validation but Stripe does a really good job explaining this in their blog post. They say in our experience writing code to deterministically accomplish small decisions we can anticipate like we always want to lint changes at the end of a run it saves tokens so it saves on

**[0:13:45]** cost at scale and it gives the agent a little less opportunity to get things wrong. This is important just because coding agents are getting more powerful. Same with LLMs. We still have these issues where large language models won't do exactly what we say or they'll skip steps entirely. So in aggregate we find

**[0:14:02]** that putting LLMs in contained boxes like having separate nodes for the agents separate for deterministic steps it compounds into systemwide reliability upside and that is what they're doing with blueprints. That's what all these other companies are doing as well like Shopify with roast. I'm even playing around with a lot of these ideas myself.

**[0:14:19]** I'll talk about in a sec here. So the example here with Stripe Minions it might not be 100% applicable to you. You probably don't have an MCP server with 400 tools or have to do as much context curation. You also probably don't have three million or more tests in your test

**[0:14:35]** suite. But the idea here we can certainly extrapolate to a workflow that any engineer, anyone using AI coding assistance would be interested in using. This is what I call the PIV loop. I've covered this a lot on my channel before. The idea of planning, then implementing, and then validating. And you do it

**[0:14:52]** across multiple AI coding assistant sessions. And so we can create a deterministic workflow, partially deterministic workflow similar to what Stripe has done for minions. So just giving you an example here of something we can build. And it is quite easy to build this yourself. And so my typical

**[0:15:09]** workflow for working on any feature request or bug fix is I'll start with the planning phase. And so I'll have some kind of initial context like my feature request or a GitHub issue and then I'll have the agent plan the implementation or the fix. And usually I'll iterate with the coding agent on

**[0:15:24]** the plan, making sure that everything is good for validation and the success criteria, things like that. And that'll output a single structured plan that I'm now going to I'm going to cut off the context window. So brand new context window. Feed this plan into a second agent to do the implementation. This

**[0:15:41]** split is important because I want to keep my implementation agent very very focused. And then after the implementation, this is where I can add a deterministic node for validation just like Stripe does with Minion. So I can run my linting, type checking, unit testing, whatever that might be, no

**[0:15:56]** matter the programming language, like you can see here, and then have the coding agent loop back and fix anything that comes up in the testing that we run and then have a pull request review at the end and then merge. So a pretty similar workflow to what Stripe has, but

**[0:16:10]** a lot more generalized to like you could use this for building anything with AI coding assistance. And so we have these deterministic steps of enforcing a loop of human review for the plan, getting a fresh context window for implementation, running the validation. This is super powerful and like you can do this

**[0:16:26]** yourself across different coding sessions and adding the validation for the agent to do, but it's much more reliable when you have it set up in this way. Now, as far as how you actually build these AI workflows yourself, there's three things that I have to say really quick here. First of all, use

**[0:16:42]** Roast by Shopify as an example. So, Stripe Minions is unfortunately not open source, but Shopify did open source their version of these structured AI workflow harnesses. Really powerful example here. They even have some quick starts that show you what it looks like to have workflows where you have

**[0:16:59]** deterministic nodes combined with non-deterministic agentic ones. So, use this as a starting point if you're interested in building anything yourself, even using it as context for your AI coding assistant. Also, in the Dynamis community, this Friday at 11 a.m. Central time, I'm doing a workshop showing exactly how to build these more

**[0:17:18]** deterministic agent coding workflows, both with the Cloud Code CLI and the Claude Asian SDK. So, come join the community if you're interested in being a part of this and all the other courses and workshops that I have in the community. A lot going on within Dynamus. And I do certainly want to have

**[0:17:34]** YouTube content soon as well on this same thing. So, not just trying to like get you to join the community, though I would love to have you, but just saying this is where I'm covering it first. And then also, there's a lot of work I've been doing under the hood with Archon.

**[0:17:46]** Just teasing this super fast here. Archon is the AI command center. I've been doing a big overhaul with it under the hood the past few months here, turning it into basically what Shopify roast in Stripe Minions is a place for us to run these workflows in parallel. We can watch the logs and go through all

**[0:18:04]** the observability we need. There's even a workflow builder that I'm in the middle of creating right now. So, it's basically like Minions and Roast, but you can even define your workflows in a beautiful UI. I'm calling it the N8N4 AI coding. So, a lot of cool things I'm

**[0:18:17]** working on related to this under the hood. It's been a lot of validation recently seeing what these big companies are doing cuz it's very similar to what I'm working on. So, that my friend is everything that I have right now on Stripe Minions and building these structured AI workflows. This is

**[0:18:32]** definitely where the industry is heading, not towards more power to the agents, but more power to the system controlling the agents. And so, if you appreciated this video, you're looking forward to more things on AI coding and building these kinds of workflows, I would really appreciate a like and a

**[0:18:47]** subscribe. And with that, I will see you in the next
