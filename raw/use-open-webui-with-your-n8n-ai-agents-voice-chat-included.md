---
type: raw-transcript
title: "Use Open WebUI with Your N8N AI Agents - Voice Chat Included!"
youtube_id: E2GIZrsDvuM
url: https://www.youtube.com/watch?v=E2GIZrsDvuM
slug: use-open-webui-with-your-n8n-ai-agents-voice-chat-included
published: 2024-10-23
duration: "0:26:08"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** last month I showed you how to run all of your AI locally including your llms your vector database for Rag and n8n for your agent workflows we did this all using the local AI starter kit developed by the n8n team however there was one huge component missing that a lot of you

**[0:00:18]** requested in the comments open web UI so we could have a nice and featur interface to chat with our local AI setup so today I am super excited to unveil to you EX exactly that I have added open web UI into the local AI starter kit and created the custom

**[0:00:36]** functionality to make it possible for you to chat with your n8n workflows directly in open web uui just like you would with any model that you have running with olama and with open web UI you can even use voice to talk to your NN agents how cool is that open web UI

**[0:00:53]** is an open- Source chat GPT like interface that you typically use to chat with llms that are running with olama however they have a couple of key features namely functions and pipelines that give you the power to implement custom functionality on their platform to do things like chat with your own

**[0:01:10]** agents and API endpoints and that is what I leverage here to build this open web UI and n8n integration and I even have this integration published on the open webui function list on their website so I'm going to walk you through step bystep how to set up this entire

**[0:01:26]** local AI package yourself including setting up a basic AI agent work flow in n8n and integrating it with open web UI so you can chat with it there if you haven't seen my other video on the local AI starter kit I would highly suggest that you go and check that out but you

**[0:01:41]** certainly don't have to have seen that already to follow along here this is really really exciting stuff and you'll see in the video that you could easily take this edn integration and extend it to be able to use any agent that you create with open web UI so let's go

**[0:01:55]** ahead and Dive Right In so let's take it from the top and go back to the original Repository that I forked to create my own version with open web UI I would not be doing service to open source if I didn't go back to this repo and show it

**[0:02:09]** off because huge thanks to the n8n team for creating the original repo for the self-hosted AI starter kit essentially what this repository does is it gives you a Docker compose file and so we combine containers from all these different Services together in one place so that you have a neat package to host

**[0:02:27]** everything locally that you need to get started with local AI so specifically the services that are included here is n8n to build our workflow automations and make AI agents with all the other services olama for our large language models quadrant for our Vector database for Rag and then postgress for our SQL

**[0:02:47]** database to handle things like chat memory for our agents so all of these are containers packaged together running completely locally and it's just a phenomenal combination you'll see later that I have a workflow setup as a demo that combines these all together to create a really neat and simple AI agent

**[0:03:06]** and so what I did here to add on open web UI if I go into this Docker compos here you can see that all these containers are just the different Services here like postgress n8n quadrant and olama I just added one for open web UI and I'll show that in a

**[0:03:20]** little bit as well once I go over to my repository so this Docker compose is really really simple in fact this whole project is really simple but that's the best part about about it is it doesn't have to be complicated to get started with local Ai and I think that's one of

**[0:03:34]** the big reasons that my last video on my channel for this blew up so much because it just makes having everything running locally so accessible and so going over to my repository here you'll see that the readme it looks pretty similar because I just forked the local AI

**[0:03:49]** starter kit and added my own flavor into it and so I mention here that this is my version with couple of improvements that I covered in the last video on this and then also the addition of open web UI and I'll show that in a little bit as

**[0:04:01]** well and then I even have a link to my integration with NN and open web UI that I mentioned in the intro and so scrolling down to the list of what's included here this list should look very very familiar the only addition here of course is open web UI and if I go into

**[0:04:17]** the docker compose here let me go back and go into the docker compose all this is going to be in the description of this video so there'll be links to see the original repo download my version get that running all the instructions for that as well so definitely check

**[0:04:30]** that that out but yeah in this Docker compos right here all I had to do was add a section for open web UI so I'm pulling this as the fifth container for all of my services since it is the fifth thing that I'm adding into this starter kit essentially and so back over into

