---
type: raw-transcript
title: "Build a ChatGPT Style App for Your n8n AI Agents in MINUTES"
youtube_id: 6zn8vVTeFE0
url: https://www.youtube.com/watch?v=6zn8vVTeFE0
slug: build-a-chatgpt-style-app-for-your-n8n-ai-agents-in-minutes
published: 2025-04-09
duration: "0:22:03"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have a trade offer for you. If you give me just 15 to 20 minutes of your time, I will help take your N8N agents to the next level and do it very effortlessly. What do I mean by that? Well, usually when you're working with an AI agent in an N8N workflow, it'll

**[0:00:14]** look something like this. And you'll have a chat trigger at the start of your workflow, and that gives you this chat button in the bottom middle. It's very convenient for you to use this to talk to your agent right within the workflow builder. However, it's very limiting. doesn't look the best and you can't view

**[0:00:30]** past conversations if you want to continue one of them. And when you go into your chat trigger and you make the chat publicly available, essentially getting this web page deployed for it it gets even worse because this is what it looks like. It's very ugly. There's not much room to customize this page and

**[0:00:47]** you still can't view past conversations like you can with something like chatgbt.com. And don't get me wrong, I absolutely love N8N. In my mind, it is the best no code tool for building automations and AI agents. But clearly for their UI, there could be something much much better. Wouldn't it be nice if

**[0:01:06]** instead of having something that look like this, we could have a UI for our agents that looks like this? Now we are talking. We have a full chat GBT- like interface to talk to our NN agents. If this looks awesome to you, something you've always been wishing for, then I

**[0:01:21]** am now your genie. Because in this video, I'm going to show you how to set up everything with some downloadable resources, you can get this all set up for yourself in just minutes. This is the kind of interface that we always expect LLM providers to have like OpenAI, Anthropic, DeepSeek, and now we

**[0:01:37]** have this exact same kind of setup for our own agents. And we don't even have to code anything or build a custom app because this is all using the power of an incredible open- source platform called open web UI. That's what gives us the UI right here. Very beautiful. And

**[0:01:52]** there are a ton of very powerful features baked into this as well. Like we can use voice to talk to our N8N agent directly now. And so many other things that I don't even have the time to dive into in this video. But take a look at this. I'll send in a very

**[0:02:06]** standard prompt. Just the classic build the snake game for me with Python. And it might seem like it's just going to a normal LLM. I mean, this just looks like chatgbt.com, but under the hood, it is connecting to an AI agent that I have hosted directly in N8N. And we can even

**[0:02:20]** go to this workflow that I have right here. Go to the executions, and we can see this happening in real time. This is the one that just executed. I even saw that or I heard the ding that I got the response back in open web UI. I'll click

**[0:02:32]** into the agent, and sure enough, the output that we got is the snake game. And then going back into our UI, we have this response from our agent. And look at how nice this is. It's got the full formatted markdown and everything for Bash and Python. It's got highlighted

**[0:02:46]** text. This just looks so so nice. And we've got conversation history. I can continue the conversation here. I can go back to old conversations like where I previously had it code the snake game a different time. And I can continue those conversations. There's just so much that we have here that we don't have with

**[0:03:03]** this interface or with this interface right here. So, here is the game plan. First, I'm going to show you how to set up Open Web UI for yourself. It's an open- source project, so you can download it from the GitHub for free. I'll show you how to get started very

**[0:03:17]** easily. Then, I'll show you how to import the custom code that I created for you that you can import into your Open Web UI instance to set up the N8N integration. And this is all using a feature in Open Webb UI called functions. And then the last thing that

**[0:03:31]** I want to go over with you is how we can build AI agents in N8N that integrate in a very seamless way with everything else that we're setting up here. There are a couple of considerations, things that we have to add into our workflows to make this work optimally, including we're

**[0:03:46]** using an LLM in two different places even though this is for just a single AI agent. So, I'll cover all of that. It's really not that bad overall. I mean this is a pretty small workflow, and there's a link to this in the description of this video if you want to

