---
type: raw-transcript
title: "I Built the ULTIMATE n8n RAG AI Agent Template"
youtube_id: mQt1hOjBH9o
url: https://www.youtube.com/watch?v=mQt1hOjBH9o
slug: i-built-the-ultimate-n8n-rag-ai-agent-template
published: 2025-02-26
duration: "0:34:03"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** retrieval augmented generation is the most popular tool to give AI agents access to your knowledge base essentially making them domain experts for your documents and it's really easy to implement Rag and no code tools like n8n as well because it is so widely adopted and supported but I'm going to

**[0:00:18]** be honest a lot of times rag sucks for me and the reason for that is mostly because it relies on a lookup that often times can miss key context and related information good luck trying to analyze Trends in a spreadsheet when the rag lookup only pulls a fourth of the chunks

**[0:00:34]** for the table and you need the whole thing and I find it so frustrating when I ask it to do something like summarize a meeting but then it pulls the meeting notes from the wrong date like come on the date for the meeting is right there in the title the document why can't you

**[0:00:47]** get the right one and not to mention that rag often struggles to connect different documents together to give you that often necessary broader context really this boils down to two things first rag isn't able to zoom out to entire documents or sets of documents unless the context is small enough and

**[0:01:05]** then secondly rag has no concept of proper data analysis so now the question is how do we overcome these limitations and there are a couple of ways to do it but my absolute favorite is a gentic rag and in this video I'll show you what that is why this solves our problems and

**[0:01:21]** I'll show you exactly how to build an agentic rag agent in Ann plus this workflow that I walk you through I'll have as a downloadable template for you to bring in your own NN instance in minutes so this is the bird's eye view of the agentic rag agent in n8n that I'm

**[0:01:36]** going to walk you through right now and I will be the first one to admit there's a good amount going on here but don't worry I will walk you through everything because this is what it takes to make a good agentic rag setup including I'll be walking through the rag pipeline as well

**[0:01:50]** so you understand everything going from our files in Google drive all the way to extracting from the different file types and adding into our superbase knowledge base and I do want to make a local version of this as well using the local AI package so let me know in the

**[0:02:04]** comments if you'd be interested in that and this entire workflow is sort of the version three of the n8n rag agent that I've been working on this is the last version that I covered on my channel previously this is a much simpler implementation so a good starting point

**[0:02:19]** that handles some different file formats and everything but it doesn't work with tabular data very well as we'll see later in this video you need to add tables differently from csvs and Excel files to the knowledge base compared to other things you can't just treat it as a text document CU you have to be able

**[0:02:34]** to query that table and also this agent only has rag for its tool you can see based on this tool node here there's nothing else that it has so if the rag lookup fails to get the information it needs the agent has no other way to explore the knowledge in superbase it's

**[0:02:49]** just stuck and it has to tell the user that it doesn't have the answer even though there's other ways you can look at these documents to potentially get the answer in a different way and that is what we're doing in this workflow right right here so let me zoom in on

**[0:03:01]** this a little bit so you can see the tools that we have for our rag agent so we still have the rag lookup tool just like we had in our previous example which by the way this is an improved version that can site its sources so even that is a step up but then we also

**[0:03:14]** have all these other postgress tools for our rag agents so that can do other things to look at our knowledge and so that gets into our definition for a gentic rag all agentic rag is is giving agents the ability to reason about how they explore the knowledge base instead

**[0:03:30]** of just giving it a single tool it also includes agents being able to improve the rag lookup queries and choose different tools to answer different user questions so in the old version of our agentic workflow here we do have the ability to improve the rag lookup because we have rag as a tool the agent

**[0:03:48]** could decide to invoke it a second time with a better query so we have that part at least but there's no way for it to explore the knowledge base in different ways or figure out based on a user's question oh I need to look at the data in this way

**[0:04:00]** but with these three postgress tools right here we are giving it to our agentic rag agent in this upgraded version because it can list out all of the documents that are available in the knowledge base and then it can get the file contents of specific ones so if a

**[0:04:14]** rag lookup fails for whatever reason then instead of doing that lookup we can look at the files available to us and then reason about which document or documents we might want to look at to get that answer so if we ask it to summarize the meeting notes for February

