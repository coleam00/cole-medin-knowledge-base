---
type: raw-transcript
title: "Google's Agents CLI: The CLI + Skills Combination to Ship AI Agents EASILY"
youtube_id: 1wfY7GCVvh0
url: https://www.youtube.com/watch?v=1wfY7GCVvh0
slug: googles-agents-cli-the-cli-skills-combination-to-ship-ai-agents-easily
published: 2026-06-10
duration: "0:15:19"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** These days anyone can build an AI agent pretty easily and now even shipping them to production is straightforward. That's what I want to show you in this video. How we can use a combination of a CLI and skills to make it so our AI coding assistant can walk us through creating

**[0:00:15]** an agent from idea all the way to a reliable deployment and we're going to be using Google's agent CLI for this. It is a very powerful tool. It's open source. I'll link to it in the description. It helps us build agents with Google's ADK which is an agent

**[0:00:30]** framework that a lot of people are using. Now I got to say it's been a while since I made a YouTube video of just building an agent. Usually I'm focusing so much on AI coding assistants these days and the biggest reason for that is tools like this make it so easy

**[0:00:45]** to build agents. There's not as much substance for me to cover in videos. Now it's not always trivial. You can still have complex memory systems and rag architectures. I'm not trying to say that every agent is a walk in the park now but with tools like the agent CLI

**[0:00:59]** like I'll show you here it is significantly easier to build AI agents now even compared to 6 months ago. Okay, so go down memory lane with me for just a couple of minutes here then we'll do a live build with the agent CLI. I'll show you how easy it is. So when I started my

**[0:01:14]** YouTube channel a couple of years ago my videos look like this. We were in VS code and I was showing you line by line how to build AI agents with LangChain as the framework at the time. Like let's define our model. Here's how we bring in our system prompt. Here's how we add

**[0:01:29]** tools to our agent. It was a good time but man did it take a while to build any individual agent and so no AI coding assistants at the time. And then once we started using AI coding assistants like a year or two ago we were still living and breathing in the documentation. Like

**[0:01:46]** these are the docs for Google's ADK. I build a lot of agents with Pydantic AI as well. A lot of frameworks out there but AI coding assistants weren't reliable with any of them. We didn't have the idea of skills to really just like inject all of the context and all

**[0:02:00]** the docs that it needed. And so we would go through the quick start still. We'd pull certain pages and give it as context to our coding agents. There were a lot of bugs that we had to work through ourselves cuz coding agents just weren't at that point yet. It was still

**[0:02:13]** quite a bit of work. And now we've gotten to the point where in 2026, you don't have to spend a single second in the documentation yourself because we basically bring it into our coding agent. It's just single command to install the CLI and skills. And now with natural language, we can ask our coding

**[0:02:30]** agent to build the agent, evaluate it, deploy it, harden it. Everything is packaged together. And so what I'm showing you in the video here is universal, but I'm just showing Google because with the agency CLI, they do it best. The skills that take your agents all the way to production. Okay, so back

**[0:02:47]** to the repo. If we scroll down in the read me here, we can see the commands to get an idea for how the agency CLI works. And the coding agent is going to drive all of this, by the way. More on that in a second. So we have commands to

**[0:02:59]** scaffold the project, evaluate the agent. We can run a single prompt against the agent. We can even optimize the prompts based on our eval data. So there's self-iteration built into this as well. And we're not going to run any of these commands ourselves. We're going to let our coding agent do all of it. So

**[0:03:17]** you can think of the CLI as the capabilities that we're giving the coding agent. It can just run all of these commands. And then the skills that ship with it tell the coding agent how to use the CLI. That's what makes the combination so powerful. The CLI is the

**[0:03:32]** capability, the skills are the instructions. And so for example, one of the skills that ships with Google's agency CLI is the instructions for how we actually write the code for the AI agent. This is where we really have all of the documentation, like the Google ADK documentation, baked into our coding

**[0:03:49]** agent through this skill. That's why we never have to go to the documentation or even reference it for our coding agent. It's super cool. So, going back to the list of skills, every stage of building an agent that we have CLI capabilities for, we have a skill to go along with

**[0:04:07]** it. So, your coding agent knows how to drive the entire process end to end, only following your instructions and your spec. And so, this is what I love about Google's Agent CLI. There are a lot of frameworks out there that have skills to help you build agents, but

**[0:04:22]** they don't take it as far as going to your deployment and even production observability, for example. This is why I love the Agent CLI. And so, I am working with Google to bring this video to you. It's an honor to even say that, but this is legitimately what I'm

**[0:04:36]** building with right now, because the ADK with the Agent CLI allows me to go to production so easily. So, let me actually show you that now. Let's build an agent and get it all the way to deployment. So, the way to get started with the Agent CLI, like we saw earlier,

