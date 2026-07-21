---
type: raw-transcript
title: "The MOST Profitable AI Niche NO ONE is Talking About"
youtube_id: 1lvAvLXXA10
url: https://www.youtube.com/watch?v=1lvAvLXXA10
slug: the-most-profitable-ai-niche-no-one-is-talking-about
published: 2024-08-21
duration: "0:16:22"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** recently I have found an absolute Gold Mine of a niche for AI agents for you to build either your own SAS product or to help other businesses as a consultancy today I'm going to show you what this Niche is how it is a game Cher for you and I'll even show you a powerful AI

**[0:00:16]** agent that I've created myself in this Niche that is making a good amount of dough I am just going to cut right to the chase this Niche is building AI agents for an incredible platform called go high level go high level is essentially a CRM for marketing agencies

**[0:00:31]** it is a massive Suite of tools to help agencies streamline things like landing pages lead capture lead nurturing email campaigns invoicing marketing automations Google reviews appointment scheduling and a lot more okay but why go high level why pick a specific platform for a niche for building AI agents it's a bit odd I'm going to be

**[0:00:52]** totally honest but that is actually the beauty of it hear me out here I have been using go higho for over a year now and I can honestly say that there is nothing like it it is an amazing platform but what you might be wondering is if go high level does all these

**[0:01:07]** things that I mentioned earlier wouldn't that mean that it's going to be the Jack of all trades but the master of none and to an extent that actually is true but here's the thing that is exactly the opportunity that you have here go high level is way more than just a platform

**[0:01:22]** there are thousands of businesses that are literally built around go high level and all the features that it provides but I can tell you from personal experience working with agencies that there are a lot of opportunities to extend the functionality of go high level to fill in the gaps because it is

**[0:01:38]** the jack of all trades and the master of none especially when it comes to ai go high level has done some integrating with AI more recently but it has definitely fallen short go high level also has an incredible API so it is so easy to extend the platform like their

**[0:01:53]** API is so good that you would think that they are a developer first platform it's constantly being updated and improved on top of that go high level makes it possible to create custom apps very easily with their app Marketplace so they're literally encouraging us developers to build these kinds of

**[0:02:09]** things that I'm describing and also these Marketplace apps make it really easy to handle authentication if you're building a SAS integrate with their API set up web hooks to handle events on the platform and also to manage permissions to make your app really secure okay so just stop and think about this with me

**[0:02:27]** for a second here we have this incredible platform that is thousands and thousands of businesses making millions of dollars on it and it has all these different features but each one of these are just this far from perfect where they're good but there's an opportunity for you to come in and build

**[0:02:43]** AI agents to make them better and make a lot of money it is just the perfect storm because on top of that they have an incredible API in an app Marketplace to encourage us developers to make these things you couldn't have a better combination and so there's no clickbait

**[0:02:57]** here when I say that I have literally found the gold mine for an AI agent's Niche there is even a 14-day free trial for go high level so I'd highly encourage you to take advantage of that explore the platform do some research and I promise you you will find dozens

**[0:03:12]** of ways to extend the platform with AI and very practical ways I'll even get really specific here to get your juices flowing to think about ways you can build AI agents in go high level one of the biggest things for marketing agencies is to reach out to as many

**[0:03:27]** people I.E leads as possible as fast as possible with as much personalization as possible that is the name of the game for digital marketing speed volume and personalization and guess what is really good at doing this if you do it right that's right it's ai ai agents are just

**[0:03:45]** the perfect solution for personalized lead nurturing at scale essentially just having a ton of conversations with all the people that have given you their information in an ad or a landing page your goal could be to have them purchase a product schedule an appointment book an event whatever it might be and every

**[0:04:02]** single business needs this it doesn't matter if you're a solar panel company a roofing company a chiropractic office a personal trainer whatever it is your business relies on nurturing these leads and an AI agent is going to help you you can find all these businesses on go high

**[0:04:18]** level there are a ton of opportunities to build different things in go high level but in my humble opinion this is one of the biggest opportunities and in fact this is exactly what I created an AI agent for leading nurturing and go high level that uses laying chain laying

**[0:04:33]** graph and pine cone for Rag and I'll show you exactly how I did it so you can just steal this from me for your SAS or your clients all right so here's what I'm going to do first I'm going to walk through what it looks like to create an

**[0:04:44]** app in the go high level Marketplace and then we'll dive into the code and I'll show you a bit of what it looks like to create this AI agent that I've made for lead nurturing and go high level so first of all I wanted just to show The

**[0:04:56]** Marketplace apps that are available for public use at this point there are a ton out there in fact there are even some that are out there specifically for lead nurturing already now the reason you'd still want to create something yourself is there are one a ton of opportunities

