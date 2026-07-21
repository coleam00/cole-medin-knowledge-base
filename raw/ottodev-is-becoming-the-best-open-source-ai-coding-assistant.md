---
type: raw-transcript
title: "oTToDev is Becoming the BEST Open Source AI Coding Assistant"
youtube_id: 5I9VgwauuzU
url: https://www.youtube.com/watch?v=5I9VgwauuzU
slug: ottodev-is-becoming-the-best-open-source-ai-coding-assistant
published: 2024-11-17
duration: "0:14:55"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** there are a lot of really exciting things happening with autod right now our for Kolton new that we are building to be the best open- source AI coding assistant last week we officially launched our community over in the automator Think Tank and I did a live stream that was just a blast celebrating

**[0:00:17]** the launch and there's already been a big uptick in the engagement on the project after that so many of you are making awesome additions to autod Dev and our core team of maintainers has really really stepped up thank you so much you guys and big shout out to you

**[0:00:32]** for that given all the recent updates for autod Dev there are a couple of really awesome new features I want to highlight for you now on top of that I also get to share an initial road map with you guys for autod Dev and I have a quick update on crowdfunding to support

**[0:00:45]** all the efforts for this project then at the very very end I want to talk a little bit about troubleshooting autod Dev because there's a few things that come up for that a short and sweet intro let's go ahead and dive right into it all right so over in the GitHub repo for

**[0:00:59]** autod Dev there's some PRS that I want to give shout outs for and then we'll go into the UI and test some things out so the last PR that I covered in my live stream was from Tommy respecting the provider choice in the UI making sure that that is always what is actually

**[0:01:12]** used in the back end as well and then muu tin I hope I'm saying your name right he added support for Gro and the latest Sonet and Haiku models as well so that is absolutely phenomenal and then there's the issue with AMA where the base models only have 2,000 tokens in

**[0:01:27]** their context length by default so Patrick added some configuration into autod Dev so that we don't have to do that whole separate process that I outlined in one of my other videos where you create a model file with a variation of any AMA model so now anything from

**[0:01:41]** AMA is going to work right out the gate so this is awesome and then a couple of huge features I'm going to show you in a little bit here from the codus he has been doing some amazing work within autod devb code streaming is a really big thing so you can actually see the

**[0:01:55]** large language model type out the code in each file as it is generating it as a close to it just generating the file behind the scenes and then slapping it all in at once which is what it did before and then also a bolt terminal that's attached to the workbench this is

**[0:02:09]** a huge addition as well because beforehand on the left hand side of the auto Devi you would see the commands that the large language model is choosing to run but you wouldn't actually get to look at the output so if the command failed you wouldn't really know and it would just seem like autod

**[0:02:25]** Dev was broken not that the llm was hallucinating a bad command so now you can actually see that and that is really big uh next up Aaron he did some of our stuff for containerization at some point uh just doing a little bit of Cleanup in our repo there's a couple of some just

**[0:02:40]** bug fixed stuff here as well like janen and5 adding missing flag um Ally doing some important bug fixes after some other features we merged in so thank you for doing that uh and then Edward he also added in something really cool which is standardization of model provider code so other providers like

**[0:02:56]** open router now it officially fetches all the models that are available ailable there instead of us having a hard code in that constants file the models to get from that provider so that's a really awesome addition as well and then he even added a place a little button you can click that links you to

**[0:03:11]** get the API key uh for that provider or with AMA it sends you right to the download page so now it'll kind of just give you the instructions right there on how to get the keys that you need for your different providers and then last up I just wanted to mention there's a

**[0:03:25]** small PR from Chris here but he's actually been doing a ton of work behind the scenes getting all these things merging coordinating stuff adding all these tags that you see here to our PRS and bugs so thank you Chris for doing all that as well so with all those shout

**[0:03:37]** outs there I really want to get that in because I respect all of you guys for everything you're doing here and I'm so thankful for that but now we can get into the UI and play around with some of these new features all right so over in the UI for autod Dev now let's play

**[0:03:49]** around with some of these awesome new features so there's so many cool things here now even before we go and start generating our code so the first one that I want to showcase here if I go to open router there's now this massive list because it's automatically fetching

**[0:04:03]** all the models that are available in open router and it's sorted alphabetically they even have pricing for the models absolutely fantastic and so yeah it's just a really really much needed feature they also have this button now to get your API key so it'll bring you to the account page for open

**[0:04:17]** router I'm not logged in myself on this browser here because I'm using Chrome Canary but this is where you get your API key and then you can enter it in right here or just set it in your EnV file like I do now we can actually go and generate some cod code so I'm just

