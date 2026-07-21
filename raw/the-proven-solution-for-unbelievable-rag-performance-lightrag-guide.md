---
type: raw-transcript
title: "The PROVEN Solution for Unbelievable RAG Performance (LightRAG Guide)"
youtube_id: Fx3J8k--U3E
url: https://www.youtube.com/watch?v=Fx3J8k--U3E
slug: the-proven-solution-for-unbelievable-rag-performance-lightrag-guide
published: 2025-04-06
duration: "0:23:05"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** One of the questions I get asked the most is how in the world do I make my RAG AI agents more accurate? And that is what I want to cover with you in this video. It's a very important question because RAG is still the way to bring external knowledge into our agents

**[0:00:15]** making them experts on our documents and data, and it's still as relevant as ever, even as LLMs are starting to handle millions of tokens in a single prompt. And generally, RAG is pretty accurate. We ask our agent a question. It searches our documents with rag and that extra context that it fetches

**[0:00:34]** usually helps to give us a better answer. But why should we settle for just pretty accurate? Some benchmarks give basic rag 75% accuracy for pulling relevant information to answer a user's question while others site as low as 35 to 45%. If you want to build a real AI

**[0:00:52]** solution that just won't cut it. And today I'm going to show you a powerful solution to this problem because it's clear that you can't just go into a tool like N8N and Langchain, build some simple RAG AI agent and call it a day. There is definitely a lot more than what

**[0:01:08]** meets the eye that goes into building rag solutions that actually work. And I have been in the trenches the past weeks diving deep into these strategies. And as I've been drinking from the fire hose of rag strategies, enhancing rag with knowledge graphs has really stuck out to me. Specifically using a powerful

**[0:01:27]** open-source framework called light rag. Light rag not only vectorizes your documents like traditional rag. It also builds up an allimportant graph that connects topics, ideas, concepts together from your documents to take the contextual understanding of your AI agent to the next dimension. And the best part is it's pretty easy to get up

**[0:01:47]** and running. So right now, allow me to transform your rag strategy with a very simple implementation of light rag that's still pretty powerful and we'll even compare it to a basic rag setup. So we've got the code and we've got the proof. Let's dive into it. So here is

**[0:02:03]** the GitHub repository for light rag, the star of our show today. And this framework is legit. They even have a research paper attached to this repo if you really want to dive into all the technicalities behind this framework and they've got a nice diagram to go along with this in the repo as well. I don't

**[0:02:22]** want to focus on all of the technicalities today because that gets very deep but you can do that if you want. Right now I just want to focus on getting you started with light rag because that in my mind is the most practical but it is a very legit

**[0:02:35]** framework. So, I wanted to call that out quick so you know that there's a lot going on behind the scenes. But working with it is very, very easy. You just install it as a pit package and then their quick start gives us an overview of what working with light rag looks

**[0:02:48]** like. You can think of light rag as being three distinct parts. First, we set up an instance of our rag pipeline like this. And this is where we define things like the embedding model and the large language model we want to use. And you can customize all these things. And

**[0:03:02]** then the second step is inserting data into our knowledge graph and vector database. We do both at the same time with rag.insert and just passing in any string that we want from any documents that we have to parse. And this will automatically chunk things and insert things for us in an optimal way. So it

**[0:03:20]** takes care of a lot of stuff for us. And then the last part is running the actual query. It's just rag.query with our question and then our search mode. There are a lot of different ways that we can search our knowledge base with light rag. We can do a naive search that's

**[0:03:33]** just basic rag. We can do something like a hybrid search. We can even do a mix search which is really cool because this will use both vector retrieval basic rag and it'll search the knowledge graph. So we literally lose out on nothing from basic rag because we have that and more

**[0:03:50]** with light rag. That's what makes it so powerful. And there are a lot of options for customization as well. Like I mentioned you can change the LLM and embedding model that you want to use. You can use any OpenAI like API. If you want to use something like Gemini or

**[0:04:04]** Open Router, you can use Olama. They have direct support for Olama for local LLMs. And they have a lot of examples in their example folder of using these different options as well. And even including other things like AWS Bedrock or Azure OpenAI. So, they've got you covered with examples for pretty much

