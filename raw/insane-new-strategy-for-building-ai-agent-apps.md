---
type: raw-transcript
title: "INSANE New Strategy for Building AI Agent Apps"
youtube_id: yRIEpNlacd0
url: https://www.youtube.com/watch?v=yRIEpNlacd0
slug: insane-new-strategy-for-building-ai-agent-apps
published: 2025-01-19
duration: "0:27:02"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I get asked a lot How I build my fullscale AI agents so I recently kicked off this miniseries showing you my entire process in this series we are building a GitHub agent that can consume entire repositories for code Q&A and in the last video we integrated our agent

**[0:00:17]** with the live agent Studio Agent Zero platform to quickly give our agent a polished front end and we said goodbye to the ugly terminal now in this video we are taking that and bringing it up a notch by Rolling our own fully C custom front end with the help of a couple AI

**[0:00:33]** coding assistants including our very own bolt. DIY which we as a community are building to be the best open- source AI coding assistant I love using AI coding assistants to help me with any app that I create but they all have their pros and cons bolt. DIY is open source and

**[0:00:51]** you can use any large language model many of which are completely free to use but since we're so focused on working with many different llms we don't have the opportunity to optimize for just one like lovable or bolt. new so often times these platforms will actually give you

**[0:01:08]** better performance when you're starting an app from scratch and then we have our AI idees like wind surf or cursor the ones that run on your computer instead of in the browser and they are phenomenal for making more directed changes with your applications but the in browser editors like bolt are still

**[0:01:25]** much faster at getting you started with your project if only there was a way to combine all of of these tools together to get the best of all three worlds we want something that is powerful free to use and easy to work with throughout the entire process of creating our app well

**[0:01:41]** in this video I'm going to show you exactly how to do that we're going to combine these tools together we'll use lovable bolt. DIY and an AI IDE like wind surf recursor to create a front end for our GitHub agent complete with conversation and chat history sound like

**[0:01:58]** a lot well it's actually super simple to use all these platforms together and I'll show you exactly how to do that and explain my reasoning behind using these different tools throughout the video super exciting stuff so let's dive right into it now this is the live agent Studio the platform that I've been

**[0:02:13]** pouring my heart and soul into over the past few months to build up this place for us to collaborate on open- Source AI agents together you can build your agents with any platform like with python or n8n or voice flow publish it here for the world to try out so we can

**[0:02:29]** just work on pushing the industry forward together building incredible AI agents and obviously to build an agent for this platform you have to follow some specific guidelines so that it is compatible and that's what we went over in the last video we followed this guide that I have here on the live agent

**[0:02:46]** Studio that walked us through the exact process of building an agent for the studio and it's not like I'm just showing you how to build an agent only so it can go on this platform this really teaches us best practices about turning our agent into into an API

**[0:03:01]** endpoint so that we can hook it into any front end and so that's what we're going to do in this video is take the exact same code I'll even show that quick this is what we worked on in the last video we turned our pantic AI agent into an

**[0:03:13]** API endpoint and without even having to change this at all we're going to use AI coding assistance to build a front end that can hook into this API just like we did with agent Z so this is Agent Zero the platform that we hooked our agent into last time now we're going to use

**[0:03:28]** all of these AI ID to build our own front end and of course we could just leave our agent here on the studio and build it for the studio I mean that's what I built this platform for after all is to be an open-source repository of AI agents but we really do

**[0:03:44]** want to go and build our own front end now so that is what we're going to do with the exact same code that we worked with for our agent in the last video now what does our process actually look like for using all these different AI coding assistants to build a front end for our

**[0:03:58]** GitHub agent well we're actually going to start with lovable which I have never covered on my channel before even though it is a fantastic platform I've been so focused on bolt with bolt. DIY and really you could use either bolt. new or lovable here to get started CU these

