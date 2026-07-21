---
type: raw-transcript
title: "I Found the Limits of the Most Popular LLMs"
youtube_id: uIWNzcqHQ58
url: https://www.youtube.com/watch?v=uIWNzcqHQ58
slug: i-found-the-limits-of-the-most-popular-llms
published: 2024-08-28
duration: "0:32:41"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have built an AI agent with rag access to my Google Drive and access to my Asana for tasks today I'm going to show you how I built this AI agent but more importantly I'm going to use it to push the limit of a bunch of different llms

**[0:00:13]** by making increasingly complex requests until I break each one every single llm has its limits and today I'm going to find those so I'm going to be testing a couple of GPT models CLA 3.5 Sonet and then also a fine-tune version of llama 3 by Gro that is made specific spefically

**[0:00:30]** for function calling this is going to be fun I'm just going to have a blast with this to give you a good example one of the more complicated requests that I'm going to be testing with is take my August 24th meeting notes for my Google Drive and put it in your knowledge base

**[0:00:45]** then go into my coding project in assana and Mark every task as complete that was mentioned as being done in the meeting notes you tracking with me here there is a lot going on it is definitely not a simple request you have to go to the vector database for red

**[0:01:00]** go to Google Drive for the files and then also go to a for the task management it is not something that some of these llms are able to handle I will tell you already While others actually can handle it and so if you're curious which ones will break and which ones

**[0:01:14]** won't for these kind of requests watch this video and find out which llms can actually handle these more complicated agentic requests so I'm going to start this video by walking you through how I built this agent so you can steal it for yourself and then I'm going to break as

**[0:01:29]** many llms as I possibly can with this agent so without further Ado let's dive right into it all right so here we are in the code for the AI agent with Rag and access to my Google Drive and AAA this is going to be a bit more of an

**[0:01:41]** overview versus building it from scratch mostly just because there's a lot here in terms of tools and also I've covered a lot of Concepts involved here in other videos on my channel in detail and so I just want to keep this high level for now so at least you'll get a good idea

**[0:01:55]** of how this agent works if you want to take it for yourself and use it or expand upon it which if you do there's going to be a link in the description of this video for a GitHub repository for you to take all this code which all this

**[0:02:06]** that we're going over now is going to be in the folder llm agent evaluation framework now the reason I called the folder this is actually quite cool is I'm thinking about turning this whole process of trying to break llms into something automated so you could actually test how good any new model is

**[0:02:23]** for agentic workflow so you could take a new model from hugging face or GPT whenever they're released and you could throw it into this framework and it would actually run automated tests to try to break the llm and then spit out some sort of score so if you think

**[0:02:37]** that'd be cool just let me know in the comments because I am definitely considering making a video on that and actually taking this really far and turning into some sort of test suite for nlms which I think would be super neat so anyway that's why I called the folder

**[0:02:49]** this and in here we have our main python script which defines the streamlet UI for this whole application to test llms and then we have a bunch of tools that are split into a SAA Google drive and Vector database tools so I'll show all this in a little bit here and then we

**[0:03:03]** also have our Lang graph runnable which manages the whole execution of talking to the AI and then having the AI internally make all those tool calls and the decisions around those I also have an example environment variable file that has everything you need to be able to test all the different llms that I'm

**[0:03:19]** going to be testing in this video so you have like your open AI API key your grock API key and your anthropic API key and then you have the main environment variable LM model and this is where you could Define which model you're actually testing with and so if you change it to

**[0:03:32]** from GPT to Claud my script will intelligently realize that it needs to make a chat anthropic instance to interact with Claude or if you change it to um this model right here for the fine tune grock llama 3 it'll know to use chat grock and so all that's

**[0:03:46]** intelligently determined by this environment variable so just a little bit on the environment variables there really easy to follow along with this uh there's nothing here for Google Drive access because that's all actually managed through a credential file and so I have a link here with a python Quick

**[0:03:59]** Start makees it really easy to understand how to get all that set up if you want to run this agent yourself so with that we can dive into the first file here which is our streamlet UI so this is where we basically just set up the user interface and then whenever a

**[0:04:13]** user message comes through we're going to interact with our Lan graph runnable to get the response from the AI and make any tool calls for this to actually be an agent and so in the main function here I just Define the streamlet UI starting with the title I initialize the

