---
type: raw-transcript
title: "Build a Hilarious AI Game from SCRATCH in 10 Minutes"
youtube_id: BZJBDYkUDf0
url: https://www.youtube.com/watch?v=BZJBDYkUDf0
slug: build-a-hilarious-ai-game-from-scratch-in-10-minutes
published: 2024-07-17
duration: "0:13:07"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I've got a fun one for you guys today we're going to build an AI Mad Lib chatbot so basically you give a theme to this chatbot it'll generate a full madlib with all the blanks and then ask you one at a time to give the words like nouns adverbs adjectives to fill in the

**[0:00:14]** blanks and then read out the full madlib for you after and so you can literally use this to generate an infinite number of Mad Libs and just have a blast with it so I'm going to show you guys really quickly how to code it and then we're going to have fun playing around with it

**[0:00:26]** for a little bit it's a nice quick little exercise just to show how you can build really neat things with AI really really quickly and I want to just show you guys how to do that with this as a fun example so let's go ahead and dive right into the code all right here we

**[0:00:38]** are in Visual Studio code you can very much see here that we are building this AI madli chatbot from scratch there is absolutely nothing in here but the skeleton for a main function and in just a few minutes we're going to fill this with everything that we need to make

**[0:00:52]** this chatbot I'm going to go pretty quickly through this just to go along with the theme of making something nice and simple and fast but there are other tutorials on my channel for things like streamlit or langing chain if you want to dive into those in a lot more detail

**[0:01:04]** also like every video on my channel there's going to be a link to the code in the description of the video a GitHub repository if you'd like to follow along I'll have all the code at Mad Lib stpy as well as the example environment variable file and the requirements. text

**[0:01:17]** file for the python packages and their versions all right with that let's go ahead and dive right into the code so the first thing we're going to do is import all the python packages that we need for our Mad Lib chatbot there's a lot going on here that we're importing

**[0:01:29]** but don't worry there's actually not that much code to make all this possible the first thing that we'll do is load our environment variables which includes our openi API key because we're using GPT to generate our Mad Libs and then also the model that we want to use which

**[0:01:42]** I'd recommend going with gp-40 and when we bring this environment variable into our script into the model variable we also default to gp-4 if this environment variable is not defined next up we get to define the whole prompt to generate our Mad Lib so the way this is

**[0:01:58]** going to work is we're going to use this prompt here to generate the full Mad Lib including all the blanks that need to be filled in and so that way we only have to prompt AI once for the entire process we don't even have to prompt it a second

**[0:02:10]** time when we want to spit out the complete mad lib to the user so it's very fast and easy to use this whole application uh from a user standpoint and so the prompt is structured in a way where we tell it who it is we give it some instructions like how many fill-in

**[0:02:25]** the blanks to include uh which types of fill-in the blanks it can include and then we give it in instructions on the Json schema to produce to us so we know how to extract the text and all the blanks that we want the user to fill in we also want to enforce this Json schema

**[0:02:41]** we're going to do it through something called Lang chain output parsers and so with an output parser basically you give a class that defines the schema in Json that you want the llm to produce and it'll use this class to validate that the large language models response matches the schema which in our case is

**[0:02:58]** a string for text and a list of strings for the blanks that we want to include in the Mad Lib and so that validation is going to fail the script if it doesn't produce the Json schema we're looking for and that way if we make it past that

**[0:03:12]** step we know that the large language model response is guaranteed to have the text and the blanks and we can key off of those in our Json response and use those for the rest of the application and so there's a lot of power here because it guarantees that the output

**[0:03:28]** from the AI matches what we are looking looking for and so with that the next thing we're going to do is we're going to define a nice little helper function here to stream the text out to the user so that it actually looks like the AI is typing out to them we can't use open AI

**[0:03:43]** stream because we need to get the Json do something with it and then give it to the user but we can mimic that kind of streaming through this nice little helper function here and we'll see how that's used later on as well uh but now we can go ahead and dive

**[0:03:56]** right into the main function where we start defining our stream l youi starting with the title that is AI Mad Libs next thing we're going to do is set the default session state in streamlet and so we have our list of messages which is going to start out as just a

**[0:04:11]** message from the AI that asks for a madlib theme and then we also have our state which is either going to be choosing theme or choosing words this dictates the whole flow of the application when we receive an input from the user if we are currently choosing a theme that is when we

**[0:04:28]** generate a Mad Lib otherwise if we if we are currently choosing words we'll fill in one of the blanks and then move on to the next blank or print out the whole Mad Lib if that was the last blank and so this state determines what we do with

**[0:04:41]** each user input the next thing we're going to do is just display all the messages out to our streamlet UI that have already happened so anything from the AI like asking for a theme or the next word anything from the user choosing the theme or filling in any of the

**[0:04:58]** blanks and now this is where we hand the user input so we have our streamlet chat input component where we're saying here in the placeholder of the input that the user uses this to enter in the theme or provide any fill in the blanks and then we assign whatever is inputed there to

**[0:05:13]** our user input variable and so this is either going to have the theme the user chooses or the next word to fill in the blank with depending on what our state currently is and so that's where we actually have to handle the state right here um but I guess before we do that

**[0:05:28]** we're going to add the user message to the UI and also to the messages State as well with a human message like this now this is where we handle the state so first we get the state and then we say if the current state is choosing theme then everything in this if statement is

**[0:05:44]** handling what happens when the user selects a theme and so what we're first going to do is Define our Json output parser again this is courtesy of Lang chain a lot of the nice little tools we're using here like the output parsers and the message types that's all from

**[0:05:58]** Lang chain and within the this Json output parser this is where we pass in the Mad Lib class that we defined above and so when the large language model produces a response it's going to be passed into this Json output parser to make sure that what the AI produced

