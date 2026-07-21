---
type: raw-transcript
title: "This Slack AI Personal Assistant is Better than a Real Person"
youtube_id: oMwipO6cmPQ
url: https://www.youtube.com/watch?v=oMwipO6cmPQ
slug: this-slack-ai-personal-assistant-is-better-than-a-real-person
published: 2024-10-04
duration: "0:12:24"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have had so many people reach out to me and ask about how to implement an AI personal assistant in slack and I get it there have definitely been times where I have spent a large portion of my day in slack working with a team or in a

**[0:00:14]** community so I totally get that it is really really valuable to have ai tools to boost your productivity within the platform it's funny because a few years ago when chat gbt was just starting to get popular I was a part of this slack community and the owners of this

**[0:00:29]** community were wondering could we use AI as a sort of FAQ personal assistant that would be able to automatically generate really good answers to commonly asked questions that are put in the slack channels and it's funny because this kind of rag implementation is now one of the most classic AI use cases so it's

**[0:00:47]** crazy that even three years ago people are wondering if this kind of thing was even possible but even though it is a classic use case having chat platform assistance is still one of the most crucial AI use cases for any business I've thought about implementing a slack AI assistant in a video and I might

**[0:01:04]** still do that in the future but since it's such a classic use case it doesn't really make sense to reinvent the wheel especially when you have platforms out there that make it so easy to do this like run Bear Run bear makes it so incredibly easy and affordable to create

**[0:01:19]** your AI slack assistant or multiple assistants for that matter and you can also use other platforms besides slack like Discord or teams your slack chatbot can have have rag functionality the ability to search the web it can invoke custom tools summarize slack conversations and channels and the list

**[0:01:38]** goes on you can also invite your assistant to only specific channels in your slack workspace and so that way you can limit which chats are exposed so as long as your entire slack workspace isn't filled with sensitive information there is a place for you to use run bear

**[0:01:53]** to boost your productivity in slack I honestly don't know a single person that wouldn't benefit from having an AI personal assistant in their favorite chat platform so allow me to show you how easy it is to do it with run bear so to get started with run Bear all you

**[0:02:07]** have to do is go to run bear. I'll have a link in the description and then click on this get started button you'll go ahead and create your account and then you'll be brought to a dashboard with a free tier where you can play around with run bear for a few messages and see if

**[0:02:19]** it is right for you and if you want to move forward with using run bear longterm I also have a discount code in the description and a pinned comment so feel free to use that I don't do collaborations very often but run bear is a platform that is worth me bringing

**[0:02:33]** to you because it makes it so easy to build personal assistance in your favorite chat platform and as I go through it I think you'll see how valuable it really is and so once you're signed in and brought to your dashboard you can see that it is really really

**[0:02:46]** nice and simple let me go to the overview here first of all and there are just two tabs that I want to focus on in this demonstration we have the assistants and then the Integrations and so the Integrations is where we're going to be setting up our connections for

**[0:02:59]** things like like our knowledge base and slack and then assistance is obviously where we go ahead and create the bot that we invite into our slack workspace and so for Integrations here you can see there are a lot of different channels that you can connect like I mentioned

**[0:03:13]** earlier and then for your knowledge base you can use Confluence Google drive or notion I've used Google Drive a lot in my other videos so mixing up and using Confluence today it is really easy to connect all these platforms for slack there's just a simple OA flow you have

**[0:03:28]** to go through and then for confluence there's even documentation that gives you on how to create an API key put it in here to get that connection set up and then for the rag demo today I've got just a single document here just AI generated research for a AI application

**[0:03:44]** text stack and so this is what I've got right here for Rag and so we'll see that in a little bit when I ask questions when we get the bot in slack so now we can move on to creating our assistant in run bear so I'm here in the assistance

**[0:03:55]** tab now back in the dashboard and I'll click on ADD assistant and the first really amazing feature that I want to call out here is that sure you can just use a base model if you want to and that's what I'm going to actually do in the demo to keep it simple but if you

**[0:04:08]** want you can use an existing Ai and this is just so cool I've never seen this on a platform before besides run bear I have seen custom gpts before but even that is cool but what I've never seen is you can actually create a custom AI agent with Lang chain and Lang serve and

**[0:04:23]** then connect that in Runar and they have their own python SDK you can develop custom AI in Python and then hook that into your run bear assistant as well that is just so so powerful so for now I'm just going to use an open AI assistant but yeah I'm definitely going

**[0:04:39]** to be using that in the future um and then I'm actually going to go back to my assistant that I've already made just so that I can walk through step byep everything that I did and not have to type it all out for you again so I'm going to click edit on this assistant

**[0:04:51]** here I've got a name that I've given it slack assistant with knowledge base and then the instructions this is where you tell the agent how to act you can tell the assistant the behavior it has how to format its responses all that good stuff and so I just gave something very

**[0:05:06]** generic here as an example just telling it that you're going to receive knowledge through Rag and use that to help you answer user questions you can also select your model basically anything that's available uh with GPT and then you can add your external knowledge Source this is where I added

**[0:05:22]** Confluence so I selected Confluence here and then I just copied the URL of my Confluence document and put it in let me go right here I put it in right here clicked add and then it ingested it as the PDF and now I have that available as knowledge and so I'm going to later once

**[0:05:38]** we're in slack ask it a question that it could only answer if it has the information from this document right here and so going back now we get to all of the actions and this is another really really cool feature of run bear there's so many actions that are baked

