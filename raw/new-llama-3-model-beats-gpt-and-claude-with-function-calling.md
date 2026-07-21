---
type: raw-transcript
title: "New Llama 3 Model BEATS GPT and Claude with Function Calling!?"
youtube_id: RtEzpBhQWIc
url: https://www.youtube.com/watch?v=RtEzpBhQWIc
slug: new-llama-3-model-beats-gpt-and-claude-with-function-calling
published: 2024-07-21
duration: "0:14:06"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** this week history has been made for the very first time ever the best large language model for function calling is an open source model that you can run locally it's no longer a proprietary model like a GPT or CLA grock an AI company that builds infrastructure to help you work with any local model has

**[0:00:18]** recently developed their own version of llama 3 which is specifically designed for function calling and this thing is absolutely insane it's crushing it on the benchmarks beating every single AI model with function calling and so today I'm going to show you guys exactly how to use this model and we're going to do

**[0:00:35]** some testing to really see if this thing is as good as the benchmarks say it is all right so here we have the blog post from grock where they unveiled these llama 3 models that have specifically been designed for high performance for function calling now the first big

**[0:00:48]** question that I had when I heard about this because honestly it seems too good to be true is how can they actually say that their version of the Llama 3 model is the best at function calling the way that they're benchmarking this is with the Berkeley function calling leader

**[0:01:02]** board and we'll dive into this in just a second here but one thing that I wanted to call out really quickly from this article first of all there's 70 billion parameter version of their llama 3 is number one on this leaderboard right now which is really cool it's got a 90%

**[0:01:15]** accuracy um I mean that's the big deal right now but one thing that I find even more interesting honestly is their 8 billion parameter version of their llama 3 is only 1% worse for overall accuracy this much smaller model and is number three on the leaderboard so it's beating

**[0:01:30]** out all GPT models and every single Cloud Model except 3.5 Sonet with function calling right now 3.5 Sonet as you can kind of guess from what I just said is number two on the leaderboard so we can actually go over and take a look at this Berkeley function calling

**[0:01:44]** leaderboard right now this is not updated with Gro llama 3s at this point um but we had 3.5 Sona in first before the updates and then gbt 4 and Claw 3 Opus which is super cool now just looking at this initially it's a little vag like what do these accuracies and

**[0:01:59]** rankings really mean um if you want to though you can read up on everything that goes into this leaderboard and how they do their benchmarking with function calling um so just a little bit here they are trying to be very representative of most users use cases with function calling and they call out

**[0:02:15]** things like agents and Enterprise workflows and so they're really trying to model their evaluations based on how people actually use large language models for function calling and so I've spent some time diving into this and it really does seem accurate but what we're going to do now is we're going to

**[0:02:31]** actually dive into using this new gro llama 3 model for function calling and see how accurate it actually is and so we're going to use the AI personal assistant that I've been developing in my AI Master Class video and we're going to use it with this grock Lama 3 Model

**[0:02:46]** to see how well it can help me with my task management and so let's go ahead and dive into comparison first starting with GPT and then trying out with this new llama 3 Model so in order to truly evaluate the effectiveness of this new gro llama 3 model for function calling

**[0:03:02]** we need to compare it to another powerful model using the same AI agent and so the model that I'm going with here is GPT 40 and the agent that I'm going with is this task management agent like an AI personal assistant that I've been developing in my AI agents Master

**[0:03:18]** Class series here on my channel and so this agent it helps me manage my tasks in AA which is my favorite task management software there's a UI for this as well with streamlet and it uses a a lot of Cool Tools like Lane chain to build this up really really nice and

**[0:03:33]** easily and so if you're curious about any of those things you can check out other videos on my Channel or in the master class series but I'm just going to go over this code really quickly here and then we'll dive into testing it out with GPT then I'll show you how to

**[0:03:44]** change it to use the gro llama 3 model and we'll test it out there as well and so really quickly here the link to this code is in the description of the video in a GitHub repo so you can check it out if you want but I'm just going to go

**[0:03:54]** over this in a really high level right now so first of all we have a section that defines all the tools that we're giving the agent to interact with a SAA on my behalf to manage projects and to manage tasks and so here are all the tools and then we get into the next

