---
type: raw-transcript
title: "You HAVE to Try Agentic RAG with DeepSeek R1 (Insane Results)"
youtube_id: uWDocIoiaXE
url: https://www.youtube.com/watch?v=uWDocIoiaXE
slug: you-have-to-try-agentic-rag-with-deepseek-r1-insane-results
published: 2025-02-02
duration: "0:22:20"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** deep seek R1 the latest and greatest open- source reasoning llm has taken the World by storm and everyone is talking about a implications and it strengths and weaknesses but what no one is really talking about is the kind of really powerful agentic workflows that it unlocks and it needs more of a spotlight

**[0:00:18]** so that is what I'm going to be doing in this video showing you a super simple and really powerful agentic rag setup with R1 and we're going to be using small agents by hugging face a super simple agent framework to keep it very easy to understand and follow along plus

**[0:00:34]** we're going to be doing everything locally with the R1 distill models this a gentic rag setup centers around the fact that reasoning models like R1 are super powerful but also quite slow and because of that there are a lot of people myself included that have started to experiment a little bit with

**[0:00:51]** combining the raw power of models like R1 with faster more lightweight models that actually direct the conversation or a gentic flow you can basically think about it as these models having R1 as one of their tools so that when necessary they have access to more reasoning at the expense of a slower

**[0:01:08]** response and for our use case in particular what that means for us is we're going to have an R1 driven rag tool that can be used to extract in-depth insights from a knowledge base while still keeping the rest of the conversation very very Nimble and I've been using this to get some incredible

**[0:01:23]** results even with the smaller distill R1 models the example in this video is meant to be more of an introduction to the these kind of agentic flows that's why we keep it simple with small agents and a local knowledge base but I am certainly planning on expanding this a

**[0:01:38]** lot more soon creating a way more robust but still similar flow with pantic AI and Lang graph so definitely let me know in the comments if you're interested in that I have some wild ideas that I would absolutely love to build out and share with you but anyway enough of that let's

**[0:01:53]** get into this implementation with R1 and small agents so I wanted to start by showing you this diagram here so you can conceptualize what we're building with a genck rag and R1 at a very high level and again this is going to be pretty simple here because I want to just

**[0:02:07]** introduce you to this huge rabbit hole that you can really go down with using reasoning llms combining them with other llms in these kind of workflows it's something that people are just not focusing on enough so I really want to cover this with you but also keep it

**[0:02:21]** concise and keep it simple that's why we're going to be using small agents so we have our primary llm right here I made this diagram with the help of Claude so Claude called this fast agent so this is an llm like Llama Or quen that is not a reasoning llm and because

**[0:02:37]** we are using small agents they actually break down problems in steps so you have this little bit of a loop here that I'll show you when we build out the workflow so it thinks to itself a little bit not as a reasoning llm just as a regular one

**[0:02:49]** and then when it decides that it needs to look up knowledge it'll call this tool right here so this entire box that we see as the second bottom box this is just a single tool for our primary llm that is driving the conversation and so we'll have the user query passed in

**[0:03:06]** it'll do a retrieval with rag in our Vector database to pull the relevant context to answer the user question and then feed that into the reasoning llm which is R1 in this case to extract the necessary insights from the context and then give it back to our primary agent

**[0:03:22]** to continue the conversation and it might look a little complex here but it's actually going to be very very simple thanks to small AG agents and also still very powerful thanks to R1 so here is the homepage for small agents which is our ticket to bootstrap our agentic workflow with R1 very very

**[0:03:40]** quickly and they have very simple documentation to go along with a simple framework here so if you click on the guided tour uh from the homepage of small agents this is the page I'd recommend reading through to get a solid understanding of the core of what small agents offers they talk about installing

**[0:03:57]** it and how you can run it with any model that you would pick from hugging face just using their inference API they talk about their code agent their tool calling agent and how you can set up your tools and create custom tools very very simple nice and concise guide here

