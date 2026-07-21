---
type: raw-transcript
title: "Flowise + n8n - The BEST No Code + Local AI Agent Combo"
youtube_id: 23s2N3ug8B8
url: https://www.youtube.com/watch?v=23s2N3ug8B8
slug: flowise-n8n-the-best-no-code-local-ai-agent-combo
published: 2024-12-04
duration: "0:29:13"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** before we get into the main video I have two announcements that I'm very excited to share with you really quickly here the first one over in our automator Think Tank Community I am opening up sections for both n8n and local AI obviously playing very well into this video things that I'm going to keep

**[0:00:15]** focusing on a lot on my channel the second announcement I am doing a collab with zuar and his YouTube channel AI Workshop where he does a ton with NN war on that coming soon but I'm very much looking forward to that collab so with that on to the main video the future of

**[0:00:31]** AI is ultimately going to be running everything locally your llms your reg pipeline your workflow automations and the list goes on a few months ago I covered the local AI starter kit developed by the n8n team which provides an amazing proof of concept of running all of your AI needs locally and that

**[0:00:49]** video completely blew up on my channel it is still my most viewed to date by far and I think the biggest reason for that is like me you realize that local AI is the way of the future and this package is a very powerful demonstration that running everything locally and

**[0:01:06]** having all the power that you need on your computer is not that far off from reality the biggest blocker right now is just that open source llms aren't quite as powerful as the close Source ones right now but that Gap is diminishing very quickly more recently I added open

**[0:01:20]** web UI into the local AI starter kit to make it possible to interact with your NN agents in a beautiful locally hosted UI and now I'm adding adding another platform into the mix flow wise flow wise is a low SL noode AI automation tool it is completely free open source

**[0:01:39]** and built on top of Lang chain which I also love and the best part is it pairs really really well with n8n and that's what we're going to cover in this video n8n is still my favorite no code AI automation platform especially because of how well it integrates with hundreds

**[0:01:54]** of applications but there is definitely a steeper learning curve for n8n especially when building your AI agents flow wise on the other hand is as simple as it can come and has become my go-to platform to very quickly prototype AI agents for what I am building and I

**[0:02:11]** integrate it with n8n because I use n8n workflows as my agent tools to interact with things like slack and Google drive it is just the perfect combo to build AI agents super quickly that can really do anything and in this video we'll build an agent together using flow wise and

**[0:02:28]** n8n to demonstrate the power of this combo and really showcase why you want to use both platforms together and not just stick with one and we're going to do all of this within the local AI starter kit let's Dive Right In so let's start with an overview of flow wise pH

**[0:02:42]** of prototyping is very crucial and you want to do it fast and that is what flow wise combined with n8n does very very well and flow wise is backed by y combinator ton of people are using it it's super easy to install they have their GitHub repo here so you can see

**[0:02:56]** all the code for flow wise they've got instructions on how to run it both with npm and with Docker which by the way Docker is what we're going to be using for the local AI starter kit and if we go into their Docker folder here they have instructions on how to run

**[0:03:11]** everything with Docker so really the only prerequisites that you need for flow wise and the local AI starter kit is GitHub desktop and Docker desktop and I'll have a link to both of those in the description of this video so you have those installed and you're going to be

**[0:03:24]** able to follow along and do everything that we are seeing right here and so they even have instructions on how to run it including setting up the EnV file there's a lot of environment variables that I'm not bringing into the local AI starter kit because I want to keep it

**[0:03:36]** simple but you can add things like user authentication to flow wise as well so definitely check this out if you want to look into a bit more of what is available for environment variables but yeah this Docker compost file right here that defines the flow wise service this

**[0:03:50]** is what I use to bring it into the local AI starter kit and that's what I'm going to show you how to run right now so let's dive into actually getting this running all packaged together with this AI start kit that I've extended with flow wise and so if we scroll down in

**[0:04:04]** this read me here we've got instructions on how to install this and I'll have this Linked In the description as well but it's super basic you literally just need like three commands to get this entire thing up and running because first of all you have to do a get clone

**[0:04:18]** of this repo that's why get is a requirement I obviously already have a clone which is why I get this error U but once you have that you just need to CD into the repository Right Here Local AI package and then and then if I do code Dot and I have Visual Studio

