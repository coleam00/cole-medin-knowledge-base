---
type: raw-transcript
title: "Claude Code's Real Purpose (It's Bigger Than You Think)"
youtube_id: j2tI3YGVEz0
url: https://www.youtube.com/watch?v=j2tI3YGVEz0
slug: claude-codes-real-purpose-its-bigger-than-you-think
published: 2025-10-15
duration: "0:21:31"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Did you know that you can use Claude Code for a lot more than just coding? Thanks to Anthropic's Claude Agent SDK within our own automations and workflows, we can build Cloud Code right in. It unlocks an insane number of possibilities. And I know that's a lot to unpack, but that's what I'm going to

**[0:00:18]** do for you in this video. But take a look at this. First, I have my Claude code integrated directly in Telegram. And behind the scenes, I have it working on my Obsidian vault. This is my second brain, my knowledge base where I do all my note-taking and my YouTube scripting.

**[0:00:33]** And so I can have Cloud Code help me with that. And since it's Telegram, I've got it on my phone as well. So take a look at this. I'll send a message on my phone. You'll see it on my computer as well. And then we'll see Cloud Code in

**[0:00:43]** action. So add a small bullet point list of potential personal AI automations to my AI automations you need now script. Okay, cool. So I'll send this in. There's the message. And then Cloud Code gets right to work. You can see it typing right here. So, I'll go over to

**[0:00:59]** my Obsidian Vault, and in just a second, we'll see a bullet point list pop up. And boom, there we go. Potential personal AI automations. And of course, Cloud Code has responded back to us in Telegram as well, even listing out the tools that it used to find the file,

**[0:01:15]** read it, and edit it, just like you would see in the Cloud Code terminal or the terminal for any AI coding assistant. But I won't even stop there. I also integrated Cloud Code directly in Obsidian. And so we have this chat interface using the co-pilot community plugin and I can talk to my cloud code

**[0:01:32]** right here as well. So I can send in a request like add a couple more ideas to the potential personal AI automations in the same script that I edited in Telegram. And so we'll see that right now. And there we go. We got the travel planning assistant. It added a few more

**[0:01:46]** as well. Looking really, really good. And so I'm able to manage my notes and knowledge and everything with the help of Cloud Code in these different applications that I can even use on my phone. It is such an incredible thing. And this is all thanks to the fact that

**[0:02:00]** Claude Code is really just a simple yet powerful wrapper on top of Claude. In the article where Anthropic released the Cloud Agent SDK, they called it the agent harness that powers Claude Code. And they've actually been using cloud code for a lot more than just coding for a while now for things like deep

**[0:02:19]** research, video creation, note takingaking, like what I was doing with Telegram and Obsidian. And so a couple weeks ago, they renamed the Cloud Code SDK to the Cloud Agent SDK because it really is this engine that can power any of our AI agents we want to build. And

**[0:02:35]** that's what I'm going to show you how to do in this video. I'll show you how I did that Telegram and Obsidian integration. I'll even show you how in code like in our Python code here, we can create our own custom AI coding assistants to define our own system

**[0:02:49]** prompts and build into our own workflows, even build our own eval monitoring solutions. Like I have a Sentry integration that I'll show you how to build where you can watch when we execute our Cloud Code agents remotely. We can see all the decisions that it decided to make, things like our token

**[0:03:06]** usage. There's just so much that I have for you in this video. And so I'm going to start by giving you just the basics of the agent SDK. How do you build with it? Then we'll get into some of these integrations. I've got a lot in store for you here. So with that, let's go

**[0:03:20]** ahead and get started with the cloud agent SDK. So I'll have a link in the description to this repository where I have all of my demos and integrations for things like Telegram and Obsidian. And a lot of what I have created here is just based on the claude agent SDK

**[0:03:36]** documentation which I will also have linked in the description. And I will say claude code is definitely the agentic coding leader right now. A lot of other tools are going to be copying them and building their own SDKs. Like we already have the codeex SDK which just unfortunately doesn't have the best

