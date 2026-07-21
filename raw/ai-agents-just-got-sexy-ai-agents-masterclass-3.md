---
type: raw-transcript
title: "AI Agents Just Got Sexy - AI Agents Masterclass #3"
youtube_id: ft9Z67d1wik
url: https://www.youtube.com/watch?v=ft9Z67d1wik
slug: ai-agents-just-got-sexy-ai-agents-masterclass-3
published: 2024-07-07
duration: "0:16:18"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have seen so many people make really really cool AI agent applications but they either have no user interface to interact with their chatbot it looks really terrible or even worse they spend days weeks even months working on their interface when it really doesn't have to be that complicated and so that's

**[0:00:17]** actually want to show you how to do today I'm going to show you how to take the AI agent that we've developed over the last couple of Master Class videos and create a really beautiful and simple user interface around the chatbot it's going to be so easy to make and it's

**[0:00:30]** going to make everything look so much better so let's go ahead and Dive Right In All right so here we are in the code we had from the last Master Class video where we incorporate laying chain to make our asaa AI agent chatbot much simpler and more powerful and now we get

**[0:00:45]** to add the user interface cuz before we were just using the terminal and it wasn't very pretty and now we're going to make it look really sexy and easy to use and we're going to use all of this to make things much easier to work with in all the projects that we got in the

**[0:00:57]** master class going forward just like the last two videos I had I'm going to have a link in the description of the video to the GitHub repository where you can follow along with everything that I'm doing here and I show you exactly how to set up everything just like I have so

**[0:01:10]** you'll clone the GitHub repo and you can pull in this folder right here 3- agent-- and then I have the example environment variables you can follow along with very easily and also the requirements file so you can see the exact python packages and their versions you'll need to run everything that I

**[0:01:24]** show here so with that we can Dive Right In to the code so the first thing we're going to do here here is import our shiny new toy streamlit this is the python package that is the key to creating beautiful and simple user interfaces in fact it's so simple that

**[0:01:40]** we don't even have to change the way we're interacting with our large language model right now and so this function right here to create our Assa task we don't have to touch that at all this function even to prompt our AI we don't even have to touch this right now

**[0:01:53]** we will when we get into streaming later to make our responses even more robust in the UI but for now we're going to leave this exactly as is the only thing that we're going to touch to get our UI up and running is our main function because this is where we handle our user

**[0:02:06]** messages and our AI messages right now we just display them out to the terminal as you can see here but now we're going to make it actually display to an interface that we have running in our browser with streamlet and so right off the bat we're going to start by adding

**[0:02:19]** our first component to our streamlet UI and that is a title so the way that you add any component to the UI with streamlit is you say streamlit or St for short because that's how we imported it in our script Dot and then the name of the component that you want to add so it

**[0:02:34]** can be uh user input or title chat message dot whatever you want and then we're saying the title is a SAA chatbot so we could literally run this now we had to have a user interface that's blank except for we have a title now and is that simple to get started you don't

**[0:02:49]** have to have all the boiler P that you need if you were to develop a full website uh with something like react or vanilla JavaScript with HTML and CSS super super nice the next thing that we're going to do is we are going to initialize some session state so

**[0:03:05]** everything that you want to manage in your user interface with streamlet you manage with session state so we'll store our chat history I.E the messages we'll store the user input all these things are going to be kept in the session state so that it can be maintained as

**[0:03:20]** the application runs and so if messages is not in the session state currently we're going to set it to an array which is a single value which is the system message so this starts the default context for the conversation which this is where we just provide context like

**[0:03:35]** your personal assistant who helps manage tasks and a sauna and we give it the current dat as well to help with its accuracy for due dates now the reason we have to check and make sure that messages is not already in the session state is because of something very very

**[0:03:51]** key with streamlet this is very important to know whenever there is any change to your user interface with stream li like a user enters a message there's new text on the screen large language model produces a response streamlet will rerun your entire python script that's how it Cycles through and

**[0:04:08]** updates the UI with anything that changes and so with that we need to make sure that we only initialize the message's session state if it is not initialized already otherwise anytime you were to input something or the AI were to respond if we didn't have this if if statement here it would reset the

**[0:04:25]** messages every single time there's a UI State change to this array with just the system message message so it clear the entire chat history and go back to the system message every single time we don't want that and so I took a bit of time to explain that there because

**[0:04:38]** that's really important to understand how streamlit works and this is just a good example of how we have to set up things keeping that in mind all right so next up what we're going to do is display all the messages in the UI that we currently have in the

**[0:04:52]** chat history so remember this runs every single time there's any kind of change and so every time the script runs we need to read display the messages to the UI don't worry it's really nice and quick so it's not going to look glitchy or anything just because it's redoing

