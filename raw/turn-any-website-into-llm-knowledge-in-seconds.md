---
type: raw-transcript
title: "Turn ANY Website into LLM Knowledge in SECONDS"
youtube_id: JWfNLF_g_V0
url: https://www.youtube.com/watch?v=JWfNLF_g_V0
slug: turn-any-website-into-llm-knowledge-in-seconds
published: 2025-01-12
duration: "0:18:46"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** one of the biggest challenges we face with large language models right now is their knowledge is too General and it's very limited for new things because of its training cut off for example my favorite new shiny framework for building AI agents is pantic AI but if I go over to Claude right now and ask it

**[0:00:17]** what pantic AI is it has no clue and even if I use an llm that can search the web the information that I get back is still going to be very Bare Bones but on the other hand if I take all of the framework documentation for pantic AI

**[0:00:32]** and put it in a knowledge base for the llm and I ask it the exact same question the answer that I get is spot on that is why rag is such a huge topic when it comes to AI right now which that by the way stands for retrieval augmented

**[0:00:45]** generation it's a method for giving external knowledge that you curate yourself into an llm basically to make it an expert at something that it wasn't before like an AI agent framework you're using your e-commerce store you name it the problem is that Cur R step can be very difficult and slow for example if

**[0:01:03]** you want to ingest an entire website into a knowledge base for your llm how do you actually do that and get it done fast so that it's not 2027 by the time your knowledge base is ready and AI has taken over the world anyway that is where crawl for AI comes in crawl for AI

**[0:01:20]** is an open-source web crawling framework specifically designed to scrape websites and format the output in the best way for llms to understand and the best part is it's it solves a lot of problems that we typically see with these systems for website scraping usually they're very slow overly complicated and super

**[0:01:39]** resource intensive but crawl for AI is the complete opposite it's super intuitive very very fast easy to set up and extremely memory efficient so in this video I'll show you how to super easily use crawl for AI to scrape any website for an llm in just seconds and

**[0:01:57]** at the end of this video I'll even quickly showcase a rag AI agent that I built basically to be an expert at the pantic AI framework of course using crawl for AI to curate all the framework knowledge into my knowledge base and really you could take what I built and

**[0:02:12]** use it for any website super exciting stuff so let's go ahead and dive right into it so the two big things that we're going to focus on right now is crawl for AI which this is their GitHub right here completely open source and then also pantic AI now this is not a pantic AI

**[0:02:28]** video but it's just a very good example of full documentation that we can scrape with crawl 4 Ai and bring into a knowledge base for our llm now back over to crawl for AI the first obvious question when we visit this page is what is the point of crawl for AI why even

**[0:02:45]** use it and luckily at the top of their readme here on their homepage they have a very concise description for why you should care about crawl for AI and the first big thing is when you visit a website and you extract the raw HTML from it I mean this looks like a mess and as a

**[0:03:02]** human looking at this it's very hard for us to actually extract useful information from it and a good general rule of thumb is if it's hard for us as a human to understand something it's probably harder for a large language model as well and so one of the most

**[0:03:18]** important things that crawl for AI does is it takes this ugly HTML that we get when we visit the raw content of a web page and it turns it into markdown form which is actually even human readable format like a super clean way to represent a web page and all the

**[0:03:36]** information that we see when we typically visit a UI like this just in something that's all text space so we can give it to a large language model for reg and just for llms to understand it better in general so that's the first thing and it does it very very

**[0:03:49]** efficiently it's super super fast it handles a ton of things under the hood like proxies and session management things that are not easy to handle so it's not like you can go and make your own version of crawl for AI very easily as well just because you know how to use

**[0:04:03]** the request module in Python to pull HTML from websites and it's also completely open- source and very easy to deploy they even have a Docker option which I'll probably cover in another video on my channel later on they're doing major updates soon to their Docker deployment so I don't want to focus on

