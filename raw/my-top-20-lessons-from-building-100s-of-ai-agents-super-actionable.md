---
type: raw-transcript
title: "My Top 20 Lessons from Building 100s of AI Agents (Super Actionable)"
youtube_id: OFfwN23hR8U
url: https://www.youtube.com/watch?v=OFfwN23hR8U
slug: my-top-20-lessons-from-building-100s-of-ai-agents-super-actionable
published: 2025-08-20
duration: "1:03:34"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I've got an exciting one for you today. What you're about to watch is a special live event that I hosted during the launch week of the Dynamus community. A ton of value that I've never shared on my YouTube channel before. I'm doing this in celebration of the Archon launch

**[0:00:14]** and reaching a thousand members in the community. So, just a thank you to you and a way to show you what we've got going on in Dynamis. So, this is lessons that I've learned from building hundreds of AI agents over the past couple of years. And it was actually really hard

**[0:00:28]** to condense all my lessons down into the top 20 that I present here in this event. So, a ton of value packed into this. And so, with that, let's get right into the event. And also, let me know in the comments if there's any strategies or tips that I cover here that you want

**[0:00:42]** me to make a full video on. There we go. And so, the plan for today is just to give you guys a bunch of really practical lessons that I've learned um just from building hundreds of agents over the last few years here. mostly the last couple of years. And I typically

**[0:01:00]** don't do presentation style videos or live streams. I'm usually either just chatting with you guys like I do in live streams or when I'm making a video, it's always like really hands-on, like let's code something. I want this to be like really practical and hands-on. Um, and so even though it is a presentation, I'm

**[0:01:17]** going to work hard to make it really engaging for you guys. So, typically I'm against just like showing slides. Um, but yeah, I've got my usual mix of like a little bit of memes and just a ton of practical advice for you guys here, uh, to keep it fun. So, yeah, there's 20

**[0:01:30]** lessons in total that I want to share. And, uh, the first thing I want to say before I kick this off at all is that, um, it was really hard to take something like lessons learned from building AI agents and like actually um, put it down into a presentation that I can give in

**[0:01:47]** less than 10 hours. I mean, there's so many things that I can talk about, different lessons that I've learned. And so the most difficult part out of all this is just thinking about what are like the few that are the most important that I can share with you guys. And so I

**[0:01:59]** could probably even do like another event just like this just sharing a whole another set of 20 lessons. Um but these 20 are the ones that I wanted to focus on the most with you guys. And so yeah, we'll just go through this right now. Um and starting with I want to kick

**[0:02:15]** this off here by just giving everyone a quick reminder of what an AI agent actually is. So I give this definition in the AI agent mastery course and a lot of you already know it at a high level what an agent is but I just want to give

**[0:02:27]** this um as a refresher for everyone. So an AI agent is a program that uses a large language model to reason about how it interacts with its environment and to take varying courses of actions to achieve a goal. And so there's kind of two parts to that. First we have

**[0:02:43]** interacting with the environment. Those are the tools that we give the agent to do something like um pull messages from a slack conversation or draft an email in Gmail or Outlook. Like that's the it interacting with its environment and then taking varying courses of actions. The thing that makes agents so powerful

**[0:03:01]** and also dangerous as we'll see in a little bit is that it can decide what it wants to do based on what goal you have for it. And so it might decide to take five steps or three steps or one. We don't know. It's it's non-deterministic in that way because we're letting the

**[0:03:17]** agent have that level of control. And so that's an agent at a high level. And then what I want to dive into for my lessons with you guys today is I want to start with u a few highlevel lessons that I've learned from building agents. So just kind of zooming out to the top

**[0:03:33]** level of just building agents as a whole. And then I want to give you lessons that are specific to each of the different components that we have for an AI agent. And so if you've been through the first part of the AI agent mastery course, you've seen this graphic already

**[0:03:50]** because one of the very first videos that I have in module one of the course is breaking down the different components to an AI agent. We have the agent program. This is the system prompt, your general instructions to the agent for how you want it to behave and

**[0:04:02]** the tone that you want it to have. You have the large language model. That's the brain of your agent that has all that reasoning capability. And then you have the tools. These are the capabilities that you give your agent to interact with its environment. And then last we have the memory system. So that

**[0:04:17]** is both short-term memory like the conversation history and then also long-term memory being able to remember your preferences and goals and things like that between conversations and also rag and just like knowledge bases in general is often considered a part of long-term memory within the memory systems as well. So yet another quick

**[0:04:36]** refresher there on the components of an AI agent. I'm going to give you lessons that I've learned specific to each of these just as a way to keep this presentation really really organized for you guys. Um, and so then after I go through all this, I'll I'll also open up

**[0:04:48]** a time for a Q&A. Um, probably within the last like 15 20 minutes of the hour that we have here. Um, and so I'm going to try to go through one less lesson every two minutes because I have 20 in total. So I'm going to go through things

**[0:05:01]** pretty quickly here. Um, and so this is the kind of thing where it'd probably be beneficial to even like watch the replay of this later if you want to pick out certain lessons and really listen in on those again. Um, because I am going to go rather quickly. But yeah, the goal

**[0:05:14]** with this is like even if you're already familiar with half of these lessons and like you already understand that and you implement that for your own agents, hopefully at least like five or 10 of these are going to really resonate with you and be useful and like I've got a

**[0:05:26]** ton of really practical stuff to share with you guys here. So yeah, that's an overview of everything. And now diving into it, starting with the higher level lessons that I've learned. A lot of it is based around the biggest challenge that we have with agents. And that is

**[0:05:40]** the whole idea of hallucinations. And I pulled this uh this image off the internet. I just thought it was funny uh because it's an AI agent with a long nose like Pinocchio. Like every time he lies, his nose grows bigger. And I think this is really uh this really just hits

**[0:05:54]** spoton because when AI agents hallucinate as in they make a mistake or they just completely make up information, they act so confident when they tell you that information that's just completely wrong. Like they'll even cite sources from the internet that just don't exist and they'll just tell you

**[0:06:09]** with 100% certainty that like this is what it used um for its information. And so yeah, they they just seem to like lie very freely sometimes. Um and that's what a hallucination is. And I know that in general hallucinations, it's a very overused term. Um, and we hear this so

**[0:06:27]** much in the AI space, but I just think it's a good label for a lot of these mistakes that agents and just LLMs in general can make. And then they're also very confident as they present those mistakes to you. So that's the biggest challenge that we have. And so a lot of

**[0:06:40]** the highlevel tips and and lessons that I've learned that I want to share with you guys is working around these hallucinations. And so the biggest reason that we have to deal with this in the first place is because for the first time ever when developing software, we have the whole

**[0:06:57]** idea of non-determinism. And that's a a very fancy word um but I like using that a lot. Essentially what it means is before we had AI agents when we built a piece of software, we would take some input like this is someone's email or this is a request that we have to an API

**[0:07:15]** endpoint like whatever that input is and then we would always get the exact same output every single time we run that automation or whatever it is with that given input. And so it doesn't matter if we run that workflow 100 times. If we give the same input, we're always going