**[0:04:30]** going to like select a GPT 40 as my model here just so I have something nice and fast I don't want it running locally as I do this demo quick here and I'll just build uh one of the templates that we have here and so now we'll see on the

**[0:04:41]** right hand side that it's typing out the code now before it used to just create the package.json behind the scenes and then dump it all in and then move on to the next file but now we can see it type things out and it's pretty quick here um

**[0:04:53]** but you can definitely see it typing and then we also have this bolt terminal in the bottom right now so let me before we go to the preview actually go back to that here we can see the commands that it's deciding to run whereas before it would just tell us on the left hand side that

**[0:05:05]** it's running npm runev but we wouldn't get to see the output so if the command failed we had no idea why and it was really hard to debug and we still have our own terminal if we want to run our own commands here um but then the bolt

**[0:05:17]** terminals where we can see what the llm is actually doing and so yeah that is pretty much it in a nutshell as far as the new features here a lot of things that are currently being worked on like uh loading in local projects for example something that is much much needed uh

**[0:05:30]** prompt caching I think there's another PR out for that a lot of other PRS for smaller things as well that we're looking into because there's just so many opportunities for little tweaks for autod Dev as well awesome changes across the board really excited for other things that we have coming up soon as

**[0:05:44]** well all right next up is our road map so I shared this site in my live stream last Sunday uh but one of the core maintainers on the autod dev team here he shared this with us it's Road map. sh it's this platform that makes it super easy to build really Nic looking road

**[0:06:01]** maps they have a lot of like templates here things they've already made like official road maps for the platform but you can also create your own which is what I have done for autod Dev here so this is just very much a rough draft of a road map at this point we're just

**[0:06:13]** getting started we're still very much in the planning phase together as a community for the direction we want to take autod Dev but I wanted to have this up for us to edit as we plan things and then just share with you right now so you can see behind the scenes that we as

**[0:06:27]** a community and core maintainers are really doing a ton of work making sure that we have a strong vision for autod Dev because in the end if we're just implementing a bunch of random features willy-nilly without any direction this project is going to die and I fully acknowledge that and with that I'm

**[0:06:44]** working on this and a lot of other things as a community to make sure that we are always pushing this project forward with a Clear Vision and so this road map is going to be updated a lot over time I have some of the things that we've already done already U and then

**[0:06:57]** yeah like one of the next things for example is getting crowdfunding so we can actually put bounties on features to pay developers to implement these things to really keep the project progressing quickly and then we have our initial set of high priority features that you can see in the read me right now in the

**[0:07:12]** autodab repository like preventing Bolt from always rewriting a ton of files U Better prompting for smaller llms right now you can't even use a 3 billion parameter model for example it just won't open up the web container uh loading local projects that's currently being worked on that's a huge one that

**[0:07:27]** so many of you want really really important attaching images to props for models that can actually support it running agents in the back end so having like a Chain of Thought kind of system with mixture of agents for example to generate better code a lot of opportunities there a oneclick deploy to

**[0:07:43]** netlify like the commercial bolt not new has is kind of one of the next big things after these uh this set of uh currently high priority features another one building in different prompts for different llms it's pretty obvious that if you just compare the performance of Sonet to other models that bolt. new was

**[0:08:00]** definitely made testing constantly with Sonet prompted for Sonet and so having different prompts that work better for different llms especially local ones is going to be a really important feature to get per better performance for other models because it definitely happens a lot where the performance of other llms

**[0:08:17]** is just not as good as Sona and it can be disappointing and so we want to continue to work on that and we definitely have that on the road map to take care of that and then the last really exciting thing and this road map is going to be extended a lot um in the

**[0:08:30]** near future as well but the last thing that we have on right now is something super exciting and it is an extension Marketplace and I'm not going to dive into what this looks like a ton right now because I'm going to make separate content on this and we're still planning

**[0:08:42]** it out but imagine if you could have different plugins for autod Dev that developers could create without even having to update the autod dev repository so we have this marketplace where you can post extensions that users can then toggle on and off in their UI so that as we have more and more

**[0:08:59]** features for Auto Dev we don't just have this insane feature bloat where there's so many different things on the platform and so many options and it's hard to navigate the UI so if you can instead just enable certain features that you want that's going to make it so that

**[0:09:12]** everything's still really clean but then we can continue to add more and more features into autod Dev so that's kind of the big end goal that we have at least in the shorter term until we expand this road map more um but that's just going to be absolutely phenomenal

**[0:09:25]** so yeah like I said expanding this road map a lot over time but I hope this gives you a good idea that we are working our butts off to make sure we have a really good vision for this project doing things that actually help it scale as well like this Marketplace

**[0:09:36]** so it doesn't just turn into a mess as we build on top of it more and more so really really exciting stuff and with that I want to dive into a quick update on crowdfunding so a little bit on crowdfunding so many of you on the live stream last Sunday said you got to make

