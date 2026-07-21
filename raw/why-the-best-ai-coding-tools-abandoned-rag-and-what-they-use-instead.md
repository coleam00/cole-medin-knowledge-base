---
type: raw-transcript
title: "Why the Best AI Coding Tools Abandoned RAG (And What They Use Instead)"
youtube_id: 60G93MXT4DI
url: https://www.youtube.com/watch?v=60G93MXT4DI
slug: why-the-best-ai-coding-tools-abandoned-rag-and-what-they-use-instead
published: 2026-02-18
duration: "0:14:53"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Rag is dead. Or at least that's what a lot of the internet will tell you, especially on LinkedIn and X. And personally, I've been doing a lot less rag content myself. It's something I used to cover every single week. But the narrative that rag is dead and it's

**[0:00:15]** being replaced by other things. This is just simply not true. There is a little bit where this is happening with some use cases and we'll cover that, but also it's a lot more nuanced defining what exactly rag is. Now, there are some use cases, especially around coding, where

**[0:00:32]** agents have gotten so powerful with their search capabilities and context windows that we simply don't need traditional rag anymore. But even though this dominates the internet right now, especially AI coding assistance, this is still in the minority out of all agentic use cases. Rag is still critical for

**[0:00:49]** majority of applications that you build with generative AI. So, I want to cover when that is the case and when rag is dead. Now before we move on, there is a key distinction that we have to make together. When people say rag is dead, they are specifically referring to what

**[0:01:04]** I like to call traditional rag or semantic search where we have chunks from our documents and then we embed those into a vector database. This is the super classic pipeline. Now rag, it's short for retrieval augmented generation. So you can extend the definition of rag to really any kind of

**[0:01:23]** search an agent can perform because really rag is just grabbing any kind of external information pulling it into the LLM's context window so we can augment its answer so it has more to go off of. And so everything that I'll cover in this video with what coding agents have

**[0:01:39]** been shifting towards it really is rag just a different kind of rag over our classic semantic similarity search. This is what a lot of people are saying is dead and it really isn't for most use cases. So the question is rag dead? The answer for you depends entirely on your

**[0:01:57]** data. How structured is it? So code is a good example of very structured data. We'll cover this in a little bit, but like I said, for a majority of use cases, we are still dealing with very unstructured data because we just have a sea of knowledge that's stored in Google

**[0:02:13]** Drive, SharePoint, our SQL database, whatever that is, and we just want to have all that text in our vector database so we can search through it. And the important thing here is with our searching of unstructured data, unlike something like code, we have ambiguous natural language. We want to be able to

**[0:02:29]** find synonyms and find text that's similar based on conceptual meaning. These are the kinds of things that the embedding model in the vector database can help us with. It doesn't matter how powerful an agent is with searching with its own tools and with its context window. When we have massive knowledge

**[0:02:45]** bases of unstructured data, we need some way to find these synonyms and similar concepts that can be buried across thousands or even millions of documents. That is where traditional rag is still very much alive. Okay, let me give you my favorite example here. Let's say that we want to find all references to Star

**[0:03:05]** Wars spaceships in our knowledge base. Well, if I simply search Star Wars spaceships, I do some kind of regular expression or keyword search like we'll cover here, there is no way that we're going to get every reference to the X-wing or the TIE fighter or the Millennium Falcon because it is

**[0:03:22]** conceptually similar to our search of Star Wars spaceships. So there's no keyword matching there. It's unlikely the paragraph explicitly says this is a Star Wars spaceship. Maybe it's referenced higher in the document, but probably not in that paragraph that we're trying to pull in. So we're relying on the embedding model to

**[0:03:38]** capture that semantic similarity. And so I know this is just a silly and fun example, but I'm sure you can think of a million kinds of searches across your own documents where you would rely on something like this. It's only once we get to exact identifiers and syntax, we

**[0:03:56]** have organization directly through file paths. This is where we start to get into very structured data where we don't need semantic search and we can rely on these tools built into these agents, especially coding agents. That's what I want to cover with you right now. So, just for a second here, think about with

**[0:04:11]** me the environment in which a coding agent operates. The first thing is for the code in your codebase itself, everything is going to be perfectly spelled. Now, of course, you could have a typo and a function name, but that just means your code is broken. So, assuming your code is working, that

**[0:04:26]** means that everything is perfectly spelled and we have those exact identifiers and syntax. And so, regular expression searching, keyword searching, all that is going to work very well. We're not relying on ambiguous natural language or having to find things based on synonyms and conceptual meaning. And so that is why we don't rely on that