**[0:04:15]** platforms are both optimizing for a single llm you generally get the best results starting your project and getting a solid foundation so honestly lovable and bolt. new are pretty comparable they do better at certain things though and I actually find that for that style applications like what we're going to build right here lovable

**[0:04:33]** does a bit better and then bolt. new does better other things like building landing pages for example so that's why I'm using lovable and it has free credits to get started which is why I can say it's free when we start with a solution like lovable and so we're going

**[0:04:46]** to lay the strong foundation with a single prompt that I'll show in a little bit get our project started which you could do with bolt. new as well if you wanted so that still is an option and then we're going to take that project that we build for free with the free

**[0:05:01]** credits that we initially get with lovable or bolt. new and then we're going to move over to bolt. DIY and the reason we want to do this is because bolt. DIY you can run yourself and use completely free models and so we can take our initial project from lovable or

**[0:05:18]** bolt. new and then tweak it to our hearts content completely for free one problem that people run into a lot using a solution like lovable is their initial project turns out great they just a few credits but then they want to tweak something they want to add a light theme

**[0:05:34]** there's a little button that's not working or they want to change the UI and they they slowly use more and more credits as they're making these changes and then they hit their limit and they can't continue that is the problem that bolt. DIY solves even though it might

**[0:05:47]** not give as good of a performance creating that initial Foundation you can use it for free to continue making more and more and more changes and never run out of usage that is the beauty and so essentially we're going to build in lovable publish to get pull into bolt.

**[0:06:02]** DIY from GitHub make our changes there and then we will download the project and we can bring it into an AI IDE like wind surf for example this is what I'm going to be using you could use cursor as well there's free credits that you get for wind surf too and so by the time

**[0:06:16]** we bring in this project into wind surf it'll be pretty much finished and we can just use an AI IDE to make some of those last touches and we run it running on our computer anyway because that's how we're going to deploy it within the rest of this AI agent Series so that's

**[0:06:31]** everything that we've got now let's dive into the prompt to get started with this app using lovable all right here is the prompt that we're going to be feeding into lovable to create the foundation of our front end for our GitHub agent and I'm going to cover all of this right

**[0:06:45]** here now a lot of this is going to make more sense if you saw the last video where I created the API endpoint around the agent because we need to be very clear with our agent here how you actually communicate with it lovable needs to know the inputs the outputs and

**[0:07:00]** how we handle the messages because it has to read all this in the front end to display the conversations and the chat messages and so starting off I'm actually quite General with the UI itself I just tell it to make a beautiful dark theme using some of these

**[0:07:15]** colors you you could specify specific hex codes if you wanted to as well and then I give a URL for the agent this is going to dictate the entire flow of the application obviously making sure that it's connected to the right API endpoint so this is what I had set up in the last

**[0:07:31]** video I literally have my terminal running this agent right here so once this is built and lovable we're actually going to be able to start talking to it immediately and then I specify the input schema so this is the payload that has to be sent into the agent through this

**[0:07:45]** API endpoint and then I also clarify what all of these parameters are so most of this prompt is really just telling it how to work with the API I don't even specify much with the front end because that is where I really need to get specific these tools like lovable they do a

**[0:08:02]** fantastic job making user interfaces even without much Direction it's more the specifics the functionality that you really have to get specific with and so things like the output schema as well being specific with that and then also lovable does have a direct superbase integration but I find it even more

**[0:08:20]** simple for what I'm building here to just have it bake the superbase URL in public key right in the code instead of creating that v.v file that it likes to do when you set up superbase integration so I just tell it right here and you can paste these things in because they're

**[0:08:34]** not private you're not putting your superbase secret key here you're just putting your URL and your public key and then also specifying here the schema for the messages table in super base because it's going to have to know what it pulls from in the table to display the

**[0:08:51]** conversations and the chat messages and so actually even before I go through the rest of this prompt let me go over to superbase and show you these things really quick so here we are in super base I just want to really quickly show you how to get that project URL and