**[0:04:45]** the REM here I just want to go over the instructions really quick before I dive into that I have customized everything to my repository so all the get clone commands are going to be cloning my repo and working with the directories there so I changed that up from the original

**[0:04:59]** repo and then I also have 10 steps here for instructions on how to set up everything that I've got going on here including the n8n and open web UI integration with the demo workflow that you'll have in your n8n instance automatically when you install it through my version right here and so

**[0:05:17]** these 10 steps is what I'm going to quickly go over right now so you could follow these in the REM if you want or you can follow along right here and I'll show you how everything works and make it really nice and clear for you now all right so getting this installed from

**[0:05:30]** scratch there's just a couple of steps that you need to do I'm going to go over these quite briefly because in the last video on this on my channel I went into it in a lot more detail but essentially all you have to do is follow the installation commands at the top of the

**[0:05:42]** REM right here so for example if you have an Nvidia GPU you'd run these commands for Mac You' run these ones for everyone else if you just want to run on the CPU you would run these commands and the only thing you have to do before this is you have to go to this env.

**[0:05:57]** example file and change up everything here here to your liking and then rename it Tov so this is going to define the settings for postgress like your username and password for the database as well as what the database name is and then for these encryption Keys you can

**[0:06:12]** just make this whatever you want just make it an alpha numeric string that's relatively long um but this is all running locally so it doesn't really matter too much what this actually is so after you have this renamed Tov then you'll follow these instructions here in the readme to do the docker compose

**[0:06:28]** command and so I'm going to pull up my terminal here so you can see what it looks like let me bring this on to this monitor here I just ran Docker compos d-profile GPU Dasia up and then this is about what your output is going to look like it's going to pull all the

**[0:06:42]** different containers and then you'll start seeing a bunch of logs from all the different Services here like postgress open web UI quadrant olama and your terminal is going to hang because it's going to sit there and just constantly wait for log output from all the different services that you have

**[0:06:58]** running within this Docker compos file now to actually get Docker I would recommend getting Docker desktop that's my preferred platform I know a lot of people have different opinions on Docker desktop um versus just using Docker without it just do whatever works for you but I'll have a link in the

**[0:07:14]** description for Docker desktop if you want to install it and run this the same way that I am so once you have this up and running like this and you're getting all of this output it'll take a little bit to pull the models that you want to run from AMA so I'm going to go back to

**[0:07:29]** my my browser here and show you in the docker compost file right here if you want to change which olama models are pulled when you run the docker compost command you just want to edit this line right here so you can see right here that I'm currently pulling llama 3.1 for

**[0:07:45]** my LM and then nomic embed text for my embedding model that we also will be using in the NN workflow so you can just kind of copy this section right here and duplicate it or just change the model whatever you want to do to change which models are going to be available to you

**[0:08:00]** and then you can also go into the AMA container while it is running and pull more models that way as well and I show how to do that in the other video on my channel for this so at this point you have everything up and running and so

**[0:08:13]** what you can do now to go to n8n is you just go to Local Host Port 5678 as long as you didn't change any of the ports in the docker compost file this is the URL to get yourself into n8n it's going to have you create an account at first but

**[0:08:29]** this is just a local account you are not actually signing up for n8n so everything is local I promise you like you could literally use your social security number for the username and it' be totally fine because it's all just setting up the account for your local NN

**[0:08:44]** instance and so once you're in it if you spun up this whole thing using my setup you're going to have this local rag AI agent automatically in your n instance already because I have that packaged in this whole thing here and so clicking into it this is what we've got here as a

**[0:09:01]** nice little demonstration where I combine all of the different Services together like quadrant postgress n8n and olama and this workflow is very similar to the one I have in my first video on this local AI certic kit but I made a couple of changes especially to make it

**[0:09:17]** a web hook which is how we're going to integrate it with open web UI so I'm going to cover this workflow very briefly here but because the focus of this video in particular is on the open web UI integration I'm going to skim over this and then move over to open web

**[0:09:31]** UI and show you how to actually integrate it with this workflow so let's go ahead and dive right into this workflow including how to set up all the credentials for n8n to connect to the different services like quadrant and olama again this is just a demonstration workflow I had to build something so

**[0:09:48]** that we can have some substance to test out with the open web UI integration but really just using the web hooks here that I'll show in a little bit you can set up any n8n workflow to work with open web and we'll dive into that in a little bit and I'll show you how you can