**[0:04:49]** is to run the single command to install the CLI and skills. And then we can get into just asking it to build any AI agent. But, I'm not even going to run this command. I'm going to take it upon myself as a challenge here to build and deploy the entire AI agent without

**[0:05:03]** running a single command in the terminal myself. So, I'm going to go straight into Cloud Code here. I'll use my speech-to-text tool and I'll say, "I want you to search the web so you know how to install the Google Agent CLI, and then I want you to install it

**[0:05:17]** in this project here." All right, cool. So, we'll go ahead and send that off. I'll come back once we have everything good to go. All right, and 30 seconds later, we have the Agent CLI installed with all of the skills as well in my .cloud folder. If this was another coding agent, it would

**[0:05:32]** be somewhere else, but this does work with any AI coding assistant as long as it supports skills. So, now I'll go in a new Cloud Code session. I'll do /skills. You can see that all of them are loaded here to build the agent, deploy it, etc. And then I'm going to copy a prompt that

**[0:05:46]** I have off camera just to save a bit of time here and paste it in. I'm telling it to use the installed ADK skills to build an ask your data agent. So, this is just something simpler for a demonstration here, but the user gives a CSV and a question, and it's going to

**[0:06:00]** write Python code. So, it's going to do code execution to answer our questions over the CSV. And I'm specifically choosing code execution here because this is one of the things that you have to do in isolation. It's actually a bit of a challenge to really make that reliable when you have an agent deployed

**[0:06:16]** to production. And code execution is one of the things that Google takes care of for us when we deploy it to the cloud using the skills here. And so, we can see that it loaded the CLI workflow skill, scaffold, and ADK code. So, it knows how to spin up the code base and

**[0:06:33]** build the agent for us. Now, for the sake of speed, I am just jumping right into the build. I'm doing a little bit of vibe coding here. So, even with these skills, I still would recommend going through your usual planning and implementing process with your AI coding assistant. I cover that all the time on

**[0:06:49]** my channel. You want to work with your coding agent like Claude Code to build a spec for the agent you want to create, and then you would send in that spec for it to start loading these skills and building the agent. But, because we're not also building something super

**[0:07:02]** complicated here, it should be able to one-shot this for us. At least because it can also iterate and build those evals. We'll see that in a little bit as well. So, you can see it even came back to ask me a question here, which ADK code executor should the agent use? And

**[0:07:15]** so, definitely we want to use the built-in sandbox. This is one of the best parts of the ADK is code execution. A lot of agents rely on that now, and in a production environment where you could be executing any kind of arbitrary code, you need to do it in a secure way. So,

**[0:07:31]** all right, let's go ahead and just let this agent rip through the implementation. All right, so while the AI agent builds, there's an elephant in the room that I have to address here. I can't leave this out of the video. So many people ask me about this. They say,

**[0:07:42]** "Hey, Cole, if we have coding agent SDKs now, why should we even use a framework like Google's ADK or Pydantic AI or LangChain, all these more {quote} traditional frameworks?" I know it's kind of silly even calling it traditional, but they are a lot older than these coding agent SDKs, these

**[0:08:01]** really powerful harnesses that give us a ton of capability right out of the gate, the same capabilities used in these AI coding assistants. Cuz you can build some very powerful AI agents on top of things like the Anti-Gravity SDK. But, the thing is, those more traditional frameworks, they're still really

**[0:08:19]** important when you want to ship your agents to production. And so, let me just break it down nice and simple for you. A lot of people are using coding agent SDKs to build their own second brains or agentic workflows that they run themselves. But, the problem with these tools is, yes, they're really

**[0:08:36]** powerful, but that comes at a cost. It's a lot less token efficient to use these SDKs, and you're going to get slower responses. And so, for anything you're running yourself like your second brain, where you care more about the output quality over the speed and the cost, these are fantastic. I've built my own

**[0:08:54]** second brain on top of these coding agent SDKs. But, anything where you're building an agent into a platform, anything going into production, it's almost always more ideal to build with a framework like Google's ADK because it's something a lot more minimalistic, right? You're building an agent from the

**[0:09:11]** ground up, you get to control the prompting and all the tooling. And so, you can make it so it's very token efficient and very fast. There's a lot of research out there that tells us that if there is a customer on a platform and they don't get a response or at least

**[0:09:25]** that first token within 4 seconds from your agent, they're just going to leave or at least there's a super high chance that they're going to leave. So, we need our agents to be fast and lightweight if we really want to scale them in a platform, that's what this video is

**[0:09:39]** really showing you how to do. Using one of these frameworks like the Google ADK, we're using the agency CLI to build an agent that can scale incredibly well. We're going to deploy it in a environment that can immediately be used by even millions of people. All right, and 5, 10 minutes later, we now have our

**[0:09:55]** agent. And I even asked it to tell me what it did with the agency CLI. So we get an overview of the different commands that it ran. It didn't do anything with evaluation or deployment yet. So we'll do that in a second. I'll end the video quickly with that. But we

