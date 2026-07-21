---
type: raw-transcript
title: "My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering)"
youtube_id: goOZSXmrYQ4
url: https://www.youtube.com/watch?v=goOZSXmrYQ4
slug: my-complete-agentic-coding-workflow-to-build-anything-no-fluff-or-overengineering
published: 2026-02-23
duration: "0:42:27"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Everyone knows that you need a framework for working with coding agents, but not many people have one that's simple, really their own, and something they can evolve over time. Now, there are a lot of overengineered frameworks out there on GitHub. All these multi-agent systems people are creating. I respect what

**[0:00:17]** people are working on, but a lot of times you just need something really simple that just gets the job done for you. because I know that you have good ideas that you want to build and you don't want to spend more time creating your agentic coding workflows than you

**[0:00:30]** do actually coding. And so that's what I have for you right now. This is my dead simple framework that I use every single time I'm starting a new project with my coding agent. Now, brownfield development, working on an existing codebase, is slightly different. That's for another video. This we're focusing

**[0:00:46]** on green field development. We want a simple framework to get our feet on the ground running as fast as possible building anything new. And everything that I am covering here is universal. These principles will apply no matter the coding agent that you are using. So there are really two parts to this video

**[0:01:02]** and I'm going to be doing a live build with you as I'm explaining everything here to make it super concrete. And so what I have right now with my codebase is pretty much nothing besides my AI layer. So there's a few commands and skills that I brought over. This is what

**[0:01:16]** I use as a starting point for every single one of my projects. We're going to be creating something from scratch. And so we need to start with our initial planning, creating what is called a PRD. This is the initial scope of work that we have to create the minimum viable

**[0:01:30]** product for our application. And there's a lot that goes here setting up our initial AI layer before we get into any of the actual coding. And then we take our PRD and we split it up into phases of work. And we're going to knock it out with PIV loops. And so I'll talk about

**[0:01:46]** what that means. We'll see an example of that. And then while I'm going through this entire implementation, I'll be covering the four golden rules that we want to follow all of the time. So these golden rules are going to fit in pretty naturally as I'm going through creating

**[0:01:58]** the PRD, our AI layer, and doing a PIV loop. For example, the context management. Context is your most precious resource when working with AI coding assistants. That's going to be a big theme throughout. also creating commands and skills for everything and the system evolution mindset because what we're going for here with our

**[0:02:16]** system is to create something that is reliable and repeatable. And so I'll be speaking to that as I go through everything. So just trying to hit on some of the core themes that you'll see throughout this. It's going to be a very valuepacked video. And so we'll start

**[0:02:29]** here with our initial planning creating what I like to call the AI layer. So I'll explain what that is and we'll build it together right now. So your AI layer is all the assets in your codebase that you created to be context for your coding agent like your PRD what are we

**[0:02:45]** going to build your global rules how are we going to build it the commands so we have reusable workflows for our coding agent we'll focus on the prime one at first and then also sub agents so we can delegate for research and generally how I work with my AI layer and I have this

**[0:03:00]** as a resource for you is I have a more generic set of commands that I'll bring into any new project. And then the point of this is as my code base grows and I start to build it out, I will also evolve my commands to make them more

**[0:03:14]** powerful for the specific use case, just making them more specific to my code. And that's generally my recommendation for you. And so use this as a starting point if you want. I'll have a link to the GitHub repo in the description. The point of keeping this so simple is that

**[0:03:28]** you can take it for yourself and easily evolve it for your use case and how you like to work. That's why I recommend something like this over a more complex framework like BMAD or the GitHub spec kit. They're really, really powerful, but it's hard to really make it your

**[0:03:42]** own. I want you to be able to make this your own. So, right now, I'll show you what it looks like to create an entire PRD, define the initial rules for our codebase. We'll even customize our first command a little bit, and then I'll talk about sub agents throughout. And I know

**[0:03:55]** we're doing a lot of planning before we write any of our actual code with the piv loops, but it's important to do this. Doing the planning up front might seem like we're taking things too slow, but if we create a really good plan, like we have good rules, a good PRD, it

**[0:04:10]** means that all of our development after is going to be a lot faster and more reliable. So, let's start with our PRD. A lot of people call this a spec. Again, it's just the entire scope of work to build out the initial version of our application. And then after that point,

**[0:04:25]** when we have a good foundation, it moves more to brownfield development. That's the next video that I've got coming. So stay tuned for that. And so what I'll do here with my cloud code, I got a basically empty project here besides my AI layer is I will simply have a casual

**[0:04:40]** conversation at first just telling it about my idea, maybe some ideas I have for the tech stack and the architecture. You start really unstructured, which also just makes it easy to get started. And then you eventually get to the point where you use your conversation as context to create a structured PRD. And

**[0:04:58]** I have a command that'll help us get the job done. I'll cover that once we get there. But first, let's just start with our idea. And so what I want to build just as a fun example for this video is something kind of like Linkree, more like a self-hosted version where you can

