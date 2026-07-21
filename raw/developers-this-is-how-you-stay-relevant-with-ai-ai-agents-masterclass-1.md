---
type: raw-transcript
title: "Developers, THIS is How you Stay Relevant with AI - AI Agents Masterclass #1"
youtube_id: zaNIvRllycM
url: https://www.youtube.com/watch?v=zaNIvRllycM
slug: developers-this-is-how-you-stay-relevant-with-ai-ai-agents-masterclass-1
published: 2024-06-23
duration: "0:16:55"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** there is no doubt at this point that artificial intelligence is the number one thing that all developers should be focusing on the problem is many developers maybe even like yourself are not focusing enough on AI agents which is the real way to unleash the full power of AI all an agent is is some

**[0:00:19]** large language model that is given the ability to interact with the outside world able to draft emails or create tasks or add contacts to your CRM whatever it might be and you can take this so far you can develop agents that work together to accomplish very complicated tasks or autonomous agents

**[0:00:36]** that are used as customer support all of these things that are actually useful and truly powerful are built with agents and so that is why I am starting this master class to show from step one all the way to a full application how to develop agents and really Unleash the

**[0:00:51]** Power of artificial intelligence and so if you're interested in actually using AI to build cool things you need to use agents and so let me show you how throughout this master class I promis to deliver a lot of value very very quickly and to prove that immediately today we

**[0:01:07]** are going to build our first AI agent completely from scratch and so this is going to assume that you have a basic understanding of python if you don't at this point you should definitely check out some other tutorials there are a lot on YouTube because I today just want to

**[0:01:21]** Dive Right into creating AI agents all the code that we have here and that I'll have in future tutorials will also be in GitHub that'll be linked in the description so you can feel free to follow along and get all the code from there and so we are starting really

**[0:01:34]** really basic here I am going to open this file that I have it's just a skeleton for a main function and we'll fill in everything to create our very first agent this agent is going to basically be a a GPT chatbot that is able to interact with the outside world

**[0:01:49]** to create tasks for us so the platform that I'm going to use for this is called as SAA it's a really nice platform to manage projects and tasks it's something external that I'm going to be using with AI so that I can actually tell it to create a task it'll do it and we'll see

**[0:02:02]** later that'll go in the browser in the assana website and sure enough that task will be there and that's the start of an agent start of something very very very powerful and so let's begin the first thing that I need to do here is I need to import all of the required packages

**[0:02:17]** for my agent things like Asana and open AI so we'll do that there'll be instructions for how to install these packages um in the GitHub as well and that that'll be linked in description so no need to fret there uh next up what we need to do is actually Define some

**[0:02:31]** environment variables for our project and so these are variables that um are containing things like Secrets or configuration that you don't want to have just pasted in your code and so things like the open API key and your ASA access token so you'll create a EnV file at the same directory as your

**[0:02:48]** python script I'll have an example in the GitHub repo and you'll fill in all these things here getting your API keys for AA and open AI is really really easy you can just Google how to do it there's not much that goes into that so that is our environment variables and then what

**[0:03:03]** we need to do is actually load those environment variables using the EnV package so now we can access those through os. EnV which you'll see in a little bit here actually right now when we create the open AI client and so here I'm actually defining the model which

**[0:03:19]** we'll use later but I'm getting that through the environment variable and then defining it uh default here gp-40 if that environment variable is not defined all right so next up we actually have to create our assana client within our python code and so I get the access token through an environment variable

**[0:03:37]** and then I create the client and then specifically set up the tasks API because there are a bunch of different apis in AA that are all organized under the one API client so I have to instantiate the task API specifically because my GPT uh chatbot here is going

**[0:03:52]** to have the ability to create tasks for me in a SAA uh all right so now the next thing that I need to do is I need to the start defining the messages for my chat bot so specifically the way that you interact with GPT um in your python code even

**[0:04:07]** outside of your python code it just isn't really obvious to you is there's a list of messages that is maintained and each message has one of three roles it is either a system role which means it is background context for the AI it is a user role as in it is a message from the

**[0:04:22]** user which we'll see in a little bit and then also what we'll see in a little bit is the third type which is the role of assistant and that is actually the response from from the AI and then with that you also have tools as well which we'll get into because that is how the

**[0:04:36]** GPT model interacts with the outside world and so to start we're going to have a very first message defined right out the get-go which is the system message and this gives the context for the AI so I'm saying something very basic you are a personal assistant who helps manage tasks in a sa and then I'm

**[0:04:53]** also giving the current date which is important because the AI needs to know the current date to then be able to know when to put the due dates on for tasks and we'll see that in a little bit but that'll be something that we'll add as one of the options for a task is when is

