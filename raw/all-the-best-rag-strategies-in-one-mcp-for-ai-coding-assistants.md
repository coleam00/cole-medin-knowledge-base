---
type: raw-transcript
title: "All the BEST RAG Strategies in ONE MCP for AI Coding Assistants"
youtube_id: BdZ_GOaaz7M
url: https://www.youtube.com/watch?v=BdZ_GOaaz7M
slug: all-the-best-rag-strategies-in-one-mcp-for-ai-coding-assistants
published: 2025-06-04
duration: "0:21:10"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Don't you just wish that your AI coding assistant could truly understand your project and documentation? One of the biggest problems that we have with AI coders just in general right now is they hallucinate all of the time when they're working on bringing libraries and tools into our project for things like

**[0:00:17]** Superbase or MCP or Pantic AI, whatever you are working on. And I'm building out a big solution to this problem. I've shared it a bit on my channel already but it is my crawl for AAI rag MCP server. And recently, I've added in a few new rag strategies into the mix to

**[0:00:34]** make this server even more powerful providing up-to-date documentation to your AI coders. Plus, I have some even bigger plans for this server that I want to share with you right now. Because what I want to do with this MCP server is build it into the next evolution of

**[0:00:49]** Archon. And I've shared that a bit on my channel already. But right now, we have a lot of disconnected tools to help with our AI coding. We have things like boomerang tasks in Rue Code gives us different agents to manage different parts of developing our project. We have

**[0:01:04]** context 7 for giving up-to-date documentation for our AI coders. And then we have things like cloud task manager to turn our AI coder into a project manager as well. And these are all fantastic tools, don't get me wrong. But what I want to build with this MCP server, I know that it is a big

**[0:01:21]** undertaking. I want to kind of combine all these things together into creating a master MCP server that will solve all of our needs for AI coding. Like being able to have a strong knowledge backbone with Rag. Also being able to have different agents manage different parts of our project and helping us plan

**[0:01:39]** things and manage our tasks. There is a lot that I want this to do and I'm starting here with the core of it with a rag knowledge base and that's why I've been implementing some additional strategies. So that's what I want to cover with you right now. So like usual

**[0:01:51]** I'll have a link below in the description to this MCP server. So you can run this yourself. It's completely free and open source and it's very easy to set up. So I have instructions in the readme here for how you can configure everything including how you can enable

**[0:02:06]** and disable the different rag strategies that I'll cover in a little bit. And once you go through all of this setup here, doesn't take very long, then you'll have the server up and running. So you can go ahead and connect to it within your AI coding assistant, even

**[0:02:19]** other AI agents and NADN and things like that. And so I show what that looks like, just an example for some of the configuration. It's a very typical process for setting up MCP servers. And so once you have that configured, we can now start to add documentation into our

**[0:02:34]** private knowledge base. And we'll have Superbase hooked up. That's part of the instructions as well. And so for just a demo for this video, I'm going to be using the documentation for the Versell AI SDK. This is a front-end library helping you create front-end applications around your AI agents. And

**[0:02:50]** they have an LLM.ext page. And so this is all of their documentation that they've combined into a single page in markdown format specifically to be ingested for LLMs using tools like our RAG MCP server. And a quick side note here, this MCP server supports different types of websites that it can crawl. So

**[0:03:08]** it can crawl an LLM's text like this. And there are a lot of different websites that have this available especially for library documentation. You can just give it the base page and it'll recursively scrape through all of the things in the navigation and the pages linked in there. Or you can give

**[0:03:23]** it a site map. A lot of websites have this as well. So it just lists out all the individual pages and the server will go through each of these and crawl them kind of like as if it was recursively going through the navigation. So a lot of different options there but yeah we

**[0:03:37]** can start with the llms.ext. This is the easiest way to get the knowledge for our AI coding assistance. So absolutely perfect. So what I can do is I can copy this link and then go into my windsurf and now I can say crawl and then paste in the llms.ext and because I have my