**[0:07:31]** to get the same output. That's what I mean by a deterministic workflow. And I've covered this in the course as well. And so with non-determinism now with an agent, when we receive a certain piece of input, we aren't guaranteed to always get the same output out because the

**[0:07:47]** agent is giving that ability to reason about what it wants to do. And it will make those decisions differently even when you give it the same exact prompt. And so the danger with this is that it could do fine the first 50 times you give it a certain prompt. like you ask

**[0:08:02]** it to uh research the web for something specific or whatever that prompt might be, but then the 51st time that you give that exact same request, it can completely botch it. It might search the wrong thing or not even invoke the tool that you want it to invoke even though

**[0:08:16]** the last 50 times it did it fine. And so that kind of brings me to the first big tip that I have here is that to avoid hallucinations really affecting you deeply, you want to use AI to save time, not replace you entirely. And so I have this uh quote here from uh Peter Parker,

**[0:08:36]** Spider-Man's uncle. He says, "With great power comes great responsibility." So these AI agents, they're dangerous because they reason about how they want to accomplish a goal. For the first time ever, we have software that doesn't always behave the same. Might work in one case and then break in another case

**[0:08:51]** with the same input. And that's dangerous, but also it's powerful. Having agents being able to reason about what they do in their environment unlocks a whole new level of automations and ways that we can um improve efficiencies in our business. There's so many different things we can do with

**[0:09:07]** agents. Uh but the the goal here is to share the responsibility with the AI so that you can catch hallucinations. And to make this like really really clear, I have a good example here. And I I did share this in the AI agent mastery course as well, but this is just my

**[0:09:22]** favorite example in general. I always say that like you wouldn't want to trust an AI agent to manage your inbox and automatically reply to every email. That is way too much responsibility that you're giving it. You want to share that responsibility. And so the way that you can do that is instead of having the

**[0:09:39]** agent always reply automatically to the emails, it can just automatically create email drafts. And so it's still saving you time because it gets you started on each reply um to your emails. But then if it hallucinates and it gives a really bad response, like maybe it tells the um

**[0:09:57]** person who emailed you that you can meet at a time that you're not actually available, well then you can correct it. And so any mistake, any hallucination that it makes is just going to cost you a little bit of time because you have to correct it a bit versus it would

**[0:10:09]** actually send that email and um in that case it's replacing you entirely and then that responsibility becomes very dangerous. So I hope that makes sense and I don't want to just say that like you never want to build out a process with AI that replaces something you're doing entirely. Um but the safest bets

**[0:10:24]** for implementations for AI um for yourself or your business, whatever that is, is usually the ones that are going to save you time. And then any kind of hallucinations aren't going to like negatively impact you greatly like sending a an email to someone that is just like a totally terrible thing you

**[0:10:39]** wouldn't want to actually say. So yeah, I hope that makes sense. That is the the first one there. And then the second lesson, again, just saying really high level at this point is you don't want to skimp on the planning and prototyping phase of building your agents. And so I

**[0:10:55]** covered this in my road map for building AI agents. That's what we're looking at right here for this screenshot. And I dedicate two entire modules in the course to this because it's just so important to have a good foundation for your agent. You don't want to dive into

**[0:11:09]** the implementation of your agent right away without knowing what you're really working towards and what kind of tools you want for your agent and things like that. It's worth spending that time up front because if you spend five hours planning your agent, that could end up saving you 20 hours of development down

**[0:11:23]** the line. So it might kind of sting at first like, "Oh, I'm spending so much time not actually making something yet." but it's going to make the whole process faster in the end. You just kind of have to have that foresight and and be patient with the first part of the

**[0:11:35]** process. And so that's why I cover it so much in in what I do um within the course and just this is how I build my agents in general. U because there have definitely been times when I first started building agents that I um I didn't do a lot of planning and

**[0:11:48]** prototyping and then I just had to scrap everything and start again. And that's when it gets to that point where it's like, oh, I actually ended up having to spend 20 more hours on this agent um because I didn't spend a few hours planning up front. So yeah, do not skimp

**[0:12:00]** on these phases. Uh then the the next one here is to beware what I like to call the hallucination explosion or another word for this is uh compounding non-determinism. And whoa, Cole, that those are really fancy phrases. All I mean by this though is that if you have

**[0:12:18]** many agents that are working together to solve one problem like a multi- aent workflow, you have to be careful about the inaccuracies of all these LLMs and they kind of build on top of each other. Like for example, if you have three agents that each individually work well

**[0:12:36]** 95% of the time, as in they only hallucinate 5% of the time, the fact that all three of them have to work correctly for a single execution to be, you know, quote unquote successful, that means that your whole system is only actually going to work 86% of the time.

**[0:12:51]** And um actually, let me pull up a calculator here because I I'll I'll do like a little live calculation to show you how I got this number. Because let's say agent number one, it works successfully 95% of the time. So 0 n5, but then it also relies on the second

**[0:13:06]** agent. Like maybe it's communicating to it through the A2A protocol like I covered on my channel previously. Let's say that this agent also only works successfully 95% of the time. Well, you have to actually multiply these two numbers together if you want to compute how likely your entire system is to be

**[0:13:24]** successful. But then let's say that it's using the MCP protocol to work with some external tools and maybe it only leverages this MCP server correctly also 95% of the time. Well then yet again you have to multiply 95% into this equation. And so rounding up that's what gives us

**[0:13:42]** that 86% that I have in the slide right here. So only 86% of the time is this solution actually going to work correctly because even if two of the components here are successful, you still might have one that fails and that could bring the entire system down. And

**[0:13:57]** so that's why you have to be very very careful with kind of what I like to call the hallucination explosion. It's an explosion because the more agents that you have in the mix, the more likely you are to have these errors kind of compound on each other or I guess I

**[0:14:09]** should say the chance of these errors compounding on each other. And so the biggest way to tackle this is to just have strategies in general to reduce hallucinations. And so this gets into uh the next few lessons that I have here from building AI agents which are all

**[0:14:25]** about how to reduce hallucinations in general. Nowadays when building my AI agents, I always rely on AI coding assistants to exponentially speed up my development. And that brings us to the sponsor of today's video, which is Windinsurf. And Windinsurf has a special place in my heart because it was my

**[0:14:42]** first ever AI coding assistant. Seriously, before Windsurf, I was working in VS Code, no extensions like Copilot. Windsurf has always stood out to me for a few different reasons. First of all, it's speed. Like you can watch here on the right hand side in our Cascade agent. Also, we have access to

**[0:14:58]** all of the best third-party models listed right here. And they've even built their own. It's crazy. And then also within their Cascade agent, there's just so many different features that we have. Cascade can handle complex coding tasks with longerterm agentic memory. We can run multiple conversations in parallel. And they've added a new native

**[0:15:17]** planning mode so that we can handle even longer, more complex tasks with ease. The important thing to know is that this is not just a Vive coding tool. This is an enterprise ready solution that's actually already being used by over 30% of Fortune 100 companies. And with the