**[0:05:13]** set up your own kind of landing page that has a bunch of links that you can organize. You have analytics like the click-through rate on your different links. I want to build something like this. It's a good example for right now because it's not super trivial where you

**[0:05:24]** could just vibe code it really easily with some of the more um cool features we can add in, but also it's not going to be overly complicated where we'll barely have anything by the end of this video. And so I'm going to use a speechtoext tool to get the job done

**[0:05:37]** here. I highly recommend using something like Aquavo. This is what I use. There are a lot of good free and open- source options as well. Whisper flow, Epicenter whispering, great tools that we have here. I love using speech to text cuz I can promise you I will never be able to

**[0:05:52]** type 226 words per minute. And so I'll use a tool like this just to give a big brain dump at first for what I want to build. And this is going to be really raw, but I'm going to go ahead and do a brain dump live for you right now. And

**[0:06:04]** pay attention to what I asked Claude Code to do for me because this is just as important as the ideas that I'm sharing. I'll explain a little bit about that after as well. And by the way, you can do this entire thing with any AI coding assistant. So here we go.

**[0:06:18]** I want to build a link in bio page builder. So something kind of like linkree. Users can create an account. They can create their own landing page where they specify the links. They can change the order. I want them to be able to have analytics so they can view the

**[0:06:31]** click-through rates on their links as well and they can customize the theme. And then for the text stack, I'm thinking probably like Nex.js. I'd like to use Neon for my database and Neon authentication. So definitely spin up a sub aent to do some research for that. Um, and then for the architecture, not

**[0:06:46]** super picky on that. Definitely want your recommendations for that and just how we're going to handle the theming and the link building, all of that. And so I want you to also spin off an agent to do a bunch of web research on just like best practices for creating these

**[0:07:01]** linkree type applications. And then what I want you to do after is come back to me with a bunch of questions so we can get on the same page with even the little details for what we are building here. All right, very good. So, I'm going to go ahead and send that off and

**[0:07:14]** it'll just transcribe in a couple of seconds here. There we go. And boom, we are off to the races. And the most important thing that I did there is actually right at the end when I told it to ask me a bunch of questions after it does its research. So, this is really

**[0:07:29]** important to drive home here. Your number one goal for any kind of planning with coding agents is to reduce the number of assumptions that your coding agent is making. Because in the end, when a coding agent makes a mistake in your codebase, half the time it's not that the code is bad, it's that you just

**[0:07:46]** weren't aligned on what exactly you should be building. The common adage is that one line of bad code is just one line of bad code. One line of a bad plan is maybe a 100 lines of bad code. But then one bad line in a PRD, that could

**[0:08:01]** be a thousand bad lines of code because you have misalignment. And so I have been doing a lot of experimentation with ways to, you know, reduce assumptions over time. And having the coding agent actually just give me a flurry of questions has worked so incredibly well for me because especially Claude Code

**[0:08:19]** with its ask user question tool where it can give like multiple choice or write your own answer. We'll see that in a second. It's so powerful. Like they do a really good job thinking about all the edge cases and little details that maybe we aren't even thinking about. like it's

**[0:08:32]** hard for us to just reason oursel about what assumptions the coding agent might make. So it's very very powerful. And then the other thing that I did as you can see right here is we have different sub aents that are running for research. I love using sub aents for any kind of

**[0:08:47]** planning creating the PRD or even for the planning process of the piv loops that we'll talk about in a little bit. And so with Cloud Code, I don't actually have to create my own sub agents because we have the exploration and research sub agents built right into the tool. For

**[0:09:03]** other coding agents, you might have to build your own, which is why I wanted to call it out here. But pretty much every single good coding agents these days supports the idea of sub agents. And I love using them for research. And the reason for that is context isolation.

**[0:09:17]** Again, one of the key themes here is we want to really protect the context of our main coding agent. And the reason that research is such a good use case for sub agents specifically is because when they explore, they're looking at everything. They're doing a bunch of codebase exploration or web research.

**[0:09:35]** They're loading in tens, even hundreds of thousands of tokens for their work, but really all we care about is their findings, the summary at the end that they return to our main context. And so, we can keep our main context clean. I don't recommend using sub aents for

**[0:09:48]** implementation because with implementation we usually care about all of the context of the files that we've been editing and creating otherwise it leads to a lot of hallucinations in my experience and that's also why claude code doesn't have any built-in agents for implementation it's just for research and that's exactly what we are

**[0:10:05]** seeing right here and so I'm going to let everything complete and then I'll come back once it has the questions for us all right so all of our sub agent research is done and we now have the initial set of questions to answer. And as I go through this, I think you'll

**[0:10:19]** really appreciate as much as I do because we are clarifying a ton of things. Every single question that we answer here is removing an assumption from the coding agent. And because it's multiple choice and usually one of the options it presents here is good. We can blitz through this really quickly. And

