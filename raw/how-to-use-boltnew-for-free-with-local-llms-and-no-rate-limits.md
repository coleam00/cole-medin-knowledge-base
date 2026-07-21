---
type: raw-transcript
title: "How to Use Bolt.new for FREE with Local LLMs (And NO Rate Limits)"
youtube_id: 8ommGcs_-VU
url: https://www.youtube.com/watch?v=8ommGcs_-VU
slug: how-to-use-boltnew-for-free-with-local-llms-and-no-rate-limits
published: 2024-11-06
duration: "0:16:10"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** recently we as a community started autod Dev a for bolt. new that aims to implement a bunch of much needed features including being able to use any large language model like local ones with olama bolot new itself only supports using one llm Cloud 3.5 Sonet but so many people want to use local

**[0:00:20]** llms especially because with them you never have to pay a dime or hit those nasty rate limits ever again and that's why adding the ability to use other large language models is the first thing that I added to autod Dev and today I'm going to give you some tips and tricks

**[0:00:35]** for using local llms to build your full applications for you and together we'll build an application within autod Dev using a local llm to chat with an AI agent that I have built in n8n and the best part is we're going to be using a smaller model Quin 2.5 coder 7B to

**[0:00:53]** create this full application and it actually does really really well and this kind of smaller model can really be run on almost any computer to go along with this this Sunday November 10th at 700 p.m. central Time I will be doing a live stream on my YouTube channel I am

**[0:01:08]** super pumped for this and the reason I'm mentioning this here is because I'm going to take the application that I'm about to show you how to build with quen 2.5 coder and take it to the extreme by building it with 25 different llms you heard that right 25 different large

**[0:01:24]** language models 10 of them through apis and then 15 of them that I've installed on my computer with Ama so I can see what kind of power I can really get with unlimited usage for free on my machine I am not going to sugarcoat the fact that you still will generally get the best

**[0:01:39]** performance with massive close Source models like clad 3.5 Sonet and gbt 40 but hitting those nasty rate limits sucks and so I really want to test out other llms For You especially local ones to see what kind of power we can get and so this video is in a sense a teaser for

**[0:01:56]** my live stream on Sunday where I'll be doing that with a bunch of different models but I also do want to take the time right now to give you some very key tips and tricks for getting the most out of your llms and working with autod Dev and really just bolt. new and other AI

**[0:02:09]** coding assistants in general so let's go ahead and dive right into it all right so here we are in the readme 4 autod Dev now this tutorial that I'm about to show you with using local LMS and tips and tricks for that that assumes that you already have autod Dev up and running on

**[0:02:23]** your machine if you don't yet this read me which I'll have a link to in the description of this video has very good instructions on the full setup and also how to run this both with Docker and without Docker and there's even a video on my channel that I'll link right here

**[0:02:38]** where I show how to get everything up and running with Docker including installing olama and getting your local llms on your machine with that and so definitely check that out if you haven't already if you don't have it up and running but if you do now we can dive

**[0:02:51]** into what it looks like to run things with local llms cuz I got a couple of very important tips and tricks for you to make it work really really well no matter what you are going to develop all right the first big tip for using local llms with autod Dev is you want to avoid

**[0:03:08]** the issue where the model doesn't actually open up the web container and create the files within that what do I mean by that we'll just check this out right here I'm running the Bas quen 2.5 coder without the fix that I'm about to show you right now and if I have it

**[0:03:22]** create an app Watch what it does it just has a regular chat window here it doesn't open up the web container with all the code and the preview for you and so it's kind of useful here cuz it's creating good code but there's no magic of bolt. new here this web container

**[0:03:38]** which I open up manually just now is completely empty there's no preview we basically could have just chatted with AMA within the terminal and gotten the same results here so not very great but there's an easy fix for this and the reason this problem happens is actually because of something pretty silly with

**[0:03:54]** olama for some reason the default context length for any olama model is 248 tokens and that unfortunately is not big enough to fit the bolt. new prompt so you squeeze in something and it loses some of the context and that's why it doesn't understand how to interact with

**[0:04:11]** this web container but luckily with AMA there is a very easy way to create a slight variation of any model you want that has an increased context length and you can use that along with any other model that you pulled from olama and that's what I'm about to show you right

**[0:04:26]** now so I'm back in the read me because I already have a section on how how to do what I'm just about to show you right here so super important note on running AMA models and this has the instructions on how to create a slight variation of any olama model that has that increased

**[0:04:41]** context link so that it magically Works a 100 times better within bolt. new I've tested this myself with multiple different models and it really does do do the trick of fixing this huge issue and so all you have to do is create a file called Model file or it can really

**[0:04:54]** be any name at all and I'll show you an example in a little bit here and you just put in these two lines and so it's from and then the model ID of your olama model that you want to use within autod Dev and then the parameter for the

