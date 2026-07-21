---
type: raw-transcript
title: "I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does."
youtube_id: R-5_2nsF_ZM
url: https://www.youtube.com/watch?v=R-5_2nsF_ZM
slug: i-love-the-karpathy-llm-wiki-but-it-doesnt-scale-heres-what-does
published: 2026-07-08
duration: "0:18:58"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** There are two very different kinds of AI agents in the world and right now it feels like everyone is hyper fixated on one of them, personal agents, like the one you're looking at right here. You're generally have a coding agent like Claude Code or Hermes or Open Claw

**[0:00:14]** running on your machine, helping you manage a bunch of interconnected markdown documents that make up your knowledge base. And so typically you'll have something like a Karpathy LLM Wiki for your organization. You have your index documents with your tagging and categorization and all of your entities. You're building this up over time with

**[0:00:32]** your agent. And don't get me wrong, personal agents are extremely powerful. This is mine you're looking at right here. I use it every single day. But also there is a line that has to be drawn where personal agents they don't scale. And really it's when you want to

**[0:00:47]** ship an agent to other people, you no longer can use the LLM Wiki locally running agent setup. It has to look totally different. And that's what I want to focus on in this video because I myself been doing of content on personal agents. And I feel like I haven't

**[0:01:03]** covered the other side of the coin enough recently. And so we'll talk about what this really looks like, why we have to fundamentally change our approach to building agents when we're shipping for other people. So let's first start by talking about why everyone is building personal agents or second brains in the

**[0:01:20]** way that they are. Then we'll get into how the architecture has to ship for production agents and how we can accomplish that. And so everything for a personal agent is markdown driven. It really doesn't matter what you build for yourself or what you use off the shelf like Hermes. It is always markdown. And

**[0:01:37]** the reason for that is for a personal agent, it's just the simplest and most flexible. It is so easy to build up your knowledge base over time as you're having conversations with your second brain and pulling in other information. The power here is keeping everything on your own system so it can be as

**[0:01:53]** accessible and fast as possible. And at this point we don't really care about governance or access control or a lot of the traceability and auditability that you need in production systems. And so, just keeping it as simple as possible. But, as soon as other people are using your agent, so many users at once, you

**[0:02:11]** have live data, you need to care about things like access control and retrieval at scale, that is when this just it doesn't cut it anymore. I mean, first of all, there's a reason we have databases in the first place. If you're managing everything with just markdown documents, your organization and search, even just

**[0:02:26]** creating all the files and managing all that is never going to scale. And also, second brains are actually quite expensive. Generally, you're using a coding agent SDK like Claude or Codex, and you're using it with your subscription. And so, when you go to production, you can't use that

**[0:02:42]** subscription anymore cuz it's only for personal use. And all of the system prompts and tooling and everything that you're dumping into your second brain and having it read through entire markdown documents, like it doesn't really matter how much you optimize it. It's really never going to cut it for

**[0:02:57]** how much you have to scale the retrieval and the cost optimizations in production. And so, that's where we get to our architecture here. What does it look like to ship an agent for others? We still want to have all the same benefits of a second brain where we can

**[0:03:10]** have user memories and we're able to organize information for the agent to retrieve well, but everything has to look different. And I also want to go into this by saying that this setup right here is way more common than personal agents. I think the reason people are so hyper-fixated on these

**[0:03:26]** right now, it's for good reason. It's that it's just so applicable to everybody. No matter what you do in your life, you can use a second brain to help you manage your job or your personal life. But, the thing is, almost anything that's really providing real business value is an agent that is shipped as a

**[0:03:43]** part of a platform to a production environment with other people logging in and talking to the agent. And that is the architecture that we're we're about right here. So, here we're using a database to scale. Markdown doesn't cut it anymore. We can't just have a Hermes or Claude code wiki for production

**[0:03:59]** agents. And there are two things that our database needs to store and handle for us and give our agent access to. We have the context retriever and agent memory. These are the two things that I'm going to focus on for the rest of the video here. And I'm going to be

**[0:04:13]** using Redis as a platform to drive all of this in this video, but really these ideas apply to any system you're going to create for a production agent. Because essentially what we have here is a wrapper over our database. It's the context layer for our agent. So, we have

**[0:04:30]** the context retriever. This is giving our agent access to our business data and telling it the format, helping it understand what it can query. And then the agent memory is the short-term and long-term memory for our customers. We want to build up intelligence of our users for the agent over time. So, for

