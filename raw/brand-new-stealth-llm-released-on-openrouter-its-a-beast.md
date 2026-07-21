---
type: raw-transcript
title: "BRAND NEW \"Stealth\" LLM Released on OpenRouter (It's a BEAST)"
youtube_id: nCzDnpWSiro
url: https://www.youtube.com/watch?v=nCzDnpWSiro
slug: brand-new-stealth-llm-released-on-openrouter-its-a-beast
published: 2025-04-03
duration: "0:14:42"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** we have some exciting news that is hot off the press for the first time ever open router is giving us a stealth model which they're calling quazar Alpha it's the pre-release of an upcoming long context Foundation model and what it means by Foundation model is this is one

**[0:00:18]** of the next big guys it could be GPT 5 Claude 4 Gemini 3 we don't know at this point because they're not saying which model lab they are partnering with but they are partnering with one to give us early access to the model which has 1 million tokens for its context length

**[0:00:34]** which is very impressive and it's specifically optimized for coding which is really important because in general coding seems to be the most important use case for AI and AI agents in general and it is fit for general purpose as well and the best part is it's available for free to use through the open router

**[0:00:52]** API right now so here is the page for quaz R Alpha on open router. I'll have a link to this in the description of this video you can use their chat room to have a conversation with quazar Alpha like you would with an interface like chat gbt domcom otherwise you can

**[0:01:08]** interact with quazar Alpha through the API if you want to use this llm in your AI agents in something like your python codes you just go to open router. sign in go to your keys and then create an API key and you can start using this model for free so what I want to do with

**[0:01:23]** you right now is figure out how good is this model I want to test it on a few things for building AI agents I want want to test it as an AI agent and then I also want to go in bolt. DIY and create an application with it and just

**[0:01:36]** see how fast and Powerful it is so first we have preliminary benchmarks already for quazar Alpha even though it was just released today so take these with a big grain of salt because the model is brand new we don't even know what the provider is yet and there could be a lot that

**[0:01:53]** changes between the pre-release and release of this model but it's still fascinating for me to do some initial testing and just culate things and I encourage you to do the same like let me know in the comments which provider you think this is maybe it's open AI maybe

**[0:02:06]** it's CLA and I'm curious your experience using it to test things like writing code and AI agents as well but as it stands right now for the general tests quazar Alpha is pretty close to qwq 03 mini and deep seek R1 it falls short a little bit but it still does rank

**[0:02:24]** slightly higher than Claude 3.7 Sonet so it's pretty impressive but then when we go down to the coding specific tests with python and Bash this is when it really starts to shine take a look at this it beats qwq 32b and it's almost as good as 03 mini and deep seek R1 which

**[0:02:41]** is really impressive especially because as you'll see later in this video this model is very fast compared to both of these more sluggish llms they're much bigger it seems like quazar Alpha is a smaller llm like maybe even closer to the size of qwq I don't know at this

**[0:02:59]** point it's all specul just based on the speed of responses that I'm getting but again it's really fun just to speculate test out this model see what we're getting ourselves into and who knows maybe the next couple of weeks the full release of this model will be available

**[0:03:12]** to us and then in the open router chat room I just wanted to play around with this model a little bit and see how fast it is and so I'm just going to select one of these preconfigured options for me for it to build a professional growth plan so I'll just click on this we can

**[0:03:26]** see how fast quazar Alpha is and boom look at this this is Lightning Fast definitely much faster than deep seek R1 and 03 mini doesn't seem like it's a reasoning llm which I didn't really expect it to be but it is really really Snappy and so speed definitely a huge

**[0:03:44]** Edge for this one compared to a lot of other llms now one really big bummer is that because it's a 1 million token context length llm I wanted to test it with a very very long prom so what I did I'll actually show you I took the full

**[0:03:58]** llms do text for Lang graph so it's all the documentation for this framework which is super super long you can see my scroll bar in the top right here it's massive and I went in back into the chat room and I pasted this in and then I tried to ask it to um based on this

**[0:04:15]** documentation create an AI agent send in this request and what it seems to do every single time is this should definitely fit within the 1 million token context length I mean this is definitely not a million tokens but I get an error every single time I have have a longer prompt so I think there

**[0:04:31]** might be something that's not fully working with this llm yeah cuz I get this 400 error right here whenever I try to do a longer prompt so it's kind of a bummer that I can't test like the needle and the Hy stack problem seeing how well it can pick out little bits of

