---
type: raw-transcript
title: "The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)"
youtube_id: lbyPJqCI-tw
url: https://www.youtube.com/watch?v=lbyPJqCI-tw
slug: the-ultimate-guide-to-building-your-own-mcp-servers-free-template
published: 2025-04-13
duration: "0:27:54"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Everyone is starting to realize how big of a deal Anthropic's model context protocol is. It's the first ever standard for connecting LLMs to your services like Gmail, Slack, GitHub, web search, the list goes on. And you can use it to give higher level capabilities to your LLMs like long-term memory. As

**[0:00:20]** we'll see in a couple of minutes here there are a lot of these MCP servers already out there to connect us to these different services. But the true power comes in building our own so we can connect our own agents to any service that we want, all using the simplicity

**[0:00:35]** and power of MCP. In this video, I'll be breaking down the full process for you on building your own MCP servers to connect your agents to anything. And to make it well worth your time, I'll also be walking you through my template that I've created for you to get you up and

**[0:00:50]** running building your own MCP servers very easily. I've spent hours creating the perfect foundation for you to save you a big headache. So, I'm really excited to show you that and also just how to build these servers in general. A lot of value packed into this video today. So, let's dive right into it. If

**[0:01:06]** you are not familiar with Anthropics MCP already, I would highly recommend checking out this video, which I'll link to above. But in general, the three main resources that I use to learn about MCP and building my own MCP servers are the official docs for MCP, which we're looking at right here, a list of

**[0:01:24]** existing MCP servers on GitHub, and then also Anthropic's official GitHub repo for the MCP Python SDK. So, let me explain all three of these really quick and then I'll also have links to these in the description of this video. So the official docs are just really useful to get a general grasp of MCP, and they

**[0:01:42]** have pages for pretty much anything including building your own servers and clients, which we'll be using in this video. And then the existing list of MCP servers is just very useful to use as a reference point. You can use these servers as examples for how to build your own. And this is just a great

**[0:01:59]** repository of a bunch of servers that we probably will want to use ourselves just in general and to help us build our own servers. And then lastly, Python is the language I'm going to be using to build MCP servers. It's just the simplest and the most used overall. And so using this

**[0:02:14]** as general guidance for how to build MCP servers specifically with Python is very, very useful. Now, the first big question I want to answer for you is what does it really mean to build our own MCP server? And to start, let's go to the existing list. So you can click

**[0:02:29]** into any of these MCP servers like Brave Search to give our LLM very powerful web search capabilities. We can scroll down and see the configuration that we' put into any MCP client. This is any application that supports MCP like Windsurf Cursor, N8N, Claw Desktop, your own AI agents. There are so many

**[0:02:48]** different places that we can use MCP to give all these capabilities to our agents and tools. And so you copy this and then within the official MCP docs it shows you how to use MCP servers, get that all hooked into cloud desktop. And so we can go to our cloud desktop and

**[0:03:03]** then follow those instructions to set up our configuration. And so this is what my config looks like right here. I just pasted exactly what I copied from GitHub into my cloud config and then set my Brave API key. And then I even have a couple of different MCP servers here

**[0:03:17]** just to show you how you can use as many as you want, combining all these tools together to add all these new capabilities to our LLM. Like I even have Archon here, which is my open- source AI agent builder, which I have some exciting updates coming soon for

**[0:03:30]** it, by the way. So stay tuned for that. But anyway, that's our configuration. And then back in Claw Desktop here, once you restart, you'll have access to all of these servers. I have a lot right now. But now we can ask it a question that it would only be able to answer if

**[0:03:43]** it has access to a web search capability. And so I'll let it use the Brave MCP server for this chat. And then boom, look at this. We now have up-to-date information that usually with the knowledge cutoff for LLMs, we wouldn't be able to answer this kind of question. So that's the power of MCP.

**[0:04:00]** It's that easy to add new capabilities to our LLMs to take them to the next level for us. But there are some limitations for this. Like what if the way that this MCP server interacts with Brave is not how we want to interact with Brave? Or what if there's some

