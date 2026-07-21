---
type: raw-transcript
title: "Build a FULL Stack App for your n8n AI Agent in 20 Minutes"
youtube_id: JyolNYRbAcs
url: https://www.youtube.com/watch?v=JyolNYRbAcs
slug: build-a-full-stack-app-for-your-n8n-ai-agent-in-20-minutes
published: 2024-10-02
duration: "0:20:27"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** everyone and their mom is using n8n to build AI agents right now it is the most popular topic on my channel and rightly so it is just so incredibly easy to use NN to build simple yet powerful AI agents without having to write any code the problem is most of the time you

**[0:00:17]** can't just build an agent with NN and call it good you actually need a front end for yourself and other users to interact with your agent in a clean and simple way sure you could just use the n8n chat widget that it gives you for your agents but most of the time you

**[0:00:32]** need something much more to actually have a good user experience so today I'm going to show you how to use my favorite combo to build incredible and secure interfaces for your AI agents that you can literally create and deploy in an afternoon and the best part is you don't

**[0:00:48]** have to create a full react or nextjs project like you would with vzero and you really don't have to code anything because we are going to have the llm do that for us I know it is a shocker that I'm not using bzero here but I think you'll like how neatly this works out

**[0:01:03]** there is a time and place to use v0 and also decode a front end yourself but that is a discussion for another video right now we just want something quick and awesome and that is using the combo of Claud streamlet and super base why this combo well let me tell you really

**[0:01:18]** quick first of all streamlet it's a python package that makes it super easy to build websites no need for JavaScript at all and then Claude is really really good at coding with streamlet and I know that Claude in general is already really good at coding it is insane even

**[0:01:35]** considering that and then we tie it all together with super base for easy authentication and there's a good chance that you're already using superbase for your an agents anyway for things like your chat memory and rag so I'll start by showing you how to use cloud to create a basic streamlet interface for

**[0:01:51]** the N agent without authentication I'll show you the N8 end workflow as well for the agent and how you have to set it up to make it accessible to the front end then we'll go back to using Cloud again to add super base authentication both to the front end and the back end with n8n

**[0:02:07]** so without further Ado let's dive in so starting in Claud we're going to put in the first prompt to create the basic version of the streamlet app without authentication now all the prompts that I'm using here as well as all the code that I generate and tweak and all the N

**[0:02:22]** workflows are going to be in a link in the description below to a GitHub repository so you can just take everything that I've developed right here and use it for yourself to have a really good starting point and so the first prompt that I have here is create

**[0:02:35]** a basic streamlet application with a chat interface to talk to an llm and I also this is really really important I specify what it looks like to actually chat with the llm and when and how to use this web hook also one thing that I want to mention is I have very basic

**[0:02:50]** authentication here with a hardcoded bearer token and so this isn't using superbase authentication it's not robust and you shouldn't use this in production but I still want a little bit of protection so that people can't just access my Na and workflow and suck my llm credits and so that's just an

**[0:03:06]** important note there and then I also get really specific with how to use this web hook because it's a post request and it needs specific items in the payload to work with the na workflow specifically I need to pass in the session ID which is what na uses for chat history and I'll

**[0:03:23]** show that workflow in a little bit here and then also the chat input that's the second parameter in the payload that obviously just the user prompt from the interface and then the response is also really important I have to tell Claude that there's a output key from the

**[0:03:38]** response Json and that's what contains what I get back from the llm that I need to display back out to the user and so with that I'm going to go ahead and hit enter and Claude is just going to chug right through all of this code it does

**[0:03:49]** it so so fast it'll open up the code on the right like we see here and this is looking perfect so we got a couple of placeholders that we have to fill in and I'll do that in a little bit when I bring this code into my visual Studio

**[0:04:00]** code IDE we generate a random session ID for chat memory we have this function here that sends a request to the llm and gets the response back with all the headers and using the output key everything that I spec specified this is perfect and then in the main function

**[0:04:16]** here we set up our streamlet user interface with the chat input and then whenever we get input we are going to add it to our user interface get a response from the llm and then output that as well super simple but this is working perfectly and so now really

**[0:04:31]** quickly I'm going to show you what you need to do in n8n to make this work with a web hook and then we'll also dive into actually getting this code up and running all right so here I am now in my N8 end workflow where I have fully built

**[0:04:42]** out a rag AI agent that I've also made accessible to my front end and so I just want to say that in a separate video on my channel which you can see above I have fully built out this agent so if you're curious how I did that feel free