**[0:15:33]** Cognition acquisition, the creators of Devon, Windsurf has gotten a makeover. It's a lot more reliable and snappy. They're continuing to add a ton of new features like Deep Wiki and Vibe and replace. And they're not slowing down anytime soon. Plus, I am seriously looking forward to the native Devon and

**[0:15:50]** Windsurf integration that's coming soon. I'll have a link to Windsurf in the description. They are definitely worth checking out. Yeah, one thing that Benedict said, I think you can reduce hallucinations a lot if you let another AI check the output. And I'm glad you mentioned that because literally that's

**[0:16:05]** what I'm covering now in this in this fourth lesson right here is the whole idea of AI agent guard rails. And so what guardrails are is just a piece of logic that you have that runs either before you call into your agent or your LLM or after. And so then if you detect

**[0:16:23]** something that is either going to likely cause hallucinations or you you do detect a hallucination in the output guardrail, then you can go down this failure path where you'd either let the user know that their process um or that their request wasn't able to be handled for whatever reason or maybe you'd loop

**[0:16:41]** loop back to the AI agent and have it try to correct itself. You can take proper course of action based on if one of these guard rails fails. And to give you a clear example of what these guardrails look like, let's say that you have an agent that is a travel planning

**[0:16:58]** agent. Um, and so you as a user, you give it the destination, your budget, how long you want to go on your vacation, and then the agent will help you plan an itinerary. It's a very common use case that I've seen before. A lot of people build this as an example

**[0:17:13]** when they show new AI agent frameworks. Um, and so as an input guard rail, one thing that you want to avoid for this travel planning assistant is you don't want to have it plan an itinerary um, when you are extremely under budget. Like if you want to go to Dubai for a

**[0:17:28]** week for only $500, you probably couldn't even buy the plane ticket for that much depending on where you live. And so that would definitely cause a lot of hallucinations if you were forcing the agent to try to uh, plan that trip when it's extremely under budget. And so

**[0:17:42]** a good input guardrail is you could have a smaller more lightweight LLM that just quickly evaluates the user's request for their trip and determines is the budget actually reasonable for the trip. And so then if they do say like I want to go to Dubai for $500, then it'll go down this

**[0:18:00]** failure path where you would tell the user like hey this is way under budget. You've got to adjust something here um for the travel planning assistant to actually be able to help you. So that would be a really good guardrail. But then if they want to go to Dubai for a

**[0:18:13]** weekend, maybe it's like $3,000 or whatever, like something within a reasonable range, then it could continue to the travel planning assistant. And then for an output guard rail, maybe you would have another agent that is verifying that the travel planning assistant actually planned an itinerary for the number of days that the user

**[0:18:31]** said they wanted to go on a vacation for. And so if they said that I want to go to Germany for 10 days and the itinerary was only for 8 days, well then this LLM would be able to detect that pretty easily. Like that's the thing with these guardrail agents is a lot of

**[0:18:45]** times they can be a lot more lightweight. Like you could use GPT 4.1 mini instead of GPT 4.1 because a lot of these decisions that it has to make around like is this input or output good? they're a lot simpler and so you could just detect really quick like does

**[0:19:01]** this itinerary actually make sense given what the user um said and then if it is then you return that file final itinerary otherwise maybe this output guardrail would loop back uh in a failure case and have the agent replan the itinerary. So guardrails are super super powerful in general it's just a

**[0:19:17]** huge way to reduce hallucinations and a lot of times they can be pretty simple to set up. Uh, and then the next strategy for reducing hallucinations is yet another thing that I've covered a lot before is the whole idea of specialized agents. And this one is really a lot simpler to explain um than

**[0:19:36]** guard rails. Because really, if you think about it, like the way that companies work with humans, with people, is that you always want to distribute responsibility between many people that specialize in different things. You're always going to get better results when you have specialization, when you have distributed responsibility among humans.

**[0:19:56]** And it's the same way, it works the same way with agents. And so if you have one agent that handles all of your tool calls for Slack and then another one that handles all of your tool calls for working with your database, you're distributing that responsibility. that's going to lead to a lot better

**[0:20:10]** results because if you overwhelm one agent, one LLM with way too much responsibility, it's going to start to fail frequently understanding how to leverage these different capabilities that you've given it to solve the goal that you have for it. And so, I've covered this a lot before with like

**[0:20:28]** having specialized agents that each use an MCP server, things like that, but in general, this just helps a lot. And the one thing you do have to be a little careful of here is this does kind of start to point us back to the hallucination explosion I was just

**[0:20:42]** talking about because now you do have an orchestrator agent that has to make the right call like which specialized agent do I point to. But typically this decision can be quite simple. So you don't have to worry too much about that compounding non-determinism that I was talking about because there at least

**[0:20:58]** I've seen from the agents that I've built that this primary orchestrator that has to figure out which specialized agent to use, it very rarely picks the wrong one, especially if the roles for each of these agents are very distinct. And I'm very clear in the system prompt to my primary agent exactly when it

**[0:21:15]** needs to call into each of these specialized agents. And so this helps reduce hallucinations quite a bit. And then the very last strategy that I have here for reducing hallucinations and yeah these are these are all taken up in the lessons as well. So this is lesson number six um is examples examples and

**[0:21:33]** examples. And I'll talk about this more when I get to one of my lessons for system prompting specifically. But it is just so helpful to an LLM or AI agents in general to give examples in the system prompt. And we see this with all of the the best AI agents and the most

**[0:21:50]** popular AI coding assistants like Vzero and Cursor and Bolt. New like they all have very concrete examples in their system prompts. And so like this screenshot that I took right here, this is an example of um it's an example of an example in the system prompt for Bolt. The front-end application

**[0:22:11]** developer that you can use in your browser. Um, and so yeah, like it even says right here like example colon and then they just paste in an example of exactly what they'd want the bolt new agent to output in a specific case. And they don't hold back from including any

**[0:22:28]** context. Like they have all the nitty-gritty details of the pluses and the minuses and the at symbols and all the different line numbers for diffs. Like they've got everything covered in this example here. just showing the agent exactly what to output given some input that they describe kind of above

**[0:22:43]** here in the system prompt that's cut off right now. But yeah, examples are just so so powerful and you can use examples to tell an agent how to use tools um exactly the format that you want it to output. Pretty much any kind of direction that you want to give to the

**[0:22:57]** agent. Examples oftentimes help with that and sometimes they can be overkill like they'll make your system prompt longer. Um, but in general they're really useful especially for anything that's a bit more complex with your agent. And so yeah, hope that one makes sense there. Um, yeah. And then the the

**[0:23:14]** next thing that um I want to cover now is diving specifically into lessons for one of the components that we have for an AI agent and that is the agent program. And so again, this is the system prompt for your agent. Um, the instructions that you give it to

**[0:23:29]** determine its behavior and um the tone that you want it to have. And so the first lesson that I've got for your system prompt for your agent is that you want to avoid adding what I like to call negatives. And this is especially true for longer system prompts. And so as a

**[0:23:48]** bad example of prompting, you might say something like, "Explain quantum physics to me and do not use complex language." That's a negative right here. Like you're telling it not to do something. And then a good example of a prompt is explain quantum physics to me and use fifth grade level English. And so in

