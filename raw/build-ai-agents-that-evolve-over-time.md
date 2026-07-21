---
type: raw-transcript
title: "Build AI Agents that EVOLVE Over Time"
youtube_id: iOZpiXLT7iY
url: https://www.youtube.com/watch?v=iOZpiXLT7iY
slug: build-ai-agents-that-evolve-over-time
published: 2025-03-09
duration: "0:25:06"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** One of the biggest advantages to building AI agents over traditional workflows or automations is they're supposed to act more like a human. That intelligence to make decisions on the fly and do things on your behalf is why AI agents are oftenimes considered the most important use case for LLMs. But

**[0:00:19]** for being so humanlike, they sure have a terrible memory most of the time. And I have a very clean and simple solution for this that I want to bring to you today. Because here's the thing. Right now, everyone is very focused on using their documents to teach AI agents

**[0:00:34]** through RAG. And that is certainly important, but it isn't really memory. What about giving our AI agents the ability to not just learn through documents we give it, but also through our conversations? We want AI agents that learn as we interact with them, so they can remember things like our goals

**[0:00:51]** our preferences, instructions, or corrections that we give our agent, and the list goes on. this kind of long-term memories when you really start to take your AI agents to that next level of personalization and humanlike behavior. And in this video, I'll show you step by step how to build one of these

**[0:01:09]** self-learning agents using an open- source Python library called Mem Zero which is simple to use and built for exactly what we're trying to do building up knowledge, aka memories about individual users as they interact with the agent. This tool is my best friend right now. And if you stick till

**[0:01:26]** the end of this video, I think it'll be yours as well. So, let's dive into Mem Zero right now, and then I'll show you how easy it is to use to evolve your AI agents. So, first of all, what does long-term memory and Mem Zero solve for us? So, I'm going to show you really

**[0:01:42]** quick what a chat with an LLM looks like that doesn't have this implemented, and then I'll show you the end result, what we're building towards right now, what we can do with agents that have long-term memory. And so as our first test, I'm here chatting with Gemini 2.0

**[0:01:56]** Flash. This is an agent or really just a chatbot that doesn't have long-term memory. And so for my first prompt here I'm just describing to it a text stack that I'm using to build my SAS company. And so now, theoretically, the chatbot understands the different services that I'm using for things like Reddus and

**[0:02:14]** Superbase. But now, watch this. I'm going to go into a new chat. And then in this new chat, I'll ask it a question around these services that I described to it. So I'll say something like what considerations should I have for my database? And you would hope that if

**[0:02:28]** this was really an intelligent agent, it would remember my text stack between conversations. But as you can see here there is nothing that it's giving me that shows that it really understands what I'm using. It references some things like Reddus that I'm using, but also it's just listing out a bunch of

**[0:02:44]** different services like MongoDB, Oracle things that I did not mention in my text stack at all. And so you can see that Gemini doesn't have that long-term memory. And so when I start a new conversation with it, I have to fill it in on all of the important details from

**[0:02:58]** a previous conversation to get it up to speed. And that is super annoying. So now let's contrast this with an agent that has long-term memory built with mem. And so the final result, what we're working towards in this video, I have available for you to try for free right

**[0:03:13]** now. So if you go to studio.automator.ai, you'll see the Pyantic AI mem agent. This is what we're going to be building, but I want to show you how this contrasts with Gemini. And so I'll paste in the same prompt here saying that I'm working on a SAS company. Here is my tech stack. And so

**[0:03:29]** we'll see just like before it acknowledges my technologies. But then when I go into a new conversation, and I'll do that in a little bit here, it's just processing the memories right now. I'll go into a new conversation, ask Gemini the same question, and this time it'll be able to recount the technology

**[0:03:46]** that I'm using. Give me something that is a lot more tailored to me personally. So, brand new conversation here. I'll say, "What considerations should I have for my database?" And so, I'll give it a second to give me a response. Come back and you'll see that the answer is going

**[0:04:00]** to be much, much better. Boom. And there we go. Take a look at this. when considering the database for your SAS company. So first of all it remembers that I'm building a SAS company. Now it's talking about Superbase Postgress and if I do a search for Reddus here

**[0:04:16]** yep, it's talking about Reddus, my fast API. Unlike Gemini, it's not referencing technologies that I'm not using. It's only referencing the things that I am using. And this is a very basic example but I hope you can use your imagination to just run wild with what your AI