**[0:04:54]** to check it out I'm not going to go into detail on everything here because I want to just focus on how to integrate the na n agent with the front end making it accessible through a web hook and so let me dive into that right now I'll zoom in

**[0:05:06]** to where we get the triggers for our agent and typically when you create an agent with n8n you're going to have a win chat message received trigger this is what gives you this chat widget in the bottom Middle where you can interact with your agent within the workflow UI

**[0:05:20]** and also if I click on more info you get the embed codes that you can embed for a nice little chat widget that's all fine but I obviously want a web hook so that I can interact with this through apis in my front end and the way that you do

**[0:05:33]** that is you simply add a web hook trigger at the start just like we have the win chat message receive trigger and then you add a respond to web hook at the very end right after the tools agent just these two nodes that is it it is super super simple but obviously I still

**[0:05:48]** want to cover this for you because it's important to get it right and I'll also talk about the web hook as well because there's a couple of things that are really important to keep in mind here first of all your production URL will be active as long as as your an workflow is

**[0:06:02]** toggled to active in the top right so this is the URL that you're going to put in to fill in the placeholder in the python code so CLA gives us a placeholder for the web hook URL that is this and that is controlled by the path here also for the authentication you

**[0:06:17]** want to select a header off and again we're going to use super base later but this is just for super basic authentication and then for the credentials you can click on create new credential and then right here the name you want it to be authorization because that is the name for Bearer token keys

**[0:06:32]** in our API calls and then for the value here you're going to put Bearer with a capital b space and then the name of your token and we'll see this when we go into the python code exactly what that looks like but you want that to match exactly with what you see here I'm

**[0:06:47]** obviously not going to show my password here um but yeah authorization and then Bearer space and then your token and so I'm going to close out of this because I obviously have mine set up already and then to respond you want to change it from immediately to using respond to web

**[0:07:01]** hook node because we add that here at the end and what this is going to do you don't have to change anything it's going to by default take the output items from the previous node which obviously includes the output key from the llm and it's going to return that back to the

**[0:07:16]** web hook request and so that's how we get the response from the llm as a response to the API call so with that that is literally everything so we can now save it and then go over to implement our python code in our IDE fill in the placeholders and then run it

**[0:07:30]** and test it another thing that I want to mention really quickly we had the payload with session ID and chat input because if I go into the edit Fields here what I do is I have this work for both the win chat message receive trigger and the web hook trigger so this

**[0:07:46]** is the value that I have for the when chat message received the chat widget trigger but if it doesn't exist then I go to the payload from the web hook request so it's json. body. chat input and then for the session ID it is exactly the same and so that way no

**[0:08:02]** matter if we are triggering from our chat widget or our web hook we can use both but and those are both going to lead into this edit Fields node where we get the chat input and session ID so that for example in the postgress chat memory we can use the session ID taken

**[0:08:18]** from the previous node and that's all going to work correctly so we need those specific Keys chat input and session ID or the N workflow will not work all right so with that out of the way we now have everything that we need to just dump our python code from Claude into

**[0:08:32]** Visual Studio code and we've got our front end and so what I'm going to do here is go into this folder that I'll have in the GitHub repo this is what I'll link in the description of the video and I will create a new file here I'll just call it n8n YouTube agent just

**[0:08:46]** some kind of random name I've got a couple other scripts already here just from when I was testing this earlier um and so now I can just copy and paste from Claude all the code that it gave me and I'm going to touch literally nothing besides the placeholders that it needs

**[0:09:00]** me to fill in here and so I'm just going to open up another one of these scripts that I already have just so I can copy the web hook URL which I showed you how to get an n8n and then the bearer token as well so this is everything after the

**[0:09:11]** bearer space that you set up in your credentials in n8n so you can see here that it's Bearer space and then the token that you set up in n8n of course I'm going to change this after so you can't just call my workflow and have the credentials for it um that's why I have

**[0:09:25]** it hardcoded here but yeah that is the only thing I'm going to change and there are a couple of pack packages that you'll have to install with python as well so you can follow the instructions from Claud on that or I also have a requirements. text file in this folder

**[0:09:37]** here so you can just do pip install dasr requires. text and then have the exact same environment as me because obviously this is working perfectly and yeah with that we can go ahead and run streamlet to kick off our front end all right so to run this script all I had to do is go

**[0:09:51]** into the directory where I have my python script and then run the command streamlet run and then the name of the script that instantly opens up an instance of in my browser right now have this very very simple chat widget you can expand this in a million different

