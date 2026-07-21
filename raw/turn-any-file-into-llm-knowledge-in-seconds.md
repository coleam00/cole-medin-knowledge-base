---
type: raw-transcript
title: "Turn ANY File into LLM Knowledge in SECONDS"
youtube_id: fg0_0M8kZ8g
url: https://www.youtube.com/watch?v=fg0_0M8kZ8g
slug: turn-any-file-into-llm-knowledge-in-seconds
published: 2025-10-01
duration: "0:21:22"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** One of the biggest problems we have with large language models is their knowledge is too general and limited for anything new. And no, dumping your documents into chat GPT every time you want to use them is definitely not enough. That is why retrieval augmented generation is such a

**[0:00:19]** huge topic when it comes to AI and it always will be. It is a method for curating external knowledge for a large language model. So you can basically make it an expert on your data, your meeting notes, your business processes, literally anything you want. Now the problem with rag is that this curate

**[0:00:36]** step where we're getting our documents ready for our agent to put it in our vector database, it can actually be very difficult, especially when we don't just have a bunch of ideal documents that are in something like a markdown format where it's raw structured text for our LLMs. What if we don't have a bunch of

**[0:00:54]** markdown? What if we have a bunch of different file types like PDFs? Good luck trying to extract the raw text from this. Or word documents, even working with audio files or video recordings. How do we extract the data from all these different file types seamlessly for our rag pipeline? Well, that my

**[0:01:10]** friend is where doc comes in. It is a free and open-source tool I'm going to show you how to use today to work with all these complex data types so you can properly curate your data no matter how complex it is to get it ready for your rag implementations. So we can actually

**[0:01:25]** work with complex files like this. It's not just raw text. We got tables, we got diagrams, we have pages that split things. We're going to be able to work with it all. That is what Dockling gives us pretty much right out of the box. So right now I'll show you how Dockling

**[0:01:39]** works and how you can get started with it super easily. Very quick to get up and running. I'll show you how to work with different file types in Dockling. And even at the end of this video I'll show you a complete rag AI agent that I built. It's a template available for you

**[0:01:52]** right now that uses Dockling in the Rag pipeline to work with the different file types and even uses some of the chunking strategies that Dockling gives us in the library. So it really does help us take care of everything in our rag pipeline. And like I said, the data curation step

**[0:02:08]** is the most important part of Rag because it sets the foundation for everything. So, Dockling is a Python package. All we have to do to get started is install it with PIP. And then they have some examples, super basic in their readme here. Plus, they have a documentation page. And so, I'll link to

**[0:02:24]** both in the description. Great resources to get you started, of course, with this video as well. So the third link I'll have in the description is for the complete AI agent that I have made for you using Dockling under the hood. And so at the top level of the repository,

**[0:02:40]** we have the agent. And then within the Dockling basics folder, this is where we have a few use cases I want to walk you through. So you have a super solid grasp of how to use Dockling at quite a basic level. So really simple scripts here to show you how easy it is to work with all

**[0:02:56]** of these different file types with dockling for our rag pipelines. So we will go through the features of dockling at a high level and how to work with these different file types and then kind of a culmination of that will be this rag agent that is using dockling under

**[0:03:10]** the hood. And so this question right here the answer actually comes from one of the audio files that I have in the documents folder. So what I'm parsing here for my knowledge base is exactly what I have in the GitHub repo for you. Take a look at that. We got an ROI of

**[0:03:24]** 458%. I can confirm that is the right answer. So that is looking really really good. And I do even have the full rag pipeline in this repo as well. Now I will say if you want a more complete rag implementation that is also using dockling under the hood I am hosting a

**[0:03:41]** workshop in the Dynamis community this Friday where I'm building dockling into the primary rag pipeline that I have as a part of the AI agent mastery course in the community. So if you are interested in building productionready rag pipelines and agents definitely check out Dynamis. And the recording for this