**[0:24:05]** this case in selling in instead of telling it not to do something, you are telling it to do something. And the reason that you want to do this is when you get very long system prompts. I've seen this time and time again. I don't really know why, but LLMs, they love to

**[0:24:20]** drop the negative, as in they will kind of like take out the do not and then they'll do the very thing that you told them not to do. like they'll use complex language and obviously in this example here it's a very very basic prompt and and this really only applies to longer

**[0:24:36]** system prompts like of course it would listen in this case but once you have system prompts that are like five six 10 paragraphs it will start to do this thing where it'll drop the negative and so you'll see something like this a lot where like when you want it to you know

**[0:24:50]** give a very simple explanation for something you'll tell it to like use a specific type of language like high school language or fifth grade level language. I'm sure you guys have seen that a lot. Um, yeah, Benedict said, "This behavior also refers to humans. Humans also don't hear the negatives."

**[0:25:06]** Yeah, it's true. And and yeah, I mean, kind of like what I was talking about with specialized agents, too. Like a lot of the ways that we think about how humans behave and how to make humans uh do things well. I mean, that applies to AI agents as well. Um, so yeah, that's a

**[0:25:20]** good point. Um, and then the next thing for system prompts, and this is probably the most obvious lesson out of all the 20 that I have for you guys here, um, but this is this happens very frequently still, is you want to avoid contradictions in your system prompts.

**[0:25:36]** And so, like in this example that I have, this is just a fake system prompt that I had Claude help me generate just for an example for you guys. We tell it that it's a knowledge assistant at the top here. And we're telling it to give very concise and efficient answers.

**[0:25:51]** But then in the very next paragraph, we tell it to make sure that we give a comprehensive coverage of the topic and we include historical context and theoretical frameworks, practical applications, blah blah blah blah. We're telling it to be like very comprehensive in its response in the very next

**[0:26:07]** paragraph. And this is a contradiction. The LLM is going to take these two pieces of instruction, try to balance what it wants to do, and it's going to usually just kind of randomly pick between one of these, like either be very concise or be super comprehensive, and you're going to get very

**[0:26:24]** inconsistent results and a lot of hallucinations. And I've seen this so much. And obviously when you're creating your system prompts, you you probably don't want to or you're probably not going to end up making a very obvious contradiction like within two adjacent paragraphs. Like that probably won't happen. But when you have longer system

**[0:26:44]** prompts and you're telling it at the start to do something, then maybe six paragraphs later, you're describing how you want to take a specific action and that's going to contradict with kind of like the role you gave it at the start of the assistant prompt. We see this

**[0:26:56]** kind of thing a lot. And so like one example uh of what I did, there was an agent that I built one time that was kind of like a customer support agent and its goal was to get the person communicating with it booked um for an event on the calendar. And what I said

**[0:27:12]** at the start of the system prompt is I told it to be very flexible and accommodating for when that user is available for getting that that meeting uh booked. But then later on in the system prompt when I was giving it instructions on how to use the calendar

**[0:27:28]** tools that I had for it, I told it to be rigid. As in you look at the calendar to see the times that are available for a meeting and you only ever offer those times. You never offer times that are outside of the range that you got available times for. And so there was a

**[0:27:45]** contradiction there. I told it to be very rigid when I was describing how to use the tools, but then at the start of the system prompt, I told it to be very accommodating to the user. And so I ended up finding that a lot of times it would offer times to the user that

**[0:27:57]** weren't actually available. The calendar API did not return to it. And it was just because I told it at the start of the system prompt to be accommodating to the user. So as soon as I took that out or at least I clarified you want to be accommodating um for um maybe just like

**[0:28:13]** I don't know like the like you want to have a nice tone versus like actually be accommodating for the calendar. Then I stopped getting those hallucinations. it started to only ever give times to the user that it got from the calendar API. So very important to keep those kind of

**[0:28:28]** things in mind. So when you start to get like really mixed results where sometimes an agent does things properly and sometimes it doesn't, it's usually because of some kind of underlying contradiction that you missed in your system prompt and it happens more than you would think. Um and then the the last system prompt

**[0:28:44]** tip that I have for you guys. I'm just checking the time here to make sure that I'm doing good. Looks pretty good. Yeah. So the next system prompt tip that I have for you guys is to version your prompts. And so just like you want to version your code so that you can revert

**[0:28:58]** back to a different version of your code if something more recently breaks, you want to be able to do the same thing with your system prompts. Because as you are evolving your system prompts over time, even if you think that you have provided more context and of course it

**[0:29:13]** would make the AI agent perform better, you still will run into situations where maybe your system prompt gets too long and it overwhelms the LLM. Maybe you added in one of those contradictions and you didn't realize it. you'll hit that kind of snag where you want to quickly

**[0:29:26]** revert to a previous version of your prompt that maybe wasn't quite working to your liking and that's why you tried another version but at least it was better and so you can revert back to that and then work through your other version back in your development environment and see if there's some

**[0:29:40]** contradiction you accidentally added or if you have to give better examples like whatever that is to improve that third version then you can go back to it. So versioning is very important just like it is for your code. So, uh, yeah, and Jiren asked, "What tools are you using to manage your

**[0:29:55]** prompts?" Langfuse is a really good one for sure. Um, and then also just like having a separate place in your GitHub repository for your prompts and just versioning it along with your code. That definitely works as well. Um, but tools like Langfuse are also fantastic. Um, so yeah, that's everything for the

**[0:30:10]** system prompt. Now, we move on to large language models and the general lessons that I learned from working with LLMs within AI agents. Um, the first tip that I got for this is that swapping large language models can actually be pretty dangerous even if you are swapping to an LLM that is supposed

**[0:30:30]** to be better in just every way. Um, like just as an example, a couple of years ago or I guess whenever GPT40 was released, I had an agent that was running with GPT4 Turbo. That's kind of like the last LLM that OpenAI had released before they released GPT40.

**[0:30:50]** And they they gave the benchmarks when they released 40 and they're like, "Yep, this is just better than GPT4 Turbo in every way. Uh, we recommend that you guys upgrade to this model." And so I did that. I took my agent and I just flipped the switch and I changed the LLM

**[0:31:03]** from from 4 Turbo to 40. and things were better in some ways, but then it started having these like super weird hallucinations because different LLMs, even if it's like supposed to be just a straightup better LLM, they understand system prompts in different ways and they take actions in different ways. And so, you

**[0:31:21]** have to be very careful for that. You can't just swap your LLM, push your agent to production with that change, and then just call it good. Like, you have to do a lot of testing under the hood to make sure that your system prompt still holds for that new LM that

**[0:31:33]** you're using. Because like I said, even if the LLM is better, that doesn't actually mean that your agent is going to perform better. You might have to tweak your system prompt. You might have to um even change your tools that you have for your agent. I mean, hopefully

**[0:31:45]** you wouldn't have to do that. Usually, it's just changing the system prompt. That still has to happen a lot. And we've seen that before with other things like bolt.diy as well. Um, and like I think Bolt. New had this even happen as well where like they were originally

