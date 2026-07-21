---
type: raw-transcript
title: "Use ChatGPT in Two Clicks on ANY website with a Custom Chrome Extension"
youtube_id: 3kI14Jpzj_E
url: https://www.youtube.com/watch?v=3kI14Jpzj_E
slug: use-chatgpt-in-two-clicks-on-any-website-with-a-custom-chrome-extension
published: 2023-05-09
duration: "0:21:56"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I use AI models like chat GPT and hugging face every single day to help me accomplish a wide variety of tasks in my software development career but one thing that's really annoying is sometimes you're on a website in your browser and you want to quickly get some help from chat gbt for example but you

**[0:00:20]** have to go over to chat gbt's website their UI to interact with the AI you have to sign in and then you have to select the model you want to use and then you have to type out your prompt and then you have to take that copy it

**[0:00:32]** and then bring it over into whatever text box you were in before make your changes and then do whatever you're going to do that you want to chat gpt's help with it's not super annoying but when you want to do that repeatedly throughout the day it takes up a good

**[0:00:46]** amount of your time to constantly go back to the UI and get that answer and bring it back over to where you actually want to use it and so what I'm showing you guys how to create today is a Chrome extension that allows you to interact with GPT on any website without having

**[0:01:02]** to go to the openai UI or whatever other UI there is for a different model that you want help from and so how about I just show you right now what I mean so let's say I'm on Twitter and I want to quickly get chat gpd's help to create a

**[0:01:15]** new tweet well so I'll just say write me a tweet about artificial intelligence now I'll show you the power of the Chrome extension right here so I'll right click on this text box I don't even have to have the text highlighted and then there's this option here that

**[0:01:27]** you usually wouldn't see when you just have the vanilla Chrome that says Chrome GPT so I'll click on this and then it's spinning for a little bit and then it'll actually replace my text with its suggestion for the tweet that I could post now obviously this is an ideal like

**[0:01:43]** having quotation marks and things like that but that's because I don't have any prompting here this is literally just sending the exact text that you gave as the prompt GPT and then replacing what you have with the response but you can see how this could be used for a lot of

**[0:01:55]** different things too you could take this and add some custom prompt engineering to it or you could chain it with other large language models and you can do a lot of things behind the scenes and have that all be just under the hoods but you can use a Chrome extension to interact

**[0:02:09]** with the AI so we'll do another example here let's say I'm on a YouTube channel I want to write a quick reply to the video this is one of Alex harmosi's latest videos so I'll say write me a funny YouTube video reply about being broke so I'll do the same thing here

**[0:02:25]** wait a little bit and then it'll give me a hopefully funny response sometimes AI isn't the best at being funny but let's see what it does here for a YouTube video reply it's taking a while because it'll actually probably spit out a lot of text usually when it takes a while

**[0:02:39]** yeah it spits out a couple of paragraphs here so I'm not going to read the whole thing but yeah there we go even with a lot of text it can throw that in there for you and then just one more example here to really drive my point home of

**[0:02:50]** how useful this thing can be let's say you're an online code editor like this and you want to add an HTML div with a text time on and make the text Center because I don't want to actually send the entire text box here as the prompt because I don't want to include this

**[0:03:06]** stuff right here I'll actually highlight the text I want to send a GPT and then right click and click on Chrome GPT and you can see that almost instantly it was super fast this time it added this div right here with the center text saying hi Mom and if I scroll down at the

**[0:03:21]** bottom of my code pen here sure enough I got the text hi Mom so those are a few examples to really drive home how this can be used and why you'd want this so you don't have to go all the way over to chat.openai.com and sign in and paste in

**[0:03:36]** everything and then take the response back take some time and so now what I'm going to do is I'm going to show you guys how to create this alright so I am here in a blank slate in Visual Studio code the only thing I got here is the

**[0:03:49]** PNG which is going to be the icon for the Chrome extension I'll just use the same one that I had for my quick demo I had at the start and so we'll do everything from scratch here and then also at the end of this tutorial series trees will be a couple of videos because

**[0:04:01]** you can get into a lot of depth with this I'll actually make a public GitHub repository we'll have all this code so for now I won't have anything available but at the end I will but you can also code along with me so let's go ahead and get started right now so making a Chrome

**[0:04:15]** extension is not actually that difficult before I've done any kind of this Dev element before I thought making extensions would be difficult like how do you integrate with chrome itself do you have to know about all the different code within Chrome or do you have to know how to integrate with different web

