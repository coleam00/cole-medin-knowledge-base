---
type: raw-transcript
title: "Introducing Archon - The Revolutionary Operating System for AI Coding"
youtube_id: 8pRc_s2VQIo
url: https://www.youtube.com/watch?v=8pRc_s2VQIo
slug: introducing-archon-the-revolutionary-operating-system-for-ai-coding
published: 2025-08-13
duration: "0:28:46"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Earlier this year, I introduced you to Archon, my open source tool as the world's first agent, an AI agent that builds other AI agents. But as I was creating Archon and getting feedback from all of you, I realized that there was so much more that I could be doing

**[0:00:15]** with Archon. And so, behind the scenes, the past few months, me and a few other guys from the Dynamis community have been shaping this new vision and platform for Archon. And I'm super excited to bring you the beta launch of that. Right now, we are turning Archon into the operating system for AI coding

**[0:00:33]** assistance. It's super exciting. I'll explain in this video what that means and how you can get started with Archon yourself today. Now, listen up because there are some big problems for AI coding assistance that Archon is aiming to solve. As powerful as they are, AI coding assistants almost completely lack

**[0:00:48]** two of the most important components of context engineering. I'm talking about rag for our knowledge and documentation and project management tools like cloud code and curo. All they have is basic web search and internal task management tools that we can hardly interact with. And so I built archon to solve this and

**[0:01:06]** completely revolutionize the way that we use AI coding assistants today. And I'm releasing it as an open-source beta tool that gives you a full command center to work with your coding assistants and collaborate with them at a much deeper level. Buckle up because in this video I'm going to give you a demo of Archon.

**[0:01:23]** I'll show you how you can start using it yourself today. And we'll even have a conversation with one of the other maintainers from the Dynamis community, Shawn Buck. We'll dive into the future of Archon and our vision for it and how it relates to context engineering and all the other stuff that I've been

**[0:01:37]** covering on my channel recently. And I mean this sincerely. If you are not hooked on using Archon for all your AI coding after watching this video, then I'm just simply not doing my job conveying the power of this operating system to you. So, here is the GitHub repository for Archon, which I will of

**[0:01:54]** course have linked in the description below. And I'm actually using the original repository for Archon because it's very much an evolution of what I was doing before. So, I just replaced it with everything that we have here with the new operating system for AI coding. So with the new archon, it is a command

**[0:02:10]** center for AI coding assistants. So for us, it's a sleek interface to manage the knowledge, context, and tasks for our projects. And then for the coding assistant to collaborate on the same things, it's an MCP server. That's the beauty of it. The UI is native to humans. MCP is native to the LLM. So we

**[0:02:29]** each have our way to collaborate on the same projects together. And then I'll also in my demo cover all the different components that we have to archon like the documentation and rag task management all that good stuff. And the other thing that I'll say here is that my demo in this video is just to get you

**[0:02:44]** started on what's possible with Archon. If you really want to dive deep with me, definitely come to the Archon beta launchparty live stream happening this Saturday, the 16th at 9:00 a.m. Central time. I'll actually build something end to end using Archon to power my knowledge retrieval and task management.

**[0:03:01]** and it's going to be a good time. So definitely be there for that live stream. And one of the things that we've worked so hard on with Archon is making it easy for you to get started. So if you scroll down in the read me here or you just jump to the quick start, we've

**[0:03:14]** got a very simple guide to get Archon up and running. So just a couple of prerequisites that we have here. Docker desktop, you need a Superbase account for the database that manages everything under the hood. And then also an OpenAI API key for your LLMs and embedding models. And then also we support Gemini

**[0:03:29]** and Olama. You can run everything completely locally with Olama with your own private knowledge base and MCP server if you want to do so. And so for the setup instructions here, you just simply have to clone this repository in a terminal. Go into the directory here and then you have to configure your

**[0:03:45]** database and your environment variables. And so I'll pull up my repo right now just so I can show you an example of this. You have your example. You'll just copy it, rename it to and then fill out your Superbase URL and Superbase service ro key. And those are the only required

