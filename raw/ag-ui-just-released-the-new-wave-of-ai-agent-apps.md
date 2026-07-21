---
type: raw-transcript
title: "AG-UI Just Released: The NEW WAVE of AI Agent Apps"
youtube_id: BFWviieMyGw
url: https://www.youtube.com/watch?v=BFWviieMyGw
slug: ag-ui-just-released-the-new-wave-of-ai-agent-apps
published: 2025-05-21
duration: "0:21:40"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** 2025 has definitely been the year of AI agents, but even more than that, it's been the year of agent protocols like Anthropic's MCP, making it so easy to connect tools to our agents, or Google's A2A, making it very seamless to connect agents to other agents. But as powerful

**[0:00:18]** as these protocols are, there's still a very big missing piece. Because if we want our users to be able to interact with our agents, we need a front end some way to turn our agent into a full application. But until now, there hasn't been a standard to very easily connect

**[0:00:33]** our agents to any front end like we can do with tools and other agents. But that has all changed now with the introduction of AGUI. This is a protocol for connecting your agents to your front end to your users in a very standard way. And just like MCP and A2A, I think

**[0:00:50]** this is really going to shape up to be an absolute gamecher. So right now, I'll introduce you to AGUI and show you how to use it. It is definitely worth investing your time learning this protocol right now because it really is the missing piece to take your agents to

**[0:01:04]** that next level, turning them into full applications. So, let's go ahead and dive right into it. So, here is the official announcement for AGUI that was developed by the CopilotKit team, which if you didn't know, Copilot Kit is an open-source front-end library for building agentic applications. So, it

**[0:01:21]** very much makes sense that they would be the team to build out this kind of standard to connect our frontends to agents. And this graphic shows really nicely what it looks like. We have AGUI which is a middleman just like MCP in between our application built with something like React and then our AI

**[0:01:37]** agents built with something like Langraph or Crew AI or Pyantic AI. And so it's a protocol just to make this connection very seamless just like we have with MCP and A2A. And this is so powerful because it's our way to connect our agents to users. And that is crucial

**[0:01:54]** because most agents in general and I I like this. They actually talk about this here. They talk about autonomous versus conversational agents. And so something like copilot kit and agui is not going to be useful if we just have an agent running entirely autonomously just doing things behind the scenes. But most

**[0:02:11]** agents you want to have some way for users to work alongside them. Especially for things like human in the loop just making sure that we are still a part of the process whatever our agent is doing. And so we almost always want a front end to work with our agents. But until we

**[0:02:26]** had AGUI, that wasn't very easy. There are a lot of challenges that come with building a front end connecting to our agent without some kind of standard. For example, it's definitely an expectation at this point that your AI agent will produce the output in real time. It'll actually look like the agent is typing

**[0:02:43]** out the answer to you, just like you've seen in things like Claude or GPT. But that isn't very trivial to set up. You need a way to have your API endpoint that's running your agent stream out those tokens in real time to your front end. And you have to handle that in your

**[0:02:58]** front end as well. And then another good example, tool orchestration. Working with different tools that your agent will use. The UI oftentimes need to show progress and the results of using these tools. There's a lot of components that go into even a single execution of an agent that you want to display out to

**[0:03:14]** your front end. A lot of other things here as well. I think the other thing that's really worth hitting on is what they call the framework sprawl. I think that's a really good way to put it. There's so many different ways we can build our agents in the back end with

**[0:03:26]** Langchain or Crew AI or Mao. There's so many different examples, but they all work in slightly different ways. We have to connect our UI into agents built with these frameworks in slightly different ways. We have to reinvent adapters like they said, handle different edge cases that just come up from using these

**[0:03:42]** different frameworks. But when we have something like AGUI where we can have just one set standard now that's a middleman between the front ends in these different frameworks now we have to worry about that a lot less in our frontends. Everything is just much simpler when we develop it. And the best

