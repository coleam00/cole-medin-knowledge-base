---
type: raw-transcript
title: "THE BEST Tool for AI Agent Workflows - LangGraph FULL Guide"
youtube_id: w_HeP0A2MF8
url: https://www.youtube.com/watch?v=w_HeP0A2MF8
slug: the-best-tool-for-ai-agent-workflows-langgraph-full-guide
published: 2024-08-11
duration: "0:24:08"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** welcome to the big leagues today we're going to talk about what goes into building production grade AI agent applications I'm going to show you how to do it with the most powerful tool for building agentic workflows which is Lang graph now when most developers build AI agent applications their code gets

**[0:00:16]** really really messy as they try to tie different agents together they have no clear concise and generic structure for defining the agent interactions and so they're left with a bunch of spaghetti code that is really really hard to maintain you don't want to be that developer I don't want you to be that

**[0:00:31]** developer I once was that developer and it was very painful so I'm going to show you how to avoid that completely using Lang graph which makes even your most complicated agentic workflows clear concise and bug-free and that my friends is the developer dream so I'm going to start with a quick overview of Lang

**[0:00:48]** graph then I'll show a couple of examples to make it really clear for you how it works and then I'll even show you in code how to implement land graph we'll actually be augmenting the task management AI agent I've been building as a part of the AI agent Master Class

**[0:01:01]** series we're going to make the code 10 times cleaner and more scalable and it's going to be really easy to follow along with even if you haven't seen the other videos in the AI agents masterclass Series so let's go ahead and dive right into L graph so here we are in the

**[0:01:14]** official documentation for Lang graph which is a product of Lang chain now Lang chain is like the best library for working with large language models so it makes sense that Lang graph would be the best for working with agentic workflows their documentation is really nice and concise L graph is just so easy to use

**[0:01:30]** and actually the first sentence here in the documentation sums up really nicely building language agents as graphs Lang graph is a library for building stateful multiactor applications with llms used to create agents and multi-agent workflows which is exactly what we are looking for and there got some key

**[0:01:47]** features listed here which all of these things I'm going to be implementing when I en enhance the task management agent but we got cycles and branching which is really important to define those graphs and have the AI agents work together the persistence so that you can manage the

**[0:02:00]** state within the graph even between different executions you have human in the loop for approval for certain things which is a really important part of AI you don't always want AI running and doing everything on its own you have streaming support so you can have that typewriter style output from the AI in

**[0:02:14]** our user interface and then obviously integration with Lang chain which makes sense since Lang graph is a product of Lang chain so a lot of really important key features here they also have a couple of conceptual guides that if you want to dive into L graph deeply which I

**[0:02:28]** recommend you do these are good to check out to truly understand how L graph works because you've got the graph which is the highest level concept then you have the state which is all the variables that are maintained in the execution of the agentic workflow like the chat history or um the number of

**[0:02:44]** retries that you have for tools like whatever your state might be you manage that and then you have the nodes which are basically your agents the edges which is how all the agents are connected together even conditionally and then some other really important things as well like checkpoints and

**[0:02:56]** threads which we'll dive into a little bit when I code some stuff up with our task management agent so I definitely recommend diving into all of this but for now let's go into some examples all right so here is our first example of an agentic workflow that would work really

**[0:03:11]** really well with Lang graph this is the kind of thing that you definitely would not want to code with out clear and concise structure that lane graph would give to you and so this what we have right here is an agentic workflow for generating charts and so like the user

**[0:03:24]** input as an example here is generate a chart of the average temperature in Alaska over the past decade and so the execution will first go to the researcher which is going to do some research to gather information to ultimately create the chart then it'll produce a response which will go to the

**[0:03:40]** router so this is the core part of the graph which is going to determine for every single message that comes from the researcher do I need to research more or can I go and generate the chart now and so if there needs to be a tool call like

**[0:03:53]** searching the web or something it'll do that and go back to the researcher or if it just needs to continue doing more research it'll do that otherwise if the research is done then it'll just go to the chart generator and so this will actually invoke tools to execute

**[0:04:05]** code to generate that chart and then send it back to the user so there's a lot of things going on here a lot of different routes that can go through the chart and so it's really important to have something that clearly defines these AI agent interactions and that's

**[0:04:18]** what Lane graph would give you so let's go on to the next example so this is a fun one because this is an agentic workflow for code execution and this could even be a part of the previous example because we needed to execute code to generate the charts and so we

