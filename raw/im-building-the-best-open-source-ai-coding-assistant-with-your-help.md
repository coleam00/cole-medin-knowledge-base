---
type: raw-transcript
title: "I'm Building the BEST Open Source AI Coding Assistant with YOUR Help"
youtube_id: p1YvKuRfEhg
url: https://www.youtube.com/watch?v=p1YvKuRfEhg
slug: im-building-the-best-open-source-ai-coding-assistant-with-your-help
published: 2024-10-20
duration: "0:16:22"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** recently I took bolt. new one of the best and most popular AI code generators out there and I made my own version with some much needed improvements the biggest thing that I did is I made it possible for you to choose the llm that you use to generate your code with the

**[0:00:17]** main version of bolt. new you are forced to always use just one model but with my version you can even use local llms with tools like AMA so you can generate an infinite amount of code completely for free my video on this bolt. new Fork that I made last week completely blew up

**[0:00:34]** it is now the third most watched video on my channel but even more importantly the engagement from all of you was insane and completely unmatched by any video on my channel which by the way means the world to me and really fires me up so many of you gave suggestions

**[0:00:49]** feedback even contributions to my fork and by the end of this video you'll see that I'm really taking all of that to heart because here's what I'm going to show you right now we're going to dive into a list of requests Ed features that I've added to my GitHub repo for my

**[0:01:04]** version of bolt. new including some that have already been implemented by me and some of you watching this video right now it's really become clear to me that we're actually building up a community around this project and to say that I am completely stoked is still absolutely an

**[0:01:19]** understatement let me just say that there are a lot of AI code generators out there and my Fork is not perfect but that is exactly the opportunity that we have as a community to to improve this together and get inspiration from other tools to build this into something that

**[0:01:35]** is truly incredible and who knows what this could morph into maybe at some point it'll actually become its own thing and not just a bolt. new Fork I am open to whatever and I'm just excited to be building on this together most importantly this project is just a

**[0:01:48]** fantastic way to learn how to leverage Ai and build some amazing things with it so allow me to show you the improvements that have been made to this Fork already I'll also give a really nice and concise demonstration and talk about future work for this project so without further Ado

**[0:02:04]** let's dive in all right let's start with a quick demo of this Fork a Bolton new and then I will dive into all the features that have been added and give a bit more of an in-depth demo on those as well so with this Fork right here you

**[0:02:18]** will see a couple of drop downs that you will not see in the official version of bolt. new because you can't select your llm but here in this Fork you can you can choose your provider like I can select open AI for example which you can't do with the regular version of

**[0:02:31]** bolt. new and then I can select the model that I want to use as well and then you can type in your prompt right here for what you want to have the AI generate code for or I can select one of these predefined templates as well so I'll select one of these it'll open up a

**[0:02:46]** chat widget on the left side and then the code widget on the right side and it'll go ahead and just start creating all the files for my project even running npm commands to start all this up and give me a preview of the app as well it is just absolutely fantastic so

**[0:03:00]** let me pause and come back once this is done all right so just a few seconds later and we have this to-do app that is now created and so I can go back to the code quickly here and you can see that I can look at all the source code as well

**[0:03:12]** and then within this preview it's literally just like a version of node running in my browser here I can now test out this app and yeah I mean like it's really really simple but you can build some more complex things with this especially some really nice front ends

**[0:03:23]** is what bolt. new is really good at bolt. new itself is just a wonderful platform and my Fork is just adding some much needed improvements so let's go ahead and dive into what has been added recently so here we are in the GitHub repository for this Fork of bolt. new

**[0:03:39]** and you can see here that it is 14 commits ahead and two commits behind the main open-source version of bolt. new I'm going to be keeping this constantly up to date so these two commits that are behind are actually some pretty minor changes so I don't need to bring those

**[0:03:53]** in right now but then 14 commits ahead because we have been working together as a community it's not just me making these changes to continuously improve this fork and that is what we're going to go over right now so let me scroll down right here because in the read me

**[0:04:07]** at the root of this repo I've have added this new section here that goes over the requested additions to this Fork so this full list right here and there's probably more I can add as well is everything that you all have been commenting in the YouTube video the

**[0:04:21]** original one that I made for this bolt. new fork and so I've really been going through all of your comments considering all of your suggestions and adding pretty much all of them right here and if there's any that are missing please comment below because I want to make

**[0:04:34]** this a very comprehensive list because we really are building on this as a community and you can see here that some of these have already been implemented so the first big one that was requested like multiple times within the first couple of hours of the video being released is an integration with open

**[0:04:49]** router to use their huge range of models that they have on their platform so I went ahead and I added that and then there were four poll requests that were made over the last few days for some of the other things that were also requested so an integration with Gemini