**[0:10:34]** so we can be pretty confident going into the implementation that we have all of the details locked down. And so for example, how should the public page URL structure work? I actually like option number one here. And then boom, on to the next one. How many pages should each

**[0:10:47]** user be able to create? Let's just do one page per user. I mean, some of these I'm just going to keep going with the defaults here. But there are a lot of instances where it really fundamentally misunderstands something. And that's where I can type my own answer to really

**[0:10:59]** clarify. So I don't know if I'll run into an example right here. But what I'm going to do is I'm just going to go through and answer all of its questions. Come back once I've done that. You don't really need to see me do every single question here cuz it might do up to like

**[0:11:11]** 20 25 questions. like it will take this pretty far and so again you have to be a bit patient with this but every single question you answer could save you from having hundreds of lines of bad code. So actually here is a good example where I want to clarify something entirely

**[0:11:27]** different from what it suggested here. So it's saying this is the second batch of questions that Claude has asked me by the way. Should the link editor have a live phone frame preview? So, kind of like lovable or bolt-on new where you have the the view of what you're

**[0:11:40]** creating and then you have the builder on the left side or should it be inline? And I kind of want to actually have both options here. So, I can go to the chat about this and so then it will ask me the other questions after, but now we

**[0:11:51]** get to have a little bit of a conversation for this thing specifically. And so, I'll say right here, I want to have an inline editor, but I want the option to be able to see the preview as well. So, essentially, I want to have three buttons. one where I

**[0:12:03]** just see the editor, one where I see both, and one where I just see the preview. So, I send that in, and then it'll come back and ask me more questions, and I'll just continue the process. So, here we are. Claude finished asking me a bunch of questions,

**[0:12:15]** probably more than I need, but you can really just tweak this to whatever you want to do. And now, it's time to create our PRD because, as we can see from the final spec summary, it really does have a clear understanding of exactly what we're going to build, even where I'm

**[0:12:29]** going to deploy it. I'm going to deploy this to Verscell after I build it. This is fantastic. Like I feel like it isn't really assuming much anymore. So now what I'm going to do is just run my create PRD command. I'll just put this includ. You can really put this wherever you

**[0:12:44]** want. You can even call it whatever you want. And so I am using the command that I mentioned earlier because going back to our four golden rules, one of the big ones here is to commandify everything. If you do something more than twice, which I have definitely started more

**[0:13:00]** than a couple of projects, you should make it a command. And then otherwise known as skill because cloud code did recently merge commands with skills. But I still like to have the distinction of commands are things that you invoke yourself like /commit. And in skills, that's when an agent decides to read

**[0:13:17]** context like understanding how to do something new. And so I'm creating a command here because I'm deciding okay at this point in the conversation I want to run this command to output a structured PRD. So as a part of this command I'm giving it the exact structure all the different sections

**[0:13:34]** that I want in the PRD. So that way I'm making my whole process repeatable. Right? A big part of this system that I'm showing you here is you can create something that works for you and then you can do it over and over and over again for new features and new code

**[0:13:48]** bases. And so I'm going to do /create PRD. I'm going to let it rip and I'll come back once we have our final PRD. All right. So our PRD is now created. And it is very comprehensive, but that's good because it's not like we're going to send this into our coding agent to

**[0:14:03]** implement. Instead, we're going to build things in phases that are described by our PRD. So I'm not going to do a ton of validation on camera right now. definitely not worth your time. But I do want to say that it is important to read through this and make sure that you

**[0:14:17]** really are aligned on everything. Otherwise, it is going to lead to a lot of bad code in the future. And so the first thing I want to call out really quick here is we have our MVP scope. And in this we can see all of our questions coming to life in our PRD. And that's

**[0:14:31]** important because the conversation we just had was really just unstructured context to feed into the PRD. The PRD is the only thing that's going to survive. So we need to make sure that the entire conversation that we have with our agent is really put in here. We have our out

**[0:14:45]** of scope which is equally as important. What we don't want to build right now. We have the entire directory structure. So it already understands generally what is going to go into our codebase which is good because we've already established our tech stack and architecture. And the important thing

**[0:14:58]** with this is that we have our phases of work. And so from this when we use our prime command that I'll talk about in a little bit we're able to establish like okay what have we already built in our codebase what do we have to build next based on the PRD. So this is going to be

**[0:15:13]** one of the important pieces of context at the start of every conversation as we build our MVP. And by the way here's the section itself where I lay out the phases. Each one of these is going to be a granular implementation one of our pivloop. So we build the foundation then

**[0:15:28]** we build the link management. Then we do the theme and we're going to plan each one of these individually so we're not trying to have the coding agent ever do too much at once. Okay, so we just created our PRD and that really is the biggest thing. So we're almost there