**[0:04:21]** anything to really help you get up and running quickly. And then as far as customizing the database that you use to store all of your knowledge base, they have a couple of options. You can use Neo4j for the knowledge graph and then also you can use Postgress. They added

**[0:04:38]** this recently. You can use Postgress for both the vector database and for the graph DB with Apache age. And then one thing that's outside of the scope of this video that I definitely want to cover later. What I've been playing with is using Neo4j for just the knowledge

**[0:04:53]** graph and then Postgress for just the vector database and combining those two together to really play into their strengths. So I've been taking this pretty far, but let's start with an overview just getting you up and running with a basic and powerful implementation of light rag. And at the bottom of the

**[0:05:08]** repo, they also show how light rag compares to what they call a naive rag. That's just basic or traditional rag. And just look at the differences in these percentages for how light rag performs on all of these data sets. And they give you instructions here for how you can run all these tests yourself if

**[0:05:26]** you want to replicate these results. And so they put a lot of effort to really give you the proof in the pudding here with light rag and how good it is. And so they compare it with a bunch of different data sets. They even compare it against graph rag. So this was a more

**[0:05:40]** complex implementation of something similar from Microsoft. Light rag is simpler, faster, and it shows to be even more powerful as well. So, it's really just seems like the optimal knowledge graph framework in my mind, which is why I'm showing it to you today. So, first thing I want to do a speedrun here

**[0:05:55]** showing you really quickly how to get up and running with light rag with the three components that we saw in the GitHub repo. Then I'll dive into building it into agents and we'll even compare it against traditional rag to see how well it does. And so first things first, we need to create the

**[0:06:11]** initialization of our rag instance just following what we saw in the GitHub repo. So we define our working directory where we'll create the knowledge graph locally and then choosing the embedding model and large language model that we want to use as well. We're just using OpenAI for both of these. Then we

**[0:06:26]** initialize our storage and the pipeline so that we can insert into our knowledge base. And that's what we do next. We just use the asynchronous insert function to insert all the information that we want into our knowledge base. And these could come from files if you want as well. You can pull in files

**[0:06:41]** locally or from the cloud, turn them into strings, and then insert them in exactly the same way. And light rag will take care of all of the chunking and optimize insertions for us. Once we have everything in our knowledge base, then we can run a query. So I can say rag dot

**[0:06:56]** and then use the asynchronous query function. I give it my question and then I'm asking it to use the mixed mode for search. So it'll use both the vector database and the knowledge graph to find my answer for me. And then finally I'll just print out the result at the end.

**[0:07:10]** And so now I can go to my terminal and I can execute this Python script. And so it's going to build up the rag pipeline insert everything into it, and then run a query based on the question that I defined at the bottom of the script. It's just that easy to set up everything

**[0:07:25]** for light rag. And obviously there's more that goes into integrating with an agent, but that's what I'm going to show you in this video. And boom, there's our answer. It says that Python is the choice for us. And yes, that's definitely right given what I inserted into the knowledge base. So, this is

**[0:07:40]** looking really good. And to expand on this more, I've got something special to show you. So, in order to show you how to use LightRag and how powerful it is I created this solution, which is a downloadable resource for you. So, you can go to the GitHub link in the

**[0:07:55]** description, take this right now, and use it for yourself to get started very quickly with Lightrag. And I'll show you in this video how I set up everything. But the structure of this project, we have two rag agents. We have one traditional rag implementation using Chroma DB for a fast and local vector

**[0:08:13]** database. And then I have a second AI agent built with light rag. Both of these are paid AI agents and I'm using the same knowledge base for each so you can test them side by side. specifically the knowledge base that I built up for each of these is I took the entire

**[0:08:31]** Pantic AI documentation. So this is my favorite Python agent framework right now. I'm just using their documentation as an example for this video. If you go to /lms.ext with their base URL ai.pyantic.dev, you'll get this massive text file. This is all the pideantic AI documentation put together in a single

**[0:08:53]** text file specifically for rag AI agents. And so I took this and I ingested this both into Chroma DB for our traditional rag agent and then also I have a knowledge graph just set up locally for light rag. And so both of these agents I have running as

