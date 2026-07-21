---
type: raw-transcript
title: "Are You Building REAL AI Agents or Just Using LLMs?"
youtube_id: GYFTQU2iV4A
url: https://www.youtube.com/watch?v=GYFTQU2iV4A
slug: are-you-building-real-ai-agents-or-just-using-llms
published: 2025-02-23
duration: "0:18:29"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** these days everyone is putting an llm into any program and calling it an agent but it is not that simple and I see this all of the time especially with no code tools like n8n here's the thing there is a big difference between actual AI agents and a workflow that just happens

**[0:00:17]** to have an llm inside of it and it's a very important distinction as well because the way that you build agents versus workflows and the place for each is entirely different so you have to know what you are building both are very valid valuable but they each solve an

**[0:00:32]** entirely separate set of problems so let's go ahead and break this down together I'll show you not only what an agent is but also what it isn't and I think that's really going to help it click for you right now plus I've got some visual examples to make things

**[0:00:44]** crystal clear and we'll also cover some agent definitions from hugging face and anthropic when to use an agent versus when a simple workflow is actually better and I'll show you an example of an agent and a not agent in the real world a lot of value packed into today

**[0:00:59]** so let's go ahead and dive right into it all right so here's how this is going to go first we're going to Define together what an AI agent actually is I bet that if you were to ask the average person building AI agents what an agent is they

**[0:01:13]** would not be able to give you a concise definition so that's what we're going to do right now create a concise definition of an agent using the help of hugging face and anthropic and that's going to set the stage for the rest of this video I'll actually show you with n8n some

**[0:01:27]** examples of agents and then some examples of workflows that you might think is an agent but it isn't actually and so starting right here with this blog post by hugging face they have this really nice single sentence definition of what an agent is and I don't think this is enough but it's a good starting

**[0:01:44]** point here AI agents are programs where llm outputs control the workflow and the key word that I apply to this is nondeterministic and what I mean by that is we don't actually know exactly what is going to happen in a workflow when an agent is controlling it it's not as

**[0:02:02]** simple as step a then step B then step C because an agent determines what is executed in a workflow when and how many times and another good definition that hugging face gives in their AI agent course I'll have this on the screen here I think this is so important they say

**[0:02:19]** that AI agents are AI models that are given the ability to interact with the environment to achieve a certain goal and that also speaks to how agents are goal oriented versus with work flows it's kind of just go in a linear path to do a certain Thing versus agents

**[0:02:34]** actually have a goal in mind and they have to reason about how to get there so that's what hugging face gives us and that is definitely a very good start but another definition that I very much appreciate is this one from anthropic and so they put out this video on their

**[0:02:48]** YouTube channel quite recently here tips for building AI agents but they also talk a lot about this distinction between agents and workflows just like we've been talking about for the last couple of minutes here so just go ahead and check out this clip super super good stuff yeah so I think something we

**[0:03:04]** explored in the blog post is that first of all a lot of people have been saying everything as an agent referring to almost anything more than just a single llm call um one of the things we tried to do in the blog post is really kind of separate this out of like hey there's

**[0:03:18]** workflows which is where you have a few llm calls chained together and really what we think an agent is is where you're letting the llm decide sort of how many times to run you're having it continuing to Loop until it's found a resolution and that could be you know

**[0:03:33]** talking to a customer for customer support that could be iterating on code changes but something where like you don't know how many steps it's going to take to complete that's really sort of what we consider an agent yeah that's just so good and also that aligns very much with the definitions that we just

**[0:03:48]** saw from hugging face 2 and if none of this is really clear at this point do not worry because the examples I'm going to showing N I think are really going to drive this definition home this whole idea of non-deterministic agents determining what is executed in a workflow and just the difference from a

**[0:04:04]** sequential workflow overall so leading into the n8n workflows I just want to show a couple of diagrams really quick because I know diagrams help me understand things really really well and if it does for you too I think this will be really valuable because this really outlines the definitions together of