**[0:03:57]** part is AGUI is completely open- source and it's a standard where we're not relying on a specific framework. So just like with MCP anthropic built the model context protocol but it's not like we have to use cloud for our LLM. Same thing with AGUI. It was built by

**[0:04:13]** Cop-ilot Kit, but we can build any front end with any framework and connect that to any agent. And here's how it works. We have our user that interacts with our application built with something like React. And then we have that middleman that I was talking about. This is AGUI

**[0:04:27]** that will then connect us to our AI agents. And every time we have some kind of operation that our agent performs like it streams out some text or it makes a tool call, we have these standard events that we emit out through AGUI back to our front end. And so our

**[0:04:42]** front end has this very standard way to display everything that the agent is doing. And that's what solves a lot of these problems that we have with real-time streaming and tool orchestration and framework spall. We just now have to rely on these events coming into our front end, displaying

**[0:04:56]** those out however we want using something like Copilot Kit if we want to make that easier for the actual front-end development. So that's how AGUI works as a whole. But now I want to get really practical with you, actually build out a full example so you can see

**[0:05:09]** this in action. So, in the official documentation for AGUI, which I'll link to in the description of this video they cover both how to build an AI agent in the back end that works with this protocol, and then they also show you how to build front-end applications that

**[0:05:25]** work with AGUI so we can connect our agents to our users. And I'm going to walk you through both. I'm going to go through the quick start with you and show you at a very fundamental level how AGUI works. And then I'll even show you how to build agents in the back end with

**[0:05:39]** AGUI, how we can use any framework we want as well. And this connect to AGUI page is going to be the main one that I'll walk you through to get our demo up so you can see at a very foundational level how this protocol works. And so you can follow along with this as well

**[0:05:53]** if you want to play around with the demo yourself, dive into it, and just see how you can build out with AGY. So there are some prerequisites that you need with Node.js and npm. And then also we'll be using OpenAI for our LLM. And then you can go through these instructions here

**[0:06:07]** to clone this repo that has the example. We can install everything and run it. And then they walk through the core code components as well. So this is the demo that I have spun up right now. And you can do the same thing in just like a minute. Like it's super fast. And we can

**[0:06:20]** work with a couple of the examples that they have here for us to see AGUI in action. And this is all integrated with Copilot Kit. But again, we don't have to use Copilot Kit with AGUI. It just makes things very simple for us. And so for this first example here, I can just get

**[0:06:35]** a basic response from the LLM. So you can see it streamed out to us. But then this is also an example of using AGUI for front-end tools, as in we get the response from the agent and that will dictate something that we would change in our front end. Like in this case, I

**[0:06:49]** can say change the background to red. And so we'll get a response from our backend that tells it to update the background color. Take a look at that. We can say now change it to blue. And boom, there we go. nice and fast and this is not a very trivial

**[0:07:04]** implementation like this is a basic example but having this kind of interaction between our backend and tools in our front end is not super basic and let's just try another one as well let's do the toolbased generative UI so in this case we'll talk to our agent and the output is going to be

**[0:07:18]** interactable for us to then also change what we see right here so I'll say generate a haiku about AI and then boom we get our haiku and then I can interact with the tool call in the front end here to apply it and then it's now going to

**[0:07:32]** update another state that I have within the front end. So just a couple of examples here showing at a very high level how we can make our AI agent super interactable with tool calls and everything right within our front end. And this is the kind of thing that if

**[0:07:45]** you don't have something like AGUI, it's not going to be that easy. The sponsor of today's video is Lutra. It's a very userfriendly way to create automations with natural language. You interact with it just like chat GBT or Claude except there are hundreds of integrations to make it way more powerful. And it can in

**[0:08:03]** real time build customcoded integrations to work with these different services. And then all of these integrations that you combine together for these automations that you create can be saved to use in future conversations and set up as scheduled tasks. It's very powerful. And Lutra integrated with MCP recently. So, we can now bring MCP

**[0:08:23]** servers into our automations as well. Once you're assigned in Lutra, you can go to the custom integrations page and hook in MCP servers. You can hook into any MCP server that you built yourself running remotely or use any of these recommended ones. Like I can go into a

