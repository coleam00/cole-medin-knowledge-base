---
type: raw-transcript
title: "Your ULTIMATE n8n RAG AI Agent Template just got a Massive Upgrade"
youtube_id: iV5RZ_XKXBc
url: https://www.youtube.com/watch?v=iV5RZ_XKXBc
slug: your-ultimate-n8n-rag-ai-agent-template-just-got-a-massive-upgrade
published: 2025-09-03
duration: "0:19:20"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Retrieval augmented generation is the go-to way for giving your AI agents access to your knowledge base. And over the past few months, I've been experimenting with every rag strategy under the sun and combining the best together into a single N8N agent template for you. And I've been evolving

**[0:00:17]** this for a long time now, starting with super basic rag as an introduction all the way to what we have now with multiple rag strategies combined together. I've been making some big upgrades to this template that I want to show you today and I want to show you

**[0:00:31]** how you can use this template for yourself. Now, the reason I'm putting so much effort into these different strategies in the first place is a basic rag implementation is just not enough. If you aren't strategic about the rag strategies that you use, it's just going to seem like rag is fundamentally

**[0:00:48]** flawed. So, what do I mean by that? Well, I have the very first version of my NANN rag template so that I can explain the fundamental flaws that we have with a very basic implementation. Now, let me be clear. This template is a good introduction to Rag, but there is a

**[0:01:03]** reason I've been evolving it so much over the last year. So, every RG implementation has two components. We have our rag pipeline where we convert documents from our document store into the format that we're going to store in our knowledge base. So, we chunk things up into bite-sized pieces for our LLM.

**[0:01:23]** And then we give tools to our agent. This is the second component to search through our knowledge base. And so, I'll just give you an example here. I'll ask it a question where it's going to have to search through the documents that originate in my Google Drive. Going

**[0:01:35]** through the knowledge base to find the information to answer my question. Now, both the rag pipeline and Asian Tools, there is a lot of risk here that they miss key context and related information. When we do these very direct searches, a lot of times we're just not getting what we need from the

**[0:01:52]** knowledge base. If you're not very strategic about how you are chunking and curating the knowledge for your knowledge base, it doesn't matter how effective your agentic search strategies are, your agent will fall apart. And the same thing applies if we're curating our knowledge really well, but then we don't

**[0:02:07]** have effective search strategies. And so we want to solve for all of this. And this is what I have for you in the latest version of the N8N rag template. So this is what has evolved to now. It looks a lot more complex, but I'll break it down in this video. We have

**[0:02:21]** strategies for effective knowledge creation and effective knowledgebased search. And also, I want to hear from you what other strategies you want me to add into this template as I continue to evolve it. I could add in knowledge graphs or contextual embedding. So many different ways to build on top of this.

**[0:02:38]** Let me know in the comments what you think. So, I just wanted to say that really quick, but yeah, let's get into it now. And really, these rag strategies are going to be super helpful for you no matter the rag agent you want to build. So, you can use this template as a

**[0:02:50]** starting point. I'll speak to how you can do that and adapt it to your use case throughout this video as well. So, here are the three big strategies that we're going to be covering in this video that I've added to the template. First of all, we have a gentic chunking. Then,

**[0:03:04]** I want to dive into a gentic rag. And then, finally, we will cover re-ranking. Now, a gentic rag is something that I added in the last evolution of this template. So, check out this video right here if you really want to dive deep into that. But what I've added for the

**[0:03:18]** first time now is a gentic chunking and reranking. And man, do these strategies make a big difference. And so these are the huge upgrades that I'm talking about. Really excited to be covering this with you right now. Now the first rag strategy that I want to dive into

**[0:03:31]** with you that I added is a gentic chunking. And this one is really powerful because what we're doing is leveraging the intelligence of a large language model to help us determine how to chunk our documents. In a more traditional rag implementation, like in this template right here, we're using a

**[0:03:48]** more deterministic approach where we're splitting documents every 1,000 characters or 400 characters. And the problem with this is we're now splitting ideas in our document between different chunks that we'd want to actually have grouped together. And it even goes so far as to split in the middle of words

**[0:04:05]** and sentences with a very basic implementation. And we can get a little bit more elaborate and try to respect sentence and paragraph boundaries, but you're still going to be splitting in the middle of ideas that you want to have grouped together. And so this just leads to a lot of context loss when we