**[0:03:53]** documentation right now. But even if you don't like cloud code for whatever reason because there's rate limiting issues or pricing or whatever, just know that like what we're covering today is definitely going to be possible in the near future with a lot of different AI coding assistants. And so going down in

**[0:04:08]** their quick start here, we can see that in just a few lines of Python code, we can create our own custom instance of cloud code. We can set our own MCP servers and permission and system prompt and then we can query it. And what you're looking at right here is

**[0:04:23]** essentially what I have in the first quick start for you. So you can go through this read me or just follow along right now. In the quick start, I have this simple query example. Literally the most basic script I could possibly create for you. So first we define our options for our own agent,

**[0:04:39]** which I'm only specifying my system prompt, but if you look at the docs, you can see all the different things that we can change to really customize the agent for us. And then I'm going to query just by calling the query function that I'm importing from the cloud agent SDK. Just

**[0:04:54]** a simple Python package. And then I'm going to loop through all of the messages that it gives me back and print those out to my terminal. And so the way that this works is very similar to the Claude Code CLI. So I'll pull that up as a reference here. When we use the CLI

**[0:05:10]** for any AI coding assistant, we send in our request and we get these blocks back. It doesn't stream the tokens out to us in real time. It just sends us text block by block like a little bit of information recognizing our request. Then it's going to do some web search.

**[0:05:25]** So this is a block. And then it acknowledges the web search. So that is another block. And then it edits a couple of files. Like each one of the messages or actions that it takes is a single block that we receive as the user. And so it works the exact same

**[0:05:39]** way. So when we loop over the messages here, we're looping over those blocks of information or action that cloud code is doing based on the query that we send in. And so let's see this in action. I'll go back over to my terminal here and I'll run the simple query example.

**[0:05:56]** And in just a little bit, we're we'll get a couple of blocks back starting with the system prompt. And yep, so there's our system prompt. And then we'll see the response that we get from coding assistant. So I asked it a very simple question and we get a very simple

**[0:06:11]** response. And then claude code with the agent SDK also always sends a final result message. So that's our signal that we are done interacting with cloud code for this turn in our code. And by the way, the way that authentication works with the cloud agent SDK is it

**[0:06:28]** will default to using your enthropic API key and your credits there if you have it set as an environment variable. But if you don't set your anthropic API key, which honestly I'd recommend not doing that, then you can use your cloud subscription. So the exact same authentication that you've gone through

**[0:06:45]** already if you're using cloud code. So I have my max plan. I'm not paying any API credits for everything I'm showing you in this video. I just had to run login, which I've already done this because I'm using cloud code on my desktop. Now, the other quick start example I want to show

**[0:07:00]** you is how we can build our own custom CLI using the cloud agent SDK. So, it's going to be pretty much what we do with cloud code normally, but I'm showing you that like now it's our own Python code, our own custom agent. So, I have a little bit of logic here for managing

**[0:07:17]** the conversation history. Not super important. The main thing that I want to cover here is the primary chat loop. So we define our options just like we saw in the very basic example for the agent SDK. So we have things like our current working directory where we looking at

**[0:07:32]** files. We've got our system prompt that you can customize. And then also another thing I wanted to show you is that we can set up granular permission management. The tools that we're allowing our agent to use. And this is also where you can set other things for MCP servers. By the way, more on that in

**[0:07:47]** a little bit. So yeah, we create our options and then we create an instance of our client. And then we just call that query function again. So client.query sending in the latest user prompt. And then just like before, we are looping through all of those message blocks that we get when we are receiving

**[0:08:04]** that response from the cloud agent SDK client. We're printing out regular text in one way and then the tool usage in another way. So we can also see live in the terminal the tools that cloud code is deciding to use just like we'd see in their official CLI. So there we go. It's

