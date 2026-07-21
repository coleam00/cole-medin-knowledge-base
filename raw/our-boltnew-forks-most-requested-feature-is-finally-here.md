---
type: raw-transcript
title: "Our Bolt.new Fork's Most Requested Feature is FINALLY Here"
youtube_id: nkqQfABopyc
url: https://www.youtube.com/watch?v=nkqQfABopyc
slug: our-boltnew-forks-most-requested-feature-is-finally-here
published: 2024-12-01
duration: "0:15:25"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** over the last month and a half we as a community have been knocking it out of the park building up autod Dev our forab Bolton new which we are building to be the best open-source AI coding assistant and one of the most requested features to add to autod Dev is the ability to

**[0:00:16]** load existing local projects into the platform so that you can continue to work on them within autod Dev and I am super happy to announce that it is finally available this super highly requested feature is now ready for you to use thanks to Edward one of the core

**[0:00:33]** maintainers of autod Dev who also has his own YouTube channel that I'll link to in the description of this video cuz I really want to give credit where credit is due it is so awesome that we have this now there are also a lot of other incredible people making equally

**[0:00:46]** amazing contributions to autod Dev so we're going to dive into all of this right now and also a couple weeks ago we started a road map for autod Dev just to lay out the vision and at the start of that road map is a bunch of really high

**[0:00:58]** priority features that we've already started Ed to knock out these are the things that we really need for autod Dev to make it a mature project so I'm super excited to show them all off and talk about what's going on also really exciting developments on the horizon for

**[0:01:11]** autod Dev very soon here we are set to announce a strategic partnership that is going to absolutely supercharge this project beyond what I could have even dreamed of when we started it's really a best case scenario really looking forward to announcing this to all you very soon we are still figuring out the

**[0:01:28]** timing and logistics for everything and and so that's why I can't speak to it a ton right now but later on this video I will talk about how it is going to help autod Dev and really turn it into the mature project that we are all looking for really exciting stuff so with that

**[0:01:41]** being said let's dive into everything we've got all right so let's Dive Right into testing out this new local project load feature and I'll also showcase some other features as we're going through this example here because you can see looking at the UI there is a lot of work

**[0:01:56]** that has been done on autod dev since the last time I made an update video so many cool features here we've got importing chats which you can export by the way as well once you're actually within the coding view import folders that's what I'm about to show here a lot

**[0:02:09]** of really neat UI changes to make it more similar to the commercial bolt. new um also if you go into the chat history here you can search through your chats now you can collapse the model settings so you have more room in your UI and yeah so many cool things here a lot more

**[0:02:24]** once we actually get into the coding as well and so yeah let's go ahead and import a folder so I'll click on import folder and I've got this example project right here that I'll select I actually built this in autod do so I built it exported it and now I'm re-uploading it or you

**[0:02:38]** could upload something that you built with bolt. new or you coded yourself whatever you want to do so I'm uploading 13 files into this site I'll click on upload and boom there we go it loaded everything in and it also understands all the files that imported as well so I

**[0:02:51]** could say something like describe these files and it's going to have all that context it needs to continue from where we left off with whatever I in imported here and so yeah it totally understands what's going on here which is super super nice the one thing I'll say there

**[0:03:06]** is a limitation to bolt. new as a whole when it comes to loading in projects you're not going to be able to load in massive massive projects because that's just going to crash the site as it's trying to import all the files and so make sure that you keep it to I don't

**[0:03:21]** know maybe less than 100 files just to be safe also don't bring in your entire node modules folder because even though we have an ignore setup to not take in you know like GitHub or node modules folders and things like that it still has to be brought into the front end

**[0:03:35]** before it can be filtered so just keep in mind keep your Imports Nimble and then it'll work really really well um so yeah I can toggle the model settings here nice little UI change and them yeah we can look and see its answer and yeah it totally understands and it can even

**[0:03:48]** extend this so I could say extend this to improve the UI I'm just giving you something very generic here just to show that it's able to work with these files as well it's not like it just understands it it's actually as if we coded this in entire thing and we're

**[0:04:01]** just continuing on in the conversation so absolutely beautiful also some other features here you can revert to a specific message in the conversation which is really really helpful because if it messes up and you just want to scrap what it did in the last message or last couple of messages you can do that

**[0:04:17]** you can Fork the chat from this message as well really really awesome features that we just need so so bad you can export the chat so this is that option I was talking about earlier so that back in the main UI you can import a chat um there have been some enhancements to The

**[0:04:31]** Prompt enhance feature as well so many amazing things going on with this project here so what I'm going to do here is pause and come back once this is done updating my code all right so it's finished making its changes really proving that it not only understands the