**[0:04:16]** services or capabilities that we want to work with that there isn't an existing MCP server for? That's when we really need to get down and dirty and build our own MCP servers so we can interact with the services we want and have the full level of customization and control to

**[0:04:32]** really make our agents do what we want them to do. And that's what I'm going to show you how to do in this video. Now the reason I showed using an existing MCP server is I want to prove a point to you that what we're about to create

**[0:04:43]** together is going to work in exactly the same way as all of the MCP servers that you've already been working with. So I'm really setting the stage here to show you that these servers that are built by Anthropic, they follow all the best practices and they work with every

**[0:04:56]** client you can imagine. We're going to build one that works in the same way. And I'll even show you this is my new updated cloud desktop configuration. This is the MCP server that I'm building as an example in this video. It integrates with mem which is a library

**[0:05:12]** to give long-term memory to our AI agents. So we're going to make it so that Claw Desktop can remember things that we've said in past conversations. It definitely doesn't have that capability right now. And look at the configuration for this. It's set up in this JSON file exactly like all of our

**[0:05:27]** other MCP servers. very nice and easy. And the way that we interact with it and the way that we build it as well, as we'll see later, is also the same. And so I can go back into claw desktop here and I can ask it another question like

**[0:05:40]** what are my memories? And this is going to now use a tool not developed by anthropic but by me and what you are going to be able to create after this. And so I'll allow it to get all memories. And once it runs this tool it's going to tell me just one memory

**[0:05:55]** that I like chicken cuz I kept it very simple. I just inserted one memory into the knowledge base right now. But yeah I was able to use this tool that I built and retrieve that. It's so cool. Everything looks the exact same, but now we can add our own capabilities. So

**[0:06:09]** just because this is so exciting to me I want to show you really quick how we can use this MCP server in a lot of other ways as well with anything that supports MCP. Like I have this custom Pantic AI agent that I have connected to my MCP server that's running locally

**[0:06:23]** right now. So I can go in the terminal and run a script that's going to ask it for all my memories just like I did in Claw Desktop. And because it's connected to the same MCP server, it has the same tool. We get the same answer back. And I

**[0:06:35]** can even go into N8N and do the exact same thing. So I'm showing you all these different kinds of clients. I have yet another one here with N8N connected to the same MCP server. And so I can go into my chat and just like before I can ask it, what memories do I have? And

**[0:06:50]** it's kind of boring. We're getting the same answer every single time. But that's the point. I'm showing you how we have one MCP server that we're able to connect to from all these different clients and we built everything ourselves. Take a look at that. You currently have one memory. You like

**[0:07:05]** chicken. It's a funny way to word it. It's like we're we're dropped on the severed floor and the only memory we have is that we like chicken. So there you go. If you know the reference, you know the reference. But this is so neat. We're able to connect with all these

**[0:07:17]** clients. And so now let's dive into building this server. and it's a template that you can use to build anything you want as well. So, here is the Python MCP template that I have spent hours preparing for you, really trying to incorporate all of the best practices for MCP that I see a lot of

**[0:07:33]** people failing to implement. And so this is a MEM zero MCP server. So, I wanted to build something that's concrete and practical, but it's also general enough. that's very basic where you can just take out the mem zero specific parts if you want and implement all of your own tools to really build

**[0:07:50]** this into your own MCP server following all the different components that I'll explain in a little bit that really makes this a robust server that supports the different transport protocols for MCP as well which is a very important thing and so the readme that we have at the root of this GitHub repo that I'll

**[0:08:06]** link to in the description of this video it shows you how to set up and run everything and you can follow these instructions for your own server once you have it set up following this template as well. And the very important thing with this is that just because you

**[0:08:20]** can feed all the documentation into an AI coding assistant to build a server for you doesn't mean that it's going to work all the time. And so another really good use of this template is you can just copy everything in this main function and paste it in as a part of

**[0:08:36]** your prompt to your AI coding assistant when you're asking it like in Windsurf cursor to build an MCP server for you. This example is going to help the AI coding assistant 10 times better than any documentation that you can pull from MCP to help it understand how to build

**[0:08:53]** these servers. So use this as a resource for yourself and the AI. And the other thing is I see a lot of MCP servers that are just not built the best. Like Chromobb is a good example where it's a solid MCP server overall, but the way that they in instantiate their client is