**[0:08:22]** just cool that I can even say official CLI. Like we're building our own CLI right here. So I'm going to start this here. Python simple CLI.py. And it's not as pretty as the official CLI. But the point here is just to show you how easy it is to use cloud code

**[0:08:37]** programmatically. So I can say hello for example, just get a really simple response back. And then I can also say something like what files do I have in my directory? So having it use probably a bash tool here. So yep, there we go. using the bash tool to check the files

**[0:08:52]** in my directory and then in a second we'll get our response back. There we go. We have the following files sessions simple cli.py simple query example. So basically the directory that I'm giving it access to right now if we look at the settings is just the current directory

**[0:09:06]** that we're in. So this quick start folder right here. So it's just listing out everything that we got here. And I could go and make file changes here. I can do everything I can do with cloud code assuming I'm giving it the necessary permissions. So that's a quick

**[0:09:20]** start how we use cloud code programmatically. Now I want to cover with you the fun stuff. Let's actually get into the integrations now with things like Obsidian and Telegram and see how powerful this really is cuz it's cool to see us customize an agent in a CLI. But at this point it's not anything

**[0:09:36]** really special compared to what we've already had. So now that's what I want to show you. So the first integration I have for you is the Obsidian one which I'm just stoked for. I've been doing so much with Obsidian recently. Actually moving away from a lot of different

**[0:09:50]** applications to it. If you're not familiar with Obsidian, it is a completely free and local solution for knowledge management and note-taking. It's kind of like my second brain. I'm using this every single day now. A lot of things that are similar to Notion, probably the best comparison that I can

**[0:10:06]** make that you're probably familiar with. And so they also have a bunch of open source community plugins. So you can enable that and go to the co-pilot one specifically. This is the one that I installed that gives me this interface that I can connect to really any LLM

**[0:10:21]** that I want or my own custom agent. That's what I'm going to be running right here in the demo that I gave earlier. And so you can follow the instructions here to get everything fully set up. I'm not going to cover that in detail right now. Uh just a

**[0:10:33]** couple of steps that you need to connect your own custom agent once you're running this API that I have around the cloud agent SDK. So cool. Let me actually run this right now. So, I'll go back to my terminal here. I'm within the Obsidian Integration folder. I'll just

**[0:10:47]** run Python API server.py. Fall is working. Well, then you have it running on port 803. And I'll show you the code for this really quickly. Like, I don't want to focus on code a ton in this video, but I still want to show you specifically how I'm using the Cloud Agent SDK in Python

**[0:11:04]** code. I've even got an MCP server for this one as well. It's pretty cool. So, okay, let's go down to the chat completions endpoint. So, I'm using OpenAI API compatibility to create this API endpoint in a way where I can automatically hook into it with that C-pilot extension that I have installed

**[0:11:22]** in Obsidian. And so, we get the conversation history that's sent in from Obsidian. We format it in the way that we need to send into the cloud agent SDK. And then we define our options just like we've been doing with the quick starts here. So, I have my current

**[0:11:36]** working directory, which this is going to obviously be my Obsidian vault. I have my system prompt, the allowed tools, and then I also have an MCP server connected here as well. So, this isn't something I've shown yet, but the same way that you set up MCP servers in

**[0:11:52]** your coding assistance or cloud desktop or whatever, you can set those up as JSON config for your own custom cloud agent SDK agents as well. Very, very easy. This is a standard IO server that I use quite a bit called sequential thinking. It basically just gives instructions to the coding assistant or

**[0:12:09]** my agent in this case how to think through something step by step. Um, so I just get more thinking tokens out of my LLM. And so I set up all my options, pass it in, and then I create a client just like we did in the other example,

**[0:12:22]** call the query, and then I'm going to go through all of the message blocks that I've received. And I'm specifically converting them into a format that I can stream out to Obsidian so that I get the output on in my Obsidian vault just in the the right-h hand chat bar right

**[0:12:40]** here. So yeah, pretty simple overall. I mean, there's a good amount of code that goes into the OpenAI converter here that I don't need to cover. You can take a look at that, throw this into your AI coding assistant if you really want to dive in. But the main thing I wanted to

