---
type: raw-transcript
title: "AI is TOO EXPENSIVE if You Don't Do This"
youtube_id: ZzRCrhA3JUQ
url: https://www.youtube.com/watch?v=ZzRCrhA3JUQ
slug: ai-is-too-expensive-if-you-dont-do-this
published: 2024-07-31
duration: "0:11:26"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** using large language models to create AI applications is insanely expensive it might seem cheap at first when you're just prompting it a couple of times in development but when you have a full production application with a lot of users you are quickly going to get a bill for thousands of dollars and so

**[0:00:16]** today I'm going to show you how you can save 90% or more on your AI costs how you might ask well think about it this way usually when you create an AI agent a majority of the requests that go to this agent are rather simple things like make a task for me or I have this

**[0:00:31]** question it's only a small portion of the time usually where you'd have more complicated requests things like do research on the latest models for me and then send an email to my co-workers with the pros and cons for each now that is a complicated request for an agent but

**[0:00:45]** usually you're only going to have requests that are that complicated 5% or 10% of the time now the big problem is if you're using just one large language model for your entire AI application you have to pick a model that is good enough to handle that 5% or 10% of complicated

**[0:01:02]** requests even if the model is really expensive and that extra power is unnecessary 95% of the time now here is the real kicker you don't have to use just one large language model and you can save a ton of money by using more than one now what do I mean by that well

**[0:01:18]** let me show you and let me show you how you can implement this so to demonstrate this concept really really clearly I've got a diagram here that I actually used in another one of my videos where I talked about some of the uses of AI agents and this is diving really deep

**[0:01:32]** into one of those specific uses which is using an AI router so basically what you do in this setup to save a ton of money with AI is you take a request and you have a first step which is a large language model that decides the complexity of the request so basically

**[0:01:48]** it's going to Output a yes or no is this request complicated and you have to implement custom rules in the prompt for this router to accurately determine the complexity of the request if it determines that the request is indeed complicated then you would route it to the more expensive model if the request

**[0:02:05]** is not complicated then it'll go to the cheaper model which is still going to be able to handle it because it is a basic request and so either way you get a good response but now you don't have to send every single prompt to the more expensive model and pay a lot more money

**[0:02:19]** it is Pennies on the dollar if most of the requests can go to the cheaper model even if you have to pay for this first step of using the AI router because there are models out there that are so much cheaper compared to others and so you want to use those as much as you can

**[0:02:35]** so I hope that explanation was helpful and with that we're going to go into actually developing this so I'm going to show you how to implement an AI router and then how to set up this routing so that some of the requests go to the cheaper model and some go to the more

**[0:02:47]** expensive model and then we'll even play around with this and see it in action so here we are in the code we're all be implementing the AI router to save a ton of money on large language model costs and showing you how to do that what we have right here is a GPT 40 powered AAA

**[0:03:02]** task management agent that I've actually been building as a part of my AI agents Master Class series if you haven't been watching the series no worries you can easily follow along with the code here because I'll show what this does quickly and then we'll dive into enhancing it to

**[0:03:15]** use llama 3 for the less complicated requests so first a really quick walkr of what this code does so right now we use GPT 40 for our model and we have a bunch of tools to finded to interact with sauna things like creating projects for us deleting tasks for us marking

**[0:03:30]** them as complete anything that we would need to do to manage tasks in a sauna we create a mapping of these and then we bind them into our chat open AI object so we can interact with GPT and have it do things in a sauna on our behalf and

**[0:03:43]** then in our main function here we have a Streamlight UI defined so we can nicely interact with our agent to do all these things in a sauna all of it powered by GPT right now so now what we're going to do is go back to the top of the file and

**[0:03:56]** start enhancing it so you can use llama 370b for all the simple requests and then keep the more complicated things for GPT 40 like we might want to create a project and a bunch of tasks within it within a single request that would be something for GPT 40 and for using llama

**[0:04:13]** 370b we are going to be using Gro it is so cheap using llama 3 with Gro it's like 11% of the price of GPT 40 for the input tokens and then 5% of the price for the output tokens and so we'll also Define the model here which we're going

**[0:04:27]** to be using the function calling fine-tune version of of llama 3 provided by Gro which is very very powerful but again much much cheaper and so now going down past our task functions here we're going to create a nice little helper function to get the latest messages basically a short version of the chat

**[0:04:45]** history which we're going to give to our router so it has the context to determine if it should go to llama 370b or go to GPT 40 just based on the complexity of the request and so with that we can start defining our function that is going to decide the complexity

**[0:04:59]** I.E deide the model to send the request to and so the first thing we're going to do is Define the chat grock instance because again we're using llama 370b not just to handle the simple request but also as the router itself because it's that cheap and then we'll also get the

**[0:05:14]** latest messages which we're going to put into the prompt here so I'm not going to go in the prompt in a lot of detail I spent a good amount of time crafting this but the most important thing here for the AI router prompt is to be very specific in the way that you tell it how

**[0:05:28]** to determine if a request is complicated or not I very much established the rules here based around aun tasks because that is what my agent is responsible for doing so you think about what your agent might be responsible for doing what kind of requests would come in and then you

