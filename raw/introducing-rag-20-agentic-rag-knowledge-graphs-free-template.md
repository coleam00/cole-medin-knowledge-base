---
type: raw-transcript
title: "Introducing RAG 2.0: Agentic RAG + Knowledge Graphs (FREE Template)"
youtube_id: p0FERNkpyHE
url: https://www.youtube.com/watch?v=p0FERNkpyHE
slug: introducing-rag-20-agentic-rag-knowledge-graphs-free-template
published: 2025-06-25
duration: "0:38:49"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Over the last couple of months, I have been diving deep into basically all of the rag strategies under the sun. I just want to find the best way possible to give my AI agents the ability to search through my knowledge. And the two strategies that I keep going back to

**[0:00:15]** time and time again are agentic rag and knowledge graphs. That's why I've been covering them so much on my channel recently. And the best part is it's actually very easy to combine the two strategies together to create some extremely powerful knowledge retrieval systems for our AI agents. And that, my

**[0:00:33]** friend, is what we're going to be diving into today. So, buckle up because I've been pouring a lot of time into building the perfect neatly packaged agent template, showing you the power of using both vector databases and knowledge graphs for rag. So, in this video, we'll see how it works. We're going to kick

**[0:00:51]** things off with a demo right away. Then we'll dive into why Agentic Dragon knowledge graphs when it applies. I'll show you how the agent works and I'll even show you how I use cloud code to help me build this template for you. So with that, let's go ahead and dive right

**[0:01:05]** into it. So to show you the power of this agentic system very quickly, I have a demonstration here in the command line. So I built this simple command line interface talking to my agent that is hosted through an API endpoint. And this agentic rag agent has access to

**[0:01:20]** both a vector database and a knowledge graph through agent tools. So it can pick and choose how it explores the knowledge that I've ingested in my knowledge base. And I can show you what this looks like actually. So first of all I'm using Postgress for my vector database taking advantage of the PG

**[0:01:37]** vector extension. And so I'm using the neon platform for Postgress. Now this is a SQL database. It's a lot more than just a vector database, but I can use my PG vector extensions. You can see that I have the embeddings here for all of my document chunks like you would see with

**[0:01:51]** very traditional rag. And just for a super simple demonstration, I have a single document in my knowledge base. Right now, it's all about AI initiatives for big tech companies like OpenAI and Microsoft. And so I have this document chunked up and embedded and stored in my knowledge base in Neon. But then I also

**[0:02:11]** have it in my knowledge graph. So I'm representing information in a different way very relationally here to give the agent the ability to explore the knowledge in a different way. That is what agentic rag is all about. And so I can zoom in on this a little bit and we

**[0:02:24]** can see a couple of examples like Amazon relates to anthropic because Amazon has invested into anthropic. If you didn't know, all of the anthropic infrastructure runs on AWS. And I can go down, we can see some other examples here, like maybe how Microsoft and OpenAI are partnered together because

**[0:02:41]** OpenAI, it solely uses Azure for hosting OpenAI models. And so we can kind of see how these companies are coupled together. So, this is a really good example of when we'd want to use both a vector database and a knowledge graph because when we're thinking about AI initiatives for big companies, we want

**[0:02:57]** to look at how companies are doing things together like Amazon and Enthropic and OpenAI and Microsoft, but then also if we want to just look up individual information on specific companies, maybe it's better to go to the vector database. And this is the kind of reasoning that we want to allow

**[0:03:13]** our agent to perform as it is answering our questions. That is all available to it now. So we can ask a question like for example what are the AI initiatives for Google and this under the hood is going to search the vector database. It doesn't need to do the knowledge graph

**[0:03:28]** in this case and we'll actually see this here. I say the specific tools that the agent used. So in this case it just did a simple vector search querying for the Google AI initiatives. And here is our answer. This is looking really nice. Then for another example here I can ask

**[0:03:43]** a different kind of question seeing how two companies relate to each other. the kind of thing that would definitely call for a query to our knowledge graph. So, for example, I could say, how are OpenAI and Microsoft related? Kind of a silly question, but I just wanted to

**[0:03:56]** explicitly call out something that would cause it to search the knowledge graph. And so, this time it'll do that. There we go. We use the graph search with the query OpenAI Microsoft relationship instead of going to our vector database. And we got a good answer talking about Azure, how it's the sole provider for

