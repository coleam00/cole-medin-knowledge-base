---
type: raw-transcript
title: "Turn ANY Website into LLM Knowledge in Seconds - EVOLVED"
youtube_id: FQlCWrsUpHo
url: https://www.youtube.com/watch?v=FQlCWrsUpHo
slug: turn-any-website-into-llm-knowledge-in-seconds-evolved
published: 2025-04-30
duration: "0:26:39"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** A while ago on my channel, I covered Crawl forAI, an incredible open- source tool for you to crawl pretty much any website to get it into the perfect format for LLM knowledge for things like your rag AI agents. And let me just say the feedback that I got on that video

**[0:00:15]** was amazing. And so many of you started using crawl for AI for your own projects, including myself for Archon my open-source AI agent builder. So now I want to take crawl for AAI much further with you because a lot of the questions that you guys had were how to

**[0:00:30]** handle different kinds of websites. Sometimes we have a sitemap so we can see the different URLs that we need to crawl. Other times we have to figure it out ourselves from the navigation and then other times we have this new idea of an LLM.ext where the website gives us

**[0:00:45]** a single page with all the documentation specifically for us to give to our LLMs. And so right now I'm going to show you how to handle all of these different scenarios with Crawl forAI so that no matter what kind of knowledge you want to bring into your LLMs, you can do that

**[0:01:00]** in seconds. So here is the homepage for the Crawl for AI documentation. I'll have a link to this in the description as well because this is my resource for all of the code that I have created that I'll show you throughout this video. And I covered this on my channel before.

**[0:01:14]** I've talked about Crawl for AI, but a lot has changed and this project has completely blown up recently. Take a look at this. It's completely open source, so it's on GitHub. And the repo currently has 42,000 stars, which is just amazing. People are realizing that this tool is just the best at what it

**[0:01:32]** does. And scraping the internet to create knowledge for our LLMs is really important because a lot of the knowledge we give our agents comes from the internet. So, we need a way to scrape that effectively and to do it quickly. And Crawl for AI definitely gives us both of those things. It is blazing

**[0:01:49]** fast, as we'll see in some of my demos that I have for you in a bit. And it produces webpage data that is AI ready. It spits out what's called markdown format, which is just the optimal format for LLMs to understand these pages and pick out distinct sections from them.

**[0:02:04]** And if you're curious how projects like Context 7 are able to scrape up-to-date documentation constantly to provide that to AI coding assistants, I can guarantee that they're using something like crawl for AAI. And it wouldn't surprise me if they actually are using crawl for AAI to scrape all the documentation for

**[0:02:21]** Superbase and Fast API, MCP, Nex.js, all these different libraries because it's so fast and so efficient. And it's also what I use for Archon, my AI agent builder, like I mentioned in the intro which speaking of Archon, I have some big updates for that slash potential changes of plans that I definitely want

**[0:02:39]** to get your feedback on. So, if you're interested in Archon, please stay tuned for the end of this video. I want to share some things with you on that. But right now I want to focus on crawl for AAI. And then in the documentation for crawl for AI on their homepage they have

**[0:02:52]** a quick start that shows us at a high level how we can build this crawler and then use it to crawl pretty much any URL that we give it. It is so easy to use this. And then within their installation instructions we can see just how easy it

**[0:03:05]** is to set this up. You just have to have Python installed and then you can pip install crawl for AI and then run their setup command to install the playright browser so that your terminal can run a browser to scrape pages under the hood and do the rest of the necessary setup.

**[0:03:20]** So that's all you have to run to get things set up and then I can show you that within my windsurf here I have a first example to show you really quickly which is definitely inspired by the quick start that we just saw. So I create this instance of an async web

**[0:03:33]** crawler through crawl for AAI. And then the URL that I'm having it scrape is the Pantic AI documentation. And so going back to my browser here, I'll show you that this is the page that we are about to scrape with crawl for AI. And I could just take the raw HTML of this page and

**[0:03:49]** give it to an LLM, but it's not going to be able to pick out different sections very well and just understand the page as well as if we give it the markdown format. And I'll show you in a second exactly what that looks like when we run this script. And so this page right here

