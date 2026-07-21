---
type: raw-transcript
title: "ChatGPT is the GIFT that keeps on GIVING - Introducing Auto-GPT"
youtube_id: JeHObBsyKKM
url: https://www.youtube.com/watch?v=JeHObBsyKKM
slug: chatgpt-is-the-gift-that-keeps-on-giving-introducing-auto-gpt
published: 2023-04-18
duration: "0:16:48"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** haven't heard of or use GPT at this point you must be living under a rock this super powerful AI technology has revolutionized the space and for the first time it's given extremely robust artificial technology into the hands of everybody across the world to use for free on top of this GPT is also a gift

**[0:00:21]** that keeps on giving and what I mean by that is people are finding ways to use this technology every single day that we couldn't even dreamed of just a couple of months ago when this technology first came out and one example of this is auto GPT now what Auto is short for is

**[0:00:37]** autonomous and so basically what Auto GPT is is it is a an experiment a program that somebody has created and a lot of people have contributed to where it operates autonomously as in you give it a task and it can actually generate steps to solve this problem to

**[0:00:54]** complete this task and it'll execute those steps as well so it goes on its own to do something that you tell it to do and you don't even have to guide it to get the end result an extremely powerful thing A lot of people are saying this is the Sparks of AGI which

**[0:01:09]** stands for artificial general intelligence and any kind of AI that is strong enough to be an AGI is something that can think on its own act on its own and actually come up with its own goals and reach those goals through steps that it defines itself so that's just a really quick

**[0:01:25]** explanation as to what AGI is and why this thing is so powerful so for example one way I could use this as I'm building software for Cardinal branding or a branding agency in the web 3 space is I can actually take everything that I've been doing so far with GPT for boosting

**[0:01:40]** our Twitter engagement and I can use Auto GPT to make my prompts better to in the end make our Twitter engagement better as we're using GPT for this and so basically I'm using AI to make my prompts for the AI better and auto GPT can actually do that really really well

**[0:01:58]** and there's just really a million different things you can do with this technology so I'm going to go through the documentation of this show you how to get started really quickly and then I'll just give a demonstration and just show you how powerful this technology really is so let's dive into that right

**[0:02:11]** now so all of the code for auto GPT is stored in this GitHub repository right here it's open source so you can actually use this as a really cool learning tool as well to see all the code that goes on behind this but if you just want to get started and use it like

**[0:02:26]** I'm going to show right now you can go down to the readme here and they have really really clear instructions for how to get up and running super quickly with auto GPT the requirements are super simple you just need to install python 3.8 or later and they have a link right

**[0:02:41]** here and then you also need to get an openai API key and you can just Google how to do that it's really really simple the one thing to keep in mind is that when you are using an API key you have to pay for the requests that you are

**[0:02:53]** making to open AI 4gpt4 or gpt3 and so it's not free it's not super expensive though so I'd really encourage you to try this even though it might cost you a couple of dollars but it's not going to be anything more than 10 bucks if you're just giving it a

**[0:03:07]** quick try here for a couple of goes and then it also says that a Pinecone API key is required that's for the vector database to give Auto GPT long-term memory it's not actually a requirement though so you can really think of it as an optional thing like the 11 Labs key

**[0:03:22]** if you want the AI to actually speak to you as it's thinking through the steps to solve the task that you gave it and so with that in mind once you have those set up and you also need to install git which is super easy to install as well you can clone the

**[0:03:36]** repository uh change your directory into this new directory you created for the repo and then install the required python packages needed to run this and that's all you have to do for these commands to run and then uh really the last thing before you can actually run it is you just need to rename your dot

**[0:03:53]** env.template file in that directory you have now two dot EnV and then just add your openai API key we're directed to super easy to get started I got this set up in less than five minutes and then at this point you can run the python script that'll actually start Auto GPT and then

**[0:04:10]** within the terminal where you have run this command you can start interacting with it too set up the AI give it your goals give it the tasks that you wanted to do and then it'll just start going and it'll wait for user input upon each task so that it

**[0:04:24]** doesn't just go Haywire it's kind of a funny thing if you scroll down to the bottom here you can actually run it in continuous mode and so you give it a task and it'll Define its own goals it'll start executing on the steps it needs to reach those goals and you'll just keep going

**[0:04:39]** and going and going super cool thing but it can be dangerous so what you do when you don't run in continuous mode is the the AI will think through step by step how to accomplish the tasks that you give it but then each time it's about to execute a task it will ask for

**[0:04:55]** your permission to do what it's going to do whatever it is to to reach the next next step and so this way you can kind of oversee it and make sure it's not doing anything stupid and just exit early if it ends up doing something really dumb or maybe even potentially

