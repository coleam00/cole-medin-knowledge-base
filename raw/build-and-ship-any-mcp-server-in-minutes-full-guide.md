---
type: raw-transcript
title: "Build and Ship Any MCP Server in MINUTES (Full Guide)"
youtube_id: Zw3sfAIpeH8
url: https://www.youtube.com/watch?v=Zw3sfAIpeH8
slug: build-and-ship-any-mcp-server-in-minutes-full-guide
published: 2025-07-09
duration: "0:31:01"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Everyone these days is using MCP servers, but almost no one knows how to actually build and ship production ready MCPs. And that's what we're going to dive into in this video from scratch. And I'm going to make it surprisingly straightforward with a template that you can use right now. When Enthropic

**[0:00:16]** launched the model context protocol last November, it was genuinely impressive. Finally, a way for us to connect our AI agents to our external tools. It is the way to give our agents and also our coding assistants like cursor and claude code superpowers by connecting them to our systems and data. And MCP really

**[0:00:36]** blew up starting March of this year. Everyone was and still is paying attention to it and it's getting adopted all over the place. But when it first blew up, there was still a huge problem with it. It was essentially still a toy. security vulnerabilities, no authentication, documentation was

**[0:00:53]** lacking at best, and there was no way to deploy remote MCP servers. When you wanted to run one yourself, you had to actually download and host the MCP server on your own computer. But my friend, that is all changed now. While everyone has been focusing on cloud code

**[0:01:08]** right now, and for good reason, Anthropic has been quietly building out the production infrastructure for MCP that we have all been waiting for. They have streamable HTTP as a new transport for the protocol that actually scales. They're implementing OOTH, so we have real authorization and authentication to secure our MCP servers. They have a

**[0:01:28]** bunch of documentation around security best practices now. And we have enterprisegrade remote MCP deployments with platforms like Cloudflare that actually make it really straightforward. So, Anthropic is really pushing MCP far. And let me just say they have been crushing it recently with Claude, Cloud Code, and MCP. Right now, I'm going to

**[0:01:49]** show you exactly how to build productionready MCP servers from the ground up. This is the future of how we're going to be powering all of our AI agents. And it starts with this super comprehensive template that I have created for you. This is what we're going to be covering today. and I follow

**[0:02:04]** all the best practices here for ways to add tools into our MCP server to handle authentication and monitoring and security and deployments. This isn't just a tutorial. This is a complete blueprint for you to take and use to build any MCP server that you want. We're going to build it together, then

**[0:02:21]** we'll deploy it to Cloudflare, and then I'll even show you how you can use AI coding assistance to use this as a starting point to build anything that you want. I'm really excited for this. So, let's go ahead and get right into it. So, what we're going to be building

**[0:02:32]** in this video is a TypeScript MCP server that has authentication built in with GitHub OOTH. We'll also be integrating with Sentry so we can monitor our MCP in production. And we'll deploy it to Cloudflare. Cloudflare is not sponsoring this video or anything. They're just the go-to platform for deploying remote

**[0:02:50]** MCPs. And I've gotten a lot of requests to cover them specifically. So, finally, here it is. Also, we'll be supporting the new streamable HTTP transport layer and then for legacy purposes supporting SSE. And then just to have a very simple but still practical demo for this template, we're building a basic MCP

**[0:03:08]** server that works with our Postgress database. It's kind of like a chat with your database MCP server. So, you just have to give the connection details for your Postgress account. We'll get into that in a bit. And then we have these three tools. One where we can list all

**[0:03:21]** of the tables that are in our database. We have another one to execute readonly queries on our database and then another one to execute write operations. And this is where GitHub ooth comes in because we're going to have authorization protecting this MCP tool specifically. So only a specific set of

**[0:03:38]** GitHub users can even see and use this tool. And the reason that we're building this as a TypeScript MCP server is because TypeScript is becoming the go-to language for building MCPs. I haven't covered TypeScript enough on my channel and also it is the best programming language to use to build remote MCPs

**[0:03:56]** that we want to deploy to Cloudflare. And getting this template up and running yourself is very straightforward. There are just four prerequisites that we have here. First, you'll have to install Node.js. Then you'll need a Cloudflare account. You can just use the free tier. This will work for this entire demo. So,