**[0:04:28]** 23rd and the rag lookup fails for whatever ever reason maybe it pulls from the wrong date whatever it might be then we can instead just look at the documents and see like oh yeah the title of this document is literally February 23rd meeting note so I'm going to pull

**[0:04:41]** that get the contents for it and then use that to answer the user's question so you can already see how it's able to in different ways look at the knowledge base use rag look at the entire document it has all of that in its tool belt and then we also have this tool to query

**[0:04:55]** Excel and CSV files as if they are SQL tables super super cool this is a bit of a fancier part of the implementation but it makes it so powerful to be able to get things like sums and maximums over tables that you typically can't get with rag because

**[0:05:10]** it's never just pulling in an entire CSV file unless it's really small so now it is time to take our agent for a spin we'll ask it some tougher questions that maybe the old version could have answered with just rag maybe not but the most important thing I want to show you

**[0:05:23]** is it using these different tools to explore the knowledge base in different ways depending on the question that I ask so I have these six documents in my Google Drive some that are spreadsheets some that are regular documents and I already have this all in my super based

**[0:05:36]** knowledge base and I'll walk through getting this all set up later as well so we have our documents table that includes things like our embeddings for rag metadata and the contents for each of these chunks then we have the document metadata table that I'll explain more later this has the high

**[0:05:49]** level information for our documents like the URLs for citing sources and the titles as well and then we have our document rows table this is how we take our CSV and Excel files and store them in super base where they can be queried with SQL queries even though we don't

**[0:06:04]** actually have to create a dedicated SQL table for each CSV or Excel file it's very very neat and so I'll go back over and let's go ahead and ask it a question for one of our documents actually first I'll open one of these I'll just show you the data and the question that I'm

**[0:06:17]** going to ask so we'll go into the 2024 Revenue metrics by month this is all fake data generated by Claude by the way um and we'll ask it a simple question like which month do we get the most new customers and maybe you could pull in this entire table with rag because it is

**[0:06:34]** small enough but we want to see our agent write a squl query to fetch this because if this table was big enough we wouldn't be able to pull the entire thing in with rag because it would just take the number of chunks that it would accept and that might only be like a

**[0:06:46]** fourth of the table and so we might not even pull in the record that has the most number of new customers and then it would give us the wrong answer so let's go back and actually ask that question here so I'll say which month did we get the most new customers and my goal here

**[0:07:01]** is to see it invoke the tool to write a SQL query yep there we go it did so I'll even click into this so you can see this is the query that it decided to write a little bit more complex we won get into that right now but yeah look at that 129

**[0:07:13]** new customers in the month of December and that is the right answer so we got everything back and yep right here it says the correct answer all right so next question I'm going to have a blank slate for the conversation for each one so I cleared that let's go back over to

**[0:07:28]** Google Drive and open up a text document this time so areas for improvement this is a customer feedback survey I'm going to ask it how can we improve and then see if it can pull this from this document specifically without me calling it out explicitly so I'll go back here

**[0:07:42]** and I'll just ask what are areas we could do better with and I specifically don't want to use the word Improvement because I want to make sure that this lookup isn't just relying on the fact that we kind of just say word for word areas for improvements so I'll just say

**[0:07:55]** areas we can do better with and it yeah it use rag for this time around mobile access integration capabilities and Reporting customizations and that is exactly right so boom we got the right answer so now I'll go back clear the conversation again and this time I wanted to explicitly look at the

**[0:08:12]** contents of a file instead of Performing Rag and surprisingly this can be tricky to get it to do when you're in a test environment with only this much data it's hard to make rag fail so it needs to actually pull the contents of an entire file so I'm going to be explicit

**[0:08:27]** here I'm going to tell it to use this tool just so you can at least see it in action but trust me from my experience with rag in general this kind of functionality certainly is necessary because rag isn't always reliable because of what we were talking about earlier on so let me open up this

**[0:08:41]** product team meetings minute I'll tell it to look at this file specifically to then pull the action items that we have so let me go back over to n8n for this test I'll also have it site its source but first let's ask it to get the file contents of the product meeting minutes

**[0:08:56]** and then tell me the action item so I'm explicitly asking it and there we go yep it called the tool to get the file contents it returned the entire document here and yeah this answer looks good Marcus to provide a timeline that looks good everything else matches up yep that

