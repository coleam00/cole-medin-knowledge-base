---
type: raw-transcript
title: "This RAG AI Agent with n8n + Supabase is the Real Deal"
youtube_id: PEI_ePNNfJQ
url: https://www.youtube.com/watch?v=PEI_ePNNfJQ
slug: this-rag-ai-agent-with-n8n-supabase-is-the-real-deal
published: 2024-09-04
duration: "0:16:28"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** most rag tutorials on YouTube you know your classic chat with your PDF documents are really not showing you how to build something you can actually use for real you'd have to change a lot and I mean a lot to really make it production ready and honestly it might

**[0:00:15]** work well at first but you're going to run into issues as your knowledge base grows your documents get updated and users on your app ask questions that you didn't expect or test now I'm not promising the perfect solution by any means but I definitely have something that you're going to want to check out

**[0:00:30]** today because I'm going to show you how to build a robust rag AI agent with no code using n8n and superbase n8n is an incredible and costeffective workflow automation tool similar to make.com and zapier and then superbase in my mind is the best absolute best database platform that also supports vectors for rag using

**[0:00:52]** PG vector and that's what we're really going to be leveraging today to make something that's way more immediately usable for rag than a lot of the things you've seen on YouTube at this point it is so so easy to combine n8n and super base together to create a production

**[0:01:07]** ready coste effective no code and simpl to understand rag AI agent where you can use literally any of your documents as a knowledge base we'll start by quickly showing how powerful this rag agent is and then I'm going to walk you step by step through setting this up yourself so

**[0:01:23]** you can do it in less than 15 minutes including setting up super base and creating This na end workflow for your rag agent so let's go ahead and Dive Right In All right so here is the full NN workflow for this rag AI agent which I'll dive into in a little bit but right

**[0:01:38]** now I have to show you how cool and easy to use this thing is and so at this point I have absolutely nothing in my rag knowledge base and I can even go over to super base and show you that this documents table that manages my knowledge base has nothing in it at this

**[0:01:52]** point and so now what I can do is I can go into the chat widget in the bottom middle here in my an workflow and I can ask a question to my agent that it shouldn't have the answer to right now because I don't have any documents for

**[0:02:04]** its knowledge and so I can ask something like what are the action items from the 825 meeting and this is something that will make it able to answer in a little bit here but right now I want to show that it doesn't have this answer at this point and so sure enough it can't find

**[0:02:20]** the answer so now let's go ahead and create a document in its knowledge base so that it can actually answer this question and so I'm going to take some fake silly meeting notes that I made uh for 825 I'm going to copy these I'm going to go into the folder that I'm

**[0:02:34]** using for the knowledge base for this agent so this is all hooked into n8n I'll click on new Google Docs so I'm going to make this as my file here and then I'll paste in everything here and then for the title of this document we'll just say 825 meeting notes so now

**[0:02:48]** there's going to be an NA workfl that triggers to add this into the rag knowledge base and so I'll come back once that is done in like 30 seconds to a minute so just a minute later and this na workflow has executed I'll show more what these executions look like later

**[0:03:03]** and how they work but if I go into the step here where I insert into my knowledge base sure enough the page content here is exactly what I created in this Google doc just now and I can also go over to superbase and see that our documents table that manages our

**[0:03:17]** knowledge base also has a record now for this meeting notes file we got the metadata as well including the Google drive file ID and then also the embedding Vector which we'll actually use for Rag and so now I can go back to my chat in 8N so I'll go back to the

**[0:03:31]** editor go to chat and then uh this is our last request here where it didn't have the information in the knowledge base this is just from a prior test where it was working obviously but now I can just copy this question and ask it again and this time it's going to have

**[0:03:45]** the answer because this document is in its knowledge base as I showed both in superbase and the N workflow execution and sure enough there we go we got the correct answer this is exactly what those silly action items are that we have in our Google doc right here so

**[0:04:00]** super easy to use this thing works really really well it handles any updates to Google Drive files as well and so now I'm going to dive in and show you step by step how to actually build this thing all right so I've already fully built out this N8 end workflow for

**[0:04:13]** my rag AI agent because I want this to be a really smooth walkthrough but I will go through this step by step for you so you have a really clear understanding of how this works and you can implement it yourself I'll even have a link to a GitHub repository in the

**[0:04:25]** description of this video where you can download this workflow yourself and bring it into your own n8n in instance very very easily all you have to do is download the Json file for this workflow and then go to the three dots here in the top right of your instance and then

**[0:04:39]** click on import from file so you'll bring in that Json file and then the only thing you have to do is put in your own credentials for things like the Google Drive and superpa base and then any customizations you might want like your folder for your knowledge base and

**[0:04:51]** Google Drive and then you're good to go it just takes a couple minutes you'll have this thing fully set up so you can steal it from me very very easily all right so with that we can actually dive into this NN workflow and see exactly how it works so the first thing that I

