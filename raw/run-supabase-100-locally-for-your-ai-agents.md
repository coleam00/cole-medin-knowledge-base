---
type: raw-transcript
title: "Run Supabase 100% LOCALLY for Your AI Agents"
youtube_id: pOsO40HSbOo
url: https://www.youtube.com/watch?v=pOsO40HSbOo
slug: run-supabase-100-locally-for-your-ai-agents
published: 2025-02-16
duration: "0:29:37"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** everyone loves supab base it is an incredible open-source platform that definitely seems to be the most popular database for AI agents right now it's postgress sequel under the hood so not only can you use it to manage the conversation history and state for your agents but you can also use the PG

**[0:00:17]** Vector extension to literally turn it into a vector database for rag so it's just the perfect platform for AI agents not to mention all the other awesome features as well like authentication and object storage that you get right out of the box and so to me it definitely seems

**[0:00:32]** like no matter what you are building with AI there is a place for super base because super base is so incredibly useful and Powerful it was no surprise to me that many of you asked me to include it in the local AI package that I've been working on and that I've been

**[0:00:47]** sharing some on my channel and luckily since superbase is entirely open source and they have instructions for self-hosting it with Docker it's actually pretty easy for us to bring it into the fold of our local AI services and that's exact actly what I'm going to show you how to do in this video now

**[0:01:03]** super base was a little bit trickier than the other platforms to get Incorporated but that's why I'm going to walk you through it step by step right now so you can get this revamped local AI package up and running super quickly and the best part is if you've used

**[0:01:16]** super base not locally before everything is going to look very familiar to you I'll even show you how to build a rag AI agent in NN that's running 100% local using our superbase instance plus we'll use a local file trigger instead of Google Drive like I've done with other

**[0:01:32]** videos on my channel so that it actually is entirely local I know that's a big thing that a lot of you ask for in other videos on my Channel with this package also I just want to say that this local AI package revamp that I'm doing now is

**[0:01:45]** just the beginning I really want to turn this into the golden standard for local Ai and also start to incorporate it into other projects than a building like archon so more on that later you know I'm always the guy with big ideas and so with that let's dive into setting up

**[0:02:00]** superbase locally so this is the local AI package completely revamped now with superbase and it has its own dedicated GitHub repository now so before I just had it with a bunch of other things in my AI agents masterclass GitHub repo but now since I'm revamping it and doing a

**[0:02:17]** lot more with it I have a dedicated place for it so I'm going to have that in a link in the description of this video check it out right here this is the Remy that you'll see at the homepage of the GitHub repo and this local AI package was originally made by the na

**[0:02:30]** and team let me zoom in a little bit here so you can see this um so I took what they built and they curated together and I built on top of it in previous videos on my channel to add things into the package so it started out with just n8n olama quadrant and

**[0:02:45]** postgress those were the four services in the local AI package and then I added in flow wise for another low code AI agent Builder open web UI so we can have a chat gbt like interface and now I'm adding in super base which I'm replacing postgress entirely since super base is

**[0:03:02]** post under the hood and then quadrant is also kind of similar because you can use it as a vector store just like you can use superbase but I'm keeping quadrant in there I kind of have a note on this here just because it's faster than superbase so for some use cases you

**[0:03:15]** might actually want quadrant but in general I love using super base just because I can use it as a SQL database and as a vector store for rag as well so this is everything that is now in the local AI package I'm going to show you how to get it all set up right now now

**[0:03:30]** all right as I walk you through this guide step by step for installing the revamped local AI package I'm going to be sure to hit on some points that I missed in other videos on my channel for this package things like how do you actually restart and update your local

**[0:03:43]** AI stack or how do you exclude things like ama if you're already running it on your computer so you don't want it running in Docker as well so even if you've seen other guides on my channel for this local AI starter kit this is still going to be really helpful for you

**[0:03:56]** and then if you haven't I'm still going to be very comprehensive going through this step by step so back to the readme here which again I'll have Linked In the description of this video it's just the homepage of the GitHub repository scroll down till you get to the prerequisite

**[0:04:08]** section cuz I want to focus on this first there are a few things that you have to have installed before you can go on to the rest of the installation instructions the first thing is you'll need python here to run a script that does a lot of the superbase setup that

