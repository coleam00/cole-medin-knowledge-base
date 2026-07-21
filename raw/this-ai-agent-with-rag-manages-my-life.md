---
type: raw-transcript
title: "This AI Agent with RAG Manages MY LIFE"
youtube_id: 7dKQPbSXiB8
url: https://www.youtube.com/watch?v=7dKQPbSXiB8
slug: this-ai-agent-with-rag-manages-my-life
published: 2024-08-04
duration: "0:10:53"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** today I'm going to show you how to build an AI agent that can search through your meeting notes or summaries and create tasks for you based on the action items that come up in your meetings and all of this is going to be using a super easy to use chatbot with an interface I am

**[0:00:14]** seriously using this thing every single day now to manage my life because it saves me a ton of time most of my tasks come up in meetings and so this just keeps things really organized for me and this AI agent is actually going to be an extension of the rag implementation in

**[0:00:29]** the last AI agent Master Class video that implementation which by the way you don't have to see the video for to get a lot out of what I'm about to show you was a good implementation but it was just a start there were a couple of key flaws with it the first flaw being that

**[0:00:44]** this rag implementation it always use rag no matter what the user prompt was it would go and search through the documents because it was assuming that you were always just asking a question about the documents but in a real world scenario we want an AI agent that will

**[0:00:58]** intelligently determine if it needs to go out and search through the documents or if it can answer the user question right away and so that is what we're going to be implementing the second big problem is that that previous rag implementation it was just rag it wasn't doing anything else with other tools

**[0:01:15]** interacting with other apis like a SAA which is what we're going to be doing here to make the whole AI agent that I mentioned at the start of the video and the very last problem is that we loaded the vector database into memory and we loaded the documents into the database

**[0:01:29]** every single time we ran the chat bot which is really inefficient I'm going to show you how to make a vector database stored locally on your computer and then we don't have to load the documents into it every single time we run our script so all these things are going to come

**[0:01:42]** together for us to create a really powerful AI agent that can manage our tasks for US based on all of the action items that come up in our meetings so let's dive into this in just like five minutes and then we'll test it out so the first thing that we need to do is we

**[0:01:54]** need to create our local Vector database and load all of our documents in it and so the documents on going to be using for the vector database are in this meeting notes folder which is going to be in my GitHub repo that I linked to in the description of this video we got

**[0:02:08]** some PDF and text documents here which are just fake meeting notes that I use GPT to produce these are the same meeting notes that I had in my last AI agents Master Class video where I gave the introduction to rag which by the way if you don't understand rag at a on a

**[0:02:22]** basic level I would definitely recommend checking out that video and coming back here and continuing with this but anyway those are our meeting notes that's what we're going to be using for all the testing with rag here when we create this Vector database and load the documents then we'll run our AI agent

**[0:02:36]** which will have that available now it'll load the vector database with the documents already in it and use that to search when necessary and so with that we'll close out of this and then start implementing our script to create the vector database and load the documents so the first thing we're going to do is

**[0:02:51]** import the packages that we need which is pretty much just a bunch of things from Lang chain because Lang chain is going to help us with our embedding function it's going to help us with chroma which is our Vector data database and it's going to help us load these

**[0:03:02]** documents and split them into chunks as well and so with that we're going to also load our environment variables because the one value that we have as an environment variable for this script is the directory that we want to use to load all the documents from and so

**[0:03:15]** that's just going to default to the meeting notes directory that I just showed you with the two PDF documents and the three text documents then we're going to Define our function to load the documents so given a directory it's going to use the directory loader from Lang chain to load

**[0:03:30]** all the documents in that folder and so with this directory loader we can do PDF documents we can do text documents we can do even do other documents like HTML markdown Word documents there are also a lot of other types of document loaders in Lang chain if you want to have

**[0:03:45]** something more custom for your own types of file formats or ones that might not be supported by the directory loader so this is just the most convenient one for this use case but Lang chain provides a lot so no matter what kind of documents you want to have in your rag

**[0:03:56]** implementation you can do it with Lang chain next thing we're going to do is split these documents into chunks there are a lot of ways to chunk but as a simple one here I'm just chunking based on 1,000 characters per chunk so if a document is 3,000 characters it'll be

**[0:04:10]** split into three chunks and that way we don't have to return the entire document to the large language model when it picks out something uh from that document in the vector database when it's matching with a user search and so then with that we're just going to return the documents here and now in our

**[0:04:25]** main function we're going to get the documents by calling this function with the rag directory creating the embedding function using an open source hugging face embedding model and then we're going to instantiate chroma and save it all to the chroma DB folder and so then once you run this script this is

**[0:04:40]** literally this is the script once you run it you're going to have a chroma DB folder that has a SQL light file as well as a folder with a lot of other stuff in it and so once you run it and get this you know that you are good to go now the

**[0:04:53]** AI agent can load this chroma DB instance and not have to load the documents again because it is all stored here locally on your computer next we get to actually Implement rag into our AI agent so not only will it be able to do things in a for us it will also be

