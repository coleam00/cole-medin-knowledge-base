---
type: raw-transcript
title: "Claude Computer Use + Bolt.new - The ULTIMATE AI Coding Combo?!"
youtube_id: R6AYmqcOXaw
url: https://www.youtube.com/watch?v=R6AYmqcOXaw
slug: claude-computer-use-boltnew-the-ultimate-ai-coding-combo
published: 2024-11-24
duration: "0:10:31"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** super super cool and this just kind of speaks to the direction that we are heading with AI where we're going to be able to be hands off the wheel having AI even researching to assist itself which is kind of what we're seeing here so a glimpse into the future really exciting

**[0:00:14]** stuff I have got a fun one for you today a very different kind of video super experimental but I'm really excited to show you what I have been playing around with so first of all AI coding assistants whether they're in the browser like with bolt new or autodev or

**[0:00:29]** as an IDE like windsurf or cursor are so powerful and save you hours and hours building literally any prototype for an app that you could dream of. But one major flaw with all of these is that they don't have external knowledge for crucial things like library documentation. And so you have this

**[0:00:46]** issue where they're not up to date with a lot of things that you might want to code. And what do I mean by that? Well, let me just go ahead and show you. All right, so I'm in the UI for Bolt because we are going to build an app that I can

**[0:00:56]** guarantee will fail even though Bolt is an incredible AI coding assistant. Now, the reason I can guarantee this is because we are going to build an app around a library that I know any LLM does not have knowledge of because it's a smaller library and it's relatively new as well. And the library is called

**[0:01:15]** N8N demo. It's essentially what allows N8N to display preview widgets on their website for their AI automation workflows. And so they have some instructions here on how to add it in your HTML. They have installation guides for how to include the script tags for all the JavaScript you need for it. But

**[0:01:33]** all this information a large language model like claude 3.5 sonnet used in Bolt does not have access to. This is the issue of external knowledge. So, I'm going to paste in this prompt here to build a frontend to display an N8N workflow with the N8N demo tool. And I

**[0:01:49]** give it the JSON for the workflow as well. But as you're about to see here, it is going to completely botch this because it doesn't have the information on this library that I just showed you to actually build this out. So, what I'm going to do here is pause and come back

**[0:02:03]** once Bolt is done trying to create this application. So, I had Bolt give its best shot and it completely failed just as I predicted. And I again I want to say this is not Bolt's fault at all. It is an incredible AI coding assistant. You're going to have this exact same

**[0:02:18]** problem with cursor windsurf autodev. It doesn't matter because it doesn't have the external knowledge of this N8N demo library. And so it even failed installing the dependencies here. It tried to fetch it from npm. Didn't do this right. Totally botched it. We have no preview here. I even had it try to

**[0:02:35]** fix itself and we've got nothing because it just doesn't know how to work with this library. It's plain and simple. It's almost as if we need rag for an AI coding assistant where we could somehow go out to the internet, fetch this information for how to use it and then

**[0:02:49]** also how to install it with the script tags and then feed that into the prompt to augment it so it has that information. And so you could build this into a platform like Bolt where it go and research the web before it actually fulfills your request, for example. Um,

**[0:03:05]** but what if you have other platforms that you want to integrate with where you have your own knowledge of your documentation and your code and stuff that you want to reference? It might actually be easier if you could just have an artificial intelligence controlling your computer, doing all

**[0:03:20]** this research for you on libraries and things like that, and then going back into something like Bolt and injecting what it finds in the prompt before it kicks off the code build. And that is exactly what I'm going to show you how to do right now using the Claude API for

**[0:03:36]** computer use. So, it's going to be really, really fun, super experimental, but let's dive right into it. So, what is the Claude computer use API? Well, really, it's exactly what you think it is. It is a way to use Claude to control your computer and do things for you like

**[0:03:50]** type in your input boxes, search the web, click through different applications, and it works so so well. And it's really it's a first of its kind, which is what allows us to do what I'm about to show you here. And if you scroll through this article, which I'll

**[0:04:04]** have linked in the description, you'll see a link here for a reference implementation. Clicking on this is going to bring you to this GitHub repository right here, where you can run it yourself with Docker very, very easily. And it's going to spin up a virtual machine so that you have the

**[0:04:19]** cloud computer use API working within this environment that's just in the browser. It looks like this. I'll show you right here. Um, and so it's not actually controlling your full computer, just this virtual machine right here because obviously it's kind of a security concern. They have a lot of

**[0:04:34]** caution around that if it's really controlling your computer. So they recommend running in an environment that looks like this where we can prompt claude on the left side and then have this kind of fake machine spun up for us on the right hand side. This is what we're going to be playing with right

**[0:04:47]** now. So it's so cool how it's easy to get started. You don't have to worry about security because this is all experimental. You just play around in this little test environment here. And that's what we're going to be doing. So, I have Bolt spun up right here. I'm