**[0:15:41]** getting to our first implementation. The next thing that we have to set up is our rules and this is going to be pretty basic at first because our rules are definitely going to evolve the most as we are evolving our actual codebase. And so I'm using cloud code, but I'm just

**[0:15:55]** referring to aagents and agents.mmd because this is more of the universal standard for the naming for global rules. And so the important thing here is that the constraints and conventions that we always want our coding agent to follow, this goes in our global rule file. And so this is things like the

**[0:16:13]** commands to run our application, our testing strategy, our logging strategy. No matter what we're building, we always want our coding agent to see this. And so we want to create this right now, at least an initial version to get us started. And then the other component I have here is the reference folder. You

**[0:16:28]** can also use claude code skills for this by the way, but this is just more universal cuz a lot of times we have other contexts we want the agent to have in mind, but only when we're working on specific parts of our application like a guide to building front-end components

**[0:16:42]** if we're working on the front end. And the reason we don't want to just dump this all into our agents.mmd is this is loaded into the context of the coding agent every single conversation. And remember context is precious. So we want to keep this really concise and then

**[0:16:56]** just point it to each of these files. So we can tell the coding agent if you are working on the front end then you can read this file or if you're building new API endpoints then you can read this file. So this is essentially progressive disclosure. We have different layers of

**[0:17:09]** context that the agent can discover over time to make sure it's only loading what it actually needs based on the current task at hand. And so for this one, I have yet another command. Again, commandify everything just like I have a template I like for my PRDS. I have a

**[0:17:24]** template that I like for creating my global rules. And so, first we are going to discover what we already have in the codebase because I created this to work for existing code bases and new ones. And so for this really all it's going to explore is the PRD. It's going to figure

**[0:17:38]** out what's our tech stack, what's our architecture, do some web research for testing and logging strategies, and then bring all that together with my guidance to create my global rules. And I have the exact structure here. And so, it's going to be based off of this template that I have. So, I'll show you this very

**[0:17:54]** quickly as well because this is the template that I love using for all of my global rules. And you can see that everything here, we really do care about our agency no matter what. like, okay, here's our tech stack, the commands to run and test things, our project

**[0:18:07]** structure. So, it has essentially an index of our codebase, our architecture, our code patterns, like things like naming conventions, testing and validation strategies. It's pretty basic overall, but we're going to create this first and then I'll give you a couple of examples of reference documents like our secondary ondemand context. And so I'll

**[0:18:24]** go into Claude here and really just in the same conversation where I created my PRD, I'm just going to do create rules because I can really use all of this conversation as context to help. Uh so it just right away it knows, okay, here's our PRD, here's our text stack

**[0:18:38]** and things like that. All right, so our create rules command finished and we now have our global rules. And so I have it pulled up already. Pretty standard here. We have our text stack, the commands like we're using Drizzle ORM for our database for example, project structure, architecture, code patterns. For the

**[0:18:54]** sake of brevity, I'm not really customizing things here or applying my own thoughts to this very much. But depending on how technical you are, this is your time to make sure that the constraints and conventions, the code patterns is really aligned with how you want to create your code bases. So you

**[0:19:09]** can spend a lot of time with this if you want. I'm just not doing it because I'm focusing on the highle ideas with you right here. And so I also had to do some web research on best practices for creating things like front-end components and API endpoints. And then

**[0:19:22]** based on that, I had to create some ondemand context as well. And again, these could be cloud code skills if you would like. And so if we go back to the global rules and we scroll down to the on demand context section, here we go. When working on front-end components,

**[0:19:34]** read this file. When working on API routes, read this file. So the claw.md is the only thing loaded in up front, but then it'll decide to bring this in when it needs. And in my experience, it's really good at referencing this, especially if our global rules is concise like it should be. Like we don't

**[0:19:51]** even have 240 lines here. Just 233 lines for our global rules. And then we have our APIM MD and components.md. These are a lot bigger because when we are working on the task and it's very specific to this then it's okay to bring in a lot more information to make sure we have

**[0:20:08]** good guidance for our coding agent. So again going back to our diagram here the rules this is how we want to build things. The PRD is what exactly we're going to build. And so with both of these things in mind the last thing that I want to talk about here is commands

**[0:20:22]** specifically the prime command. Then we'll get into building the plan for our first phase and creating the code. So, at this point, we have the initial AI layer. We have our PRD, our rules, and those generic commands that I brought in that you can feel free to use for

**[0:20:37]** yourself. And so, we're going on to implementation now. But here's the thing. At the start of every new conversation with an AI coding assistant, we need it to catch itself up to speed on the codebase. What are we building? What comes next? That is where the prime command comes in. And so, this

**[0:20:53]** is a command we'll run / prime at the start of every new session. It is a guided process for it to explore our codebase and get itself to the point where it has the mental model where it's ready for the next feature implementation. And so we'll have it

