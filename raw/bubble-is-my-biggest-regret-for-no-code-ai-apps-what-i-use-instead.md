---
type: raw-transcript
title: "Bubble is My BIGGEST Regret for No Code AI Apps - What I Use Instead"
youtube_id: rbVp40BIBBs
url: https://www.youtube.com/watch?v=rbVp40BIBBs
slug: bubble-is-my-biggest-regret-for-no-code-ai-apps-what-i-use-instead
published: 2024-09-20
duration: "0:12:02"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** let's talk about no code AI app Builders because there are a lot of no code platforms out there that allow you to create AI agents and a lot that help you create websites but there are not many that do both and actually do it well and let's face it if you want to build a

**[0:00:15]** full stack AI application without coding anything you definitely need both sides of the coin now what most people do is they just go to one of the more popular app builders that are starting to integrate with generative AI like bubble I'm sure you've heard of bubble before but here is the big problem with these

**[0:00:31]** platforms they have a ton of hidden fees and you start to blow a huge hole through your wallet the second you really start to scale your AI application and I'll even show later on in this video an example of how bubble charges you out the wazu and drains your

**[0:00:45]** bank account from under your nose this is a big problem but I have actually found an awesome platform that solves this and makes it so easy and affordable to create full stack AI applications with no code and this platform is M moment makes it possible to build complex AI agents with rag tool calling

**[0:01:04]** Dynamic prompts all the works and integrate it into a front end with their robust website slapp builder you can even manage your databases your API connections for tools and build workflows in their workflow Builder all within the platform it is pretty awesome and I'm going to briefly show you

**[0:01:20]** everything I found moment pretty recently and I just had to reach out to them because you need to know that you don't have to pay for platforms like bubble when something like this is available and so I'll first show you why you'd want to pick M over something else

**[0:01:35]** and then I'll show you very briefly how I built a full AI agent in the platform using all of the really cool features that I mentioned just a bit ago all right I'm going to keep picking on Bubble here because it really is just a good example it's one of the most

**[0:01:48]** popular no code app Builders and most of the other ones are going to have a similar pricing structure in the same hidden fees and that is what we're going to look at right now and so on the pricing page for bubble it seems nice that first you're paying a predictable

**[0:02:02]** certain amount of money per month even with a nice free tier here but it breaks down when you look into the details of each of these plans so if I click on the full comparison and I scroll down to the infrastructure here you can see that the number of operations that you can make

**[0:02:16]** in your application they call them workload units that's things like uh requests to your database or API calls any of those operations you're limited in the number that you get before you actually have to start paying per 1,000 workload units and let me tell you your application is going to hit this limit

**[0:02:34]** so so fast because every time a user of your application refreshes the page or goes to a different page there's going to be multiple workload units that are expended to call apis and make database operations every single time they load the page and so you'll hit this limit

**[0:02:50]** and then you're going to start paying 30 cents for every 1,000 times that there's any interaction with your apis or databases and that adds up so so fast I have even seen websites where every time a user reloaded the page it costed like 10 cents for that bubble built

**[0:03:06]** application absolutely ridiculous it makes the pricing not predictable and that is not good but what I'll show you here I'll contrast this with the pricing for moment moment is entirely predictable for their pricing because instead of paying per workload unit or per time that you call a database or API

**[0:03:24]** or whatever you actually pay for the infrastructure and so this single tenant kit is a really good example of how you pay for what you need as far as like cores and memory and database storage and then you are guaranteed that that is what you pay for the month no matter how

**[0:03:38]** many times users refresh your page and make calls to your apis or your databases and so it is 100% predictable in there is so much power to that I would recommend this kind of pricing for you when you choose any platform or service no matter if it's for app

**[0:03:53]** Builders or AI agents or Integrations or task management whatever it is and so having this for your AI agent an app builder is a really beautiful thing and so moment is just great for your pricing all right one last thing on the pricing and then I'll dive into how I actually

**[0:04:08]** built an AI agent with moment so the team at moment they've done a lot of competitor analysis and of course they focus on Bubble just like I am in this video right here poor bubble but honestly they deserve it um so in this test here the team at moment they ran a

**[0:04:23]** bunch of operations with bubble that they were actually able to do on the free tier with moment and it cost it 5,000 W's which comes out to a grand total of $155 so something they were able to do really really quickly on moment took a minute and 18 seconds and $155 on bubble

**[0:04:44]** and that's just absolutely ridiculous if you can do that with the free tier on moment imagine what you can do when you start paying for their infrastructure with their predictable pricing and you are saving thousands of thousands of dollars compared to something like bubble so now I get to show you how I

**[0:04:58]** built an AI agent in moment very very easily and so before I even dive into that I want to show you the landing page for a moment really quick because I confirmed this with them they built their website that we're looking at right here with the moment app builder

**[0:05:11]** it's kind of meta they use moment to build moment but it just shows you that you can use moment really to build any robust beautiful front end that you need to with all the animations that you need I mean this website looks amazing compared to even a lot of other AI

**[0:05:26]** platforms that I've seen um and so all you need to do to get started is just click on their get started it's free button in the top right create your account and you can start playing around they'll give you free AI credits you can use their app builder everything in the

**[0:05:39]** platform that I'm about to show right now and so with that we can dive in and I'll show you everything that I set up for my AI agent and that actually will use each of the different sections of their platform that I mentioned earlier and so starting with the AI I have this

