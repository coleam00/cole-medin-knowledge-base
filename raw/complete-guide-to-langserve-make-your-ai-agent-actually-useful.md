---
type: raw-transcript
title: "COMPLETE Guide to LangServe - Make Your AI Agent Actually Useful"
youtube_id: qgH_KFSFMUE
url: https://www.youtube.com/watch?v=qgH_KFSFMUE
slug: complete-guide-to-langserve-make-your-ai-agent-actually-useful
published: 2024-09-01
duration: "0:17:18"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** imagine having all the power of a custom-coded AI agent sitting behind a single scalable API endpoint in the cloud running 247 well today I'm going to show you exactly how to make that I'm going to take the AI agent that I've been building as a part of my AI agents

**[0:00:17]** masterclass series built with Lang graph and Lang chain and deploy it to the cloud as an API endpoint using a tool called Lang serve the tool that does all the magic of creating an API wrapper around my AI agent which in my case is a lang graph app but you can do this with

**[0:00:33]** any Lang chain chain so what I'm about to show you is going to work no matter what agent you have built with Lang chain and this is really important because you cannot be stuck running your AI agents on your local computer Forever at some point you need to deploy it to

**[0:00:48]** the cloud so it's running 247 and can scale as well and the best part about all of this is there's literally only three lines of code that I have to change in my front end my streamlet UI to interact with my new Lang serve endpoint I'll show you how to do that as

**[0:01:02]** well so here's everything I'm going to do today first I'll walk you through setting up the fast API endpoint for the agent using Lang serve then I'll go through the three lines of code that we have to change to make our front end work with this new Lang serve endpoint

**[0:01:17]** next and this is the best part I will show you step by step how to deploy your AI agent to your own dedicated Cloud Server using digital ocean for literally only $7 a month and then the last thing we'll do is we'll test out this AI agent now let us deploy to the cloud and make

**[0:01:33]** sure that everything is still working perfectly all right so I'll have a link in the description of this video to the GitHub repository where I will have all of the code for the Langs serve endpoint and the AI agent that I am showing here so you're going to want to clone this

**[0:01:46]** locally if you want to make any changes or extend this AI agent and then obviously also clone it onto your digital Ocean droplet or whatever Cloud instance you have to host your Lang serve endpoint and so there's a few files that we're going to be going over today but before we get into actually

**[0:02:01]** deploying it first we have the Lang serve chatbot script and this is where we have our streamlet UI the front end that we're only going to be changing three lines of code then we also have the file where we Define our Lang serve endpoints with fast API and then lastly

**[0:02:15]** we have runnable pine that's just where I have my L graph app set up with all the nodes defined and all the interactions with the llm and the tool calls all that good stuff and I'll show that very briefly here I've already worked on this in a separate video on my

**[0:02:27]** channel so you can check that out if you want um but I'm just going to give a little bit of an overview so you know what I am actually deploying here um for my example then we also have an example environment variable file so if you want to take a look at how to set up your API

**[0:02:40]** keys and Define the model that you want to use in the AI agent all that is neatly laid out here with instructions for every environment variable you'll want to set and you can also do that in your Cloud instance where you host a ler endpoint you're going to want to create

**[0:02:54]** aemv file and set all that up and I'll show that when I actually deploy this thing so really quickly going over the L L graph code we have here I have this agent set up that's going to use either an open AI anthropic or grock model depending on the llm model environment

**[0:03:09]** variable and then I have a bunch of tools that I'm binding into this model to create the agent that I use in my Lang graph app and so to start out very simply I'm just going to use all of my Asana tools that I've been using in my

**[0:03:21]** AI agents masterclass Series so it's basically just a bunch of crud operations for tasks and projects like updating tasks getting tasks uh creating projects uh you know creating tasks all that good stuff these are the tools that I'm giving to my AI agent to do my task management for me or to work alongside

**[0:03:39]** with me for it so at this point when I buy the tools I have this chat bot that I can now use in my L graph app and so I have a node simply for calling this model that has the tools bound to it and then a node for handling any of the tool

