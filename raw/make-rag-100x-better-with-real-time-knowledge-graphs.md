---
type: raw-transcript
title: "Make RAG 100x Better with Real-Time Knowledge Graphs"
youtube_id: PxcOIINgiaA
url: https://www.youtube.com/watch?v=PxcOIINgiaA
slug: make-rag-100x-better-with-real-time-knowledge-graphs
published: 2025-05-28
duration: "0:26:41"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Retrieval augmented generation is used in most AI agents. It is the way to give your documents and data to your agent to build up a knowledge base for them. But as I always say on my channel, rag by itself without additional strategies built on top has some pretty big

**[0:00:16]** limitations. And one of those biggest ones is that rag is very static. And what I mean by that is it is your responsibility to constantly keep the agents knowledge base in sync with your data store. And that process is inefficient. and unreliable. And so that's a problem because when your

**[0:00:33]** business or platform is constantly evolving and you're working with constantly changing data like user preferences or internal metrics or market conditions, Rag just can't keep up. And so that's why I'm really excited to dive into an open- source platform with you right now called Graffiti. Graffiti is all about building temporal

**[0:00:51]** aare knowledge graphs. And it sounds fancy, but basically it's a layer on top of rag that is meant for constantly ingesting everchanging data, also keeping a historical record of how your data has changed. So your agent is aware of how the knowledge base is changing over time. It's just so powerful for

**[0:01:08]** these very dynamic environments that you want to inject your agents in. And so right now I'm going to introduce you to graffiti and how to use it. It's super easy. and I'll even compare it to other knowledge graphs like light rag and how you can use graffiti with other rag

**[0:01:22]** strategies. A lot of value packed into this video. So, let's dive right into it. So, here is the GitHub repository for graffiti which I'll link to below in the description. And man, this is one of the best written rees I've seen in a while. Gets you up and running so

**[0:01:35]** quickly and you do it completely for free. And so, we'll dive into that in a little bit, getting it set up ourselves going through their quick start. But first, I want to cover a bit more why we want to use graffiti, what it really looks like to have a temporal aare

**[0:01:48]** knowledge graph. And so, we have this fact here that Kendra loves Adidas shoes, but then she sends a message that says, "Oh, my shoes broke. Now I think Puma shoes are the best." And instead of just replacing that fact in our knowledge base, we're adding in both but then we're adding some historical

**[0:02:03]** context here, saying that she doesn't like these shoes anymore. She used to but now she likes Puma shoes. And having things like user preferences evolve over time. This is a very simple example, but it shows how powerful that is. Because a lot of times if we have something like a

**[0:02:17]** customer support agent, it needs to know their past preferences as well, not just what they currently like, because that gives that extra context to really give that personalized and above and beyond customer experience. And again, you could take this and apply it to so many other different kinds of dynamic

**[0:02:33]** environments that you have for your business or your platform. And all of this temporal aware knowledge is stored in a knowledge graph that looks like this. And so this is Neo4j. That is the engine behind the scenes powering our knowledge graph for the graffiti that we'll get into in a little bit. And so

**[0:02:49]** we have all of these pieces of information that are linked together. So we have relationships that help us understand how all the information in our knowledge base relates to each other. And also because graffiti is temporal, how it changed over time. And so like for example, we have GPT4. It

**[0:03:05]** relates to GPT3.5 in the sense that it is a previous version. And so we have this kind of metadata that helps us tie all of our information together. This is why knowledge graphs in general are just a lot more powerful than traditional rag. And they both serve their purposes. And

**[0:03:20]** so a lot of times you'll have one tool given to your agent to search a knowledge graph and then another tool for it to do a more traditional lookup in a vector database. Combining those two things together are very powerful. So I don't mean to say use knowledge

**[0:03:33]** graphs and just screw traditional rag. like you still want to have that and build on those additional strategies like hybrid rag and contextual rag things I've covered previously on my channel but yeah this is a very important component to have in most of your AI agents so that you can represent

**[0:03:48]** how knowledge is related when your agent is searching through it and there are a lot of other implementations for knowledge graphs as well one really popular one is graph rag and then there's a version of it that I covered on my channel called light rag but graffiti definitely serves different use