**[0:04:22]** I'll show you in a little bit here you'll also want git or GitHub desktop to obviously clone this repository I'd recommend GitHub desktop if it's on your personal machine not on some computer in the cloud if you're hosting local AI there and then also Docker or Docker desktop because all of these local AI

**[0:04:37]** Services run as Docker containers and I'd recommend Docker desktop again just like with Git if you're running this on your personal computer and so once you have all these prerequisites installed just using these links right here you're good to move on to the rest of the installation instructions which I'll

**[0:04:52]** walk you through step by step right now so the first thing you're going to want to do is clone this GitHub repository so you just take this First Command right here open up a terminal and go ahead and run it and obviously I already have this repo cloned but if you don't then it's

**[0:05:05]** going to pull all that from GitHub you'll get a very different output right here running the command and then you go ahead and change your directory into local AI package so now my current directory in my terminal is exactly what I have open up here in my IDE and it's a

**[0:05:19]** pretty simple repository overall because it's not like we have to have the code for all the different Services bundled into this repository we just have to reference the docker containers in our primary file right here which is our Docker compose do yaml so this file is responsible for defining all of the

**[0:05:36]** different Docker containers that we want to pull together and create for our local AI package and so everything that you saw in the read me right here we have defined in the docker compos file so we've got n8n olama flow wise open web UI all these are defined as the

**[0:05:52]** individual containers like this is the open web UI blocked say that we want that as one of the services within our stack and these are the conf configuration items for it like the port that we're hosting it on and the name of our container that we're going to be

**[0:06:04]** using in our Docker compos Network and the one thing that is not included in here is superbase I'm going to touch on that in a little bit here because we actually need to clone the superbase repository separately and use a separate Docker compos file combined with this one and the primary reason is actually

**[0:06:22]** because superbase runs many different containers together when you host it locally and so it it's kind of a mess if I just dump it all in this ER compos file so more on that later but let's actually get to the next part of the setup and then we'll dive into some of

**[0:06:35]** the intricacies of getting superbase specifically installed into this package so yeah after you have everything cloned and you changeed your directory now it's time within an IDE to make your EnV file and to set your environment variables and it's pretty simple overall there's going to be a lot of environment

**[0:06:54]** variables that you see in the env. example file open that up right here there is a ton here and this mostly comes from superbase because there are so many different things in superbase that you can configure it looks pretty overwhelming but luckily to get just the foundation of superbase set up you can

**[0:07:11]** leave most of these environment variables as their default values there are only a few that you actually have to care about that I have pointed out in the readme here so that is what we're going to set up right now if you want to do more complicated things in superbase

**[0:07:24]** like set up their email authentication there are more environment variables and more setup for that but you don't don't need that for most of the AI use cases you'll be building with local AI so we not cover that right now cuz I want to keep that concise but just know that

**[0:07:37]** there are a lot of other things um if you want to set up other stuff in super base and they have a guide for that as well so I'll have this Linked In the description of the video as well because superbase put out a very comprehensive guide for self-hosting with Docker and

**[0:07:51]** this is actually the resource I used to learn how to incorporate superbase in the local AI package and so a lot of the stuff that'll show you how to do in a little bit is actually going to be using this so use this as a guide both in this

**[0:08:04]** video and also more of the advanced stuff at the bottom if you want to learn other things like dashboard authentication or actually setting up more advanced things like your um yeah email server if you want to configure an email server within local superbase not the stuff I'm going to cover right here

**[0:08:20]** so anyway all we're going to do right here I'm going to actually delete this Dov file and start from scratch I'm going to make a brand newv file walk through setting up all of the config ation with you right now and we're going to do it pretty quickly so don't worry

**[0:08:33]** I'll walk you through it step by step it's not actually that complicated here so I'm going to copy everything from. example and then paste it into this newv file that I just created here and so the first thing at the top is our n8n credentials and these we can actually

**[0:08:49]** set to whatever we want so we Define the secret here and this can just be a random alpha numeric string doesn't really matter what you set here I don't care either what I show you right here just because this is running enti enely locally on my computer and I'm going to

**[0:09:02]** reset mymv after I record this video anyway so that's everything for the n8n you just Define your own JWT secret and encryption key and then the rest of what we want to set up is for superbase specifically and so the first thing that we need is our postgress password this

