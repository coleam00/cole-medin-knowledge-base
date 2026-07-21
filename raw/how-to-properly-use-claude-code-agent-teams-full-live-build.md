---
type: raw-transcript
title: "How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD)"
youtube_id: uvs1Igr4u6g
url: https://www.youtube.com/watch?v=uvs1Igr4u6g
slug: how-to-properly-use-claude-code-agent-teams-full-live-build
published: 2026-02-16
duration: "0:50:21"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** So, I have a fun one for you today. I just finished a live stream where I did a full build live with a new Cloud Code agent teams. And so, I built an entire feature on top of an existing codebase, going through the entire planning process, having Cloud Code ask me

**[0:00:16]** questions so we get on the same page, sending that into an agent team as a structure plan, and doing endtoend browser automation testing. And so what I did is I took a very basic agentic chat application that I created as a foundation for this stream and I built

**[0:00:34]** payment into the application using chargeb as my platform. And so it's a very basic chat application, but what I built is the ability to purchase tokens and then you use these tokens one at a time to talk to the agent. And so it's a really good example of an implementation

**[0:00:49]** that needs to touch the database front end and backend. And so using an agent team to work on all those areas in parallel and communicate to each other autonomously as they do so. And you'll see in this video that we are able to blitz through the implementation pretty

**[0:01:03]** quickly even with some technical difficulties that I had. So very cool. I think that agent teams are a little bit unreliable right now but definitely pointing us towards what the future is going to look like for agentic development. having an entire fleet of agents working for us talking to each

**[0:01:19]** other without us having to facilitate that. So without further ado, on to the clip from the live stream. So this is a feature that was just released to Cloud Code uh with the release of Opus 4.6. So I think just like a week and a half ago, this was released to the world. And I

**[0:01:37]** want to get into this with you guys because it is an experimental feature. It doesn't work extremely extremely well at this point. We'll talk about it as we use it live. But I really do think that this is where agentic engineering is going because what we have with agent

**[0:01:50]** teams here is the ability to spin up multiple agents working in parallel but actually communicating with each other. That is the big distinguishment from sub aents. We've had sub aents for a while where we can invoke them in parallel. But the thing with sub aents is they don't communicate with each other,

**[0:02:09]** right? Like we have our main agent that spawns sub aents. they do some work. They have some kind of result and they report back to the main agent, but there's no coordination. But with agent teams, we have the main agent that it uh spawns all these teammates, but they all

**[0:02:24]** share a task list and they communicate to each other. So teammate one can send a message to teammate three. Teammate two can send a message back to the main agent as it's working. They can knock off tasks and like coordinate with each other like I'm going to handle these two

**[0:02:36]** tasks and you handle these three. It is very very powerful. Now the two downsides to agent teams, one it's very non-deterministic. You're giving a lot of control to the main agent to figure out like how do I coordinate with the agent team here and so you lose a bit of

**[0:02:51]** control for sure. And then the second downside is it's very tokenheavy when you have all of these agents running at the same time. There's a lot of overhead in as far as token usage just to have these agents communicate with each other as well. And so there are definitely

**[0:03:06]** some things that I think need to be worked on with Asian teams until it's really ready for you to like build production grade software with it. But the reason I want to cover it with you guys is I think we're going to get there probably within the next half a year.

**[0:03:19]** Building with agent teams I think will be the norm. And so I want to showcase doing a real like actually useful production build with you guys with agent teams right now. And then like I said earlier, at the same time, I want to do a really fun version of building

**[0:03:34]** with agent teams where we just try to see how many agents we can have working at the exact same time. So I am ready to blow through a lot of credits with Claude Code right now. Building with agent teams. And so here's what here's what I got for you guys. For the first

**[0:03:48]** build, the more real build, I have this agentic chat application that I built earlier this week. It is a very basic application where we can just like send a message into the agent. Uh like I could just say like hi for example. Uh all right. So obviously it's not like a

**[0:04:07]** fully perfect production application because I built this just as like a foundation of a chat application. You can think of like a really simple version of chat GPT or claw.ai. And what I'm going to do with this application is I'm going to use agent teams to build a payment integration so

**[0:04:25]** that users can purchase tokens and they consume tokens to talk to the agent. And in order to do this, I'm going to be integrating with ChargeB. So this is like a a Stripe sort of application where you can build monetization into your products, into your platforms. And so we're going to be building with

**[0:04:42]** ChargeB here. It's a solution that I've been really appreciating recently. for uh building monetization into platforms and they have a skill a chargeb integration where we can build this skill into our codebase. So claude code immediately has access to understanding how to build effectively with chargeby to make sure you avoid hallucinations

**[0:05:04]** because of the training cutoff that training cutoffs that LLMs have. And so we're going to be building with this u and so we're going to have to touch the back end the front end and the database. We're going to have to change the database schema to support transactions

**[0:05:18]** and tokens on users. And we're going to have to build in user authentication. I'm going to be using superbase for that. And then we have to touch the front end obviously to have a page for billing. We have to touch the back end to work with the leveraging the tokens

**[0:05:31]** when we are interacting with the agent. So there's a lot that we have to do here. So we're going to be able to use an agent team to work in parallel working on the front end, back end, and database. So it's a really really good use case. I've done some work before in

**[0:05:44]** workshops last year where I built a payment integration on top of an agentic chat application and I want to do it again just because it's it's a really good example of something that's not trivial. It's not really easy to build a payment processor into an application, but I can definitely do it with just one