**[0:09:12]** just not ideal. And I don't need to get into the weeds of this right now, but it's just not built the best. And then Mem also did actually release their own MCP server. So, I'm not building something completely new, but if you dive into the code for their MCP server

**[0:09:26]** again, I don't want to get into the weeds of this right now. You can clearly see that they didn't quite understand how MCP really works. It only supports one transport and they duplicate the description for their tools. There's a lot of things going on here that's not right. And I don't agree with some of

**[0:09:41]** their decisions. Like, you have to use the Mem Zero API key. You can't use this MCP server for free. Like you can use my Mem Zero MCP server for free. So honestly, I just feel like mine's a better version overall. And yeah, it just seems like no one quite knows at

**[0:09:57]** this point how to truly build an MCP server correctly. That's what I want to give you as my gift right now is this as a template that shows you how to really build these servers. Well, another thing really quick. If this template looks good to you and you want more resources

**[0:10:12]** and templates that look like this and really give you a good launching pad for anything you want to build with AI check out dynamis.ai. It's an exclusive community that I recently opened up the weight list for and I'm going to launch later this month. I've got a ton of live

**[0:10:26]** events courses resources and templates like this MCP server all for you. You can think of it like my YouTube channel, but going even deeper because there's only so much I can do on YouTube each week. I'm going to keep putting out a ton of valuable content for you here

**[0:10:41]** but also Dynamus is where you can go deeper. So, check that out if you're interested. Dynamus.ai. But yeah, let's get back to this template here for building an MCP server, following all of these best practices to give you a good head start. Now, I'm not just trying to get on my

**[0:10:55]** high horse here and tell you that everything I'm giving you is absolutely perfect. But what I am telling you is that I have spent hours and hours of time researching other MCP servers diving into the documentation, building things myself, and learning through trial and error. All of this to give you

**[0:11:11]** this template to save you a huge headache. And so, just please take this and run with it. And so, what I'll show you right now is how we can use this template and other documentation to build an MCP server. And then also I want to walk you through the general

**[0:11:24]** structure so you can truly understand what's going on with these MCP servers because in the end I'm not a huge fan of vibe coding. I want you to really understand what's going on as well. And so with that let's start with the Python SDK documentation so you can see at a

**[0:11:38]** high level what goes into a server. And so it's very easy to get started. You just pip install MCP and then you can import fast MCP which is Anthropic's very easy for way for you to spin up a server. And so you just with this single line start your server for MCP. And then

**[0:11:55]** to attach tools in, you just have to do a little bit of code like this. And so it's atmcp.tool. And then the function that you define below it is now added as a tool to your MCP server. So now when you attach your server to something like cloud desktop, it now has the ability to

**[0:12:10]** call this calculate BMI function and the LLM will decide the weight and height and then it'll get the response back. So it's just like a typical tool call for an agent that you'd implement with something else like N8N or Crew AI or Langchain or Pantic AI whatever it is.

**[0:12:26]** So that's how we add tools to our servers. It's very very easy. And there are other components that you can attach to your servers as well like you can have prompts that the LLM can fetch as a template. You can do images. There are also resources. So this is kind of like

**[0:12:41]** data that you want to keep an LLM updated with in real time. You can attach all these different things. Mostly what people care about these days though is attaching tools to our server because that's really what makes the LLM more agentic when it can do these things on our behalf using the tools that we

**[0:12:57]** have in MCP server. So that's what I'm going to focus on in this video. But really just looking at this documentation, it makes it seem pretty simple. We just define our server and then we attach a bunch of tools and it mostly is that simple. It's really not

**[0:13:11]** that bad. And on top of this, like I've been telling you, you can use an AI coding assistant to make it even easier. And so, going back to the official MCP documentation, they literally have a tab for building MCP with LLMs. So, you go here and then you can visit this page

**[0:13:28]** for the LLM-L.ext. And this gives you the full documentation for MCP in markdown format. So, you can copy everything here and then paste that as a part of your prompt to your LLM. So it now understands everything with MCP. It's super nice. And so you can do that. I