**[0:04:00]** environment variables to start. And then we can dive into our database setup. And so I'll show you this within Superbase and your Superbase project. You just have to go to the SQL editor. That's this tab right here. This is going to work both for local and hosted Superbase. So like I said, you can do

**[0:04:15]** everything 100% local if you want to host Olama and Superbase. So you just go into the SQL editor and you paste in the content that I have within this file in the repository. So this gives you all the SQL to create all the tables that Archon uses under the hood to store your

**[0:04:30]** knowledge, your projects, and your tasks. And then going back here, the only other thing we have to do is use Docker to spin up all of our containers. You just copy this command, go into your terminal here. I'll just pull this up and show you and run this command to

**[0:04:43]** build the Archon MCP server, the backend, and the user interface that we use to work with our coding assistant. So here are the default ports that everything runs on. You can configure this as well and there's more instructions on that at the bottom of the readme. So the first thing we can do

**[0:04:58]** is just go to localhost 3737. That's going to bring us to this page right here where we can start configuring archon. We can crawl the knowledge, set up the MCP server. That's what I'm going to walk you through right now. So when you first go into Archon, the first

**[0:05:11]** thing that you want to do is configure your settings. So that's the bottom tab right here. We're also working on an onboarding flow that'll walk you through some of this because you need to set your API key for Google or OpenAI. Or if you select Olama, which is in progress

**[0:05:24]** right now. We're working on this because Archon is in beta. Then you don't have to set an API key at all. And then we can also copy our IDE global rules. And so we have global rules crafted for you to guide your AI coding assistant on how to leverage archon effectively. And you

**[0:05:40]** can definitely customize these as well. And so right now these are the ones that we have for cursor wind surf and cloud code. We're also working on generalizing this to make it so it'll apply no matter your AI coding assistant. You can definitely just take one of these and

**[0:05:51]** use it for something else like hero or augment code if you want as well. So you can just copy these rules and then add them along with your other existing global rules. You can just tack this on to whatever you're already using with your AI coding assistant. And then

**[0:06:05]** there's a lot of other different settings that I'll probably talk about more in the live stream. I don't want to get into right now, but you're it's very configurable. It's customizable to you. And that's one of the things that makes Archon better than something like Context 7 because this is your own

**[0:06:18]** private knowledge base. You get to manage the strategies for Rag and the way that we're extracting code examples and things like that. So, you're very much building your own configurable private knowledge base, which that's actually the next thing that I want to cover here in the knowledgebased tab.

**[0:06:32]** When you add your knowledge with this button in the top right, there's a lot of different options that we have here for the different knowledge sources that you can add. And then your coding assistant through the MCP server can perform rag to search through all of this documentation and business

**[0:06:46]** knowledge. And so I can give it a URL to scrape. Like for example, I can have it scrape the LLM's full.ext for pyantic AI. So any kind of website, sitemaps, llms.ext, just full websites that it'll crawl through recursively. You can give it all these different kinds of URLs

**[0:07:02]** just like I had in the crawl for AAI rag MCP server that I've been building on my channel. I'm incorporating all these things into Archon just like I said I would. And you can also upload your own documents as well. If you want to upload business documents like PDFs that will

**[0:07:15]** guide the AI coding process, you can do that. And it's going to chunk those up and embed those, put them in the knowledge base for rag just like the technical URLs for things like library documentation. And I'll actually show you what this looks like in real time here. Like if I just recrawl one of

**[0:07:30]** these, like for example, I've got the documentation for Pantic AI, mezzero, langraph, and then cloud code. And I can rec crawl one of these. I'll show you just how beautiful this looks. It's so cool. We have real-time feedback from the API through these websockets that we have set up that'll give us the status

**[0:07:45]** of our crawling. So in this case, it takes that first URL and it actually using crawl for under the hood. It recursively goes through, finds all the different URLs to navigate through to give us the full documentation. So it found 44 in total. Now it's crawling through all of those in batches of five.