**[0:03:52]** crawl for rag mcp server connected it can now use these tools. So, it's using this one to crawl a single page. Now, in my terminal here, I have everything running right now. So, it's using OpenAI for the embeddings and the LLM, and I'm going to support other LLMs in the

**[0:04:06]** future as well, by the way. Same for embedding models. But anyway, it's going to be scraping everything and then putting that in our Superbase knowledge base, including code examples that's related to a gentic rag, which we'll see in a little bit. And so, then Windsurf tells me that it was successful in doing

**[0:04:21]** the crawling. And then if I go back into my database now and I go to my sources and I refresh. Boom. There we go. We have the AISDK.dev as our single source. Now in this knowledge base, I can go to the crawl pages table and we can see all the

**[0:04:35]** different chunks that we have inserted here. And I have a pretty robust chunking strategy already behind the scenes. I'm going to keep working on that as well. And then we have our code examples. This is something that I've added recently that I think has improved results quite a bit where aside from

**[0:04:50]** just crawling all the documentation and putting that in crawled pages. We can use a gentic rag to build up a second vector database essentially with all of the code examples. So our agent can specifically look up examples along with the documentation to really help it understand how to use the examples in

**[0:05:07]** the docs to build something similar in our own project. And so we got all of our examples here. It looks like there are 22 in total that it pulled from the Verscell AI SDK documentation. So now back within my AI IDE, now that I have the knowledge base set up for the

**[0:05:22]** Verscell AI SDK, I can ask a question like use the Versell AI SDK docs to tell me how to stream the text from an OpenAI model. So just a simple example. And of course, you could also use this within your coding process as well. I'm just showing a very simple example here. Um

**[0:05:37]** so we're going to give it a second here to do a couple of searches. So it can also go back and look and refine its search over time. And so I'm going to let it do its thing for a little bit and then we'll see it output the answer

**[0:05:47]** after it gets a couple of examples here. And there we go. So it took a little bit for it to go through some examples, but we now have the answer. So it outputed something that looks very correct to me. So we get OpenAI, we import that from the AI SDK, we get the stream text

**[0:06:01]** function, and then we get the result out like this with the text at the end. And this is looking really, really good. All right, so there we go. So we got some little bit of documentation here, just a basic example. And of course, we can take this much further and actually use

**[0:06:14]** it within our coding process. And so I have an example here where I took one of the templates from the Versel AI SDK and I used my new knowledge base to make some improvements here to make a really good-look website integrated with Cloud 4 kind of as a chat interface with this

**[0:06:30]** tool here to get weather information. And so you can see that I'm using the crawl for AI rag MCP server to crawl the docs in the middle of creating some code. And this is along with all the other things that it's doing like analyzing my pages and making changes in

**[0:06:43]** my code, all that good stuff. And then I have this front end that it created for me. And take a look at how nice this looks. It's really, really clean. And um specifically the demo that I'm going off of here, if you are curious, is I started with the uh get started with

**[0:06:57]** Claude 4 demo in the AI SDK. And then I made some changes to make it look a lot nicer. And then also I can ask it a question like what is the weather in Minneapolis, Minnesota? and it's actually going to use the weather tool and then display this really nice

**[0:07:11]** looking result here with the information that we get back from the tool call streamed out to the front end. So, a neat little app that I created and improved upon very quickly using this rag MCP server. So, just showing you how it's super simple to hook in the MCP

**[0:07:25]** server and have this really powerful rag that is meant specifically for AI coding assistance. And I've made it even more powerful recently, like I said implementing some different strategies for rag with contextual embeddings hybrid rag, agentic rag, and reranking. So, I want to cover what these look like

**[0:07:42]** right now, now that we saw a quick demo of things, and then I'll talk about some more future plans that I have for this MCP server and archon. And if you want to dive more into using these rag strategies, I have a couple of workshops that I did in my Dynamis AI mastery

