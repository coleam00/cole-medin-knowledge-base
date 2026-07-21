---
type: raw-transcript
title: "Pydantic AI + DeepSeek V3 - The BEST AI Agent Combo"
youtube_id: zf_D2Eafvk0
url: https://www.youtube.com/watch?v=zf_D2Eafvk0
slug: pydantic-ai-deepseek-v3-the-best-ai-agent-combo
published: 2025-01-05
duration: "0:29:21"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I get asked all of the time how I build my fullscale AI agents so I recently started an exciting minseries where I'm showing you my entire process so far you see me go from the planning phase all the way to prototyping a full AI agent with n8n which I did in my recent live

**[0:00:18]** stream now in this video the third one in the series I'm going to take this n8n prototype and turn it into a full production ready python agent with pantic AI which is my absolute favorite framework for building agents right now plus we're going to use the new deep

**[0:00:34]** seek V3 large language model through open router so we can make our agent super powerful and still dirt cheap and I'll even show you how to use other llms as well through open router because you definitely don't want to be tied down to just one here is the best part if you

**[0:00:49]** followed along with the n8n live stream or you just saw the end result the exact same structure that we use there for our agent is going to guide our coding process today making everything that we do right now surprisingly straightforward I hope it makes it very very obvious why I bothered to even

**[0:01:05]** prototype with n8n in the first place and also don't worry if you missed a live stream or if you just don't care about making an agent with NN you can definitely treat this video as a standalone guide to building a powerful agent with pantic AI if anything it

**[0:01:20]** actually just helps a lot to have the NN workflow as a visual reference for what we are building to make things Crystal Clear it's pretty neat by the end of this video you're going to have a full fully customized agent that's capable of consuming entire GitHub repositories for

**[0:01:35]** code Q&A and it's ready to grow into a truly production grade agent through the rest of the series so right now I'm going to start by quickly reviewing where we are at in my AI agent road map and the NN prototype that's going to guide what we code today then we'll take

**[0:01:51]** the n8n agent as a blueprint along with an AI coding assistant to make creating an AI agent with custom code right now super super easy so let's go ahead and dive right into how easy it can be to build an agent with pantic AI all right so here we are in the AI agent road map

**[0:02:07]** that I showcased a lot in the first video in this series and so right now let's talk about where we are at in the process so the first step is to plan our agent and that's what I covered a lot in the first video where I talked about

**[0:02:20]** what we actually want for our GitHub code Q&A agent and then in the live stream I went through prototyping an agent with n8n which really is just important to choose some no/ L code tool to build something fast and so there's other good options as well like voice

**[0:02:36]** flow and flow wise and it's really important to note here I want to pause and just say this you don't always have to transition from a no code tool to custom coding your agent like I am doing in this video I just often find that it's necessary for me to do that because

**[0:02:52]** of the amount of control and customization I get when I have all of the code for my agent and so that's why what I'm doing is transition positioning right now to using pantic Ai and then we also covered in the live stream a little bit of Step number three which is

**[0:03:07]** getting your database set up we set up super base to manage the table for all of our messages that were being created by our NN AI agent and so right now in this video we're not going to focus on the database too much but we're definitely going to once we get a

**[0:03:20]** front-end set up because we're going to have to have that database to connect the front end to our agent but right now we're really going to focus a lot on step number four this is where we right now this is what the video right now is going to cover which is moving our n8n

**[0:03:35]** prototype over to python using pantic AI there are a lot of other good Frameworks out there as well like llama index crew Ai and Lang chain so many options pantic AI is my favorite right now but all the concepts I'm going to be talking about here are really going to apply no matter

**[0:03:51]** which framework you're using cuz we're going to talk about best practices for building agents and managing conversation history and your API keys and all the tools for your agent so a lot of this is going to carry over no matter which framework you choose to do and so with that let's dive into our NN

**[0:04:07]** prototype and have that guide us into building our agent with pantic AI so here we have the full prototyped AI agent with n8n that I made in my last live stream which was the second part of this series now I don't want this to be a whole another n8n tutorial I just want

