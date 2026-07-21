---
type: raw-transcript
title: "We're Taking this AI Coding Assistant to the MOON [Plus Installation Instructions!]"
youtube_id: 31ivQdydmGg
url: https://www.youtube.com/watch?v=31ivQdydmGg
slug: were-taking-this-ai-coding-assistant-to-the-moon-plus-installation-instructions
published: 2024-11-03
duration: "0:13:10"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** it has only been 3 weeks since I started a fork of bolt. new and this project which I have been calling bolt. new any llm has grown so insanely fast that I am having a hard time keeping up with it I initially started this Fork just as a

**[0:00:15]** way to help you all use a bunch of different llms including local ones with AMA within bolt. new but in the last couple of weeks a massive Community has formed around this project and we have started to do a lot of really incredible things together so today I am continuing

**[0:00:30]** the trend of giving a bunch of updates and announcements on the project like I've done the past couple of weeks there are so many exciting things going on and you have no idea how stoked I am to continue growing this project with you and trust me there are only going to be

**[0:00:45]** more and more ways for you to get engaged first announcement there are huge things happening this Sunday November 10th so I'm actually going to be doing a live stream this Sunday at 700 p.m. central Time in place of my usual Sunday video I haven't done a live stream in months so I am so pped for

**[0:01:02]** this and I'm just going to be chatting with all of you and talking about all of the big updates and announcements that I'm going to cover right now all right so last week I open up applications to become a core contributor to bolt. new any llm and we are already at 36

**[0:01:16]** applications I love it and I seriously appreciate each and every one of you and I definitely going to make sure I find a way to get all of you involved heavily having individuals like you help me is what keeps this project growing because it is definit defitely already gotten to

**[0:01:31]** the point where it is way bigger than me next up I'm actually planning on renaming bolt. new any llm to autod Dev why well I am definitely down to merge this project into the main bolt. new repo at some point but for now it's really important that we keep this

**[0:01:47]** project distinct because we are doing a lot of really cool things with it plus autod Dev is just a really sweet name and it plays well into another thing that I'm building behind the scenes for us so another little teaser for you on that also huge news here last week I

**[0:02:04]** mentioned that I'm opening up a discourse Community for autod Dev and I have a date for that now it is this Sunday that we are releasing the discourse community and that's going to be one of the big things that I Showcase in the live stream next Sunday so I'm

**[0:02:17]** really excited for that and as you can see here we are almost done getting it set up and it is shaping up to be a really awesome platform for us to collaborate together I sincerely wish that I could have launched this sooner for all of us but I really really wanted

**[0:02:30]** to make sure that everything is ready for us and that we have core contributors engaged there so we can really hit the ground running when we launch we are on a mission to create the best open- source AI coding assistant out there and so far together we have

**[0:02:44]** been absolutely crushing it it is definitely far from perfect at this point but especially once we get the discourse Community launched core contributors helping me with the huge demand and more and more of you engaged this project is going to continue to truly develop a life of its own and help

**[0:03:00]** help us all code better and faster right now in this video I'm also going to cover how to run autod Dev yourself really easily with Docker it's going to be a full step-by-step guide that'll be really easy for you to follow even if you're a non- technical person so many

**[0:03:14]** of you have asked for this so I wanted to include it along with all the updates that I just shared it's also really really important that I make it as easy as possible for everybody to get up and running with autod Dev so you can have the most people engaged and contributing

**[0:03:28]** so let's go ahead and dive right into that so all the instructions that I'm about to go over right now to get autod Dev uper running yourself I will have in the description of this video and you can also find them in the read me here at the root of the GitHub repository for

**[0:03:42]** autod Dev so if you scroll down once you go to the repo you'll see the initial setup instructions to get all the prerequisites downloaded get the repo pulled and then there's instructions both to get everything up and running with Docker as well as instructions to run without Docker so I'm going to focus

**[0:03:58]** on running with Docker because it's my preferred method it's easier and what I would recommend but there's instructions for both if you don't want to use Docker for whatever reason but right here in this video I will focus on running with Docker and there's just a couple of

**[0:04:11]** commands that you need for that so let's go ahead and get started with the initial setup so there's a couple of prerequisites that we need the first one obviously being Git You need to be able to pull this GitHub repository so you have to install git on your machine for

**[0:04:26]** that you can just go to g- sc.com there's 's a link to this both in the readme and in the description of this video and then you can download for your operating system like right here it recognizes that I'm on windows so it says download get for Windows and then

**[0:04:41]** the other prerequisite that we need is node.js and so you can just go to nodejs.org and then download uh just from their homepage right here really really easy to get this set up um there's instructions here on how to verify that you actually have node in your system path so you can use the node

**[0:04:59]** commands um typically this is going to be installed by default working perfectly right out the box for node and so this is just here if you encounter any issues with um actually running the node commands once you have node.js installed it's a really really simple process and then you can go on to the

**[0:05:15]** next step here where you can copy this Command right here to clone this GitHub repository so you have the autod dev code on your machine and so you just open up a new terminal and um right here I'll just paste in the command to clone this repository and I already have it

**[0:05:31]** obviously which is why I get this error message right here but if you don't then it'll pull everything take a little bit and then you'll have all the code on your machine so that is all it takes to get this repository cloned and get all the prerequisites set up the next thing

**[0:05:44]** that you have to do is set up your API keys if you're going to use any large language model that requires that so if you want to use GPT for example or if you want to use open router to use some of those open source lmms hosted there

**[0:05:57]** you have to set up all those API keys and so the way that you do that is there is a file that you need to edit and then rename in the repository so let me go ahead and open that right now and show you so right here at the root of the

**[0:06:10]** repo uh we have this file called env. example you're going to want to fill all the API keys for the providers that you want to use and then rename this file Tov so for example if you want to use autod Dev just to work with GPT models and open router models you would follow

