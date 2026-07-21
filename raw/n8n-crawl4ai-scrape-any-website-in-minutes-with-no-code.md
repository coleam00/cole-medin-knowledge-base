---
type: raw-transcript
title: "n8n + Crawl4AI - Scrape ANY Website in Minutes with NO Code"
youtube_id: c5dw_jsGNBk
url: https://www.youtube.com/watch?v=c5dw_jsGNBk
slug: n8n-crawl4ai-scrape-any-website-in-minutes-with-no-code
published: 2025-01-26
duration: "0:33:47"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** last week I introduced you to crawl for AI an open-source llm friendly web scraper that makes it super easy to crawl any site and format it for a rag knowledge base for your AI agent I even did a follow-up video where I built a full rag AI agent leveraging this

**[0:00:17]** knowledge base that we built with crawl 4 AI the thing is we did everything with python code and so a ton of you ask for me to do the same thing in n8n so that we can scrape sites and build a full rag implementation with no code you asked

**[0:00:33]** and now I am delivering in this video so right now I'll show you how to super easily deploy craw for AI with Docker and leverage it in your n8n workflows to scrape website pages in just seconds and we're going to be doing this without writing a single line of code and we're

**[0:00:49]** going to build a simple AI agent that leverages crawl for AI to build itself a knowledge base in superbase so that it can be an expert at pantic AI which is my favorite agent framework right now a neat little example and this is the kind of end workflow that you can really

**[0:01:04]** steal for yourself and extend to fit any use case that you have there are a lot of ways to crawl websites but most of them are slow expensive and not very easy to work with but crawl for AI is the complete opposite it's fast intuitive and completely free because it

**[0:01:20]** is open source I mean the only thing you actually have to pay for is the machine in the cloud to host your crawler that's only if you're not just running it on your own computer so it is a Fant fantastic platform and I recommend it even though there are a lot of ways

**[0:01:33]** specifically within NN itself to crawl websites but they really just all fall short of crawl for AI in my mind so I am super excited to show this to you right now so with that let's dive right into it all right so this is the full 8 end

**[0:01:47]** workflow that we're going to go over in this video we've got the bottom portion right here which is what actually leverages crawl for AI to scrape a bunch of pages and put it in a superbase vector store for Rag and then the top part here is a very simple proof of

**[0:02:01]** concept implementation for an AI agent leveraging this knowledge base and so this is basically following what we built within python in the last couple of videos on my channel so before we built everything directly within a python script here so we pull all the pages from pantic AI we scrape through

**[0:02:19]** all of them using crawl for AI and then put them into our superbase Vector storage just like we're going to do in n8n but we're going to do it now with no code at all so say goodbye to this code we're doing it all in n8n and just as a

**[0:02:32]** review I'm going to be using the exact same documentation here for pantic AI as the example it's just a great resource to use because it's the kind of site that we are okay scraping it's really important to keep in mind I have to preface this video you want to scrape

**[0:02:48]** ethically there are a lot of websites that block scrapers and request you to not scrape and it is important to follow those rules the way that you can check generally is if you go to a website like youtube.com and you you add in/ robots. text you'll see some rules right here

**[0:03:04]** that help you understand when and how you can scrape a lot of times they'll say don't scrape at all the terms of use is also another good place to check for any given website um or platform just to make sure that you're following the rules and scraping ethically so with

**[0:03:18]** that in mind which we can do for the pantic AI documentation I want a quick way to get all of the web pages available right here so basically all the navigation that we have right here I want to be able to pull all of these URLs for myself within the N8 workflow

**[0:03:33]** and the way that we're going to be doing that is with what is called a sitemap.xml so if you add SLS sitemap.xml to the end of a lot of websites like documentation pages and e-commerce stores you'll get this XML right here that gives you most of the time every single web page that is

**[0:03:51]** available on this site and so we can parse this within our n8n workflow just like we did with python before to get all the web pages then scrape them one at a time with crawl 4 AI so that actually is the start of this workflow but before we even get into building out

**[0:04:07]** this n end workflow and I'll go through this in a good amount of detail for you we first need to actually get crawl 4 AI deployed so that we can use it as an API endpoint within n8n so back when I had the python code before we just imported

