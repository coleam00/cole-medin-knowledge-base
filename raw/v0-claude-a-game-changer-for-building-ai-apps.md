---
type: raw-transcript
title: "V0 + Claude: A GAME CHANGER for Building AI Apps"
youtube_id: BpVuhKbSVS4
url: https://www.youtube.com/watch?v=BpVuhKbSVS4
slug: v0-claude-a-game-changer-for-building-ai-apps
published: 2024-09-08
duration: "0:21:40"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** if you're interested in building AI apps and you haven't heard of vzer at this point you are probably living under a rock this platform makes it so so easy to use AI to build robust front-end components or even build entire front ends everything it creates are Shad CN

**[0:00:16]** components that you can bring into your own project and customize super super easily and it's a huge plus that Shad CN is just an incredible component Library we'll also be using CLA because it pairs really really well with v0 for some of the small details and honestly Claude

**[0:00:32]** 3.5 sonnet is hands down the best large language model for working with code so anyway let's face it you and I would rather be spending most of our time building our AI agents but we know that building a front end is necessary as well no one is going to use your AI app

**[0:00:47]** if it's ugly and vzero combined with Claude has literally saved me hours and hours of coding my nextjs front ends which is an absolute Lifesaver for me because generally I would much rather be spending my time in the back end working on my AI agents so if that's you as well

**[0:01:02]** definitely stick around because I'm sure that you're going to be liking this just as much as I am so what I'm going to show you how to do today is create a fullblown user interface to chat with the rag AI agent that I built in the last video on my channel using n8n and

**[0:01:15]** super base the UI is going to be really clean and simple and I'm even going to use vzer and CLA to add user authentication to the front end and use the authentication to manage the agent's chat memory for each user all in just minutes so it's going to going to be a

**[0:01:30]** really good example of how you can super quickly build something that's more than just the bare bones using Claude and VZ so without further Ado let's Dive Right In all right one of my favorite Parts about this vzer and Cloud combo is just how easy it is to get started you just

**[0:01:45]** need two tabs open up in your browser I've got vz. deev chat and then also claw. new very easy to remember URLs keep in mind that there's a different version of vzer if you don't go to the chat page if you go to just vz. deev that one I don't like as much they made

**[0:02:03]** a lot of improvements recently to VZ which you can find in the chat version specifically so there's been a lot of critique of vzero in the past of it not working very well in generating mioc UI but with a lot of the recent changes versell has made to vzer it is starting

**[0:02:17]** to work really really well hence why I'm making this video right now so I'm also going to have a link in the description of this video to a GitHub repository where I'm going to have all the prompts to vzero and Claude in a text file there I'm going to also have the end end

**[0:02:33]** workflow and I'll show in a little bit downloadable for you and then lastly all of the nextjs code that we generate I will also have in the repository as well so with that we can go ahead and get started with our first prompt to v0 so I'm going to start with a very basic

**[0:02:47]** example and then we'll build on this with prompts as we go to make it the fully robust application with authentication that I described at the start of the video so at first we're just going to create a basic chat bot and I describe a little bit of how I

**[0:02:59]** want it to to work and then it's just going to respond with placeholder messages right now and then later on we'll actually hook into the NN workflow for the rag AI agent so I'm going to send this and then what it's going to do is open up a page kind of like chat gbt

**[0:03:13]** domcom where I can just talk to this AI as it is building this front end component for me and you can literally see it writing the code as we speak which is so so cool and then it switches over to the preview tab so it shows me the front end as it's building it out in

**[0:03:26]** the code so I can switch between the preview and the code and watch a code and real time so I just love the whole interface they have here it's really easy to work with um and it's cool to see it just type away for me so what I'm

**[0:03:38]** going to do here is just fast forward once it is finished coding everything for me all right so just a few seconds later and it is done so now I can go over to the preview tab here and we've got a chatbot the UI is very barebones at this point but it is actually quite

**[0:03:52]** easy to make it look good just with prompting it more but we can start by testing this out so I can say something like hi and it doesn't really matter what I do because it's it's going to follow my instructions and just have it respond with a placehold message for now

**[0:04:04]** but this is working exactly as I asked it to so this is a really solid start all right now we wanted to actually interact with the rag agent that I have built within n8n so what I'm going to do really really quickly is give a brief overview of this agent that I have in

**[0:04:19]** n8n and then we'll prompt VZ again to change this so instead of just responding with a placeholder it'll actually invoke the web hook for my n and workflow to get a response from the agent there and so going over to my NN tab here let me zoom in for you uh what

**[0:04:34]** I've got here is pretty much the exact same workflow that I built in the last video on my YouTube channel so go ahead and check that out if you are interested how this works I'm just going to give a really really brief overview at this point so the way that this agent works