**[0:10:05]** ways but we got the Bare Bones right now and we can talk to our agent so this is a full rag AI agent running as that NN workflow and so I can even ask it a question based on the documents that I ingested in one of the previous videos

**[0:10:18]** on my channel so I can say what are the action items from the 825 meeting and this is going to make that web hook request and anyn is pretty fast I'm using a fast LM and so we'll get a response very very quickly here there we go the action items from the meeting are

**[0:10:33]** and then yeah just some silly stuff that I generate with GPT but this is looking perfect and so now we can move on to adding superbase authentication and making this a lot more robust and secure something that you can really start to build and actually use in production for

**[0:10:46]** your business so back in Cloud because we are going to do a very similar thing to just enhance this whole streamlet app to include superbase authentication and there's a again a couple of specific things I've added to the prompt for things that I know well help clot a lot

**[0:11:00]** ways to prevent it from hallucinating and so I'll go over those very quickly as well and So within the prompt I'll just paste this in right here and I'll say now update this app to use superbase for authentication one thing that it loves to do is have a login Tab and not

**[0:11:14]** a signup so I tell it to do both here and then I also tell it to use the the user superbase token as the bearer token for the web hook so now instead of just having something hardcoded it's actually going to be a bearer token that we can

**[0:11:28]** generate with the superbase python library and so it's going to go out to our superbase instance and generate a unique bear token for that user that we can then verify in the back end in n8n that yes this token is valid and is assigned to this user and we can even

**[0:11:46]** get the user email and other profile information in the N workflow just from the barer token as well it's very powerful stuff that is still really easy to use and so you'll see that in a little bit here and then I also want to display a couple of pieces of

**[0:11:59]** information just to show you how robust this is like the user email in a left side panel and then sometimes Claude likes to hallucinate and use features that are deprecated so I just specified this at the very end here so with that I'll go ahead and hit enter and just

**[0:12:13]** like before it's going to generate all this code very beautifully on the right hand side here and it's going to look pretty similar except it's going to be a lot more robust now couple more placeholders that we'll need to fill in for super base overall it looks pretty

**[0:12:25]** similar like the send message to llm is pretty similar except we now have a new parameter of the token which we're going to get dynamically from superbase once we've actually signed in okay so I had to pause and come back so I needed to figure out exactly where everything was

**[0:12:38]** in this code but once they sign in that's when the user object is added to the session State and that's what has the token within it and so if I scroll down here when we call the llm we're going to get the user from the session State and then call the access token

**[0:12:52]** attribute of it and that is what we give to pass as a bearer token to n8n now and so yeah I don't want to dive into this code in a lot of detail but just looking at it initially this is looking absolutely perfect and so now I'm going

**[0:13:04]** to quickly show you what you have to do in the n8n workflow to work with this superbase authentication and then we'll set it up in Visual Studio code again and test it out so back in n8n now because I want to show you how easy it is to change up this workflow to work

**[0:13:18]** with this new super based beer token that is specific to a user instead of using that single hardcoded authorization Bearer token that we set up as a credential in n8n and so the first very important thing that you need to do is go into the web hook trigger

**[0:13:33]** and turn off that authentication because we're not going to have the web hook do the verification now it's going to be the step after it because we want to manually handle this new super base token so turn that off everything else can remain exactly the same now next up

**[0:13:48]** there's a couple of pieces of information that we need from superbase including our project URL and our API key and you can get both of these in the API settings in superbase so you just go to superbase click on Project settings and then go to API in the

**[0:14:04]** configuration and you can copy your url here I'll show you where to use that in a second and then for the API key you can copy so you can reveal and copy this service Ro secret that is your secret superbase API key that you can't share with anyone on the other hand the

**[0:14:20]** anonymous API key this is public as long as you have row level security defined on your table so people can't just read and write whatever and you can look that up and look into what it is then you can share this with anybody and so that is how we're actually going to have that in

**[0:14:33]** the streamlet UI later so this is public and this is your private API key that you want to pass in right here so I'm going to click into the HTTP request the headers that we have here to verify the users Bearer token is we have an API key

**[0:14:48]** and this is the secret that I have copied and pasted here from superbase I'm not showing the whole thing that's why I can reveal this here and then to verify a user's Bearer token we want to pass in their token as the author authorization for this call as well so

**[0:15:01]** the authorization and then the header is going to be json. heads. authorization so it's going to fetch the authorization from our web hook the superbase token that was passed in and then use that also as the authorization header for this HTTP call and the URL that we want