**[0:03:51]** calls and then I have this router this conditional router where basically if the AI agent says it wants to invoke a tool then I go to the tool node otherwise I just return the response the user so it's a very very simple Lane graph implementation but I want

**[0:04:04]** something basic because I'm focusing here on showing you how to deploy something not make some really Advanced AI agent so it's nice and simple for you here and so defining the workflow we just have our agent and Tool nodes with that conditional Edge I can pile it with

**[0:04:17]** memory and then return it and so this is the Lang graph app that executable that I'll be binding into the fast API endpoint to serve this with Lang serve and so you could do something like this with any Lang chain chain so you can extend this to anything that you built

**[0:04:31]** with Lang chain like I've already mentioned and so with that we can get into our Lang serve endpoints and this is really quick to get through langur makes it so easy to set up these endpoints and so first I'm just going to import everything that I need here the

**[0:04:44]** main packages that we're bringing in is fast API and Langer and then also UV corn for hosting and so with this I'm going to also import my function to get the runnable so I'm importing this function into my Lang serve script and then I'm going to create a fast API

**[0:05:01]** instance this is going to be the app that I serve the routes within and then I'm going to add some middleware here just for Cores you don't have to worry too much about this but you can set some tight security policies and stuff if you want so there's a lot that I'm not going

**[0:05:13]** to get into here but with Lang serve you can do all the usual security that you would with API endpoints and this is just a bit of a demonstration of that here and then within my main function I'll get my langra runnable again this could be any Lang chain chain or Lang

**[0:05:27]** graph runnable and then I will use this function from Lang serve add routes to basically put the runnable inside my fast API so this is where we use fast API and buy the routes in from my Lang graph runnable and then with this literally the last line of code here is

**[0:05:44]** just using uvicorn to run this app and I'm going to just have it hosted on 00000000 with Port 8000 and you can play around this however you want just make sure that you change your environment variable that references the endpoint to actually hit your API for your AI agent

**[0:06:01]** and so that is literally it we have now created our API endpoint you can run this with python Langs serve D endpoints stop pi and there you go and that's exactly what we're going to do on our digital ocean droplet and then in the chatbot here I promise three lines of

**[0:06:15]** code here they are first we're going to import remote runnable from Lang serve then we're going to get the endpoint URL from the environment variable and then last of all instead of getting the runnable directly through the get runnable function that we're now importing for our lengths endpoint we're

**[0:06:31]** going to set up a remote runnable instance with this URL and so when we deploy it on digital ocean that will change the environment variable to reference the IP address of our digital ocean droplet this is it we have now done all the code that we need and we

**[0:06:46]** can go on over to digital ocean and actually deploy this thing all right so here I am in digital ocean I've already skipped through a couple of the really really easy First Steps like signing up and creating your first project within digital ocean uh but it just takes a few

**[0:07:00]** minutes to do that so Blaze through that and you'll get to this point here we're I'm going to show you step by step how to deploy this with Langer from scratch I'm literally going to buy a new digital ocean droplet just for this demo so you know that I'm doing everything from

**[0:07:12]** scratch so click on the create dropdown in the top right here and go to droplets and then these settings are going to change a lot depending on the amount of memory you want and where you are so I'm just going to select the New York Region because it's the closest for me keep the

**[0:07:26]** data center as the same the default is usually good and then for the oper operating system just sticking with Ubuntu is generally good um same with the basic plan and then for the droplet I mentioned $7 a month and the way that you get that is going to premium AMD

**[0:07:40]** which is usually the default selected and then going to the $7 a month option now if you want to have more memory to run a chroma Vector database locally or to store larger files or maybe you need more than 25 gigabytes um because you are going to be storing a ton of files

**[0:07:57]** for rag whatever it might be you can choose a larger one but generally this is going to be all You' need for this application and so I'm going to select this especially just because this is a demo and you can always scale it more later like I would

**[0:08:09]** do if I'm going to take this further $7 a month is good and then you can choose either an SSH key or a password for authentication I believe it typically recommends SSH Keys passwords in my mind are a lot easier to manage so I typically go with that especially

