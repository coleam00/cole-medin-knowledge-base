---
type: raw-transcript
title: "Create Your Own Private Local AI Cloud Stack in Under 20 Minutes"
youtube_id: hKrl5Gr7hM0
url: https://www.youtube.com/watch?v=hKrl5Gr7hM0
slug: create-your-own-private-local-ai-cloud-stack-in-under-20-minutes
published: 2025-03-12
duration: "0:16:51"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have covered the local AI package a lot on my channel it is hands down the easiest way to get all your local AI up and running in a single stack for free I'm talking your llms databases automation tools Local web search and your user interface and as I'll show you

**[0:00:18]** you can use this package to super easily spin up local AI environments in the cloud on demand because here's the deal even with local AI you don't always want it running on your own computer because maybe you have other people like your internal team that you want to be using

**[0:00:34]** your local AI setup or you want it running 24/7 and you don't want your stack constantly hogging all the resources on your machine or maybe you just want access to Hardware that you don't have and really it could be all of these reasons combined together and the good news is that deploying your local

**[0:00:52]** AI stack to the cloud solves for all of this and it is still considered local as long as you manage the cloud instance and and so in this video I will walk you through step by step taking the local AI package and deploying it to your very own private Cloud instance so you can

**[0:01:10]** have the local AI dream without being stuck to only your machine plus with some new additions to the local AI package this process could not be easier so this is very much a straightforward no fluff guide and I'll even cover Cloud providers and different Hardware requirements cuz I know those are big

**[0:01:27]** considerations for local AI as well and on top of all this I'll show you how to set up subdomains for things like n8n and open web UI so it is very much an endtoend guide now this is the local AI package I'll have a link to this GitHub

**[0:01:42]** repo in the description of this video the beauty of this package is we take all of these local AI services that you see right here bundle it all together in a way where we can install it and configure it in just a few steps that I have outlined in this readme it is so

**[0:01:58]** simple to get everything up and running and in a previous video on my channel that I'll link to right here I show how to use these steps to get everything set up on our own computer and now we're going to do it in the cloud so this package which was originally created by

**[0:02:12]** the n8n team I've extended to include all of these services so we've got n8n superbase olama open web UI flow wise quadrant and then recently I added CRX NG for local and private web search which includes reddis for caching by the way and then what's really important for

**[0:02:31]** this video is I included caddy now which is managed https and TLS so this is how we can have secure endpoints for all of our services that we have running in the clouds you can go to N.Y yourdomain.com for example and that'll bring you right to the n8n instance hosted securely in

**[0:02:51]** the cloud and that is with caddy so that's really important for this here and so I'll walk through all these steps now and I'll show you how to go through this in a way that will work for really any Linux machine that you have in the cloud so it doesn't matter if you're

**[0:03:03]** using digital Ocean or Lambda Labs AWS your own server if you have your own data center you can follow these steps I'm making it as generic as possible so it can apply to you no matter really where you're deploying your local AI setup so for this video we're going to

**[0:03:18]** be using digital ocean to deploy our local AI package they are not sponsoring this video this video doesn't have a sponsor at all I just use them myself I generally recommend them that's why I'm covering them here and they have the best options in my mind for CPU

**[0:03:32]** instances so if you're not running larger local llms that require a dedicated GPU digital ocean gives you the best options that I've seen you also have aami Cloud previously known as linode it's another good option for CPU instances too and then a quick barrage here for GPU instance platforms the main

**[0:03:50]** point I want to get across is to do your own research based on your needs and budget there are a lot of options out there because we've got Lambda Labs vulture we have paper space which is a part of digital ocean but is its own platform and then if you want to go more

**[0:04:05]** Enterprise of course we've got AWS Google cloud and Microsoft Azure all of these are going to provide you with GPU instances that you can deploy the local AI package to in the exact same way that we are going to do with digital ocean there are only a few platforms that

**[0:04:20]** don't work the best and I'll just cover those really quickly I want to make sure that I cover this all so that you guys aren't left using a platform that just doesn't work because tensor do is one of them it's a great platform for cheap gpus but they don't allow you to open up

**[0:04:33]** all the ports that you need for the local AI package and then we have platforms like runp pod and novita which are also great but they deploy everything as containers and since you can't run containers within containers very easily it's a lot more work to get the local AI package spun up in one of

**[0:04:50]** these and so that's why I'm sticking with digital ocean as well they do also offer GPU droplets if you want to pay more to have something really beefy for your local llms so now let's move on to creating our instance so I have a brand new project set up in digital ocean I'm

**[0:05:04]** going to go ahead and click on Create and then droplets in the top right to keep costs low for this demo I'm going to be creating a CPU instance so there's no dedicated GPU so I'm going to choose my region go down and then select this instance for $42 a month it gives us 8

