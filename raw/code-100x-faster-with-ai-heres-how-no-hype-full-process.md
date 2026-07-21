---
type: raw-transcript
title: "Code 100x Faster with AI, Here's How (No Hype, FULL Process)"
youtube_id: SS5DYx6mPw8
url: https://www.youtube.com/watch?v=SS5DYx6mPw8
slug: code-100x-faster-with-ai-heres-how-no-hype-full-process
published: 2025-03-30
duration: "0:32:10"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Everyone knows that if you're not using an AI coding assistant, you are going to fall behind no matter what you are developing. But what people usually don't know is how to use these AI coding assistants effectively. I mean, sure you can't just throw whatever you want at an AI IDE like Windsurf or Cursor

**[0:00:17]** and sometimes you'll get good results but if you don't have a clear process for working with them, that is definitely not the case all the time. And it is so frustrating when the LLM goes from a senior software engineer to what seems like a pack of primates mashing on a keyboard, deleting parts of

**[0:00:34]** your code, implementing features that you don't want, you know the pain. And you have to have a well- definfined process when using AI to code if you want highquality outputs and you want them consistently. And if you don't have that refined process yet, I promise you that by the end of this video, you'll be

**[0:00:51]** at a whole new dimension of developing with AI, cuz I'm going to walk you through my full workflow step by step and just get into those nitty-gritty details so you can just copy my process to 10x, even 100x your productivity when developing with AI. And to make this

**[0:01:07]** well worth your time, there are three things that I'm going to promise to you. The first is that we're not going to over complicate our setup, which I see people do a lot with AIDS. The second thing is we're not just building a toy. We're going to use this workflow to

**[0:01:20]** build a full practical and useful example with a superbase MCP server. More on that in this video. And then the third thing is that this process is going to work for you no matter what you are developing or which AI IDE you are using. Last thing really quick. If you

**[0:01:35]** want to level up more than just your AI coding workflow, but your AI skills as a whole, I have the perfect thing for you. Check out dynamis.ai. It's an exclusive community that I just launched the weight list for. It's where I take my expertise that I bring to you constantly

**[0:01:48]** on YouTube to a much deeper level with courses, live workshops, weekly sessions, daily support, and the best part, a community for you to join with other early AI adopters. So check out the link, join the weight list, and with that, let's dive into our full process for coding with AI. So what you're

**[0:02:05]** looking at here is a Google doc, which I'll link to in the description of this video, that gives my full process of coding with AI. So use this as a resource for yourself. We're going to be referencing this constantly throughout the video as well because this is everything. This is our full process

**[0:02:21]** starting with the golden rules at the top. So, I'll cover these quick and then we'll see how they really dictate a lot of the rest of our process starting with step number two where we'll go into actually starting our project. And so the very first golden rule, this one's

**[0:02:34]** super important. We want to use these higher level markdown documents that have instructions for installation documentation, planning, and tasks. Use these to give context to our LLM. And so we're going to be creating and managing these using AI to help throughout the creation of our project. And then the

**[0:02:53]** next three rules here are all about not overwhelming the LLM because the longer context you give to an LLM, the more likely it is to hallucinate. And so, for example, you want to keep all of your code files under 500 lines. You want to start fresh conversations often because

**[0:03:10]** longer conversations can really bog down an LLM. And then also, you don't want to overwhelm the LLM by asking it to do too many things at the same time. In fact, I usually find that it's best to just ask it to do one new feature or implement one new thing per prompt that I give it.

**[0:03:26]** Much better results. If you have really long files, long conversations, you're asking for a lot of things at the same time, that's when you start to get terrible results no matter which LLM or AI IDE you are using. And then also, not everyone likes tests. Most people don't.

**[0:03:41]** But it's very important to ask the AI to write tests for its code. Ideally, after every new feature that it implements and that's how you really get consistent output. Also, be specific with your requests. And so, this is where it's actually better to provide a little bit of extra context. And so, you don't want

**[0:03:58]** to overwhelm the LLM, but you also don't want it to be left to its own devices. You want to be very specific with what you're looking for. Like don't just describe what you want to build at a high level, but get into the details of the technologies that you want it to