**[0:08:38]** sauna, use this server, then I just have to authorize my account to connect it and I can start using the MCP server in all of my Lutra automations. For example, I can ask Lutra to create a new project for me in ASA and put a task in it as well. And so I'll send this in and

**[0:08:54]** it's going to right away leverage the MCP server and it's going to write custom code to use the different tools in this server. That's how I can integrate with other things along with this MCP server at the exact same time. So it'll reason and then start taking these actions. And so I'll pause and

**[0:09:09]** come back once it has completed. And boom, Lutra has created our project and task. I can even see this in ASA. I got my task here to create spicy mango chicken and I can save this automation now. It generated the code for it. I can reuse this later in future

**[0:09:23]** conversations. Very, very powerful. So I'll have a link in the description to Lutra. I would definitely recommend checking them out if you want to automate a bunch of tasks in a very conversational way just with natural language. Going back to their example in the documentation here on connecting to

**[0:09:38]** AGUI, let's cover the core components that make all of this possible. This is so important to understand. And then I have this demo up and running right now like I just showed you. So I'll go into my IDE and show you that code. Also some additions that I made to take this even

**[0:09:53]** further. And so like I said, the core of AGUI is all of these events that our backend emits to our front end. And they have an example of this right here. So in this case, we aren't actually using a large language model. They're just simulating what an Asian execution will

**[0:10:09]** look like. But we emit this event saying that the run has started. And then we have our thread ID so we can keep track of the specific conversation. We have an ID for this current execution itself. So we have a lot of that metadata that's passed to the agent as well which is

**[0:10:23]** super important. So we can do things like fetch the conversation history if we need. And then we move on to say that we are starting a message. So we're streaming out that response. Here's some of the content. And then here is the end of the message. And at the very end of

**[0:10:36]** the agent execution we'll emit this final event as well saying that the run is finished. And so that's what it looks like when we don't use an LLM. But when we do want to use an LLM, they have an example that I applied here that takes it further. So in this case, we are

**[0:10:50]** actually using GPT 4.1 Mini to drive our conversation. And this is exactly what we saw in the demo just a couple of minutes ago. And so we output this event first. And let me zoom in on this just so it's very easy for you to see. We output our event saying that the run has

**[0:11:06]** started. Then we use the OpenAI client to start a message response from GPT4.1 Minion and we're giving it some tools as well to do things like change the background color. So if we want to change the background color, the LLM will output that tool and that'll be one

**[0:11:21]** of the things that we stream out to the front end. And I'll get into that in a second here. But yeah, going up back to the top here, we input all of our messages. So we get the conversation history passed in from the front end with AGUI as well. And then we start to

**[0:11:34]** get our response. And so we're going to loop over all the chunks that we're getting back as we're getting the output in real time from GBT4.1 Mini. And we're just going to output each of these chunks as they come in. So we're returning the delta here as in these are

**[0:11:49]** the most recent chunks that were produced. So our front end can build up that response over time, displaying it in real time to the user. And then for any tool calls that happen, we're doing the exact same thing, but instead of it being a text message chunk event, it is

**[0:12:04]** a tool call chunk event. So we're telling the front end that all the parameters here are related to a tool call, like changing the color of our background. And then once all this is complete, so we're just going through this loop of getting everything from the agent response, then we'll just send

**[0:12:18]** that last message just like we saw in the basic example without an LLM saying that the run is now finished. So that way the front end knows that it can move on to whatever it might need to do to process things after the agent execution is complete like telling the user they

**[0:12:33]** can send their next message or whatever that might be. So this is a really important event to send as well. And then we also have the whole idea of sending error events which is really good just to make sure that whenever we have an error in the back end it doesn't

**[0:12:44]** just crash the application and our front end doesn't know what happened. we can send an event that tells our front end specifically what issue the agent encountered so that we can handle that appropriately. So yeah, basically all of the different event types and there's 16 in total that we can send here. This is