**[0:08:01]** And then after it does that, it'll go through the embedding and chunking process, getting everything ready for rag in our Superbase knowledge base. And so I don't need to show the full process right here. I definitely encourage you to play around with Archon yourself. Like there's anything that I'm not

**[0:08:15]** showing here that you're curious about, try it yourself. It's so easy to get started like I showed you. And like I said, I really hope that it just blows your mind. And so once you have your knowledge set up, then you can connect your MCP server. So you go to the MCP

**[0:08:29]** server tab and here you can see the logs for your server on the top. You can stop your server and restart it if you're doing things like changing your environment variables. So I'll go ahead and start it again. Super easy to manage the MCP. And then we have tabs here to

**[0:08:43]** instruct you on how based on your AI coding assistant to connect to the Archon MCP server. And we're working on expanding this as well to cover different coding assistants like hero and augment code and client. So like winds surf cursor cloud code. I can click on cloud code because that's the

**[0:08:57]** one that I'm going to be using in my demo here and we got super simple instructions. So we just take the cloud MCP add command, copy this, and I'll use that in a little bit. But the other thing I want to show you first is the project management tab. This is where we

**[0:09:11]** have task management for our AI coding assistants. And I'll show you one of the other projects where I'm actually like in progress here. And the beauty of this is that the connection that we have here with us and the UI and the coding assistant and the MCP server, it is real

**[0:09:25]** time. So while the coding assistant is running, we can correct things. We can edit the description of a task. We can move something back into the backlog and describe why. And the coding assistant will have that reflected immediately when it reads the task the next time. And as it is doing things, we also get

**[0:09:40]** to see things get populated and moved around in the UI in real time. And that really helps us project manage it, really have that deeper level of collaboration. like I was saying. And so let's actually just see this in action. I've got a new project created for an AI

**[0:09:53]** news agent for the demo that I'm going to give you here. So we'll go to the MCP tab. I'll go to cloud code. I'll copy this command here to add the server. I'll paste this into my terminal here that I have running in my IDE. I already have it added, but otherwise it would

**[0:10:06]** add it for the first time. I can do cloudm list, which will actually test our connection to archon as well. Looking really good. And so what I'm demoing here, this is an agent that I actually built in the Dynamis community for one of our workshops. So it's a

**[0:10:18]** langraph in Padantic AI agentic workflow that we have here based off of a prototype that I have in NAND. So I went through the full PRP process which I'll link to a video right here if you're curious to dive into this more. So I described initially what I want. I used

**[0:10:32]** my execute PRP command to generate this PRP which is the full spec for what we want to build. And so I'm going to be using this plus task management and rag with archon to build the complete thing. So I'll go into claude and then I'll paste in the command to execute this

**[0:10:49]** PRP. So I'll go ahead and kick this off. And then also for demonstration purposes in the PRP, I'm telling it to use the existing project in archon and create the tasks for the project and perform rag early on just so for our demo purposes we can see that happen right

**[0:11:04]** away so I can show you Archon in action. So I'll pull up archon again. I'll go back to the project management tab and then within our news agent here we can see the tasks start to get populated. Right now it's listing the projects that we have in Archon. So it's using the MCP

**[0:11:18]** server and then in a second it's going to start creating some tasks. So it finds that we have nothing here. We're starting the project from scratch. So there we go. It's going to do some rag research and then start populating our tasks. And so I have the knowledge for

**[0:11:32]** podantic langraph already crawled like I showed you in the knowledge tab. So now it's performing those queries to get that information to enhance its code generations. So there we go. We got 129 results. I can do control-R to expand this. We can see the different chunks that it retrieved from this retrieval.

**[0:11:48]** And it's going to look at code examples as well. There's a couple of different things. Yep, there we go. Searching for code examples. There's a couple different functions that we give it for more agentic rag to search through our knowledge base in different ways. And there's a lot of strategies for rag that

**[0:12:00]** I have built into this under the hood. And so yeah, I'll pause and come back once it gets more to the task management side of things. All right, so there we go. It created its first task right here to update the graph state. And I didn't even have to refresh my page. It's all