**[0:10:02]** really make it fit to your needs so first of all the way that this workflow works is we start with a web hook and So within this web hook right here it's just a post and then we give a path like I just wrote invoke n8n agent so this is

**[0:10:16]** going to give us a URL and this is one of the things that we're going to feed into AMA so it knows the endpoint to hit to talk to our n8n agent and then for authentication I actually set up the function in open webui to work with a

**[0:10:31]** header off if you want to use a bearer token um but also because this is running locally you don't necessarily need that authentication so I'm just leaving that as none right now and then be sure to change the respond from immediately to using respond to web hook node that is really important otherwise

**[0:10:48]** it will respond immediately to the open AI request without actually going to the agent and getting the output so super super important there and then what we do is we go into our AI agent and this is where we generate the response based on the prompt that is fed in from the

**[0:11:04]** web hook so if I go to my executions here like this one right here and I go into the web hook the body of the request has a session ID that's how we have a unique identifier for the chat history and then also chat input chat input is the field that has the prompt

**[0:11:22]** for our llm and so that is what we feed into our tool agent right here so it takes the previous node chat input value as the prompt and then we use olama for our chat model and to set up your credentials for olama all you have to do

**[0:11:37]** is click on create new credentials and if I go into the one that I currently have the base URL is just going to be HTTP colon backb Slama colon and then the default port for olama which is 11434 so this is all you need to do and then you can click on

**[0:11:55]** Save and it'll test the connection and then you are connected to olama and then it'll automatically use use that for all the other nodes that we have here for AMA uh like our embedding model that we use both here and here for example and then for postgress it's a little bit

**[0:12:09]** more um but it's not too tricky overall all you have to do again click on create credentials and then for your host it's just going to be postgress because that is the name of the postgress container so that's how the containers communicate to each other and then the database user

**[0:12:23]** and password are all based on the values that you set in the EnV file that I covered earlier and then the other settings can remain the same and then you click on Save and it'll test out this connection as well just like it did with AMA and then when we get the

**[0:12:37]** response from the agent we're going to respond to the web hook with the first incoming item so this is going to take the output attribute from the llm and then return that to open web UI when it made that web hook request and so that is it that's everything we have for this

**[0:12:53]** workflow uh as far as the actual flow and then I can also cover the tools here because we have the vector store tool that is hooked into our agent for Rag and so for this we're using the quadrant Vector store we're just retrieving documents based on the query and then

**[0:13:09]** for the credentials here again you just click on create new credentials for this the API key doesn't actually matter this is a big confusion in my last video where people are like oh is this actually local why do I need an API key this is just there if you want to use

**[0:13:24]** the hosted version of quadrant but because we are running everything locally including quadrant this can be whatever you want and then for the URL it's just HTTP col backb quadrant colon and then the port which is 6333 so again quadrant is the name of our quadrant container in the docker compost file and

**[0:13:44]** that's why we specified that right here so that is everything for our tool and then for our knowledge base we are using Google drive to ingest our documents now you could use a local file trigger you could use anything for rag here I'm just using using Google drive as an example

**[0:14:01]** where I'm ingesting these documents I'm deleting the old vectors when I want to update a document then I'm downloading it extracting the text and then putting it into the quadrant Vector store so a super simple flow I went into a lot more detail on this in my other video just

**[0:14:16]** know that for the Google Drive credentials this is another thing that I want to clarify here it says that your ooth redirect URL needs to be Local Host but that won't actually work you can't use Local Host to set up credentials in the Google app admin console so you just

**[0:14:30]** have to use a different domain like an actual domain not Local Host and then it'll work here so don't worry about that it's not a big deal that it tells you to use Local Host you don't actually have to um but also you could just use a local file trigger because I know a lot

**[0:14:44]** of people wanted to use local files to make it entirely local and you can do that as well and then once you insert into the quadrant Vector store I've done this workflow once through for a single file you can actually go to this URL Right Here Local Host um port

**[0:15:00]** 6333 dashboard and you'll see your collection here for your documents and it'll show you the vectors and everything that you have in here and so there's a whole quadrant dashboard as well with this whole setup which is really cool to interact with your vector database outside of n as well if you

