---
type: raw-transcript
title: "The Subagent Era Is Officially Here - Learn this Now"
youtube_id: GX_EsbcXfw8
url: https://www.youtube.com/watch?v=GX_EsbcXfw8
slug: the-subagent-era-is-officially-here-learn-this-now
published: 2026-03-18
duration: "0:15:15"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** GPT 5.4 mini and nano were just released and for the first time ever it's called out in the headline for these models that they are built for sub aents especially for AI coding and this is more important than you would think. I mean yes these are fantastic models and

**[0:00:15]** we'll talk about that as well but what's more important here is the message from OpenAI. They are putting a lot of effort into designing LLM that are specifically meant to be used for sub aents and sub aents are just a big deal right now in general. There's a lot happening with

**[0:00:30]** them in the industry. Cloud code is building a lot around sub aents. We also have Google that just released Gemini 3.1 Flash Light built for intelligence at scale. Recently, there's been more focus on building the smaller models than the larger most powerful ones. And that says something. That's why I'm

**[0:00:46]** saying we're going into the sub agent era. And so, I want to talk about what that means for you and just share with you how I'm using sub aents right now because I'm using them for literally everything. All of my research, all of my AI coding workflows. Now, for the

**[0:00:59]** longest time, Claude Haiku 4.5 has been my model of choice whenever I want something extremely cheap and fast for my sub agent usage. So, I'm using sub aents all the time for web research and codebase analysis. We'll talk about that in a little bit as well. But for a very

**[0:01:15]** cheap model, it's still not that fast. 53 tokens per second is pretty good, but we're still paying $1 for every 1 million input tokens and $5 for every 1 million output tokens. So, it's still not extremely cheap. And so now we have GPT 5.4 nano and mini. Even nano is more

**[0:01:34]** powerful than claude haiku 4.5. And it is a fifth of the price. And look at the throughput here. 188 tokens per second according to the 5.4 nano listing on open router. And even 5.4 mini is cheaper than cloud haiku. Also very very fast. This is way more powerful than

**[0:01:54]** cloud haiku 4.5. And so I'm literally thinking I might want to switch to codecs from Cloud Code because of how much I love using sub agents. Now I know benchmarks aren't everything, but let me quickly show you why I'm saying these models are a lot better than Haiku 4.5.

**[0:02:09]** So the benchmarks right from OpenAI say that 5.4 Mini and Nano, they actually crush the predecessor GPT 5 Mini. But if we look at LiveBench, GPT5 Mini has a global average score across the benchmarks of about 66. And then looking at Claude Haiku 4.5, it's only 61. So

**[0:02:30]** LiveBench doesn't have 5.4 mini and nano yet, but even looking at the predecessor that even is still better than Claude Haiku 4.5. And so we're seeing these cheaper and faster models that are also getting way better at the same time. But let me also be very clear here. The

**[0:02:45]** point of this video is to not just shill the new OpenAI models. Yeah, they're cool, but I want to focus on the trajectory here. Especially with competition, we're going to keep seeing all of these smaller models being built that are faster, cheaper, and still really powerful. And if we keep this up,

**[0:02:59]** we're eventually going to get to the point where we pretty much have an unlimited budget for sub agent usage. And that's going to unlock so much for us to solve a lot of these problems around context rot. Let's talk about that right now. So, the simple idea behind context rot is large language

**[0:03:15]** models get overwhelmed with information just like people do. Just because your quad code, codeex, whatever can support 1 million tokens doesn't mean you should overload it with that much information. We see a general decline no matter the large language model as we load it with more context. So there's more

**[0:03:32]** hallucinations. It picks out specific information. We need it less often. This is a real problem. There's a lot of solutions to context rod. I actually covered it in my last video that I'll link to right here with the whisk framework. And one of the most important things that I covered there is isolation

**[0:03:48]** with sub aents. If we want to keep our main context clean so that our main agent can be very focused, especially during AI coding sessions, one of the most important strategies is to delegate a bunch of codebased analysis or web research to sub aents. These are the two

**[0:04:05]** uses of sub aents that I'm relying on every single day pretty much every single AI coding workflow because we can have it do tens or even hundreds of thousands of tokens of research and then just provide the context that we really need to our main agent. So we can extend

**[0:04:22]** our coding agent with all these arms of sub aents doing different context gathering but then still keeping our main agent very focused. And this is becoming more and more plausible to do an insane amount of codebase analysis and web research because these LLMs that we can use to power our sub aents are

**[0:04:39]** getting cheaper and better and faster. Now, the reason we care so much about using these faster and cheaper models for sub agents is because the work that we're delegating to the sub aents are the kind of things that are super tokenheavy, but also don't require as much reasoning power. So, it's overkill