**[0:04:28]** message state with just a system a message to start and this is giving the context for our agent and then also I display all the messages to the UI and then I react to any user input in the chat input component in my UI and so basically whenever a user inputs

**[0:04:45]** something it's going to call this prompt AI function and display the chunks over time as they are generated in my L graph runnable and so going up to this function right here it's very very simple I just Define the config and then execute my Lang graph runnable and I do

**[0:04:59]** it an aing synchronous mode so that for the models that support asynchronous streaming like anthropic and open AI models we'll actually get that nice typewriter style output from the AI where it looks like it's actually typing out a response to us very very cool and to go and see what that actually looks

**[0:05:16]** like here in my runnable dopy where I Define the whole Lane graph runnable first of all I have this model mapping and so this is where we take the environment variable and based on what keywords are in that model ID we're going to have a different chat object

**[0:05:31]** instantiated these are all from Lang chain so like chat open AI for GPT chat grock for grock and then also chat hugging face if we have a Bas llama model that isn't the grock finetune one now chat hugging face doesn't seem to work for Tool calling yet at least using

**[0:05:46]** the hugging face endpoint and so we're not going to be testing with that today but I've heard they're adding support for it so theoretically at some point in the near future we would also be able to use any models and hugging face for this as well as long as the model itself

**[0:05:59]** supports function calling um that's being used through hugging face so just a little aside there so we get the model mappings here and then what we do is we bind all of the functions that we're defining in all these different tool files together into the single dictionary and then we map that we bind

**[0:06:16]** that into the chat object that we create based on the model ID in the environment variable and so at this point we have this chat object that has all of the vector database ASA and Google Drive tools all bound into it and we can now use it in our Lang graph runnable and so

**[0:06:32]** the state for this Lang graph is just the messages that's all we care about here as far as the state of this whole application so we have one node for calling the model and that's where we just get the response from the AI which would include any tool requests that it

**[0:06:45]** has as well and then we have our tool node and so if it needs to make any tool calls we're going to do that and so we'll Loop through every single tool call that the AI requested to make we're going to get the name of the tool and

**[0:06:57]** the arguments and then we'll invoke the tool with the arguments get the output and then add that to the conversation history as a tool message and so that way the AI has the context around the tools that it has requested to use and the result of executing those tools so

**[0:07:11]** it can make a final response for the human for us in this case and then I have a router node in this graph which basically just it takes the AI response and it determines is it done should I send the response to the user or if it is requested to make tool calls I need

**[0:07:27]** to continue on in the graph go through that Cy of making tool calls until it decides it doesn't need to anymore and so then to Define this workflow and compile it it's very very simple we just have our agent node and our tool node and these are connected through this

**[0:07:42]** should continue function so once the agent is done it'll determine if it needs to make a tool call if it does it'll go here and then go back to the agent afterwards otherwise it'll just exit if it decides it doesn't need to make any more tool calls and that is it

**[0:07:55]** so we compile this app and then we return it in this get runnable function and that's what we have here in our main script right here to get it and then use that in our streamlet UI very very nice and simple and then for our tools that we have here first of all we have a and

**[0:08:12]** so this is everything that we've been using for my AI agents Master Class Series so creating projects managing tasks deleting tasks marketing those as complete all that good stuff um and then for the Google drive this is going to include things like searching for a file for example that's a really key one for

**[0:08:29]** bringing things in Rag and then also being able to download the file as well so it'll download the file locally and then return that path to AI so that it can use it to put it into the knowledge base I have purposely not included a function here to read the contents of a

**[0:08:44]** Google drive file I can only download it and get the path that way if the AI ever reads any content from a Google drive file it's because it first added it to the vector database the knowledge base and so that way we can guarantee that if the AI spits out any information that is

**[0:09:00]** related to something I have in a Google drive file I know that it is in the vector database we can validate it that way and then so we also have functions for like uploading files leeting files updating fil like basically crud operations on our folders and our files

**[0:09:14]** in Google Drive so nice and simple there um all of this code is going to be available to you if you want to incorporate any of these tools yourself as well so even if you don't necessarily want to use this agent but you want to set up your own kind of thing that has

