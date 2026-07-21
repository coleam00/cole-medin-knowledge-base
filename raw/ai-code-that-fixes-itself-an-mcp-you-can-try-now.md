---
type: raw-transcript
title: "AI Code That Fixes Itself (An MCP You Can Try Now)"
youtube_id: 8Mib-hb6Fcg
url: https://www.youtube.com/watch?v=8Mib-hb6Fcg
slug: ai-code-that-fixes-itself-an-mcp-you-can-try-now
published: 2025-06-18
duration: "0:23:28"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** AI coding assistants. We both love them and hate them. They speed up development a lot, but also they make these stupid little mistakes all of the time that are so frustrating and they get caught in infinite loops trying to resolve them. That's why one of my biggest missions is

**[0:00:15]** to make AI coding assistants actually reliable. And I've been doing that through a couple of things recently. both my crawl for AAI rag MCP server giving external knowledge for libraries and tools to our coding assistants and also through archon which is my AI agent builder and I've been teasing a version

**[0:00:34]** two overhaul for a while now a lot of work has been going on behind the scenes now I can finally tease for you what the UI is looking like and it's looking really really nice more on this later in this video but the big thing that I have

**[0:00:47]** been experimenting with recently that I think is going to be a big deal in the future is combining knowledge graphs with AI coding assistance. And so in this video, I'll show you what I mean by that and how it solves a very big problem that we have for AI coding right

**[0:01:01]** now. And by the way, everything that I'm about to show you here, I have already added to my crawl for rag MCP server. So if this looks fascinating to you and you want to try this out with MCP and your AI coder right now, you can go ahead and

**[0:01:14]** do that. And I've got instructions in the readme for how to set up absolutely everything. And so I want to start by showing you what I have stored in my knowledge graph and then giving you a good example to show why this is so powerful. So let me go ahead and zoom in

**[0:01:27]** on the center node of our graph that I have here in my Neo-4j graph visualization. And what we have here is a repository for pyantic AI. So you'll see this in a bit, but what I have done is I have taken the entire repository in GitHub for Pyantic AI, which is my

**[0:01:44]** favorite open source AI agent framework, and I have turned it into a knowledge graph that can be queried by AI coding assistance. And so all repos have the tag of repository. We have files which are these green nodes, all the files in source control. They have functions which are dark blue. They also have

**[0:02:02]** classes which are teal. And then these classes like for our agent have functions. themselves with these red nodes and then also attributes with these beige nodes. And so I've taken the entire GitHub repository and made it relational in this knowledge graph specifically in a way that can be

**[0:02:18]** queried by AI coding assistants. And there are actually hundreds and hundreds of nodes in this graph. I'm only showing the first 300 so it doesn't look very cluttered. Now the reason it's so powerful to store repositories in this way is because when we are using paidantic AI to build an AI agent with

**[0:02:35]** the help of an AI coding assistant a lot of times what they do is they will hallucinate specific functions or attributes with the classes that we are creating and I have an example to make this very concrete for you. So, I actually used windsurf to build an agent

**[0:02:50]** with padantic AAI for me and it got almost everything right. And I'm not going to dive into the code for padantic AI and how it all works. I just want to illustrate something at a higher level. But in this case, it defined the agent correctly like this. We're defining our

**[0:03:04]** large language model and our system prompt, giving it a tool. This all looks good. But if we scroll down to the way we actually use this agent, we are calling the invoke async function. This is hallucinated windsurf with claw 3.7 sonnet. It totally missed the mark here. This is not a valid function. And the

**[0:03:24]** way that we know that is if we go to our knowledge graph where we have our agent class that we defined earlier in the code. There is not a single red node here for invoked async because that function does not exist. And so what happened is Windinsurf even using the

**[0:03:39]** documentation for podantic AI that I gave it, it didn't quite catch the exact syntax for how to call an agent and get the streaming output. And because it didn't catch that information, it just filled in the blank and completely made something up. And this is what AI coding

**[0:03:55]** assistants do all of the time. And I even have a script that leverages the knowledge graph to check for these hallucinations. This is also in the crawl for AI rag mcp GitHub repo by the way. So I can pass in the path to this script as an argument. And this doesn't

**[0:04:10]** use an LLM for analysis at all. It's all just deterministic code going out to the knowledge graph and checking all the ways that we use pideantic AI here. Does it actually match with what is possible based on the information we have in the knowledge graph? And sure enough, we