**[0:04:19]** that now but just know that that is available as well and there's a ton of other things that they do that are super valuable as well like one really important thing is removing irrelevant content I mean when we go to the h ml here we have a ton of script tags and

**[0:04:32]** there's probably a lot of information um that we can view on the page that is very obviously redundant or just not useful to us and that they take care of removing that as well So eventually what we get back from scraping the site with crawl for AI contains just what we care

**[0:04:46]** about actually ingesting into our knowledge base and getting started with crawl for AI is so easy all you have to do is PIP install the python package and then run this setup command which is going to install playright under the hood that is the tool that crawl for AI

**[0:05:03]** uses under the hood to scrape websites and basically have this browser running in the background that can visit these sites and playright is a fantastic also open source tool that I use for a lot of testing for my web applications as well so very very familiar with it I can

**[0:05:18]** recommend this as well so I think it's a great choice for actually having that web scraping functionality under the hood and getting started is so so easy it's just as simple as this little script right here and so I actually have my own version of it if I go into my

**[0:05:33]** source control here I've got my own version of it just scraping the homepage of pantic AI their documentation so let's go ahead and test this out and see what kind of output we get and by the way all of the code that I go over in this video I'll have in a GitHub

**[0:05:47]** repository that I will link below and so right now we're starting with just these basic examples right here starting with this one to pull the homage of the documentation for pantic AI and then we'll get to my rag AI agent later and I'll show showcase that a little bit as

**[0:06:01]** well and so yeah I've already installed crawl for AI it took like 30 seconds to install everything including play right under the hood and so now I can just go ahead and run our script and within seconds we're going to have the entire page printed out in the terminal here so

**[0:06:16]** so fast very very impressed with this and this isn't like the perfect format for us as humans to understand cuz we have all this little markdown syntax and stuff but this is definitely a great format for an llm to understand this entire page especially compared to what we get if I just go back to the pantic

**[0:06:35]** documentation here I'll just open this back up if I inspect the page Source this is the HTML that we got the markdown from and imagine pasting all of this into an llm prompt I mean it's just a mess it's definitely going to hallucinate when you try to ask a

**[0:06:49]** question with all of the HTML tags and everything in there and so it's just so much better when we have something that looks like this all right so we saw a basic example using for AI to get the markdown for a single file but obviously we have to take this a lot further to do

**[0:07:05]** something that is actually useful for our llms now the first thing that we want to do is make it possible to ingest every single one of the pages in the pantic AI documentation so you want to get the markdown for the introduction page installation getting help contributing all of these at the same

**[0:07:22]** time and the first problem we have to tackle to actually make that possible is we need an efficient and scalable way to be extract all of the URLs from the documentation here now I could just go and manually copy and paste the homepage and the installation page and the agent

**[0:07:38]** page and just bring that into a list in my code but that is very inefficient and not scalable as more pages are added I'll have to manually do the same thing and constantly update the list myself and so luckily there is a very good solution for this introducing the idea

**[0:07:55]** of a s map so for most Pages out there on the internet right now if you go to the homepage and then add SLS sitemap.xml it's going to give you this XML which gives you the entire structure of the website all of the pages that exist there and so you can do this right

**[0:08:12]** now for the pantic documentation like I'm doing right here and all the pages that you see here are the same ones that we see in the navigation right here and I can do the exact same thing for the crawl 4 AI documentation it's very meta but I could use the sitemap.xml to get

**[0:08:29]** all the pages in The crawl for AI documentation to scrape with crawl for AI so yeah you can do this with most websites most e-commerce stores like if they're built with Shopify or WordPress they'll have this as well CU in general websites have this for search engine optimization and also for crawlers I

**[0:08:45]** mean a lot of websites want you to crawl them because they want their information very widespread like if I'm building an AI agent framework I want people to crawl this and build agents around it because then they're using my framework and it's just more accessible which by the way if you are curious if you can

**[0:09:01]** scrape a website there's a lot of Ethics behind web scraping typically what you can do is go to a website like youtube.com and then add robots. text to the URL here and this will give you a page that tells you their rules for web scraping so this says that any agent is