**[0:04:11]** OpenAI models, just like we saw within our graph visualization in the Neo4j dashboard. And then just for one last example here, I can ask a kind of question that I would want to use both the vector database and the knowledge graph and then just see what it comes up

**[0:04:25]** with. So I could say like what are the initiatives for Microsoft? How does that relate to anthropic? And then I can say use both search types. And so I'm just explicitly calling it out here, but what you can do is in the system prompt for your agent, and we'll dive into this in

**[0:04:44]** a little bit. That's where you can be very clear when you'd want to use the different search strategies based on the specific data that you have in your knowledge base. And so there we go. We use both the vector search and the graph search. And so first, we are looking for

**[0:04:58]** just Microsoft AI initiatives. Once we have that information, we hone in more by doing a comparison between Microsoft and Anthropic, seeing maybe how their strategies relate. I'm not totally sure exactly. It's just kind of a example that I pulled out of my butt, but yeah, I just wanted to show you how we can

**[0:05:13]** watch it use these different strategies and I set up this CLI so that we can see the different tools that it's using in real time. This is all a part of the template that I have for you. And by the way, if you are curious, the tech stack

**[0:05:25]** that I use for building this knowledger graph agentic rag agent, I have everything listed at the top of the readme. These are all libraries and tools that I absolutely adore and I cover all these on my channel quite a bit. And then also in the Dynamis community. So podantic AI for my AI

**[0:05:41]** agent framework. That's really the core of this agent is podantic AI graffiti for our knowledger graph library working alongside Neo4j which is the underlying knowledge graph engine that's the user interface that we saw earlier with all of the nodes we got Postgress with the PG vector extension to essentially turn

**[0:06:00]** a SQL database into what can act as a vector database we have fast API for building our agent API in Python and then finally the AI coding assistant that I used to help me build This entire agent is claude code which is an absolute beast of an AI coding

**[0:06:17]** assistant. And you can also see a couple of files that I have in the repo here to give you a glimpse into how I was working alongside Claude code. And towards the end of the video, I will dive more into how I use cloud code to build this. So definitely stick around

**[0:06:30]** for that as well. So we will dive into the agent template that I have for you in a little bit, how you can get it up and running yourself as well. But before we do that, I want to dive more into a gentic rag with you. Hopefully through

**[0:06:43]** that demonstration, you already have a sense for how it works and why it's so powerful. But I still want to talk about how rag has evolved to this point and also how knowledge graphs play really well into this. Here we have an article from Weevate, which I've shown on my

**[0:06:57]** channel before because I've talked about aentic rag before. I'll link to this in the description of the video. They talk about traditional rag versus a gentic rag, making a very clear comparison. And I appreciate this article a lot and there are two main diagrams that I want to cover here. So the first one is what

**[0:07:13]** is called vanilla rag. Some people call it naive rag, classic rag. There's a lot of different names for it, but essentially this is a very simple process where you take your documents, you split them into bite-sized chunks for a large language model, and then you use what is called an embedding model to

**[0:07:28]** create the vector representation of all of your information. And then you store that in a vector database. Like in our case, we're using Postgress with the PG vector extension. So we can handle vectors, but this could also be quadrant or pine cone. It could be weave. There are a lot of different options for a

**[0:07:45]** vector database. And then what happens is when a user query comes into our AI agent, we feed that through the embedding model as well. So we can do a match in our vector database. Basically just retrieving the document chunks that are the most similar to the user's question. And then we feed that in as

**[0:08:01]** additional context to our AI agent. So it becomes a part of the prompt to our large language model. So it has that additional information to answer the user's question giving that final response that is augmented by this extra context. That's why it's called retrieval augmented generation. Now this

**[0:08:19]** seems all fine and dandy, but the reason why naive rag is almost never enough is because it is extremely inflexible. Take a look at the data flow here. The user query comes in, we embed it, we get the relevant context from the vector database, and then we feed that into the

**[0:08:34]** large language bottle. And now our agent has to use that context, whether it likes it or not, to answer the user's question. And that is bad because what if the agent wants to refine its search or do a deeper dive? What if it wants to think more about how it explores the

**[0:08:49]** knowledge? If we have something like multiple knowledge sources, it doesn't have the option to do any of that. It is extremely inflexible. And so that is where a gentic rag comes in. This is the second diagram from the weave article. A gentic rag is all about giving the agent