**[0:04:32]** pages I was confused on that part but it's really simple so let me show you the first thing that you have to do is you have to make a file called manifest.json now this file is basically the metadata about your Chrome extension it tells Chrome what version of the

**[0:04:48]** extension machine do you want to use it tells Chrome where to get the icon for your extension it tells it what files it's going to reference like the JavaScript and the HTML and the CSS for your extension all that good stuff it's the backbone of your extension and like

**[0:05:05]** I just mentioned the extensions are made with HTML CSS and JavaScript so it's just like making your websites there's no other fancy technology you have to use like I thought there might be when I first started making Chrome extensions so let's get started coding the manifest.js all right so the first thing

**[0:05:22]** that we need in this file is simply a couple of parameters that Define things like the Manifest version the name of the extension the version of our extension and then the permissions that we need and so there's quite a few things here I won't get into the details

**[0:05:37]** of the permissions but depending on what your extension needs to do how it needs to interact with the browser or pages of the browser you might need different permissions here and then the next thing that we need is we need a section that defines the icons for our Chrome

**[0:05:52]** extension you can also Define what icon to use for different resolutions of the icon in my case to keep things simple I'm just going to use the the exact same PNG file for these different resolutions but I just wanted to show you that you could have different ones next up this

**[0:06:07]** is one of the important pieces of the Manifest where we actually start to reference some files that will be creating code for the first one we have a service worker which is background.js now the background.js file is going to be responsible for creating the infrastructure of our Chrome extension

**[0:06:24]** so this is where we'll actually say when you right click on Chrome there's going to be this new Option called Chrome GPT or whatever you might end up calling it and then finally and this is it this manifest.json is pretty small we have the content scripts and so here's where

**[0:06:40]** we actually have the code that does the work for us so the background.js says when you right click there's this option called Chrome GPT and then when you click on that option background.js sends the work to content.js which will actually make that query to GPT get that response and then put it back in the

**[0:07:00]** text box that you have as your active element when you're interacting with chrome GPT so this is all we need next we can go ahead and make a file called background.js and we'll add that code to tell Chrome that this extension has an option when you right click called

**[0:07:17]** Chrome GPT and this file is pretty small so the first thing that we need to do right here is we need to create a context menu item the context menu that is what you get when you right click on Chrome the menu of all the different options that you can select there and so

**[0:07:32]** we'll add a new item to this menu with an ID of chrome GPT a title of chrome GPT and then a context of all and you can dive into the documentation if you want to understand the different contexts here I'll just keep it simple and not go into that and then if you

**[0:07:48]** wanted to create multiple for example you could just call this function again with a different ID and a different title so for example if you wanted to extend this to have specific prompt engine engineering for tweet replies for example you could create another option here and so then when you right click on

**[0:08:05]** Chrome you would see Chrome GPT which itself would be a drop down where you could say Chrome GPT or Chrome GPT tweet reply next up what we need to do is we actually have to create a listener for this new context menu item so when you actually click on this new option in the

**[0:08:23]** right-click menu what we want to do is say if the menu ID is Chrome GPT so if you clicked on Chrome GPT then we're going to send a message and this is going to go to the content.js file will write in a second we'll send a message saying hey we've clicked on Chrome GPT

**[0:08:40]** now you need to do the work of actually parsing the text in the text box talking to GPT and then giving back that response and then just to give another example quick if we had the Tweet reply option too that would just be another else if so if it's Chrome GPT and that's

**[0:08:58]** based off of the ID right here then then send this message to content.js if it's Chrome GPT tweet reply matching this ID then send this message to content.js so that's it that is all this background.js file has to do now we actually get to implement the real work in the

**[0:09:15]** content.js file so we'll make another file right here called content JS and now we'll actually get into the meat of this extension so first of all we need to be able to receive the message from background.js so the first code we have right here is we're adding a listener

**[0:09:31]** for the Chrome runtime Whenever there is a message and that message comes from the background.js file so when we say chrome.tabs.send message that's going to activate this listener right here and if the message type is Chrome GPT then we do all the work for this extension and this chrome GPT type matches exactly

**[0:09:53]** with what we're passing in right here so you can see how these two are very intricately connected these two files are the core of this Chrome extension application and so I'm going to put in quite a bit of text here but this is the first part of actually running this

**[0:10:07]** extension so first of all we have our text box options of text area and input so those are the different HTML element tag names that could be text boxes that we're interacting with that we want to get a GPT response from and so then what we're going to do is if there is an

**[0:10:26]** active element if the user is clicked into one of these text box then we want to store that text box because that's where everything is going to happen for this extension and also if the user hasn't highlighted any text then we'll just consider all of the text in that

