---
type: raw-transcript
title: "Effortless RAG in n8n - Use ALL Your Files (PDFs, Excel, and More)"
youtube_id: T1ZKEmDN8AA
url: https://www.youtube.com/watch?v=T1ZKEmDN8AA
slug: effortless-rag-in-n8n-use-all-your-files-pdfs-excel-and-more
published: 2024-10-09
duration: "0:18:18"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** making rag AI agents with n8n is super easy the AI agent node combined with the vector store retrieval and document inserter tools make it incredibly intuitive to create a simple rag Pipeline and use it to chat with your documents the hardest part of the whole setup is really just actually extracting

**[0:00:19]** the text from the documents that you want to put in your knowledge base especially if you want to use PDFs or other document types that don't convert as easily to Raw text last month on my channel I built one of these rag AI agents and a lot of rock stars maybe

**[0:00:34]** yourself included extended my workflow to make it work for their use cases and everything with the actual Vector database using superbase seemed to work phenomenally for everyone the tricky part came up when they wanted to extend the workflow to work with other document types like PDFs or Excel documents so

**[0:00:52]** today I'm going to show you how to work with different file types for Rag and n8n so you can start using your PDF documents in just minutes n8n unfortunately does not provide a single node that you can use to extract text from any file type so the problem is not

**[0:01:08]** trivial but I'm going to break it down for you so it can still be a really simple setup and I'll even show you how to extend what I've built to work with literally any type of file by the end of this video you'll be able to take your

**[0:01:20]** PDF and Excel documents and upload them into your Google drive along with a bunch of other file types and have them in your knowledge base ready for your rag AI agent in just minutes so let's let's go ahead and Dive Right In All right so I wanted to start off by

**[0:01:34]** showing you the workflow that I've already have for the rag AI agent n and this is what we are going to extend to work with PDF and Excel documents for rag I already built this in another video on my channel so I'll reference that here and you can go ahead and check

**[0:01:48]** that out if you want to dive into how I built this in a lot of detail I'm just going to give a brief overview of this agent and then we'll go into the changes needed to work with different file types and so right here this is the old

**[0:01:59]** workflow and I'm going to show you the new one right now so I'll click over to it and boom it's going to look almost the exact same but the big difference here is in the bottom right so let me go back to the old one we're extracting from the document all the text with this

**[0:02:14]** single node right here and then in the new workflow we've got some branching going on so based on the file type we're going to go to a different type of extract node in n8n to work with those different file types and I'll show what that looks like in a little bit here but

**[0:02:30]** first of all what I want to do is zoom in and head on over to the top of the workflow so I can show you very briefly what actually happens for us to chat with this agent and so at the start here we have two triggers we have one for the

**[0:02:44]** chat input and that's what gives us this chat option in the bottom Middle where we can talk to our agent within the NN user interface and then the other trigger right here is a web hook and this is how we can use our NN agent as an API I've got content on that on my

**[0:02:59]** channel as well so you can could have something like a streamlet app or a nextjs app built with cursor or vzer or something that uses this agent through the API and then what we do is we have this tools agent and this is where we Define the prompt from the user the

**[0:03:14]** system message and we hook in our model I'm just using GPT 40 mini in this case there's a lot of different models you can use in n8n um like through Gro or mixol or if you wanted to use uh Claude you could do that and then we have a

**[0:03:27]** superbase postgress database for our chat history and then the only tool tied to this agent is the retrieve documents tool that's given to us by n8n that allows us to perform Rag and we have a superbase vector store to take care of that and again we're just using open AI

**[0:03:44]** for our models here for the embeddings and then also to process the documents the chunks that we receive from rag so all that together is what allows us to interact with our agent for rag now the bottom part here is the workflow where we actually put documents into the

**[0:04:01]** knowledge base for the agent here to have that context and so starting with the triggers for this workflow here I'm going to go through these one step at a time because that's going to lead us into the end of the workflow where we're going to be splitting into these

**[0:04:17]** different options here based on the file type so I'm going to click into here we have a trigger for when a file is created we're going to trigger this workflow and this is specifically within one folder that I have here in my Google Drive and then we have a very similar

**[0:04:31]** trigger for when a file is updated in this exact same folder so n8n is going to pull this folder every single minute for any files that are created here or if I change any of these files in any way like renaming them or adding or deleting content in the file all of that

**[0:04:47]** and so what I'm going to do here is actually fetch a test event and so that way we can see the input that we get to our workflow uh when a file is created and it's going to look very similar for when a file is updated as well and so

**[0:05:00]** I'm going to now go on to the next node here and you can see we have the input so this is exactly everything that we get when the workflow is triggered when a file is created and this is very important I'm going to reference this later because there's information here

**[0:05:15]** that tells us which type of file we are ingesting and that way we can split to the correct extract node to work with that file type and you'll see that in a little bit and so I'm going to run this step as well we're going to get the

**[0:05:27]** output including the file ID and the file type now look at this the file type is application slvn Google Apps document this is the standard notation that denotes that the file that we are working with here is a Google doc now if it was a PDF document for example this