**[0:05:06]** this every time there's any change to the UI so we Loop through every message in the state and we get the type of message and then we create a st. chat message component and then within it we use st. markdown to add the content to that chat message box that'll either be

**[0:05:22]** for the user or for the AI really really nice and simple now what we're going to do instead of looping forever we don't to do that within the user interface we're just going to react to the user input so we're adding a new st. chat input component to our UI with a default

**[0:05:41]** text of what would you like to do today that's just a placeholder and anytime there's any input that the user enters in this component it is automatically going to be put in this prompt variable and if there is anything in this prompt variable then we're going to do

**[0:05:55]** everything within this if statement and the first thing we're going to do is instead of appending messages to this array that we were managing in our python script before we going to actually add it to the UI with a new chat message component and we're going to add it to the session state so

**[0:06:12]** anytime there is a new message from the user or the UI we have to update both the user interface and the session State that's really important to keep in mind we want those two things to be consistent and so we update both at the same time and then for getting the

**[0:06:29]** response from the AI we're going to open up a new chat message component of type assistant and then we're going to get the response just like we did before except we're passing in the streamlet session State for the messages instead of that message array we had before and

**[0:06:44]** then adding st. markdown with the response and again adding the AI response to the message State just like we did with the user message and that is literally it I took just five minutes transform this entire thing from a terminal to a user interface with streamlet so so easy and so now we get

**[0:07:02]** to run it and see what our chatot looks like so we're back in the terminal this time to run our streamlet UI but this time we just run the application in the terminal we don't have to live in there and type in there and so the command to

**[0:07:14]** run this user interface is streamlet run and then the name of the Python script which is Agent with ui. piy in this case note that I don't have to give the full path to the script because my current directory is where I'm at right here uh with the python script and so you just

**[0:07:30]** go ahead and hit enter it'll take a little bit to spin up the UI and then you'll get these lines right here that say Hey your app is running in your browser and it'll actually automatically open up the tab in your browser with the user interface for your chatbot so let's

**[0:07:43]** go over to that all right our chatbot is looking much much better now not being in a terminal this user interface looks so clean and simple I love it it even displays the system message to us to show that this is the start of the conversation that default context we

**[0:07:58]** could also hide this if we want a lot of chat Bots don't show the system message but I just wanted to have that there to show you what it looks like also just a couple things I want to point out really quick you can deploy this in like a

**[0:08:09]** couple of clicks it's so easy to deploy streamlet applications so it's actually a full website there's also a ton of settings you can play with as well um like changing the theme all that good stuff and so yeah it's just a robust UI right out the gate with barely any work

**[0:08:24]** on your end it is so nice so yeah let's go ahead and let's uh actually talk to the AI hey how are you get a response super super quick I love it all right let's let's try to actually create a task now on auna so I'll say I

**[0:08:37]** need to go on a run by Tuesday all right let's see what it does for us here and boom there we go created a task going to run by Tuesday July 9th perfect and it even gives us a link and since we used st. markdown it's displayed neatly

**[0:08:54]** here in a hyperlink that is wonderful and so we can actually go over to Asana now and see if the task was created for us so let's go over TOA and boom there it is go on a run due date Tuesday Perfect all right there we go uh so now

**[0:09:09]** as a bonus I'm going to show you how to add streaming to the user interface and so that way the responses from the AI come out in typewriter style where you can see it typing out the message instead of it just throwing everything into the user interface at the same time

**[0:09:23]** it's definitely something you want in a more robust chatbot UI and so I'm going to show you how to do it now I wish I could say that streaming with AI agents that have tool calling is really simple but unfortunately there is a bit of trickiness to it but that is why I am

**[0:09:37]** here to break it down and make it really easy for you to understand and so the first thing to think about is how would we do streaming if we didn't have tool calling it's actually really simple and there's even a video I uploaded recently on my channel where I show how to create

**[0:09:51]** a streamlit chat bot without tool calling all you have to do here is in the function that you invoke the large language model with you just need to take the stream from the AI and return it end the function there give it over to streamlet to display on

**[0:10:04]** the UI really really easy but with tool calling it's a little bit trickier because we actually have two different calls to the AI depending on if we need to invoke a tool or not so this function here prompt AI it needs to create a stream return that to the front end

**[0:10:21]** display but it still needs to continue to invoke the function if applicable and then if it does invoke a function actually invoke the large language model a second time to get the response based on the result of calling the tool and so we can't just get the stream here and

**[0:10:37]** then return because that'll end the function so it can't do the function calling we need to return the stream and then still continue and we're going to do that using python generators and I'll show you how to do that so we can actually yield the chunks of the stream