**[0:09:25]** Google Drive hooked into it feel free to use these functions as well um and then lastly we have our Vector database functions so just a few of them here uh first of all we query our documents so given any kind of question from the user we'll get the relevant documents from

**[0:09:39]** the vector database so the AI can use that to give the response to the user and then we also have uh given a file path we can add that document to the knowledge base and that that's what I was saying earlier where we don't have a way to read the contents directly from a

**[0:09:51]** Google drive file but we can add it to the knowledge base and then get the information that way and then lastly we have a nice little tool here to clear knowledge Bas and so that way after I run a test I can quickly clear everything so I don't have to go

**[0:10:04]** manually delete the vector database for the next test that I'm running so that is literally everything there's a good amount of code here um but overall it's pretty simple pretty easy to follow and so with this we can go ahead and start breaking a bunch of large language

**[0:10:17]** models starting with GPT 40 mini all right it is now time to break as many llms as we can starting with GPT 40 mini I picked this one cuz it's kind of in the middle here of of the models that I'm going to test it should do pretty

**[0:10:31]** well with most of the requests that I have here but there are a couple more complicated ones that from some of my initial testing it doesn't quite get right and you'll see what I mean when we get to that point and so I'm going to spend most of my time with this and then

**[0:10:44]** I'll test the other ones but go a little bit quicker because we'll see where we'll break some models pretty quickly and other ones that we can do really complicated things with and so starting off with a really simple request here I'm going to ask it to make a task in my

**[0:10:56]** coding project in AA to build the next thing just something silly and random that's what I'll be doing for a lot of my tests here so within my coding project in ASA you can see there's nothing here right now these are all just placeholders that's why they're grade out and so I'll go ahead and hit

**[0:11:10]** enter make this request and then we'll check Asana right after and see if that task is there and GPT 40 mini will give us the confirmation as well so here we go task build the next big thing has been created in my coding project and sure enough here we go that worked

**[0:11:25]** perfectly so it has passed the first very basic test now I have a text document on my other screen here with some other things I'm going to copy just you know to see me type it out here uh the next thing is just going to be something really simple from Google

**[0:11:37]** Drive so I'm going to ask it to download my 822 meaning notes from my Google Drive so it'll actually have to do the search pull that and then download it and so there we go the meting notes have been downloaded and it gave me the file name as well in a text file very very

**[0:11:50]** neat so it converted the Google Doc to a text file downloaded it locally all using the tools that I've given it and by the way the 822 meeting notes is just this file right here I've got it zoomed in nice and big for you um but this is

**[0:12:02]** just this document right here just a again another really silly little thing here just to have a something quick for a demo and so just a couple of action items here which we'll do with rag in a little bit here um and also what I can show you here is my terminal so let me

**[0:12:17]** bring this onto the screen here I have it print out all the tool calls that it makes and the result of invoking those tools and so for example it called the search file in Google Drive function with the query name contains 822 meeting notes so this is a specific format

**[0:12:33]** that's required to search in Google Drive so by the way that's something that some of the weaker models might not get right is you have to say name contains and then in single quotes uh what you're searching for and then we got the result here so it gives the ID

**[0:12:45]** of that file and the name of it as well and then I download the file so I invoke the tool to download the file and then I get that result which is the text file right here and then that's what it ends up giving me in the chat it tells me the

**[0:12:57]** text file and so as I'm testing models and when things go wrong we can look here to see exactly how it messed up and so we'll see that in a little bit once we actually break these models because trust me we are going to be breaking these models and so let's go to a more

**[0:13:10]** complicated request here just slightly more complicated we're going to build up to actually breaking this model seeing how far we can take GPT 40 mini so I'm going to say take my 822 meeting notes that I downloaded and put it in your knowledge base and there we go sure

**[0:13:24]** enough it did that successfully and now because it's in its knowledge base we should be able to ask what are the action items from the 822 meeting let's see uh and if it gives me the right answer there we go Yep this is everything that we saw in the document

**[0:13:41]** right here word for word so it got that right and we know that it didn't read it from the Google drive file directly it got it from the knowledge base because I don't even have a tool available like I mentioned earlier to get the contents from a Google drive file I can just