**[0:09:05]** the ability to reason about how it explores the knowledge base instead of always force-feeding that context as kind of a pre-processing step. And so we are able to define our queries like the agent can actually think about how it would formulate a query for rag. It can explore different vector databases for

**[0:09:22]** example. We can have other tools like web search to supplement what we get from our knowledge base. There's so much flexibility here and a lot of different ways that we can define an agentic rag system like what we are doing in our case with knowledge graphs is instead of

**[0:09:36]** having two different vector databases to compartmentalize our data. We're storing the same data in a vector database and then also in a knowledge graph representing it very differently. So the agent can reason to itself like, "Oh, this is a question where I should just do a lookup in the vector database just

**[0:09:53]** to find information on a single company like Google for example, like we saw when we were doing the demo earlier. But then if we want a more relational lookup like the user is asking about Microsoft and OpenAI, well then we want to go and explore a knowledge graph. We want to

**[0:10:08]** see how our entities and relationships are set up to really get the best answer for the user." And we're able to do that with a knowledge graph and with a gentic rag. Again, just giving our agent the ability to reason about how it explores our knowledge. It is such a powerful

**[0:10:21]** thing. So, that is what we've got set up here with both our vector database and our knowledge graph. Now, we can dive into getting this template set up. I'll show you how to get everything up and running yourself. Get some documents in our knowledge graph and vector database.

**[0:10:35]** It's actually pretty straightforward. So, let's dive into that. So, here is the agentic rag with knowledger graph agent that I'm super excited to bring to you right now. Trust me, I've been pouring a lot of time into building this. So, right now, I'll get you up and running with it super easily. So, you'll

**[0:10:50]** have the exact same agent and CLI set up that you saw in the demo earlier. So, I'll have a link to this GitHub repo in the description. You can follow along with this readme there to get it set up. Otherwise, I will walk you through it right now. It's pretty easy to get

**[0:11:03]** everything up and running. And so, as far as prerequisites go, what you have to have installed already, you just need Python. You need a Postgress database like we're using Neon in this case. You'll need a Neo4j database and there are a couple of options we have for that

**[0:11:17]** I'll cover in a second. And then you will also need your LLM provider API key. This agent is set up so you can use different OpenAI API compatible providers like OpenAI Olama for local LLMs. You can have this entire thing running entirely locally and you could also use another one like Gemini. So a

**[0:11:35]** lot of different options that I have for you there. So the first thing that you want to do, and I've already got this taken care of, so I'll just call these commands really quickly, is you in a terminal want to create a virtual environment like this, and then install

**[0:11:47]** all of your dependencies with pip. Next up, we want to get everything set up in our SQL database. So it is ready to act as our vector storage. And so we will be using Postgress, which is a SQL database, using the PG vector extension. So it can act as a vector database. I

**[0:12:03]** want to make that very clear. And so the way that you can get all of the SQL to run is you just have to go into the SQL folder and then I have a single file here where you can copy everything that you need. I just have a couple of

**[0:12:15]** caveats that I mention here. It's really important. If you're using a different embedding model than the default one that I'm using, which is text embed 3 small from OpenAI, then you just have to make sure that wherever I reference the vector dimensions like 1536 right here, there are two other places. you just

**[0:12:32]** want to update that to whatever the dimensions is for your embedding model if you're using something else like Olama. And then the other quick caveat is that this is going to destroy your tables and recreate everything. And so I would recommend doing this in a new project like what I'm doing in Neon. I

**[0:12:47]** just have a new project created for this knowledge graph and a gentic rag agent. So go ahead and copy all of this SQL and then you can head on over to a Postgress database. Like in my case I am using Neon. And so you can just go to neon.te.

**[0:13:01]** They have a super generous free tier to get started with this, which is why I'd recommend using this as a Postgress platform. It's also really cool. Fun fact, one of the founders of Neon, Highkey, he's been actively contributing to Postgress because it is an open- source platform for over 20 years. So,

**[0:13:18]** they know what they're doing here with Neon. Super easy to get started. Just go ahead and create a project for free. And then you can go to the SQL editor tab and then just go ahead and paste in with controlV all the SQL that you copied from that file that we have in our IDE.

**[0:13:34]** And I'm actually going to do this with you here. So I'm going to run this and I'm going to have it recreate everything. And so I have all these warnings here, which is all good. You can ignore these. But it has dropped everything and recreated it all. So if I