**[0:04:32]** installed this will open it up right away within my VSS code and here's my Docker compose file so you can see right here that my recent addition is the flowy service with open web UI being the last thing that I added in beforehand and so this is just running on Port 300

**[0:04:48]** And1 U actually flow wise by default likes to run on Port 3000 um but that's where we have open web UI right now so just running it on Port 3001 super easy addition and then setting up your environment variables is also very very easy you just take your env. example

**[0:05:05]** file in the repo rename it Tov like I dead here and then you can change any postgress settings that you want or leave these as the default and then for your n8n encryption stuff you can just have this be a random alpha numeric uh character set it doesn't really matter

**[0:05:19]** what you have here this is just for n8n under the hood and so once you have this renamed Tov you can go ahead and right away and run the last command here which is using docker compose to start this up and so I'll just paste this in here also

**[0:05:34]** by the way for Linux I believe it is Docker Dash compose so keep that in mind but Docker compose and then I'm running it with my Nvidia GPU there's also instructions for how to run this with mac and then if you're just running on the CPU if you don't have a powerful GPU

**[0:05:48]** for your local llms and so I'll run this right here it's going to spin it all up for me and so it's going to pull all of the images if I don't have them already and then once this is all done we'll go ahead and open up flow wise and n8n so

**[0:06:02]** let me pause and come back once this is installed all right once you have everything installed with the docker compost command you can go into your Docker desktop and see your compost stack right here with all of the services running we got n8n quadrant postest flow wise I'm not running open

**[0:06:18]** web UI right now because I'm not using it in this video I'm also going to be using the olama hosted on my computer so I don't have to reinstall my llms which is why I don't have that here as well but if you run that command I just gave

**[0:06:29]** you you'll have all all of that running here ready free to use in the browser and one thing I want to cover really quickly before I go into the browser is if you click on any of these containers here you get to see the logs in real time and you can go to the exact Tab and

**[0:06:44]** execute any commands within the image here and so there are just so many powerful tools for you right here to debug your containers in real time as you're building up your local AI stack so just wanted to call it out really quickly here because it's super important that you know how to get the

**[0:06:58]** visibility you need to really debug things as you are building and so with that we can go over into the browser here and yeah to access flow wise all you to do is just go to Local Host Port 3001 so you can reference your Docker compost file that I have in the repo to

**[0:07:14]** see what port you need to go to for each of the different services so it's 31 for flow wise for n8n it's Local Host Port 5678 for uh open web UI it's Port 3000 you get the idea just reference the docker compost file and So within flow wise right here I already have a chat

**[0:07:33]** flow that I've created but for this demonstration just to show you how easy it is to do everything I'm going to make my flow wise agent completely from scratch and so let's go ahead and dive right into doing that so as I build out this agent I'll cover other parts of the

**[0:07:47]** platform like tools credentials and variables but I want to Dive Right into setting up the chat flow and so we're going to do that the one thing that I'm not going to cover here is Agent flows this is a new beta feature Within flow wise a whole new level of agents that

**[0:08:02]** you can build within the platform but I do want to start pretty simple here so I'm going to go with the classic chat flow where you can still build really powerful AI agents and integrate with n8n like we are going to do and so the agent that we're going to build I'm

**[0:08:14]** going to do it completely from scratch just so you can see how easy it is to do we're going to give it the ability to search the web interact with NN workflows to create Google Docs summarize slack conversations send slack messages all that good stuff so let's go

**[0:08:27]** ahead click on add new and we have a blank slate here where we can now add in all these different components from Lang chain and right away you can see looking at just all the options that we have here for agents and for things like document loaders there's a lot here

**[0:08:43]** that's a bit harder to set up in n8n like I can just load right from the brav search API you can't do that in Ann without a good amount of work and I will say this is super important to know anything you can do inflow wise you can

**[0:08:55]** technically do in n8n that's why I still prefer n8n and like I I said I don't know if flow wise is the most production ready application but it's so easy to build things so fast and that's why flow wise is beautiful and so what we're going to do is start with our tool agent

