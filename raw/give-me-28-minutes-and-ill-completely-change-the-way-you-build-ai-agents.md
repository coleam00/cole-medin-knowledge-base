---
type: raw-transcript
title: "Give Me 28 Minutes and I'll Completely Change the Way You Build AI Agents"
youtube_id: TV8SyEuSMIA
url: https://www.youtube.com/watch?v=TV8SyEuSMIA
slug: give-me-28-minutes-and-ill-completely-change-the-way-you-build-ai-agents
published: 2025-05-11
duration: "0:28:21"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** At its core, building AI agents is rather simple when you just have an LLM that you want to connect to a couple of tools, especially with the help of no code tools like N8N and AI coding assistants. But when you really want to start to tackle more complex problems

**[0:00:15]** and build truly robust AI agents, it becomes a lot less of a walk in the park. And something I get asked all of the time is how do you just look at a problem and know the AI agent to build for that and the different components to build into it? And that is what I want

**[0:00:30]** to share with you right now. I want to dive into my powerful mental model for building agents. Because essentially over the years, I've built a framework for myself for taking any complex problem revolving around AI agents and breaking it down into bite-sized chunks to make it easy to build. Let me show

**[0:00:46]** you what I mean. Clearly, you can see that I have a lot in store for you. I'm holding nothing back sharing my full mental model with you. and we're taking advantage of how visual N8N is to make this very easy to follow along and I've got a lot of very easy to grasp examples

**[0:01:01]** as well. So I want to make this as simple as possible covering the concepts that you can combine together to then make more advanced AI agents. So, the mental model that I'm going to be sharing with you now, I'm calling the seven node blueprint for AI agents. Because any AI agent that you could

**[0:01:16]** possibly dream of making can be broken down into components that are going to fall into one of seven categories. And those seven categories are what I want to focus on here. Because really, any problem in life can be made easier by breaking it down into smaller components. And that is what this

**[0:01:33]** blueprint gives us. It's a guide to do that for building AI agents. And so we'll dive into these seven different nodes. But the first thing that I want to cover with you is the core principle that guides this entire process. The reason I call it nodes, the seven node

**[0:01:48]** blueprint is because of this right here. This is just so important to understand that agents under the hood are really just graphs. Well, that's cool, Cole. But why is that important? What does that even really mean? Well, let me take a couple minutes and explain this to you

**[0:02:03]** because this really is the core of our mental model. And I'll start here with a diagram from the lang chain documentation covering what an AI agent is at a high level. So we have the input from a user. This goes into an LLM that can take actions on our behalf with

**[0:02:17]** tools. And then we produce the final output after the agent is done running. And if you take a look at this diagram closely, you'll see that this is really a graph. We have this cycle here. And this applies to any AI agent you could possibly make where you have this cycle

**[0:02:31]** of the LLM deciding to use a tool getting feedback and reasoning about what happened when it used that tool and then it can invoke more tools. Like this cycle can repeat any number of times just based on the reasoning from the LLM. And this is very different from

**[0:02:46]** traditional automations and workflows where we follow a much more linear and deterministic path. We always have some input that is processed in some way in the exact same way every time and then we have the output at the end. But with agents, we have these cycles of reasoning now with these tool usage and

**[0:03:03]** we can have agents that are working with each other and we don't necessarily know like for one execution. Is one agent going to use this tool or call upon this agent? We have that non-deterministic behavior that is facilitated by the cycles that we have in a graph. And so

**[0:03:18]** that is why agents can be thought of as graphs. And the reason that that is so powerful for us is because when we have these different cycles and these different nodes in a graph, that allows us to reason about how we break the agent into smaller components. And

**[0:03:31]** that's what we're going to dive into in this video is taking a look at more complex AI agents, the different parts that go into it, how we can focus on just subsections of the graph and build those out. And also, you can kind of think of these graphs as just being a

**[0:03:45]** bunch of Lego bricks that are put together. Like you have a guardrail for your agent. We'll get into that. We have your tools. We have your fallbacks. And you can build each of those individually, combine it all together to make a truly robust AI agent. And that is what we're going to be doing together

**[0:03:59]** with our framework. So here's an example of an AI agent that uses all seven nodes in its process. And this is supposed to look a little daunting for you. That's the point that I'm driving home is that we have these more robust agents that might seem hard to digest. We can break

**[0:04:14]** them into smaller components. And so I'm going to be walking you through each of the different components here like long-term memory and our fallbacks and our guardrails, focusing on those individually. Then we'll come back to this example. See how they all combine together to make this more robust AI