**[0:05:03]** so for both Gemini 1.5 Flash and pro so that was added as well and I'm als I've also referenced each of the individuals who have made these pull requests so you are a part of this community building up bolt. new I thank you for that because these contributions have been absolutely

**[0:05:18]** fantastic and I'll even go over each one in a little bit of detail here next up is using AMA for our models originally I just had a big list hardcoded that was available in the dropdown in this forab bolt. new but the problem with that is not everybody has all of those models

**[0:05:36]** downloaded locally through olama and so what this guy did right here is he made it so that the list of models that are available when you select olama as your provider is dynamic based on which ones you actually have pulled on your system which is really really cool because

**[0:05:52]** otherwise people were selecting models that they didn't actually have pulled and so it wasn't working with aama for them and they were confused so thank you for this addition as well also being able to filter the models by provider which you saw in the brief demo um that

**[0:06:06]** I had earlier so thank you Jason for that really really fantastic and then the last one this was actually probably the most requested feature out of all of them is being able to download what bolt. new creates as a zip file locally on your machine so you don't have to

**[0:06:20]** copy and paste every single file to bring it out of Bolt and it's funny because I actually did a very similar implementation of this myself uh cuz I was going to add this in as a part of this video that I'm making right now but then he went ahead and added this which

**[0:06:35]** is awesome it looked like pretty much the exact same as my implementation but there was a couple of things he did in addition that I appreciated a lot so I pulled in his version because I appreciated that a lot as well and I just stashed the version that I made so

**[0:06:47]** yeah thank you so much for these additions here I'll just go to the poll requests really really quickly and open up each one of them I've closed them all because I've merged them all in already so let me open these up one at a time yeah thank you again for these additions

**[0:07:00]** like this is so cool that we're working together to build this amazing thing um so the first one here added the download button to generate a code in a zip file really really basic commit the main thing that he did was updating the workbench client to add a new button

**[0:07:15]** here to uh click download to get the zip file and then he just uses the jszip and save as from fil saer this simple function right here to go through all the files put them together in zip and download them really really nice work there uh the next one letting the olama

**[0:07:31]** models be autogenerated from the olama API super clean as well let me check this out for yall so yeah if you go in here the base URL for AMA is as an environment variable now and then if I go down to uh the constants file all of the olama models are removed from the

**[0:07:49]** hardcoded list and then he has this function here to query um from the oama API all the models that are currently installed and then add those into the list so super awesome thank you for that as well and then this one for adding Gemini support really really nice and

**[0:08:05]** simple he just followed the exact same way that I added support for all the providers that I initially added for this Fork so really really awesome uh thank you so much for that um so yeah now we can use Flash and pro Gemini 1.5 super nice um and then yeah the last

**[0:08:22]** Improvement right here is adding the provider filtering and so I had to do a little bit of work to make this work with some of the other merges that we had um so I have my own commit on top of all this to make it all come together

**[0:08:34]** really nicely um but yeah this is super nice as well just being able to have a list of providers and filter on that so you're not sifting through that huge list of models that I showed in my original video you could just select olama for example and then see only

**[0:08:47]** those olama models and with the other change only the ones you have on your machine so just making things really really nice and clean and so let me actually go back to bolt here and I'll go into each of these in a little bit more detail and actually show it in the

**[0:09:01]** UI so back in the UI for the bolt. new Fork cuz I'm going to show you these five changes that were implemented really quickly and then we'll also go back to the readme to talk about future work for this project so first big thing we have is this drop down here for all

**[0:09:14]** of the providers so in my original video on the bolt. new Fork we didn't have this this list was just massive with all the models put together but now we can select just open rouer for example and see the models that I've added to that constants TTS file that I showed in the

**[0:09:30]** other video where I Define all the models so you can select one of those and just run with it also we have the Google integration with 1.5 Flash and pro that was another change that was made I'll just go to open router right now because that's the addition that I

**[0:09:42]** made that was the most requested thing at first um so yeah you can just type out your prompt or select something predefined like before and then when we get to the code window here I will show you the next thing because after open router there was a huge flood of

**[0:09:56]** requests for being able to download the code because otherwise you'd have to actually copy and paste the content of every single one of the files created in the web container here to take it out of the bolt. new UI but let me show you once we have a couple of files created

**[0:10:10]** here I will download the code and I'll show you the zip with everything in it so let me pause and come back once this is ready all right so it's almost done generating the code here so I'm going to go ahead and click on download code and then uh pull up project for.zip and

**[0:10:23]** bring it over and there we go look at that we've got all of our files even with the nested folder structure as well looking really really good okay one last thing that I I didn't cover quite yet let me go to a new conversation here um is the olama thing so if you select