**[0:04:22]** search through our knowledge base and we're finding these chunks. Well, maybe what we have in this chunk, we actually want to have part of this chunk to really have that complete thought to answer the user's question. And so with a gentic chunking, this is the power here is we're giving the document to the

**[0:04:37]** large language model. We're telling it like based on the need that we have to keep ideas together, how should we split up this document? And so now going into my database. So this template uses Postgress. I've actually evolved it. So you can use any Postgress database like Superbase or self-hosted Postgress. I'm

**[0:04:55]** using Neon here for my database. We can see that with a gentic chunking. If I click into any of the chunks that we have here, we can see that we start with the beginning of a sentence and we go all the way through all these bullet points. So, like we're keeping this full

**[0:05:10]** idea, like this list of bullet points together. And you'll see that same kind of thing as I go through the different chunks here. We're not splitting in the middle of words or sentences that often. That's what we want to preserve here. Now, we do have to chunk documents. Like

**[0:05:24]** we can't just store every single document as a single record here because that's way too much to pull into the large language model and it's going to make the embeddings really inaccurate. So we need to have these bite-sized pieces of information. But as much as we can, we want to keep the concrete ideas

**[0:05:39]** together splitting the document with the help of a large language model. That's what agentic chunking gives us. And the rest of this rag pipeline is really the same as the previous iteration of this template. So again, check out the Aentic rag video that I linked to earlier if

**[0:05:55]** you want to dive more into this. So I'm keeping things concise here focusing on the newer strategies as well. But just for a quick recap, we have our document store, which in my case is Google Drive. You can easily update this though to be something like Dropbox or SharePoint

**[0:06:08]** instead. So we're watching for files that are created or updated. And if a file is updated, we also want to delete the old rows so we can insert just the new ones. And then we download the file from Google Drive. And then based on the file type, we have these different nodes

**[0:06:21]** in N8N that extract the text from that file format. So we even support tabular data with Excel and CSV files. I'll get into that a bit more when I talk about agentic rag. And then we have our textbased files. So Google Docs, text documents, markdown documents, PDFs. We

**[0:06:38]** extract the text from there. And then for these types of documents, this is where we feed into our agentic chunking system. And because this is a lot more of a custom implementation, there's not really a way to do this without code. But this is where the beauty of the lang

**[0:06:53]** chain code node comes in. So we can attach a large language model that we can use with the lang chain library right in nadm. This is a thing of beauty and I actually use cloud code to help me build this out. So basically the important things here is we have this

**[0:07:08]** prompt that we feed into our large language model that describes its role and the instructions for how we want it to intelligently split documents to keep the core ideas together. And you can see here that like based on some of the splits it's not ideal but for the most

**[0:07:24]** part it very much is starting the chunks and ending them with a key idea kept together. That's what we're trying to accomplish here. And this fixes a lot of problems that we have with rag where we just have so much fragmented context between the different chunks that we

**[0:07:39]** have for our document. So I send this prompt into the LLM and basically the LLM is going to output a word to split two chunks on. That's how we create these chunks over time. And all of this is going to be stored in our vector database. And so you could very much

**[0:07:56]** swap this out to use another vector database like Quadrant or Pine Cone if you want. Generally I love using Postgress. So I also evolved this template to work not just with Superbase like I had before but also any Postgress database. Right now I am using Neon which I have been loving recently. It's

**[0:08:13]** blazing fast serverless Postgress free to get started and I'll show you really quick. If you go into the dashboard, click on the connect button. This gives you all the information in the connection string here for you to connect with your Postgress credentials in N8N. So, super easy to get started.

**[0:08:28]** And really, that's everything for a gentic chunking. The last thing that I want to say here is that the other beautiful part of a gentic chunking is how flexible it is. Because you can tweak this prompt based on your use case to get really specific with how you want

**[0:08:44]** the LLM to split your documents. And so I've tried a lot of other strategies for chunking like recursive character text splitting, working with markdown documents and there are different subsections. I tried semantic chunking which is actually using embedding models instead of large language models to determine these boundaries. But man,

**[0:09:03]** agentic chunking is just the most flexible and the most powerful. So I absolutely love it and that is really the big thing that improves our knowledge curation, our rag pipeline for this template. The sponsor of today's video is depot and their brand new remote agent sandboxes for cloud code.

**[0:09:20]** I'll get into that in a little bit. But what depot has built is insanely fast globally distributed cloud infrastructure and persistent caching to make for extremely fast application builds. Things like remote container builds and GitHub action runners. And companies that have switched to depot have gotten up to 55 times the