**[0:03:59]** download this N8N workflow as a starting point to build your own agents that can hook into Open Web UI very easily. First things first, we have to install Open Web UI. I've already kind of covered what it is. It's our own self-hostable interface to chat with our own LLMs and

**[0:04:14]** AI agents. And the beauty of Open Web UI is you can run it entirely offline on your computer. And so this is kind of outside of the scope of this video, but you can use it to chat with your Olama LLMs. You can use completely self-hosted N8N and connect it into Open WebUI. You

**[0:04:29]** can run everything on your own computer. And so I'll have a link in the description to this repo for Open Web UI. You can scroll down on the readme here to look at the installation instructions. There are two different options that we have. First, we can install with Python. So if you have

**[0:04:43]** Python on your machine, that is the only prerequisite. You can then install open web UI with pip and then run the open web UI serve command to spin up the application on your computer and then you can access it in your browser with this URL right here just localhost port

**[0:04:58]** 8080. The second option is with docker. It's very easy to install with just a single command. And there are a few different command options here depending on your machine and configuration. I would just pick the top one if you're unsure. Otherwise, you can feel free to read through these different options and

**[0:05:14]** pick the one that is right for you. It's very simple for us because these different options are depending on if you're using Olama or Open Web UI. We have a unique case where we're just going to connect directly to an N8N agent. We're not using either of those

**[0:05:26]** providers. And so, this top command is just kind of the good default. So that's the options given in the readme for Open Web UI. There is one other one that I want to cover really quickly because we have the local AI package that I've covered a lot on my channel

**[0:05:40]** already. This is my collection of local AI services like your database. You've got self-hosted N8N, Olama, and Open WebUI. So, all of these services are packaged together for you to install. I'll have a link to a video right here where I have instructions for getting this up and running. But everything I'm

**[0:05:56]** covering in this video can be done with the services included in the local AI package. So, honestly, this is probably the most convenient way to get everything up and running from scratch for yourself. So, I'll have a link to this in the description as well if you want to get nadn and open web UI or just

**[0:06:12]** open web UI through my local AI package completely free and open source. After you have open web UI up and running with either Python, docker or the local AI package, you can then go into your browser and access the interface. Typically, the URL is going to be either

**[0:06:26]** localhostport 3000 or port 8080 depending on how you installed it. And then you'll have this interface after you create your local admin account when you set up Open Web UI for the first time. And then right away you can go and start chatting with your Olama LLMs or

**[0:06:41]** OpenAI LLMs. But what we care about in this video is connecting to our N8N agents. And there are two ways to do this in Open Web UI both through setting up this custom function that I have created for the N8N integration. And so I'll link to this function in the

**[0:06:56]** description of this video. This is our ticket for everything. Now, I'm not going to dive into the details of all of this Python code here, but just know that I definitely saved you a big headache creating all of this so that the integration is something that you can just hook into your Open Web UI in

**[0:07:09]** minutes. And so, the first way to do it is just going to this URL and clicking on this get button right here. And then you just type in your current URL for Open Web UI, like localhostport 3000 and then you click on import to web UI. The other way that you can install this

**[0:07:25]** if you want to do it manually, maybe even change some of the code yourself if you're more technical, you can click on the copy button right here to copy all the function code. And then back into Open Web UI, you can go into the admin panel in the bottom left, click on the

**[0:07:39]** functions tab, click on the plus icon in the very top right to add a new function, and then you can just paste in all the code that you copied from that function page. And then the only other thing you have to do is add a function ID and description. You can just make

**[0:07:52]** these up yourself and then click on save and then boom. Either way, you're going to now have this function for the N8N agent connector. That's at least what I called it. You'll have this available to you now. And then when you go into your workspace here and you start a new chat

**[0:08:07]** you can select this as one of the LLM. So I have all these other LLMs that I just have through Olama, but now I have this one just alongside all of those which is my custom function to connect to N8N. And we're not quite ready to go yet because we still have to configure

