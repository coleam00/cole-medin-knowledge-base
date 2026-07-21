---
type: raw-transcript
title: "Qwen Just Casually Started the Local AI Revolution"
youtube_id: y6Wh4SpRoao
url: https://www.youtube.com/watch?v=y6Wh4SpRoao
slug: qwen-just-casually-started-the-local-ai-revolution
published: 2024-11-13
duration: "0:16:06"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** all right I'm going to start right out the gate saying something a little cheesy here but by the end of this video you are definitely going to be on the same page as me yesterday November 11th 2024 marks one of the biggest days for AI this entire year and I know that is

**[0:00:15]** saying a lot trust me but after my initial testing of what I'm about to show you now I sincerely mean it I have not been this excited about anything in the AI space for a couple of months now except for autod Dev of course but yesterday a new version of my favorite

**[0:00:32]** open source large language model quen was released and it is quen 2.5 coder 32b I found out that quen 2.5 coder 32b was released last night right before I was about to go to bed and I literally got up went to my office booted up my computer again downloaded the model and

**[0:00:50]** started testing it out with a bunch of different things including autod Dev our bolt. new fork and some of my AI agents and let me tell you it literally felt like I was in a fever dream I had to CL myself to make sure I was actually awake

**[0:01:03]** because the results were that insane and I had to go look at my code and make sure it wasn't actually using 01 behind the scenes the results with quen 2.5 coder 32b were that good now I know that you might think that I'm exaggerating that this is too good to be true but

**[0:01:17]** don't just take my word for it allow me to demonstrate to you how well this model works with both autod Dev and an AI agent that I created specifically to push limits of AI to test new llms like this and the best part is I'm running quen 2.5 coder 32b entirely locally so

**[0:01:36]** I'm paying nothing for it and you don't have to either super exciting stuff so let's go ahead and dive right into it all right so before we dive into testing quen 2.5 coder 32b a lot of you for these kind of videos have asked me to go over how to pull these models Hardware

**[0:01:53]** requirements and then some considerations as well if you don't have the beefiest computer so I'm going to cover that right now first of all my recommended way to use local large language models is with olama so you just go to ama.com click on this nice big download button here and then you'll

**[0:02:08]** have it already ready to go ready to pull any model in their library and so I'll have a link in the description for this but you want to go to the quen 2.5 coder page for AMA and they'll give you the command right here that you can just

**[0:02:20]** copy to pull and run quen 2.5 coder 32b and you can select other variations as well here like the 7 billion parameter one that's been out for a while and now they recently released a lot of other ones like 14b and 32b so 14 billion parameters this model I haven't tested

**[0:02:37]** myself yet but this is going to be a really good option as well if you don't have the BS machine you could run this instead if 32 billion parameters is just too large I would highly recommend if you're going to run the 32 billion parameter model that you have at least a

**[0:02:52]** 3090 graphics card from Nidia and so for my computer specifically I'll pull up my task manager so you can see I have 23 90 gpus I made an investment here to build this computer because AI is just my life so I picked up two Ed 390 graphics cards

**[0:03:08]** um but a 32 million parameter one is able to run on just one of my cards so you don't need two yourself and then if you don't have a 3090 there are a couple of options that I want to cover very quickly here first of all if you click

**[0:03:20]** on the the drop down here for the parameter options and click on view all you'll see a lot of different variations here that you can download each and every one of these for quent 2.5 coder and if I scroll down to the 32 billion parameter section here there's a concept

**[0:03:36]** called quantizing with local large language models where essentially you can reduce the size of the model significantly while only reducing the performance a tiny bit and I don't want to dive into that it could be a whole separate video but you have options like a Q2 quantizing where the model is 12 GB

**[0:03:55]** instead of the 20 GB from the default one that old Lama has for you you can pull this one if you want a smaller one and try to run that and also you have all these options for the 14 billion parameter as well so I'd recommend trying that out as well too if the 32

**[0:04:09]** billion parameter model just blows up your machine when you try it so give it a shot run 14 billion as well just get Quin 2.5 coder on your machine because it is absolutely killer so let's go ahead and test out the 32 billion parameter version so not surprisingly

**[0:04:24]** one of the first things that I wanted to test with this new model is autod Dev our Fork bolt. new which which is one of the best open- source AI coding assistants out there and so I've got quen 2.5 coder 32b loaded up with olama and autod Dev and just like with any llm

**[0:04:39]** it helps to start with a very simple prompt and then get iteratively more complicated so we can build something that isn't just trivial and so just to start out I'm having it create a react chat interface with Tailwind where I can send in a message and get a sample

**[0:04:51]** message back and quen 2.5 coder 32b is going to knock this out of the park so it's running locally it'll take a little bit to actually build this and so what I'm going to do is pause and come back once this is complete all right so we got our very first iteration of the chat