**[0:04:30]** agent. And for each of the examples including this one right here, I even built out a diagram so you can really see what's going on under the hood and an even simpler level than the N8N workflow itself. And so what you see here is essentially what we have in this

**[0:04:45]** diagram. And there's a lot of components here, but that's why we're going to focus on each of them one at a time. Now, let's dive into each of the seven nodes. Then I'll show you an example for them all after as well. So the first node that we have is our LLM node. This

**[0:05:00]** is the brain of the agent that has all the reasoning and decision-making. And so when you're interacting with GBT 4.1 or Gemini 2.5 Pro or Claude 3.7 sonnet all these LLMs that you're familiar with, they are all operating within the LLM node of our agentic workflow. And then when they want to take action on

**[0:05:17]** our behalf, that is when they leverage the tool node. So this is our node that performs the web search or the code execution database queries and the decisions made by the LLMs are going to be invoking these tool nodes when they want to perform actions for us. And then

**[0:05:32]** the third type of node is a control node. And these are very powerful because AI agents are pretty unpredictable because we're giving them the reasoning ability to decide what they want to do. And so control nodes add a little bit of deterministic behavior to our Gentic workflows because

**[0:05:48]** instead of using an agent to run the logic here, we're just using regular workflows or code. So we have some more deterministic behavior built into our flow. And so this will handle things like filters, conditions, routing as well. So if we have output from an agent that is going to dictate what path we go

**[0:06:05]** down in a graph, the control node is going to handle that. It's going to route based on what the AI agent outputed, and it's going to do that in a deterministic way. And then we have our memory node. This is both for long-term memory and short-term memory. So we have

**[0:06:19]** vector databases for long-term memory conversation history for short-term memory. Typically what you'll have in your agentic workflows where you want to implement this is you'll have some kind of node at the start and the end to manage the long-term memory for your agent as it is conversing with your

**[0:06:35]** users or yourself. And then we have guardrail nodes and these are crucial to make our AI agents much more reliable. You have both input guardrails and output guardrails. So before you are using an LLM that's connected to a bunch of tools, you might want to validate the user input or validate the output of the

**[0:06:54]** agent against some rules that you have defined. And you can use LLM as these guardrails. You can use deterministic code. We'll get into that more in a little bit, but guardrails are just so important to make sure that we're filtering bad outputs, that we're validating the format of inputs and

**[0:07:07]** outputs. super crucial just to make sure that our AI agents don't run a muck and totally hallucinate something that is going to make the whole agent fail entirely. And then we have fallback nodes. So when something goes wrong with our AI agent, instead of just ignoring the error or crashing the application

**[0:07:25]** most of the time we want to do something specific like have our AI agent retry whatever it was doing or producing some default response for the user letting them know that there was an error and how they could try again. Whatever that might be, we just want to make sure that

**[0:07:39]** we handle errors in our agentic workflows gracefully. And then the last kind of node is the user input node. So a lot of times even in the middle of an agent operating, we want to get some kind of feedback from the user or confirmation that they want to move

**[0:07:54]** forward with whatever tool the agent decided to use. So like before we actually use the agent to book a hotel with Airbnb, maybe we want to send those details to the human and confirm like do you actually want to do this? Like does this look good to you? And so this kind

**[0:08:08]** of interrupt that we have, it's called human in the loop. if it's an interrupt that we have in our agentic workflow waiting for the input from the human before we continue and I'll show you what that looks like as well. So these are all of the seven nodes and we're

**[0:08:20]** going to dive into an example for each of them and then at the end I'll go back to that more complex example combine everything together so you can see very clearly how we can start simple build like with the Lego bricks like I was saying earlier into something that is

**[0:08:34]** more robust. So this first example should look very familiar to you because this graph that we have which represents this NAN workflow looks exactly the same as the diagram that we saw earlier. We have the input that goes into the LLM and tool loop and then we have the

**[0:08:50]** output at the end. And this is the core of building any AI agent. So if you've built any agent in N8N before, this should look very familiar and simple to you. And we're knocking the first three out of the seven nodes down with this single workflow because we have the LLM

**[0:09:05]** we have memory, at least short-term memory in this case, and then we have a single tool that we're giving to our agent. Specifically, this tool allows it to create records in our Air Table table that we have right here where we're just going to list out a bunch of dishes that

**[0:09:19]** we have. And so I can go back to my agent. I can now ask it to make two new dishes. And because we're asking it to make two dishes, it's going to invoke this cycle two times. And so we can see that right here that we used our air