**[0:04:31]** could literally have one step of one agentic workflow being an entire agentic workflow in and of itself it's very meta but L graph would even make that easy to manage and so what we have right here is a question that comes in from the user or maybe a request like generate a chart

**[0:04:47]** and then it's going to generate the Preamble Imports and code and so it'll try to then import the code as another step and if it fails then it's going to go back and try to basically just redo it but if it succeeds then the Imports are good to go so now we can go ahead

**[0:05:01]** and execute the code so if it fails then it'll basically restart the whole process and try again and then if it doesn't fail I.E the Imports were successful and then the code was generated and ran successfully then you would come back to the user with the final answer pretty cool stuff not very

**[0:05:17]** trivial and so it's important to have something like Lang graph to make this possible because if you were to generate all of this from scratch Cod it all up from scratch it would not be easy all right so the last example I have here is the simplest and it goes directly with

**[0:05:30]** what I'm going to be implementing in code to put Lang graph with our task management agent we've been building as a part of the master class so a lot of times when agents interact with tools it goes in a loop and the reason for that is you have an agent that decides it

**[0:05:43]** wants to invoke a tool like creating a project in a sauna that tool will run and then the output will be given back to the agent now the agent will do one of two things here either it's going to give the response back to the user like yes I went in ahead and I created this

**[0:05:58]** project for you here's a link to it or it's going to decide that based on the user's request it needs to continue to invoke more tools to do more things so maybe it'll go back to the tool calls and it'll say okay now that I created the project I have to go into the

**[0:06:11]** project and create tasks within it and so it'll run the tools again and then go back to the agent to again make that choice if it needs to invoke more tools or give the response back to the user and so this Loop can go on for a very

**[0:06:23]** long time usually it doesn't do it more than a couple times or a few times but there's still a loop here where it's very beneficial to implement langra which is something that we're going to do now within our task management agent so I wanted to start by going over what

**[0:06:36]** the task management agent looks like before implementing L graphs you can really see how powerful it is so what we have here is the code for the task management agent that I've been creating as a part of the AI agents Master Class series it's pretty neat you can talk to

**[0:06:49]** the chat bot and ask it to create tasks for you mark them as complete create projects anything you'd want to do to manage your day now I don't want to focus on all of the tool functions and the stream that you want everything right now I want to just talk about the

**[0:07:01]** function for prompting AI because this is what we're going to enhance with Lang graph so I have this function called prompt AI where we give it a list of messages which is the chat history and then we're going to create a chat bot and get the response from the latest

**[0:07:14]** message from the user then we check to see if there are any tool calls that need to be invoked and if so we go through each one of them and call them so we get a bunch of tool messages added the chat history based on the result of

**[0:07:26]** invoking these tools and then we use recursion to call Prompt AI again with these tool responses so that we can generate another response based on the result of calling those tools and so that's using recursion we also have this nested calls variable here to make sure we're not recursing forever this is

**[0:07:42]** literally the last example that I showed where Lane graph could help because we have an agent that will invoke one or more tools and then go back to the agent where it'll decide either to invoke tools again and go through that Loop or give the final response to the user now

**[0:07:56]** this overall is a pretty concise function and it works decently but it is not extensible if we want to add human in the loop or if we want to handle different tool calls in different ways or if we want to change a large language model depending on if we've already

**[0:08:09]** called tools or not any way that you can think of extending this functionality this is not going to work very well this function is going to fall apart and it's going to start looking like spaghetti code which like I said at the start of the video that is what we want to use

**[0:08:22]** Lang graph to avoid and so I am going to show you now how to change this so that we can use Lang graph for our tool calling to make our sauna task manag agent that much cleanable and more scalable so the one thing I wanted to mention before diving into the L graph

**[0:08:35]** implementation is that I've restructured the task management agent code a little bit just to make it more concise and clear and work better with the L graph implementation so all of the functions for interacting with a SAA all the tools that we have are implemented in this tools. piy file as well as that mapping

**[0:08:50]** that we use to bind the tools into our AI object and then we also have runnable dopy which is where we'll be implementing Lang graph and then our main script here which will have the Stream UI like usual and this is where we'll interact with our Lang graph

**[0:09:03]** runnable our runnable just being an instance of our graph that we can use to execute our agentic workflow so all these scripts are going to be in the seven L graph agent folder because this is the seventh AI agents Master Class video and I'll also have the example