**[0:04:43]** information from a massive promp so that's a bit of a bummer can't really test that but we can still move on to other things and see how powerful it is as an AI agent a AI agent Builder and within bolt. DIY to create front ends next up I want to do some coding with

**[0:04:59]** quazar Alpha we're going to have it build an AI agent using archon which is my free and open source AI agent Builder that I've been working really hard on the last couple of months and so I actually covered this in my last video on my channel I used Cloud 3.7 Sonet

**[0:05:13]** within archon to build an AI agent Army a bunch of agents that are all connected to mCP servers to do different things in my services like air table Brave fir craw it's like the ultimate personal assistant and So within my environment tab I already have archon set up where

**[0:05:29]** you connect it to any model you want in open router so I just changed the configuration uh for the open router connection to use quazar Alpha instead of CLA 3.7 Sonet for both my primary cating and reasoning models and by the way I'll have archon Linked In the

**[0:05:44]** description of this video if you want to use it yourself to build some really powerful AI agents with quazar alpha or any other model that you want and so back in the chat here to create an agent with archon I'll paste in the prompt that I used in my last video to build

**[0:05:59]** this agent army with clae 3.7 on it so I'll send it in and one thing that I noticed immediately when I was running this test a couple of times before recording this video is that it is blazing fast compared to clae 3.7 Sonic and that's kind of the theme of this

**[0:06:14]** video is quazar Alpha is pretty powerful it seems about on par with clae 3.7 Sonet but just looking at the terminal here how fast it's getting through the these requests it's at least four times faster than clae 3.7 Sonic which is super impressive it also probably means that it's going to be a lot more

**[0:06:32]** affordable as well because generally the faster llms end up being a lot cheaper like GPT 40 Mini compared to CLA 3.5 Sonet for example and so it's chugging along here it's creating that final code for my agent which is going to be pretty long cuz archon builds a lot for us and

**[0:06:49]** so in just a second we'll have everything pop up on the screen and usually this would take at least a couple of minutes with Cloud 3.7 son it so I'd have to pause and come back but in this case I didn't pause the video at all I recorded the entire time it

**[0:07:02]** took about maybe 30 seconds to a minute to to make this whole thing instead of multiple minutes and yeah look at this this is really really solid code I'm going to just scroll through this really quickly here to make sure that it set up everything right this looks about as

**[0:07:16]** good as what was created by Claude 3.7 Sonet so it didn't quite get all of the mCP server configuration right but neither did clae 3.7 Sonet so it wasn't a one shot for either llm so they seem about equal overall but this is really good looking code so I'm just going to

**[0:07:34]** iterate on this a little bit off camera just like I did with Claude 3.7 son it in my last video and then we can actually use this agent with quazar Alpha as the llm so we can not only test quazar Alpha as the agent Builder which did a pretty good job here but we can

**[0:07:48]** also use it as the agent itself all right it took two more tries to get the code in a working state which is exactly what it took with CLA 3.7 Sonet as well so I have it now in my file system up and running and I have it connected to

**[0:08:02]** my custom front end and since it is an mCP agent Army what we can do is ask it to work with a couple of our different services like Brave air table for our data storage and slack for our communication and so the first prompt that I'm going to give it is to search

**[0:08:19]** the web for the newest and best llms in 2025 and so that will require it to go out and use the brave API to get that information and then I wanted to take the top five the web search and add it to this specific table in air table and

**[0:08:34]** then finally send the results in a slack message and so it's not the simplest of requests here I'm requiring it to use quite a few different tools to accomplish all the tasks that I lay out for it in this single request and so let's go ahead and send this in I have

**[0:08:48]** quazar Alpha running for every single one of the agents here and so I have my terminal open just like I did with archon the first step it did it correctly it's calling the brave agent to query the best llms in 2025 and then it calls the air table agent to add this

**[0:09:04]** list into my table that I have open up right here and so in just a little bit we'll see it populate as the air table agent adds these records and boom like clockwork there we go we got the five records and now it's calling the slack agent to send a message summarizing the

**[0:09:20]** results and this is also very very fast compared to anything I've seen with this mCP agent Army before I was using GPT 40 Mini for my model for this agent and quazar Alpha is actually faster than even GPT 40 mini which is generally known to be one of the fastest close