**[0:08:20]** our function. And so I'm going to go back over to that here. And then within the settings icon for valves, this is where you set the specific pieces of information that are custom to you that the function needs. And I'll cover how we set each of these when I go over how

**[0:08:36]** we build our agent for the Open Web UI integration. But we're going to need our URL for the agent, a bearer token so we can keep our agent secure and only access it through open web UI. And then we have the input and output fields to determine the specific value we're

**[0:08:52]** expecting to come into our N8N workflow and what we are outputting. And then for the emit interval, you can typically just leave this as the default. You can see that it's the interval in seconds between status emissions. So getting an update on how the function is performing when we are chatting with it in the

**[0:09:07]** interface. Building your own automations and AI agents in platforms like N8N is a great way to create custom tailored solutions to the problems you're trying to solve. But as nice as it is to build everything yourself, there's so much that goes on behind the scenes to make automations and agents that are truly

**[0:09:26]** scalable configurable robust and secure. And a lot of times, if you're a business owner that has a lot of requirements around these things, you don't have the time or desire to really invest into that. You want an enterprise ready solution that's more out of the box. That brings us to the sponsor of

**[0:09:43]** today's video, which is ZAMS. ZAMS is an enterprise platform to build AI agents to automate back office work. And it makes building these AI agents very effortless, secure, and powerful. AI agents today are kind of like what the internet was like at one point. Quite powerful, but also very inaccessible. It

**[0:10:01]** took the web browser to really make the internet accessible to the average person like you and me. And ZAMS is doing the exact same thing just with AI. They're giving agents a UI layer to make it actually work for businesses. Instead of forcing companies to stitch together all of their automations, tools, and

**[0:10:18]** knowledge bases for AI, ZAMS takes care of it all. You got knowledge AI for understanding your data, process AI for getting things done, and predictive AI to help you as a business owner make smarter decisions. And it's all built for enterprise use with control governance, and security baked in

**[0:10:37]** throughout the entire platform. And they have a whole suite of impressive technologies under the hood to process billions of data points instantly, build predictive models with ease, and turn natural language into full automations. So, I'll have a link in the description if you want to book a ZAM's demo, and

**[0:10:53]** see how it can transform your business with enterprise level AI agents. So don't worry if not all this made sense to you yet. I'll show you how to set each of these values as we go through the N8N agent template, which speaking of that, let's do that now. And this is

**[0:11:08]** going to be a downloadable resource for you, which I'll have linked in the description. I feel like I've said that four or five times already. I really am trying to make this a valuepacked video for you with a lot of resources to get you started. And so, I want to cover

**[0:11:21]** this agent. I made it as simple as I possibly could just to demonstrate the core pieces that you have to have for this open web UI integration. And so yeah, very basic agent. It just has a single tool to search the web with the Brave API just so I can have at least

**[0:11:35]** one tool here. But the big things I want to cover mostly are at the start of this workflow. Starting with our web hook trigger. So, instead of there being a chat trigger like we had at the start of the other workflow in at the beginning of this video, I'm using a web hook

**[0:11:50]** trigger because this is going to give us a public URL that we can use to communicate with this workflow and thus communicate with our AI agent. And so you want to go to the production URL and copy this. And you can set the path yourself to whatever you want. So you

**[0:12:05]** copy the production URL, make sure your workflow is toggled to active, and then that is what you paste in right here for the N8N URL value. So that's the first one. But then the other consideration with this is that when we have a public URL to communicate with our workflow

**[0:12:21]** that means anybody could just theoretically call into this and spend our LLM credits. And so we want to protect this endpoint with header authentication as well. Now, a caveat to this is if you are running on the local AI package or just running N8N completely locally, then you don't

**[0:12:38]** really need this because people can't go into your computer. But if you have N8N running in the cloud or self-hosted through something like Digital Ocean then you do want to protect all of your web hook endpoints. And so, you can do that by selecting header authentication and then creating custom credentials.

**[0:12:55]** And I'll show you how to do that in a second. Um, but I just want to say really quick that you definitely need this if you're not running N8N on your own machine. Otherwise, people are going to be able to call this workflow an infinite number of times and you might