**[0:05:07]** number of context that is where you define the new context limit and so as long as you do something above 8,96 because that's the default limit for bolt. new you are good to go so this number doesn't specifically have to be 32,768 but that's just what's recommended in general when I did some

**[0:05:25]** research on this earlier and so you add this into your model file and then all you have to do is run this Command right here and like I said I'll show you an example right now so within my model files folder that I have here in my bolt. new repo you'll have to create

**[0:05:38]** this yourself I'm not pushing it into GitHub I have this file right here called quen 2.5 coder and so the model ID specifically for me in this case is quen 2.5 coder 7B because that is the AMA model that I want to increase the context limit on so I have that set up

**[0:05:55]** right here in this file and then I have a terminal right here where I'll just run the command create - F and then my file is called Quin 2.5 coder and then the name of the model that I want to give I'm giving like essentially a new model ID in ama I'm just going to give

**[0:06:09]** it the exact same name but with autod Dev as a part of it so I know that this is a model I can use for autod Dev so I already have this created actually so if I do an AMA list you can see all my models here and just like all them that

**[0:06:21]** I pulled from AMA I just have this one sitting alongside it right here quen 2.5 coder autod Dev 7B all right so you'll run that and then when you go into into your bolt. new instance let me go and create a new chat here and select AMA the model is going to be available just

**[0:06:36]** like any of the other ones that you pulled and this one if I select build it Todo app and react you'll see right away that it is working way way better it opens up the code window it's creating package.json within the web container everything's working just like it would

**[0:06:51]** with Cloud 3.5 Sonet or those larger models because we now have the right context link the sponsor of today's video is flexis spot and this wonderful chair that I am sitting in right now out of all the AI platforms I could have showcased like I usually do I chose

**[0:07:05]** flexi spot something kind of different for a personal reason for the past couple of years I've dealt with sciatico which is very very painful I would not wish it on my worst enemy and one of the biggest reasons that I got it is because I was sitting for hours and hours every

**[0:07:21]** single day with not the best posture and not the best chair for years and that does a number on your back having an ergonomically correct wrecked chair is super important for your health so if you are sitting in a chair for hours and hours with your day job I would highly

**[0:07:37]** recommend getting a good chair protecting your spine and flexi spot is one of the best chairs for that so I'll have a link in the description to get the chair if you use the code c750 at checkout you'll get a $50 discount and flexxip poot is doing a Black Friday

**[0:07:53]** promotion on November 13th and 17th at 9:00 a.m. where the first 20 customers have a chance to get their chair for free so definitely go ahead and check that out all right so before we dive into creating a full application with quen 2.5 coder 7B I want to mention a

**[0:08:08]** couple of really important things quick first of all what I'm about to show you here I'll be going pretty quick especially through setting up the n8n agent and getting that hooked into the web app but on my live stream this Sunday November 10th at 700 p.m. central Time I'll be diving into it in a lot

**[0:08:23]** more detail so come to the stream with any questions that you have on this or really anything on autod dev in general because I'd love to chat with you there the second thing that I want to mention is there's no getting around the fact that you will run into some issues with

**[0:08:37]** local llms that you don't with the bigger models like Claude and GPT and that's just the simple truth due to the fact that smaller models aren't able to handle the larger prompts of AI coding assistance not just autod Dev and so there's some issues that come up due to

**[0:08:52]** that and there's just so many requirements for creating all these files and organizing it within the web container but if you want a very good large language model that is still super super affordable and open source I would highly recommend using deepseeker version 2 the 236 billion parameter

**[0:09:11]** version you can get this either through open router or through the Deep seek API directly and this model absolutely kicks butt and let me show you why you'd want to use this over another model like CLA if I look at the pricing here in open router it is actually cheaper than even

**[0:09:28]** GPT 40 Mini by a little bit so 14 cents per million input tokens and 28 cents per million output tokens this is so much better than Claude because Claud is $3 for every 1 million input tokens and then $15 for every 1 million output tokens and so deep sea coder is like

**[0:09:48]** more than 20 times more affordable than clae and it's going to be something pretty similar for GPT as well so way cheaper and it's still open source and also the benchmarks for C coder version 2 are incredible as well so super good performance I would highly recommend giving this a shot if you want to still

**[0:10:08]** run autod Dev locally and not have to worry about rate limits on their commercial platform but have a good model that's going to get you through any kind of web app that clad would be able to as well so yeah I would highly recommend this and with that we can dive

**[0:10:21]** into creating with a completely local LM cuz there's still a time and place for that as well it's just so cool the kind of power we can have just running right on our machine and you you could run a deep sea coder locally as well 236 billion parameters is pretty massive so