**[0:05:45]** would be application SL PDF and the way that we get this file type is through the mime type parameter of our trigger output so take a look at this when a file is created there's a ton of different attributes here on this file it's content when it was created when it

**[0:06:03]** was last updated the list goes on one of the parameters here is called mime type it's kind of a funny name but this basically tells you what the file type is again it'd be something like application PDF if it was a PDF document and we'll see that as well later when I

**[0:06:19]** trigger this same workflow with a PDF document so this is what we use this is really important because this is what's going to determine how we Branch later on to the correct ract node so we get the file type here and then the next thing that we do is we want to delete

**[0:06:35]** all of the old records in our Vector store for this document because that way we're going to get a fresh set of vectors for this document to make sure that we don't have old versions of it in the knowledge base because that will confuse the llm a lot and then the next

**[0:06:49]** thing we're going to do after we do that delete is we're going to download this file onto our n8n instance so that it is ready for us to extract the text from it because at this point we just have a binary file that's downloaded and then the next step is where we do the

**[0:07:02]** extraction now we get to the fun part this is where it really is different than the old workflow that we have here because in the old workflow we have a single node that extracts the document text now the problem with this is it only works for file types where you can

**[0:07:18]** just extract the raw text like a text file a Google doc you know like a markdown file or a CSV all those simpler file types when we have more complex file types like Excel docu doents or PDF documents it's not that simple and so I'll show you something really quick if

**[0:07:35]** you click on the plus icon here to add a new node into the workflow and you search for extract if I click on extract from file boom we have all of these options here for different variations of this extract node that work with different file types and so this is how

**[0:07:52]** you give yourself the power to work with a bunch of different file types like HTML Json PDF Excel pretty much everything that you could possibly need you have here and so you could also extend this to have even more branches to handle something else like if I wanted to include HTML as well I can add

**[0:08:10]** another branch and the way that we determine which extract node we go to is based on that mime type and so the file type right here that we get remember going back to the edit Fields node right here we set the file type based on the mime type that's available to us now in

**[0:08:29]** this file type parameter and so that is exactly what I'm referencing in this switch node right here so if the file type is equal to application PDF then we're going to go to this top Branch right here to extract specifically from a PDF document now the next up what we

**[0:08:49]** want to do is if the file type is equivalent to this is the exact notation for a Google sheet or actually not a Google sheet an Excel document those are two different things if it is an Excel document then we're going to go down this middle path right here where we are

**[0:09:04]** extracting from an xlsx document and then finally if it is a Google doc we're going to go down this bottom route that just extracts the raw text because that is a simpler format where we don't have to have a special node and also I want to call out that we

**[0:09:21]** have a default value here so the fallback option if the file type is none of these three we're just going to go down the bottom route so if it's something like a CS or a readme or a raw text file all these can also be extracted from this node so we're just

**[0:09:34]** going to use this one as well as a fallback option now a really cool resource that I want to point out and I'll have a link to this in the description by the way I'll also have a link to this workflow in the description as well check out this resource right

**[0:09:46]** here so in the Google workspace they have this documentation that tells you the exact string for every mime type so if you're curious like what is the mime type for a rich text file well it's just application SL RTF PDF is application PDF let me zoom in a little bit here and

**[0:10:04]** so this is how you can tell exactly what your mime type is going to be for the different files that you might want to process and rag so use this as a reference point for yourself if you want to extend this to have even more branches for different types of files

**[0:10:18]** use this to know what the mime type is of course the other solution is also just to you know upload one of those file types to your Google drive here trigger the workflow and then you would get to see just going in right here uh you know what the mime type is um like

**[0:10:33]** this so you could also do it that way but this is a really nice table to use as a reference there um so yeah that is everything so I'm going to run this switch here and we'll see that it's going to go to Output two as in it's

**[0:10:45]** going to go to this bottom Branch so it's index starting at zero so the PDF is output zero the uh Google or the Excel sheet is output one and then the fallback option also for Google Docs is output two so we output that data and then right here we just extract the text

**[0:11:03]** these are some fake meeting notes that I just have in my Google Drive and then we insert those into the vector database with this final step here so that is everything for a document like a Google doc and now I want to actually upload a PDF document so I have uploaded a PDF

**[0:11:20]** document to a new folder that I've created in my Google Drive I'm going to have a separate folder for each one of these files here I'll demo the Excel file as well uh just because n doesn't necessarily have the most recent uploaded file when you do a test event

**[0:11:35]** and I want to demonstrate that way so I'm just going to guarantee that it has the file that I want through having it through a new folder So within and and end here for the triggers I've changed the folder to PDF and so now when I click on fetch test event I know for

**[0:11:47]** sure that it'll pull my PDF and sure enough my MIM type is application PDF now I will say though that uh yeah you typically want to keep it all in one folder obviously and then when you have this workflow in active mode these triggers are going to activate for any