**[0:12:12]** in real time thanks to the websockets that we have here. And there's another task popping up. The websockets that we have here between the MCP server and our user interface. It is such a beautiful thing. So it's starting to just there we go. Create all the tasks that we have

**[0:12:24]** here. And then it's going to knock them out one by one slowly moving them into in process and then in review, moving on to the next one. And like I said, we can update these descriptions and things in real time, add our own tasks, and it's going to automatically incorporate those

**[0:12:37]** things without us even having to interrupt Claude code or your coding assistant. That is the beauty of it because a lot of times when you interrupt a coding assistant, it causes a lot of problems. It starts to hallucinate because you cut it off in the middle of thinking and when you

**[0:12:50]** resume it with another set of instructions, it's not really in its natural flow. And so if I update the task in my interface, then it's going to pick up those changes when it comes time to actually get to that task. And so we're collaborating in a much better way

**[0:13:04]** than just doing an escape or a double escape here, typing in wherever we want it to fix, and then having it try to pick up where it left off and incorporate that when it makes sense. So I hope you can kind of see like why this matters so much that we're able to work

**[0:13:16]** with the coding assistant in a UI and allow it to be a lot more flexible in the way that it takes in our feedback when the time is right. And so yeah, that's what I wanted to show for Archon right now. I'm obviously not going to walk through the full end to end because

**[0:13:29]** I wanted to keep this simple and definitely come to the live stream if you want to see me like actually use this to completion. But yeah, that's everything that I wanted to show for Archon right here. Next up, we have a word from our sponsor, which sponsors are how I'm able to do these things like

**[0:13:44]** Archon for free for you. Then we'll get into the conversation with Shawn and talk more about the vision behind Archon and the future of it. Now, we've been talking a lot about Cloud Code in this video, and it is my favorite AI coding assistant, but when it comes to building

**[0:13:58]** front-end applications, I still rely a lot on AI powered app builders like Lovable or Bolt. New. And that brings us to the sponsor of today's video, which is Hostinger, and specifically their Hostinger Horizon's platform. It's a new player in the AI app building space that's been on my radar recently, and

**[0:14:16]** it's really started to impress me. And what sets Horizon apart is Hostinger is already your platform for your professional email, your domain, and your website hosting. So now you just have everything under one umbrella, including with Horizon now, this beautiful new platform for building our frontends. And it's just like other AI

**[0:14:32]** app builders where you describe in plain English what you want. Like here, I'm having it create a website for my Dynamus AI mastery community. And then boom, after a couple of minutes, we have this beautiful UI created for us, ready to iterate on and even host. And I

**[0:14:45]** actually took the same prompt and I compared it with lovable and with bolt new and I definitely think that Horizon's won here. Plus, we can edit the code directly if we want to work more alongside the coding assistant. They have integrations with superbase and with e-commerce. You can build an

**[0:15:00]** online store super easily in Hostinger Horizons. And also, like I said, it's very easy to iterate as well. So, for example, if I want to take this button and make it actually work, I can just send in this prompt to have the join buttons go to my website. And there we

**[0:15:14]** go. 30 seconds later, these links now work absolutely beautiful. And I can publish in a single click because I'm integrated directly within Hostinger with their domain and website hosting. And I can even use my own custom domains like I'm doing right here. So I have everything hosted on Hostinger built

**[0:15:30]** with Hostinger Horizons. And getting started could not be easier. I have a link in the description below. And also when you use my discount code, you get 10% off your plan. And I'm just showing you right here really quickly how you can apply my discount code, which I also

**[0:15:44]** have in the description. Super super easy. And yearly plans of Horizons also get free hosting and a free domain. And so if you've had that app that you've wanted to build for a while now and you just haven't found the tool to use it, definitely check out Hostinger Horizons.

**[0:15:59]** All right, we have the man himself, Shawn here. And there have been a lot of amazing people that I've met in the Dynamis community the past few months, and Shawn is definitely one of them. So, he was super interested in Archon towards its inception and he wanted to