**[0:04:10]** you just go to cloudflare.com, create a free account. Everything in this entire video is free, by the way. And then you'll need a GitHub account for OOTH. and then obviously a Postgress database for this specific MCP server. Once you have all those prerequisites in place, then you can install the Wrangler CLI.

**[0:04:27]** This is how we can work with Cloudflare in the command line in our computer. So, it's just mpm install-g for global wrangler. And then you run the Wrangler login command. This will direct you to Cloudflare in your browser to authenticate. So, now your CLI is authenticated with your new Cloudflare

**[0:04:43]** account. And then the last thing that you have to do is just clone this repository. Okay, so you just go up here, get clone, and then this is your URL. And then you can run the mpm install command to install all of the dependencies here for our Wrangler

**[0:04:56]** Cloudflare worker project. And then you are good to go. So before we dive into the main MCP server implementation for this video, there's one more thing that I do not want to miss with you because we need to set a solid foundation here, understanding how MCP works at a core

**[0:05:11]** level. And so I have a basic example in this repo that I want to cover first. Then we'll add in the extra layers of complexity for things like authorization, monitoring, and deploying to Cloudflare. In this basic example, I have based a lot on the documentation that we have here in the GitHub page for

**[0:05:28]** the TypeScript MCP SDK. So, I'll link to this in the description as well as the primary template that I have for you. Really, everything that I'm covering in this video, I'll link in the description. So, there's just a gold mine of resources for you. But this is really important. We don't want to miss

**[0:05:42]** the core of what makes an MCP server. So with TypeScript, we want to import MCP server and then also the transport layer that we're using. Like they're using standard IO in this case for a very basic example. Obviously, we're going to be upgrading to using streamable HTTP and SSE. That's more what you need for

**[0:05:59]** remote MCP. But anyway, we create an instance of our server and then we can register tools. That's what we'll be focusing on in this video. These are all the functionalities that our server exposes. And then you can also do other things like sampling and resources. There's a lot of different components to

**[0:06:13]** an MCP server. And then you just define the transport that you want. And then you spin up your server. And that's it. You now essentially have an API endpoint, but instead of it being for a website, it's for an AI agent. And that's really important to keep in mind.

**[0:06:26]** It's like everything that we're building here is not new. And the best practices around security, it's not new. It's all just APIs, but repackaged in a standard for AI agents specifically. That's all MCP is. But even though that's all it is, it still is very powerful. So that

**[0:06:42]** is our quick start and that's what I want to show you here. So I have the repo for our template cloned locally. And then we have this simplemath.ts. This is the very basic MCP server that is adjusted to work with Cloudflare. And then we'll build on top of this to make

**[0:06:57]** our full implementation. So the agent/mcp, this is actually an import from Cloudflare. It's their agents offering. So we use this to build the main class for our MCP server. Then we define a server just like we saw in the GitHub page. And then we initialize all of our

**[0:07:13]** tools. So it's just this.server.tool. We give the tool a name. We define the arguments as well. You can also give a description to help the AI agent know when and how to use a tool. We'll cover that later as well. And then the function definition itself is what is

**[0:07:28]** going to run whenever our AI agent or coding assistant or whatever invokes the tool in this MCP server. So this is a very basic implementation where it's just a tool that we can pass in numbers that we want to add, subtract, multiply or divide. And then towards the bottom

**[0:07:42]** here, we're going to serve this MCP server both with SSE for legacy purposes. And then also /mcp just the regular.serve. This is for streamable HTTP the new transport that we have. So with that, now going back to our readme, all we have to do, assuming you already have Wrangler set up with these steps,

**[0:08:02]** is you just have to run the Wrangler dev command specifying the configuration for our MCP server, our simple version. So you just run this command in the directory where you cloned this repository. And then boom, our MCP server is now up and running, ready to be connected from any MCP client,

**[0:08:18]** cursor, cloud code, cloud desktop, anything. And I'll even show you an example right now with cloud desktop. So, I've got my cloud desktop up. You can see that I have the math MCP server with my calculate tool. And the only thing I had to do to set this up is go