**[0:05:07]** interface where we'll get a sample message back after we type in our own so this is looking good so now let's add in the next prompt here to really give it some requirements here so I got some UI requirements and then some ux ones as well and then some functional things

**[0:05:21]** like have an AI agent just respond with a sample message after waiting two seconds with the loading indicator and so now we're starting to get to something that isn't just trivial and it's still pretty basic but this is the kind of thing that other local large language models will totally botch and

**[0:05:37]** so I'll even show that after this with another model but first what I'll do here is pause and come back again once this iteration is complete and boom we now have our updated chat interface that is starting to look a lot better still probably some tweaks we could do here um

**[0:05:52]** but overall we even got a nice little loading indicator here got a sample message this is all looking absolutely fantastic and I can continue to prompt this to to touch up The Styling actually hook up an API endpoint like I did in another video on my channel for this

**[0:06:06]** interface with autod Dev you can take this much much further it is all working really really well so back to the drawing board here because I want to show you how other local llms will mess up in a way that quen 2.5 coder 32b simply doesn't notd and so I've got code

**[0:06:22]** llama 34b loaded in here and I'll show you that this this model it's actually a little bit bigger than the one I just used and it still is going to mess up so I'll start with the same basic prompt here and it'll probably do this fine um but when we get to the more complicated

**[0:06:37]** stuff it starts to really mess up because as much as I hate to break it to you local llms in general just aren't as powerful as the big guys like claw 3.5 Sonet and so it really does help to uh use those a lot of times but with quen

**[0:06:51]** 2.5 coder 32b you actually can use that to build most things so let me pause and come back once this is done with code llama okay and look at this before I even got to the more non-trivial stuff it actually messed up right away it failed to run the npm Run Dev command

**[0:07:09]** because it never installed Vite it didn't run that First Command that you'll always see Sonet and quen 2.5 and other models run where it does that mpm install so it it never installed anything there's no preview here a very basic example failed with code llama 34b again this is even a little bit bigger

**[0:07:27]** than Quin 2.5 Cod or 32b and it totally failed so I hope this shows you how exciting specifically this new model is with Quin 2.5 coder 32b uh just amazing how much this can do compared to other llms that are supposed to be equal in size and power the sponsor of today's

**[0:07:47]** video is novita AI it is an all-encompassing AI Cloud platform that makes it really easy to get up and running with open source large language models they have three primary products on their platform including the llm API that makes it really really easy to use a bunch of large language models with a

**[0:08:03]** simple API they have server list to make it really easy to deploy and not to manage infrastructure for your AI applications and they also have GPU instances which are really really configurable you can pick a type and then even select the number of gpus all the way up to eight for that specific

**[0:08:19]** instance type and graphics card which I haven't seen on another platform before which is phenomenal you also have a bunch of templates here like AMA with open web UI and you can create your own template really easily with any container image you could even for example use our bolt. new Fork right out

**[0:08:34]** the gate in an ovita AI instance which is just phenomenal so I've actually created an instance myself with olama and open web UI with two 390 gpus really easy to get up and running in just minutes you have a nice terminal to interact with your instance in the

**[0:08:47]** browser and then also I've got open web UI open up here um using uh code llama 13B and I can say create the snake game for me in Python and it is just blazing fast so just awesome these instances absolutely kick butt and then for the llm API there are a lot of really unique

**[0:09:04]** models that they have available here so a lot of standard ones like llama 3.1 405b but also a lot of unique models that are meant more for like creative writing tasks for example so they have a really unique set available in their API very competitive pricing as well for

**[0:09:18]** their models and then the last thing is it is open AI compatible so you can just override the base URL here set it up just like you're talking to GPT in your applications so it's really easy to drop and replace this to use novita in place of something like GPT if you want to use

**[0:09:32]** local llm so I'll have a link in the description of this video to novita AI I would highly recommend it checking it out it is a platform that I've used in the past and will continue to use for a bunch of my infrastructure for large language models so the next thing that I

**[0:09:45]** wanted to test quen 2.5 coder 32b with is with this agent that I built with Lang chain and Lang graph that specifically is meant to push a limits of large language models to test new ones like what I'm doing right here and so there's actually another video on my

**[0:10:00]** channel where I show how to build this agent and I do some more testing with other llm so I'll have a link to that in the description of this video along with the GitHub repost you can download this agent and run it yourself so I'm not going to go into the details of this

**[0:10:13]** because I covered that in my other video but it's a streamlet front end and then I'm using L chain and L graph for this agent hooking it into a bunch of different tools so that it can interact with a so I've got a ton of different tools for a SAA for task management and