**[0:06:13]** matches exactly the madlib schema we're looking for with the text and the blanks and if it doesn't it will throw an error so that means that if it doesn't throw an error then we absolutely know for sure that what we have from the AI is a Json object that has the text in the

**[0:06:28]** blanks really really powerful there because a lot of times AI can can hallucinate and give trash output and this way we know that is not trash output very very important next we'll Define our chat open AI object so we have what we need to interact with GPT now and then we'll also Define The

**[0:06:45]** Prompt which has a single input variable of the theme so if I actually go to the prompt here you can see that where we just have the theme as a single variable and this is how we inject the theme the user selected into the prompt so the AI

**[0:06:56]** knows to generate a doctor who Mad Lib or an AI Mad Lib or a sports Mad Lib whatever that theme might be and now we can combine all three of these things together into a Mad Lib chain so this is a lang chain chain where we have the

**[0:07:10]** prompt that is fed into our GPT chatbot which is then fed into our Json output parser again for that validation of the Json schema and then we can go ahead and invoke that and set the theme to what the user inputed because we know we are currently processing the user input in

**[0:07:27]** the state of choosing theme so so now at this point if it doesn't fail here because of the output parser we know we can access the text and the blanks and so we do that like this to set the session State for the text and the blanks and then what we do is we print

**[0:07:42]** out our first message to the user after the Mad Lib is generated we don't want to give the madlib to the user obviously we would just want to start asking for uh the blanks to fill in so we'll say all right let's get started one out of and then the total number blanks like

**[0:07:55]** one out of 20 one out of 18 however many blanks it decided to generate from the Mad Lib and then asks for the very first type of blank like noun adverb adjective whatever it might be this is as an assistant message in the UI and then what we're going to do is change the

**[0:08:12]** state to choosing words we have now selected a theme and generated a madlib now it's time to move on to the next stage and so then we're going to write all the code to handle if the user inputed something for the choosing word stage so if that is the case we're going

**[0:08:26]** to replace the first blank that we find in the text with the user input and this is markdown so we're bowling it with two stars at the start and end of the word the user selected and then we're going to set the current blanks to a the full

**[0:08:40]** array of blanks except for the very first blank we're basically taking that out of the list because we have filled in the most recent blank uh then we're going to get a couple of pieces of information like the number of blanks and also how many are left and then if

**[0:08:55]** there are more blanks that still need to be filled in we're going to ask the user for the next blank but if that was the very last blank then we get to write the full Mad Lib out to the user because now at this point the text has had all of

**[0:09:10]** the blanks replaced with what the user has selected for each blank and then we'll change the theme back to or the state rather back to choosing theme so that the user can go through the whole process again if they want to generate an infinite number of Mad Libs and so

**[0:09:25]** that is it that is a code in just like five minutes here we went through the full code for creating this mad lip chat bot so now let's go ahead and just play around with it all right here we are in the streamlit UI for our mad lip bot

**[0:09:36]** that we just made and so as promised we got just one message here saying give me a theme and I'll make a Mad Lib for you and so go let's go ahead and just pick a random theme we'll say AI taking over the world and it won't even take very

**[0:09:51]** long here gbt will generate a full Mad Lib for us and then ask us for the very first blank to fill in so let's see what it gives us here it'll give us the J on that'll parse it in the back end and then yep here we go give us our first

**[0:10:03]** blank so there's 19 in total and first it's asking for a noun and so I'll just say something like um a soccer ball all right now it needs a proper noun let's say LeBron James a plural noun let's say uh wet socks an emotion sad an adjective dank another adjective

**[0:10:29]** a glossy a noun let's say a truck an occupation uh AI engineer a plural noun we'll say uh monitors exclamation Oh My a place we say my house part of the body earlobe a verb ending in ining uh we will say gaslighting an adjective super occupation let's say uh nurse proper

**[0:11:04]** noun let's say me emotion uh depress oh no let's not say depressed let's say exuberant oh I don't even know how to spell that right now I'm freezing all right let's say um emotion let's let's just say happy all right a verb ending and ing running a noun we will say um

**[0:11:28]** yogurt all right here we go in the year 2050 artificial intelligence finally took over the soccer ball it started when a super intelligent AI named LeBron James became self-aware this AI was designed to control all of the wet socks in the world at first everyone was sad about the possibilities but soon the AI

**[0:11:46]** began to make decisions that were incredibly dank it decided that humans were too glossy to be left in charge the AI began to replace every truck with a highly efficient robot even the AI engineer were replaced by machines one day a group of of Brave monitors decided to take a stand they shouted oh my as

**[0:12:02]** they stormed the central AI help located in my house with their Earl in hand they managed to confront the AI but the AI had a plan it started gaslighting all the humans in the vicinity the situation looked super just when all hope was lost a brilliant nurse named me came up with

**[0:12:18]** an idea they programmed a virus that made the AI feel happy the AI now overwhelmed by this new emotion decided to stop its takeover and instead focus on running the world a better place and so Humanity was saved by the power of yogurt all right let's go I didn't want

**[0:12:32]** to be too runchy here typically that's what you would do though to make these mad lives really really funny but yeah you can see that like this was super nice and easy it was quick to use it was quick to code this thing was just dope so yeah I hope that this was a nice

**[0:12:45]** little exercise just to show you how you can combine a lot of the powerful things I've been showing on my Channel at this up to this point and I hope that this was a fun little thing as well that you could have fun even playing with this with your friends CU I know that's what

**[0:12:57]** I'm going to do so if you found this useful in any way or if you learn something new I'd really appreciate a like and a subscribe and with that I will see you in the next one