**[0:21:07]** read documentation, explore the structure. It can use sub agents to do all this as well. Checking the git log because that's another thing that I'll talk about more in a bit as well is using git log as our long-term memory so it can see over time how our codebase

**[0:21:21]** has been evolving because that'll help it make decisions around what it's going to build next. And so after this command, it's going to output to us its understanding of the codebase. So we can validate it knows what's up with our codebase and we can go on to building

**[0:21:35]** the next thing. And so not to cover the prime command in too much detail right here, but we do some operations with git to take advantage of the history. And then we're reading through the core files and identifying anything that we need to pay special attention to that

**[0:21:47]** are like main entry points to our application for example. And then this output report is how we can validate its understanding. And we can evolve this over time to make it specific to our project. Just to give you one really small example here for reading core documentation, I could say read the

**[0:22:04]** Drizzle migrations so you understand the database schema, right? It even had the tab complete there. I knew exactly what I was going for. And so as you kind of build your own understanding of like what are the core things I want my coding agent to pay attention to in this

**[0:22:17]** codebase like maybe other documentation we have in the reference folder for example, we can add that here. And so now what I'll do is I'll go into Claude, but I'm going to start a brand new conversation because now we're going to get into our first piv loop and I'll

**[0:22:30]** explain the entire pivot loop in a little bit here. But watch this. I'm just going to run prime and that's going to be the beginning of my conversation before I do anything. I want to explore. And so in this case, it's going to realize like, okay, this is a brand new

**[0:22:42]** project. Let me check the PRD. And it's going to recommend like let's do phase one first. Let's create the foundation for our project. So our prime completed. Here is the project overview. a link in bio page builder the current state it's an empty repository with just documentation I did do a test build

**[0:22:59]** earlier which is why it says this but I cleared everything for right now and then it pulled the first phase the foundation from our PRD and this is what it's recommending that we build and that's exactly what I am going for here I want it to pick out phases one at a

**[0:23:12]** time from the PRD so we have granular implementations for our PIV loops which speaking of the PIV loops we are going to get into this now and so PIV is short for plan, implement, validate. We take focused work, usually a phase from a PRD, and we run it through this entire

**[0:23:31]** process. So, we create a structured plan, that's this part right here, around what we're going to tackle. And this process is actually pretty similar to creating a PRD. Then, we go into the implementation. And our goal here is to delegate all coding to the coding agent. And then, we do the validation after.

**[0:23:49]** And so I'm going to cover really quickly what this process looks like. Then we're going to go through it in action. And so first of all, when we are in our planning, we have two layers of planning. We have the top level project planning. That is what we already did

**[0:24:02]** creating our PRD and our rules. And now we have the taskspecific planning. So like I just mentioned, these are pretty similar. Creating a structure plan is pretty similar to creating our structured PRD. The main difference is the structure plan is just very focused on an individual feature and all of the

**[0:24:22]** tasks that come with that. So now we're getting down to the code. We're not as high level, but we are still going to start with a very unstructured conversation. I like to call it vibe planning where we're just going to explore general ideas. What's the architecture for what we're building

**[0:24:37]** specifically? Spinning off sub agents for codebase analysis and documentation. and then just figuring out like what are the specific tasks that we need to knock out for this feature. And so we have this conversation. I'll show you an example of this. And then we turn that into a structured document just like

**[0:24:54]** with the PRD. So the goal here is to create a detailed plan of attack for the AI coding assistant based on our conversation. So the conversation is a part of our context. But here we have very specific sections that I want to create in the structure plan. the goal

**[0:25:11]** and success criteria of this feature, any documentation that we want to reference that maybe one of the sub agents found, our task list, which can be as specific as even the individual files that we want to create and update. And then probably the most important part out of this entire plan is the

**[0:25:26]** validation strategy. This is kind of like test-driven development where we want to be very specific with how we can validate the feature before we even write a single line of code. This forces both us and the coding agent to be very specific about the success criteria and so we create our structure plan and we

**[0:25:45]** are very much a part of this but then we delegate all of the coding to the agent itself. This is not vibe coding though the only reason that I'm going to trust the agent but verify is because I am sandwiching the implementation with the planning and the validation that I am

**[0:26:01]** very much a part of the process for. And so we are going to have the coding agent check its own work with unit testing, integration testing, and end toend testing. We'll see that as well. But then I am going to run my own code review and manually test the

**[0:26:14]** application. I'll spin it up myself. I'll go through the application just like a user would. Make sure that everything is working good before I make that commit and send it off to production or staging or whatever. The important thing here is that in between the planning and the implementation, I

**[0:26:29]** am going to be resetting the context. This is one of the golden rules. Context is very precious. And so I have a long and detailed conversation figuring out this feature we're going to implement. And then the structured plan that I create right here, I want it to be all

