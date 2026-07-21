---
type: raw-transcript
title: "This Bolt.new Fork is EXPLODING - Don't Miss out on What's Happening!"
youtube_id: jm007pw2v1A
url: https://www.youtube.com/watch?v=jm007pw2v1A
slug: this-boltnew-fork-is-exploding-dont-miss-out-on-whats-happening
published: 2024-10-27
duration: "0:16:47"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** two weeks ago I released a fork of bolt. new which is one of the best AI coding assistants out there my primary goal was to make it possible to use any large language model especially local ones to work with bolt. new because the official version only supports using a single

**[0:00:17]** model I just wanted to release something cool and practical just like any other content on my channel however once I released this Fork a lot of you started to contribute additional features and it became clear to me after only like 10 days that we are really starting to

**[0:00:32]** build a community around making the best open- source AI coding assistant out there at least that's the vision that a lot of us have now and I am stoked out of my mind for this so today I have four quick updates that I cannot wait to share with you I'll cover each of those

**[0:00:47]** and then also dive into recent feature additions to the fork and cover priorities for upcoming changes to the project I'll also shout out all of you who made contributions recently because I seriously appreciate each and every one of you you a lot of exciting stuff so let's go ahead and get right into it

**[0:01:04]** so first things first I just wanted to call out that we have had 20 pole requests into this bolt. new fork in just the last week alone so our Fork is going really really strong and there's so many amazing people contributing amazing things and really it's gotten to

**[0:01:20]** the point where I have committed to myself to really maintain this long term and build this up for the community because together we are really making something awesome and I don't just want this to be another project for content for my channel I really want to turn this into something larger for all of us

**[0:01:35]** to build together to go along with that my second update is I'm soon going to be releasing a discourse community so we can have a place to chat about this project plan upcoming changes maintain everything really just make sure that together we are in fact building the best open- source AI coding assistant a

**[0:01:52]** lot of you have requested a community recently and so I'm really excited to bring this to you and also this is going to be a part of a larger project that I'm building behind the scenes to have a community for my entire channel so I'm really excited for that and the bolt.

**[0:02:06]** new Fork is going to be a huge part of this community so stay tuned for more updates on the community because I am so so excited about that and we'll be releasing it really really soon the next update that I have is that I am opening up applications to become a core

**[0:02:20]** contributor to this bolt dot new Fork anybody is welcome to make contributions by forking the repo making their own changes and then bringing it in as a poll request the difference is with a core contributor you're actually a maintainer of the project with access to the repo you can do things like approve

**[0:02:37]** poll requests merge poll requests make emergency bug fixes all that good stuff because this project is growing to the point very quickly where I need help I can't just maintain everything myself especially as we scale and start to get dozens and dozens of poll requests every single week so I want to ensure the

**[0:02:54]** success of this project and having others come alongside and help me as maintainers is going to be really really important important so in the description I will have a link to the Google form an application to become a core contributor so if you're interested in that and you have a lot of experience

**[0:03:09]** developing especially with generative Ai and open source projects I really really want you to apply I'm expecting there to be quite a few applications and so even if you're really really qualified doesn't necessarily mean that you will become a core contributor but I need a lot of help and so I will be accepting a

**[0:03:25]** lot of applications so please apply below I am looking forward to working with you and having you become a maintainer for this bolt. new for the last update that I have for you is that this project is blowing up so much that I'm going to start making regular

**[0:03:38]** content on it on my channel including a tutorial soon on how to get this up and running yourself on your machine something that a lot of you have requested and it's really important to make this really easy for everybody to get up and running and really accessible I might even be making content weekly

**[0:03:54]** for updates on this project I'm still trying to figure out my content calendar and how it'll work but I want to make regular updates regardless because I want to keep this project moving really really fast just like it already is so that's everything that I have for updates and now I would love to dive

**[0:04:09]** into recent additions to this fork and talk about upcoming changes as well all right let's go ahead and dive into the recent additions to this bolt. new Fork so I'm in the root of my GitHub repository here with the read me and if you scroll down a little bit you'll see

**[0:04:22]** this wonderful list that we have here of everything that's been added and needs to be added and will be added soon so I'll cover the second list in a little bit but right now I want to focus on the things that have been added recently so on the last update that I gave for this

**[0:04:35]** Fork my last video this was the last Edition that I covered which by the way this is really fantastic as well being able to download what the AI builds for you as a zip file um but next up the first thing that I merg into my main branch after that last video is this

**[0:04:51]** change right here and I'll call out each of the authors when I show the actual poll requests so I'm not going to cover that here but you can see all the authors of these additions right here as well so improvements to the main bolt. new prompt essentially what was done here

**[0:05:06]** was a little bit of Chain of Thought prompting within the main bolt. new prompt just to get the llm to think a little bit before it spits out all the code um so it's not like a major thing that'll make it work all of a sudden with even really small llms but this is

