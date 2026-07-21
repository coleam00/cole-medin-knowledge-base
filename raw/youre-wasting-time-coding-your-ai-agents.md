---
type: raw-transcript
title: "You're WASTING TIME Coding Your AI Agents"
youtube_id: VxTw9tzzlbc
url: https://www.youtube.com/watch?v=VxTw9tzzlbc
slug: youre-wasting-time-coding-your-ai-agents
published: 2024-08-18
duration: "0:11:36"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I love coding my own AI agents it gives me so much control to make whatever I want but here's the thing coding an AI agent takes a ton of time and a lot of debugging and if you think to truly create a powerful AI agent you have to

**[0:00:15]** code it yourself well I have got some news for you today we're going to talk about n8n and how you can use it to create super powerful AI agent workflows with absolutely no code n8n is a really powerful workflow automation tool similar to or zapier but it stands above the

**[0:00:33]** competition by far because of two big reasons first big reason why n8n is absolutely the best is you can self-host it and what that means is you pay a grand total of 0 to run your workflow executions with NN no matter how many you have per month at one point I was

**[0:00:49]** paying $174 a month for zapier and my business still had a lot of room to grow so this can save you thousands and thousands of dollarss literally the only thing you have to pay for with n8n is the machine that you have in the cloud to host your

**[0:01:02]** own instance and that can be as cheap as $6 a month if you use a service like digital ocean which is what I used the second reason why n8n is absolutely the best is it has direct integration with laying chain which is my favorite library for building AI applications

**[0:01:16]** that I cover a lot on this channel So within n8n as a part of your workflow execution you can have your own custom Lang chain chain where you can choose any large language model you want there's a ton of options for working with chat memory uh there are so many

**[0:01:30]** Ops options that you have for different tools that you can use and you can create your own tools and there's also things like structured output so you have all the robustness you would usually have in an AI agent that you code yourself but this way there is no

**[0:01:41]** code and you can have it as a part of an n8n workflow so here's what I'm going to show you today I'm going to take the AI agent to manage my as tasks that I've been building as a part of my AI agents Master Class series and I'm going to

**[0:01:52]** show you how to recreate a basic version of it on n8n with no code in just a few minutes so you'll be able to create a powerful AI agent with no code in N by the end of this video all right so before we dive into creating our Asana

**[0:02:06]** AI agent N I want to talk about self-hosting because this is what makes NN so powerful and freaking affordable no matter how much you are scaling it is my favorite feature of Ann maybe besides the Lang chain stuff and so they have really really great documentation on how

**[0:02:23]** you can self Host this is the page specifically for self-hosting with digital ocean which is my favorite service for cloud compute uh I am not sponsored by digital Ocean or ending end or Ling chain or any of these guys it'd be awesome if I was but these are just

**[0:02:37]** the services that I love to use that I've been using for years and years and years I've used digital ocean for a ton of other things and has always worked well for me so I'd recommend going through this documentation and signing up for digital ocean and hosting there

**[0:02:50]** $6 a month is all it takes on digital ocean to get Cloud compute that is powerful enough to run n8n so with that out of the way we can go ahead and actually dive into the n8n platform so here we are in the n8n UI which is directly hosted within my digital ocean

**[0:03:04]** droplet and n8n you can see right away is so so simple and that is a beautiful thing because we don't want a ton of stuff bloating our software so all we have here is workflows and credentials and so I'm going to start by going into one of the basic workflows that I've

**[0:03:18]** already created just to describe a little bit how n8n works and this will actually be the workflow that we have to create tasks in auna and so if you've used make.com or zapier or something like this before this will look really familiar to you because every node that

**[0:03:31]** we have in a workflow which is basically just a graph of actions combined together is either going to be a trigger or an action and so right here we have a workflow trigger so this is the entry point to our workflow and then every other node within this which is just one

**[0:03:45]** in this case is an action and that's what's going to actually do something like go out to aana and make a task which is like what this does right here or go out to Google Drive or Salesforce or our superbase database whatever it might be and so with this workflow it's

**[0:03:59]** just a very basic workflow where we are creating a task in auna and so we have a name and a due date that's passed into this workflow and so we have Dynamic data here to create a task given a name and a due date and then I just put

**[0:04:12]** everything in my coding project in AA for now we'll see that in a little bit how that works it'll be very similar to the Asana AI agent that is in uh the other videos in my AI Master Class series and so that is this workflow in essence for every single action you have

**[0:04:27]** the parameters and then there settings as well and they also have documentation so for every action you have in NN there's documentation to make it really really clear as you set things up and it also helps a lot with your credentials as well so like when you create

**[0:04:40]** credentials for a sauna you need an access token but sure enough they have documentation even to help you get credentials for specific applications you can connect to to NN so they make everything so so easy not just for self-hosting but also everything within the platform itself and getting your

**[0:04:55]** workflow set up so it is just absolutely beautiful and so what we going to want to do is actually copy the workflow ID that you have in the URL right here so at the end of your url within this page you're going to have the workflow ID and

**[0:05:08]** you're going to want to copy that for the next step here because this is where we go into the workflow that actually has our AI agent and this is where things get really really fun so the entry point for this workflow is this chat input right here and so if I

**[0:05:22]** actually play this here I'll go to the chat you can see here that you can type a message within a chat window kind of like what we had in the Stream like I that I use very often on my channel here and so I could say something like Hi how

