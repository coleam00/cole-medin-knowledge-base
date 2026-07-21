---
type: raw-transcript
title: "The Secret Sauce for SIMPLE + POWERFUL AI Apps - AI Agents Masterclass #2"
youtube_id: hA_D9FywKgA
url: https://www.youtube.com/watch?v=hA_D9FywKgA
slug: the-secret-sauce-for-simple-powerful-ai-apps-ai-agents-masterclass-2
published: 2024-06-30
duration: "0:13:17"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** if you want to know how to build really powerful AI applications in the simplest way possible you have come to the right place today I'm going to show you how to build powerful AI applications with AI agents made very simple with Lang chain Lang chain is a really powerful python

**[0:00:16]** Library which basically just gives you a suite of tools that lays the groundwork for you to build really powerful AI applications without having to worry about developing a lot of different things that go into AI like chat memory or output parsers or dynamic prompts all these things it provides to you as a

**[0:00:32]** suite of tools so you can get on the ground running building the application of your dreams without having to put in months and months of work getting things set up initially and so what I'm going to do is I'm going to actually take the project the AI agent that I developed in

**[0:00:45]** the last Master Class video and augment it turn into something using Lane chain and show how simple and Powerful it is and there's even a bonus at the end where I can show how you can make something like this into a multimodel agent that can actually use different

**[0:00:59]** models like cloud and GPT so without further Ado let's dive right into the code all right so here we have the exact code that we worked on to create an AI agent in the last Master Class video my goal for this master class is really to have each video build on each other and

**[0:01:14]** so that's exactly what we're going to do here we're going to take the exact code we had before and I'm going to show you exactly what to change to turn the AI agent into a lang chain agent instead of just using the GPT SDK like we did before so it's still going to use GPT

**[0:01:28]** under the hood um aside from being able to use Claud with the bonus that I have at the end of the video um but it's going to be leveraging a lot of stuff that laying chain provides us to make things simpler so the first thing to mention before we dive into the changes

**[0:01:41]** to make this work as a laying chain agent is I just want to mention that I've changed up the example environment variable file a little bit and so if you're following along you're going to want to go back to this pull my code again from GitHub and change these up I

**[0:01:55]** got good documentation so you know exactly what to set here and then also the requirements file has changed there's new python packages because we are using Lang chain and so that's actually the first thing we're going to do here is we're going to import all the new tools that we need from Lang chain

**[0:02:09]** here you can see there's a lot of things here um we have the tools we have the chat open AI object and we also have new ways to represent the messages that are going to make things look a little bit simpler so now going down to our main

**[0:02:22]** function here instead of saying that we want um the system message in this Json format we can actually say it is a system message so this is using a laying chain tool already to make things nice and simple we'll actually do the same thing here where instead of this being

**[0:02:39]** Json for a user message it is now a human message and then we can change the way that we handle the AI responses as well so we're already making things look nice and simple with Lang chain which is super neat U so note here that the the response from the AI now is not just

**[0:02:53]** text anymore it's also an object which has content this is now the text that we want to print out with the terminal so it's a little bit of a difference there because of the way that we build up the chat history now it's going to be with these human messages system messages and

**[0:03:06]** AI messages from Lang chain um so the next thing that we want to do and this is where we really really get to simplify things we're going to add a decorator to this function and it's very simple it's just at tool and that's using this right here from Lang

**[0:03:21]** chain and what this is telling Lang chain it's going to tell our agent in a second here is that this function is a tool that it can invoke and it's actually going to tell the AI agent to look at the dock string to know when to use this tool and what arguments to give

**[0:03:37]** the function you can see because we Define the arguments here and things like the date format for the due date and so because we are using the doc string now to tell AI when to use this function we don't need this messy object anymore like we did when we just used

**[0:03:54]** the GPT SDK this messy object that told us the description of the function the name of the function function the parameters and everything but now we don't need that anymore because we can get it just from the doc string and then the function definition and so I'm actually going to completely get rid of