**[0:13:46]** can go into Windsurf for example. You can do this with any AI coding assistant that you want. And I can just go ahead and paste in all the documentation. Boom. There we go. It now understands MCP completely. And the other thing you can do with some AI coding assistants

**[0:14:00]** like Windsurf is they support the MCP documentation natively. So in Windsurf I can just type at MCP and then hit tab. And now it's going to use rag to search to the MCP docs for me. And so there are other ways you can attach the documentation as well. But yeah, this is

**[0:14:17]** a very great starting point. And then you can also paste in my example for my template. And so essentially what your prompt is going to look like is you would say use the MCP docs attached here. Okay. So then we have the documentation. Then I'd say also use

**[0:14:34]** this Python MCP server as an example for the MCP server that you are about to build. So you give this full example right here and then at the bottom of the prompt you would say uh now I want to build my own MCP server to integrate with let's just say light rag for

**[0:14:54]** example. I did a video on this recently. It's a really powerful open source tool for knowledger graphbased rag. And so we could build a server just using the AI coding assistant to essentially have light rag as a tool now for claw desktop or N8N whatever we would want. And

**[0:15:10]** that's it. That's all that has to go into this prompt. And I don't want this video to be focused entirely on using AI to build an MCP server. So I'm not going to send this in and work with this right now. But that's the general structure for a prompt for using AI to code the

**[0:15:24]** MCP server. And so what it would spit out is probably not going to be perfect right away, but it's going to give you a good starting point. And hopefully because it has this template, it'll be pretty close to perfect. That's one of the main goals I have with this. We now

**[0:15:37]** know how to use AI coding assistance to work with MCP and how MCP servers are structured in general. Now, let's dive into this template. I'm going to quickly go through building it from scratch. I'll just reveal the different components to you and explain how it all works together, how I'm implementing the

**[0:15:53]** best practices for MCP2. So the first thing we have to do after our usual imports at the top of our Python script is we want to define the lifespan for our MCP server. I see a lot of MCP servers missing this. It is a very core concept. The reason that we need this is

**[0:16:10]** most MCP servers have some sort of client like a database connection. It could be a mem zero client like we have in this case for setting and retrieving memories. It could be your superbase instance. We only want to define one of those for the entire lifetime of the MCP

**[0:16:27]** server. So for the whole life cycle, we want to define the client once and then never have to redefine it again. And then we also want to be able to do a bit of cleanup at the end because usually when you have something like a database connection, you want to call some sort

**[0:16:41]** of close method to gracefully shut down the connection to the database. And you can do that as well in the lifespan. And so if you've ever implemented an API endpoint before with something like express or fast API, you've probably seen something like a lifespan or life cycle before. It's kind of like the

**[0:16:59]** singleton pattern as well. If if you're into software engineering, I mean, don't worry if you're not. I'm just trying to make connections for some of you here. But yeah, it's just very important to define in our case our mem zero client and then return that. And this single

**[0:17:11]** client, the same instance is now going to be available for all of our tool calls going forward that we'll define in a bit. So very very important. So it's added as a part of this context which is then going to be an argument that's given to all MCP tools going forward.

**[0:17:26]** We'll see that when we define them. And so after the lifespan, now we can instantiate our fast MCP server. So this will look very similar to what we saw in the Python SDK documentation. We just have a couple of extra parameters here because we're giving it a name and

**[0:17:41]** description. We're defining the lifespan here. Obviously, we have to include that in our server. And then for the SSE transport, I'll explain this more later. We we want to define our host and port. So the client will connect to this specific host and port to reach our MCP

**[0:17:57]** server. And now we get to define all of our tools. So we're already to the last component of our MCP server. So just like we saw in the docs, it's mcp.tool or whatever the name of your server is. And then we just define a function that represents one of the capabilities that

**[0:18:13]** we're giving to our server. And so in this case, this first function is going to use mem to save a memory so that our agent can retrieve it in a future conversation. And so the context is given implicitly as the first parameter. So now we can access the memsure client

**[0:18:29]** that we defined right here. And then the second parameter everything after the first one is chosen by the LLM. So it decides whatever text it wants to save as a memory. And then also we have this dock string. And this is actually crucial because whatever we write right