**[0:06:01]** run of agent teams. And so it's the perfect level of complexity. And so we're going to get into that. We're going to be using agent teams here. And so my plan is to start by creating a plan with the coding agent. So I'm going to be using cloud code for

**[0:06:15]** this. Um obviously it'd be cool to use Curo, but agent teams isn't supported in Curo. So I'll be using cloud code here. And so I'll work on top of this existing application. So I'll just say like, "Hey Claude, based on this application, what are your ideas for how I can build a

**[0:06:31]** payment integration?" And then I'll have it ID it with me. I'll show you what this process looks like because the planning process is just as important as the actual implementation if not more. So, there are some new strategies that I've been coming up with recently for how to plan effectively with coding

**[0:06:46]** agents that I want to showcase to you guys. And then once I have the plan, I will send it into cloud code to spin up an agent team and knock it out. And then while that goes in parallel, that's where I will uh do more of a fun example

**[0:06:59]** where we'll just try to like see how many agents we could have running at once with agent teams. So hope that sounds good to you guys. I'm excited for this. And uh so I'll just give you like one more demo of this application really quickly just to show you what we are

**[0:07:14]** building on top of here. And so I'll go into my claude code and uh let's start our planning process here. So, I'm going to do claude. And for the sake of brevity for this stream to make sure that everything goes really quickly, I'm just going to run in yolo mode here. And

**[0:07:31]** so, what I'm about to show you guys is a really good example of brownfield development. We have an existing application and now I'm going to do some planning with cloud code to create a comprehensive feature on top of our existing application. And the planning process, the planning process is so important.

**[0:07:53]** And what I generally do to start is I do what's called a prime. And so I have a command for this just slashprime. And what it does is it walks the coding agent through a step-by-step process of understanding the codebase. Right? It's s super super simple here. I just I mean

**[0:08:14]** there's a lot of different versions of prime commands that you can build. But the goal here is to set the context up front for the conversation. Here is all the core files for the codebase so you now understand the what you need to do to research this new

**[0:08:29]** feature that I'm going to ask you to build. And generally my prime commands aren't so like here's this file, this file, this file. I just set it up this way to make it really brief here. But usually it's more dynamic. I ask it to like search through the codebase,

**[0:08:43]** understand all the core files and read them and then come back to me and give me a report of all of like just everything that you understand about the codebase. And so I'll let it finish its prime here and then we'll get on to the planning. And so again, I will run a prime command

**[0:08:58]** at the start of every single new conversation when I want to build something new. Okay, so yeah, priming is done here. So I'll say I am looking to build a payment integration into my application. Specifically I am interested in integrating with ChargeB. So I want to touch the database front end and backend

**[0:09:23]** here. So we're going to have to do a lot of planning to build the ChargeB payment integration. I want users to be able to purchase tokens in order to talk to the agent that I have configured in this application already. And so we're going to have to set up a couple of packages

**[0:09:38]** in ChargeB. And then we're going to have to integrate those. We're have to create a billing page in the front end. And then we're going to have to uh set it up so that users purchase tokens. And then it's one token deducted per interaction with the agent. and we're going to have

**[0:09:53]** to think about some other functionality like refunding the token if the agent has an error and things like that. And so there's a lot we have to ID it around here. So I want you to go through the codebase and help me understand how I can build a charge payment integration

**[0:10:09]** into this application and then after you do some research, I also want you to search the web a lot so that you understand um how to build with chargeby. can use the chargeb skill that I have integrated here as well. Um, and so yeah, that this is this is the

**[0:10:26]** chargeb skill right here by the way. Um, and so once you understand how to work with my codebase and integrate charge, then I want you to ask me a bunch of questions. This is the big thing here because we're going to clear up any confusion, make sure we're on the same

**[0:10:41]** page with every single way that we're going to integrate this new feature into the codebase. So ask me a lot of questions for things like how the building should work and how the front end will look and how we'll manage tokens and things like that. All right. So I know that's a a lot of

**[0:10:55]** of a big just brain dump that I gave here, but that's what I do with my planning is I start really struct unstructured at first. I just give a big brain dump of what I wanted to look into. Searching through the codebase, searching the web. It's using the charge

**[0:11:10]** me integration skill that I showed earlier as well. So that way it knows like it has basically perfect documentation on how to build with charge into my Nex.js application here. And then the big thing that I want to focus on with you guys here is asking the questions.

**[0:11:28]** So I told it specifically to ask me questions after it explores the codebase because the number one goal of planning is to reduce the number of assumptions that the AI coding assistant is making building the new feature. Let me say that again that is worth repeating. The number one goal of planning is to reduce

**[0:11:49]** the number of assumptions the coding agent is making because there are two kinds of mistakes a coding agent can make. And technically both are your fault. It can make it can just write bad code because your plan isn't clear enough or you didn't do enough validation or it can just deviate

**[0:12:07]** from what you want it to build. Like it maybe it's just misaligned with exactly how you're going to build that feature. And so something that I've started doing a lot that I'm showing you guys right here is literally just telling it to ask me a bunch of questions. Like I'm not

**[0:12:23]** happy unless it's asking me at least 10 questions here. Like how do you want to set up the billing page or how should we structure the packages for purchasing the tokens? How should we showcase the chargeb payment page? Like I'm going to have it ask me all those things and then