**[0:07:56]** community recently. So, certainly check out dynamus.ai AI if you want to go deeper with me into things like rag strategies. I also have a full course there for building AI agents that I'm building out right now. Daily events, a big community of people that are all mastering AI together. It's definitely

**[0:08:12]** the kind of thing that you want to get in on. And you can also just check out the code for this crawl for AAI rag server if you want to look at how I implemented these strategies. But to really go through it step by step with me, I've got some awesome workshops in

**[0:08:23]** Dynamis for that. But anyway, let's get into these strategies. So starting with contextual embeddings, this is actually a rag strategy that was introduced by the anthropic team. They have this article on contextual retrieval which includes contextual embedding which I'll link to below in the description. Essentially what you do is instead of

**[0:08:41]** just embedding the raw chunks for your documentation that you're splitting up you're going to take each of the chunks when you split up your documents and you're going to run a prompt for every single chunk. And essentially that prompt is going to preface your chunk with extra context that tells the LLM

**[0:09:01]** how this chunk fits in with the rest of the document that it is a part of. And so this is kind of what your prompt looks like. You give in the whole document and then you say here's a chunk we want to situate within the whole document. Give some extra context so

**[0:09:14]** that when the LLM retrieves this chunk it has that extra information. And you can use prompt caching to make it so that it's not that expensive even though you have to put in the whole document. And luckily for us with our documentation pages, they're usually not that long. And so within the source code

**[0:09:28]** here, I just want to dive into the source code a little bit for each of these different strategies. I have this function to generate contextual embeddings. We have that exact same prompt from the anthropic article calling into OpenAI. And again, I want to support other LLMs in the future for

**[0:09:42]** this server as well. But calling into OpenAI to get that extra context and returning that. So now our chunk is going to be that extra context prependence. we have this triple dash here separating from then the actual chunk context itself. And so now when the LLM retrieves this information, it

**[0:09:58]** knows better what to do with it. And so within our database, what that looks like here for the Verscell AI SDK, if I click into the content of any one of these chunks, we have this triple dash separator just like we saw in the code where we have the actual chunk content

**[0:10:14]** but then we also have this prepended text here that just gives more information about how this chunk is useful. And especially for chunks that are more like for in the middle of a document or a page, it's really really useful. So you have more of a sense of

**[0:10:27]** what went before and after this specific piece of information that you pulled in this record. And then going back to the readme, we have hybrid search. And so hybrid search is all about being able to give your AI agent the ability to do a keyword search on top of regular rag.

**[0:10:45]** Because rag itself is semantic search. It's not doing exact keyword matching. And so sometimes that means that if you are looking for open AAI and you search for open AAI, the chunks that you get back from rag don't necessarily have the word open AAI in it, even though you

**[0:11:00]** probably want to only pull chunks that do. And keyword search is a way to get that specifically from your knowledge base. And so what that looks like in the code really quickly is if hybrid search is enabled, and again that's through these environment variables. So we can toggle contextual embedding on and off

**[0:11:14]** as well by the way. And then hybrid search right here. If it is enabled then we're going to perform this query here. Just doing a keyword search, a case insensitive keyword search in Superbase, pulling from our code examples or from the crawled pages table. We have tools now, and I'll get

**[0:11:30]** into that with agentic rag, but we have tools for both the code examples and then our regular knowledge base. And we're just doing this search, seeing if that the the content or the summary contains that keyword that we are looking for. We'll use the LLM to determine certain keywords to pick out

**[0:11:46]** of as well. And then we'll just combine that with regular rag so that we have both sets of chunks that we're returning to our LLM. And I can actually show you what that looks like here because if I go into N8N, I built a very simple AI agent that I have hooked into my crawl

**[0:12:02]** for AI rag MCP server. And so just like I connected to it in Windsurf, I'm doing it here in N8N. And again, I have instructions in the readme for how to hook into your different agents and N8N and AI coding assistants and everything but this is my SSC URL. And then I have