**[0:05:53]** right into the platform so you don't have to set up anything custom so image interpretation image generation that is really cool school um a current date as well cuz a lot of times llms don't actually know what day it is that's kind of important for um you know time

**[0:06:06]** sensitive questions like it says here the ability to search the web we're going to be testing that out as well it can fetch information from a URL so basically doing web scraping it can search slack conversations so it can summarize conversations in specific channels and then finally this is

**[0:06:22]** another really cool feature is you can add custom functions using the openai specification for function calling here so just like you would do function calling in your custom agents when you're just querying GPT in Python you can set up that kind of Json right here and have it really perform any action

**[0:06:40]** you could possibly want so that is really really cool just how how basic run bear can be but also how extendable it is to do whatever you need it to do as your personal assistant and then there's also a lot of advanced options as well I'll leave all this as default

**[0:06:54]** but there's so many things you can play around with if you want to really fine-tune your assistant for ex exactly how you want to respond um and so with that you can go ahead and click create in my case it's just update and then we can go over to slack and actually invite

**[0:07:08]** this in and play around with it and so what I'm going to do is go to the channels here and I'm going to connect it to a new channel so this is what you'll do for the first time you set it up I'll select my channel here of Kaya

**[0:07:20]** Fitness and then for the slack Channel I'm going to use YouTube run bear assistance this is a brand new Channel that I have created for this demonstration a here and so I'll go ahead and click next and then there's a lot of different ways that you can actually trigger your Bot so it's not

**[0:07:36]** necessarily going to respond to every message that you put in this channel which is really good because sometimes you want it to just kind of be in a side car they're ready to respond when maybe you would have a specific keyword or a certain Emoji there's a lot of options

**[0:07:49]** here so what I'm going to do is I'm going to have it trigger just when you mention at run bear just like you would add a user in slack so I'll go ahead and click create and there we go so now all I have to do is invite run bear into this channel so

**[0:08:02]** I'm going to go into my slack now here in my YouTube run bear assistant slack Channel and what I want to do is invite run bear into this channel specifically so I'll click on the members in the top right go to Integrations click on add an app and then select run bear and then is

**[0:08:17]** all it takes boom we now have run bear in this Channel and we can go ahead and chat with the assistant that we just created it is that easy and so I'm going to start with a rag question because that's going to be one of the most common use cases for a personal

**[0:08:30]** assistant in any chat platform so I'll say Runar and I'll say what is the text stack that I am researching and what it's going to do is acknowledge my question and then immediately tell me in the thread here that it is processing my request and each thread is going to be a

**[0:08:47]** separate separate chat memory just like you would have a separate chat memory for each chat in chat gp.com so you can kind of compare a thread and slack to a conversation in chat gbt and there we go we got a perfect answer from run bear here based on exactly what I have in my

**[0:09:04]** Confluence document so this is looking really really good and so I can even ask it a followup here to test another tool for the assistant I can say search the web to determine the pricing for each and so now it's going to take a little bit longer because it's going to search

**[0:09:20]** the web for grock pine cone superbase olama but it's going to get a response back to me actually going out to the intermet just like I asked cuz it's not going to have this information by itself and there we go it's starting to format the response this is looking really

**[0:09:34]** really good and boom all right yeah super base with a Pro Plan at $25 per month uh yeah $70 cheaper per month compared to Pine Cone because yeah the starter is $70 for pine cone the starter tier so that is looking good and then yeah pricing for Gro all right I don't

**[0:09:50]** know if this is like entirely accurate but I definitely did go out to the internet I think this is accurate so this is looking really really good um yeah I love it and so it's also using conversation history obviously cuz it had to know what it told me in the

**[0:10:02]** previous message in the conversation about services to then look those up um so yeah awesome another tool that it has that I want to showcase is the ability to summarize slack conversations so I have this channel right here that I used in another video on my channel where I

**[0:10:18]** basically was just talking about uh troubles with creating an AI pet startup just something silly and random so I added run be into this channel as well so it has the ability to read this conversation and now I can go back to my other channel that I'm using and I'll

**[0:10:32]** say at run bear summarize the conversation in the YouTube channel and I'll say take in all comments just so that it's taking in everything for its summary and so just like before it's going to open up a new thread brand new chat history here and we'll see it's

**[0:10:49]** going to start pulling the messages from this channel here and giving me a summary and this is a really important use case for personal assistance in a chat platform because a lot of times you're going to have a bunch of different conversations going on when you take a step away and then you come

**[0:11:03]** back and you don't want to read through 30 messages that all have a bunch of different threads on them too and so this is just really really convenient and can save a lot of time and there we go it gave us a summary talking about the startup technology needs it's a

**[0:11:16]** little bit long so I can say make it more concise but this is looking really really neat and so I'll get even more concise summary it'll spit out in just a few seconds and now I saved myself having to read a bunch of messages um so yeah there we go almost there and boom

**[0:11:31]** all right more concise I like it this is working perfectly so we've tested out all the cool tools and you can just see how easy it is to make a really powerful bot a personal assistant in slack that can save you a ton of time so that is

**[0:11:44]** everything that I have for run bear today I hope you can see how valuable a platform like this is even me as someone who's Technical and can maybe develop something like this I don't want to reinvent the wheel when there's something as powerful as run bear because in the end even though it's a

**[0:11:59]** classic AI use case there's still a lot of work that goes into making a personal assistant that robust with all those tools and the ability connect to all those platforms so I love it I'm going to be using run bear continuously in the future as well for my business and I

**[0:12:15]** hope you will too if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