**[0:12:40]** if there's anything that I think it didn't ask me, I'll just tell it to do that. And I' I've started to really prefer this approach over just trying to specify everything in prompts. Like, of course, I could just say like, I want the billing to look like this. The

**[0:12:57]** package prices should be 10, uh, 15, and $25, right? Like, you can specify all that in the chat. But the reason I like having it ask me questions is a lot of times it'll ask questions that I didn't even really think I needed to. Like, it's making some other kind of

**[0:13:13]** assumption that I didn't even realize I had to specify. And Claude Code has this new feature built in. and the I think it's like maybe a month old at this point, but it has this um ask user question tool where it can uh pop up a multiple choice thing

**[0:13:29]** here which also just makes it really fast. Like I can if as long as it uh is on the same page with me and I can just go with its recommended option. Then I can just click through things really quickly and and also like if I need to I

**[0:13:41]** can type my own answer in the text box. So I can get really specific if I want or if it already has like a good recommendation I can just hit enter and then go on to the next question. So you'll see that in a little bit here. All right. For web hook security, how

**[0:13:53]** should we verify incoming charge me web hook requests. Um I will say here I have a username and password set in the ENB. All right. Should we handle web hook item potency duplicate events? Charge me may send events multiple times. Um no, keep it simple. Honestly, I don't

**[0:14:14]** think we're going to really have race conditions with that. for the billing page transaction history. What information should each row show? Let's say um simple list. I I want some things to be I don't need to be like too comprehensive. Okay, here we go. This is good. So, you mentioned using the

**[0:14:30]** Versell agent browser CLI for end toend testing. Should the plan include specific endto-end test scenarios? Yes, you always want to define your validation upfront. This is another really important thing to keep in mind is as a part of the structure plan, we will tell the agent, here's the linting

**[0:14:47]** and type checking we want you to do. Make sure you write unit tests and run the unit tests. And then the endto-end testing, this is the most powerful part. There's also a lot of content that I've been doing on my YouTube channel recently using the Verscell agent browser CLI. It's a very powerful

**[0:15:02]** browser automation tool that allows the agent to spin up a browser and test the website just as a user would. And it's a big upgrade over other tools I've used in the past like the Playright or Puppeteer MCP servers. And so yes, I want this to be a big part of the plan

**[0:15:19]** so the agent can self- validate. So that way by the time the final result comes back to me, it's actually tested everything. It's gone through, purchased tokens with Chargeby, interacted with the agent, and made sure that tokens are deducted. Like I want it to do all of that validation. I want to give it the

**[0:15:34]** power to do that before it even writes a single line of code. Um, so okay my there's so many questions here. Should charge items be created manually in the chargeb dashboard? Uh, I want you to set up the um items in charge B as a part of the

**[0:15:53]** implementation. So include this in the plan. And I'll say I'll just say like once we actually create the plan because right now I'm not having it actively create the plan yet. I'm going to ask it to do that once I've gone through everything I feel like I need to here. So for the conversation

**[0:16:12]** to user um relationship since chat currently has no user ID should conversations be tied to authenticated users. Yes, that is important. What should the charge be customer ID be? Uh superbase. That's right. Okay, very good. So uh man, we have asked a lot of questions at this point. I really hope

**[0:16:30]** we're getting to the end of it soon here and we can always close out of the next set of questions and just say like, "Hey, I think we got everything we need." Okay. All right. A few final clarifying questions. So, we're almost there, but this is like really good and

**[0:16:44]** it's not that many tokens overall. So, this is super high value, not too tokenheavy. Um, you said the billing page should be at flash billing. Should this be under the dashboard layout at dashboard billing or a standalone page? Um, sure. I guess we can do that. For the charge me item setup. Should it be a

**[0:17:04]** standalone script or part of existing? Uh, we'll do standalone. Should the chat page redirect to login if not authenticated? Yes. Okay. Submit answers. Okay. I think at this point we have what we need. So anyway, we are now going into planning mode here because it has everything that

**[0:17:21]** we need and it's going to create the plan which um I'm actually going to interrupt it here because I have my own work that I my own way that I want it to to do this. So one thing that I I I really like using and I I cover this a

**[0:17:37]** lot in the Aenta coding course as well is I have my plan command. This works better for me than the plan mode and the planning process that is built into claude code. So it's a command where I just describe what I want to build and then it's going to

**[0:17:54]** create a very structured plan. So the way that I always do my planning process with coding agents is I start unstructured like you guys already saw. I just kind of give a brain dump of what I'm looking to build. I have it search the web and search the codebase. Ask me

**[0:18:08]** questions. And now I'm going to formalize all this into a structured plan. And so that is what this command does. And so I'm going to uh do slash plan create an implementation plan. And then well actually one thing that I realized this is kind of like a bug with

**[0:18:23]** Opus 4.6 is I I called this plan command the same as the internal cloud plan command. And so usually I just have it look at this path. So um hold on let me copy this path and I'll say uh look here and use this command. Now uh let's create the

**[0:18:43]** structured plan or this chargeb payment integration which by the way this is how you use commands for any coding agent that doesn't support them directly like cloud code. This is just a little bit of a workaround I have to do because I just have a bad name for the

**[0:19:00]** plan command because it's the same as the internal one. Like you'll see if I do slash plan then there's like two versions and Claude Koga is confused. I just forgot to change the name beforehand. So I just tell it to look there and because commands are just markdown, it can read that and then it's