**[0:05:19]** GB of RAM and two CPUs this is enough for the entire local AI package unless you want to run larger local llms so if you want to run any llms that are larger than seven or eight billion parameters you will need a dedicated GPU and that will cost you a pretty penny more but

**[0:05:38]** that's required if you want to use larger llms like 14 32 or 70 billion parameters but a lot of people will opt to do a CPU instance because it's cheaper and they'll just host AMA somewhere else or just use an API like open router because at least the rest of

**[0:05:53]** their stack is still private and local they're not paying anything for those Services except for the machine to host it so that's what we're going to be doing right here and of course if you have your own server hopefully you've got a GPU so you have that covered and

**[0:06:04]** then for our image I want everything set up with Docker already and Ubuntu is the most popular distribution of Linux so I'm going to select this one right here in the marketplace and so if you're following along with any other provider you will be able to find a new BTU Linux

**[0:06:18]** instance you can follow along with all the same commands that I'm going to be covering and then for the authentication SSH keys are a bit more secure but just to keep it really simple here I'm going to set up a password so I'm going to set up my password and then for my host name

**[0:06:32]** I'm just going to say YouTube local AI package and then I'm going to do this off camera click create droplet once I have my password set and it come back once my instance is ready all right so now my instance is created I can click into it now go to access and then launch

**[0:06:50]** a droplet console with root because I do need to have privileged access to run some of these commands that I'll show you here so I'm doing it as a root once we are in our instance now the there are a couple of steps that we need to do

**[0:07:02]** before we can follow those Base instructions and pull in the local AI package repository so going back to the read me here I have a dedicated section for some of the extra things you have to do when you are deploying to the cloud because we have to open up some

**[0:07:16]** firewalls and then also set up our DNS records and so I'll walk you through that right now first of all for the firewall stuff I've already run these commands in the instance you don't have to watch me paste in all these commands but you need to enable your firewall

**[0:07:29]** rules and then open up the ports for all of our different local AI services like superbase flow wise and open web UI and then n8n as well and then if you want to expose CR xng or olama you can run these commands as well the reason I don't do

**[0:07:44]** these by default is because CRX andg and AMA are not password protected like our other services so You' just be exposing it for anyone to use so typically I just keep these private and I don't open up these ports so the other local AI services on the instance can access

**[0:08:00]** cuz it's all through Local Host but then outside and accessing from the internet you wouldn't be able to use CR xng or AMA so after you have all your firewall rules set up you just run ufw reload and then all of those rules take effect and just keep in mind for all of these you

**[0:08:16]** do have to have privileged access so that's it for the firewalls now we need to set up our DNS records and this is going to be the same pretty much for no matter your DNS provider so I'm using hostinger it's not sponsored it's just because this is what I use use for my

**[0:08:30]** DNS for automator doai and what you want to do is go to digital ocean find your ipv4 and copy that and then you'll go ahead and paste that in the points to whatever that destination IP address is and then we want it to be a type a record and then for the name here this

**[0:08:47]** is the subdomain that we want to use so if we want yt- nn. automator doai to point to the n8n instance in our digital ocean droplet we set it up like like this we just say the name is yt- NN that is our subdomain so I'll go ahead and add this

**[0:09:05]** record click confirm and then we can do this for all of our other ones as well so I can do YT superbase I can add this and then we can do open web UI and then I'll add that and then lastly for now we can do flow wise and you can do the same

**[0:09:19]** thing for CRX olama any other services that you might add yourself to the local AI package as well so that is everything for DNS and that's everything that we have for our extra steps for deploying to the cloud so now we can go up to the top and we can run everything that we

**[0:09:35]** have as the base installation steps so I'm going to start by copying the get clone command I'll go ahead and open my instance back up paste this in Clone the repo and then change my directory into it so now everything we see with an LS is what we have at the root of our

**[0:09:50]** GitHub repo and one extra step that I have to do here just because I have everything in a feature Branch right now I have to change my Branch you won't have to do this though cuz I'll have everything in the main branch by the time you're watching this video but now

**[0:10:04]** we have all the configuration for things like caddy which I won't go over to this in detail right here I want to keep this tutorial concise and the things that you care about but you can dive into that if you are curious but now what we want to

**[0:10:15]** do is set up our environment variables so I have an example for everything in this env. example file so what we want to do is copy the. example file and I'll zoom in a little bit just to make it really easy for you to see we want to

**[0:10:30]** copy this into a newv file and so now the contents of VN EnV look exactly the same as. env. example and so now we'll use Nano to edit it and so this does assume that you have Nano and git and Docker already installed I do call that out in the remme those are prerequisites

**[0:10:49]** you can just install those based on your Linux distribution if you don't have them already let's go ahead and edit this file so in the EnV file I have comments that tell you which are required and how to set up all of these variables and so for n8n this is just