**[0:08:25]** because it's still really secure as long as your password is good and they have very strict requirements for passwords and so I'm just going to paste in one that I have here there's a couple of requirements that you have to follow so just keep that in mind and then that's

**[0:08:37]** it and so now I'll log into my instance with this password going forward uh the rest of the stuff is pretty good you can give it a nice name as well so I can say like uh Lang Ser AI agent for the name and then any tags that I might want and I'll keep it in my

**[0:08:52]** YouTube Project so I'll go ahead and create droplet and it'll take a little bit to spin this up for you and so what I'm going to do here is pause and come back once this droplet is ready for me to log into it literally 20 seconds later and this droplet is now spun up

**[0:09:05]** and ready for me to log into it so the way that you do that is click on the three dots here then go to access console and then you can go ahead and log in as a root and you can change that user later if you want to as well so

**[0:09:16]** it'll open up a new browser tab here where I am in my Linux instance and we can go ahead and get everything ready to deploy our Lang serve API endpoint and so git is actually already installed in this machine um when you spin up the droplet and so I don't even have to

**[0:09:31]** install that I can just go right ahead to cloning my AI agents master class and get repository and I can see CD into it do an LS and see that everything that we have in the GitHub repo is right here in my machine already so I have a bunch of

**[0:09:43]** different commands I'm going to copy and paste in here so you'll see me looking on my other monitor I'll also have all these commands in the description of this video so you can follow along just by copying those as well the next thing that we're going to do is install python

**[0:09:57]** bnv so that we can create our virtual environment so it's an optional thing but creating virtual environments is highly highly recommended when you work with python no matter what environment you are in so we're going to go ahead and install this um and yep super super quick there are going to be a couple

**[0:10:13]** things that are not as quick we'll get to in a sec but yeah that one's nice and quick so now we'll go ahead and actually create our virtual environment and the path that you have for this doesn't really matter too much we just need to create it and then activate it with that

**[0:10:25]** path and then make sure that we actually are in that environment and I'll show what that looks like in a a second as well so there we go we have it created and so now I'm going to activate it with the source command so using that path that we just defined and here we go so

**[0:10:40]** now we know that we're in the virtual environment because my command line starts with AI agent VNV now whereas before it didn't so now if I do a pip list this is going to show me the python packages that I have specifically in this virtual environment and that's

**[0:10:53]** where we're going to install everything in one of the next steps here and so next what I'm going to do is I'm going to CD specifically into the folder of my git repo that has all the code that I've already went over here like our runnable dopy links or endpoints dopy and then

**[0:11:07]** the Lang serve chatbot dopy and here is where we can run the command to do the python package installation for all the packages that we need for Lang chain for Lang serve for UV corn all that good stuff so I'm going to go ahead and paste this in here python or pip install - R

**[0:11:23]** requiring inst. text and then no cter so that we aren't loading as much in a memory because this droplet only has 1 gigabyte of memory uh so we need to make it not store all the packages when it um builds them and in the cach there so what I'm going to

**[0:11:38]** do is pause this video and come back when this installation is complete because it definitely takes a good amount of time to install all of the Python package that we need for this Lang serve implementation all right so that took a solid five minutes so it takes a while because there are a lot of

**[0:11:52]** python packages here but if everything works well you're going to see something like this where it says successfully installed and then a bunch of different packages including all their dependencies you can also do a quick little Pip list if you want to see and make sure that all the packages look

**[0:12:07]** good here that are installed and so with that next what we can do is create ourv file so I'll just do nan. EnV it'll bring me into an editor where I can put in all of my environment variables like llm model for example everything that I have in the env. example file in the

**[0:12:23]** GitHub repo so I'm obviously not going to fill this out on camera because it's going to have all my API keys and stuff so I'm going to pause the video and come back when this is done all right so it just took me like 10 seconds it'll probably take you a little bit longer if

**[0:12:34]** you have to go fetch your API keys and stuff but it shouldn't be too bad and then we can move on to the next step which is setting up our firewall so before we can actually run our Lang serve endpoint we need to open up the firewall so that that Port 8000 is