**[0:19:14]** the same as if I just did slash plan with the right command. And so we we've already got it asking really good questions here. So let's go through this. So the previous branch had a whole working implementation. Obviously I tested this before the live stream to make sure that everything was was

**[0:19:30]** working really well. Uh but I still want to build it from scratch with you guys. So I want to ignore it entirely. So I'm going to build something from scratch to really show this full implementation end to end. The chat is currently unauthenticated. Should we uh should chat now require superbase O so we can

**[0:19:46]** track token balance per user? Yes, we will require authentication. What token package? Three tiers is good to me. Should users get free tokens when they sign up? Uh yes, 10 tokens. So I so I gave a good example there of like most of the time I'm just going

**[0:20:03]** through the multiple choice just selecting options. Look at how fast that allows me to go through the Q&A of the agent here. And then at the very end there was one example where I did want to write my own thing more of a classic like let me give a free form answer to

**[0:20:17]** the agent. So I'll go ahead and submit my answers. And claude code is programmed in a way where it only asks a few questions at a time but it's going to give me more questions in a little bit here. And so it'll think through what I gave it and then in a second here

**[0:20:32]** we should see more multiple choice pop up. There we go. Perfect. Okay. So, what defines a token consumption? When should one token be deducted? So, we're getting pretty specific here, but this is exactly what I'm looking for. Again, reducing the assumptions the coding agent is making. And so, I'll say per

**[0:20:48]** conversation turn. So, one token is deducted per full round trip. So, user message plus AI response. So if the LLM call fails then what should happen? So yes, I want to autoreund the token. Where should the billing page live in the app navigation? Let's do um dashboard/billing. Uh or I'll just do like slash billing

**[0:21:10]** here. I think I'll keep it simple. What should happen if the chat UI or what happen in the chat UI when a user has zero tokens? So we will say um disable input and show a buy tokens button. Yeah, that sounds great to me. So submit those answers. Very good. And then we'll

**[0:21:25]** just see if it keeps coming up with more. And then at this point, I want to be thinking to myself as well, what other questions should it be asking that it hasn't yet? Because cloud code is oftentimes never going to be perfect with understanding um exactly everything we're going to build. Maybe there's

**[0:21:42]** other things I have set up ahead of time. Like I already have my Chargeb account, so I probably want to tell it about that for the planning as well. So, just trying to think through like literally everything I possibly can to remove those assumptions. So, okay, even more questions. Good. Keep them coming,

**[0:21:56]** Clyde. Keep them coming. For the first three token pack tiers, what quantities and prices do you want? So, um let's see here. 50 tokens for let's do it this way. So, I'll say uh $5 for 100 tokens. And then we'll do uh $10 for 250 tokens. So, we want to make it more uh bang for

**[0:22:24]** your buck over time. And then $25 for 500 tokens. Isn't that Oh, wait. No, that that's not good because it'd be uh 600. There we go. Okay, there we go. All right. So, how should the billing page look? What components do you want? Uh so, do I want

**[0:22:40]** a full billing page? token, balance card, three purchase cards, transaction history, or just a minimal purchase page. Um, you know what? Let's go for it. Let's go for the full billing page. Should we use Chargeb's hosted checkout page? Redirects to ChargeB then back or an embedded inapp experience?

**[0:23:01]** Uh, yeah, let's go through a hosted checkout. That is definitely going to be less for us to maintain then. And then it'll redirect to billing success after and update our token balance. That is perfect. Good. And like there's a lot of different ways that you can integrate with ChargeB. And so I'm really glad

**[0:23:16]** that it's asking all the right questions here. Quad code just does such a good job of asking the right questions. Like honestly, there's probably not that many other things I'm going to have to specify at this point. Do you want the token balance to be visible in the chat

**[0:23:28]** header? Always visible while chatting. Uh yes, that is 100% what I'm looking for. And that's what I was even saying earlier is going back to the UI here. I want there to be something like right here that says my token balance and then some kind of link to go to the billing

**[0:23:43]** page as well, which that's one thing I probably need to specify here. It didn't really ask about that. It's like how would the user get to the billing page from the homepage of the site here where we're chatting with the agent. So I'll probably specify that if it doesn't ask

**[0:23:56]** in a little bit. So for the database, should token balances be stored as a single balance per row or as a ledger of all transactions? Uh yeah, balance and ledger is good. Uh, should tokens be deducted before sending the message? Uh, yes. And then do you already have a

**[0:24:12]** ChargeB account set up? Ah, yeah. Yeah. So, this is actually where I want to specify some more things here. So, I'm going to say, uh, yes, I already have ChargeB set up. And I even have a Ingro set up here ready to go. So I have the chargeb web hook that's already set up

**[0:24:34]** to send requests to slashi/webhooks/chargeb and I already have all the environment variables set up in my.env for chargeb and so we should be able to go right into our end toend testing with the versel agent browser CLI once we have all the code written for the chargeb integration. So that's very important

**[0:24:55]** for you to keep in mind going into the plan that I'll create with you in a little bit. And so there is some work that I did ahead of time to get things set up just to make our build, our live build here faster. So I already have a

**[0:25:07]** charge v account set up. I'll show you this here. And this is how like all payment platforms work by the way is they have a web hook. So whenever you make a purchase in the platform, it's going to send a request to this web hook so that we can process the payment. Like

