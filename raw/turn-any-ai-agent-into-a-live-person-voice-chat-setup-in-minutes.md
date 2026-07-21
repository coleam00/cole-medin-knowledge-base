---
type: raw-transcript
title: "Turn ANY AI Agent into a Live Person - Voice Chat Setup in Minutes"
youtube_id: L9JqdwdCiyE
url: https://www.youtube.com/watch?v=L9JqdwdCiyE
slug: turn-any-ai-agent-into-a-live-person-voice-chat-setup-in-minutes
published: 2024-11-15
duration: "0:16:24"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** something I haven't focused on enough on my channel is voice AI agents and a lot of you have asked me to implement voice with a lot of different projects on my channel and I get it it's super nice to be able to just chat with your agents like it's a person one of the biggest

**[0:00:14]** reasons I haven't focused on voice agents at this point is most platforms don't make it very easy to implement them but one of my favorite no code AI automation platforms actually does it really really well Vector shift and a lot of you have asked for more content on Vector shift after my last video on

**[0:00:32]** it so today I get the pleasure of knocking two birds with one stone for you in this video I'll show you how to build a full voice agent with a knowledge base from Google Drive in just a few minutes with no coding and you can deploy it to your own website Vector

**[0:00:46]** shift is similar to Lang flow flow wise n8n and other AI automation tools but there are a few key features that make it stand out for a lot of use cases and the capabilities around voice agents is definitely one of the big ones I love open source platforms like flow wise and

**[0:01:04]** NN that you can host yourself I use them all the time I'm going to keep making content on them in the future but I still come back to Vector shift for a lot of what I do and so I'm excited to share this with you now I'll even show

**[0:01:17]** you as I'm building out this voice agent how you can build pretty much any agent you want within the platform and we'll also use autod Dev at the end to build the front end around the agent that we make in Vector shift super exciting stuff so let's go ahead and dive right

**[0:01:31]** into it all right so before we dive into building a voice agent with Vector shift I just want to say really quick that the previous video for Vector shift on my channel is where I really dive into an overview of the platform and how to use all their different features like their

**[0:01:45]** knowledge base and their workflow Builder and the deployments and all that so check out that video I'll reference that right here if you're curious to learn more but right now we're just going to dive into specifically building a voice agent and talking about all the different features for agents with that

**[0:01:59]** so now I'm in the dashboard for Vector shift where I've got all my pipelines here and this is where I'm going to show you how to build a voice agent in just a few minutes and I'm going to do it completely from scratch the one thing that I'm going to use that's already set

**[0:02:11]** up is my knowledge base that I built on the previous video on my channel but these are really easy to build you just click on new give it a couple of options here fill that in and then hook in your Google Drive and then you can select any

**[0:02:22]** folder that you want to ingest into the knowledge base here and so for this knowledge base specifically I've got it hooked into my Google Drive and then if I click on this preview button here I can even see all the documents that are adjusted from the folder that I selected

**[0:02:37]** and I can select one of them it'll even give me the different chunks that are included here uh with the knowledge base so super super cool the kind of visibility that you get within what's in your knowledge base as well which I appreciate a lot so this is my knowledge

**[0:02:50]** base now we can go over to the pipelines and I'm going to make a brand new pipeline here from scratch and we're going to build our voice agent so I'll give my pipeline a name I'll just call it YouTube voice agent and now just like with any other automation tool you have

**[0:03:04]** to start with an input and so I'll drag in this input node here again in the other video on my channel I go into a lot more of these nodes in detail U but we just start with an input here and then right away you'll see how easy it

**[0:03:15]** is to integrate with audio all I have to do is Select this drop down here and go from text to audio and boom now the input into this workflow is audio and this is what allows us to integrate with the voice part of the vector shift platform that'll show after we build

**[0:03:28]** this workflow and obviously the next thing we have to do is turn this audio into text so we can feed it into the large language model and so conveniently named we have this multimodal tab and we have our speech to text node and so the input right here is going to go into the

**[0:03:44]** audio for speech to text there's a couple of options here for the model I just recommend using open AI whisper and now we already have the text version of the audio that was inputed into the workflow and so now we can go to the large language model Tab and I'm just

**[0:03:58]** going to use GPT 40 Mini for my model here so I'll go ahead and select that you can use your own API key if you want I'm just going to use some of the free credits that they give you when you start on Vector shift and uh what I'm

**[0:04:09]** going to do now is Define both the system message and the prompt so the system prompt is where you can Define the behavior of the large language model where you typically say something like you are a personal assistant blah blah blah and so I'll say you are a personal

**[0:04:24]** assistant who helps answer user questions to the best of your ability something just kind of generic right now as an example but this is where you define the behavior for your large language model aside from just what the user is prompting and so next up what we want to do is Define the user prompt and

**[0:04:42]** this is also where we're going to integrate with our knowledge base and I'll show you how to do that in a little bit as well now one beautiful thing with Vector shift is you can Define like right here I just have a single input into this node but you can Define