**[0:13:54]** download it and then put that file directly in the knowledge base so this is working phenomenally now we can go on to some more complicated requests here so all right this is the fun one I'm going to uh create a new project in a sauna called new Todo and then put in

**[0:14:09]** three tasks just again a bunch of really silly random things and so in N right now we do not have a project called new Todo or I guess we do now have it because it's already created it it's parsing the requests in real time here so you can actually see this happen in

**[0:14:23]** real time um and so it's going to make all those tasks within the project and then return the final result to me basically just telling me that it did everything that I asked it to do so let's go over here there we go the project new Tod do has been created and

**[0:14:36]** the following tasks have been added pet a dog create renewable energy and reinvent the wheel uh so let's check and there we go yep they are all added I didn't give due dates for any of them so that's why it's today uh for all three but this is working just as expected all

**[0:14:50]** right so now we're going to take a another request here we're going to combine the vector database with Google Drive so instead of first asking it to download the Google Google drive file and then in a separate request asking it to add to the knowledge base I'm going

**[0:15:03]** to do it all in one because this is where you can start to confuse agents if you have make it have to infer certain actions it should take sometimes it'll mess up U but sure enough it actually worked here and so I'll just ask it the same question that I asked it before

**[0:15:17]** what are the action items but this time from the 823 meeting and make sure that's in the knowledge base as well so let's give it a sec for it to do that retrieval and there we go that is correct I can even go to the file here and show you so 823 meeting notes uh

**[0:15:29]** same kind of deal as the 822 just silly random stuff but it got that right so this is looking really good all right so next one I'm going to do is do a little bit of combination with Rag and Asana so I'm going to say make a task in my coding project for

**[0:15:44]** every single action item that's in the 823 meeting notes and so we'll see them pop up one at a time here as the agent makes them and sure enough everything that's making here is exactly what we have in the 823 meeting notes here so this is working beautifully we have not

**[0:15:59]** broken GPT 40 Mini at this point but I promise you we will get to that I just want to work up to it to show you how it can do a ton of things and so by the time we break it it's actually going to be a very complicated request um so

**[0:16:12]** let's see what else do I got here um okay here we go this this is a fun one okay so first I'm going to create a new project in a sauna called new Todo and I already have that here so I'm going to actually delete this project so

**[0:16:26]** it'll basically recreate it for me just as another little bit of validation there um so there we go it's gone now so I'm going to say create a new project called new to-do and put in these tasks and so very very silly stuff but let's see if it can do this for me so here we

**[0:16:41]** go we got the new to-do project recreated and then we'll see the tasks pop up again just like we saw before in the coding project um give it some time to make all those requests and then it'll spit out a response again so we got all this happening in the terminal

**[0:16:54]** here uh like create a sauna task with this as the name and this as the project ID which is my new to-do project just created um beautiful beautiful and it made all that so this is perfect um now what we're going to do take a look at my

**[0:17:08]** 824 meeting notes so uh just a couple of random things here and then also we have a few items here that map to some of the tasks that we just created in this new Todo project uh so these three map to three of them here and so what I'm going

**[0:17:24]** to do is make another request where I'm going to say I want you to take my 824 meeting notes so it doesn't even have it in the knowledge base yet it has to know to go to the drive put it in its knowledge base and then Mark all the

**[0:17:37]** tasks in new Todo as complete that are mentioned in my 824 meeting notes and so three of these should be marked as complete once this request is finished once it makes those calls and so let's see what it's doing here looks like it failed okay so I think we have

**[0:17:55]** officially broken yep we have officially broken GPT 40 mini cuz I can promise you that I can get this to work with larger models I think we have finally found how far we can take 40 mini which is pretty good it did pretty good in fact in some

**[0:18:09]** of my testing it's actually done things like this successfully it's just because it's an llm and there's a little bit of Randomness there are some things that don't necessarily work 100% of the time even though they might 50% of the time and so the issue that we have here um

**[0:18:23]** it's kind of hard to tell from the error message uh but really what happened is it gave incorrect arguments to to um marking a task as complete U and so what I'm going to do is I'm going to ask it to retry the operation we we'll see if I