**[0:05:07]** able to search through documents for us and so I'm going to go over to this script here and we'll go ahead and Implement rag so what we have right here is the Asana agent that we've already been building as a part of the AI agents Master Class Series so I have all my

**[0:05:20]** tools here for interacting with AA doing things like creating projects and updating tasks I have the mapping of all these tools which we then bind into our chat object which is either open AI or anthropic a model from one of those two companies we stream the response handle

**[0:05:36]** any tool calls and then the main function here we have our streamlet UI defined so we can neatly interact with our chatbot to do things in a sauna for us and so now I'm going to go back up to the top and we're going to enhance this thing with rag so it can work with our

**[0:05:48]** documents just like it can work with aana and it'll intelligently decide what it needs to do with both of those and so the first thing we're going to do is import all the packages from laying chain that we need to interact with our Vector database and then we're going to create a

**[0:06:01]** function here to get our chroma instance and in this case we don't even have to do anything with a specific folder because we're just going to load that Vector database that already has the documents loaded from this other script that we made right here so you want to

**[0:06:14]** run this first and then you can run the agent So within this function here we're going to create our embedding function instance using the same model that we used when we loaded the documents and so then when we instantiate chroma we're going to point to that same place that

**[0:06:28]** we saved the chroma database that Vector database and then pass in the embedding function as well and that is literally it and now we can just get an instance and call it DB this function is so simple that is all we have to do to load in the vector database now because we

**[0:06:41]** don't have to redo things with the documents like we did in the last implementation in the previous AI agents masterclass video so next up what we're going to do is we're going to create a function which is going to be a tool to query documents so just like our ASA

**[0:06:57]** tools we're going to have a doc string here that tells the large language model how to use this function when to use it and what the arguments are and so it use this rag to query documents for information gives an example call the args is just the question and then

**[0:07:11]** returns a bunch of text that closest matches what the user asked in the latest prompt and so here we're going to do a similarity search with our chroma instance and return the top three documents that match using cosine similarity and then we're going to format these documents and return it and

**[0:07:28]** that is literally it we we have now defined a tool that gives a large language model the power to search through our meeting notes and so now we just have to add it to the mapping and boom that is it now since we have our tools created dynamically based on the

**[0:07:42]** mapping this tool is now a part of our AI agents now we can go ahead and test this thing out and see if we can get meeting notes and create tasks from the action items all right so here we are in the streamlet UI in my browser that I

**[0:07:54]** kicked off simply with the command streamlet run and then the name of my python script and so I'm going to start with a very basic question here that I know there is an answer to in one of my five documents that I have loaded in my Vector database so let's say you

**[0:08:07]** remember Emily was talking about the wellness program but you don't remember exactly what's included you could ask the llm just like I'm doing here and sure enough Emily proposed that we have yoga sessions and Mental Health Resources as a part of the wellness program and I know because I read

**[0:08:22]** through the documents that this is the correct answer which is beautiful so the rag part is working perfectly now here's the wonderful connection that we can make that makes this AI agent truly powerful we can take this answer from reg and now we can create tasks in a

**[0:08:35]** sauna based on it so I can say okay great now create a new uh project in a sauna called a wellness program and make both of these a task so it's a very complicated request and it's using some information that it retrieve from the documents for us and if we

**[0:08:56]** wanted to we could even just make it one single prompt where it's like get information from the wellness program that Emily proposed and then turn that into the tasks with this new project so it wouldn't even have to do the rag and then we tell it to make a task so that

**[0:09:08]** is how powerful it can be I just wanted to kind of play it out here in a little bit more detail and sure enough the wellness program has been created in a SAA with these two tasks so now I'm going to switch over to ASA let's see if

**[0:09:19]** this actually worked so yep sure enough we got a new project called wellness program then I click into this and yep Mental Health Resources and yoga sessions both due today that is beautiful didn't give a due date so it just chose today but that is wonderful it was so easy to not have to go into

**[0:09:36]** the documents and search and find that specific part especially if the meeting notes are long and then go over to ASA and copy those things over this saves a bit of time but that's going to add up from all the meetings and all the tasks that you have because we're all busy

**[0:09:49]** people and there's a lot on our plates so that is wonderful another really cool thing that I want to mention is even if it doesn't save you an hour every meeting because it doesn't take that long to get action items from a meeting manually it's still going to keep you

**[0:10:02]** more organized because it's going to reduce the friction it takes you to go back through meeting notes and pull out the action items lot a lot of time we'll neglect to do that just because it's annoying and so using an AI agent to do this kind of grunt work for us is a huge

**[0:10:15]** plus because the organization that provides us is going to actually save us more time in the long run keeping us efficient and dropping the ball in the least amount of things compared to the time it saves and that initial just pulling the action items from the meeting so yeah this thing is just so

**[0:10:29]** cool I'm I'm using it all the time now I hope that you could find it useful as well to help you manage your life if you did I hope that you will also stick around because I'm going to show you how to extend this into the cloud as well so

**[0:10:40]** that the documents can be in the Google Drive the vector database doesn't have to be locally we can really make this a production application so if you're looking forward to that I would really appreciate a like and a subscribe and with that I will see you in the next

**[0:10:51]** video
