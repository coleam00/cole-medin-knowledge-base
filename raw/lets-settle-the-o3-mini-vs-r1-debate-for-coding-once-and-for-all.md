---
type: raw-transcript
title: "Let's Settle the o3-mini Vs. R1 Debate for Coding ONCE and for ALL"
youtube_id: xfFyAumTjT0
url: https://www.youtube.com/watch?v=xfFyAumTjT0
slug: lets-settle-the-o3-mini-vs-r1-debate-for-coding-once-and-for-all
published: 2025-02-05
duration: "0:19:14"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** after the release of deep seek R1 an incredible open source reasoning llm open AI almost immediately fired back releasing 03 mini which is their next generation of their Advanced reasoning models and this one is very impressive as well and they had to fire back quick I mean deep seek R1 was kicking their

**[0:00:19]** Bud being open source and more powerful than all of their other models and so now we have two very impressive reasoning llms and everyone is wondering probably including you which one is better and there are a lot of different ways to compare these llms and different things they can do but coding is one of

**[0:00:37]** the biggest things that everyone cares about and so right now we're going to use bolt. DIY our open source AI coding assistant to settle this debate and code some apps both with o03 mini and deep seek R1 and see which one is better so right now I'm just going to have a blast

**[0:00:54]** using these two llms to write some code and see what kind of results we get together and I do want to preface by saying both of these models are absolutely incredible in their own right and there's a lot of differences between them as well so it's not super easy to

**[0:01:07]** compare them in every way though right now we are going to see which gives us the better code and I mean the first big difference is that R1 is open source while O3 mini is not and there are also a lot of other differences as well like architecture context limits the total

**[0:01:22]** parameters for these models and then also what they excel at a lot of times 03 mini is considered to be better at more directed tasks that we see and a lot of AI agents but then R1 is considered better at more logical freethinking tasks like solving logic problems and deep research so just keep

**[0:01:40]** that in mind when we compare R1 to 03 mini right here it's not an end all Beall comparison and I really want to emphasize that but it certainly is going to sway my decision for which llm I use to code and that's one of the biggest things that I do with AI right now so

**[0:01:53]** I'm super excited to try out both of these llms in bolt. DIY all right so I wanted to start by talking about what we are going ourselves into with o03 mini and R1 and this article on hugging face I found definitely worth the read just to get a grounding for the differences

**[0:02:09]** between these models so I'll have this Linked In the description of the video the first thing that I liked a lot is this table that they have right here that covers all the differences between these models besides just the obvious R1 is open source and o03 mini is not and

**[0:02:23]** honestly the most interesting thing that I saw is the architecture difference I mean open aai 03 mini it's a dense Transformer architecture like most of the open AI models and then R1 is a mixture of experts combined with reinforcement learning from Human feedback and so a completely different

**[0:02:41]** architecture which is super fascinating most people they put both of these models in the same basket just because they are reasoning llms but they operate entirely differently under the hood and I know that most of us in the end just care how these models perform for our tasks like coding and AI agents but it's

**[0:02:58]** still fascinating that the these two models operate so differently when they're being compared head tohe head in so many different ways right now so super cool and this article also goes through some coding examples as well which I thought were really good examples and it seemed like O3 mini

**[0:03:15]** pulled ahead for most of these but then R1 still had some advantages like little things like the UI and stuff for some of these examples and it did do better for a couple so they seem pretty head-on with each other in these examples but now it is our turn to use bolt. DIY and

**[0:03:30]** see what we can make with both so here is our bolt. DIY repository you can literally go to the URL bolt. DIY and it'll redirect you here for all of the code for open source AI coding assistant and then if you scroll down in the homepage here in this read me you'll get

**[0:03:45]** a list of all the cool features that we're working on as well as instructions to set it up and run it locally on your computer which is what we're going to be doing right here and so we are going to be testing R1 and 03 mini with just

**[0:03:57]** coding right now using bolt. DIY I might also make another video in the future comparing them for AI agents as well which is another huge thing that I always cover on my channel and a really cool idea I actually have for this is all of the agents that are submitted

**[0:04:12]** right here as a part of the automator AI agent hackathon I might actually try them as AI agents with both R1 and o03 mini so let me know in the comments if you're interested in that I think that'd be super cool also you can try all these agents right now if you just go to

**[0:04:27]** studio. automator doai you can try out all these agents agents and vote for which one you think should win the hackathon competition which is going on right now so definitely check that out I wanted to plug that really quick cuz it's a super exciting thing that we have

