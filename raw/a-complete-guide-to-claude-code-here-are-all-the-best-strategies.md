---
type: raw-transcript
title: "A Complete Guide to Claude Code - Here are ALL the Best Strategies"
youtube_id: amEUIuBKwvg
url: https://www.youtube.com/watch?v=amEUIuBKwvg
slug: a-complete-guide-to-claude-code-here-are-all-the-best-strategies
published: 2025-08-06
duration: "0:50:18"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have been addicted to Claude code the past couple of months. I live and breathe in this terminal. There's a reason why I've been covering it and context engineering so much on my channel recently. The things we can do with these tools and frameworks now is insane. I feel like I can build

**[0:00:16]** anything. But as much as I've been talking about it on my channel recently, I haven't actually covered a start to finish. Let's dive into all the features of Cloud Code and how we can make the most out of this beautiful coding assistant. So that is what I'm going to

**[0:00:29]** cover with you right now. We're going to talk about best practices, strategies, and tips for global rules and commands and agentic workflows and hooks and sub agents and parallel agents. I'm going to dive into it all with you. So even if you've used cloud code a lot before,

**[0:00:43]** you're still going to get a lot out of this. Also, I know that cloud code is not perfect. Anthropic's new rate limits, outages, the cost, and so as we go through these strategies, I'll also talk about how they apply to other AI coding assistants as well. for definitely not limited to cloud code,

**[0:01:00]** but it is the best of the best by far. And so, yeah, just a valuepacked guide for you today. Let's go ahead and dive right into what I've got for you. So, all of the tips and strategies that I've got for you today, I'm going to have in

**[0:01:12]** this readme, which I'm going to be adding into the context engineering GitHub repo that I've been building up recently. So, I'll have a link to this in the description so you can follow along with me implement all of these strategies as we go through them together. And so context engineering and

**[0:01:27]** the PRP framework, my big things recently. I'm going to cover that in this guide, but also some other things that I've never covered on my channel before that are really important for making the most out of cloud code. And so just to give you an overview of all

**[0:01:40]** the strategies we're going through today, I want to start with global rules with the cloud.MD files and best practices for using those. Then dive into permission management. We'll go into custom slash commands so we can set up these agentic workflows that we can run with a single command. Then we'll

**[0:01:55]** get into MCP servers and I've got a couple of big recommendations for this. Also a huge teaser for the overhaul for Archon. Archon version two which is going to be released next week. We got a beta launch for that. More on that in the middle of this video. So stay tuned

**[0:02:10]** for that. Then we'll get into context engineering with the PRP framework. I'll just give you a quick overview of this and how you can get started in a three-step process to have this full framework for context engineering that gives your AI coding assistants everything they need to build production

**[0:02:26]** ready software for you. Then we'll get into leveraging sub agents, one of the newer features to cloud code that's super super exciting. And then we'll also get into cloud code hooks so we can have these automations built into different parts of the development life cycle as we are using cloud code. Then

**[0:02:42]** after that we will go into the GitHub CLI integration. It's really amazing just how much Cloud Code can interate directly with GitHub doing things like managing issues and PRs in our repo and automatically creating PRs based on requests that we have for us. So we'll dive into that here even with a slash

**[0:03:00]** command to automatically fix GitHub issues. So it'll go out to GitHub, find an issue, make a fix for it, create a pull request. We'll see that in action. I'll also dive into what is called YOLO mode. So we can run cloud with dangerous permissions but do it in a safe way in

**[0:03:13]** containers. And then last but not least, I want to dive into parallel agent development. So we can have multiple instances of cloud code operating on different parts of our codebase or all attempting to implement the same feature at the exact time. So we have different options to choose from. And that'll wrap

**[0:03:31]** it up for everything that I want to cover with you today. So, I hope you can see from this that no matter how experienced you are with Cloud Code at this point, there are going to be some nuggets in here for you and maybe even completely revolutionizing the way that

**[0:03:43]** you use Cloud Code. All right, so I have a completely empty folder open up in my IDE except for the readme that has all of our strategies that I just copied over from the template that I have linked in the description. And even if you have never used or installed cloud

**[0:03:57]** code before, I've got you covered because I have their super simple installation steps at the top of the readme here, which for Mac and Linux, it's just a single command. They also added support for Windows recently, but I still have a better experience with the Linux subsystem within Windows. So

**[0:04:12]** I've got instructions for that here, just a couple of extra steps, which I actually followed to install it myself. So within my IDE, I do control J to open up my terminal. I have a Ubuntu WSL1 running and then I run the cloud command and there we go. We have our terminal

**[0:04:26]** open and it's so easy to get started with cloud code. You just have to tell it what you want it to do. Like I have a question about my repository or I want you to implement XYZ. Just go ahead and get started. If you're new to Cloud Code, just throw in some commands, see

**[0:04:40]** what it's capable of doing. And then when you want to take Claude code from being good to great, that's when you want to start implementing all the strategies that I'm going to get down and dirty and cover for you right now. And so we'll start with the first one,

**[0:04:53]** which is our global rules. Basically, the system prompt to steer claude code so that we can have it behave the way we want it to. Your claw.md file is like your wind surf rules or your cursor rules if you've used other idees before. It's the highlevel instructions where

**[0:05:08]** you want to put things like your best practices or patterns that you want it to follow. It's basically the system prompt that you get to craft for cloud code. And there are two ways that we can create it. The first one, the easiest way is to use the built-in /init

**[0:05:22]** command. So going into my terminal here with cloud code, if I type in /init, this is going to walk me through an initialization process where the creation of the cloud.md is a part of it. So, Claude Code will walk me through creating the system prompt for itself. But what I like doing even more is

**[0:05:39]** creating my own claw.mds because I like being really meticulous about this instruction set since it is really like the highest level instructions that we have for our coding assistant. And so, as an example that I have for you, if we go back to the repo that I have linked