**[0:04:22]** crawl for AI as a library but now we need to call into an API endpoint where we have crawl for AI hosted externally with Docker and so before we get into this I'm going to show you exactly how to do that and don't worry it is super easy here we are in the crawl 4 AI

**[0:04:38]** documentation now back when I was using Python and not n8n I just had to go to the installation tab to get started I used pip which is the python package manager to install crawl for AI and then I imported it directly in my Python scripts and used it there but in n8n we

**[0:04:54]** do not have the same Choice there is not a place to run this pip install command and it's not like we can use this right within any Python scripts it's just not a dependency that is available to us and so for n8n we have to deploy crawl for

**[0:05:06]** AI in a completely different way and that is why I mentioned Docker just a minute ago Docker is our ticket to deploy crawl for AI in a way where we can actually interact with it as an API endpoint and that is what we're going to do within our n8n workflow so going back

**[0:05:24]** over that really quickly and again I'm going to go over this workflow in a lot of detail in a little bit these HTTP requests nodes are where we are interacting with crawl for AI so I have this API endpoint set up that I have hosted in the cloud and I'll show you

**[0:05:36]** how to do that with Docker this is just waiting for us to send requests to crawl specific website so we give it a URL to crawl and it'll return the markdown and the links to the images and it'll have the HTML everything back over to us so that we can then process that and put it

**[0:05:53]** in our knowledge base for Rag and so that's what we're going to do right now getting Docker set up and it's important to note that there are a few different ways that we can install crawl for AI with Docker the first option is we could actually include crawl for AI the docker

**[0:06:08]** image within our local AI starter kit that is a fantastic option that I'll probably cover in another video so let me know in the comments if you're interested in seeing that the other solution I'm going to show right now is not doing that just because I want something a little bit more Universal

**[0:06:22]** and I'll get to that as my last solution here the second option is that you can run crawl for AI just by running this container locally or on the cloud instance that you already have running n8n if you are self-hosting n8n so it's a fantastic way to do it if you don't

**[0:06:38]** want to spend anymore to have a dedicated instance for craw for AI because if you're already paying for the machine to self host n8n or you're just running it locally on your machine you don't have to pay anything now there is one thing to keep in mind though and

**[0:06:51]** that is the crawl 4 AI Docker container is a little bit of a resource hog CU it is running an entire headless browser to scrape the web for you so it does take a good amount of CPU and RAM and so I actually would recommend hosting this separately because if your crawl for AI

**[0:07:08]** instance is getting really bogged down you don't want this hosted on the same place as your n8n because that might slow down your n8n as well and so I would recommend hosting it as an entirely separate instance in the cloud and that is what I'm going to show you

**[0:07:21]** how to do right now so if you do just want to host it right on your computer or right in an instance that you already have running n8n you can just run these commands right here you can pull the image from Docker obviously as long as you already have Docker installed and

**[0:07:34]** then you can run it and you can also optionally run it with a secret token so that you can protect your endpoint so not everyone can just use it to use your crawl 4 Ai and so yeah these two commands it's all you need to get started it is so so easy now the more

**[0:07:49]** complicated setup is when you actually want to have it as a dedicated API endpoint and so that's what we're going to cover right now there are a lot of platforms out there to run a Docker container as an API endpoint the one that I have found the easiest by far

**[0:08:04]** though is digital ocean I cover digital ocean quite a bit on my channel I love their product not sponsored by them in any way I just use them for my instances in the cloud and also things like this and I'm just about to show you for Docker deployments and so the way that

**[0:08:20]** you can deploy crawl for AI within digital ocean is using their app platform so I'm going to click on this to create a new app platform and you can pull from a git repository which is super neat but in this case I'm going to pull from a container image here and the

**[0:08:36]** crawl 4 AI container images are hosted here on dockerhub and so I just went to hub. deer.com search for crawl for AI and this gives me all of the images that are currently available for the different architectures that we have here and so I'm going to select Docker

**[0:08:52]** Hub and then the repository that I want I'm just going to look at the version that I want right here now for deploying to digital ocean the a version that you want specifically is basic amd64 that's just the Linux architecture that they have for digital ocean so this is the