**[0:09:10]** looks perfect and then I'll also ask it to site its source so site your source so I want a link to the document cuz I want to maybe go and check then to make sure I had the right answer if I don't have the document pulled up already and

**[0:09:22]** there we go gives us a link right here I can click on this and then boom we have the document open right from our agent look at that the sponsor of today's video is unra an open- Source no code llm platform to create apis and ETL pipelines to turn unstructured documents

**[0:09:37]** into structured data and this is so important for AI agents especially with rag because you're not always going to have simple CSV and text documents for your knowledge base so you can easily just extract all the text and dump it in sometimes you're going to have PDFs where you have to pull specific tables

**[0:09:54]** from or you're going to have images that you need to extract information from for something like a receipt and that's what stack can help you with and you could even turn it into an API endpoint to put into something like an 8 end workflow to handle your more complicated documents

**[0:10:08]** so here is the GitHub repository for unrack and you can think of this platform as being three distinct Parts first you have the prompt Studio this is where you can engineer your prompts to work with the llms and make sure they know how to extract the information from

**[0:10:21]** your unstructured documents and then you take those prompts and you add them into workflows this is where you build these flows to automatically extract the information from your documents then you can deploy the workflows as data apis and ETL pipelines and they have fantastic documentation that I'll have

**[0:10:37]** Linked In description for how to work with all these different components for the things like API deployments and ETL pipelines and I also just want to call out the prompt Studio really quick because it is just fantastic how easy it is to upload a file like this receipt

**[0:10:50]** that I just pulled off Google and then Define prompts to extract all the different key pieces of information you want like the line items and the tax amount and the dollar amount of at the bottom and it just does so well extracting all this so you define your

**[0:11:02]** prompts here figure out exactly what you need and then go on to build your workflows so if you have more than just simple CSV and text documents that you could extract with a single node in n8n I would highly recommend it checking out unrack it just solves so many problems

**[0:11:16]** that we have working with our more complex documents and it's so important for a huge variety of use cases including rag agents so I'll have a link in the description below to unrack definitely recommend checking them out if you want to work with all of your data and and not just what's simple so

**[0:11:31]** now you know at a high level how this agentic rag setup works so I want to drill down now into the different components so that you have what it takes to take my template and extend it to your specific use case this is a very good starting point but I don't expect

**[0:11:45]** it to be an outof the-box solution for you I do want you to work on the prompting and the tools and the pipeline change things up to work with your specific knowledge base and so zooming in here I'm going to show the first part of this workflow and that is running all

**[0:11:58]** the nodes in this red box to set up your superbase database cuz we have these three different tables here and we have to create each one of them so the first node is to create our documents table and if you've set up rag with NN before this query probably looks very familiar

**[0:12:14]** to you CU this is in the setup instructions for superbase so you might already have this you could always just use what you already made or rename the documents table and the query here but this builds our documents table where we store the embeddings for rag the metadata and all the contents of each

**[0:12:30]** file as well and then we have the second node to create the metadata table and this table is what stores the higher level information for our documents so that our agent is able to look at things at a higher level compared to just dead rag lookup decide based on the title if

**[0:12:46]** it wants to analyze an entire file um like the revenue metrics for example and it also has the URLs so that can cite its sources both Rag and the entire file lookups here on these tools for the agents that cite it sources when it calls those and then the last thing that

**[0:13:02]** we have that I'll explain more later is the schema so for just the spreadsheet type files we Define the schema here and that tells it what Fields there are when it queries the data for that table in the document rows table which Speaking of that that is the third node here is

**[0:13:19]** creating the document rows and all of the data for each row is stored in jsonb in this row data column right here that is how we're able to essentially create SQL queries for our table data but not have to create a brand new SQL table for every file that we ingest because it's

**[0:13:39]** all done within this Json B which is flexible we can have any kind of schema stored in the row data right here so that is kind of what we see right here like for example this file we have cohort initial customers all these different things but then for this

**[0:13:53]** spreadsheet we have CAC LTV Mr all that different data is stored in row data and then the schema right here tells the agent how to query it what columns are available to it and it's not the perfect setup because it doesn't tell you things like the type of the data so it might

**[0:14:09]** try to do a sum over something that actually has dollar signs for each number so it's a string so not a perfect implementation again this is just a template to get you started um but it does show the concept very powerful in a simple way and that's the main thing