**[0:05:53]** in the description, I have a claw.md prepared for you, which is generally what I use when I build Pythonbased applications. And so you can use this as a template for Python. And then also within the Dynamis community, we're working on different cloud.mdls for different kinds of projects like

**[0:06:10]** building agents or building nex.js apps or Rust applications. We're creating all these templates and we're doing it a part as a part of a community initiative. The context engineering hub is something that we started recently in Dynamis that I'm super pumped about. Basically, we're creating this gold mine

**[0:06:26]** of AI coding resources like global rules like we're just talking about, claude hooks and sub aents and different slash commands and PRP templates. Like no matter what you want to build, you can come here, find resources to save you hours setting up that initial context for your AI coding assistant. So

**[0:06:42]** definitely check out dynamus.ai if you're interested in this and want to be a part of this. And so I took the Python rules from that resource and I have that available for you just to get started with something here. here. And so what I can do in the root of my folder here, I

**[0:06:55]** can create a new file and just call it claw.md. And then I'm just going to go ahead and copy and paste the contents from the template that I have available for you. So this is how easy it is to set up global rules for your coding assistant with claw.md. And so now what

**[0:07:08]** you can do is you can go in your terminal here and you can just ask it what system instructions do you have. And part of what it'll cover here is the claw.md. We didn't even have to read it explicitly because it's just brought in automatically. So here we go. We got

**[0:07:20]** things like Kiss and Yagny which we have covered directly in our claw.md. And also you could have multiple claw.mds at different levels of your repo. And so I'll show you what this looks like right now just as the example that I have here. You can have a cloud.md in your

**[0:07:35]** frontend folder and then one in your backend folder. These aren't read by cloud code automatically, but there is system prompting under the hood in cloud code. So it understands like if I'm operating in the frontend folder and I see a cloud. MD there, I should look there for front-end specific context. So

**[0:07:49]** it's very intelligent about how it works with these. And then another really pro tip that I have to give you here is that a lot of teams are starting to use claw MDs in a very sparing way as in they don't put a lot of context into the

**[0:08:02]** claw.md. Instead they have their patterns and best practices and other business documents outside of their claw.md and then they just reference those files in their global rules here. So that way it's a lot easier to share things between your team members. It's easy to switch between AI coding

**[0:08:19]** assistants, which is something else that I told you that I would be talking about here. And so, yeah, that's a really powerful way to manage your global rules. And then also, I have a note right here. Other AI coding assistants, they always have some kind of global rules or steering documents, whether

**[0:08:32]** it's cursor or kirao or augment code, like they all have this notion of global rules. Also, one last thing that relates to global rules is prompting strategies for cloud code. And man, could I make a full video on this, but a couple of things I want to call out really quickly

**[0:08:48]** is there are keywords with cloud code. Things like important, proactively, ultraink. They're actually built into the model. And so, it's important to use these when appropriate. Definitely try some of these out. Like try throwing Ultraink into a prompt and just see how much more it'll use tokens to think

**[0:09:03]** through a problem. Also, Claude loves to overengineer and implement old code or keep old code for backwards compatibility. So prompting against things like that, like keywords like production ready that cause it to overengineer, definitely important to keep in mind. So yeah, there's like a gold mine of information that I have for

**[0:09:20]** prompting. I just wanted to throw out a couple of things here to really help you as you're making your global rules and even prompting beyond that. Next up, we have permission management. So by default, Claude is going to ask you for permission before it does any command or

**[0:09:34]** edits any code in your codebase. And that's good for security purposes, but we also don't want to always have to improve it for every single little action that it takes. And so we can set up a set of commands that it can run without asking for our permission. And

**[0:09:49]** so there are two ways that we can do that. The first way is that we can use the permissions command in cloud code. So when I go through this, it'll walk me through an allow list and a deny list. And I can set up all these rules right

**[0:10:01]** within the CLI. The thing that I like doing though is I like defining these myself in the settings.local.json file. So this is a special file that lives in our.claw directory. And this dotclaw directory is where we'll see other things like slashcomands and sub aents going forward. But within this

**[0:10:18]** file, I can allow all of these actions within this JSON. And so within the template that I have for you, I have a settings.local.json with all the commands that I usually like to give it permission to run without my approval. So things like GP and ls so it can search through our

**[0:10:35]** codebase, moving directories and making directories, running Python commands. I like it to do all these things for me. Now something that I never add to this list is I never add the rm the remove command because I always want to approve before it deletes any files. And so it's

**[0:10:51]** one of my recommendations that I have here. And the other thing is never just to give it bash star because this means that it can run any command without asking for your approval. So, you want to be explicit, calling out different commands or groups of commands that you

**[0:11:03]** want it to run versus just letting it run everything. That is way too dangerous. And if you really do want to do that, then you can run in YOLO mode in a dev container, which I'll cover later on in this guide here. So, that's everything for permissions. It's really

**[0:11:17]** nice to have this set up right out the gate so that it can operate more autonomously and you don't have to babysit it as much. And so, with that, we can move on to mastering custom slash commands. This is where we can build our own agentic workflows just as simple

**[0:11:30]** prompts for cloud code. And all you have to do to create a slash command is within yourcloud folder, you have to create another folder called commands. And then you can create a slash command as a markdown file. So I'll call this primer.mmd. This is one of the examples

**[0:11:44]** that I'll pull from our template in a second here. And so this is where we create a set of instructions that we can reuse basically as an advanced prompt for cloud code. You can get very elaborate with these. Like I said, building entire agentic workflows, guiding cloud code through a multi-step

**[0:12:00]** process. So, I'm going to keep it simple right now, but just know that you can take these really, really far. And so, the example I'm going to use here is priming context for Cloud Code. So, it's a set of instructions, a set of steps that I'm telling Cloud Code to take in

**[0:12:15]** order to get it up to speed with a current codebase that I'm operating on. So, it's a really powerful command to run for cloud code when you're working with an existing codebase, but you're starting a brand new conversation. So, you're coming in fresh with cloud code. You want it to catch itself up on the

