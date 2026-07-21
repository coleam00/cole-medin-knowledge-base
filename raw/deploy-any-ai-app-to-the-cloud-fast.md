---
type: raw-transcript
title: "Deploy ANY AI App to the Cloud FAST"
youtube_id: 259KgP3GbdE
url: https://www.youtube.com/watch?v=259KgP3GbdE
slug: deploy-any-ai-app-to-the-cloud-fast
published: 2024-10-06
duration: "0:21:20"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have built a lot of AI applications on my channel over the last couple of months and the most requested followup is that I would make a video on how to deploy them to the cloud so I am super excited to bring you exactly that today we're going to take the local AI starter

**[0:00:18]** kit by n8n that I did a deep dive into last month and deploy that to the cloud don't get me wrong it is really fun to build your AI apps locally and get them set up and working but in the end when you want something for real that has

**[0:00:32]** other users on your platform it cannot be stuck in your development environment simply put you have to make it accessible on the internet for other people to use in a secure way deploying your applications can be a bit tricky I am not going to sugarcoat it but that is

**[0:00:47]** why I'm going to break it down step by step for you now so that it feels like a walk in the park we'll cover using a custom URL setting up https and getting your N8 workflows to connect to the other local AI service in this new setup on top of that we are going to keep oama

**[0:01:04]** and the databases secure so they are only accessible within the n8n workflows I am going to be deploying the local AI starter kit to the cloud since that is the most popular solution that I have covered but I will explain throughout this video how what I'm doing will make

**[0:01:19]** it possible to deploy literally anything that runs on Local Host with a port on your computer a streamlet application olama a nextjs app if you don't want to deploy it to verel a do ER container that deploys something with the URL and the list goes on so no matter what you

**[0:01:35]** are building this applies to you so without further Ado let's dive in so first a little bit of an overview what I'm deploying to the cloud right now again you can use what I'm showing you now to deploy anything to the cloud but I'm picking this specifically because I

**[0:01:49]** have to choose something and this is the most popular solution that I have covered on my channel and so what this is it is a local AI starter kit by the n8n team and so what it does is it packages together olama for your llms quadrant for your vector database for

**[0:02:06]** rag postgress for your SQL database for things like chat memory and then also n8n for your workflow automations it is an amazing tool and again I did a deep dive into this tool and how to set it up on another video on my channel but the primary thing here is all of these

**[0:02:23]** services are running on your local host when you have this running on your computer and so n8n for example would be on Local Host Port 5678 and so that's fine when you just want to access it yourself on your computer but when you actually want to deploy it you want a URL like N.Y

**[0:02:42]** yourdomain.com that would then redirect to the instance of n8n that's running on Port 5678 on the machine that you're hosting it on in the cloud so that is what I'm going to show you how to do right now so for my cloud provider today I chose digital ocean I really really

**[0:02:57]** prefer digital ocean for most use cases and so I'm just going to keep it simple using what I'm really comfortable with here the one thing I'll say that it's not the best with is when you want to have a really powerful machine in the cloud to run really really good large

**[0:03:10]** language models like 3.2 90b for example in that case you're probably going to want a machine from a service like runp pod which is what I'd recommend for that they have a lot of different options to get very powerful machines with a lot of vram to run those larger models but in

**[0:03:25]** my case I'm just going to use smaller models and also if you're deploying something like a streamlet app or a nexj s app you don't need a lot of power and so yeah digital ocean just has really good offerings for that so I'm not affiliated with run Potter digital ocean

**[0:03:37]** but these are just my preferences for those different use cases and so once you're signed into digital ocean you can go in the top right and click on create here they do have GPU droplets but um they're pretty Limited in their offerings right now which is why I

**[0:03:50]** recommend runpod for the beefier machine so I'm just going to click on a droplet here and create something pretty basic and so I'll walk you through step by step very quickly what I have here so you can have the exact same machine as me if you would like I'll leave the

**[0:04:03]** region and data center the same and then for my image here I'm going to go to the marketplace and choose Docker for Ubuntu so this is the only thing that might be a little different for you if you have a different distribution of Linux or if you aren't using Linux then the steps

**[0:04:17]** that I'm going to go through now aren't going to be exactly the same because even if you're using Linux you might have a distribution with a different package manager like yum for example but if you have a Linux machine in the cloud with Ubuntu the steps are going to be

**[0:04:31]** exactly the same no matter what cloud provider you are using and so I'm trying to make this tutorial here very cloud provider agnostic and so it doesn't really matter if you're using digital Ocean or not as long as you've got a new boont to Linux machine and that is