**[0:11:06]** any alpha numeric string that you want to set as something decently long to make it secure and then for the superbase secrets you want to set up your postgress password and also the login details for your superbase dashboard and then I have links here that bring you to the superbase

**[0:11:21]** self-host guide this will help you set up your JWT secret Anonymous key and service roll key and it makes it very very easy to go through that and then for your pool or tenant ID you can set this to just kind of whatever number you want like 1,000 for example so really

**[0:11:37]** easy to set up all these values the one thing that I go through with you right here is setting up the caddy configuration because these are all of our subdomains so let me show you this I'm going to uncommon all of the subdomains that we set up in hostinger

**[0:11:52]** or whatever your DNS provider is and I'm not going to uncomment AMA and cxg cuz I'm not using those and then for the let's encrypt R email you can just set this to whatever your email is like I'll do col medine automator doai and then for the host names here obviously change

**[0:12:09]** this to whatever subdomain you set up in your provider and what your actual domain is so for n8n for example it was yt- nn. automator doai and then I'll pause and come back once I have the other ones set up all right there we go all of our subdomains are exactly what

**[0:12:26]** we have set up in our cloud provider so now to save and exit from this file with Nano there are a few commands first you want to do contrl X then it'll ask you if you want to save so you'll just type Y and then finally you can press enter

**[0:12:41]** so again that is contrl X then y then enter and now the contents of this I'm not going to print it out here because I edited all my other Secrets as well behind the scenes it'll print out that entire EnV so you can make sure that everything was applied and now we are

**[0:12:55]** ready to run that script that's going to spin up everything with lock ER and so going back to the read me there are a few different options for this command because there are different profiles to use depending on your GPU or if you want to run in CPU mode so if you have a

**[0:13:13]** cloud instance with an Nvidia GPU like if you're using Lambda Labs or AWS or something like that or a digital ocean GPU instance then you'll run this command maybe just replacing python with Python 3 a lot of Linux distributions you have to specify Python 3 for the command we'll see see that in a second

**[0:13:30]** for our case specifically since we just have a CPU instance I'm going to run this command to run the AMA instance on my CPU because I don't have a GPU so I'm going to copy that come back over here and paste this in you'll see that it says python not found so typically it

**[0:13:48]** just means you have to add a three at the end so specifying Python 3 I'll go ahead and run this and now it's going to kick off that entire process where it pulls the super base repository and it starts the super based containers there's some settings behind the scenes

**[0:14:02]** that it sets up for CRX and as well so this script takes care of a lot of things so you'll see it pull and run the superbase containers and then it'll wait a little bit and then it'll pull and run the rest of the containers for our local

**[0:14:13]** AI stack and it has it all together in a single Docker composed Network so all of the containers can communicate with each other and this will take a little bit because some of these containers are rather large and it has to pull the AMA model and import the n workflows and

**[0:14:27]** everything and so I'm going to pause and come back once this is done and just a few minutes later we have all of our containers up and running your logs should look something like this and there was a bit of a glitch with my digital ocean droplet here that's why

**[0:14:40]** you see some blank space but your logs will look something like this where we have the superbase containers pulled and executed and then the same thing for the rest of our local AI package for everything like n8n open web UI and caddy and to see all of your containers

**[0:14:55]** running you can do the docker PS command it'll show you every single one of the containers in the stack you can make sure that they all say that they are up if you see any that are down or restarting then you probably have some sort of issue that you would want to

**[0:15:07]** look into and you can also do Docker logs DF and then the name of your container and this will give you all the logs for that specific container like we're looking at caddy right here and the- f means that it'll follow as more logs come in as well so just a couple of

**[0:15:22]** commands to help you manage your stack but now we can go over to our browser and test this out so I'll do a new tab and I'll do yt- nn. automator doai and there we go all right we have our Blank Slate sign up page for n8n we could do

**[0:15:40]** yt- superb. automator doai and it'll take us to our dashboard asking us to sign in we can do YT open web UI all right there we go we got open web UI so everything is working perfectly I'm able to connect to it from an external browser just on my computer and this is

**[0:15:57]** beautiful and I'm not going to cover how to use all these different platforms here there are other videos on my channel that I'll link to in the description of this video if you want to dive into how to create local agents with n8n and ol and everything right

**[0:16:10]** here we just wanted to focus on setting up our local AI stack hosted in the cloud and we have accomplished that so there you have it the fastest way to deploy your local AI setup to the cloud and as a whole I have a lot more coming for the local AI package as well because

**[0:16:28]** I am always adding new new Services making constant improvements and putting out more content for things like guides on creating local AI agents leveraging this package so if you appreciated this content and you're looking forward to more things local Ai and AI agents I would really appreciate a like and a

**[0:16:46]** subscribe and with that I will see you in the next video
