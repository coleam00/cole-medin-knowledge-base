---
type: raw-transcript
title: "OpenAI's o1 is Barely Usable, but I Fixed it..."
youtube_id: IsxXO3EbIqc
url: https://www.youtube.com/watch?v=IsxXO3EbIqc
slug: openais-o1-is-barely-usable-but-i-fixed-it
published: 2024-09-18
duration: "0:24:47"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** open AI recently released the latest and greatest large language model 01 and this thing is absolutely crushing benchmarks and in general is just an incredible step forward for generative Ai and I'm sure you've seen dozens of people talk about 01 already testing it out explaining how the Chain of Thought

**[0:00:18]** works or maybe just playing around with it but today I've got something for you that is completely different than anything else you have seen on 01 and I can't believe that people are not talking about this because there are straight up things that you cannot do with 01 that are crucial for developing

**[0:00:33]** AI agents or complex AI applications in general hold up I just dropped a truth bomb on you there and so you deserve to know exactly what the heck I am talking about in the beta preview of 01 there going to be a lot of key features that are missing from the model including

**[0:00:48]** tool messages and function calling which are both absolutely necessary for AI agents what this means is unlike other models like GPT 40 01 by itself will not be able to interact with the outside world with things like apis or web search you need function calling for that and this is seriously a bummer

**[0:01:07]** because you can't use the now most powerful llm for most AI applications just take that in for a second it sucks but I have come to the rescue because I have custom coded function calling for 01 you heard that right I have replicated open AI tool calling and let

**[0:01:23]** me tell you this setup supercharges 01 and makes it an incredible AI agent the ridiculous reasoning capabilities of 01 combined with the ability to interact with any API is a game changer I'm going to show you exactly how to do it and the best part is you can use any llm with

**[0:01:40]** this setup and so if there's ever another situation in the future where you have a powerful llm that doesn't have function calling you can plug that llm in just like 01 so you can instantly use it to create AI agents so let's go ahead and Dive Right In I'm going to

**[0:01:54]** show you exactly how to implement this and then we'll test it out to see how powerful 01 really is as an AI agent all right so when I say I'm going to show you exactly how to implement this I mean we're going to code this thing from scratch you can see what I have here is

**[0:02:08]** just the skeleton for a main function and we're going to walk through step by step setting up all of our tools implementing the prompting and the Custom Tool calling for 01 and then also the UI with streamlit so we can interact with our chatbot in our browser and so

**[0:02:22]** the first thing that I want to say is that there is going to be a link to all of this code in the description of this video in a GitHub repository and so you can just go ahead and steal it from me if you want to start using it right away

**[0:02:33]** without having to worry exactly how everything works CU I don't want you to have to be very technical to get a lot out of this and so I'm going to go through all the code but don't worry if you don't understand everything I'm not going to go in super great detail

**[0:02:45]** because the main thing here is just to show you quick what I built and then test it and show how powerful 01 is as an AI agent and so if you download this code from the GitHub repository you'll have this script right here which will go through all the code for in a bit

**[0:02:59]** you'll also have a requirements text file so you know all the python packages that you need to install in what version and then also an example environment variable file so you know exactly how to set up your environment just like mine to run this with no hitch all right and

**[0:03:12]** with that we can go ahead and start coding our custom function calling 01 AI agent I am absolutely stoked for this so the first thing that we want to do here is import all the python packages that we need for this agent and this kind of reveals a lot of the services and

**[0:03:27]** libraries that I am using for this agent so I'm going to touch on this really really quick first of all I am using assana Asana is my favorite task management platform that I use every single day and so this agent is going to help me manage all my projects and tasks

**[0:03:41]** in as so that's what we're going to be doing for all of our tools and I'll show that in a little bit here we also going to be using streamlet for our user interface it's a really nice and easy to ous python package for UI and it works

**[0:03:53]** well with AI as well and then the last thing to call out here is I'm going to be using Lang chain it is my favorite python Library for making it very easy to work with llms and it develops a lot of things for you so you don't have to

**[0:04:05]** reinvent the wheel with things like prompt templates and chaining all that good important stuff with llms and so with that we can move on to some of the code and so the first thing that we're going to do here is load our environment variables which includes the large

**[0:04:18]** language model that we're going to use I would recommend 01 mini and then also this is going to be explained a lot more later but you're going to optionally be able to show the a a I's thoughts as 01 is thinking to itself when it is reasoning about all the tool calls that

