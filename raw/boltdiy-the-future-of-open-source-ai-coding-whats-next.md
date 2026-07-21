---
type: raw-transcript
title: "bolt.diy: The Future of Open Source AI Coding - What's Next?"
youtube_id: aZn8PhqUZVU
url: https://www.youtube.com/watch?v=aZn8PhqUZVU
slug: boltdiy-the-future-of-open-source-ai-coding-whats-next
published: 2024-12-18
duration: "0:20:48"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** last week I announced that my platform automator is partnering with stack Blitz to make bolt. DIY the official open- Source bolt. new and with that announcement our community and project completely blew up and I could not be more pumped but just as important as making this partnership with stack Blitz

**[0:00:19]** is keeping up the momentum so that we can slingshot this opportunity into truly building the best open source AI coding assistant which by the way if you want to be a part of this incredible project come join us at our community over at think tank. automator doai and

**[0:00:34]** check out the URL bolt. DIY and we are definitely moving fast so in this video I share with you some updates resources and a revamped road map to help keep you in the loop with all the incredible things going on with the project we as a team have been thinking very long term

**[0:00:51]** with bolt. DIY and a lot of the features that we want to implement things like a prompt library to work with different llms better and a plug-in system to make bolt. Di Y super extendable and a lot of the team has also been working really really hard building up a set of

**[0:01:06]** resources for you to help you get started with bolt. DIY host it yourself and troubleshoot common issues and I showcase all of that one of the biggest tasks that we are working on besides just pumping out more amazing features with you and for you is improving the quality of our repository things like

**[0:01:23]** organizing PRS setting up releases improving the stability of the project to really take the maturity of Bolt do DIY to the next level obviously a ton of exciting and really important stuff going on so let's Dive Right In all right the first thing that I want to showcase for you to help keep you in the

**[0:01:40]** loop with everything going on is our bolt. DIY road map and since this is an open source project there's no timelines here uh this is totally subject to change as we work on casting the vision together for bolt. DIY but having this road map is really really important for

**[0:01:56]** that just so that we have a sense together where we are actually taking bolt. DIY so I'll have a link in the description to this road map it's also in our readme and our documentations really all over the place because this is a pillar guiding us as we are moving

**[0:02:10]** along with the project and so to start I've got the Genesis of bolt. DIY back when it was called bolt. new any llm adding the ability to use different llms then we go down the road map here for all these things that are finished like creating the core maintainer team

**[0:02:25]** launching our community improving our documentations and FAQs and getting kind of a V1 up for that improving our repo like with cicd and issue templates and releases all these things that we've set up quite recently act actually to create a strong foundation for our project and then kind of fun here I added in become

**[0:02:43]** the official open source bolt. new which obviously that happened just last week super super exciting and before I put this here I actually had uh get crowdfunding for the project like financial support for contributors and different PRS and the reason I replaced that with this is because the

**[0:03:01]** partnership with bolt. new does also come with financial incentives for the project not for me but for the project because we're going to be working with stack Blitz to do things like host events with prizes cash prizes to incentivize contributions to bolt. DIY so a lot more coming on that soon but

**[0:03:19]** that's why I put this in here instead of crowdfunding and then we also had a bunch of really high priority features that we knocked out over the past few weeks here so I'm not going to dive into all these here but a lot of things like loading local projects in GitHub

**[0:03:32]** attaching images to prompts which I'll Showcase in a little bit here with some additions to that uh and then also a lot of things for settings and just getting our project more mature overall and I'll dive into some of those things when I go over new features as well and then we go

**[0:03:47]** down into the rest of our road map here things that are yet to be implemented and this is where we really dive into what is next for bolt. DIY now that we have this partnership with stack Blitz things are going really really well for the project with engagement what do we

**[0:04:00]** want to take this momentum into what features do we need one of the first big ones is adding in a prompt Library it has become very very obvious as we have been working on bolt. DIY together that different llms need different prompts the original prompt created for bolt.

**[0:04:16]** new stack Blitz very much made specifically for clae 3.5 Sonet just doing a ton of trial and error tweaking little things to make it so that it understands the the config for vit and tailwind and how to structure the project projects and all of that and other llms that might be actually almost

**[0:04:33]** as powerful don't do as well because the prompt just isn't made for them and so if we can get some sort of Library where it's like if you're using the quen family or if you're using llama 3.3 or if you're using Gemini here's the prompt that you want to use and then also

**[0:04:46]** making that very adjustable and extendable as well and then obviously one big one that people are asking for a lot is having file walking and diffs like commercial bolt. new especially to make it so that bolt. DIY doesn't have to rewrite files as often and this is something I definitely want to work with