**[0:12:53]** show you is just how easy it is to use our own agents and then set up all the things that we want like permissions and MCP servers and system prompts and everything. It is a beautiful thing. So, we can go back into Obsidian here. I'll start a new conversation and I'll just

**[0:13:07]** say my potential personal AI automation list is too long. Make it shorter. So really not providing much context at all. So it's going to have to search and find this list and it's going to have to think about how to shrink it and then finally edit the file to do so. So I'll

**[0:13:20]** come back once it's done that. All right, there we go. Much nicer. That was getting way too long. And then we get the response on the right hand side as well. Now this isn't the most perfect integration. I don't have this as a production ready thing for you to use

**[0:13:33]** right now. It doesn't print out the blocks one by one and so it just kind of throws everything to me at the end here. But it's working great. It made the edits. It was able to find my file and know exactly what to change. Really, really neat. So, that is the Obsidian

**[0:13:48]** integration. And it's just cool to see Claude Code doing something other than coding. It's helping me with knowledge management and YouTube scripting. It's really, really neat. And the thing that I'm taking advantage of here that Claude Code gives me that other agents don't is the really powerful capabilities around

**[0:14:03]** searching through files, reading files, and editing files. That's the agentic wrapper on top of claude that I get to leverage in my own code. Now, so this entire video I've been focusing on everything except for coding with the Claude agent SDK. But honestly, probably the most powerful use case is creating

**[0:14:21]** our own custom AI coding assistance with the tooling that we have here. And so going back to the Telegram integration now, before I was just using this to work on my Obsidian Vault, but I'm going to show you how with my phone now, I can kick off remote Claude code tasks with

**[0:14:38]** my own custom agent with all its own configuration. And so this is the last example that I have in the repository for you. And I've got two examples specifically. I've got one with the Century integration and one without. So there's two things that I want to show you with this. First of all, I want to

**[0:14:55]** show you how easy it is to build cla code into any application we want. Like I'm picking Telegram here, but this could be Slack, it could be GitHub, it could be email, whatever you want. And then the other thing with Sentry I want to show you is how when we have Cloud

**[0:15:09]** Code built into our own workflows and automations, we get to set up our own monitoring solutions, which makes it very easy for us to go back later, especially when we're using remote coding, and validate the work that's done with our coding assistant. and we can actually see the decisions that it

**[0:15:25]** has decided to make. And so before I execute this example, I want to show you what that looks like really quick. So I'm within my Sentry dashboard here and they have documentation on how to instrument your own AI agents with Sentry, which is what I did to really

**[0:15:40]** just get Claude code hooked into Sentry. And then I have this amazing dashboard that I showed you just really briefly earlier where we have all these traces. So every single time we interact with Claude code, it's a single trace that we can click into to see the response and

**[0:15:57]** the prompt that went into it. We can look at the different tools that it executed. Like in this case, it decided to um edit the bot.py file, for example. We can see the tokens usage and the number of tool calls for each execution, how long it took. Like all this

**[0:16:14]** visibility we get is very very important. If you're actually serious about building your own AI coding assistance and your own AI coding workflows, you need this kind of tracing and that's what Sentry gives us. So very very cool. So with that going into the implementation here, it's pretty simple

**[0:16:31]** overall. There's a lot of different custom commands that I built into Telegram. So that's neat. But the main thing is I have this function to handle any message that comes in through the Telegram API that is sent to my bot. And this could be a Slack bot. It could be a

**[0:16:47]** Gmail account that I have. Like I just need to have some kind of trigger to watch for messages. And then I can pass on the request to Claude code. So going down here, I set up my options for the Cloud Agent SDK just like I've been doing in the past. And then I call it

**[0:17:02]** right here. So, I get my client and I query and then I go through all the message blocks. I receive them and then I'm going to send them all back out to Telegram. Very easy. The code took me a single shot to build with Claude code. By the way, I did not iterate a single