**[0:04:05]** cases has some pros over these other more static knowledge graphs. Now, full disclosure here before I dive into the comparison. I have actually partnered up with Graffiti to bring you this video. However, I was going to cover it anyway. A lot of you have been asking me to do

**[0:04:19]** so and these are my honest thoughts comparing Graffiti to other knowledge graph solutions that I've covered in the past like light rag because the thing is with graph rag and light rag and other similar solutions, they're meant more for static document summarization. And so when you have information like maybe

**[0:04:35]** documentation that doesn't change very often, using something like this like light rag might actually be better. Graffiti is meant more for working with dynamic data. But the thing is for most of your use cases, working with your platform or your business or just your life, like you're working with very

**[0:04:52]** dynamic data. And that's why I'm so excited about Graffiti, why I've really been looking forward to covering this for quite a while now. It's all about working with continuous incremental updates to your information, building out that historical context that we saw earlier with that example. And also Graffiti is a lot more lightweight and

**[0:05:09]** scalable. One of the things that I didn't really like about light rag was how slow it was with both building up the knowledge graph and then also for the quering itself. But graffiti is super fast for both. Typically subsecond latency, and we'll see this when we dive into the quick start. Very, very

**[0:05:26]** impressive. It also makes it a lot more scalable. So you can seriously take graffiti all the way to production environments to build the ultimate rag solution with knowledge graphs for your AI agents. So with that, let's now dive into a quick start. Let's get our hands dirty with some code here, seeing

**[0:05:42]** graffiti in action. So, I'll walk you through a simple quick start so we can understand the basics of how to build with graffiti. And then I'll also show you how to build a full knowledger graph rag AI agent with pideantic AI where we can use graffiti as the tools for our

**[0:05:56]** agent so that our agent can search our knowledge graph. Got a lot of stuff prepped here for you. And the quick start is based on what we have here in the readme. And there are only a couple of prerequisites for graffiti which is Python, Neo4j, which is our knowledge

**[0:06:10]** graph engine. And then we'll be using OpenAI for our LLMs and embedding models. But you can use a lot of other providers as well like Gemini or Anthropic. And so they have a lot of documentation that covers this. Like if we go later on in their readme, they

**[0:06:24]** show us with an example how to use graffiti with Azure OpenAI and Gemini models as well. And then if you go into their official documentation, which I'll link to this in the description, too and go to the installation tab, they have some instructions for working with different LLM providers. And this could

**[0:06:40]** be something like Olama if you want this entire implementation to be 100% local which will work because we can host Neo4j completely locally since it is an open- source knowledge graph engine. And then we can use Olama for our LLMs which is super super neat. And speaking of Neo4j, there are two primary ways

**[0:06:58]** that we can run Neo-4j on our own machine. The first way that they recommend is to use Neo4j desktops. You can just go to this link, go through the instructions to get this downloaded, set up on your computer, and then there's a few pieces of information that you have

**[0:07:12]** to save, which is going to be the URL for Neo4j, and then your username and password. We'll use those later in our environment variables. So, that's one way. The other way that actually I would recommend because I put effort into doing this for you is I took my local AI

**[0:07:26]** package which I've covered a lot on my channel before where I curated a bunch of open source solutions that you can run all together and I added in Neo4j and so you can refer to this video if you want setup instructions for the local AI package. It's a little bit

**[0:07:39]** older but everything still works except you'll just have to set a couple of extra environment variables for things like the Neo4j username and password. Very easy to get this up and running though and I can even show you that within my own Docker desktop here. I have Neo4j that is running as a part of

**[0:07:56]** my stack. So we can see it at the top right here. So this is my knowledge graph and that's what I showed you earlier when we were looking at the knowledge graph here with all of these nodes that we have all connected together. And we'll build this up in our

**[0:08:08]** quick start too. So that's getting Neo4j installed. couple of ways to do it. Very easy. And then with that, we can dive into the quick start. And so I'm going to go off this readme now because I have my own version of the quick start that I want to share with you. So let me show

**[0:08:22]** you this. So within my AI IDE, I have everything shown here that we're going to be diving into. And I'll have a link to this in the description as well. If you want to dive into this GitHub repository, take these examples that I built for you, test them out, use this