**[0:09:32]** table tool two different times. And now we have two new dishes. For some reason GBT 4.1 Mini just loves spicy mango. Like it repeats this a lot even from my earlier testing too, which is kind of funny. But anyway, we built two new dishes, five and six, and we used that

**[0:09:48]** tool two times to accomplish that. Really, we used each of these nodes two times. So, we definitely had a lot of cycles going on here in this graph managing our tools and memory. So, in the last example, I showed you a memory node with short-term memory, but usually

**[0:10:02]** when I think of memory nodes, it's more for long-term memory. So, I wanted to give you this example here. So, in this graph, before the input goes directly into the LLM, we're actually adding in this memory retrieval step. And in a more robust memory implementation you'll typically have this as a vector

**[0:10:18]** database. you'll pull relevant memories to then feed into the prompt for the LLM. And then we have a step at the end of the graph execution as well to extract relevant memories from our current conversation and store those at the end. And so usually you'll want to implement something like the mem zero

**[0:10:34]** library for long-term memory. And you can see with their add function when you add memories to the vector database, it itself is a graph, which just further proves my point that agents are just graphs under the hood. But anyway, so you'd usually want a more robust implementation like that. For a basic

**[0:10:50]** example here, I'm just using a Google doc to manage all of our long-term memories. And so I can say something like I hate spicy mango. And this is going to then be fed into the LLM. It's going to extract that memory. Like right here, it extracts the memory. User

**[0:11:05]** dislikes spicy mango. We're doing that with an LLM that runs after our primary agent. And then it's going to store that in our Google doc. And so sure enough our Google doc now has the information that the user dislikes spicy mango. And so now I'll refresh the conversation. So

**[0:11:19]** we're not using short-term memory. This is using long-term memory. I'll say "Make me a dish based on what I don't hate." Just some really silly example here. So it's going to pull the memories that we have from our Google doc. It's going to feed that in as a part of the

**[0:11:34]** prompt to the LLM. So right here, we're we're adding in the long-term memory and then it's going to produce the dish for us. Since you don't like spicy mango, here's another dish and it gives us a sweet mango chicken salad. So, it stuck with the mango still, but at least

**[0:11:49]** it's not spicy. That's actually hilarious. But yeah, so you can see that it leveraged the long-term memory there. Typically, we would do something like storing the memories in a vector database instead of just a Google doc. But that just gives us a very visual example here. The sponsor of today's

**[0:12:03]** video is Bright Data and their very impressive MCP server. This is your universal solution to give your AI agents unblockable real-time access to the web. And this is much more than just web search. This is giving your agents the ability to use the internet any way a human could. They have a whole suite

**[0:12:22]** of services to make sure that you can handle any kind of web page, solve captures automatically, handle complex JavaScript, not get blocked from sites. They have it all. And they even have specific web scrapers that are built for you to use out of the box for pretty much any platform you could dream of.

**[0:12:38]** And the star of the show that I want to show you here is their MCP server. You can take all of their scrapers and proxies and other services and bring them right into your AI agents. So in my case, I'm using Pantic AI, my favorite agent framework to connect my agent in

**[0:12:52]** just a few lines of code to the Bright Data MCP server. So, with this script in total, less than 100 lines of code, I now have an AI agent that can use the internet in pretty much any way imaginable. And so, for example, I can have it get me the BIOS for Amazon and

**[0:13:06]** OpenAI from LinkedIn. And it'll intelligently use the LinkedIn specific scraper as one of the tools that the Bright Data MCP server gives me. And take a look at that. Here are the BIOS for Amazon OpenAI. I can confirm, I checked this off camera, this is indeed the correct BIOS. This is looking so

**[0:13:23]** good. It's lightning fast. And I can even ask it something else like, "Give me the flights from Minneapolis to San Francisco today." And it'll figure out the best flights for me and recommend them here. Take a look at that. All right. Gave me four options. This is looking so good. And it's just amazing

**[0:13:36]** how it can intelligently pick the right tool to use so that basically no matter what I want to get on the internet. Bright Data is able to do that for me. I just love it. And so I'll have a link below to Bright Data and their MCP server, they've got free credits to get

**[0:13:49]** you started. So definitely dive in, get this kind of capability into your own AI agents. It's just so powerful. So, next up, we have both the user input and control nodes. And these two different types of nodes often go in tandem together, which is why I wanted to give

**[0:14:03]** you this example. They definitely don't have to be used together all of the time, though. But what we're doing in this case is we are adding in human in the loop. And so, our agent has this tool to send a Slack message. But before we actually follow through and send that

