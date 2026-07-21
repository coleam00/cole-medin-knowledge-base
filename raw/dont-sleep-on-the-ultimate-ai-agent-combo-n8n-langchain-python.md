---
type: raw-transcript
title: "Don't Sleep on the ULTIMATE AI Agent Combo (n8n, LangChain, Python)"
youtube_id: 8hAMASB-RpM
url: https://www.youtube.com/watch?v=8hAMASB-RpM
slug: dont-sleep-on-the-ultimate-ai-agent-combo-n8n-langchain-python
published: 2024-09-22
duration: "0:24:58"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** AI is single-handedly making this decade one that is going to go down in history at this point that isn't even Up For Debate and one huge part of that is AI agents which are large language models that are able to interact the outside world through apis web scraping code

**[0:00:16]** generation and the list goes on there are a million different ways to build AI agents both with code and no code Solutions and there are really good arguments to go both ways on the one hand no code Solutions like flow wise and n8n make it so incredibly easy to

**[0:00:33]** build powerful AI agents without having to debug and maintain a bunch of code on the other hand coding your own AI agents with languages like Python and libraries like Lang chain give you all the customization and control you could possibly need and sometimes no code tools just don't offer that a lot of

**[0:00:50]** times you have to code your own AI agents for production because no code Solutions often times aren't feature Rich enough when your requirements start to get really specific and so a lot of times people will start with no code and then move away from it out of necessity

**[0:01:05]** however I have actually found the perfect trifecta that actually combines code and no code to give you the best of both worlds quick and easy to develop AI agents that are still extremely powerful and able to meet any of your needs what's the secret here it's using n8n

**[0:01:21]** for the Asian tools and then python plus Lang chain for the AI agent itself I am obsessed with this combination because it really does leverage the strengths of code and no code so well all right just hear me out on this n8n makes it so easy to set up credentials for your services

**[0:01:38]** and then connect them all together in workflows that you can actually create as API endpoints for your agents and then python plus Lang chain allows you to create AI agents really easily with any llm that you choose and very few lines of code and then you can hook into

**[0:01:53]** your N8 end workflows in like five lines of code and then create custom Tools in Python for anything that maybe you couldn't do an n8n so it is just the perfect combination and if you can't see the beauty of it at this point I don't know what to tell you so I'm going to

**[0:02:07]** walk you step by step through how to set up this kind of agent with a fun and practical example that I've created for you and we'll even test it out at the end to see how well it does my goal by the end of this video is to have you

**[0:02:19]** convinced that this is the way to build your AI agents all right so since we are combining code and no code for this AI agent there's going to be two main parts to what I'm walking through here first is going to be the n8n workflows that give us the tools to interact with

**[0:02:34]** services like slack and Google Drive and then in the second half I'll walk you through coding the agent with python and langing chain and actually integrating with the NN workflows to bring everything together so what this AI agent is going to be able to do is send messages in slack summarize

**[0:02:51]** conversations in slack and upload files to Google Drive just a few simple example tools that I put together here for this agent to make something simple and still pretty practical but what I really want to drive across here as the main point is that you can extend this

**[0:03:07]** to anything because the sky is the limit with what workflows you can create in n8n and integrate into this agent and so just think of what you want to make and then as I'm walking you through this think about how you could so easily just do that with what I'm setting up here so

**[0:03:20]** the first thing I want to do is quickly walk you through the three N8 end workflows that I'll be using for tools for our AI agent that we're making with python and langing chain now I'm not going to cover how to set up NN or how to set up each of these workflows in

**[0:03:34]** great detail because the main thing that I want to cover here is how exactly you can use NN workflows as Tools in a python plus Lang chain agent I don't want to spend all the time boring you with the details of setting up these workflows right now but I have a lot of

**[0:03:49]** other videos on my channel and there are a lot of other resources on YouTube for actually setting up NN and getting into the nitty-gritty details of making these workflows and so again this is just going to be a highl level overview but I want to show you what we are actually

**[0:04:02]** doing for these tools so the first tool that I have here is one to summarize a slack conversation and so it starts with a web hook because there's going to be a URL that we invoke within our python code to make this tool call and with this request here it's going to go in to