**[0:08:32]** to the top left, file, settings, developer. This is where you enter in your configuration for MCP. So, you just click on edit config. This will bring you to a folder that'll look like this. And then you can open up cloud desktop config. So, I'm going to open this up. I

**[0:08:47]** have a bunch of new lines here. So, you can't see my secret keys and my other MCPs. But to connect to this one, we just do npxmcp remote and then it is going to be our localhost 8789 because that is the URL that we have this running in right now

**[0:09:02]** because we want to use streamable HTTP that is going to be our /mcp endpoint. So this is how we connect to our MCP server. Now we can test this out. So I'll close out of this. You have to restart your cloud desktop by the way once you add in the configuration. And

**[0:09:16]** now I can say use the calculate tool to calculate. And then I'll just do a random number multiplied by a random number. And so I'm being explicit here just because I want to make sure it's using the tool. But I'll send this in. And now Claw Desktop will ask for

**[0:09:29]** permission to use our custom MCP server. In my case, I already approved this before, but it'll ask you for permission. And there we go. It used the calculate tool. We have the two numbers multiplied together. There is our response. So this is looking really, really good. That is MCP at a very high

**[0:09:45]** level. Now, let's start adding in the fun stuff for GitHub authentication, security, monitoring, you know the drill. So, here is the game plan just so you know the exact order of things here. I'm going to start by showing you how to get this MCP server up and running

**[0:09:59]** yourself. It's very easy. Then, we'll dive into how everything works. I've got some key resources to share with you as well. Then, we'll deploy everything to Cloudflare so we have a production environment for our MCP. And then last but not least, like I promised in the intro, we'll show you how to use AI

**[0:10:14]** coding assistant. So you can literally take this template, give it to an AI coding assistant, and have it build any MCP server for you that you want. And so at this point, you already have Wrangler installed and configured. You've got the packages installed, you got the repo cloned. Now we can move on to setting up

**[0:10:29]** our environment variables. And so you just have to make a copy of this file and rename it to.dev.vars. This is just like aenv, but more specific to Cloudflare workers. And there are only four environment variables that we have to set up. At first we need our GitHub client ID and

**[0:10:44]** secret encryption key and then your database URL which depending on your platform this can really be any Postgress platform. It can be superbase neon you could host Postgress yourself. Just get your connection string for this environment variable. And specifically the way that you get your GitHub ooth app is within GitHub you just go to your

**[0:11:02]** settings in the top right go down to developer settings and click on ooth apps. You can make a new app here and this will then give you your client ID and secret. So very easy to get that set up. This is for the authentication for our MCP. A very important component. And

**[0:11:16]** then for the encryption key, you can just set this to whatever value you want. Very easy to get all that set up. And then we'll cover sentry towards the end to add monitoring for our MCP in production. And that is it. That is everything. And now we can go ahead and

**[0:11:28]** run the Wrangler dev command to get our MCP server up and running. And so it's going to be very similar to the simple example that we already covered. So I did that on purpose so everything will start to look very familiar for you. So we're running kind of a simulated

**[0:11:41]** version of our production environment here. So we're running a Cloudflare MCP server, remote MCP, but it is just running in our terminal here on our local machine. And the port is different from the simple example. And so you just have to go back into your cloud desktop config or the config for whatever MCP

**[0:11:56]** client you're using like cursor or cloud code and just change the port to 8788. And then you want to restart your MCP client. And so that's what I already did with cloud desktop. And now within here we have our new MCP server. So I should probably rename this from math. But

**[0:12:12]** anyway, clicking into here, we now have our three database tools that we have for Postgress. And so I can ask a question like what tables are in my DB? And then when I do this right now, I've already gone through the GitHub OOTH process and approve this tool usage. But

**[0:12:28]** for you, what's going to happen here is it's going to actually open up a page in your browser to sign in with GitHub before you use this MCP. That is the beauty is we have this gateway now to our MCP server with GitHub authentication. And the world is your

**[0:12:43]** oyster for the way that you can protect your MCP server now that we have authentication in front of it. And so I'll show a couple of screenshots here what that actually looks like to go through that flow. Then we go back to claude code where we have what we're

**[0:12:55]** looking at here where it says I have 19 tables in my database. And this is looking really really good. And we can even test another one here. I'll say what records are in my users profiles table. And so this will query a specific table here. I'll give it a second to run