**[0:25:22]** in our case, we're going to add the tokens to the user record in our Superbase database. And we can even like test this web hook to make sure. Oh, it looks like I have to log back in here because my my page just grew stale. But I'll log back in

**[0:25:36]** and then we can like test the web hook, which it's going to uh I think it's going to fail right now. Yep, it's going to fail right now because we haven't implemented the endpoint yet. But in the testing that I did yesterday to make sure that this live build worked

**[0:25:50]** smoothly, um obviously I built the web hook and I tested it here and everything was good to go. So we have it set up on the chargeb side where it's ready to send the requests here. So now all we need our coding agent to do is implement this API endpoint that handles when

**[0:26:04]** there is a successful purchase so we can update the tokens for the user in the database. And so I'm using because this is my way to get an HTTPS URL so that I can expose this to the worldwide web so that we can uh handle the requests coming in from ChargeB. So very cool.

**[0:26:22]** All right. So with that, let me collapse that for now. Go back to the agent and I'll send this in. So for web hooks and local development, do you have a tunneling tool set up? Uh yes, I already have Ingro set up like I explained in the previous answer.

**[0:26:41]** So one thing that Claude code doesn't do here is it doesn't make the questions dynamic based on what you've answered previously. And so it doesn't really know yet that like I already explained that which is why I have to send that in. But I think that's also why Cloud

**[0:26:54]** Code only asks a few questions at a time because that way it can make sure that it didn't just send you like 20 questions in a row, but then your answer to the second one makes it so it has to ask you like an entirely different set of 18 questions coming up. So I I like

**[0:27:08]** what it does here. So honestly, like it's probably asking more questions than I'd really want at this point, but that's all good because I shouldn't really complain. The more questions the better honestly because it's going to it's quite a bit of context that it's spending here asking me these questions.

**[0:27:24]** But once I create the plan, I'm going to go into a brand new context session, a brand new session with the coding agent because the structured plan at that point is the only context I need to get the job done. It's a big thing that I teach in the Dynamis agent coding course

**[0:27:39]** is after you create your plan, that's all the context your agent needs. You can now reset the context window and then go into the implementation. Okay, so we have our plan here. Very good. Very good. So I'm going to go into plans. So it outputed it into my agents

**[0:27:57]** plans folder. So let's view a preview here. So I always recommend I won't spend too much time for the sake of brevity here, but I always recommend doing a very in-depth review of the plan before you send it into implementation. And the reason for that is pretty simple. Your plan is very

**[0:28:15]** high leverage, right? Like one error in your plan can lead to hundreds of lines of bad code. But one line of bad code is just one line of bad code. So you really need to make sure that your plan is well structured and actually aligned with what you are looking to build. Now

**[0:28:33]** because I had it ask me so many clarifying questions, I shouldn't really have any issues in my plan here. That's the whole goal. reducing the assumptions up front by having an ask me questions, but it's still important to go through and check everything. And so, you don't have to go through

**[0:28:48]** every single line, and I'm definitely not going to do that on a live stream here, but I at least want to do like a quick sanity check to make sure that everything's structured, right? I mean, this is all following the exact structure for a plan that I have

**[0:29:00]** outlined in my plan command, right? Like, I want to start with the summary, the user story, the key decisions that we're making here. So, this is all based on the questions that it asked me, by the way. So we can directly see all of our work going directly into this plan.

**[0:29:13]** And then we have the different patterns that it's going to follow based on what we already have in the codebase. This is very important for brownfield development. We have to make sure that we are following the conventions that we already have set in the codebase. Otherwise, our codebase is going to

**[0:29:26]** become an unmaintainable mess as we're building more features if they're not following the same convention. And then we have the task list. So it broke things down very nice for us for things that we have to change in the database. the back end and the front end. And then the other thing that I want to

**[0:29:42]** pay really special attention to here is the validation. I want to make sure that it's very comprehensive with the end toend validation using the agent browser CLI. So here are all of the user journeys that it's going to test. And yeah, this is a lot, but this is really

**[0:29:57]** important. it is worth it to me to spend the extra tokens during the validation to make sure that we are testing every single way that a user can use the new feature that we have built. And so this looks fantastic to me. In fact, I'm actually going to take this and put it

**[0:30:12]** right into implementation here. And so I'm going to and it's great because we uh never even had to compact our conversation. We did everything that we needed for planning within the single context window for claude codes. This is great. So, I'm going to open up a new instance. I'm going to keep this open

**[0:30:29]** just in case I need to adjust anything in the plan or ask any questions over the plan. I'm going to go into T-Mox here so I can use the agent teams. And then within this repository, I already have it enabled. If I go in thecloud folder, you can see in the

**[0:30:44]** settings.local.json, I have the cloud code experimental agent team set to one. So, we've got it enabled. I just need to go into cloud here. And then obviously again I'll just use dangerously skip permissions so that things are fast. Do not want to approve things in the middle of the live stream

**[0:31:00]** here. And then what I'll do next is I will use a command. So build with agent team. This is a command that I covered recently on my YouTube channel. So let me actually go back to my channel here. I want to show this really quick for anyone that is curious.

**[0:31:18]** Um because cloud code by itself is surprisingly not that good at using cloud agent teams because it is such an experimental feature. The problem with building in parallel is there are a lot of blockers that you have like you have to define the database schema before the backend agent can really do anything and