**[0:04:54]** parameters within these boxes here that give multiple different inputs available in this node and so let me just show you what I mean right here so I'll start by saying the user asked the question and now I want to have an input specifically for the text that we are getting from

**[0:05:11]** the speech to text here and so I'll use their syntax here which is with squiggly brackets so two s brackets and then prompt and then closing it out and then there we go we now have an input called prompt where I can drag the text into it and so then what I'll do is also add in

**[0:05:26]** the context as well so this is what we integrate with our knowledge base and so I'll say use the following context to help answer the question if applicable I don't want it to use the context if it's not actually related to the user's question but here I'll add another variable here

**[0:05:43]** and then boom we now have a second input into this node really really easy to set that up and so we can now integrate with the knowledge base which I'll get into in a second but first I just want to talk really quickly about how you could use really any agent that you want

**[0:05:57]** within Vector shift here and the way you can can do that is through the Integrations tab right here and then a couple other things that I'll dive into as well so there's so many different services that are available here to integrate in Vector shift just like with other platforms like zapier or NM and if

**[0:06:13]** there's an integration that's not available in Vector shift that you want to use that's available in something like zapier or make.com you can just use those Integrations set up a workflow there and then call into it within Vector shift and so you have everything that you need here and you can also

**[0:06:27]** integrate with other platforms like n8n because if I go to the data loaders tab there's an API node this gives you all the configuration you need to hook into any API endpoint so if you have a custom agent built with python you want to call instead of using the llm node here or if

**[0:06:42]** you have an NN workflow that's a web hook you can do any of that here and that's really the flexibility that Vector shift gives you to work with anything that you want for your AI agents and that's kind of what I was talking about earlier and so I could

**[0:06:54]** replace this node with a web hook call into an n8n agent for example obviously is going to be just a simple example where this works for me but I just wanted to show you really quickly how you can basically build anything that you want it's awesome and they even have

**[0:07:07]** like a logic tab here a lot of other different things you can do like they have a summarizer node just built in so you don't have to set that up yourself so so many things for convenience here as well which is why I love Vector shift so much so anyway going on to the

**[0:07:20]** knowledge base now I'll drag in my knowledge base node and then the query for this to figure out what documents I actually want to send into the large language model for context I'm just going to drag the textt output from speech to text and that's going to go

**[0:07:34]** into the query for the knowledge base and then I'll select the knowledge base that I showed earlier that I have set up already from the other video on my channel and then the result of this is going to go into the context for the large language model so if I ask what

**[0:07:46]** are the meeting notes from 823 it's going to find that document and send those chunks in as the context for the large language model super super easy to set this up and now the response the text output from the large language model we want to feed that into a text

**[0:08:03]** to speech node and so you have open Ai and then also 11 labs for this I'm going to keep it simple with open AI um but 11 Labs does give you a lot more voices and customization as well um but yeah I'm just going to take the response from

**[0:08:15]** here feed it into the text for the text to speech node and then the model I'm just going to use the default and same thing with the voice as well but you got a couple of options here which is pretty neat and then for the audio output now I

**[0:08:26]** want to feed that into my output node so I'll go back to General drag in output change the type from text to audio and now I can drag the audio in here keep in mind that you have to change the type to audio before you can even make this

**[0:08:40]** connection otherwise you'll drag it and it won't do anything so switch it to audio drag it in and now boom I'll zoom out a little bit cuz we have fully completed this workflow as promised in just a few minutes we now have a voice agent and so now with this workflow you

**[0:08:54]** can click deploy in the top right it'll save your workflow and now we can integrate it in a voice spot so it's a separate part of the platform that we'll dive into right now all right so now I am in the voice Bots section of the vector shift dashboard because this is

**[0:09:08]** where we can hook in the workflow that we just made with audio input and output into a voice spot that we can actually embed as a chat widget on our website or through an iframe as well so I've got my headphones on now because as we test this you're going to hear my desktop

**[0:09:22]** audio and I don't want there to be an echo so I almost never have headphones on when I record but I'm doing that right now for this demonstration here so I already have a voice bot set up here because there are a couple of more boring details I didn't want to set up

**[0:09:35]** on camera like setting up the icon and some of the text here um and this is actually hooked into a different agent that I made as I was prepping this video but to change it here I'll just click on the pipeline that's the workflow that we just built and here you can see that

**[0:09:49]** most of the pipelines I have within Vector shift are grayed out because obviously you required to have audio for your input and your output so this is the one that's currently used this is the one that we just made together now so I'll select this one and then I'll

**[0:10:02]** click deploy changes and then boom we now have a voice agent set up and all of these different customizations here are things that you can go through to change the UI of your embed so lot of options for customization here you can even take off branding if you want I'm just have

**[0:10:18]** it here because I appreciate Vector shift uh but anyway so many options that you have here which is awesome and you can change the uh the image URL as well this is a custom little bot icon that I uploaded so a lot lot of options for um your UI there and now once it's deployed

**[0:10:34]** if you click on the export button in the top right it's going to bring you to a link so I can actually open this as its own web page and that's what I'll test out in a second here and also you can protect the password or SSO off and then

