---
type: raw-transcript
title: "This MCP Server for AI Coding Assistants Will 10x Your Productivity"
youtube_id: G7gK8H6u7Rs
url: https://www.youtube.com/watch?v=G7gK8H6u7Rs
slug: this-mcp-server-for-ai-coding-assistants-will-10x-your-productivity
published: 2025-04-20
duration: "0:15:33"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** AI coding assistants are extremely powerful. If you're a software engineer they'll make you at least 10 times faster at your job. And if you're not as technical, well then they'll allow you to build things that you could have only dreamed of making in the past. But we all know that their biggest limitation

**[0:00:15]** right now is that when you work with specific tools or frameworks, they hallucinate all the time. What we really need is a tool that gives us instant rag for our AI coding assistants so they have that necessary context for our tools and frameworks. And I have found exactly that. An incredible new tool

**[0:00:34]** that is also free called Context 7. And it's the kind of thing that where once you see it, you'll definitely think to yourself, how is this not been a thing already? So right now, allow me to introduce you to Context 7 and how you can get it up and running yourself in

**[0:00:48]** just minutes to code anything better. So, here's the homepage of Contact 7 which I'll link to in the description of this video. And the first thing that jumped out to me is the fact that there are 1,856 different tools and frameworks that we can add into our AI coding

**[0:01:05]** assistance with Context 7 so that they can perform rag on all of this documentation. That is just insane to me. And they have the documentation for everything you would care about. They've got Nex.js, JS, MongoDB, Superbase, a ton of others that we don't see here like Pyantic AI, React, Langraph, MCP.

**[0:01:25]** To me, it feels like they have it all. They have everything that I would care about using at least when I'm building my apps. So, ignore the navigation for now. I know that the MCP server is probably screaming out to you, but we'll get to that. The first thing I want to

**[0:01:37]** do though is show you one of these individual pages. Like, we can click into Superbase. We can see some metadata like the total number of tokens that make up this documentation which we don't have to send all of this into the LLM of course. That's why we do a

**[0:01:49]** directed lookup with rag and we'll see that in a second. But then we can also refresh this documentation at any point. So also everything that we have in context 7 is going to be completely up to date and we can refresh it to really make sure that is the case. And then in

**[0:02:03]** the UI we can basically perform the rag ourselves that our AI coding assistant will be doing. So we can see how it works under the hood. So I can search for authentication for example and click on show results. This is exactly what would be given into our AI coding

**[0:02:17]** assistant if it were to search the superbase documentation for authentication. And we can even control the number of tokens that we get back from the search. And my favorite part about contact 7 overall is just how well structured the documentation is. This is not your average LLM.ext text where you

**[0:02:36]** just take the entire documentation for a specific framework, dump it in a single file to send into the LLM and chunk up. Instead, they have all of these individual components that they've curated as these little snippets that we can feed into the LLM in a way that it

**[0:02:51]** can parse it very well. And also, each of these components are examples to help the LLM see how to use this tool and framework. And I've covered this on my channel before, but I think that giving examples to the LLM is really the best way to help it code reliably. And it

**[0:03:06]** seems like Contact 7 has really taken advantage of that fact. Like they've built all of their documentation around providing just a ton of examples based on whatever we are searching for like authentication. That is so powerful. So let me be clear here. There are AI coding assistants like Cursor that

**[0:03:24]** already have something similar baked into the platform. Like with cursor, we can add custom documentation. But this is provably less powerful than context 7 because of the way that they curate all these examples in their documentation and also because of some things that they have in their MCP server. So

**[0:03:41]** speaking of that, let's get into the MCP server and see how we can really use this for ourselves. And this MCP server is our key to implement this into our own AI coding assistance. So I'll link to this in the description as well. And they have a nice read me here to help

**[0:03:55]** get us started. First talking about what we have to deal with without context 7. All these things that we've definitely seen before, like hallucinating APIs that don't even exist, getting generic answers from old package versions, and what we get with context 7 is everything that I've already been telling you, like

**[0:04:11]** getting up-to-date version specific documentation with code examples. That is the key. And it's all straight from the source. I don't know how they're able to scrape from almost 1,900 different pieces of documentation and getting that all up to date constantly. I'm very impressed with this platform as a whole. But yeah, they pull it off for

**[0:04:29]** us. And so they also have instructions for installing this in our AI idees like cursor and windsurf. And then the process for doing it in other ones like client or rue code is going to look pretty much the same. We just have to copy this JSON configuration. And then

**[0:04:44]** I'll show you really quick how to do it within windsurf. And so in Windsor, if you just have to click on this hammer icon for MCP servers, click on configure. It'll open up this MCP config.json file where you can then paste in that configuration that you copied from GitHub. In this case, I

