---
type: raw-transcript
title: "You're Hardly Using What Claude Code Has to Offer, it's Insane"
youtube_id: uegyRTOrXSU
url: https://www.youtube.com/watch?v=uegyRTOrXSU
slug: youre-hardly-using-what-claude-code-has-to-offer-its-insane
published: 2026-03-23
duration: "0:14:43"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Cloud Code has been shipping features at a ridiculous pace recently. And even if you're not using Cloud Code as your primary driver, it is still fascinating to see how far these tools are pushing the limits for AI coding. Remember, it was only a couple of years ago that we

**[0:00:17]** all were using these tools just for autocomplete. And then in the last year especially, we've gotten to autonomous agents that build out entire features end to end. And now Claude Code is leading the charge, turning their coding agent into essentially a multi- aent orchestration platform. It's very powerful with all their recent emphasis

**[0:00:36]** on agent teams and sub agents and even coordinating your work across devices. So that's what I want to cover with you right now. All of the biggest new features added to Cloud Code in the last couple of months. And yes, you heard that right, only the last couple of

**[0:00:51]** months because that alone already gives us about a dozen features that I want to cover with you right now. like the new 1 million token context window, agent teams, we have get workree support, new commands built right into cloud code. Of course, we have the new remote control.

**[0:01:04]** A lot of other ones that we'll hit on very quickly. And the important thing for all of these is you might be using some of these features already. Others you might not have even heard of, but for all of them, I'm also going to give you some tips and tricks for when you

**[0:01:17]** want to pay attention to these features and when it might not be important for you, so you can focus on using the parts of the tool that actually matter for you. So with that, let's get into the first feature. First of all, we finally have support now for a 1 million token

**[0:01:31]** context window. It is now generally available for both sonnet and opus. And so with this, we can now fit up to 750,000 words into the short-term memory of quad code. So we can theoretically ingest entire code bases. Now, the unfortunate thing with this though, and this is very

**[0:01:49]** repeatable with my testing, is once you get to about 250 or 300,000 tokens, you will see a huge uptick in hallucinations. And so, at any point in your conversation, you can run / context to see your current token usage. And so, yeah, it's nice that we can go above

**[0:02:06]** 200,000 tokens now, but you don't want to actually push it that much further. Once you get to 250 or 300,000 tokens, you generally want to do a memory compaction or write a handoff prompt and start a new session. So, this is a feature that's really cool to have, but

**[0:02:21]** with the limits of the LLMs right now, we don't want to push it too far yet. Next up, we have agent teams. This is similar to sub aents, except these agents that work in parallel can now communicate with each other. So, they can knock off a task list at the same

**[0:02:36]** time, and they can make sure that they aren't stepping on each other's toes. And so for example, I can send in a prompt here where I want to create an agent team for a codebase review. So one is going to do a security review, one a performance review, and one a test

**[0:02:49]** coverage review. And they might need to communicate with each other because potentially the test coverage review agent might need to understand some of the security concerns that the first one raises. And so we need that real time communication. And if you use T-Max terminals like I am right here, you can

**[0:03:04]** see all of the agents working at the exact same time. And I can do controlB and any arrow to switch between the different sessions. So I can work with them in real time. So at any point I can interrupt any of the agents working in parallel on the right hand side here or

**[0:03:18]** I can talk to the lead agent and ask about how the agents are coordinating and inject more context at any point. It is very very powerful. I also have a video that I'll link to right here where I cover agent teams in more detail and especially how you can get the most out

**[0:03:32]** of using agent teams. Keep in mind that this is a very experimental feature. The agents don't communicate very optimally right now. And so I'd say it's really powerful when you want to build proof of concepts quickly, but I wouldn't use agent teams yet for anything that you're going to be shipping to production. All

**[0:03:47]** right, so now we've gotten to actually my mostused new feature for Cloud Code, and that is the native support for Git work trees. And this is a big deal because it allows us to very easily work with multiple copies of our codebase with claude at the exact same time. So I

**[0:04:04]** have one workree called feature 1, another called feature 2. And the important thing to see here is that we have a copy of our repo living in the.claude/workreees folder for each of our work trees. And real development is always working with feature branches and different pull requests. So if we want to do parallel

**[0:04:22]** work with claude code and we don't want our different feature branches to be overriding each other's changes then we need local copies of our codebase and now we can do that immediately with claude. We don't have to work with separate commands and run claude in different work trees manually like we