**[0:05:08]** it do so that is the very first thing next up what we want to do is I'm going to have this entire application just run in my command line for now and so what I'm going to do is I'm going to Loop forever and ask the user for another

**[0:05:21]** message to send to the AI and then if they type Q then it breaks out of that and ends the application all right so then the first thing we're going to do is uh once we actually get the input from the user we're going to add that to

**[0:05:34]** the list of messages and so you can see here that instead of system we have user for the role and then the content of this message is going to be exactly what the user typed into the terminal and then what we're going to do we haven't created this function yet but we're

**[0:05:47]** going to create a function that allows us to give these list of messages which we'll continue to add on to so there'll be chat history and we'll prompt the AI with it and so once we get the response we'll just print that out to the terminal so that you can have the chat

**[0:06:03]** there in the terminal and then we'll add the response to the messages as well so this is the role of assistant so at this point we have a system message and then we're building up the chat history with the user messages and then the AI responses so that is really everything

**[0:06:18]** in our main function now we have to Define everything else for the AI agent uh the function interact with the SAA and all that so let's get right into that all right so the very first thing we have to do outside of our main function is create the function to

**[0:06:32]** actually add tasks to a sauna and so this is going to take two parameters one is going to be the name of the task and the other is going to be an optional argument which is when is the task due and it's going to default to today and

**[0:06:45]** we'll set up logic to handle that as well I'll add a quick doc string in here this is really helpful to understand how to explain the function of the AI which we'll see in a little bit and then we'll add the initial logic here to set the due date to the current date if it is

**[0:06:58]** the default of today next what we'll do and you'll have to look at the Assa API documentation if you want to do other tasks in assana that's how I figured out how to do this is we Define the data that we want to give to as to create the task so it's

**[0:07:13]** just the task name when it's due and then also the project ID so it knows what section of your all of your project lists to actually add the task to and then all we do is call the task API to create that task get the response and return that other otherwise if there's

**[0:07:30]** an error we'll just return the error and we don't have to get too fancy with this because we can kind of just throw whatever we want at the AI and it'll parse what it needs out of that response and we'll actually see that in a little bit where it'll be able to understand

**[0:07:43]** this Json and even give us the link to the task once it's created it which is super cool so that is the function for creating a task in a sauna next up what we want to do is create the function that actually prompts AI so we give the

**[0:07:56]** list of messages that we see here in the main function and we have our very first call to GPT where it's just client. chat. completions doc create and we pass it three things here first we give it the model that's the thing that we had set up in the environment variable then

**[0:08:11]** we give it the list of messages this is more than just the current user message it's the entire chat history as well so it has all that context and then we also need to give it the tools that it has now the tools this is what really makes

**[0:08:24]** it an AI agent because these are the functions in your python code that it can run to do things to inter act with the outside world now in order for it to understand how to use your functions well and how to understand what the function returns you have to set up a

**[0:08:39]** little bit of configuration here so that's what I'll show right now so we're going to create a very simple function that doesn't accept any parameters called get tools I just want to have this outside of the prompt AI function for Simplicity sake right here tools is an array where each item is an object

**[0:08:57]** that defines a function that the AI can call the reason there's a lot here is because we need to tell the AI when to use this function which is what the description is used for then we need to tell it what to actually pass into the function so we

**[0:09:12]** Define the parameters here like there's the task name um and then this is how it knows what to give for the task name then we have Doon and then how it knows what to give for Doon this also includes the date format which is really really important if you give a bad date format

**[0:09:27]** then Asana won't be able to create the task due and then we give it which parameters to the function are actually required so there's a lot here but it's really just when to use the function and what to pass in and that's all you have to do and and AI is actually going to be able

**[0:09:42]** to intelligently determine from the conversation what the task name should be and what the due date should be so you don't have to tell it exactly this date format for it to be able to understand what you want and turn it into that date format so there's a lot

**[0:09:55]** of intelligent stuff going on behind the scenes here which is part of what makes agents so so powerful they're able to take natural language and turn it into code in a way to interact with the outside world and so with this function defined now what we can do is for tools

**[0:10:10]** we can just pass in the call to get tools to return all these tools for our AI prompt next what we'll do is we'll actually get the message from the response and so this message is going to be in the same format here it looks like there's a lot going on here but really

**[0:10:27]** there's a specific format that GPT always returns its AI responses in and we can follow that in fact I can show you really quickly what that format looks like all right so I wanted to show this quick just so that you understand what GPT returns in Python code so every

**[0:10:42]** time you get a response from the chat completion you're going to receive an object that looks like this and so the part that we care about is the messages section and so we need to get the choices and then within choices there's going to be an array and we care about