**[0:05:19]** still a really helpful addition um just to make the llm perform a little bit better for this open source version of Bolt so thank you very much for that next up we have the Deep seek API integration this is a great addition because you can use deep seek through

**[0:05:35]** open router as well for example but a lot of people actually requested the Deep seek API integration itself um Because deep seek coder is just a fantastic model for coding projects in general so it fits really really well with this Bolton new Fork also the addition of mistol a lot of people like

**[0:05:53]** using mistol so this is a great API integration as well uh and then for the last integration Edition this one is unique and very very cool open AI like API integration so for those of you who don't know a lot of providers like grock for example actually make their API for

**[0:06:12]** using their llms open AI compatible and what that means is in your code you could be using the B cell AI SDK Lang chain it doesn't matter you can set up an open AI instance but then just change the base URL from the URL that points to open AI for like GPT to whatever the URL

**[0:06:31]** is that that provider set up so like grock for example or those even other things like like fireworks or together like all these have open AI compatible apis so you can act like you're just setting up an open AI instance but actually use the models through that provider and so uh what this did right

**[0:06:46]** here is make that generic Recon set up as an environment variable that base URL so you can talk to all those different services so really this adds a lot of Integrations at once which is super super neat so a little bit more technical there but for those of you who

**[0:06:59]** care about that I wanted to call out what that does exactly because that is just fantastic the next one is the ability to sync files to a local folder this is a one-way sync so you can take the structure that was created all the files created in the web container

**[0:07:12]** within the bolt. new UI and push that out to a folder on your computer so it's similar to being able to download the project as a zip um but this way you just get it directly within a folder on your computer uh which is really nice and convenient there's kind of like two

**[0:07:28]** ways basically now to to extract everything from this bolt. new Fork once you generate a project zip vile might be better when you want to send it over to someone right away and then this one-way sync to a local folder might be better when you want to then like open in vs

**[0:07:43]** code for example without having to extract from a zip so both are fantastic additions this one is just the newer one here uh last up or actually second to last right here being able to containerize the application with Docker this is a big one that I was really

**[0:07:57]** looking for so I appreciate this getting added as as well because it's also going to make it easier to get this up and running on your local machine so when I make a tutorial in the near future on how to get this up and running I'm going to be doing it through Docker because

**[0:08:10]** it'll make it easier for everybody and then the last change that we've got going on right now is being able to publish projects directly to GitHub this is fantastic because not only now can you download it locally as a zip file or pushing it to a folder you can push it

**[0:08:26]** directly to GitHub and I've tested all of these integration here including this one so I actually have like a public repo where I just published a sample app using this functionality and it worked fantastic and it is great um and yeah this one specifically there might be a

**[0:08:40]** couple of changes that would be good improvements to this like the UI isn't the best for publishing to GitHub right now um but this fan this is still a fantastic change and really all of these could maybe use like a little bit of um more addition and and refinement but

**[0:08:55]** that's what open source is all about just making these changes and continuing to iterate on it together so absolutely fantastic and then also I just want to call out that I have some pull requests here that are still pending there's still some things I have to look through

**[0:09:08]** and a couple of comments that I had for some people just questions for followup before I merge these things um but I'm getting all through all of this and U that's my commitment to you because I really want to consider every single one of your poll requests and so each of

**[0:09:20]** them that I've merged I've also commented on um provided my feedback and tested and everything so I'm really paying close attention to everything that is coming into this Fork um so lastly I just want to cover these poll requests really quick and call out everybody who has made changes so first

**[0:09:35]** of all Kofi added the structured planning step like kind of like that Chain of Thought to improve the prompting so thank you Kofi for that uh David added a fix for llama 3.1 models because the max tokens had to be reduced very very slightly to make it work

**[0:09:50]** otherwise those models were crashing when you use like grock with LL 3.1 for example so thank you David for that Aaron added the docker editions which I appreciate a T because again I'm going to be using these for my tutorial on how to get this up and running yourself um

**[0:10:05]** and then let's see here we got the GitHub functionality by Gonzalo thank you very much for adding this um that was one of the bigger changes so I appreciate it a lot and then adding the oneway sync to local folders was done by mfer so thank you very much for that and

**[0:10:20]** if I'm pronouncing anyone's names or GitHub usernames incorrectly I'm really really sorry I'm trying my best here um but yeah a lot of people have very unique GitHub usernames um yeah so adding mistro models by aru thank you very much for adding mistol everyone loves mistol so much much needed um

**[0:10:36]** enhancing olama model integration adding some typescript stuff as well just to make that really really clean by TK thank you very much for adding that in uh the Deep seek integration by Zenith awesome thank you very much for that again deep seek coder is a fantastic model especially the 236 billion

**[0:10:53]** parameter version for bolt. new so I definitely recommend trying that out and then adding the opening I like integration by xery thank you very much for adding that and then the last one that I merged at this point by Noob y DP adding the further changes to support

