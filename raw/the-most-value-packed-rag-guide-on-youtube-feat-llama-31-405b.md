---
type: raw-transcript
title: "The Most Value Packed RAG Guide on YouTube (Feat. Llama 3.1 405B!)"
youtube_id: BrUW8_cCTew
url: https://www.youtube.com/watch?v=BrUW8_cCTew
slug: the-most-value-packed-rag-guide-on-youtube-feat-llama-31-405b
published: 2024-07-28
duration: "0:11:33"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** welcome to the most concise rag tutorial on all of YouTube rag stands for retrieval augmented generation is one of the most powerful parts of AI agents because it's how you bring external knowledge into a large language model so it's able to answer user questions with more information than just what it was

**[0:00:16]** trained on we're going to do a deep dive into how rag works and then I'm going to show you guys how to build a super powerful chatbot in just a few minutes so we can chat with our local documents using the new llama 3.1 405 billion parameter model which is super great and

**[0:00:31]** easy to work with so let's go ahead and get started so let's start with a very basic definition of rag in its Essence retrieval augmented generation involves a user sending a question to a large language model but instead of the llm handling that question right away it's first directed to a database of

**[0:00:48]** knowledge where complicated Vector mathematics is used to match that user question with the most relevant knowledge in the database and then that knowledge is sent to the large language model so it has an extra context to answer that question that it wouldn't be able to with adjust the information that

**[0:01:05]** was used to train the model and so one really good example here is this database of knowledge could be a bunch of meeting summaries and so the user could ask something like what are the action items from the meeting on the 20th and that information will be given

**[0:01:18]** to the llm so it could formulate a nice response something concise to answer the user's question about that meeting so with that super simple definition of rag let's dive into how we actually bring these documents into our knowledge database so for every document that we want to be a part of the knowledge that

**[0:01:34]** we can give to an llm we're going to split them into chunks and the reason we do that is when we have a user question that we map to knowledge we're going to return all that knowledge to the llm as context and we don't want it to be the

**[0:01:46]** entire document so we're going to split up every document into nice and concise chunks of a 100 characters a thousand characters you can play around with this and turn each one of these into vectors that we then store as embeddings in our Vector database so now we have all of

**[0:02:00]** our knowledge these document chunks represented mathematically so we can use cosign similarity or other mathematical functions to determine how similar one text is to another in this case it'd be how determining how similar a user question is to a specific chunk of text and so what that actually looks like

**[0:02:19]** here is a user is going to ask a question and we're going to use that same embedding function that we use to create the vectors for the document chunks to create a vector for the user question and then put that into the V Vector database and match it with the

**[0:02:32]** most relevant knowledge that has this most similar Vector to the user question and then return the top K similar chunks so maybe you're going to give the five most similar chunks that you found for the user question feed that into the prompt for the large language model which then uses it to answer the user's

**[0:02:49]** question so this is kind of a a bit more of a detailed diagram of the very first one that I showed and so with that really basic understanding you could take this and dive so much deeper into how rag works and there's so many different way ways to optimize it but

**[0:03:01]** this is rag in a really basic sense so let's go ahead and use this knowledge to now create a chatbot where we can use llama 3.1 to talk with our local text and PDF documents so not only am I going to show you in just a few minutes how to

**[0:03:13]** build a super powerful chatbot to use llama 3.1 405b to talk to your local documents but I'm going to show you how to do it absolutely from scratch as you can see here we just had the skeleton for a main function in the python code so I'm going to walk you step by step

**[0:03:28]** how to implement rag to talk to your PDF and text documents so first things first there going to be a link to the code in the description of this video a GitHub repo so you can follow along if you want and with that we'll go ahead and start

**[0:03:39]** importing all of the packages that we need here so we have Lang chain we have streamlit for our user interface we got hugging face for our access to llama 3.1 405b I go into all these things in a lot more detail in other videos on my channel if you're curious about that

**[0:03:53]** I'll also be pumping out a lot more content on rag because there is so much that you can do with this this is just the beginning so after we all of our packages here we're going to load our environment variables which includes our model which defaults to Lama 3.1 405b as

**[0:04:06]** well as our directory that we want to chat with the local documents in and then with that we're going to create our function to get our local model and we're caching this with streamlet so that it doesn't instantiate our model every single time it reruns the script when our UI reloads and so to start what

**[0:04:21]** I'm going to do is just use a hugging face inference endpoint so this isn't actually pulling the Llama 3.1 model locally and that's because this model is massive my computer is not good enough to run it most computers are not good enough but if you actually want to run

**[0:04:36]** llama locally and your computer is good enough you can use this code instead so you just replace this code with what I got commented out here and then this will download the Llama model locally and run it for the rest of the code that I'll show in a bit here and so with this

**[0:04:50]** we'll get an instance of the model and then we'll move on to our function that is going to load the documents and get them ready to put them in a vector database and so given a directory this is going to use the Lang chain directory loader to get all these documents into

**[0:05:04]** my script there are a lot of different loaders that you have in Lang chain I'm just using a directory loader because this is a super convenient one to just pull in everything given a folder and so with that I'm going to split the documents into chunks like I talked

**[0:05:18]** about earlier just having a chunk size of 1,000 characters there are a lot of different ways to chunk but this is just a really simple method that I'm going to implement right now and so with that I'll return all the documents and then go on to our function where we actually