**[0:04:47]** is we have a chat input that can come in either through the chat widget in NN which is this widget right here or through a web hook that I added specifically for this use case and so the web Hook is basically going to to accept two parameters the session ID and

**[0:05:03]** then also the chat input the session ID is what's used for the chat memory and then that's fed in this agent which uses GPT as the AI you can use really anything you want and then we've got chat memory with postgress and then rag using superbase for our Vector DB and

**[0:05:18]** then it just responds with a web hook where it has just a single output parameter and that's what we' feed back into the front end to display the response to the user and then the way that we ingest documents for rag is we have a this folder that we're watching

**[0:05:31]** any file Creations or updates and those are going to get fed into the vector database uh through downloading it on the n8n instance and extracting the text from csvs PDFs text files whatever it might be so that's everything for this workflow and so now we need to prompt v0

**[0:05:49]** on how to update the component to actually interact with this web hook here so if I double click on the web hook I can get the URL that I need to invoke to reach out to this agent and then also so I have header authentication set up through a specific

**[0:06:02]** Bearer token and so I'm going to have that in the prompt as well so I'll switch back over to v0 and then I'll paste in the prompt that I have the second prompt here so I'm going to tell it basically to create the same chatbot functionality but this time to invoke

**[0:06:16]** this agent using this as my Bearer token so I just have something hardcoded here to make a quick example obviously you'd not want to have your authentication token just in plain text generally but I want something quick here so in a C application you do this a little bit

**[0:06:31]** differently but anyway that's how the authorization works and then I'm telling it the inputs into this web hook which is like I said before the session ID and the chat input so let's go ahead and hit enter here and now see what it does to actually update the code so it's going

**[0:06:46]** to basically give its thoughts as it decides how to modify the code and then it'll rewrite everything from scratch as you can see here and hopefully most of what we see will look the same but it's going to have all the new functionality baked into it as well so I'm going to

**[0:07:00]** fast forward and we'll come back once this is done it is done updating my component and now this time instead of running it within the browser I'm going to actually download this and create my own nextjs project on my laptop with this as one of the components and it's really really

**[0:07:16]** easy to do this with v0 all you have to do is click on the install button in the top right and then copy the npx command that it gives you so you're going to want to have npm installed on your machine but it is very easy to do that

**[0:07:28]** and that is the only dependency to get started with this and so I'm going to open up a terminal here and then paste in the command that it gave me and this will actually create a brand new nextjs project in this folder since I don't have one yet and it'll install Shad CN

**[0:07:41]** along with it and then also it will create everything that I need for my next JS project and so yep sure enough it says it doesn't have a next chass project so I'd like to create one I'll call this uh v0 agent front end and then it's going

**[0:07:57]** to just go through a couple of other settings so I'll fast forward through that really quickly all right there we go so now I'm going to go into my VSS code and we can actually take a look at this and see what it has made for us so let me zoom

**[0:08:10]** in a little bit for you here just that it's easy to see so I've got my vzer agent front end folder here and then within it I have a brand new nextjs project and then if I go into components I have my AI agent chatbot now this is

**[0:08:23]** the component that we actually created in vzer that is embedded within this nextjs project so we have a couple of errors right away this is uh something kind of strange that I've noticed with v0 is when it Imports strings into a component um when you do the npx install

**[0:08:38]** command it has the double quotes and then single quotes and so really quick trick here that you can do to get rid of this is you can do a find and replace in vs code so I can replace all double quote single quotes with just double quotes and then I can replace all of my

**[0:08:52]** single quote double quotes so the other way also with double quotes and so this will get rid of pretty much all the errors we have here except for one at the top um for some reason sometimes VSCO doesn't recognize when packages are installed but if you really want to make

**[0:09:04]** sure it is installed you can also do an npm install - s and then the name of the package so in this case lucide react and this is for one tiny part of this component but we still need it so we'll go ahead and install it now all right so

**[0:09:18]** with that installed we can go ahead and run the command to start our nextjs app locally so we run npm runev and this will spin up the server on Port 3000 Local Host so now I can go back to my browser are here open up a new tab go to

**[0:09:32]** Local Host 3000 and it'll take a little bit to compile and then sure enough here we are with our AI agent chatbot again the UI isn't the best at this point we can go ahead and test this thing out so I'll say hi and see what we get as a response

**[0:09:45]** from our llm there we go hello how can I assist you today and I can even go over to my n8n and go to my executions and sure enough just a tiny tiny bit ago we had a successful execution starting from the web hook here let me zoom in starting from the

**[0:10:01]** web hook and then we got the response of hello how can I assist you today just like we saw in our front end I can even ask a question using rag like what are the action items from the 825 meeting let's see if it can do rag just like we

