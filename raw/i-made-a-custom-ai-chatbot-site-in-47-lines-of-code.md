---
type: raw-transcript
title: "I Made a Custom AI Chatbot Site in 47 Lines of Code"
youtube_id: blQAUBtCgdc
url: https://www.youtube.com/watch?v=blQAUBtCgdc
slug: i-made-a-custom-ai-chatbot-site-in-47-lines-of-code
published: 2024-07-03
duration: "0:08:46"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** today I'm going to show you how you can build a GPT powered custom chatbot with a full user interface and only 47 lines of python code building custom chat Bots has never been easier now the first question you might be asking is why bother building a custom GPT chatbot why

**[0:00:17]** not just use the GPT website the big reason for that is there is so much power that you can put into a custom chatbot this goes into what I teach here on the Channel with AI agents but you can create these chatbots that will actually interact with external Services

**[0:00:33]** third party libraries API endpoints to do things for you that GPT cannot do for you schedule appointments manage your tasks look at your calendar availability all these things that you can't just do with gbt you can do it with an agent and that starts with having a custom chatbot

**[0:00:50]** so without further Ado let's di right into creating this chatbot in 47 lines of code so to start we have a very basic python script that's just a skeleton with a main function We'll add everything in here for our custom chatbot and user interface so just a fair warning I'm going to go pretty

**[0:01:06]** quick through this today because I want this to just be a really quick example of how to build a custom chatbot if you want a lot more detail on things like working with Lang chain or streamland or creating AI agents I actually have an AI agents Master Class series on this

**[0:01:20]** channel where I go into all these things in much greater detail so you can follow along really clearly but today we're just going to make something really cool really fast and so the first thing that we want to do is actually import all the libraries that we need for this

**[0:01:33]** application things like streamlet for the UI and Lang chain for interacting with our large language model which is gbt in this case along with that I have a requirements. text file so that if you want to follow along you can actually clone my GitHub repository and you'll have all the python packages and their

**[0:01:49]** versions defined here and then also a EnV example file for you to see the invironment variables that you need to set to authenticate with open Ai and also set the model that you want to use and So speaking of that we will load our environment variables with this simple

**[0:02:03]** line right here and then Define the model which is based on the llm model environment variable and defaults to gp-40 because that really is uh the most powerful model at the time of this recording except for maybe Cloud 3.5 but anyway that is a whole separate video so

**[0:02:19]** let's keep going all right the first thing that we want to do is we want to add a title to our user interface and the way that streamlet works is whenever you want to add something add some sort of component to the user interface you just call St which is how we are

**[0:02:33]** importing streamlet in the script Dot and then whatever the component is that you want to add to the UI so in this case I want to add a title and I'm calling it streamlit chatbot the next thing that I want to do is if the messages is not defined in the session

**[0:02:48]** State for the streamlit UI yet I want to Define that and so I'm going to start off with just a simple array with just one message to start and that is the system message which kind of sets the context for the whole convers ation with the chatbot you can include a lot of

**[0:03:03]** things here like you are a personal assistant or you are a financial expert who does XYZ that's where you set that kind of thing here in the system message uh for just kind of like a demonstration purpose here I just have it say the current date because actually AI doesn't

**[0:03:17]** always have the current date a lot of models are missing that so it's just kind of nice to add that so that is how we initialize this session State uh with the messages one really important thing to note with streamlet is that every every time there is a UI State change

**[0:03:32]** with your streamlet UI it'll actually rerun your entire python script and so that's why we say here if messages is not currently in the session State because of course the first time we run our script it won't be but then when there's a UI State change and it runs

**[0:03:45]** the script again it will be there so we don't want to run this again because that would override the list of messages that we built up in the chat history and set it back to just a single element array with the system message all right so moving on what we're going to do is

**[0:04:00]** we're going to actually add all of the messages that are currently in the message state to the user interface and so we get the Json for each message and we add a component here st. chat message so just like the title this is a component that we're adding to the user

**[0:04:16]** interface and within the chat message we are using markdown to just display the text message that is either going to come from the assistant or from the user and so this builds up the history every time the UI State reloads and displays all of the chat messages between the

**[0:04:31]** user and the AI the next thing that we want to do is we are creating a chat input component that is going to be in our user interface and if there's actually a value here like the user types something out and hit enter then that is going to be assigned to The

**[0:04:46]** Prompt variable so if this prompt variable is defined I.E the user actually inputed something then everything within this if statement we are going to perform in this current cycle of our UI so the first thing that we're going to do is we're going to add this new chat message to the UI then

**[0:05:04]** what we're going to do is add this message to the session state so basically every time there is an assistant message or a user message we need to update both the UI and the list of messages in the session State at the same time so that's what we're doing

**[0:05:17]** here and then we're going to get a chat message ready to display the assistant response so within here we are going to create an open aai chatbot instance and then we're going to stream the response from invoking the AI with the list of messages that we've currently built up

**[0:05:35]** which also includes the latest user message and so that's how we're going to get the response to the user message from the AI and then all we need to do is write that stream from open aai out to a stream within streamlit and so that's going to update the UI so that we

**[0:05:52]** have that stream that comes out in a nice typewriter style where it types out the response from the assistant you'll see that in a second here and then the very last thing that we have to do is we just have to add the AI message the response from the assistant to the

**[0:06:04]** streamlit session State and that is it like I promised 47 lines of code and I can make this even shorter if I cut out all the comments and stuff and that is literally everything so now we can go ahead and run this chatbot all right so to actually run this chatbot now that we

**[0:06:20]** have it all coded up in 47 lines we just need to run the command streamlit space run space and the name of our python script which in this case is streamlit Das chatbot dopy uh just keep in mind that I'm in the current directory where the script is and that's why I don't

**[0:06:35]** have to write out the full path to the script so with that once you run it you're going to get a couple of lines spit out that look something like this and it'll actually automatically open up your browser so you can see the user interface right away so let's go ahead

**[0:06:47]** and switch over to that all right so here I am now in my browser in the streamlit chatbot page that opened up when I ran the streamlet command and you can see here right away that the system message is displayed so this already show is that it has that as that first

**[0:07:02]** message in the chat history and then to actually talk to the AI all I have to do is say something like hey how is it going and then you can see here the response spit out really really fast and it spit out in typewriter style so it actually you could see it typing out the

**[0:07:17]** response it did it pretty quickly but you can see that it wasn't just instantaneously the entire response thrown into the UI super super nice streamlet also has some neat little features where you can do things like go into the settings and change the theme and stuff stuff um so there's a lot

**[0:07:31]** there to make this a robust UI right out the bat without having to do a ton of custom coding with react or vanilla JavaScript HTML and CSS you can just have this right away within a simple python script it is really really nice so let's ask another question here let's

**[0:07:45]** say how far is the earth from the sun there we go that is so so beautiful so you can see here that it's really basic at this point there's not a reason to do this over just using chat gp.com but now that this is all custom coded I

**[0:08:05]** can take this so much further by turning into an AI agent and having it interact with my calendar interact with my tasks or interact with a Discord server or a slack Channel there's so many things I can do that I can't do with GPT and I have the possibility to take this so so

**[0:08:21]** far so that is everything that I've got for you today creating this chap B 47 lines of code if you found this useful in any way I would really appreciate like And subscribe also feel free to check out my AI agents Master Class where I go into all these things in much

**[0:08:35]** more detail creating more powerful applications using Technologies like we see here with streamlet and laying chain so thank you for watching I will see you in the next one