**[0:09:10]** streamllet user interfaces. And so this looks the exact same but each of these is chatting with one of the AI agents specifically. And so I can ask the same question to both and we can see what kind of results we get because under the hood things are looking a lot different

**[0:09:24]** in the way that the agent is actually accessing the knowledge base. Now one of the main limitations of light rag and really rag as a whole is that it can be quite difficult to work with real time data because every time you want to update your knowledge base you have to

**[0:09:38]** reinsert documents into your vector database and recomputee your knowledge graph. It is not a fast process. So, how in the world are you supposed to build AI agents that integrate with complex and constantly evolving data like user interactions and time-sensitive metrics? The solution to this is a powerful

**[0:09:57]** open-source platform for building real time knowledge graphs called Graffiti. Graffiti is sponsoring this segment, but I specifically waited to put them in this video because it is the perfect solution for you when you need something like light rag, but for constantly changing data, and it powers the core of

**[0:10:15]** Zep's memory layer. So, it really is the real deal. So, here's the GitHub repository for graffiti. And because it's open source, you can get started with it right now completely for free to build powerful rag agents in Python. And what really makes graffiti stand out is the way that it can maintain constantly

**[0:10:32]** evolving relationships in a knowledge graph and it can maintain historical context so your AI agent can know how these relationships have changed over time. It is very unique. I will have a link to graffiti in the description. If you're looking to build AI agents that work with constantly changing

**[0:10:50]** information, then graffiti is the solution for you and I'd highly recommend checking them out. So to start out with a nice and simple test, I just want to have both agents use the Pyantic AI documentation to create me a full AI agent implementation for an agent that can search the web with Brave. It's just

**[0:11:07]** a nice and simple test that I like to run a lot when I'm trying to have an AI coding assistant build an AI agent for me. Like I do this with Archon, my AI agent builder as well. And so I'll take this request, I'll send it into the

**[0:11:19]** light rag agent and then go over to the streamllet UI and send the exact same request into the Chromma DB agent. And because Chromb only has to search the vector database and not the knowledge graph as well, it is going to give us a faster response. But yeah, I just saw

**[0:11:34]** that flash here. Take a look at this. For some reason, it decided to use the duckgo search tool provided by Pinantic AI instead of doing anything with Brave. And this is a classic hallucination where the wrong context is pulled from the documentation and that causes it to think that it has to use something

**[0:11:53]** completely different to implement the agent. So it's using a totally different search tool instead of brave probably because of what was returned from rag and I don't know that absolutely for sure but I have seen these kind of hallucinations a lot with traditional rag and so now let's go over and see

**[0:12:08]** what was produced for light rag. So let me scroll up here to see the top of the results. Yeah, this is looking a lot better. I mean, you don't have to understand Pantic AI code. This is just an example that I'm using, but I'm very familiar with the framework. And this

**[0:12:22]** looks like clean Pantic AI code, and it is using Brave for the web search tool. So, this is looking a lot better. And it doesn't fully implement the Brave search, which makes sense because the agent only has the Pyantic AI docs, not the Brave doc. So, it's just simulating

**[0:12:39]** this request, which I respect that. and it's just having a placeholder for the model here. So, it's not perfect code. Like, I couldn't just run this as is but it definitely seems like it has a better context around what I'm trying to build and tying that specifically to the

**[0:12:53]** documentation in Pantic AI for that. So this is looking good. I'd say that light rag wins. And you'll see that in general, light rag will just almost always outperform traditional rag especially as your knowledge base grows exponentially. So if you have thousands or hundreds of thousands of documents

**[0:13:11]** that's when normal rag really starts to fall apart, but light rag is going to keep up because we have so much more contextual understanding of our knowledge because we have the knowledge graph as well. So maybe I'll do some more testing later, but right now I want to show you exactly how I built this

**[0:13:27]** light rag agent so you can build them for yourself. All right, so lastly back to our GitHub repo because we now know how light rag works, why it's so powerful, and we tested it against traditional rag. And so now I want to show you how you can build your own