**[0:04:23]** to show this workflow again because it's a visual representation like I already said of what we're going to make in pantic AI and it actually just makes it so much easier to code the agent when we have the structure for it defined in a no code tool already I mean the biggest

**[0:04:38]** thing that you can do to help you tackle complex problems is break them up into smaller steps so if we have one step to create a proof of concept with an easy tool like n8n and then the second step to actually code it with pantic AI That's just breaking a complex problem

**[0:04:53]** like it's very obvious how it helps and also we can even download this workflow Json so I click download right here I can take a Json representation of this workflow and give it to an AI coding assistant like wind surf or cursor so it also has a good understanding of what it

**[0:05:09]** needs to build for me so there's even a second reason to start with a no code tool and then transition to coding and so I'm going to as I'm building my agent with pantic AI reference the parts of this workflow for a visual representation that connect to what I'm

**[0:05:24]** doing in my python code and so yeah for this workflow right here just a super quick overview we have this chat trigger right here which is what we use to actually interact with our agent in the live stream and then we have this AI agent node this is what does most of the

**[0:05:40]** work for the Prototype we've got our system message here which I'm going to have to copy that into pantic AI we're using Gemini 2.0 flash for our large language model which is going to be deep seek V3 now but you could still use Gemini 2.0 flash we're just using the

**[0:05:55]** basic window buffer memory for conversation history management and then we have our two tools here that we're going to have to build in pantic AI as well we have one tool which is this flow right here this is what gets the structure of a GitHub repository for the

**[0:06:11]** agent to know what files are there and then the second tool right here is used to get the contents of a specific file and so there's a lot of intelligent processing with this agent where it has to know okay if I'm going to get the contents of this file I need to first

**[0:06:25]** get the structure of the repo to know where all the files are then pick out the one I need to analyze get the contents of it and then get the answer for the user and so there's a lot of calling multiple tools allinone just to answer a single user question so it's

**[0:06:39]** definitely an agent in that sense where it has to do a lot of intelligent thinking even to answer more basic questions in a geub repository one other super important thing to call out that I did in the live stream is I took the NN prototype and turned it into this which

**[0:06:53]** is the same agent but compatible with the automator live agent Studio which is the platform that I've been develing V oping to be an open- Source community of developers creating AI agents and sharing them on a single unified platform and so I'm going to have a link to this in the description as well it's

**[0:07:10]** a great reference for you to know how to build an NN agent for the live agent studio and the hackathon competition that I've got going on right now for the month of January and so yeah this is everything that we got for n8n now on to building with pantic AI so here we are

**[0:07:26]** at the documentation for pantic AI and this is going to be a crucial resource for us because this is everything we need to create our agents with pantic and the other thing is AI coding assistant like wind Surf and cursor in general don't know these Frameworks very well like pantic AI or Lang chain crew

**[0:07:44]** AI llama index you name it they just don't really have that knowledge and so typically I'll reference the documentation like this very closely as I'm building my agent and then the tools that I create for my agents that's when I'll use an AI coding assistant so I'll talk more about that later as well but

**[0:08:00]** luckily the documentation for pantic AI is incredible it's so clear they've got everything you need to get started segmented really really well so you can dive into building your agents they've got really nice examples you can dive into your models and how to set up things also like overriding the base URL

**[0:08:17]** and that's how we're going to use open router later on with the Deep seek V3 and then they got really awesome examples as well so like this weather agent right here is a really clean example of how to build your agents with pantic AI and generally when you set up

**[0:08:31]** your agent there's three big things that you need to care about first of all is your dependencies for the agent this is things like the HTTP client or API keys that your agent needs when it is invoking tools and so you define that all here and then pass them into the

**[0:08:46]** agent when you execute it and then the second thing is you define your agent itself which is where you specify things like the system prompt and also the model you want to use like deep seek V3 in our case for this video and then the last thing is setting up the tools for

**[0:09:00]** your agent and pantic AI makes it so easy to do this compared to a lot of other Frameworks that I've seen is all you have to do is Define a regular python function that has arguments U everything that you typically have in a python function but you add this

**[0:09:15]** decorator at the top a decorator is just a thing in Python where you put this line above a function with an at symbol and then for pantic here it's just the name of the agent. tool and that instantly turns this function into one of the tools available to the large