**[0:06:31]** the instructions right here to get the API key for open Ai and then slap it right here and then for open router you get your open your API key right here and then slap it in right here that's it you don't have to set the keys for the

**[0:06:44]** providers you don't want to use like if you're not planning on using Gemini you don't have to set the Google generative AI API key so set the ones you want and then rename this file Tov like I have right here I'm not going to show this file because I have all my API keys in

**[0:06:59]** there but once you said it you would have a EnV as well when you rename this file so that is everything for getting the API key setup now we get to The Specific Instructions for running with Docker so everything we've done up till this point is the necessary setup no

**[0:07:15]** matter how you want to run autod Dev and it's very similar for the official bolt. new as well now we get into some custom stuff that the community has developed along with me so you can run this all with Docker very very easily so the prerequisites for this are obviously get

**[0:07:32]** and no. JS as mentioned above because you have to do that initial setup and then also Docker so you just have to go to doer. very nice and simple URL there and it'll typically recommend that you install Docker desktop I like using Docker desktop I've had a good

**[0:07:47]** experience with it there are others who have not necessarily so you don't have to have Docker through Docker desktop uh there's a lot of opinions on that but typically I'd recommend just getting Docker desktop it's a very nice user interface and then you have all the typical Docker commands and it also

**[0:08:02]** installs Docker compose for you which is the tool that we'll be using in a little bit here to run different containers together and have some more configuration for Docker so get Docker installed and then we can run a couple of npm commands that we have set up in

**[0:08:18]** this project to build our container now the beauty of Docker is it is an isolated environment and so everything that is necessary to run autod Dev is going to be installed in this contain container that is created for you to run the application so if you are trying to

**[0:08:33]** run without Docker and you experience any issues at all like with the access violation I've seen a lot of people run into that or like a module is missing uh or you just get weird errors where it's like oh your API key header is needed I've seen a lot of random errors when

**[0:08:48]** people try to run it without Docker and that's all because everyone's system is a little bit different so when you run the container you're guaranteed to have the exact same setup as someone like me who hasn't work working perfectly fine so that is one of the big reasons that I

**[0:09:02]** would recommend running with Docker and why I'm covering that right now and so for the development environment which you'll typically want to start with you will run the npm Run Docker build command and so I'm going to open that my terminal up quickly and just show that what that looks like here paste this in

**[0:09:18]** and it's going to take a little bit for you if you're building the container for the first time I've already built it so it's using a lot of cache stuff here which is why it ran really really fast but you'll get a lot of blue output that looks like this and then some warnings

**[0:09:29]** that we might fix later but you can typically ignore those um so that is how you build the container so at this point you have this ready to execute but it's not running yet and then if you want to build for production there's a separate command for that U there's just a little

**[0:09:45]** bit of difference between like a development environment and a production environment for this that I'm not going to get into right now but as you're doing development to contribute to autod Dev you will use the development environment these npm scripts are just kind of also a wrapper around Docker

**[0:09:58]** command so you can use these Docker commands directly to build the container if you want 1B right here this step right using these commands is an alternative to using the helper scripts so actually if you don't even want to install node on your machine at all you can just run these commands directly

**[0:10:16]** because then you don't need npm commands so that's just a little aside I would recommend just installing node and running the this npm Command right here and then you can move on directly to step number two and this is using Docker compos with profiles to actually run the

**[0:10:30]** container so you have this image built ready to execute now you want to spin it up and start autod Dev on your machine and so for the development environment we'll run this Command right here so I'm going to go ahead and copy this open up my terminal again and clear it and then

**[0:10:45]** paste in this new command and so again it's going to be pretty fast for me because I've already ran this and started it before but it's going to give you a warning for each of the API keys that you haven't set in your EnV file in my case there's just one that I haven't

**[0:10:59]** set here um but all the other ones are good to go and then you'll get the output u in your terminal just like you would if you were running outside of Docker so your terminal is going to hang right here and just wait for more output from the back end of autod Dev just like

**[0:11:14]** if you ran in a terminal just with pnpm and so now you can visit local hostport 5173 and you could start playing around with autod Dev and so the one thing I will say is if you're using Google Chrome you'll have to install Google Chrome canary you can just Google it

**[0:11:31]** super easy to install it it's a great web development browser and for some reason Google Chrome doesn't work with bolt. new it's not even an autod Dev specific thing so just something to keep in mind there but if you're using Firefox um especially if you're on Linux you can't even have Chrome then you're

**[0:11:45]** totally good using Firefox there's not like a web development version of that browser like there is with chrome so yeah that is pretty much everything um and then as far as to next steps when it comes to um really playing around with this maybe even making changes in

**[0:12:01]** contributing to the repo I'll make another video in the future on what it looks like to make changes to this attach a debugger to help you with debugging as you're adding more features I'm going to go in depth on those things what it looks like to create pull

**[0:12:14]** requests and stuff as well in another video but I want to keep this simple right now just helping you get started with autod Dev because like I said earlier on in this video I just want to make it so easy for everybody to get up and running with autod Deb so we have

**[0:12:26]** the most people engaged in contributing to have the highest chance of massive success with this project so that's everything that I've got for running autod Dev let me know in the comments if you have any questions on any of this at all I would highly encourage you to get

**[0:12:39]** involved in autod Dev because together we are building a truly powerful AI coding assistant that is accessible to everyone it's definitely not perfect yet but it is getting better each and every week and if you have any questions or concerns about the project at all please comment below because I'd love to chat

**[0:12:56]** with you about this project as we grow it together if you appreciated this content and you're looking forward to trying out or getting involved with autod Dev I would really appreciate a like and a subscribe and with that I will see you in the next video