**[0:09:03]** Anonymous key and then also that messages table and talk about that just a little bit here to give you some extra context which is going to be very important for lovable we include that in the prompt as well so first of all to get your project URL and public key go

**[0:09:18]** down to the project settings in the dashboard for super base and then go to the API section in configuration so you can just copy your url right here as well as your public key and again both of these things you can paste right into the prompt to the llm even if it is not

**[0:09:35]** a local llm the service roll key this is the only thing that you would really want to keep secret and probably never given to a prompt for an llm but these two things are okay and you can even have these published in a GitHub repo they are public information and then the

**[0:09:50]** other thing if I go to the SQL editor in the last video in the series we ran this SQL right here to create the messages table that our AI agent is using to store all of the messages in the conversation and so obviously we need to interact with this correctly within the

**[0:10:05]** front end as well so everything that I ran right here which created this messages table that is what I'm pasting in as the schema for The Lovable prompt as well back over to the prompt let's finish this off really quick here so yeah we specify the schema for the table

**[0:10:19]** that I just covered and we also specify here that we have real time enabled for this table because we're actually going to subscribe to changes to the messages table able to immediately pull new messages that are coming in from our agent and in the developer guide that I

**[0:10:35]** have on the automator live agent Studio I have instructions on how to set up everything so you can literally just copy all of the SQL that I just showed running in superbase to set up your messages table here and then also we have this line right here to enable

**[0:10:49]** realtime communication for the table that means that our front end can watch for changes to the table as in new messages that come in and so that's very important to specify for our prompt right here because we need lovable to know to set all of that subscription stuff up to watch for changes to this

**[0:11:07]** table and then I also specify for the messages here the content and the type so it needs to extract this information to display things about the messages correctly and then finally I just have a random list of requirements here that I have for my application and this is

**[0:11:21]** usually what I'll do for all of my prompts to AI coding assistance like this when I'm starting a new project is I'll just kind of have the end be a dedicated section to dump a bunch of random requirements that didn't quite fit into anything else above things like

**[0:11:35]** making sure it can handle markdown I want there to be a loading indicator when we're getting the response from the AI agent a lot of the ux stuff specifically that I focus on right here and then also I want to have superbase authentication enabled with email and password and when you have your

**[0:11:51]** superbase project set up there's nothing more that you actually have to set up for this to be possible which is super neat so it's just this single line right here that I add to the bottom of the prompt and we'll have authentication with super base fully set up in our

**[0:12:03]** lovable app after we run this prompt So speaking of that let's go over to lovable and run this now this is the fun part I copy The Prompt go over to lovable just paste it in and let it rip just make sure that you give your superbase project URL and public key in

**[0:12:20]** place of those placeholders that I had and that's it so I can just go ahead and hit enter and then boom it's going to immediately start creating my app for me so so neat and this is the kind of thing that would take days and days to work on

**[0:12:31]** and tweak like what we're going to do with bolt. DIY in a little bit here but it's just so fast with these AI ID e now and so yeah amazing I'm just going to let it go and pause and come back once lovable is done creating my app all

**[0:12:44]** right look at this we have a full front end built already with lovable now there's one little tweak that I had to do right here just a few suggestions that I gave as kind of a second shot prompt here just to make it more presentable to show you what level can

**[0:12:58]** really do but for for the most part it was just a single shot prompt and it built this full front end we got super base authentication I have a test account that I already have created here in my super base account so I'll just log in with that really quick here and

**[0:13:11]** then boom look at this we already have the conversation history pulled I can view all my old messages that I have in the messages table start a new conversation I can collapse this and I can log out I mean things don't look perfect here so we are going to do some

**[0:13:24]** more tweaking we'll do that with bolt. DIY but this is already looking phenomenal and so yeah I've got my agent running locally right here nothing's happening in the terminal yet but I'll show you that when I actually talk to it here it's going to work so I'll say Hi how