**[0:04:21]** basically just pull a bunch of slack messages from a specific Channel that I have referenced here and you could make this Dynamic if you were to extend the agent and have it actually like look up Channel IDs and then pass one in to fetch messages from a specific Channel

**[0:04:36]** but just to keep it simple here I have the channel hardcoded and so going over to this little test slack workspace that I have created here this is what I have for my demo here so I just have this little conversation that I made with myself as an example it's just somebody

**[0:04:51]** that is planning a new startup for AI pets and they're trying to figure out their text stack so this is what I've got for a little nine message conversation here something that we'll be summarizing and so I pull all those messages I aggregate them all together into a single field and then I can pass

**[0:05:08]** that into my large language model with a prompt telling it to summarize this conversation so I dynamically pass in the combined list of messages from slack telling the llm to summarize it and then for my model here I'm just going to be using GPT 40 mini and then once I get

**[0:05:27]** that response from the llm with the summary I resp on to the web hook with that item and so now I'm go I go back to the python code with that summarization and then my agent can do whatever it wants to do with that summary so that is

**[0:05:42]** the first tool that we have here for slack the next tool that I want to cover really quickly here is the one to post a message to slack now this one is even simpler than the other one because there's really just one action that we want to do here to make the message and

**[0:05:56]** slack and so of course we want to start and end with the web host again because we want to again call this URL within our python code to invoke this tool to send a message to slack and So within our python code will have a function that'll accept an argument of the

**[0:06:12]** message text to send and then it'll invoke this web hook with that as part of the payload so that we have the text we actually want to send into the slack Channel and so we have that dynamically referenced here and the message text attribute of this node to send a slack

**[0:06:28]** message again I have the channel hardcoded here you could make this Dynamic if you want with another tool to look up Channel IDs in the slack workspace but I'm just keeping it simple here the other thing that I wanted to quickly mention here just like a a really neat little Golden Nugget to save

**[0:06:43]** you some time setting up the slack credentials is a little bit trickier in NN than some of the other credentials it's still easy overall because NN makes it super clean to do everything it provides you documentation um but keep in mind that when you go into their documentation for setting up the

**[0:07:00]** credentials they reference the navigation in kind of a strange way that didn't quite make sense to me um and so let me find this here yeah so it'll tell you to like go to add features and functionality and select permissions that doesn't seem to actually exist if you go into api. slack.com where you

**[0:07:19]** need to go to set up your slack app to get the credentials to put into n8n to get to permissions you actually want to go to ooth and permissions so once you are there that's where you'll see the redirect UR URL that n8n asks from you to get from slack and then also for the

**[0:07:34]** Scopes here let me just scroll on the bottom I was playing around with a lot here when it tells you it needs certain Scopes you'll run the workflow and you'll get errors when those Scopes aren't set up um but in your user token Scopes here you can just set these are

**[0:07:46]** the ones that you typically will need to actually read messages so when like you're summarizing the conversation with that other workflow these are the ones you need and then I think there might be some other ones you have to set up for sending messages but anyway this is

**[0:07:58]** where you do all of that so just keep that in mind just a little bit of a golden nugget for you there um so back to the workflow here I've got my credential set up already of course um and then yeah just the last thing respond to the web hook

**[0:08:10]** with that incoming item so basically the result of sending the slack message so the third and final tool that we have here is for creating a file in Google Drive specifically a Google doc now this tool is really simple just like the last one a single action that we have here to

**[0:08:26]** create a file in Google Drive so we have a couple of parameters that are coming in from the API call which is basically just the name of the file and the text to put in it and then I'm hardcoding the folder that I'm going to upload to Google Drive just to this meeting notes

**[0:08:41]** folder that I've kind of been playing around with with other videos on my channel and then lastly one really important thing is in the extra options here I added this toggle to convert to a Google Document otherwise the text that I upload Google Drive will just be put

**[0:08:54]** in a raw. txt file and I like Google Docs I just want it to look really nice and so that's why I did that and so then everything else with the web hooks is exactly the same and that is this workflow you can see here how once you

**[0:09:06]** kind of get it down with how the web hooks work and what actions you want in the N workflows it is so so easy to set up any tool that you want for your Python and Lang chain code and speaking of that we can dive into that now and

**[0:09:19]** actually start using these workflows for our agent now for my favorite part we get to code the AI agent with python and Lang chain and interact with our n8n workflows really quick before I get started I'm going to have a link in the description of this video to a GitHub