**[0:09:16]** environment variable file requirement. text file like usual so that you can set up your environment just like mine to test this out yourself so all this is just going to be in a GitHub repository which I'll have a link to Below in the description of this video so with that

**[0:09:29]** we can begin our L graph implementation so I'm going to go over to runnable dopy which I'm going to be implementing completely from scratch to show you very concisely step by step how to set up this L graph implementation to give you the best idea of how L graph works and

**[0:09:43]** how it actually helps us with this task management agent so the first thing I'm going to be doing here is importing all of the libraries that we need from Lang graph as well as Lang chain and then I'll also be importing our tool mapping from tools. py because this is what

**[0:09:57]** we're going to bind into our chat AI objects so that the tools are available to the llm next I'll load the environment variables and fetch our model that we're going to be using and then I'll use that to create either a chat open AI object or a chat anthropic

**[0:10:11]** object based on the model so we can use Claud or gbt in this case and then I'll bind the tools so we have all that available to the llm to do things in a sauna for us so with that we can begin our Lan graph implementation starting with the state of the graph so this is

**[0:10:26]** the first key concept of L graph we're going to be talking talking about State and then going into our nodes and then our edges and all three of those things form together to make the full graph for our AI agent execution so with the state this is where we Define everything we

**[0:10:41]** want the graph to keep track of for us and in this case it is very simple we just care about it keeping track of the messages so for example as it's calling tools and adding tool messages to the chat history we will keep track of that in the graph state right here now don't

**[0:10:57]** worry about the types too much here usually in like graph you'll Define a type for every piece of State like a string or a list whatever this is basically just saying it's a special kind of list where we have this add messages function so whenever we set messages to a single message instead of

**[0:11:12]** overriding the entire list of messages it'll just add that one message onto the chat history and that is like the most complicated part of this entire L graph setup so if you didn't understand that fully don't worry overall this is really really basic that's just the one little

**[0:11:25]** tricky part is that we're going to be adding messages on u in that way and so that is it for the state for this graph super super easy so now with that we can go on to our nodes and so we're going to create one node for invoking our AI

**[0:11:39]** agent and then another node for handling the tools that that AI agent might decide to invoke and that's going to create that Loop that I had in that other example where the AI agent will call the tools and the tools might go back to the agent which then might

**[0:11:53]** invoke more tools and so let's start by creating the node for calling our model invoking our AI agent essentially and this is going to be in a synchronous node because we want to stream out the responses so that we have that nice typewriter style so that it looks like

**[0:12:07]** the AI agent is typing out to us in our streamlet UI just like it was in previous implementations of this task management agent and so the key thing to understand here for nodes in Lan graph is that every node that you have defined has two variables that are automatically

**[0:12:22]** given to the function and that is the graph State as well as our configuration things like our thread ID and the maximum number of nodes that can be executed to avoid infinite recursion so the big thing here to focus on is the state because now what we can do here in

**[0:12:36]** this node is we can fetch any piece of state that we want just by calling that part of the state dictionary and so I want to grab the messages in this case fetching that from the state and that is all I need to do to have that piece of

**[0:12:49]** information in the node now so I can do things with it like invoking our model with the messages and so I'm using the asynchronous invoke of our chatbot enhanced with the tools getting that response printing out for debug purposes and then finally adding this onto our messages state so the way that you take

**[0:13:06]** a node and you have it update the state of the graph is you just return an object of the node where the keys are going to be the pieces of state that you want to update and the values are what what you want to update them to and so I

**[0:13:19]** can even have other pieces of State updated here by just having a comma separate a list of all the different key value pairs just like you typically do with the dictionary in Python and so in this case I'm going to add add the response onto the chat history by just

**[0:13:31]** setting messages to the response and again because we have this annotated list with the add messages function this isn't actually going to set messages to just the response it's going to take the response and add it onto the list of messages so that is how that works there

**[0:13:45]** and that is how we get the AI response and add it onto the chat history just like we did with prior implementations of this agent so that is our node for calling our model next we'll Define the tool node and so this will take in the state and we don't even need the

**[0:14:00]** configuration in this in this case we just need the state and so we're going to fetch the messages again and then get the last message and if the last message exists and there are tool calls on it basically just making sure that last message is actually an AI message that