**[0:09:40]** Source llms that's available to us right now probably only beat out by Gemini flash or maybe the models that you have through Gro or one of those providers that are super fast but yeah this is insanely impressive and it did everything perfectly it searched the web it populated the right table and it sent

**[0:09:56]** the message with the results from the search so this is working absolutely perfectly quazar Alpha is definitely impressing me both as an agent Builder and as the llm running the agent itself now the last thing that I want to do is test out quazar Alpha with bolt. DIY

**[0:10:13]** it's our open source AI coding assistant that allows us to build a beautiful front ends it's similar to bolt. new and lovable except we have access to pretty much any large language model that we want including any that are available through open router so without me even having to update bolt. DIY we instantly

**[0:10:30]** have access to quazar Alpha for free to build out our front ends and so for a nice and simple test that's still not super trivial I want to have it replicate an image of a landing page that I'm giving it and so this is my own landing page actually for dynamus AI

**[0:10:46]** Mastery it's an exclusive community that I just opened up the wait list for so if you want to transform your career and business with AI definitely check out dynamis doai and join the weit list there are limited spots available so get in on it now because the early adopter

**[0:11:03]** price is going to go away pretty soon after the community launches and so anyway that's dynamis AI I have a screenshot of the landing page that I sent into bolt DIY and I'm just telling it to make a landing page it looks exactly like the image that I attached

**[0:11:19]** and surprisingly a lot of llms do pretty poorly with this I mean the best of the best like Clan 3.7 Sonet and 03 mini for example they do pretty good but there's a lot that goes into copying something that looks exactly like this landing page and I don't expect it to get it

**[0:11:36]** perfectly but we'll see if it can lay out the general structure get some of that core text in there I'm going to give it a little bit and see if it can finish and so yeah looks like it created the page already so again like usual quazar Alpha is blowing my mind with its

**[0:11:50]** speed it didn't actually install the dependencies and run the project though so it messed up a little bit here I'll just say install the dependencies and run the project so it has to run those npm commands to kick everything off for us so we can actually see the preview of

**[0:12:05]** our landing page so I'll give it a second to do that and boom there we go this is looking really really good it's not centered here so it's not perfect but man this looks pretty close to the landing page and I can full screen it as well so you can see that yeah the video

**[0:12:20]** goes on the right hand side and there's obviously not a real video for it to put here which is why we get this error otherwise though it looks really really good and yeah I mean this this pretty much duplicated the UI exactly I'm super impressed and we can just test another

**[0:12:34]** one really quick here I'll just do something for fun I've got another quick prompt here to build me a beautiful chat application chat with an AI agent just with a placeholder message response right now but yeah I want a full chat conversation history a sleek and modern Dark theme design so let's see what it

**[0:12:50]** can spin up for us here and so it's going to start with the template here for a modern react AI app it's going to create app. TSX and wow yep already done all right so now it's installing the dependency so we don't have to ask it explicitly this time to do it and it

**[0:13:06]** started up and wow that was like 10 seconds and we have this conversation now so I can say hi and we get a sample response back it's got a really beautiful front end with a gradient for a background like wow this is this is amazing we created this in 10 seconds

**[0:13:21]** with quazar AI so I'm just really impressed overall so that is everything that I have for quazar Alpha right now seems like a very powerful llm overall and the speed is the most impressive part and if it sounds like I'm overhyping quazar Alpha in any way I don't mean to I'm just very passionate

**[0:13:39]** about AI so I'm really excited about everything that I am talking about but I do think that it is a very powerful llm it's maybe not going to revolutionize AI once it is released but definitely for use cases that need a good amount of power and a lot of speed it could be a

**[0:13:55]** game Cher because generally you have to sacrifice speed a lot when you want a lot of power with current llms like R1 and 03 but that might change with quazar Alpha I definitely foree that that's kind of my hot take big prediction out of this and I'm curious what you think

**[0:14:10]** as well I mean speculation right now is just really fun especially for the first ever cloaked model that we have on open router so what do you think the provider is for this is it open AI is it claw what kind of pricing do you think we're going to get for this when do you think

**[0:14:24]** it's going to be released I'm super curious so let me know in the comments what you think and also your experience using llm as well so if you appreciated this content you're looking forward to more things Ai and AI agents I would really appreciate a like and a subscribe

**[0:14:38]** and with that I will see you in the next video