**[0:13:02]** everything that our front end might need to know for everything that's going on with our AI agent. This is just so powerful and I'll get into this more in a bit when I build out a backend with Python. But you should be able to kind of start to envision here how you're not

**[0:13:17]** just limited to using OpenAI. Like you could use any LLM, any framework that you want, as long as you are emitting these standard events that are showing the different tool calls and output messages and things like that. It doesn't matter what you're using, you're going to be able to do that with AGUI.

**[0:13:32]** And then the way that we leverage this agent as an API endpoint is going to depend on the framework that you're using. So obviously in this examples they are using C-Pilot kit. And so within our primary React page here, we set up this instance of Copilot Kit where we're giving this runtime URL

**[0:13:49]** that's going to point to this API endpoint where that agent is running with all the code that I just showed you. And so I don't want to dive into Copilot Kit a ton right now. Honestly it does deserve its own tutorial. So I might make a guide specifically on

**[0:14:02]** Copilot in the future. Definitely let me know in the comments if you'd be interested in that. But the copilot kit just gives us a way to set up these React components to interact with our agents through API endpoints that implement things like agui. And so this is our primary page. This is our tool

**[0:14:18]** that gives us the ability to change the background color like we saw in the demo. And then we just inject the co-pilot chat here within our JSX so that we have that place to talk to our agent. And then within the route here for slash API slash and then what was it

**[0:14:35]** here like slappi/copilot kit. This is our route for that where we're just using this instance of the copilot runtime that works for nex.js. So we have this nex.js endpoint here where we're going to be passing in this runtime that defines our custom agent. So this custom agent class

**[0:14:52]** right here that corresponds to exactly what we set up right here. So custom agent, we're just importing that into our API endpoint and then setting that up. That is what's going to be called when we make this post request to /appi/copilot kit. So copilot kit does a lot of the work here of making it very

**[0:15:09]** easy to integrate the agent within the front end. But you don't have to use copilot kit at all. You could build something entirely yourself that's just going to leverage these different events that we get back from our AGUI compatible endpoint here for our agent. So, we can watch for the text messages

**[0:15:26]** and stream those out. We can watch for the tool calls and we can display those however we want to. There's a lot of flexibility here. No matter how you want to build your front end or your agent AGUI gives you that connection. So, you can use anything that you want. For

**[0:15:41]** example, I was easily able to adapt this example to use a Python backend for my agent instead of something that is built also in JavaScript like the front end. So, let me show you that. Here I have my other instance of windsurf open up here where I followed their example. So if I

**[0:15:56]** going back to the documentation here instead of the connect to AGI page, if you go to build with AGUI, then you'll be able to see the example using Python. So they walk you through what it looks like to set this up. This is very similar to what we saw where we're just

**[0:16:09]** going to be yielding these different events like the run started, the run finished, or here is the next test text message. Like it's going to look very similar, but this time we're in Python. We can use libraries like crew AI or pyantic AI. And I'm not using those in

**[0:16:23]** this case, but you very easily could. And so I have this fast API endpoint that's hosted just with slash AWP. I'm getting the message ID here. And then I'm sending in that event saying that all right, I'm starting the response from the agent and then I'm using GPT4.1

**[0:16:39]** mini just like I did with the JavaScript. And then I'm going to loop over all the chunks that I get back in the stream when I'm streaming the response from the LLM. And I'm going to send a bunch of these chunks just by yielding them. And the event type for

**[0:16:52]** each one of them is just text message content. And I'm sending that delta as well. So we can build up that response over time in the front end. And then just sending the text message end and run finished at the end. So this is a basic example that doesn't handle the

**[0:17:05]** tool calling. So I can't change the background with this agent like I can with the one in JavaScript. But I just wanted to show you at a very basic level how we can use Python instead. And then going back to my custom agent here, I'll actually replace the code entirely with