**[0:31:59]** running with cloud 3.5 sonnet and then when they changed to cloud 3.7 sonnet, they had to tweak their system prompt a ton. Um, like actually more than you would think. And so, yeah, it's really good to just keep that in mind in general. And then also, your favorite

**[0:32:13]** LLM isn't always the best. And I see this happen a lot. I've been prone to this myself even where I get super attached to a specific LLM and I don't really consider using other ones even though I know deep down that there are different LLMs that are better at

**[0:32:29]** different things. Like sometimes you might get really attached to Claude 3.7 Sonnet. Like that's just your favorite LLM and you try to use it all of the time. And I find Claude 3.7 Sonnet um to generally be the best LLM for coding um overall. I mean there's a lot of debate

**[0:32:45]** for that but then Gemini 2.5 Pro I find works better for more of my creative agents like they need kind of like writing assistant or something like that and so just knowing those differences of when different LLMs work better and not just being super stubborn and always sticking with one like that is super

**[0:33:01]** important. Like maybe you love using the Quen models like the new Quen 3 that was just released. Um, but you might find with a little bit of testing and if you allow yourself to explore that once in a while with a little bit of testing that mistrol actually works better for one or

**[0:33:14]** two your agents for example and so then you can switch to that for your local AI implementation. So yeah, it's just important to be open-minded especially as more and more LM are released being willing to like test those and not just like look at the benchmarks and try to

**[0:33:26]** make a snap decision based off that. And it's easy to swap LLMs and test things really quickly so it's worth doing so. And then the last lesson that I have from LLM specifically is that you want to watch your context links. And this applies mostly to local LLMs. Um because

**[0:33:45]** especially like a lot of the big guys now like Gemini 2.5 Pro or Llama 4, Claude, like they all have such long context lengths that you usually don't hit that limit anymore. But there still are a lot of LLMs where you do. um like a lot of OpenAI's models are 128,000

**[0:34:03]** tokens for their contacts length. Like you can definitely hit that if you um are retrieving a bunch of chunks from rag or pasting in big documents. And then local LLMs oftentimes have a lot smaller contacts limits like 32,000 tokens. And you'll often hit those because the biggest thing is that the

**[0:34:18]** conversation history is a part of the prompt to the LLM. And so as you're sending in more messages and having a longer conversation, you can hit this limit. And the problem is once you hit that limit, you start to lose part of the conversation. It's it's included in

**[0:34:31]** this like forgotten context at the end here because the limit only spans this part of the conversation. And the very important thing to keep in mind with this is that the system prompt like your general instructions to the agent that we've already covered, that's generally included at the very top of a

**[0:34:50]** conversation because it's the highlevel instructions. And so when you hit that context length, you'll see that the system prompt is the first thing to go. You start to lose those instructions for the agent. And so you'll see this a lot with local LMS especially when the agent starts to seem to just completely forget

**[0:35:07]** your instructions and not understand how to use the tools anymore. That's generally because you hit the context length and now you're starting to lose your system prompt. So it doesn't even know it has access to the web search tool anymore. So if it's not calling in a brave anymore and you have no idea why

**[0:35:21]** you're in a longer conversation, it's definitely because of a context limit issue. So certainly good to keep that in mind. Um and so yeah, that brings us into the memory systems here, long-term and short-term memory. So I've got a few lessons for this as well. The first one

**[0:35:38]** for short-term memory is that previous hallucinations are likely to be repeated by the agent. And I've got another really simple example here that I just had Claude generate for me. And usually it's not going to be this small of a conversation for this issue to crop up, but it just demonstrates it well. So

**[0:35:58]** like in this case, the user is asking uh when was to kill Kill a Mockingbird published and then the AI said it was published in 1962. And then you as the user, you'll correct it and you'll say no actually it was published in 1960. And then you guys have all probably seen

**[0:36:14]** this before when you corre correct the LLM. It'll say something like, "You're absolutely right. I apologize for the error. Yes, it was indeed published in 1960." And so then now you would think that it would have that correct information. But then if you continue the conversation a while and you come back and say

**[0:36:31]** something like, "Tell me about Harper Lee and her famous novel." It might repeat that hallucination that it was published in 1962. And you'll see this a lot where even though you corrected its mistake, it'll still repeat it in the same conversation. And that's one of the reasons why it's really dangerous to

**[0:36:48]** have long conversations, especially in things like your AI coding assistance because if it understood something incorrectly in your codebase or in the conversation previously, it might make that same mistake again. I've seen this before where like there was an error invoking a tool like the web search tool

**[0:37:06]** and then later on the conversation you ask it to do the web search again and it'll say that it can't like it won't even try because it just knows from the previous point of the conversation that that didn't work even if you told it later that oh yeah you just did this

**[0:37:19]** thing wrong that's why it didn't work. So yeah, that's one big reason why you want to start new conversations quite often with your agents and AI coding assistants. And the next thing here, I've got the uh prototype pulled up for the N8N agent that we build in the AI agent mastery

**[0:37:36]** course because the biggest thing that helped me understand long-term memory better, and like maybe this is obvious for a lot of you guys, but this really hit home for me, is that long-term memory for your agents is just another rag. Like that's literally all it is. So within our prototype here we have the

**[0:37:52]** tool for our agent to retrieve memories and then we have the tool for it to retrieve documents. Both of these just using rag like you can see that the tool is exactly the same. And then the way that we insert memories into supabbase is using the exact same node in n as how

**[0:38:09]** we insert our documents into superbase within our rag pipeline. And the reason this is so important is because a lot of these strategies that we learn for better rag retrieval like query expansion or re-ranking like all of these nitty-gritty strategies which I'm going to be covering in the live

**[0:38:28]** workshop this Friday by the way. So go to the events tab and check that out if you're interested. I'm going to be diving into rag strategies. But a lot of those rag strategies apply to working with long-term memory as well because it just is essentially another table in

**[0:38:41]** your vector database just with memories generated by the agent instead of documents that you're pulling from your data source like Google Drive, your local files, SharePoint, whatever that might be. And obviously not all of the strategies will apply to memories and like you have to treat them differently

**[0:38:58]** than your documents. Um, but in general, a lot of those ways to make rag more accurate are going to apply to memories as well. So, really good to know that. Um, and then the last memory lesson that I have here is that you want to include tool calls

**[0:39:14]** in your conversation history. And I I got this nice diagram actually from a lang chain documentation page that shows what I mean by this. So typically what I've I've seen people do this a lot and actually it's really unfortunate. The NAND agents do this as well where they

**[0:39:30]** don't include in the conversation history anything related to tools and so you store the human message then the agent response and then you just flip back and forth between these and that makes up your entire conversation. But really what we want to do is we want to include everything related to the

**[0:39:48]** tools as well. So whenever the agent makes a request to use a tool like send an email or read a Slack message, we want to include that request and then the response that we get back from calling this tool like here is the message or here's the action and the

**[0:40:04]** success from that like we want to store that in the conversation history. And the reason for that is because a lot of times the agent can re-reference things that were returned by the tool calls in a subsequent request that we have for it in the conversation. As a good example