**[0:04:20]** what hugging face and anthropic were talking about because essentially an agent is given abilities like tools to interact with things like Google drive or Slack whatever it might be they're given goals and preferences through the system prompt and then prior knowledge as well through something like short-term memory just with the

**[0:04:38]** conversation history or long-term memory with something like rag so all of that is given into this agent and then it's able to perform actions in the environment to do things on your behalf like draft an email send a message in slack query a database all those kind of

**[0:04:55]** things that tools enable an agent to do and then it's a loop here because we have this step where there's the observations the agent observes what happens when it invokes these tools in the environment like it sees what happened when I queried the database what did I get back what do I need to do

**[0:05:12]** next and it might decide to actually go back and interact with the environment again we don't necessarily know how many times it's going to do that to achieve its goal that's the non-deterministic behavior that I mentioned earlier and then one other diagram that I also think is really valuable it's a little bit

**[0:05:28]** more to it here but it speaks a lot more to the tools part of what makes an AI agent an agent because tools are the functions we give it to do things like explore the web hit some API like the weather API in this example or to perform rag over your knowledge base or

**[0:05:45]** use a calculator whatever those tools are to allow the agent to interact with the environment and so you have the user input on the far left side that goes into the llm that's the brain of everything that's deciding what it needs to do to achieve the goal the user gave

**[0:05:59]** it and this is everything in its tool belt because maybe to get an answer it needs to search the web or it needs to look in the knowledge base and so it'll perform those actions and then the observations will go back to the llm again to potentially invoke the tools

**[0:06:14]** again in that non-deterministic Loop then the final results after it decides that it's performed everything it needs to do to achieve the goal it sends that back to the user so with that in mind I think we have a very clear definition of what an AI agent is and the different

**[0:06:30]** parts to it so now let's go ahead and take a look at some examples of workflows that are not agents so we're starting off right away with my favorite example of a not agent as I like to call it the job of this workflow and people build these kind of workflows all of the

**[0:06:44]** time is to take a prompt from the user for a certain topic and then craft a post specific to X and then post it to X and then do the same thing for LinkedIn and a Blog and then you have some sort of llm at the end that summarizes what

**[0:07:00]** was posted to do each platform and gives a response back to the user this is not an AI agent it is a workflow that is just chaining llm calls together just like we saw in the anthropic video like this is a very clear definition of that and the way that you can tell this is

**[0:07:18]** why I love n8n and by the way if you don't understand n8n or you haven't used it before this is just so visual that I hope that this makes sense for you still but I love NN because it just shows how this is very sequential you create the X

**[0:07:30]** poost and then you post it and then boom you just do the same thing for LinkedIn and the blog there is no nondeterminism here you never would post twice to X or decide not to post to the blog for whatever reason if you actually had those decisions here and an llm was

**[0:07:46]** controlling that then it would be an AI agent but everything is just step a step B step C and then you're done it is not an agent and don't get me wrong this is actually quite a valuable workflow I see people building these all the the time in make and n8n and zapier because it's

**[0:08:03]** really important to use some sort of llm with a very welldefined system prompt to craft the message very specifically to each platform because what you post on X is going to be very different than what you post on link in but it doesn't mean it's an agent and so I can actually do a

**[0:08:19]** little test run here I'll just say AI like write me an xost for U Ai and then a LinkedIn and then a blog post and we'll see this work and like it works really well and this is a good example of where a simple workflow is actually better than an AI agent we could turn

**[0:08:35]** this into an agent where it would have a tool to make an X poost and then a tool to make a LinkedIn post and then we would ask it to do each of those things but we don't actually want that non-determinism because what if the agent for whatever reason completely

**[0:08:49]** hallucinated and decided that it needed to post to X twice or not make the LinkedIn post when we want it to we don't really want to give the agent the option to control the workflow here so it is better that we make it sequential and just make it a regular workflow here