**[0:05:03]** the stack Blitz team now that we're partnered with them to figure out how we can implement this into bolt. DIY just like they did for commercial bolt. new so more to come on this soon as well also we want a one-click deploy to netlify that would be super super sweet

**[0:05:18]** another thing that we want to do just to help organize our repository better is have a can band styled board to manage our PRS especially the high priority ones just so that we can hit kind of like a a board for us to see at one glance what are the things we're working

**[0:05:31]** on right now as a team as a community what are the things that we are not yet but we have as high priority and then maybe a backlog just that kind of organization to help really keep us moving along getting all of these things implemented and then the other thing

**[0:05:44]** that I alluded to at the intro is building a sort of plug-in system to make bolt. DIY super extendable and that is what this extension Marketplace is right here and along with that there's a lot of different components we need to it like an a backend to handle the

**[0:05:58]** extension library and integrate it with bolt. DIY a front end for people to post their plugins and a front end for us to manage them kind of as administrators as we big bring plugins into the ecosystem a lot that goes into this but the beauty of this feature right here is it's going

**[0:06:13]** to make it so easy for people to contribute features on top of bolt. DIY without having to also edit our repository and make a poll request and that's also going to mean that we can avoid feature bloat as well so as we have all these features getting added we

**[0:06:29]** can make them to leble so it's not like you have 50 different features all with their own buttons in the UI that would end up just making it very confusing for us we can still have our foundational bolt. DIY but then through the marketplace have all these neat little

**[0:06:41]** things that we can add on to it like some of the things that we have down here like being able to upload documents before you start prompting bolt. DIY to give it extra knowledge uh you can maybe have better planning where maybe before it even starts to code anything it

**[0:06:56]** starts with a reasoning model like qwq it reasons about what it wants to produce based on your prompt puts that in some sort of readme or markdown file and then starts coding that kind of pre-planning Step could be really awesome as a plug-in as well and then also a super base integration kind of

**[0:07:12]** like commercial bolt. new is working on and then the last thing that I have on the road map for now and again this is going to be extended a lot as we continue to cast Vision together as a community the last thing that I have here is maybe some sort of plugin where

**[0:07:24]** you could have agents behind the scenes like a mixture of experts that create the code instead of just a sing single call to a single llm that would be super cool probably a huge opportunity there to use smaller llms as well to work together to get some better results

**[0:07:38]** because obviously right now with bolt. DIY we don't really get the best results with smaller llms especially if they're 7 billion parameters or less but if we have some sort of agentic system in the back end that would open up so many possibilities for more power for the

**[0:07:52]** project overall and using smaller llms so that's everything that I got for the road map right now again this is open to a lot of change anyone can contribute their ideas to the road map here and we're constantly going to be evolving this as we're building the best open

**[0:08:06]** source AI coding assistant today's video is sponsored by lizer which by the way if you're curious how I'm able to do so much for bolt. DIY with no Financial incentive for me sponsorships are one of the big things that make that possible and I'm genuinely excited to bring lizer

**[0:08:21]** to you today because they are solving a massive paino for Enterprises trying to implement Ai and they do that with their agent Studio look we all know that building AI agents can be very complex whether you're trying to build your own rag Pipeline connect your agent to third

**[0:08:36]** party services or work with AI automation tools but lizer with their agent studio is completely changing the game you can create entire AI agents that are Enterprise level without a single line of code they have a really easy to use agent API to create your agents with just a few lines of code if

**[0:08:53]** you are a developer they have a ton of pre-built agents and they make it very very easy to integrate with third party services like Slack and Gmail what makes lier truly stand out is it's agentic approach and commitment to AI safety and reliability the Asian studio is built

**[0:09:08]** directly on Laser's no code agent framework which is the first and only framework that truly and natively supports AI safety and responsibility which that's the kind of thing I would definitely go read up on if you're curious to learn more this not only means that you can build poc's very fast

**[0:09:24]** with lier but you can also build reliable and Enterprise grade agents lier truly does offer UT most customization for everyone for developers they can very easily build their agents access API endpoints and integrate with existing software and then for business folks on the other hand they can very easily without coding

**[0:09:41]** at all create agent co-pilots and build apps around them very very quickly if you want to transform how you build your AI applications definitely check out the lizer agent Studio I'll have a link in the description as well their documentation is fantastic and you can literally have an AI agent up and

**[0:09:57]** running in just minutes next up one thing that a lot of you in the community have been requesting is more resources to help you get started with bolt. DIY host it yourself troubleshoot common issues and the works and we as a maintainer team have been working really hard on getting those resources for you