**[0:09:19]** allowed to scrape YouTube however there are certain pages that are not allowed and so this is super important to keep in mind if you want to be very ethical with your web scrap scraping which I highly recommend check the websites you're scraping for robot. text first before you just go ahead and do it like

**[0:09:36]** GitHub is another good example here where they actually say if you want to crawl GitHub please contact them first a lot of them will be like this so keep this in mind I very much owe it to you to provide this little segment talking about ethics before I dive into the rest

**[0:09:50]** of the video um it it's very fitting to do that because we're talking about uh URLs that you can add to pretty much any websites you can do/ robots. text or the/ sitemap.xml and so we're going to in code pull this sit map and then we are going to extract every single URL

**[0:10:08]** and then feed all of those into craw for AI and we want to do that very efficiently as well cuz right here we're just going to be pulling in every URL and then looping and going through one at a time if we do it just in a loop

**[0:10:22]** with this code right here we want something more efficient and so if we go to the documentation for crawl for AI which is right here that'll bring us to this page right here and if we go down to multi URL crawling there is a lot that crawl for AI gives us for this and

**[0:10:39]** that's what we're going to be leveraging for the rest of this video so first of all if you just crawl your websites in a loop like this like we would do if we just continued off of this example right here it would be very inefficient we're spinning up a brand new browser for

**[0:10:54]** every URL that we are visiting and there's no opportunity for parallel process processing which we're going to get into as well and so their recommendation they give a full example for this for how you can use the same browser session for all of the pages that you're visiting and pulling and so

**[0:11:11]** that brings us to the second script that I have built for us here and I'm not going to go over all the code in detail because this is mostly following the example that we just saw right here so I just copied this in brought it into my code editor and then I have this custom

**[0:11:26]** function right here where I pull that site map that I just showed you so I pull it I extract using XML processing all the URLs from the sit map and then I pass them all into this function to crawl the URL sequentially with the same browser session and so the code gets a

**[0:11:44]** little complicated with the browser config and crawler config but don't worry about that in general you can just take this example and use it for yourself it crawls every single URL and it's not going to print out the content of every markdown CU that would just be way too much in the terminal it'll just

**[0:11:59]** show us the length and whether or not it succeeded in crawling the site and so I'm going to go back to my terminal here and run this second script here and it's going to take a little bit because it has to crawl all of them sequentially we'll get into parallel processing next

**[0:12:14]** to make this even faster but even this just took seconds it was so fast processing each one of these Pages giving me the length and whether is success or not for each one of these URLs so at this point we already have a very fast way to get the markdown for

**[0:12:29]** every single pantic AI documentation page and it's ready now for us to put in a vector database for rag to use with our large language model it's super neat and it was so easy to set this up with crawl for AI but before we actually get into anything with rag I want to take

**[0:12:45]** this one step further because I want to make this even faster it was already fast here but we're still processing each one of these URLs sequentially there's no parallel processing and we can definitely do that with crawl for AI so we can visit multiple Pages at the exact same time pull the mark down for

**[0:13:03]** every single one of them and then combine it all at the end to a single list just like we're doing right here and so the way that we can do that if I go back to the crawl for AI documentation and just scroll down a little bit they have an example doing

**[0:13:16]** this exactly this parallel processing and it's essentially going to be the same we're still just using one browser but we're creating different sessions that are all going to be up at the same time visiting these URLs in parallel and just like last time I mostly just copied the example that they had right here and

**[0:13:34]** then brought it into my code editor and then again just like last time the main thing that I added is that function to use the pantic AI sitemap.xml to get all the pages that I want to pull the markdown for and scrape and so I'm going to open up my terminal again and

**[0:13:50]** actually one last thing before I do that for the batch size we are doing 10 so it's going to visit 10 pages at the exact same time get the markdown for all of them and then move on to the next set of 10 and then repeat that until it has

