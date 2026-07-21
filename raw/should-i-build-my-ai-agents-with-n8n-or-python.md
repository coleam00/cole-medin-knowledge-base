---
type: raw-transcript
title: "Should I Build My AI Agents with n8n or Python?"
youtube_id: V-0ExE6imTg
url: https://www.youtube.com/watch?v=V-0ExE6imTg
slug: should-i-build-my-ai-agents-with-n8n-or-python
published: 2025-10-19
duration: "0:16:01"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I get asked this question more than anything, so it is about time that I make a video covering this. Should I be building my AI agents with N8N or Python? Or more generally, should I build my agents with no code tools or in code? If I had a dime for every time

**[0:00:17]** someone asked me this, Elon Musk would wish he had my net worth. And so my goal in this video for you, just very broadly, is to make it easy for you to make a decision use case by use case. Should I stick to N8N as the easy way to

**[0:00:30]** build AI agents or move to code, get over that learning curve and probably learn how to leverage AI coding assistance as well? And all the pros and cons that I have here in this beautiful diagram that'll guide our video today, I honestly don't think that any of them

**[0:00:45]** are hot takes. But of course, there are always nuances that you might think of as we go over this. And so definitely let me know in the comments if you agree with everything that I'm saying here or if you think that there's something that I've missed. And before I go and say

**[0:00:58]** anything positive or negative about either, I just want to be super clear that I have a deep level of respect for building AI agents both with N8N and Python and all the AI agent frameworks that we have there. In fact, at the end of the video, there is something else

**[0:01:12]** that I want you to consider. We don't necessarily have to pick one over the other. More on that later. But right now, I want to explain my general recommendation and then get into the pros and cons to really help you think for yourself how what I'm saying applies

**[0:01:27]** to your use case. And so, at a high level, I recommend using N8N to build your AI agents for any kind of integrationheavy internal tools, proof of concepts, and team collaboration across skill levels. So, N8N is a very integrationheavy platform. You can connect to hundreds of different services so easily. And so any kind of

**[0:01:47]** internal automations you have for your team, N8 is great for that. And then proof of concepts simply because you can build so quickly with N8N. And then across different skill levels because there is a lot less of a learning curve building your agents and automations in N8N versus in Python. Now, when you

**[0:02:04]** really want to get to production scale applications or anything where speed, control, and flexibility, like how much can you really design the solution around exactly what you want, that is when I recommend going with Python. I know a lot of people that start with N8N because it's easier and then they move

**[0:02:21]** to Python when they really want to take their ideas far. Not saying that you can't do the same with N8N, but that's just generally what I see. And I do use both as a part of my workflow still because I'll use nitn to prototype so I can ideulate quickly and then move to

**[0:02:35]** Python when I really want to scale things and have a lot of the flexibility that I'll be talking about throughout this video. And so with that, I want to move on to the pros and cons here. I love my pros and cons list and I made it look all nice and pretty for you as

**[0:02:50]** well. And so I want to start with N8N, talk about the good and the bad there and then how that relates to Python. And by the way, when I say N8N versus Python, I mean more generally no code versus code, these are just the two tools that I use extensively myself and

**[0:03:03]** what I cover on my YouTube channel. So starting with N8N, it is both very easy to get started. The learning curve is quite small and it is a beautifully visual agent builder. So I've got a workflow up just as an example to talk about here. When I'm building with N8N,

**[0:03:20]** it feels like I have this canvas. It's like an art form to create my AI agents and automations. I just love how easy it is to connect my different nodes together. I can visualize the tools I have connected to my agent, for example. You definitely don't have this kind of

**[0:03:35]** experience when you're working with code instead. And of course, you've got your hundreds of integrations and thousands of templates to help you get started. One of the things that N8N makes so easy is integrating with your different services like my database with Postgress or Google Drive. I just go in here. I

**[0:03:53]** can pick from the hundreds of different integrations that we have. And then it walks me through setting up my credentials. And then boom, I'm good to go for each service in just a couple of minutes. And it's not that easy to do with code. A lot of times you find

**[0:04:05]** yourself rebuilding the same integrations that other people have thousands of times because it isn't just a node you can drag into your workflow. And speaking of leaning on other people, there's also thousands of templates for us to use in the N template library. No matter what you want to build or the

**[0:04:21]** service you want to integrate with specifically, you'll probably find something here to help you get started so you don't have to start anything from scratch. And that's part of what I do with my YouTube channel as well is sharing these templates like this one for an Aentic rag agent with knowledge

**[0:04:34]** graphs so that you have a place to start from. This isn't the end goal, but this is a template for you to build on top of and customize to your use case. And so there's a lot of things out there to help us do that with N8N. And also for a