**[0:09:29]** language model and you use this doc string here this comment at the top of the function to tell the large language model when and how to use this tool so the arguments to the function what its purpose is everything you need to know to use this tool correctly and do that

**[0:09:44]** for each one of the tools that you want and we'll see that in a little bit as well for our agent so so easy to set up and then in the main function you just have to set up your dependencies execute your agent passing in any conversation history and the current user prompt and

**[0:09:59]** then you get a resp resp and you can print that out so so simple to get started and then the other thing that I want to mention is if you head on over to the automator live agent Studio studio. automator doai which I'll link in the description you can try the n8n

**[0:10:14]** Prototype version of what we're going to build instantly right now you have to install nothing yourself that's the convenience of it and what I want to do with all my guides going forward is have these agents that I'm building available for you to try right away so you can try

**[0:10:26]** it here on the automator live agent studio and then also what we're about to be building so I'm going into my code editor here is also available for you to download so there's going to be another link to the GitHub repository where you can download all this so you can try it

**[0:10:40]** right away on the studio or download everything we're going to build right now yourself and then I've got this read me to help you install and run everything so it's got instructions for getting the python packages installed and so you can have the exact same environment as me and then also setting

**[0:10:54]** up your environment variables like your open router API key and the large language model you want to use which by by the way this is how you can use any large language model you want for the agent that we're about to build and then also setting up your GitHub token

**[0:11:07]** obviously you're going to need that to access the GitHub API for your agent to invoke the tools to do things like analyze a GitHub repo and look at the specific content of files so that's everything we got now we can go ahead and go to our Blank Slate here and start

**[0:11:22]** building our pantic agent all right so the first thing that we want to do for our agent you always start out your Python scripts with importing all of the pack packages that you need so this is everything that we've got all from the requirements. text file so if you

**[0:11:34]** install it this way you'll have this all available and then we can load the environment variables that we need so again that's going to be our open router API key the specific large language model from open router that we want to use and our GitHub access token and then

**[0:11:48]** with that we can pull the llm that we're looking to use with a default value of the deep seek V3 and then we'll set up our model this is using an instance of open AI model from pantic but we are overriding iding the base URL and API key to use open router so instead of

**[0:12:03]** going to open AI it'll go to open router and that's how we can use deep seek V3 there and you could change llm model to be gemini or Claude or quen or mistol whatever you want you can set that super easily here and it's going to work instantly no matter the model that you

**[0:12:18]** want so we're using deep seek cuz it's a cool large language model but if you prefer something else you don't like deep seek whatever it is you just change it so easily and so that is setting up our model and then we have the first part of building our pantic agents that

**[0:12:31]** I referenced earlier and that is setting up our dependencies and so in this case our agent needs an HTTP client to interact with the GitHub API and it also needs the GitHub token so that it has the authorization to make calls to the G of API to do things with the public

**[0:12:47]** repositories that we give links to for our agent and then with that we can move on to the second part of our agent which is creating the actual agent instance and so the first thing we want to do is Define the system prompt for our agent and that I am taking directly from our

**[0:13:05]** n8n prototype right here so if you click into the agent node and you go into the system message I'm copying this word for word no reason to reinvent the wheel here that's one of the reasons I built a prototype is just to make it so there's less work for me when I actually code

**[0:13:20]** things just to keep my head clear and so I'm not doing too many things at once when I am creating the code for my agent so don't even have to think about the system prompt already got that covered from the Prototype and so now I can Define the actual instance of my agent

**[0:13:34]** using the agent class from pantic and so I pass in the model which is what I have set up right here pointing to open router with deep seek V3 I give it my system prompt the dependencies that I'm expecting the agent to receive when we execute it and then finally there's also

**[0:13:50]** retry logic baked into pantic AI as well which is super neat because a lot of times you get random uh you know like rate limit errors when you try to call llms and so this kind of Tri logic is super helpful as well so that is everything for our agent we've already

**[0:14:04]** done the first step of setting up our dependencies defining those and our second step of creating our agent and so now we can already go into defining our tools which is the last step for creating our pantic AI agent and again the way that you do that is just with