**[0:04:12]** they got some examples as well and then also some references here just so you can see all the parameters that you can use to set up your agents and tools which we'll get into when we create our agentic flow as well so absolutely wonderful you just install this with Pip

**[0:04:25]** which I'll show later as well and then the other thing that we want to install is olama because this is is one of the ways for us to run our one locally so you can just click on this download button right here just by going to ama.com and then when you search for

**[0:04:38]** models like I can search for deep seek R1 right here we have all these different versions that are available for us to download and run locally so the 671 billion parameter model this is the massive version the real version of Deep seek R1 that you couldn't really hope to

**[0:04:55]** actually run on your own Hardware unless you're paying tens or hundreds of thousands of dollars or you have a very small quantization which I don't want to get into that in this video but these other versions right here are quite small and realistic for anyone to run on

**[0:05:10]** their machine so the 7 billion parameter version is what we're going to be running in this video here and so what deep seek actually did it's super fascinating they took their competitors which are quen and llama and they essentially fine-tuned them Based on data produced from deeps R1 to turn

**[0:05:27]** these into small reasoning llms that we can run locally very easily so absolutely fascinating that's what we're going to be doing later I'll show you how to run this all with AMA later as well and then the other option that we have is we can install deep seek

**[0:05:40]** directly from hugging face or use it through their inference end points here and so I'll show later how to do that as well when we set up the code um but yeah you can use hugging face or olama to get any version of Deep seek that you want

**[0:05:52]** including the distill versions as well like if I wanted to install Quin 2.51 14b uh this version of R1 and so so yeah so many options for you now let's dive into getting things set up with small agents and then I'll show you how to run all these models after that all right

**[0:06:08]** now it is time to create our agentic rag system so everything that I'm going to be going over here all of the code that I've got right here in vs code I'll have in a GitHub repository which I'll have a link to in the description of this video

**[0:06:22]** so if there's anything that I didn't cover super clearly you can also read through this read me right here that you'll see there so I make sure that it's super easy to set up and follow along with everything that we're building here I also have a em. example

**[0:06:35]** file to show you how to set up all the environment variables that you need also this is able to work with both going through hugging face for your models and also going completely local with olama so with that let's dive into building out our agent I'll walk through this

**[0:06:49]** with you step by step we are building this from scratch here so the first thing that I want to do is import all of the libraries that we need most of which is going to be relying on small agents all of these different classes that we have here for our agents tools and even

**[0:07:02]** our UI that we'll get to build up very very quickly then we'll load our environment variables and grab the ID for our reasoning model like R1 or you could go use o03 mini cuz apparently that was just released I found out in the middle of recording this video we're

**[0:07:16]** going to be using R1 for our reasoning model and then the tool model ID that's going to be the ID of our model that is going to be driving the primary conversation like quen or llama a non reasoning llm and then we have our hugging face AP token which this is

**[0:07:31]** optional there are a lot of models you can use for free through the hugging face API but some are restricted and then you get better rate limits if you just pay the $9 a month for hugging face Pro and get your API key then we're going to define a function to get our

**[0:07:45]** model which there's going to be a different way that we do it based on if we're using hugging face or not so that's determined through this environment variable right here if we are using hugging face then we're setting up an HF API model instance so this is how we use the hugging face face

**[0:08:00]** API to pull that model like llama 3.3 or Quin or whatever it might be and then if we are not using hugging face I.E we are using AMA then we're going to take advantage of the fact that olama is open AI API compatible so we set up an open

**[0:08:15]** AI server model but we're changing the base URL to just point to olama that is hosted locally on our computer so as long as you went to ama.com and installed it and you're running it on your computer this will point to your olama instance and then the API key you

**[0:08:29]** you can set this to whatever you want because we don't actually need a key when we're using olama locally so that's how we get our model now we can actually use that to create our agent so first of all I want to create my reasoning model because this is what I'm going to use in