**[0:12:18]** the MCP server just running in a terminal um outside on my machine like we saw earlier. Um, and so now I can go into a chat and you can even see my previous conversation here where I asked it to crawl the LMS.ext text just like we did in Windsurf, but I can start a

**[0:12:32]** new conversation here and then I can ask it to use the docs to tell me what the Versell AI SDK is. So, just making sure it actually uses my server here. And it's a very basic question because I just want to start simple and show you what the input and output is for the MCP

**[0:12:47]** server. And so, let me close out and go back into it. So, we can see that we called the perform rag query tool from our MCP server with the query for the versel AI SDK. We're not filtering on any source right here because it's a very basic question. And then everything

**[0:12:59]** we get on the right hand side is going to be a combination of the chunks that we returned from the keyword search and our semantic search, the more classic rag lookup. And so there's a lot of information here because we got quite a few chunks. Um certainly not too much

**[0:13:13]** for an LLM though. But now we get go back and then here is our answer. It's the built by the Versell team built to scale applications and features. Uh elevating AI applications. Yeah, this looks really good. It's a very comprehensive answer. So there we have our hybrid search. Now the next strategy

**[0:13:30]** is a gentic rag. Now I've covered a gentic rag a good amount on my channel already. It's all about giving your AI agent the ability to explore your knowledge base in different ways. And one really common pattern for a gentic rag is to have multiple different vector databases that serve different purposes

**[0:13:48]** and then your agent has tools to access each one of them. And that is exactly what we are doing with the code examples table. So it's an entirely separate table for rag kind of like a separate vector database almost where we are specifically storing all of the code

**[0:14:03]** examples that relate to the libraries that we have crawled. And so I have crawled pages that just has all of the documentation and then honing in specifically on the examples. And I find examples so powerful. Giving those to AI coding assistants just help them so much. And so having a dedicated section

**[0:14:21]** and ability to search these specifically, I've gotten some really good results with this. And like I was hinting at earlier, we have one tool specifically to perform a rag query, not in the code examples, just in the crawled pages table. That's the one that we saw being used in N8N. But then I

**[0:14:38]** have another very similar tool, but this time to search the code examples table. So both are using rag but it's different knowledge bases that the agent can reason about which one it would want to search based on the user question or what it is trying to code. That's why

**[0:14:52]** it's a gentic rag. There's more reasoning at play here. Different ways that the agent can explore the knowledge base. And so then just to show you a very simple example back in N8N. I'm going to be very explicit here because I just want to make sure this is a solid

**[0:15:04]** demo. But also with your global rules and your system prompting and everything, you can make it know how to use these different tables really well. But I'm just telling it to search for the AI SDK code examples to find one using the OpenAI streaming output. And so I can go into here. I'll see the

**[0:15:21]** first run where we're just getting all these sources that are available. And then a second execution where we're now using the search code examples function with streaming output with OpenAI as our query. And then I have my source ID here. And now what we get back, it's going to look very similar. It's just a

**[0:15:36]** bunch of chunks, but now they're coming from the code examples tool instead of our poreform rag query tool. And so going back to the output here, we have an example. All right, take a look at this. We have our post request. We're sending in the output to OpenAI, and

**[0:15:51]** then we're returning an assistant response. I'm not entirely sure if this is correct, but the important thing here is that we are getting these examples back. Like take a look at this. We have this example directly from the AI SDK and based on kind of the code that I saw

**[0:16:05]** here, we're importing assistant response from OpenAI. It looks like it's kind of spitting that out like it's exactly what I wanted to do. It found an example and it spit that out to me. That is absolutely perfect. And so then that brings us on to our last strategy here

**[0:16:19]** which is re-ranking. Something I haven't covered on my channel yet, but this is definitely another very powerful strategy. The job of re-ranking is to take the chunks that we have returned from our vector database and order them into the ones that are actually the most relevant for the question or the thing

**[0:16:36]** that we are trying to code. It uses a separate kind of AI model. So not a large language model but a model called a cross encoder to analyze the query and the chunks that we got back and then order them based on the evaluated relevance. And so going to the code what