**[0:13:38]** are you and uh looks like it can't I can't hit enter to send the message so I might want to fix that as well so I'll just click Send and there we go boom we got the message on the front end it's talking to our agent we can see the

**[0:13:50]** prompt coming through right here we got a response in real time look at that this is beautiful and I can even continue the conversation here um just I mean r Rand question but yeah look at that this is super neat just basically one prompt to lovable and now we want to

**[0:14:07]** take the UI and ux and make it a little bit better so we're going to push it to GitHub and then pull it from GitHub in bolt. DIY so let's do that now and really start to refine our app that we've been building for free so far all

**[0:14:20]** right let's get this published to GitHub so I'm going to click on edit code in the top right click on transfer repository and then I'm already signed in but it's going to have you go through an authorization flow very quickly if you haven't already but I'll just go

**[0:14:33]** ahead and click on my account and then boom it is immediately going to create a GitHub repository that has all of the code that we just created within lovable so I'm going to click on this link and here we go we got our our repository it is private by default which you can

**[0:14:48]** bring it into bolt. DIY as a private repo if you sign in the other option is you can just make it public so you don't even have to sign into GitHub in bolt. DIY and since I want to share this with you anyway I'm actually going to go

**[0:15:01]** ahead and make it public right now so just go to settings and then scroll down and change visibility change to public I want to make this public I understand all the effects boom there we go and then I have to authorize let me do that and I'll come back once I have this as a

**[0:15:17]** public repo repo is published now we can go ahead and install bolt. DIY and bring in this project in just seconds so there are a lot of resources on our automator Think Tank on YouTube for how to install bolt. DIY because you're actually going to run this on your computer unlike

**[0:15:36]** lovable or bolt. new so it runs in the browser but you run it on your computer and then you just visit your Local Host URL to access it like we're seeing right here so if you go to the main bolt. DIY homepage of the repo here which I'll

**[0:15:49]** have Linked In the description you'll see a ton of really helpful instructions to install it you can install with node.js with Docker there's even a button just to download the zip for all the source code right here I'm just going to show you the easiest way that I

**[0:16:02]** found to install it with node.js and so the requirements here is that you have node.js you just go to nodejs.org download and install super quick and then you also want get so that you can clone the repository bring all the code for bolt. DIY onto your machine so you

**[0:16:18]** just go to get- sc.com and there'll be a button here automatically to install it for your operating system Windows Mac or Linux so that's how you install install all the dependencies here so now we just want to clone the repository I'm actually going to do this from scratch

**[0:16:35]** right now in just like a minute to show you how easy it is to get up and running with bolt. DIY even though you do have to run it on your own computer so go to the repo click on the code drop down right here copy the URL to a clipboard

**[0:16:47]** and then I'm going to another terminal here on my screen so let me bring that over to this Monitor and I'm going to do get clone and then the repo link that I just copied so it's going to bring this all in super fast it's a pretty lightweight app overall so I clone the

**[0:17:03]** repository from scratch and now I'm going to change my directory into it and now all I have to do to install all the dependencies for bolt. DIY is run the command pnpm install so this is going to take a little bit to install all the packages so let me pause and come back

**[0:17:19]** once that is done all right took like 3 seconds honestly I paused and came back in like 3 seconds and now we got everything installed so now we can run the command pnpm run Dev and again all these instructions are in the readme here in the repo so I'll run this and it

**[0:17:34]** will just after a couple of seconds here start bolt. DIY on Local Host Port 5173 by default so you can copy this URL and go into bolt right here so it's going to refresh I'll give it a little bit of time here and you can go to over the

**[0:17:49]** terminal and see things that are happening like right here is registering all the providers that we have for bolt. DIY you can use basically any large language model that you could dream of again many of them are free I'm going to refresh here to get rid of this white

**[0:18:02]** screen many of them are free which is the beauty of using bolt. DIY to iterate on this project that otherwise you would have had pay a lot of credits for to continuously iterate on within lovable here and so then to set your API key there's instructions no matter the