**[0:04:25]** found seven valid uses of pideantic AI. So like the way that it created the agent is valid, but then it found a hallucination. And this is exactly what I was hoping it would do. It says that the method invoked async is not found on the class panticai. And we can give this kind of

**[0:04:44]** hallucination detection reporter as a tool to our AI coding assistant. So it can generate a script, run it against the hallucination detector, find any mistakes that it made based on our knowledge graph, and then self-correct. That is the power that we have now. And the way that it knows there is a

**[0:05:00]** hallucination here is because it went to the agent class in my knowledge graph. It looked around at all of these red nodes and yeah, sure enough, invoked async does not exist. And so then it can see like, oh, maybe the function that I should use here is run_stream.

**[0:05:16]** This is the right function to use. And so an AI coding assistant can then get that feedback, go in here, and change this to run_stream. And then I can go back to my hallucination detector, run this again, and sure enough, now we have eight valid uses of panic AI, and our

**[0:05:32]** hallucination rate is down to 0%. And the best part is this also works with function parameters. And so if I use the right function, but I add in an argument that doesn't actually exist, like this isn't a valid parameter, it'll also detect this. So let me go ahead and run

**[0:05:47]** this yet another time. And just also look at how fast this is because it doesn't use a large language model for this analysis at all. And boom, there we go. We now have one invalid use of a function because the test argument does not exist on runstream. So again, going

**[0:06:02]** back to the knowledge graph, it did that by going to this runstream function. Looking at the parameter list here, like okay, we passed in a user prompt. We can pass in model settings or any dependencies, our conversation history, but there is nothing here for a parameter called test. That is how it is

**[0:06:17]** able to determine that there is a hallucination. And so we can use this kind of feedback and we can allow the agent to explore this knowledge graph as it is generating code so that it can self-correct when it makes these little mistakes that usually get it caught in

**[0:06:30]** these infinite loops of trying to resolve these very minute problems. These are the kinds of things that sure you can just go to the documentation for Pantic AI. You can look at examples for how to use agents but sometimes documentation doesn't show these little details and parameters for functions and

**[0:06:47]** things like that. And so that is why it's very powerful to give our agent the ability to actually search through the underlying code for these open source libraries and tools that we are using. Now, one thing I want to cover really quickly before we move on, just to set

**[0:07:00]** the stage, is even though this MCP server is going to be a gamecher for a lot of things that you want to code, I don't want to sugarcoat it by saying it's always going to be the solution. Because depending on what you want to build, for certain kinds of things,

**[0:07:13]** there are tools out there already to help you immensely that have this kind of self feedback and correction built right in. Like building front-end applications is a really good example because we have tools like our very own open source bolt. DIY. We've got Bolt.new and Lovable. I've actually used

**[0:07:30]** Lovable a lot recently, even to build the first version of my Dynamus AI Mastery Community landing page. And it works so so well. I have very few hallucinations in general. And when I do run into problems, they're able to look at the error in the React code or

**[0:07:44]** whatever and then go back and fix it. It's very hands-off for me. So, it's autonomous. It has that kind of self-correction. Very, very powerful. And then another really good example is Browser Automations thanks to a platform called Browserbase. And man, this is a one-of-a-kind company. I've actually been so impressed that I've partnered up

**[0:08:03]** with them on this because for building frontends, we have these different solutions like Lovable and Bolt. And bolt.diy. But for browser automations, I haven't found anything like this. It is insane. And so they have this open- source browser automation framework called stage hand which is definitely worth looking into using super super

**[0:08:23]** powerful because we can automate things with playright. In fact it is built on top of playwright to create these browser automations but they're very brittle because the external websites that we're crawling they can change and so we need an AI agent to be able to intelligently navigate these sites. And

**[0:08:38]** that's what Stage Hand helps with. And they've recently released a platform called Director, which is super super exciting. You can use Director to create browser automations kind of like how you create frontends with lovable or bolt. So you can just go in and ask it like I want to go to my local AI package in my

**[0:08:57]** GitHub and I want to get a summary of all my issues and pull requests and it'll reason to itself figure out how it needs to navigate the web in real time to make that happen and generating the code as it goes and take a look at everything that it did for me and then