**[0:13:46]** go back to my tables, I showed you earlier that I had some data, but now everything is empty because I'm going to walk you through setting up our knowledge base again. So that is everything for our SQL. Now we can move on to setting up our Neo4j. So there are

**[0:14:01]** two different ways for you to get Neo4j up and running that I would recommend. I'm not going to cover this in detail right now, especially because for option A, I already have covered this on my channel. And speaking of option A, that is using my local AI package. So I've

**[0:14:16]** curated a bunch of free-touse and open-source software together in a neat package for you to easily deploy to your local machine. And Neo4j, our knowledge graph engine, is one of those free and open-source services. And so I will link to my local AI master class right here specifically for the timestamp for

**[0:14:35]** setting up this package if you want to have Neo4j up and running through that. And then as a part of setting up your environment variables for that package, you can grab the username and password. And we'll set that up in this project in a little bit. And then the other option

**[0:14:48]** very simply is just to install Neo4j desktop following this link. It's very easy to get this up and running. And then you can get the connection details from the dashboard. So either way, you'll have Neo4j up and running. You'll get your username and password which you'll set in thev along with all of our

**[0:15:05]** other configuration. So we can dive into that now. So go ahead and make a copy of the enenv.example file and rename it to env. I'll just walk through all these values very quickly here. So the first thing is we need to set the database URL for Postgress. Now the way that you get

**[0:15:21]** this connection string is going to change depending on your platform, but most of the time they make it really easy for you. Specifically for Neon since that's what we're using right now. When you go to the dashboard tab for your project, you can just click on connect and then you can copy the

**[0:15:36]** connection string here. Just make sure that you show your password or you can manually replace the stars. But yeah, you just copy this connection string and that's going to be exactly what you paste in for your database URL. And then for Neo4j, by default, it's going to be

**[0:15:51]** this right here. So it's bolt and then localhostport 7687. And then you will have your username and password that you copied from the last step. Next, we have the configuration for our large language model. So, you want to set your provider and we can work with any provider that is OpenAI

**[0:16:08]** API compatible. So, that'll be OpenAI, Open Router, Olama, or Gemini for my favorite four options here. A lot of different ones that you can choose from. And then I have examples for what you'd have to do to set the base URL for each of these. And so, OpenAI is what I have

**[0:16:24]** by default for you. But if you want to do something entirely locally with Olama, for example, you can do that as well. And then you just have to set your API key, which for Olama, you can just type in Olama. Otherwise, you get your API key for the provider. And then you

**[0:16:38]** can pick the model that you want to use. By default, we're going to be using OpenAI with GPT4.1 Mini. And then for the embedding provider, it's the same deal. So I've actually configured this in a way where you can use a different large language model provider compared to your

**[0:16:53]** embedding provider. And the biggest reason that I did this is because if you want to use a large language model from open router for example, they don't actually offer embedding models as well. So you can set open router for your LLM, but then for your embedding you could

**[0:17:07]** use something like OpenAI or Gemini. So I'm providing utmost flexibility to you here. That is the goal. So it's the same kind of deal for the provider for embeddings base URL API key and then the embedding model that you want to use. And then the very last thing is I allow

**[0:17:22]** you to choose a different large language model for the process that is going to take our documents and we'll get into this in a little bit and transform it into the knowledge for our knowledge graph and for our vector database. And so you can often go with a much more

**[0:17:39]** lightweight model like we are using GPT 4.1 nano in this case. So that is it. And then the rest of these environment variables you can tweak if you want, but I would just recommend leaving these as the default values. This is just little configuration things for our knowledge

**[0:17:54]** graph and ingesting documents, things like that. Everything starting from ingestion lm choice and above. That's what you have to configure to get things up and running yourself. So set all of that. Make sure you're doing it in av file notv.ample. and then we can move on to the next step

**[0:18:12]** where we can actually start running things and getting our knowledge base set up with our quick start here. So, moving on to our knowledge base. Now, I don't have a super comprehensive rag pipeline or anything. This is just very basic. You want to make this documents folder, which I'm going to have this in

**[0:18:28]** the repo by default anyway. And then I have a bunch of sample documents that you can copy over or you can bring in your own markdown documents into this documents folder. Everything in here is going to be automatically ingested into both the knowledge graph and vector database when we run our ingestion

**[0:18:45]** script. If you are curious how to build a full rag pipeline in an AI agent around that where we're actually watching for files as they come in and are updated in Google Drive or local files, definitely check out the AI agent mastery course in Dynamis AI which is my