**[0:04:31]** agents are able to do when they can remember past interactions with users and start to almost build a user specific knowledge base. And that's what Mem does as well because it segregates the memories by user using a user ID. I'll show you how to use that with superbase authentication later as well.

**[0:04:49]** And getting started with Mem Zero could not be easier. They have this GitHub repo which I'll link in the description of this video and you just have to pip install Memzero AI once you have Python on your machine. It is that easy. And they have a platform to host Mem Zero

**[0:05:03]** for you. Otherwise, if you want, you can self-host this completely for free. It is a 100% open- source project. That's what we're going to be leveraging in this video. I'll start with a very basic implementation of Memzero, actually based on this template that they have right here. And then I'll get a little

**[0:05:18]** bit more complicated over time to add in really important things like superbase authentication for our user identification and also for our vector storage for our memories. So most of the time I find that to learn a new framework or tool it makes sense to just start building with it. And so that's

**[0:05:35]** what we're going to do right here with Mem Zero is dive right into the code. I do have a section at the end of this video covering a bit more how mem works behind the scenes. So check that out if you're interested. Stay till the end for that. But right now, I just want to code

**[0:05:49]** some things with you. So, this GitHub repo that you're looking at right here I'll have a link in the description to this. You can download this, follow the read me for getting everything set up. You can run all of this code that we're going to be creating together. Also

**[0:06:01]** what we're going to be doing here is going through iterations, starting really basic with me zero. We're going to code this from scratch together and then going in steps to do things like integrate Superbase for storing our memories and then also building a simple front end with superbase authentication

**[0:06:16]** so we can have users log in to grab that user ID for each user to store their memories separately in a database. I mean that's one of the biggest use cases with Memzero. So I'll show you how to do that. And then the last thing I'll say here is that the repo also showcases the

**[0:06:31]** studio integration version that I showed earlier on the live agent studio. So, if you're curious how to use Memzero to build AI agents with Pyantic AI, check out this code right here. It's a great example for that. And so, with that let's dive into building a simple implementation with Mezero. So, I'll be

**[0:06:49]** sure to go step by step through everything here to make sure it all clicks for you. So, the first thing we're going to be doing is importing our libraries and our environment variables. That's everything that we have set right here, starting with just our OpenAI API key for version one. But then for future

**[0:07:04]** versions, we'll get into defining our model through environment variables and the configuration for superbase. And so with that, we'll move on to setting up our configuration for me zero. There is a lot of different things you can define here. And you can check the docs for this like our database for example that

**[0:07:20]** we'll see later. But right here, we're keeping it very simple. Setting up the configuration for our LLM. So when the LLM is used by mem to extract memories from the messages or perform a search we are going to be using GPT4 mini just keeping it very simple then we'll create

**[0:07:37]** our openi client and our mem zero client as well using this configuration as you can see like we're doing right here and then for our primary function for this initial version we have chat with memories so it takes two parameters we have the current message from the user

**[0:07:54]** and then we have the user ID ID because we have to find a way to segregate the memories between users and the user ID is the way to do that. So we would never want to accidentally fetch a memory from a different user when someone is chatting with our agent. So first we

**[0:08:09]** retrieve the relevant memories. So using the mem zero client we're just using the search function passing in the latest message from the user their ID and then we are limiting to three three of the most relevant memories and then we create a string version of this just referencing the object that's returned

**[0:08:27]** right here. We want it to be a string because we're passing that into the system prompt. So it's just a very basic system prompt that I have set up. You are a helpful AI. Answer the questions based on the user's latest message and the memories that we are giving. right

**[0:08:40]** here dynamically from what we retrieved with mem zero. And then we create that message array that we're going to pass into the OpenAI client because this is where we make our request to GPT4 Mini with all of the messages that we currently have built up in the conversation. And this isn't a

**[0:08:58]** conversational bot. You'll see here that the messages that we pass in to GPT4 Mini, we only have the system prompt and the user message, the latest user message. We're not building up conversation history over time. And this is important because I'll show you in a bit. We're going to prove that we don't

**[0:09:17]** have any conversation history at all but the agent is still able to remember things. And so, just keep that in mind. We're not building up conversation history. So we'll get the response from the agent and then we will append to the messages the response because we're going to now take the user message along

**[0:09:36]** with the AI response and we're going to call the add function of the mem zero client. So it's going to based on the user message and AI response extract key memories for our specific user and then store that and right now it's just stored in memory and then later we'll