**[0:09:12]** it gives me exactly what I'm looking for at the bottom. Like I've been really impressed with director trying it with some different use cases and whenever it clicks on the wrong button or whatever it always self-corrects and so I have this browser where I can see things in

**[0:09:25]** real time as it is navigating the web. Like right here it's in my local AI package and then it's going between pages. I can watch it click on all the buttons and all that. And then also it's generating the code for this script. So I can reuse this automation now. Very

**[0:09:40]** very cool. or I can just use it as my platform to send in a request like go buy my protein powder on Amazon then I can go sit my coffee and come back and then that's taken care of for me. So you can do those kind of automations as

**[0:09:52]** well. So really awesome platform. Browser automation, like I said, is just another example of when you don't really need it to just code it yourself in your AI IDE and use something like this MCP. But there are definitely a lot of use cases. In fact, most of them I would say

**[0:10:07]** where hallucination is a big problem and you do want something like hallucination detection built in. That's what I'm trying to build here. And let me be very clear, this entire strategy of using knowledge graphs is very experimental. I'm still working on refining and validating the idea overall and making

**[0:10:24]** the hallucination detection accurate. And I've been putting a lot of time into building this out, getting to the point that we're at right now. And so I gave an update on my channel last week saying that I'm going down to one video a week so I can put more effort into each

**[0:10:39]** video. And so that'll either mean that the video is going to be longer like my local AI master class or it just means that I'm putting in a lot more effort behind the scenes like for this video. And trust me, I definitely have been. There's been so much work that I'm

**[0:10:53]** putting into this because it really is my mission to find all the strategies possible to make AI coding assistance more accurate and then building that eventually into what will be the overhaul of Archon with Archon version 2. And so Archon is going to combine managing projects kind of like Claude

**[0:11:10]** Taskmaster. That's what we're looking at right here. And the AI coding assistant can actually manage this all through MCP. And then I've got knowledge for rag with all my different rag strategies that I have in the crawl for AAI rag MCP. I'm adding that into archon as well. Probably also adding in this whole

**[0:11:26]** knowledge graph strategy once I have this refined too. And then you can manage the MCP server also through the user interface here for Archon. So just a little bit of a teaser for what is coming with Archon. I'm super excited for this and it's going to remain completely free and open source for you

**[0:11:41]** as I build this out. I have some help from someone in the Dynamis community as well. Um, so I'll kind of, you know, reveal him once we do more of an official launch of Archon V2. But really exciting things for that. So going back to knowledge graphs here, what I want to

**[0:11:54]** do now is take all of this knowledge graph capability, actually add it into the crawl for AI rag MCP server, and then use this with Claude code. I want to give Claude code the ability to work with this knowledge graph, build a Pantic AI agent that has zero

**[0:12:10]** hallucinations. Let's go back over to our IDE and try that out. So, now over to the code for the crawl for AAI rag MCP server, which I'll have a link to this in the description, by the way. If you want to try all this out for yourself right now, you can. It is

**[0:12:25]** completely open source and available for you. And so, I want to walk you through some of the functions that I've added to the MCP server that we're going to give to Cloud Code in a second to explore the knowledge graph. And trust me, it makes a big difference. It's actually so cool.

**[0:12:40]** And so if you want to use the knowledger graph part of this MCP server and your environment variables, you just have to set use knowledge graph to true and then enter in your own credentials for your own instance of Neo4j, which is very easy to get this up and running hosting

**[0:12:54]** it yourself by the way. And because I have a very comprehensive readme here, instructions for that are included. So you can install Neo4j either through my local AI package, which I would highly recommend. It's one of the services that comes in the package or you can install Neo4j desktop very easily as well. So

**[0:13:12]** get that installed, set up the credentials here and then you will be good to go. So now I just want to dive really quickly into the new tools that I have added to this MCP server. So the first one is a tool literally to run the hallucination check script that I showed

**[0:13:27]** you earlier. But now instead of the output coming to us, it's going right back to the AI coding assistant because it's using this MCP server. So it can self-correct like it knows the mistakes that it made then and you just have to give it a script path. So it will write

**[0:13:40]** out a script and then pass that path in. And keep in mind if you're using the Docker version of this MCP, this doesn't work very well because the script isn't going to be in the container. Um but there are some other tools that I've got that still make it so that you can

**[0:13:53]** explore the knowledge graph. So this is the first one here. And I know this script is getting really long. I am going to be working on refactoring this. But the second tool that I'm giving is one to query the knowledge graph. And so you can explore different classes, uh,