**[0:11:10]** the olama API base URL this was a problem initially when we added some more functionality around AMA where it wasn't actually working unless you actually had olama hosted Local Host on Port 113 or 434 um so if you had it host on like another machine for example it

**[0:11:26]** wasn't working here but with these changes now it actually is working so thank you very much for adding that in that is everything that we have for changes so now I want to dive into upcoming changes for this project including some very top priority items that I'm really excited to get

**[0:11:43]** implemented okay the very last thing that I want to cover in this video is a list of upcoming changes including a couple that are really really high priority that I want to have implemented ASAP to make this truly a robust project here so the first one that I want to

**[0:11:59]** call out is that someone has already implemented a poll request for a big issue with bolt where it loves to rewrite files or sometimes entire projects so it's a bit of a larger change so I still need to do the pull request here but I want to call out this

**[0:12:12]** has already been done it's just not merged yet then we get to a few of the really really high priority items these are things that like if could be implemented like today would make this project like two times better 10 times better I don't even know because there's

**[0:12:26]** a lot of possibility here larger changes overall the first one is better prompting to make this work for small or large language models a huge issue right now when you use models that are especially like smaller than like 30 billion parameters or even 70 billion parameters is the code window doesn't

**[0:12:43]** always start so you prompt the llm to make an app for you and it'll just act like a regular chat widget where it doesn't open up the web container on the right side of the interface and that's a huge problem because one of the big goals of this project is to make it

**[0:12:56]** possible to use any llm including local ones and sure there are local ones that are big enough to do this but for a lot of people's Hardware they have to use smaller ones and so it is so important for me to figure this out it's going to be one of the more challenging parts of

**[0:13:10]** this project but it is high priority because it is a big deal also the open- source version of bolt. new does not Implement image attachments by default that's something that they have kind of close source for their official version and so we need to add that because that

**[0:13:23]** would be a great addition uh the last high priority item is more General we could take this in a lot of different ways I'm super flexible and open to whatever you might want to implement but being able to actually run agents in the back end as opposed to just calling a

**[0:13:38]** single model because right now you select your model like Cloud 3.5 Sonet and you just send a single request in get a a response back and then that has all the artifacts and stuff that you display in the web container but there's there's no like actual agentic workflow

**[0:13:53]** behind the scenes where you could have multiple different models interacting together or have different processes for like Chain of Thought and self-re ction and self-improving behind the scenes before a response is given there is millions of things that you could do with agents in the background and so

**[0:14:07]** this is like probably the most exciting thing for me honestly out of everything in this list that is yet to be implemented is using agents in the background and again this can be done in so many different ways and so if you are inspired to make a change make a poll

**[0:14:20]** request for this I'm so open to whatever you might want to do with agents whether you're going to use Lang chain or swarm or llama index or crew aai like it doesn't matter to me totally custom just make an awesome po request and I will dive so deep into that and make sure

**[0:14:35]** that we get that integrated um then we got some Integrations that are still left to do with other llms like LM Studio together Azure open AI hugging face and perplexity um so any of these would be awesome also the open AI like integration could apply to some of these

**[0:14:51]** as well so it's something that I still want to look into or we could look into as a community and then yes just a couple of other features that' be really nice that I'll cover really quickly here being able to deploy directly to something like versell or netlify would

**[0:15:03]** be super cool um being able to load projects into the apps maybe even having like a two-way sync with a local folder um would be super cool the ability to revert code to an earlier version so if you are working with Bolton and it like messes up and you're like oh just go

**[0:15:18]** back please you can kind of do that with the prompting right now but usually it doesn't quite revert fully uh so that would be great prompt caching Just For Speed the ability to enter API keys in the UI so that you can spin this up and not actually have to go and create thatv

**[0:15:33]** file um and then also having the llm plan the project in a markdown file so that that would be like a part of the file structure like it'd be one of the files there so you can kind of see its thought process behind the scenes and it also might lead to better results

**[0:15:46]** because it' kind of be like a Chain of Thought enhancement as well so that is everything that we got right now if these three got knocked out in the last in the next like week or two that would be insane so that's kind of what I'm crossing my fingers for here and I'll

**[0:15:59]** I'll work on contributing myself um but yeah at this point I'm definitely like kind of taking on the role of just like organizing everything together but I would love to contribute more as well so yeah that's everything as far as future work and what we got coming up all

**[0:16:11]** really really exciting stuff so there you go that is everything that is happening with this bolt do new Fork it sure is a lot but I am loving it and I'm so excited to see where we continue to take this project as a community and I'm going to be continuing to provide a lot

**[0:16:26]** of updates as I get the community going as more features rolling in as we plan more things as I get some applications for core contributors yeah I'll keep you up to date on all of that so if you're looking forward to that if you're excited to get updates on this fork and

**[0:16:39]** use it for yourself I would really appreciate a like and a subscribe and with that I will see you in the next video