**[0:13:08]** see a huge spike in your OpenAI bill or whatever provider you are using. And so to set up your credentials here, the name is going to be authorization and then the value, I'm going to type it in this box because this box hides the value. The value is going to be bearer

**[0:13:23]** and then space whatever token you want to set. So bearer and then a space and then your custom token. And so I'm going to delete this and then I'm going to type it in right here. So bearer space and then test off. And then whatever you set for your token, you're going to go

**[0:13:39]** back into open web UI and you're going to add that right here. And so the function assumes that you're prefixing with bearer space. So you don't include that here. You don't say bearer space test off. You just have the token that you set in N8N. So I hope that makes

**[0:13:55]** sense. So I'm going to close out of this cuz I already have this set. That is how you add authentication. So now your agent is protected and it can only be called within open web UI or wherever you are invoking it and you have the right bearer token used. So that is our

**[0:14:09]** web hook trigger to kick everything off with our agent. Then I guess the last thing really quick, double clicking back into the web hook. If you're running on local host or you don't need a header authentication for whatever reason, you can just set this to none and then leave

**[0:14:22]** the value blank in open web UI or just set it to whatever value you want. If you don't need security around your agent, obviously I do in my case. So I'm going to make sure that I have this set because I am running with N8N host in a

**[0:14:35]** digital ocean in the cloud. I need to make sure that I have my endpoints protected. I'm not running on local host. I do have open web UI through the local AI package. This is running a local host, but just for what I'm using for this video, I have N8N running in

**[0:14:49]** the cloud. And so I have that set. I got my security set up. And then the next two things that we want to set is the input field and response field. And these two values I are determined by what we expect to come into our N8N workflow and then the name of the field

**[0:15:04]** that we're outputting at the very end. And so to make that very concrete for you, I'll go to my last execution. And so starting with the input, I'll click into the web hook. And you can see that the user message that comes into our NAN workflow, the name of this field is chat

**[0:15:18]** input. And that is determined exactly by what we have typed in right here, chat input. And so you just want to make sure that whatever you're expecting in NN like in this case, I'm expecting the value to be called from chat input. I want to make sure that that is what I

**[0:15:33]** have typed in open web UI. And I can even show you this here. If I click into my agent node, you can see that I'm expecting the user prompt to come in from the chat input value of the web hook body. And then for the output right here, the reason I'm calling it output

**[0:15:48]** is because if I go to the very end of this execution in n, you can see that the response from the AI agent is in the output field. And so I need to make sure that this maps with this value right here because that way my function in

**[0:16:02]** open web UI knows where to look to find the AI response. If this was set to something else, then it wouldn't work. It wouldn't find the LLM response, and then I wouldn't get an answer in my UI. So, it's very important to make sure that these values match with what you're

**[0:16:15]** expecting to come into the workflow and what you are outputting. And then back over to the AI agent, I just want to show you that besides this bottom part that I'll cover in a little bit, the rest of this is just a very simple N8N AI agent. And so, we have our LLM hooked

**[0:16:28]** in. You can use whatever provider you want. I've got Postgress for my chat memory. I've got this single tool that I won't cover in detail here, but this is just connecting us to the Brave API. So we're giving the capability to our agent to search the web just with this little

**[0:16:41]** workflow at the bottom here as a tool. And then I don't even have a system prompt. So, I've kept this very, very simple because this is just a template to get you started. You can build out whatever AI agent that you want in N8N and hook it up as long as you have this

**[0:16:55]** first part of the workflow and then the thing at the end where you just map the output field to what you're expecting in Open Web UI. It is that easy. You could use MCP servers. You can make a dozen different tools. You could use many agents in this workflow. You can do

**[0:17:08]** whatever you want. I'm just giving you a very basic starting point. The last thing that we have to cover here though is why the heck do I have the second LLM call in this workflow. And in order to show you why we need this, let's first go and chat with our agent another time.