**[0:14:14]** requested tools to be called then we're going to Loop through every single tool get the name of the tool and if it is defined if that tool is actually one of the tools that the AI can invoke then we're going to invoke it and then add that new tool message onto the chat

**[0:14:29]** history so the AI has context to then answer the user's question based on what happened when it tried to invoke that tool and so again we're just going to update the messages with the the new history of the tool response outputs and so with that we can go on to the next

**[0:14:46]** piece of the graph which is defining our router and so this is going to basically be a conditional Edge depending on if the agent needs to invoke a tool or not we're either going to go to the tool node or just return the response back to the user and so the way that looks like

**[0:15:01]** is we're going to get the last message just like we did in the tool node and we're going to check if there is a function call or not so if there is not any tool calls that need to be made that means the execution is done and we can

**[0:15:14]** give the response back to the user so we're going to return end end is just a lan graph literal that means the end of the graph and so that will cut the execution and give the response back to the user otherwise if there are tool calls that need to be made we simply

**[0:15:28]** need to return the string tools which is the name of our tool node and so that way the execution will flow to the tool node which will handle any of the tool calls that need to be made and so with that we have our conditional Edge and now we can create the function that's

**[0:15:42]** going to bring this all together to create a single app workflow that we can invoke to use our L graph runnable and so I'm going to create the workflow here based on our graph State and then Define the two nodes that we have here for calling the model and handling our tool

**[0:15:57]** calls I'll set the entry point to agents because when a user enters something into our uh chat box on the streamlet UI we want it to go to the agent which then would decide either to go to the tools or go right back to the user and then

**[0:16:10]** we'll add our conditional Edge so we're using the should continue function and this flows from the agent node so agent node goes to this decision here where either we need to invoke tools or we have to go to the end and send the response to the user and so then if we

**[0:16:24]** do go to tools then we need to go back to the agent after we invoke the tools so that it can generate the final response for the user and so all of this comes together to Define that graph that I had in the third example where we have

**[0:16:35]** the agent that will go to tools go back to agent Loop forever until there's no longer any tool calls and then it'll go back to the user with the final response and so now we can just create this workflow by compiling it together into an app and then returning that to the

**[0:16:48]** user so now this is what we're going to use in our streamlet UI to get the response from the AI now instead of using that prompt AI function that I showed earlier and we have persistence setup here basically just in memory it's so easy to use with with L graph you

**[0:17:02]** just have to use a sqlite saver and then you add that as a checkpoint or into the workflow when you compile it so that basically when you execute the graph once and you're managing the state it's going through and invoking tools whatever and you come back to the user

**[0:17:14]** and then you go back again it'll have that chat history still saved within that execution of the graph and so that persistence is a really powerful thing that is so easy to set up with Lane graph so with that we have everything we need and now we can go ahead and

**[0:17:27]** implement this in our main script with our streamlet UI all right so this whole setup for the streamlet UI and actually using our lane graph runnable I'm going to walk through it from scratch as well but this one's going to be a lot quicker because we already have the whole

**[0:17:39]** execution with the graph defined at this point and so I'm going to import everything I need to start including the get runnable function where we can get that app from Lang graph and use it to interact with our agent next up I'm going to create an instance of that

**[0:17:54]** runnable I'm going to use st. resource so it's only defined the first time we run the script and not every time streamlet reruns the script when we have UI State changes and so now at this point we had the chat bot available to us to invoke the entire graph and you

**[0:18:08]** can even use Lang serve which is another tool from Lang chain to turn this runnable into an API endpoint which is something I'm going to be making content on later it is a super powerful thing because you can have the power of your entire agentic workflow just behind a

**[0:18:22]** single API endpoint and that's how you get things running remotely in the cloud as well because right now this is just all running on my laptop or your laptop top if you are following along so we have a local instance of our chatbot created here and then we're also going

**[0:18:35]** to get a thread ID because this is kind of something I alluded to already in the configuration for our Lan graph runnable where we have a thread ID and that's how we basically manage a single session so that we have the state persistence between executions so if I have a thread

**[0:18:49]** ID of 1 2 3 4 and the graph is running and creating that chat history and then I call it again with the thread ID of 1 2 3 4 it's going to have that same chat history that it's save from the prior execution and so all that is dictated

**[0:19:02]** through the thread ID which again I just want to have it defined once so it doesn't keep changing every time our state and the UI changes and so then I'll Define the system message here and so this is just basically telling the AI agent who it is and how it helps us and