**[0:18:36]** can get it right with a retry here um yeah that didn't work it's because the whole chat history is messed up now with that error so we kind of broken gbt 40 mini so now what I'm going to do is I'm going to move to Claude 3.5 Sonic I'm

**[0:18:54]** going to make a couple of more basic requests but move a little bit faster get to this point again and see if it'll work with clae 3.5 sonnet all right so here we are with clae 3.5 sonnet now and I've totally refreshed my environment so my Vector database is cleared I can even

**[0:19:10]** prove it now by asking what are the 822 action items and because the vector database is cleared it's not going to have the answer this time um but actually Clan 3.5 Sonet is so intelligent that it knows to go search my Google Drive add it to the knowledge

**[0:19:25]** base and then put it into the answer here and so um CLA is actually so good that unlike with gbt horal mini I can't prove the vector database doesn't have the information easily um because it just does everything it needs to get that information which I guess it kind

**[0:19:41]** of does prove it because it didn't give it to me right away it had to go do all these things but sure enough it has its entire thought proc process put out here which is beautiful and then it gives me the right answer at the end here um so

**[0:19:53]** we're already kind of seeing how CLA 3.5 Sonet is way better for agentic workflows than G PT 40 mini and this is the kind of testing that I'm trying to do I'm trying to set up a way to really determine like what model should I use when I want to build a production level

**[0:20:08]** AI agent application and so far the answer is CLA 3.5 Sona at least compared to GPT 40 mini um because yeah it did everything here it literally did uh rag and Google Drive all within like a single sentence request which is super cool um so now what I'm going to do is I

**[0:20:25]** don't even have to do the basic stuff like we know that it's going to do it if it was able to do this and give me the right answer here U so I'm going to have it do the same requests that gbt 40 mini failed with and so I'm going to start

**[0:20:37]** with creating a new a project in auna called new Todo and putting in all these tasks the same thing that we did before um one thing that this does way differently than GPT 40 mini it's kind of like what I mentioned earlier it actually spit out its thought process

**[0:20:49]** for everything which is kind of cool like I actually like how it does that and everything works with the typewriter um style so we see it like type out as it's producing its thoughts it's very very cool um and so let me go over to this new to-do we can see all the tasks

**[0:21:02]** getting created or I guess they already are created oh here yeah fifth one came in just now and then here we go we get the response back from uh Claude and we are good to go so now we can test the real deal here this is what broke GPT 40

**[0:21:16]** mini so the Moment of Truth can Claude 3.5 Sonet do better than GPT 40 mini for this more complicated request all right so first it is getting the meeting notes from the Google drive it got them it's going to download them and then after it downloads them add them to the knowledge

**[0:21:32]** base good good good and then query the document to find the tasks that were complete it's doing all of this I can even open my terminal here and you can see all the the tasks that it's doing this is working perfectly so far uh it did the rag to get the tasks U and now

**[0:21:48]** the very last thing is to actually Mark the tasks as complete that are mentioned in the document and so let's see moment of truth if we can actually do this right or if we're going to get an error again uh and so yeah it's taking sweet time with this so I'm going to pause the

**[0:22:01]** video and I'm going to come back when it is done oh nope I didn't actually have to I just just about to pause it and it's doing everything now so all the the tool calls are rolling in to Mark the tasks as complete we can even go into a

**[0:22:14]** sauna and it's marked the first one as complete uh let's see if it can mark the second one it's taking its time because there's so many things that are happening here like it's just crazy the amount of operations that this thing is doing for me here um and well let's

**[0:22:26]** check here so this review the budget is marked off and yep sure enough that's one of them that we have and the Google Doc here so it should also Mark off spend the rest of the budget and then also cry cry it over a few drinks um yep

**[0:22:39]** so marked off spend the rest of the budget and cry it over a few drinks so we are good Claud 3.5 son it handled the most complicated request that I really have at this point I'm looking through my list here and um yeah I think that's really the more the most complicated one

**[0:22:55]** that I had because that made GPT 40 mini fail uh but 3.5 Sonic Claude got it perfectly um so this is awesome so far we have a winner so let let's move on and let's test the grock fine-tuned Llama 3 Model all right it is now time to break the fine-tuned version of llama