**[0:13:10]** this. There we go. So select star from user profiles. Looking really good. And I just have three records right now with just the test accounts that I have created in this superbase. This isn't my production superbase or anything. So yeah, there we go. This is working so so

**[0:13:23]** well. So now let's get into how I built this MCP server, all the best practices that go into it. Starting with the resource that I used as the beginning point for creating this template for you because Cloudflare in their AI repo. They have this demo here, building a

**[0:13:38]** remote MCP server with GitHub OOTH. This is a fantastic resource that got me started. Like I said, I'll have a gold mine of resources in the description. So, this will be linked in the description as well as some other really helpful docs from Cloudflare on building a remote MCP server. And then also they

**[0:13:54]** have a section specifically on authorization, which this is awesome to check out if you want to extend past GitHub and add an authorization for other providers as well like Google or X. So, these are great resources. And then last but not least, I want to talk about the security checklist for MCP.

**[0:14:10]** So, this is what I used to determine all the best practices that I needed to follow to build my MCP server. And so, super pro tip here, you can take this resource, again, linked in the description. You can go through this checklist, copy everything here, and literally just paste it in as a part of

**[0:14:27]** your prompt to your AI coding assistant when you want it to build an MCP server. You want it to follow these things. And that's what I did. And you can maybe take out some of these things that might not apply to your server. Like not everything here is going to be super

**[0:14:40]** applicable, but this is a really good starting point to just open your eyes to all of the security practices that are important not just for MCP servers, but really any back-end infrastructure. I mean, really, like I said, MCP servers are just APIs, but for agents. And so, yeah, this is just really important to

**[0:14:56]** follow this. And so, that's what I did. There's quite a few rules here, but it all boils down into what I have at the top of the readme here. So we want our database integration with a lifespan. The security checklist talks a lot about lifespan so we can manage resources like

**[0:15:10]** database connections in our server and close those down gracefully. We want modular singlepurpose tools so the LLM doesn't get confused when it's using our MCP server and descriptions are very important for that. We'll talk about that in a bit. We want role-based access using GitHub OOTH in our case,

**[0:15:28]** especially protecting those more sensitive tools like executing any write query in our database. And then security best practices, things like validating and sanitizing the SQL queries that we run with this server, monitoring in production with Sentry is huge. And then having a cloud platform to deploy the remote MCP to that is good for scaling.

**[0:15:47]** That's why we're picking Cloudflare workers in our case. So these are the key practices that I'm following here. And I'll walk through our server very quickly here. And I'll just point out when each of these apply. And what we're about to see here, a lot of it looks

**[0:16:00]** very similar to the simple example that we already went over. I did that very much on purpose just to kind of ease you in to all these other layers that we're adding in for things like authorization, getting things ready to deploy to Cloudflare as well. And so, first of

**[0:16:14]** all, we have this list at the top, all of the allowed GitHub users that can use that more sensitive write query tool. And obviously in production, if you want to go past a demo, you'd want to have this list somewhere in a database. I'm just using this for simplicity purposes

**[0:16:28]** here. But it's the same kind of deal. We're using the MCP agent that we're importing from the Cloudflare agents package, setting up our server, and then as a part of our lifespan, we want to close our database down gracefully whenever we exit the server so we don't have memory leaks. And so the way that

**[0:16:42]** this works is when we start up our server, and I'll show you this here. When we start up our server, we're going to get an instance of our database. We're going to use that throughout the lifespan of our MCP. And this is something I see people just miss all of

**[0:16:56]** the time. Lifespans are so important. Definitely one of the things that's covered in the security checklist. They call it a life cycle management, but then they have the whole concept of shutting down, cleaning up resources like our database. That's what we're doing here. So, we get the database

**[0:17:08]** instance. This is what we use throughout the lifespan of our server. And then we're going to clean up when our server closes. And then when we initialize our tools, this is where we get into tool descriptions. So what we're looking at right here, this is actually used as a

**[0:17:23]** part of the prompt to our large language model that is leveraging this MCP server. That is so important to keep in mind. This context is key for the agent to know when and how to use this tool. So make sure that you have a nice clear and concise description for every single