**[0:04:48]** the demonstration that I have for you today, I'm going to be using Redis. This is the best platform that I could use for a demonstration of both the business context and the user memory all in one place because they recently put out Redis Iris. This is in preview right

**[0:05:03]** now, but it is extremely powerful. It really is the entire wrapper over Redis as the database to give your agents better access. So, we have the context retriever. This is how we allow our agent to understand and search through our data through an MCP server. Very, very neat. And then we have agent

**[0:05:20]** memory. This is for the short-term and long-term memory of our users and actually storing their memories in Redis as well. So, we'll talk about all this. I'll cover how it all works, but first I want to just give you the high-level overview here. And I will say that I am

**[0:05:34]** working with Redis on this video. They reached out to me and I've been looking for a database platform to use as an example for this exact video for a while now. And I've been seriously impressed by what they've released here with context retriever and agent memory. That's what we're going to be focusing

**[0:05:50]** on here. And again, you can take these ideas and apply them to any production system. This is just what gives the best explanation right now. So, going back to our database, this is our key-value store that houses a bunch of mock data for an e-commerce store. I picked this

**[0:06:06]** as the example because every single e-commerce store should have an agent to help you with analytics and a customer-facing one for support. And so, we have all of our information for our customers. This is just key-value pairs, nice and flexible and unstructured in Redis. This is obviously fake for each

**[0:06:21]** one of our users here. And then we have orders, and then we have products and shipments. So, this is all of the data that we want our agent to be able to search through to help users understand where their orders are, to perform analytics for the internal team, that

**[0:06:35]** kind of thing. And so, to build an agent on top of this, I've created a Pydantic AI agent. I'll link to this GitHub repo in the description as well. I still love using Pydantic AI for all of my production agents because coding agent SDKs, like the Claude agent SDK or Codex

**[0:06:53]** SDK, I know they're very popular now, but they're slow because they're made for longer agentic coding tasks, and they're also more token heavy. So, for anything that you're shipping to production, Pydantic AI is still my recommendation. So, this is a Pydantic AI agent that has access to the context

**[0:07:08]** retriever MCP that we'll cover more in a bit, and then also the tools to access the agent memory, all happening in the same Redis database using Redis Iris to access the database with both of these capabilities. And so, I already have this agent up and running. I'm not going

**[0:07:24]** to get into the code for it today cuz that's not the point of this video, but I'll show you how the context retriever and agent memory can work in tandem. This is the big payoff, and then we'll get more into how each of the individual components work. And so, I know this is

**[0:07:37]** a little bit of a silly demonstration. We don't have any user interface. There's also no authentication, so I have to say explicitly who I am, but obviously when you take this agent, like if you build with Pydantic AI and Redis Iris, you're going to build it into a

**[0:07:50]** front end and you're going to have authentication, so the agent knows who you are without you having to say so. But here for the demo, I'm saying it's Jordan Rivera, customer 1004. Why is my order late and can you handle it the way I asked last time? This is actually a

**[0:08:04]** pretty loaded request because it has to take advantage of memory to know what we mean by this and it needs to search through business data, specifically the orders for this specific customer. And there we go, we got the answer from the agent. Hi Jordan, here's the full picture of what's going on. And take a

**[0:08:20]** look at this, for the CLI tool I built here, I'm also listing out all the individual tools that the agent called in order to leverage the memory and the context layer for it. So everything going into Redis under the hood. So first, it searched through memories to find my preferences for order handling

**[0:08:35]** and then it got information on the customer and then also found the orders and used that to get the shipment. So we can watch the agent go through the different relationships that we have in Redis, which by the way, without context retriever, it'd be very hard for the

**[0:08:48]** agent to do this because there's no schema. Everything is just key-value pairs. And so that's one of the big things that context retriever does on top of Redis is it provides that structure. It's kind of like the metadata in a Karpathy LLM wiki. We're telling the agent the different ways

**[0:09:04]** that it can search and filter so it can access things more efficiently. And so we have information on the delayed orders and then you can see right here that your customer notes say you prefer reshipments over refunds. And so that specifically is a memory that it extracted in a prior interaction with

**[0:09:20]** this fictitious Jordan Rivera. So very, very powerful. It's really cool to see how quickly he was able to capture all of this information. Like a lot of context it had to load in order to give us this complete answer and it did it without having to spend tens of