**[0:08:43]** my rag tool so I get the model based on the ID this is going to be either the ID from hugging face or AMA and then I create an instance of the code agent so in small agents the base agent actually executes its actions through code it's a

**[0:08:58]** very unique paradigm I kind of have mixed feelings about this um cuz sometimes I don't want my agents to execute their actions through code but this is how you set up a base agent and small agents so we're just going to roll with this and obviously this llm doesn't

**[0:09:12]** need any tools at all because it's just going to Simply reason about the context given from a vector database using our reasoning model and then I don't want to add any extra tools there's a lot of Base tools like web search that you can inject right into your small agent

**[0:09:26]** agents which is super cool um but I don't want any of that for my ER here and then also like I said when I showed the diagram you can actually have these small agents break up the problems step by step and kind of go in a little bit

**[0:09:39]** of a feedback loop so I'm saying right here for my Reasoner I want it to have Max steps of two so it's going to only reason back to itself one extra time um because I've seen it kind of hallucinate when it starts to get into a loop of

**[0:09:53]** doing it six or seven times if you uh don't limit it right here so that's a super important thing that I noticed from my testing so that is our reasoning model now we want to get into our rag tool so the first thing that we need is an embedding model CU we have to take

**[0:10:08]** the user query and embed it and then match it against relevant context in the vector database which by the way I'll show later how to set up the knowledge base as well I just wanted to get our agent up and running first so we create this embedding model from hugging face

**[0:10:22]** so we're going to just be running this locally on our machine and then we're going to get an instance of our Vector database again I'll show how to set this up later as well and so now that we have our embedding model and we have our Vector database instance now we can

**[0:10:37]** Define our tool this is going to look very similar to setting up your tools in another framework like Lang chain or pantic AI you use this tool decorator that we imported right here from small agents to tell our llm that this is a tool that it has in its tool belt and so

**[0:10:54]** I'm calling this rag with Reasoner because it's taking the context from the vector database and using R1 to get insights from it and the parameter here is simply the user query so what we want to actually search the vector database with and so again just like with Lang

**[0:11:09]** chain and pantic Ai and other Frameworks we use this dock string right here this comment at the start of the function to tell the llm when and how to use this tool specifically so we describe the tool and then also give the argument that it needs to provide whenever it

**[0:11:24]** calls this tool because it has to pass in the user query and so first of all we're going to use our Vector database to do a similarity search with our user query and we're returning the top three relevant chunks of information that we stored in our knowledge base and then

**[0:11:39]** we're going to just create a nice formatted string here to feed into the llm which this is not going back to our faster llm right away we are going to be putting it into R1 to extract the insights and so this is the prompt that we're going to be feeding into R1

**[0:11:54]** essentially just giving it the context and the user's question and getting the answer back and we're even add adding in a little bit here saying that if there isn't sufficient information we can actually return back to our primary llm a better query for it to go through this

**[0:12:09]** Loop because we have that with small agents to then try again with a better query for rag so we're already getting some kind of outof the-box power here that's more than just simple one-hot rag it's really a gentic rag because our one is able to work with this other model

**[0:12:25]** and even tell it how to give better queries to actually search the vector database better so it's really cool how even with something simple like this we're starting to see a little bit of power and you could easily see how you could extend this to do so much more to

**[0:12:39]** make a really really robust agentic rag setup and so we just call our Reasoner like this with small agents it's so easy it's our model. run we give it the prompt and then we're saying reset equals false because this is how we keep the conversation history going so that

**[0:12:54]** it can continue to Reason Not only about this current prompt that was sent into it but also previous prompts and what it retrieved from the vector database earlier on as well and then we just return the response to our primary llm which by the way that is what we're

**[0:13:09]** setting up right here so our tool model as in our primary llm we get the model and then we create a tool calling agent everything looks very similar as before we're not passing an extra tools it is allowed three steps right here and then for the tools it's just an array with a