**[0:04:11]** use, the different libraries, what you want the output to look like. Be specific and that helps a lot as well. And then the last two rules here, write docs and comments as you go. You want the LLM to constantly be updating documentation both in these uh you know

**[0:04:26]** higher level core files, but also comments in the code as well. that helps both yourself to understand what it's doing and also itself as it references these files in later conversations. And then the very last thing is to implement environment variables yourself. Do not trust the LLM with your API keys and

**[0:04:45]** securing your database, all that good stuff, because you do not want to be this guy. I put this link in here cuz I just thought it was really funny. This is an example of what can go seriously wrong when you vibe code. This guy built his full SAS with Cursor. He didn't do

**[0:04:59]** any of the coding and he's all hyped here. This is March 15th. He's like, "AI is not just an assistant. It's the builder now." But then look at this. Two days later, he gets hacked. Random things are happening. Maxed out usage on API keys, people bypassing subscriptions, probably because he

**[0:05:14]** didn't have correct database security. All these things going wrong because he trusted AI to manage his environment variables, his database security, all of the things around security. You have to make sure you understand yourself. And really, you should understand all the code that AI is producing. I generally

**[0:05:31]** don't recommend vibe coding, but even if you do vibe code, at least make sure that you understand if your project is secure or not. That is super important. And so, with all these golden rules out of the way, we'll see these constantly throughout the rest of this document

**[0:05:45]** let's get into starting our project beginning with our planning. So, for the planning phase, it's pretty simple. We just want to create our planning and task files. And we're going to do this before we're even getting into any coding at all because we want to have that higher level direction before we

**[0:05:59]** write a single line of code. And so our planning document, this is where we have the highle vision, architecture constraints, all of these highlevel pieces of information that we want to give as context to the LLM. And we can ask the LLM, the AI coding assistant throughout the process to reference this

**[0:06:16]** file, which is especially useful at the beginning of new conversations so it can quickly get up to speed with everything that we're doing in our project. So it doesn't have to analyze different code files to figure that out itself. And then at a slightly lower level, we have

**[0:06:30]** the task markdown file. This is where we track all of our tasks, things that have been done and still need to be done. And throughout the conversation, we can have the LLM update and create new tasks delete tasks, mark them as done, all that good stuff. And that really allows

**[0:06:46]** us to be the project manager for the AI coding assistant, which is important because we want to dictate everything that it does. And this is just a resource for us to do that well and have the AI coding assistant help in that process, too. And so for creating these

**[0:07:00]** files, I usually don't even do this in an AI IDE. I'll just use a chatbot like Claw Desktop for example. And so I have this sample prompt right here for the Superbase MCP server that we want to create. And so we're using MCP as a connector. So we can use apps like Claw

**[0:07:16]** Desktop, our own AI agents to connect to Superbase so that it has tools to do things in our database. And so for the planning for this, I'm just telling it to use the Brave API because I have the Brave MCP server set up. I'm not going to get into a ton of details on this

**[0:07:32]** because that's kind of outside of the scope of this video. Just use this as an example for very quickly asking it to plan both the planning.md and task.md files. And so I'll send in this prompt and then it'll search the web for me. So I'll allow it to do that and then let me

**[0:07:48]** come back once it has created both of these files. And there we go. Claw desktop created both files for me. And it did it right there in my file system because I have the MCP server for that too. So it made him right here in this directory. So I can open that up in

**[0:08:01]** Windsurf which you can use any AI coding assistant. Just keep that in mind. I'm using Windsurf but this will work with cursor client root code. It doesn't matter. This process applies to all. And here we have our planning file. So I'm going to need to open this preview here

**[0:08:16]** and take a look at this. We have our overview. We have the project scope, the technical architecture, technology stack, all these things that we can now give as context to the AI coding assistant when it starts the project to make sure that it's starting on the right foot. This is certainly not a

**[0:08:32]** perfect document. Like I wouldn't really want a what is MCP and what is superbase section. We don't really care about that. And so I'm going to edit this off camera and just save you the boring details here. But this is a good starting point. And typically you will