**[0:09:50]** it possible to donate to this project so we can fund the implementations of different features as developers knock things off the list that we're maintaining and I'm with you there and definitely considering starting a Kickstarter it's one of the best crowdfunding platforms out there to get that going for us however there are a

**[0:10:08]** couple of other options some Partnerships that I can't really speak to quite yet that might happen behind the scenes so I'm working through that I'll definitely have some more updates in the next week or two um but some yeah really exciting opportunities just trying to figure out the best one for us

**[0:10:21]** as a community uh talking to our maintainer team about all that as well so more on that coming soon all right so I wanted to spend a little bit of time talking about about debugging autod Dev because there are definitely a wide range of issues that can come up when

**[0:10:34]** you try to run it yourself with API Keys the preview not showing and things like that and there's a lot of things you can do to troubleshoot at yourself to either fix it or get better error messages to share on our community here in the think tank or in the YouTube comments and get

**[0:10:49]** better help CU first of all the first issue that a lot of people get is this error message in the UI that says there was an error processing your request now this is not a helpful error message message it's just something that bolt. new slaps on the front end letting you

**[0:11:03]** know that something's wrong but there's actually going to be more helpful error messages elsewhere and so the first thing is if you get an internal server error like a 500 error you're going to see some output in the terminal here where you started autod Dev and so this

**[0:11:19]** is where you'll see something a lot more helpful compared to just oh there was an issue with your request and that's the kind of error that would either help you fix it or something you could share in the community to get help the other thing is if I go over to um autod Dev

**[0:11:32]** here if you go to your developer tools so let me just right click and go to inspect and then you'll be in your developer tools here you can do that in like almost any browser and then go to the console tab this is where you're going to see error messages that are

**[0:11:46]** going to be presented to you if there's an issue in the front end versus the back end so the back end is going to be issues in the terminal here and then the front end like 400 errors will you'll see in the developer console here so if I use a model to uh build a website here

**[0:12:01]** within autod Dev you're going to start seeing a lot of output in the terminal here and if there's any issues even with the bolt terminal as well you can see that there's output from the bolt terminal as well you'll see that here and it'll even tell you if there's a

**[0:12:15]** backend error because it'll say a 500 internal error for back end and then it'll be some sort of 400 error for the front end and I'm using a weaker local model here 16 billion parameter one um just because it might actually fail here and then we can see that happen in real

**[0:12:30]** time with an error so there we go boom all right we got a 404 error the llm hallucinated something with the code where it wasn't able to generate the preview and so this is actually what happens a lot of times with a blank preview is there's nothing wrong with

**[0:12:43]** autod Dev it's actually just a large language model that hallucinated something either with the code or the file structure or the commands that it decided to run and so let me go back into the inspect here and you can see like in this case it's kind of hard to

**[0:12:55]** tell but I've seen this issue before and I know for sure this is the llm hallucinating something there's not an issue in autod Dev so I can go and use a larger model that's not just 16 billion parameters and I wouldn't get this issue especially if I'm using something like

**[0:13:07]** you know clot or gbt or the 236 billion parameter of deep seat coder and also for internal 500 errors it's going to look something like this where you just have a ton of output in your terminal here and usually a lot of these can be fixed just by restarting the site and

**[0:13:21]** actually if I go back to the think tank here um this error right here x API key header missing that typically is something that will be fixed when you just restart your container or your site um and so yeah I've pretty much covered this one U this one as well the blank

**[0:13:34]** preview typically an llm hallucination like I said and then the last thing is everything works but the results are bad and this unfortunately usually just means you're using a large language model that's smaller and they mess up a lot there's just kind of the hard truth to that there so using a larger model

**[0:13:49]** like a couple I list here is a good way to get around that you can still use local LMS because maybe you want to test out a model you don't have the BS computer or you want something really fast it's still there's still a time and place to use that and just play around

**[0:14:01]** with it but a lot of times your results are going to be a little bit iffy and so it's good to use the largest model you can when you're trying to build you know the big apps and things like that so I hope that's helpful this is a pinned

**[0:14:11]** comment in the issues and troubleshooting category uh within our community here so read through this it'll really help you either fix the error yourself or have a better error message to share so you can get the help that you need no one can be as excited about autod do as me but I hope that you

**[0:14:26]** are feeling pretty close there are so many exciting things happening with this project and I wake up every single day just so excited to continue to build this together as a community a lot more content on autod dev coming in the near future including more tutorials and use

**[0:14:41]** cases and also more live streams so stay tuned for that if you appreciated this content you're looking forward to more things autod Dev I would really appreciate a like and a subscribe and with that I will see you in the next video