**[0:09:11]** node and so if I just search for Tool we can see that we have this tool agent I'm going to drag this in and there we go and you can see it's like vector shift here where we just have to drag out to different nodes to connect all the

**[0:09:22]** things that we need for our agent and so really basic we can start with our memory here so if I Collapse the agents and tools and clear my search let's go down into the memory here so there's a lot of different options that we have here I'm going to start with something

**[0:09:38]** really basic I'm just going to go with buffer memory but you could also use postgress if you want to because that's a part of the local AI starter kit I'm just going to start simple and do this but just know that you can use the other things that we have in the local AI

**[0:09:50]** starter K which is the beauty of it so there's our buffer memory and now we want to use AMA for our chat model and so again super easy I had to search for that's it there we go we got our chatama model boom all right and then you can

**[0:10:05]** even set up a cache as well like look how easy it is just set up all these things I'm going to collapse this here and go down into uh the caching oh that's right up here so let me go to cache and then a lot of options for this

**[0:10:17]** as well so many things that yeah like setting up like a reddish cache just absolutely beautiful I'm going to stay simple here but reddish is probably what I'd recommend if you really want to build something uh robust but yeah I'll just use an inmemory cache for now and

**[0:10:29]** then then we get to set all the parameters that you'd want to set for olama so first of all we have our base URL here and the base URL it's a little tricky because it depends if you want to use olama running in the container for the local AI starter kit or if you want

**[0:10:45]** to use olama running on your own computer so right now for me I actually want to use olama running on my computer and the reason for that is I don't want to reinstall all the models that I have for olama on my computer in in my olama container in the starter kit and so the

**[0:11:03]** base URL when you are within the flow wise container pointing out to your computer it's host. doer. internal this is just standard Docker notation to reference the host machine I.E my computer that is currently running olama if you want to instead reference the olama instance running in the container

**[0:11:27]** you have to reference the container name that you just get from the docker compost file so the olama service that is in that Docker compose file that we run is just called ol so you would literally just replace local host or host. doer. internal with olama and then

**[0:11:43]** boom that references olama within the container so when I was covering the uh local AI starter kit in some other videos people were confused by that so that's this is how you reference your computer and then referencing the container name is how you reference the service running in there so super

**[0:11:58]** important I wanted to spend spent a minute just talking about that just that we're all on the same page there and then for the model name this is where I can reference like quen 2.5 coder 32b and the way that you get this name here is you just go into your terminal run

**[0:12:12]** the olama list command and this gives you all the models that you have installed with olama and I'm just taking quen 2.5 coder 32b which by the way this model has performed the best for me as an AI agent it's kind of funny that it's a coder model that I'm using not for coding but

**[0:12:28]** it actually does work the best which which is pretty interesting and I can adjust the temperature here to make it more deterministic by lowering the temperature going into additional parameters there's everything that you'd want to set up within ol llama one thing I'd recommend changing is the context

**[0:12:42]** window size because for some reason you can read it right here every single olama model defaults to 248 tokens for the window size so anything that is past that is going to be cut off from the current context in the call tolama which is pretty bad because if you have a

**[0:12:58]** longer conversation history or tools like web search that return a lot of text it's going to start to truncate what you send into the llm which is not good and so you want to Jack this number up something like 32,000 is what I typically do this the specifics of the

**[0:13:12]** number doesn't matter a ton just make that bigger otherwise your AMA models were will not perform very well they'll miss out on tool calls and hallucinate stuff so yeah very important to keep that in mind so we spent a good amount of time on the chat AMA node here but

**[0:13:26]** that one takes the longest because of everything we're setting up for um our model here and so I'll drag in the tool calling chat model into chat Lama here and boom we are connected all right and then the last thing we have to set up before we test out our agent for the

**[0:13:39]** first time is we have to give it a tool since it is a tool agent you can see with the red asteris here that the tools are required and so let's go ahead and add one of our tools and so what I'm going to start out with here we're not

**[0:13:51]** integrating with n8n yet that's going to come in a second I want to start out with a web search tool so I'm going to use the brave search API which I absolutely Ely love and so we're going to connect the tool here to the brave search API and then this is where we set