**[0:17:39]** one of the tools in your MCP server. Then we're getting our single database instance. This is our tool to list all the tables we have in our DB. And then we're also returning a very nicely formatted string here with all the information that we got back from that

**[0:17:52]** query. So that's yet another thing is like this information goes back to your LLM. So you want to treat it with respect. Make sure that it's formatted very nicely. And we're doing this in JSON here. And then for our other tools, very similar. This is our one to execute

**[0:18:04]** readonly SQL queries. And this is an example of implementing security best practices. So we're validating our SQL query. And I'll show you what that looks like. We're looking for dangerous patterns and we're failing the tool call if we find any of these. So this is just a simple example the kinds of things

**[0:18:19]** that you want to be thinking about when implementing security for your MCP servers and like I said really any kind of backend infrastructure that you're making and you want to make sure that AI coding assistants are following these kinds of things as well as you're using them to build these servers. And so I'm

**[0:18:34]** going to scroll down here skip past the rest of that tool. This is where we get into GitHub authorization. So when we have GitHub ooth set up in our server and we'll see what that looks like towards the end of this file. We have this value here, this.props.login.

**[0:18:48]** This has all the information about our user and the login specifically gives us their GitHub username. So we can check to make sure that they're in this list of allowed users. If they are, then we expose this tool. Otherwise, we're not even going to make this tool as an

**[0:19:03]** option for the user when they are using the server through their MCP client. But if they are allowed, then we have this. We're validating the SQL query again. We're executing that, making sure that it's a safe operation, and then returning the results of executing that query. And we're adding error handling

**[0:19:17]** with these catch blocks into all of our tools as well. You want to make sure that you handle errors gracefully, maybe even having the MCP server return an error message so the agent can communicate back to the user and say what exactly went wrong. So that is everything for our tools. Then at the

**[0:19:33]** very end here, we're using this OOTH provider that we are importing from Cloudflare. So, one of the beauties of Cloudflare, they're not just making it easy for us to scale and deploy our MCP server. They actually handle the server side of the authentication as well. There's a lot more logic that we would

**[0:19:49]** have to implement if we weren't using Cloudflare's OOTH provider. So, there's still some of the client side stuff that we have to implement here. And you can look into this if you're curious. You could also change this to work with something like Google Oath instead. In our case though, we just have that set

**[0:20:03]** up for the GitHub client side and then the server is handling the rest. And so we have our API handlers. We have one for SSE. And then we have one for streamable HTTP. And then we have an authorize and register endpoints here. You can follow the Cloudflare documentation to know how to set all

**[0:20:17]** this up. And then we have our GitHub handler. That is all the client side OOTH logic that we have. And then we have our token endpoint to end things off. So that is everything for GitHub authentication. It is that easy to get things set up. And you can always use an

**[0:20:31]** AI coding assistant. If you want to point it to this and then point it to the GitHub handler and say just change this for Google or change this for X, you can definitely do that. And then the very last thing going back to the readme here, the very last thing that I want to

**[0:20:44]** cover before we deploy is monitoring. And so this I've kind of made this an optional thing. So Centry is actually sponsoring this video. They're partnering with me to show you how to monitor MCP servers in production. But I wanted to cover this anyway. And Century really is the best platform. It's really

**[0:21:00]** the only one that I know of that makes it super easy to integrate application monitoring with MCP server specifically. It's so cool because if I go into my dashboard here, all you have to do is go to centry.io, the free tier works for this by the way, you have to just make a

**[0:21:16]** new project and specifically the project type. If I click on create new project, you just want to search for Cloudflare workers JavaScript. That's the type that you create for Sentry. You'll get that DSN which you use as your environment variable. And then we can start seeing traces come through like it use my list

**[0:21:32]** tables for my MCV. So I can click into this and I can see the logs and all the metadata that happened with this query. I can see the duration if there are any errors that come up. I'm also going to get an email like you can see right

**[0:21:42]** here. This is just an example of the email you get. So you have alerting setup for when things fail. It is really powerful to have this kind of monitoring in a production environment especially once we deploy things to Cloudflare. So super important. If you want to set up

**[0:21:56]** Sentry, all you have to do is add in this environment variable, the DSN, and you just get that from your Sentry dashboard once you sign up with the free tier. And then you just want to swap these two files. So you can rename this one to index_enty, something like that. And then you just