**[0:15:15]** just want to poke around with things so that's definitely worth calling out as well so that is everything that we have for this workflow and now we can dive into the open web UI integration all right we have gotten to the best part because we are now actually in open web

**[0:15:31]** UI and all you have to do to access your open webui instance is go to Local Host Port 3000 it'll have you create an account but just like with n8n you're not actually creating an account with open web UI it is just for your local instance so don't worry you're not

**[0:15:47]** actually you don't even have to be on the internet to do that it's just completely local for your open webui instance now one thing I want to say before I dive into the n8n integration is if you want to play with your old Lama models here in open webui you might

**[0:16:02]** notice when you click on this drop down to select a model that it's actually pulling the models from oama hosted on your computer not the olama that is running in the container with this local AI setup if that is happening to you and it actually did happen to me what you

**[0:16:16]** can do is click on your name in the bottom left go to the admin panel click on settings and then connections and there's going to be the place right here to change the url for your ol Lama API this might be set to local host or something like host. doer. internal you

**[0:16:32]** want to change that to olama click on Save in the bottom right and then reload your page and then when you click on select the model this dropdown should have the models that we pulled for olama in the container that we specified in the docker compost file so just something really important that

**[0:16:49]** I wanted to get out there for you because I ran into that myself now we can actually dive into the n8n integration and the way that we do this is with it a function in open web UI called functions so if I click on workspace in the top left here and then

**[0:17:05]** click on functions this is where we can specify any custom functionality that we want for open web UI to interact with our own agents and API endpoints including an n8n web hook so let me show you this really quick if I go to the functions page of the open web UI site

**[0:17:22]** you can see all these different really awesome functions that people have done for like a mixture of Agents pipe that's super cool or if you want to use Gemini models in open web UI or anthropic you can do all these and basically every single function is just a python script

**[0:17:38]** that is created in a way very specific to what open web UI needs for a new integration and so you have this pipe class here where you define all these valves which are essentially just values that you can pass into the pipe like your specific n8n web hook URL or your

**[0:17:54]** Bearer token all these things and then yeah I'm not going to get into like a lot of detail with how you have to set this up but it's very specific to open web UI these functions are specific to what they expect for these kind of Integrations and so I actually learned

**[0:18:10]** how to do this through copying other functions and learning from other functions on the open web UI site so I took one and kind of changed it to my needs and that's how I built what I'm just about to show you right here so let me click into this this is my n8n pipe

**[0:18:25]** and I've even published this to the open web UI site so right here you can see the Creator is coam that's me there's actually already 16 downloads even though I published this today which is super cool I haven't even released the video I'm recording it right now and

**[0:18:38]** people have already downloaded which is super super neat um so yeah what I will show you right here is just a brief overview of this pipe and then we will test it out so essentially we have these Valves and so we have like the n8n URL the bearer token the input field so this

**[0:18:53]** is basically what the user prompt is going to come in as to the web hook which is that chat input property that I showed earlier and then also we need to know with the Json response to the web hook what's the name of that property that actually contains the response from

**[0:19:11]** the llm and so these are both custom because you might have different attributes that you're inputting and outputting to your n8n workflows and so if I go into my function here go into the valves on the right hand side here these are all things that you can customize and so valves are essentially

**[0:19:29]** just parameters that you get to as the consumer of the function set for yourself without having to even go into the codes that's the convenience of it here so for my case what I did for my web hook you can see that it's invoke n8n agent going back to my pipeline here

**[0:19:47]** that matches exactly with what the path I have set here for the web hook in the workflow and one really important thing to keep in mind here is the way that the containers communicate with each other is based on the container name so you don't actually use Local Host for your

**[0:20:02]** n8n web hook URL in open web UI you use n8n so replace Local Host with n8n and then everything else matches exactly with what you see here within your n8n UI and then going back to the function here I have a function that emits certain status messages to the open web

**[0:20:21]** UI output so you can see little updates as it's generating the response and then I have this pipe function this is the primary function that's the entry point to my customization and it also includes the body this is the list of messages that is the conversation and that's what I

**[0:20:38]** add on to as well once I get the response from the llm so essentially what I do is I just extract the last question from the user and I make an HTTP request a post request to my n8n URL I pass in the bearer token which is optional and then my payload contains