**[0:19:17]** some context like the date and then we'll go ahead and start creating our function to prompt AI so now this time instead of just invoking the chat object directly within prompt AI we are going to invoke our Lan graph runnable and it is a synchronous just like the graph is

**[0:19:34]** a synchronous with the call model node because we want to stream that output in a nice typewriter format like I already mentioned and so first we'll create the config for runnable which is just the thread ID in this case and then we are going to invoke our chatbot and we're

**[0:19:49]** going to use the asynchronous stream events function so every single time there's a new Chunk from the AI we're going to get this in this asynchronous for Loop and if the event is of type on chat model stream AKA we are getting a single Chunk from the AI model we are

**[0:20:07]** going to yield it to our main function which is going to be calling this prompt AI so every single time we get a little piece of content this function itself is a generator that keeps yielding those chunks over and over and over again so you can continue to tack those onto the

**[0:20:22]** AI response that we are displaying in the UI and so with that we can start defining our streamate UI to do all the interaction so we have a title here we're going to initialize the chat history to just that system message to start and then we're going to display

**[0:20:37]** all the chat messages that we currently have built up in the chat history and then we're going to have that prompt to the user within that chat box on the bottom um where we'll handle the user prompt put in this variable here and then whenever the user does type

**[0:20:50]** something we're going to add that onto the UI as well as the message State and then we'll prompt the AI by calling this prompt AI function and so so we're going to again asynchronously Loop through every single chunk that this prompt AI generator is giving to us and for each

**[0:21:05]** one of those chunks we are adding it onto the response content and what we're going to be doing on the UI side of things is we start with this empty assistant message just this placeholder and every Chunk we get we're going to keep adding it onto that chat message in

**[0:21:22]** the UI so that over time it it fills in with the ai's response so it looks like it is typing out to us and then at the end once we have the full response with all the chunks finished and the graph is done running then we'll add that on to

**[0:21:35]** the chat history that we're managing here because that's what we're going to be continuing to pass into the graph and so with that we have everything to find this is much simpler overall and it is very very extendable because of the power of L graph so let's go ahead and

**[0:21:48]** test this out and make sure that everything is working with this brand new shiny implementation of our task management agent all right so here we are in the streamlit UI that I simply started up with the command streamlit run and the name of my main python script so what I want to test out here

**[0:22:03]** is I just want to make sure that this works just as well as prior implementations of this task management agent in my AI agents Master Class Series so I want to make sure that we still got the nice streaming output that it can remember different chat messages that I can do the tool calling all that

**[0:22:17]** good stuff with the clean new implementation using L graph so I'm going to start with a very basic request and say uh list out the projects I have here we go so it should go out to Asana and and find the projects for me and then list them out and there we go

**[0:22:32]** YouTube Fitness business personal en coding and so I'm going to ask it to now create a task for me in the coding project so in the coding project I need to uh code a new SAS by uh let's say Wednesday all right so let's have it make something in a sauna and then I'll

**[0:22:50]** go and actually validate that in a little bit here so there we go create a new SAS has been added in the coding project due by August 7th Perfect all right so I'll just say thank you so I'll just do like a non-tool call test to make sure that all works well and sure

**[0:23:03]** enough it does so perfect yeah just a quick little test there and so now we can even shift over to AIC quii and sure enough yep in my coding project which I'm already in we got code a new SAS due by Wednesday so everything is working perfectly but now the code is much

**[0:23:17]** cleaner and more scalable with Lang graph so I hope that the power of Lang graph has been made evident to you through this walkthrough and that you can see that it is crucial to use it for agentic workflow implementations I know this is a bit more of an advanced topic

**[0:23:31]** compared to other things on my channel but don't worry I'm going to be pumping out a ton of content around Lan graph because it really is so powerful that I need to use it for everything in the AI agents Master Class Series going forward so a lot more to come on that with

**[0:23:43]** things like human in the loop which is one topic I really wish I could have covered here and then also a lot of other things like using Lang serve to actually deploy your Lang graph runnables in the cloud so you can use it in a front end using something like the

**[0:23:54]** versel AI SDK so yeah so many different topics I'll be covering with lra in the future so if you're interested in that and if you found this video helpful I'd really appreciate a like and a subscribe and with that I will see you in the next video