**[0:14:03]** pulled the mark down for every single page and so I have a new terminal open up right here I'm just going to run this script just like I did before and last time I showed how fast each run was now I'm going to show how memory efficient it is so when I run this it'll show the

**[0:14:17]** current RAM usage for the script which it starts at 91 megabytes it's going through all these batches very very quickly and at the end we can see the peak usage which is only 119 megabytes so throughout this entire time even though there's an entire browser running in the background visiting 10 pages at a

**[0:14:36]** time it's still only ever used 119 megabytes of memory at once which is just incredible and the last example was actually basically as fast but that's only because of caching in general this batch processing is going to speed it up a ton which is super impressive and so

**[0:14:55]** now we have the perfect thing for rag because we're doing it very very quickly and a lot of times you need that I mean this example has 42 pages but if you have something like an e-commerce store with hundreds or thousands of products you can imagine that this is going to

**[0:15:09]** start to be a drag if you are processing things sequentially not using the same browser and same session that's why using crawl for AI and having all these efficiencies is so important very last thing and this is my true gift to you I have already built out a full rag AI

**[0:15:25]** agent that is a pantic AI expert so using the exact same process with crawl for AI that we just did I pulled all of the pantic AI documentation and then I put it into a vector database for its knowledge base built a full agent around it and created a front end that we're

**[0:15:41]** looking at right here and my gift to you is this is already available to you I have the code in a GitHub repository that I have linked below and then in the next video on my channel I'll be go covering how I actually built this agent and it will be available on the live

**[0:15:56]** Asian studio for you to try immediately so super super neat and also a little bit of a sneak peek right now so let me paste this in here I'll just ask a basic question like what are the supported models and this is the kind of thing that Claude or any other General llm

**[0:16:11]** would definitely not have the answer for and it even links me to the different pages in the pantic AI documentation for my reference very very neat and I can ask a ton of other questions as well like I can say something like give me the weather agent example for from the

**[0:16:30]** documentation obviously I just know that this agent example exists and so I'll ask for it and it'll go and search for it find this full example for me and it does it so fast as well and this is perfect like this is a pretty complex example because it's showing me

**[0:16:44]** basically every part of creating an agent with pantic AI which is super super neat so there we go this is the full agent and I'll be showing you exactly how to build it very very soon on my channel now the reason that I'm not covering how to build the entire

**[0:16:57]** agent in this video is I want to keep it concise and focused on just crawl for AI especially because there's a lot of other use cases for web scraping besides just rag even though rag is definitely one of the biggest ones for AI and just in general right now but if you go to

**[0:17:13]** the GitHub repo I have a readme right here covering everything with this agent you have all the code for my entire process of crawling all these sites again with a very similar process to what we went over in this video and then actually inserting that into our Vector

**[0:17:28]** database which I'm actually using PG Vector with superbase here and then I have my agent that I built with pantic AI very meta but it is my favorite framework right now and then I have my streamlet interface so all this is available for you with instructions on how to run it yourself and then also

**[0:17:44]** stay tuned for my video later this week where I'll show you exactly how I built it so there you have it a bulletproof lightning fast way to scrape any sight and give it to your llm as a knowledge base and this is useful for you pretty much no matter what your use case is

**[0:17:59]** because there is almost always a time and place to take data from external websites and bring that into your llm and so that in my mind makes crawl for AI a GameChanger and don't get me wrong there are a lot of ways to bring knowledge into an llm you can manually

**[0:18:14]** curate data use new advanced concepts like KAG a lot of things I'll cover in more videos on my channel but it is still the most common way to make an AI agent and expert at something you care about to scrape data from a site and provide it to a knowledge base for rag

**[0:18:29]** and in the next video on my channel I'll do a deep dive into the rag AI agent that I demoed earlier which I'm super excited about because I put a lot of effort into building it for you so if you appreciated this content I would really appreciate a like and a subscribe

**[0:18:42]** and with that I will see you in the next video