**[0:31:37]** things like that. And so I've built a command that essentially guides cloud code on how to more effectively use agent teams. So it's not trying to do literally everything in parallel. There are some things we can do in parallel, but my command implements what I call a contract first approach. The lead agent

**[0:31:55]** defines the contracts between the front end, backend, and database and anything else similar to that. And then it sends that in as part of the prompt to each of the agents running in the team. So they can work in parallel, but they still have that sort of coordination defined

**[0:32:10]** up front. And this has been working really, really well for me. So, I cover that in this video right here. If you're curious, if you want to dive more into that on my channel, I've got that. So, what build with Asian teams does is it's a command that includes all those

**[0:32:23]** instructions. And so, all I have to do is pass in the path to the plan. So, I'll copy the relative path here. And then the second parameter that I have with this skill, I'll just show this really quick. So, I'll go to um uh where is it? skills build with agent

**[0:32:42]** team. The second parameter here is a number of agents. And so if you don't specify this, you actually allow cloud code to decide the number of agents that you're going to have in the team. So it can figure that out based on your plan. It's really dynamic because what this

**[0:32:55]** command does is it takes the plan figures out how do I split this work into different agents in the team and then how do I define like what is parallel versus what do I need to define as the contracts up front, right? like we have the um contract first approach.

**[0:33:11]** Define the contracts, map that before you start spinning up all of the agents, right? Like that's it's only step five where we actually spawn all the agents in parallel. So we're still doing most of the work in parallel, but we're doing all of that really important stuff up

**[0:33:26]** front so the agents don't have to step on each other's toes as much. So for this case, to keep it more deterministic, I'm going to say that I want three agents. So I'm going to actually define that myself. All right. Right. So, I'm going to go ahead and send this in. Also going to

**[0:33:39]** say uh make sure you use the charge B skill as you implement. Very important that um the backend and front-end agents do that. So, it's something that I probably should have included in my plan, but I'm just going to be very explicit here because this is going to be super

**[0:34:01]** important to make sure that it doesn't do any kind of code hallucinations with ChargeB. So, I'm going to take advantage of this skill. This is something that I really appreciate about ChargeB and most SAS platforms that you're going to bring in as a tool in your codebase, a library

**[0:34:18]** or just some kind of capability you're paying for. It's pretty important. I I think this is the also the future of agent coding is every single platform that you integrate is going to have some skill that you can bring into your coding agent so it knows how to best

**[0:34:31]** leverage the SDK. Right? This is like a guide for how we can use the chargeb SDK to build things properly first try in our next.js code and this does make a real difference. I tested building both without the skill and with it and it's very very helpful giving context to the

**[0:34:49]** agents because a lot of times agents because of their training cutoff they don't know the right documentation for these libraries or they maybe don't know it at all because it's a newer platform and so being able to give it easy access to update information it's something that I worked on a lot last year with

**[0:35:04]** archon but now a lot of these tools are just building that in um like what we have right here with the charge be skill all right very cool we can see that uh we have our first we have the core core agent. I guess our lead agent decided to

**[0:35:16]** create a core agent for our implementation of charge v. Very, very cool. So, it's starting by claiming task number one in that shared task list. And then in the meantime, our um lead agent here is spinning up the other two agents in parallel. So, okay, we got our three chargeb

**[0:35:34]** agents running at the same time. So, we have a core, a front end, and a backend agent. I assume the core agent is working more on like the database schema and like the authorization stuff. I'm I'm not actually sure entirely. Um but you could always ask it, right? Uh

**[0:35:49]** WSL-shutdown. Sometimes you got to do this. Unfortunately, WSL is a pain sometimes. Um okay, so go back to my terminals. Let me start a new WSL. I have to do this because Asian teams does not work in just Windows. if I want to have the different T-Mux terminals. So,

**[0:36:09]** I'm going to restart everything here. Dangerously skip permissions. All right, very good. And then I'll do build with team. And then I will pass in the plan again. So, copy the relative path. There we go. And then hopefully we won't crash this time because we aren't spinning up 12

**[0:36:30]** sessions, 12 agents or actually 13 in total. All right, there we go. So yeah, now now we will get back to things once it has started all the agents. I guess the agents were were actually running in parallel. We just kind of missed it. So it crashed. It crashed, but all of the agents, they

**[0:36:53]** were actually working behind the scenes. It it was just like the terminal that was bugged. So we did actually we we had all of the agents work in parallel. Now it's just we need our lead agent to come back and fix things. So interesting, interesting. So it's going to fix the

**[0:37:08]** linting errors and then run the final validation. So in a roundabout way, we had the agent team work. So I know that maybe it wasn't the best demonstration because my WSL crashed, but the agents did actually build everything. So that's pretty cool. We just didn't get to see

**[0:37:23]** all the logs, which with the small terminals in T-Mux, it usually wouldn't be the case anyway that we'd see much happening. But this is cool. So, it spun up another agent in the team here to handle the backend fixes. So, okay, that's pretty neat. All right. And then back to your

**[0:37:39]** question here, Sean. I'll show this again. How can we track agent intercom communication? So, we can't really The one thing that I will say is we can go to the lead agent here. Like I can do controlB back to the lead agent and I can say like how have the agents been

**[0:37:54]** communicating with each other? And I'm not going to do that. I'm going to let it just keep going here. That's kind of cool. It spun up a whole another team for the fixes here. So, we got most of the way with the previous agent team, then it crashed. Now, we're