**[0:03:58]** Friday workshop with Dockling is going to be available permanently in the community just like all of the workshops that we're doing every single week. So let's start now with the readme that I have in the Dockling basics folder. A little bit of a progression that I have mapped out for you so we can get through

**[0:04:12]** the foundations of this pretty incredible tool. Starting with a simple extraction. We just want to take things like the text and tables out of a PDF document. That is the first script that I have for you here. and it's based on the basic example that we have in the

**[0:04:28]** dockling documentation. So we have our source, we create this document converter object and then we convert the source to a document. And so now we have this object that we can export to different types like JSON or raw text or markdown. Markdown is typically considered the best format for LLMs like

**[0:04:47]** I said at the start of this video. And so that is what we want to do. And take a look at this. We have extracted text from a decently complex PDF. Like I'll actually show you this here. If I go to this PDF, it's not trivial with all of

**[0:05:03]** the code examples and diagrams and tables that we have in this. That is what we're extracting with just a few lines of code in dockling. It is super cool. And I'm pretty much doing the same thing here. I have the path to one of the PDFs that I have in this documents

**[0:05:16]** folder. I'm creating that document converter, converting it, exporting it to markdown, and that's pretty much all I display in the script. So, I'll actually show you this right here. And it handles everything with OCR under the hood. So, we have object recognition. There's quite a bit of machine learning

**[0:05:32]** that's actually happening to extract everything from the PDF, especially because of little nuances you have with PDFs with things like tables being split between pages. We have to handle all of that. And Dockling also has a lot of functionality built in for you if you want to customize the OCR process. So

**[0:05:49]** there are a lot of different options that we have for different OCR solutions. Things like Tessact for example. You might have heard of that before. So there we go. This is the complete markdown of our PDF. And we're not extracting images or capturing or anything right now. There are ways to do

**[0:06:06]** that in Dockling as well, but it does actually recognize it. Like this is where we have an image and we can handle tables. Like overall this is beautiful. And it was pretty fast as well. Like definitely less than 30 seconds to handle this entire PDF. And so now this

**[0:06:19]** data is ready to be chunked up and put in our knowledge base for our rag agent. We'll get to that in a little bit. All right. Now, for the second example here, I just want to show you how easy it is to work with multiple different file formats in Dockling because under the

**[0:06:34]** hood, it recognizes the file extension and it knows what to do to work with those different file types without us having to do that much more in our code. And so now in our second script, take a look at this. If I go down to the bottom, I have a list of a few different

**[0:06:49]** files that I want to extract from. I got a couple PDFs, a word document and a markdown just to show we can keep working with raw text of course as well. So we create our document converter and then I have this function to process any document and it's pretty short overall.

**[0:07:05]** We can just call the converter.con convert on that file path. We don't have to specify what the extension is. We don't have to specify a strategy. I mean there are some options we have if we want to customize things but dockling can be so so basic and still work

**[0:07:20]** extremely well and then we just export it to the markdown and then that's it and we just print the output of each of these files and so I'll go ahead and run this script as well. I'll pause and come back once we have the process complete for each of these files. And there we

**[0:07:34]** go. We got our little summary here of everything that it extracted from our four different documents. And this time I also set it up so that this script outputs to a folder right here. So we can quickly take a look at the outputs from our different files. And so for

**[0:07:47]** example the word document that we processed. I can click into this right here. We got our meeting notes. There we go. Looking really good. And it's all structured markdown. Take a look at how beautiful these tables look. These are perfect markdown tables that it took from the Word document. And we have our

**[0:08:03]** PDF for example. Even more beautiful tables. And it recognizes where we have images. like this is just so so good. Exactly what we need to now chunk up and put in our knowledge base. And I'll actually show chunking strategies in a little bit. But the next thing that I

**[0:08:18]** want to cover with you here is working with audio files. And there's a specific way to handle that with Dockling very easily as well. So using audio files in Dockling does require a couple of extra dependencies because we need a way to pull a model to handle speech to text.