**[0:09:04]** so this is our final response gives us kind of a summary of what it posted to each platform and uh I mean there's a little bit of glitch here but yeah you get the point of this like it demonstrates very clearly that this is like a really solid workflow just not an

**[0:09:16]** AI agent so with that in mind let's go over to another example here I'm going to do a little bit of a a Twist on this one so for this next one I'm starting right here in the n8n chat window and I want you to decide as I'm having the

**[0:09:28]** conversation with this workflow or agent is it a workflow or is it an agent and so what this one does it is a tech stack expert so I describe the application that I want to build and then it walks me through some questions to help me figure out what technologies I should

**[0:09:42]** use for my front end my back end my database all that good stuff so I'm going to kind of fast forward through this as I am talking to it and yeah make the decision for yourself is it a workflow or an agent all right there we go we now went

**[0:10:09]** through this conversation it asked questions about our front end our back end and AI coders that we're using um how many users we have and then after the whole conversation it now recommends everything for the front end uh right here we got the back end authentication taking in my preference database llm

**[0:10:28]** hosting looks pretty neat so now the question I have for you is given the complexity here and how it seems to be able to reason about the things that I want and make judgments around different Technologies do you think that this is an AI agent that's operating in an

**[0:10:43]** environment to achieve the goal helping with my tech stack or is it just a workflow or just a regular llm chatbot so make the determination for yourself now I'm going to go over to the nend workflow and you'll see what it actually is so I'm going to make that switch

**[0:10:58]** right now take a look at this the entire conversation we just went through was driven by a single llm that is not an AI agent and the reason we know it's not an agent look at this the tools part of the agent node is just dangling here there's

**[0:11:14]** nothing given to it for it to interact with the environment so it's just a regular chatbot one of the criterias for the agent is that it can interact with the environment to achieve a certain goal not just act as a normal chatot because the entire conversation that we

**[0:11:30]** just went through was driven only by this fancy system prompt here there was nothing within invoking tools to figure out certain things for our teex stack it was all defined right here now the important thing is this workflow or chatbot unlike the other one is non-deterministic we don't necessarily

**[0:11:48]** know how many steps it's going to take for it to figure out what AI coding assistance we're using because maybe we'll ask get a question and it'll answer it and then re askk what AI coding system we're using before it goes on to ask us about our front front end

**[0:12:00]** or a back end so it is non- deterministic we don't know how many steps this conversation is going to be until it gets to the point where it finally tells us our Tech stack but it's still not an agent because it's not interacting with the environment in any

**[0:12:13]** way so the last example it actually did interact with the environment because it had made a post on X it made a post on LinkedIn it made the blog post but it was sequential and that's what made it not an agent in this case this one is non-deterministic it isn't actually

**[0:12:28]** sequential but it's not an agent because it's not interacting with the environment so both examples show the different criterias for what determines if something is an agent versus just a chatbot like we have in this case or a workflow like we saw in the other case so now it is time to move over to some

**[0:12:45]** other examples in n8n showing you examples that are actually AI agents this is our first example of an agent that is more than just a simple workflow because unlike the last two examples we went through this fits all of the criteria first first of all it has tools

**[0:13:01]** to interact with our environment to achieve goals for the user because this agent manages long-term memories and notes using Google Docs it's actually pretty neat I'll share a link to this in the description this is from the n8n workflow template library that I found very very neat agent and also it is

**[0:13:18]** non-deterministic because sometimes the agent will decide that it doesn't need to save anything to the notes or the long-term memory and other times it will so we don't always know what tools it's going to invoke or how many times it will invoke each one so we can see an

**[0:13:31]** example of this here I'll actually chat with it right now so you can see I'll just start with a basic message at first just saying hi and in this case it is not going to decide to invoke either of the tools here there would be a green circle around them if they were invoked

**[0:13:44]** because it was just a very basic message but now we can ask it something that we know it'll save to the long-term memory I'm going to be very explicit here just to make sure I'll just say uh very important I need to learn how to tie my shoes just something really silly here