**[0:09:33]** repository where you can find all of the code that we're about to create here if you want to quickly snag that for yourself and implement it but right now I'm going to walk you through step by step creating all of this code for interacting with n8n building our AI

**[0:09:47]** agent all that good stuff you can see right here I just had the skeleton for a main function in my main python script and then I have this other blank python script where we'll be creating all the tools to interact with the n8n API endpoints also with all the code in the

**[0:10:03]** GitHub repository is also a requirements. text file so you can see the python packages and their versions to have the exact same environment as me and then also a env. example file that you fill out with your own credentials like things for your your anthropic or open a API Keys all of your production

**[0:10:21]** NN web hook URLs that we went over earlier and then also when you set up the authorization on your NN web hooks you're going to have a ER token I have instructions on how to create that as well within n8n you're going to want to get all that set up in here rename this

**[0:10:36]** file Tov and then you'll be set up with the exact same environment as me so now we can actually create our agent tools that will interact with our n8n API endpoints and I'll start within this utility python script for defining the tools by importing all the packages that

**[0:10:51]** I need things like EnV and then also the tool utility from Lang chain which is a function decorator that actually makes it so that functions we Define here can be used as tools that we bind into our agent next up I'm going to load the environment variables and then bring in

**[0:11:07]** everything that I need for n8n including that Bearer token that'll have as my authorization header you set that up in n8n and then also the three production URLs that we need here to call each of the web hooks for those different n8n workflows next up I have a little helper

**[0:11:23]** function here and this is probably the neatest part of this whole setup because it makes it very easy easy to create as many tools as you possibly want because all of them are going to leverage this function that makes it super clean to make these API requests to the n8n

**[0:11:40]** workflows and so the first thing that I do here is I have all my parameters defined things like the method which is either going to be a get or a post depending on the type of operation the URL which is the n8n workflow URL and then the function name because this is

**[0:11:56]** going to basically be how the AI knows which tool it's actually invoking and then optionally a payload like if you have to pass in something like the message you want to send in slack the actual text for that and so with that we'll Define our headers which includes

**[0:12:11]** our Bearer token that we need otherwise n8n will reject this API call and then we can try to make this request and so this supports both get requests and post requests with a payload we have both between our different workloads that we have in n8n and then if we get a success

**[0:12:29]** will call to the API endpoint we will raise for status in case there's like a forbidden 4 or3 error and then we'll return the response from the API endpoint so the agent can reason about what happened when it actually called this tool and then we'll have an accept

**[0:12:45]** here basically just if there's any error at all we'll just catch it and then return back to the agent telling it that there was an error with this specific function here's what the error was so that it can try to correct itself and maybe call the tool again so that is

**[0:12:58]** everything that we need now this neat little wrapper function that makes it so easy to set up any tools working with NN you'll see that right now um and so we'll go ahead and start defining these tools and so the first one that we want right here is the tool to summarize a

**[0:13:15]** slack conversation and when you use the tool decorator here so you put at tool at the top of your function that's Lang Chain's way of turning this function into a tool package and so we're going to get all of our different tools together together combine them put them

**[0:13:31]** into the large language model and the large language model is actually going to use the doc strings here to understand when to use these functions and how to use them so I give a little description I give an example call and then I specify any arguments and also

**[0:13:47]** what this function will return so that it can reason about the output like maybe when I summarize a slack conversation I obviously return the summary and so I tell the AI that it can expect to get the summary back uh which also helps it know when to invoke this

**[0:14:01]** tool specifically and look at how simple this function is it is literally just five lines of code here because I return Calling this function right here this helper function that I made specifically it is a get request I have this environment variable that defines my exact n8n API URL and then I have the

**[0:14:20]** name of the function as well it is that easy and for the other two tools it is also just as easy so we have one to send a slack message again doc string to help but understand when and how to use this tool it's a post request I've got this

**[0:14:34]** URL and then my payload is going to include the message that I want to send in slack and so that's the one parameter that I have for this tool and I tell the large language model in the doc string exactly what this parameter needs to be so that it knows what to pass in for the

**[0:14:50]** message for sending a slack message and so that my very last tool that I have here is creating a Google doc and so this time I accept two parameters because I need the name of the file and the text within it and again I just call invoke N8 and wook it is so so easy so