**[0:10:16]** had in my previous video on my channel where we had the chatbot within n8n and there we go it's not formatted really nice but we got our action items and this is exactly what I have in the Google Doc in my Google Drive that I've ingested into my superbase Vector data

**[0:10:29]** database so this is looking awesome so at this point you might be wondering where Cloud comes into the picture and we'll get to this in a little bit because what we're going to do now is get a little more complicated with the requests to v0 to start making the front

**[0:10:42]** end look better and also add authentication and sometimes v0 will trip up and that's when we can really use CLA to help fill in the gaps because it is so detail oriented when it comes to code and so what we're going to do right now is go back over to v0 and

**[0:10:55]** we're going to make some enhancements with another prompt here so I'm going to paste this in right here first thing that I want to do is actually parse the AI responses as markdown so if you go back to the app this just doesn't look very nice right now um we're also going

**[0:11:08]** to make the UI a dark theme and add a navigation header and also we're going to add a sidebar so just making the UI look more full and then we can fill it in with things later when we actually take the app to production and so I'm going to go ahead and enter here and

**[0:11:21]** just like before we're going to get to watch in real time as it updates the code all right so it's made all the updates for so we'll go over to the preview Tab and sure enough this is looking a lot lot better and so we can even like see the left sidebar here um

**[0:11:38]** really really nice looks like there's not a way to close it so maybe that's something we'd want to correct later I'm not going to focus on that right now uh one thing it did tell me though is that I need to install react markdown now as another MPN package to make this work so

**[0:11:50]** now to actually bring this into my nextjs project it's really really easy I don't even have to install this again all I can do here is just go back to the component file click on the copy icon on the top right and then go back over to vs code and then replace everything that

**[0:12:04]** we currently have in there with what I just copied from the vzer UI and so with this now I'm going to have to install react markdown and then also restart my server so I'll go back in the terminal here I'll close out of this and I'll do mpm install react

**[0:12:21]** markdown and then once that's installed really really quickly we can go ahead and run the mpm Run Dev command again to spin up our server uh on the local host Port 3000 again so I'll go back over to my browser here go back over and refresh and let's see if it works

**[0:12:37]** without any issues so it's recompiling the site and we'll see if we have any luck here we do not we have our first error so what I'm going to do here is I'm going to go back to the code analyze it and then figure out what I need to

**[0:12:50]** send into Cloud to actually help me fix it all right so looking at my terminal here it looks like I have an import error so what I'm going to do here is instead of going back to v0 which might work I'm going to go to Cloud because with the little details like this that's

**[0:13:03]** where Claud really really shines now I don't want to use Claude to make this entire thing for me because I really appreciate the UI of vzer and it's custom tuned and trained to make these Shad CN components that are really easy to import but I can use it for the

**[0:13:17]** debugging so that's what we're going to do here so I'm going to start by copying this error that I'm getting I'm just going to copy the error message go back over here into cloud and paste that so I'm going to say I'm getting this error with this nextjs component and then I'm going to

**[0:13:35]** paste in all of the code of this component so I'll go back over there copy everything go back to my browser doing a little bit of dancing right now paste it in it looks like I added a file I don't I meant to paste in the text but

**[0:13:47]** this should probably work as well so I'm just going to hit enter and see what it does for me to help me fix this error all right so it spit out a lot here and I love how it starts the response by saying that it wants to look

**[0:14:01]** over the code and then it prints it all on the right side here cloud has a really nice UI just like vzer different purposes you're not going to be able to really build components as nicely in Cloud but for debugging this is really beautiful so the issue basically is just

**[0:14:15]** how we are importing AI agent chatbot in whatever script we have in our project that's actually taking in the component and so what I'm going to do here is I'm going to read through everything that I gave here go back into my code make the fix and then we will Rec compile it so

**[0:14:30]** Claud got the error exactly right it had to do with the Imports like it said like I suspected from the error message where specifically we either have to remove the default here from the export or in the page. TSX file where we import AI agent chatbot we have to remove the

**[0:14:46]** curly braces because this is a default import now and so we import it directly from the um AI agent chatbot file instead of deconstructing an object of the exports from this file so with that that'll get rid of the error and I also used Cloud to fix an error where it was

**[0:15:01]** saying that the variants didn't exist on the buttons and so I did that off camera just to not spend more of your time there um but I use CLA to fix a couple of things here so that's really showing the power of using it with vzer to really make a powerful combo and so with

**[0:15:15]** that now I'm going to restart my browser here and so I'm going to say mpm runev again it'll spin it up I'll go back over to my browser refresh the page here and this time we should have zero errors so let's see what happens after after it compiles there we go all right this is

**[0:15:33]** looking a lot better now so it's still a lot of placeholders for things here but this is looking really really nice so let's test it out again so I'll say hi make sure we get a response from our na end workflow again and yep sure enough we do so this is looking really really