**[0:05:53]** agent that I've created that is going to extract tasks from meeting notes and so basically what my agent is going to do is take take in a bunch of meeting notes that have action items in them and then extract the action items from the notes and allow me to add them to my calendar

**[0:06:09]** and so I'll demo this as well once I show how I've set this up very briefly and so clicking into this AI agent here you have all the configuration that you would typically expect to have for an AI agent so I can select my model my temperature I have my inputs that I put

**[0:06:24]** in for the dynamic prompting and so the meeting is going to be passed into the agent and then added onto the prompt like this right here and so we give a bit of instructions and then we paste in the meeting notes that we wanted to extract the action items from you can

**[0:06:37]** even give roles and constraints there's so many different levels of customization that you have here and then you can also integrate thirdparty apis and data for your tool calling and so you can really make this an AI agent that can interact with the outside world in any way through literally any API

**[0:06:54]** that you want to set up in your API Tab and I'll go to this in a little bit as well and so you set up all these tools you can even use workflows that they have in their action flow tab to add those as tools for the agent as well uh

**[0:07:07]** so it is just so so powerful you can do structured output as well like you see right here everything that you need in an AI agent you can start a conversation on the right hand side here to test all your agent as well so I can dump in a

**[0:07:19]** bunch of meeting notes and test it right here I'll wait to do that until I actually do it in the UI but you can test your agent very easily as well and then for the front end here I'll just show this really really briefly it's anything that you would need in a

**[0:07:32]** website builder so I can click on ADD component you can see here that like all these different components you can add into your website um it makes it so so easy to also make it mobile responsive as well because if I scroll to the right here I can see what it looks like on a

**[0:07:46]** phone or on a tablet obviously I I didn't make this 100% perfect here um but you can make it look really really good on any device that you want which is super super important because more people view your website on a phone than you would think and so it's really

**[0:07:59]** important to do that and so then clicking on any component here there's a ton of customization on the right like you typically see at the website builder and then if I click on this button here you can see that when I Define an action for clicking on a button I'm able to

**[0:08:13]** specify one of the workflows that I have in my moment app and so this is how we can get that integration between the front end and my AI agent that is through the workflow here so if I go into my action flow I have all these different workflows that are created for

**[0:08:27]** the things I need to interact with my Google Calendar and my AI agent and so for my create task for example let me zoom in on this for you here I first get some initial context in this workflow um like I get the meeting notes and then I insert

**[0:08:42]** those into my database so I I even have a database that contains all the conversations I have and the messages and the meeting notes all that good stuff and then uh let me zoom in another time here then I extract the the action items using my AI agent so I call it

**[0:09:00]** directly within my workflow here super super easy store what it responds with in the database and then send that back to the front end to display and also I have all my API Integrations here to manage my Google credentials as well and so yeah to get the refresh token and

**[0:09:16]** then also to actually create that event in my Google Calendar so it's so easy to just set up any API endpoint you want with any parameters that you need and so I know that was super brief but I just wanted to give you a quick overview of what I built and now I'll actually test

**[0:09:29]** it out and show you how wonderfully this thing works and so going over into uh this Google doc that I have here these are the fake meeting notes just something silly I created here that I'm going to paste in and extract the action items from and so I've copied everything

**[0:09:43]** here and then I'll go into my front end that I have in my preview mode here in moment so you can preview anything before you actually publish it which is a really helpful feature and I'll just go ahead and paste in everything that I have here for my meeting notes and then

**[0:09:55]** I'll click on get started and it's going to run that whole workflow there to send these meaning notes into the llm to get the action items from it and then we'll see here that all that is displayed dynamically in this UI very very beautifully I mean the whole UI here is

**[0:10:10]** not like super super amazing looking but it's robust in its functionality and so right here it took the three action items and that's correct there were three in the meeting notes here and it gave me the schedule for each of them and so I can go ahead and actually add

**[0:10:24]** these to my calendar and so you can see here that U just a little bit of like backend debugging here I say when the task succeeded I can add another one here and then I can add the last one boom there we go we've added these all to my calendar now so I can go over to

**[0:10:38]** my Google Calendar and you can see these are not here before and so like right what I need to do is hire a media buyer and that's on my calendar from the 9th to the 18th um and then we have plan and marketing campaign from the 9th to the

**[0:10:52]** 19th and then lastly prepare media for campaign from the 9th to the 17th so again this is all just like fake little action items that I have here um but you can see how this would be so so useful to just dump in your meeting notes with your team and have it put them on your

**[0:11:06]** calendar for the time frame that you need to spend on them and so just a quick little example you can also have this add to like a SAA or task management software as well again you can use the API and moment to connect to literally any service and have those as

**[0:11:19]** Tools in your workflow or for your AI agent directly and so it's a super robust application and you've got your front-end and your AI agent it is a Perfect combo with predictable pricing so that is moment in a nutshell I would really encourage you to try this out for

**[0:11:34]** free and see that you don't need platforms like bubble with a ton of hidden fees and just ridiculous pricing and what I gave was just a simple example you can take moments so far and build really complex AI applications that have very practical business value and so again I would encourage you to

**[0:11:50]** try it out completely free and let me know how it goes too if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video video