**[0:12:30]** codebase before implementing a new feature. And so, it basically is just a prompt that we have here, which by the way, for other AI coding assistants like cursor and curo that don't have these slash commands, you can literally just use this as a prompt. And so, the nice

**[0:12:44]** part about having this as a slash command though is that it's just very reusable. Like instead of us having to copy and paste this or type this out in cloud code, we can just do the slash command. I'll show you what that looks like in a second. And it's also just

**[0:12:56]** very easy to share prompts with your teammates when you can just send them these commands that they can run with a single line. So this primer right here. Now what we need to do to run it is I'm going to go back into cloud code. I'm going to exit out of cloud code and

**[0:13:11]** start a brand new session so we can load in all the new commands that we've added in ourcloud folder. And then we can do slashp primer. And so I'll go ahead and run this. And it's going to start following all of the commands that we have listed out here. So it'll start by

**[0:13:24]** using the tree command. We'll see it do that. And then it'll read the claw.md and the readme. So it's going to do those one at a time. There we go. So it ran the tree. We'll see it read the claw.md next. There we go. All right. So you get the idea with this. So we're

**[0:13:37]** priming our context here. And so going back to the readme, the last thing that I want to cover for these slash commands is you can also have parameters with these slash commands with arguments. So when you have a slash command like this where you have this dollar sign

**[0:13:53]** arguments keyword, that means that whenever you invoke this command like slashanalyze performance and you pass in another parameter after a space here, that is going to fill in what you have for the dollar sign arguments here. you're going to replace this keyword with whatever you type out here. So you

**[0:14:10]** can parameterize these slash commands, which just is another really nice thing to just make these commands more convenient for you. And so with other AI coding assistants, you can just like tell it to look at this command, use it as its prompt, and then like for the parameter, I want you to use this value.

**[0:14:26]** So you can still do this with other coding assistants, but slash commands just make it so easy with cloud code. Next up, I want to talk about MCP servers. As awesome as Cloud Code is, there's still a lot of opportunities to enhance it with external tools. And MCP

**[0:14:40]** is our way to connect Cloud Code to those. And so I've covered MCP a lot on my channel before, even how to use it with Cloud Code. But I've got some simple instructions here for how you can manage MCP servers and add them. I've talked about others on my channel

**[0:14:53]** before, like my crawl for AI rag or like Superbase or Neon, so you can manage your database within Cloud Code. One that I really want to focus on here though that's made a huge difference for me is the Serena MCP server. This one's incredible. I just found out about this

**[0:15:07]** last week and it is already doing a lot of good work for me. So this MCP server, it does a lot of the things that Claude Code does to understand your codebase and search through it and find the files to edit for changes that you ask for, except it does it better. It is an MCP

**[0:15:22]** server that's all about semantic retrieval and editing your code. So it's a very codingheavy MCP server. It's a gamecher. And so we can add this into cloud code to enhance its understanding of our codebase. So it's a wonderful MCP to work with existing code bases, which I know is something that a lot of you

**[0:15:40]** have been asking me to cover more on my channel. And so make sure you have UVX installed. This is how you can install it in WSL. And then we can add Serena just with this command. So I'll go into my terminal here. I'm not in the cloud CLI. I'm exiting out a bit right now.

**[0:15:54]** And so I can add the MCP server. There we go. We've added Serena. And then I can do claude MCP list. And this is going to tell me the MCP servers I have connected. And it's going to verify the connection like we have with Archon. I'll talk about that in a sec. And then

**[0:16:06]** also Serena. And we could also do cloud MCP remove Serena if we want to remove that connection. Obviously, we don't want to do that right now. And so the other thing that we can do in order for cloud code to be able to run Serena without asking us for permission is we

**[0:16:20]** can add it to our settings here. So I can say mcp_serena. That is the specific syntax to allow automatically access to all of the tools here. And so it's mcp and then the name of your mcp server. Like I can also do mcp archon. There we go. So now it's able to use all the

**[0:16:40]** tools from these mcp servers without asking for my permission which I generally prefer and I'd recommend doing the same. And then the other thing that we can do I'm going to give you a live example of Serena here. I edited my primer.md this slash command to specify I want you to use Serena to search

**[0:16:57]** through the codebase and then just keep trying to use Serena if you get any errors because that happens sometimes. But yeah, we're going to change the behavior of our slash command leveraging this new MCP server. And just to give you a more complete example, what I'm going to do here is add some stuff into

**[0:17:11]** the codebase. So I'm just going to take this here. I'm going to copy this. I'm going to take what I have for the Pantic AI PRP template I covered recently on my channel. I'm just going to add this as content to our repo here. So, we have something for it to search through with

**[0:17:25]** Serena. So, okay, we got a more complete codebase here. Now, I can go back into Claude and I can run that primer command again, but this time it's going to behave a lot differently. There we go. I'll send off the primer and it's going to start by using the tree command just

**[0:17:39]** like before. It'll read the claw.md and the readme, but then in a second here and I'll skip down to this for you. Okay, actually there we go. It's already starting to use Serena and so we'll see it leverage different tools within the Serena MCP to really understand my

**[0:17:51]** codebase. Take a look at this. All these different calls to Serena and I had to approve none of them because I already added them into my settings.local.json for the Serena MCP. And so I'm not going to go through and like show the full output of this command here. But yeah,

**[0:18:05]** it's just going to have a much better understanding of our codebase, especially as our codebase gets larger. That's when cloud code can start to fall in its face and you want to have tools like Serena. And then the last thing for MCP is me and a few other guys in the

**[0:18:17]** Dynamis community are working on a massive overhaul for Archon. We're going to be making it the MCP server for AI coding assistants. And I cannot wait for this. It is going to be the knowledge and task management backbone for all AI coding assistants. And this Wednesday, the 13th, my next video at 700 p.m.