**[0:09:17]** is going to be the password for our database and again just like with n8n you define this yourself so I'm just going to do something kind of silly here I'm just going to say test password so again I'll change this later and then we want to set our dashb Bo login as well

**[0:09:31]** so just like when you use a hosted version of super base you can log in to see all your tables and your users and your SQL editor and all that you have the exact same setup with local superbase and I'll show that later as well you have your own locally hosted

**[0:09:45]** dashboard as well and so this is the login for that so you can set the username to whatever you want the password the same as well just say test dashboard password I don't really care how secure it is right now and then these two values you can leave as the

**[0:09:59]** default and then we'll get to these three in a second here the last thing that I'll show you how to set before we go back to the superbase documentation is the Pooler tenant ID and so this is for the transaction Pooler connections to your superbase database and so for

**[0:10:14]** this doesn't really matter what you set it to just set it to some number right here that will be your tenant ID that you'll use again for when you are connecting to superbase with the transaction Pooler method and so that is everything besides the JWT secret so let's actually go back back to the guide

**[0:10:30]** right here for self-hosting with Docker because they have a really nice little tool here that actually helps us get set up with these last three environment variables we need to configure so if you scroll down a little bit above the halfway point for the documentation you'll see right here it actually

**[0:10:46]** generates a JWT secret for you so if I refresh the page watch this we have y1 RM if I refresh the page and then come back look at this it changed so we have a brand new JWT secret every time we refresh this page so we can just use

**[0:11:00]** this for our secret it's really convenient that we don't even have to bother generating it ourself we just paste this in right here and that is our JWT secret and then for the anonymous key and service roll key we can go back to the documentation and it can generate

**[0:11:15]** those for us so you just click on Anonymous key and then you click on generate JWT and then boom we can just copy this and bring it into our environment variable right here so I'll just go ahead and replace what I have right here nice and easy so these are

**[0:11:27]** the keys that are usually generated for you when you have the remote superbase instance but now since we're running it locally we have to actually Define these ourselves that's what we're doing right now and then for the service roll key we'll just click on this dropdown switch it to service key and then click on

**[0:11:42]** generate JWT again so I'll go ahead and copy that and then replace that service roll key just like I did the anonymous key and then look at that boom we now have everything configured for our environment variables it was actually pretty easy overall and so now we can

**[0:11:56]** finally go on to getting everything started with the Docker compos stack now to spin up our local AI stack there are a few different commands that we see here depending on your architecture so if you have an Nvidia GPU like me and you want to use that for your llms in

**[0:12:12]** the AMA container you'll use this Command right here and then if you have an AMD GPU on Linux you can use this and then for Mac users you unfortunately can't use a graphics card within a Docker container it's just a limitation of mac and so you can either just run

**[0:12:26]** entirely on the CPU which you can still use smaller lm's like less than 8 billion parameters with just a CPU or you cannot run olama at all so if you do D- profile none it's actually just going to not run the olama container at all so if you have Ama running outside just on

**[0:12:43]** your computer you can still reference that from within your n8n container or your superbase container whatever it might be and then there's some additional instructions for uh using Mac as well so that's everything depending on your architecture also if you just aren't on Mac but don't have a GPU you

**[0:12:59]** can run on the CPU as well and so all of these commands together each of them are using this start services dopy and this is a script that I made for you to make it super easy to get everything up and running and the reason it's a little bit

**[0:13:14]** more complicated now is because superbase is not just a single container let me show you what I mean it's it's kind of interesting so if you go into the superbase GitHub repository which you'll see in a bit why I actually have this in Source control right now and

**[0:13:28]** then you go into the docker folder and go into the docker compose file superbase actually has its entire own stack just like I have for my Docker compose file for the local AI package and the reason they have that is because superbase is actually made up of many

**[0:13:47]** different containers combined together like you have the studio which is the interface you're used to seeing when you have a superbase running remotely you've got Kong you've got the authentication container you have the res container real time all the different services that you have like the the object

**[0:14:03]** storage in super base are running as individual containers combined together and so I can't really just copy this entire thing and then go into my own Docker compose and just dump it all in here I mean that's going to be a total mess and I don't want to have to