**[0:16:13]** get involved and contribute to a much larger vision that he brought to me. Um, Sean is it's he's a visionary and he's got incredible ideas, a lot of which you've already seen in the last 5 to 10 minutes in this video here and he's going to dive into more. Um, and so

**[0:16:28]** yeah, it was just like this immediate connection that we made um, with the vision for Archon because I'm more of like the technical person building out the back end like you guys have seen with the first version of Archon and the crawl for AAI rag MCP and then Sean has

**[0:16:41]** the vision for the UI and the UX and like really building this into a beautiful user experience as we're building this operating system for AI coding assistance and and what you're looking at right here. So Sean, why don't you go ahead and tell us how you got interested in Archon initially, what

**[0:16:55]** got you involved, and how you've gotten to where we are now. Thanks, Cole. So, um, yeah, it's it's exciting to be here. I'm a huge fan of obviously the Dynamus community being a part of it. Um, and you know, I came across I'm a business owner and I

**[0:17:11]** started getting interested in AI. How is this going to impact my business? Um, I used to do development in the past and I used to be in the IT field. Uh, but being an entrepreneur and a business owner, I needed to figure this out. And I came across your channel, oh, probably

**[0:17:25]** almost a year ago now, really in the early stages. And I I there's a lot of great content creators out there. But what attracted me was your view of first order principles and learning things the right way. And so I immediately signed up for Dynamis Community, but what I

**[0:17:38]** didn't expect was all the amazing people I'd meet. I've met with other business owners. We're working on projects together. It's been a lot of fun. But that Archon video of your original Archon video really captured me and and then crawl for AI and what it was doing on the back end. And I was like, man, if

**[0:17:53]** we just had a really good user interface that could see what's going on the back end, people will see how cool what you're building is. So this is all a testament to what you built and um I just hope to contribute to it and encourage more people to contribute

**[0:18:06]** because this is what we need. We need people contributing together to build tools to help us. So that's how I got interested. Awesome. Yeah, I appreciate it, Sean. And this definitely is a tool to help everyone. Like literally, no matter what you are using AI coding assistance to

**[0:18:18]** help create, this is like the backbone now for things like the task management and the knowledge that I've shown you all in this video already. Like this is useful no matter what you want to build. And the other thing I want to say is if you want to get involved in Archon, you

**[0:18:32]** can do so today. Like it's super easy to get started. I've got the repo linked below. And also, I've got the Archon Beta launch party live stream this Saturday, the 16th at 9:00 a.m. Central time. So, I'm going to call it out a few times throughout this video because I

**[0:18:46]** really want to see you there. So, definitely be there for the launch of Archon. I'm going to dive a lot deeper into using it in action throughout the stream as well. But with that being said, I want to dive more into the vision for Archon now. So, we've

**[0:18:59]** combined things together and I really want to hear from you, Sean, because everyone's already heard about my vision. what's your vision for Archon and what's led to everything that you've implemented here? Yeah, so thanks for that Cole and and and I think ultimately why Archon and there okay there's tons of coding

**[0:19:17]** assistants out there. There's Gemini, Clog Code, CL, all CLIs. There's there's VS Code branches, but how do I keep control of what everything's going on when I'm doing development? And what is consistent for me as I interact with my agents? And I want to from a user experience perspective, build more

**[0:19:38]** interactions with agents, not agents replacing humans, that they're co-pilots with us, that we're working together. And I really feel like a lot of people need to take user experience and user experience isn't just cool looking UIs like my Tron-like UI, but it's really honestly what you did with the crawling

**[0:19:54]** with everything working is also a part of user experience, but also visual elements to the user. The vision of Archon to me should be all things helping humans and coding assistants work together. Whether that's working on your project documents, whether that's working on your tasks, whether that's refining your process and the future

**[0:20:12]** with Dynamus Community, what people are building on to is really cool. Being able to see what your sub agents are doing. Um, again, this is really just about visibility and just if you've ever been in a point where you're like, I don't know where my codebase is at.