**[0:26:46]** of the context the coding agent needs to get the job done so that I can have a fresh conversation where the plan is the only thing I send in because it has all the documentation to reference. It has the entire task list. So we know what we have to do. We know how to validate. So

**[0:27:01]** that way we can just cut things off and go into execution to keep things very focused, right? We want to not have a bunch of context bloating the conversation when we get into writing the actual code. All right, so with that, let's now get into our first piv

**[0:27:16]** loop. And this is going to be a lot simpler than you would think because we really are going to reap the rewards from all of the planning that we did up front. We are on the same page with our coding agent. we're confident, understands what we want to build. And

**[0:27:28]** so there's not even that much planning we're going to have to do for each of these phases, at least at first. And so going back here, we finished the prime. We are on the same page of the coding agent. And I just gave a really simple prompt here, like, yeah, phase one looks

**[0:27:41]** good. Just confirm to me exactly everything that we're going to build. Now, usually for piv loops, after the first one, it's a bit more detailed, like let's look at the codebase and figure out how exactly we're going to build this. But right here, it's really simple. So this looks good. And now

**[0:27:54]** remember commandify everything. I want to turn this conversation and this idea of phase one into a structured plan with a task list and validation. So I have another command for that. It is just called create or plan feature /pl feature. There we go. So I'll send this in. And now plan feature just like the

**[0:28:12]** create PRD it has this idea of a structure plan built in. So I'll show you this command as well. So plan feature open this up. So it accepts an optional argument where I can specify what I want to build. In this case, I just using the conversation history. So

**[0:28:28]** it already knew. But we go through a phased process here. So feature understanding, diving into the codebase, which is again more applicable for future piv loops. But it does a lot of research, pulling relevant documentation, making sure we have a a rich set of context going into the

**[0:28:43]** execution. And then what you're looking at here, this is the template. So we want to describe the problem statement, any context or reference. We have our implementation plan with the task list right here. And then of course we have our testing strategy. We want to define the validation up front. And after we

**[0:29:01]** create this plan, of course, we're going to validate it. We're going to make sure that we're very specific. The step by step here's exactly how we want you to validate the application. And I am actually using the Verscell agent browser CLI skill, which I made a video on that I'll link to right here. So

**[0:29:17]** we're going to build in full browser automation. The agent is going to spin up the backend and front end, run the database migrations, go through and like build its own link tree and basically just make sure everything is working exactly how a user would use the application. So pretty exciting. The

**[0:29:32]** validation is going to be very detailed here so that by the time control is passed back to us, we can be very confident in the implementation. Still doing validation ourself, but it's going to be a lot less work. Okay. And our plan is created now. So let's go ahead

**[0:29:46]** and take a look. So, I did a bit of validation off camerara. I'll show you that in a little bit. Usually, you will iterate a good amount because you want to make sure that it's understanding of phase one is aligned with what you have in the PRD, what you actually want to

**[0:29:58]** build. Go through all of the sections. I encourage you to do so. So, here's our implementation plan with the task list. It's very detailed, which is good. We want to be specific now that we are very focused on a single feature. We have our validation with the whole validation

**[0:30:11]** pyramid as I like to call it. So, type checking and linting and unit testing. And then we're very specific for the endto-end testing, all the user journeys we want the agent to go through so we can be confident in the implementation when it comes back to us. And that's

**[0:30:24]** something it didn't really do that well at first. And so I did have a follow-up prompt here just to give you a quick example of how we can iterate and refine the plan before we send it off to implementation. And then one other little golden nugget. I promise we'll

**[0:30:38]** get into implementation in a sec, but this is really important. Generally, coding agents aren't the best at working with environment variables. they'll get tripped up if you don't have the environment variable set before implementation. It'll just do a bunch of mock testing and say everything's validated when it isn't actually. It's

**[0:30:54]** really frustrating. And so, usually what I like to do in parallel with the planning is I will create av.example. And I'll have it look here so it knows all the environment variables that I have set. And then I will set up my environment variables as well. So, obviously I won't show this file because

**[0:31:11]** it has my secrets for the database URL and things like that. But because I already have that set up now, it can rip through the entire implementation and then not just write the code, but it can run the database migration, start up the back end and front end, use the Verscell

**[0:31:25]** agent browser CLI to test everything, and it doesn't have to get interrupted for me to set my environment variables. And so I have this stage set up perfectly now going into implementation. And I'm pretty happy with this plan. So now remember context reset because context is precious. I am now in a brand

**[0:31:42]** new context window where I will use my execute command and the one parameter is the plan that I'm pointing it to. This is all it needs for its context now. And so what I'll do is I'll pause and come back once it's gone through the entire thing. And really we are delegating all

**[0:31:58]** the coding to the agent now reaping the rewards of all the effort we put into planning. Every single piv loop app through this point is going to be so fast now because of the work that we put into this. All right, our implementation is complete. We can see from the

