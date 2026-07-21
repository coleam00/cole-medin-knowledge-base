---
type: raw-transcript
title: "10 n8n Tips in 10 Minutes to 10x Your AI Automations"
youtube_id: Nsu9BzQv5C4
url: https://www.youtube.com/watch?v=Nsu9BzQv5C4
slug: 10-n8n-tips-in-10-minutes-to-10x-your-ai-automations
published: 2024-11-20
duration: "0:11:11"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** n8n is my favorite no code AI automation tool where you can basically build any AI agent you want and integrate it really easily with more than 500 different applications but there are some parts to the platform that I see people trip up with a lot so in this

**[0:00:16]** video I'm going to give you my top 10 tips for working with n8n in 10 minutes specifically focusing on the underutilized and trickier parts of the platform to make you 10 times better within n8n also we're going to be releasing a dedicated section for n8n in our automator Think Tank Community so

**[0:00:33]** stay tuned for that the goal here is to give you a ton of value really really quickly there are other videos on my channel where I dive into building out full workflows at n8n but here's going to be a little bit different we're going to go kind of fast so a lot of things to

**[0:00:46]** dive into let's get right into it all right my first couple of tips here are going to be more recommendations related to AI agents the first one being a lot of n8n tutorials for AI agents show using the windowed buffer memory for your agents check history and then the

**[0:01:01]** inmemory vector store for rag I would highly recommend not using either of these they don't scale as soon as you get users on the platform it won't work very well in production because these run in the memory of your n8n instance it is not very scalable what I'd

**[0:01:17]** recommend using instead and this is very very easy to set up is super base because there is a SQL database with postgress within super base and so you're able to use it for your postgress chat memory and then also there's an extend mention called PG Vector for embeddings for rag so you can use the

**[0:01:34]** superbase vector store so still one platform but it's going to be production ready and very very scalable super base is just amazing so this is my recommendation here tip number two a lot of people ask me what large language models should I use within my n8n workflows and the short answer is it

**[0:01:50]** depends a lot on your use case but I can give a general recommendation just so you can have something good and dive right into building your workflows so if I click on the chat model here we can see our different options what I would say is if you want the absolute best

**[0:02:02]** large language model right now I would choose anthropic and go with clae 3.5 Sonet if you need something that's absolutely fast and you don't need something that's super powerful I would go with Gro and go with a llama model and then finally for something that's very very affordable but still pretty

**[0:02:18]** strong I would choose open Ai and go with GPT 40 mini and then for the embedding model I would highly recommend going with text embedding three small for your model from open Ai and having that for Rag and then whatever model you choose here for your chat model I would

**[0:02:33]** also just use that for the model that processes your chunks from rag all right so the next few tips that I have here are going to be based around this rag AI agent that I built on another video on my channel the first tip being here number three is that you have to extract

**[0:02:48]** text from different file types with different nodes in n8n so if you want to extract text from a PDF document that actually has to be a different node compared to if you want to extract text from a text text document or a an Excel spreadsheet and so when you click on the

**[0:03:04]** plus icon to add and extract from file node you have all these different options here so you have to include all the ones in the workflow here based on the file types that you are going to be ingesting into your vector database and I go into detail for how to set up this

**[0:03:18]** kind of thing in that other video on my channel that'll have referenced right here tip number four how to work with previous node outputs in your current node and what I mean by that is if I click into the set file ID here I reference the file ID and MIM type

**[0:03:33]** output from the previous node right here which is the Google Drive trigger that I have and the way that you get this output on the left hand side is you just have to run a test execution by clicking on test step you'll have this output and now if I want to I can go and find the

**[0:03:49]** ID again drag it in like this and that's how it creates that expression to reference the value from the previous node and you're going to do this kind of thing in basically every single workflow but here's where people get tripped up this way of referencing a previous node

**[0:04:02]** only works for the node that was just ran so the one right before this node if you want to for example have download file reference a value two nodes back you can't just say json. file ID anymore you have to actually reference the name of that node so set file ID corresponds

**[0:04:24]** to set file ID that we see right here that's how you can reference that value if you do Json dot here it's only going to be able to reference these values from the previous node delete old doc records so that's the distinction between when you can use Json Dot and

**[0:04:40]** when you have to actually reference the name of the node tip number five when you are building AI agents within Ann a lot of times you want them to be an API endpoint so you can integrate them within other platforms like open web UI or custom python code that you've

**[0:04:54]** developed there's so many different platforms that you want to integrate with n8n and the way that you do that is through a hook node so you have this as an entry point into your agent but also it's nice to be able to test your agent right in the platform with this chat

**[0:05:09]** widget right here and the way that you can do that is by adding in the win chat message received trigger so if I just search for chat right here I have the chat trigger so you can actually have both at once and you just combine these together into this edit fields which has