**[0:04:37]** had to do before. It saves me a ton of time. I'm using this every day. Next up we have a couple of commands that are now built directly into cloud code and these are powerful. So, Enthropic, they were using these internally for a while and they figured like, hey, if this is

**[0:04:50]** so good for us, let's just share this with everyone and build it directly into the tool. So, we now have /simplify and slashbatch. And I'll give you a demo of this one in a bit as well. So, slsimplify, you just run this after any implementation and it guides the coding

**[0:05:06]** agent on simplifying the codebase because we all know that large language models are way too prone to overengineering and so you end up doing this a lot yourself after anyway. So now it's just a tool built in for us. And then what slashbatch does is this allows us to handle larger changes in parallel.

**[0:05:24]** So we're orchestrating large scale changes across our codebase. Any kind of larger refactor is a perfect use case for slash batch because it splits up the work and then dishes out different agents to handle it. There are a million examples where you need to do larger refactors in a codebase. So just to give

**[0:05:40]** you a quick example, let's say I have all of these console logs splattered throughout my codebase and I want to replace everything with a more productionready logging strategy. So what I can do is just go into claude and say /batch replace all console log calls with a structure logger that I have

**[0:05:56]** already set up in my utilities folder. I can send this off. It's going to create the sub aents, handle all of the coordination itself, and then come back to me with a refactor codebase that can create my poll request. All right, next we have remote control. And this is

**[0:06:10]** super cool because it is the coordinating work across devices that I mentioned at the start of the video. What I can do is at any point within a conversation on my desktop here with cloud code, I can do slash remote control. This is going to create a cloud

**[0:06:25]** session that I can now use directly on my phone assuming I have the cloud app. So check this out. I'm going to refresh on my phone. I have the conversation here. If I send in a message like hi, then right now we can see it pop up instantaneously on my computer. So I can

**[0:06:40]** now work on my computer but from my phone anywhere. Super cool. All right, so for the next couple I'm going to stay pretty high level but they still are very important. Starting with sub aents. Sub aents are becoming a bigger and bigger deal for all AI coding tools

**[0:06:55]** right now. There's a video that I'll link to right here where I talk all about this. But yeah, it's just very cool the C-cloud code leaning into building more and more into sub agents. A lot to cover here. You can see the documentation is very extensive. I'll just focus on a couple right now. So,

**[0:07:11]** first we have persistent memory. It is not just our primary cloud code agent that can remember things for future sessions. Our sub agents can help with that as well. We can also define hooks at the sub aent level. Before the last couple of months, when you built a hook,

**[0:07:27]** it had to be used by cloud code all of the time. But now we can do it at a granular level for individual sub aents because different agents need different rules that we're adding in through hooks. So just very powerful the level of control that we have with sub aents

**[0:07:40]** now through these features and a lot of other ones. And then we have the new automemory. So claw.md this is the classic rule file. These are all the constraints and conventions that we curate for our coding agent. But now with automemory, Claude has another way where it can curate memories for itself.

**[0:07:59]** So it accumulates knowledge across sessions to learn from its mistakes, for example. Very, very powerful. It's enabled by default. We can disable it if we want. And it just builds up these memories in a memory folder within our global.claude. And so it's a bit more nondeterministic than the claw.md because we're not

**[0:08:15]** managing it. And I think both are still very useful, but it's about time that our coding agent can finally remember things itself without us having to prompt across our different sessions. So if you want absolutely the most control possible, I would recommend just sticking to the claw.md. But if you want

**[0:08:32]** to give your coding agent a bit of autonomy to learn from its own mistakes, then definitely rely on both the claw.md and automemory. So I hope you found all this really helpful for you so far. Next, I want to cover two small but useful commands that were added to

**[0:08:46]** Claude Code very recently. We have slashbtw and slashloop. So, starting with slash by the way, this is for when you want to have a sidecar conversation with claude codes. So, you want to ask a quick question, but you don't want to bloat your primary context window for claude

**[0:09:02]** code. So, imagine that this was a larger conversation that we're having here. It's just really simple for the sake of demo, but remember cloud code starts to hallucinate quite a bit once we get to about 250,000 tokens in the context window. So, we want to do everything in

**[0:09:17]** our power to prevent cla from getting there, including using /btwide questions we want to ask. Like, let's say I didn't know what CRUD stands for. I could say, what is CRUD, right? Like, I can have this very brief conversation, get the answer, and then I can escape out of this and continue with my work as

**[0:09:34]** if that never happened. So, it's for our own information, right? So, escape to dismiss and then we're back to where we were before. Now, one really important thing to understand with /btw is cloud code does not have tools when you're in this mode. So, it can't do any codebased