**[0:40:19]** of this, uh we have rag. Like when you you perform a search in your vector database and you retrieve relevant chunks, the agent is going to use that to then answer the user's message. But then the user might have a follow-up message that could also be answered from

**[0:40:35]** the chunks that it retrieved from that first rag lookup. And so if we have the tool responses as a part of the conversation history, the agent can re-reference that to answer the second user question without having to do another lookup. So it's just faster and it just makes the agent more likely to

**[0:40:52]** give a correct response because it's referencing things that it already retrieved successfully. And so we don't have that at all if we just don't in if we don't store the tool calls and responses in the conversation. Very very very important. And then the very last one that I want

**[0:41:08]** to cover here is and I'm going to give maybe like seven minutes to try to get through this pretty quickly here because I want to do some time with uh for Q&A with you guys. I want to focus on the tools briefly here and really I want to

**[0:41:20]** just dive into the anatomy of a good tool. How you can set up a tool all the different components and I want this to apply no matter the tool or framework that you're using. So if you're using N8N or Pantic AI, Crew AI, Lang Chain, whatever it is, like everything that I'm

**[0:41:34]** talking about for tools here are going to apply. And so the first thing is the descriptions that you give to your tools are key because everything that you give as a part of the tool description is indeed included in the prompt to the LLM to tell it when and how to use a tool.

**[0:41:51]** And so it's worth being pretty descriptive here. And so telling the agent like what's the purpose of this tool? How do you call it? What are the arguments that are here? Like for this rag tool, we have to pass in some kind of query so that we can search the

**[0:42:06]** vector database with that query. And my general rule of thumb when working with tools in general is that the tool description like what we're looking at right here, that is your place to tell the agent how to use the tool, this individual tool. And then the system prompt is where you can tell the agent

**[0:42:24]** how to use different tools together. And so that is where you kind of zoom out at a higher level. How do you incorporate these tools together to accomplish a single goal? And then the tool description is where you hone in on all of the nitty-gritty details for an

**[0:42:38]** individual tool. And both are very important because a lot of times you don't want to just use one tool per execution. Like you want your agents to reason about how they can use different tools together. And so that's why you want to include that in the system prompt as well.

**[0:42:52]** And then the next one is for more complex tools especially just like we do in our system prompts we want to give examples specifically examples for what the parameters might look like. So like for this rag this retrieval tool for the user query we're giving it some examples

**[0:43:08]** of how we want to format the queries that we would use to search the vector database. And so, like I said, for very simple tools or especially ones that don't have any parameters at all, like if we just want to fetch the channels that are available to us in Slack, for example,

**[0:43:24]** we might not need examples, but oftentimes they can be very helpful, especially when our parameters might be a little bit more complex or we're very particular about how we wanted to format things like our queries. And then also for pretty much all of your tools, you want to catch the errors

**[0:43:41]** and then return the problem to the agent. And so you'll see this in my template that I have for module 4 of the pyantic a the pantic AI agent for um the AI agent mastery course. Every single tool that I create for the agent, I always wrap the entire thing in a try

**[0:43:57]** block and then I have an accept here. And you can do something similar in in N8N with um the like error workflows and for any other framework like this. I'm showing a tool from my Pantic AI agent, but you can set up something pretty much the exact same in any framework as well

**[0:44:13]** like Crew AI or Eggno or whatever that is. You just catch any exception here. And the reason you want to do this is there's twofold. The first is that if an agent uses a tool incorrectly, you don't want your application to crash. Sometimes a tool is going to fail just

**[0:44:28]** because the agent hallucinated a bad parameter. It's not because your code is actually bad. And so you don't want to just like, you know, crash the entire application. The other thing is that when you tell the agent exactly what went wrong, and I don't really do that here. This isn't a best example cuz I

**[0:44:44]** just returned an empty list. But if you were to maybe return an empty list and some error message as well, you can tell the agent what went wrong with the tool call so that it has a chance to maybe invoke the tool a second time fixing up the parameters or whatever might have

**[0:44:58]** caused that error. And so that kind of just gives it another level of reasoning like not only what tools should I call on how, but also how should I reinvoke them if there are any issues that come up. It's very powerful. And then the next thing is for your

**[0:45:13]** tools. You want to be very careful to only return what the LLM needs to know. And this actually came up in in our community yesterday. Someone was talking about using the um Shopify API. Mark was talking about using the Shopify API in one of his agents. And for the tool

**[0:45:30]** calls that invoke the Shopify API, the results that you get back, like this is what we're doing at Superbase. We're fetching a bunch of records from Superbase and we're storing that in result here. But often times when we're using APIs from different services like Superbase or Shopify, what we have in

**[0:45:47]** results is going to include a lot of metadata like maybe the time for this query or other pieces of information that we need related to the query that isn't like just the data that we care about. And there's going to be a lot more included usually. And so you want

**[0:46:02]** to make sure that what you return is just the information that you care about giving back to the LLM. Like in this case, we only care about sending back the actual data. That's why I'm doing results data and not just result. I could be lazy and just send in the

**[0:46:15]** entire result to the LLM. But if that includes this massive JSON body from the API with a ton of extra information, I risk overwhelming the LLM and just making it so it doesn't correctly pick out of that JSON the information that it actually cares about having. And so

**[0:46:31]** that's why you want to format things. And you'll see that as well with all the different tools that I set up um within the AI agent mastery course. And then the very very last thing that I want to cover with you guys, the last lesson, the 20th one that I've got for you is in

**[0:46:46]** general what the anatomy of a good tool looks like. And um this is kind of hard to see. So I'm going to see if I can actually pull this up um within Windsurf here because I have I have this example live instead of just in a slide here.

**[0:47:00]** So, let me zoom in on this um because I want to just show you really quickly the anatomy of a good tool. And so, a lot of this is just covering what I've already showed um for the different tips that I have, the different lessons for tools, but I just want to quickly like tell you

**[0:47:13]** how this all applies in a single tool here. So, this is my full tool for rag. You give some kind of user query. It'll search the vector database and it'll return the relevant chunks for the agent to uh use that to aid in answering the user's question. And so the first thing

**[0:47:28]** is we've got the examples in the prompt and I have a very detailed prompt here including different arguments that we have for this tool. And then we have the whole thing wrapped in a try catch block. So I've got the try and then the accept at the end. When we get an error

**[0:47:43]** retrieving the documents from rag, I also tell the agent exactly what that error is. So the response includes the error message itself so it can reason about how to fix that problem when it would maybe invoke this tool a second time. And then the other thing that I

**[0:47:58]** wanted to show you here uh for the anatomy of a good tool is what I talked about just a little bit ago where you want to only return the information that is relevant to the agent. So in this case when we get this result from superbase and we're calling that match

**[0:48:10]** document function for rag. We are getting all the documents and then we're just going to loop over them and create this string for each document that includes the ID, the title, the URL, all that important metadata and then the content of that chunk as well. We don't need anything else. And trust me, there