**[0:04:43]** really really standard anyway so I'd recommend that and then for the droplet size I'll just choose the largest U basic plan one that's available to me because I want some good CPU here um and then for the password I'm just going to get that from another screen that I have

**[0:04:58]** up here um this is also we're going to be referencing the steps as I go through it with you guys so I'll just paste that in and then I'll leave everything else the same I guess I can change the host name here I'll just say YouTube uh AI

**[0:05:09]** app deploy all right and then this is looking good so I'll go ahead and click on Create droplet and then it takes about like 30 seconds to a minute it is super super fast and then we'll be able to log into our droplet so there we go after just like a minute like I said my

**[0:05:23]** droplet is now ready for me to access so I can just click on the three dots right here click on access console and then launch droplet console and boom that is it we are now connected into our machine and we can go ahead and enter in any commands that we want so now as promised

**[0:05:37]** I get to walk you through step by step how to deploy an AI application to the cloud with this local AI starter kit as an example I have done nothing on this machine at this point so this is going to be from start to finish every single step that you need on another monitor

**[0:05:51]** here I have all the steps I'm going to copy and paste so I can also be nice and quick so you don't have to watch me type everything out um so the very first command that we have here is going to be to clone our git repository for the

**[0:06:03]** local AI starter kit and then now that I have cloned it I have this new folder here that I can change my directory into and so now with that there's a couple of things that we want to edit that I went over in my last video on this as well so

**[0:06:16]** first of all we have ourv file so I'm going to do nan. EnV because we have to set up a couple of things here for postgress and also our n8n security and so for postgress you can change your username and password to into the database and you're going to set this as

**[0:06:32]** part of your credentials in n8n and then also the name of the database so I'm just going to be deleting this instance after this video so I'm going to leave it all as the same and I'm also going to just show you these secrets that I type here because it really doesn't matter um

**[0:06:45]** since I'm getting rid of this and so for these secrets you can really just type in whatever you want it doesn't really matter it just has to be something that you don't want to share because these are encryption keys that you are creating yourself um and so I'm just

**[0:06:57]** going to kind of type in whatever here and then leave everything that's same for postgress you can change this to fit your needs as well and then to exit out of this it's going to be control X or command X if you're on Mac and then y to

**[0:07:09]** save and then enter and then boom there we go so now if I do a cat. EnV I can see that my updates to this file have been made and so now I'm also going to change the docker canose file too because there is one thing that I want

**[0:07:23]** to add in my oama container to actually pull the things that I want when this runs because otherwise I'm going to have to pull those at runtime to have the models I want available to me in the na workflows and so what I'm going to do is I'm actually going to copy what I want

**[0:07:39]** this line to be right here so this this command is what runs when the AMA container starts and I want to add in another model so I'm going to pull the embedding model as well namic embed text because without this available we don't actually have a model available to us

**[0:07:54]** for our embeddings for Rag and so I'm just making that one update here like I made in my other video contrl X Y enter boom and we have those updates made so now we've made all the changes that we need in our source control here and we can move on to our firewall steps and so

**[0:08:10]** now before we actually run anything with these containers we need to get a few things set up and that's what I'm going to walk you through here starting with the firewalls and so the First Command that I'm going to run here is pseudo ufw enable now this command doesn't actually

**[0:08:25]** need to be run in the docker digital ocean droplet but it for a lot of your different droplets or if you're using a different cloud provider you have to make sure that ufw is enabled for firewalls and so I'm going to do that and now we can do some enabling and so

**[0:08:41]** the next command that I'm going to run here is going to be to open up ports 80 and 443 without these open in a later step when we set up our SSL CT for https it will fail so we have to run these and get that set up and then we will do a

**[0:08:57]** pseudo ufw reload so that we can apply those rules for the firewall so there we go that is everything we need firewall reloaded perfect now we can move on to our next step um because again there's a couple things we have to do before we actually run anything here for our

**[0:09:12]** containers and so I'm going to paste in The Next Step here and that is to install engine X engine X is a reverse proxy and that is what's going to make it possible for set it to set it up so that there is a URL that a user visits

**[0:09:24]** and then behind the scenes it routes that request to n8n that is running on the Local Host here on Port 5678 and you'll see when I set up the configuration for NN how it makes that connection and so let me do pseudo app install engine X I will continue with

**[0:09:41]** this operation and it's going to take a little bit to install uh because NN or engine X is a little bit larger here but in the meantime I'll just copy the next command here um and then yep there we go so it was only like you know 15 seconds

**[0:09:56]** even though it was bigger nice and quick and then I'll paste in the next command here um and so this is where it gets a little technical with engine X we have to set up all of the reverse proxy configuration but just bear with me because it's not that hard overall