**[0:05:34]** are you and we'll actually get a response from the AI right within the n and workflow so we can test things out really really quickly with our agents which is super super cool and then what we're also going to do is compute the date and time and the

**[0:05:47]** reason for that is we want to tell our assana assistant what day it is so it can accurately determine due dates when we give relative dates like this Saturday or next Friday and so we get the current date and then it'll output that as an item that we can use use in

**[0:06:00]** other actions going forward in the workflow and so I'll go back to my canvas here and we can go into our AI agent and this is where we really hook up a lot of really cool things to make this a full-blown AI agent you can see right here that we have an open AI model

**[0:06:13]** that we have hooked in I got my API key put in the credentials here we've got a window buffer memory which is just a basic type of memory and there are a lot of different types of memory that you can have here like we can use redis for

**[0:06:25]** example also for the large language models you can use like literally everything that care to use anthropic Gro olama open AI everything that I've used in my master class videos before we have that here as well and then the other part that's really cool is we can define an infinite number of tools to

**[0:06:42]** attach to our AI agent just like we did with laying chain in our python code and so if I wanted to create more tools I would just have to drag out um to these other tool nodes that I would create right now I just have one which is going

**[0:06:54]** to reference that workflow that I showed earlier to create tasks in a sauna and so that's where we need that workflow ID that we have copied here but you can see that you give a description to tell the AI agent how to use this tool and then you can even have structured input so we

**[0:07:09]** can tell it that you are going to be giving the tool I.E this n workflow a name and a due date and that corresponds to exactly what I showed before those Dynamic parameters that go into creating the as task so you can control things really really well and tell the agent

**[0:07:26]** how to use the tool just like you would with custom code so it is just a beautiful thing and then within the agent itself we have the text which we're going to reference the text that is sent in from the trigger to this workflow which is when a chat message is

**[0:07:40]** received and so all you have to do in NN to reference something from a previous node is you have to execute it first and then you'll have it available in the input dropdowns here so I can just drag the chat input right here and it's going to add it in so I already had it there

**[0:07:54]** so that's why we see it twice now but that's how easy it is to bring in something Dynamic from another node that already executed in the workflow and so it's going to be the same thing with the current date we're going to input that into the system message here where we

**[0:08:05]** also tell it you're a helpful assistant who helps create tasks in a SAA similar to what we did when we wrote this all in our python code so it's just amazing stuff and there's other settings as well that you typically don't have to play with but there's just so much control

**[0:08:18]** that n8n gives you like this this is just amazing to me um and then the last thing that we're going to do is just respond to a web hook and so this is kind of just the end of the workflow where we spit out an output element that

**[0:08:30]** we could then use with an API so I've also set this up with streamlet so I can literally just call this entire NN workflow as an API and get the response back to display to UI but you don't even have to do that because n8n makes it really easy to Define custom user

**[0:08:45]** interfaces around your chat bot as well I'll show that in a second here but I just wanted to also test out having this as an API endpoint instead of making it all within an n8n chatbot and so what I wanted to show here as a last thing is

**[0:08:59]** how we can take this chat bot and actually create a UI around it really really easily with n8n and so what I'm going to do is I'm going to click on this chat button here in the bottom middle and then it says add chat to external application using an chat

**[0:09:13]** package and so you click on more info and it will literally give you an embed that you can put on your site and you can also use react or view embeds as well if you want to install NN chat with mpm I'm just going to do this for now

**[0:09:25]** because it is so easy to set this up so the one thing I wanted to do before I show this is you have to go into your chat component and make sure that you have the chat publicly available and so I'm not going to have this publicly available once I actually publish this

**[0:09:38]** video because that means you could go to this URL and just start using my chatbot and spending my open AI credits um but you have to make this public first you can also add authentication if you want to protect it and then you can take that in bed and put it in your own website or

**[0:09:53]** in this case I'm just going to use an online HTML editor so I dumped in exactly what it gave me as the embed and n8n and then run it and sure enough I've got this nice little button in the bottom right that you see in a lot of

**[0:10:04]** websites where I can click this to open my chat bot and here I can go ahead and ask it something like what can you do for me and the responses from the N agents are actually really really fast like you can see right here so yep calls up that can help me in a and so I can

**[0:10:18]** say something like cool I need to uh bake cookies by Friday so we'll see if it'll make a task for me in AA so give it a couple seconds to perform the actual action with the N workflow and there we go I've created the task to bake cookies by Friday you can view it

**[0:10:34]** here so it gave me the link otherwise I can also just go into auna directly and sure enough I've got a task to bake cookies by Friday this was not there before I just had this single task from a prior test so everything is working beautifully with this chat bot that I

**[0:10:49]** can have as an API endpoint or I can have as a chat widget that I showed just now you can turn it into anything you want and this is all with absolutely no code so there you go in just a couple of minutes we built a powerful ASA AI agent

**[0:11:02]** chatbot in N with no code I am a big proponent of using no code solutions to build your simpler AI agents so you can truly dedicate the time you need to the more Cutting Edge and complex AI agents that you have to code from scratch just because of the complexity of what you

**[0:11:18]** are building and so I hope that you can use n8n as a new tool in your tool belt to build your AI agents much more efficiently and with less hassle if you found this useful and you plan on using na at all I would much appreciate a like

**[0:11:31]** and a subscribe and with that I will see you in the next video