**[0:14:22]** that I'm trying to do with this agent so the second part to our workflow is our rag pipeline that's everything in this blue box where we're taking documents from something like Google Drive and bringing it into our superbase knowledge base and obviously we have to do that before we're creating our actual AI

**[0:14:37]** agent because we need a way to test to make sure the tools we're giving it to explore the knowledge base are working and so I'll walk you through the pipeline right now I won't cover creating all of the different credentials for things like Google Drive and super base because I have done that

**[0:14:51]** before in other videos on my channel like for this version of the workflow and if you go to create new credentials there's always going to be an open dock button that n and gives you it brings you to their documentation page that makes it super easy to set up your

**[0:15:03]** credentials the one thing I will say for the postgress nodes though and the credentials for that is that the N8 end documentation is not very clear you need to use the transaction Pooler method for connecting to postgress so you go into your dashboard for superbase click on connect in the top middle this will save

**[0:15:21]** you a huge headache by the way it did for me you don't want to use the direct connection parameters these won't work you want to use the transaction cooler ones where the port is 6543 so this will give you everything you need obviously except for the database password which

**[0:15:36]** hopefully you should have so with that out of the way let's dive into the start of this pipeline which is our Google Drive trigger so clicking into this node all we're doing in Google Drive is polling every minute for new files that are created and you can swap this out

**[0:15:49]** for a Dropbox or a local file trigger which I'll show you that when I make the local AI version of this this is just an example using Google Drive so it's watching every minute for files created in a specific folder that I give it in my drive and then I have a similar

**[0:16:02]** trigger for files that are updated as well so this workflow will handle both files being created and updated there isn't a trigger to watch for files that are deleted unfortunately it's kind of a big bummer I hope they add that in NN just so that you could clear your

**[0:16:15]** knowledge base when you delete a file in Google Drive as well so currently that is not supported and then one thing that was really missing from my old version of this workflow is it didn't handle properly when multiple files came into the trigger at the exact same time it

**[0:16:29]** would just send one file through this entire workflow and skip the rest of them but in this version I am handling that for you I know that was a big piece of feedback that I got I added this Loop in so now it can handle when you dump in

**[0:16:42]** multiple files within the same polling minute or update multiple and I even show this here because in my pin data for my Google Drive trigger I have two items I'm sending in two files and handling that in this Loop and so what it'll do here is send one file through

**[0:16:58]** this ENT Tire flow just like we saw before but then it'll Loop all the way back and do the same thing for the next file and the next file until it gets through everything that the trigger gave into the loop so I hope that makes sense definitely wanted to improve that for

**[0:17:13]** you all and so now we're zooming in on just a single file level the rest of this happens for just one file at a time first of all i' ran everything here already so we'll see the inputs and outputs because I have a test execution that I went through that's why you see

**[0:17:27]** the green boxes for all these and so in this first note here we're setting the stage for the rest of the workflow with all of our important information like the file IDs for our queries the file type to determine how we want to extract the content and then the title and URL

**[0:17:39]** as well which is going to be going into the database now the next thing you want to do is clear out all the old data for this file in superbase and that is if we are updating the file we're just going to do it every time in case and the

**[0:17:50]** reason we want to do this we want a blank slate because we want no chance that there's any data from an old version of our file left in the knowledge base for our agent to query when it shouldn't be available and to give you a very clear example of this

**[0:18:03]** let's say you have a file that is initially 10 chunks cuz it's something like 10 paragraphs but then you delete the last paragraph now it's only nine chunks if you try to just update the existing chunks in the database instead of clearing them and inserting them new you're only going to update the first

**[0:18:19]** nine and then that 10th chunk because the file used to be longer is going to remain in the knowledge base even though it's from an old version of the file and so the most Surefire way that's generally recommended is just to delete everything so we're deleting all of the

**[0:18:33]** document rows specifically for this file ID using that metadata field that I'll show you later on and then doing the same thing for the data rows as well for all of our tabular files and again just based on the file ID that we already set we're just going to delete all of those

**[0:18:49]** records in the superbase table and then we want to do our first insert or this is actually an upsert too because if the file already exists we're just going to update the metadata and then if it doesn't exist we will insert the metadata and this is just setting the