**[0:14:18]** manually update the container versions when superbase updates things so I want to actually be able to reference their Docker compos and their GitHub repo and combine that with my own and that is exactly what this python script does for you so it'll actually clone the superbase repository or pull it to

**[0:14:36]** update it if you've already run the script before and then it'll combine the superbase docker compose file with our own for the local AI package to bring everything together and this is a little bit more technical um so don't worry if you don't understand this part but it's

**[0:14:51]** really important that we also run it on the same Docker Network so that way our n8n instance or whatever other container we have can very easily connect to our superbase containers as well and so this it right here is the um what I pass into the command to make it all run in the

**[0:15:07]** same Docker compos Network so that's super important and then another thing that the script does for you is if you ever want to restart everything like maybe you want to shut down your stack for a bit and then turn it on later or you want to update one of your

**[0:15:20]** environment variables and have that actually take effect you can just run the script again it is that easy and it'll restart everything for you and then another thing is if you want to to upgrade your containers like maybe there's an update to n8n or an update to superbase whatever it might be you can

**[0:15:35]** just follow these commands in the readme right here and that will take care of everything you just spin down everything with this First Command pull the latest updates to all of the containers in both Stacks with this command and then you just run the start services. with your

**[0:15:49]** profile like CPU or GPU Nvidia and it'll rerun everything it is that easy to restart things to take new effects with environment variables and to update your container as well so I hope that makes a lot of sense and so right now I'm just going to go ahead since I have an Nvidia

**[0:16:04]** GPU I'm going to take that First Command at the top just copy that go over to my terminal and I'm going to go ahead and run this and so for me since I've already run this before it's just going to pull the latest changes from the super based repository it'll actually

**[0:16:20]** pull everything for the first time if you haven't run this before and then it's going to tear down all of the existing containers that are running and then reboot them them all back up and that is how I do a full restart here and also really important to note if you

**[0:16:35]** already have workflows in an and ORF flow wise or if you have data in your super base tables tearing down the containers will not get rid of that so you don't have to worry about losing anything when you run this script to restart your containers everything will persist so do not worry about that I

**[0:16:50]** know that's a big question that I had when I was first covering the local AI package on my channel here and so right now it is yeah it's tore down everything and now it's restarting all the super base stuff and so it takes a little bit here um actually it's basically already

**[0:17:05]** almost done you do get a warning right here where it says it found orphan containers for everything that was just started with superbase you can ignore this I don't know exactly how to fix this um if you know just let me know and I'd love to take care of that but anyway

**[0:17:17]** yeah everything is up and running now so I can actually go to my Docker desktop here let me show this um by the way these are the settings that you want for your Docker desktop there's a couple of things like exposing the Damon um without TLS that you want to make sure

**[0:17:30]** that you have checked if you're using dock or desktop with Windows um just a little tip there a little aside there's a troubleshooting section in the readme as well that I would definitely check out if you're having any problems but yeah I'll close out of the settings here

**[0:17:41]** I'll go to my local AI package right here running in Docker desktop and look at this we have all these different Services running here uh which is super neat there's so much that goes into this package now you can literally like go into a llama I can look at the logs for

**[0:17:55]** it I can go into the exec Tab and I can actually enter in a command like I I can say AMA pull and I can look or AMA list that's the wrong command there and I can see the models that I have available to me in ama and I could even say AMA run

**[0:18:10]** and then I could copy the name of the llm that I have pulled I'll show in a second how I defined this I'll copy this and paste it and then boom I'm now interacting with quen 2.5 instruct and since I'm using the Nvidia GPU profile it is using my Nvidia GPU uh to run quen

**[0:18:28]** 2.5 right here so look at that super neat so you can interact with all these containers and see the logs as you are running things in your local AI package and by the way let me actually show this really quick here in the docker compose file this Command right here defines the

**[0:18:42]** llms and embedding models that are pulled for AMA by default and then the very last thing that I want to hit on before we create an agent together is I have a troubleshooting section in the read me right here with some common problems that I've seen with running

**[0:18:55]** superbas locally and some things that I've actually run into myself so so hopefully if you run into any issue it'll be listed here and there's a resource for a lot of these you'll be able to get through everything that I ran into if you did yourself that's kind