**[0:04:10]** this function we don't need it anymore and this is the thing that simplifies the code the most and is really neat especially because imagine if you have multiple different tools you have to have that messy object for every single one of them it just makes your code bloated and so you can actually leverage

**[0:04:24]** this setup instead which is nice because everything here you'd have anyway because you want to have doc strings in your python code for good documentation anyway and so now to actually use that instead of using the GPT SDK like this to get a response from the AI we're

**[0:04:39]** going to do it a little bit simpler and so now we're going to create an instance of that chat open AI object from Lang chain remember this is using the open AI API key environment variable to actually authenticate with open AI so it needs to be named exactly this way and then what

**[0:04:55]** we're doing just like before is creating a list of tools where in this case we only have one tool cre a SAA task and so it's an array where this is the only element of the array and then what we do to actually put the tools in the AI

**[0:05:08]** model is we call the bind tools function on our assana chatbot and give it the list of tools which again is just one in this case and now to actually get the response from the AI instead of using the GPT SDK we invoke this ass chatbot with tools object that we have which is

**[0:05:27]** our large language model augmented with the tools in a very simple way and then to tell if we have any tool calls this is a little bit different as well we just check to see if the tool call array actually has an element in it or not and

**[0:05:42]** if we do have tool calls we're going to do the exact same thing that we did before where AI is going to tell us basically I want to invoke this function here are the parameters that I want to use and so a lot of the structure is going to look the same but it's still

**[0:05:55]** going to be much much simpler especially because at this point we've bound the tools without having to have again that messy object we can now just use this create AA task with a doc string and it knows exactly when to use this function and so let's see what we do next so the

**[0:06:10]** next thing that we do I'll go back to the the original code is we just change the way that we add on to our chat history and so now we're just going to take the AI response and dump that into the message and this is going to have

**[0:06:21]** the content as well as any tools that it wanted to call and then what we're going to do just like before is we're going to Loop through every single tool tool call I should say we haven't actually used the tool yet and we're going to extract the name of the tool just like before

**[0:06:35]** and then we're going to map the tool name to the actual function using this uh dictionary mapping that we had before as well and then we're going to invoke the tool with the arguments that the large language model said it wanted to use to invoke that tool and then what we

**[0:06:50]** do to actually append the message instead of having to create this custom object here we can just depend a tool message again from Lang chain with the output and then the ID of the tool that we called nice and simple and then again to invoke with the response now that the

**[0:07:06]** AI actually or now that we actually called the function for the AI we need to give it the response so it can then create the response for the human and so again we're going to just invoke our ass chatbot with tools with the latest message history which now includes the

**[0:07:20]** result of the tool calls and then return that to the user and so at this point that is everything that we had to do but you can see that this is much much simpler than what we had before and this is just getting started with Lane chain this is a super simple example of how

**[0:07:38]** Lang chain just does so much for you under the hood it is a beautiful thing so let's go ahead and let's test this out all right so here we are back in the terminal and is time to run our AI agent and see if everything works well so

**[0:07:52]** python laying chain Das agent. py I renamed the file from the last masterclass video and it's going to look the exact same where it just allows us to in put anything to chat with the AI so I can say hey how are you doing and at this point it probably should not

**[0:08:05]** create an AA task for me so let's make sure that works looks good how can I assist you today I'll say I need to uh bake some cookies by Sunday we'll see if it creates a task for us here everything should work just as it did before the

**[0:08:18]** actual functionality should not be different but everything is simpler in the code and sure enough I've added the task of bake cookies for you it's due by Sunday June 30th which is perfect so let me go over to a here and sure enough you see that baked cookies due date Sunday

**[0:08:33]** looks good all right so everything is simplified and works exactly the same so now we can do the little bonus part which is actually to make this work with Cloud as well and so I'm going to make it possible to use different AI models and Lane chain is what makes this