**[0:10:57]** the first item there and then within it we can get the messages attribute so going back to the code here that's why we do completion. choices get the first element and then get the message and this message is going to be in a similar format where we have the

**[0:11:11]** role and we have the content but then also because there's a possibility of the AI calling tools here we have another attribute called tool calls and so what we'll do with that is we'll say if there are any tool calls we need to actually perform that action now and so

**[0:11:27]** our agent has the option to perform multiple different actions there can be many tool calls in our case there's only ever going to be one because we just have the option to create an Assa task but you can imagine as you develop this outport to be able to add things to a

**[0:11:41]** CRM along with create the task or upload a document along with creating a task you might have multiple tool calls in one call to the agent and so if there is a tool call we need to create a mapping that Maps the string that it outputs it'll basically say the name of the

**[0:11:57]** function it wants to invoke and we map that to the actual object in our python code which is the function next up we'll add the tool request to the messages and so at this point we haven't actually invoked the tool but AI has returned a response to us that says I want to

**[0:12:14]** invoke this tool and so we'll add that to the chat history so that later on AI has the context that at this point in our chat it did invoke this tool now what we're going to do like I said there could be multiple tool calls so we'll Loop through each one and for each tool

**[0:12:31]** call we're going to grab the arguments that the AI has decided to invoke the function with so we'll grab the arguments and we'll actually call the function with those arguments the two stars here is just a fancy way to turn an object kind of like this where we

**[0:12:47]** have all of our arguments defined and actually turn those into arguments for a function column so now with this we'll call create a SAA task with whatever the AI decided for the task name and whatever the AI decided for the Doon variable if it decided to give something

**[0:13:03]** because remember it is optional so what is next after we call the function well at this point we want to append another message to the history which is going to be the result of calling the function you can see that the content here is the result of calling the function whatever

**[0:13:19]** that function returned as a string um and so now at this point we have both the request to call the function and the result of calling the function in the chat history and now after this we can finally call the AI to get the response for the human because at this point

**[0:13:35]** everything that we've added to the messages is just context for the AI to know what has been happening in the conversation but now we need to actually uh query the AI again and tell it hey you asked to call this function we did it here's the response now write

**[0:13:51]** a message back out to the user based on what happened when the create AA task was called and you'll see in a second that it can actually take part of the response and spit that back out to the user to give something like a link to the task that was created and then we

**[0:14:06]** just return that so we can add it into the assistant message and add that on to the chat history so that is everything that we have for agents. py the script is now complete and we can run it to create tasks in aauna and just chat with our AI

**[0:14:22]** so let's go ahead and do that now all right so now I have my terminal open and I'm ready to execute my script to talk to my chat bot one thing to mention really quickly is that I did populate myv file off camera obviously I don't want to expose my open Ai and AA API

**[0:14:39]** keys and so that's the one thing that I did not add to my code on camera but with that being done I'm now ready to run my script so I'll say python agent stpy and this will immediately prompt me for the first user message and so this is still just a regular GPT chatbot that

**[0:14:53]** builds up chat history so I can ask it regular questions like how are you doing um but when it decides it needs to create an assuna task then it will do it so the agent intelligently decides when it needs to actually run that function make that tool call based on the

**[0:15:08]** conversation so you can see right here that it asks something very very normal but if I give it a question or I guess a request rather like create a task for me to make a thumbnail for my next video and I need this done by Wednesday then it'll actually make the decision to make

**[0:15:21]** the tool call and create that task in AA for me so sure enough here we go I've created the task for you to make a thumbnail for your next video the task is due on Wednesday June 26th you can find the task here and it even gives me

**[0:15:33]** the link because we gave it everything that assana returned back to us in the function call as that final prompt to make that final assistant message and so I'm going to actually go into isana here and sure enough this project I promis was completely empty before now here's

**[0:15:51]** the task that it created for me create a thumbnail for next video due on Wednesday and we could take this a lot further and add priority and status and aign we could make it so the agent will ask us for things if we didn't give it yet like oh you didn't mention who to

**[0:16:03]** assign this to and then we could give it like you could take this so far and this is just a very basic agent to begin with so that is the power of AI agents in just a few minutes we created a full AI agent from scratch that is able to chat

**[0:16:17]** with us just like GPT can but also create AA tasks for us with understanding our parameters like the task name and the due date so we don't even have to give it exactly what what the function in the python code needs and it can still do that for us really

**[0:16:33]** really cool stuff in the next tutorial what I'm going to be walking through is how you can actually create AI agents in a bit of an easier way and so I showed you something just to cover the basics but now we can take this further and make it simpler and more powerful so

**[0:16:48]** stay tuned for that I'd appreciate a like And subscribe as well and I'll see you in the next one