**[0:17:19]** time on building this entire bot for Telegram and Claude Code. It was so so cool. So, this is my bot. Now, here's what I'm going to do. I have this running in my terminal on my other monitor already. And I'm going to change my directory. So, one of the nifty

**[0:17:34]** commands I have because this is my own custom agent. I can do all these things. I can do set current working directory. I can go back into and copy this path right here. And I'm going to paste it in right here. Let me add a space and delete this part. Okay. So, what I'm

**[0:17:50]** doing with this command is I am changing live where my remote cloud code is pointing to on my computer. So now it's ready to make changes in this repository that we've been playing with today. And so what I'm going to do, this is actually so nuts. I'm going to from my

**[0:18:07]** phone ask Claude Code to improve itself, my own custom agent. I'm going to have it edit its own file to add an MCP server. And so back on my phone here, I'm saying add the sequential thinking MCP server to my Claude agent. And I'm going to be editing this file that I

**[0:18:25]** just showed you, the Telegram bot with Sentry. And I'm also going to be telling it to look at the previous example with the Obsidian integration because that's where I already connected the sequential thinking. So, all right, I'll send this in. Boom. And it's typing. So, it's going away at the request already. And

**[0:18:41]** it's going to build out my sequential thinking MCP. So, in just a second here, I'm going to actually go to the part it's going to edit because it's going to edit the options. So, in just a second, we'll see it change this live. And the request started from my phone. And it's

**[0:18:54]** going and it's going. And there we go. All right. We've added the sequential thinking MCP and the permissions as well. So, that doesn't have to ask me when it wants to use any of the tools in this server. That is just so so cool. And yep, I see on my phone that I got

**[0:19:10]** the response. So, let's go back to Telegram. Awesome. So, we got all the blocks sent to us at once. It's similar to Obsidian where I probably could refine this more, but yeah, it did a lot of tool calls to accomplish this. So, it read through this file a bunch with glob

**[0:19:23]** and read and then finally it made that edit at the end to update our configuration. That is just so cool. And so, now it literally fixed itself or I should say improved itself. So, I can go back to my terminal here. I can run it again and then I can actually ask it

**[0:19:37]** like use sequential thinking to give me five fun facts about claude code. All right. So, I'll go ahead and send this in, and I'll come back once it comes back with its request, cuz it does take quite a while when it thinks through something step by step. All right,

**[0:19:51]** perfect. It took its sweet time, but finally, we have our response. So, here are our five fun facts. And then, yeah, it used the sequential thinking many, many times because every time it wants to produce a thought, it calls the server again. But yeah, this is freaking awesome. We literally used our own cloud

**[0:20:08]** agent SDK agent to improve itself. And I didn't even have to do it right from my computer. We can also go back into Sentry here. I'll refresh and we can see the logs for this so that if we weren't watching the live, we can go back and validate that everything actually makes

**[0:20:22]** sense. So yeah, let me click into this one here and we can see all of the tool executions for sequential thinking. This is I mean pretty much what we saw in Telegram, but we can also dive in more to see the different tool inputs for example. So we can actually dig into the

**[0:20:36]** parameters it sent to all the tool calls for the sequential thinking MCP. So ton of visibility, ton of customizability. We can integrate with any application we want like email, telegram, slack, whatever. This is just a beautiful playground. So that is everything that I got for you on the claude agent SDK and

**[0:20:54]** building our own custom agents. And I really do think this is the future of AI coding where we take this lightweight wrapper like Claude code and we use it to programmatically define our own custom agents to build them into our code bases, our workflows to really suit our needs the best because when we use a

**[0:21:12]** tool out of the box, we can never customize it as much as we'd want compared to when we actually get to write the code. And I hope that I enlighten you to that today. So, if you appreciate this video and you're looking forward to more things on AI agents and

**[0:21:26]** AI coding, I would really appreciate a like and a subscribe.