**[0:08:44]** want to iterate on this quite a bit within the chatbot or wherever you're working on this file. And then we've got our tasks as well. So I can open a preview for this. We can see all the different tasks that it set up for us. And we'll have the AI coding assistant

**[0:08:57]** knock these out one by one and add new ones as necessary as well. And this is pretty overkill. So again, you're going to want to iterate on these thing. Like we don't need that many tasks for this. This is pretty crazy. Um but yeah, I mean this is a good starting point. One

**[0:09:11]** last tip that I want to give on the planning phase, something I like to do a lot is instead of just using a single LLM like Claude, I want to use multiple different large language models to help me plan my project. So, I'll just give the same prompt to each of them and then

**[0:09:24]** combine everything at the end. Now, the trick is you have to have a good platform that can help you work with these different LLMs in one place without having to pay multiple subscriptions. And there are a lot of different apps out there for that. But one of my favorites that is sponsoring

**[0:09:38]** this video, but I do use them a lot is Global GPT because they're very affordable. You can get started for free with access to all the best LLMs like Deepseek and 03 and Claude. And they even have tools added in like Deep Research or Perplexity for example. If

**[0:09:54]** you really want to go deep in your planning, you can do that with Global GPT. And there's a lot of other tools as well, like if you wanted to use ideoggram or midjourney to help you plan your assets for your project as well. You can do all of that. So, you're going

**[0:10:06]** to have an interface that's very similar to Claude Desktop like we just saw, but just being able to access these different LLMs very easily, do things like deep research. And so, yeah definitely use a platform like this if you want to really dive deep in your planning for your project. So, I'll have

**[0:10:22]** a link in the description to Global GPT. Definitely recommend checking them out. But yeah, that's just the last quick tip that I wanted to give for planning your projects. Now, let's get into the next phase. Now that we have the planning and tasks done, it's time to move on to

**[0:10:35]** global rules. This is essentially system prompts for your AI coding assistant. So, all the high-level instructions that you want to give to the AI coding assistant, you do in the global rules so you don't have to type it out explicitly every time. Like for example in our global rule we can say always read the

**[0:10:54]** planning file at the start of a new conversation. So that way when we start the conversation ourselves we don't have to explicitly ask it to do so. And so it saves you from typing a lot on all your different requests because instead of saying please implement this and then

**[0:11:08]** write tests and then check off the task you can just tell it to do so in the global rules like check the tasks, make sure you write your tests for all your new features. We have that all now as kind of a system prompt to the LLM. This

**[0:11:21]** is the global rule that I have set up in my AI coding assistant. You can use this yourself. Tweak it to your needs depending on your technology stack and any other requirements that you have. But yeah, this is a really good starting point for you. And then I even have

**[0:11:33]** instructions for the four most popular AI idees how you can get this set up. And so specifically, let me copy this. I'll show you how to do it in Windsurf because that's just the AI IDE I'm using in this video. I'll copy this and then I'll go over to Windsurf and then you

**[0:11:50]** click on the additional options in the top right manage memories and then you have your global rules. This is going to apply no matter what directory you're in. And then you have workspace specific rules. So if you want to have rules for just your current project, you set it up

**[0:12:04]** here. Typically, it's recommended to have workspace rules because a lot of times different things like the technologies that you're asking it to use are going to be specific to that project. And so, I would typically recommend workspace rules. So, we can go into here and then just paste in

**[0:12:21]** everything that we copied from the Google doc. And then I can just like my other markdown files, I can open up a preview and see that we have now have these rules set up for the AI coding assistant. So, we tell it how to use these different markdown files. This is

**[0:12:34]** how without having to always ask it to look at planning and mark off tasks in the prompts on the right hand side it'll still know how to work with these files. And then we tell it about some of our other golden rules like don't create files that are longer than 500 lines. We

**[0:12:48]** tell it about creating tests for each of the features. Um, and then we give it some style guidelines as well to make sure that the code is clean that it produces. We tell it how to work with the readme file so it can maintain documentation. And then at the bottom, I

**[0:13:02]** like to have a bunch of kind of miscellaneous rules to help it as well. So that is our rules as a whole. And now we can keep our prompts to the LLM quite simple because we have all these different things we're trying to have it do and make sure it's following, but we