**[0:04:09]** section which is the function to actually interact with our AI agent and so I build up the chatbot and bind all the tools to it and then handle all the prompting here and also handling any of the tool calling that comes up when the AI wants to invoke a tool as an agent

**[0:04:25]** next up we have the main function and this is just where we Define everything with a streamlet UI so I can interact act with my AI in the browser and have it manage tasks just through natural language that I spit at it uh through the chat component and so that is

**[0:04:38]** everything for this AI agent now let's go ahead and see how well it does with gp4 all right so here we are in the Streamlight UI for the task management AI agent that we have running with GPT right now the way that I ran this script is I just ran the command streamlet run

**[0:04:54]** in the name of the Python script that I just showed you you do that in a terminal and then it'll give you this UI in the browser for you to interact with your agent and so what I'm going to do right now to test how good GPT is with

**[0:05:06]** function calling is I'm going to give it a very difficult task where it needs to invoke many different tools to interact with a SAA to do something rather complex for me and then we'll test the exact same thing with the grock Llama 3 model and so I'm going to start out with

**[0:05:20]** a very simple question I'm going to say give me the 10 steps to create an AI agent application and so basically I'm just having GPT start out by doing a little bit of research for me so it'll give me the top 10 steps to make an AI Agent app it's a little vag but we're

**[0:05:33]** just doing this as an example and then what I'm going to do is I'm going to say okay great now create a project in ass sauna called I'll just say like AI Agent app and add each step as a task that is due by Friday all right so now we are

**[0:05:53]** kicking off many different things behind the scenes where GPT has to know to invoke the tool to create a project and then go go into it and create tasks for every single step so it has to also understand the due date that I gave and its previous response to be able to pick

**[0:06:07]** out each of those tasks and turn them into a nice little title for me for each task and so it's going to take a little bit here because it has to invoke every single one of those tools um but I'm specifically letting it go here and not just pausing and coming back when it's

**[0:06:21]** done because I want to show the speed here and also compare that to the grock Llama 3 Model so here we go I've created a project in AA called a Agent app and I've added each of these tasks and it gives the links as well so that worked

**[0:06:35]** flawlessly that is awesome and so now I'm going to do a couple of other little tests here and then we'll go and actually check it out in AA so first I'll say nice I have finished um defining the purpose and scope I don't spell it right but that's totally fine

**[0:06:52]** because I wanted to mark this task as complete all right it has marked it as complete nice and I'll say I'll just do another test where I want it to delete a task I'll say I actually don't want to test the application I do not recommend this but this is just a test here

**[0:07:08]** because I want to remove this task uh there we go it's removed it all right nice and now I'm going to test adding another task I'll say instead I want to hire someone to test my app so I wanted to add that as a task instead oh nice

**[0:07:23]** okay so before it even adds a task it asks me for the due date which is really good so I'll say Saturday all right added in by Saturday so now it's thinking here we go yep hire someone to test the app here we go all right so now let's going to ASA

**[0:07:38]** and actually check out and make sure that all these things worked as the bot told me it did so here we go over to ASA we've got a new project called AI Agent app I click into this and then boom here we go we got a task for every single one

**[0:07:51]** of the steps to build an AI Agent app toine the purpose and scope is complete we don't see test the application anymore and we do have a new task created that is due by Saturday to hire someone to test the app and this is new in two Saturdays from now which is also

**[0:08:05]** nice that it that it determined that so everything worked great now we're going to go over to the grock Llama 3 model and see if it can do this just as well or maybe even better or faster so let's go ahead and dive into how we change the

**[0:08:19]** code to do that all right so I'm going to spend just a minute going over the changes that it takes to use the grock Llama 3 model and then we'll go ahead and test this one just like we did with GPT to see how it fares with function

**[0:08:30]** calling and so the first thing is I'm going to import a new module from Lang Chen Gro where it's just chat grock and we'll use this to instantiate a grock model for our chatbot instead of an open AI one and then for our model that we have finded through the environment

**[0:08:45]** variables we're going to have a default here of the Llama 3 grock 70 billion parameter version and so with that all the tools are going to be exactly the same so all this code is going to be very very very similar the only difference here is instead of using a a

**[0:09:00]** chat open AI object to instantiate the chat bot we're going to use chat grock passing in that grock llama 3 70 billion parameter model you could even test this with the 8 billion one as well because that one is apparently number three on the benchmarks and so that'd be cool to