**[0:15:19]** to go to it's a get request that goes to our project URL slof slv1 user and so this is going to return to us a valid user object as long as this superbase Bearer token that was given into this N8 end workflow actually is assigned to a user and so what that looks like here is

**[0:15:41]** I have this if statement and basically if there is a valid user object that is returned there's going to be an email attribute and if there is an email attribute that means that the authentication was successful there are a lot of different ways to handle this but um yeah you can just check on the

**[0:15:57]** email essentially and that means that there's a valid user if there's notv valid user we can return with an error otherwise we can go on with the rest of our workflow exactly like we had before and we still have the chat input and session ID parameters and the payload to

**[0:16:10]** do everything else that we need for this AI agent the other thing that I want to mention very quickly and that's really it is that it's not necessarily ideal to just have your superbase API key pasted as the parameter here you could use another service like AWS Secrets manager

**[0:16:26]** to store this in a more secure place and fetch that in the work workflow and then pass that in as the value here I just wanted something simple but just keep in mind that there are ways to make this even more secure it still is pretty secure overall as long as your NN

**[0:16:39]** instance doesn't get hacked so with that that is everything that we have to change in the N workflow I hope that this makes sense how we are using this HTTP request against our project URL to verify the user let me know in the comments if you have any questions on

**[0:16:53]** that but let's go ahead and dive right into taking the cloud python code and updating our streamlet app so back in Visual Studio code I'm going to now take everything copied from CLA again and replace the file that I already had that just had the very basic authentication

**[0:17:08]** and now in this case I'm not going to go over all this code because it is looking perfect already um and so I'm just going to fill in the placeholders here and then we'll run it and test it out again and so again I have another script that's up already that I'm just going to

**[0:17:21]** copy everything from so your superbase URL and Anonymous authentication key I already showed how to get those so you'll copy those over from your superb interface and paste them in here and then the web hook URL is going to be the same if you just edited your workflow in

**[0:17:35]** place otherwise just copy that so I'm going to do that off camera and then come back once it is done so you can see here that I filled in all of my placeholder values it's going to look pretty similar for you and that is it there's nothing else that I have to

**[0:17:48]** touch in the code I know already that's working good because I I did test it behind the scenes so all you have to do to run it I'll open up my terminal again again just the same command streamlet run NN YouTube agent piy and then going back to my browser here we now have this

**[0:18:02]** view that presents us with a login and if I say something like test gmail.com and some random password that's invalid we get an error saying that it is invalid loging credentials maybe we'd want to handle this error a little bit better that doesn't look very good um and so there's obviously things you'll

**[0:18:17]** probably have to correct with Claude but Claude is very good at correcting itself but anyway I'll refresh here and then I'll log in with something valid so I'll say this is just kind of like a test account that I had created here so I'll log in with this click sign in and it

**[0:18:32]** says login successful but module streamlet has no attribute experimental rerun so this is something that I said Claud would hallucinate so again you kind of have to work with Claude a little bit I'm keeping this in to show that like it's not perfect right off the bat but Claude will correct itself and

**[0:18:46]** so I can even go in here and say um don't include experimental stuff and it'll correct itself so I'm going to go through this with Claude and then come back once I have it fixed all right so I work with it a little bit off camera and it corrected itself first try for the

**[0:19:00]** experimental reruns and I also had it fix up the UI a little bit as well I again wanted to leave that there to show that it really is an iterative process to build these things with clae but when you have a model as powerful as Claude it does a really good job correcting

**[0:19:14]** itself and not getting into an infinite Loop of hallucination and so with this I'm going to enter in my credentials again with this little test account that I have and we can go ahead and test everything else I'll go ahead and click log in and then boom there we go we got

**[0:19:27]** this beautiful interface that even shows me that I'm logged in with my email and my session ID too and this is looking really really nice so now I can ask it the exact same question what are the action items from the 825 meeting and oh nice it's even got a

**[0:19:42]** loading bar here this is looking really good and it's got all the super base verification behind the scenes in the workflow now and there we go exact same answer as before this is perfect I hope that this gives you a huge Head Start for developing really nice interfaces

**[0:19:57]** for your n8n AI agent there are a lot of opportunities to expand on this to give even more security or more robustness to your front end but this is a really good Head Start and I'm going to continue to make more and more content around n8n even talking about other platforms like

**[0:20:14]** open web UI to work with front ends for your n end agents as well so if you're looking forward to that and you appreciate this content I would really appreciate a like and a subscribe and with that I will see you in the next video