**[0:18:20]** provider that you select like if I select ol and I want to use well I guess is a bad example because you don't have to set an API key but if I'm using Google or if I'm using anthropic whatever you can click on this button and it'll show you how to get the API

**[0:18:32]** key so once you have your API key for Google I'm using Gemini 2.0 Flash in this case there's so many cool models you can use like deep seek through open router for example but I'm going to use Gemini 2.0 flash which is completely free I got my API key so I'll just click

**[0:18:48]** on the edit button right here paste it in Click check and then boom I got my API key set for Google and I am ready to go it is that easy you don't even have to set your API keys in the en file so I have to do nothing to mess with the

**[0:19:01]** actual code go into VSS code or anything like that and so now we can go ahead and import our git repo and start playing around with the project right here in bolt. DIY now to bring the GitHub repo into bolt. DIY just click on the clone a git repo button so you have to enter a

**[0:19:16]** URL here which I just copied the URL for what Lev will published for me and then if this is a private repo you will have to sign in otherwise since this is public it is instantly going to bring in everything for me here and even run the the commands to install all the

**[0:19:30]** dependencies and start the site up for me so in just a second once it's done here in the terminal installing all the dependencies and running it we're going to see the exact same app that we had in lovable because at this point we haven't changed anything so now that we have it

**[0:19:44]** running here in bolt. DIY now we can use Gemini 2.0 flash to tweak everything that we want that our heart could Desire with the UI and the ux to make this app perfect and we can do it completely for free so right now it's still loading things up right here so I'm giving it a

**[0:20:00]** little bit of time um there we go all right so now we have it up and running and we can even test this so I can say I can log in here just like I did with lovable sign in we can see that everything is exactly the same with this

**[0:20:14]** project right here now one thing I will say is that chatting with the agent will not work within bolt. new or bolt. DIY because the web container actually blocks requests to the Local Host agents here so lovable is a bit better in this way just because it doesn't block those

**[0:20:32]** requests so right here we're just going to be working with the UI and ux and then we'll download it bring it into an AI IDE like wind Surf and continue there and run it there so what I'm going to do right here I'm just going to do this off

**[0:20:45]** camera I'm going to do a bunch of little prompting here to tweak certain things it's not going to be super interesting for you so I'll pause make a ton of little changes to make this look nice just as a good example and then come back once that is done so here we are

**[0:20:58]** with a much better version of our front end using a bunch of tweaks with bolt. DIY and it's a little boring to just go through this with you which is why I did it off camera but yeah you can see the full chat here everything that I did

**[0:21:11]** with bolt. DIY that would have taken quite a few credits in something like lovable and the main thing that I want to give as a piece of advice here is just request it to add one thing at a time that makes it so much easier for the llm to just understand what you're

**[0:21:26]** doing and implement it correctly and Gemini supports images and soul does boat. DIYs so you can click on this button right here and literally drag what you want to take a screenshot of share your screen and it'll add it as an image here which is super neat because I

**[0:21:40]** can share context around what doesn't look good and actually have it reason about it visually which is so so cool so yeah we've got a header here the logo button looks better we've got our chat that we can now hit enter to send and if I click into an existing conversation it

**[0:21:56]** looks so much better and we even got this little togg here for our theme which it's not too much different so I might want to tweak that more later as well but yeah this is just so awesome and going back to lovable which again this was phenomenal for our starting

**[0:22:09]** point it's already much much better this is what we got with lovable that we built on top of with bolt. DIY like the logout button looks bad the messages look bad here we can't hit enter to send a message it's just amazing now so now going back over to bolt. DIY all we have

**[0:22:26]** to do to download it to then bring it onto our computer computer to take it Forward is just click on this button right here download code that is it it'll download a zip file that you can then unzip and then just run the same commands that it ran initially like the