**[0:05:09]** dangerous whatever that could be and so like I said all this is experimental this is in no means like a full product or it really finished in any way but it's the start of something really amazing and so I already have done all these um setup steps at this point and so I can

**[0:05:27]** get started and show you guys the demonstration of this so I'm going to run python script slash main.pi and we'll get started with using GPT so I'm going to make this full screen here and so uh the first thing that it wants is um it wants me to Define some of the

**[0:05:45]** context for what I'm trying to do here it wants the roll and the goals and so I can use my previous settings or I can say that I want to start something from scratch here so the first thing it asks me is name my AI like I could call it

**[0:05:57]** entrepreneur GPT so in this case um what I want to do for a demonstration for you guys is I want to get Auto GPT to give me clear steps for growing a Twitter account really simple but there can be a lot of depth that goes into really creating that list of steps and

**[0:06:16]** so I'm going to call this Twitter Dash GPT all right so it says Twitter GPT is here and blue text it's really cool how they color code everything like this is a nice UI even though it's just in a terminal and then it says describe your ai's role for example you're an AI

**[0:06:33]** designed to autonomously develop and run businesses with the goal of increasing your net worth pretty cool so I'll say uh Twitter GPT is an AI designed to grow a Twitter accounts through creating engaging tweets and any other kind of content on Twitter such as replies so I'm going to keep it a little broad but

**[0:07:00]** say that you're going to focus on having engaging replies and then just having good tweets to grow your Twitter account so we'll say that and then we'll say entering five goals for your AI and so one example they have here actually is grow your Twitter account so I'm going

**[0:07:15]** to have that as one of the goals and then I'll also say a spark conversations with tweets and replies it's one of the best ways you can grow a Twitter account is by not just putting out content that people like but also putting out content that's easy for people to engage with and so

**[0:07:33]** that's one of the things that I want to try to coax Auto GPT into understanding here or maybe it'll just figure that out on its own as it goes through the tasks to reach the end goal of getting a list for me of things to grow a Twitter

**[0:07:46]** account and so another goal I can have here is I'll say create a list of steps to take to grow any Twitter account so I'm not going to be specific to like software development or marketing or some Niche within like an account could be for in Twitter I'm just going to keep it

**[0:08:09]** General here and let's just go with those three goals let's keep it pretty simple here and so at this point it's going to start thinking and really processing the first set of tasks that it needs to go through to reach any one of these goals or all of these goals

**[0:08:24]** and so the first thing it says here is I think our first goal I'm reading this text right here I think our first goal should be to grow the Twitter account we can achieve this by posting engaging and relevant content that will attract followers and it has quite a bit

**[0:08:40]** of text here I don't want to read through all this every single time because there's like I said quite a bit here it would take a while but really uh it gives its thoughts it gives its reasoning for its thoughts and then it gives a plan and then also it

**[0:08:54]** uses a technique that I already showed on my YouTube channel where it criticizes itself uh to really make sure that it is thinking about things from different angles and so at this point it's created the first task for me and so this blue text that you'll see every

**[0:09:10]** single time it's done printing out a bunch of text that is the next action that is going to take so first it is going to browse Twitter and it's going to ask the question what are some successful content types for similar Twitter accounts and so I can enter y to authorize this command so

**[0:09:28]** I'll run it and then it's going to actually process the explore page of Twitter and it's going to see if it can find anything to answer the question that it has right here and uh you can see right here that it didn't actually get anything useful I don't know why exactly but anyway it

**[0:09:46]** says so in essence we couldn't find anything useful on Twitter I'm going to actually do a Google search that's basically what it what it's doing here so its plan is to use a Google search to find popular tweets and so now its action is to do a Google

**[0:09:58]** search with the input of popular Twitter accounts to follow and so it's going to get inspiration from finding specific accounts and this is a really powerful thing that GPT cannot do on its own you need something like this that that actually provides an infrastructure for GPT to browse the internet to get this

**[0:10:15]** kind of stuff otherwise you are limited by gpt's cutoff of September of 2021 that's the training cutoff where it doesn't know any information after that date and so at this point it actually got a lot of stuff here like you can see it found some Twitter accounts to mimic and

**[0:10:32]** now it's saying that we need to analyze the content posted by popular Twitter accounts to inform our content creation strategy and so we're just going to let it analyze Twitter accounts that's what it's doing right here and it's going to I guess pick out some trends for things

**[0:10:47]** to talk about or just a general format of successful tweets I don't know exactly what it's it's going to find here it's a bit of a black box even though it gives me a lot of text there's still a lot of things going on behind the scenes where I don't totally know I