**[0:10:44]** active element to be what we're going to replace with the response from GPT but if they have highlighted a specific portion of text within a text box only that is going to be the actual prompt and what we replace with the response from GPT and so that's what this

**[0:10:59]** participated of text does right here and so if we haven't actually found the prompt from the user so if they don't have an active text box with text in it or there isn't anything that's highlighted then we send an alert to the user and tell them that they don't

**[0:11:15]** actually have a prompt and therefore they have to do something different to really use this extension like they have to actually highlight some text or be within a text box next up what we do at this point we know that we have a prompt to send a GPT we have a valid piece of

**[0:11:28]** text and so this bit of code right here this actually sets that loading cursor so that the user knows that it's making that request to GPT because it takes a bit of time we don't want to just make it seem like nothing is happening so that's why we have this code right here

**[0:11:42]** next up we actually make the request to an API I'm just going to use the localhost right now and Host this API on my own computer and I'll show how to do that in a second it's really quick to set up and so this is the general format

**[0:11:57]** that you do for fetch requests in JavaScript we're making a post request with these headers and then our body is simply going to be the prompt which is the prompt that we just fetched in the code up here based off of what the user has in their text box or what they have

**[0:12:12]** highlighted and then it always works this way where you have two thens in your code you have the then where you accept the response and you turn it into Json and then the next function call actually takes that Json data and does the real work and that's what I'll show

**[0:12:28]** in a second here now you don't have to do it this way but this is very common practice for fetch requests with JavaScript and so now what we're going to do is we're going to get the active element because now that we have the response from GPT we need to replace

**[0:12:43]** that text with the response so if there is an active element then we need to actually do the job of taking the response from GPT and putting it in that active element replacing anything that was highlighted by the user and and so then if there's not an active element

**[0:13:02]** that means that we rely on them actually highlighting a certain bit of text and so that is what this code does right here that it's with the content editable type of HTML attribute it has to be handled in a little bit of a different way I don't want to get into the details

**[0:13:16]** a ton here because I want to keep this video concise but just know that with content editable it just has to be handled in a little bit of a different way where you use the concept of a range where you don't have to do that with text areas or input elements in HTML and

**[0:13:33]** so now at this point no matter what kind of text box the user is working with this will take the reply from GPT and put it in where they have their highlighted text or the entire text box if they haven't highlighted anything what this does right here is if there's

**[0:13:47]** no text box to put the code in and if the user hasn't actually highlighted anything that we could replace we just tell them through an alert message what GPT replied with and then at the end we just remove the loading cursor very simple now this is the part that I meant

**[0:14:03]** to explain right here we catch the error from the JavaScript fetch so if there was an issue getting the response from the API we just log the response remove the loading cursor and then we Alert in the browser the error from getting the request from chrome GPT something that

**[0:14:22]** the API would return that we would then display to the user so they know what exactly went wrong hopefully that'd be something useful but at this point that is it we have the complete Chrome extension and so now the only thing we have to do before we actually use this

**[0:14:35]** is create that API for making the requests to GPT and so we'll do that really quick it will not take very long alright so for the API I'm just going to create a very simple express.js API if you don't know what Express is just feel free to give it a Google because it's a

**[0:14:52]** really powerful JavaScript API framework and I'm just going to use a very basic example of it to get us up and running here so one thing I do want to note is that you do have to have a DOT EnV file here the same directory as server.js where you would give your openai API key

**[0:15:07]** and openai organization so when you have an account in open AI you can get both of these things very easily it will cost you money keep that in mind this is not free but it is not very expensive especially if you're just toying with it a little bit to learn how this kind of

**[0:15:20]** thing works so anyway you can get to the server.js here first of all there's a few libraries that I need to import like I said I'm using Express I'm using body parse and cores which are extensions of Express to make this work very simple things and then I have the libraries

**[0:15:36]** from openai or the packages from openai configuration and then the actual class for the openai API and then next I'm using a library called dynb safe this is going to handle our EnV environment variable safely and then next I'm going to actually set up the openai API so

**[0:15:56]** here I'm using those environment variables to get an instance of the open AI configuration and then creating the API from that here and next we actually get to use express to create the app which will have some code to run it in a second here and you can see this is

**[0:16:12]** where we're actually using the extensions of cores and body parser and then we're saying from the model we want to use GPT 3.5 which is chat GPT and then the port that we're going to host this on is 3000 because if we're going to go back to the Chrome extension code