**[0:09:49]** exploration to answer your questions. It's only going to be able to answer things based on its knowledge and the short-term memory. So, only ask very basic questions with /btw. Otherwise, if you have a larger question that requires codebase analysis, have it kick off a sub agent to explore. Then we have the

**[0:10:06]** slashloop command. We finally have a way to schedule a recurring prompt in cloud code. And they have a really good example here. So let's say we just finished a bunch of work and we want to deploy it to production. So we kick off the CI/CD pipeline, but we want cloud

**[0:10:21]** code to wait for everything to be deployed to maybe do a validation at the end. And so we can do /loop. We're going to send in this prompt every five minutes. Check if the deployment finished and tell me what happened. Give me a status update at the end. And

**[0:10:35]** honestly, the possibilities are pretty endless here for how we can use a sloop. Just to give you another example here that I just came up with myself, I could do /loop every 30 minutes. I want to run all the tests to make sure everything is passing. So, we can have this sort of

**[0:10:48]** quality gate agent running at the same time. We're working with other cloud code instances. So, we can guarantee that we're constantly checking the tests as we're working. We could use something like a hook to alert us if any tests are failing. So, we can address that in our

**[0:11:00]** other instances. We can also use slashloop to automatically pull websites for information if we're waiting for some kind of update. There's a lot of things outside of coding that we can do with sloop as well. Also, earlier this month, Cloud Code finally built voice support into the platform. I have been

**[0:11:18]** using speechto text tools as my primary way to talk to Claude Code for over a year now. So, it's cool to see Cloud Code adding native support for this. You just have to do a /voice to enable it for the first time and then you can go ham. Now, one thing I will say, there

**[0:11:34]** are a lot of very powerful external speechtoext tools out there like I use Aqua voice. A lot of people love using Whisperflow or Eperenter Whispering, which that's a free and open source one by the way. And from my experience, these tools still are a bit better at least than the voice mode built right

**[0:11:49]** into Claw Code. So, still a reason to use these other tools, especially cuz then they work for every text box on your computer. But if you don't have one of those tools already, definitely do /voice and start using this. It'll save you so much time typing. Makes it

**[0:12:04]** especially easy to do those brain dumps that you need to do during your planning sessions with your coding agent. All right, so the second to last feature I want to cover with you really quickly is our ability now to adjust the effort level for any models in cloud code. And

**[0:12:19]** this is very useful because we need to balance the reasoning capability of cloud code with our token usage because we really want to avoid hitting either the 5hour or weekly token limits in cloud code. And so when we go into cloud code we can see the effort at the top of

**[0:12:36]** our session when we just started or we can run slasheffort at any point just like we can run slashcontext. And then when typically at the start of a conversation when you want to change the model you do slashmodel and then you can also use the left and right arrow

**[0:12:50]** keys to change the effort. So medium is the default. It also just generally is what I recommend having as a default. But if you're going into a session where you know you're trying to solve a very complex problem with cloud code or you want that extra regioning for whatever

**[0:13:03]** reason, you can go between low, medium, and high. And then opus specifically also has max effort which is going to use a lot of tokens but oftentimes this is worth it when you get really stuck on a problem. All right so for the very last new cloud code feature we have

**[0:13:19]** scheduled tasks and so in the same place where we have /loop they talk about this as well. We can set one-time reminders like remind me at 3 p.m. to push the release branch. And then also outside of any specific cloud code session we can also set up what are called cron jobs.

**[0:13:33]** These are tasks that we want to run at a recurring basis. Like every hour at the top of the hour, we want to run tests or check our CI/CD pipeline. Whatever we want Cloud Code to do on our behalf without us even prompting it. So, there's a few new tools built into Cloud

**[0:13:48]** Code to make this happen. They talk about the whole cron syntax here to specify how often we run things. But the useful part about Claude Code is we don't have to know this. We can just ask Claude to create these tasks for us. uh you know list out our tasks, even cancel

**[0:14:03]** certain ones. So, we manage all of these tasks under the hood just with natural language. It's very, very cool. So, there you go. That is everything big added to Claude Code recently. And let me know in the comments if you want me to make a dedicated video for any of

**[0:14:17]** these features cuz I definitely could do that. And I hope you can see with everything that we're adding here with the agent teams and sub aents and coordinating work across devices, all this is pointing to cloud code becoming this multi- aent orchestration platform. Very cool to see. And so if you

**[0:14:33]** appreciated this video, you're looking forward to more things on AI coding and cloud code, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.