**[0:04:46]** file structure but it can interact with it just as if I had coded it up within the same conversation absolutely phenomenal one thing I'll say when you import projects a lot of times you'll have to tell it explicitly to run the installation and execution commands so I did that here and then it ran the npm

**[0:05:02]** install and npn rum Dev to spin up this site that we see right here so yeah you can just like type a message and then it responds with an example this is just a very basic prompt it doesn't look the best cuz I just threw out a random

**[0:05:14]** prompt have it build something just as an example here but yeah it looks pretty neat like this is pretty awesome for just a single prompt I loaded it in I was able to make improvements to it as well so absolutely phenomenal loading local projects is working great all

**[0:05:27]** right I want to go over the road map here even though I have on another video already just to set the stage for some of the new features that I'm going to Showcase right now so if I scroll down on this road map we'll get to this first

**[0:05:39]** set of high priority features because some of them we are working on right now others have already been implemented so loading local projects obviously what I just showcased that is done next up loading GitHub projects that is in progress and I'll showcase that pull request as well even though it hasn't

**[0:05:54]** been merged in yet and then the other one attach images to prompts I'll also showcase this one even with the demo later in this video this one's in progress and is almost done and then some other ones that we're still working on here but we're nailing these down

**[0:06:08]** we're making very great progress on that which is super important to set the stage for going down the rest of our road map here which by the way we're going to keep extending this road map as we continue to lay out the vision for autod Dev so super exciting stuff and

**[0:06:21]** with that we can dive into recent changes to autod Dev all right where I last left off on my last update video for autod Dev we were at the streaming of code put by the codus which by the way he's made some other phenomenal additions that I'll cover later as well

**[0:06:35]** and so since then we've had a lot of amazing changes not all of them are covered here cuz I want to keep this list pretty concise but a lot of tiny additions to autod Dev as well that are just as important to make the project really mature so I'll cover some of

**[0:06:48]** those in other PRS very quickly too but we have Edward again I'm linking his YouTube in the description of this video he added the ability to revert code to earlier versions which I already showcased then we have the coher integration by Hassan also by Hanan Dynamic model max token links which is

**[0:07:03]** really important cuz different models had different requirements for Max token links and then sujal has added in prompt caching and then again the big high priority task that's been knocked out loading local projects again from Edward so he's been making some incredible additions and then we also have some

**[0:07:18]** other high priority things that are in progress here almost done the top one being attaching images to prompts and so we've got that almost done here just a couple of additions that need to be added to really make it a PR that's ready to be merged and I'm working with

**[0:07:33]** the developer on that but this is going to be really exciting to bring in I'll even showcase this later on in the video giving a little demo with that U so yeah some other poll requests that I want to cover really quickly here with some smaller things Dustin luring has been

**[0:07:44]** doing some phenomenal additions to autod Dev super recently even as recent as this morning I've merged in a couple of PRS uh from him and so some stable additions that he added just like some things to really make this project all cleaned up and nice and tidy a lot of

**[0:08:00]** work that he's been putting into this also he's the one who worked on the UI and helped me bring in the prompt caching request from Sue Hall which by the way this is the original PR for that so thank you so much for your work on this this is super important as well

**[0:08:12]** with the prompt caching but yeah then back to the PRS here a lot of little things that are super super important um like fixing the artifact action list loading a lot of linting things and things with tests and cicd so sual and then also Oliver let's see if I

**[0:08:30]** can find a PR from him yeah here we go Oliver they've been doing some things with linting and testing and stuff that I really really appreciate cuz we really need to start on that to make autod Dev more mature so thank you so much for your fixes for that quicko some mobile

**[0:08:43]** friendly updates uh here we got the coher support so many really awesome things then also the codak kiss he also added this dedicated documentation page for autod Dev so whenever we have a new merge in the main it recompiles US based on the readmes we have in the repo the

**[0:08:59]** markdown files that we have for like the contribution guidelines and our main readme and it makes a dedicated page for the documentation which definitely makes the project look more mature I appreciate this a lot it really is just taking what we have in the repo but it makes it so that you don't have to go

**[0:09:14]** within the different markdown files there to see all this uh we even got like the new FAQs as well which I added pretty recently so super cool that we have all this here I appreciate that a lot and so yeah with that that's pretty much everything that's been added in now

**[0:09:28]** I want to talk about some of the inog stuff that is really exciting first up we have the git repository integration so you can load git repos into autod Dev just like you can load local projects this is in progress by the kodus he's been making a bunch of other amazing

**[0:09:43]** changes so I definitely trust that he's going to knock this one out of the park it's not ready yet but it will be pretty soon here and then that's going to be an awesome addition to have along with loading in local projects so whether it's in get or local you'll be able to