**[0:22:12]** rename this to index.ts. So I just have a separate version here if you want to enable Sentry for production monitoring of your MCP. And I'm not going to dive into the details a ton here. What I did do is I followed this guide that I'll also have linked in the description, monitoring

**[0:22:28]** your MCP servers in production. And they actually went off of the uh GitHub ooth example from Cloudflare and they showed how to integrate the monitoring within it. So really, really convenient. It worked out super well for me. I'm really glad I found this resource. But yeah, we just configure Sentry. We have a

**[0:22:44]** function to handle any errors that come up. So we can have that tracing within our Sentry dashboard. And then going down to the bottom here, we just have to wrap our OOTH provider within Sentry. So it's just sentry.withentry. We're just installing that mpm package. And then we're wrapping our worker. This is set

**[0:23:00]** up in basically the same way that we have in our nonentry version. So we're just kind of creating this wrapper here that's going to watch for any errors that happen with any of our tools and then log those out to Sentry as well as all the successful calls. So you can

**[0:23:12]** just see at a high level everything that's coming in, all the traces for our MCP server. So yeah, Sentry is just an awesome platform. I would highly recommend using them to monitor not just MCP servers, but also just any kind of back-end application. I use Sentry to monitor my AI agents in production as

**[0:23:30]** well. And so I use Langfuse as my platform more specifically to monitor agents, but then my whole like backend infrastructure and rag pipelines, Sentry is a great option for that kind of monitoring. So with that, we now have an MCP server following all the best practices that we can take to production

**[0:23:46]** with Cloudflare. So the first thing we have to do, we already have Wrangler set up. So we just need to run some commands to get things set up in our production environment. So I've got my terminal back up here. We need to first create a KV or a key value store. This is we're

**[0:24:00]** going to keep track of everyone that is already authenticated with GitHub. And so it's kind of like our mini database to manage OOTH. And so wrangler KV namespace create and then the name for our KV store is going to be oath KV. So I'm not going to run this command

**[0:24:14]** because I already have this created. But once you do, it's going to have an output here that's going to give you your unique KV ID. So you want to copy that. We'll see what to do with that in a bit. The other way that you can get this ID once you have this KV created is

**[0:24:28]** you can just go to the KV section of storage and databases in your Cloudflare dashboard and then you'll see it right here. So you can just copy the ID here as well. So take that ID then go into your regular.json C. There'll be a placeholder here for the KV ID that

**[0:24:41]** you'll just replace with your unique identifier. So once you have that now go back to the readme and we are ready to deploy. So we can just run the Wrangler deploy. It is that easy now that we have everything set up to deploy to Cloudflare workers. So we will have our

**[0:24:56]** MCP server running remotely in the cloud. So Wrangler deploy and this is actually blazing fast. It just has to upload it to the Cloudflow worker environment. Super super fast. And then there we go. We now have our production URL for our remote MCP server. It's so so cool. We can use this to then connect

**[0:25:14]** to it with cloud desktop in a little bit or whatever MCP client you're using just like we did when we were running it locally. And the other way that you can get this URL, just by the way, if you go into the workers and pages tab here in

**[0:25:27]** compute workers, we can see all of our Cloudflare workers. Right now I just have the MCP server right now. So you can click on the visit link right here. It'll say 404 not found. But this is the our production URL. So you can copy that. We can also, you know, do the /mcp

**[0:25:42]** endpoint. It's going to say invalid token because we're not authorized with GitHub obviously. But yeah, this is our URL. So you want to copy that. And then you can go into your cloud desktop configuration or whatever you are using for your MCP client. And then we're just going to replace this URL like this.

**[0:25:58]** Boom. There we go. We are now good to go. So, we're connected now to our production MCP server. So, cool. And the last thing we have to do before we actually test this is we need to set up our environment variables in production. So, running locally, we just did things

**[0:26:14]** in.dev.vars. Now, we have to actually put these secrets in the cloud. And so, you can manage this in the dashboard if you want as well. So, the way that you do that is you click into your worker. And by the way, you can see all of your requests