**[0:18:36]** Central time, it's going to be our official open-source beta launch of this new version of Archon. And as another celebration, we have a launch party. I'm going to be doing a live stream on Saturday the 16th at 9:00 a.m. Central time. So, definitely mark your calendars for that. This is going to be a huge

**[0:18:53]** celebration for Archon, which has an incredible user interface. Now, you can manage tasks for your coding projects with your coding assistant in real time. So, as it updates things through the MCP server and as you're updating things, you're communicating back and forth in real time. We've got knowledge as well,

**[0:19:10]** so you can crawl documentation kind of like my crawl for AI rag MCP. And we have all those different strategies that I've been working on. We've been pouring our heart and soul into Archon. So, this is just giving you a little bit of a teaser right now. So much more coming

**[0:19:23]** for this very, very soon. The next strategy that I want to dive into with you is context engineering with the PRP framework. And I've covered this a lot on my channel recently. So, I'll link to a video right here if you want to really dive into this because it really does

**[0:19:38]** deserve its own video like a lot of the things that I'm covering here. So, by the way, if you want to see more of one of these strategies in a complete video, definitely let me know in the comments. But context engineering with the PRP framework, it's a three-step process for

**[0:19:52]** us to define exactly the feature or new project we want to create. We generate a comprehensive document for context for our coding assistant and then we execute it and we have instructions as slash commands to take care of the last two steps for us. And so I'll just walk you

**[0:20:07]** through this process really quick. Definitely check out that other video if you really want to dive into this more. And so within the PRPS folder, this is always where we define our initial MD. This is where we outline what we want to build, any kind of examples that we want

**[0:20:21]** to give it or documentation, any other kinds of considerations that we have for it. And so I'm taking the template that I have for you that I made earlier on my channel with building pyantic AI agents specifically. So I'm just using this as a simple example here. So you describe

**[0:20:36]** your feature, which in my case to keep it really simple, I'm just going to use the default that I have here. So I'm going to build a simple research agent using Pantic AI. And then a lot of times it's helpful to describe the tools, dependencies, and system prompts that

**[0:20:49]** you want for your agent. I'm just going to delete this to make it really simple and fast for our purposes here. You want to provide any examples that you have like for the Pantic AI use case that I gave for you guys. I have examples already in here for different agents

**[0:21:03]** built with Pyantic AI. So, I'm referencing all these here so that when we generate our PRP, that's that longer form prompt that has all the context for the coding assistant. It's going to have all these examples within it. So, it'll reference those things, bring it into context so it has those examples to

**[0:21:19]** build off of. And then same kind of thing with documentation. So referencing things from the Pantic AI documentation directly. So it reads those pages. So we're telling it explicitly where to go look to get all the information that it needs and then just any other kinds of considerations that we have here. Some

**[0:21:36]** things that I see it messing up on a lot like how it manages environment variables. So I'm just calling it out right here. So you create your initial MD and then going back to the readme. The next step after that is we need to generate our PRP. So, I'll go back into

**[0:21:50]** Claude Code here and I'm going to clear the conversation because we're going to just start from fresh here. And I'll just say slashgenerate pyantic AI PRP or whatever your slash command is called to generate your product requirement prompt. And then we just give it the path to our initial MD. And so I'll kick

**[0:22:10]** this off. It's going to take a little bit. So I'll pause and come back once it is done. But all this is going to do is go through my initial atm do any of the research that it has to do to grab all that context form that super long prompt

**[0:22:22]** that we're then going to execute in our last step. And take a look at this. It's even using archon under the hood. I didn't even tell it to, but we have the MCP server connected. So, it's using that for rag searching and looking at our code examples here. So, you're

**[0:22:34]** getting a little bit of a taste of how archon works. You'll see this a lot more in the beta release next week. But yeah, basically what we're doing here when we're generating a PRP is we're basing everything off of this base PRP. This is the template that we're using to create

**[0:22:49]** this large prompt that we're going to execute in the next step to generate all of our code. And so we cover core principles for Pantic AI, what to do and not to do. So I've crafted this base PRP very specific to building AI agents with Pantic AI, covering all the context we

**[0:23:04]** need. Something else I really like about PRP is we cover the different tasks like here's what you should do step by step to build an agent with padant AI. Then we get into validation loops aka validation gates. So telling the AI coding assistant how it can validate itself to make sure that its output is

**[0:23:21]** good according to like what we care about for AI agents. It's really really nice. A final checklist some anti-atterns. That's basically what we're going to have it create here, but specific to the agent that we want to create from our initial MD. And there we go. Our PRP is generated. And you

**[0:23:38]** always, always want to validate your PRPs before you execute them. Make sure that it complied with the base PRP, that everything's filled in to your specifications, that everything looks good. Like if you gave this to another engineer, they could go ahead and use this to implement the agent end to end

**[0:23:54]** exactly as you want. That's the goal that we have with such an extensive prompt as a PRP. And so yeah, this looks perfect to me. So now I can go ahead and execute this. And so I'll go back into cloud code. You generally want to clear the conversation with /clear. We want to

**[0:24:09]** start with fresh context here because the PRP has everything that it needs. And so now we can do the other command. Instead of generate, it is execute PRP. And so then again, we'll just give it the path here to the brave research agent.md. There we go. So now we're kicking this

**[0:24:27]** off. It's going to build the full agent for us. So it'll read the PRP first because that's the argument that we're giving the slash command. We talked about arguments with slash commands earlier. Then it's going to go through and it's going to read anything else that we have in our structure here,

**[0:24:41]** including all the examples that we told it to. It's going to do web research on the documentation. It's even using Serena. Take a look at this. So it's using Serena to understand our code structure. It's going to be using archon for rag as well. There's so much happening under the hood. So, I'm going

**[0:24:54]** to pause and come back once we have our complete implementation. And there we go. After about 20 minutes, we have our AI agent. And just like with the PRP, I would very much encourage you to go through and validate the code that was outputed here. I did that off camera. I