**[0:09:39]** performance increase for their builds. And there are a ton of integrations with things like GitHub actions, CircleCI, Docker, and GitLab. And depot's cloud infrastructure has positioned them perfectly to build what I've always wanted for cloud code, remote agent sandboxes. And now they are here. It is a beautiful thing. Basically, what we

**[0:09:59]** can do is kick off a ton of remote Cloud Code sessions in parallel, all working on different features and issues in our GitHub repositories, and it's never running on our own machine. It's all running on Depot's infrastructure and getting started is super easy. So, I'll link to this quick start in the

**[0:10:15]** description as well. You just have to follow these steps to install the depot CLI, get your anthropic credentials connected and then we just operate in the terminal just like we do with cloud code. So, for example, I am asking it to summarize the archon repository linking to my repo. This is kicking off a

**[0:10:32]** session which we can view all of our sessions in the dashboard here. I can click into this and we can see the logs just like we're working with cloud code on our machine, but this is all running remotely. We could even kick this off from a mobile device if we want. The

**[0:10:43]** possibilities are endless for this and the power that it gives us. So, if you've always wanted to be a cloud code mastermind, kicking off a ton of remote sessions in parallel from anywhere, definitely check out. I'll have a link in the description. Now, the next rag strategy that I want to hit on is a

**[0:10:59]** gentic rag. This one is a gamecher and the implementation can differ a lot depending on your use case. But the general idea that I convey with this template is you want to give your agent the ability to explore your knowledge in different ways depending on what works best for the specific document and user

**[0:11:16]** question. And the way that the agent determines where to look is just all based on the system prompt. So you give it the ability to search in different ways and then in the system prompt you describe what that exactly looks like and you can tune this to your use case.

**[0:11:30]** So we want to be flexible here. That's kind of the theme for a lot of these strategies. So going back to our original template, there are two reasons why it is inflexible. First of all, we're only giving our agent a single tool to search our knowledge base and

**[0:11:46]** we're handling all file types in our rag pipeline the exact same way. But it works a lot better if we actually treat each of the different file types with respect. Like going back to the most up-to-date rag pipeline, for example, we're handling tabular data in a much different way where we're storing the

**[0:12:04]** records individually. Take a look at this. If I go back to my Postgress database in Neon, we have this special table called document rows specifically to store the rows for the tables that we are ingesting from Google Drive. like I have this uh fake mock data generated for a revenue spreadsheet here. We're

**[0:12:23]** storing each one of these records as an individual row in this document rows table. And the really cool thing with this, and again I dive into this a lot more in my agentic rag specific video is we're giving a tool for our agents specifically allowing it to generate SQL

**[0:12:37]** queries to calculate things like sums and averages and maximums over this tabular data. That's the kind of thing that rag normally completely falls on its face with. So, we can't just search tabular data just like we search text data. We can't ingest it the same way. And this can apply to a lot of different

**[0:12:56]** file types as well. So, I hope you're starting to see the idea here, the flexibility that we're adding with a gentic rag. Another really good example is sometimes if your documents are short enough to fit into the context for the LLM comfortably, you actually want to view the entire document instead of just

**[0:13:12]** viewing a couple of chunks. And so that's another thing that we're doing here within the most up-to-date rag pipeline. We're inserting what's called the document metadata. So essentially we have this separate table here where instead of storing all of the chunks split up we just have one record per

**[0:13:30]** document and then if our agent decides like oh this chunk is useful let me view the entire document it can actually do that. So we give it one tool to list all the documents that are available in the knowledge base. So, it's going to query this document metadata table and then

**[0:13:45]** when it finds a document like, oh, I should look in the research brief here. It can actually combine all of the chunks together to grab the complete document to look at it with a much more holistic picture. So, we have this tool as well, specifically to get all the

**[0:14:00]** file content for a specific file just based on the file ID that we have coming in from Google Drive. So, now I'll actually give you a couple of demos here so we can see a gentic rag in action. And so I'll open up the chat and I'll say what is the average revenue uh in

**[0:14:15]** August of 2024. And so this is going to query the sheet that we have right here. And so I'm going to go back. We can see that it first listed the documents that we have available to us. So it's querying the metadata. It's seeing that we have these specific columns here so