**[0:20:24]** There's document files all over the place. Claude created stuff everywhere. What task are you in on your internal to-dos? I don't know where you're at. And that was a frustrating Issa always had. So that's what we're trying to solve here. Um, real quick, you'll see that all of this is an element to help

**[0:20:42]** you interact with that more and give you visibility. Where are what what's going on? What's in process? What's been done? What do I need to review right now? You can easily kind of interact with this and be able to see the information and data. You can copy the task ID and put

**[0:20:58]** it into your MCP. And that's the beauty of this too is again the MCP is the interface for the agent. The UI is the you could use Archon, you know, without a UI if you want. You could you could have it go off and still do that with

**[0:21:10]** the MCP, but there's a power in you seeing the UI and and and being there. So if you want to work on your documents together, right, we built in the ability to uh whether you're having PRPs, you want to do mobile app development, we kind of have a nice looking view so you

**[0:21:25]** can interact with it, but even a markdown editor so you don't have to, you know, you can just kind of edit your markdown here. A lot of these cool things and experiences for you to play around with. Um, but your agent will create. It's really cool to see when I

**[0:21:40]** kick off a project and then all of a sudden it's like, "Oh, let me create the project at Archon and set all the tasks." And it puts it in there and I go look and I'm like, "Yeah, this plan looks good." It's so much easier for me to work with than seeing their to-do

**[0:21:51]** list. And this is how we interact with stuff with with combon boards and task boards. So, as you can see, I'm using Archon on a daily basis. And when it comes to user experience, I believe people should be users first. if you're not using your app like that's how you

**[0:22:05]** improve it. So hopefully uh everybody sees the little features and things that built in to make interaction a lot easier. But my projects are working here. I these are this is actually I'm about ready to deploy this uh to production once I finish testing. As you can see I'm in the testing phase. Um

**[0:22:22]** it's great. It's been extremely helpful for me. I hope it's helpful for you too. And I I would just really encourage people to contribute. uh what are your talents and skills and let's make Archon better together and then we all get to benefit from the use of it.

**[0:22:36]** Awesome. I love that Sean. Now, the next thing that I want to dive in with you, Sean, I think this is probably the most exciting is talking about the future of Archon, cuz I know especially you, I mean, myself, everyone else that's getting involved in the Dynamus community, like we all have our future

**[0:22:50]** vision for Archon, but especially you, Sean, you have so many incredible ideas that I've spent a good amount of time uh listening to you talk about because like they get me fired up, too. And so the first one that I want to spend some time hearing from you about is your ideas of

**[0:23:04]** how we can integrate a lot of the things we've been doing with context engineering and like the PRP framework, how we can integrate that into Archon. Exactly. So, um, as we saw in some of the demo before, things like the documents, there's a user interface there, but being able to start to layer

**[0:23:19]** on more context in the future, like being able to define what your processes are, what agents you want to do in certain checkpoints in a very visual way that could be then sent to sub aents or whatever system, but I like to see things visually. Cloud sub aents have

**[0:23:34]** been great, but reading a bunch of markdown documents is I don't know which step goes next and I get confused in those processes sometimes and sometimes it kicks off an agent and it wasn't what I wanted. But I I'm envisioning a cool view where you can see like a network

**[0:23:49]** chart where they're working and you can see who's doing what. Um we we've got some cool people in the Dynamus community doing stuff with multiple being able to do local models and and do local models in parallel. Um, there's a ton of stuff going on to really help

**[0:24:05]** with context, but I look at context from a couple different perspectives. You have sort of your end goal of what you're trying to achieve. That's sort of your business context, right? Then you have the project context for what you're trying to do here, but you also have technical context, business knowledge

**[0:24:22]** context. The agents need context for how they're supposed to operate, like a development team. Um, and all context goes many many many levels. It's not just rag, right? Rag helps with context, but to me context is just keeping everybody on the same page. A lot coming with that. There's a lot of cool people