**[0:09:35]** thousands of tokens. In fact, I don't even think it spent a thousand tokens to get this information. So, in order to break down all of this for you nice and simple, of course, like usual, I have an Excalidraw diagram. So, we'll use this to talk about the business data and the

**[0:09:49]** context retriever right now, and then we'll get into the agent memory in a little bit. But, I want to show you everything that happens under the hood just to get that one response that we saw in our CLI. And so, again, the context retriever is for the business

**[0:10:02]** data, things like the customers or orders. And so, the way that it works, when we start with our Redis database, everything is unstructured. The agent doesn't have a way to really know, what is the information that I can even search through, much less how do I search through it efficiently. And so,

**[0:10:17]** context retriever is helping us do both of those things. And so, when we set up a retriever service, it is going to essentially help us document and establish the structure for our agent. And it even takes it as far as creating an MCP server. I'll show you this in the

**[0:10:34]** Redis dashboard in a little bit, but it auto generates the tools. So, it builds the intelligence of our data, and then formulates that into these are the tools to filter through things and to search by text, all the operations that our agent needs to search through our database at scale. It does not matter

**[0:10:51]** how many records we have in our Redis database, it's going to be able to sift through everything cuz the tools allow it to search by user, filter by the status of an order, whatever it might need to do. And so, now going into the Redis dashboard, we have the context

**[0:11:05]** retriever service. And so, setting up a brand new service is very, very straightforward. So, I already have mine built right here for North Peak Support. So, this is my context retriever service. And you can see that it exposes an MCP endpoint. More on that in a second. But, when you first set it up,

**[0:11:23]** you have to define your entities. And this is really cool because this is another tie-back to the Karpathy LLM wiki. We provide structure to the agent by telling it the different core entities that it's going to be operating on when it is sifting through our data. And this maps pretty much one-to-one to

**[0:11:41]** the different tables that we have in our underlying Redis database. And so, going back here to the retriever, we have the customer entity, we have the product entity, but you can see we're starting to specify a schema here. We're building the structure as the context layer on top of the database, like the different

**[0:11:58]** types that we have, how things are related, so it can go through that kind of like you would do in a knowledge graph in a personal agent. There are a lot of ties that we can make here. And so, now that we have the entities defined, this is the intelligence part

**[0:12:12]** that I was talking about. After you work through the setup process to create those entities, it is automatically going to generate all of the MCP tools based on the different ways you're going to have to access the data, like filtering a customer by city, filtering by email, basically just tool for each

**[0:12:28]** one of the attributes, and then for other types, like the text type, we also have a full search capability. So, being able to find keywords within the customer or the product description, that kind of thing. And this is my favorite part of the entire platform, just having these tools auto-generated.

**[0:12:44]** And I'll show you, if we go back into our CLI here, I will do {slash} tools, and we can see that these are all the tools that are automatically loaded into the MCP server attached to my Pydantic AI agent. And by the way, getting the MCP server attached very, very

**[0:12:58]** straightforward. It's just like any other MCP server. You can, of course, if you want to read the documentation right here. I'll have that linked in the description as well. I literally just gave the documentation to my Claude code and told it to connect and authenticate the context retriever MCP, and it just

**[0:13:15]** one-shot the whole thing. So, very easy to get this incorporated, giving it immediate intelligent access to all of the underlying data. And so, for example, going back to the CLI here, I can ask it, "Show me every delayed order with its product and total. So, more of a back-end analytics question. You

**[0:13:30]** wouldn't want every user to search over other users, but you can imagine this being an agent for people on your team for the e-commerce platform. And so, there we go. Here are the five delayed orders across the system, and the powerful thing here is instead of having to read an index document and then

**[0:13:45]** search through other markdown documents or figure out the schema of the database and then query that, it just had to make a single tool call, one MCP tool to filter the order by status, and that gave it all the information that it needed, and we got our final answer. And

**[0:13:59]** then, another example here, do we have any support tickets mentioning a refund? So, one where we're going to have to do a text search because we're going to have to see, does the ticket include the word refund? And there we go. Search ticket by text, a single MCP call again,

**[0:14:12]** query with refund. Here are the five support tickets mentioning a refund. Super fast, super efficient. And so, in the end, what it comes down to is no matter what your agent needs access to in the database, there's an MCP tool for that. And if you find that for some