**[0:19:09]** of the goal of this troubleshooting section here so that is everything for getting the local AI package set up you now have everything up and running so like you can literally go to local hostport 6333 SL dashboard and then boom there's quadrant I know we're not using that in this video right now but I'm

**[0:19:26]** just showing like everything is available to you you can go to let's see 3000 And1 and then boom there is your flow wise and you can go to 8,000 and then you have your super base and if you go into it for the first time it'll ask you to input your username and

**[0:19:41]** password which remember you set as the dashboard username and password in the EnV file and this should look very familiar to you everything that you're used to seeing when you go to the remote superbase instance in your browser and then we also have n8n so you're going to

**[0:19:55]** go to local hostport 5678 and then it'll have you create a local NN account it's not actually a cloud one so it is running locally it'll have you create an account and then you'll have this overview right here where you'll have the local rag AI agent as that one workflow that is imported

**[0:20:11]** automatically but we're going to actually create another one here so I'm going to create the superbas rag AI agent I'll have this automatically import into your n8n instance as well so this will immediately be available to you when you go into n8n the only thing that you actually have to set up

**[0:20:26]** yourself is your credentials and so I'm going to walk through that right now and just briefly describe how this agent works exactly and so first of all it's just a basic AI agent using the agent node in n8n where we have our olama chat model connected we have superbase for

**[0:20:43]** chat memory just using the postgress node and then we have superbase for our Vector retrieval so that we have rag through superbase now instead of quadrant and to get all the credentials set up I'll start with AMA here you'll go to credentials and the drop down here create new credential and then the base

**[0:21:01]** URL is going to be o Lama instead of Local Host so it'll be HTTP olama and then the port is 11434 and then when you click save it'll automatically test your connection and if the containers are set up and all running properly it'll say connection tested successfully I'm going to switch

**[0:21:19]** back to my other credentials here and then it'll load all of the models that you had pulled with AMA when it was first imported so we got our embedding model and then Quin 2.5 7B instruct as well and then for superbase here our connection through postgress I'll create

**[0:21:34]** new credentials the host is actually going to be DB and the reason it's like that I'll actually go back over to my IDE here and then go to the docker compose file for superbase look at this the superbase the primary database container in the stack is just called DB

**[0:21:51]** and since these containers like n8n and superbase are all in the same Docker Network we can connect to it by just referencing the name of the container as the actual host and so then our database is going to be postgress and then the user name and password is going to be

**[0:22:08]** whatever you have set up in your environment variables and then keep the port the same all that is good to go I'm just going to close out of this but if I actually go and edit my other credentials that I have right here and you go ahead and click on I'll just

**[0:22:19]** click on retry you can see just like with AMA connection tested successfully so that is everything with AMA and then superbase and then when you connect connect let me just show this there's a slightly different setup when you connect with the superbase vector store versus actually connecting with the

**[0:22:37]** postgress node The Host this took a little bit of time for me to figure out so I hope that I save you a headache with this you can't actually say DB right here for some reason this doesn't work if you say DB for the host name here you have to actually say host.

**[0:22:53]** doer. internal so essentially that's telling NN to go outside to my machine my local PC and then go back into Port 8000 which is mapped onto the super base container so then you just have your service roll secret which you have set in EnV and that is it that is all the

**[0:23:12]** credentials that you have to set up you can reuse those credentials for the rest of this workflow as well this is the workflow that actually brings files that we put in a local folder into our local superbase Vector store so let me really quickly show you my rag pipeline right

**[0:23:29]** here how I get local files into my local superbase and then we'll test out the rag agent here just a really nice and simple demo you could literally just do this kind of rag setup within open web UI with the rag functionality but I just want to keep things simple here you

**[0:23:44]** could definitely take this workflow and extend it to your heart's content in n8n again this is going to be automatically imported into your n8n instance when you pull the repo and run everything like I showed you how to do earlier and so at the start of our pipeline right here as

**[0:23:58]** promised it it is a local file trigger and so it's watching for files that are added and changed in this folder specifically and the reason I know to use slata shared is if I go to the docker compos stack and look at the n8n service specifically the shared folder

**[0:24:15]** which is this guide right here on the left hand side is mapped to /data Shared in my n8n container and so when I add a file in here like test. text this file is now also in my container right here in SL dat shared and then SL test. text