**[0:14:19]** this python decorator just like the example showed in the pantic AI documentation so I'm saying my GitHub agent. tool and now this function is going to be one of the tools available to it and I have this dock string right here this common that again tells the large language model when to use this

**[0:14:36]** tool like we give the purpose right here that tells it when and then also how to use this tool what are the arguments that it actually expects here and one pro tip that I've got for you that I already alluded to is that it's super helpful to use an AI coding assistant to

**[0:14:51]** create these tools while they don't really know the ins and outs of pantic AI and other agent Frameworks to set up this part of it when it comes to the tools and using really wellestablished apis like the GitHub API AI coding assistants absolutely knock it out of the park and the other thing you can do

**[0:15:09]** is you can go to your prototype your n8n workflow click on the three dots in the top right here and download it so this will download a Json representation a text representation of this workflow and you can just go into a conversation with wind surf or your favorite IDE paste in

**[0:15:25]** the Json here and then you can say uh build out and then you can give the name of the function uh and then because you've already given the arguments here and your doc string telling when and how to use this function you don't actually have to specify too much for it to know

**[0:15:41]** what to build because it has this as a reference it has the NN workflow as a reference so it knows what part of this workflow is the tool you're trying to build it's so easy like obviously this is super super crude you're going to want to at least give you know like a

**[0:15:55]** paragraph or two describing what exactly you're looking for just so it can connect the dots with the workflow you're giving it but yeah in general using AI coding assistant to make these tools is amazing that's what I did for these tools like all the code that I'm about to show you here I did not make

**[0:16:08]** myself I used wind surf to do it and you could do it just as easily in cursor um or ater like whatever whatever AI coding assistant you want to use I just happen to be using wind surf right now and so yeah super basic what we're going to do

**[0:16:22]** here is first of all we're going to use this regular expression that we used in n8n so again nothing new here just going off my prototype we're using this regular expression to extract the organization and repository from our GitHub repo URL and so we get the owner and repo just like we do in n8n and now

**[0:16:43]** we make the request so we have the headers here where we have our GitHub access token we make the request to the GitHub API and if it fails to get the information of the repo then we tell it hey fail to get the repo info that way the llm can tell the user that it failed

**[0:17:00]** to use the tool otherwise we're going to get the size of the repository and we're going to return all this information so this is actually a tool that we don't have in the n8n Prototype because right now our n8n prototype is able to get the repository structure and get the

**[0:17:15]** contents of individual files and we're going to add those as well we also have this third tool that I'm starting off with here to get the metadata of the repository which is super useful because now a user can give a link to a repo and ask the agent what is the size of this

**[0:17:29]** repo or how many files are there how many stars does it have and it'll have all that information now which is super cool and so that is our first tool and now defining the second tool it's going to look very very similar in fact there's a lot of redundant code that I

**[0:17:41]** have here just to make it very clear how each of these tools work independently and so now we have this next tool which is to get the repo structure so this going back to our prototype is following this path right here so again we need to extract the organization and repo from

**[0:17:58]** our URL and then we need to make this specific call to the GitHub API to get the contents of the main branch and so let's go back and actually do that so we have again another doc string saying when and how to use this function and then we get the owner and repo again

**[0:18:14]** it's a little bit of redundant code I probably could make a separate function and do this but I just want to make it very clear for each tool what is happening and then we make another request so I'm making a call this is exactly what we have in n8n looking at

**[0:18:26]** the main branch of this repo and actually if it fails to fetch from the main branch I even have this backup here where it goes to the master Branch so we're already starting to see some functionality that I didn't have in my prototype CU right now it only looks at

**[0:18:40]** the main branch it doesn't go to the master Branch as a backup but we do that here and so we're getting the content of the repository and then at the end of the tool here we're just structuring it to look really nice and so for all the folders and files we're bringing this

**[0:18:54]** all together into a single large string to return to the large language model so it now has the context of the structure of the repository and actually what that looks like here I'll give you an example from the Prototype again this is just the beauty of the Prototype is it gives