**[0:19:00]** community of other early AI adopters like yourself. I dive a lot deeper into rag, building up a full pipeline, creating a robust agent around that, even going as far as deploying it to production. So if you want to go a lot deeper, check out Dynamus. Right here though, we are starting nice and simple,

**[0:19:17]** just taking all these different markdown documents. And so everything that I have in this test folder here is just a bunch of sample documents talking about the big tech companies and their AI initiatives. So it is a use case that does work really well with both vector databases and knowledge graphs combining

**[0:19:34]** them together like we saw in the demo. So make sure that you have everything set up in your documents folder and then let me just go back to the readme here. I'll wait for a second for that to load. Scroll back down. I lost where I was cuz

**[0:19:46]** I was opening up those other markdown documents. So all right, here we are. So you got your documents folder set up. Now we can run basic ingestion. And so I'm going to go ahead and run the command python-m ingestion.est. And then I'd also recommend passing in the d-clean flag because this is going

**[0:20:05]** to wipe your knowledger graph and vector database tables um so that we can start from scratch. And so I'll go ahead and send this in. And it's going to initialize the connections to our database and then also our knowledge graph. So give it a second to do that.

**[0:20:19]** So it's initializing with graffiti. And then boom, there we go. So it created seven chunks and it inserted all those into our vector database. And then the next part is going to be working with OpenAI because we are going to be inserting things into our knowledge graph making a bunch of different

**[0:20:35]** embedding calls and chat completion calls as well. It's very computationally expensive to create our knowledge graph because we have to use large language models to define all of the entities and the relationships that we see. And so things in Neon for Postgress are really quick. Like I can go to the tables here.

**[0:20:54]** I can go into chunks. We have our seven chunks. We have our single document. And then when we go into Neo4j, if I run this query again, we have part of our knowledge graph built up now. But all of these different um episodes as they're called with graffiti, that's what we

**[0:21:09]** have with pink. And then the different entities and their relationships, all of this has to be defined by large language models. So you have to be patient when you are building up a knowledge graph. I optimized this as much as I could, but it still does take a while compared to

**[0:21:24]** just the couple of seconds that it took to insert into neon. And so that is why also I have this option here. If you want to um do no knowledge graph, you can do faster processing. Um that is an option as well. Um but yeah, I would recommend just being patient, letting

**[0:21:41]** this go for a while and then you'll have everything in your knowledge graph. Then the actual querying of the knowledge graph is very fast. It's just the inserting that takes a while. And so I'm going to go ahead and pause and come back once I have all of these graffiti

**[0:21:54]** episodes added to Neo4j. And there we go. It was only like 20 seconds later and it finished. So for this single document, it took a couple of minutes to process it. So a few seconds for the vector database and then 2 minutes for our knowledge graph. So we took this

**[0:22:08]** document right here talking about big tech AI initiatives and we now have that stored. And so now I can go back and I can re-query in Neo-4j. And then boom, we have the full knowledge graph created again like we saw at the start of this video. So we are good to go. So we have

**[0:22:24]** our knowledge ready. Now we can run our agent. So I got to do the same thing here. I'll go back to my readme, open up the preview, scroll down. Okay, so yep, we ran this step now. Um, so now the next thing that I want to mention before

**[0:22:37]** we actually run our agent API endpoint, I want to talk about configuring the agent behavior. So we want to allow the agent to reason about when it's going to use the vector database, when it's going to use the knowledge graph, when it might decide to search both as well. It

**[0:22:54]** is up to you to define this behavior. I can as much as I possibly can create a template that has a good generic prompt for the large language model, but based on your information that you're putting into your knowledge base for rag, you need to control when the agent is going

**[0:23:11]** to look in the different places. And so the way that you can do that, if you go into the agent folder, you have prompts.py. This is the primary system prompt that we are using for our agent. And everything that we include in here, these are the instructions that tell the

**[0:23:26]** agent when and how to use each of the different capabilities that we are giving it. So, we're telling it like you have the ability to search the vector database, the knowledge graph. There are a couple of other things that I don't want to dive into quite yet, but some

**[0:23:38]** other capabilities that I'm playing around with. And then towards the bottom, I tell it exactly how to use these different tools. So, for example, and this is just more of a getting started prompt. I think you could tweak this a lot. I say use the knowledge graph tool only when the user asks about