**[0:14:05]** up our first credential so in this case I already have credentials set up you can set these up outside of the workflow Builder as well there's a dedicated tab for that that I showed earlier um but you can also click on the drop down and click on create new here give it a name

**[0:14:20]** and then give it your Brave search API key and this is going to be save so you can use it within other workflows that you're building within flow wise as well and again dedicated place to manage that too so we now have the brave search API everything is developed here and we can

**[0:14:35]** test it out for the first time so I'm going to click on Save here and just call it my YouTube agent just give it a random name all right click save and then if I click on the chat icon in the top right here that's why I mve my face

**[0:14:48]** by the way so you can see the full uh chat widget here on the right side now I can test it out so I'll say um search the web and tell me Elon musk's Network all right so the kind of thing that I won't be able to get without actually

**[0:15:02]** searching the web because of the training cut off for these large language models and so it's going to take a little bit here because it is running quen 2.5 coder on my machine I can hear the fan spinning up right now that didn't actually take too long though but yeah as a November 2024 which

**[0:15:16]** is the current month his net worth is $348 billion so he's got a little bit of extra change to spare here and then also very neat within flow wise is it tells you the tool that it used so it told me use the brave search here is the input

**[0:15:32]** and then this is the output that was given to quen to actually get me the response here so absolutely beautiful now we get to finally integrate n8n with flow wise and we're going to do this through making n8n workflows as tools that we attach to our tools agent here

**[0:15:48]** just like we did with the brave search API so there's two parts to this first we have to create our 8 end workflows which are going to be our tools then we go back into flow wise and with some custom code I'll make this really easy for you don't worry we're going to

**[0:16:03]** create custom Tools in here that use API requests to our n8n workflows to use them as tools and so both of the n8n workflows and all of the flow wise custom tooling that's all going to be in the repositories let me show you right here so within our flow wise folder

**[0:16:22]** right here this is where we have the docker compost file for the local AI starter kit we have the Json for the whole chat flows you can can import it into your flow wise yourself and we have the Json for all the code for the custom tools that are making those API requests

**[0:16:37]** into n8n so if you get stuck on anything here just bring it in yourself I'm making this as easy as I can for you and then within our n8n tools workflow folder we have the Json for you to import all of the little tool workflows that we're going to be building right

**[0:16:50]** here and I'm not going to build those from scratch like I did with flow wise cuz I want to create and make this really nice and simple for you and so going over into our na n here is our first tool workflow and so because we're interacting with NN through API calls

**[0:17:06]** and flow wise we need to have a web hook trigger here and this is how all of our N8 and tools are going to start we just have a get or a post request depending on what we're doing and then I have just this test header authentication set up

**[0:17:19]** right here for my Bearer token you don't have to use authentication if you don't want but yeah there's a lot of other videos on my channel where I dive into setting up these kind of workflows so I'm not going to go into huge details here but just know that I have a web

**[0:17:33]** hook and then a respond to web hook for every single one of my n8n tools and this tool specifically it's just a basic one running a local host on my n8n instance in my local AI starter kit but I just query the tables that are in my postgress database that is also hosted

**[0:17:49]** locally so I have this all set up referencing the postgress service so I'm using the postgress database within my AI starter kit using the username password password and database that are all defined in myv file so I set this up as a nice simple tool to start just

**[0:18:06]** because it's showing using another service within the local AI starter kit so that's what we have on the n8n side make sure you have your workflow saved and that it's toggled to active as well so that we can use this production URL to call this API endpoint within flow

**[0:18:20]** wise and now back over to flow wise this is where we can bring in so if I search for Custom Tool we have a custom tool node right here and so I'll drag Dr this in and then for the tool that I want to select well first of all let me connect

**[0:18:33]** this here so tools goes to Custom Tool and the tool that I want to use here is get postgress tables so I already made this so once you select it that's the only thing you have to do here for configuration but if I go into to actually view the code for this here you

**[0:18:48]** give it a name and you give it a description and the description actually tells the large language model when to use this tool so it's super important to be descriptive here I could probably be more descriptive if I wanted to than just use this tool to get the procress

**[0:19:03]** table but this definitely will do for now and then for the input schema this is where you define all the properties that need to be given to the tool their type and their description again this is also used by the llm so it knows not just when to call the tool that's what