**[0:10:28]** then Google Drive for our file downloading and uploading files to Google Drive and searching through folders and then for rag I am integrating with chroma for a local Vector database so that we can um basically take the things from Google Drive add it into a knowledge base for

**[0:10:43]** the llm to answer questions and so all these tools combin together to create an agent that is very much not trivial there's a lot of different tools that the large language models get to choose from based on a user's question and so local llms often mess up and actually

**[0:10:59]** one really good example is that I used llama 3.1 70b from Gro in the last video on my Channel with this and it completely messed up on all these things that I'm about to show you quen 2.5 coder 32b it definitely does well with so let's go ahead and dive into this

**[0:11:15]** testing right here so I've got my asaa open right here so we can see it creating tasks and stuff I've got my front end interface here with streamlet and then I have my terminal open as well where we'll be able to see all the decisions that AI agent decides to make

**[0:11:30]** for Tool calling kind of like what we have already right here from testing that I was doing earlier so I'm going to start with a very basic prompt here what projects do I have in AA I don't even have to type it right I'm just going to let it go here so we'll go into the

**[0:11:44]** terminal here and it's going to yeah call the get as projects tool gets the Json result from the asaa API and then it tells me our projects are YouTube Fitness business personal and coding and this is exactly right based on what I have on the left hand side here and also

**[0:11:58]** note that that the projects within my coding project here the tasks list is empty because now I'm going to ask the second question here to create a task in my coding project due by the 18th and so it has to reason about a few different things here like the ID of the coding

**[0:12:13]** project the due date the name get all that together to now invoke create auna task with these arguments and yep so it's got the due date the task name looking really good and it's going to tell me after it finishes this that it has made the task in the project coding

**[0:12:28]** so let me go over to my coding project and there we go boom due by Monday the 18th build the first billion doll agent looking absolutely fantastic so now what I want to do is I want to have it do something with my knowledge base with Rag and Google Drive so I'm going to ask

**[0:12:43]** it to download my meeting notes from 823 and add them to your knowledge base so it has to do a couple of things here together to actually make this request happen and so first of all it's going to search and download the file from Google Drive looks like it did not find the

**[0:13:00]** file with its initial search because it was very very specific here and so yeah so it says that it did not find my file but I'll just say uh search for meaning notes and so I'll just give it a more uh General instruction here to search and there we go now it found the 823 meeting

**[0:13:17]** notes and so sometimes with agents you have to correct it and steer it a little bit but it's still looking really really good so now that it has found the file it needs to download it and actually add it to the knowledge base and so let's see what it is able to do here here it's

**[0:13:30]** clocking a little bit it's really thinking hard so I'm going to give it a second here all right and decided to download The Right file this is looking really really good and now it needs to add it into its knowledge base and there we go yep successfully added the file to

**[0:13:43]** the knowledge base looking absolutely fantastic and now it says it has been downloaded and added to the knowledge base absolutely fantastic and so now I can ask it what are the action items from the 823 meeting notes and I actually made it so that the only way to

**[0:14:01]** access this file is through the vector database so it can't just search the file directly it has to perform Rag and so let's go back to the terminal here yep it query the documents what are the action items from the 823 meeting notes and then we have our source of this file

**[0:14:15]** that we just downloaded and we got these meeting notes and let's go back over so discuss latest and greatest headphones figure out how to use AI to get rich bake 13 cookies and mow the lawn I know this is really really silly this actually matches exactly with what we

**[0:14:29]** have have in the file I can even show this here if I go back to um my file right here in my data I have this document file that it downloaded from Google Drive and sure enough these are the action items that we have so this is working super super well llama 3.1 70b

**[0:14:45]** would have broken a long long time ago so absolutely fantastic and still pretty basic AI agent there's a lot of questions I could ask it to do some more complicated things but you can see here that it worked really really well with all my different servic serves other

**[0:15:00]** local large language models would have failed miserably even with like creating tasks in a sauna and so taking it even further to downloading things from Google Drive searching for files adding to the knowledge base all fantastic that it's able to do that the world of local and open- Source AI is so exciting right

**[0:15:17]** now and quen 2.5 coder 32b is honestly the biggest reason that is the case I absolutely love how much power I get with this model for my agents and it's especially important for agents I want to have running constantly on my machine where it wouldn't be practical to pay

**[0:15:33]** for an API to use a model like CLA 3.5 Sonet because I be racking up a huge bill I hope that through this video you can see at least at a high level how powerful these local llms can be it is just so incredibly exciting to me how

**[0:15:48]** quickly the Gap is diminishing between the massive close Source models like 01 and Sonet and local llms like quen 2.5 that you can run yourself for free if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next

**[0:16:04]** video