**[0:38:06]** back just validating things and doing the final end to end testing. Um, so yeah, there's not really a way to besides just asking like how have you been communicating with the agents. You'll get a decent answer if you do that. So it it does have that meta reasoning of knowing how the agents have

**[0:38:22]** been talking to each other, but there's no like dashboard that says like this agent claimed this task and sent these messages to these agents. I think you could probably build that with hooks or something. I wouldn't be surprised if Anthropic improves Asian teams in the near future by adding in more

**[0:38:40]** observability, but right now it is blatantly missing in my mind from the tool. Why does Asian teams cost more than calling sub agents? Fair question. So, the main reason is just because of all that overhead with communication. Managing the share task list, sending messages to each other. A lot of it

**[0:38:58]** isn't optimized at this point, but it's not like it's that crazy. In fact, let's look at that right now. So, while this is running, let's go to my usage file settings. So, I like using cloud desktop just to check my cloud um usage for my subscription. And take a look at this. It's not that

**[0:39:17]** bad. I've only used 16% of my current session and it resets in 37 minutes. And we've done a full implementation. I know that it it crashed and so we had to spin everything back up. But like we still did use Asian Teams for that entire implementation and it was only 16%. And

**[0:39:35]** I've only used 11% u for my weekly limit. And that's a lot of stuff I was doing yesterday and the day before as well or I guess it resets every Friday. So, just the work I was doing yesterday, too. It's not that bad. I I I'm kind of

**[0:39:48]** surprised that people have been complaining so much about it consuming a lot of tokens because with the 100 or $200 a month max plans for Claude, you're going to be able to spin up teams all the time and not run into limits. It's fine. It's it's really like they

**[0:40:04]** they probably can do a lot of optimizations, but it's still not that bad right now. Um, cool. So, the three agents worked in parallel. We have our backend fixes, billing page, and test fixes. So, it says that everything is perfect. Now, one thing that Opus 4.6 missed. And

**[0:40:21]** unfortunately, Opus 4.6 specifically seems to miss this a lot for me is it will always ignore the endto-end testing that I want it to do with the Asian browser CLI. And so I'm going to go into AquaVoice here and demand that it does the full testing because I want it to,

**[0:40:38]** like I said earlier, go through all of the user journeys and make sure that everything is working perfectly before controls pass back to me. So I'm going to say, "All right, I need you to go through the end toend testing with the agent browser CLI. You totally missed

**[0:40:53]** that. We need to go through all of the user journeys, and I do not want you to stop. You cannot stop until you've tested every user journey and you are confident the application is working perfectly. So go ahead and start up the application. Make sure that you are

**[0:41:10]** going through each of the user journeys that we have outlined in the structure plan. You can read the structure plan again if you need to, which it shouldn't need to because we haven't even had to reset the context window. So I probably didn't even have to say that. But

**[0:41:22]** anyway, I'm just being very clear here that you cannot skip this step. I don't know why Claude with Opus 4.6 specifically, this has started to happen for me. It's not the biggest deal because I can just have it um start things up again and um pick up all that

**[0:41:38]** testing that it failed to do, but it's just annoying that I have to do that. All right, so um let's see. I don't like that it's making the curl directly to like Okay, you need to use the Verscell agent browser CLI. Honestly, I have been more impressed with Opus 4.5 than I have with Opus 4.6.

**[0:42:02]** I've got the skill here. You have the ability to use the Asian browser. It it with Opus 4.5, it used to automatically go to the end to end scenarios without me having to ask it. Okay, there we go. So, now now it's using the skill. So, we're good now. We're on track now. But

**[0:42:20]** I don't like that I have to ask it that. It's like it's pretty consistent now. Um, now it probably does mean there's an opportunity for me to improve my plan or improve my command so that it's more clear it has to get right into doing that. But, um, it is kind of like annoying

**[0:42:38]** whenever there's a new model that comes out. Sometimes you do have to adjust your prompts and your commands to work with that newer model. It might be a more powerful model, but it understands your prompts differently. And I've had that happen a lot, especially when switching between different providers.

**[0:42:54]** But even if there is like an upgraded version of an LLM from another one, it it just understands the input differently. That's all it comes down to. But it's very cool to see it go and use the Asian browser. I could have had it do it in headed mode as well.

**[0:43:09]** Actually, let's do that. Uh do headed mode so we can watch the validation because it's just doing everything behind the scenes with a headless browser right now. But it'd be really cool for us to like watch it go through the user journeys like buying tokens and interacting with the agent. Um, so let

**[0:43:27]** me close the current browser, reopen ahead of mode so you can watch. Let's I think that'll be good for the stream so we can actually watch things. So it's finding issues as it's going, which is okay. I totally expect that. This isn't necessarily the the fault of using Asian

**[0:43:41]** teams, but this is why I do endto-end testing. No matter how clear my plan is, there's always always going to be those little issues with the code that it has to address, and it'll find those things when it tries to actually use the website as a user would. So, this is

**[0:43:55]** good. This is what we're looking for here. Um, and yes, this is exactly what I have seen before as well. You'll it'll say like all tests complete at the bottom, but then there's a wall of text with this hidden thing like, oh, test X didn't work. Well, that's just because

**[0:44:10]** of some other issue that already existed. Man, that grinds my gears. That exact thing happens all of the time. And there are definitely ways to like improve that by being specific in your global rules or your commands to like not say that, right? Like you can include in your instructions. Um, do not