**[0:09:09]** one that you're going to want to use so specifically the repository is going to be uncle code SLC craw for aai and then the image tag is going to be basic D amd64 and I can just get that by looking right here in dockerhub so I can see

**[0:09:23]** it's Uncle code SL craw for AI Uncle code is the GitHub username of the creator of crawl for AI by the way super awesome guy um and then yeah basic D amd64 is the tag that we have after the colon so that's how we figure out these two things then I'll go ahead and click

**[0:09:39]** on next now we can identify the resource that we want and so this is really up to you I'm going to click on edit for the resource size here you can go as cheap as $5 a month so you can get some dirt cheap app platforms up here on digital

**[0:09:54]** ocean just keep in mind that you're probably going to need more RAM and vcpus for running crawl 4 AI CU again it is running an entire browser under the hood and so you might even need upbs of 4 GB of RAM if you're craing a ton of pages at once just keep that in mind and

**[0:10:09]** we can tweak things in the N workflow to have smaller batch sizes and things to work with smaller instances if you want so I'm just going to select this one and it's $50 a month but I'm just going to remove this after the day so I'm just paying a couple of bucks to get my

**[0:10:22]** knowledge base ready and then I can remove this app platform and it's so easy to deploy it again if I want and I'll move the containers down to one instead of two so it's just a base $50 a month and then for the port right here I need to change it from 8080 to the

**[0:10:36]** actual Port that we have for Docker which is this 11235 so I'll go ahead and paste that there and then click save and that is everything that we have to do for our resource configuration so go ahead and click on next and now the only other thing that we have to really

**[0:10:50]** Define here is our environment variable for security so again we could just not include this environment variable so that our API endpoint for crawl for AI is unprotected but I definitely want to include that protection here and encourage you to do the same and so our environment variable is just called

**[0:11:07]** crawl for AI API token so I'm going to add this as a global environment variable here and then the value is going to be whatever you want your Bearer token to be so I'm just going to say test off I'm going to obviously delete this after I record this video so

**[0:11:22]** I'm just hardcoding this I'm making it visible to you this is going to be my Bearer token for my crawl for AI endpoint so I'll go ahead and click on next we got our environment variables defined now and then we can review our info make sure that everything looks

**[0:11:36]** good which it sure does and then it go ahead and click on create resource and it is that easy within a couple of minutes here it's going to go and actually build this container for me get everything set up in my environment within just a couple of minutes we'll

**[0:11:48]** have crawl for AI available to us and the app platform here on digital ocean automatically gives us an SSL protected full https endpoint ready for us to hit within our na and workflow there we go just a couple minutes later we are completely live and we have this URL for

**[0:12:05]** us to access our app deployment now and actually if I go to the homepage it just takes me right to the homepage of the documentation for crawl for AI and I can also hit the health endpoint here which is just a part of the container and I can see yep I'm got a status of healthy

**[0:12:21]** gives me some stuff for the CPU and memory usage as well super neat so easy to set this up with digital ocean and again a lot of other platform to do it I'm just showing you as an example here of something I would recommend also this entire thing is optional if you're just

**[0:12:36]** going to be running the container yourself or where you are hosting n8n and I'll talk about how you can use that as well in the n8n workflow how you would adjust URL to work with Local Host and the documentation for Docker deployment does cover that as well because it shows you I mean this is the

**[0:12:52]** URL that you would use instead of what I'm going to show you when you just have it hosted alongside your NN instance or on your computer locally so with that we can dive into our N8 end workflow and actually leverage our new crawl for AI endpoint the sponsor of today's video is

**[0:13:08]** 10 agent an open source framework that helps you build voice interactive AI agents in like 20 minutes imagine having your own AI agent that can see and understand you through your camera and your screen in real time and process voice commands in parallel and this isn't just a product this is an open

**[0:13:26]** source tool for you as a developer to build these agents yourself with these capabilities that's what got me so excited about partnering with them 10 supports a ton of really helpful pre-built modules for speech to text llm and text to speech so it's very easy to iterate on your agent as you are