**[0:26:28]** and metrics and monitoring here as well. But if we go into settings, we can see all of our secrets. So you can set these manually here or you can just follow the commands in the readme to put all of your secrets just from the command line. So it's just wrangler secret put and

**[0:26:42]** then the name of your secret like client ID. And then you'll just enter in the value once you are prompted. So I'm not going to do that here cuz I already have that set up like you could see in my dashboard, but you can go through with that and you don't have to redeploy. All

**[0:26:53]** of your secrets will be good to go. So now we are ready to connect to our MCP. So I've got my configuration all set up. I'm going to off camera here restart my cloud desktop. Open it back up again to apply the latest URL. And there we go.

**[0:27:08]** We can now test this out. So I'm going to say what tables are in my database. The same kind of query as before. What tables are in my DB? But before I do this, I actually had this pop up just now. There we go. We have our authorization request. So, this is what

**[0:27:23]** I was talking about earlier where I had a couple screenshots come up, but now we're seeing this live. So, it's requesting access. I'm going to click on approve. And then I just need to authorize my GitHub account, which I already did. So, that page isn't popping up here, but it'll have you connect your

**[0:27:37]** GitHub account for your first time. So, there we go. I can close out of this now. And then I can enter in my query. What tables are in my DB? And this is going to look the exact same, but now it's using a remote MCP. So, let's give

**[0:27:48]** it a second here to connect. For some reason, Claude is just taking its time. And there we go. It's using our MCP server. Let's see if it gets the 19 tables just like if we were running it in development. It's taking a little bit longer here just because it's a remote

**[0:27:59]** MCP now, but still really fast. And there we go. We got our 19 tables. And I could even try a request here just to try with the GitHub O the protected tool. So I can say add a new record to my projects table. It can be just random values. So

**[0:28:20]** we'll just try this out here using this tool. So add a record to my projects table and so I'll go ahead and pop up my superb basease and I'll show you this afterwards. But yeah, so it's inserting into projects got random values that it's generating here. It's requesting to

**[0:28:33]** use this tool. So I'll just allow it always. We'll see if it can add this record to Superbase. And there we go. We added the record. Sweet. So it is for an AI powered recipe generator. And sure enough, if I go into my Superbase dashboard, I now have a project for an

**[0:28:48]** AI powered recipe generator. Take a look at that. So, we have our MCP server fully working and we have it deployed to Cloudflare. So, I can go in here, I can view the metrics, I can see all the requests coming in. So, I can refresh this and we'll see the requests go up.

**[0:29:02]** There we go. We got 27 requests now because we have all the the whole like handshaking process with MCP as well. That's why there's so many requests. But yeah, everything is working perfectly. So that is deploying MCP servers following best practices in a nutshell. So there you have it. We have created an

**[0:29:18]** MCP server from scratch, implemented best practices for things like our tools and lifespan and security and monitoring and we've deployed it as a remote MCP that we can now use anywhere with any MCP client. And we have GitHub OOTH. So it's not like people can just abuse our

**[0:29:34]** MCP and you can set up things like rate limiting and even monetize your MCP server in this way. And I have been talking about using AI coding assistance throughout this video already. But the big thing I want to say with this is you can literally take this GitHub

**[0:29:47]** repository, put it in your current project where you want to make a new MCP server and you could tell your cloud code, tell your cursor, whatever to go look at these files to understand how I've implemented an MCP server following all these best practices. You can even have it reference the readme. You can

**[0:30:05]** have it reference the security checklist like we talked about earlier. You can use all this for context. This is kind of like context engineering like I talked about in my last video. All of this can be context to provide really good examples to the AI coding assistant. So it can knock out any MCP

**[0:30:20]** server that you want to make. And you can even do things like switch from GitHub to Google for your OOTH. And so definitely check out my last video on context engineering if you want an example of a process where you can incorporate what I just talked about. I

**[0:30:32]** don't want to cover that all from scratch right here because I just covered that on my channel. So definitely check that out if you are interested. But yeah, with that, you now have what it takes to build production ready MCP servers that are bulletproof. And so I hope that you found this

**[0:30:47]** template super super useful. If you did, I would really appreciate a like and a subscribe. Definitely a lot more content coming for MCP and deploying agents to production in general. And so with that, I will see you in the next