**[0:14:15]** message, we're going to get the human approval. And so, we'll see this in a little bit. But when we get that approval request, that comes into our DM here in Slack. And then when we approve the message, it'll send it here in this research channel saying here is the

**[0:14:28]** approved message. And then just for demonstration purposes, if we deny the message, like we don't approve it, it'll still send it within Slack, but it'll just say that this was the uh disapproved message. So going back to the workflow here, the way that this goes is that we have the human in a loop

**[0:14:44]** that's then connected to our control node. So this is that deterministic routing logic. Like I mentioned earlier control nodes are great for routing because we want the same thing to happen every single time we approve the message or deny the message. So that's what we're doing here. We don't have this

**[0:14:59]** agent reasoning about what to do based on the approval. This is the same deterministic code that'll run every single time. And so let's go ahead and do something. I'll say make a new dish and send it in Slack. And so it's going to now leverage this subworkflow tool.

**[0:15:15]** But we'll see in a second that this will turn purple because now it is waiting for our approval. This is our signal in N8N that it's waiting for us to do something before it continues with the rest of this workflow. So I'll go on Slack, go into my private DMs, and there

**[0:15:28]** we go. It is introducing a new dish citrus infused grilled chicken with mango avocado. So it still has mango in the recipe. I love it. All right, so I'm going to go ahead and approve this here. We get this popup from N8N letting us know that the workflow completed. We can

**[0:15:43]** see this here. Everything is green now in N8N. And then if I go back into the research channel, here we go. Here is the approved message. And we got our new dish. Looking good. And so in this case the control node went down this top path in our graph. Sending that message

**[0:15:57]** saying that it was approved. And then I can just restart the conversation. Send the same message here. We can see what happens when we go down the bottom path. And so it'll ask for our approval again. This time it made spicy mango again. I don't know why it keeps doing that.

**[0:16:12]** There's literally no conversation history. It doesn't know that it did that a bunch already. So I have no idea why it keeps coming up with this over and over again. But this time I'll say no. You already did that. I'm going to decline now. Okay. So action recorded

**[0:16:23]** and then into the research channel. Here is the declined message because I don't want spicy mango for the 100th time. I have no idea why 4.1 Mini keeps doing that. But yeah, there we go. We have human in the loop with control nodes together making this all possible for us

**[0:16:38]** to approve things that can oftenimes be high risk. Like if you have your agent book a hotel or send an email to your boss, a lot of times it could hallucinate in a way where you'd want to disapprove and have it retry, whatever that might be. We just want to add

**[0:16:51]** ourselves into the mix to make sure that we have some say in what the agent is doing. Now we have the allimportant guardrail nodes. And this is how you can make your agents more reliable by validating the inputs and outputs to your agentic workflow. So we have both

**[0:17:05]** input guard rails and output guardrails. And so this graph is a little bit different than what we actually implemented here because I just have an output guardrail to make this simple. But I wanted to show both and I'll give you an example of both really quickly and then we'll dive into this example.

**[0:17:18]** So for an input guardrail, let's say that you're building a travel planning assistant. You give the agent your budget, where you want to go, for how long, and it'll plan an itinerary for you. As a good input guardrail, you might want to have an LLM that will quickly evaluate if the budget is

**[0:17:33]** actually reasonable for the trip. And then if it's not, you would have some kind of fallback where you tell the user like, "Hey, your budget is not reasonable. You need to adjust that before you actually interact with the travel planning assistant." That'd be a really good input guard rail because if

**[0:17:47]** you have the agent try to create an itinerary and the budget is just ridiculously low, then it's going to hallucinate a lot. Like this kind of input guard rail just prevents that from ever even potentially happening with our travel planning assistant. And then as a good output guardrail, you want to maybe

**[0:18:02]** make sure that the itinerary that the agent produced actually is the amount of days that the user said they want to go on their trip for. So just be a really simple thing just analyzing the output making sure that the days match and then if it doesn't you would have some kind

**[0:18:15]** of fallback. Otherwise you would just then output the final itinerary to the user. So good examples there of input and output guardrails. What we're doing in our case is we're going back to the whole generating dishes here. We have this agent that will make a dish based on our request. And then we're going to

**[0:18:30]** feed that into this output guardrail. This is a critic node to make sure that we're actually giving the necessary information for our dish like including the name and the description. Also the origin of the dish. This agent, this critic is going to output true or false. Did this agent do a good job at giving