**[0:05:29]** inst initiate our Vector database so I'm using chroma for a local Vector database that's just going to run in memory you can also use chroma and save it to dis to have more persistent Vector DB storage um but overall chroma is just really the best platform for having a

**[0:05:44]** local Vector database and so we're going to call the function to load all the documents in our rag directory that we have defined through our environment variable and then we're going to also create the embedding function using an open source hugging face embedding model and so this is what we're going to be

**[0:05:58]** using to create the vectors for both our user questions and our document chunks and so we combine both these things together to then create the chroma Vector database instance that's going to be in memory using the documents as well as our embedding function and then with that we're just going to get an instance

**[0:06:14]** of the database with calling our function again this one is cached so that we're not reinstantiate the vector database every time the UI refreshes next up what we're going to do is Define the function to query our documents so given a question we want to get the most

**[0:06:28]** relevant knowledge that is in our Vector database I have a really nice dock string for this function just as a teaser to show that we're going to do some tool calling with rag later on so that we have an agent that will decide when it needs to do rag instead of just

**[0:06:40]** doing it all the time so anyway just a teaser for another video so in this function here we're going to use the chroma similarity search function on our Vector database given the question and then we want the five most related pieces of knowledge five most related document chunks to be returned in this

**[0:06:56]** similar docs array so then we're going to format that out and then just return that here and so this function is going to be used in our next function we create here which is to actually prompt the large language model and so with this we're going to get the last user

**[0:07:10]** message and we're going to query the documents based on this last user question and then format The Prompt around that so we're going to give it the context for answering the question which is what we fetch from the vector database and then end with the user's actual question so this is what we're

**[0:07:25]** going to actually feed into our chat hugging face object so we Define it with the large language model model that we have above based on the environment variable and then we get the response by invoking it with the full list of messages except we're replacing the very last message with the user message

**[0:07:41]** augmented with the extra context that's why we are fetching every message in the array except for the last one and then adding on this custom message here which is our context and question combined together into one prompt and so with that we have everything we need to prompt the AI so we're just going to

**[0:07:58]** return the response and so now the last thing we have to do is just Define our streamlet UI in our main function that leverages everything that we just defined here so we'll start by creating a title chat with local documents we'll initialize the initial state for streamlet we'll display all the messages

**[0:08:13]** that are going on to the UI and then we'll handle the user input here and so I even have a couple of example questions of things that you could put in and I'll actually test with these you'll see in a little bit and so we'll add the user message to the UI add it to

**[0:08:25]** the session State and then actually prompt the large language model with the messages get response add that to the UI in the state and we are good to go that is literally everything for this chat bot so now all we have to do is add in some documents and then run the chat bot

**[0:08:40]** and chat with it and so if we go into my documents here I have this folder called meeting notes and then within it I have two PDFs and three text documents so that is what I'm using to chat with my local documents right now and so for all

**[0:08:52]** of these documents I'm going to have them actually in the repo if you want to use they're just kind of madeup meeting notes that I literally just had GPT produced for me here so these is what the PDFs look like and the text documents are very similar but I just

**[0:09:03]** wanted to show that we can use the Lang chain directory loader to load both text documents and PDFs and you can use other loaders in Lang chain as well if you wanted to use Word documents or HTML documents or markdown files you can handle any kind of file with a local rag

**[0:09:18]** system like this so very very powerful so with that let's go ahead and run the chatbot and test it out so here we are in the streamlet UI that I ran simply with the command streamlit run the name of my python script hold up this in the browser and now we can chat locally with

**[0:09:32]** our PDF and text documents powered by llama 3.1 405b so I looked through the five documents that I had there put in the vector database and I picked out a few example questions so we can test if this thing is really working for us so the first question I'm going to ask is

**[0:09:46]** what's included in the wellness programs Emily proposed and boom right away it gave yoga sessions and Mental Health Resources it picked this out out of all the texts that I had from the PDF and text documents and I'm not going to go and show this now in the document but

**[0:09:58]** this is the correct answer and so with that I'm going to just test out again here so what are the results of the team survey so a very generic question but there is still a correct answer here to pick out from the five documents that I have the PDF and text documents so let's

**[0:10:13]** see if this can give us the right answer and there we go overall morale is high but some team members Express concerns about workload and deadlines and this is exactly right so it went out it found the five most relevant chunks threw that all into the large language model and it

**[0:10:28]** is able to concisely answer even with all the stuff that we throw at it in the prompt so yeah let's just do one more here but this is looking really really nice so last question here what was discussed in the meeting on the 22nd so instead of very specific answer now I

**[0:10:40]** want to actually summarize a lot of text and here we go review of previous action items Art and Design updates server stress test preparation marketing metas and adjustments and focus group planning for cyber Warriors there we go that is a really nice and concise summary of the meeting all fetched using rag so this is

**[0:10:57]** working perfect so that wraps up the most concise rag tutorial on YouTube I hope that you found this helpful and it gave you a really solid foundation of understanding for how rag works and how to implement an agent with it there are a ton of topics with Rag and you can go

**[0:11:12]** so deep with it I'll have more videos on my channel in the future going over all these things because this is just the Baseline you can get so complex with rag with optimizing it and using it as a part of AI agents and so yeah a lot more

**[0:11:24]** to come on this but I hope that you found this helpful if you did I would really appreciate a like and a subscribe and with that I'll see you in the next video