**[0:04:38]** going on but anyway back on over to bolt. DIY we're going to be using 03 mini directly through the openai API and then deep seek R1 through open router so I'm going to be using the Nitro version cuz I've been getting some outages with the Deep seek API which is kind of

**[0:04:54]** unfortunate so it's a little bit more pricey here but their normal version of R1 is this one right here which which is much more affordable and so Nitro is yeah more pricey right here going through together AI but generally deep seek R1 is much much cheaper um and then

**[0:05:09]** 03 mini this is the pricing for that right here so both models are going to be a bit more pricey but we're going to get some insane results so let's go and actually test that now all right now it is time and I'm going to start with 03

**[0:05:22]** mini here because it is the newer model so we're going to create a simple application with 03 mini then do with R1 then go on to one that's a little bit more comp Lex and then repeat that process just a couple of times and we should have a winner by the end of this

**[0:05:35]** so to start out with 03 mini I'm going to build a simple application just using one of the starter templates that we have here in bolt. DIY so nothing fancy to get started I do find that even with these simple prompts it still speaks a lot about the strength of the llm though

**[0:05:51]** so hopefully even with something simple like this we'll start to see which one might be better and then it should be clear as we go from app to app so let me pause and come back once it is done coding everything here 10 seconds later and we already have our app built out by

**[0:06:05]** 03 mini now there is one thing that it did not do it ran the install command here but it did not run the command to actually run the site and so I had to run that myself here in the bolt terminal I just typed in npm runev and

**[0:06:19]** then we have our preview here so looks pretty good overall I'd say that 03 mini I definitely knocked this simple task out of the park I mean there's a couple of weird things like when it says the background photo is by unsplash I don't really know why it has that here I mean

**[0:06:34]** there's not even a background image but I mean overall the functionality is looking good I can add a task mark it off delete it and add more yep it's looking great swapped over to R1 now let's do the exact same thing remember I'm using the Nitro here but this is

**[0:06:47]** just regular deep seek R1 under the hood this is just going through together instead of the deep seek API because they have a major outage right now which you've kind of been seeing a lot here which is unfortunate but anyway let's go ahead and build our react with Tailwind

**[0:07:00]** to do app so yet again I'm going to pause and come back once the app is fully built with R1 okay so it took a bit longer than 03 mini here maybe 20 to 30 seconds instead of 10 so speed definitely goes to o03 mini but R1 still

**[0:07:16]** completely knocked this out of the park with this very basic example here and actually it ran the command to start the site for me unlike 03 mini so it did more of a true one shot so definitely I think the functionality goes to R1 as well and also I like what it produced a

**[0:07:32]** bit more I mean the O3 mini was more simplistic and maybe you might like that but I like how it actually thought to itself it took this simple prompt and reasoned better about what I would actually need so I didn't say that I needed some of these features here but

**[0:07:45]** it knew that I really would want it so here's an example if I add a couple of tasks here you can see that it says zero of two complete so there's really more here like that there's nothing like this with the version that 03 mini produced and it updates in real time as I Mark

**[0:07:59]** things off delete it this is looking really really nice and then it's kind of cool it says your task list is empty and Serene it's very peaceful right here when I don't have any tasks and it doesn't show the image I think that's actually more of an issue with the web

**[0:08:11]** container with bolt overall this looks absolutely perfect so I think the functionality goes to R1 speed is definitely going to 03 mini right now but enough of this basic example let's actually take this to the next step with something more complex the sponsor of today's video is repo Cloud a phenomenal

**[0:08:28]** Cloud platform that is also an open source app Marketplace I've never heard of something like this before it is just super cool and they have super competitive pricing for their instances and elastic Auto scaling so you're only paying for when your instances are being used which saves you a fortune on your

**[0:08:45]** Cloud Bill and they have oneclick deployments for all these open source apps that I'll show you in a little bit and they are continuously updating them and it's super easy to bring these updates into your instances running these apps the pricing for the reple cloud instances are super impressive and

**[0:09:01]** very competitive so if you go to their website reple cloud. and then go to their pricing page right here you can click on all of their instance types and you will see the comparison of their pricing compared to similar instances from all of their competitors I'm talking ec2 on AWS digital ocean Lino

**[0:09:19]** Railway render all these platforms that I've used before that I like and I'm very familiar with but reple Cloud beats them for pricing for every single instance type it is so cool you can click through all these whatever your needs are reple cloud has got you covered and they have the dynamic