**[0:18:49]** us a dish? And if it did do a good job then we're just going to output that to the user. But if it didn't, then we're going to retry. So we're going down this bottom path in the graph. We're going back to our original agent regenerating the dish, but also with the feedback

**[0:19:04]** from our critic node given so it knows how to make a better dish this time. And typically what you would do with these kind of guardrail flows where you want to retry the process is you would actually have this loop go all the way back around to the original agent. But

**[0:19:19]** then you have to handle things making sure you don't have infinite loops and stuff. And so I have it set up in this way just to keep it really simple here. But just know that this would be more of a cycle in the graph typically where you'd have the self-evaluation or

**[0:19:31]** critique whatever go back to the original agent when you wanted to retry. But anyway, that is our guardrail. And so now what I can say is let me start a new conversation. I'll just say make me a dish that isn't spicy mango. We'll cover this in the full example later

**[0:19:45]** making sure we don't repeat the same recipe. But in this case we created a dish. How about a classic chicken Alfredo? But we didn't give enough obviously because the critic note here said valid is false. And then it said the feedback is the response does not include the origin of the dish. And so

**[0:20:02]** that's one of the things that we had this output guardrail check making sure that we have an origin. And so now that goes back to our primary agent where this time it's going to give us a dish and then tell us the origin as well. Take a look at that. All right. So we

**[0:20:16]** got better output this time. Obviously this is a very silly example, but you can think about how your output, you want specific things included like the origin of the dish, and this is your way just to make sure that you can evaluate the output to ensure that and then retry

**[0:20:31]** if that isn't the case. So, guardrails are super important, just reducing hallucinations, making sure the output matches what you actually need. So, the last kind of node that we have to cover here is our fallback nodes, and these are super important to make sure that we're handling errors in our agentic

**[0:20:46]** workflows gracefully. We don't want to just crash our application or ignore the errors entirely. And that's what fallback nodes are all about. And so this is going to look very similar to our control node example from earlier because usually you use control nodes with fallback nodes. And so we have our

**[0:21:01]** example where we wait for approval to send a Slack message. If we approve the message, then we will go ahead and send that. But now if we deny it, we're just going to throw an error in the workflow. And you can do something very similar in Python code or whatever as well. within

**[0:21:14]** N8N, we handle that with our error trigger. So this is the process that we're going to run anytime there's any kind of error in our AENTIC application. And so the powerful thing with fallbacks is we can throw this error in any part of our Aentic workflow, like not just

**[0:21:28]** here. And then we're going to handle those errors all in the same consistent way. In this case, just sending a message alerting that there's an error. This could be an email. It could be some default user response that you give back letting them know that they need to

**[0:21:40]** retry. whatever that might be, you can handle that in this part of our fallback workflow. And so in this graph, we can see what this looks like. We have our typical LLM into a loop. This goes to a control node where we're either going to take some action and then give the

**[0:21:54]** output or we're going to hit some kind of error and then go through this fallback process. And so in this case, I don't have an agent here because I just want to keep it really simple. But I'm going to test this workflow. It's going to then ask me for approval. Please

**[0:22:06]** approve or decline this message. I'm going to approve it this time. and we'll see it go down this path uh of not an error like we just sent the message here. But then if I test the workflow again and this time I decline it. Then we'll see it go down the path of the

**[0:22:21]** error. And if I go to my execution history, I can take a look at this. It executed the error workflow. So I got to zoom all the way in. Go back here. Now it executed the error trigger here. You can see that the error is an error has

**[0:22:34]** occurred because that's the message that I sent in here. And that is what I'm going to send in this slack message. So now in Slack, I'm just going to message myself. So I say right here, an error has occurred. So instead of sending it in the research channel, I'm just

**[0:22:48]** alerting myself internally that there is an issue with this agentic workflow. That is what we are able to do with fallback nodes. Super powerful. Now here is the big payoff. We can go back to our full example. Now that we covered each of the different nodes, we can see how

**[0:23:02]** they combine together to build something more complex like this agentic workflow. So even though there's a lot going on here, we can break it down step by step to make it very very simple. And so let me do that for you. I'll go through each part of this process and I'll even point

**[0:23:16]** out which node is being used in each part. And so right off the bat, we are fetching our long-term memory at the start just like we did in our other long-term memory example. Then that is fed into this primary agent. And this is going to again generate a dish for us.

**[0:23:30]** But this time it has a tool to look at what we already have in the menu to make sure it doesn't generate a dish that is already here, which is good because we don't want to generate that stupid spicy mango chicken thing for the 100th time. And so we have our LLM, our tool nodes