**[0:19:08]** us this visual representation we can get a look at what's already happening under the hood with the Prototype that we're also doing with pantic AI and so because the the new lines aren't actually rendered out here it looks kind of Jank but it this is describing all of the

**[0:19:21]** folders and files it includes all the nested folders and files as well this is the entire structure of the repository which by the way way I believe this is the I actually don't know which repo this is I think I'm looking at someone else using it on the studio so I don't

**[0:19:36]** actually know what repo this is but anyway that's the structure that is produced by this tool right here and then finally we just return it and so now it's just a massive string describing the repo structure to the the uh large language model and so now we have our last tool here which is to get

**[0:19:51]** the content of a specific file and so now going back to the Prototype that's this Branch right here so again we need to extract the owner and the repo or the org in the repo rather and then make this request right here to get the contents of a specific file that the

**[0:20:06]** large language model passes as one of the parameters so we have the GitHub URL as a parameter and now the file path as well and so again we got a doc string here describing the when and how we're getting the owner in repo and then we're making them request this time to this

**[0:20:22]** endpoint of the GitHub API where we give the specific file path that we want the contents of and again we go check the master bre Branch if the main branch fails as a backup and then all we have to do is return response. text cuz the response is going to contain the object

**[0:20:37]** which which is the file from GitHub and so we just return the text of that and that is it so so easy we now have completely created a pantic AI version of the Prototype here that we have in n8n and we even added in another tool and some other features here that it

**[0:20:54]** didn't have and so starting with the Prototype and also again using an AI coding assistant to help you with these tools it just makes it so easy even if you're not a super technical person you can build up these agents so so easily and so now the last thing that we have

**[0:21:08]** to do we're not focusing on the front end in this video that's going to be the next video in the series but I still want to create a little CI a command line interface so that we can work with our model with our agent in the uh command terminal right here and so let's

**[0:21:22]** build that right now okay so to make the CLI here it's just going to be like 50 lines of code super super basic it's nothing that we're really going to keep going into production it's just a simple way to interact with our agent for now so again we're going to start by

**[0:21:35]** importing everything that we need for our CLI including the GitHub agent right here so what we just built here we're importing into the CLI to use then we'll load our environment variables and then also we have log fire which is the monitoring baked into pantic AI I'm just

**[0:21:51]** configuring to not use it for now uh and then we'll set that up later in a different part of the series when we dive into monitoring for our agents and now I'll Define a CLI class which is going to initialize the dependencies that we want for our agent including the

**[0:22:06]** GitHub token that we get from the environment variable and then we have this function here to chat and so this is just going to be interacting in the terminal so just this right here and so it's going to ask the user to enter the message and then it's going to be this

**[0:22:19]** infinite Loop here of asking for a message and then calling the large language model our pantic AI agent and so we get the input from the user and then we just run the agents so we have the dependencies that we set up right here in the initialization function for

**[0:22:35]** the CLI class we have the user input which is what I typed into the terminal and then we're also keeping track of the messages as well so I want to as the message history send everything in except for the very last message which is going to be the latest message from

**[0:22:50]** the user and then we are going to take in this is kind of the the last part of the function that's a little bit more complicated because the results that we get here and here I'll even show this in the pantic AI documentation if I go to function calling or function tools here

**[0:23:08]** and I look at this let me scroll down a little bit when I get the messages from the result of calling the large language model it includes everything including all of the tool calls so when it decides to look at a GitHub repository the conversation history is going to include

**[0:23:25]** the lm's request to look at the GitHub repository and the conversation will also include the response from calling that tool that python function so you're going to have like hey I want to look at the repo and then the tool saying hey here's the structure of the repo all of

**[0:23:41]** that information is going to be included in the conversation history and so I'm taking out all user and AI messages so I'm just getting the tool calls here and I want to include that in the conversation history as well and the reason I want to do that is when the llm

**[0:23:57]** decides to look up something like the repo structure we don't want it to have to do so again later on in the conversation it can just reference what was already returned to it when it called it for the first time and so it's important to have that as a part of the

**[0:24:11]** conversation history and then finally we print out the response from the AI uh from our agent and then optionally we can also print the tool calls as well I have that commented out right now but we can also get a little insight into what tool calls are being made the exact