**[0:10:38]** olama as your provider it's only going to show you the models that you have downloaded through AMA so I just have a few right now just some quite 2.5 ones so these are the only ones I have available and so now we don't have that huge list filled with models that you

**[0:10:51]** might not actually have downloaded on your machine looking really really nice so the last thing that I'm really excited to talk about is future work for this project so that's pretty much everything that doesn't have a nice green check mark next to it in the list that I already covered and all of these

**[0:11:06]** things each and every one of these I'd be so excited to add to this Fork bolt. new but I'm pretty busy I mean I'm working on all this other content for you and so this is where I need your help as a community we can Implement all these things and even learn from other

**[0:11:21]** tools as well to bring in more feature requests to this list there's so much we can do to make this something awesome together and so I took all the requests from the last YouTube video on this bolt. new Fork put it here starting at the top we have the LM Studio

**[0:11:36]** integration because a lot of you use that instead of something like AMA for your local models so yeah that was requested a lot for that reason also integration with the Deep seek API because the deep-seat coder models especially the 236 billion parameter one absolutely kick butt and so I totally

**[0:11:53]** get why a lot of you have requested that API integration as well and then also a big thing that that I noticed and a lot of others commented on as well is that some of the smaller models didn't perform that well with the bolt. new prompting so when you ask it to make an

**[0:12:11]** app what it would do is it would just open up a regular chat interface like if you went to chat gbt domcom and it wouldn't actually open up the web container on the right side creating files and all the code there so there is definitely an opportunity to improve the

**[0:12:26]** bolt. new prompting to make it more under understandable for these smaller models that aren't able to handle as much context now there is a workaround that I want to mention very quickly even though there's still opportunity for improvement here what some people have called out in the comments on the last

**[0:12:42]** video what you can do is send in a prompt with the smaller model like build this to-do app for me quickly stop the prompt as it starts generating go onto the right hand side there's a button to open up the code container so you do that and then you redo your prompt I

**[0:12:59]** don't know why that helps but a lot of people have reported that it does and I've even tested it myself so try that out for now but yes this is a really needed Improvement as well to play around with that prompting um next up being able to attach images to the

**[0:13:14]** prompts that's something you could do in the official version of bolt. new the paid version but they didn't add it to the open- source version so we have to actually add this ourselves which is kind of unfortunate but I guess they have to have some close Source features

**[0:13:26]** just to be able to monetize well still but that'd be nice for us to add to our Fork right here um and then the next one really really exciting is being able to run agents in the back end instead of just having a single llm that is handling everything there were a lot of

**[0:13:42]** different requests in the last video for different use cases with agents but I have something generic here that we could Implement and then expand into those more specific use cases so being able to actually have an agentic workload in the background with multiple different llms working together to

**[0:13:58]** create code and much more robust way than any single model could that would be super awesome we could use um like Lang graph and Lang chain or maybe open AI swarm there's a lot of different tool options that we have or maybe even something custom this would be probably

**[0:14:13]** one of the bigger ones out of this entire list but if we could get this and this version of bolt. new it would be a GameChanger like there's never been an AI code generator that has agents running in the background to generate code that would be so cool also being

**[0:14:27]** able to publish projects directly to GitHub like you can do in the paid version of bolt. New U loading local projects into the app so if you're working on something in vs code for example being able to actually bring it into bolt. new to have it continue working on the project with you instead

**[0:14:43]** of having to start from scratch with a prompt in the platform that would be super nice and then the very last thing is there's definitely some opportunities for just improving the main bolt. new prompt in general for not just things like having it work better with smaller llms but even just to get better results

**[0:15:01]** especially because sometimes it seems like the open source version of bolt. new doesn't do quite as well when it comes to the UI like the ux and all of like the functionality with like State Management and stuff works well but it seems like for some reason the paid

**[0:15:14]** version of bolt. new has some better prompting for making the UI look nicer sometimes um I've noticed that it performs just as well sometimes and others it's like oh the UI is a little lacking here and so there's definitely some room for improvements to the prompting in General you can find that

**[0:15:30]** massive main bolt. new prompt in this file right here in Source control so yeah that is everything for improvements and there's probably a lot more that can be added to this list so let's keep doing let's keep adding to this list tackling these things together and making something truly amazing with this

**[0:15:45]** bolt. new Fork so that's everything that I've got for updates on this bolt. new Fork it is really turning into our Fork instead of my Fork because we really are working on this together and I am super pumped about that I really think that we can take this far and it's not something

**[0:16:00]** that I'm going to monetize or anything like that I really just want this to be something that we work on as a community and I'm excited about that and just learning about AI with all of you because that is the whole goal of my channel in the end so if you appreciated

**[0:16:12]** this content you're looking forward to more on this bolt. new Fork I would really appreciate a like and a subscribe and with that I will see you in the next video