**[0:10:07]** have the entire agent built and tested now. And so I also had Claude code create a really simple Streamlit UI after I built the agent, just so we have something to see to really test our agent. And so we can either use a deployed agent once we have that or the

**[0:10:21]** one that's just running locally. And so I can upload a sample data set that I had it generate. I know a lot of this is pretty trivial, but I don't want to convolute things with a really complicated example. So just keeping it nice and simple. And so the question

**[0:10:33]** here is what's the median revenue per order and which row is the biggest outlier above the mean? And so it's going to right now create the code, run the code, and then give us the answer in just a second. And there we go. The median revenue per order is a $1,348.65.

**[0:10:51]** And the best part about this UI, and this is what the agent communicates back to us as well, is the exact code that it wrote in order to do this calculation. So it loaded in the data. It was small enough where I guess it just wrote the CSV in line. Obviously it could read

**[0:11:03]** from the file as well. And just using Pandas to get us the answer, printing it out. So very, very cool. That is how we got our answer. So now it's time to take this agent further by evaluating it, refining the prompt, and getting it deployed. So starting with evals, then

**[0:11:17]** we'll get into deploying the agent to end things off, testing that in Streamlit again. So really simply, with natural language, just like building the agent, I'm saying use the ADK skill to evaluate the AI agent we built here. I'm doing this in a new conversation to show we don't even need the context from the

**[0:11:34]** conversation where we built the agent in order for it to understand how to run everything here. So, it loads the eval skill, it understands our existing code base, and then basically it just runs a test set that it created when it built the agent. So, you definitely would want

**[0:11:48]** to expand this if you're really going to production, but right now I just have a three test case set here, and so it ran each of them and we can see that each of them passed. And so, it's really sending a query to the agent per evaluation making sure that the response matches

**[0:12:02]** with the expectation based on the test data that it's sending into the agent. This is awesome. And so, you can also if the evaluation shows the agent isn't working the best, use this as an opportunity to iterate on the system prompt, the tools that you have for the

**[0:12:16]** agent, get it to the point where it's ready for deployment, and now to deploy this agent all we have to say is deploy this agent, right? Like that simple. It's going to load the skill, it's going to go through the full process getting this deployed to the Google Cloud. You

**[0:12:30]** might have to do some kind of authentication and set up a project in Google Cloud, but it'll even walk you through all of that, show you the steps to take, the commands to run if you need to set up things completely from scratch. Obviously, I already have a lot

**[0:12:43]** of this set up in my environment as I was prepping for this video, but yeah, overall it's really straightforward. And there we go, 6 minutes later and our agent is now deployed to production. So, it literally spun up an instance in GCP for us to host our agent. Of course, you

**[0:12:59]** can configure all of this. it should also give you a console playground URL, so you can go right to the web to test our agent that is now running in production. So, we can send messages here. Of course, we have that Streamlit UI that I'll test in in a second. We

**[0:13:14]** have memories, evaluation built into the production environment. We have full auditability with traces. This is big as well. And then also all the code execution that I was talking about earlier, that also runs in sandboxes in our production environment. And then the other really powerful thing here with

**[0:13:29]** our agent is that it has an identity. So you can see that right here. Also, if I go in the service configuration, we can look at the deployment details. And so we can set permissions for our agent, just like you could another user or a service account. We can also track our

**[0:13:43]** traces per agent, per user as they're using our agents. And we have the URLs here to incorporate the agent right into any platform that we have built deployed to production. Very, very cool. So I'm going to go back to Streamlit here. This time I have the deployed agent selected.

**[0:14:00]** I'll upload the sample data set again. And then let me just copy over this question here. So slightly different question this time. Which region grew its total revenue the most from quarter 1 to quarter 2 and by what percentage? Just another basic question to show you that we have the same interface here,

**[0:14:14]** but now this time running through the deployed agent that we have in GCP. Take a look at that. We got our answer, the code that I wrote, everything looking really, really nice. So we took our agent from idea all the way to production in this video without me

**[0:14:30]** running a single command myself. Claude code drove the entire thing. So that's the Google agent CLI in 15 minutes. It is such a powerful tool to take any agent from idea to production. Now, depending on what you're going to build, it might be more complicated than what I

**[0:14:45]** presented here. If it's multi-agent, complex rag system, but this still is going to be the tool that can guide that entire process for you. You might just have to spend more time specking things out with your coding agent. But yeah, I'll link to this in the description. Just try it out. Build an agent and just

**[0:15:01]** see how easy it is these days, even compared to just a year ago. And so if you appreciate this video and you're looking forward to more things on AI agents and AI coding assistants, I would really appreciate a like and a subscribe. And with that, I will see you

**[0:15:15]** in the next video.