**[0:08:47]** possible without very many lines of code and so I'll show you how to do that and we'll actually test with Claud as well so we're taking a quick detour here before I show how we can add in CLA to the agent cuz I want to just show how

**[0:09:01]** powerful this really is using Lane chain for this I don't think I describe it well enough in the following section of the video so the biggest reason that Lang chain is amazing for what I'm about to show you is that different AI models actually have a different way of doing

**[0:09:18]** tool calling and so this is actually called out in the very top of the documentation for Tool calling and laying chain for anthropic it returns tool calls in this way so I mean it looks nice but it's a very specific format and then open AI also has their own format these are not

**[0:09:37]** the same so if we were still just using the GPT SDK instead of Lang chain and I were to bring in the anthropic SDK for Claude I can't just combine those together in a couple of lines of code to have you be able to use either for function calling it would actually take

**[0:09:53]** a good amount of work because I'd have to handle these different formats for the tool calls but with Lang chain you don't and that is what you're about to see and that is just one of the many super powerful things with Lang chain I'm going over this now because it is

**[0:10:06]** the groundwork for AI agents going forward with all the videos in my master class I wanted to initially show what it looked like to use a GPT SDK and now we can see how we can build on top of it with Lane chain and so that's why I'm

**[0:10:20]** doing that but we're going to be using Lane chain in every single video going for so yeah I just wanted to call this out super super powerful stuff but anyway let's get into adding in CLA all right this will not take long because it is amazing how simple this is

**[0:10:34]** let me show you how to make this so you can use both GPT and Cloud for this agent depending on your choice so the first thing that we need to do is simply import chat anthropic from langing chain so it's going to be a similar kind of chat object like we have with chat open

**[0:10:49]** AI so now that we have that imported let me just show you this this is just so cool so I'm just going to change this line to this boom that is it so I'm going to say if our model that we have defined as the environment variable has

**[0:11:01]** GPT in it then we're going to use chat open AI otherwise we're going to use chat anthropic and so let me just save this here and just show that like this is what I'm referring to right here so we can call GPT 40 to use open AI or if

**[0:11:15]** you want to use anthropic we can use cloud 3.5 whatever Cloud Model we might want to use this is the most powerful one and that is literally all it takes and so now what I'm going to do behind the scenes I'm going to switch the environment variable and then I'll show

**[0:11:28]** you my terminal and we can test it out with Claude all right so here we are in our terminal again running our AI agent but this time powered by Claude 3.5 Sonet all right so I'm going to test this the exact same way as I did with GPT so I'll just ask it something very

**[0:11:43]** simple like how far is the earth from the sun just to get some sort of response from the AI where it doesn't actually need to invoke the create a sauna task all right we got a solid answer from it and now I'll say something very very different I'll just

**[0:11:58]** say I need to mow the lawn by tomorrow all right and let's see if CLA will make a task for us in N just like GPT and sure enough there it is it's even a very similar response which is pretty cool I've actually noticed that claw and gbt will give different

**[0:12:13]** responses sometimes with this kind of task creation as I was you know testing things as I made this video so that's an interesting thing like you can always try different models if you need a different kind of response but anyway let's go in a sauna and actually test

**[0:12:25]** this out sure enough there's the task mow the lawn by tomorrow all right there we go nice and simple and so you can see here that the functionality remain the same but this code is so much simpler now and we're able to switch between models with a heartbeat if I want to use

**[0:12:41]** GPT or CLA really powerful stuff the ability to uh have these tools defined so simply with Lang chain and being able to switch between models I'm going to be using that a lot in this master class going forward as we start to create more complex AI agents especially

**[0:12:56]** applications that have agents working together as we get into some really exciting things with other tools like L graph so if you are looking forward to that I would appreciate a like and a subscribe stay tuned we're going to be going through this adventure together building some amazing things so thank

**[0:13:11]** you very much for watching and I will see you in the next masterclass video