**[0:09:53]** hook in superbase and then we'll just return the response. That is it. It is a super simple function. And then for our main function we're just going to loop forever taking the input from the user and then if they exit we'll let them exit from the program. Otherwise, we

**[0:10:07]** will call our chat with memories function with the user input, the latest user message to get that next response and do everything with memero that we covered in this function. And we're just using the default value of default user uh for the user ID. That's why we only

**[0:10:21]** have one parameter here. But that is it. That is our version one. So now let's go ahead and test this out. So I have my Python environment already set up and my environment variable set. So now I'm just running the command Python iterations and then version one basic

**[0:10:34]** mem. And so we're in a chat interface here with GBT40 Mini. I can just say something really basic like hi. And we'll get a response. At this point nothing will be stored for our memories because there's just nothing worth saving at this point. And I'll prove to you right here that we don't have

**[0:10:49]** conversation history at all because I'll ask what did I just say? And if we were storing more than just the latest user message, then it would be able to tell us that we said hi. But right here, it isn't able to recall previous conversations or statements. And so we

**[0:11:04]** have no conversation history, but I can still have it store a memory. And so I'll say something new like, I like all kinds of cheese except goat cheese which is true, by the way. I like everything besides goat cheese, even blue cheese. I don't know what it is

**[0:11:21]** about goat cheese. But there we go. We got a response. And then behind the scenes, it called that memos add function to add that memory. And so even though we don't have conversation history at all, I can still ask it what are my food preferences and we'll get a response. It

**[0:11:36]** knows because it retrieved from the long-term memory, not the conversation history, what my preferences are as far as cheese. And it doesn't matter how many messages or conversations there are in between the statement and when it has to recall that memory. We're still going to be able to retrieve this because it's

**[0:11:53]** stored in that long-term knowledge base which right here it's just storing in memory within the script that I'm running here. But once we move on to Superbase, it'll store the embeddings for the memories in Superbase and we can see them in our database. And so let's do that right now. So, I probably could

**[0:12:11]** have included Superbase straight away in version one, but I wanted to keep that version as simple as possible. But luckily, adding Superbase in is not that difficult cuz watch, I'm going to do this in just a few lines. Watch this. Boom. That is it. We just have to change

**[0:12:25]** the configuration for our Mem Zero client. Specifying now for our vector store, instead of using the default in-memory method for storing our memories, we want to use superbase. And then for the connection string, we just have this set up as an environment variable. And so going toev.ample, I have instructions as a

**[0:12:43]** comment here for how to set this up. Also, I'll just show you right here really quick. If you go into your Superbase instance, click on connect in the top middle. Go down to transaction pooler and then view parameters. These are all your parameters. You can also just copy this connection string right

**[0:12:58]** here. It's so easy. The only thing that you have to fill in is your placeholder for your database password. So, as long as you got that, hopefully you remember that, then you're good to go. And then I also made it so you can make your model dynamic based on an environment variable

**[0:13:11]** as well. Those are the only changes. The rest of this is exactly the same as version one. And now we have Superbase set up. So, we can talk to our agent and watch our memories get stored in Superbase. And I'll show you that. It is so cool. Now, back in the terminal, we

**[0:13:25]** are running version two instead of version one. And going over to my Superbase instance, the memories table. This is where Memzero will put all of our memories is completely empty. And by the way, to get to this, you need to go to the VEX schema. It's different than

**[0:13:39]** the public schema, which you're probably used to as Superbase. So go to VEX and you'll find this table here, which Memur will create for you. So you don't even have to go and execute SQL yourself. It is very, very convenient. So let's go back over to the terminal, have a chat

**[0:13:52]** with it, and watch our memories pop up in Superbase. And so again, I'll just start off with something kind of random. I'll say uh I will shoot my foot before I code with PHP again. All right, which is kind of true by the way. Not a huge fan of PHP. I much prefer other things

**[0:14:09]** like JavaScript, Python, or Go. U but yeah, here we go. So, it created the vector for our memory. That's why we have this massive list of numbers here. Um because at first it searched and it didn't find any memories and then it made one and then it gave us a response

**[0:14:23]** at the bottom. It seems like you're really frustrated with PHP. Yes, well kind of. I mean, I haven't had to deal with it in a while, but yeah. Back over to Superbase. I'll refresh my table. And then boom, there we go. We now have our first memory. And looking at the

**[0:14:37]** metadata here, we can see what text was vectorized. User is frustrated with PHP and does not want to code with it again. Yep. And then we have the user ID, which is just default user. And we'll change this to be something more realistic once we add superbase authentication. And