**[0:04:35]** it is making and so if we turn this off all that stuff is going to be hidden behind the scenes and not shown in our user interface if we turn it on then we can actually get an inside into how o1 is reasoning about everything which is super super cool I'll explain that more

**[0:04:49]** in a little bit here the next thing we're going to do is to find all of our configuration for AA including our access token and then we can get into defining our tools again this is going to be a bunch of different asaa tools I've actually used GPT 4 to help me

**[0:05:04]** create all these functions so it's really simple mostly boilerplate API code for Asuna so I'm not going to go over it in detail but just know that these are going to do a bunch of cool different things in ASA for me and I'll bind these as tools into my Asana chatot

**[0:05:18]** that's going to be using 01 that's going to be my AI agent and so the first function here the first tool is going to be creating a task in a sauna then we're going to have one to get our projects in a sauna another one to create a project

**[0:05:32]** another one to get all tasks within a project one to update a task such as the due date or maybe the description of it one to delete a task and then that's actually the last one so just a bunch of simple little functions here that will help me manage my tasks and projects in

**[0:05:49]** AA and the last thing that I'll do here is create a binding here a mapping from the name of each function to the actual reference to the function object in my python script and this is what we're going to use to bind every single tool into the agent so it can invoke it and

**[0:06:05]** so that's what we're going to do right now but it takes a little bit of setup to actually get this ready because the first thing that we need to do is create a list of descriptions that's going to tell our AI agent exactly when and how to use each tool and the way that we're

**[0:06:18]** going to do that very neatly is with the dock string that we have for each tool function and so this is what a dock string looks like right here and for every doc string you can see that I give a description of this function which will tell it when and how to use it an

**[0:06:33]** example call all of the arguments in great detail that it needs to supply to invoke the tool and then also what it can expect as a return so it can reason about the output of this tool so all this is packaged together neatly telling the agent everything it needs to know

**[0:06:50]** about every single tool and that is combined together into this neat little list of tool descriptions that we're going to bind into our first prompt to the llm to help help it understand everything about these tools and we'll get into that in a little bit as well the next thing that we need to do

**[0:07:07]** is we need to Define exactly how we expect 01 to return a response to us because we need a specific format to be able to process its response all the tool calls that it's requesting and also all of the arguments for each tool that it wants to invoke and so we're going to

**[0:07:25]** be doing that through a couple of classes that we're going to embed into the agent as an output parser and that's a lang chain concept that I'll explain in a little bit when we set that up and so first of all we have a class that defines how we expect a tool call to be

**[0:07:40]** formatted when the llm requests to invoke a tool and there's two parameters that we need first of all the name of the tool which is just a string and then also the arguments which is a dictionary and this is going to be a dictionary that maps to all the specific arguments

**[0:07:55]** that we need to invoke a tool like the ID the data whatever it might be and so if it needs to invoke this function it would say task GID colon is this ID data colon is this dictionary and that's how we would call update auna task just as

**[0:08:11]** an example and then at a higher level we have the actual response from the llm and so when it gives us a response when we invoke our chain that is the 01 agent it's going to give us a r dictionary response that has two attributes the first one is a list of tool calls which

**[0:08:29]** can be empty and this is just going to be a list of the class that we just defined above so the name and Arguments for all the functions that it wants to invoke and then the second thing is the content and this is whatever text it actually wants

**[0:08:42]** to return back to the user usually this is going to be empty when it wants to invoke tools but if it is done invoking tools or decides it never needs to content is going to be filled in here with the response to the user so with all this set up we can now finally

**[0:08:57]** create the prompt that is going to to tell the 01 agent exactly how to work with this custom function calling setup and so I have actually spent a lot of time pouring into this prompt and making it really good it's pretty detailed here so I'm not going to go into it greatly

**[0:09:12]** but basically it just describes to the llm how to work with these different schemas how to work with the custom function calling and when to invoke it how to work with that I give it all the descriptions of the tools using the dock strings that I described earlier and

**[0:09:26]** then finally I tell it about the idea of giving thoughts so B basically a thought is going to be an AI message that starts with thought colon and it's going to be an internal dialogue that the llm has with itself and so it's not to be shared with the user it's just meant to give