**[0:08:34]** And so make sure you install FFmpeg. I've got instructions depending on your OS. And then also if we look at the requirements in this project, I did add OpenAI Whisper, which is an open source tool. We're going to be using Whisper Turbo as our speech to text model

**[0:08:47]** completely locally. Everything here with Dockling is local by the way, just grabbing models from Hugging Face. It is a beautiful thing. And so going to the third script that we've got right here, we have our audio path. And then we call this transcribe audio function. And this function is pretty basic overall. We are

**[0:09:06]** setting up what is called an ASR pipeline. And there are a lot of different options that you can configure for your speechtoext pipeline. You can take a look at the dockling documentation for that. I'm just going with the defaults mostly here to keep things simple using the whisper turbo

**[0:09:20]** model. So I set up my document converter just like we did when we were working with textbased files. And then again just like with textbased files, we call converter.convert. And then we can export the MP3 content as a markdown document. That is the beauty of Dockling is all of the different file types we're

**[0:09:39]** working with, they all just end up as markdown. So we basically have the ideal documents folder here where everything is set up as markdown ready to be put in our knowledge base. And we have to have this extra step of data preparation to make that happen. But Dockling just

**[0:09:54]** makes that so easy. All right, I ran the third script off camera to transcribe our about 30 secondond audio file. And in total, it took 10 seconds and outputed 576 characters. And 10 seconds is not bad considering this is running completely locally with Dockling. So here is our transcript output. And then

**[0:10:14]** of course I have it in the output folder as well. And it even has timestamps here for all the sentences that it transcribed. You can disable this of course if you want, but it is pretty nice that we have this metadata to build into our rag system for any of our audio

**[0:10:27]** files. Very, very nice. And so, going back to our readme here, the last thing that I want to cover. Now that we've gone over extracting from different file types and seeing how easy that is with Dockling, I want to talk about chunking. Not only can Dockling help us with the

**[0:10:42]** data extraction from our documents, it can also help us with the chunking part of our data preparation. And this is crucial because we cannot just take our document text once we have it extracted and dump it in our vector database. That is way too much for the LLM to retrieve

**[0:10:59]** all at once with RAG. We can't just give it the entire document, especially when they are much bigger. What we need to do is split our documents into bite-sized pieces of information for our LLM to retrieve. So, it gets just that paragraph or that bullet point list, whatever it needs to answer our

**[0:11:16]** question. And there are a lot of different strategies to do this effectively because obviously the challenge here is how do we define those boundaries? How are we going to split? Are we going to split right here? Like this would be chunk one and this would be chunk two or we going to split right

**[0:11:30]** here. How exactly do we do that? We definitely want to make sure that we don't split in the middle of paragraphs and bullet point lists for example. And so that's what Dockling helps us with. It's a pretty technical challenge under the hood, but Dockling makes it easy with a few different strategies that it

**[0:11:45]** give us. And the one that I want to focus on here that is getting insane results for me is hybrid chunking. This gets a little bit technical, but bear with me because I think this is fascinating and super powerful. With hybrid chunking, we are using an embedding model to define the semantic

**[0:12:01]** similarity between the different, you know, paragraphs and sentences that we have in our document. So, we use the embedding model to figure out where can we split in this document to still keep the core ideas together in these bite-sized pieces of information for the LLM. And because Dockling takes care of

**[0:12:19]** all the logic of the strategy under the hood, using it is actually pretty simple. So, in the fourth script that I have for you here, we have a path to a PDF that we want to process. And so, we're going to turn this into a dockling document just like we've been doing in

**[0:12:33]** our other scripts. But instead of extracting the text from it right away, we're going to create this hybrid chunker object. There are a few different parameters that you can customize here. Once you have this though, you just call chunker.chunk on the document. So this is our PDF doc,