**[0:16:27]** if you remember in our fetch we were fetching localhost 3000 so that's the port honor computer hosting this API and so now we actually have the code that I'm sure anybody who's used Express is very familiar with and that is app.listen on this port and then this is

**[0:16:42]** the message that we print when it's actually ready to start receiving requests and the way that we add the ability to receive requests is with just an app.post so remember this is a post method if it was a get method it'd be app.get and then this is just the root

**[0:16:56]** directory of the API so it'll just be localhost colon 3000 slash and then that'll get us to this endpoint right here and all we need to do in this endpoint is we need to make a request to open AI so I'm using the chat completion function with the model and then the

**[0:17:13]** message is simply going to be the prompt attribute of the request body which we have set up in the Chrome extension and then for a maximum number of tokens this just dictates how long the response and the request to open AI can be together I just edit at a thousand but this isn't

**[0:17:31]** like a value that I did a ton of math to figure out I just threw that there and so once we have this response from open AI based off of the user prompt given from the Chrome extension we just need to fetch that reply I'm just doing a

**[0:17:44]** console log here so we can see on the API side what the reply is and then we just send that as a response back to the front end trimming the start because sometimes open AI likes to include some white space before the actual text of the response for chat gbt so that is all

**[0:18:00]** that we have there and then to actually run this code all we have to do is go into a terminal so I am in the terminal right here where I have this code and then I just have to do node server.js and you can see that it console logs

**[0:18:14]** Chrome GPT API listening a port 3000 and we now know that we are ready to make requests to this API to get a response from GPT based off of a prompt that we give it in the body of the request very simple so now we've actually gotten to

**[0:18:28]** the point where we can upload this extension to Chrome and start using it alright so the place that you go to manage your extensions and upload your extensions is this URL right here just Chrome colon extensions and you can see I already have my Chrome GPT 1.0 uploaded here for the demo that I had

**[0:18:48]** already given you guys but just to do this all from scratch with you I will remove this and then I will upload it from scratch with the code that we had just created together and so what I want to do is click on this load pack button right here and then I just have this

**[0:19:02]** Chrome extensions folder this is the silly name I gave for the demo this is the one that we actually were working with the code I created just now so you don't actually have to go into the folder you can select the folder itself that has your manifest your

**[0:19:16]** background.js and your content.js files along with your icon as well and so I'll select this entire folder and now you can see that what appears here is like just what I deleted because it's all the exact same code you can even click on the service worker to get the

**[0:19:31]** console.logs from your extension so if you want to do any debugging this is how you do it as well and so now what we can do is actually go back to one of my previous examples and see if it works exactly the same way as it did in my

**[0:19:43]** demonstration so I'll highlight this text I'll right click it and I'll click on Chrome GPT and it turns out that it's not working and so the reason that this is not working is because I need to actually refresh my page to load the new extension because it's actually you try

**[0:19:59]** to reference an old extension so I'm going to copy this and I'm going to refresh it so I'm going to get the blanks of this code snippet and codepen that I had and then I will paste in my prompt highlight it and then do Chrome GPT and there we go now it's working

**[0:20:15]** exactly as we had before in my demonstration and you can see that the high mom text is at the bottom and so that is it if you follow it along you have now successfully created a Chrome extension to be able to interact with GPT on any website super cool stuff now

**[0:20:31]** anything that I can do in a 20 minute tutorial is honestly pretty basic obviously it took me a lot more time to develop that from scratch so I can then show it to you but there are a lot of opportunities to build on top of this to really make an application that you can

**[0:20:46]** then productionalize and sell to people one thing you'll have to do is you'll have to actually make the API out there somewhere on the internet not just running on your computer you're also going to have to include authentication for this extension using a tool like Firebase for example and then if you

**[0:21:00]** want people to pay for it you'll have to integrate it with something like stripe for credit card payments so there's a lot of things you have to do to actually take this forward into a production application but this will lay down the foundation for you to do anything to

**[0:21:11]** build on top of it in any way you want for custom prompt engineering for things like tweet replies or creating emails you could even do something like YouTube video summarization by taking advantage of the subtitles that you have on YouTube videos so you could like right click on a YouTube page and click

**[0:21:26]** summarize this video or maybe even have it in like a text box on the side of the video tools like Merlin have for example there are a lot of other Chrome extensions that already do cool stuff so you can use that for inspiration too for whatever you want to make so I hope you

**[0:21:39]** guys find this super helpful make sure to like And subscribe if you did and stay tuned for the next video for this series we'll actually take this a little bit further and do some more cool stuff kind of like some of the things that I was talking about already so thank you

**[0:21:52]** guys for watching and I will see you in the next one