**[0:10:50]** while still continuing through the function to invoke the tool and get that second stream as well so the first thing that we're going to do in our main function is accept the stream from The Prompt Ai call so everything looks pretty similar except we now get a stream that we write out to streamlet

**[0:11:05]** using the nice built-in component st. right stream nice and easy there and then we also need to update the way that we incorporate this message into the session State as well because now that we're getting a stream we're not getting that full AI message Lang Chang object returned to us from prompt AI so we need

**[0:11:23]** to build this manually where the content is going to be the full response once the stream is complete that is what we add to the session State for the AI message so that is everything that we have in the main function now we get to add streaming to prompt Ai and we don't

**[0:11:39]** even need to change the way that we create our Assa chatbot with tools object but we do need to change the way that we invoke it because instead of invoke we're going to use stream so we have the stream now that we get to go over the chunks and so we're going to do

**[0:11:53]** that just like this so we Loop over all of the chunks in the Stream and for every chunk that that is created we're going to yield it this is using the concept of generators in Python and so now the stream that we're putting in streamlet is going to be updated each

**[0:12:09]** time we yield a chunk but we don't have to exit The Prompt AI function so we're returning values without cutting the function short and then we also build up this gather Json which is going to include all the tool calls as you can see here so if there are any tool calls

**[0:12:25]** it is going to be in the gathered. tool calls array and so so now we can say if we have any tool calls we're going to invoke the tool just like we did before where we get the name and the arguments from what the large language model returned and then we'll actually invoke

**[0:12:39]** that tool and add it as a tool message to our chat history for the context for the AI and then going back down to the bottom here the way that we get that second response is very similar we get the stream from invoking prompt AI just like we got the message from recursively

**[0:12:55]** invoking prompt AI before and we're going to Loop over all of the addition chunks in our additional our second stream and we'll yield these chunks as well and so this entire time we've just been yielding chunked after Chunk from both of these responses that's what's going to be given to the user interface

**[0:13:11]** but we never had to return early in fact we don't need a return at all and so we can delete that as well and so that is it it's a little bit more complicated than what we've been working with before this point but it's still not that bad

**[0:13:24]** yielding instead of returning just to give all these chunks to the user interface while we can still continue on with that function so I hope that makes sense now we get to actually dive in and see what our chat bot looks like with the streaming all just a couple of

**[0:13:37]** Corrections I want to make before we dive into looking at the user interface with streaming I forgot to change AI response in a couple of places here it actually to actually be changed to gathered because that is the name of the variable that we have now that we're

**[0:13:50]** building up the response as we get the chunks and so we just have these couple of changes right here the other thing is I added the AI message here at the bottom you just have to make sure that you import that as well so I was getting a couple of Errors I was running this

**[0:14:03]** but those are the quick fixes so now we can just dive right into the user interface all right we're back in the as chatbot site I didn't even have to rerun my streamlit command to make my changes apply because streamlit automatically has hot reloading Incorporated so any changes you make to your code will

**[0:14:18]** automatically be reflected in your site without having to rerun anything so let's go ahead and test out the streaming so I'll ask a simple question again like hey how are you doing and there you go it typed it out you could see that it wasn't just thrown into the UI all at once like we saw

**[0:14:33]** earlier and so let me ask another question just to get something a bit longer so you can really see it typing out so I'll say uh when was the first 4 minute mile and how long exactly did it take all right there we go nice Roger banister May 6 1954 and so now we can

**[0:14:54]** actually test out creating tasks with streaming as well and so I'll say I need to to break the 4minute mile by Monday all right wow okay it didn't even let me do it right away it's it it's warning me that's kind of stupid to break the four minute mile within two

**[0:15:14]** days of training um I'll say create the task anyway I don't care I'm going to do it let's see what it does for me here there we go created the task for me and aun due by Monday July 8th we can head on over to ass and see if it worked

**[0:15:31]** and there we go all right break the four-minute mile by Monday it's very very ambitious AI didn't even think I could do it but I believe in myself so I'm going to do it anyway that is it we have successfully Incorporated streaming into our chatbot so there you have it in

**[0:15:46]** a short amount of time we've created a full user interface for the assana AI agent chatbot in the next masterclass video I'm going to soup the heck out of this chatbot and make it so it can do a lot of different things in a sauna besides just creating tasks and so I'm

**[0:16:01]** going to turn it into an agent that can fully manage my tasks for me and for you as well and so I look forward to seeing you in the next Master Class video If you enjoyed this content I would really appreciate a like And subscribe and I will see you in the next one