**[0:14:07]** different methods, even allowing the AI coding assistant to write custom queries to explore the knowledge graph in really custom ways. There is a lot of functionality baked into this. It can run these commands. So it determines the command based on this documentation that helps it understand how to explore the

**[0:14:23]** knowledge graph. So it can do things like list the methods that are available for the agent class. And so if we get this hallucination reported back where it's like oh this is an invalid argument then it can go and look what are the valid arguments and query the knowledge

**[0:14:37]** graph in that way. And then the very last tool that I've given I got to scroll down here because there's a lot of functionality to make all this possible. The very last tool that I have is one to parse a GitHub repository. So you just send in the GitHub repo as long

**[0:14:51]** as it ends in.get. You basically tell the AI coding assistant like I want to parse this GitHub repo into the knowledge graph and you give it the repo and then it'll go ahead and call this tool with the right repo URL and then add that into the knowledge graph. And

**[0:15:05]** this entire process of indexing and storing a repository takes less than 30 seconds usually depending on the size of the repo because there's no large language model being used here. It's all deterministic code that parses through all the files in the repo. So it'll actually like clone it locally in a

**[0:15:21]** temporary directory and then process everything and store it in the knowledge graph. And so you can do everything here. You can add in a repo and then you can start having your AI coding assistant query it and check for hallucinations using it. So that is everything that I've added to this

**[0:15:35]** server. Now let's actually bring this into cloud code and build an agent with it. All right. So here we are in my cloud code that I have loaded up in a terminal in my windsurf. And this is my command to add the crawl for AAI rag MCP server that I currently have running in

**[0:15:50]** a terminal on my other monitor here. I've got instructions in the readme for how to set this up. It'll run on port 8051 by default. I'm just running this on port 8052. And so I'll run this command to add the server. And then I can run the command claude MCP list to

**[0:16:05]** ensure that this is the one that I have added. And I have a blank slate here. So this is the only MCP server that I'm currently using in Claude. So now we can load up Claude and we can start having it create our Piantic AI agent grounded in the truth that we have for rag and

**[0:16:20]** the knowledge graph through the MCP server. But before we kick things off here, I want to show you the instructions that I have through the claw.md file because I have given a very specific and in-depth scope of work for claw to knock out for me. I'm starting out by telling it that it's an AI coding

**[0:16:38]** assistant tasked with creating a robust pyantic AI agent. And then I give it a lot of information towards the end for what exactly that needs to look like. And I just used a large language model to help me generate this whole thing. But the most important part is I define

**[0:16:51]** a workflow here for how to leverage the crawl for AI rag mcp server properly. For example, for phase one, we have to make sure that we have the sources available for pideantic AI in both our knowledge base for rag and also our knowledge graph for the hallucination detection. So we make sure that that's

**[0:17:10]** all set up and then we go on to our research phase. So we're searching through code examples. We're performing rag to look over the padantic AI documentation and then we do a deeper dive for step three querying the knowledge graph to get specific methods and attributes on things like the agent

**[0:17:25]** class for example. So we start higher level with the podantic AI docs. Then we use the knowledge graph to get more granular given some of the classes that we have researched from the documentation. So this MCP server is just a beautiful thing. It allows us to have this flow for our agent to start

**[0:17:41]** high level and then get more granular with its research, finally going on to our fifth step here of generating the code and then validating it, checking for hallucinations, writing unit tests and iterating on that. So it'll self-correct as well. So I'll kick off a task here for Claude to create this

**[0:17:57]** agent. It'll go through all of these steps without me having to intervene at all. And then by the end of it, it's going to have self validated. So we will have a perfectly working agent and it's not absolutely guaranteed but hallucinations are definitely kept to a minimum now when we follow a process

**[0:18:15]** like this that is certainly made possible mostly just by this MCP server that we have and because the instructions are so clear here my actual prompt claw can be very basic. I'll just tell it to follow the plan to build the paidantic AI agent. I don't have to be

**[0:18:31]** specific in my prompt because I already am in the claw.md file. And so the first thing that Claude is going to do is it's going to generate a bunch of to-dos. So there we go. We got a list of everything that we have to knock out. And so the

**[0:18:43]** first thing that it needs to do is check for the sources and the knowledge graph. And so it's going to do that. So starting with step one here, we'll wait a little bit and it'll make its first call. There we go. So we are calling the query knowledge graph with the command