**[0:14:54]** then just the created at time stamp as well. So that's metadata that we've got. And now to show you that this is really working as long-term memory, I'm going to quit my script and restart it completely. So even if there was conversation history with what I'm setting up here, we still have a fresh

**[0:15:11]** instance of the script. And so I'll ask it what are my coding preferences? And we'll see what it comes up with. So, first it searches the memories. It finds the one that we have right here. And this is going to work great even if you have a ton of

**[0:15:24]** memories. By the way, I just have one to keep everything simple here. And yeah it says based on your memories. You seem to prefer avoiding PHP for coding. I mean, yes, to say the least, that is what I said. So, that is working great. And now, the next thing that we need, we

**[0:15:38]** want something that really handles user authentication. Right now, we're just using a default value for the user ID. So now I'll show you how to set up superbase authentication use the user ID from the signedin user for the memory and we'll have a whole front end for it.

**[0:15:53]** So for version three to demonstrate superbase authentication I've created a very simple streamlit user interface. So most of the code that we see here is just boilerplate that claude 3.7 helped me create. So I'm not going to go over this from scratch like I did the other two versions but I'll go over it really

**[0:16:10]** quick in case you're curious. I mean it's pretty cool how easy it was to set this up with Streamlit. Um, so we need our Superbase URL and key to authenticate to Superbase for the Superbase authentication. It's kind of meta, but I hope that makes sense. So we just set those as the bottom two

**[0:16:25]** values in ourv file. And then we are getting our config for me and creating our mem client in the exact same way. And then for all signups and signins through Superbase, we're storing the user as a part of the user interface session state. So that way we can pull

**[0:16:43]** the user ID when we are calling into our Memzero client. So we're using that for our user ID instead of just that default user placeholder value that I was using earlier. So our chat with memories function is still effectively the same besides a couple of differences to make

**[0:16:59]** it work well with the interface. But the important thing here is the user ID is now actually going to be dynamic instead of just being hardcoded. So the way that we do that is down here in the code for the user interface, we're fetching the current user. So once they're signed in

**[0:17:15]** this user value exists. And within it we have the user ID. So we're fetching the user ID like this. This is coming from Superbase. So that then when we call chat with memories, instead of not having that value there, so it was just that placeholder default value, we're

**[0:17:30]** passing in a legitimate user ID. So now armed with this, let's try it out. I'll show you how this works. I'll use a couple of different test accounts in the user interface to show how it remembers things differently depending on which email I'm signing in with. So for

**[0:17:44]** version three, because it's a Streamlit app and not a regular Python script we're running it with the command streamllet run and then the path to version three. That'll automatically open up this page in our browser where we can now log in on the lefth hand side. So I have a couple of old emails

**[0:17:59]** that I'm using for some test accounts here. Let me go ahead and log into one of these. So I'll go ahead and log in. And then boom, we are now logged in with this account. And this is using Superbase for authentication. So there's nothing that's mocked here at all. We

**[0:18:12]** already have Superbase O set up. It's very, very easy. And it even shows us our current user ID. So we can use this to reference with the memories that are stored and make sure that it is actually storing the information for our current user. And we can clear our memories as

**[0:18:26]** well. And so let's go ahead and tell it something. I'll say that I think we have already achieved AGI and people are just hush hush about it. So I'm giving it an opinion. Obviously something that it should store as a memory for me. So let's watch it rip. Give it some time to

**[0:18:45]** store that memory. And there we go. All right. So if I go back over to Superbase now and I refresh, we have that old record from testing version two. But now we have this new record. The user believes we have already achieved AGI and people are hush- hush about it. And

**[0:18:59]** the user ID instead of being that placeholder default user like we saw with version two, we have a real user ID from Superbase now. And I can copy this and go back to the interface and search. Yep, sure enough, that maps exactly to the user ID that Streamlet says I have.

**[0:19:16]** And so now what I can do is I can log out and then I can log into another account and see that our memories will be stored separately. So I'm going to use another one of my old emails here and log in. All right, sweet. And the conversation is still here, but remember

**[0:19:35]** the agent doesn't keep track of conversation history. So I I could just refresh, but I'm just going to keep going here. I'll say I don't think we have achieved AGI at all. So I'll send in this message. And so now it'll store a memory, a complete opposite memory