**[0:14:00]** but now we'll see that it invoked our save notes tool so now if we were to actually go into our Google doc we would see whatever it decided to save for us to need to learn how to tie our shoes and so now I can actually refresh the

**[0:14:15]** conversation here and so there's nothing with the conversation history that could help it remember this this is entirely from being fetched from the Google Doc right here at the start of the workflow I'll ask it what do I need to do and so it'll fetch from the notes here and then

**[0:14:29]** give the response that um look in the notes I'll have look in the notes and it'll say you need to learn how to tie your shoes all right look at that so it retrieved that from the notes it didn't invoke either of these tools this time because it was just answering a question

**[0:14:44]** for us and so this is very much an agent and this workflow it's very basic overall it's very cool uh it doesn't work 100% of the time like you could see there that I had to tell it to look in the notes but still a very good example

**[0:14:54]** demonstrating something that is an agent because it's non-deterministic and it is answering questions for us as in that is its goal using the environment here with Google Docs so this next example I'm really excited to show you cuz it is a GitHub agent that I built for my AI

**[0:15:10]** agent series on my YouTube channel so given the URL for GitHub repository it can analyze the structure of the repo and then decide to look at individual files obviously being very non-deterministic because it can pick what files to look at and it's interacting with GitHub that is its

**[0:15:26]** environment and so I'll go into the chat here do a little demo here so I'm giving it the repository for archon that is my AI agent Builder that I've started recently that I've been building an iterations and each iteration has a different read me so I can ask it to go

**[0:15:40]** and analyze each one to then describe to me the different versions that we have here so you can see that it decided first to invoke the tool to get the overall structure of the repo and then four different times it decided to analyze each of the readms for the

**[0:15:55]** different versions of archon and then it's giving me a nice and concise description of each version so we have version one version two version three and then I assume the fourth call was just analyzing the read me at the root of the GitHub repo very agentic here we

**[0:16:09]** see that it decided how many times to invoke these tools to use each ones then if I ask a followup question it might decide to invoke none of the tools very agentic in this case so just another good example of an agent in n8n that is non-deterministic and interacts with our

**[0:16:24]** environment so the last example of a not agent that I want to give is one in the real world and that is chat gbt domcom because really it's just a conversational chat bot just like the text stack expert that we saw earlier even when you have web search enabled

**[0:16:40]** really it just searches the web gives that as context to the llm and then it's not like it's an agent that could decide it needs to search the web again to refine its search or whatever it might be so if I ask it a question like what is the net worth of Elon Musk it'll

**[0:16:55]** search the web feed that as context in the llm to give me my final answer but if it found the wrong information it's not like it could decide to search the web again so you could argue that it's an agent because it could decide to search the web or to not search the web

**[0:17:09]** but besides that very basic decision it really is just a normal chatbot and if you compare that to something like winds surf this is very very agentic because if I give it a prompt here like um let's let me delete this little extra bit that I have here update the model I'm using

**[0:17:25]** for my agent so I just built this agent with pantic AI and wind Surf and now I'm updating it to change the large language model that's used there is a lot more going on behind the scenes with decisions that wind surf has to make it's deciding to analyze a file then

**[0:17:39]** it's deciding to invoke some tools here actually using archon my AI agent Builder so you can see it's very agentic here because you have no idea what it's going to decide to analyze what files it's going to decide to edit it makes all of those decisions in a single flow

**[0:17:53]** so comparing that to chat gbt there's just so much more decision making going on so I hope this video helped you clearly understand the difference between AI agents and workflows that just have llms baked in and both are very valuable don't get me wrong but I definitely see more of a future with AI

**[0:18:10]** agents there's just so many more possibilities that they unlock so much power available to us now and so that's what I focus on with my channel so if you appreciated this content and you're looking forward to more things AI agents I would really appreciate a like and a

**[0:18:24]** subscribe and with that I will see you in the next video