**[0:10:10]** there's only a few commands that we have to do even though it might be a little more Technical and so next one I'm going to do is I'm going to go into this enginex configuration for an application that I'm going to create and this is where we start the config to make it

**[0:10:24]** possible to have a URL that points to a specific port in this machine and then I'm going to paste in some conf fig here which I will have available for you to copy in the description of this video and I actually should mention that all of the steps that I'm running here I

**[0:10:37]** will have there for you in the description for you to copy so you don't have to type out anything yourself the one thing that I'll say for this config is that it gets really nitpicky with tabs and spaces I would recommend just sticking with spaces and having two

**[0:10:50]** spaces per tab so right here it's just two spaces and then for these that are indented one level deeper it is four spaces so make sure that you have all these spaces otherwise sometimes you will get errors that'll tell you that it's not recognizing characters in that line weird things like that um but yeah

**[0:11:07]** you can see here that I have my domain nn. dynamis doai that is listening on Port 80 80 is the default port for when you are visiting a website with HTTP and so we'll set up https later but when you visit this site on HTTP you are then

**[0:11:25]** redirected to local hostport 5678 and that is where we have n8n posted and you can see how if you have a nextjs app on Port 3000 or a streamlet app on Port 5601 whatever it is you would just set that here and that's how you can reverse proxy to get your url to point to this

**[0:11:42]** right here this local host and this port and so this is how you can use it to literally deploy anything that you want on the cloud and so again making that connection back to other things as well so I'm not just focusing on the local AI starter kit but anyway that out of the

**[0:11:57]** way I'll do a control X again y enter ENT and boom we are good to go so next up we need to actually enable the application we do this by creating a symbolic link from the folder that we created in the sites available folder to the sites enabled folder within engine X

**[0:12:13]** so I'm going to run this and now that'll actually make it so that our URL is going to be set up to go to local hostport 5678 for n8n and then I can run a command to test that our configuration is set up correctly and that our site is

**[0:12:26]** enabled and for that we can run the command pseudo engin x-t and this is going to tell us if everything is looking good and so yep it says a syntax is okay the test is successful and we are good to go all right and so with that I'm going to

**[0:12:43]** Simply do a Reload here so I'm going to copy this command paste it in do a Reload and we can go ahead and move on to our CT now before we get our SSL certificate for https so our site is secure we need to go into our DNS

**[0:12:59]** settings now so you could have done this really at any point in the last like 10 steps so I'm just going to do it now because it's required for SSL and so all you have to do is go to your digital ocean droplet right here so I'm in the

**[0:13:11]** settings for my droplet and copy your ipv4 then you're going to take that and then go into your DNS provider so I am using name cheep um but whether you're using Blu host Squarespace name cheep it doesn't matter you're going to have someplace that looks like this where you

**[0:13:26]** go into your settings and you can view it'll be called like DNS s DNS settings Advanced DNS some view within your provider that gives you all of your records here like text records cname records a records so find that right here and then you want to add a new

**[0:13:42]** record so it'll be an a record the host will be n8n or whatever subdomain that you picked to host and then for your IP address you paste in the IP before of the digital ocean droplet and so there we go I've added this a record and we are good to go back to digital ocean to

**[0:13:59]** to Now set up our SSL SE that is everything that you have to do within your DNS settings it is super super simple and so now moving on what we can do is install CTB that's what we're going to use for our SSL seert now I had to verify some things off camera so I

**[0:14:14]** already ran this command but I promise I really haven't doing this from scratch I just had to quickly do that off camera so you can see that's why it said it was already installed but you'll install that it might take a little bit and then after you can run the command to set up

**[0:14:28]** the CT for your domain so um for me it's going to be nn. dynamis doai and again I already ran this command and so it's going to ask me if I want to um yeah I can just say renew and replace the certificate there'll be different settings where it'll have you enter in

**[0:14:44]** your email and agree to their terms and conditions if you haven't done this already I'm just going to renew this certificate here um but the message that we get as a success is going to look very similar here where it says deploying certificate and then successfully deployed the certificate

**[0:14:57]** and that is it we now have everything set up for enginex and certbot for SSL so we can finally run our containers and start up our local AI starter kit so I know that some of these steps were kind of technical but again you just got to bear with me through it um and I hope

**[0:15:14]** that this makes it really really clear so again Ask me in the comments if you have any questions on these things but now we can actually run this thing and so I'm going to change my directory back into our self-hosted AI starter kit and then I can copy the command to run this

**[0:15:29]** with Docker canose and so you can run this with the GPU as well there are instructions in the readme for the local AI starter kit repo on how to run this if you're going to use Mac or if you're want to use your Nvidia GPU I'm just going to use the CPU because I have a