**[0:13:43]** building it and you can choose any kind of model that you want like open AI real time or Gemini 2.0 and they integrate with a lot of different things like RTC which makes it super easy for you to set up your agent with low latency and good interruptibility which are both super

**[0:13:57]** important for realtime application and these are the kind of things that are not easy for you to set up from scratch so over on their playground at agent. the. we can try out 10 agent right now it's so cool and this is a developer platform meant to help you

**[0:14:12]** build agents so what we're seeing right here is not a product it's just a barebones proof of concept to show what we can build with our agents here so I'm going to unmute I'm already sharing my screen showing the NN H page just watch this little conversation it's super neat

**[0:14:26]** how I can see my screen in real time in one sentence describe to me what you see on my screen okay I see the n8n website which is described as a secure AI native workflow automation platform for technical teams all right I'm sharing a new screen now tell me what you see here

**[0:14:43]** in one sentence in one sentence I see a workflow template for an AI agent to chat with files in super based storage all right very very cool if you want to configure things more yourself you can definitely do that for the llm speech to text or text to speech when you host it

**[0:14:59]** locally and you have access to the 10 agent playground there and then for developers 10 support C++ go Python and node.js and it seamlessly operates on any operating system and mobile devices if you are interested in building multimodal AI agents or just learning more about them I would definitely check

**[0:15:16]** out the GitHub repository which I'll have Linked In the description of this video and this really is a one-of-a-kind open- Source framework from what I've seen so I am super impressed definitely recommend checking it out this entire n8n workflow that I'm about to go over with you right now I have in a GitHub

**[0:15:32]** repository that I have Linked In the description of this video so you can download this for yourself right now bring it into your own NN instance and then customize it to your heart's content to do whatever you want for crawl for AI cuz keep in mind what I'm

**[0:15:45]** building out right here with you this is just a proof of concept to really lay the foundation for you to use crawl for AI within n8n and the rest of the stuff in that GitHub repository that's the python code the python version of what we're building right here so definitely

**[0:16:00]** check that out as well if you're curious and also the python version of this agent the pantic AI expert I have hosted for you right now on the automator live agent studio so you can go to studio. automator doai you get some tokens for free to play with these agents so you

**[0:16:14]** can go to the pantic AI expert and try this out right now without having to run anything you can have a conversation with this guy just to test it out with your questions on the pantic AI docs and just see what you're getting yourself into by building this with me so it is

**[0:16:29]** the p python version so it's not the exact same what we're building here but it has very much similar functionality and so with that let's get into building out our n8n workflow the first thing that we want to do is get a list of URLs that we want to scrape with crawl for AI

**[0:16:44]** and in this specific use case we are doing that through that sitemap.xml file that I showed you earlier for the pantic AI docs and so I'm going to click on test step right here which by the way I'm going to do this for every single step along the way so we can really dive

**[0:16:58]** into how this process process works and yeah I get the XML back so exactly what we see right here this is what we have for the output of our first node and then next we want to convert this into Jong this is just much much better to work with within n8n so now we have a

**[0:17:13]** list of all of the URLs for the pantic AI documentation now the next thing that we have to do if you notice this right here n8n still thinks this is a single item but we really wanted to recognize each of these right here as a separate item each with a URL for a page to

**[0:17:30]** scrape and so that's what this node does right here we split out based on this value right here so it's url set. url and we're turning them all into individual items so now n8n truly recognizes them each as individual items in a list so that we can Loop over each

**[0:17:47]** one of them now and so I'll click on test step and there's a little bug in n8n where sometimes it won't actually show the output when you're running test step to fix this you just have to refresh so I could just kind of cut that out um but I wanted to show that to cuz

**[0:18:00]** it's probably going to happen to you as you're playing around with na workflows as well so I thought that'd be useful so you just refresh and then click on test step for the current step that you want to see the output of and so that is this Loop right here so when we click on test

**[0:18:13]** step in a loop it's just going to show us the first item in a loop which is the homepage for the pantic AI documentation and then the second item would be the second page that we see right here third item would be this one and so on and so

**[0:18:26]** yeah we got the location right here and the last modification as the first item in our Loop and then this by the way is where you can update the batch size as well so if you want to process five URLs or 10 URLs at the same time you can adjust this right here just