**[0:18:57]** for repos. And also uh if you want to make it so that it approves things by default automatically, you can just add into the settings.local.json that'll be created here in yourcloud folder. Otherwise, you'll have to approve these actions yourself. And so yeah, go ahead and do all that. Approve anything that

**[0:19:14]** you need to. But yeah, let me actually go down and see what it's doing so far. So yeah, so first it got a sense of what's actually available. Making sure that padantic is in the knowledge graph and our knowledge base. Now it is performing rag queries. Take a look at

**[0:19:26]** that. exploring the documentation, looking at code examples. Now, it's moving on to step three, diving into the knowledge graph as well, looking at specific classes and things like that. So, there we go. Quering the knowledge graph with the class of agent. This is just so beautiful watching it unfold.

**[0:19:42]** And it is going to take a while because it's doing a lot of these queries here, but they're all very fast and they don't add that much context to our prompt. And so, we're also not just bloating this conversation here. Um, but since it will take a couple of minutes to build out

**[0:19:55]** this agent fully, what I'm going to do is pause and come back once our agent is complete and we should have very few hopefully zero hallucinations. And there we go. Just a few minutes later and cloud code with the help of rag and our knowledge graph has generated the entire

**[0:20:13]** agent first try and it is working. We'll see this in a little bit, but it followed this entire process. So doing some of the initial searching that we saw with code examples and rag and knowledge graphs already. And then going down, it actually implemented the code right here. And then it does some

**[0:20:29]** validations and selfcorrection as well. So I won't scroll through everything here, but I'll go ahead and do control J to exit out of CL code. Take a look at the agent that it built. And it's got types with pideantic. It created the agent really, really well. We got a

**[0:20:41]** dynamic system prompt, and we're injecting multiple tools into the agent. This is really solid pyantic AI code. And going to the terminal here, I already configured my environment variables with the OpenAI API key. And I set up my virtual environment. Now I can go ahead and execute this agent. Take a

**[0:20:57]** look at this hallucinationfree pyantic AI agent. And so we have a couple of test queries that it runs here. And I don't think it's actually fetching the weather in London. This is a mock weather tool, but it's still showing that we're creating multiple tools, adding them into our agent, and then

**[0:21:13]** using the agent to figure out the tool to use based on the query. This is working so so well. Like, man, I'm impressed. Like, first try, and this is a pretty simple agent. Like, I'm mainly building this for a demo purpose here, but it isn't like extremely trivial.

**[0:21:29]** Like, there is a good amount of code that is generated here for this agent, like over 300 lines. And so, it's really cool that we were able to do this first shot. I mean, more than cool. This is like amazing to me. And um I will say that the confidence score that it gives

**[0:21:43]** is kind of weird. I think it's because in my claw.md I didn't really make the best instructions. So I think it's thinking that when I say no hallucinations, it's actually for the agent, not for the coding process. So that's on me. I probably could have refined this quite a

**[0:21:56]** bit more. It is really important to spend a lot of time refining your claw.md. But still, this is working really, really well. And it's able to do this thanks to being grounded in the truth of pinantic AI both with rag and by our knowledge graph both as a part of

**[0:22:11]** our crawl for AI rag MCP server. Plus as a bonus we can run the hallucination detector ourselves just like we did earlier at the start of this video. So I'm giving it the path now to this hallucination free agent. It's kind of funny that it call that. But this is the

**[0:22:26]** agent that Claude Code generated for me. I'll run this manually through the hallucination detector so we can take a look. And there we go. We have 12 valid uses of panenti in the script and zero hallucinations. Things are looking really, really good. So that is everything that I wanted to show you

**[0:22:43]** with knowledge graphs and rag with my crawl for AI rag mcp server. Everything that I'm going to be building into archon with the huge version two overhaul that is in the works right now. So definitely stay tuned for that. I have huge plans to turn Archon into the

**[0:22:58]** best MCP server in the world for AI coding, both with knowledge and task management. And we are getting insane results right now, even as we're just testing out Archon as we're building it in the ver very, very early alpha stages. And so, if you appreciated this video and I sparked your imagination or

**[0:23:17]** I'm just intriguing you with Archon and Rag and knowledge graphs, definitely give me a like and a subscribe. I would appreciate that a lot. And with that, I will see you in the next