**[0:15:43]** very basic digital ocean droplet and then I'm including the Dash D flang for detached because if you don't include this then your terminal will actually hang as it waits for more logs from the docker containers and so I'm just going to run this here and it's going to take

**[0:15:58]** a little bit longer for you because you're going to have to pull all of these images I did this ahead of time so you don't have to wait for all of that to pull um but when it starts successfully you're going to get a view that looks like this where we have all

**[0:16:11]** of our containers running and then the ones that are just run for the setup like NM import we'll say exited um but it'll be in green because that means that it was successful so we are good to go and you can even do a Docker um can pose log if you want to

**[0:16:27]** see the logs from all the container so this is what's currently being spit out in the logs and this will update in real time so as I make requests to n and postest and all that I can run this command again to see all of my logs that

**[0:16:39]** are happening in real time and you can also do other Docker compose commands like Docker compose down or stop if you want to destroy the containers you can do all the commands to manage the containers with Docker compose and then just the name of that argument that you

**[0:16:54]** want to add to delete or view the logs whatever it might be and that is everything that we need so we can now go into the browser and go to nn. dynamic. or whatever your url is and boom we now have access to our n8n instance that is

**[0:17:09]** running on our digital ocean droplet and so I'm going to set up my account really quick I'll just kind of put in whatever here um because we got to create our account the first time that we're in CU I really am doing this from scratch here so I'll set up my account and there we

**[0:17:24]** go and so I'm going to um actually import a workflow that I had from a previous video and come back once I have that all right so I have imported my workflow from my previous videos and we are going to quickly set up the connections here so that I can show you

**[0:17:39]** how to get everything working in the N workflows now that we're hosted in the cloud and so if you have followed these instructions to this point to deploy a xjs app a streamlet app or something like that this obviously wouldn't apply there but at this point your streamlit

**[0:17:53]** or nextjs app or whatever you're trying to deploy is working now and so this is just a little bit of a bonus for if you are deploying the local AI starter kit specifically and so to set up the credentials here first I'm going to click into olama I'm going to uh create

**[0:18:08]** new credentials here and then for the base URL actually what you can do is because this is all set up with Docker compose each service that is within the docker compose file as a separate container can reference the name of the other service in Docker compose so we

**[0:18:26]** specifically call our olama container just olama so I can reference it like this the port is 11434 I'll go ahead and click save and then my connection is successful so there we go we are good to go and then for postgress it's going to be a very similar deal here so the host is going

**[0:18:44]** to be just postgress because that's the name of the service in the docker compose file and then the database is n8n my user I believe was just postgress um actually let me verify that really quickly here what did I call my user let me U go back back to my environment file

**[0:19:00]** and check that okay I called it root that's right okay so uh the user is root not three O's and then the password I just had as password um and there we go so I'll go ahead and click save and we got that connection as well so we are

**[0:19:13]** looking really good and then the last one right here is just to get quadrant set up so I'm going to select my credentials here and then the API key can actually be whatever you want because this is running locally it doesn't actually matter and it won't break the connection and then the um

**[0:19:26]** right here for the URL is just going to be quadrant HTTP quadrant and then the port is 6333 go ahead and click save this connection is good as well and that is everything so now I'm going to go back and then set up the same thing for AMA

**[0:19:43]** really quick for the embeddings and um then yeah we can go ahead and test it out so I'm I'm just using llama um yeah 3.1 8B right now it's not the best with rag so I'm just going to delete this tool right here um and just have a quick chat message with

**[0:19:57]** it because I don't want it to go through the whole rag process right now so I'll just say hi and make sure that my connection with postgress and AMA is working good there we go we got a response from llama 3.1 8B so everything is looking really really good couple of

**[0:20:12]** last notes here it says that it's dangerous in my URL bar here but I think that's just because I've been playing around with the SSL Sears a lot testing this out and getting it set up deploying it to different digital ocean droplets and so typically you won't see that

**[0:20:26]** it'll be a good SSL sht right away um and then the other thing that I wanted to mention here is that the rest of this workflow uh with the Google Drive ingesting of documents for Rag and all of that that is going to be um something that you can find in other videos on my

**[0:20:41]** channel so I'll reference that as well if you're curious about how this workflow all works in n8n I obviously just wanted to focus on how to get this deployed in the cloud today so there you have it you now have what it takes to deploy anything that runs on Local Host

**[0:20:54]** with a port on your computer to the cloud and it's really important to do that to actually take your application to production so I hope that you found this really really valuable and clear if you have any questions about this process or creating AI applications in general just let me know in the comments

**[0:21:10]** and I will answer for sure so if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