**[0:09:42]** the llm context for itself about what happened when it invoked a tool or any errors that it needs to correct when invoking a tool and so that show thought environment variable at the top when it's set to true that's actually going to be displayed to the user so we can

**[0:09:57]** actually go into the llm internally and see all of its thought processes as it's invoking tools and reasoning about the outputs of them but if it's set to false then all of these messages that I'm talking about here that start with thought colon are going to be hidden

**[0:10:12]** from us and so we'd have a regular chatbot where we're not seeing the inner workings of its thought processes and that is honestly my favorite part about this whole setup I'm kind of proud of of how I implemented all this because it makes it really easy if we want to see

**[0:10:24]** exactly how it is invoking all the tools and correcting itself when it needs to do so so yeah really cool stuff and so with that we can get into our functions for actually prompting our AI agent and so the first thing that I'm going to show you here is a Nifty little function

**[0:10:38]** that adds one of those thoughts to the conversation history and so using our streamlet session State we're just going to append that thought as an AI message but again we're describing in context for the llm that it actually wants to ignore these thoughts as far as providing an answer to the user and just

**[0:10:55]** use that for its own internal dialogue and then if we want to show the thoughts based on that environment variable will display it to the UI as well and so with that we can start our prompt AI function this is where we do all of the work of

**[0:11:08]** actually interacting with our agent we have a couple of things for error handling that I'll get into in a little bit basically you want to make sure we don't Loop forever sometimes the llm will hallucinate and do that and so we have a little fail safe here but the

**[0:11:20]** first real thing that we want to do in this function is Define our Lang chain chain that is going to be our chat openai instance that will reference the 01 model and so we're using a Json output parser using that tool call or response class that I defined up here

**[0:11:37]** and what this is going to do is basically enforce that the output we get from the 01 llm is going to be a dictionary that has exactly these values and nothing different so we're going to be guaranteed that if the invocation of the llm does not fail that means that we

**[0:11:56]** have a list of tool calls and a content stram that will be guaranteed and so going forward in this function we will just assume that we have those two attributes available and that they are formatted in a valid way so the next thing that we want to do is actually invoke our chat

**[0:12:13]** and we're going to do that with the streamlet session State the messages that we're building up that will maintain the conversation history and if there's any kind of exception getting a response like if it didn't give the right output format with the tool calls and the content then we're just going to

**[0:12:28]** recursively call the function again to prompt the AI and that looks like I have an extra old parameter here I'll fix that after but anyway just a little bit of recursion to basically have the AI redo its answer and most of the time it'll get it right the second time if it

**[0:12:42]** actually fails the first but 01 is pretty good at not doing that the next thing that we're going to do is check to see if we have any tool calls and so again tool calls at this point is guaranteed to be an attribute of the response because we are using our Json

**[0:12:56]** output parser so if we do have any tool calls then we're going to Loop through every call that we have get a reference to that function that tool function that we want to invoke and then actually invoke it with the arguments that 01 has decided it wanted to call with like the

**[0:13:13]** due date and the name of the task to create whatever that tool argument might be and then if we fail to invoke the tool for whatever reason like maybe the arguments were invalid then we're going to add a thought to the llm and basically tell it that you tried to

**[0:13:27]** invoke this tool but you failed to do so and here is why we'll include the exception message in the thought and so that way we're going to recursively call Prompt AI it's going to basically retry but with this added context so it knows exactly what it got wrong so it knows

**[0:13:42]** how to correct itself and this is very very powerful and from my preliminary testing it works so so well so I'm really excited to show this to you because we basically just add this thought and then use recursion to try again now if we don't fail to invoke the

**[0:13:57]** tool then we'll print the output and then add a thought so giving context to the llm that hey you invoke this tool with these arguments and here is the response that you got back and so that way it knows how to reason about the output to ultimately give an answer back

**[0:14:11]** to the user like yes I did create this task or yes I did create this project or mark this task as complete whatever it might be and so then the next thing that we're going to do is add this tool call to the list of tool calls cuz one thing

**[0:14:24]** that I've noticed that even 01 likes to do even though it's a really powerful llm is sometimes it'll hallucinate and try to make the tool call a second time when it's already made the tool call and it should be just giving its final response to the user and so I've added a

**[0:14:38]** little bit of airor handling for that just to make this whole AI app even more robust and this works super super well as well because basically what we're going to do is this entire tool calling right here only happens if the tool call that it wants to do is not already