**[0:13:25]** single item because right now to keep it simple for a gentic rag we just have a single tool right here to use the rag with Reasoner and that is it that is all it takes to create that entire workflow that I showed you the diagram for you earlier and now to create the user

**[0:13:40]** interface with small agents it is a single line of code because they are integrated directly with gradio UI so that with this single line right here we can invoke the primary agent and this is automatically going to um actually apply the uh let me go back to this right here

**[0:13:56]** yeah so it automatically applies reset equals false to the primary agent so that we have full conversation history within the UI as well and then we just do launch that's it we already have a UI so now we are good to go we have our agent set up now I just want to really

**[0:14:11]** quickly show you how to create our knowledge base and get our llms downloaded locally and then we'll test it out so we just finished making our main agent using a knowledge base that we didn't actually have set up yet so I wanted to do that first that's the meat

**[0:14:24]** of what we're building here but I still want to show you my process here for getting our local knowledge based set up with chroma DB so I'm keeping it super simple with this local knowledge base that every time I run the script to load all these PDFs from my data directory

**[0:14:39]** right here it actually deletes the vector database entirely and then creates it again and reloads these PDFs so just keeping it very very simple you can add your own PDFs into this data directory if you want or just use these that I'll have in the GitHub repo as an

**[0:14:52]** example it's just fake data that's generated from cloud but anyway we use Lang chain here to load all these PDFs and then split them the chunks like you typically do with rag I didn't think too hard about how I was splitting or anything just again basic example and

**[0:15:06]** then we have our function right here to clear the vector database and then using the exact same embedding model that we used in our agent we're creating embeddings for all of our chunks and then putting it into our chroma database and so you can run this as many times as

**[0:15:18]** you want because it is going to clear the vector database each time before it inserts all the PDF so you're never going to have any duplicate data and so once you have all this set up and your PDFs in the data folder all you have to do is go into a terminal with this

**[0:15:32]** directory right here and then run the command python inest PDFs dopy it's going to be super quick it's all just running a local Vector database and it'll get all that knowledge set up for you that's going to be leveraged in the agent that we just built so the last

**[0:15:46]** thing to do before we run our agent is get olama and the models set up so I have instructions in the REM for how to do that this is actually a super important tip because olama models by default only have 2,000 48 tokens for their context limit which is super

**[0:16:03]** limiting it's not enough for most use cases and so these instructions actually show you how to turn your olama models into a version that has a larger context limit like 8,96 tokens for example which is much more fitting for most local LMS and most use cases and you can even Jack

**[0:16:21]** this number up to something like 32,000 as well if you are running a larger local llm that can support that many tokens in a prompt and so yeah follow these instructions basically you go into the AMA models folder right here and I have some of these already created for

**[0:16:36]** you as examples or you can build your own model file it's just two lines it's super simple for whatever llm that you want so you call this file whatever it doesn't actually matter this is just for your reference and then the first line it's from and then the ID of the model

**[0:16:51]** that you get from AMA like if I want to use deep seek R1 7B I'd copy this ID and then paste that in right here and then the second line you define the number of tokens that you want for the context limit now so 8,96 would just be my

**[0:17:04]** recommendation for these models that we are running cuz I want to be running 7 billion parameter version of Deep seek R1 distill and then 7 billion parameter of quen instruct for my primary llm that is not a reasoning llm so these two examples are already here for you and

**[0:17:19]** then going back to the REM you just copy one of these commands like I can copy this one right here and then you go into your terminal where you have this current directory loaded up and then I'll just paste in this command and it's super simple and if you don't have the

**[0:17:33]** model already from AMA it's going to download it for you right here and then create your version based on the model file and then if you have the model already downloaded it's not like it has to create another copy of it so if your model is 10 gbt it's not like it takes

**[0:17:48]** another 10 GB to have this version of it it's going to just use the exact same model that was already downloaded and then just add the configuration on top of it so you don't have to worry about it taking more space based on your hard drive or anything and now you have a