**[0:19:18]** the description is for but also how to call the tool these are the properties that it has to come up with a value for like the database name or when we get to slack what message to send all that is defined right here and then this is where we have the big scary code but

**[0:19:34]** don't worry it's very very simple it is extremely basic JavaScript just to make an API request to our n8n workflow this is the kind of thing that you could literally just use wind surf or go into 01 and just ask it to write this code for you very very basic there's a couple

**[0:19:51]** of things specific to flow wise like how you reference the input variables um and also how you work with your variables that you set outside of the platform but that's also very easy as well that's why these comments are here just to help you understand that so I have the workflow

**[0:20:07]** URL right here and you can see that it's referencing my NN container again go to your Docker compose file and see what is the name of my container for NN in this case it's just NN so I do that and then it's hosted on Port 5678 and so this is

**[0:20:23]** going to reference what we have right here with our locally hosted n8n in the local AI I starter kit and then the web hook URL that's just everything that we get right here if you click on production URL so keep in mind that n8n tells you to use Local Host right here

**[0:20:39]** for the URL but that's not actually right when you need one container to talk to another you have to reference the container name so I'm just hammering that in because that's the biggest confusion on my original video for the local AI starter kit and then the last thing that I want to cover right here is

**[0:20:56]** this variable that I have set up for the bearer token you you don't want this kind of thing hardcoded in your tool because then when you export your tool and share it with somebody else they're going to get your credential and so the way that we set that up let me save and

**[0:21:09]** exit here you just go into your variables right here and then you can set up any variable that you want so in this case I'm exposing my value right here because I'm just going to disable this once the video is done but you just add the name the type that it is and

**[0:21:24]** then the value and this is what would actually be my Bearer token right here and so once you set that up then you can go back into your flow right here go or go into your tool and then you can reference it just with the dollar sign vars do the name of your variable so

**[0:21:38]** that's how you set up custom things for credentials and stuff within flow wise and so now let me save this here and we can actually test it out so I'm going to go into my chat widget here I'm going to click on this button to completely clear the chat history and then I'll say uh

**[0:21:52]** what postgress tables do I have and so this is going to activate my workflow here so we can actually watch for this year if I go to executions right now we don't have an execution in the recent history but boom there we go we saw in real time there we go it

**[0:22:07]** returned all the tables that I have here and and now we're going to get a response from the large language model all right so there we go I called the function twice for some reason I'm not really sure why quen decided to do that you could even see that second execution

**[0:22:22]** pop up here but I got the right answer it pasted all the different tables that I have here and if I go into my workflow and look at the response there we go it concatenated all the table names together and that looks exactly right so there we go we are now interacting with

**[0:22:36]** NN for our first tool now let's set up a few more n8n workflows as tools just to really make this a robust agent I'm going to go through this one pretty quickly here because it's not the focus of the video all these different workflows but we're going to set this up

**[0:22:50]** nice and quick here so I'm going to add another Custom Tool like this all right boom and then the tool for this I want to summarize a slack conversation and so let me drag tools into Custom Tool I'll zoom in a little bit as well and then for this one

**[0:23:07]** again very very similar summarize a slack conversation give it a description an input schema we're just making this fetch request right here to our NN workflow this one I'm actually using a production NN instance that I have hosted with a real domain and the reason I have to do that I wish I could use my

**[0:23:24]** local AI starter kit NN for everything but it's not hosted with https and so you can't actually set up Google Drive and slack credentials when you are running just on Local Host so for the postgress tool I could but for all these other ones with Google Drive and slack I

**[0:23:41]** have to actually have a domain name so if you want to have it running entirely locally but using slack and Google Drive you need to have it hosted on a domain so keep that in mind I'm not going to go through that right now so that's why I'm

**[0:23:52]** just using what I have right here with my hosted n8n that I have hosted myself within digital ocean with with a domain name um so it still kind of is local in that extent where I'm not using n ncloud but anyway very similar workflow here we have a web hook and a respond to web

**[0:24:08]** hook I fetch messages from a slack conversation and I summarize them with a basic llm call to GPT 4 mini and then I get that response back and that is what I give to my agent here within flow wise so really really nice and simple that is tool number two and so now I'm going to