**[0:04:01]** is what we're going to transform into LLM knowledge. And so I have my terminal open. Um and I'm going to just run that exact same script that I just showed you. And on top of getting this beautiful markdown format that you'll see in a second, you'll also see just

**[0:04:15]** how fast that is. Just take a look at that. It just in seconds scraped this entire page and formatted it for us into something that is much easier for our agents and LLMs to understand. And so we have these bullet points and then we have the markdown where we have the

**[0:04:30]** different headings and the subheadings. And so everything is just very structured for our agents. And so that's my first example just to give you the basics of how we use crawl for AI. But now we get to the real stuff because I want to show you what you really came to

**[0:04:44]** this video for which is scraping entire websites. Right now, we just crawled a single page, which it was important for me to show you a basic example. But what we really want to do is crawl entire websites. We want to pull the markdown for every page that is available to us

**[0:05:00]** then feed that into our AI agent for rag so that it can become the expert on our e-commerce store or understand the full documentation for something like Pantic AI, whatever website it is. I have you covered now with a few different strategies for crawling really any website that I'll hit on right now. So

**[0:05:17]** the first main way that you can crawl websites is through what is called a sitemap. And so a lot of websites will make this available where you can go to the root domain and then slash sitemap.xml. There are a couple other different URLs. They might look a little

**[0:05:32]** different, but usually it's going to be /sitemap.xml. And this is going to give you this very structured document here that tells you all the URLs that are available for you to visit for this website. And so this is the primary method in my previous crawl for AI video

**[0:05:47]** that I showed as a way to get access to all the different web pages that are available in a given website. But sometimes you don't always have a sitemap. This is really convenient and if it's available to you, you probably want to use it. But sometimes you don't

**[0:06:01]** have that. And so you need crawl for AAI to actually start from the homepage and then find the rest of the pages through navigation. do some kind of recursive scraping where it goes through these pages and finds all the links that it has to visit. That is the second method

**[0:06:15]** that I have covered for you here. And then the last method is a lot of especially documentation for frameworks and tools. They've started to put out what's called an LLMs.ext. And so usually this is going to be either /lms.ext orlms-full.ext. And essentially what they do with this is they take every

**[0:06:36]** single page for their documentation and they combine it together into a single page. So we have one document that we can bring into our program we can chunk up and add it into our vector database for rag. So it's literally documentation formatted and this is all markdown just

**[0:06:52]** like crawl for produces. It's formatted specifically for LLM knowledge. And so that is the third method of scraping data from a website that I'll show you with crawl for AAI. And essentially one of these three methods is going to be able to be used no matter what website

**[0:07:08]** you are crawling. And so I truly am showing you here how to extract LLM knowledge from any website that you want. So your golden ticket to crawl any web page with any of the three methods that I shared with you and to do it very fast is this GitHub repository which I

**[0:07:23]** have as a free resource for you. So link to this in the description of this video. And the way that I have structured this repository is I first have this crawl for AAI examples folder. This is where I show you at more a granular level how we have these

**[0:07:36]** different strategies set up to crawl web pages in crawl for AI. So first we have crawling a single page. So this is the very basic example that I showed you earlier. Then we have this example that I don't want to cover too much in this video but you can crawl web pages

**[0:07:50]** sequentially. So you just process one URL at a time. But what crawl for AAI does really well and what makes it blazingly fast is you can crawl batches of URLs in parallel. And so that's what I have for the last three scripts in the examples folder here. So starting with

**[0:08:06]** the script to crawl our site maps. This is going to take that site map like this is the one that we have for crawl for AAI that we saw earlier and it's going to take batches of these URLs and extract them markdown from each of them in parallel. So we can then feed that

**[0:08:20]** into our vector database for our rag knowledge base. I know it's very meta here. We're using crawl for AAI to crawl crawl for AI. But I mean, yeah, this is good documentation to crawl and get into our AI coding assistance and things like that because we definitely want to

**[0:08:34]** create a lot of agents around this. So that's for sitemaps. Then we have the one to crawl our LLM.ext. So this is just going to take a single URL. It's a lot simpler because the LLM's.ext is just one page with all of the documentation. And I do show you in this