**[0:08:36]** as a starting point to use graffiti however you want to use it. And this readme has instructions to set up everything and the prerequisites are the same as the ones we saw in the graffiti readme. So follow this if you want to get everything installed and ready to go

**[0:08:49]** to follow along or just use this template for yourself. There are two things that I want to cover with you here. I want to start with a quick start where we are going to add data into our knowledge graph with graffiti and do some simple querying. And then I want to

**[0:09:02]** show you how we can build a full AI agent to leverage this knowledge base as tools for the agent so that we can run this script to evolve our knowledge base over time and then in parallel ask the same question a couple of times to our agent so we can see how our data evolves

**[0:09:18]** over time, how that also changes the answers of our agent over time. And so let's start with the quick start so we can get a sense for how graffiti really works. And so they have some boilerplate at the top here. The first thing that's important is making our connection to

**[0:09:31]** Neo4j. So we have to pull all of our environment variables for Neo4j, which you can just set in thev.example file instructions in the readme of course. And then in our main function, we make that first call to initialize graffiti with all of those Neo4j credentials. And then we build our

**[0:09:49]** indices and constraints just setting up our initial knowledge graph once we are connected to Neo4j. And then we can start adding in our episodes. So episodes are all of the pieces of information that we want to store in our knowledge graph. That's just what graffiti calls them. And the best part

**[0:10:05]** about these episodes is they don't have to follow a specific format. Like in this case, we have the content here which is just a string. And so for this example, I'm just going to be putting in a bunch of information about different LLMs like Claude and GPT. So for this

**[0:10:19]** first episode, it's just a string, a single piece of information. We do that for Claude. But then for GPT, the content is actually an object. So instead of it being a text episode type it is a JSON episode type. And so we can specify these key and value pairs. And

**[0:10:34]** so no matter how you have to represent the information that you want to store in your knowledge graph, you can do that. And there's different formats that are available to you. And this actually shows what we saw in the example earlier where that relationship between GPT4 and 3.5 was that 3.5 was the previous

**[0:10:52]** version of 4. And so when the LLM is working with our episodes and inserting those into the knowledge graph and building up those relations, it goes off of these values to do that. So we have this dynamic creation of our knowledge graph just based on how the LLM is

**[0:11:06]** understanding the data that we are giving it. That's what makes it so powerful. And we'll dive into what the knowledge graph looks like again once we run this quick start. And so after we create our episodes, we're just going to call graffiti.add episode for each one. We have some metadata as well, like the

**[0:11:21]** name of the episode and the source. And because this is a temporal knowledge graph, we need the reference time as well. That is super important because we have to know when we inserted this information. And then also if we do ever invalidate it in the future, like Kendra

**[0:11:34]** doesn't like Adidas shoes anymore, we also have to know when this data became invalid. And that happens more under the hood. And then there are a few different ways for us to search our knowledge graph. And graffiti makes it so so easy. Take a look at this. It is a single

**[0:11:48]** function call graffiti. And then we can ask a question like which AI assistant is from anthropic. And there are other parameters you can specify here like the number of nodes or facts that you get back. You can check out their documentation if you're interested in that. I'm just keeping it really simple

**[0:12:04]** here like they did in their quick start. And then for each of the results that we get back, we have a unique identifier that we have for the node. We have the fact itself. This is the actual information that we stored. And then we have valid ad. This is when we put the

**[0:12:19]** information in the knowledge graph. And then like I said earlier, if we invalidate at any point, we'll also have this information available to us. And this is so powerful to give to our AI agent so it can reason about what information is actually still relevant for answering our question. And then

**[0:12:34]** another really cool thing that you can do is you can do a center node search. And so like if you pick out a specific piece of information and you want to search more kind of around that specific node, you can do that. So like for example, we can take the top result from

**[0:12:49]** our first search and then we can do a more refined search using a center node to dictate this operation. And so it's just another parameter that we add to our graffiti search. So maybe for example we know that we're asking a question related to claude 4. So if we

**[0:13:04]** first find claude 4 in our knowledge graph then we can search around that like what is the parameter size for example. So then it wouldn't accidentally pull the parameter size for GPT or the cost for GPT like whatever we're searching we can make it more specific. So just another really good