**[0:17:20]** what I've created with the help of an AI coding assistant of course to use our Python endpoint. So instead of having all the logic right within here to interact with GBT4.1 Mini, I'm now going to be calling this endpoint that I have running right now in my terminal. I

**[0:17:35]** could even show you that here. So if I open up my terminal and show you this right here, I got the API endpoint that is currently running. And so we're going to hit that and then we're going to create this reader where we're just going to process the stream. So we're

**[0:17:46]** going to be displaying things in exactly the same way when we had everything implemented just in JavaScript. So just a little bit of extra code to take care of that. Returning this process stream to our co-pilot kit runtime so it can handle that accordingly following the AGUI protocol. So back in our front end

**[0:18:03]** here and I've got the terminal open up as well cuz I'll show you that we're now using our Python API endpoint with AGUI. So, I'll go ahead and just send in a message like what are the best AI agent frameworks,, which, it's, not, going to, give a good answer because it's training cut

**[0:18:17]** off. But yeah, we can see here that we now got a post request to our endpoint just now. We're getting our response streamed out looking very, very nice. It was that easy to adapt basically entirely switching our agent under the hood, but it's connected to our front end in the same way. So, that's the main

**[0:18:32]** thing I wanted to show you. I went from a JavaScript agent all the way to a Python agent. And so that could be going from MRA to crew AI, whatever you want to do, but I still don't have to change anything in the front end. I can still

**[0:18:44]** interact with the agent in the exact same way. And if any of this seems complicated to you, do not worry. You're not alone. And they provide a way for you to very easily use AI coding assistants like Windsurf and Cursor to help you build with AGUI. both building

**[0:18:59]** out your agents and your backends and making that compatible and building out your frontends with your own code or using a tool like copilot kit, whatever that might be. And so this page in the documentation, if you just scroll down you'll see developing with cursor, they have this

**[0:19:15]** llm's-fold.ext. And so you can take this and you can give this as documentation to your AI coding assistant. So cursor has their built-in docs feature. You could just paste this into your prompt. There are also MCP servers like my crawl for AI one where you could crawl this

**[0:19:30]** and use this as a rag knowledge base for windsurf or ruode or whatever you want to do. So yeah, this just makes it very accessible for you to start building with AGUI connecting your agents to your users. Now the very last thing that I want to touch on is the current state of

**[0:19:48]** AGUI. Obviously this protocol is brand spanking new and so it's not super mature at this point. Like I said, it's definitely worth exploring this protocol, starting to learn how it works, maybe not using it for literally everything yet. I wouldn't go there because there's still a lot that has to

**[0:20:05]** be developed out. And we've seen this with other protocols like MCP and A2A. I mean, A2A still really hasn't been widely adopted yet either. And then MCP it's starting to get there, but it took a long time. It was November of last year that MCP was first released by

**[0:20:21]** Anthropic. It wasn't widely adopted until maybe around March of this year. So like four or five months. And the main reason for that was just when they started their documentation wasn't the best. The protocol wasn't the most mature and was barely handling things like security. I think we're seeing a

**[0:20:36]** lot, of, that, with, AGUI,, at least, to start. And honestly, they're doing a lot better of a job than MCP did at first. So props to them. I'm very impressed. And yeah, it was really easy to work with. And it definitely just makes sense the way that they set up all these

**[0:20:50]** different events for our agents and how that communicates to the front end. So that is a wrap for our AGUI introduction. I'm definitely going to be keeping tabs on this protocol, maybe even starting to integrate it in my own applications. And if this was interesting to you and you want to dive

**[0:21:05]** deeper into building full agentic applications, definitely check out dynamis.ai. It's my community for other early AI adopters just like yourself. And as a part of it, I'm building out a full course right now where I'm going from start to finish my full process for building agents, including building out

**[0:21:22]** these kind of frontends to connect your users to your agents. And also, I do want to cover AGUI more on my channel in the future, building out some specific use cases as well. So, if you're looking forward to that and you appreciated this content, I would really appreciate a

**[0:21:35]** like and a subscribe. And with that, I will see you in the next