**[0:05:43]** define the rules for the router based on that so it can determine well when a request is complicated and when it is not and then I also embed the latest messages in here so it has that context not just the last user message but also a couple previous messages as well so it

**[0:05:57]** has everything it needs to determine the complexity and so with that we will invoke our chat Gro instance the router and then return that response which is either going to be cheap or expensive i e use llama 370b or use GPT 40 and so now we have a function that neatly wraps

**[0:06:15]** the router to get the output of cheap or expensive based on the chat history and so with that we will enhance our prompt AI function starting with adding a parameter here which is going to be cheap or expensive which model am I going with and so now where we Define

**[0:06:31]** our chat object it's not going to be just chat open aai anymore we're also going to instantiate chat grock if the decided model is cheap otherwise if it's expensive we'll continue to use GPT 40 like before because we need it to handle those more complicated requests and so

**[0:06:47]** that is literally it that is all it takes with the routing here most of the work is done in this function here and then within this we just have to Define which model we instantiate for our Assa chatbot based on if it is cheap or expensive and so the very last thing we

**[0:07:00]** have to do just for the recursive calls for Tool calling is just add that parameter for the recursive call to prompt AI that is everything for enhancing our prompt AI function and so now within our main function where we handle the user input we just have to add on a little bit because we need to

**[0:07:14]** call the decide model from prompt function given the chat history and then we'll even print out here which model we're going with cheap or expensive and then we'll add that in as the second parameter to our call to prompt AI so that is literally everything we have to

**[0:07:26]** do now so now the less complicated requests will go to L Lama 370b powered by Gro and then all the more complicated ones will go to open AI GPT 40 so let's go ahead and test this and make sure that we haven't inhibited the performance and we're actually using the

**[0:07:41]** cheap model most of the time all right so let's test this thing out and make sure it uses the right model depending on the complexity of my request so to run this chap B in the browser I just went into my cost-saving AI router folder in a terminal and I ran the

**[0:07:54]** command streamlet run cost-saving task agent in the code Linked In the description of the video I've got a requirements. text file so you have all the dependencies you need to install this and run it just like I am here with streamlet once you run it there will be

**[0:08:09]** a local URL that spawn up and that's what we're looking at right here on the left hand side in the browser so let's go ahead and test out this Assa agent so I'll start with a very simple prompt here and I'll just say hi and sure enough you can see on the right hand

**[0:08:20]** side it's going with the cheaper llm which is llama 370b in this case and so now we'll actually do something within a sauna but we'll still keep it pretty simple so I'll just say what projects do I have and again going with the cheap model here because it's just a single

**[0:08:35]** action you have the following projects YouTube Fitness business personal and coding and that is correct and we'll even go into a and look at some of this stuff in a little bit here I just want to run a couple of more tests and so now I'll do another request here I'll say um

**[0:08:48]** cool within the coding project make a task to build a SAS we'll do this going with the expensive model now I guess because it thinks it has to go within the project and make a task and so it's deciding to go with the expensive model you could probably do

**[0:09:06]** this with a cheaper one so maybe I'd want to update my AI router prompt but regardless this is working pretty well um and so yep it built or it added the task build a sass so going into a here sure enough with a due date of today build a sass so it just picked a due

**[0:09:21]** date because I didn't give it one but sounds good I guess I got to build a sass within a day so I should get cracking um yeah let's try another one here okay great uh also add um do marketing for the SAS let's see what it does here okay so it's

**[0:09:37]** going with the cheap llm this time U probably because it already has the context around what project it should be adding the task in so that's nice so we'll go within coding here and do marketing for the SAS also due today very nice all right so now let's do a

**[0:09:51]** more complicated one and make sure that it goes to the expensive model for sure so I'll say uh add three more tasks code thing one code thing two and code thing three and this should go with the expensive model and yep sure enough it does going with the expensive model

**[0:10:08]** we'll see what it gets back to us with here it takes a little bit a little bit longer now because it actually has to create each one of those tasks in a sauna but yep it made all those and here we go code thing one two and three all

**[0:10:20]** due by today I've got a busy day ahead of me so I should probably wrap up this video but that is actually it it's definitely working well you can always adjust the AI router prompt if things aren't working exactly as you want so if there are more complicated requests

**[0:10:33]** going to the cheat model um or vice versa and you don't want that always change the prompt feel free to play around with that but this is working great so that wraps up the implementation of the AI router to save a ton of money with large language models really the hardest part there was

**[0:10:48]** getting a good prompt for the AI router the rest of the code was easy peasy and if you can get that prompt down so that the router can accurately determine which model to send the request to based on the complexity of the user message you are going to be in the right place

**[0:11:02]** to save a ton of money cuz you can use those much much cheaper models to handle a majority of the requests to your agent so I hope that you found this useful and that you can use it to save a ton of money as you're developing a SAS an AI

**[0:11:16]** agent an application whatever it might be and if you did find it helpful I would really appreciate a like and a subscribe and with that I will see you in the next video