**[0:18:39]** make sure that your instance can handle it because remember crawl for AI can be a CPU and RAM hog so really be careful with this one and I'm just sticking to a batch size of one to keep it simple right here and I think the rest of this

**[0:18:52]** workflow would actually have to be modified a little bit if you do have a higher batch size than just one so again this is just a approv of concept to get you started here with crawl for AI I want that to be the focus of this video so we get this item right here now we

**[0:19:06]** can move on to the rest of this workflow the rest of what we see right here is all running within the loop so for every single one of the 49 items that we pulled right here we're going to run everything for each one of those because that is what we're going to do to scrape

**[0:19:21]** and then put in super base for rag so we're making our first API request to crawl 4 AI now and so you can see that the URL that I have right here matches exactly with what we have in the app that we set up in digital ocean and if

**[0:19:36]** you are hosting crawl for AI locally if you're running the docker container on your computer or in the same instance where you are hosting n8n then you would just have to change this to Local Host port 11235 and then update this to http as well so going back to the docker

**[0:19:54]** deployment page for crawl for AI if I scroll down to the first example they actually show you this URL so if you're hosting the docker container on your own infrastructure just referencing it with Local Host this is exactly the URL that you would use instead of what I'm using

**[0:20:09]** right here to connect to digital ocean so I do want to cover those different ways that you might be hosting craw for AI when you're referencing it in n8n so that's the URL and then for the authentication right here if I go back to the documentation we specifically set

**[0:20:23]** it up so we have this Bearer token here so again going back to digital ocean and I go to my environment variables here I have this environment variable set up for the bear token I just have the value of test off and so going back to n8n we

**[0:20:38]** set up a generic credential type and we have it as header off and the way that you want to set up this credential here I'll just create new credentials to show you an example the name has to be authorization because that's the header name for a bearer token and then the

**[0:20:54]** value here I'm going to go to an expression view so you can actually see what I'm typing you want to type error and then a space and then whatever that value is that you set up in your environment right here or just whatever you specified right here when you ran

**[0:21:08]** the container if you are hosting it locally so I said test o for my value So within n8n it is Bearer space and then test off so I'm going to close out of this and I'm going to refresh because I already have it set up so let me just go

**[0:21:23]** back to this node right here all right so we got our URL we figured out our credentials and now we have the body of our request and so this again just going back to the documentation I'm not doing anything fancy here I'm very much following the documentation and showing

**[0:21:37]** you how to incorporate it into n8n so the Json this is our payload we have two values here first of all we have URLs and I don't know why this is plural you just give one URL here I actually tried it with multiple comma separated and it did not work so you just give one URL

**[0:21:53]** here that you want to scrape and then you have a priority as well because the crawl for AI Docker container supports running all of this in cu's so you give the sites that you want to scrape in cues and you can Define priorities so that you can Define the

**[0:22:07]** order in which your requests are actually handled by your crawl for AI deployment I'm not going to get into that here because I want to keep things simple but just know that there is so much documentation they have here for so many things you can do to customize your

**[0:22:21]** crawl for AI deployment as well I'm going to keep it simple but yeah just know that there is a lot available to you and so going back to n8n for for the body URLs I just have the json. location so that pulls the URL from the last node

**[0:22:35]** that is executed and then we have the priority of 10 so I'm just not using this here but I'm really just showing you that I'm following the documentation exactly uh by including this here so let's go ahead and run this and so what we get back here it's not quite what we

**[0:22:50]** would expect we get a task ID what the heck is a task idea I thought it was going to scrape and give me the markdown of the HTML back well let's go look at the documentation let's not get ahead of ourselves here so when we scrape the SL

**[0:23:03]** craw URL not when we scrape it when we call it to scrape for us it's going to give us back a task ID and the reason we're doing this is because scraping a website might take longer than you would usually have an HTTP request go for so you're essentially kicking off a task

**[0:23:21]** and then given a task ID so you can check up on the status of the task later on so I can ping this endpoint so instead of SL crawl it's slash task and then the task ID to essentially ask my crawl for AI instance for the status of

**[0:23:39]** this specific scrape task that I gave it and so if I go out of here and I click on wait it's going to wait 5 seconds and then I have this second request that is going to call the task endpoint with the ID that I got from the first request to