**[0:05:11]** to prove upon existing software that's out there also there are always going to be competitors no matter where you create a SAS or any kind of product and so this shouldn't deter you on top of that if you're doing something more like a consultancy model you're going to be

**[0:05:26]** working with clients that have very specific needs that you're going to be building software for lead nurturing for that something more generic like this for example wouldn't necessarily be able to solve so that's just a little Spiel I've got on why you'd want to do this even though there might be some things

**[0:05:40]** kind of like it already uh but anyway it's just cool to see this Marketplace in all the different ways that you can extend go high level already with things that are already built but then to actually build something yourself it's very very easy you just go to your apps

**[0:05:52]** right here you can click on this button to create a new app and it'll pop up this thing right here where you can create an app just given a name whether it's private or public and then a couple of other options right here so at this point my app is just a private app

**[0:06:03]** because I've been using it internally for an agency and helping us boost our Revenue a lot and save us a lot of time we can also make it a public app to share as well if you were to make it more of a full-fledged sass that you're going to be marketing to other agencies

**[0:06:17]** using go high level so once you create it here the one thing that I wanted to show that's super super cool is how easy it is to handle web hooks within the platform and create your own custom code to handle the web hooks like I did for myself so you give a web hook URL in

**[0:06:33]** your app I'm just in the settings for my app here and so this is just like a uh Google Cloud function URL that I have here so anytime that there is an inbound message which is an SMS message or an outbound SMS message I just have these two things ticked here it'll send a

**[0:06:49]** request to this endpoint right here so I can have any code that I want to handle it and that's where I have my AI agent that is going to handle inbound and outbound messages to be that lead moning bot for my agency so really really powerful stuff and you can see here that

**[0:07:05]** it's super easy to set up you just create an app and then you've throw in a web hook URL here and choose which events you want to trigger it and then you're good to go and now we can go on to the code and see how I handle these

**[0:07:16]** requests all right so I want to start off right away by saying that this is a very broad overview of this AI agent that I've created for lead nurturing and go high level I want this video itself to be more focused on how go high level is an amazing Niche for building AI

**[0:07:29]** agents if there is a lot of interest in this I will definitely go through this code in a lot more detail and fully give away all of my secrets so the whole front end that I built for this product I don't have the code available at this point but I'm not trying to hide

**[0:07:43]** anything I just don't want to throw everything out there at once because this is actually a pretty complex product overall um but I'm definitely down to give away all my secrets so like I said if there's more interest in this I will make videos on this in the future

**[0:07:54]** to extend what I'm showing here so with that being said there's a link to this code that I'm about to show uh in the description of this video a GitHub repo so you can feel free to check out the entire backend for the AI agent that I've made with go high level so yeah

**[0:08:08]** just a bit of a broad Overview at this point to show how powerful this thing is so like I showed earlier we have that web hook that I set up in my Marketplace app um and so whenever there's a text message that comes through in a go high

**[0:08:21]** level account it is going to hit this endpoint right here we also have an emulator endpoint to test the different agents that you can make for your clients and then also an endpoint to update our knowledge base our Vector database with pine cone to handle any FAQs that we'll have for our clients as

**[0:08:37]** well and so the way that this whole application works is you have different agencies that all have separate agency go high level accounts they can come into my platform Here sign in and then connect different agents to different clients that they have which are basically going to be sub accounts

**[0:08:55]** within their main goal high level account and so they might be a digital marketing agent gency that has a solar panel company they're helping out and a chiropractic office they can create a separate agent for each that both have different prompts maybe even different models a different temperature whatever

**[0:09:11]** it might be so you can configure custom agents for different clients that you have all within sub accounts and go high level so it's very powerful and dynamic stuff and so when a text message comes through into the platform it is going to be for a specific contact in a specific

**[0:09:27]** location I.E sub account within a single agency and so my endpoint here which is just a Google Cloud function that uh receives the web hook request from my go high level app it does some authentication and then it fetches the company ID which is basically just the agency and it fetches the location ID

**[0:09:47]** which is their contact and then it does all the authentication and then what it does is it determines the agent that is tied to that contact that just sent a text message and that's through tagging so it's something you do in goal high level where you have some automation workflows

**[0:10:03]** that can put specific tags on leads and that's what determines what agent actually applies to that specific contact so even within one client like let's say the solar panel company you're helping you could have different ads that you want to nurture in different ways and so you can have different tags

**[0:10:19]** on different leads and set up different agents within my platform here that I call textually um to nurture these leads in different ways and so it's super super robust and I know I'm doing a lot lot of talking here but there's just so much involved in this platform which is

**[0:10:33]** why I'm not giving away all the code all at once even though I'm definitely down to do that if there is interest so anyway determines the agent that is tied to this contact which is going to determine the prompt and the actions what calendar to use and all that good