**[0:08:49]** script how to chunk things as well because obviously we would not want to take this massive document and dump that into a prompt for the LLM. And so we want to chunk that up. And so then that leads us to our last one here. And this is the most complex but also the most

**[0:09:03]** flexible because we can give it any website URL. It doesn't have to be an LLM.ext. It doesn't have to be a sitemap. and it can scrape the homepage or whatever that page is that we gave it and then intelligently determine other links to other parts of this web page

**[0:09:17]** and scrape those as well. And it does it in a recursive way where we can specify the depth like how many levels we want it to go down. So it can search for all the different URLs that we have for this web page. So it can scrape everything

**[0:09:30]** essentially as if we gave it a sitemap.xml. So very very powerful stuff. The sponsor of today's video is Aqua Voice, an insanely powerful and accurate AI voice system that works on any application on your Mac or Windows computer. You just have to install Aqua Voice once and you can use it anywhere

**[0:09:48]** with literally the press of a button. Take a look at this. Archon is my AI agent builder that uses Crawl for AI Pideantic AI, and Superbase. And then I let go of the button and look at how fast that was and also how accurate it is as well with words like pyantic AI

**[0:10:04]** and crawl for AI that usually these voice systems would completely botch. And talking numbers, Aqua will start up in around 50 milliseconds and get you responses in as fast as 450 milliseconds. And it makes 17 times fewer mistakes than Siri and Google voice typing. So you get insane speed

**[0:10:22]** and accuracy. And I have not seen something as smooth as this before. And my favorite way to use Aqua is within my AI coding assistants like Windsurf because Aqua has this feature called deep context where it can view your screen to understand what you're currently working on. So it can

**[0:10:38]** reference certain components of your code, spell things correctly, really help you communicate effectively with your AI IDE. For example, update my async webcrawler call to use the browser config that I imported from crawl for AAI in line 2. And boom, it spelled everything correctly like my async webcrawler, browser config. It really

**[0:10:57]** understands the code that I'm working on so I can communicate effectively with Windsurf. And within the Aqua app, you can tweak your settings. You can toggle deep context on and off. Add things to your dictionary so it dictates it properly. Give custom instructions based on different applications. There's so

**[0:11:12]** much control that you have here. And then the main component of this GitHub repository is I created an AI agent that has this script as well to insert documents into its knowledge base that combines all three strategies. So you can give this script a URL and it will

**[0:11:28]** intelligently determine is this a sitemap, an LLM.ext or a regular web page and then use that specific strategy depending on which type of URL it is. And then this is all set up with a pyantic AI rag agent that is using Chroma DB for its vector database. So I

**[0:11:44]** just wanted something really simple and that you can run locally. So that's why I chose Chroma DB. But you could obviously use Superbase or Quadrant or Pine Cone something else for your vector database as well. So a very simple agent overall just leveraging a tool that will allow us to search all of this knowledge

**[0:12:00]** that we give to our vector database through what we crawl with crawl for AAI. And within the readme that I have for this repository, I show you how to get everything up and running. So prerequisites installation instructions, setting up your environment variables, how you can use these different scripts to get the

**[0:12:16]** knowledge base set up and to run the agent itself. So all the instructions are here and I can actually show you a demo of this live. So, I'm going to run the insert docs function and then I'm going to copy the URL for the sitemap for crawl for AAI. So, I'm going to send

**[0:12:32]** this in. It's going to determine that it has to use that first strategy to scrape everything from a sitemap. And look at that. We're fetching all of these URLs in batches. I think I have a batch size of five or something like that. So, it's it's scraping five at a time. Doing this

**[0:12:48]** very very quickly. And so there are quite a few pages that we have for crawl for AI. It created 457 chunks in total that it's now inserting into Chroma DB. And actually basically the insert into Chroma DB takes longer than the scraping itself. That is how blazing fast crawl

**[0:13:05]** for AAI is. And we could even make it so that it batches in sets of 10 or 20. So it scrapes even faster. And there we go. We have everything inserted into Chroma DB. So that process is now done. But what I can do is just run this another