**[0:09:55]** take care of both so really looking forward to this one the other one that we have that I already alluded to is attaching images to prompts this one is super close to being ready so I the only reason I haven't brought it in yet is I just have a couple of pieces of feedback

**[0:10:09]** for the developer here just to make sure that it is a topnotch PR because this is a really important request this is a really important feature to get right and so yeah we'll be bringing this one in really soon but I actually want to showcase this to you right now because

**[0:10:23]** it's that close to being done and I'll even show you how you can do that so if you have GitHub desktop installed you can go down to the bottom of the poll request and open this in GitHub desktop and what that's going to do is switch you from the main branch to a branch

**[0:10:39]** specifically for this PR and then within my terminal here I can run pmpm install to reinstall the packages because things are going to be a little bit different in this Branch most likely and then I can either run with Docker or just run with pmpm right in my command line here

**[0:10:54]** so just to keep it simple I'll just run it with um The pmpm Run Dev Command right here and then I'm going to uh open up my Google Chrome Canary again and go back to my homepage and refresh and then boom there we go so now we are within this

**[0:11:10]** pull request specifically where we have this new button here to upload a file and so I'm going to upload a file I'm going to go back to my documents I have this sample web page right here that I'm uploading as an image and so yeah you can see this is working really really

**[0:11:24]** nice and I can even start by asking it to describe this image just to show that Claude can actually comprehend this image that I uploaded and by the way this is only going to work for models that actually support images like Claude for example um you know you can go to

**[0:11:39]** open Ai and go to GPT 40 that's another example but if you go to a llama and you try to use like you know quen coder for example it's not going to understand images so make sure that when you test this out and once this is in main

**[0:11:52]** especially that you actually use a model that can understand images so I'll have it describe this image here let's see what it comes out with um so yeah there we go it describes this website very very well that is perfect and one of my critiques is it doesn't show the image

**[0:12:06]** yet right here in the chat history that's one of the things that I'm looking for before I merge that um but once we have that this is going to be like absolutely perfect and so now I can even say uh code up this website for me now I'll go into the web container and

**[0:12:19]** it'll try to replicate it and usually when you upload an image like this even the best models like Claude can't replicate it super well but you can definitely see here even just looking at the text in the the HTML here that it definitely is understanding the image and then trying to replicate it that's

**[0:12:35]** the important part here is the feature works I don't know if the results are going to look the best but let me pause and come back once it's done and we'll see if it can even match it at all all right so it is done and yeah the results

**[0:12:45]** are about what I expected it doesn't really have images and so that hurts it a lot as well um it didn't replicate it extremely well but yeah like I said you can definitely tell that the feature of image uploading is working because it is at least a replica to some extent with

**[0:12:59]** the layout and the colors so yeah it's pretty cool this feature is working great looking forward to have this in the main repo very very soon here now I want to spend a little bit of time talking about the Strategic partnership that I mentioned at the start of the

**[0:13:11]** video and like I said there we're still working through the timing of the announcement and Logistics and so I can't talk specifics yet but it's still really important for me to share with you how that's going to help autod Dev because there's definitely a couple of big opportunities that we have to take

**[0:13:25]** autod Dev to the next level first of all we as a core maintainer team have done pretty good with organizing this repository considering it's only a month and a half old but it's still definitely not the most well organized open source project by any means there's a ton of

**[0:13:42]** opportunity for improving tests in cicd creating issue templates managing our poll requests better even managing the community better and this partnership is going to bring in open-source experts who are going to really make that happen we as a team have really been putting in the time and effort now but this

**[0:13:58]** expertise is what's really going to make this project shine as an open- Source effort also this strategic partnership is going to bring in financial incentives which is the reason I haven't started a crowdfunding campaign yet so when I say Financial incentives I mean things like rewarding people for

**[0:14:13]** contributing to autod Dev supporting the core contributor team myself not included by the way um but really just everything that we need financially to again take autod Dev to the next level and also this partnership is going to bring a lot of visibility and credibility into the project so that it

**[0:14:30]** is definitely going to transition into something that is not just a hobbyist project this is going to be the real deal and really what pushes autod Dev to be the best open- source AI coding assistant so really exciting stuff coming soon stay tuned for the announcements for that definitely still

**[0:14:45]** a lot of work that has to be done for autod Dev to really turn it into the best open- source AI coding assistant but we are certainly getting there the progress has been phenomenal and super encouraging for me and the entire community and stay tuned for all these

**[0:14:59]** updates upes that we got coming up soon for autod Dev and if you haven't recently go ahead and download all the cool new features some of which I showcased in this video and try it out for yourself and also join our think tank as well our autod Dev community and

**[0:15:12]** just be a part of everything that is happening here if you appreciated this content you're looking forward to more things autod Dev I would really appreciate a like and a subscribe and with that I will see you in the next video