**[0:04:45]** semantic search indexing a codebase and putting it in a vector database. Also think about this. We have built-in organization because we have the file structure, the architecture of our codebase. And so the agent can use file navigation tools to go through different folders and hone in on where exactly

**[0:05:03]** it's going to be looking for that answer, like a file you want to edit or documentation you want it to read. And then the last thing with coding agents is they live in the terminal. So they have access to all these pretty powerful search tools built right into the

**[0:05:16]** operating system like Rip Grep and Glob. And so that's what all of these coding agents are relying on. Now we have some like cloud code that started with traditional rag and moved away and then others that just never implemented any kind of codebase indexing which by the way if you don't have to have an index

**[0:05:34]** for a codebase that is a beautiful thing because this retrieval pipeline is just another thing we have to maintain with the coding agent and it is a very difficult problem to keep the indexed codebase in sync with the actual changes you are making to the code because code

**[0:05:50]** changes a lot more frequently than most unstructured data that we have in a knowledge base. Most of the time when we have a vast array of documents, very few of them are changing even on a daily basis. And so it's a lot easier to keep things in sync. So I hope it's clear at

**[0:06:06]** this point that rag or I should say traditional rag is very much dead for code, but for most other use cases, it is very much alive. But don't just take my word for it. Let's get into what some of the industry leaders have been saying with these coding agents as they've been

**[0:06:21]** moving away from rag. The sponsor of today's video is Scribba, a coding education platform that works completely differently from anything else out there. So instead of just watching the video and then going to your own editor to try the concept, you can edit the instructor's code live and see your

**[0:06:38]** changes in real time. It's like pair programming with your instructor. So let me pause the video and show you this really quick. So we have our rendering in the top right. I can go to let's say header and I can change this from chef claw to chef cole and then I'll run this

**[0:06:52]** and boom take a look at that. We can play around with the ideas as we are going through the video. And this is just the best way to learn how to code which is very important to do by the way so you can build the foundation to work

**[0:07:04]** with coding agents and fix the issues that come up when they hallucinate. And Scrimbo recently launched their full stack developer path. Over a hundred hours of content for both backend and front end, including frameworks like Nex.js. And so, like I said, this is your foundation for building any

**[0:07:19]** software, even using AI coding assistance. And Scribba has a lot of free courses to get started. Plus, with the link in the description, you can get a 20% discount on their pro subscription. So, the best example of this is Claude Code. Boris Churnney, he's one of the maintainers of Claude

**[0:07:35]** Code. A lot of people take his tweets as gospel. And so when someone asked why doesn't Claude use embedding models or traditional rag, he said early versions of cloud code actually did use rag with a local vector database, but they found pretty quickly that a gentic search generally works better. A gentic search

**[0:07:52]** is what I was talking about in the Excal diagram. We're giving our agent these tools directly in the terminal to navigate through our file structure and view our code. And so this is technically still rag like I was saying, but there's nothing with a vector database. And so I'll show you this with

**[0:08:08]** a live example of cloud code. So cloud code recently implemented this search tool that hides the underlying bash calls that are made. So I'm asking it to not use a search tool and then go through my codebase to help me understand how my error responses are constructed. And so we can see here that

**[0:08:25]** it's using GP. It's using a tool called said. It's using cat to view the contents of specific files. There is a lot of work that's going on here, but there is no vector database, no traditional rag, and it gives me a fantastic overview at the end. And like

**[0:08:40]** I was saying earlier, Claude Code is far from alone. So Nick Pash is one of the original creators of Klein put out this article, why I no longer recommend rag for autonomous coding agents. And it's kind of a hot take cuz he goes so far as to say that the rag narrative is a mind

**[0:08:55]** virus. And what he means by this is there's this general idea, especially in 2023 and going into 2024, where anytime you need your agent to search something, you need traditional rag, semantic similarity search. And so people would shove it into any kind of agentic use case. It'd be completely

**[0:09:12]** overengineering. That's the mind virus that he's talking about. And so if you're building a coding agent, think twice about rag because it's a massive distraction both for your team and for the agent itself. And I've seen this firsthand because I did a lot of work with Archon last year. Rag for AI

**[0:09:29]** coding, which by the way, this is why I'm shifting the vision and working on some things for Archon under the hood. But I've seen it where the chunks that you get back from your knowledge base for your codebase, it just kind of confuses the LLM more than it helps. And