**[0:19:02]** initial stage for our document here with things like the title and the URL and then later for the tables we'll be setting the schema I'll show you that in a bit as well and we can set this here because this table doesn't rely on having the content for the file yet

**[0:19:15]** because we're going to extract that later and that's when we'll be able to populate the documents table because we'll have that content extracted to add in the the content column here create our embeddings and add those all that good stuff the reason that I'm I'm using postgress here and then super base here

**[0:19:32]** they're kind of interchangeable but postgress offers some better nodes for things like running SQL queries doing upserts like perform an update if it's not there insert it you don't have those options for the superbase nodes but I do want to use super base for deleting because it has this filter option that I

**[0:19:48]** didn't see with post grass so that's just a little aside why I'm kind of mixing and mingling the postgress and super based nodes in this workflow so okay at this point we have a blank slate and we inserted the initial metadata now we want to extract the content for the

**[0:20:02]** rest of this pipeline so we download the file from Google Drive so this data field that output is the file itself like I could download it or view it so we don't have the content of the file yet we have the file itself stored in our NN instance now so we can extract

**[0:20:16]** from it and then we go on to this switch node So based on the type of file there needs to be a different way for us to extract the content from it because the way that you take content from a PDF or a spreadsheet or a Google doc those are

**[0:20:28]** all different and so we have these different branches that are all determined based on this switch right here so if it's a CSV file like it is in this test run then we go down output two that third branch otherwise if it's a Google doc or also the default is the

**[0:20:44]** output 3 as well then we go down this bottom Branch right here so for my test we see the green line going to extract from CSV because this test is working with a CSV file that I uploaded to Google Drive and it's actually quite simple if we're extracting from just a

**[0:21:00]** PDF or a text document we just have a single node here and I'll even show you if you go to add a new node and search for extract all these different file types are supported so if you want to extend this to work with Json files or extracting from HTML files you can add

**[0:21:14]** these extract nodes in and then you just need to add another Branch into the switch statement here so it's very easy to extend this for other file types as well if it's something that's not supported within those options that you saw there you can always create a custom

**[0:21:26]** n workflow to extract from different file types too so the world is your oyster here the different possibilities are endless for how you can work with really any file type that you want and then other file types like markdowns and text documents can also be handled by just extracting from the text document

**[0:21:42]** like this node covers a lot of different file types as well what I do want to focus on though is extracting from csvs because this is where it gets a little bit more complicated and we want to populate the schema in the metadata and the rows as well so let's go back into

**[0:21:56]** our n workflow I'll show you how this all works for CSV and Excel files so in this demo I'm just running this CSV path right here but for Excel it's exactly the same the rest of these nodes are the same we just have to have a different extract node and so first we are taking

**[0:22:11]** the contents from the CSV file and turning it into rows in our n8n workflow and then we want to do two things at once because we want the data from our table file to be available in reg so we want to turn it into a text document and

**[0:22:26]** chunk it just like the rest of our documents but we also want it to live in the document rows because we want to be able to query it as if it is a SQL table we're giving our agent the ability to do that so we have two different paths that

**[0:22:39]** we are going down here the first one for all 15 records that it pulled from the CSV we are inserting each of those into the document rows table so like this is all one file for example everything right here we're inserting all these records within this node right here and

**[0:22:56]** then in parallel we also want to start to turn it into a text document so we're going to aggregate everything together so instead of there being multile records it's just a single item which is an array of all of our rows and then we want to summarize it which essentially

**[0:23:09]** just turns it into a string because now we have a text document that we can chunk up just like if we extracted from a PDF or a markdown file whatever you might have in the top and bottom branches right here and then all of that goes into superbase which I'll cover in

**[0:23:23]** a second here so in the end the tables are treated just like any other text document but also we have this route right here where we're setting the schema so using this fancy JavaScript that I'm not going to explain in detail right here we're taking the headers from

**[0:23:37]** the CSV and defining that as our schema and then updating our metadata record so that the agent can access that schema as well so this is where we set this piece of information so we tell it that this CSV file has these headers and that's how the agent knows like it'll read this

**[0:23:55]** record first to get the metadata for the customer cohort analysis it'll see that this is the schema so then it knows how to write the SQL queries to query the rows here so I hope that makes sense so the agent has to look here first understand the schema then go and query