**[0:23:46]** our memory nodes that we have for long-term and short-term memory. And then we also have this guardrail here. So we're using what's called an output parser to make sure that the format that this LLM outputs always has a dish name and a dish description. And the reason this is a guardrail is because we have

**[0:24:02]** this autofixing output parser. So if the agent doesn't produce the exact format that's needed, it's going to retry using the secondary LLM to aid in that. And by the way, if we were to give this guardrail LLM some tools, this would be another agent. And that's how you

**[0:24:17]** implement multi- aent workflows as well. You just have to have bunch of these agents strung together, or you can use agents as tools, like sub agents. And so I know I didn't talk too much about multi-agent workflows in general with this, but if you just have a lot of LLM

**[0:24:30]** nodes brought together, each with different tools, that's how you build multi- aent workflows. But anyway, just a quick tangent there. So that's our guardrail. Then after we create that dish and we have the name and the description that's guaranteed by our guardrail, then we can send the message

**[0:24:45]** in Slack getting that approval. And then we have this control node that's either going to hit that same error workflow that's going to tell us internally that there's an error with our agentic flow or we're going to send that dish in Slack and then we're going to add that

**[0:24:59]** dish to air table as well. So because this is not an agent performing this action, this is yet another control node just inserting that meal here in our air table base. And then we're going to go to the next long-term memory node. just using another LLM to extract these key

**[0:25:13]** memories. Like maybe we gave some preference along with our request to create a meal. Like we might have said something like we like dessert with our meal or we like dishes that combine sweet and savory. So that's what we have in our long-term memories. This will keep adding on to that and we'll call

**[0:25:28]** this node to save the memories as well. And then we just have an LLM chain at the end here that is going to summarize everything and give us back that final dish. And so going back to the start we've got LLMs, we got our memory nodes we've got our tools, we have our

**[0:25:42]** guardrail here, we have human in the loop. So we've got that user input, we have these control nodes here to manage the deterministic code, we have our fallback, and then we have long-term memory to wrap it up as well. So all of these seven types of nodes we have

**[0:25:57]** implemented in this flow. And so the reason that this is powerful for us to understand these different components is we can reason about what we want to add into this by just thinking like does this agent need long-term memory? What kind of guard rails do I want to

**[0:26:10]** implement here for input or output guardrails? What I want what do I want to do when there's an error in my flow? What kind of fallback do I want to have? We can ask ourselves these questions one at a time, breaking down this more complex process into something that

**[0:26:23]** starts to feel a lot simpler when we think about it this way. That's the power. like it wasn't that hard for me to build this full flow when I just thought about each of the seven nos and what I want to implement here. So now we can just test this out. I'll open up the

**[0:26:35]** chat again and I'll say make me a dish that isn't already on the menu. So just making sure that it uses this tool to check the menu so it can generate a brand new dish for me. So it's going to do that. It also pull my long-term memory so it knows that I like desserts

**[0:26:50]** with my meal. I like things that are sweet and savory. So I'll go over to Slack now. See what I need to approve. coconut lime shrimp with sweet chili couscous. That actually sounds really really good. Like my stomach is gurgling right now. So, I'm going to go ahead and

**[0:27:03]** approve that because that definitely sounds good to me. And so, now going back to the flow, it's going to send that message in Slack. And so, I can see that in my research channel. Here we go. And then I also have it added to my menu here in Air Table. Take a look at that.

**[0:27:16]** And then let's see if there's any memories that were added. I'll go to my memory. Uh let's see. An important detail is that the user wants a dish that is not on the menu. Okay. So yeah now it knows going forward that in general I don't want dishes that are

**[0:27:29]** currently on the menu. So that looks really, really good. Take a look at that. And I know I didn't show the error flow here, but that's just going to look very similar to what we saw before. Just a full example of this flow making a very tasty dish that um I wish I could

**[0:27:42]** go make right now. So there you have it. That is my seven node blueprint, my mental model for building any AI agents breaking things down into bite-sized chunks to make it super easy to build more robust AI agents. And I want to create content on things specific to

**[0:27:57]** like guardrails and fallbacks later as well. So certainly stay tuned for that. And then I'll continue to focus on frameworks like Pantic AI and Langraph that literally focus on agents as graphs. Like that is the abstraction that they have. It's just what makes them so powerful. And so if you

**[0:28:14]** appreciate this video and you're looking forward to more things AI agents, I would really appreciate a like and a subscribe.