**[0:13:19]** example to show like how powerful having these knowledge graphs are. Like not only is it easier for our agents to understand relationships between things but also we can make our searches more refined by doing something like searching on a center node and then just printing those results in pretty much

**[0:13:33]** the same way. And then another thing that Graffiti showed in their quick start that I don't want to cover too much here just to keep things brief there are different search recipes. So different ways you can explore the knowledge graph and perform these searches based on what is optimal for

**[0:13:48]** your use case. So check out their documentation and dive into this if you are interested. Just yet another way we can take this further. And so we're just doing a different kind of search type where we're looking at nodes directly instead of edges. Everything looks pretty similar except for this extra

**[0:14:03]** configuration that we build out and then printing things in pretty much the same way. And then also at the very end here this is important to prevent memory leaks. We have to close that connection in Neo4j. Uh we don't want that to persist after our script is done

**[0:14:16]** running. So that is everything for our quick start. And so what we can do and I'll go through the knowledge graph again and show these nodes in action as they're being created. But I can go ahead in my terminal here now just running python quickstart.py and then it's going to run

**[0:14:31]** a lot of things under the hood. But I'll actually show you like I'll refresh this constantly. So we can watch our knowledge graph getting built over time. So it's completely cleared right now. I cleared the demo that I showed you earlier, but I'm going to click play here. Go to graph mode. And then boom

**[0:14:46]** we have the first couple of nodes that are added to our knowledge graph for Claude. And then it's going to be doing some more processing for OpenAI, all those episodes that I showed you earlier. And if we look at the terminal here, let me actually go up. There are a

**[0:14:58]** ton of different requests that are happening to OpenAI, both with the embedding model and then the LLM itself. And the reason that there are so many requests is because we have to process those episodes and build all these relations. There's so much that is happening under the hood. And you can

**[0:15:12]** definitely use cheaper LLMs to make sure this process isn't too expensive. It's really not that bad. And so I'll run this again. And boom, there we go. We have one kind of cluster here for GPT4. And then we have another cluster for Claude. And sometimes the LLM will

**[0:15:27]** connect these together like it did in the demo I showed you earlier. There is a bit of unpredictability with knowledger because we are relying on an LLM to build up these relations when we are adding these episodes. But overall like this works really, really well. And so I can't even go back to my terminal

**[0:15:42]** here and I'll show you some of these searches that we had. So first all we had that basic search which AI assistant is from Anthropic. And then we do get the ranked results back. So this top fact actually directly answers our question. Claude is the flagship AI assistant from Anthropic. And then we

**[0:15:59]** can search based on the center node as well. So we have this re-ranking search where we're using the center node of Claude 4. And so like I was saying earlier, like maybe we want to ask the token limit for an LLM, we would want to if we're looking at Claude specifically

**[0:16:13]** use Claude as the center node. So that way we don't accidentally pull the token limit for GPT4. And so we can do that kind of as a re-ranking technique. And in this case, the question is still answered by this fact. So this one is still at the top, but you can envision

**[0:16:29]** scenarios where we don't quite get the right information, but then we can do a research with that as the center. So hopefully the adjacent nodes that we pull does have, you know, the perfect context that we need. And then we just have that other uh search as well with a

**[0:16:42]** different strategy that I don't want to cover right here. But yeah, that is everything for our quick start. So back to our readme now because I want to move on to building out a full AI agent using a lot of what we just covered, but now something that we can talk to that'll

**[0:16:56]** use the knowledge graph as a tool. And so I'll start with this script right here because this is where I'm going to be adding in more information to our knowledge graph, but I'm doing it in a special way where I do it in batches and then we can talk to our agent in between

**[0:17:08]** each batch so we can see how the information evolves over time. Also how that changes our agents answer over time. I think this is really the best way to show you the power of graffiti. And so within this script, we are connecting to Neo4j in the exact same

**[0:17:23]** way. We have this function to add episodes. All of this is going to be very similar to the quick start, but then what we're doing is we're adding information in phases. And so in phase one, we're adding in some episodes here talking about the best LLMs. And so