**[0:05:00]** already have it set up using context 7 as this first MCP server in my configuration. So then you can just save it after you make those changes. I'm going to just close out of this for now. And then once you hit refresh, it'll reload your MCP servers and you should

**[0:05:14]** see context 7 with two tools that are available to us. And it's worth understanding how these tools work so we can leverage them properly. So I'm going to focus on this for a little bit. Then we'll use contact 7 within Windsurf to build a really cool AI agent. And so

**[0:05:29]** I'll go back to the readme because they do talk about these tools very briefly here. The first one is a tool to resolve a library ID. And all that means is that our AI coding assistant is going to give a search term like superbase for example and then we'll get a list of the most

**[0:05:45]** relevant documentation pages and it'll find the ID for the one that it wants to perform rag on. Like maybe superbase is going to have an ID of /supase something like that. It has to get that exact ID and then it can call the get library docs function once it has that exact ID.

**[0:06:02]** So this is the tool where we perform rag over the documentation for a framework or tool like superbase or nex.js JS whatever that might be and then our AI coding assistant also decides the topic which going back here that's going to be something like authentication or in Pantic AI it might be an agent or in

**[0:06:21]** crew AI it might be agent handoffs like whatever that search term is the agent decides it right here for the topic and then it can also decide the number of tokens that it's going to get back from the search so this is yet another thing that makes it more powerful than

**[0:06:36]** something like the custom docs built into cursor our agent can actually reason about how many tokens it thinks it has to fetch from the documentation and we can instruct it through something like global rules to tweak this value ourselves. It's very powerful because you might need to fetch a different

**[0:06:52]** number of tokens depending on the documentation that you are using. And so with that, let's go back into Windsurf and build something really cool with contact 7. And I do want to mention that I have my full process for building with AI coding assistance already. I covered that on my channel previously. I'll link

**[0:07:08]** to that above. I'd highly recommend checking that out because that entire process is very complimentary to using Context 7. I'm really just using Context 7 as yet another MCP server to make my process even more powerful. So, like you saw in that video, I've got my planning.md file that you're looking at

**[0:07:26]** right here. I've got my task file. I have my project rules set up, which I'll open this and show you. Everything is exactly the same as what I covered in that video, except I also have this section at the top for context 7. And you'll probably want to tweak this to

**[0:07:40]** your needs. Like, for example, I'm telling it to start with 5,000 tokens for its search and then increase to 20,000 tokens if it needs to, and then as a fallback, use the Brave MCP server. So, specific to the exact workflow, I've been kind of just going through trial

**[0:07:55]** and error with Context 7, figuring out how to use it best. But really in my global rules, this is a place for me to tell it how I want it to use those two tools that we just went over. And so I'm giving that extra context so it can

**[0:08:06]** really leverage context 7 the best. And so with that, what we're going to build right now is an AI agent that itself can use context 7 for rags. So this is going to be super meta. I'm using Context 7 in Windsurf to build an AI agent that can

**[0:08:21]** use Context 7 just to show a really simple yet powerful example. The sponsor of today's video is Scribba, a platform that turns coding tutorials into interactive pair programming sessions where you can edit the instructor's code in real time. It completely revolutionizes the way that you learn how to code. And honestly, it blows my

**[0:08:40]** mind. While AI can help us code faster the foundation of being a great developer still rests on understanding the core concepts both for the front end and back end. And that is where Scribba comes in. And they just released something very exciting. Scribba has primarily focused on front-end

**[0:08:56]** development courses in the past, but now they have released a comprehensive suite of full stack development courses. So you can master superbase, express, SQL Nex.js, all these important technologies. And they have a lot more courses coming soon. What makes Scribba truly special is a revolutionary scrim technology. That's what lets us pair

**[0:09:15]** program with the instructor. Take a look at this. Right now, I'm watching one of the videos from the Superbase course. The instructor is explaining some code to me. He's editing things in this file as well. I have it muted, which is why you can't hear him right now, but you

**[0:09:28]** can see the subtitles in the bottom. This video is currently playing. And the really cool part is at any point within this video, I can start editing the code myself. It'll pause where the instructor currently is. I can make my own changes. I can see them live within the website

**[0:09:43]** that's running in the top right. I can even get instant feedback from AI on the changes that I'm making. And there are specific challenge points in the videos where the instructor will prompt you to make your own changes as a part of the course. It is so neat. I've never seen

**[0:09:57]** anything like this before. It's just so interactive. Scribba has everything that you need to master full stack development. So head on over to scribba.com. I'll have links in the description as well. This is your chance to level up your coding skills and they have free courses to help you get

**[0:10:12]** started. And so I already have a prompt prep for this. I'm going to use pideantic AI as my AI agent framework to build this agent and using context 7 to get the documentation for it within Windsurf. Just like we saw with cursor there is a native way to get the