**[0:04:48]** noode platform, N8N scales extremely well because of something called Q mode. That's definitely more advanced. I'm not going to cover that in this video extensively obviously, but like for a noode platform, N8N scales to thousands of users quite well. And also, I definitely have to call out that N8N is

**[0:05:07]** open- source and self-hostable, which also means we can build our AI agents to run completely locally if we're working with sensitive data or just want a very secure environment. And so, I have always appreciate N8N a lot for that. So, a lot of high praise for N8N. It

**[0:05:22]** really is an incredible platform, but there are unfortunately some cons that we have to cover here. First of all, N8N is 100% open- source and self-hostable, but that doesn't mean that it's free for you to commercialize your workflows. You have to pay a license fee. Now, I'm not

**[0:05:38]** going to do a cost breakdown right now, but definitely go research that if it applies to you. Just know that this is a big reason that I use N8N for internal tools and proof of concepts because I'm not commercializing either of those. Also with N8N we hit what I call the

**[0:05:54]** noode performance and noode integration box. So for performance there is an overhead for these noode platforms with these node builders. They're never going to be as efficient as directly running code. Even with a language like Python that is generally considered to be one of the slower languages, it still has a

**[0:06:15]** lot better efficiency compared to N8N. And then what I mean by the integration box is we are boxed in to the integrations that N8N supplies us. And sure, it's pretty fantastic how many there are overall, but it's going to get to that point where you find that one

**[0:06:32]** tool that you really want to use, but it's not there in the integration list. And so you have to build the integration yourself, typically with an HTTP request node. But that gets more complex. And often times, especially because of AI coding assistance, at that point it's easier to just code the solution. And

**[0:06:49]** even for the integrations that are there for you, they don't always have what you need. One good example is Google Drive. We're able to watch for files that are created or updated in a Google Drive folder, but not for files that are deleted. And for something like a rag

**[0:07:04]** pipeline where we need to keep our knowledge base in sync with Google Drive, that's actually pretty important. And so this is a good example where I had to build this workflow with a direct integration using the HTTP node to the Google Drive API to watch for files that

**[0:07:18]** are deleted and I have to do so periodically. It's not an ideal solution, but that's what I was forced to do with N8N. And kind of going along the same lines here, when you can't do something in N8N, a lot of times you'll resort to using code nodes, which don't

**[0:07:34]** get me wrong, it's fantastic that N8N gives this to us. So we can inject code anywhere in our workflows when we need some more customizability, but these code nodes are not very efficient. And because of security reasons, you're very limited to the libraries that you can import into the JavaScript or Python

**[0:07:52]** code nodes. And so they're fantastic. They solve the problem they aim to solve, but they're never going to be ideal. And I see these workflows all the time where they end up just being half code now. And it's like, come on, man. Why don't you just code the solution in

**[0:08:05]** the first place? Also, end workflows are difficult to version control. One of the beautiful things that we have with code is we can track the changes in our files over time and even revert things when the things go wrong. And that's all thanks to git. Now, we can just throw

**[0:08:22]** the JSON workflows for N8N in our Git repository, but JSON diffs are pretty ugly. Not to get too technical here. It's actually quite difficult to really see what has changed in your workflow over time, and it's kind of unal because you have to translate things between Git and then like bringing it back into

**[0:08:40]** GitHub when you want to revert something or see what you had in a previous version. And then last but not least, N8N does not work very well for large files, which is especially important for your RAG AI agents. I have had N8N choke, even with 20 megabyte PDF files,

**[0:08:57]** bringing it through something like a RAG pipeline. And that's even if my machine hosting NAN definitely has enough memory because there's a separate problem with node buffering. And generally what I've seen in the nan community is especially once you get to 200 megabytes for your files nan is going to choke so bad and

**[0:09:16]** you can handle tens hundreds of gigabytes easily in your Python code as long as you have the memory in your machine to handle that. So that's nan at a high level. There are definitely cons to code as well. So I want to cover that too. So moving over to code now I'm

**[0:09:31]** going to start with the cons with Python here. First of all, we obviously have a higher learning curve. Even with the help of AI coding assistance, which I cover so much on my channel nowadays, you still need to validate the code. And so, it's important for you to understand

**[0:09:47]** Python or really whatever language or AI agent framework you're working with. And so, it does take more to get yourself comfortable. And also, there is a higher chance of security issues. You need to know your stuff more. So, kind of related to the higher learning curve, but security I wanted to call out

**[0:10:04]** specifically because there's a lot that NAN handles for us with security because they manage the credentials. They help us set up the credentials like I showed earlier and so you have to worry about that less. Also, one of the biggest things with N8N is they give us the