**[0:24:26]** arguments and what was returned but right now I'm just going to keep simple input the result from the agent like what it actually says and then finally we will add the message from the llm into the conversation history so super super simple and then at the end we'll

**[0:24:41]** close the HTTP client as well and then the very last thing I have to do is just set up my main function here where I'm creating an instance of the CLI class and then running the chat which is that infinite Loop of getting the response or the input from the user and then the

**[0:24:55]** response from the agent until finally they type in quit and so that's it super super easy and I also have a comment here with a repository I'm just using bolt. DIY that's our open source AI coding assistant that I built a whole Community around we're doing awesome with it so I'm just using this as an

**[0:25:12]** example here as a repo to chat with the agent about and so I'm going to save this here and then open up my terminal here so I have my directory set to where I have these two files right here and then I'm just going to say Python and

**[0:25:26]** then C.P super super easy easy and so now it's going to give me a couple of warnings here you can ignore these no big deal and so now we say GitHub agent CLI enter your message and so I'm going to say uh describe this repo and then I'll paste

**[0:25:42]** in the bolt. DIY repo and then we're going to get some debug messages here in the terminal that's actually telling us the steps that the agent is deciding to take so first of all we accept the request and then here I can even zoom in a little bit here just to make this

**[0:25:56]** easier we accept the request and then we get the repository information and the repo structure and then I'm not totally sure why but the llm also decided to get the information for the repo a second time not really sure why it did that but we get an insight into what it is

**[0:26:11]** deciding to do here and then it gives me the full response here so it says using this repository here is everything that you need to know about the uh bolt. DIY repo so looks pretty good cool so now I can ask another question like um describe the em. example file in one

**[0:26:31]** line so now I want to actually go and look at a specific file in the repository and because it already called the tool to get the repo structure it doesn't have to do so again to know where the env. example file is and so it goes right away into running the tool to

**[0:26:47]** get the file content and so it just says that it's a template for setting environment variables required for all the API keys for llms and base URLs which is totally right and I can even ask another question on this file like what is the first API key and because

**[0:27:01]** there's conversation history it knows that I'm talking about the EnV file specifically and there we go the first uh API key is the grock API key which if you go into the bolt. DIY repo and you look at em. example I know this is the right answer the grock API key is the

**[0:27:17]** first one that's set there in env. example so there we go and this is all using deep seek V3 and it's so easy I can just go back here and the llm model if I go to mymv file which I'm I'm just going to show the example I obviously

**[0:27:30]** don't want to show mine with my uh open outer API key but I could change this if it was originally uh deep seek SL deep seek chat I could change this to GPT 40 and then boom I'm instantly using GPT like it's so easy to change the model as

**[0:27:44]** well so don't think that you're tied to a specific model and also it's important to note like you're not tied to a specific framework either like you don't have to use pantic AI to build this it's going to look quite similar to build something with laying chain or crew AI I

**[0:27:58]** just prefer pantic overall because of how easy it is to set up my agents and it still gives me all the control I need with things like setting up parameters like the base URL and defining all the context for my functions for my tools like it has everything that I need but

**[0:28:13]** the general practices here are going to apply to any framework that you use in general so I hope that you found this super helpful again this is all going to be linked in the repo and that is what we've got for our GitHub agent so there you have it a powerful custom coded AI

**[0:28:27]** agent built with pantic AI I and deep seek V3 and we started with just a simple concept build an agent that can consume entire GitHub repositories for code Q&A and we took it from concept to n8n Prototype all the way to a fullscale pantic AI agent built in Python and so

**[0:28:45]** right now we have a solid foundation of an AI agent that's flexible powerful and affordable and of course our journey does not stop here in the next couple of videos I'll walk you through building our agent into a front end so we actually have an interface to work with

**[0:28:59]** our agent and then for the rest of the series we'll be adding on some more functionality and features to truly make the agent fit our needs and then we'll go into deploying it into production so if you appreciated this video and this Series has already taught you a lot

**[0:29:13]** about building AI agents I would really appreciate a like and a subscribe and with that I will see you in the next video