**[0:10:27]** documentation for podantic AI. But like I told you earlier, the results that I get with context 7 is just way better than using the documentation retrieval that's built into the AI IDE. So, we're going to use it to search Pantic AI and then it's going to integrate contact 7

**[0:10:42]** as an MCP server just like we did in Windinsurf, but it's going to set up everything for us. And this is a little bit more of a technical thing, but it's going to have the base URL and specific model be environment variables. So, we can control that to use any model that

**[0:10:56]** we want from Open Router or Olama Gemini, OpenAI. We get to pick that and then it'll also create a simple command line interface so we can chat with our agent in a terminal. And so because I instruct it in the global rules to check the planning and task files, it's going

**[0:11:11]** to do that first. And so I'll have to give it some time to check those files and then do some other preliminary work. But then after a little bit, it'll get into using our MCP server for context 7. And there we go. I skipped ahead a bit just because there was some initial work

**[0:11:26]** that I had to do. But yeah, it made that first call to resolve the library ID for Padantic AI. Then that second call to get library docs just like we knew it would do. Now that it had that ID, it's searching for 20,000 tokens. These are all the chunks that it got back, which

**[0:11:41]** are looking like the exact examples that I have seen before in the Pantic AI documentation. Makes another search to get some information on the configuration. And then it decides to finalize things with the Brave web search as well. Not really sure why it needs this, but I guess it could only

**[0:11:56]** really help. It only costs one flow credit anyway. And there we go. So now it creates the agent. So we got that created. And then we have all this other stuff that it created as I was explaining everything as well. And so with that, I think we're actually good

**[0:12:08]** to go. Maybe I'll ask it like, are you done? Because sometimes Windinsurf does this thing where it'll pause in the middle of implementing things. So I'll see. Okay. Yeah. So it's not quite done. So I'm going to pause and come back once we have everything implemented. And boom, there we go. We have our full

**[0:12:23]** agent built out with the help of contact 7. And I did have to iterate twice off camera. There's just a couple of little errors that came up, but now I have everything working perfectly. I haven't even accepted the changes yet. So, you can see that this is hot off the press.

**[0:12:35]** All this code is brand new in the 13 files that it created for us. And so I'm going to accept this now. And then I'll go over to my terminal and we can run this thing. And so, I have my environment variables set up already in thev based on

**[0:12:49]** thev.example that it gave me. I have my virtual environment activated with all the packages installed. Now I can run the command python main.py and then I'll use the chat command. And it made a really beautiful command line interface here. Like I actually have not worked with something that looks this nice in a

**[0:13:06]** long time in the command line. So I can say a basic message like hello. Look at that. It's thinking thinking. It'll give me a response here. And then I can make sure conversation history is working. I can say um what did I just say? So just kind of the little preliminary tests

**[0:13:21]** that I usually like to do when I've created a new agent. Making sure everything's working there. You just said hi. Cool. Yeah. So now I want to leverage context 7. And so I'll say what superbase docs are available to me. So I want it to first call that tool to

**[0:13:36]** search for the documentation IDs that are available. Print that out to me. There we go. I got nux superbase superbase couple of others here. And then we have all the context 7 ids. So this is looking great. Our agent that we made, our custom agent is integrated with context 7. And so now I can say

**[0:13:53]** great use this to tell me how to watch for real time changes in my Superbase DB. All right. So just kind of some specific random example here just to make sure that it can perform rag on the Superbase documentation using all the examples that it has in its arsenal to

**[0:14:10]** give me some working code here. I'm not going to go and actually test this right now, but I'll just see if it looks good to me. And yeah, subscribing to the channel ID for Postgress changes from my knowledge of Superbase and how this works with JavaScript code. This looks

**[0:14:25]** good. Yeah, especially this like this. This looks very very familiar to me. So there we go. We performed rag on Superbase and now our agent is instantly hooked into almost 1,900 different documentation sources using context 7. If it wasn't for that, we would have to scrape all these pages ourselves, store

**[0:14:42]** it all, and embed it all into our Superbase database or Quadrant wherever, hook that all into our agent. But now we have this all through a single MCP server. This is just so cool. Like really, Context 7 just changes the game for agents and AI coding assistants. So there you have it.

**[0:14:58]** Context 7 in a nutshell and how you can use it to level up your AI coding game. And you can just take this MCP server for contact 7 and put it into whatever your current process looks like for using AI coding assistance. It doesn't matter if you're using my process that

**[0:15:13]** I've shared on my channel or a tool like Claude Taskmaster. This is just going to make anything even more powerful for your AI coding. So if you appreciated this video and you're looking forward to more things AI coding and AI agents, I would really appreciate a like and a

**[0:15:28]** subscribe. And with that, I will see you in the next