**[0:24:26]** add another Custom Tool here and this one is going going to be uh actually creating a Google doc and so this one very very similar document text and title for the properties here makes a post request to let's see that workflow right here just a single node sandwiched

**[0:24:41]** between the web hook and respond to web hook to create a Google drive file based on the text and the title that I gave through the AI so the AI agent determines both of these things right here so that is tool number three let's drag that in right here and then finally

**[0:24:58]** we're going to add a fourth tool here so we're really making this thing nice and robust all right so last tool here sending a message in slack so let's connect that here drag that in right here all right it's looking a little messy here I could probably organize

**[0:25:13]** this better but that's all good so let's zoom out a little bit all right and then yeah the what I want to do here is send a message through slack this one it just takes in the message and it calls my fourth workflow here which I'll show very quickly to send a a message and

**[0:25:29]** slack right now the channel is hardcoded just to flow wise n8n but you can make this another parameter where actually maybe the agent would fetch all the channels in your slack figure out the one to send it to get the ID for that and then pass that into this workflow as

**[0:25:43]** a second parameter along with the message so there's so many things you could do to make this even more robust I'm just keeping this simple right now now to actually test out this agent and push limits a little bit here let's have it do something that actually requires

**[0:25:55]** it to call multiple Tools in one request and so what I have right here I'll show my slack I have this very basic silly Conversation Set up where I said I'm doing some research on Elon Musk but having trouble finding his net worth just to have something for the llm to

**[0:26:10]** search the web for here and so now open up my chat window here and I'll paste in a question I have summarize the slack conversation and do some research on the problem given there so the goal here is to get it to call the summarize slack tool and then call the web research tool

**[0:26:24]** after and so one thing that I need to clarify here is the Channel that I want it to summarize so I'll give it the the channel and now since this is running locally it'll take a little bit for it to do everything so let me pause and come back once it has the answer for me

**[0:26:38]** all right there we go it called the summarize slack conversation and then it called the brave Search tool and this is looking great so yeah it's got some recent information that it wouldn't have if it was just going off of its training cut off looking really really nice and

**[0:26:52]** then yeah now I can ask it to do something else here so I'll say great now create a concise Google doc with your findings all right so just continue the conversation have it invoke more tools requiring it to reason even more about parameters for like the title of

**[0:27:07]** the document and the text to put in and stuff so yeah let me pause again and come back once it is done with this too nice all right that actually only took like 5 to 10 seconds I'm pretty impressed so it even gave me a link here which is super neat so let me copy this

**[0:27:19]** and then go into my other browser where I'm logged into this Google Drive specifically um and yeah let's open this up so I'm going to open a new tab paste this document in and there we go it uh did it in markdown which is pretty neat but yeah here's a very concise document

**[0:27:33]** outlining its research so this is working absolutely beautifully just so cool how we can integrate flow wise with NN together for all these tools and having even do some non-trivial stuff with input parameters and combining different tools together last step here let's have it send a slack message with

**[0:27:50]** this link and the summary of its findings so I'll say send a message in slack and the channel is hardcoded so I don't have to specify the channel here I'll just say send message in slack with this link and a summary of your findings all right let's see if it can do my

**[0:28:05]** final request here and boom there we go it sent the message in slack if I go to the execution history here for post message to slack you can see that we have our recent execution and uh we can see all the workflow status everything that happened within n8n and then when I

**[0:28:22]** go within my slack Channel let's check it out boom there we go here's a Google doc with all the information this is the right link looking good and it sends the summary this is exactly what I told to do this is working perfect and it's just a beautiful demonstration of how you can

**[0:28:35]** use n8n and flow wise together to build some awesome agents and prototype really really fast I hope that just like me you can see the value of using flow wise in N8 end together to create some really powerful AI agents in the blink of an eye that's why I added it to the local

**[0:28:50]** AI starter kit which by the way a lot more content coming on the local AI starter kit very soon here and if you have some ideas of what you think should be added to the package next please let me know in the comments below if you appreciated this content and you're

**[0:29:04]** looking forward to more things local AI I would really appreciate a like and a subscribe and with that I will see you in the next video