**[0:10:19]** integrations ahead of time. We don't have to set up things oursel unless we're hitting the integration box. With code, that's different. Even if there are a million developers that have already set up a Google Drive integration, a lot of times you'll find yourself rebuilding it from scratch because there's no clear here's your

**[0:10:37]** node to dump into your workflow like we have with N8N. And then last but not least, code can often be very difficult to visualize. There are some tools to help this. For example, when I'm building my AI agents with Langraph, I have the Lang graph studio. So I can see

**[0:10:53]** for my multi- aent workflows, for example, here are the different agents that I have. Here's my guard rail. Here's my fallback. And I can see what my workflow looks like even as I execute it. And you have tools like Langfuse for tracing. So you can get a lot of

**[0:11:08]** visibility and sort of a visualization into what is going on, but it's never going to be as much of that canvas like we have with N8N. So definitely there is the advantage to no code tools there. But now we get into the pros of code. And this is where I think you'll really

**[0:11:25]** start to see why people will start with N8N but then move to Python for a lot of things. As much as both are fantastic because Python is where you have full control and customizability. There are limitations you'll hit with no code tools where there's just nothing you can do because when you have the

**[0:11:43]** code, that's when basically every possibility is open to you. Just to give one really quick example here in N. There isn't actually the idea of parallel execution. You can set up your workflow in a way where it will run two different things, but these will end up running simultaneously. Even though the

**[0:12:04]** workflow builder kind of makes it look like they're going to run in parallel, but in code, you can truly run things in parallel. For example, one of the AI agents that I build in the AI agent mastery course in Dynamis is this research agent that runs multiple research agents in parallel. So, for

**[0:12:24]** example, I can say I want to build an AI pet startup. And so, this AI agent helps me with competitor research. It helps me analyze SEO and marketing. Take a look at this. And it kicks off all of these specialized research agents at exactly the same time to help me with my

**[0:12:41]** request. And you can't do this in NAND. It's just not possible. But with Python and any programming language, we're able to do parallel execution. So, not only is it faster because the language itself is faster than no code tool, but also we're able to do things like parallel

**[0:12:57]** execution. Also, token streaming like you're seeing right here is another thing we can't do in N8N. So, just showing you a really good example of a couple of random things. You'll see this quite a bit where we have a better user experience, a better speed thanks to everything being in code. And going

**[0:13:13]** back, we got the better performance kind of like I've already covered. Also, access to top open-source AI tools and libraries. All these things that I've covered on my channel like graffiti for knowledge graphs, dockling for rag. We have crawl for AI for crawling websites. You can integrate these things with NN

**[0:13:30]** and I've shown some of that with like crawl for AI and graffiti for example, but it's a lot more difficult. It's not as simple as installing a Python package, setting up your environment variable, and then boom, you're good to go. And then the big thing that I mentioned a couple of times already is

**[0:13:44]** being able to use AI coding assistance because they are getting so powerful, especially tools like Codeex and Claude Code. Right now, you can build things so quickly that part of the advantage of N8N being easier to build things. That's starting to diminish just thanks to AI coding assistance. Also, code is always

**[0:14:04]** going to scale better even though Q mode is really nice for N8N. We can also run our agents locally. So, everything can be open source with Python assuming you're using the right tools. But then also there's no license concerns also assuming you are using the right tools. And then of course we've got version

**[0:14:22]** control with Git. So it's just a lot easier to manage our different environments, having backups and being able to revert to different versions of our code, the kinds of things that it's just not as realistic with our no code tools. So there you go. That was a lot

**[0:14:37]** of detail on the pros and cons of both, but I wanted to be very specific for you so that you can take what I said here. Think for yourself how it applies to your own use cases. Make the decision for you. And the last thing that I'll leave you with to consider is the hybrid

**[0:14:55]** approach. You don't have to just pick N8N or just pick Python. You can for example use N8N for the orchestration all of the entry points and integrations for your applications but then offload the heavy processing like your agents chunking for rag the data set handling for those larger files you can give that

**[0:15:14]** all to external Python microservices and even deploy both of the things together Python and N8N on the same instance in the cloud and I've even shown that on my channel before like with my graffiti MCP server video for example because then you can take advantage of the pros and

**[0:15:30]** cons of both platforms, using them together, relying on their strengths. So, I hope this video has been very helpful for you to help you make that allimportant decision that will apply no matter what you are building. And of course, let me know in the comments if you agree with what I'm covering here or

**[0:15:46]** if you think there are some nuances that I should be covering or anything that I've missed. And with that, if you appreciated this video and you're looking forward to more things on AI agents, I would really appreciate a like and a subscribe. And with that, I will see you in the next