**[0:13:40]** light rag agent just based on all the code that I have here as a free resource for you. So you can take a look at this read me at the root of the repo and you can go through these instructions to set up everything yourself or you can just

**[0:13:53]** take this code and bring it into your own project. I don't mind. I just want you to use this however you wish. I just want to provide as much value as I can to you, but I want to really quickly cover a few of the important files for

**[0:14:04]** setting up our light rag agent. So first we have this one right here. This is our Python script that is responsible for pulling the Pyantic AI documentation and building up our light rag knowledge base. And all that's going to be stored locally in this pyantic docs folder. So

**[0:14:20]** all these JSON files represent our vector database and knowledge graph. And later I might include Neo4j or Postgress for external storage but right now I'm just keeping it very simple with a local knowledge graph. And so within this script first we're going to import all of our libraries and load our

**[0:14:38]** environment variables. And then in the main function there are just two things that I need to do. First I have to initialize the rag pipeline like we saw in the quick start example in the light rag repo. And then I want to fetch all the podantic AI documentation and just

**[0:14:53]** insert that into our knowledge base. That is all that this script has to do. It's pretty simple. And so we'll just implement these two functions right now. Starting with the function to initialize our rag pipeline. And so I just followed the documentation from light rag for this. It's all pretty boilerplate stuff.

**[0:15:10]** It's nice and simple. We first create our rag instance just based on our working directory that we'll define in a second. And then we select our embedding model and large language model. So I'm just using OpenAI for both specifically GPT4 mini for my large language model. That's what I'm using for the Chromabb

**[0:15:28]** agent as well. And then I just have to initialize the stoages and the pipeline status. And now I can return this rag instance so that we can then use it to insert all of the records. And so that's it for initializing things. Now we can build up the function to fetch the

**[0:15:42]** podantic AI documentation. So first I added in this piece to define the working directory. So that's important because that tells the script that you need to create the knowledge graph within this folder right here like we can see because I already ran this script. So we've got that defined and we

**[0:15:58]** create that folder if it doesn't exist. And then I select the URL for the Pantic AI documentation. And that's the beauty of having the LLM's.ext is this entire script only has to pull from one URL to get all of the documentation for rag. It's very very neat. And so within my

**[0:16:15]** function to fetch the padantic AI docs all I need to do is use the HTTP client to fetch this single URL and then return the text for it and then also just handle any other errors as well. And that's it. So now this call gives me all of the Pantic AI documentation as a

**[0:16:33]** single string that I can then insert into my knowledge base because lightrag takes care of the chunking and inserting and everything. And so within just 53 lines of code, we now have this script that we can run whenever we want to update our knowledge base with the latest Pantic AI docs. And then keep in

**[0:16:49]** mind once you run this script to build up your knowledge base, it's going to take a while because it has to create the vector database and knowledge graph and compute that all. And so to create all these files, you'll have to probably wait at least 20 minutes because it is

**[0:17:03]** ingesting the entire Pyantic AI documentation. But you just run this once and then you don't ever have to run it again unless you want to update your knowledge base. And so you just deal with that long run the first time and then when we run our agent going

**[0:17:17]** forward, it's going to be very fast spinning up that instance of our rag knowledge base. And so now over to our agent, I'm going to import all the libraries that we need and then define the same working directory so that we're referencing the knowledge base that we created with the other script. And then

**[0:17:33]** I want to throw an error if we don't have our OpenAI API key set. Obviously we need that for our agent. And then I'm going to initialize our rag in the same way that I did in the other script. So defining the working directory, our embedding model, and our large language

**[0:17:48]** model. And then I'll initialize the stoages. And I don't have to initialize the pipeline status this time because we only are doing that here since we're inserting into the vector database. So now I can just return rag. And then boom, we have a rag instance that we can

**[0:18:02]** then inject into our agent so it can perform rag. And so we'll define the dependencies for our agent. So this is the light rag instance that we're going to inject into our agent just using classic pantic AI dependencies. And then we'll define the agent itself, which this should look very familiar to you