**[0:10:14]** and Dustin one of our team members is one of the people who has done a great job with that so he has this post here in our automator think tank with some resources to help you get started with bolt. DIY so they're here over on his channel he's got a link here I'm going

**[0:10:27]** to link to this in the description of the video by the way as well as well as the other resource I'll share in a second but he's got some videos helping you use bolt. DIY once you have it up and running and then also how to get it

**[0:10:37]** running on Ubuntu and Windows the windows one doesn't have audio so you'll have to just watch along and see how he's running the commands but he makes it very easy to get started and we are also working a lot on our documentation here so in the read me I'll scroll down

**[0:10:51]** to where we go over how to run it we've simplified a lot of these steps here for you for every every operating system making it super super clear how to run things both with Docker and without Docker so we've got more resources we're just making our documentation easier to

**[0:11:06]** understand in general and continuing to work on our Docker setup and things like that just to make it easier to run even aside from all the documentation helping you out more and then the other resource that I want to share also in our automator Think Tank here Michael

**[0:11:21]** another member of our core maintainer team made a really really awesome and comprehensive guide on how to deploy bolt. DIY with cloudflare pages so if you want to host bolt. DIY yourself so you're running it yourself but not on your local computer cloudflare is the recommended way to go about it there are

**[0:11:40]** other platforms like kify that a lot of people want to deploy to but this is honestly what I'd recommend this is the guide that I'm going to keep pointing people to because Michael has done a fantastic job with this and it is a very very long guide here um but mostly just

**[0:11:54]** because there's a lot of images and also because he's super detailed with everything here so that we when you go through this you can be confident that you're going to get all the steps that you need to run this yourself with Cloud Player and then in the end it's really

**[0:12:06]** less than 20 steps so it's not going to take you that long and it's definitely worth going through this if you want to host bolt. DIY yourself have a URL that you can use for yourself and share with your friends and other people as well and this is not going to work with olama

**[0:12:19]** because it's not like your site can connect to your local computer there's still that back in making the requests to the large language model that would usually be running on your computer but all the other providers are going to work you can set your API Keys directly within the UI and he talks about that

**[0:12:33]** too great resource so thank you Michael for that thank you Dustin for the resources to get started with bolt. DIY and a lot more resources to come soon as well just to continue making the barrier to entry very low for bolt. DIY so you can get involved try it out yourself get

**[0:12:49]** excited with it join our community and help contribute and make this the best open source AI coding assistant all right we've gone over the road map for bolt. DIY and the direction we're heading with the project and also given you a bunch of awesome resources to get started yourself and host it yourself so

**[0:13:04]** now we can go on to the new features that were added to bolt. DIY cuz there are a ton of insanely cool new things like usual and then also a couple people that I want to call out specifically for the insane amount of work that they have put into bolt. DIY recently we are

**[0:13:19]** really chugging along here with some amazing new things for the project and so I'm going to exit the full screen here because there are a few GitHub tabs that I want to go over here the first one is this page showing all the recently merged PO requests and within

**[0:13:32]** our first page here it only goes back to 3 days ago which is insanely cool this entire page is just in the last 3 days so so much work is going into the project the momentum we're getting from the stack Blitz partnership is insane and it's carried out by also a couple of

**[0:13:49]** very specific people here so if you look through this first page almost all of the poll requests are by Dustin he's one of the members of our core maintainer team and then also on your bond the Kodak kiss and so both of you guys I just got to shout you out just looking

**[0:14:04]** at this first page right here seeing your name so much thank you so much for all the work that you're putting into uh creating things for bolt. DIY and helping to maintain it as well and a huge thanks to the entire maintainer team and I'll showcase some of your

**[0:14:18]** stuff as well but I just have to call out you to looking at this first page here and even going on to like the second page and the third page seeing your name so much a lot of other awesome additions from other people as well I wish I could cover everything but man

**[0:14:31]** there is just so many things even in the last week after the partnership with stack blitz so thank you everyone for all the things that you've been contributing we've got releases now as a part of the repository official releases that are automatically generated with a change loock through cicd thank you on

**[0:14:47]** your bond for that so many awesome things a couple of poll requests that I want to go through specifically what I'm going to actually do for that is I'm going to build an app within bolt. DIY and then call out specific things things and then go and show the the pull

**[0:15:01]** requests for that as well um and so the first thing that I want to do is Showcase this new setting model that we have that has so many awesome features to help improve the maturity of our project so if I go to the settings in the bottom left here we have this whole

**[0:15:14]** new model with all these different options here like you can toggle providers on and off so you don't have this huge bloat of providers uh you can set your connections and things for GitHub and we have features here like um the codus anuron also implemented an optimized prompt an experimental prompt