**[0:12:01]** files that you create or update in your Google drive without you having to actually run these steps manually so don't think that you'd always have to run these manually I'm just doing it here because I want to demonstrate the output at each step of the way to make

**[0:12:13]** this really clear for you and so now what I'm going to do is I'm going to go to the switch I'm going to click on test event and this is going to run everything leading up to this node right here and sure enough the branch that it has chosen now is the first Branch

**[0:12:27]** because the myot type is application SL PDF and so now you can see this green arrow here let me zoom in this green arrow points to the top extract from PDF node now because it has made that decision based on the mime type and so now when I run this it's going to

**[0:12:42]** extract the text from the PDF now one thing to keep in mind is that this output is different from the output from the extract document text the output from this node goes to a field called Data but the output from PDF goes to an attribute called text and so something

**[0:13:01]** super important to keep in mind this is like a really big Golden Nugget that tripped me up even when I was first setting this up when you go into the your default document loader this is where you load the text to then split into chunks your data has to correspond

**[0:13:17]** to the output field from the extract node and so if you are extracting from a raw text file or like a Google doc whatever it might be it's going to be json. data because again going back back to that node it outputs to the field data but then if you are extracting from

**[0:13:34]** a PDF document it's going to be json. text so again going back to this node right here it outputs to the attribute called text and so the way that you can do that within the double squiggly bracket JavaScript here is you can just say I want to access this attribute if

**[0:13:51]** it doesn't exist then I'm just going to go to this attribute and then if that doesn't exist like if it's an Excel file then I want to use the attribute that is outputed for the Excel file because a little sneak peek here for the um yeah it's going to this summarize right here

**[0:14:07]** the final step for extracting from an Excel document is going to Output to a field called concatenated Data so really important to keep in mind you have to set this up to work with the different attributes that can be outputed from these different nodes so I can then run

**[0:14:21]** this to insert it into our Vector database and let's see boom there we go we in inserted four items because it split up our PDF into four different chunks here all right so looking good so now the last thing that we want to do very quickly is just an Excel document so I'll upload

**[0:14:36]** that and come back when I'm ready to test that out as well all right so I've got an Excel file in this new folder called Excel again just to guarantee that that is the test event that is fetched and so if I click on fetch test event we now have an Excel file so I'll

**[0:14:50]** scroll over to the mime type and here we go we got that specific format and if I go back to this sheet that Google gives and I do a search sure enough this is exactly the mime type that it tells you to expect for axlsx file and so now I'll do the same

**[0:15:06]** thing where I just go to the branch and run everything leading up to it and we'll see what it chooses this time and there we go yep it has chose the second Branch for the Excel files and so now it's a little bit more specific with how you process these kind of files and this

**[0:15:22]** is something that I'll probably make a video on later on in my channel because there are a lot of different ways to split up records in a CSV file for rag what I'm going to do here is I'm just going to keep it really simple I'm going to extract everything in a table format

**[0:15:38]** right here and then I'm going to aggregate each of these records together into a single item and so basically I'm just going to take the entire Excel file and treat it as raw text to chunk it accordingly um and so then I'm going to summarize here which is basically just

**[0:15:53]** going to take this array and turn it into a single string and this is the string that I'm going to put into my database for rag there are a million different ways to do this you might want to create a record for every Row in your vector database or maybe you want to

**[0:16:09]** have 10 records per row there's a lot of different things you can do to play around with um how you inest documents in a table format like this I would say a lot of it depends on your use case so again I'll probably make a video on that

**[0:16:22]** in the future but right now I'm just going to do something really really simple where I just turn the entire document into a single string that I would would chunk just like I would with a raw textt file and with that we then have everything that we need to insert

**[0:16:34]** this document into the vector database and sure enough it just inserted a single record here because yeah like I said I essentially just treated this as a small raw text file instead of you know a bunch of different records in an Excel sheet and so with that we can now

**[0:16:50]** go over to our documents table it'll be populated now with all these different records here and yeah we've got our Google doc right here and then we got all those different vectors for our uh PDF document and then we have the Excel document here too and so what I'm going

**[0:17:06]** to do is open up my chat window here and just ask it a question that it would only know based on my let's just do my PDF document so I'll say uh what are the action items for Chris or from Chris see what it says to this so it's going to go

**[0:17:22]** and search the vectors here this is going to be something in my PDF document and yeah Chris has two action items finalize beta test testing for Space Rangers present a draft proposal for flexible working hours and we can even go into the superbase node here and see what it fetched from our knowledge base

**[0:17:39]** there we go it fetched four different chunks here and this G or I guess three different chunks here and this gave it everything that it needed to answer the question so this is working perfectly so I hope that was a really good followup for the previous video where I built a

**[0:17:51]** rag AI agent so you can take it forward with any type of documents that you want to have in your knowledge base if you have any any questions at all just let me know in the comments and I'd love to help you as you're trying to figure out

**[0:18:04]** how to ingest different types of documents how you best want to split them up for your knowledge base and all that good stuff if you appreciate this content I would really appreciate a like and a subscribe and with that I will see you in the next video