**[0:23:13]** by grock now everyone knows that llama 3 is not as powerful as the anthropic or open AI models and so I'm going to start with a couple more basic tests and then probably get to the point where we'll break it pretty quick even though this is fine-tuned for function calling so

**[0:23:27]** we'll see I might be surprised but I'm going to start with a couple of more basic requests so first I'll say what projects do I have in assana we'll see what I can spit out for us here and so it's pretty quick that's one of the really awesome things with Gro you have

**[0:23:40]** the following projects in Assa YouTube Fitness business personal and coding I'll say cool uh create a task in my coding project to build a SAS due by Sunday let's see if it can handle this for me so basic requests still not like super super trivial um so yeah let's go

**[0:23:59]** over to assana check it out in my coding project there we go build a sass due by Tuesday okay so all right looks like we already broke Rock because it gave the wrong due date and this is something that I know absolutely for sure that Claude 3.5 son

**[0:24:15]** it and GPT 40 mini could handle perfectly fine I didn't test due dat specifically but I've done a lot with that in my AI agents Master Class Series where I used GPT 40 mini and even Claude 3 saw it and it did this fine so that's really unfortunate um it looks like we

**[0:24:31]** already found a Breaking Point here so I'm going to try a couple other things just to see if it could um kind of make up for itself here but it's already not looking too good um so I'm give another request here I'm going to say uh take my

**[0:24:45]** 823 media notes from Google Drive and put it in your knowledge base and so now I'm going to test out some Google Drive and some Vector database stuff because everything before this was just with AA specifically so let's see what I can do here so I'll open up the tool calls here

**[0:24:58]** and this is is interesting so it's searching based on the full text so not the name of the file but the actual contents um and it did not find anything that's kind of the problem here um but now it searches for name contains meeting 20248 d23 um so yeah I don't it's not going to

**[0:25:15]** find anything um because it that that exact search there doesn't exist in either the contents of the file or the name of the file it'd have to search for 823 like CLA 3.5 son and gbt 40 mini did so it is not doing too hot here um let's see how

**[0:25:34]** long it actually retries for because it it goes in the L graph Loop and so it could theoretically like keep trying this tool call Forever uh so what I'm going to do is I'm going to pause the video and come back when it's done and see if it can actually fix itself here

**[0:25:46]** all right so I am back and it is still just trying to make a bunch of different searches here and we even hit the recursion limit like I unpaused at the perfect time here where it tried for 25 times um or at least maybe like 12 or 13

**[0:26:01]** times because that's the number of node executions in L graphs you have a model call then a tool then a model call then a tool so it tried like 12 or 13 times here to search for the file and it couldn't find it and so this finetune version of llama 3 by Gro is not looking

**[0:26:15]** too good it's able to handle some basic things like searching for projects and creating a task even though the due date was wrong but it's not able to do multi-step workflows really um and so yeah it's not it's not looking good I'm going to try one more thing and then

**[0:26:28]** we'll go over to testing with gp4 turbo so I'll show you how I reset stuff here I can go here and clear the cache and so this way it'll get a new L graph runnable with the new chat history and then I can just do a rerun here so it'll

**[0:26:41]** reset everything for me and then I can go ahead and try another request and so what I'm going to do is I'm going to try to fix it by telling it specifically what to search for now I can always make my tools clearer I can give better instructions for how to give arguments

**[0:26:56]** things like that to make it so weaker models can actually perform these actions but if something like GPT 40 mini which is already super super cheap or CLA 3.5 Sonic can handle these things without me having to get really specific I might as well use them um but I'm

**[0:27:10]** going to I'm going to try to actually make this work here so I'm going to take I'm going to say take my meeting notes I'm going to say titled uh 823 meeting notes so I'm going to give the exact title that we have in Google Drive so we'll search by that titled 823 meeting

**[0:27:26]** notes from Google Drive and put it your knowledge base so hopefully with the exact title now it'll do the full search correctly this time and oh there we go so I found the file 823 meaning notes but I encountered an error when downloading it so now I'm going to go to

**[0:27:41]** the arguments and see what happened um so let's see downloaded the file and it looks like it gave the wrong file ID yes it definitely did because here's the file ID from the query and that is not what it passed in as the file ID for our download file tool so it did part of the