**[0:04:58]** signed in. It's just like I'm working in the browser on my own computer. But what I can do on the left hand side here in the Streamllet UI after I set my enthropic API key is I can tell it what I want it to do. And so, what I'm going

**[0:05:11]** to have it do is research the N8N demo component for me, figure out how to use it, how to install it, and then inject that into a prompt in Bolt. Have it create the full application for me. And this entire time I'm going to be doing nothing. Hands off the wheel. It's just

**[0:05:27]** going to be Claude navigating within this environment right here. And so yeah, let's go ahead and try it out. So as this is very experimental, I'm going to do a little bit of handholding in my prompt to Claude to give it a bit of information on how to research the N8N

**[0:05:42]** demo component. This kind of thing is not going to be something you can do to build any application or work with any library, but at some point it is going to get there with the power of large language models where you're going to be able to describe in just a couple of

**[0:05:55]** sentences what you want and it's going to be able to do all the research in the world you need to feed the kind of context into something like Bolt or like I said there might just be that kind of integration right in these AI coding assistants. And so the prompt that I

**[0:06:08]** have here I'll paste it on the lefth hand side. I'm basically telling it you have access to bolt new which I have up for you in the browser. Your job is to do some research on the nn demo component. Here's the website to go and do that research. That's the bit of the

**[0:06:21]** handholding that I was describing. It could potentially Google it itself, but it might find the wrong resource. Um, so I'm just guiding it there. And then I'm telling it the workflow JSON that I want to include for my N8N workflow preview. And then I give it some instructions on

**[0:06:36]** how to actually fulfill my request here. So again, a little bit of handholding, but it's just still so so cool what it can actually do. So I'm going to start in just a blank tab in Firefox here, send it in, and let's see what this thing can do. I'm going to fast forward

**[0:06:50]** as it goes through all the actions here and come back and start talking again once it is done. All right. So, it doesn't show anything right now, and it's because it messed up its research just a little bit. Uh, if I scroll up to the top of the prompt here, it didn't give all of

**[0:07:20]** the script tags to include. It just included one. So, it messed up a little bit. So, I'm going to have it fix itself here. Again, this is all experimental. Can't expect it to work super well right now. But, it's just so cool the direction that we are heading with AI

**[0:07:34]** that it's getting to the point where you could probably do this kind of thing pretty soon here. So, I'm going to have it correct itself. I'm going to say you need uh these three script tags. So, I'll paste it in. Boom. and then have it update itself and then um I'll come back

**[0:07:48]** again once it has finished this iteration. Boom. All right, we can click show workflow. And this isn't actually going to work because you can't have I frames within the web container. But that's totally okay because what we can do is just deploy it to Netlefi now. And then I will actually be able to view it

**[0:08:09]** in Netlefi. And yeah, I've tested this before. It works really, really well. every single time the iframe doesn't work. So the LLM didn't mess up here. It's just getting blocked by a course policy or something like that. Um, so let's have it deployed to Netlefi and then try it out there. All right, great.

**[0:08:24]** So now we have Netlefi. So I'm going to click on this link and then I'm also going to full screen it here. So boom, there we go. All right, N8N workflow viewer. It's loading my workflow and there we go. We got the preview widget. Um, and we can zoom in, zoom out, click

**[0:08:37]** into the node and look at that. This is absolutely fantastic. And obviously it's a super basic uh JSON workflow for a single node right now, but you could have any end workflow displayed on the site in this way. Super super cool. We built this all without having to touch

**[0:08:55]** anything besides that little correction at the end there. Um but you could see that if I didn't have the cloud computer use API do that research before this, it completely botched it. Didn't even come close. But now it actually got that information it needed on how to create

**[0:09:10]** this widget and install it with a little bit of handholding from me. Super super cool. And this just kind of speaks to the direction that we are heading with AI where we're going to be able to be hands off the wheel having AI even researching to assist itself which is

**[0:09:24]** kind of what we're seeing here. So a glimpse into the future. Really exciting stuff. If this doesn't get you jazzed up, I don't know what will. It is just so cool to me that I have a large language model, research the web on library documentation for me, craft a

**[0:09:37]** beautiful prompt to then feed it into another LLM that writes all the code, runs all the commands, spins up this environment for me to play around with the website, and I barely had to hold its hand. And I definitely will have to less and less as large language models

**[0:09:50]** get more powerful and as we start to do things like even creating documentation on the web specifically for AI to scrape. I think that's a big thing coming in the future as well. So, I hope that this demo is just a nice little glimpse into the future for you because

**[0:10:03]** it's definitely going to get to a point where Rag for AI coding assistance, as I'm calling it, is going to be very doable either through computer use like I showed or just direct integrations within these AI idees like Windsurf for example. So, just so cool and yeah, very

**[0:10:20]** experimental at this point, but it's going to get very real very very fast. So, if you appreciated this, I would really appreciate a like and a subscribe. And with that, I will see you in the next