**[0:13:18]** time, but instead of using the crawl for ai sitemap, how about this time we use the pidantic web page. So not a sitemap or llm's.ext. So I'm going to go ahead copy this URL, paste it here. Now it'll say that it detects that it is a regular web page that it has to crawl. Regular

**[0:13:32]** URL and we'll give it a second and boom there we go. It starts with the homepage and then it checks the navigation. It looks for what are called internal links. That's the phrase used with crawl for AAI to find all the different web pages. go through there, find even more

**[0:13:45]** links to other parts of the web page. Really trying to hit on everything. Like I don't have the sitemap.xml. So if I have a certain depth, like I go three levels deep, I'm not absolutely guaranteed to hit every single web page but you can set that depth to something

**[0:14:00]** more like five or six if you want as well. And then pretty much you are going to hit on any page you could possibly have within this website. Especially things for documentation like Pantic AI or Langraphph where you're not really going to go that deep. the navigation on

**[0:14:13]** the lefth hand side usually it's going to cover most of what's available in the website and so this takes a little bit longer overall because it has to do with more of this recursive searching and so I will pause and come back once this scraping is complete and there we go we

**[0:14:27]** are done and this time it inserted 2,420 chunks into chroma so definitely the podantic documentation is just much larger than what we have in crawl for AI and then the very last test we obviously just want to use an LLM's text. And so I'm going to remove that link to pantic

**[0:14:44]** AI and then paste in the llm.ext for langraph, which is my favorite AI agent framework to orchestrate different agents together. And so this time it's going to just pull that single page instead of going to many different pages and it's going to chunk that up. So it's very very fast now. It pulled that one

**[0:15:00]** page, split it into 788 chunks, and now it's inserting that into Chroma. So I'll pause and come back again once that is complete. And there we go. We've inserted all of our langraph chunks into Chroma DB. And now I've showed you every single method. Now I want to demo the

**[0:15:15]** agent to you. Ask it some questions just to make sure that all the knowledge that we brought into our agent from call for AAI is working well. So I have a streamlet interface created that I show you how to set up in the readme. So I'm just going to run the command streamllet

**[0:15:26]** run in the name of my streamllet python script. This is going to spin up a page in the browser so we can start talking to our agent. And it takes a little bit for the first message to go through because it has to load the Chroma DB instance. But otherwise, these messages

**[0:15:40]** get a responses from the agent blazing fast. So, first I'll have it verify that it has access to the Piantic AI doc. So verify that you have access to the Pyantic AI doc. So, I'll do a quick search. Confirm for me that it has access to the documentation. Good. And

**[0:15:56]** I'll say now confirm Superbase. This is one where it doesn't actually have that access. And so, yep, there we go. The documentation available does not contain anything about superbase because we only crawled crawl for AI, pyantic AI and langraph. And so now I can refresh the conversation here. I'll just ask it a

**[0:16:12]** simple question about pyantic AI. Just show me how to create a very basic agent. And so it doesn't give me a step by step in the documentation, which is fine. I don't really expect it to have that, but I'll just say give me something very basic here. So just so I

**[0:16:26]** can see that it yeah, it got something from the documentation. So there we go. That is looking good. All right. Right. So, refresh the conversation. Now, we can try something out with crawl for AI. So, I'll ask it something basic like how do I install crawl for AI? We'll see if

**[0:16:38]** it can give me those pip commands like we saw earlier. Yeah, there we go. So crawl for AAI setup. So, all the setup commands as well. Looking really good. And then I can do something for langraph. I could just ask the same question here. I just want something

**[0:16:48]** really basic because I'm focused on crawl for AI, not rag um and chromadb too much in this video. So, I'll just say how do I install langraph? We'll see if we can get the instructions for that as well through the documentation. Yeah pip install lang graph really basic.

**[0:17:03]** Maybe the LLM would have been able to get this just with its own knowledge but I know that it's searching through the database under the hood and we saw that it definitely needed to do that for things like crawl for AAI and Pantic AI. So yeah, this is working great. So, I