**[0:16:51]** that looks like here is if we are using reranking. So again, this is determined from what we have set within our environment variables. Then we're going to call this function to rerank the results. And so we're just going to call this model. This is a cross encoder model that just runs locally on your

**[0:17:08]** computer. I'll even show you that we set it up right here. So we have this cross encoder that we're just downloading from HuggingFace. So we're pulling an open source model using that to do our reranking and then we just return the sorted results based on the score. So we

**[0:17:23]** get the scores by just calling model.predict on all of these pairs that we create. So we create these pairs of the user query or in this case the AI assistant query and each chunk and then we're going to score them and then sort them. And so going back into N8N we can

**[0:17:39]** see what this output looks like. So this top item in the chunk that we returned from code examples this has the highest score. So, if I scroll down to where we see the re-rank score, and I know this is kind of really messy JSON, but this is all very easy for the AI coding

**[0:17:54]** assistant to read here. The re-rank score is a three. And then if we go all the way down to the last chunk, the re-rank score is a -10.4. So, this value doesn't mean a lot to us, but basically the smaller it is, like this is a a very

**[0:18:08]** negative number. That means it's not as relevant. That's why it's at the bottom of the list. And then this one was a three. It's the most relevant. And obviously like we saw when we compared it to the output, this is indeed the example that it decided to go with and

**[0:18:20]** share with us with our question of how do we stream output with open AAI. So re-ranking is just a powerful way also to make it so that you can return return a lot of chunks from rag like 50 different chunks and then you use re-ranking and then only return the 10

**[0:18:35]** most relevant. So it's a way to basically work with more chunks without having to feed more into your LLM and overwhelming it and making your prompt way too long. Um, so reranking is another very powerful technique and this kind of starts to get into my future plans for this rag MCP server as well

**[0:18:51]** because I want to implement even more strategies. Things like multi-query rag and query expansion, even building out a gentic rag with knowledge graphs with something like graffiti or light rag. There are so many different strategies that I can build out here to really make this the best possible rag MCP server

**[0:19:07]** you could have for AI coding assistance and a lot of things that I'm experimenting with behind the scenes right now. So, I'm taking my time with this and that's why we haven't really seen much action with Archon at this point because by the time I build this into Archon and really shift my vision

**[0:19:22]** for Archon into being the knowledge backbone for AI coding assistance, I want to really make sure that I have the optimal rag strategies for this and continuing to build Archon into like helping you manage tasks for your projects and setting up agents to manage different parts of your project to build

**[0:19:36]** out. There's so many ideas that I have for this, so many reasons to get excited for this and I'll keep this open source. I'll keep building this in public and so you can continue to follow along with me and even help me build this out if you want. Like I very much encourage that. I

**[0:19:50]** actually have someone helping me right now building out a front-end overhaul for Archon so that we can set up autocrolling so that we can keep our documentation up to date, managing our MCP server from the UI. basically turning Archon into a full application that we can then hook into our AI coding

**[0:20:06]** assistants and AI agents because it's going to be general enough where now it's going to be rag for like anything you want. And so Archon I really have this vision to have it power like a majority of the agents and AI coding assistants that people are working with.

**[0:20:20]** I think it has what it takes to get there and there's a lot of vision that I have behind this to take it that far. So that is everything that I have right now for this crawl for AI rag MCP server and my plans to eventually turn it into the

**[0:20:32]** next evolution of Archon. And I want to emphasize again that this is and will continue to be a completely open- source project. So you can get involved in so many different ways. You can help me out with changes making PRs in GitHub. You can give suggestions to me here in the

**[0:20:47]** comments below or in the GitHub repository. just any way that you want to get involved, I would absolutely love it because this is a big undertaking and so I definitely need your help. So, if you appreciated this content and you're looking forward to more things around this MCP server or AI agents in general

**[0:21:03]** I'd really appreciate a like and a subscribe. And with that, I will see you in the next