**[0:48:27]** is a lot more that we get back from this result object. And so that's how we make sure that we're only giving what we actually care about the LLM receiving. And then we're just returning that as a nicely formatted string. Because just like humans benefit from having things

**[0:48:41]** well formatted for them, agents also benefit in the same way. And that's often why oftentimes why you hear markdown as being the best format for agents is because markdown just formats things very nicely. Like let me open up a readme here so I can show you like this readme file. Like this is using

**[0:48:59]** markdown where we have sections and numbers and subheadings and um code blocks and things like that. Like all of that just makes it so that the agent has a better idea of how things are structured. And so that's why also in my tools I'll spend the time I'll I'll

**[0:49:14]** actually code out creating a well formatted string to give back to the agent. Um but yeah, what I'm going to do now is I'm going to enable Q&A. And so I'll try to go through some questions in the regular chat as well. Um, but yeah, I I hope that those lessons made sense

**[0:49:30]** to you guys. I hope that even if you're like an expert at building agents, at least a few of those like, "Oh yeah, I didn't really think about it that way." I just hope that that can help you um build more effective agents. And so, yeah, I just want to spend some time

**[0:49:41]** with some questions for you guys for 10 or 15 minutes here before we wrap it up. Um, but yeah, let me go through the chat and see if I can find anything. And then also you guys can feel free to start posting in the uh Q&A channel as well.

**[0:49:53]** Yeah, first congratulations on a booming community. Thank you very much. I appreciate it. Uh and your question, my tools are not forming properly. There's no syntax error but still can't get my agent to start using tools. What might be the problem? Yeah. So I mean this depends a lot on what exactly you're

**[0:50:08]** building with like if it's N8N or Pantic AI. So I'd be curious on that. Um because it yeah kind of sounds like the thing that I have to dive into a little bit more to really be able to to say um because there are a lot of things that

**[0:50:20]** could be wrong there. Um syntax there's no syntax error but I can't get my agent to start using the tools because it seems like there might just be like a connection error there between the agent and the tool. Um so I guess my first question is like will the agent ever use

**[0:50:34]** the tool or are you hitting a snag there where it doesn't even seem to recognize that the tool is there? So I'd start with that. hard to give like something super concrete um at that point. Um yeah, let's see. Fred, are there ways to lock in the system prompt so it does not

**[0:50:48]** scroll off as the context gets long? Perhaps encapsulating the system prompt information as memory. So, you kind of can. I mean, you could take the instructions from the system prompt and just like prepend the the latest user message with that. Like here are some instructions. Now, here is the

**[0:51:05]** user message. Like, you can send that in as the latest prompt to the LLM. So you could definitely do that or you could kind of like you're saying have your general goals and preferences and and instructions as a part of the uh long-term memory. So it could retrieve

**[0:51:19]** that and have that as a part of the latest user message as well. So, you definitely can. Um, generally what I would say though is like if you're getting if you're hitting a problem where the system prompt is starting to get cut off, you're going to want to

**[0:51:32]** resolve that anyway because if it gets through the system prompt and it loses the entire system prompt, then you're going to start losing parts of the conversation as well. So, it's still going to be a problem. Like, you don't really want to work around this issue and and like leave the issue as it is.

**[0:51:44]** definitely want to address that and either use a different LLM that can handle longer context or figure out how you can make sure you don't hit that context limit like maybe for rag agents you'll just return less chunks like whatever that might be I would definitely address that as a priority

**[0:51:59]** instead of trying to work around it u but good question though yeah and then Ryan asked do you have a specific method to optimize system prompts especially when switching between LLMs um and so yeah I don't want to get into this a ton right now but this is where LLM eval EV

**[0:52:13]** valuations really come in handy. Um, specifically LLM as a judge is a very powerful setup where you use another large language model to um, usually evaluate the responses from your agent. It can also generate the the requests to the agent as well and be used to automatically tune the system prompt. So

**[0:52:35]** it can create you would kind of like give it your system prompt, have it generate questions or requests to your agent, evaluate the output, and then automatically tweak the system prompt based on that. Um, and usually I find that like manually adjusting the system prompt is more powerful, but you can go

**[0:52:51]** down that route if you want. But yeah, usually it's either going to be like having some sort of automated evaluation and adjusting the prompt yourself based on those results or just having an LLM as a judge kind of like on either end automatically tweaking the system prompt. Yeah, good question.

**[0:53:07]** Um, next up, oh, I gotta scroll down. Whenever I click into the replies for a Q&A and I go back out, I have to scroll back down, which is kind of unfortunate. Um, yeah, I have a workflow where there is a WhatsApp chatbot using Puppeteer. Uh, didn't provide an API key.

**[0:53:27]** I use an API key that processes the payment system. I only use the AI agent in the conversation part of the chatbot. the rest I set with a classifier direct different actions such as creating a balance, depositing, withdrawing. You think my approach is good? Um, yeah. I mean, that sounds good to me. Um, in in

**[0:53:45]** order for me to like really like give you a solid like yes or no, I'd probably have to see it a bit more because this seems like quite an involved workflow. Um, but I guess I'm curious like what exactly your thought is with the classifier there. Um, I mean it sounds

**[0:54:00]** good, but I yeah, I definitely have to take a bit more of a closer look at that. I mean, and and honestly, like you could you could build out both approaches because the tools will kind of be the same. Like those actions that you take either directed by the agent or

**[0:54:14]** just buy like a separate classifier like a um m like an ML setup there. Like you could definitely just test both um reuse those actions and see what works better. Um but yeah, I mean that looks that's looks like a really cool use case by the way. Like that's awesome.

**[0:54:30]** Um, Eric asked, "Thank you for these lessons. Gold." I appreciate very much, Eric. Uh, where in the community can I refer back to it? Yeah, good, good question. So, all of the events that I have in Dynamus, these work or these events and then like workshops that I

**[0:54:44]** do, anything is going to be automatically recorded and then the recording will be uploaded within like around 30 minutes of the event being complete. And the way that you can go back to that, um, actually, let me share my screen quick. So here in the homepage of Dynamus, you can go to the events

**[0:55:00]** calendar. You can click on any past event like I can go to the community introduction from yesterday and then click into it. Go to the page for this past event and then the recording will be right here for you to view. Um and so that'll be uploaded within 30 minutes of

**[0:55:14]** the event being complete. So very very easy to go back through those events. You can also go to the live events tab and then instead of um just viewing the upcoming events, you can view past events and then you can also get into that event view um this way just like we

**[0:55:27]** did through the calendar. So super easy to view those um those past events and get the recordings for those. But yeah, good question. All right, let's see. We got a few more questions here and then I will wrap it up. So it looks like we got four more. So I'll try

**[0:55:44]** to get through these four more that we have in the Q&A. Uh, and then I think I will call it there. Um, yeah, thank you, Max, by the way. Appreciate it. You are very welcome. Thank you, Andrea. Appreciate it, guys. I'm just taking a look at the uh regular chat quick here

**[0:55:58]** and then yeah, let me go back to the Q&A. All right, scroll down. Patrick asked, "With image recognition, is there a way to use examples?" Examples here are the attributes from this image and use this as an example when classifying other images. So typically for like an image recognition like if