**[0:17:37]** we're going to talk about GPT 4.1 Gemini 2.5 Pro, and Claude 3.7 Sonnet. So all that information is added in phase 1. But then within phase 2, we're going to add in that Enthropic just released Claude 4. Now we have a new best LLM. Before it was Gemini 2.5 Pro

**[0:17:55]** but now it's Clawed 4. And so we're going to see how our knowledge graph will update as certain things become invalidated as we add newer, more relevant information. And then in our last phase, just kind of as a joke, this isn't real. I'm saying there's a new revolutionary type of AI model called

**[0:18:12]** massive language models or MLMs for short, not to be confused with multi-level marketing. So we have this brand new thing that's making LLMs completely irrelevant. We've got our first MLM which is called Nexus One. And so yeah, like now LLMs are completely obsolete. We got to focus on MLMs. And

**[0:18:30]** we'll see how our agent responds to this information being added into the knowledge graph. And so yeah, we're just connecting it to Graffiti in our main function, running each of these phases and then waiting for the user to input like, yes, it's time to move on to the

**[0:18:42]** next phase. And I'll we'll see this when I do a live demo with you. And then for our AI agent, it's just a simple agent built with Pyantic AI. And I'm not going to dive into exactly how Pantic AI works in this video. There's a lot of other

**[0:18:54]** content on my channel for Pantic AI, but we have our dependencies here where we're going to pass in the Graffiti client to our agent so it can use it in its tools. We'll set up our model based on our environment variables and then create the instance of our agent itself

**[0:19:09]** with the dependencies here that includes our graffiti client. And then within the single tool that we have for this agent just keeping it very simple, it is one to call graffiti to search our knowledge graph. And so we have the context passed in with our graffiti client and then

**[0:19:24]** also the user query that the agent decides. So it will figure out what it wants to query our knowledge graph with. And then we're going to perform that graffiti search. And then very similar to our quick start, we're going to loop over all the results and create a nicely

**[0:19:38]** structured result to return back to our agent where we have all the information like the fact itself, when it was inserted, and then also if the fact was invalidated, when that happened. And so all that context is given back to our agent to reason about the facts that it

**[0:19:52]** wants to use to answer our question. And then in the main function, we just have a connection made to graffiti with Neo4j. And then a simple command line interface to talk to our agent. And so I'll show you that right now. I have one terminal open where I'll talk to my

**[0:20:07]** agent. And then a second terminal open where I will run this LLM evolution script. And so I'll start by running agent.py. I'll just show you a very basic message to get started. I'll just say hello. Nothing really right here. And then I'll just say like what is the

**[0:20:22]** best LLM? And so in this case, it's going to call that tool to search our knowledge graph. Right now, there's not really a good answer that it has because we haven't run the other script yet. And so I'll do that now. I'll go Python LLM evolution.py. And so it's going to make

**[0:20:37]** that first set of insertions with those episodes for Claud's 3.7 Sonnet, Gemini 2.5 Pro, and then also GPT4.1. So I'll go ahead and pause and come back once that is done. All right, there we go. We have all of our facts inserted. And so I'll even go back to Neo4j. I'll run the

**[0:20:55]** query again. And then boom, we have an evolved knowledge graph with some information on Gemini 2.5 Pro Claude and GPT as well. All right, looking good. So now I'll go back over to my agent and I'll ask it the same question. What is the best LLM? And there is actually

**[0:21:11]** conversation history here. So I don't want it to just default to using the same answer as before. So I'll say search again. So now it'll perform that search and you'll see how fast this is compared to other tools like light rag. There we go. All right. The best large

**[0:21:23]** language model right now is Gemini 2.5 Pro. In just a couple of seconds, we got our answer. That's so good. All right. And so now we'll go back to my LLM evolution execution. And I can just type continue to move on to adding the next set of episodes specifically with the

**[0:21:41]** introduction of Claude 4. So again, I will pause and come back once that is all inserted into Neo4j. All right, the information is all inserted. Let's take a look at our knowledge graph again. And all right, it has grown even more. So where is Claude 4? Okay, so we got

**[0:21:55]** Claude 4 now. It is now the best LLM. And I I don't know why we have it in two cases here. So it might be because I didn't clear everything from my quick start. Maybe. Not entirely sure. So like I said, unpredictability of LLMs. These graphs aren't always going to look