**[0:12:47]** actually available for external machines like our laptops to connect into the droplet and reach the API endpoint so there's three commands that we have to run here the first one is pseudo ufw enable uh because we have to actually enable the firewall and then the next one is

**[0:13:04]** pseudo ufw allow and then 8,000 or whatever the port is that you have set up for your Lang serve endpoint so if you didn't change the code that I gave you at all it would be 8,000 that's what I have for mine so allow 8,000 and then now that

**[0:13:18]** the rule is added we just need to do a pseudo ufw reload and it'll say that the firewalls reloaded so now we have that new configuration and the port is opened up into our droplet for inbound traffic and so now that is literally all we need to do so we can go ahead and run our

**[0:13:33]** Lang serve endpoints I'll just say python Lang serve endpoints dop and if everything works well we'll see that nice little Lang serve message like this saying that we are good to go and so now what I can do to actually verify that this is working before I even update my

**[0:13:49]** front end to reach this endpoint is I can test it out in my browser so what I want to do is copy the ipv4 from my digital ocean droplet so I'll copy that go into new tab paste that go to Port 8000 slash dos so SL dos is an endpoint

**[0:14:05]** that is made available for any langing serve runnable basically and so with this if you have everything set up right you're going to see a page that looks just like this where we get some documentation here and it doesn't really matter what we see here I'm not going to

**[0:14:20]** go over this this is just to see that it is working so now we can go over to our friend en code and change it to point to this endpoint and test it out so the very last thing we just need to test this out in our front end and make sure

**[0:14:31]** we can actually Reach This endpoint and talk to our AI agent just like we did before we are hosting the Lan graph app on our local computer and so we have everything set up already changed up for this endpoint in our front end code here and so we just have this agent endpoint

**[0:14:46]** URL and I need to update that and so you'll go into your EnV I'm just going to show the example EnV so I'm not showing my secrets and you go to the agent endpoint URL and you would just paste in the ipv4 that you got from from the digital ocean droplet the same thing

**[0:15:01]** that I copied before when I did that/ docs test in the browser note that this does have to be HTTP not https in a more advanced tutorial maybe I'll go into setting up SSL and stuff but for now I just wanted to keep it really really basic um I also don't have any

**[0:15:15]** authentication on this endpoint or anything but like I showed with cores and stuff you can easily set that up just like you would with any API endpoint so this is very very basic it's just an unencrypted HTTP endpoint but you can definitely make this as secure as you would want and I could even make

**[0:15:29]** a tutorial on that later if enough people are interested in that but you can always figure it out yourself so anyway with that I'm going to pause here actually set this in myv and then we'll run it and test out this agent and we can go ahead and start talking to our AI

**[0:15:44]** agent just like we did when the Lan graph endpoint was hosted on our computer and so I'm going to make a very simple tool request here I'll just say what projects do I have in assana and we can actually watch the output if I go to my droplet here so you can see there's

**[0:15:58]** nothing at this point besides it recognizing the call the slash docs so I'm going to go back to my browser make this request we'll get the response from the agent there we go I got YouTube Fitness business personal encoding this is actually what I have for my projects

**[0:16:10]** in ASA and then I'll go back over to my digital ocean droplet and sure enough we got all of the usual standard output that we had when we were running this in the terminal on our laptop so we can see all the different projects that it got from the Assa API call all the different

**[0:16:25]** print statements that we have in our graph execution everything is working perfectly so we now have this deployed running in the cloud 24/7 all the power of this AI agent behind an API endpoint so I hope that was super super easy for you to follow along and learn how you

**[0:16:41]** can deploy any AI agent built with Lang chains super easily using Lang serve if you have any questions about any of the steps at all just put a comment below and I would love to help you out because I want to make sure that everybody who watches this including you can get

**[0:16:55]** through this very very easily like I also mentioned I'm going to have all of the steps that I went through in my digital ocean droplet in the description of this video as well so you can feel free to copy anything that you want I'll have the link to the repo as well so

**[0:17:07]** everything that you need will be available for you if you appreciated the step-by-step walkthrough I would really appreciate a like and a subscribe and with that I will see you in the next video