**[0:24:34]** and so I'm using this folder so that I can dump things on my personal computer and have it actually go in my n and end container as well and Trigger this right here so you also want these two options ticked by the way otherwise this won't work but I'll go ahead and click on test

**[0:24:46]** step and then I can actually go back into here and let me go back to my test file I'll paste in some content right here that I just want to have in my Vector database so super simple test information right here click on Save and then boom look at that we now triggered

**[0:25:02]** with a change event and then the path which we're going to be using as our file ID essentially in the vector database is set right here as well so then I can go on to the next node right here which is basically just determining if it is an add or change event because

**[0:25:15]** if it is a change event like it is in this case we want to clean the vector database of any vectors for this file specifically so using this metadata filter again using the path as a file ID we're just cleaning the vector database of anything with this file so that we

**[0:25:31]** have a blank slate to make sure what we are inserting is really everything for the updated file we don't want any old vectors hanging around for a previous version of the file and then we pull the file within our NN workflow so now this node right here gives us this data

**[0:25:47]** output which is the contents of the file actually really is the file itself and then in the next node we extract the text from the file and so at this point we put a file on our local computer it went onto our n end container into our workflow and now we have the text from

**[0:26:02]** it it is nice and simple and then the next thing that we want to do within our superbase node before we actually run this we need to set things up in our database here so if you click on the docs tab right here it'll bring you to this page scroll down a little bit and

**[0:26:18]** then click on a quick start for setting up your vector store you want to copy all of this SQL right here because this is how we are going to set up our Vector database here and so I'm going to go to SQL editor and then I'm going to click

**[0:26:32]** on the plus icon create new snippet and then paste this in boom there we go and now we can run this right away except there's one change we have to do the size of our vectors is actually 768 because we're using the nomic embed text model from AMA that's just the vector

**[0:26:48]** size specifically so we'll change it to that this you can set to whatever embedding model you're using what the vector size is and then you can go ahead and just run this by clicking on run in the bottom right and fail for me cuz I already have executed this but for you

**[0:27:01]** it'll work and then we'll have this documents table let me scroll down to that right um where is the documents table right here boom there we go so it's an empty documents table right now but what we can actually do is we can run this to insert our vectors and

**[0:27:17]** usually I get an error like this it's kind of weird there's not actually a problem with my workflow all I have to do is just save and then refresh so I'll refresh n8n and then I'll just run test step right from the superbase vector store I'll make a change to my file just

**[0:27:33]** to trigger things again and then uh it executes and boom there we go so it's a little glitch with n8n where when you going through it step by step it fails at this node for some reason um but anyway I refreshed and ran it right from there and now if I refresh in superbase

**[0:27:46]** we have our record here so my to-do list is and then look at that it looks really really nice and we got the file ID for the metadata everything is looking good so now what we can do is go into our chat and it's kind of a weird file so I

**[0:27:59]** have to be explicit here telling it to use rag but I can just say uh look at my um test file and tell me what my to-do list is so now I'm chatting with quen 2.57 me instruct running locally using my GPU and you can see here that it

**[0:28:17]** invoked the superbase vector store tool retrieved my to-do list we can even see the results of that right here from what it pulled from the vector store and look at that based on your test file your to-do list is watch a movie code the next big SASS and learn how to tie my

**[0:28:31]** shoes all right it is working perfectly again just a very basic demo example here but we have everything including superbase running entirely locally and you could go and deploy this to the cloud keep it on your machine do anything that you want with this extend it with more services the world is your

**[0:28:49]** oyster with this local AI package so there you have it we now have super base running entirely locally in our local AI package which really is starting to sh shape up to be the perfect tool for you to run all your AI locally and build any AI agent that you could dream of and I

**[0:29:05]** have a lot of plans like I already mentioned to keep expanding this local AI package but also I want to hear from you so let me know in the comments what other tools or services or Frameworks you think I should include because I really want to build this into the

**[0:29:18]** golden standard for local AI but I need your help to make sure I'm including everything that I should and really this is a community-driven project as well so if you appreciated this content you're looking forward to more things local AI I would really appreciate a like and a

**[0:29:32]** subscribe and with that I will see you in the next video
