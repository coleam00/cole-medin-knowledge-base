---
type: raw-transcript
title: "AI Agents: The Future of AI or a Passing Fad?"
youtube_id: gp452XlJSb4
url: https://www.youtube.com/watch?v=gp452XlJSb4
slug: ai-agents-the-future-of-ai-or-a-passing-fad
published: 2024-07-24
duration: "0:11:42"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** agents is a huge buzzword in the AI space right now but is it all hype honestly for a lot of people it is because they get excited about agents without truly understanding what they are or how they are useful but for those of you who really understand the what

**[0:00:17]** and the how of AI agents you know that they are more than just hype large language models are incredibly powerful but they have a lot of problems many of which can be solved using agents and so today I'm going to go through thep top five problems with large language models

**[0:00:32]** and how AI agents can be used to solve those problems to create truly powerful Ai and I'm going to be using real world applications of things I've developed so you guys know that this isn't just Theory this is the real stuff that you can apply literally today first I'm

**[0:00:47]** going to give you guys the simplest explanation of AI agents possible AI agents are large language models like Claud GPT or llama that have been given the ability to interact with external service or each other and maintain persistent state to accomplish infinitely more than just an isolated chat bot so AI that is able to book a

**[0:01:09]** meeting on my calendar remember something I said a month ago or verify its answer with another AI model is an agent in a general sense just to give a couple of examples there and the best way to understand why AI agents are so powerful and how they can be useful is

**[0:01:25]** to look at the biggest problems with large language models that agents can solve so with that let's dive into the top five problems with AI and how agents can help all right I've created some really Nifty diagrams here to demonstrate everything that about to show I hope they can really bring these

**[0:01:40]** examples to life to show you guys how truly powerful AI agents are and how they help with all these problems that we see with llms so the first big problem with large language models is they are very very isolated the way that a base large language model works is you

**[0:01:55]** send in a message and you get a response only based on the knowledge that was used to train the llm that is it and that is not enough for most real world applications more than just a very basic chatbot you need to enhance the AI with external knowledge and allow it to go

**[0:02:12]** out into the real world and actually do things and so an example of a really powerful AI agent application I've developed is this lead nurturing application I created for an agency and so a lead will send in a text message to us and a large language model will

**[0:02:26]** generate a response but because it is an AI agent it can use use rag to get FAQs from a database or it can use the calendar to check availability or book a meeting and if it takes any of these actions it'll regenerate its response based on the result of fetching FAQs or

**[0:02:42]** booking a meeting to send that final text message to the lead all this is possible with AI agents being able to interact with the database and the go highle calendar that makes it an agent if it was just a large language model it would be these two parts of the diagram

**[0:02:58]** and that's it lead sends a text gets a response and it can't do anything else it wouldn't be very useful another thing that sucks with llms is a lot of times they will actually hallucinate so even if they don't have access to these tools they'll say they will so it'll send a

**[0:03:13]** text message back to the lead saying yeah I booked that meeting for you even though it didn't actually do that and so AI agents are powerful not just for giving AI the ability to interact with external services but also to avoid hallucinations so that is problem number one with AI and how agents can help so

**[0:03:29]** let's move over to problem number two and see how AI agents can help with that so what we got right here is an AI personal assistant to demonstrate the example of prompt bloat this is the second issue with large language models even if their context length allows for

**[0:03:45]** a prompt of a certain length it doesn't mean that it's going to perform well with it because the bigger your prompt the more likely you are to experience the needle in the Hast stack problem where the piece of the prompt that you need the AI to pay attention to to give

**[0:03:59]** a good response is so lost in a massive prompt that it misses it and it gives a bad response so in this case we have an AI agent that's able to interact with all these services but all these tools are going to make the prompt huge and so

**[0:04:12]** when a user requests something that would need to create a task in a sauna or use the stripe API to fetch an expense it won't necessarily do that it might miss out on that tool because the prompt is so big and so it's just going to give a confused response and you

**[0:04:26]** could have an example like this that isn't an agent in any way where Maybe there's different types of outputs that you needed to produce based on a response so that would make a big prompt where it isn't even an AI agent I just use this because this is a really solid

**[0:04:39]** example that goes into the solution we have here and the solution is to use many agents that are tied together through a router and so the user will send a message here to the first AI agent which is just a router it'll take the request from the user and say oh can

**[0:04:54]** I generate a response right away as in no tool use needed or if I do do I need to go to a sauna or do I need to go to Google drive or do I have to go to the vector database or Gmail it'll figure out which one the request is related to

**[0:05:08]** and then forward that request to that specific agent so it's like oh yeah this is something related to tasks then it'll go to the assana agent and the assana agent will have all the tools specific to Assa to handle that request and so that way you are delegating and so the

**[0:05:24]** all the prompts are much much smaller because they're all split up and you just use the router to figure out which one of the prompts to go to essentially and so this gives a much better response because you get rid of the issue of prompt bloat which confuses the AI to