**[0:13:17]** don't have to ask it each time. Now that's the important part with global rules. So, we've got our global rule set up now. Should have just taken you a couple of minutes. Now, we can move on to configuring our MCP servers. So, if you are not familiar with MCP, I would

**[0:13:30]** highly recommend checking out this video that I linked to above where I did a comprehensive overview, but really it's just a way to give more tools to our AI IDE so it can do things like search the web with Brave. So, these are the core three servers that I always use that

**[0:13:44]** I'll go over in a bit. I've got links to install each of them. I've got instructions for how to set up MCP in your different AIDes and even a link here to a list of other MCP servers. You can go here and download any other ones that you might want to include. You can

**[0:13:58]** click into any of these links to see exactly how to set it up within your AI IDE. So, it gives the instructions for setting up your configuration. So, the core three servers that I always use, I want my AI IDE to be able to interact with the file system, not just the

**[0:14:14]** current project, but other folders on my computer as well. Like maybe I have an image folder. I want it to be able to pull assets into the project from that. or I want it to reference other projects to learn how I did something previously. I can do all of that when I have the

**[0:14:28]** file system server. And then I also want my AI IDE to be able to search the web. And some AI idees have web search baked in. But the Brave API is very powerful in the way that it actually uses AI under the hood to summarize a bunch of

**[0:14:44]** the different web search results. So you get some really powerful output. You can use this to do things like pull documentation for tools, libraries or frameworks that you are using. And then the last one that I really like using is Git. And the reason for this is you

**[0:14:58]** should really set up every project as a Git repository. So you have version control. You can manage backups of your projects, have different versions that are all saved. And so with the git MCP server, you can do something like this example prompt that I have here where you say like, okay, I like where we're

**[0:15:14]** at right now, and before I implement more features, I want to really have a backup of the current state. So please make a git commit to save the current state, which by the way, this is something that I highly highly recommend doing because sometimes you can go five

**[0:15:28]** requests, 10 requests to an AI IDE. It implements all these things and you realize that it completely broke the project five requests ago. So if you have backups along the way, you can revert to a working state. Otherwise sometimes you'll get into this state of hell where your project is totally

**[0:15:44]** broken, but you've gone too far and you can't really go back. And so Git is your savior for that. So that's why I love using this server so much. And then also, if you want to have more like long-term memory, implement rag within your AI IDE, you have a lot of other

**[0:15:57]** tools. For example, the Quadrant MCP server. So, I'm not going to get into that cuz a lot of AI idees like Windsurf already have memories. Like I can go in here and manage memories and it can generate those for me. I just have a blank slate right now, but you can ask

**[0:16:11]** it to keep track of memories between projects and stuff. So, might not need something like this, but there's still great MCP servers anyway. So, yeah, get all these set up. In my case, let me go back over to Windsurf here, and I'll open up my configuration. You just click

**[0:16:24]** on configure MCP right here. And I have this MCP config.json. So yeah, you can see I have my file system, Brave Search Git, and then this is kind of out of the scope of this video, but I have Archon which is my AI agent builder that I have

**[0:16:39]** baked into Windinsurf as well. So I set up all these servers. Just follow the instructions that I have laid out right here in this document. So get your MCP set up and then use those as I describe throughout your project and it's going to help you a lot. So now it is time to

**[0:16:55]** give that initial prompt to the AI IDE to start our project because we have our MCP servers configured, our global rules set up and we have those planning and task documents created. And like I call out here, even though we have these documents that give those higher level

**[0:17:10]** details to the AI, we still want to be very specific with our initial prompt because that determines the entire starting point for our project and that is one of our golden rules to be very detailed in what we are looking for. And so this can mean a lot of different

**[0:17:25]** things depending on your project. But the key piece of advice that I have here is to give a lot of documentation and examples to the AI coding assistant. And there are three different ways that we can provide examples and documentation. The first one is that a lot of AI idees

**[0:17:41]** have built-in features for pulling in documentation. For example, in Windsurf I can type at MCP and then hit tab. And that's going to now include the MCP documentation in the prompt to the LLM. So it'll use rag under the hood to search through the documentation and use that to augment its answer. You can do