**[0:23:56]** again Ask crawl for AI hey what's the the status of this request and if the request is fulfilled we will actually get the HTML and the link to all the images and the markdown and all of that so let me actually refresh NN we hit that weird little bug again so I'm going

**[0:24:10]** to refresh n8n go back and kick off right from this node right here so I'm going to click on test step and we're going to have to wait 5 seconds for that wait step but it's going to kick off the crawl task and then right here we ping

**[0:24:23]** the task based on the task ID that we got from our first HTTP request so yeah we' get that wait 5 seconds and then we check on the status and within 5 Seconds the crawl task has already complete so we instantly get back everything that is scraped for us so we

**[0:24:39]** have the URL the HTML there's a ton of information here because it gives us all of the links and it gives us the markdown if I go all the way down we got all the markdown here so we got everything that we could possibly want from that scrape task and then we also

**[0:24:53]** have the status here which it's completed right now but if this was still processing and we'll I think I'll probably show you this later as well it'll say pending or processing instead of completed and so then we right after this request here we have this if statement where we basically just check

**[0:25:09]** to see if the status is completed and if it is not completed if the if statement is false then what we want to do is loop back around wait another 5 seconds and then check again so we're in this infinite Loop here basically just every 5 Seconds asking our crawl for AI

**[0:25:27]** deployment is the task complete complete yet is the task complete yet and then finally once it is status will be completed so that this if statement will be true and then we can do the last step here which is taking the markdown that we pulled from this job that we ran and

**[0:25:43]** adding it into our knowledge base so I'm going to click on this task right here it hit the true Branch because the status is completed and so now that's going to guide us into the final step of inserting into our knowledge base we have finally gotten to super base now

**[0:25:57]** which is super exciting so for the embedding model I am just using open AI text embedding 3 small connected my API key it's super easy to do that by the way you just have to click on open docs right here and it'll guide you through how to get your API key which you can

**[0:26:11]** basically do for anything in NN it just makes it so easy to get all of your credentials and then for the data loader I'm just using the default data loader and then the data specifically I'm getting by result. markdown so from the output of the last node it's json. res.

**[0:26:28]** markdown and then also for the metadata here it's not super important but I'm specifying the page that this chunk came from as well which is just nice to have in the database so I can see exactly what page from the pantic AI documentation this specific chunk that is created came from and then for the

**[0:26:46]** splitter I'm just using a text splitter with a chunk size of 5,000 I didn't put a ton of thought into how I'm chunking my data for rag here um you can definitely play around with this for your use case specifically and see what just gets the best results for you and

**[0:27:00]** then for the node itself with superbase all I had to do to connect my superbase account is I just had to give it my host which is My superbase URL and then my service R secret so I have this superbase project created right here I just went down at the bottom here to my

**[0:27:16]** project settings to the API tab copied my URL which is right here and then I revealed and copied my service rooll Secrets those are the two things for your super base credentials and then the only other thing that you have to do is set up your table to actually store the

**[0:27:31]** knowledge base in subit base and the way that you can do that they have a very good starter template for you so if I click on the docs right here in the superbase vector store node and then scroll down to a quick start for setting up your vector store click on this find

**[0:27:46]** this SQL to execute right here copy everything starting on line 4 because the vector extension is already enabled in superbase by default just copy this right here and then you go over to superbase go to the SQL editor and then paste in everything right here so you're going to paste in this and then click on

**[0:28:06]** run in the bottom right here and then that'll automatically create your documents table and this match documents function which is what actually performs reg on your superbase knowledge base so now on the table editor I have this documents table right here which is currently empty because I haven't done

**[0:28:22]** anything to actually execute this workflow but that is the full superbas setup so I took a couple minutes to show that there cuz it's really important to make sure you know how to do that and now we can actually test the step so let's run it here and boom there we go

**[0:28:36]** we've got our first three items cuz it took the homepage of pantic AI and it split it into three chunks and inserted each one of them into our knowledge base right here so I'll click on refresh and there we go we've got the content for each and then the embeddings as well so