**[0:10:47]** you also have the embed code right here a script tag if you want to have it as a chat widget or an iframe if you want it as a part of your website itself and that's what we're going to use in a little bit when I build a front end with

**[0:10:58]** autod Dev for my voice agent the other thing that I want to mention really quickly before we test it out is that Vector shift has incredible documentation on building voice spots really everything in general is documented super well on the platform that's one of the big big things I look

**[0:11:13]** for when I'm using a platform instead of just making things all myself is it has to have really good documentation and I'm sure that you appreciate that as well which is why I wanted to call it out really quickly here but anyway let's get on to actually testing out this

**[0:11:27]** agent and so right now it's a pretty basic voice agent that has its knowledge base based on my Google Drive and so that's what I'm going to be focusing on here as I test it out so let's go ahead and start this conversation so I'll mute it quick here so that I can talk to you

**[0:11:42]** before I talk to it so what I'm going to do here is I'm going to ask it a couple of questions and then I'm going to cut as it's generating the response because it's not the fastest that's something that I have a little bit of a gripe with

**[0:11:52]** it's a little slow to generate response compared to some of like the phone calling platforms like vapy for example uh but it still works really really well and it's not like it is a phone conversation so it doesn't have to be as fast but yeah so I'm going to go ahead

**[0:12:04]** and unmute and talk to it and let's just see what this thing can do hey so I'm just wondering uh what can you help me with I can assist you with a variety of tasks including one answering questions I can provide information on a wide range of topics including history

**[0:12:21]** science technology and more two research assistance I can help you find information or summarize topics you're interested in all right so I'm going to stop it there because it was saying quite a bit but now I'm going to dive into asking another question specifically with my knowledge base so here we go what are

**[0:12:38]** the action items from the 823 meeting notes the action items from the 823 meeting notes are one discuss the latest and greatest headphones two figure out how to use AI to get rich three bake 13 cookies for Mo the lawn you can view the full notes Here talk docs.google.com

**[0:12:58]** documents where b409 next9 all right so it started citing the source and it was really botching the URL also you probably won't want it to give the source but I could just include that in part of the prompt to not give the source as a voice agent so no issues

**[0:13:16]** there that was actually pretty funny though um but yeah I got it right so those action items were really silly but it is actually what I had in that document cuz I just made something silly as an example I've used that document for a lot of other videos on my channel

**[0:13:27]** as well but yeah this is working extremely well and so now what we can do is create a front end around this iframe here so that we can have this Vector shift voice agent on our own sites let's go ahead and dive into that with autod Dev all right so here we are within

**[0:13:41]** autod Dev our for Cab bolt. new which aims to be the best open source AI cing assistant out there and this is what we're going to use to build a NIC looking front end a simple front end around our Vector shift voice agent so I've got AMA running quen 2.5 coder 32b

**[0:13:55]** locally as the model to build this out I made a video on this model um for the last video on my channel so I thought it'd be cool to use it again here now my prompt is going to be very very simple I'll go ahead and paste it in I just

**[0:14:06]** wanted to build a vanilla HTML landing page um for this iframe here and to get this iframe I just went to the deploy section the export section of my voice agent in Vector shift and I copied this right here this iframe and the reason that I want it to be a vanilla HTML

**[0:14:22]** landing page is because the iframes don't actually work within the web container in bolt. new so you get an error saying that uh Vector shift. a failed to connect and so I actually have to bring it out of the web container into I just have this online HTML jss

**[0:14:38]** and CSS Editor called jsfiddle so I'll just take the code that's generated here and put it in this and then generate it so we can see it so just a a kind of quirky thing with the web container with bolt. new um but it'll still generate nice looking code for us that we can

**[0:14:52]** bring into the JS bidle so I'll go ahead and enter this in and it's going to go ahead and start creating the files for me so so I'm going to zoom through this and then come back once it is done generating the code all right so it successfully generated a front end here

**[0:15:06]** but just like I said it says that it refuses to connect just because the iframe gets blocked from running within the web container so it's an issue with bolt. new itself not autod Dev but like I said it's totally okay because we can take this HTML file that it generated

**[0:15:19]** I'll just copy all the contents of this and then dump it into my Js fiddle here so I'll click run and then boom there we go we now have our voice agent embedded into a front end and there's almost no styling for this because I didn't really tell it to do anything besides just have

**[0:15:34]** a little bit of a dark theme that we can see on the edges here but you could definitely take this a lot further and tell it how to embed this within like a whole landing page you want to make whatever that might be but sure enough we've got this conversation here we can

**[0:15:46]** go ahead and start it and it'll work just like it did within that web page that I showed earlier Vector shift just makes it so easy to build any agent that you need and I especially love its capabilities around voice agents because like I said at the start not a lot of

**[0:16:00]** other platforms make it easy to do that out of the box in general Vector shift just offers a lot of unique features things like analytics and other production grade stuff as well that you miss out on with other platforms and so I'd highly recommend checking out Vector shift and giving it a shot if you

**[0:16:16]** appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