**[0:20:54]** the session ID as well as whatever the user inputed for the their last message now for the session ID there's not actually a way to get the chat ID from open web ui's chat here so it's just a combination of the user ID and the first part of the first prompt so that's the

**[0:21:12]** only thing that's like a little bit Jank with this setup if you know something better please let me know and I'd love to update this but everything else is just like Crystal perfect here um and so yeah we get the response from the llm we extract the output from the llm based on

**[0:21:26]** that response field that we have as one of our valves and then we append that to the conversation and then return that after we do some error handling as well so that is everything for this pipe so you can take this code and you can put it into the function yourself like clicking

**[0:21:43]** into here making a new function or you can actually just click on get right here and bring it into your open web UI instance without even having to paste in the code or anything so it's really really convenient and so once you do that click on back and then make sure

**[0:21:57]** that you have it enabled and and then when I go back into a new chat and click on select model I'll have this n8n pipe along with all my other olama models and I can use it just like I would in ama model so I can say something like hello

**[0:22:12]** how are you all right this is going to go directly to my N8 and workflow for the agent to get a response all right doing well thank you for asking how can I assist you so I'll say sure uh what are the action items from the meeting there's just one meeting in the

**[0:22:26]** knowledge base right now for reg so I just want to retrieve retrieve that and give me the action items from what I have in quadrant so let's see what it gives me here there we go thank you for your patience I found this information about the action items and these four

**[0:22:39]** really silly things here as crazy as it looks this is the right answer because I just have something super silly that I put as a single document in my quadrant Vector store this is looking perfect and I can also go into the execution history for n8n and see that it is indeed using

**[0:22:54]** my n8n workflow for the AI agent so over in n8n now you can see that the lest execution the output was thank you for your patience here are the action items blah blah blah and this matches exactly with what we see right here in open web UI so it is indeed using the n8n

**[0:23:11]** workflow for the chat here even though it is just right next to all these old llama models it is something entirely custom and way different super super cool and then the last thing that I want to cover here if I go back to the function here I just want to say that if

**[0:23:24]** I scroll the bottom you should be able to see how easy it is to customize this for whatever kind of agent you are running because you can make a post request to an API endpoint that is hosting something with Lang serve or maybe you have a swarm agents or using

**[0:23:38]** llama index whatever it is you can do that here so you can interact with really any agent you could want with open web UI which is so cool and also using the pipelines feature in open web UI it's similar to functions but you can install more external dependencies so

**[0:23:53]** you can literally set up like laying chain or llama index or whatever within the code right here that's running in open web we Y which is just so so awesome you can just do anything you could dream of here for your local AI setup so last thing as promised you can

**[0:24:07]** use voice to chat with your NN AI agents it is just an incredible feature of open web UI and one of the reasons it was so worth it to bring it into this local AI starter kit here so all you have to do is click on the call button on the right

**[0:24:19]** hand side enable your microphone in the browser and just get chatting I have to be silent here except for when I'm actually talking to the model otherwise I'll confuse it but just listen here is really really cool hey man how's it going hello it's nice to meet you I'm

**[0:24:40]** doing well thank you for asking how are you doing today is there anything I can help you with or any questions you'd like to ask what are the action items from my meeting disc just the latest and greatest headphones all right I'm going to stop it there so you can see that

**[0:25:03]** works really really well the only thing that's kind of awkward is I was playing the audio right out of my speaker so it actually picked it up and thought I was talking when it was telling me what it said um but if you have headphones on whatever you won't run into that issue

**[0:25:16]** um but yeah like it it was worked really really well it'd be cool if they had more like custom voices and stuff it wasn't super robotic I know that the open webui team is working on that though and so like this whole thing is like pretty new and it's getting more

**[0:25:28]** and more robust like every week so really really neat I hope that you found this really cool just like I did so there you have it we have successfully extended the local AI starter kit to include open web UI and integrate it with NN so we can chat with our workflow

**[0:25:43]** agents just like we would any olama model and I am definitely going to keep extending this local AI stack in the future so let me know in the comments how else you'd like me to extend it what you would want me to add in I'm really curious to hear your thoughts if you

**[0:25:57]** appreciated this content and you're looking forward to more things local AI I would really appreciate a like and a subscribe and with that I will see you in the next video