**[0:15:31]** that is basically working on top of the current default system prompt for bolt. DIY to get better results just kind of still testing us out but yeah this experimental feature place is going to be a test bed for a lot of incredible things for the project Dustin and onir

**[0:15:47]** bond have been doing a ton of work on this whole settings model and what he did specifically here is he made this awesome debug tab so let me go back and show that quickly here so if I toggle the debug features right here I now have this tab where I can see all of my

**[0:16:02]** system information it even tells me if my connection to AMA is working this is just awesome and so this is exactly what we need to help people troubleshoot issues so along with having better documentation in the think tank and the in the readme and everything for debugging we also have this you can copy

**[0:16:18]** your debug info and then paste it into a troubleshooting post so we can better help you so this is just so important for us as we move along and get more and more people involved with the project so thank you thank you so much Dustin for that and then I already covered this one

**[0:16:32]** right here the configurable system prompt feature where onbon implemented that experimental he's got a video on this right here he even shows like how it works with different LMS which is super cool but yeah that experimental system prompt that I'm not going to dive into what was changing the prompt here

**[0:16:47]** specifically um but that is this thing right here where we have this optimized prompt that is experimental um and so I'm going to toggle that off for now just so that I can show the base Behavior here as I make an app but yeah let's just build a simple react uh

**[0:17:03]** Tailwind to-do app and then I'll showcase some of the other features that we got once we actually have this app created so the first thing that I want to showcase here Edward another one of the maintainers who has done an awesome job with helping us with bolt. DIY

**[0:17:18]** overall he implemented the ability to see token usage for every single prompt which is super important if you're not using ol or LM Studio or any free llm you want to see or at least get a rough estimate how much you're actually paying as you're working with bolt. DIY and so

**[0:17:34]** this makes that possible like he has this example right here where it tells you how many tokens for the prompt and then also the output from the llm the completion how many tokens for that as well so let me go back over to our app right here yep it made the two two app

**[0:17:47]** for us and if I scroll up here we go 6,000 Tokens The Prompt was 4,000 which includes what I said and then also everything behind the scenes with the system prompt and then also the completion it was about 2,000 tokens for all the code that was outputed and all

**[0:18:00]** the commands that the llm decided to run so that is freaking awesome and then also Jonathan he implemented the ability to full screen and resize the preview which is super cool so if I click this button right here I can now full screen this so it really looks like I'm working

**[0:18:14]** with a full website instead of just previewing what I have right here within the web container so that is really awesome this is a much needed feature as well especially when working on smaller devices so thank you Jonathan for that and then the last thing that I want to

**[0:18:27]** cover right here there's again so many features I can't cover them all um but Ed another member of our maintainer team he recently added the ability to screenshot a certain part of the preview and send that into the llm which is so so useful because when it messes up

**[0:18:43]** something instead of having to you know describe here what exactly it messed up you can actually go and take a screenshot of it so watch this I'll take a screenshot and I'll just drag it like this kind of like the Snipping Tool in Windows and then it'll ask you to share

**[0:18:56]** your screen so I'll just share this right here and then boom there we go we now have an image in the chat in the bottom left here and I can say what is this an image of I just want to like you know kind of test and make sure it

**[0:19:07]** actually understands this image and there you go it understands that it is an interface for the to-do app that it just implemented so perfect this is an absolutely phenomenal feature because you can tell it like boom here's a snippet of something that you messed up please make it look like this instead

**[0:19:21]** for example so a really awesome tool to work with the UI and also maybe you can take a snippet of errors and stuff as well within the web container here so awesome features overall so much more that I wish I could cover but these are some of the core things just to keep

**[0:19:33]** getting you excited about everything that's being added to bolt. DIY the very last thing going along with all these new features is if there's something that you want to have implemented in bolt. DIY that's not in the road map it's not in one of these PRS that I just

**[0:19:46]** covered post it here right here in our automator think tank we have a subcategory for bolt. DIY called new feature discussions give your idea here or even better make a pull request implement it yourself and will bring it in to the repository so if you really want to contribute that's what we

**[0:20:03]** encourage the most but also if you just want to throw out an idea and get a discussion going around it post it here and we'd love to chat with you more about the ideas that you've got I am really only scratching the surface here with everything going on with bolt. DIY

**[0:20:16]** and now could not be a better time for you to get involved we are truly building the best open- source AI coding assistant as a community and would love to have you be a part of it and so if you are looking to join an awesome Community working on an amazing project

**[0:20:31]** that you can do incredible things with head on over to think tank. automator doai and join us if you appreciated this content you're looking forward to more things bolt. DIY I would really appreciate a like and a subscribe and with that I will see you in the next

**[0:20:45]** video