**[0:17:16]** know that in general I haven't covered the nitty-gritty details of the code that much in this video because I wanted to give you a very highlevel overview of how this agent works, how you can scrape websites in different ways, and you can just use this repository as your

**[0:17:28]** template to get you started. You can take the functionality from any of these examples if you want to pull a specific method or you can take a look at all the details how I implemented that agent that I just demonstrated for you. And so with that, the last thing that I want to

**[0:17:43]** show you is just a quick dive into each of these different strategies, how that works within crawl for AAI. I just want to give you a more higher level idea of how these strategies are implemented. Starting with the first one for crawling our site maps. And obviously since this

**[0:17:58]** is just more of a demo script showing you at a high level how to use the sitemap crawler, I just have the URL hardcoded here. It was dynamic with that insert doc script that I showed you in the demo. Here it's just hard-coded, but we get the contents of the sitemap and

**[0:18:11]** then we extract all the URLs from it that we want to crawl and then we call this crawl parallel function. We can also determine how many URLs it's going to process in each batch when it's doing things in parallel. And so within this crawl parallel, we set up a lot of

**[0:18:26]** things to manage the memory for our crawl for AAI instance that I don't want to get into right now. But then we create the async web crawler. And so that's exactly what we created in that very first example like we saw right here. And now we're just going to use

**[0:18:40]** the A run mini function. So instead of just the basic A run function, we want to crawl many URLs in parallel with these batches that we set up. And so it's going to get the markdown from all these pages at the same time. And then we can chunk that and insert that into

**[0:18:56]** our vector database. And so this script stops because it's just an example. it stops at the point that we get the markdown for that page just here in the results. But you can take this functionality, bring it into your own agents just like I did for mine right

**[0:19:10]** here. Like I took this functionality in script number three in that example and I baked that into my insert docs. So if it detected that it needed to scrape a sitemap file like using this function right here, then we would call the functionality that is very similar to

**[0:19:26]** what we saw in the example script to crawl in batches where we're going to use the A-on mini just on all these URLs getting them all from our site map. So that is number three. And then for number four, things look a lot different because we just have to scrape a single

**[0:19:41]** page. And so really we take the URL and then with that URL we're going to call the AUN function. So just like we called a run in our very simple example to crawl one page, we're doing the same thing here. But because that's so simple, I just took this as an

**[0:19:56]** opportunity to also show you a little bit more complex logic for some chunking strategies that I've been playing around with. And so I could do an entire video on chunking strategies. And I might actually do that soon. But what I do with a markdown is I split based on

**[0:20:11]** headers. And so I chunk all of the documents based on the primary headers like just with that single pound. And then I also chunk based on the subsections that we have as well. So we have a bunch of these chunks now that are the core sections split up for the

**[0:20:26]** documentation that we crawled within this single lm.ext page. And then I also played around with some more chunking strategies within insert docs. If you want to take a look at my chunking function here as well, I call it smart chunk markdown. You can definitely take a look at this. I don't have the time to

**[0:20:42]** dive into this right now. Um, but there are a lot of strategies for working with markdown specifically because the documents are formatted so nicely with these headings and subheadings. You can work with that to really make sure that you split documents well, but also do it in a way where the distinct sections are

**[0:20:59]** all kept together in those chunks. You don't lose that contextual information. So, that is number four. And then our last strategy is crawling websites recursively because now we don't have a sitemap to guide us. We don't have an LMS.ext to bring everything together for us. We just have a single URL and we

**[0:21:16]** want to dynamically determine all of the pages that we need to scrape based on what we have in the navigation for this homepage. Like right here we have the homepage for the Pantic AI documentation. And so we pass that into this crawl recursive batch where we have a list of start URLs. So this can also

**[0:21:33]** handle more than one starting web page if you want and it's going to use the A- run many function to scrape all these URLs loop through these results and then the key part to this entire workflow is that we can access what are called internal links in crawl forai. So we get

**[0:21:50]** the result like we get the markdown back from the web page and then we can call result.link.get and then get the internal links. are called internal because we're looking for links where the domain is the same as the original page that we scraped. That's how we're able to navigate between all the