**[0:05:05]** want to do before we even get into all the actions here in the workflow is I want to get you set up with super base because this is going to be used both for our chat memory and our Vector database and that's the beauty of super base is we can use it for both and so

**[0:05:18]** what you're going to need to do is go to superb.com and then just sign in with your GitHub account you'll have a free tier which let me go to the pricing really quick and just show you the free tier is incredible like that's literally all you need to get started um there's

**[0:05:31]** no reason to go to the $25 month plan until you're really starting to scale your AI app so once you sign in and create a password you're going to be brought to a dashboard page that looks like this and so there's some credentials that we're going to be

**[0:05:43]** needing for some of the steps in NN so let me Point those out really quick and I'll reference those later so you go to your project settings in the bottom left here and then go to the database section of the configuration now here you're going to have everything that you need

**[0:05:58]** for your postgress connection for your chat memory so you have your host database name Port user and password so that's for postgress and then what you're going to need for the vector database side of things is the API connection so you go down to the API Tab and then here you have your url this is

**[0:06:15]** custom to you and then you can also reveal and copy your service R secret as well so both of these things in database and API will need later so anyway back over to n8n what we're going to do here is I'm going to show you step by step

**[0:06:29]** executing workflow and walking through every single node and so the first trigger that we have here for our na workflow is when a chat message is received so if I go to the plus icon and just search for chat this is the trigger that we are using right here and when

**[0:06:45]** you add this it gives you this chat widget in the bottom Middle where I can ask a question like uh what are the 825 action items the same thing that I asked in the demo there and so when you have this trigger gives you this chat window which makes it so easy to test and debug

**[0:07:01]** your AI agents just to iterate on it as you're developing it you don't even have to go outside of your NN workflow or deploy anything to be able to test things out so there we go we got the answer from the AI agent this is the perfect answer just based on the

**[0:07:15]** document that I've got here in my knowledge base and so with that you can even embed this on your website if you want so you don't have to write any code you can just click on more info and it literally gives you the code to embed this on your own website if you want a

**[0:07:26]** chat widget for this agent really really nice and so now that I've executed it I've got green check marks for all of the nodes that were executed so I can click into one and actually see the output from my chat trigger so I've got the session ID which is needed for the

**[0:07:40]** chat memory basically just my user session and then also the input to the AI agent and then if I go to my AI agent I can see the input on the left side which is the chat input from the trigger and then also the output which in this

**[0:07:53]** case is the action items from the 825 meeting just like I asked for so I can take the chat input and just drag in here like I did that's how I get the text the basically the request to the AI and then I've got a system message as

**[0:08:06]** well so that's how I set up the agent and then there's also a couple of things to hook into it namely the chat model which I'm using GPT in this case you can use something like anthropic as well and then I've got my chat memory which is using postgress and then I've got my

**[0:08:20]** tools for reg which I'm using the superbase vector store in this case so let me go over each one really really quickly here so for the chat model I'm just using GPT foral mini you can use any option from GPT with this node you can see the response that I got on the

**[0:08:35]** right hand side here and then for credentials all you have to do is just feed your open AI API key it is so easy and super base is going to be just as easy Google Drive is going to be pretty easy as well there's documentation that n gives you for setting up credentials

**[0:08:49]** for anything so it is so easy to walk through that and get that set up as well and then for the chat memory this is where we really get into something that is going to be better than than what you see in a lot of n8n tutorials on YouTube

**[0:09:02]** because if I click on the memory options here you can see that one of them is a windowed buffered memory and this means that it's going to store the chat memory just locally on your n8n instance which is going to overload the server that you're using to host n8n a lot of

**[0:09:15]** tutorials go with this because it's the easiest but using postgress with superbase is the way to really make it scalable and that's what makes it production ready and so setting up the credentials you just use the host database user and password that I showed how to get in super base and then uh for

**[0:09:32]** the table name it can be whatever you want and na will actually create this for you if you don't have it created already so you don't even have to create the table in superbase for this to work with NN which just makes it so so easy and then for reg we're using this

**[0:09:47]** retrieve documents tool there's a lot of different tools here but I'm just using the vector store tool and then connecting super base as my Vector store and so for the credentials for this one you just need a host and service roll secret which I also showed how to get

**[0:10:01]** and then closing out of this here you just have to select the table name and the options for the query name and to set up these two things NN has documentation for this as well so I'll click on the docs here and then scroll down to where it says a quick start for

**[0:10:15]** setting up your vector store and this gives you all of the SQL code that you need to run so you don't have to code anything to get your super base set up for rag so you just copy everything that you H that you see here all of this SQL

**[0:10:27]** code go back over to superbit and go to the SQL editor on the left side and then just paste everything in there so it'll create your extension basically adding PG Vector to your superbase account creating the table for documents and then also the function to match for Rag