**[0:24:11]** the rows and we're making that all possible right here adding in the schema to that metadata record and then the last part right here is our super base and this one is pretty simple because na takes care of so much for us with all these nodes it is quite complicated to

**[0:24:25]** chunk everything and add it into super base but it's just done with four nodes here so first of all we have our insert into super base Vector store node where we just Define the table and the query that we are using for Rag and then we have our embedding which I'm just using

**[0:24:40]** open AI um by the way I'm using text embedding 3 for my embedding model and then for all of the llms I'm just using GPT 40 mini which isn't the most powerful llm I just wanted something cheap and fast here but depending on your use case you might want something

**[0:24:53]** more powerful as well like gbt 40 or clae 3.5 Sonet anyway that's our embedding model and then we are just using a default data loaders this is what's responsible for chunking our documents getting them ready to insert into superbase and defining the metadata as well which that is very very

**[0:25:10]** important for the metadata here I have the file ID and the file title and the reason this is so important is because the metadata is how we can query to delete only the records for a specific file when we're at the start of the flow when we want that blank slate for

**[0:25:25]** inserting for Rag and then the file title itself we also want in the metadata because the agent is going to reference this to know what file it's actually looking at when it performs rag so that it can site its source and we'll get into that later but in the rag tool

**[0:25:39]** we actually have it so that the metadata is returned as well so I have this ticked right here that's how the agent is able to know what it is looking at and then finally for the text splitter just have something very simple with a character text splitter didn't put a ton

**[0:25:52]** of thought into this because it will depend a lot on your use case how you want to chunk your documents so just keeping it very very simple there but that is everything for our rag Pipeline and you also saw as I was going through this workflow I showed you the inputs

**[0:26:04]** and outputs for everything so you basically saw a whole run of this um and I've already done that so all of the files that I have in my Google Drive for both my spreadsheets and my documents I have that all injested already so I've executed this workflow for every single

**[0:26:17]** one of them I just used the trigger dumped in my files and it handled that so with the rag pipeline created and all of our knowledge ready we can now move on to setting up our agent and luckily creating our AI agent is simpler than our rag pipeline cuz we do all the work

**[0:26:31]** getting everything set up in our knowledge base and super base and then our agent only needs a few rather simple tools to leverage it so let's go through that right here so first I have a couple of triggers for this workflow I have a web hook so we can turn our agent into

**[0:26:44]** an API endpoint and then I also have a chat trigger so you can chat with it right here in the N end workflow that's what gives us this chat button in the bottom middle here and then these two nodes output slightly different formats and so I have this edit Fields right

**[0:26:58]** here just a little bit of JavaScript to handle both of these different triggers so that we have a consistent output for our agent node and so going into that right here our agent is quite simple overall I just have this system prompt right here that describes to it the

**[0:27:12]** different tools that it has to explore the knowledge base and I give it some instructions for how to leverage these tools like for example I tell it to start with Rag and then use some of the other tools if rag doesn't give you the right answer and so you can certainly

**[0:27:25]** tweak this system prompt I think that there is a lot of opportunity to make this a much better system prompt I just have this as an example for you one thing that helps a lot with these kind of rag agents is ask it to be honest like if you don't find the answer from

**[0:27:40]** Rag and the other tools that you have just tell the user instead of trying to make up something yourself and this alone can reduce a good amount of hallucinations and then for our model we just have gbt 40 mini like I showed earlier setting up a simple postgress

**[0:27:53]** conversation history right here which by the way this table is created automatically if you don't have it already in the first conversation which is why I don't create this as a fourth node in the red box so nice and simple and and just makes it easy for you and

**[0:28:07]** then we go on to our tools so the first tool that we have is Rag and you'll see here looking at the old version of the workflow this is a much simpler version and it's because n8n has had a lot of really awesome updates for AI agents since I made that last video and so this

**[0:28:23]** tool for the superbas vector store is much simpler and there's the option now to include the metadata so the file ID and the file title that we inserted in the metadata for each record like I'll show that here I go to documents and then click in on the metadata field

**[0:28:39]** we'll see here that we have the file ID and the file title all of this is brought into the results for Rag and so the agent has access to that information to cite its sources that is super super important and then we are using the exact same embedding model that we use