**[0:14:25]** reason there isn't a tool available to the agent that you find it needing, then you just work with the entities and the types to make it so that tool is surfaced to the agent. And so, with that, that's really everything for the context retriever. That's the middleman to give the agent business data access.

**[0:14:40]** Now, let's talk about the agent memory, which again is both the short-term and long-term memory for all interactions with our agent. So, I'll show you in just a second what this looks like in the database, but my favorite part about this entire system is the fact that we're storing the short-term memory for

**[0:14:57]** every single conversation. But then, Redis Iris, with their agent memory, automatically is running a background process that is extracting the key information from the short-term memory to promote it to long-term memory. This is also a very common technique in personal agents and second brains. You're working with your second brain to

**[0:15:16]** do things over time like creating plans and doing research, and you're extracting key findings and things you tell it to remember into that promoted memory like that memory.md file that's always given to the agent. So, there's a very similar idea here where we're just trying to extract the golden nuggets out

**[0:15:31]** of conversations so that we can store it in Redis and then have the agent recall that later. And so, we are using vectors here. So, it's more traditional rag with semantic search. That way we're able to scale and each individual user can have millions of memories and we're still

**[0:15:47]** going to be able to pull out the most important ones for that next conversation they have. So, back in our dashboard, our agent memory works just like context retriever where we create a service. This time though, it's not an MCP server, it's just an API endpoint. So, we have the endpoint, we have the

**[0:16:02]** API key, and I just use Claude code to build the tools into my Pydantic AI agent to access and build up the memories here. And so, everything is managed in our database just like our business data. So, we have the memory folder here, all the key-value pairs for

**[0:16:16]** memory. So, we have the session memory, this is our short-term memory, and then the background process is automatically promoting the important things to write here. These are our long-term memory. So, we have the vector, this is what our agent uses to search. It's not supposed to be human readable for us, but then we

**[0:16:31]** also have the text. And so, look at this, "User prefers reshipments over refunds for delayed orders." This is the demo I showed you earlier where I had that conversation, I said that this is how I want you to handle any of the delayed orders and now it's going to

**[0:16:45]** remember that going forward. So, any conversation in the future where I say, "Help me handle my order like last time" or something like that, it's going to find this memory and use that so that the agent operates better on my behalf. And so, going back into the CLI, I'll

**[0:16:58]** just do a new session here. So, it's {slash} new session and then, "Hi, I'm Jordan and whenever an order of mine is delayed, always reship it expedited instead of refunding me." So, usually a user is not going to be this explicit in asking it to remember a fact, but this

**[0:17:11]** is just for the sake of demo. The agent Redis Iverson is still going to be able to extract key memories even if you're not being that explicit. And so, going into a brand new conversation here to prove that there's no short-term memory guiding this, we're going to ask it

**[0:17:23]** about our preferences, and it's going to quickly pull the memories and tell us everything we need to know. Like right here, summary of everything I know from our prior conversations. We have the identity, which of course could come from authentication as well, and it should in production. Past orders,

**[0:17:36]** support tickets, and preferences. You strongly prefer reshipments over refunds. That's the golden nugget right there. And the best part about all this with Redis Iris is if you don't use that as a platform, like of course the ideas still apply to whatever you might build in your own infrastructure, but you have

**[0:17:52]** to maintain the process that extract these memories. You have to build the tooling for the search. We can also delete memories here as well. The entire layer of memory management is just handled for you, but you have full control and visibility at the same time. Because everything is just in your Redis

**[0:18:07]** database. And so, there you go. That's everything you need to know on what it takes to build the architecture for production agents. And Redis Iris is a phenomenal platform. I'll link to them in the description. They just give the best idea of how you build that layer on

**[0:18:20]** top of your database to give your agent access and structure while still keeping your underlying data flexible. And remember, you don't need this for personal agents. LLM Wiki, if using Hermes or Claude code or whatever with Obsidian, like that's actually ideal to keep things simple and flexible. But as

**[0:18:37]** soon as you go into production, this is what you need. As soon as you have other people using your agent. And I'm going to keep making content on both of these lanes here. They're both super important. And so, if you appreciate this video and you're looking forward to

**[0:18:49]** more things on AI coding and building and shipping agents, I'd really appreciate a like and a subscribe. And with that, I will see you in the next video.