**[0:14:28]** that it can write that SQL query to query the rows that we have in document rows. So here is our query that it created. We got back the answer of 309.5, which is what it gave us. And that is looking really good. If I actually go in the sheet here and do an average of B2

**[0:14:42]** to B. Sure enough, we've got 309.5. So, this is looking great. And then I can ask another question here. Like, let's just pull up the marketing strategy meeting. So, I'll pull this up and I'll just ask it to view the entire marketing strategy meeting doc and give me a

**[0:15:00]** summary. So, I'm just being explicit here that I wanted to use the agentic rag tools to get the full contents of a file, which is what it did right here for the marketing strategy meeting. And then we'll go back to our chat. And yep, here is our summary based on this

**[0:15:13]** document right here. So, sometimes you want to do that kind of thing where you want to pull the entire document when it's short enough like this to do something like a full summary that we wouldn't necessarily be able to do if we just returned a couple of chunks with a

**[0:15:25]** classic semantic search rag lookup. So that is everything for a gentic rag and it's pretty neat like with a gentic chunking it was just touching the rag pipeline. Then with a gentic rag we are hitting on both the rag pipeline and the agent search. And now last but not least

**[0:15:41]** we have re-ranking which is specific to the search part of our rag system. So what even is a reranker? Well, you can think of it as a special kind of model. Not a large language model, but a re-ranker model where its sole job is to take in a massive amount of chunks from

**[0:15:59]** our knowledge base from our search. Like in this case, I have it set to 25 and it's going to rerank and filter those out only returning the top four. And you can adjust these numbers based on your use case as well. Now, the reason this is so powerful is if we were to return

**[0:16:14]** 25 chunks straight to the large language model, it would completely overwhelm it. It's going to make our agent more expensive, a lot slower, and 25 chunks leads to a very high risk of hallucinating because there's just so much information coming in. But re-rankers are designed to handle this

**[0:16:31]** much information, and they're a lot cheaper and faster. So, they don't have general intelligence like a large language model. can't build agents around re-rankers, but they're made to take in all these chunks and do that kind of reranking and filtering. And so, going back to the very first version of

**[0:16:47]** our template with Rag, we're only ever picking four chunks at most from our knowledge base, but that's pretty limiting. What if we want to actually deal with dozens of chunks and then just pick the top ones? Well, that's what re-ranking allows us to do. So, I'll give you an example here. I'll open up

**[0:17:02]** the chat and I'll say, "Give me an overview of Neuroverse." This is just one of the uh fake companies that I had claw generate for mock data here. So, we're using the semantic similarity search tool. That's the classic rag search that we've had throughout all the iterations of our template here. And if

**[0:17:17]** I click into this, we can see that we're only returning four chunks even though our limit is 25 because take a look at this. If I click into the re-ranker model and we look at the input that came in from our knowledge base, there is a lot of information here. We are taking

**[0:17:33]** 25 chunks. Take a look at this. It's a zero index. So this means there are 25 chunks in total. And then we are spitting out the top four after we use this reranker to figure out the ones that are the most relevant based on our question of give me an overview of

**[0:17:49]** neuroversee. Really really nice. And so the large language model if we take a look at the prompt that came in. This is the full prompt to the large language model. It's not that big overall. We have one chunk, two chunks, three chunks, four chunks as a part of our

**[0:18:04]** prompt. So that's an added context for retrieval augments generation. This is much better than if we actually gave 25 chunks, but we still got to sift through that many using the reanker to deal with all that information before it goes to our LLM. So that's re-ranking and there's only one option for a reranker

**[0:18:21]** right now in N using the cohhere models. But cohhere is actually fantastic. So you just have to go to cohhere.com. you can create a free API key. I'm just on the free tier right now. So, I'm not paying anything for this, just like I'm not with Neon. So, that's how you can

**[0:18:35]** add re-ranking into your N8N agents. So, that is everything that I have for this massively upgraded version of the N8N rag agent template. And I hope that I have covered really well how you can adapt this to your specific use case, picking and choosing some of the rag

**[0:18:51]** strategies, adjusting certain parameters, even adding in your own strategies. And there's a lot more that I could cover as well. So definitely let me know in the comments if you want me to cover knowledge graphs in this or contextual embedding. So many other strategies that I could include as well.

**[0:19:04]** And rag is just so important for AI. So I'm always down to cover more with my content. So if you appreciated this and you're looking forward to more things AI agents and rag, I would appreciate a like and a subscribe. And with that, I will see you in the next