**[0:14:54]** something we have invoked but if it is something we already have invoked in this else right here we're going to add a thought that says I already called this tool with these arguments and this is the response that I already got and so then we'll go through recursively

**[0:15:08]** call Prompt AI again and then make sure that we're not making the same tool invocation over and over and over and over again and so this catches any Loops that we might have in our llm and that is very very important for this custom function calling implementation the next thing that we're

**[0:15:23]** going to do is at the end of this function here we're just going to recursively call Prompt AI so if we inv tools at this point we've invoked it successfully added the thought of the result of calling that tool then we're going to recursively call Prompt AI to

**[0:15:37]** either make the next tool call that might be necessary or produce that final response for the user like I said before something like yes I've created the task for you and then the very very last thing we're going to do in this function is if we don't have any tool calls at

**[0:15:51]** all so this is if we have tool calls and we do all this good stuff if we don't have any tool calls then we're just going to return the AI response directly because at this point it's a simple back and forth between the user and the Ai No

**[0:16:03]** tool calls are necessary and so we can take the content from the AI response and just spit it back out to the user immediately and so that's what we're doing here and so with that was definitely in depth but that is everything that we have for this whole

**[0:16:16]** custom function calling setup and what we need to do to actually invoke the AI and handle any tool calls and so really quickly I'm going to go over the main function and then that is it so I appreciate you bearing with me I hope that this is providing a lot of value to

**[0:16:29]** you even even if not all this is making sense I hope you can see how truly powerful it is and how much error handling and robustness I've added into this to make it a really powerful AI agent even though I can't leverage all of the Power of open ai's native tool

**[0:16:43]** calling and so yeah going to the main function quick here we're just going to add a title to our streamlet UI and then also initialize our session State the messages which is going to as I described earlier start with just one human message and this is basically the

**[0:16:57]** replacement for the system message because I tell the AI again you can't have system messages with o1 it's one of the limitations we're basically telling the AI who it is giving it the current date for some extra context and then here's where we inject all that tool text that big prompt that I showed

**[0:17:13]** earlier that describes to the llm exactly how to work with this custom function calling setup and so all this Begins the conversation so it has that in mind with the rest of the requests from the user the next thing we're going to do is just display all the current

**[0:17:27]** messages in the UI that are being managed in the chat history through the messages session State and then we're going to prompt the user so creating this chat input where we get the requests from the user every time we get one we'll add it to the UI and also our

**[0:17:41]** session State and then we'll prompt AI we'll call Prompt AI to get the response and then also display the ai's response to the UI and add it to the backend session State as well and that is everything we have now fully coded our stream eyi the custom function calling

**[0:17:57]** interaction with the 01 agent and everything so we can go over to the terminal now and actually run this so we can interact with our AI agent in the browser all right here we are in the streamlet UI for my 01 custom function calling AI agent and now I'm just going

**[0:18:11]** to play around with this and show you how powerful 01 really is as an agent and so the way that I started this just show you really quickly here I went into the directory that you can clone from the gith repository and I ran the command streamlet space run space1 Ai

**[0:18:26]** agent and so this instantly started up this URL here and open it up in my browser and so now I can go ahead and talk to my agent and so there's a ton of different things that I can do in a sauna here I'm just going to pick a

**[0:18:38]** couple of random things and also I have the thoughts turned on so I'm going to show you in depth what the AI is thinking about as it is processing my requests and fulfilling them and we'll see how good it is at reasoning this thing is just incredible from all the

**[0:18:51]** testing that I've done already so the first thing that I'm going to ask it is create a task in my coding project to code Thing One by Sunday and so this is actually more of a complicated request because at this point it doesn't even know the ID of my coding project so it

**[0:19:07]** has to fetch that and then it has to go and create the task reason about the date that it's due give a title for and everything and then return the response back to me so we have our first thought here it called create a SAA task but the

**[0:19:20]** project is wrong it needs to give a project ID not just a name and so it's definitely not right and also the due date parameter should be due on so there's a couple of mistakes here but it got the error and now it's reasoning about how it needs to actually fix it

**[0:19:35]** and so this time when it gave a second shot it decided first it needs to call get a projects and this is exactly right this is just beautiful the reasoning that it has here because now it's going to actually be able to get the project ID not just some arbitrary name of the