**[0:04:56]** to use something like GPT 5.4 high or claude opus 4.6. If we use those larger models for sub aents where we're doing hundreds of thousands of tokens of codebase research and web research, you're going to hit your rate limit for your coding agent very very quickly. But if you're using these faster models that

**[0:05:15]** are so dirt cheap comparatively, your sub aent usage is only going to make up a couple of percent of your total rate limit for the week. And so we need this efficiency because with these cheaper and faster models, the scale is incredible for what we can do with sub

**[0:05:32]** aents and it's only getting better and better. That's why the industry is leaning so much into sub aents right now and all these tools are building a ton of support around them. Cloud code was the first coding agent to introduce sub aents but even they have had a lot of

**[0:05:45]** recent changes adding support for building custom hooks per sub agent. Their documentation just grows every single day with what they're building into sub aents. We got them in codeex obviously as well. This is where we can use GPT 5.4 mini and then it's experimental in the Gemini CLI. It was

**[0:06:02]** added to GitHub co-pilot recently for research, code analysis, code review. A lot of these coding agents have sub agents built directly in. So you don't even have to create custom ones anymore either for most things. We have it in cursor of course. We have it in open code as well. The point is, every single

**[0:06:18]** coding agent and large language model provider is focusing so much on sub agents right now. Okay, so with that, I want to give you one big word of warning for using sub aents. Then we'll get into exactly how I use them every single day so you can walk away with some immediate

**[0:06:33]** wins. So there's a video I put out on my channel recently covering this diagram. I'll link to that video right here. This is just my entire AI coding workflow that I'm using every single day. and obviously sub aents for context isolation and research is a big part of

**[0:06:49]** that. So like I said earlier codebased analysis and validation and web research but only those things. My word of warning is do not try to use sub aents for implementation. It doesn't work. I only use it for research because we are spending tens or hundreds of thousands of tokens analyzing things and only

**[0:07:10]** returning a small summary to our main agent. That works well for research when we're just trying to synthesize a bunch of information. But for implementation, our main agent needs to be aware of all of the files that we're changing. Otherwise, it has no way to validate. There's a lot of hallucinations that

**[0:07:26]** have happened here. In my experience, I've tried to use sub agents where I have my front-end sub aent, my backend sub aent, my database sub agent. They all work in parallel, but they're not talking to each other. They're not giving the main agent everything that it needs. And so, there's a lot of problems

**[0:07:41]** that come with this. So stick to your main agent for your implementation, but then at the start of your coding session when you're just going through the planning, that is when I recommend using sub agents a ton. And so with that, let's get into how I use sub agents

**[0:07:56]** every single day. All right, I got a super quick interruption because I built my own agentic rag agent with a new database I've never used before that I'm super excited to show you. The sponsor of today's video is Oracle. And I'm excited for this one because of how

**[0:08:10]** they're approaching AI infrastructure with their AI database. So, if you've ever built any rag system or AI agent before, you know that your architecture looks something like this. You have the main database for your app and then usually you'll have a separate vector database, maybe even a separate graph

**[0:08:27]** database. You have your embedding API and the pipeline to sync everything together. That's how it's always been done. But it's not easy to manage all of that. And with Oracle's AI database, everything is unified. So you have the embeddings built right into the database and you can do your semantic keyword and

**[0:08:44]** even knowledge graph search all in one place. I've never seen something like this before. I even have my own agentic rag system that I created on top of the Oracle AI database that I have packaged up into this Jupyter notebook that I'll link to in the description. And so

**[0:08:58]** really quick, it just loads sample documents. I demo some of the different search strategies that are native to the database and then I create a lang chain and lang graph agents. I'll show you this right now. I'll run a demo here where we send in some queries and we can

**[0:09:11]** watch it perform the different search strategies in the Oracle AI database. Come back with the relevant documentation to then give us our final answer. And Oracle has an open- source AI developer hub giving you a bunch of resources to leverage their platforms like their AI database. And I actually

**[0:09:27]** submitted a poll request for this Jupyter notebook. It got approved. So I'll have a link to this in the description. Like I said, you can go and run the whole thing yourself. All right. So I'm here now in my cloud code and I'll obviously show codeex as well

**[0:09:39]** because that's where you can use the new 5.4 models. So whenever I am starting a brand new AI coding session to knock out a feature or a bug fix, I always start with my prime command. So no sub aents yet. I want to load a high-level overview of the project into the context