**[0:32:10]** screenshots that it did full end toend testing. So, we can be pretty confident in the implementation because the agent already took care of everything right here. But, it's still important for us to do the human validation so we can really make sure that we are trusting but verifying. And so, the code review

**[0:32:26]** that gets pretty in the weeds. So, I'm not going to do this right now, but if you're more technical, it's definitely important that you do so. But what I am going to do is test the application live with you. So, the only thing I did off camera is I created an account already

**[0:32:39]** just to make sure that the basic authentication is working, but I haven't done anything here yet. And take a look at this. This is so cool. It already looks really, really nice. So, I can set my display name. I can do a bio like a cool AI builder. All right. I can set my

**[0:32:52]** avatar URL. So, I just uploaded a image to im. So, okay, that's looking really nice as well. I can add some links like, okay, I'll do YouTube and then that's https youtube.com/collemine. All right, looking nice. Add another link. I'll do LinkedIn. I don't have my LinkedIn URL right now, so I'll just do

**[0:33:10]** like LinkedIn.com. Don't really care. All right, cool. And let me just add one more. I'll do X. All right, so uh let's just do X.com. Very cool. And I can drag these around to reorder them and it's automatically reflected here. I can view just the editor and then adjust the

**[0:33:25]** preview. The theme doesn't look the best right now. Like it's just white, but I think that comes in a later phase anyway because right now we are just building the foundation. So, a lot of this isn't perfect yet, but it's still looking extremely good for a starting point. And

**[0:33:37]** then I can click save. And um okay, has to load the API endpoint. So, running this local host. There we go. Change is saved successfully. So, I can do a refresh and everything is still going to be there. All right. That's amazing. So, this is looking really, really good.

**[0:33:51]** Now, what I want to talk about since we've gotten to a good foundation built is the commit message just really quickly here. And so, I have another command called /commit. And this one's really, really basic. You can make this more detailed if you want, but essentially you just want to provide

**[0:34:05]** instructions to the agent for how to create a git message because we are going to use that as our long-term memory. So going back to the diagram here, this is one of those golden rules. Your commit history is your long-term memory. So if we are standardizing our message and that's why we're using a

**[0:34:21]** command/comit to make this reusable then our agent when it's going through the prime it can look at the git log to see a history of what we built recently which will guide what comes next and maybe patterns that we want it to follow. And so that's the power of this

**[0:34:36]** commit message right here. So I'll do slash commit which I could just run get commit myself. It's really really easy but this just makes it so it's always the same kind of message for consistency. So in this case there's nothing to commit because I already ran this off camera as well. But that is

**[0:34:51]** important to take care of after every single implementation. Now one other super important thing to cover after we have the foundation of our project laid out is we want to set up a framework for regression testing. We want to make sure that as we go through future piv loops,

**[0:35:07]** so we go through this process over and over again for all the features we want to build, we need to make sure the old stuff doesn't break. And so this I'm going to cover more in a different video. All the strategies that I have for implementing this sort of testing

**[0:35:21]** harness yourself because essentially you go into the agent, you say like, okay, what we have now is great, but I could also go into AquaVoice here and say, I want you to list out all of the endto-end testing that you did. Put this into a command for me so I can run this

**[0:35:36]** later after I build other features so that we can make sure that everything that we built previously is still working, right? something kind of like that. Again, I'm not going to get too in the weeds of this right now. It takes a while to set this up and kind of create

**[0:35:49]** a test harness, but this is how you make sure that your application is stable as you're continuing to build on top of it. And it does take a lot of work to create and maintain this cuz you constantly have to update it. And so, there are also solutions out there that take care

**[0:36:03]** of this for you and they are very powerful. And one of these applications is QA tech. They have AI testing agents that evolve. They adapt with your codebase. So, as you're adding more and more features, they add more and more test cases to make sure that everything your application is working well as

**[0:36:19]** you're continuing to build it out. And so, I'll show you an example of this really quickly. It's so easy to get started. So, you go into QA Tech, they got a free tier for you to get started and try this out. I'll create a project here. And then you just have to paste in

**[0:36:32]** a URL that you want to test. And so, I took this application, since I already made a commit and push it to GitHub, I deployed it in just like a minute to Versell. So, the easiest place to host your sites for free, especially when you build with Nex.js. And so, I'm going to

**[0:36:45]** go to my project here and just paste in this URL. And so, it'll take a little bit to create your project and analyze your codebase. And what we can do is just say, I want a good test setup for my site. Help me create the first three to five test cases. And this is kind of

**[0:36:58]** like, you know, bolt.new or lovable or you can just give a prompt for whatever you want it to do to set up the test suite for your project. But this is what they recommend to get started. So, I'm going to go ahead and send this in. And it's so cool because it will dig through

**[0:37:11]** your website like actually crawl through it. I believe they use playright under the hood, but you don't have to manage the infrastructure at all. So it analyzes your website and comes up with the test cases. And so I'll come back once it has done that. So mid execution