**[0:09:35]** scaling the elastic compute that I talked about earlier that'll save you on average 93% of your Cloud bill because you're only paying for when you're actually using these instances instead of just that straight up fee for $50 a month for your instance or whatever it might be on another platform like AWS

**[0:09:51]** and then also they have their app Marketplace that's their homepage right here all of these open source apps that you can deploy in one click so easily including the very own developed by our community bolt. DIY you can deploy it in a single click along with a lot of other things

**[0:10:07]** like NN and open web UI that I absolutely love and so going to my dashboard here I actually have bolt. DIY deployed here through reple Cloud I'll click into it it has you log in for the first time so they have it protected but it yeah it's just so cool like look at

**[0:10:21]** this I got my bolt. DIY right here hosted in the cloud instantly it was literally just like one click and I had to enter in a few things and that was it so repo cloud is absolutely fantastic I'd highly recommend checking them out I'll have a link in the description to

**[0:10:34]** them and a pin comment as well give it a shot it's a great Cloud platform to host your open source projects next up we definitely have a more challenging prompt here so this one I've actually covered in other videos on my channel because I've used this to use a tool

**[0:10:50]** like lovable or bolt to create a full chat front end for my AI agents that are running locally or in n8n and so I'll have a link to this in the description this full prompt here cuz you can use it with a tool like bolt. DIY or lovable to

**[0:11:04]** create a full front end it's very very neat it integrates with superbase completely for authentication and managing the agent chat history and so I'm not going to dive into the details of this prompt because we really just want to use this to test R1 and 03 mini versus dive into what I'm actually

**[0:11:19]** making here so I'm just going to go ahead and copy this and bring it into my bolt. DIY instance here so I'll paste in the prompt I filled in a couple of things that were placeholders there like the URL for the agent and also my superbase Anonymous key and project URL

**[0:11:35]** and so now I'm going to go ahead and paste this in and we should take a bit longer here it's going to be a little bit more that it has to actually produce so yeah using 03 mini to start like last time let me pause and come back once it

**[0:11:46]** has produced the app so it took a few tries here with 03 mini to get to the working state that we're seeing right here in our app let me to scroll up and show you these errors pretty quick so first of all it started with just showing me the remix starter template

**[0:12:00]** page so it mixed up something with the routes that I had to fix it took care of that and then there were a few other errors that we had to work through here which by the way it's bolt. DIY it is super easy whenever you get an error in

**[0:12:09]** the front end just click a button that you'll see around here it'll paste in this entire error like you're seeing right here I did not paste this in myself and then it'll give it to the llm to fix so it took a few shots here but now we've got something so let's go

**[0:12:21]** ahead I'm just going to use some test credentials that I have created in super base we'll see if we have a working app and so let me sign in and okay this is looking really good compared to lovable and bolt. new which I tested the same prompt with in other videos on my

**[0:12:34]** channel this is looking pretty impressive so you can load the conversation history here for all of our different chats that we have just stored in superbase right now let's see if I can actually continue a conversation as well so I just go to this one right here I'll just say uh I'll just say hello

**[0:12:49]** we'll see if we get a response so it's loading and yeah we got a response back from our NN agent that is running live right now and the only thing it messed up is it duplicated the user message which I've seen this a lot cuz it doesn't quite understand how the

**[0:13:02]** message comes through in the database as well so it doesn't need to display it manually on the front end but overall this is looking really good so everything is working great it took a few tries to get there now let's see what it looks like with R1 all right

**[0:13:15]** Blank Slate back over to deep seek R1 through open router let's paste in the prompt and let's give it a rip just like we did with O3 mini so you know the drill I'm going to pause and come back once we have our app okay so it took a

**[0:13:28]** lot longer with R1 than it did 03 mini that speed difference is definitely exaggerated with a more complex app but I am very impressed with what R1 put out here so it actually did pretty good even with just a single shot so it took a few tries with 03 mini to even get to the

**[0:13:44]** point where it compiled with R1 it was right away so to be fair and to give it a couple more prompts like I did O3 mini I just corrected some of the functionality itself to work on that and what it produced is quite similar to actually when I used R1 to make

**[0:13:57]** something like this in one of my previous videos but yeah this is just looking so so good honestly looking better than 03 mini so same exact super base here so I'm going to log in with the same credentials and let's take a look and see how it looks

**[0:14:10]** compared to uh 03 mini okay so first problem here it looks like it's not loading in my conversations which is kind of weird so everything else actually looks a lot better but it seems like the functionality isn't quite perfect here let's see if I can send a message here to the llm so I'm saying hi