**[0:15:46]** good so now the last thing that I want to do is actually add a superbase authentication and use the authentication for the user to get their session ID and use that for the session ID for the chat memory so we're back in our v0 UI and this is the last prompt

**[0:16:02]** that we're going to do today so I'll paste it in here I'm basically just saying add the super base authentication so that they have to sign in before using the chat bot and then also use the session ID of the user for the superbase chat memory session ID so just showing

**[0:16:15]** what that's like quickly in our workflow here um what we have for our postgress chat memory is it takes the previous nodes session ID parameter to manage the chat memory so basically any user using this app is going to have their own session ID and therefore can remember

**[0:16:31]** the chat memory for specifically that user so this is a very specific addition to the app but I just want to show how you can do really specific things with vzer and CLA and it's not limited to just Bare Bones creating a front-end component so with that we can go ahead

**[0:16:46]** and hit enter and it's going to recreate the component just like usual this time adding superbase authentication all right so it is done creating the updates here for the superbase Authentication and I actually don't like what it did here because it didn't use super base's default Library helper for authentication instead it

**[0:17:07]** created a custom component for email and password when I really want to use what superbase provides to me so I'm actually going to say that I'm going to say change this to use superbase directly for authentication instead of creating a custom login component cuz I know that it's possible with superbase to not

**[0:17:28]** actually have to code the component from scratch let's see if it can fix it for me right now all right this is looking much much better so now it is not a custom UI for the login it's actually using super base we don't see anything here but we're

**[0:17:45]** going to bring it into our next JS project add these environment variables like instructed and then we'll go ahead and test it out again all right so I have followed all the instructions it has given me and this is not super super basic stuff cuz I had to actually go and

**[0:17:59]** create create a new file a route for the call back to handle the authentication then I had to create a local enem file with my superbas URL and Anonymous key which I'll show how to get in a second here um so there's a lot of setup that I

**[0:18:11]** had to do and it walked it through for me perfectly so I was able to follow this and get it to work first try with no issues which is really really impressive and so again I have all the code for this in the repository that I Linked In the description so you can go

**[0:18:25]** through that instead of having to set everything up yourself and walk through VZ yourself but really quickly how you get these two things in superbase is you're going to want to go to superb.com and sign in with GitHub create your account it's free and really easy to get started and

**[0:18:39]** then within here you're going to go to your project settings on the left hand side once you're in your dashboard and then go to API and then your project URL is right here and then your Anonymous authentication key which can be public external in your browser in people's

**[0:18:54]** browsers as long as you have Road level security enabled but you just copy that here so you'll put both of these in the. loal file in the root of your nextjs project and then as long as you have this route for the call back for handling authentication you are good to

**[0:19:09]** go and let me just show the code here quick because this is exactly what I was asking for so you sign in with super base and then it sets the user based on whoever signed in and then it uses the session as a part of the request to my

**[0:19:23]** n8n workflow um so user. ID is the session ID and so that way I can manage the chat history for each user separately it's a very beautiful thing so going back to the browser here I have done an npm install of all the new things that I need from super base and

**[0:19:39]** so I've got all that working now so I've restarted my server and here we are local hostport 3000 and now presented with a signin page before we can access our chat bot so you can sign up with an account here I've already done that so I'm just going to go ahead and enter in

**[0:19:53]** my email and password right here and then once I sign in there we go presented with my app again and this time I'm actually logged in as a user and that is going to be my session ID so I'm actually going to show this here because this is just so so cool to me so

**[0:20:07]** if I go into my table editor into my NN chat histories table I've have completely cleared it at this point so now I'm going to send a message I'm just going to say hi I'll get a response from the llm again and I'll go back to my database and now I have two records here

**[0:20:23]** and the session ID for both of them is it starts with ab7 cc5d so I'm going to open a a duplicate tab here go to my authentication look at my user that I added and sure enough the user ID here is matching exactly with the session ID in this chat so this is

**[0:20:43]** working perfectly this is just amazing I've built this thing in just minutes with vzero and Claude And there's a lot of way to go to make this a production front end but you can see how this would save hours and hours of time I could continue to work with vzero and Claud to

**[0:20:57]** build this thing out make the navigation actually do stuff make the sidebar actually save my conversations um and overall this just saves so much time and is really fun to work with as well all right that is a wrap for the vzero and Claude combo to build this front end for

**[0:21:13]** my rag agent I would really encourage you to just play around with this find ways to extend it or just use vzero and cloud in your own ways to save yourselves hours and hours of time building your front-end apps you can focus more on your AI agents a lot more

**[0:21:27]** content on my channel coming out soon for things like this working with rag local llms so if you're looking forward to that and you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