**[0:12:48]** obviously. And so we're going to get an output that is kind of similar to the markdown that we saw when we ran the first script, but this time things are going to be split up in a way where we already have our chunks ready to insert in the vector database. Like literally

**[0:13:01]** what we have as the output from this script is what we can put right in our vector database. So just like the last example, I ran the four script off camera to extract the text from our PDF and chunk it with hybrid chunking. And so in the end we have 23 total chunks.

**[0:13:18]** 13 that are between 0 and 128 tokens and 10 that are between 128 and 256. And so we have some variety here because we are allowing the embedding model within reason. Of course, we have a max token limit for each chunk. We are letting the embedding model decide what

**[0:13:35]** goes into each bite-sized piece of information to keep all the similar ideas together. And of course, I've got the output for the chunks as well. And this is looking so good. We have the top chunk with the title and subtitle. We have all of our sections together. Bulletoint lists are maintained in each

**[0:13:51]** chunk. This is super ideal. All of our sections, as long as they're short enough, they remain in a single chunk as well. And this all comes from a complex PDF. Like this is just a beautiful thing. And then at this point, we can take all of these chunks and insert them

**[0:14:05]** right into our vector database. In fact, that is what I have now as the top level example for you here. And I'll cover this in a little bit with you. This is the complete rag AI agent that takes all of these ideas. We're parsing MP3s and PDFs and Word documents. We're using

**[0:14:20]** hybrid chunking. We're getting all this ready. And then I have an AI agent built on top that can query it. And that's what I demoed at the start of this video. The last thing I want to say on Dockling before I get more into the rag agent is you should definitely check out

**[0:14:32]** the example part of their docs if you want to learn more. There are so many great use cases they have built out here and just showing you ways to customize the platform. For example, custom conversion. We can see how to use different OCR backends for extracting text from files like our PDFs. Also,

**[0:14:49]** they have this visual grounding example which is super super cool. Not only can the agent reference knowledge in our knowledge base that we have curated with dockling, but it can also literally highlight like draw a box over the part of the document that it got its answer from. Very, very cool. So, Dockling

**[0:15:06]** really handles everything that we need as far as data extraction. And so, generally how I think about it is if I'm dealing with website data, then I use crawl for AI. I've covered this on my channel before. I'll even link to a video right here. for anything else

**[0:15:20]** besides websites with any kind of documents I'm dealing with, then I will go with Dockling. So, these are the two tools that I have in my arsenal to build out pretty much any rag pipeline that I want. And so, definitely let me know in the comments if you want me to cover

**[0:15:34]** more use cases with Dockling or even showing you how to use in other platforms like N8N. I definitely want to keep covering Dockling in more content for you. All right, here is the grand finale because now we're combining everything we learned around chunking and parsing different document types

**[0:15:49]** into a single rag agent that I have as a template for you. Link to all this below. And so right now I just want to cover at a high level how this works and how doling fits into our rag pipeline and even show the agent and the tools

**[0:16:01]** that I'm giving it to search our knowledge base that we curate with the help of dockling. And so this read me that I have at the top level of the repository. This has an overview of the agent, prerequisites, a quick start, including setting up your database and all the tables that we have here. Really

**[0:16:16]** easy to get this up and running yourself if you want to use it and build on top of it. And so we have our database schema here. For the vector database, I'm using Postgress with PG Vector. And of course, you could tune this to use Pine Cone or Quadrant. They even have

**[0:16:30]** some examples with Quadrant in the Dockling documentation. But yeah, we have our document table here where we store the higher level information like each of the individual documents that we have in our knowledge base. And then we have a table to store all the chunks that we create with the doc dockling

**[0:16:45]** hybrid chunking strategy. And then we have our match chunks function. This is the SQL that our agent actually invokes as a tool to search our knowledge base. And so most of the logic with dockling itself is in the chunker.py pi right here because this is where we chunk our