**[0:18:01]** something very similar in other AI idees like cursor as well. The other option you have is using the Brave MCP server or any other MCP server that you set up for web search. So you can ask it to you know go through the internet find documentation for whatever libraries or

**[0:18:15]** tools you are using like for example search the web to find other MCP server implementations or documentation. So you can pull examples and docs this way or just provide them manually like in this example prompt that I have that we're going to be using to create the superbase MCP server. I'm just giving it

**[0:18:32]** a link to a GitHub repo that has an already existing implementation of a Python MCP server. So it's using this example kind of as documentation along with I call out the documentation for MCP and superbase at the top here. And so this is an example prompt that is

**[0:18:49]** very specific to what I am creating here. But use this just as a template for you. You want to call out documentation, give examples, be very specific in what you want it to build and then you're going to get much better results than just saying something super bland like build a superbase MCP server.

**[0:19:06]** So, we're going to take this prompt, go into Windsurf. I already have this entered in. So, I'm going to go ahead and send this in, and we'll watch it rip. And for example, I'm not even calling out the planning.md file anywhere in this prompt. But it's still going to reference that after it pulls

**[0:19:22]** the documentation for MCP and Superbase because we have that called out in the project level rules, those global rules that we set for just this workspace. And so, first it's looking through the GitHub example I gave it. It's going through the documentation. It's using the Brave web search to get Superbase

**[0:19:40]** Python client documentation. It's doing a lot here. And this is taking a lot of flow action. So, a lot of credits being spent here, but it's important to have the best starting point you can. And so generally, I'm okay with having it do quite a bit at the start here. And you

**[0:19:55]** can always prompt it to not do as much. Um, and so I'm going to let it go through all of this documentation searching here, and then I'll come back once it's moved on to the next step. All right, so it's finished looking through all the documentation. Now, look at

**[0:20:08]** that. Boom. We're moving on to analyzing the planning and tasks files. So, it's pulling in all of that extra context. And then, for some reason, it wants to create a directory, I guess. Yeah, it's planning to write the tests already. I mean, this is good. It's following that

**[0:20:21]** global rule as well. So, we'll let it create that directory. Like, there we go. Superbase mcpests. And now it's moving on to coding up everything. So it starts with the requirements.ext and then I assume it'll get into creating Yep, there we go. The server.py. And this will take a little

**[0:20:35]** bit because there's going to be a good amount of code that goes into this. So what I'm going to do here is pause and come back once it has implemented the first iteration of my server. And there we go. Windsurf created the full superbase MCP server for us in a single

**[0:20:48]** prompt. And this is not a basic implementation. It's almost 300 lines of code and it looks really good. We've got the ability to delete records, update records, we can create records. And then last, we have a tool to read rows in a table. And this very much shows that

**[0:21:07]** Windinsurf understood the MCP documentation. Like even the way that it sets up the Superbase client and defines all of our tools. It very much read through documentation, synthesized that with our markdown files for planning and tasks to create this beautiful piece of code. And if we go into the tasks

**[0:21:23]** markdown file, take a look at this. It marked off the tasks as complete. It didn't make any tests or update the readme, which I kind of wish it did. It made the tests folder, but then didn't write tests, which is kind of strange. I mean, you get weird behavior like that

**[0:21:36]** sometimes where it it understands the global rules, but doesn't do everything you would want. But that's okay cuz we'll just do that in a follow-up prompt, and I'll show you that in a second. But first, let's actually test this and see if it's working. So, we have this MCP server created locally

**[0:21:49]** now. And I do want to make a dedicated video on creating MCP servers, by the way. So let me know in the comments if you're interested in that. I'm going to kind of gloss over the implementation and running this right now because the point of this video is to show my

**[0:22:01]** process for coding with AI, not making an MCP server. So anyway, in cloud desktop here, I'm going to hook in the server. So you just go to the top left file, settings, developer, and then you click on edit config. It'll open the configuration folder. We can go to the

**[0:22:17]** cloudmcpconfig.json. JSON file which I have open right here in windsurf. So this is where I have all of my servers set up for cloud desktop specifically. And so to add in superbase I just added in this line right here or I have the command to my Python executable specifically in the virtual