**[0:25:08]** iterated twice just to clean up a couple of things. And now I can go ahead and run this agent and just show you really quickly that we have things working here. Just the power of context engineering. And it is a very, very basic agent just to give you a

**[0:25:21]** demonstration here. But it's a nice CLI that we have. We've got streaming. It has a tool for web search. I can say what is the net worth of Jeff Bezos in 2025. And it'll even show us that it's using the web search tool. We've got the text streaming and conversation history.

**[0:25:36]** It's a pretty nice agent that we have built here in a single shot thanks to PRP, thanks to the examples that we referenced in the documentation in our initial MD. So just showing you at a high level what it looks like to do context engineering with the PRP

**[0:25:50]** framework. And so with that, I want to move on to the next step that I have for you here, which is making our coding process even more powerful with PRP, really with anything. And it's thanks to having a specialized intelligence in our coding workflows thanks to cloud code

**[0:26:08]** sub aents. So with sub agents, our primary cloud code agent is given the ability to call upon any of them. And the primary agent is the one that actually prompts the sub aent. So very important to understand how that works. The sub aent has its own context window.

**[0:26:23]** So, we're not bringing in the entire conversation history into each sub agent. We're only including a prompt for our sub agent that is crafted by our primary one based on how it knows how to use that sub aent. We'll see what that looks like in a little bit. And sub

**[0:26:37]** agents are very powerful because they each have a specialized system prompt. We can limit the tools that they have access to and they work autonomously on delegated tasks. Our primary agent can also kick off many sub agents in parallel. So, it's another very easy way to add parallel agent execution into our

**[0:26:53]** coding workflows. And all of our agents, they live in thecloud folder in a new folder that we'll create here called agents. And there are two ways that we can create our agents just like with our global rules. There is a / aagents command. It's kind of like slashinit

**[0:27:08]** where cloud code will actually walk us through creating our agents. So, it'll output a file kind of like this. Or we can just build these files ourselves. And there's a couple of templates that I have available for you here. So feel free to grab these from the agents

**[0:27:21]** folder in the GitHub repo linked below. One of them that I want to show you right here just to quickly show you the power of sub aents is one that Raasmus the creator of the PRP framework. He actually built this for validation gates. So validation gates is a very

**[0:27:36]** important part of the PRP framework because at the end once we have executed the PRP and we have our code outputed we want our agent to operate autonomously writing tests iterating on those tests until it's confident that the code is working and so we can build a specialized agent to handle that and so

**[0:27:52]** I'm going to make a new file in the agents folder I'll call it validation gates.md. So these are markdown files just like our global rules, just like the hooks we'll get into in a little bit. And we have a unique system prompt here telling it exactly how to implement

**[0:28:06]** and validate our validation gates. And so at the top we have the name of our agent. Then we have a description. The description is really important because this is what tells our primary cloud code agent here's what this sub aent's all about and also how you can invoke

**[0:28:21]** it. So really telling when and how to use this sub aent. And then we can also describe the tools that it has access to. There's other parameters as well like we can even specify the model like if we want to use sonnet for or opus for we can specify that for the sub agent.

**[0:28:35]** So this is our agent. Now going back to the readme here I just want to say that while other AI coding assistants don't have the formal idea of sub aents built into their platform like cursor or hero or client or whatever you can achieve something very similar just with

**[0:28:52]** prompts. And really, just like our global rules, just like our slash commands, all of these sub aents are really just prompts. And so you could just have a folder that's filled with all these different prompts. And you could have your global rule say like, okay, when you get to this point in the

**[0:29:06]** development flow, use this prompt to perform validation gates or to update the documentation, whatever that might be. So you can achieve something very similar. It's just so easy the way that we can implement agents with cloud code. Being able to have things like descriptions and tools and specifying

**[0:29:22]** different models, it's a lot more flexible than if we just have to do it with only props. So there's still a reason to do this, but yeah, let me go ahead and show you a demo of this. So within a new cloud code session, you have to refresh your session to bring in

**[0:29:33]** new agents just like new slash commands. I'm saying here's my validation gate. I want you to make sure all the tests for the brave a research agent are working. And I'm not being explicit for it to use the sub agent. I mean, I'm being kind of explicit saying validation gate here,

**[0:29:48]** but this is just to simulate more what it would look like when we're operating in the middle of a PRP because that is a keyword that we use, validation gate. And there we go. It's now calling upon our specialized sub agent and our sub agent is making this task list. It's

**[0:30:01]** handling everything in a separate conversation window. Then it's going to pass control with an output back to our primary agent that will continue the flow or give the final response to us. And so we don't have to see this whole process right now. I just want to demonstrate really quickly how the

**[0:30:17]** primary agent is going to intelligently figure out when to call upon sub agents based on the description that we have here. Next up, we have claude hooks, which is a very powerful way to add deterministic control to claude codes behavior. So, we have all these keywords here. After any of these actions, we can

**[0:30:36]** invoke our own custom command. And so before we use a tool, after we use a tool, after we use a sub agent, we can have our own custom command that runs. It's really powerful. And this is built into hero as well, but it's not in other AI coding assistants. I definitely think

**[0:30:51]** though because cloud code is the industry leader and you always copy the industry leader, we're going to see these other IDEs like cursor, winer, and augment code implement hooks as well. It's really, really powerful. And so yeah, all you have to do to add hooks here is you have to define them in JSON

**[0:31:06]** and then add them to our settings.local.json. So I usually like organizing them in a hooks folder. And then I just have a JSON file here. I can just call this whatever I want, hooks.json. And then I have a couple of hooks in the template for you just to introduce yourself.

**[0:31:21]** These are really, really basic hooks, but just to introduce yourself to the different kind of hooks you can add and also different points in the development life cycle that you can have these actions take place. So, I'm going to copy this, bring it into here, and then just keep it really simple. Right now,

**[0:31:35]** I'm going to bring it down to a single hook, which I'll then copy this JSON and put it in my settings below everything that I have for permissions that we already covered. So, there we go. I now have this command that runs. It's going to run this bash script every single