**[0:37:23]** just want to show you really quick that it crawled my website in just a couple of minutes. And then one of the really important things is we need a way to log into our website. We want the automation to be able to do that. And so they have

**[0:37:32]** a way for us to enter in our username and password. And then they're going to store it in a secure way. Okay, so I just have a test account created here. Going to go ahead and save that. And then it'll use that to get into the website, really dig in and understand

**[0:37:44]** all of the user journeys that we want to test here. And there we go. Ed has generated a bunch of test cases for us. And we can even click into each one of these. And we can see the exact flow that it went through. And so now we have

**[0:37:56]** all these tests that are set up. And the AI testing agents in QA tech are going to evolve these test cases over time to make sure it continues to cover everything in our codebase as we build more and more features. It is super super cool. And again, we can build our

**[0:38:11]** own kind of command system to do something like this. But I really appreciate having a platform that just takes care of all of this for me. And there's agents under the hood that I can chat with to even just like work with the testing here and make sure that I am

**[0:38:23]** truly regression testing everything. And so then whenever there's anything that breaks I can come in here and say like hey there's a bug with the application right now create a test that should be failing let me address the problem and then the test should be passing and so

**[0:38:37]** that takes us to the last golden rule that I have here the system evolution mindset. So whenever we encounter a bug in our codebase it is important to not just address the bug but think about what we can fix in our AI layer so it doesn't happen again. Like maybe we need

**[0:38:54]** to be more specific about our style guide in our rules or create a new on demand context for that. Maybe we need to have more endto-end testing that's laid out in our commands, our workflows, whatever it takes to make sure that we don't encounter this issue again. And

**[0:39:08]** then we can also do what I just showed in QA or our own command system where we add a test to make sure that we don't encounter that issue again in the codebase. And so the power of this, even though it takes time to do it, is that

**[0:39:20]** we make our coding agent more reliable and repeatable over time, evolving it along with our codebase. And so we're doing three things in parallel. As we are building out our codebase, we are evolving our test base, our codebase, and our AI layer. And man, does that compound over time. And so going back to

**[0:39:37]** Cloud Code here, I'll just give you a really simple example of this. So one thing that I did do to iterate once off camerara is I worked on the style for the site. cuz if you go back to the start of the video, you'll see that I kind of forgot to talk about the style,

**[0:39:50]** exactly how I wanted the site to look. So, Claude Code just kind of made its own assumptions there and it didn't look the best. And so, I had to iterate on that. And so, one thing that I can do here is, you know, at first I didn't like the style that you implemented for

**[0:40:02]** the front end. We definitely don't have enough in the AI layer with our rules and on demand context for a style guideline. So, I want you to do some meta reasoning here. Don't change anything, but help me think about right now. what could we change with our rules

**[0:40:16]** or on demand context? Something we could add or update so that we have more consistent styles that we're going to be building as we continue to, you know, build out the analytics and other things, other pages in this application. And so the important thing I'm doing here is telling it to not change

**[0:40:31]** anything yet because usually I want to have a lot more control over changing the AI layer versus for the codebase, I just want to delegate as much of that to the agent as possible. So I have it reason with me, but I usually like to make these small and very focused

**[0:40:44]** changes myself. And you can see here that it recommends creating a style.md in the reference folder. So a third piece of on demand context for us. And so this I guess would go along with the components.mmd. That's more like here's how we should lay out things. And the

**[0:40:58]** styles.md is here's how it works. Here's how we should work with Tailwind CSS and probably shad CN for example. So, I'm not going to go through the full implementation of this and correcting everything, but just trying to give you a good example here of how when we encounter anything where we have bugs in

**[0:41:11]** the code or just isn't quite aligned with us like we have right here, it's always an opportunity for us to evolve the AI layer. And so, we're more and more in tune with our coding agent for this specific project as we continue to build it out. And that, my friend, is

**[0:41:24]** the most high lever part of the entire process, really saving the best for the end. So, that is everything. It really is a dead simple process for getting reliable and repeatable results with your coding agents when you are starting new projects because now after the system evolution, we just take it back

**[0:41:40]** up to the top and we go through more piv loops going through the exact same process to build out all the phases in our PRD, add any other features, whatever it takes to get to that minimum viable product. And then that'll take us into brownfield development with one of

**[0:41:52]** the next videos that I'll put out on my channel. And so if this all sounds good to you and you want to dive even deeper with my full resource library of commands and rules, you want to see what system evolution really looks like and get deep into that, definitely check out

**[0:42:06]** the Agentic coding course that I have in the Dynamis community. I'll have a link to this in the description and the pinned comment. And so that's everything that I got for you right now. So if you appreciated this video, you're looking forward to more things on Agenta coding

**[0:42:19]** that brownfield development video, I'd really appreciate a like and a subscribe. And with that, I will see you in the next