**[0:23:54]** two companies in the same question because then we want to analyze the relationship between two companies like we want to specifically pull out something like how Amazon and Anthropic are related together. Otherwise, let me scroll to the right here. Just use the vector store tool. And then I also say

**[0:24:13]** that combine both approaches only when you are asked to do so. Now, obviously that is mostly for demonstration purposes. Usually in the system prompt, you'd want to allow the agent to reason more behind the scenes. You wouldn't want the user to say like, "Please search the knowledge graph and the

**[0:24:28]** vector database." I mean, your end user probably doesn't even know that you have those two different data sources. But this is just what I have set up to make it very easy for me to demo things for you. So, make sure you tweak this system prompt to your needs based on the way

**[0:24:42]** that you want the agent to reason about how it explores your knowledge base. So change the system prompt optionally and then we can move on to starting our API server. So I'm going to go back to my terminal here. Um this is the what we just ran to create our knowledge base.

**[0:24:57]** I'll just clear everything. And then the command that I want to run is python-m agent.api. And by the way the directory that I am in is agentic rag knowledger graph. So that's what I have open in winerve here. So I'm at the root of this folder for this agentic rag agent and

**[0:25:15]** I'm running python-m agent.api and so we're first going to be connecting to our different knowledge sources again. So connecting to the database and then connecting to graffiti. You can ignore all these logs by the way. Um nothing's going wrong here. So yeah, we're connected to graffiti. The graph connection is

**[0:25:32]** successful and there we go. We are ready to start communicating with our agent. And there are two ways for us to communicate with our AI agent in the API endpoint. The first way that I'm not going to cover too much right now is we can make a direct HTTP request with a

**[0:25:48]** tool like curl to our API endpoint. So localhost port 8058. We can use the chat endpoint or if we want to see the tokens getting streamed out in real time through podantic AI, we can use /hatstream. But the better way to run our agent and what we saw in the demo is within the

**[0:26:05]** command line interface that I created. And so what you want to do is you want to have your terminal still running the agent API, but then you want to open up a second terminal. That's why I say terminal 2 in the readme here. And we want to go ahead and run Python and then

**[0:26:20]** CLI.py. You can also manually specify a portter URL if you change something in your environment variable configuration. Yeah, I'm just going to go ahead and run this and then we'll see that it connects to the API. It says that it's healthy and we are ready to go. And so now if I

**[0:26:33]** say something like hi, we can go over to our API and see that we have a request that was successful to / chat/stream. And then back over to our CLI, we've got our response. Now we can just like in the demo ask a question that it'll need to go out to our vector database for. So

**[0:26:49]** I can say something like what are the AI initiatives for Google? All right. So same kind of question that we asked before because I am using the exact same document for my demo here. There we go. Gives us a nice and solid answer and it used the vector search. And then same

**[0:27:05]** kind of deal. We can say how are Amazon and Anthropic related. Let's get a test here for the knowledge graph as well. Um so yep, they got a strategic partnership. We use the graph search. Cool. And then it decided to also use the vector search as well. Not totally

**[0:27:21]** sure why, but that's all about what we're doing here with a gentic rag is we're giving it the ability to reason about how it's going to look at the knowledge base. It's not going to be the same every single time because large language models are unpredictable. But as long as we get the right answer,

**[0:27:35]** which we did here, that is good. We allowed it to reason. It decided for whatever reason to search both our knowledge graph and our vector database. So this is looking really, really good. We are all set. So that is pretty much everything for the agent. And then the

**[0:27:50]** rest of the readme just talks about some different CLI commands that we have. Um, also just how everything works under the hood. And so you can read through the rest if you want here. I've got documentation for the API and everything, our whole structure. But um yeah, I mean we got some unit tests and

**[0:28:05]** things like that as well and a troubleshooting section. But that is pretty much it for our agentic rag with knowledger graph agent. So the last thing that I'm excited to share with you is how I use cloud code to build this pretty comprehensive agentic rag agent. Now using cloud code could definitely be

**[0:28:22]** a video entirely of its own. In fact, I'm almost certainly going to be doing that in the near future. So, let me know in the comments if you're interested in me doing a deep dive into how I use cloud code to get some insane results with AI coding. But I still want to, you

**[0:28:37]** know, at a high level here, show you how I use cloud code, especially to get started with this project because I do not condone vibe coding. I definitely encourage you to have the knowledge to validate the output from the AI coding assistant and to kind of, you know, add