**[0:24:39]** doing things with subs. And again, our goal is to not replace those frameworks, but give you visibility to all those frameworks and and have a central command center where you can see what's going on. Yeah. And that's where I'm excited about all the and and and if people want to

**[0:24:54]** contribute also, you could contribute on the public side. But if the Dynamus community, we're talking about a lot of cool stuff. A lot of if if this is if you want to be innovative and you want to see the next trends or you have a really good idea, come join us. We're

**[0:25:06]** open to all of this stuff publicly and in Dynamus. Yeah, definitely. I appreciate that a lot, Sean. And the really cool thing with archon is that like you said Sean, it's not a replacement for these different strategies like the PRP framework or spectrum and development or the BMAD method. It's actually congruent

**[0:25:23]** with those things and we want to build some of those processes within archon so it's easier to manage your context as you're doing those different strategies, whatever works best for you. Um, and then the other thing that I I really want to hone in on with you, Sean, that

**[0:25:36]** you've been talking about already is the whole idea of sub agents. So tell me more about like how you envision being able to manage sub agents within archon as the operating system. Yeah, so in my IT career I had a long I was a consultant with agile and helping

**[0:25:50]** teams and development teams work better together. And I see agents just like teams people reviewing different work. In fact with sub agents I see the same hallucinations actually happen with humans in corporate world that I see in sub agents all the time because of lack of context. And with humans, it's a lot

**[0:26:09]** harder because someone you'll tell somebody, "Hey, do you understand what I mean?" And they'll be like, "Yeah, I understand what you mean, but they really they really don't." Well, Claude does the same thing, but it doesn't tell you, just like we have in the real world. So, with sub agents, being able

**[0:26:22]** to define them as roles and what they do and how they hand off to each one one of another and those interactions is the context that you need, not necessarily the technology on the back end. So being able to like have a character creator where you could say this is my agent,

**[0:26:37]** you always do this and then you upload like matrix style upload its knowledge library and now it it's it but then you could use any framework whether it's claude or your own langraph framework or anything to then these would just be the definitions of how they would work,

**[0:26:52]** right? I love that so much. So, as you can see, guys, like we have so many ideas to turn Archon into just an even more of a masterpiece. And I already think it it's at that point where like this it blew my mind when I first saw some of the things that you were

**[0:27:05]** building, Sean. And and a lot of people were really excited about some of the things that I was building at first with all the rag strategies. And so, we've got this all combined together. We're doing a ton of more incredible things with it. So, you're going to be seeing a

**[0:27:16]** lot more of Sean as he continues to be a huge part of Archon. And yeah, definitely come to the launch party that we got on Saturday. So big things to stay tuned for, big things to be excited about. So thank you Sean for for talking with me about Archon today.

**[0:27:29]** Thanks Cole. And just real quick, if anybody found what I have to talk about interesting from a business owner perspective, I am starting my own YouTube channel, putting myself out there. It'll be content about this type of stuff, building things in the real world and how I do stuff. Uh so come

**[0:27:44]** over. I'd love I'd love to get to know you. Yes, you guys definitely should. So thanks Sean. On to the rest of our video. So, if you've made it this far to the end of the video, you are definitely one of the people that I want to have

**[0:27:55]** involved in Archon. Not only do we make it really easy to use Archon, which I'd highly recommend you just try it out today and give us some feedback while we're in beta, but we also made it really easy to contribute and be a part of Archon. We put a lot of effort into

**[0:28:09]** organizing this repository in a really nice way. We have the GitHub discussions linked right here so you can be a part of the conversation. We also created a contributing guide. So you can read this just right here in the repo. It gives you tips on using coding assistance to

**[0:28:23]** help you build out features in Archon, how to submit PRs, really just all the resources that you need to contribute. And so please be a part of this incredible project that we're building here. And so if you appreciated this and you're looking forward to more things on Archon and trying it out yourself, I

**[0:28:38]** would really appreciate a like and a subscribe. And with that, I will see you and the Archon beta launch party live stream this
