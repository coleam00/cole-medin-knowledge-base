---
type: raw-transcript
title: "I Built a FULL RAG AI Agent with No Code in 4 Minutes with VectorShift"
youtube_id: ieLdMih5_V0
url: https://www.youtube.com/watch?v=ieLdMih5_V0
slug: i-built-a-full-rag-ai-agent-with-no-code-in-4-minutes-with-vectorshift
published: 2024-09-27
duration: "0:10:07"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** there is a spectrum with two very opposite ends when you develop AI agents on the one hand sometimes you have a very complicated need with super specific requirements so you have to go so far as to code your AI agent from scratch and pour a lot of time into it

**[0:00:16]** but on the other hand it's really really common where your use case is pretty simple or you just want a fast proof of concept in that case it doesn't make sense to pour all the time to just reinvent the wheel when there are platforms out there that require just a

**[0:00:30]** small investment and save you a ton of time so today I'm going to show you how to use one of these platforms to build a full rag AI agent in just minutes that's nice and simple and still powerful and the platform that I'm going to use for this is Vector shift Vector shift is a

**[0:00:46]** drag and drop component workflow Builder kind of like n8n to compare it to something else I cover a lot on my channel but it focuses a lot on AI and it makes it so easy to build powerful robust and simple AI agents just like I'm going to show you and there have

**[0:01:01]** been a lot of people that have mentioned to me that they use Vector shift and like it and I even had some people ask me to make a video on and so I'm really excited to bring this to you today something nice and simple that you can use for proof of Concepts or even take

**[0:01:15]** Vector ship and extend it far because it is a platform that has a lot of power behind it so I'm just going to focus on something simple right now with it but you can take this a lot further as well so first of course I want to show you

**[0:01:27]** how to get started with Vector shift and then we can dive in to creating that rag agent and so it's really easy all you have to do is go to Vector shift. click on get started and there's a nice free tier for you to create your first knowledge base for Rag and then your

**[0:01:42]** first workflow as well and I just want to say that I haven't covered a lot of platforms like this on my channel before but I really think that there is a time and place to use these especially because of the convenience and the speed of developing agents that it gives you

**[0:01:56]** and so once you're signed in you're going to have a dashboard view that looks like this and there's a lot to offer here but I'm going to just focus on three of the main components here that we need we have chatbots knowledge and pipelines and so chat Bots is what

**[0:02:09]** I'll show at the end for how we can actually integrate our agent into a website the knowledge is how we are going to set up a connection actually to our Google drive to ingest Google Docs as our knowledge base for Rag and then pipelines is where we create workflows

**[0:02:24]** which don't actually have to be AI but of course in this case I'm going to use AI in a workflow so that we can have our chatbot and so to start what I'm going to do is go to knowledge and we're going to add a Google drive folder for our

**[0:02:38]** agent knowledge so start the timer now because I am officially getting started building this agent I'll click on new in the top right and then for the name of this knowledge base I'll just call it test KB and then I'll leave everything else as the same you can play around

**[0:02:52]** with the chunk size or the embedding model all that good stuff um but honestly the default is good for what I'm building right here and then I can pick how I add my documents to the knowledge base you can upload scrape your url uh or do what I'm going to do

**[0:03:05]** here which is add an integration I already have my Google Drive authenticated and so I can just click on Google Docs right here click into and then select the folder that I want to add to my knowledge base so this is just this meeting notes folder that I have

**[0:03:17]** here with some fake meeting notes I've generated with GPT that I've used in some of my other videos and so once I add that you can see boom in just seconds it added all those documents as vectors into my knowledge base and I can go over to my pipelines now and

**[0:03:31]** integrate this for a rag agent so I've already got some pipelines here but I'm going to create a brand new one because I want to create this from scratch so that I'm actually building this and not just using a template and so the first thing that I want to do that you will

**[0:03:44]** typically have as the start of any workflow in Vector shift is the input component so I'll add that in zoom in a little bit and then for the field name I'll just call it input and it's of type text and then what you can do is drag this input kind of like what you do in

**[0:03:58]** n8n so you drag the output into the input for another component and so what I want to do for this is I want to use an llm and so in my case uh I'll just pick anthropic right here because I really like Claude 3.5 Sonet so I'll even select this right here for my model

**[0:04:15]** and then what I can do is drag the input into the prompt or even better what I can do is I can add a custom variable here and so this way I'm going to add a variable actually let me let me do it this way I'll say input like this and so

**[0:04:29]** I can drag input to input and so the reason I want to do that is because I actually want two variables in the prompt I want the input and then also the context from Rag and so I'll say answer the question using this context to help and then in this case I'm going