**[0:56:18]** you're talking about like a machine learning algorithm or like a model that you're custom model that you're building up like a CNN or something the examples would be more like your input when you're training the model. Um so I I guess I'm not quite understanding your question unless you're talking about

**[0:56:32]** like using an LLM specifically with image analysis like not building your own image recognition model. Um, I'm not sure if you mean that example here are the attributes from this image and use this as an example when classifying other images. Um, because if you mean just like using LLM with vision

**[0:56:50]** capabilities, you could definitely like include an image as a part of your prompt like you kind of do like like um twoot prompting where where you'd be like here's an image and then here's how I want you to classify it. Now here's another image. How would you classify

**[0:57:05]** this? like you could definitely do that just as it wouldn't be a part of your system prompt. It would just be like a part of your user prompt doing something like a twoot prompting. Um yeah, but good question though. Brian asks, "Have you found that there is a

**[0:57:18]** limit to how many agents you can have under an orchestrator? Will it eventually get confused?" Yeah, so there there certainly is a limit. Um because just like you can overwhelm an LLM with too many regular tools since each sub aent is essentially another tool, you can definitely run into that issue where

**[0:57:35]** um there you might have like 20 different sub aents and that can start to overwhelm the LLM. As far as how many it takes to overwhelm because it's usually pretty simple like here is your Slack agent, here's your data analytics agent, here's your database agent. like it's usually pretty easy for the

**[0:57:52]** orchestrator to know when to call into each of them. You can go pretty far. Like you can have a good number of sub aents under the orchestrator. Um like I've seen as many as like 15 to 20 and like it still works really well because usually that handoff is just really

**[0:58:05]** really simple. Um but like if you really want to get fancy, you can start to have like an orchestrator that has sub orchestrators. Um I don't find that to be necessary like ever. Um, but you definitely could do that if you just want to like kind of create this

**[0:58:18]** hierarchy of agents to like really make sure that you never have more than 10 tools for any given agent or whatever that might be. Um, but yeah, usually I don't find this to be an issue because if you have an agent that you actually want to orchestrate like 50 different

**[0:58:32]** sub aents, you've probably got more of a problem there where you're just trying to do too much with one application and you might want to split that into different things in the first place as like entirely separate applications. Yeah, good question. All right, next one. Is there a video in

**[0:58:50]** the community for vibe coding full stack app in Pantic AI? Any vibe coding for a serverless app? Yeah, so as one of the videos in module four in the AI agent mastery course, I talk about using AI coding assistance to help us build agents with Pyantic AI. And I and I will

**[0:59:06]** say that I I don't generally condone vibe coding overall. like I don't want to uh I don't want you to trust the LLM entirely when coding things. I want you to be able to validate its output. Um but certainly using AI coding assistance is a big thing that I focus on for at

**[0:59:20]** least kind of getting that first 90% of the code created and then then you just perfecting it and fixing any errors that come up yourself. And then as far as vibe coding um a full stack app, that is something I'll cover more in module five of the AI agent mastery course when I

**[0:59:35]** build a full application around the agent that we built in the previous modules. And then for serverless, um I will be covering serverless for deploying agents in module six. And so all that is coming soon. I want to get these modules out for you guys as soon as possible.

**[0:59:52]** Um is there a support for calendarly one-on-one session with colon team for query features or client requests? Yeah, good question. So, I'll be having um generally three office hour sessions a week, which aren't going to be one-on-one sessions um because obviously there's just like so many different questions that all you guys have,

**[1:00:09]** fantastic questions, but I got to be able to address um you know, a lot of people at the same time. And so, I I won't be offering one-on-one sessions, but the office hours are going to be your place to come in with specific questions on your projects or like when

**[1:00:20]** you want to just get into the nitty-gritty details of things like that's what I'm going to be offering. And I'm specifically offering many of those every single week just to make sure that there's so much time available for that that it's not going to be like 50 people coming into each office hour.

**[1:00:33]** It's going to be a very small group of people and we can all learn together at the same time as we're going through these questions as well. They can all be recorded sessions. Um yeah, then the last question that we have here and then I'll close it off for

**[1:00:45]** all of us. Got one from Tom. Um let's see. Let me got to scroll back down. All right. So Tom asked, "What are your thoughts about process the process of fine-tuning embedding models? I feel like this is an important building block for accurate responses from rag. Maybe you could visit this one of your

**[1:01:00]** videos." Yeah, absolutely. Great question. Fine-tuning embedding models is super super powerful and definitely something that I've been wanting to cover on my channel for a while. The biggest problem is it's a bit more involved than a lot of the things I like typically cover on my channel. So, it's

**[1:01:16]** just a it's a hard video to create and it's it's not going to be as easy for people to like resonate with that really quick like, oh yeah, I'm going to like go use this in N right now because it's not that simple. Um, but it is super

**[1:01:26]** super important and specifically I am going to be creating a course on knowledgebased agents like a rag specific course for Dynamis um sometime after the AI agent mastery course and fine-tuning embedding models is going to have a dedicated portion of that course for sure because it's super important.

**[1:01:43]** Um, so yeah, really good question. And yeah, something I definitely want to focus on. Oh, and then yeah, really quick one from David. If we've made changes to your repo, how can we submit them? You can make a poll request in any repo in the Dynamus organization if you want. And

**[1:01:59]** so, yeah, right now the AI agent mastery repo is the only one that we have. Um, so yeah, definitely feel free to make a PR if you fix something up or just have a new feature. I'll take a look and I'll be pretty picky about the things that I

**[1:02:09]** add into the repo. But yeah, I mean, if there's like an issue that's like seriously needs to be addressed or something that I can add into the package without having to redo a bunch of videos or anything, then yeah, I'm all yours for that. Um, so yeah, good

**[1:02:21]** questions. And um, let me remove that there. I'm going to go back to the chat. Uh, Jiren said, "Man, such good content. I appreciate it very much." Uh, yeah, Pan said, "Vive coding is 90% code in the future, so I believe having personalized coding agents should be a

**[1:02:36]** great add-on." Yeah, definitely. Definitely. Um, Aiden said, "Appreciate the help and knowledge you give." Yeah, thank you very much. I'm glad I'm glad that this has been helpful for you guys. Um, and yeah, with that, I'm generally going a little bit over in these events, but I just love answering all your guys'

**[1:02:51]** questions, and I appreciate them a ton. And thank you all for being here and just hearing me out on all the lessons that I've learned, at least a good chunk of lessons that I've learned from building agents over the years. So, I hope that was super helpful for you

**[1:03:02]** guys. And of course, if you have any questions on any of those lessons and you want me to elaborate on anything, like please ask away in the community, come to office hours next week with questions. Um, I'd love to help address anything more that you guys are curious

**[1:03:15]** about and specifically like how you can apply these lessons into your projects. I know that there's probably a lot of questions about that kind of stuff and so I'd love to get into the details of that with you as well. So, that is everything that I have for today. Thank

**[1:03:27]** you all for being here, for coming with such great questions as well. And I will see you guys around in the community.