**[0:31:50]** time that we finish invoking one of these tools. So we're using this matcher to also kind of filter down after our tool use. And so within the hooks folder, I'm just going to create this file as well because I'm calling out the path in the command there. So log tool

**[0:32:04]** usage.sh. And then I'll just go ahead and copy the contents from the template. So there we go. It's really simple. You can also get parameters from your hook. So I could do things like log the specific tools that are used here. But yeah, keeping it really simple. It says Claude made an

**[0:32:18]** edit with a time stamp every single time. So it's going to call that now as long as we refresh our Claude session. So I'm going to clear start a new session with Claude and ask it to make a change. So a little silly here, but I'm asking it to make just some random

**[0:32:31]** change to my ignore. I don't really care what it does here. I just want to see that when I make a change, it is going to call my hook. And then we'll see something get outputed to a new logs folder that will be created in ourcloud because that is where we're pointing to

**[0:32:44]** in our script. So, I'll let it make the change to my getit ignore here. There we go. And then just in a second. Boom. All right. We got our logs folder. We have our log file. Claude made an edit just a second ago. Looking really good. So, that's hooks at a basic level. There's a

**[0:33:00]** lot that you can do with them. It honestly would deserve its own video. So, yeah, certainly let me know in the comments if you're curious on having a video diving into hooks or something like sub agents as well. Next up, I want to dive into the GitHub CLI using that

**[0:33:14]** with Cloud Code. As much as Cloud Code is useful operating in our local development environment, it's also extremely powerful and you can have it operating within your GitHub repository. So, you can have it manage issues and pull requests. That's what I want to show you right now. And so, you can

**[0:33:30]** install the GitHub CLI just by following this link. And then there's a couple of commands that you need to run here. So, first of all, just authenticating with GitHub. This will walk you through the OOTH flow and then outside of Claude here. So I'm going to clear this. You

**[0:33:43]** can just do GH repo list just to make sure that it's working for you. So this will list all of your GitHub repository. So at this point you're signed into Claude and now that you have GH in your development environment, you have the GitHub CLI command. Cloud code can start

**[0:33:58]** using this to operate on your remote GitHub repository. It's so powerful. And so like for example, what I can do here in my GitHub repo. So everything that we've been building together in this video, I have in this private GitHub repo. I can go ahead and create an issue

**[0:34:12]** right now. And so I'll open up an issue here. I'll say uh greeting for the Brave agent. And I can say, this is just kind of for demonstration purposes here, but I can say my Brave agent needs to have a greeting when I first start the CLI. So

**[0:34:28]** just something kind of silly here, but I'll create this issue. There we go. And then the issue is number one. You can see that here. And then also in the URL. And this will be important in a little bit because we're going to call out this issue to cloud code and have it fix it

**[0:34:41]** for us. And in order for it to do that, I'm going to create a custom slash command. So I have this one also available in the template for you. So I'm going to copy this. I'm going to go into mycloud in my commands. New file fix github issue MD, not sh that's

**[0:34:57]** hooks. There we go. All right. So I'll paste this in. And basically what we're doing is walking it through. when I give you an issue and this is the argument that we're passing here. It's going to be the issue number like in our case is just issue number one. It's going to use

**[0:35:10]** the GitHub CLI GH issue view to understand the issue. It's going to look through our codebase, implement a fix. It's going to write tests and validate things which that might even call upon our validation gates sub agent. We'll see. It's going to ensure everything is good to go. And then it'll also create a

**[0:35:25]** pull request. So, it's going to push things to GitHub maybe in like a new branch it creates or whatever. And then it'll also create a pull request. So, it's end to end. It goes out to GitHub, does things locally, and then goes back out to GitHub with a PR. So cool. So,

**[0:35:38]** I'm going to go back into Claude. I'm going to clear this, and then I'm going to execute this command. So, it's just simply /fixGitub issue, and then my issue number is one. So, go ahead and send this in. In a second, it's going to pull this comment right here, and it's

**[0:35:52]** going to use that to guide its development. Yep. So, we got the issue right here. Greetings for the brave agent. And the text is cut off, but it got the full text here. Now it's creating a to-do list to fix everything and then it'll create a PR at the end.

**[0:36:03]** So I'll pause and come back once it is done with this flow. And there we go. Let me full screen this for you here. The full summary. It found the issue after reading it from GitHub, implemented the fix, tested everything, made a new branch, pushed it, and created a pull request all from a single

**[0:36:19]** slash command. That's the power of slash commands with this full agentic workflow that we created. That's the power of the integration with the GitHub CLI. So going back to my issue here, we can see that we have a commit and a new branch referencing this issue and we have a new

**[0:36:33]** pull request. So if I refresh here, we'll see a one next to pull request. There we go. I can go in here. We can take a look at the changes that were made. So yeah, it made some tests and then it also updated CLI just to add a

**[0:36:44]** nice greeting here. This is looking so good. So I can go ahead and review these changes. I can merge them into my main branch. I can even have Claude help me do all of that. It's just beautiful the integrations that we have here. And of course, there's a lot more you can do

**[0:36:57]** with the GitHub CLI with Cloud Code. You can even have Cloud Code integrated directly with your GitHub repo. So, you can reference it within your issues and PRs just like a normal developer and have it fix things and create PRs autonomously. Really cool. So, we're just scratching the surface here, but I

**[0:37:13]** just wanted to introduce you to what is possible with these kind of integrations. Next up, let's go on to the YOLO mode with Devont Containers. Because at this point, we've already covered permissions. We have everything set up in our settings.local.json. We understand what it looks like to have

**[0:37:29]** things in place where Claude will do certain actions autonomously without our approval. And then other things like removing files, we generally always want to approve it before it does so. And one of the biggest reasons that we want to have these kind of protections in place for commands like removing files is