**[0:22:05]** different pages that we have in the website as a whole. And so we're going to get a list of all of these URLs that it fetches from these internal links. And then we're just going to loop back up to the top here just based on that depth that I talked about earlier. And

**[0:22:19]** we're going to call those web pages as well. So we go deeper and deeper just scraping all these links dynamically as we go until we hit that depth limit of three or five or whatever you have and then finally we have a bunch of markdown from all these different websites that

**[0:22:33]** we visited that we can return. And so this basically builds up a site map dynamically over time. So the site map is still better. It's more reliable if you have that because then you're guaranteed to have all the different links. But this is just a nice way to be

**[0:22:47]** more flexible if you're running into a page and you'll see this a lot that doesn't have a site map. So those are the three strategies and how I've implemented them. And again, take these and implement them for yourself. I put a lot of time into learning crawl for AAI

**[0:23:01]** and getting all this set up for you. So please use this as a resource and also take a look at more of the code with my padantic AI agent and things with Chromma DB. So you can see how I set that up if you are curious as well. So

**[0:23:12]** the last thing that I want to talk about that very much relates to what we were just covering with Crawl forAI is Archon. This is my open- source AI agent builder, and I'm thinking about making some big changes with it. So, please hear me out on this. If you care about

**[0:23:25]** Archon, you've got some feedback for me. I want to share with you my ideas that I have for where I want to take Archon. And then I want to know in the comments what you think about what I'm planning on doing here. And so at a high level

**[0:23:37]** Archon is able to both ingest documentation for things like Pyantic AI in its knowledge base and then also code the agent itself. So it's multi-purpose in isolation. It itself is enough to create a full AI agent for you. But what I'm thinking about doing is turning it into a better version of something like

**[0:23:57]** Context 7. So, context 7 is an MCP server that you add into your AI coding assistance to give it more knowledge to work with different tools and frameworks like MongoDB or Superbase or MCP whatever that might be. And I like this a lot. The context 7 MCP server itself

**[0:24:14]** doesn't create any code, but it provides knowledge for the AI coding assistants to do so. And right now with Archon, I'm kind of tripping over the toes of AI coding assistance because you can integrate it with Windsurf or Cursor anything like that. But when it generates the code for the agent, the AI

**[0:24:31]** IDE then also has to generate the code as well to put it into the files. So you have a lot of duplicate work there which is prone to errors. That's why I'm thinking about maybe turning Archon more into a knowledgebased specific project like focusing a lot more on rag to help

**[0:24:45]** AI coding assistants build agents instead of it itself creating the agent code. Because another thing that I've been thinking about just as I've been diving into processes for using AI coding assistance, like there's so much functionality that's already there within things like wind surf and cursor that I just want to leverage that and

**[0:25:03]** then just have archon be the knowledge engine behind the scenes instead of trying to just do it all. I think we'll get better results overall. It'll also just make archon more expandable like we can more easily add more documentation into it kind of like we have here with

**[0:25:18]** context 7. So it can be useful for a lot more things than just building agents as well. Like right now it's very limited to only podantic AI and soon lang graph and we're adding some more frameworks and stuff into it. But I think being able to just focus more on the knowledge

**[0:25:31]** engine under the hood. That's what a lot of people have been telling me as well is like they're actually more excited for that part of Archon versus the actual code generation because AI coding assistants are already knocking that out of the park. And so that's enough of me

**[0:25:44]** babbling about what I'm planning on changing here. It is a really big shift though because I'm focusing I'm very much honing in on one component of Archon now. But I think this is best for the future of Archon. But it is a big decision. So please let me know what you

**[0:25:56]** think. That's what I've got going on for Archon right now. I hope that this video has really helped you level up your RAG game, taking pretty much any website and bringing it into your Vector database. And also I have a lot more RAG content coming soon, especially covering

**[0:26:11]** different strategies for RAG that I haven't talked about much on my channel before. I really want to cover these things like hierarchical rag, contextual retrieval, query expansion, read ranking. There are so many different strategies that also go along well with what we just covered with crawl for AI.

**[0:26:26]** So definitely stay tuned for that. If you appreciated this content and you're looking forward to more things ragg and AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next