**[0:04:44]** to have another variable called context that will add in a little bit when we interact with our knowledge base and then for the system prompt I'll just say you are a helpful assistant who answers questions to the best of your ability you can kind of put whatever you want

**[0:04:59]** here the I don't have to be super picky so that is that and then the next thing that I want to do is add my knowledge base so I'll go to the knowledge base tab in the top left and then drag in knowledge base and so in this case it is

**[0:05:11]** a reader that can read from any of the knowledge bases that you have set up within Vector shift and so for this I'm just going to select the test KB that I made for this demonstration and the input is going to go to this as well so it's going to be the query for the

**[0:05:25]** knowledge base so if I ask what are the action items from the 823 meeting that is going to be looked up here and the results I will feed in as the context for the llm so it can answer the question and you can also use your own API key for clot if you want because the

**[0:05:42]** free tier is just going to give you a little bit of credits to work with these llms and then you'll need your own API keys so just keep that in mind um so yeah now we got this all hooked up and the response I just want to send to the

**[0:05:53]** output and so I'll drag this over right here and I'll just call the output output and again of type Tex text and you can even do multimodal stuff with rag or just with LMS in general it's really cool the different outputs you can have here uh things you can do with

**[0:06:08]** Vector shift again I'm just doing something nice and simple here but Vector shift is very robust and you can take your agents and workflows really far with it so with that we have completely created a rag AI agent in under five minutes incredible and the last thing that we really need to do

**[0:06:23]** here before we can deploy this thing is test it out quickly to make sure that it works and that is very easy to do in vector shap so all I have to do is click on deploy changes after I did everything in the top right here and then I can

**[0:06:34]** click on run pipeline we got all of our inputs and outputs on the right side which is why I move my face to the bottom left and now here is where I want to input something that I know the llm could only answer if it has access to my

**[0:06:48]** documents in my meaning notes folder and so I'll ask it what are the action items from the 8:23 meeting and my responses that I get with Vector shift are so so fast and you can also see how long it took to run each of these nodes as well and boom

**[0:07:05]** yeah just in seconds we get the answer including the full retrieval and So based on the contacts provided the action items are and then here we go we got these four silly things that look like they're totally random but this is exactly right so if I go to my 823

**[0:07:20]** meeting notes in my meeting notes folder this matches exactly so this thing is working perfectly now for deploying this AI agent now now that we have it fully created and validated we can do this with the publish option in Vector shift is so easy to do this you just go up to

**[0:07:38]** the export pipeline in the top right and then you can export as an automation chatbot search or form I'm not going to go into all these details for each of these right now but just know that there are so many different options and if I click on chatbot here I can name my

**[0:07:52]** chatbot and just say test chatbot and then create chatbot and then boom we now have this assistant that we can message on the right hand side customize a bunch of stuff on the left and then when I export it in the very top right we can have this as a URL we can have it as an

**[0:08:09]** API if we want to use this within a custom front that we develop or we can even connect it to slack which is super super cool so I'm not connected to slack I'm not going to dive into this right now um but that's also really really neat to have this fully integrated

**[0:08:22]** within slack as kind of like a personal assistant and the other thing that I want to mention with Google drive here is it is constantly syncing with the FES that you delete create and update within that folder so it's really really a robust implementation it's not like you

**[0:08:36]** have to manually add things into the knowledge base in the future that folder is constantly in sync if you are curious about getting started with a vector shift and building these kind of Agents just know that it is really easy to do so there are even a bunch of templates

**[0:08:49]** out there for you already if you want to get started without having to build a workflow from scratch so if you click on new to build a new pipeline you have all these examples right here that you can just load straight into your pipeline collection and add in your own

**[0:09:03]** credentials do whatever you need to customize it and so there's something like a Blog article generator template as one example this one's really really cool um it's quite robust and they even have like little documentation around here just to help you understand what's going on but yeah a lot of it revolves

**[0:09:18]** around the llm generally but in this case it's really cool cuz it's actually using an llm twice so it's like multiple different agents that are working together here to generate a Blog article so yeah just to kind of show off the templates really quick it is so easy to

**[0:09:30]** get started with any kind of agent that you want to build in Vector shift so that wraps up this simple yet effective rag AI agent with Vector shift I really do think like I said at the start of the video there's a time and place to use platforms like these so you aren't

**[0:09:44]** Reinventing the wheel I had a ton of fun building this agent I'm definitely going to expand it in the future and continue to use platforms like vector shift when the time is right for me to not code something completely custom there's a time for that as well but it's gruesome

**[0:09:59]** and so if you pre appreciate this content I would really appreciate a like and a subscribe and with that I will see you in the next video