**[0:44:30]** ignore a failing test just because you think it's due to something else that's happened before, right? And like sometimes that will help, but it still is like the nature of LLMs where they'll do that and it's super annoying. So anyway, let me uh can I make this bigger here?

**[0:44:46]** Okay, I can't. So the window size is kind of limited here. So maybe it's hard for you guys to like really read the fine print of what's going on, but yeah, let's let's get let's let it go through. So it's registering a new account with Superbase. Obviously, uh there's an issue with the

**[0:45:05]** browser here, so it'll have to determine that. There's always those things that it has to figure out is wrong at first and then it'll fix those like derpy glitches at first and then the end to end testing becomes a lot smoother. So, it'll get there. It'll get there. But, this is not

**[0:45:20]** surprising to me. But, that's why we have it do this autonomously because I don't care that it has these kind of silly problems at first because then by the time it comes back to me, everything's great. But, all right, let's let's see how we're we're looking. So, all right,

**[0:45:36]** taking a screenshot for the login. Looks good. All right, so anyway, finally the our agent figured out these issues in the back end. But it it's cool, right? Like I just this is a great demo. Even though it's annoying that this had to go for like a solid 10 minutes to find these

**[0:45:53]** issues, it's able to address everything behind the scenes because it's able to test just like I would if I were to spin up the app myself. But now I don't have to be the one to say like, "Hey Claude, the agent didn't respond to me here. You need to look into this." Like it just

**[0:46:06]** figures that all out itself. It'll retest automatically. Everything is taken care of automatically. That is the beauty of end toend testing. Now, theoretically, I could use agent teams here to do it more endtoend testing in parallel. And so maybe I'm not like using Asian teams as much as I could, but typically

**[0:46:28]** I I like to use the teams for the implementation itself, writing all the code and then I leave it up to the lead agent to do the validation at the end. And so it just so happens that the endtoend validation generally takes a while, but it's still a lot of work

**[0:46:44]** being done in parallel up front. You guys saw that it only took like 5 10 minutes to go through the entire implementation and and yes, there are some corrections that have to be done here, but it was able to chug through that build very very quickly. It would

**[0:46:58]** have taken Claude by itself like 30 minutes. So that was really cool to see. Now we just have to get through the little glitches that come up which would happen even if we weren't using agent teams. So this is good stuff. All right, so now we've gotten to the

**[0:47:11]** point where everything's working with the agentic chat. we're able to consume tokens correctly. Now we're getting on to the chargebe stuff and so it's trying to purchase tokens. It's encountering some errors already which we knew that it would because we were running into some problems when we tested it ourself

**[0:47:26]** but now it's just going to knock all of those out. And that's kind of the theme that we've had here is like yeah with Asian teams it wasn't perfect in its implementation might have happened even without it but it doesn't matter really because once we get to the endtoend

**[0:47:39]** validation it's going to find all these problems and fix them autonomously and I really don't think it is agent team's fault because this is a more complex implementation that we're doing here integrating with chargeb but I'm just showing you that like with end toend validation we're able to get through all

**[0:47:55]** of the hiccups and so that is the beauty of it. And there we go. It found and fixed all of the issues during its end to end testing. And so we have hot reload on. So Mona Truth just got to bring over the browser tab here. So okay, we have 318 tokens cuz it

**[0:48:12]** purchased some for us during its testing, I believe. And so let me see. I'll click into this and okay, good. We're in our billing page. We got 318 tokens. Let's go ahead and buy. Let's do 250 here. And so this is just using a test account in ChargeB. And so I'm not

**[0:48:28]** entering real credit card information here, but it is simulating the full production purchase flow. And so I have just a fake credit card information set up here, fake address. I'll go ahead and pay. And okay, processing payment. Waiting for your tokens to be credited. And there we go. Tokens added to your

**[0:48:44]** account. 568. Man, this is working perfectly. We got the transaction history here as well. Oh man, this is amazing. Okay, so I'll go back to the chat here. And then let's just test the full thing end to end again. So, I'll just say uh what is 2 + 2? Just I don't

**[0:48:58]** really care. Some random message here. 568 down to 567 tokens. We got a response. Very cool. Okay, man. This is working perfectly. So, again, we had to wait a while for the end toend testing to find all the issues that came up from the Asian team build, but I think that

**[0:49:15]** would happen regardless and it was able to address everything. So now I would consider this when control is passed back to me and the application's perfect for a pretty non-trivial implementation with this whole payment integration with charge me. So this is fantastic. All right, so now here I am outside of the

**[0:49:32]** live stream just giving a quick outro to the video here. I hope that you enjoyed going through the full process of brownfield development with Claude Code's new agent team feature. It really does seem like the future of a gentic engineer. You saw there the speed of those parallel agents. I thought that it

**[0:49:49]** was crash but it actually went the entire time and just like five minutes built out everything. It was more just the end to end validation that took a while. But I hope that was valuable for you to see as well how the agent can go through the user journeys just like we

**[0:50:01]** would and validate everything replacing a lot of that manual validation we have to do ourselves. So it's that planning up front and the validation at the end that really makes it so that we have stable implementations with our coding agents. And so if you appreciate this video and you're looking forward to more

**[0:50:15]** things on agentic engineering, I would really appreciate a like and a subscribe.