**[0:37:45]** because cloud code can theoretically remove things outside of our current project. It could delete really critical files on our computer. worst case scenario. Now, I haven't seen that happen, but these are the kind of protections that we want to have in place in general when we're running cloud code directly on our computer. And

**[0:38:03]** so, the solution for this, if you want to have a safe environment, but also have claude never have to ask you for permission to do things so it can go and operate entirely autonomously, that's when we want to enable yolo mode with dev containers. And so, basically with

**[0:38:18]** dev containers, we run cloud code in its own isolated environment. So our entire machine is protected. We can also have firewalls set up in place for the dev container. So it only has access to the websites we want it to. And so then we can run it with dangerously skip

**[0:38:33]** permissions where it will now no longer ever ask us for approval for anything and we can still be safe. And dev containers is an official idea from Anthropic. So they have this page in their docs which I'll link to in the description below. You can read through this if you want to understand what

**[0:38:47]** they're setting up for us here. And they give us the docker file and a couple of other things. So we can create this dev container and we can run these directly in any VS code. So you can also do forks like cursor and wind surf. We can run it

**[0:38:59]** with cloud code. Just open up in any VS code. So yeah, I'll show you how to do this right now. And I have this dodev container that's included from anthropic. I have this directly in the template for you. And so what I'm going to do right now is I'm going to go back

**[0:39:13]** to the two folders here. I'm going to copy this dev container. I'm going to bring it right into the codebase that we've been working on in this video. So there is our dev container and then going back to our readme here. The way that we run this is we in VS Code we

**[0:39:27]** just have to press F1. We have to select dev container and I'll say reopen in container and this is going to automatically build up our dev container. Open up a new VS Code environment. I'm just using windsurf right here to run cloud code in the terminal. So it's going to be building

**[0:39:40]** the dev container and then after a little bit we'll have a new environment spun up operating entirely inside the container. So I'll pause and come back once that is ready. So there we go. And then the way that you know that you're in the dev container is just in the

**[0:39:52]** bottom left it'll say that you're in the container the dev container. We can go back to reopen folder locally if you want to exit out of the container go back to your normal development environment. And so now if I do crl J to open up a terminal here and I do cloud

**[0:40:06]** this is going to open up a brand new cloud code session. And because I am in an isolated environment, basically a new virtual machine. It's walking me through the process to set up Cloud Code from scratch. And this makes sense. So I'll just go through the authentication flow

**[0:40:20]** right here. There we go. So I just opened the link to authenticate with Cloud Code. Went through the last couple of steps here. And now we are within Claude. And what I can do, by the way, if I clear this and I open Claude again, this is where I can run the d-

**[0:40:32]** dangerously skip permissions. And so we'll see in the bottom right here. So let me enter. So yeah, it's giving me a warning here. You in bypass permission mode. So I accept this and we'll see this in the bottom right that we are bypassing permissions. So now whenever I

**[0:40:46]** do something like uh write more tests, whatever it is, like it's not going to ask me for approval before I edit anything. Even if it removes files, it won't ask for approval there either. It's going to do everything entirely autonomously. But also, we have protections in place like there's some

**[0:41:01]** firewall stuff that Enthropic built into this container. We have an allow list of websites that we can visit. So you can add on to that list as well. Definitely poke around with this if you're interested in setting up this safe YOLO mode dev container environment and it's all thanks to this docker file. So all

**[0:41:16]** this is coming directly from the anthropic documentation. We now have our safe YOLO mode. Last but not least, I want to cover parallel agent execution with you in cloud code. We're going to do this with the idea of git work trees. And there are a couple of different ways

**[0:41:31]** to implement parallel agents. We saw one way with sub agents already, but this one's really powerful because with git work trees, basically it's our way to have different branches for our GitHub repository open at the same time and we'll have an instance of cloud code operating on each of them. So, we're

**[0:41:48]** guaranteed isolation. They're not going to be tripping over each other's toes because they all have their own branch open up. So, we have the codebase duplicated across these different work trees. And then basically after we implement whatever changes we want in each work tree, we can find the one that

**[0:42:02]** we want to merge in or maybe we want to merge in all of them and we can just bring them back into our main branch after each cloud code instance is done. And so there's a manual way to set this up and then there's an automated way that's really cool with slash commands

**[0:42:16]** that I want to focus on with you here. But let's start with the manual way really quick. So I'm not going to run through all these commands as a demo right now. I just want to call these out really quick. Basically, once you have your different feature branches created,

**[0:42:28]** like feature/off feature/appi, you can now add work trees. And so, you just call out the branch that the work tree is going to be based off of. And then you give a path to your local file system where you want to basically replicate the codebase into the work

**[0:42:44]** tree. So, it actually duplicates everything. So, you have a completely isolated environment in a separate branch. And then you can just change into that directory and launch cloud. And so you can do this in any number of work trees that you create. It's really, really easy. But it is pretty tedious

**[0:43:00]** for you to create all these branches, set up all these work trees, and then open up Cloud in every single one of them. And so I have an automated process for you that takes care of all this. This is what I really want to demo for you right here. And so there are a

**[0:43:13]** couple of slash commands that I have in the template for you going along with all the other ones that we've covered like the primer and the PRP stuff that I want to bring in right now. So the first one is prep parallel. So I'm going to copy this. I'll bring it into our

**[0:43:26]** commands and I'll explain it really quickly. So prep parallel MD as in prepping the parallel execution of many different agents here. So we have a couple of arguments. We have the feature name. What is the name of this new feature that we want to implement? And then what are the number of parallel

**[0:43:42]** agents or parallel work trees that we want to have? And then just in a loop here based on the number of parallel agents, it's going to create a new branch and a new git work tree. It's going to change into there and it's going to just validate that everything

**[0:43:55]** is set up properly. And then we'll run the git work tree list at the end to make sure that we have everything set up. So we're prepping for the execution of many different cloud agents here. And for this example, what I have right here with parallel execution, this is