**[0:05:24]** this specific JavaScript syntax right here to grab whichever value is defined so it's going to no matter which input it comes from get the right value like my latest message was high right here so essentially if chat input is defined I grab that value otherwise I get the body

**[0:05:41]** of the web request so this is the chat trigger this is the web hook trigger and it gets the value no matter which one is used so that is how you can set up your agent to be a web hook but also get to test it within n8n which is super

**[0:05:52]** valuable tip number six a lot of people do not handle looping properly within n8n when you have nodes that that can give multiple items in a single output like the Google Drive triggers for example you have to be careful about how you handle that so one important thing

**[0:06:09]** with n8n is it automatically handles looping in the sense that if a node outputs multiple items they will be processed one at a time for the next node but there are some important things to keep in mind with this because for example if you're trying to extract the

**[0:06:25]** text from a Google drive file and then send that into a large language model for example what are you going to do if there are actually two files that were created at the same time this workflow needs to be able to handle that so I'm going to go to an execution in my

**[0:06:40]** history to give you this example in this case there were two files that were created at the exact same time so there are two items in the output of this trigger node and I have to handle both and the way that I do that in this case specifically is after I extract the text

**[0:06:56]** from both files here you can see that two items are going through this enti ire pipeline I have this summarized node at the end that actually concatenates the output of both of these files together into a single parameter that I can then go on to the rest of my

**[0:07:11]** workflow giving to a large language model for example this is just one example but the main tip here is just be careful about how you handle multiple items in a single output in your n8n workflows you got to really think through that tip number seven is data pinning a very underutilized feature of

**[0:07:29]** n8n because a lot of times when you're in your workflows here you need to execute a test event so that you can have the output on the right hand side here to then see it as the input for the next node so you can drag and drop and

**[0:07:41]** reference these values dynamically but when I refresh n8n or Clos and come back I lose this so I have to execute the test event again which is really annoying but what you can do is if I click into the trigger here you can click on the pin data button in the top

**[0:07:56]** right and so that way this specific output is going to be there even if I do a hard reload so I'm going to save and then do a hard reload and we'll see that the pin data is still here and so now I don't have to execute the test event

**[0:08:08]** again so this speeds up development a lot as you're coming back to your workflows tip number eight is error workflows and this is super important for really making your na workflows production ready because you have to handle well when something goes wrong and all you have to do in n8n for that

**[0:08:25]** is create a new workflow with an error trigger so if I click on the add node option right here and then search for error I have this error trigger super easy to add in and I'll show how to hook this into another workflow in a second but you can do things here like for

**[0:08:39]** example send a slack message with the error details so that you know to go and handle whatever went wrong within your workflow and setting this up is really really easy So within another workflow that you want to catch the errors for like the last one I showed in tip number

**[0:08:52]** seven all you have to do is click on the three dots in the top right go to settings and then you can select a workflow that is triggered as your error workflow so I'll go tip number seven because that's the error workflow I just showed click save and then boom now if

**[0:09:07]** anything goes wrong in this workflow it's going to trigger that other one and send a slack message really useful for having production monitoring tip number nine is the schedule trigger a very underutilized feature of the N platform in my opinion because what it allows you to do is have workflows that trigger on

**[0:09:25]** an interval like every day or every hour on the half hour whatever rule you want to set up here you can make the workflow trigger at that time consistently and that's really important for things like generating reports like what I do right here I fetch all overdue tasks in a

**[0:09:39]** project in a SAA and then I send a slack message alerting that these things need to get done this is the kind of thing that you can't have event based there's nothing that happens in an app that would trigger this I just need to run this every so often at a set time and so

**[0:09:53]** a schedule trigger is perfect for that last but not least tip number 10 is the n8n workflow Library so this is over on the n8n site I'll have a link in the description to this but there are over a thousand workflow templates here that you can search through to find something

**[0:10:07]** to help you get started on whatever you want to make so I can search by apps or just keywords or even specific nodes for example like I want to have examples that use the superbase vector store node and then boom there we go we got a few examples here I can click into one and

**[0:10:21]** then even view it in their 8 end workflow viewer widget and maybe use this as a starting point for what I want to build and so I'm actually working on something behind the scenes which is going to be an AI agent that has this entire set of workflows in its knowledge

**[0:10:35]** base is sort of an NN expert so that's coming soon as well stay tuned for that but yeah this workflow library is fantastic I sincerely hope that this video has saved you a lot of headaches working with n8n it is a fantastic platform but definitely some tricky parts to it I'm also going to be

**[0:10:51]** releasing more content on n8n soon including using it for local AI projects and I'll make a big announcement once I've got the n8n section of the auto community so stay tuned for that if you're looking forward to that or if you just appreciated this content in general I would really appreciate a like and a

**[0:11:07]** subscribe and with that I will see you in the next video