**[0:17:03]** documents. And so I have this function here where we pass in that dockling document. So this is going to be our PDF or our word document. And just like we saw in the simpler examples before, we just call chunker.chunk on that dockling document. That is all we have to do to

**[0:17:18]** perform hybrid chunking. It is so easy. And then we pull the contextualized text. Contextualize basically just means we're also including things like the headings and subheadings that we have in the markdown as well. And then we create our chunk metadata. I could do a whole another video on metadata as well, but

**[0:17:33]** just providing that additional information that speaks to our chunk. And then we're just adding that to our list of chunks that we're curating. So we then take these chunks, we embed them with an embedding model, and we store them in our vector database. At this point, there is no more document

**[0:17:48]** processing we need to do because with Dockling through parsing our different file types and performing the hybrid chunking, we now have our text in exactly the format that we're now going to insert in our vector database. Again, regardless of the vector database that you use and then for our AI agent here,

**[0:18:07]** you know that I love using Pyantic AI if you've seen any of my content previously. So, we're using Pideantic AI to create our agent here. So we have some logic here to set up our database connection because we're giving that in as a dependency to our agent. So we've

**[0:18:20]** got nice system prompt here and then giving it a single tool to search our knowledge base to perform a rag query. And so I'll go to this function really quickly here. Search knowledge base. We just have a query that the agent decides basically it's search for our knowledge

**[0:18:36]** base. We set up the database connection. We embed the query with the same embedding model that we use in our rag pipeline. And then we're going to call that match chunks function that I showed earlier. So we're passing in the query here. It's going to return all of the

**[0:18:50]** similar chunks that we have, you know, compared to the user query and then that's returned to the agent to then reason about what it retrieved and use that to help give us the final answer. That is rag in a nutshell. And so going back to our diagram here, we've mostly

**[0:19:04]** been covering the data preparation, but now I'm starting to speak to the retrieval augment generation, the actual query process that we have because we create an embedding based on that query that the agent decides that hits the vector database to retrieve the relevant chunks that we have curated from

**[0:19:18]** Dockling. Then that is fed back into the LLM to give us the final response. All right, back in the terminal now, we can run the CLI that kicks off the chat interface with our agent. And I already ran the whole ingestion pipeline here that pulls all the documents and it

**[0:19:32]** looks very similar to the examples we saw earlier where it just pulls the text from each of the documents, performs hybrid chunking, puts it in our database. So we've got our knowledge base ready to go. 13 documents, 157 chunks in total, all processed by Dockling. And so now I can ask it some

**[0:19:48]** questions where clearly you'd have to go to the knowledge base to get the answers for us here. And this is all just mock data for a fake company that I generated for our demo purposes. And there we go. The revenue target for Q12025 is set at 3.4 million. And I believe this is from

**[0:20:03]** one of the PDF documents that we have. And so on my lefth hand monitor here, I've got some other questions like from one of our Word docs. When was Neuroflow AI founded? Let's make sure it gives us the answer of 2023. Yep, there we go. All right, looking good. Let's just do

**[0:20:14]** one more question here just to test something. Uh maybe from one of the MP3 files. So one of the MP3 files I talked about global finance. What ROI did Global Finance achieve? And it should say, there we go. Yep. 458%. All right. And each of these times is

**[0:20:29]** telling us that it's using the search knowledgebased tool that we saw set up in the code for our agent and in the database. So this is working phenomenally. So there you go. That is everything that I have for you today for Dockling. And like I said, this is one

**[0:20:43]** of the most critical tools for your rag implementation for any agent or application that you're building that needs to bring external information into a large language model. So definitely I do want to cover Dockling a lot more in the future, building out more specific use cases with it, showing some of the

**[0:20:59]** more advanced features like actually captioning images that we pull from PDFs. There's so many more things that we can do with this tool. Dockling plus crawl for AI is all you need for any data you have to extract for any use case. So if you appreciated this video

**[0:21:13]** and you're looking forward to more things on rag and AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next