**[0:28:50]** that last 10% at the end to really make everything working. But especially getting started, I use Cloud Code quite heavily for this project. And so I just want to kind of give you a sneak peek at my process here. Definitely will be diving into things more in the future.

**[0:29:04]** And so first thing, there are two MCP servers that I set up to help me build this all. The first one, and I'll just kind of show the commands really quickly that I use to add these. I have my crawl for rag MCP server. I have covered this

**[0:29:19]** a lot on my channel. I'll link to a video right here for this, but this is how I add external documentation through rag to my AI coding assistant. So, it knows how to build with things like pyantic AI. And then the other MCP server that I have here is I have Neon.

**[0:29:34]** So, Neon is the Postgress database platform that I've been using throughout this video and they have their own MCP server. And the beauty of this is that you can have the AI coding assistant create your project in Neon, run SQL queries, manage your tables, validate the output of, you know, running these

**[0:29:54]** schemas. It can do all of that automatically. So all of the database management you don't actually have to do yourself. It can do that throughout the process of creating your application, which is so important, especially because how agentic cloud code can be. It can do basically everything for you.

**[0:30:11]** It can help you plan and then it can go and start building a task list and then knocking those off one by one, setting things up in your database automatically thanks to Neon and then writing tests and iterating on those tests. It's this whole agentic process where it can

**[0:30:26]** literally run for 30 minutes to an hour just building everything for you. And so you definitely don't want to have to interject to actually set things up in the database yourself. And so you don't have to. It's so so powerful. In fact, I will tell you, we can go into Claude to

**[0:30:40]** get started here. I will tell you that when I initially built the first version of this agentic rag agent, I had Claude code running for literally 35 minutes. And the way that I was able to do it, give it that much work, is first I started in the new plan mode for Claude

**[0:30:58]** Code. And by the way, the way that you can get to that is you can just hit shift tab twice. And so let me do that right here. So shift tab. If you hit it once, that goes into auto accept mode. If you hit it again, then it goes into

**[0:31:10]** plan mode. So again, that is shift plus tab. You press that twice. The beauty of plan mode is that forces it to not write anything out to the file system yet. Because right now, what we want to do is create a comprehensive plan for the agent that we are building. And so my

**[0:31:25]** general recommendation for this is just to start spewing out a bunch of ideas for what you want to create and then ask it to ask you follow-up questions so it really starts to understand what you're looking to build and the kind of architecture that it should start putting in the planning.md and task.md

**[0:31:42]** documents. And so these are the three key documents that guide the entire AI coding process with cloud code. So let me actually go through these here. and you create the planning.md and the task.md in the planning mode in cloud code. That's why I'm covering this right now. So, first of all, we have claw.md.

**[0:32:00]** These are your global rules for your AI coding assistant. It's very similar to your cursor rules and your winds surf rules if you're familiar with using those other platforms that have been around for a lot longer. This is a markdown file that has our general instructions for our AI coding

**[0:32:15]** assistant, like telling it how to use the planning.md and task.md, telling it how to use MCP servers and how to work with unit testing. I have a video that I'll link to above right here as well showing my full process for using AI coding assistance. I cover global rules

**[0:32:31]** there and that's what this file actually came from. It's a resource that's available to you in that video. So that is claw.md. And then in planning mode, we have it create two other files. We have it create planning.md. This is the file that describes the project at a

**[0:32:46]** high level. So the architecture, the different core components that we need to build out and where they belong in our codebase. So we're actually referencing certain folder paths and things like that. We have the full technology stack, key libraries, the design principles. I mean, this gets pretty detailed here. It's pretty long

**[0:33:04]** and you just have Claude Code literally build this along with you as you're describing what you want made and as you are answering questions that it has. And then to go a bit more granular here, the other file is a list of tasks that you want Claude Code to knock off. And so

**[0:33:20]** it'll go through knock these off one by one and then it'll come in here and like add an X after it's done. And you can describe how you want it to do that again just going back to the claw.md for our global rules. And so you want to get

**[0:33:32]** a list of tasks at the end of your planning session as well because that is going to dictate the order of operations what it does as it is building out your project. And so back in the terminal here, you just want to have the conversation with claw code to generate

**[0:33:46]** all of that. Then once you have your claw.md, your planning.md, and your task.md, you can do shift tab again. I'm pressing the wrong button. Let me go back. Shift tab again. And now we are exiting out of planning mode. And now at this point, the prompt to kick