**[0:09:42]** see, you could even argue that these tools like RIP GREP are actually more of a directed and focused search and that's definitely better when working with a codebase. And Ader is another coding agent that's done something very interesting. What they've done is they've implemented a tree sitter, which

**[0:09:58]** sounds really fancy, but all that means is that they're giving an index of the codebase up front to the coding agent as a part of its system prompt essentially. And so this is taking advantage of the file structure that we have, the architecture with our code bases. And so

**[0:10:13]** we give the agent an overview immediately. Here are the files. Here are the core classes and functions. And so that way the agent has essentially an index of the codebase. Not an index in a vector database, but a simple highle overview of here are the different files you might want to hone in on based on

**[0:10:29]** what the user is asking you to do. So yeah, there are a lot of really cool strategies that these coding agents are implementing to avoid traditional rag and they're sharing that with the world like we just saw. And so that's what gives this false narrative that rag is

**[0:10:44]** dead because yes, it is for coding, but people see that and they don't understand this key distinction here. The only reason traditional rag is dead for AI coding is because of how structured our code bases are. But yeah, you can probably think of a million use cases where you have very unstructured

**[0:11:02]** data and you can't just rely on those tools that we were seeing earlier. Customer support, compliance and legal. I mean you can think of a million use cases with any kind of internal knowledge base where we have to rely on these things and we need this kind of

**[0:11:16]** pipeline for semantic search. Another thing that I mentioned very briefly earlier is that there's some overhead to creating and maintaining the retrieval pipeline. even a bit of cost for our chunking and embedding to store in our vector database. But this is honestly more of a feature than it is a cost

**[0:11:33]** itself because when we are chunking our documents, we're splitting them up into bite-sized pieces of information. So when we retrieve a chunk, we have just a little bit of information that ideally has exactly what our agent needs. And so it reduced the cost of our agentic search at scale. This is a really really

**[0:11:53]** rough estimate but it's about a hundred times cheaper for these really large knowledge bases when we are performing rag pulling in smaller chunks instead of reading entire documents a lot more of what we'll be doing if we have other versions of agentic search and so for smaller knowledge bases sometimes it can

**[0:12:10]** be hard to justify maintaining a pipeline but when we really start to scale things our traditional rag building and maintaining this pipeline becomes a necessity like right now let's just go Back to the clawed code example really quickly. If I were to run all these GP and said and cat commands,

**[0:12:28]** searching through a massive knowledge base of unstructured text, this would be so insanely slow and expensive. Even just this searching right here was pretty slow for me, which is good because we're giving the agent a lot of flexibility for how it finds the answer for us. But it's just not realistic to

**[0:12:44]** apply this to a very large knowledge base. we need more of a directed let's just pull some chunks here and this should have the information that we're looking for which obviously that's a bit idealistic but there are a lot of rag strategies that I've covered on my channel before I want to cover more like

**[0:12:59]** hierarchical rag to actually make rag really accurate so we can rely on just a little bit of information we pull through a few chunks to have what our agent needs instead of going through this massive process like we saw with cloud code and this is really starting to get at the last thing that I want to

**[0:13:16]** cover with you really quickly and that is the bridge because like I was saying there are pros and cons to traditional rag and other kinds of agentic search. And so for some use cases it can actually be dependent on the specific query over the knowledge base that will

**[0:13:33]** determine which strategy do we want our agent to go down because what we can do is we can give our AI agent the ability to not just figure out what to search but also how based on the specific task. And so we can go down either one of

**[0:13:47]** these routes. We give the agent tools to do both. And so this is still rag, right? This whole video, everything is still rag, but it's smarter retrieval because maybe it figures out like, okay, I can do a regular expression to find exactly what the user wants here. So

**[0:14:00]** let's go down the route of anything but traditional rag, some kind of other tool. Or maybe it's like, okay, we definitely need to match to concepts here. So let's go down the route of embedding the user query, sending it into a search in the vector database. And this, my friends, is what I've been

**[0:14:17]** doing a lot of exploration with recently. And so certainly interested in doing more content on this, bridging between both worlds because giving ultimate flexibility to AI agents so it figures out how to do the search. This is becoming more and more viable as large language models and the harnesses

**[0:14:33]** around them are getting better and better. So there you go. That is your answer to is rag dead. For coding, yes. For literally everything else, definitely not. And so if you appreciate this video and you're looking forward to more things on rag and AI coding, I would really appreciate a like and a

**[0:14:50]** subscribe.