**[0:22:34]** environment that I created. And again these details aren't super important for this video. I'll do a follow-up one for making a server. Then we have the arguments which just points to the server that Windsurf just created for me. And then for my environment, I'm passing in what I have redacted here

**[0:22:49]** but I'm passing in my URL and service key from Superbase. And so with all of that there, you just have to restart Cloud Desktop. And then if you open up your MCP tools that are available, let me scroll down to the first Superbase one. Yeah, here we go. So create table

**[0:23:03]** records. So we have this and then there's the three other tools that we have, which I'd be able to find if I just scroll through the list of tools here. And so now I can ask it something like um what records do I have in my document meta data table? This is a

**[0:23:18]** table from a different video on my channel with some rag stuff in N8N. And so it's now going to call the superbase tool. I'll allow for this chat. Okay, I just did one prompt. I did not do anything for follow-up prompting yet. And look at this. We just one-shotted a

**[0:23:35]** Superbase MCP server with Windsurf with this strategy. And this would not be possible if it wasn't for the rules that I have and having it search through documentation, giving it an example. All of that together is what made this possible. And I'm I'm actually blown away. It this was a big implementation

**[0:23:53]** for it to oneot. And it did that successfully. These are indeed the records that I have in this documents metadata table in Superbase, which is super cool. Okay, so now at this point we have a good state of our MCP server that we want to save with git. so we can

**[0:24:07]** revert back to it if we encounter any issues down the line where the AI IDE breaks things as we're adding a readme maybe tweaking the functionality of our server or adding our tests. And so I'll go into a new conversation here and I'll tell it to uh make a git repo for this

**[0:24:24]** project and make a commit. And so you can either use the git mcp server or you can just use a lot of these AI idees have native commands that support working with git repositories. And so for example in this case it tried to use a tool and failed for some reason. So

**[0:24:41]** now it's just using the git status here in the terminal and that works as well. So you can use either. And so yep it looks like there is a git repo that's initialized. I was trying to run this earlier. I ran it once before which is why it already made the git repo. So now

**[0:24:53]** it's making the git ignore which looks good. We definitely want to have that. And now it's doing the get add command. Looks good. And again, you could use the git mcp server for this as well. Um, but I'm just using the commands. So I run the status. And then now finally, it's

**[0:25:07]** going to make a commit. And so there we go. Boom. We make a commit. And now everything that we have is saved. And so we can ask it later to revert back to this commit if it messes up anything. And we want to just go to this current

**[0:25:20]** state. And so with that done, now we can move on to the next step where we want to create tests and do some things that it missed out on like creating the readme as well. And that brings us back to our main document because we're going to knock out steps number six and seven

**[0:25:34]** at the same time. Step number six goes through what it looks like to iterate on our project after the initial prompt. And the important thing that it covers here is that golden rule to only ask for one change at a time. I've got a good example of that and a very bad example.

**[0:25:52]** The important thing is to not overwhelm the LLM with your requests. And so in our case, we know there are a couple of things that we want to implement right away. We want to create that readme, the project documentation, because it didn't do that at first for some reason. But

**[0:26:05]** then the other thing that we want to knock out right away, this just brings us right to section number seven is we want to create tests for that initial version of our Superbase MCP server. And so we'll just ask the LLM to create unit tests for each of the tools that it made

**[0:26:20]** in the server. And I outlined best practices here for testing. These are the things that we want to give to the LLM, which you can just do in the global rules. And so in this template that I gave for you for the global rules everything that we saw in that section

**[0:26:34]** for best practices for testing, I just list out right here for the LLM. So you don't even have to understand exactly what mocking is, for example. You can still give that as a rule to the LLM because we want to have a dedicated directory for our tests. We want to mock

**[0:26:48]** calls to our database and LLM so we're not using it for real because we want our tests to be fast and free. And then we also want to test a successful scenario, make sure we're handling errors properly in a test. And then a edge case as well. And so we just

**[0:27:01]** include all of that as global rules. And so back over in windsurf now I can just have a new conversation up and I can ask it to create tests for server.py in and then I can just call out the test directory that I already have right here. Um it looks like there's way too