**[0:28:51]** we can do our retrieval lookup with the the vector mathematics there and then we got our metadata so it also says the page that this is from which is that little piece of information that I added as well so that is everything for this workflow so now what we need to do I'm

**[0:29:05]** going to actually delete these records so we can start fresh here I'm going to run this workflow so that we can ingest everything at once so I'm going to save this I'm going to click on test workflow and there we go look it's already going so it's making that first request it's

**[0:29:21]** waiting a little bit and okay looks like it was complete so it did the first task got the first three chunks in the knowledge base now it's going again all right boom there we go now it's got eight in so if I refresh right here we should have eight items in our knowledge

**[0:29:35]** base look at that cuz it process two pages already so what I'm going to do here is I'm going to pause and come back once it has done everything because it will take a little bit to get through all 49 Pages all right the processing is complete I got a little impatient so I

**[0:29:49]** cut it off at 30 just cuz I want to get to the last part of my video for you here um but yeah you can see that it executed this part of the loop 56 times because some of the time it was still processing the request you can actually

**[0:30:01]** click into the if statement to see that I want to show this for you really quick so like right here the status is complete it looks like it failed for this page let me go to another one quickly here uh let's go let's go back to right here so it's a true branch cuz

**[0:30:15]** the status is complete it pulled everything successfully but then on another run like this one right here we go to the false Branch because the status is still processing so this shows that not all the time is it going to be after 5 Seconds immediately available to us that's why we have to go in this Loop

**[0:30:33]** and sometimes ping a second time or a third time after 10 seconds or 15 seconds because we have to wait for that task to be finished so we have all 148 vectors inserted in our database now so if I scroll down here actually you can just see right here 148 records that we

**[0:30:49]** have in superbase and so now we can go on to our agent to actually chat with our knowledge base I'm not going to go over this one because it's super super simple I just have the chat message receive trigger and then I have the AI agent node I don't even have a system

**[0:31:03]** message or anything right here so it's super super basic I've got my superbase chat history I've got my uh GPT 40 Mini model and then I've hooked in the superbase vector store tool for rag so very very basic just using GPT for both my embedding model and my llm now let's

**[0:31:22]** open up a chat let's actually chat with this and so I'll ask it a question that it could only answer if it actually has the p pantic AI documentation in its knowledge base so I'll say what are the supported models in pantic AI all right and so you'll see that it'll start with

**[0:31:38]** open ai go to the vector store retrieval tool process the request and then send it back to the llm to give me the final response and this is absolutely perfect and we can click into super base right here to see the response these are all the uh chunks that were returned to us

**[0:31:53]** for the llm to reason about and yeah it's got all the models here this is perfect and then if I ask another question like how uh how are tool responses handled we'll see if it can pull from the tools page this time so you want to make sure that it's actually

**[0:32:07]** retrieving from the right pages of the documentation within the knowledge base here so I'll click into this scroll down until I get to the URL and there we go yep it's going to the/ tools page right here to get us the answer to our question looks good all right perfect

**[0:32:23]** this is working absolutely beautifully and again this is just very much a proof of concept but it shows you how you can deploy crawl for AI with Docker and use it through an API endpoint in n8n so you don't even have to pip andall the package cuz you can't do that with an N

**[0:32:38]** so yeah super neat hope that you can take this extend it to your use cases and do some awesome things with it so there you have it we have integrated crawl for AI directly into n8n giving us a super simple and completely no code approach to scraping any website for Rag

**[0:32:55]** and whether you're hosting crawl for AI locally or you are deploying a Docker container into the cloud like I did with digil ocean it's still the exact same process within n8n to leverage crawl for AI super super simple and it is important to keep in mind that this

**[0:33:10]** really is a proof of concept this workflow is meant to just give you the foundation to really combine these two platforms together in incredible ways so definitely check out the crawl for AI documentation if you want to look into making things more efficient or configuring your crawl for AI instance

**[0:33:26]** and also there's a lot of opportunities to improve things like actually turning our AI agent into an agentic rag approach like I did with my other video with python so a lot of stuff for you to take forward but I hope that this helps get you started if you appreciated this

**[0:33:40]** video I would really appreciate a like and a subscribe and with that I will see you in the next video