**[0:28:01]** process here it actually fetched that it queried and found the file in Google Drive but it wasn't able to download it and so again this finetune version llama 3 even though it is meant for function calling is failing here it's not giving good arguments and so yeah this one we

**[0:28:16]** broke very very quickly so as a last test let's go on over to GPT 4 Turbo all right last test now I actually misspoke I meant to say GPT 40 not GPT 4 Turbo now that model actually exists as well but since GPT 40 is kind of the the

**[0:28:32]** newer model for GPT 4 I'm just going to use that one for my test here so what we're going to do is we're going to start out with a very basic request and then we'll get into the complicated things pretty quickly because I think that gbt 40 is going to perform pretty

**[0:28:45]** well like clae 3.5 Sonet now I'm doing a lot of this ad hoc I haven't like tested a lot of this beforehand mostly just with gbt 40 mini so I'm going to be surprised by the results potentially just like you so let's give this a shot I'm going to do the vector database

**[0:29:00]** thing with Google Drive first as an initial test so I'm going to say take my 822 meeting notes I downloaded and put them in your knowledge base let's see if this works I'm going to look at the tool calls that are happening and there we go everything is working perfectly added to

**[0:29:13]** the knowledge base after downloading and we are golden so now I can say what are the action items in the 822 meeting and should get this right just like what we have here in our document so yep there we go it is right so so far it's doing

**[0:29:28]** much better than the Llama 3 Model by grock already um so now let's get into a little bit more of the complicated stuff I'm just going to dive right into the thing that broke GPT 40 mini and see if the flagship model of gp4 can handle it unlike the Mini version there's always a

**[0:29:43]** time and a place to use mini um but sometimes with more complicated stuff like this you have to use something like GPT 40 and so let's see yep created the new to-do project let's watch it get populated with these five tasks here in real time review the budget we can even

**[0:29:58]** watch them go here in the terminal creating regret all decisions cry out over few drinks last one there we go all right so we got all five we got the response from GPT 40 and now I can do my final request that broke 40 mini so take my meeting notes from the Google Drive

**[0:30:15]** put them in your knowledge base then Mark all of the tasks here uh as complete that are mentioned in my document right here so let's see if it can do this right so I'm going to go over to my terminal again all right it's oh this is this is fast it is working

**[0:30:29]** this is working beautifully um let's see if I can mark off the last one it's taking a little bit of of its sweet time just like Claud 3.5 son it did but it should get there um actually did it finish Whoa We actually broke GPT 40 sure enough it didn't mark cry it out over a

**[0:30:50]** few drinks as complete when this is clearly one of the items that we have here in the document um wow I was actually honestly I was thinking that BBT 40 would do fine here but it did not it messed up U let me let me look at the

**[0:31:03]** response again uh the following tasks have been marked as complete so it correctly identified the ones that it did Mark as complete so it's not like it tried to mark this as complete it just completely missed it and so at this point we have broken we easily broke

**[0:31:16]** llama 3 from grock we broke GPT 40 mini on the final test and then we also broke GPT 40 on the final test though it was almost there it was like 90% of the way there but CLA 3 .5 Sonet I was not able to break um so maybe in another video

**[0:31:32]** I'll have to do some more testing where I really try to hone in on Claude 3.5 Sonet and break it but at this point we have a clear winner for agentic workflows and that is Claude 3.5 Sonet so I'm actually pretty happy with the results of these tests here because I

**[0:31:46]** honestly thought that GPT 40 would be the best model for AI agents but from my testing here I wasn't able to break clae 3.5 Sonet when I could break everything else and so it really does seem like it is the best model for agentic workflows and so I hope that you learn something

**[0:32:01]** just like I did here and that maybe when you build AI agent applications in the future you might lean towards using CLA 3.5 Sonet instead of something like GPT 40 another really good model that I want to test is llama 3.1 405b but like I mentioned earlier in the video chat

**[0:32:17]** hugging face from Lang chain doesn't seem to support tool calling yet with the hugging face endpoint but in the future I will definitely be testing with that and also diving deeper into CLA 3.5 Sonic and trying to break that with an AI agent as well so if you're interested

**[0:32:30]** in seeing that in the future feel free to subscribe to my channel I'd also really appreciate a like on this video thank you very much for watching with that I will see you in the next video