**[0:27:19]** many directories here. So I'm just going to delete that at and say in the tests and so boom there we go. And I could be way more explicit here and it's probably helpful to provide some more instructions, but remember because of the global rules, it's going to follow

**[0:27:33]** those best practices without me doing anything in the prompt related to it. And so I can be very simple here. And so yeah, what I'm going to do is pause and come back once it is done creating those initial tests for me. All right windsurf created all of the tests for

**[0:27:48]** our server. And there was an issue initially where 12 of the tests were passing and then two were unsuccessful. So I went through a little bit of an iteration there just with a couple of follow-up prompts. But after that it is working beautifully. So now in my terminal I can just run the command pi

**[0:28:05]** test and then I just reference my test folder right here from the root directory. And look at this 14 tests and they all pass. and it's 14 because we're testing a successful failure and edge case scenario for each of our different tools. And then I guess a couple of

**[0:28:22]** extras as well to do things like test the lifespan with the environment variables. And this is super comprehensive. Like this file is massive, almost 500 lines of code. And that's generally what your testing files are going to look like. Sometimes they're longer than the base file itself just because you want to hit on all

**[0:28:40]** those different scenarios. And so yeah these are really solid tests and everything is mocked. This is beautiful. And so now at this point, we have our first version of the Superbase MCP server. It's working. We tested it in cloud desktop. We've got unit tests. Everything is good. Now we can move on

**[0:28:56]** to iterating things as we want. We can also create a readme file. All the while making sure that we are keeping our tasks and planning markdown files up to date because again that's that all important context that we need especially if we are starting new conversations. Then there are a lot of

**[0:29:13]** other things that we'll want to do to iterate on our superbase MCP server. I'll just do that off camera though because at this point I've already demonstrated this entire workflow. The very last step that we have here is deploying our project. Because once you're at a state with what you're

**[0:29:28]** building where you want to deploy it package it up to ship it to the cloud share with other people, you can do that with the AI coding assistant as well. And my favorite way to do it is through Docker or another similar service like Podman. And the best part is LLM are

**[0:29:42]** very good at working with Docker just because it's been around for so long. There's so many examples of it on the internet that's been used to train the LLMs. And so they can help you create a docker file to package up and deploy your application even including giving

**[0:29:57]** you the commands to use as well. And so like this is an example prompt that I have here. Just write a docker file for this MCP server using the requirements.ext file for all of the Python requirements. Give me the commands to build the container after. And so I did that already. I didn't want

**[0:30:12]** to bore you with the details of waiting for this to complete. So I created this docker file to package up the MCP server. And then I also had it create the readme in a separate command because remember one thing at a time. I had it create this readme as well. So we have

**[0:30:26]** full instructions for running everything. So installing it from git which by the way you can follow this. You can go through these instructions yourself to have this superbase MCP server running yourself which is really cool. So we built out a full working example in this video and then you build

**[0:30:43]** the container and then you can set up the configuration within your cloud desktop or your winds surf your cursor whatever just using this as the config example and that's it like that's all it takes to get started. So we have this deployed now you can literally clone this repo and do it all yourself and

**[0:31:00]** that is our full process. We literally went from start to finish with this document. Ideation to implementation to testing to writing out our documentation all the way to deploying. We took care of it all. And so that was a lot. Honestly, this video took a very very long time to prep and record everything

**[0:31:20]** for you. So I hope that this process was super helpful for you. And yeah, there might be certain parts to it that I would dive into in more details in another video. Also, I really do want to make a full video on building a MCP server from scratch and going into a lot

**[0:31:35]** more detail on that. So, let me know in the comments if you'd be interested in that as well. So, I hope that this video can help you be way more efficient when coding with AI. And please let me know in the comments what your process looks like, too. I'm super curious. I'm sure

**[0:31:47]** there's things that you would want to add to what I'm doing, or you just have other things that work really well for you. So, I'd love to hear it. There definitely isn't a one-sizefits-all approach for using these powerful tools. I just wanted to share what works well for me. So, if you appreciated this

**[0:32:01]** video and you're looking forward to more things AI coding and AI agents, I would really appreciate a like and a subscribe. And with that, I'll see you in the next