**[0:15:05]** even if I had 20 tools for this agent this file wouldn't be that much bigger it takes more space to write the doc string than it actually does to create any of these tools because I'm really leveraging n8n for most of the complexity for the actions that I want

**[0:15:19]** to do here and that's the beauty of it there's not actually that much code because I'm leveraging no code to make things that much simpler and if I really need extra complexity for a tool that n8n can't support then I could custom code something in one of these tools

**[0:15:35]** here so I have all the flexibility that I need but it's also very simple when n8n does the trick and most of the time it does like for all these tools that I have here it certainly does the trick for me so that is everything for creating the tools now we can go quickly

**[0:15:49]** to defining our extremely UI for the front end and interacting with our large language model and then we'll test it out so now we get to create the setup to interact with our large language model and set up our streamlet UI so that we can interact with our agent in the

**[0:16:02]** browser so just like with the other tool utility python script I'm going to start here by importing all the python packages that I need I'm also importing all of the tools from that other script and so let me go back over there quick because there's one thing that I forgot

**[0:16:15]** to add in and that is this final mapping here where we take the name of each of our tool functions and we map that to the actual instance of that function in the script and so that way I take this here I import it in my main script and I

**[0:16:30]** now have each of these functions imported and so what we're going to do is actually take each of these doc strings that we have that help the llm understand how and when to use each tool and that's going to be put into the prompt and that's under the hood using

**[0:16:44]** Lane chains that's how the llm knows when and how to call these tools to interact with our n8n workflows we're also going to then load our environment variables just like before this time just defining the environment variable for the model that we want to use can use anthropic or open aai models for

**[0:17:02]** this setup just make sure that you have the right open AI or anthropic API key set depending on the model that you are using with that we're going to then Define our system message here which is basically just some extra context at the start of the conversation to fine-tune

**[0:17:16]** how the llm responds and so there's just a little couple little examples I have here of ways that I'm being very specific with it so that I get the kind of responses that I want telling it things like how to format links for Google Docs B Bas on a document ID so

**[0:17:30]** just a little example there then we can get into our functions for actually interacting with the large language model and binding the tools in them so the first Little Golden Nugget that I have here I don't really want to get into this in great detail but I set this

**[0:17:44]** up this helper function right here makes it possible to use anthropic and open AI models even though they both have slightly different formats for how they produce a response when you invoke the model and so this just kind of handles the difference here and puts it into one

**[0:18:00]** single format that works with the rest of the script so again I'm not going to dive into that but this will make it possible for you to use both which is very very convenient and then with that we can actually get into our function for prompting AI so we're going to set

**[0:18:13]** up our chatbot here so it's going to be a chat open aai instance if the model is a GPT model otherwise chat anthropic and then we get all of our tools from that available tool mapping that we have defined right here and then going back to the script I find the tools in so

**[0:18:30]** this is a lang chain function that makes it so simple this would be a lot of lines of code if it wasn't for a lang chain but it makes it so easy to bind all of our Tools in and then we can invoke our chatbot now with these tools

**[0:18:42]** and we're actually streaming the output so I have a little bit of code here to go through all the chunks as it is producing the stream in the typewriter format and I am Gathering that all together and also yielding these chunks as a generator and so this is a slightly

**[0:18:56]** more advanced python topic and I don't want to get into this in a lot of great detail but I really wanted to implement this because then that way the AI is going to be typing out its response over time which looks really really neat and so I'm using generators here yielding

**[0:19:10]** these chunks as they are produced from the stream so again a little bit more advanced but it looks really really cool and so then what we're going to do after we finish getting the response when it's fully streamed we're going to check if we have any tool calls and if we do have

**[0:19:25]** any tool calls then I'm going to add this message into the conversation history so the AI knows later on that it chose to make a tool call here and then I'm going to Loop through every tool call that we want to make because the AI might want to make more than one and

**[0:19:41]** then we will get the name of the tool get its arguments as well and then invoke that tool and we just have a couple of debug print statements here that I'll show in the demo and then the result of invoking this tool we're going to add as a tool message to the

**[0:19:53]** conversation because that way AI has context around what actually happened when it decided to invoke this n8n workflow so was the message sent successfully in slack what was the summary of the slack conversation all those different outputs are put in this tool message here so that it can reason