**[0:10:47]** stuff and then it sends it into my Lan graph endpoint so I've built a full Lan graph executable that does this lead nurturing and has all the tools tied into it to interact with go high level to send the text messages to add tags to cancel appointments to book appointments

**[0:11:03]** all these things are set up as tools that I bind into my L graph executable so I have basically a tool to add tags which again that's just a construct in goal high level uh a tool to remove tags a tool to uh invoke a generic web hook

**[0:11:20]** and so you can set it up to when something specific happens in the conversation it can invoke a custom web hook I have a tool that fetches calendar availability so if you're having a conversation with the lead and they're asking about availability or you just determine you need to offer times for a

**[0:11:36]** call it would call this tool a tool to cancel appointments and then also to book appointments and so everything that you would need all the actions you would need to have a full conversation to lead to a booking or to send a link to purchase a product whatever it might be

**[0:11:51]** this is all that that you need as far as tools go for this and the way that I set up my platform is for every agent you can Define custom actions as so you can say something like when the lead says they interested in Booking an appointment then you should you know

**[0:12:06]** call this tool to get the availability and once the time is confirmed then you would call this tool and so you can use natural language in the front end I've developed to define the custom actions and tell the large language model specifically when to use all of these

**[0:12:21]** tools and so it's very very robust and unique to the needs that you have because you might not want to text availability for a call at the same time that a different agency might you have unique needs on how the conversation should be directed and all of that can

**[0:12:35]** be handled with this um so yeah it's a very robust application overall um and all these prompts are built up very dynamically so in this function that I have here this is kind of the entry point to calling the L graph executable um first I get the agent which is going

**[0:12:50]** to include everything like the prompt and the actions and all of that and then I get the prompt from the agent and I build it up with everything that I need to apply so for example I use rag here I'll even show that right here I have this function ask Vector database

**[0:13:03]** questions so it gets the FAQs um that you can put into my front end to answer common questions so it'll put that in the prompt and then there's extra context you can give about the location like the address or their office phone number things that would be used to

**[0:13:17]** answer questions as well that's injected in the prompt and then all the actions I mentioned are injected in the prompt some date information so it doesn't hallucinate dates which is something that's really really important for lead nurturing especially with brick and more to businesses that have visits scheduled

**[0:13:32]** uh and then things like the time zone as well all these things are crafted into this Dynamic prompt and then the whole base prompt giving it the goals and things to do and things not to do all that is configured in the front end as well and so in the end you have this

**[0:13:45]** massively useful prompt that has context and FAQs and instructions and actions and date context all this stuff that is then put into the Lang graph executable to generate a response basically the text message just send back to the lead and then also um to call any tools that

**[0:14:04]** are necessary to do something like book an appointment and so uh yeah I'm not going to show all the code for this because there is definitely a ton here especially in this U helpers file that I have right here for all the different uh functions to help with the tool calls

**[0:14:17]** and stuff there is so much code here i' I've poured months and months into this thing um because like I said I found this Niche relatively recently but it it was this year um so I had a good amount of time to build this thing out to help

**[0:14:28]** with the agency that I've been working with um with their lead nurturing um so yeah it's super cool stuff and yeah all these tools can be easily extended as well so I've even thought about other tools that I could have to like request Google reviews after an appointment

**[0:14:43]** things like that like there's so many different ways that I can leverage all the tools that are already in go high level like I've been mentioning and add that into this lead nurturing AI agent so yeah like I said all the code that I have uh for this I'm just going to have

**[0:14:56]** in this go highle SAS backend folder and my AI agents masterclass GitHub repo that I've just been shoving all of my code in to just make it very value packed for you guys um so yeah all the code is going to mostly be in the source folder right here so functions because

**[0:15:11]** this is uh basically just like the general folder structure for Google Cloud functions so you have like your initial U Firebase stuff and then within functions here you have the source which is going to have all these um JavaScript files that I've been showing the code for um so yeah that's everything at this

**[0:15:29]** point I would highly encourage you to explore this repo if you're curious about these things and let me know in the comments if you want me to dive into this in more detail in future videos especially showing the whole front end that I've created U for testing these AI

**[0:15:42]** agents and configuring them with the prompts and the actions and all that I'd love to show all that as well cuz like I said I'm not going to hide anything with this that was a lot of code to cover I would highly encourage you to check out the GitHub repo and really dive into

**[0:15:56]** this and glean what you can from it because I have spent months creating this AI agent for lead nurturing and go high level I hope that you found this to be a really powerful Niche that you'll explore because I definitely have found a lot of value creating AI agents for go

**[0:16:09]** high level both for me and also the businesses that I've helped out through this and so I hope that you found a lot of value in this video if you did I would really appreciate a like and a subscribe and with that I will see you in the next video