**[0:10:45]** and so going to my table editor this is what creates this documents table that you saw in the demo that has the metadata content and embeddings for all the documents that I have in my knowledge base and then as an aside this is also the table that na creates

**[0:10:58]** automatically for the chat history iies so there you have it that's basically everything in superbase that we need for this workflow here uh and then going down to the other half of this workflow a bit of a simpler piece we just have the workflow for adding files to our

**[0:11:14]** knowledge base when they are created or updated in my Google Drive and so right here I'm not going to go over creating the Google credentials but again there's really really nice documentation that NN gives for doing this um but once you have the credential set up you can

**[0:11:28]** select how often you PLL for files that are created or updated and do it in a specific folder so in my case I'm using this meeting notes folder as basically the section of my Google Drive for Rag and so then this is for when files are created and I have a similar trigger for

**[0:11:43]** when files are updated so I can actually run one of these as a test event fetch test event right here and I can get the last file that was created so that I can go through my workflow one at a time and watch all the inputs and outputs for my

**[0:11:56]** nodes so we can go on to the next step in the workflow which is basically going to extract the file ID for the rest of my workflow so I have all the inputs from my previous step the trigger I want to get the ID and pass that in as an

**[0:12:11]** output which is my file ID so now I'm going to use that in later steps to pull this file from Google Drive and extract the content from it and then put it in my knowledge base now the next step we have here with superbase this is really really important I want to delete all of

**[0:12:27]** the old vectors for this file that already exists in my database because I don't want any duplicates this is another big thing that a lot of n8n tutorials miss out on with reg is they won't delete old records and so every time a document updates and gets reinserted into the vector database it

**[0:12:44]** is going to be a duplicate of what is already there because superbase and all the other options for Vector databases in n8n they are not upserts it won't update a vector if it already exists because it doesn't have the ID of the file as the ID of the vector in the

**[0:13:02]** database and basically what that means is that it's just going to keep adding duplicates if you update a file and update a file keep reinserting it that knowledge is going to be duplicated and that is bad and so what we're doing here is we're actually going to if I go to

**[0:13:15]** super base when we insert a another Vector for the 825 meeing notes if it gets updated we're going to delete this one first and then insert a new Vector with an ID of 30 that has the updated contents of the file this is really important so basically any Vector that

**[0:13:33]** has the file ID of the current Google drive file that we are updating as a part of the metadata we're going to delete it and so going to the database here you can see that we have the file ID stored in the metadata and this corresponds to exactly the same file ID

**[0:13:47]** of the Google drive file very very important step so we're going to run this and then we can see here if I go over to superbase sure enough this record is now gone so the vector database is cleared ready to be inserted ready to have the new record inserted

**[0:14:03]** for the updated version of this file so we have no duplicates and so going back to the canvas here the next step is to actually download the file locally and so that way we can extract the text content from it so I'm just getting the file ID from the previous step and then

**[0:14:17]** converting any docs to text and Google Sheets to CSV so that I can extract the raw text so that is what I'm going to do in this step right here and now we have the raw text which is the meeting notes that we have exactly what you see right here in the

**[0:14:31]** Google Doc and now the very last step is to insert it into the superbase vector database so the credentials are the same as what you've already set up and we're going to do pretty much all the same parameters as before using the documents table and then the match documents query

**[0:14:45]** so when I run this sure enough I get an output with the page content that matches exactly with the data that we put into this step and it doesn't have to do any chunking here because the file is small enough I've got a couple of things attached to this here like open

**[0:14:59]** Ai embeddings and then also the default document loader which is just going to use a recursive character text splitter so I'm not going to get into chunking too much but this is just a nice simple uh recommendation for a simple chunking that makes this Vector database work quite well so that is literally

**[0:15:16]** everything for this workflow we now have a fully functioning honestly pretty production ready rag AI agent you might want to enhance this in some ways to add like better semantic search or maybe like keyword search there's a lot of ways you can always s a rag application but this is a really really solid start

**[0:15:32]** so I'm going to go into the chat here I'll ask another basic question like who are the attendees for the 825 meeting again having to use rag to go to my meeting notes document and here we go Lucy Bob Tom Jim and Stacy perfect that is exactly the right answer and that is

**[0:15:47]** using the new Vector that I added after replacing the old one uh when I was going through this example just now so that is everything for getting started with a production ready rag AI agent built with no code n8n and superbase is definitely one of my favorite combinations in the AI world so I'm

**[0:16:04]** definitely going to be making more content on that in the future if you have any questions at all with anything in this workflow or if you want me to implement something similar to this or to build on top of it later let me know in the comments I always love feedback

**[0:16:18]** and I hope that you're looking forward to more content with n8n and superbase if you are I'd really appreciate a like and a subscribe and with that I will see you in the next video