**[0:18:47]** here is the description for the tool that's given to the LLM. And so this will tell it when and how to use this specific tool in our server. And I'll even show you this here. If I go to the MCP server for git that I have hooked in

**[0:19:00]** windsurf right now, all of the slightly grayed out text that you see for all these tools that's below each of the titles, that is this dock string. So whatever you type here is given as the description to the LLM. So I hope that connection makes sense. It's very

**[0:19:15]** important to be descriptive with these. And then as far as the actual functionality for the MCP server with mem zero, I don't want to dive into memero right now because it's not the focus of this video, but you can see that I fetch the client from the lifespan context like this. And then I

**[0:19:30]** just use it to add a new memory to our superbase database. It's very nice and easy. And then I just return a response to the LLM saying that I successfully saved the memory. Or if there's any kind of error, I also alert the LLM of this. And so this will actually bubble up to

**[0:19:44]** us as the user because this response is given to the MCP client like claw desktop and then claw desktop would use this information either the success or the error to tell us what happened when it used this tool. So I hope that all makes sense. And then for the other two

**[0:19:58]** tools that we have in the server, I don't want to explain it in too much detail, but they're also nice and simple. And so we have one tool to get all of the memories that we have for our current user. So again just pulling the client like we did before from the

**[0:20:11]** context this time using the get all function to get all the memories that we have and then in case we have a lot of memories like hundreds and hundreds we might want to search for specific ones. So we also have a tool to do that in a very similar way. So like I said keeping

**[0:20:26]** it simple there's probably a lot of other tools you could add from me zero but I just wanted to show you something practical but also simple enough where you can really take this as a template without having to gut too much functionality. So if you want you could

**[0:20:37]** just take all these tools and delete them and then just add your own with like you know an atmcp.tool and then define whatever function you want. If you want to hook into brave or superbase or light rag whatever you want to do you can do it. So that's all the tools and

**[0:20:51]** then the very last part of our script is just a main function. This is where we really start the server. So we initialize everything and defined all the tools at this point but now we can actually run it. Let me zoom in on this a little bit right now because this is

**[0:21:05]** very important. Most MCP servers don't understand this very well from what I've seen. They usually only make the server work with one of these different transport types, but both are important for different purposes. And I will say that this whole idea of a transport with either SSE or standard IO is the most

**[0:21:24]** technical and difficult part to understand out of everything with MCP because it's the underlying way that our clients and servers can communicate with each other. And so if you really want to dive into the technicalities of this, I would suggest reading the core architecture page of the official MCP

**[0:21:42]** docs. So I don't want to dive into that in a ton of detail right now just to spare you that. I want to focus on building a server, not understanding all of the tiny tiny details. But we have two different methods for communicating with our server. I'm going to zoom in to

**[0:21:56]** really make this easy for you to read here. We have standard IO, we have SSE. And as you saw in the script, I handle both of them. And there's pros and cons to each. So with standard IO, what it's going to do is your client is actually going to start an instance of the server

**[0:22:10]** kind of as a subprocess. So the client manages the server. It's not what you would typically have with something like HTTP. And the reason that you'd want to use this is it's ideal for local processes when you have your MCP server and client running on the exact same

**[0:22:26]** machine. It's very fast. But then we also have SSE. Now, this is more what you might be familiar with with HTTP where you have your browser, your client that's connected to a server, some API endpoint. You have that connection that could also be over the internet. And so

**[0:22:42]** this is very important if you want to not just have your MCP server running on the exact same machine as your client. This is honestly what I think is more important overall, especially because I think the direction we're heading with MCP servers is everyone wants to run them remotely to monetize them or just

**[0:23:00]** host them separately from their client. And then also for certain clients like N8N, for example, they actually only support SSE. And so you would have to build your server for SSE like I'm doing right here if we want to be able to use it in something like N8N. And so you can

**[0:23:16]** kind of see with these pros and cons how we want to support both and that's what I'm doing in this case. And so there's an environment variable that you can you can set. So if you want to look at all these environment variables just take a look at the readme that I have at the