**[0:19:51]** compared to the other user. I'm doing this on purpose that I don't think we've achieved AGI. And so now I'll go back to Superbase, refresh the table again, and now we have a third record. User does not think we have achieved AGI at all. And this user ID is different. It maps

**[0:20:07]** to who we are currently logged in as right now. And so now if I ask the question, uh, do you think we have achieved AGI? Maybe that's not the best way to word it because I want it to tell me what I think, but we'll see if this

**[0:20:20]** works here. I'm asking if we've achieved AGI. Based on your memory, you believe that we have not achieved AGI. But watch this. I'm going to log out and then I'm going to log back in to my first account. And this is why you'll see this is why I'm purposefully doing very opposite

**[0:20:38]** memories here because I'll just paste the exact same question. Do you think we've achieved AGI? And I'm doing this on purpose to show that because we are segregating by user ID, there is absolutely no chance that the agent will accidentally reference a memory from a different user. So we're guaranteed to

**[0:20:54]** get the right response even though this completely different information. So based on what you've shared, we you believe we have already achieved AGI and that discussions are being withheld from the public. And also I'm giving both opinions here because I don't really know which I truly believe. That's a

**[0:21:10]** whole different discussion. But yeah this is working absolutely perfect. For one account, it says one thing. For another it says the complete opposite because it's just referencing the memory based on the user data that we have, the user ID in the metadata. So this is working absolutely perfectly. And as I

**[0:21:27]** already said, a lot of this is just examples to get you started with Mem Zero. So certainly a lot that you want to do to take this further, really build it into your AI agents to take it to production. But this does lay a good foundation to get you started. So go

**[0:21:40]** ahead and take this and run with it. And Mem Zero does do a lot behind the scenes for you. So even with just a basic implementation, this is a pretty powerful version of long-term memory. And if you're curious how Memzero works behind the scenes, what kind of extra

**[0:21:57]** power it gives you, I'll cover that in a bonus segment coming up here. So check that out if you're interested. But that's everything that we've got for the code today. The core two functionalities for me zero, which you can integrate with any agent framework by the way, is

**[0:22:10]** adding memories and then searching for them. And in this diagram, they show what it looks like in a very nice way. So for adding memories, you have your messages that come in through a conversation and then you have a large language model that is prompted specifically to extract key memories

**[0:22:25]** from the conversation. So this is different from your main agent. This is a memory portion of your system. And so these new memories are added into a vector database. So you essentially have this rag setup, this knowledge base for each individual user conversing with your agent. And you can take mem even

**[0:22:42]** further as well with a graph knowledge implementation. It's a more advanced use case I won't get into in this video. Um but you can store entities and relations as well to make it even more powerful. But with rag and the vector database this is generally enough. And the

**[0:22:56]** important thing here is it's a lot more than just rag because you're segregating data by users and also mem under the hood is doing important things like conflict resolution. So when you have new memories coming in, making sure that you aren't duplicating these memories when there might be something else

**[0:23:10]** already there that is an existing similar memory. So that is everything for adding a memory. And then for searching memories, we have another nice diagram. So everything that we're looking at right here, this is executed before our primary AI agent because it's responsible for fetching the most relevant memories to supply our agent

**[0:23:29]** with that long-term memory capability. So we have an LLM that intelligently rewrites the query to extract the most relevant information from our vector database. And again, you can use mem to take things much further with knowledge graphs as well. And so whatever those relevant memories are, when it pulls

**[0:23:46]** that from the vector database, that is fed into our AI agent. And just like with adding memories, there's a lot more that Mezero does behind the scenes than you'd think as well because they implement advanced rag techniques like reranking relevant scores, including all the metadata and timestamps, really

**[0:24:02]** making sure that that long-term memory is super robust. And there are platforms out there like chat GBT that actually integrate something kind of like mem. So there are platforms that do things better than Gemini. Um but the level of customization and control that you have with Mem Zero. You can just look through

**[0:24:21]** their Python or Node SDKs. You have so much room here to really make the long-term memory fit the best to your use case with the way that you add and search memories. It is just so powerful. So I hope that this was a clear and concise guide for you on how to

**[0:24:35]** implement long-term memory for your AI agents. And the best part about all of this is Memzero is really easy to integrate no matter your use case or the framework that you are using. And I'm definitely planning on making more content on Mem in the future. Things like advanced use cases, integrating

**[0:24:52]** with different platforms and setting up the graph memory as well. So if you appreciated this content and you're looking forward to more things AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next