**[0:11:00]** don't have a way to know exactly what it's doing uh but let's just wait here let it think for a little bit and let's see what it says so I'm gonna skip kind of the thoughts and reasoning here go right to the plane it says create content similar to successful

**[0:11:15]** tweets from analyzed accounts generate unique content with an original image and use both types of content to build our Twitter account and so I'm going to say yeah go ahead and do that that sounds great to me honestly so what it's going to do right now the prompt is

**[0:11:29]** please generate a prompt for an original image to use for our Twitter account and so it's actually going to generate a prompt for GPT so it's the AI thinking about how it can do better with the best prompt possible and in general that's just a good idea for interacting with GPT you want to

**[0:11:47]** basically have it criticize itself or have it think about a way you could give a better prompt for it so it's kind of self-aware in both cases but both of those I find are like super useful ways to get GPT to give you better output because like I always say if you give it

**[0:12:04]** trash input you get trash output and so let's see what what did it come up with at this point So the plan is to create a poll that asks followers questions about their interests or opinions on certain topics use the poll to encourage interaction and Sparkle conversation on Twitter and then analyze

**[0:12:20]** the results of that pool to inform our content strategy so it's actually come up with an idea of something that really posts do they get ideas for future content on Twitter which is pretty cool and so uh it actually generated some code that it's going to create which is pretty cool and it's going to

**[0:12:40]** run this code to generate a poll uh so let's Let It Go here um and so now it's going to refactor the code to create a function for generating displaying the poll using F strings and using an enumeration Loop to avoid calling index method in the loop and so

**[0:12:58]** this is starting to get really technical now because it's actually doing some coding to live out our goal to create a task to accomplish that goal um so this might go on for a little bit here and so what I'm going to do is I'm going to pause this video and then I'm

**[0:13:13]** going to come back when it's actually gotten to a point where it's created something cool and so I'll be back when that happened all right so it took a little bit to get here I had to go through a couple of iterations of just allowing it to execute more commands to get to one of

**[0:13:29]** my goals and the goal that it got to is it actually outputted a text file with steps to grow my Twitter account so you can see in the auto GPT workspace directory it created a text file and just now that has all of these different steps to grow a Twitter account and just

**[0:13:47]** to show where it thought about doing this you can see right here uh it's thoughts is let's create a list of steps to take to grow any Twitter account based on our previous discussions and brainstorming sessions so everything that it was looking at before and Gathering its thoughts on is finally taking an action

**[0:14:06]** here of writing out to a file called Twitter girlstuffs.txt all this text right here that it's come up with in the plan section right here and so that's exactly what we have and I could keep going and it could start maybe helping me like create content and things like that but I'll end the video

**[0:14:24]** here on this section just so that it doesn't go too long but really this list is pretty good like you could actually use this it's a little general maybe it doesn't dive as deep as you might need but it's a good start for helping you understand how to grow a Twitter account

**[0:14:37]** start by identifying your target audience and their interests using Twitter analytics to learn more about your audience that's that's a good thing to do for sure researching successful Twitter accounts with similar Target audiences creating content that resonates using relevant hashtags incorporating both unique and popular content in your tweets that's another

**[0:14:58]** that's actually a really good suggestion engaging your followers and responding to their messages and comments another good thing and then a little general thing at the bottom here evaluate and refine your strategy as needed so like I said this is all pretty general advice but it's good like this is genuinely good advice

**[0:15:15]** that it come that it came up with after doing brainstorming uh searching Twitter and Google to get inspiration and to just understand Trends in Twitter and if I kept going I bet it could actually start to generate some real content for me maybe even give me a couple of tweets

**[0:15:30]** that I could tweet over the next couple of days so this is a super cool Tool uh it's not perfect like sometimes it'll get in loops with itself where it keeps getting back to the same prompt other times it just is way too General with the suggestions it gives you kind of

**[0:15:45]** like what we saw here but this is the start of something big because this is only going to get more powerful as people figure out new ways to build tools like this just to coax it into better responses and as openai themselves generate new models like gpt5 gpt6 and more competitors come onto the

**[0:16:04]** scene we might even have something better than anything open AI is making and then this is also going to get more powerful through that so super cool stuff a lot of things that I'm going to be using for building the Cardinal branding software and so as I go through

**[0:16:19]** my journey doing that I will continue to share everything that I find here so thank you all for watching I hope you enjoyed this video and you got something out of this go give Auto GPT a try yourself and tell me what you think of it thank you for watching and I'll see

**[0:16:33]** you in the next one [Music] thank you [Music]