**[0:18:01]** version of the model like I can literally call Deep seek R1 7B 8K as one of my olama models now and if I do an AMA list you'll even see that here as one of the models that I have available and so it's just like any other AMA

**[0:18:15]** model now so we have that all set up now we can go into the environment variables and set these AMA models for our reasoning model IDs and Tool model IDs like I just go and I copy let's just say this one right here well actually I'll do the 7even billion parameter one and

**[0:18:29]** and then I paste that in as my tool model ID and then I just do the same setup for R1 7B and paste that here and that's actually the two models I'm going to be using for this demo which we'll see right now so I can actually show you

**[0:18:40]** myv file in this example because we are running everything locally so I have no API keys I deleted my hugging face API token I obviously tested that because I showed you that in the code as well but right now we are just using o llama so I have the 7 billion parameter version of

**[0:18:56]** distill R1 and then the 7 billion parameter version as well of quen 2.5 in truck so tiny models that still work really well with this setup especially because we have all the reasoning power of our one and then obviously increasing the context limits like I just showed you how to do because otherwise no

**[0:19:12]** matter the AMA llm we get a lot of hallucinations and so with that I'll go over to my terminal here and then run the command Python and then let's see R1 small agent rag. Pine so this is going to be using gradio UI which integrates right with small agents as I showed you

**[0:19:27]** to pull up our front end in just second and so it'll just be running locally right here this is an old instance that I had running so in a couple of seconds once it loads up the site I can just refresh and then we'll have a blank slate right here a new conversation with

**[0:19:41]** our agent and so because this is doing competitor analysis with all that fake data that I had in the PDFs in my data folder I'm just going to ask it this question right here compare and contrast of services offered by a couple of the companies in my chroma DB knowledge base

**[0:19:57]** this will immediately start the prompt right here with our primary conversation driver quen 2.5 7B instruct and right away it decides to use our rag with Reasoner tool which is perfect passes in the user question as the argument here and then all this context is what we are

**[0:20:13]** giving this is what we fetch from the vector database we give that to deep seek R1 to reason with and give us the final insights and something kind of weird that I see um with small agents a lot is it fails to parse the thinking tokens from these reasoning llms so you

**[0:20:29]** get this error here that you can actually ignore and it's kind of neat that you can really see all the thinking tokens it actually works out it's kind of weird though there's a lot of quirks with small agents that make me not like it a ton that's also why I want to do a

**[0:20:41]** more robust implementation with pantic AI and Lang graph um but anyway it still works and so we give the final answer back we have all the thinking tokens here and what it decided to give as a final answer back to our primary llm which then gives us the final answer

**[0:20:57]** here in the UI so look at this it even shows us in grade UI the different steps that it took and the parameters for function calls and execution logs and everything it's so cool then we got the final answer here and look at that this is so good and if we didn't get the

**[0:21:10]** right answer R1 would have actually told quen to go back and use this tool again and I see that a lot in my testing too so it's very much a gentic rag where it reasons with itself and it's also a gentic rag just because we're using entirely separate llm to handle the rag

**[0:21:24]** results as well so just absolutely fantastic in so many ways you can expand this as well just the whole idea of using R1 and other reasoning models like O3 mini now along with faster llms in a workflow it's just so powerful something that's really worth wrapping your head

**[0:21:41]** around so there you have it a super simple and effective agent rag setup with R1 and I really hope that this opens up the floodgates of ideas for you in all the ways that you could expand this simple use case here and that's what I'm going to be doing on my channel

**[0:21:55]** pretty soon here as well so definitely let me know if you're interested in that pantic Ai and L graap implementation I've got so many ideas around this and it's going to be a big project but I'm pretty motivated to get it done especially if I hear from you so if you

**[0:22:09]** appreciated this content and you're looking forward to more things AI agents and reasoning llms I would really appreciate a like and a subscribe and with that I will see you in the next video