**[0:20:10]** about the output and then what we're going to do is recursively call Prompt AI again to get a response from the llm now that it has made the tool call so it might choose to make another tool call or maybe now it's going to actually produce the final response for the user

**[0:20:25]** whatever it might be we have to do that again and then we're just yielding the chunks from this response resp so that is everything for interacting with our llm it is really nice and easy and I even made it more complicated than I had to just to get the streaming in there

**[0:20:37]** because I just think it's so cool but yeah Lang chain just makes it so fast to make AI agents and then for our main function here I'm just going to add a streamlet title set our initial messages to a single system message like I defined above and then every time the

**[0:20:52]** streamlet UI refreshes I want to redisplay everything in the conversation in the UI and then I'll also Define a chat input here where whatever the user types in is going to go into this prompt variable that I'll add to the user interface and also the internal State for the messages and then I'll prompt

**[0:21:08]** the AI get the stream and stream that out to the streamlet UI and then once the stream is complete add that to the internal message State as well and that is everything for our UI and so now we are totally complete we've got this agent fully set up and we can go ahead

**[0:21:23]** and test it out to run this AI agent with streamlet all I have to do is go into the directory that has those pip on scripts I was working on and then enter the command streamlit run n8n Lang chain agent. that's going to instantly spin up a new streamlet instance in my browser

**[0:21:38]** and take me to it right away we can see boom there we go we got our conversation with just a system message in it right now and so now I'm going to really quickly show you how we can use all these tools together to do something kind of neat it's not going to be like

**[0:21:51]** insanely powerful but it's going to show you very clearly how neat this setup is and how easy it is to work with Lang chain Python and n8n and so what I'm going to do here is ask it to summarize the conversation in slack and again the Channel's hardcoded so it knows what

**[0:22:08]** channel to do right away it's going to call that n8n workflow and get that summary have it return back and then here we go boom that's super nice and easy now I can even go to the terminal here and show my debug messages where it decided to invoke this tool and this is

**[0:22:22]** the response that it got back from the n8n workflow call and so we have a good summary here and I'm going to actually say uh do some research for me on the pros and cons of each so I'm going to have it do a little bit of work for me

**[0:22:38]** maybe you could even have like some sort of web search tool that would do some of this and then spit back a response but in this case I just wanted to use this internal knowledge to give me some pros and cons of each so it's helping me make

**[0:22:49]** a decision for my AI startup Tech stack so I'll say great thanks now create uh a Google doc with your fin findings and so now it's going to go and actually make a Google doc with everything it just spit out to me and so we're going to give it

**[0:23:05]** a little bit of time this is going to be a bit of a longer tool call so I'll pause and come back when this is complete okay I paused for like 5 seconds and then it was done so super super quick but here we go it's created a Google doc and it's even linked it for

**[0:23:16]** me which is super super nice or I can go in my meeting notes folder here that I referenced earlier scroll down to the bottom and here we go text stack research it picked the title completely on its own and going into it we've got all the marked down that's why it looks

**[0:23:28]** kind kind of silly cuz it's markdown all the markdown for the research that it did for me this is beautiful and so at this point we have summarized the slack conversation and created a Google doc and so now the last thing we want to do is send a message in slack and so I'll

**[0:23:42]** say fantastic send this link over to slack letting them know that you have done research to solve all their problems let's go so it's going to call that last n and workflow the last one we have to use and boom we sent the message in slack and I actually got the

**[0:24:02]** notification just now um and you can see that I got a new message so clicking on that there we go I've done some research on the Tex stack options here's a link to the doc with all the research this is so so easy so theoretically I didn't actually have to touch slack or Google

**[0:24:16]** drive at all to do any of this I just wanted to show you that it was all working but this is just beautiful and it's using n8n for everything that's actually interacting with these external services and so it's just so convenient to set this all up so there you have it

**[0:24:29]** that is n8n Python and Lang chain all combined together to make it very easy to build powerful and controllable AI agents if you think there there is another stack that'd be even better let me know in the comments I would love to hear from you other Technologies you'd

**[0:24:44]** want me to explore because I'm always open to new ideas for Content so if you found this valuable and you're going to use this Tech stack to create your own AI agents I would really appreciate a like and a subscribe and with that I will see you in the next video