**[0:10:35]** that's why I'm focusing on some smaller models here so let's go ahead and dive right into that all right so now we'll go through creating a full application as a fantastic starting point using a local llm I'm going to show you my big tip here which is to start really simple

**[0:10:49]** and iteratively get more complicated to avoid the most amount of hallucinations possible and make sure that you don't have something that's broken right out the gate the strategy actually works really well even with larger models like if you're using Cloud 3.5 Sonet on the commercial bolt. new this is still a

**[0:11:05]** good strategy to develop very complex applications by starting really simple and so I have a very simple prompt here to create a basic nextjs chat interface and I'm using my autod Dev version of quen 2.5 coder 7B that has that extra context link so we'll send this in and

**[0:11:22]** it'll start by creating a very simple application that's going to be pretty ugly at first but that's okay because it's going to be our starting point and then we'll get more complicated so I'll pause and come back once this is done all right so just like 15 seconds later

**[0:11:35]** and this app is fully complete and like I said it's going to look pretty ugly right now but let's see if it actually works pretty well so I'm going to say hi and then it said you said hi okay so it doesn't reply with a basic sample message it actually like repeats back to

**[0:11:48]** me what I said which that's pretty cool okay so super super simple at this point but this is now where we can iterate on it to make it something more complicated so I've got a second prompt here that I'm going to paste in and then this is where I start to get detailed with the

**[0:12:02]** UI and ux requirements and so I have things like colors defined specifically I want to describe to the llm how to design things to really make it what I'm looking for so you can give it things like colors and give it things like I need this kind of padding and these kind

**[0:12:17]** of measurements for My Views that actually helps a lot again even if you are using more powerful llms so if you know those kind of design details you can really guide it well so I'm going to send this in it's going to start making these improvements here and I will pause

**[0:12:30]** and come back once that is complete all right so it is complete and we now have a preview that is looking much much better as far as a chat interface go so I'll say hi and just make sure that everything is working yeah we even got like a little loading indicator here and

**[0:12:43]** then it sends a sample message this is looking fantastic all right so now what I want to do is just for demonstration purposes here I'm not going to make something super super complicated so I'm just going to iterate on this one more time and so I'm going to paste in

**[0:12:58]** another prompt here and it is actually going to be using an n8n agent API endpoint so that I can talk with an AI agent directly within my bolt. new application here so I'll even show you what I've got here so I have this n8n agent that I have built on another video

**[0:13:15]** on my channel and there is a web hook entry point here where essentially I have this production URL and I have this test header authentication that I'm going to delete once I finish recording this video so I just have it hardcoded into the prompt for autod Dev right now

**[0:13:31]** um but this is the entry point that talks to my agent that's hooked up with rag with a PG Vector database here and then I respond with the output I'm going to consume that here in my uh application that I'm building with autod Dev so I tell it this is your API

**[0:13:47]** endpoint I describe to it the payload it needs and the authorization and then also I tell it that the output field is going to be what I get in the Json that has the response from the llm to display to the user so I'll send all that in and

**[0:14:00]** we'll see if it can actually update the application properly to talk to my large language model over in my n8n workflow all right so interestingly enough it like messed up the styling completely when I prompted this last time here but I just had to tell it like hey you

**[0:14:15]** messed up the styling and then it corrected itself and it looks good again so now we can test it out and see if we can actually talk to a large language model now so when I say hi it shouldn't just give me a sample message it should actually invoke my workflow and there we

**[0:14:28]** go I got response hello how can I assist you today beautiful if I go into my n8n and go to the execution history sure enough just right now it is 350 my time I have this execution where it said hello how can I assist you today so this

**[0:14:42]** is looking wonderful and I can even ask it a question that would force it to go out to its knowledge base to answer so I can say what are the action items from the meeting I just have one meeting note here in my Vector database so I'll ask

**[0:14:56]** it and see what I get for a response here let's make sure that this is fully working with the N8 end workflow and sure enough it is this is the right answer I've been using this as an example for a few of my different videos so I'm very very familiar with what the

**[0:15:09]** right answer here and that is looking good all right so we have fully built out a really good starting point for a chat widget to talk to an AI agent NN super super cool stuff all using quen 2.5 coder a 7 billion parameter local llm with a llama so there you have it we

**[0:15:27]** have used a small local llm with autod Dev to create us a full project that is a very good starting point for us that we could easily take forward and turn into a production ready application and also I have other content on my channel for deploying these kind of apps I'll

**[0:15:41]** link one right here and also a lot more content coming out on autod dev including tutorials for things like how to contribute and more on how to deploy these kind of applications and work with Docker and things like that so a lot more content coming I am so excited for

**[0:15:55]** the future of autod Dev and how much it is enabling us to do especially with local llms if you're excited about that too and you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