**[0:44:09]** specifically for having many different agents tackling the same feature in a codebase. And so I also want to be clear here. Let me scroll back down. I also want to be clear here that you can use parallel agents to work on different parts of your codebase at the same time.

**[0:44:22]** Or like what we're doing here, we can use parallel agents to implement the same feature many different times. So we can pick the best implementation. It's just a faster way to develop because sometimes cloud messes up and you have to restart. But now we can just do all

**[0:44:36]** that at once. And so that is our prep parallel. The next one that we have, it's kind of like PRP where we have a prep command and then we have the actual execute command. So, execute parallel. So, I'll bring this in. I'll make a new file. Execute parallel MD. Let me fix

**[0:44:51]** the spelling there. Rename. Typos are not good. All right. So, there we go. I'll paste in the full contents here. So, we have the feature name as one argument. We have the plan to execute. So, this is just like our initial MD with PRP where we will create and I'll

**[0:45:05]** actually do this here. We'll have a plan MD and this is where we'll specify everything that we want to implement for our new feature. And so I can just say something like change the Brave agent CLI to have red and orange colors for the primary theme. Just something very

**[0:45:22]** simple for a demo just like we did with sub aents. And so going back here to the command, we have our plan to execute. So we'll pass in the path to plan.md as this argument within the slash command. Then we have the number of parallel work trees. And this should just be the same

**[0:45:36]** number that we passed into prep parallel. And so now for the instructions here, we're just telling it like you're going to create any number of cloud code agents that are going to operate implementing the same feature. So we're just describing like read the plan and then here's how you set up the

**[0:45:50]** different work trees and executing the different cloud code agents and then each of them make sure that they report their final changes in a comprehensive results.mmd so that we can go into each work tree after see what was implemented. We can test each one out, find the one that we like the most and

**[0:46:05]** then we can bring that one into our main branch. So that's the flow that we're going to go through right now. And so starting out, I'm going to go into my cloud here. I'm going to open up a brand new cloud session cuz I just created these slash commands. And so my command

**[0:46:16]** is going to be /prep parallel. And then I need the feature name as the first argument. So that is CLI UI updates. And then three for the number of parallel work trees. And so I'm going to send this off. It's going to go through the set of instructions. And so I'll pause

**[0:46:29]** and come back once this is done. All right. So we've created each of the work trees and verified everything. And we can even see this here. If we go into this new trees folder, we have our codebase replicated in each of these. This is exactly how work trees are

**[0:46:42]** supposed to operate. So we are now ready to execute our parallel process. So I'll go over to the execute parallel here. We got our three arguments. And so here's what I'll do. I'm going to actually clear the conversation here because we don't even need the context of prepping

**[0:46:57]** things. We can just dive right into the execution with no context. And so our command is going to be execute parallel. And then the same feature name. Might as well just call it the same name. CLI UI updates. Then we reference our plan.m MD because that's where we're going to

**[0:47:10]** understand the feature we want to implement. And typically you'll have quite a bit more detail here. I'm just keeping this very basic for demo purposes, but this should be pretty fleshed out just like your initial MDs. And then going to execute parallel. And then we're just doing three for our

**[0:47:23]** number of parallel work trees. And by the way, if you wanted to really take this far, you could combine this whole parallel execution with the PRP framework. Now, that would be really cool. something that I definitely want to play around with in the near future here. But yeah, I'll go ahead and send

**[0:47:36]** this off. It's going to read the plan. It's going to dish that out to three different cloud code sub aents running at the same time implementing the same feature. And then I get to pick the best one at the end. And by the way, when I say that we have parallel execution

**[0:47:49]** here, I do mean that they are all running at the exact same time. We can see that here because we have the blinking light in three spots here. We have a task for each of our sub aents, version 1, 2, and three of the CLI colors implementation. Oh, and look, I

**[0:48:02]** think one of them Oh, yeah, one of them already completed its first task here. So, we're getting through the implementation. They're running at their own speeds, all in isolation. And so, yeah, I'll come back once we are done with all three. And there we go. We are done. And our primary agent even gives

**[0:48:16]** us a summary of what all the different sub aents did in the work trees here. So, we have slight different implementations for the CLI UI updates. And I'll actually show you what this looks like. So, I took one of the sub aents here, the first one, and I just

**[0:48:29]** set up that environment with UV and my ENV, just like I did with the original Brave search agent. And here's what our UI looks like. And honestly, I like the original one more. I mean, this was just a silly example here, but it very much did implement the red and the orange

**[0:48:44]** exactly like I told it to. And each of the other ones are going to look pretty much the same. name. And then I'm not going to show it here, but going back to the readme really quickly, if I do want to pick one of these to bring back into

**[0:48:55]** my main branch, there's just a couple of commands that I need to run. So I can just do get checkout main, and then I can merge any one of these branches that our work tree is based off of back into my main branch, push it up to GitHub,

**[0:49:06]** and that's how easy it is to have parallel agent execution, and then bring it back into our main branch. So there you go. That is everything that I have for you today on using Cloud Code effectively, going from start to finish, all the different features that we have

**[0:49:19]** with Cloud Code and how you can get the most out of them. And I'm going to be totally honest, this guide did end up being quite a bit longer than I thought it would be. But I didn't want to skip out on the details here. I wanted to

**[0:49:29]** cover all these things meticulously so you have just a super solid foundation and clear understanding of how we can get the most out of cloud code with all the beautiful features for things like slash commands and sub agents and hooks and all these things really could deserve their own dedicated video. So I

**[0:49:45]** know that I mentioned this a couple of times throughout the video already, but definitely let me know in the comments if there's anything that I've covered here that you want me to expand upon a lot more. I do want to make quite a few more videos in the near future on cloud

**[0:49:57]** code and just AI coding in general because this is the future and AI for coding is really one of the most exciting use cases of generative AI right now. So if you enjoy this video and you're looking forward to more things AI coding and AI agents, I would

**[0:50:12]** definitely appreciate a like and a subscribe. And with that, I will see you in the next