**[0:22:11]** perfect, but they definitely will have the information connected in really powerful ways. And so we can even test this now. So I'll go back to my agent and I started it from scratch here. So you don't have conversation history messing with anything, I'll just ask the same question. What is the best LLM

**[0:22:26]** right now? And so now instead of saying Gemini 2.5 Pro, it should say Claude 4. There we go. Claude 4 is now the best LLM. And because we are keeping a historical record of this information and at one point Gemini 2.5 Pro was the best. It also states this. You can just

**[0:22:44]** tell from this answer how robust our knowledge base is behind the scenes when it is able to give this much information just based on a very simple query because it had all these facts returned to it. It had two different facts that one said this is the best LLM and the

**[0:22:58]** other said that Gemini 2.5 Pro was. But we look at the invalid at date. We know this is old information. So then this is our real answer, but then it still has this caveat like, man, I just I appreciate this so so much. And so then the very last test that we'll do here

**[0:23:14]** we'll do continue again to add in that whole silly concept of massive language models, MLMs. So again, I'll pause and come back once we have these episodes inserted. And there we go. We have the rest of our episodes inserted. And by the way, this only takes around 20

**[0:23:30]** seconds. So it's really fast. Even though it is building up a lot of complex relationships under the hood. I mean, just look at how big our whole knowledge graph is now. And so we can see if I go to the episode for MLM, we have mentions large language models as

**[0:23:45]** in they are no longer relevant anymore because we have MLMs. And then we talk about massive language models, what they are, how they all relate to LLMs. Yeah our knowledge graph is looking really good. And so I'll go back to the agent and I'll say, "What is the best LLM?"

**[0:24:00]** And I'll just say search again. And so couple of seconds here, we'll get our response back. All right. While Cloud 4 is currently recognized as the best LLM now there has been a recent emergence of massive language models, MLMs. And so yeah, Cloud 4 is the best, but now LLM

**[0:24:17]** just aren't the best anymore. This is just the perfect answer. I just love the caveats that we're able to get now because we have that historical information. And so I kind of just made up this example on the spot of comparing different LLMs within Graffiti here, but I think this like really really shows

**[0:24:31]** the power of having a temporal aare knowledge graph. And like basically most AI agents that you want to make with ragg could benefit from this. No matter the business that you're working in, you have dynamic data. Like something like this is just so powerful. Now, the last thing that I really want to hit on for

**[0:24:50]** you is talking about using knowledge graphs alongside more traditional rag with vector databases. You don't have to pick one over the other. That's why I cover so many different strategies with rag in general is because you can combine a lot of them together. And so I've talked about a gentic rag on my

**[0:25:08]** channel before. It's just the whole idea of giving your agent the ability to explore your knowledge in different ways. And this is an example of that. Your agent could have a tool to do a search in your knowledge graph and then also a tool to do a search in your

**[0:25:22]** vector database. It's very very powerful because sometimes information is represented better in one over the other. And so if the agent can reason like oh I didn't get what I needed when I searched the knowledge graph. Let me now look in the vector database or vice versa. Like that'll just give you better

**[0:25:37]** answers overall. And so that's why I cover so many different strategies on my channel. Why I'm introducing you to knowledge graphs right now. I think something like this really is what makes up the ideal rag solution for most of the agents that you want to create. And graffiti being one of the best for the

**[0:25:53]** knowledge graph. And I just love how this temporal aware just adds so much rich context to my agents. Like you saw in that demo, if that doesn't sell you on the idea of at least trying out graffiti, I don't know what would. It's just a fantastic platform. So there you

**[0:26:08]** have it. A clean and simple introduction to graffiti. I just love this platform and I'm definitely thinking about making more content on it in the future. So let me know in the comments if you'd be interested in that. I really think that for most AI agents, the ideal rag

**[0:26:22]** solution has a knowledge graph as one of the search capabilities and graffiti is definitely one of the top contenders for a knowledge graph tool. And so, if you appreciated this content and you're looking forward to more things raggi agents, I would really appreciate a like and a subscribe. And with that, I will

**[0:26:38]** see you in the next