**[0:09:13]** play with as well and that is all the changes that you have to use using Lang chain to work with grock is so so easy they have documentation for how you can use grock without Lang chain but this just makes it so simple so with that let's go ahead and test out this new

**[0:09:28]** grock llama 3 Model all right so here we are in the streamlet UI for the task management AI agent again but this time powered by the grock Llama 3 for function calling and so I'm just going to go ahead and go through the exact same process as before and right off the

**[0:09:41]** bat you can see this thing is so freaking fast compared to gbt which is so cool it doesn't have the streaming effect like the typewriter effect that gbt has but I still appreciate the speed a ton and so now with that I'm just going to go ahead and give it a request

**[0:09:56]** to do all the things in a sauna like we did in GPT and so right off the bat uh it's asking us to confirm the exact date for Friday okay so that's a little weird and I think it's just because llama 3 isn't as powerful as GPT but I'll say uh

**[0:10:10]** Friday is and then I'll actually check my calendar really quickly here uh Friday is the 26th all right so let's see if I can take this and run with it to add the due dates and add all these tasks into the new AI Agent app project so it's going to take a little bit

**[0:10:27]** because even though grock is really fast I think there's a little a little bit of rate limiting because I'm using the free tier and so it'll make one task and then it'll prompt itself again to make the next task and that starts to kind of rate limit itself and so I'm going to

**[0:10:39]** come back when this is done oh actually never mind there we go all the tasks for AI Agent app have been added successfully and are due by Friday that is perfect okay so it took a little bit to get it there I had to give it a date

**[0:10:51]** when I didn't have to give that to GPT but this is still pretty cool the fact that a local model can do this an open source model is freaking insane and so now I'm going to go ahead and give it another request I'll say I have finished um let's see I'm going to say I have

**[0:11:07]** finished choosing a programming language and Dev environment because I want it to actually mark this task as complete that is interesting it seems there is an error updating the task the task ID you provided is not valid I'll say no you need to look up the task IDs

**[0:11:28]** I don't want to have to give that to the model it needs to be able to determine that itself just like GPT did um okay Define the problem has been updated successfully okay I don't even know if that's the right one so it's not doing the best here but I'll I'll test it out

**[0:11:43]** a little bit more here create a new task to um hire out a Dev let's see if it can make a new task in this project to hire out a developer for me hopefully he can do this one fine we'll see what happens it's taking a sweet time here not really

**[0:11:58]** sure why this one should be pretty quick it seems like gbt is actually faster and invoking tools somehow but here we go the task hire developer has been created successfully um let's do one more test here where I will I'll um delete the task test the AI model I don't want this

**[0:12:14]** anymore let's see if we can get rid of it fine and then I'll go over to a sauna after this and verify that everything actually looks the way it should based on what llama 3 told me in this conversation so I'll just give it a little bit of time to delete that task

**[0:12:28]** and then we'll swap over over to assana all right so it has successfully deleted the task for me and now let's go over to Asana and check this out so I deleted the AI Agent app project from GPT now this is the only one that was now created by llama 3 so I'll click into

**[0:12:44]** this we'll see how it looks okay so hire developer has been added all the other tasks are here it has checked off to find the problem or task and I don't see test the AI app anymore so there we go it successfully did everything that gbt did it took a little bit more to get it

**[0:13:00]** there but it did work and so that is a huge victory for open source and local models so I honestly can't say I'm a 100% impressed with these grock llama 3 models for function calling because they're not quite as good as GPT I think mostly just because GPT is able to

**[0:13:16]** handle a bunch of tokens a lot better but still it's insane how well this model is doing compared to other local and open source models I didn't even want to compare it to a Bas llama 3 or Microsoft 5 for example because those fall apart so bad it wouldn't even be a

**[0:13:32]** good demonstration so that's why I compared it to GPT and it was almost as good which is a huge victory for open- Source models if you're an advocate for transparency in AI or making AI accessible for anybody then this is what you want to be rooting for these models

**[0:13:47]** getting almost as good as proprietary ones is a big step forward so I'm stoked with this I hope that you can take this knowledge that I've given you and apply it to add local models as AI agents in your workflows if you found this useful in anyway I'd really appreciate a like

**[0:14:02]** and a subscribe and with that I will see you in the next one