**[0:22:39]** npm install and npm run Dev to install it and run it all on your computer so I'm going to go ahead and do that right now so I unzip the file that bolt. DIY downloaded and then put all the contents in this folder right here should look very similar this is exactly the file

**[0:22:54]** structure that we had in bolt. DIY and now I have a terminal that is open up to this folder right here and I can just run the same exact commands that the llm ran in bolt. DIY so first I start with mpm install this is going to install all

**[0:23:09]** of the packages the node.js packages for our front end and then after it does this you can see it created the node modules folder so we're installing all of our dependencies and then we can run it after with the npm Run command and that's it we will now have our website

**[0:23:23]** up ready for us to play around with just like we were doing in lovable and bolt. DIY so I'll do mpm runev start this up boom it is now hosted on Local Host port 8080 so I'll actually go back over to my browser here and open that up so Local

**[0:23:36]** Host port 8080 and boom there we go and now looks like it changed I didn't realize it changed the login here it's a little funny so I'd probably want to fix that that looks pretty bad um but yeah let me log in and actually get into the real

**[0:23:49]** thing um here so I'll sign in boom there we go so yeah that's something important to keep in mind is make sure that you're aware what the llm is changing I was already logged in the entire time it was editing so I didn't see that but it'd be

**[0:24:01]** easy to fix that anyway but yeah look at this this interface just looks so clean and obviously it's just the bare bones like this is very much a proof of concept but now you can take this so much further you could continue to tweak it in bolt. DIY or you could actually go

**[0:24:16]** into an AI IDE like wind surf or cursor and keep editing it from there because again I love using AI idees like wind Surf and cursor to make more directed changes so I use the in browser editors to get me started on the project and make those initial larger scale tweaks

**[0:24:33]** and then I take it into an ADI IDE so that's my general process I'm not going to show bringing it into windsurf recursor because I've already made a video on windsurf on my channel and I think it's pretty intuitive overall but yeah let's actually test out this agent

**[0:24:47]** now so I've got my terminal open here uh to my agent I'll start a new chat and I'll just say hello and we'll see if everything is working so we got the hello in the top right here I guess you can't see it cuz my screen is uh is um

**[0:25:00]** fully zoomed in here so yeah hello and then I get the response from the agent and if I open up my terminal boom there we go we got that new response just now I can say test and there we go we got our request all right it is working

**[0:25:13]** perfectly so next step would definitely be to bring it into something like wind surf to continue making changes and generally I love doing that because a lot of these in-browser editors kind of get stuck after a while when you're making tweaks and so yeah bringing it into an AI IDE to to make those more

**[0:25:29]** directed changes also this fully up toate UI I will push into GitHub as well so you can check it out if you want I'll also have the AI agent the GitHub agent Linked In the description of this video as well and if you're curious more how to use something like wind surf I'll

**[0:25:44]** have a video right here that you can check out lot of cool tips that I have there for how to use something like wind surf but again not going to cover it here because it's pretty intuitive overall and we already have something that will take us into the next step of

**[0:25:56]** continuing to improve and test our agent and then deploy it which is what we're going to do in the rest of this series and with that our AI agent now has a fully custom and Slick front end built with the help of a few AI coders and the

**[0:26:09]** open- source power of bolt. DIY I know that it seems like a lot of moving Parts with these different AI coding assistants but I hope that this video makes it very clear for you how you can use them together very easily and using them in tandem gives you the Perfect

**[0:26:23]** Blend of free flexible and fast really I use this process for building all of my front ends and in the next videos in this series we're going to be testing out our agent and refining it more with the help of this front end and then finally deploying our AI agent we are on

**[0:26:39]** the home stretch now for actually productionizing our AI agent and turning it into something that you can monetize if you build yourself so stay tuned for that I'm super excited for the rest of this series if you appreciated this content and you've learned a lot from building AI agents in this series

**[0:26:55]** already I would really appreciate a like and a subscribe and with that I will see see you in the next video