**[0:17:23]** And so I'm going to go and open up a new chat. And I'm just going to say, "What can you do for me?" So, I'll just ask it a very simple question. And then if we go into the executions for our workflow here, we'll see that there were actually

**[0:17:38]** multiple that were kicked off. Look at all those appear. And why is that? We have this one at the start where we get the full response from our agent where it's telling us what it can help us with. But then we have these other three. Why do we have three other

**[0:17:52]** executions? Now, the reason for that is Open Web UI calls the LLM multiple times for the first message in a conversation to do a couple of different things. First of all, it uses AI to give a title for the conversation. It doesn't just use my message or use the start of the

**[0:18:09]** AI response or anything. It actually generates based on the first two messages a description of the conversation. It also uses AI to generate tags for this conversation. So if I click on the settings right here you can see that it decided for this conversation specifically, the education and technology are the two tags that it

**[0:18:28]** decided to apply here. And so, it's using AI to do that. So, if you look at this call to this basic LLM that I have set up, you can see that it generated the title. And then, if I look at the next execution, it called the AI again

**[0:18:42]** to generate the tags technology and education. And so it's just a nice feature in open web UI where it uses AI to do other things in the conversation besides just giving us the response. It creates these tags, this extra metadata like the title of the conversation as well, which is super neat. And if you

**[0:18:59]** don't wanted to do that, you can always just delete this part of the workflow. So you could delete this node, this node, and this one. And then you can just have the web hook connect directly to the agent. So you can do that if you don't want to use extra AI credits like

**[0:19:14]** more open AAI credits to generate these things. But I think this is a really nice and useful feature. And you can always just use a very fast and cheap LLM. Like I could just use GPT4 mini to generate these things and then use Claude 3.7 Sonnet for a more expensive

**[0:19:29]** more powerful LLM for my primary agent. And so you can make this very very affordable. Even though it is using four LLM calls for the first message in a conversation, you can make it so it's not actually that much more expensive or it's just going to be entirely free if

**[0:19:43]** you're doing things local with Olama anyway. And so the way that we have this set up where for the rest of the conversation it'll go down this path and then for just the metadata stuff like the title it'll go down this path is because take a look at this. If I go to

**[0:19:58]** one of these executions, click into the web hook, the session ID, the specific ID for this conversation is none. When we're generating the metadata, but otherwise for any other message that is actually communicating with our primary agent, the session ID is defined. This is our unique identifier for the

**[0:20:18]** conversation that open web UI gives us and that's what we use within the Postgress chat memory node as well for the again the unique identifier for this conversation. And so this if statement is very simple. It's just checking to see if the session ID is none or not. If

**[0:20:34]** it is none that means that we're generating metadata. So it'll just go to this very simple cheap and fast LLM. Otherwise it'll go to our primary agent. So I hope that makes sense. If that's not like 100% clear, don't worry. That's why I have this template for you to just

**[0:20:47]** download and use. You can build whatever you want as your primary agent. Just make sure you keep this here to generate that metadata like the tags and the conversation title if you care about having that. And so, it took me a little bit to realize this. I even covered the

**[0:21:02]** pipeline on my channel previously for connecting Open Web UI to N8N, but I didn't have that piece before. And that plus a couple of other things is why I'm making this video again. or not really again, but I did something kind of similar before, but it's just much

**[0:21:16]** better now. And I have this resource for you to work with. So, I hope that you found this really useful. Take this and run with it. Take this pipeline, take this agent, you can get up and running with what I have shown right here in Open Web UI so easily. So, I hope this

**[0:21:29]** video has really helped you take your N8 agents to the next level with this open web UI integration. And please let me know in the comments if you have any questions at all. I'm always in the comments answering everything. Also, I have a lot more content coming out soon

**[0:21:44]** for the local AI package, which is where I'm currently running my open web UI and N8N. So, stay tuned for that. So, if you appreciated this video and you're looking forward to more things N8N, AI agents, and local AI, I would really appreciate a like and a subscribe. And

**[0:21:59]** with that, I will see you in the next