**[0:23:28]** root of the repo. But one of them is the transport that we're using and we can set this to either SSE or standard IO depending on the way that we want to host our server. So, I made it as adaptable as I possibly could for you which is one of those best practices

**[0:23:42]** that I've been telling you about that I've really tried to make sure I hone in on for everything that's important for a server. And so, it's very easy to run with either. There's just a single command that we call on our MCP instance to run with either SSE or standard IO.

**[0:23:56]** So, it takes care of all the hosting under the hood like with Starlet for SSSE for example, if you're more technical and know what that means. Um so yeah, trust me, I've gotten really technical in my research to understand all of this, so I'm sparing you those details. At this point, we have

**[0:24:12]** completed our MCP server. And so now going back to the readme here, we can look at the instructions for setting up everything. And so I have installation instructions both for Python and if you want to run things with Docker, which I'd actually recommend. I think Docker is just a wonderful tool. It makes

**[0:24:27]** everything more standardized and easy to work with. And then you can set up all your environment variables just based on this guide right here. And a lot of this will change if you're not using Mem Zero. So if you are building your own server, a lot of this might change, but

**[0:24:39]** just for this example, this is everything you'd have to set up. And then I have instructions for running it with Python and Docker as well. And then what it looks like to connect to it with your configuration in your MCP client. So I have you covered for literally

**[0:24:52]** everything. Take a look at this. for standard IO for Python, standard IO for Docker. I've got SSE for Python and Docker. All four ways you could possibly want to connect to this server. I've got the configuration for all of that. So what I'll do right now, let me actually

**[0:25:06]** open up my terminal. I'll show you here. So, I'll copy the command to build the container. So, I'll just copy this and then I'll just paste it in right here. And then the port, I'm actually going to change this to 8070 just because I have it running already in the other port.

**[0:25:20]** And so, I'll build the container completely from scratch. I'm just in the directory that we've been working in building out our MCP server in that Python script. And so it's building the container. It's actually pretty fast overall. Like MCP servers are pretty lightweight, which is part of the beauty

**[0:25:35]** of it. So I'll let it do its thing and run everything. It's already exporting the final container. And then I can just go down to the bottom here and let's just say I want to run it with SSE and Docker right here. So I'll just copy this command and then I can clear the

**[0:25:48]** terminal and run this one. And then boom, there we go. We now have our MCP server up and running, ready to connect with any client that we want. So, it's running on port 8070. So, uh, for example, I can go into N8N just to change the port from 8060 like I was

**[0:26:03]** using before to 8070 now. And then I can ask it the same question. What memories do I have? So, I want it to tell me for the 60th time in this video that I like chicken. Let's see if we get the same thing. Yep, likes chicken. All right.

**[0:26:16]** And I can even go into the Docker container and the logs and see that all the requests from my N8N agent are coming through right here. Take a look at that. And we can take this a little bit further here. Let me actually tell it I also like

**[0:26:28]** beef. Now chicken and beef are both great. All right. So I want to store an updated memory here or maybe a second memory that I also like beef just so we can see another tool being used so I'm not just always asking the exact same thing. So all right, it updated the

**[0:26:45]** memories. Great. Now, and I can refresh this and I can now ask it what foods do I like. So now it should say that I like chicken and beef. Retrieving both of those memories. So let's see if we get the right answer. There we go. You like chicken and beef. So this server is

**[0:26:59]** working great. And it's all using the power of MCP for this connection. And it's so easy to take this and build your server for literally whatever you want. And of course, let me know if you have any questions on this template as you use it for yourself. If you think

**[0:27:13]** there's anything that I could do to improve this template, let me know about that as well, because I really do want to make this the perfect starting point for anybody looking to build their own servers. So, I hope that this video has really helped you see how easy it is to

**[0:27:27]** build your own MCP server to connect your AI agents to literally anything. Also, I have a lot more content coming out on MCP soon for things like building out specific use cases and more ways to leverage this very powerful protocol and more things for AI agents as well. So

**[0:27:43]** stay tuned for that. If you appreciated this video and you're looking forward to more guides like this, I would really appreciate a like and a subscribe. And with that, I will see you in the next