**[0:19:49]** project that it made up so it started with the hallucination but then it was able to correct itself which is just awesome and I know that maybe I should probably format this Json a little bit but I don't wanted this to be like super super massive and mainly what you want

**[0:20:02]** to focus on here is just the thought and then what it did um so now it called create a sauna task and the arguments this time included a project ID and a task name and then the due date so it it's almost right here this is going to

**[0:20:15]** actually create the task in Assa and I'm actually going to show this here I'll go into my ass and sure enough I've got code thing one due by Sunday so this is working really really well but at first it didn't actually have a due date of Sunday it had a due date of today

**[0:20:30]** because the due date parameter is supposed to be due on so what happened is it saw that it actually didn't make the due date right and so then it decided it needs to call update ass task changing the due date to 20240 922 and sure enough it calls it it updates the

**[0:20:48]** due date successfully and now we have the right due date that we saw in a sauna right here so one simple request here but it had to get its bearings about what are the IDS for projects how should it update the due date and so it had to reason about itself actually

**[0:21:03]** quite a bit here so if I scroll up and go through all this like there's like a lot of thoughts that went on here and honestly it's not the cheapest but this is actually 01 mini this is not the most powerful model because that is more expensive and takes longer I just wanted

**[0:21:17]** to go with the mini one here um and yeah at the end here we get the answer that the task is created absolutely perfect so all that internal dialogue it figures out what it needs to and then it creates the task in me it is just so good and

**[0:21:28]** now say okay now I actually want to delete it so now we'll now we remove this and then I'm just going to test with one more thing that's a little bit more complicated and then we'll go from there and I think yeah that'll pretty much be it so yeah boom there the task

**[0:21:42]** is gone we deleted it and we'll get a response uh so yeah first it just has the thought and then yep here's the actual answer so if we had thoughts turned off it would have just told us this which is absolutely perfect so now here's the next thing that I want to do

**[0:21:54]** I want to have it create multiple tasks for me at once so I'll say create three tasks for me in coding and I'll say um we'll say build the next big SAS make an uh AI pet startup not the perfect grammar there that's totally good and then I'll say uh code the next

**[0:22:18]** moon launch all right let's go and so at this point it's a little bit more of a complicated request because it has to reason about creating the first task and everything it might need to do to correct that and then create the second one and then the third one so it's going

**[0:22:32]** to take a little bit longer so I'm going to pause and come back once this is complete all right and this was actually quicker than I thought it was going to be because this time it already remembers now the ID of the coding project so it doesn't have to go through

**[0:22:43]** the whole process again of looking it up and correcting itself and so this was pretty quick here it called each of the creat a sauna tasks for each of these tasks it had the thought of that it already called it so looks like it maybe tried to uh call the same task creation

**[0:23:00]** again but it caught itself with that error catching that I have and it figured out it doesn't need to do it again and then finally it returned the response back to me I'll go over to my coding project and sure enough we've got all these tasks ready for us it looked

**[0:23:13]** like it messed up a little bit because it said the due date is today um well actually maybe that's fine is that fine because did I say It was supposed to be Sunday it looks like it tried to make the due date of Sunday but it failed so

**[0:23:25]** it didn't correct itself there so it looks like it's not perfect but it is definitely doing an amazing job and we could obviously just correct it very very easily and say something like hey you didn't make the right due date just update it quick and it would do so um so

**[0:23:38]** I'm leaving this in here to show that like it's not 100% perfect and you might want to experiment with this a little bit more if you want to take it up but it is definitely working really really well and this setup is just so so cool and 01 is amazing all right so that is a

**[0:23:51]** wrap for our custom function calling 01 agent I hope that you found this super super useful because without it you're not actually able to create AI agents with 01 hopefully in the near future once we get out of beta for 01 fingers crossed that is soon we'll be able to

**[0:24:06]** use open AI direct tool calling and not have to have a workaround like this but in the meantime this is a really powerful way to start using 01 right away for agents and also it's just a really cool implementation to learn more about how function calling actually works under the hood I don't know

**[0:24:23]** exactly how open AI does it but it's going to be something like this because obviously this works really really well especially with 01 having such good reasoning capabilities and it being able to correct itself so much so that is everything I got I got the code in the

**[0:24:37]** description as well if you want to take a look at everything we just made if you found this valuable I would really really appreciate a like and a subscribe and with that I will see you in the next video