**[0:18:20]** with the agent that we just created in Streamlib. We're using GPT4 mini just like we're using with light rag. We set up our dependencies and then we give it a nice system prompt as well. And then for the single tool that we're giving to our agent to keep things nice and

**[0:18:35]** simple, we're giving it the ability to based on a search query that the agent decides itself, it will call this retrieve tool to search the knowledge base. And so we give it a nice dock string. This is given as a part of the prompt to the LLM to tell it when and

**[0:18:49]** how to use this retrieve function. And it's very simple, just three lines of code. We take our light rag instance that we're putting into our agent. We're calling the asynchronous query function giving it the search query, and then also we're using the mix search mode. So it'll search both with vector retrieval

**[0:19:08]** and it'll search the knowledge graph. So we got the best of both worlds here. And then I also have this main function here if you want to run the agent as a standalone script. I'm not going to cover this though because the more important part is this streamllet

**[0:19:21]** application that I created. So we can interact with it with a UI in the browser. And Streamllet is not the focus of this video. So I'm not going to cover this in detail, but you can take a look at this if you want to see how we set up

**[0:19:33]** light rag as a dependency. We inject that into our agent when we execute it right here. And so this is where we call our agent for each message that we send into the interface and we're streaming that response out with the generator here so that we can get the result in

**[0:19:49]** typewriter style out in the UI like we saw earlier. So that is our full light rag agent. And of course, let me know in the comments if you have any questions on this, if you want me to expand it in certain ways, making it more robust adding in external storage. I definitely

**[0:20:03]** want to cover some more things in future videos for light rag cuz I definitely think that it is a big deal. And then for our basic rag implementation, I don't even really have to cover it because it's mostly the same. The one thing that's really cool to see though

**[0:20:17]** take a look at how long our script is to ingest the Pantic AI documentation compared to the one for light rag because we have to do all the chunking and inserting ourself. It's a lot more complex. And so this script is 177 lines of code. But if we go to

**[0:20:33]** the same script for light rag, it's only 53. So you might have a little bit more control if you're doing all of the chunking and inserting yourself. So there could be advantages to doing that all yourself with a vector database like chromadabb. But it is certainly nice that light rag is taking care of so much

**[0:20:51]** for us and it it's also optimizing so much behind the scenes that I don't really care that it's a definitely larger level of abstraction compared to chromabb. Usually I'm not the biggest fan of abstraction but because of how technically developed light rag is it's not a big deal to me. I I respect it.

**[0:21:12]** And so yeah, that's inserting the Pantic AI docs for Chroma DB. And then setting up the agent is almost exactly the same where we have our dependencies with everything that we need for Chroma. And then we have our single retrieve tool that will just use Chromma DB instead of

**[0:21:25]** light rag. And then the Streamlit app is the most similar out of everything because the UI is set up in exactly the same way. Even the way that we interact with the agent is set up in the same way. Nice and simple. One last final note for you is I encourage you to play

**[0:21:40]** around with these different solutions. So download this repo, run it all yourself, just hook in your OpenAI API key. That's the only thing you need and then you can try out these different setups with the exact same questions cuz it's all using the Pantic AI documentation under the hood. So you can

**[0:21:56]** play around with a bunch of different questions, see if you get different results with basic rag compared to light rag. And I will say for most of the requests, you will get pretty similar results, especially because it is a smaller knowledge base. Light rag will mostly excel once you have thousands or

**[0:22:13]** hundreds of thousands of documents. But it's still fun to play around with these different things and see the kind of responses that you get. And you can play around with different modes of search for light rag as well and do a lot of optimization with that. So, I'd be super

**[0:22:27]** curious to hear if you try this out yourself, especially if you have a larger knowledge base, if you get different results between these different solutions. So, I hope that this video has helped you level up your rag agents with light rag and knowledge graphs. And this isn't the only way to

**[0:22:42]** make rag more accurate, even though it is a gamecher. You also have agentic rag, query expansion, reranking. There's so many strategies that I want to keep diving into on my channel. So, if you appreciated this video and you're looking forward to more things AI agents and rag strategies, I would really

**[0:22:59]** appreciate a like and a subscribe. And with that, I will see you in the next