**[0:14:28]** and okay it works so it has the same duplicate error message issue so I didn't quite fix that even though I was trying to tell it here in the prompt so certainly not perfect but it looks a lot better than 03 mini I will say that um let's see if the conversation history

**[0:14:41]** Works everything's looking good there yes it did okay all right everything's looking good I can start a new conversation I can log out there's a lot more functionality here but definitely a couple of more glitches than with 03 mini so it's really hard for me to tell what actually is the winner here it

**[0:14:57]** seems like you could even use these two together like o03 mini to cover some of the functionality that R1 seems to mess up with like the conversations here but then using R1 to add in more features and make things just look nicer so surprisingly r1's actually better for

**[0:15:13]** the UI I just kind of thought that o03 mini would be better for that super super interesting so now let's go on to the last test case here okay so the last test that I want to do in this video is a more complex request but a much

**[0:15:25]** simpler prom so it's kind of like first I'm testing off a very basic app then I'm testing a more complex app but I guide it through the prompt in a lot of detail now I want to just give it a lot of creative freedom so just a single

**[0:15:38]** sentence here build me a fully functional chess site I absolutely love chess I was even a chess coach at one point in my life and so yeah I thought this would be fun to try here and 03 mini again it messed up a couple of times here and did that same thing where

**[0:15:51]** it just started with that welcome to remix starter template page and then when I had it correct itself it still has welcome to remix which is really stupid um but I click on this button to play chess and then it brings me to a chess board so okay I guess that works

**[0:16:04]** out fine and it's pretty cool like I click on a pawn let's move it here and it doesn't understand that I can move the pawn two spaces for the first move so it's certainly not perfect um but yeah it's working well I can capture pieces and like overall it's really not

**[0:16:20]** following the rules of Chess um so let me just try this here I think I can actually take the king I tested this earlier and yeah I can take the king so um I can put myself in check so it's not a perfect uh situation here but yeah

**[0:16:33]** it's pretty cool that I made a full chess board here just with a single prompt I could probably take this much much further I'm not doing a lot of follow-up prompts in this video because I want to keep it short and concise and really compare models versus make a full

**[0:16:44]** app but I probably could take this much much further so that's 03 mini let's go on to test the same thing with R1 now here is the chessboard produced by Deep seek R1 now for both these examples here I'm not showing the full things starting it from scratch just cuz I want to keep

**[0:17:01]** this video concise here and so yeah I'm just showing you the end result built with R1 and this looks so much better than the chess board built from 03 mini so the UI yet again goes to R1 let's actually test out the functionality so first all click upon and okay it doesn't

**[0:17:18]** follow the rules so it's just like 03 where it doesn't really work it looks like I can just move all over the place so I guess it's more meant for just if you want um yeah this is this is awful I guess it's more like if you are you know

**[0:17:31]** trusting that you and your friend or whoever are actually going to make legal moves then this would work really well um but otherwise yeah the functionality is not the best just like with 03 mini O3 mini actually did handle like illegal moves and things like that um or at

**[0:17:44]** least it tried to so I would give the functionality to 03 mini so it seems like in general R1 has a much better UI and just the ability to like reason more about what you actually want um but then when it comes to actually implementing things correctly it's it seems 03 mini

**[0:18:00]** has a bit of an edge there and then also for Speed that definitely goes to 03 mini as well so definitely pros and cons like I said just a little bit ago it seems like there might actually be an opportunity to use these two llms together and that is something I would

**[0:18:13]** love to create some more content on so let me know in the comments if you are interested in that okay I just got to say I had a blast using bolt. DIY to build these different apps with R1 and 03 mini I think it's the real winner just because I'm able to use this as an

**[0:18:28]** AI coding assistant supp any llm that I want but yeah like I said it seems like 03 is better for Speed and then raw functionality then R1 is better for UI and then just kind of actually understanding what you want to build even though it doesn't always implement

**[0:18:41]** the functionality correctly so super interesting I'm also curious what you have experienced using these two different models if you're experiencing the same kind of thing as me or maybe it's totally different one's way better than the other for you for me it seems like both are actually quite useful so a

**[0:18:57]** lot more content coming soon not NE neily comparing these models but building more things using both R1 and o03 mini both fantastic llms so if you're looking forward to that and you appreciated this video I would really appreciate a like and a subscribe and with that I will see you in the next

**[0:19:11]** video