**[0:34:03]** everything off for our build is going to be pretty simple because we already did all of the leg work up front within these three files. So the AI coding assistant cloud code, it already knows what to do basically. So now I can just say um you know take a look at planning

**[0:34:23]** and task um markdown files. I don't even have to be grammatically correct here. um and execute that plan. I mean, it should already know based on my global rules to look here anyway, but like I'm just showing you like the starting prompt can be super super basic. And

**[0:34:38]** this kind of task because it has the full planning full tasks it knows everything that has to be done. Claude code will run for a very long time because it's going to do the full process here of coding and creating tests and then iterating on that using the MCP servers to do things like create

**[0:34:56]** our neon database. It's so so comprehensive and the only thing that you have to do is approve the different actions. Like boom, there we go. We are approving our first action. It's using the Neon MCP to create a new project because I explicitly told it to create a

**[0:35:11]** new project in Neon for this agent. And I'll go ahead and approve and say that for future uses of this MCP tool, you don't have to anymore. And now it's using my crawl for AI rag MCP server. And by the way, you can set these approvals up beforehand. I just want to

**[0:35:25]** show you the different actions that it's using here. So, we're getting all the available sources and then we'll probably see it look for some documentation on Pantic AI as well, maybe. I'm not totally sure the order of operations here. Um, yeah. So, it's updating the to-dos first. Okay. Yeah.

**[0:35:40]** So, the next step here is using the crawl for AI rag to get paid AI documentation. And so, we got the query here, uh, best practices and implementation patterns. And so, I'll go ahead let it do that. And so it'll search my rag knowledge base here and get some output. And so that'll aid it

**[0:35:55]** in the initial creation of the agent. And so I think that's enough my initial process for using cloud code here with my MCPS and my whole process for working with planning.md. Oh, looks like it's already running some SQL here. So I'll go ahead and improve that as well. This

**[0:36:10]** is just so neat. It created a brand new project, ran some SQL. This is just absolutely beautiful. And so what I'm going to do here is I'm just going to kind of end this demonstration. I don't think you have to see the end result for this because you already saw the end

**[0:36:25]** result of me doing this the first time when I have the full agent available for you in GitHub now. But yeah, it's just so amazing how easy it is to use cloud code to just like go through the entire process. It is absolutely powerful. Cloud code really does stand above other

**[0:36:40]** AI coding assistants right now just because of how agentic it is. the kind of thing that we're able to build in one shot is just insane now. And then the very last thing that I forgot to mention that is super important is also giving examples to Claude Code. And so yeah,

**[0:36:55]** you can see that it's gotten through a lot of the tasks since I paused the recording. So it's just chugging away building this agent. Things are looking really, really good. The other thing that I want to show you here is the examples. And so what I have done is in

**[0:37:08]** the examples folder, I've just added a bunch of different Python scripts from previous projects that I've built that I want it to reference just to take inspiration for the way that I've done certain things like set up graffiti for the knowledge graph or built my podantic AI agents to support different LLMs. I

**[0:37:25]** have all of these different examples. Some of these things that I have shared on my YouTube channel. A lot of this that is for the Dynamus community specifically. So I have all these examples that I provided and I told it within the planning to reference these as it is building the project so it

**[0:37:41]** knows best practices for things like podantic AI and graffiti. So examples is another very powerful thing and so yeah I'm not going to have the examples in source control but what I will have for you available in GitHub is the planning markdown the claw.md that I used and

**[0:37:56]** then also the task.md. So everything that I used for that initial planning and what I fed into cloud code, you can see in the GitHub repo. If you're curious, if you want to use this yourself and model some of your planning based off of this, you definitely can.

**[0:38:11]** And like I said, this was more of just a bonus end of this video. Definitely stay tuned for the full video on cloud code that I'm going to be putting out in the near future. Like I said, I definitely want to do that as well. So this is

**[0:38:24]** everything for Aentic rag and knowledge graphs and the agent that I built for you. Thank you very much to Neon for partnering with me to bring this video to you. And if you appreciated this, if you want to use this yourself, if you just got a lot out of this video, I

**[0:38:37]** would very much appreciate a like and a subscribe. And certainly stay tuned for more videos on Agentic Ragg knowledge graphs and claude code. And so with that, I will see you in the next