**[0:09:56]** of my main coding agent. That's the workflow that I walk through right here. But now at this point, our main cloud code instance is loaded up with context. And now I want to use sub agents very extensively. I'll do this every single time. When I'm working with larger code

**[0:10:12]** bases, there's a lot of context to sift through to figure out what parts of the codebase do we really care about addressing for this feature or bug fix. And so for brand new projects or simple projects, you don't really care about sub agents. There's not really going to

**[0:10:26]** be a problem of context rot. But I'm working in my archon codebase. More on this coming on my channel soon, by the way. But the point here is it's a very complicated codebase. I have a ton of different packages. There's tens of thousands of lines of code. I don't want

**[0:10:39]** to just dive right in and say like, hey, look at my codebase and try to find the right files to address this feature. I want to use sub agents because I need that context isolation. So, I'll give you kind of a random example here, but like a real example. I hope this helps

**[0:10:53]** drive home the point for you here. So, I'll go into my speechto text tool and I'll say, I want to address a bug here. So, the issue I'm running into right now is whenever I start multiple workflows in the same conversation, they share the same work tree. So, I want you to help

**[0:11:06]** me plan this fix by spinning up three exploratory sub agents. One to search the web for best practices for handling work trees with these AI coding workflow execution tools. Another one to research the web adapter and see how the bug applies there. And then another sub agent to research the backend and see

**[0:11:24]** how we are managing work trees with conversations. So there we go. I'll send this off. And this isn't even using any sub aents that I've built for myself. Like I said, a lot of these tools are implementing sub aents directly into the platform. So we can use them out of the

**[0:11:40]** box without having to define anything. And these built-in sub aents are smart enough to use faster and cheaper models under the hood. So when we invoke the web researcher and then the other sub aents that we'll see in a second here like our codebase analysts, these are again both sub aents built into cloud

**[0:11:56]** code. They are using either haiku or sonnet under the hood instead of opus which is the model that my main context window is working in. So a clear example here of working with different models depending on if we're in our main session or if we're in a sub agent. And

**[0:12:12]** we can do the exact same thing with codecs. And so I'll just do the same prompt here. I have a bug right now where work trees are shared when I'm invoking many workflows in the same chat. So spin up three sub aents. One to do web research on best practices around

**[0:12:26]** workree management. One to look into this bug as it relates to the web adapter. And then one to look into the backend. So doing just a bit of a shorter prompt here for the sake of example. But then what I can also do is say I want you to use GPT 5.4 mini for

**[0:12:40]** these sub aents so they can be faster and cheaper. We want to be more context efficient here. And so we'll see in just a second when codec spins up these sub aents it'll explicitly tell us that they are using the new GPT 5.4 mini model. And this is so incredibly fast. It's

**[0:12:57]** really cool to see. So there we go. It's spawned three sub aents and each one of them is using GPT 5.4 mini with medium reasoning. We don't need that much reasoning here because all we're doing is synthesizing information. And I know this is a pretty basic example overall,

**[0:13:13]** but you can spin up dozens of sub aents in parallel. A lot of times when you're working on very large code bases or projects that have many code bases, there's so much context curation you have to do to really identify the problem for a bug fix or exactly where

**[0:13:28]** you need to implement a new feature. Running code reviews as well is another really good use of sub aents. There's so many times where I'm just relying on sub aents very very deeply. Like I wouldn't be able to work without them. So take a look at this. All of our sub aents are

**[0:13:42]** done across both coding agents. For Clawude Code, we used 80,000, 96,000, and 40,000 tokens across the three sub aents. And then for Codeex, it's even crazier. We used 70,000 for our uh research into the front end. And then we used almost 2 million tokens for our web research and almost 1.5 million for our

**[0:14:04]** backend research. This would be completely unreasonable if we were using larger models. But thanks to these super cheap models that are still pretty powerful, we can extend the arms of our coding agent this much to help work with larger code bases. And by the way, for cloud code, we can specify the model

**[0:14:22]** like we can tell it to use haiku for the sub aent or use sonnet for the sub aent just like we did here in codec. So a lot of flexibility, a lot of control here. I'm using sub aents for everything. That's where the industry is heading going into the sub aent era. So, my

**[0:14:37]** encouragement to you is to just try using sub agents for literally everything, not just the planning process. Another random example that's super useful is sometimes when I'm working on a feature, I'll find an unrelated bug. And so, I'll just spin up a sub agent to research that bug and

**[0:14:52]** create a GitHub issue. So, it's sort of like a sidecar so I'm not polluting my primary work. There are a million uses for sub aents and it's just going to get cheaper and faster and better over time. And so if you appreciated this video and you're looking forward to more things on

**[0:15:06]** AI coding and using sub agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