**[0:28:55]** when we insert things into super base that's super important because you just have to make sure that your model has the same number of dimensions for both the inserts and the retrievals and then going to our other tools here the first one we have is to list our documents so

**[0:29:10]** just using a simple postgress query here we're pulling all of our documents from the document metadata table so the agent can read all these and then reason about which files it wants to look at and the IDS of each of them and also for the table files the schemas as well so it

**[0:29:24]** knows how to query the document rows table and I am returning every single document here so keep that in mind if you have a large large Corpus of documents you might want to not return everything and find some way to filter the documents that you are pulling maybe

**[0:29:40]** based on a date or having the AI write a query something like that um but also keep in mind the llms can manage very long context links right now so even if you have like a thousand documents in your knowledge base you still could pull the files and the titles and IDs for

**[0:29:54]** every single one of them and dump that into the prompt for the llm so that might even still work and then after we list the documents then the agent might want to pull the contents of specific files and so I just have this query right here that is

**[0:30:07]** essentially given a file ID that it pulls from the metadata table it can use that to pull the content of all of the chunks for the document and combine that together to give us the full text for that document and the reason that I'm using the content column in the

**[0:30:23]** documents table instead of just having a Content column in the metad data table that would have all the content for the file is just because n8n includes this content column by default it's something that I can't control so if it's already here I don't want to duplicate the

**[0:30:39]** information by having the content of the file stored in the metadata as well so I just pull all the chunks together for the content and combine that with this query right here and the one parameter that the AI decides is the file ID so it picks that out from the metad data table

**[0:30:54]** and then passes that into this tool so you'll see the agent every single time that calls get file contents it always called list documents first because it needs to do that to actually know what file ID to pass into the tool to get the contents for it and then the last tool

**[0:31:11]** that we have here is the one to write SQL queries to query our tabular data and this is a little bit of a fancier implementation here it's pretty Bare Bones as well there's a lot of room for improvement for the prompt here because what we have right here for the tool

**[0:31:27]** description is given given as a part of the prompt to the llm so it knows when and how to use this tool I mean same thing for all the other tools as well but I have to be a lot more explicit here because I have to help it

**[0:31:37]** understand the document rows table it needs to know how it's structured how it needs to use the row data Json B to write these SQL queries for these different files and I give it some examples as well and these examples are pretty barebones you probably want to improve this more for your specific use

**[0:31:53]** case and how you want it to query your tabular data but I give it examples of how to use the row dat a Json B to select certain columns to do group buys you could have it um understand filtering better all of that and then I have it write the full query so the

**[0:32:09]** parameter the single parameter here is the entire SQL query that it wants to write something like this to query the contents of a specific file because the data set ID is the file ID so that's how it specifies the single file that it wants to query and then uses the row

**[0:32:24]** data Json B to query and group by specific columns and do all that fil ring as well so that is the last tool and that is everything and I know that the tools got a little bit more complex there so yeah just let me know in the comments if you have any questions on

**[0:32:36]** that but this is it for our agent so we now have everything to do what I did at the start of this video just like a quick example here I can say like what employees are at the company just something super generic I mean this is the kind of thing that like again maybe

**[0:32:49]** rag could do but I'm just showing a random example here um just to show it using all the different tools here so yeah in this case it performed Rag and decided that it didn't get what it needed so decided to list a few of the documents as well and so it told us oh

**[0:33:04]** this document didn't give us what we wanted this document didn't give us what we wanted but then the product team meeting minutes did here are the team members so look at that it's so cool like I actually just pulled this example out of my butt just now but it worked

**[0:33:15]** really well because it showed performing Rag and that not working which kind of makes sense like you wouldn't really know how to find specific names using a vector search just because you're asking for employees so then it decided to search the files which is really cool so yeah good example I hope that this

**[0:33:30]** template can get you started super fast with a jtic rag in and an n and of course let me know in the comments if you have any questions as you build out this workflow it is getting into the more advanced rag topics also a lot more similar content coming out soon

**[0:33:44]** including a completely local version of this agentic rag agent built with the local AI package so stay tuned for that if you appreciated this content and you're looking forward to more things AI agents and n8n I would really appreciate a like and subscribe and with that I will see you in the next video