**[0:05:39]** absolutely no end it is a huge problem I've encountered many many times so with that let's move on to the third problem which is the very very notorious issue of large language model hallucinations llms they love to make up information or to my point earlier say they interacted

**[0:05:56]** with an external service when they didn't actually do so like booking a meeting or sending an email now there are a lot of ways to help with this problem but the best way that I found is to implement a system using AI agents for self-reflection and so this is a very

**[0:06:12]** basic example you can get quite complicated with this but a user will send a message to the first model which will generate a response but instead of sending it right back to the user it sends it to a second model with a separate prompt for AI evaluation so you

**[0:06:26]** define the rules here of what makes the response good or bad but in a general sense it'll check for hallucinations malformed output output that doesn't follow specific rules that you have in the first prompt and as in the example I gave earlier it'll check for Tool calls that shouldn't or should have happened

**[0:06:44]** so it'll use all this to evaluate and basically just output yes or no is this response good if it is it'll send it back to the user if it's not it'll go back to the first model to regenerate the response probably providing feedback as well so it knows why its first

**[0:06:58]** response was bad and So within this Loop here you'll also probably want to implement logic so it doesn't Loop forever but that isn't very hard to do and so this is really powerful because you're giving a large language model the ability to self-reflect because one huge problem with llms is they can't reason

**[0:07:14]** about their own output which is actually a very interesting problem something I can make a whole video on but think about it this way AI can't think I need to say this thing in sentence one because I'm planning on saying this thing in sentence two I'm being a little

**[0:07:28]** vague here on purpose because because this problem is a huge overarching problem for llms and self-reflection is a good way to help with that so let's move on to problem number four and that is the issue of AI cost and agents can help out a lot with this take this very

**[0:07:44]** simple example let's say you're building an AI application that uses just one large language model 95% of the time you have very basic requests from the user but 5% of the time it's more complicated and you need a more powerful model well 95% of the time you could be using a

**[0:08:00]** cheaper model to handle these requests just fine but because you're only using one model you have to use the more expensive one that can handle those 5% of requests as well but with agents you don't have to do that take a look at this diagram right here we have a router

**[0:08:16]** an AI personal assistant router that uses rules that you establish to determine the complexity of the user request if it's something that's more complicated then you go to the more expensive model like gbt 40 in my example here but if they're request is not complicated if it can be handled by

**[0:08:32]** a simpler model you can spend less money by going and routing that to the cheaper model like llama 3 in this example both are going to give a good response to the AI because you're handling the more complicated ones here but then that 95% of the time you're just using llama 3 to

**[0:08:48]** handle these requests and so you're saving dollars upon dollars but your output is just as good and so you do all this through the router here and so you have to be very good at making the prompt solid for it to to be able to determine the complexity of every

**[0:09:02]** response here but it's not that difficult and it saves you a lot of money let's move on to the last issue for now with large language models and that is the issue of State persistence so large language models by default they have chat history and that's pretty good

**[0:09:17]** but the longer chat history gets the more likely it is to incorrectly reference or forget something very early in the chat history on top of that a lot of times you need to store things that are created in the chat in a very specific way to reference it both for

**[0:09:32]** the user and for the AI later on and you can't just go off of the chat history for that and so a really cool example I have for this here is a workout generator application I created for personal trainers to make weeks worth of workouts for their clients my wife is

**[0:09:47]** actually personal trainer so I made this to help her out a ton and So within a front end here a personal trainer will request a new week worth of workouts for a client like four workouts in the week or something like that the large language model will at the first workout

**[0:10:01]** for the week and then it'll update persistent state in a database with that first workout then it'll accept feedback from the trainer revise the workout based on that feedback update the state and then repeat this process for every single workout for the week obviously chat history could be used here but the

**[0:10:21]** AI would not perform nearly as well so agents help a lot out here because what we're going to do here is within the state manage the workouts as it's being created for the a week and give that as a fresh piece to each prompt for the AI so it doesn't have to go through the

**[0:10:35]** chat history to remember what it did for every single workout on top of that it's easier to display the information to the UI because you have the workouts in a specific format in the database and you don't have to somehow fetch it through the chat history and so there's so many

**[0:10:50]** examples of how this is useful but it's yeah it's just so good to have persistent State and not just have it be something that you try to maintain in the chat history and this kind of goes into the topic of rag as well for really long-term memory and that's something

**[0:11:03]** that I'll be making more videos on in this channel as well so that is the final issue that I'll go over for large language models for now if you aren't convinced that AI agents are the way of the future at this point I don't know what to tell you almost any real world

**[0:11:15]** application that uses AI is only useful if it leverages agents and all the examples that I gave today are real world things that I developed with AI agents to help other businesses so I hope that you found this useful and that you learned a lot of things about AI

**[0:11:29]** agents how they are useful and how they can be used to help solve a lot of issues that we see with llms if you found this useful I would really appreciate a like and a subscribe and with that I will see you in the next video
