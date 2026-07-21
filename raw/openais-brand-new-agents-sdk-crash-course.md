---
type: raw-transcript
title: "OpenAI’s BRAND NEW Agents SDK (Crash Course)"
youtube_id: e7qvd2bOITc
url: https://www.youtube.com/watch?v=e7qvd2bOITc
slug: openais-brand-new-agents-sdk-crash-course
published: 2025-03-16
duration: "0:31:19"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** quite a few months back open AI released swarm an open- Source AI agent framework that allows you to write super clean and simple python code to build AI agents and connect them together to do some powerful things I covered it on my channel a few months back and I was

**[0:00:15]** impressed but open AI made it very clear that swarm was experimental and meant mostly for educational purposes not a production ready framework but now open aai has released their brand new agent SDK it's built on top of swarm and still completely free and open source but they claim that it is now production ready

**[0:00:34]** and very easy to use to build full agentic AI apps with very few abstractions and those seem like bold claims to me so in this video I want to walk through the agent SDK with you build some powerful agents with it and then see if it's really worth using over

**[0:00:50]** all the other options that we already have out there like Lang chain and crew a pantic AI so here is the game plan first I want to show you what you can do with the agent SDK well start with a basic example and then get into more complex agentic systems that are pretty

**[0:01:05]** powerful for how simple they are to build then with that in mind I want to have an honest chat with you because open AI is claiming this is not a toy anymore it is the real deal a production AI agent framework is that really the case or are other Frameworks that I

**[0:01:20]** generally prefer like pantic Ai and Lane graph still the way to go I've got a lot of thoughts on that that I'll share at the end but for now let's dive into building something awesome with the agent SDK so here we are are in the GitHub repository for open ai's Agent

**[0:01:33]** SDK I'll link to this in the description of this video and I'll do the same for their documentation too which is pretty comprehensive walking you through getting started and all the features that they offer and The Core Concepts for the SDK are agents handoffs guard rails and tracing and I'm going to cover

**[0:01:50]** all of these in our code examples as we build with the agent SDK so agents pretty basic that's giving your instructions and tools to your llms and then the hand hand offs this is how you have different agents that work together so you have specialized agents that handle different parts of tackling a

**[0:02:06]** problem very common in good Agent architecture and handoffs are the way to make that very easy to set up within the agent SDK and then guard rails this is something super important that I don't see in Frameworks usually so having safety checks that you can create they can be custom they can use llms you

**[0:02:23]** validate input and output for your llms and you can stop responses from happening if you detect hallucinations and things like that it's pretty need and then tracing is your way to look into peer into your llms and agents running checking on all the PRS and the outputs and seeing where things are

**[0:02:39]** going wrong if they do so this is very powerful to help you debug your agents and also monitor them in production as well and getting started with the agent SDK could not be simpler so over in the documentation here just the intro homepage tab if you scroll down you get

**[0:02:54]** the installation instructions just a single line with Pip and then they have a very basic example of building an agent with the SDK and this is what we're going to be using as a starting point so I'll help you build an agent like this just Bare Bones and then we'll

**[0:03:07]** build on top of it adding all of the features like guard rails and handoffs and tracing that make this SDK so powerful so let's dive into that right now so over in this GitHub repository that I'll have linked to in the description of this video we're going to

**[0:03:20]** be building out an AI agent system in six different parts using the open aai Agent SDK so we'll start super basic we're going to build this from scratch together just laying the groundwork with a version one and then we'll add in the different features of the agent SDK that

**[0:03:35]** make it so powerful like the way it handles structured outputs adding in tool calls agent handoffs and then finally our guard rails and user context management as well so a lot of awesome different features and what we're building together here is a travel planner assistant it can take in

**[0:03:51]** preferences from a user like you can see on the left hand side and then we can ask it to plan trips for us and there's a specialized agent for managing one for hotel reservations and another to suggest activities for us to do and so it's multiple agents working together

**[0:04:07]** here because agents always operate much much better when they're specialized to something and you have many of them working together so I can say for example I'm planning a trip to Miami for 5 days with a budget of $2,000 and then it'll give a general recommendation here I can also ask it for things like give

**[0:04:24]** me some Hotel recommendations it kind of already gave me one but we'll ask it for more specific specific recommendations and we can have a conversation with it and it's going to hand off to the different agents to help us with the different parts of planning our trip it

**[0:04:38]** is super neat so there we go Hotel recommendation a City Center Hotel this is all mock data by the way but it takes in our preferences make sure that we have things like the gym and Wi-Fi amenities and then if I ask about a flight hopefully itd recommend an Ocean

**[0:04:50]** Air flight so it's taking in preferences handling different specialized agents it's not a trivial agent that we're building here we're going to be able to do it very easily with the open AI agent SDK so if you want to follow along and run all this yourself you can download

**[0:05:03]** this GitHub repository and then in the readme I have instructions for setting up everything including installing the open a SDK and all your other python requirements and then setting up your EnV file as well so you can set up your openai API key and then the llm that you

**[0:05:18]** want to use I'm going to be using GPT 4 mini for everything and by the way let me show this really quick you can run other models with the open AI SDK besides open AI models and so if you go to the models page and their documentation they instruct on how you

**[0:05:34]** can set up custom clients so that for anything that is open AI compatible like open router or olama you can use those providers within the SDK as well so I just want to note that really quick but right here just to keep things simple I'm going to be using GPT 40 mini for my

**[0:05:49]** model for everything and so over to our first implementation here I'm developing this in parts to make it as simple as I possibly can for you so we're going to start really basic here and then by the end of this like you saw with that travel planner agent we have something

**[0:06:02]** pretty cool and so first I'm going to import my libraries and then load in my environment variables which to start I'm just using the openai API key and then I can Define my agent this is directly from the agent SDK and so I give it a name I give it the instructions which is

**[0:06:17]** the system prompt for the agent and then right now I have my model hardcoded I'll use the environment variable later but just using GPT 4al mini it is that easy to Define the initial version of our agent and then in the main function I'm just calling the Run sync function for

**[0:06:33]** the runner where I pass in the agent that I want to use that we just defined and then a user prompt write me a haikou about recursion in programming and then I just print out the final output that is it it is that easy only a few lines

**[0:06:46]** of code to get everything set up initially with our framework here and so I can go to terminal now let me zoom in a little bit so it's easy for you to see I'll just run the command Python and then version one basic agent. piy and because it's GPT 40 mini it's pretty

**[0:06:59]** fast we'll get a response really quick here this is our Hau so very basic to start but that lays the groundwork for us to then start to build out our travel planner agents let's go on to version two so now onto version two we want to add in structured outputs and what

**[0:07:15]** structured outputs are is a way to standardize the response from En large language model essentially forcing it to give a Json response so that there are specific values we can always expect it to give like for our travel agent we wanted to always give a recommend reced budget and a recommended list of

**[0:07:32]** activities and we can do that with what I'm about to show you and so I have a very similar skeleton that we saw in version one this time we're going to dynamically load our model from our environment variable and then I'm going to define the model this determines the

**[0:07:47]** exact structure that our travel agent is going to Output every single time it is always going to give us a destination the duration of the trip the budget its recommended activities and then any other notes that it has for what it has outputed as well and we're going to use this within our agent which

**[0:08:04]** we'll Define right here so it's going to look very similar to our agent in version one just with a much longer set of instructions because we're getting more comprehensive here the model is defined in the same way and now we say that our output type is the travel plan

**[0:08:17]** so we pass in this class that we defined right here to instruct it exactly how to Output our response so every single time we can expect to have these pieces of information so it's not random this is is one of the ways to reduce hallucinations with llms a lot

**[0:08:33]** structured outputs are powerful and so now within our main function I just have a couple of queries that I'm going to test one after the other and so we'll Loop through each query and we'll call our agent in the same way we did before just passing in the agent and the user

**[0:08:47]** message and then I just have some fancy print statements here to make it look nice in the terminal and that is it so now we can go back over to our terminal and this time instead of running version one we'll do version two and so we'll see both queries come in one after the

**[0:09:00]** other first it's I'm planning a trip to Miami and so it's something kind of similar to what we saw in the demo and look at that we've got the duration budget recommended activities and notes and then for our trip to Tokyo the exact same thing so using structured outputs

**[0:09:13]** we get a very consistent response and that's something that you don't always get with llms very powerful stuff the sponsor of today's video is codo and I'm excited to tell you about them today because they are a free- to-use AI coding assistant that has some unique features to make them Stand Out versus

**[0:09:29]** other AI IDE they have a big focus on code quality and the biggest component of that is an agentic flow that they have specifically to help you write tests for your code and that my friend is something that is overlooked by way too many people they also just released

**[0:09:45]** Coden 1.0 an AI coder that leverages mCP way more than I've ever seen before and mCP is a big deal right now so I love seeing Cotto just leaning into that and if you don't know mCP is anthropics model context protocol it gives AI access to specialized tools to

**[0:10:03]** understand your codebase and do things within it that it couldn't do before so Cotto can be installed directly as a plugin in your IDE like VSS code or jet brain so I'm in vs code here you just go to the extensions tab search for Cotto and then click on install it is that

**[0:10:18]** easy to get started then you'll have this Cotto chat in the Le hand side so you have two modes you have the agentic mode that's the new Coten 1.0 it's going to have a very similar feel to something like Windsor for cursor except all of it is driven by these mCP

**[0:10:32]** tools you can add custom ones yourself and then you have the standard mode this is where you can do things like go through the testing agentic flow to write tests for your code and that's what we're going to do right now I'm going to show you what this looks like

**[0:10:43]** because it is just so cool so I have this simple python script right here and then to write some tests I'll show you this conversation that I went through with it so you can see what this looks like so first you tell it that you want to write test with SL test and then it

**[0:10:55]** goes through these questions to help understand the framework you want to use and the different testing scenarios that you want to cover with your unit tests and then once you do that and you can add custom ones as well it'll create all of those tests and so this is the file

**[0:11:08]** that it spit out for me with pest covering all those different scenarios that we walk through in the conversation together it is just so powerful whether you're writing new code fixing bugs implementing new features from tickets or building front end components codo Jen 1.0 can do it all and help you do it

**[0:11:24]** with high code quality so I'll have links in the description of this video for you to check out code gen 1.0 install it for free right now in your idees like Jet prain and VSS code it's definitely worth a shot now for version three we're going to add a tool to our

**[0:11:39]** travel agent tools are how AI agents are given the ability to interact with the outside world to do things like search for flights Reserve hotels or get weather information and in our case that's the tool we're going to add here is a weather tool because we want our

**[0:11:52]** agent as it's planning the trip to have weather data because that'll probably dictate the activities that it recommends and so to add tools with the open AI SDK it is super simple first we have to define a function and this is going to be what we give to our agent

**[0:12:08]** for it to be able to get weather data and so this at function tool decorator this tells the agent SDK that it is a tool for an agent and then we can Define it just as a regular python function the important thing to note here is that the

**[0:12:20]** parameters that we give to this tool this is determined by the large language model So based on the conversation it's going to pick the city and the date pass those into this get weather forecast to get the result get the weather data and then we also have this dock string this

**[0:12:36]** comment at the top of the function this is given as a part of the prompt to the llm to tell it when and how to use this tool so it's very important to get this right be very descriptive here especially if the way that you want the agent to use the tool might be unique or

**[0:12:50]** be different depending on the state of the conversation so you describe it all in the dock string and then in this case we're just using mock data for demonstration purposes but for a real implementation you definitely want to use a weather API and so in our case to

**[0:13:04]** keep it simple we're just checking to see if the city that the llm is requesting weather data for exists in this dictionary if it does then we're going to get again more fake data here and just return this string to the llm and then if the city does not exist in

**[0:13:19]** that dictionary we'll just say that the weather forecast is not available and so the important thing to keep in mind for tools is that the llm determines the parameters and then whatever string we return is given back to the llm so it then reasons about the result of calling

**[0:13:33]** that tool like now it has the weather data to help it plan its trip and then it'll format that final response using what it got back from the tool to help it do so and then to add the tool into our SDK agent it is very simple we just

**[0:13:47]** add this line right here so we give it a list of tools which in this case is a single tool we're only giving it one right now to get the weather forecast and it is that simple so now I can go back over to my terminal and run version

**[0:13:59]** three this time I got a couple of test queries just like with version two this time it'll look similar but it will include the weather data so look at this in Miami we're expecting sunny weather with temperatures around 25 to 35° C and if I look at my fake data that is

**[0:14:16]** correct it fetched the right information for Miami it's not just making that up and then if we go to uh yeah looks like we have Paris for our second query temperatures of 12 to 22 and there we go Yep this is working perfect now for version 4 let's add in some other agents

**[0:14:32]** and Implement agent handoffs so here's the thing we want to include the ability to get flight information and hotel information for our travel planner assistant as well and we could just dump in more tools to get flight and hotel data into our primary agent but it gets to a certain point no matter how large

**[0:14:51]** of a context window an agent can handle it will start to hallucinate the more tools you add into the agent so it always helps to have multiple specialized agents working together otherwise known as mixture of experts and so that's what we're going to add in here we're going to add in an agent that

**[0:15:07]** is dedicated to handling flights and another that is dedicated to handling hotels and then our primary travel agent can call upon those specialized agents when the user is asking about something like a flight or booking a hotel and so what we see right here is the exact same

**[0:15:22]** as version 3 right now but we're going to add in a couple of Agents starting with our flight agent and so we have a another model because we're going to use structured outputs for the other specialized agents as well this one will recommend flights and so it has

**[0:15:36]** information like the airline when it departs the arrival time everything that a user would care about when they are looking at different flight options and then we'll Define our tool so this agent is going to have a tool to search for flights and we Define it in exactly the

**[0:15:51]** same way as our weather tool with again a dock string that tells our flight agent when and how to use this tool with the parameters of the origin destination and the date of the flight and again just using mock data here you'd want to use some sort of real flight search API

**[0:16:09]** but I'm just going to mock this data and return it to the llm so it can take in this information and then pick one of these flights or multiple of these flights to recommend based on what the user is saying in the conversation and what their preferences are and so with

**[0:16:23]** the tool and the model defined we can now Define our agent and so we're giving the name of flight specialist list and then the handoff description this is a new attribute this is given to our primary travel agent as a description of when to call upon this agent so it's a

**[0:16:39]** specialist specifically for finding and recommending flights and then we have our instructions like before of course fine tune to our flight agent our model it has the tool to search for flights and then our output type is again this model right here so that we know that every time it outputs a response we have

**[0:16:57]** these attributes to report back to to the user so that is our flight agent then we want to Define our hotel agent so again another class we want to know the hotel name location price amenities and then even giving a justification for why it is recommending this hotel and

**[0:17:14]** then we have another tool to search for hotels quite a few parameters here but we even have the ability to search based on a Max price so there's a lot going on here the agent is able to use this as a robust tool to search for hotels in a

**[0:17:25]** specific City for a specific date and within a specific price range it's pretty neat so mock data again a lot of information for each Hotel we're going to filter by a Max price if applicable otherwise just give us all of the hotel options and return those to our hotel

**[0:17:43]** agent which Speaking of that we'll Define it right here so again handoff instruction this is a specialized agent not for flights this time for hotels finding and recommending hotels got our instructions Model Search tool and then that class so that every time it up puts a response we get all the information

**[0:18:01]** for its recommended Hotel including the justification for it it's pretty neat and so that's everything for setting up the agents now to get these handoffs configured we have to go to our original travel agent that's kind of the primary agent driving this conversation the only thing we have to add is this line so

**[0:18:18]** handoffs just like tools is an array but this time instead of tools it can call it's other agents it can call upon if it wants to hand off the conversation to the flight agent or the hotel agent it is that easy it's so simple this kind of thing setting it up with something like

**[0:18:34]** Lang chain would be a lot more complicated to get these handoffs configured and that's everything so now I'll go back to my terminal I'll do python version 4 got some test queries just like we saw earlier and so this time instead of saying I want to plan an

**[0:18:47]** entire trip I'm going to get more specific I need a flight from New York to Chicago and there we go it handed off to the flight agent which outputs these pieces of information instead of the more higher level here's the budget here's the activities I recommend all that good stuff and so it's recommending

**[0:19:02]** an Ocean Air flight and then find me a hotel in Paris with a pool for under $300 per night there we go that fits our budget it has a pool so it's got the good amenities it handed it over to the hotel agent to find this information so

**[0:19:15]** cool I just love how these agents work together uh you really want that specialization when it comes to including more than just a couple of tools for your agent so this is just a really good example of that now for version five I want to show you how to

**[0:19:27]** implement guard rails context and tracing a lot going on here that I want to show you because the open AI SDK just gives us a lot and so for a guardrail what we want to do here is we want to have a pre-check before the agent starts planning the trip to see if it's even

**[0:19:44]** realistic given the duration and the budget that the user has because if we let the agent plan a trip no matter what the user says we'll probably run into some hallucinations cuz if they want to go to Dubai for only $300 for a week obviously that can't happen so we don't

**[0:19:58]** even want the agent to try to plan that trip so let's add that guardrail right here so it's going to be another agent just like all our other guys that we have for Budget analysis so it's structured output it's going to tell us is the budget realistic what's the

**[0:20:11]** reasoning for that and a suggested budget as well so then we'll Define our budget analysis agent giving it instructions for how to determine if the budget is really realistic so we're leaving it up to the llm to make that determination which I think is fine especially for this demo case that we

**[0:20:26]** have then we pass in that budget analysis class and then we have a function to define the budget guard rail this is the function that we're going to give as the guard rail to our primary travel agent and so what we're going to do is prompt the budget analysis agent

**[0:20:40]** so we give it the latest user message which that's them saying I want to go to Dubai for $300 and then we're just telling it to analyze and see if the budget is realistic and so we'll prompt our budget analysis agent with runner. run get the final output and then if it

**[0:20:55]** is not a realistic budget we're going to print that to the terminal and give the reasoning as well and then regardless we're going to return the guardrail function output and this trip wire triggered if this is true it means that the budget was not realistic and what it's going to do is cut the execution

**[0:21:13]** short so this budget guardrail will run in parallel with our travel agent as it's starting to plan the trip but it's going to get cut short if it figures out that the budget is not realistic and then we'll just say that it's a false for the trip wire triggered if there's

**[0:21:29]** any exception that is encountered when it's trying to evaluate the budget and that is it and then for our travel agent the way that we add this in is we just add this new input guard rails parameter and then we pass in the budget guard rail for our input guard rail you can do

**[0:21:43]** output guard rails as well if you want to evaluate before you send to the user but after the agent finishes you can do either both are very powerful in this case we want to evaluate before the agent even gets a chance to fully plan the trip cuz what's the point of

**[0:21:57]** planning it if it's not realistic in the first place and that is it so now I'm going to open my terminal again let me clear this and start it from scratch python version 5 we're going to start with a few queries that should not trip this guardrail at all like going to

**[0:22:11]** Miami for 5 days with a budget of 2000 yeah it's pretty realistic and we can see that it did not trip the guardrail we got our final response and it's going to be like that for all of these except for the very last one at the bottom that

**[0:22:22]** I'll show you so it's going to be let me go to the query here it's going to say I want to go to Dubai for a week with only $300 obviously that can't happen so look at this I want to go to Dubai for a week with only $300 but boom look at this

**[0:22:35]** your budget for your trip may not be realistic and then it gives its reasoning and we get that warning at the end here that the guard rail was triggered so this is working great and this is the kind of thing that I don't see in Frameworks enough I don't see

**[0:22:47]** guard rails a lot and so I just love that the open AI agent SDK has included this I want to show you the context management as well now cuz that's going to lead into the streamlit user interface where we can set our preferences and so I have this data

**[0:23:01]** class defined for user context these are pieces of information that our tools are going to have access to that aren't actually given as a part of the prompt to the llm and so the reason we want that is sometimes we need higher level metadata to use in our tools something

**[0:23:18]** like a user ID or preferred Airlines we don't necessarily need to give as a part of the prompt to the llm and so we Define this class and then if I go all the way down to the main function in version five right here we Define the user context and right now I just have

**[0:23:33]** these values hardcoded but in our streamlet UI we'll be able to set these with that sidebar on the left side so we give our preferred Airlines Hotel amenities budget level all that is defined is an instance of this user context class and then when we call our runner. run before we just passed in the

**[0:23:50]** agent and the user's message but now we give this third parameter which is the user context and when you do this it's not given to the llm I want to to make that very clear and they make it very clear in their documentation but when we call a tool like let me go up to uh

**[0:24:06]** let's go up to the flight tool for example so I'll go up to uh search flights we have this extra parameter at the start which is the user context in this variable called wrapper and so now at the bottom of this function before we just return all the flight options but

**[0:24:21]** this time we are sorting the flight options based on the preferred Airlines if those exist and so you can see how you can take this metadata about the user their name their ID their preferences whatever and you can alter these functions and how they operate based on that information it's super

**[0:24:38]** important and so the recommended hotels and flights are going to change based on what we said are our preferences and then even in the main function below right here we'll say hey this matches your preferred amenities or for the flight will say hey this matches your preferred Airline so we can really

**[0:24:56]** personalize the communication to the user letting them know like yeah I heard what you said and here you go this is the flight that matches what you were looking for it's pretty powerful so the very last feature that I want to cover is tracing so I have their documentation

**[0:25:08]** page for it pulled up right here if you are using their default tracing functionality it's going to be using the trace dashboard in the open aai platform but if you're not using open AI models or if you just want to set up custom tracing which I'd recommend they have

**[0:25:24]** some Integrations that you can see if you scroll to the bottom of this page my favorite is pantic logfire it is super easy to set up and you get 10 million traces per month for free so pretty much free I'd highly recommend this especially if you're using like open

**[0:25:40]** router or AMA you won't have access to those traces in the open aai dashboard obviously and so going to their documentation don't ask me how they got this integration set up already with the open AI agent SDK but they did with just a couple lines of code so you can just

**[0:25:55]** go to the getting started here go through getting your log fire API key and setting that up and then in my code you can see that I import log fire and then with just these two lines of code I set this for my configuration for all of my tracing and there's nothing else I

**[0:26:09]** have to do in my code so go ahead and check this out it's so cool so I'll go to my streamlet UI like I promised I'd showcase again set my preferences on the left hand side like we just saw how to do with version five and then um I can

**[0:26:21]** save my preferences start a new conversation and say something like I want to go to Tokyo for a week for uh let's just say $3,000 all right and we get this beautiful UI now we don't have to use that command line anymore we'll get a response that looks super nice and

**[0:26:37]** then we can go to our log fire dashboard this is my execution that just happened now so I can expand into this to see the different agents that were called I can even look into my guard rail as well and see that the triggered is false it used

**[0:26:49]** my budget analyzer agent with gbt 40 mini and then I got my final response with gbt 40 mini I want to go to Tokyo for a week for $3,000 and then this is the structured output that we got this Json that my front end then transformed into this beautiful component so this is

**[0:27:04]** working really well and just overall it was so easy to create this really indepth travel planning agent with the agent SDK so I hope this was a really good starting point for you for using the open aai Agent SDK I wanted to cover all of those features so that no matter

**[0:27:21]** what you were building you can take out the different components from what I built to use for your own use case but now I want to cover the big question is worth using the open aai Agent SDK and this is of course Up For Debate so I'd love to hear in the comments what you

**[0:27:35]** think as well but I just want to give you my two cents really quick so my favorite Frameworks up until this point have been pantic Ai and L graph I've covered them on my channel a lot and the reason I like them so much besides they just work really well together is that

**[0:27:49]** they are a lowlevel abstraction and what I mean by that is they don't try to do too much for you so you have to write more code but then you get that full control and customiz AB ility that I really want when I'm building my agents there are other Frameworks like Lang

**[0:28:02]** chain and crew aai that try to do too much for you in my mind it's what's called an abstraction distraction it's really easy to use those Frameworks because they take care of so much for you but then in the end you don't really understand what's going on behind the

**[0:28:17]** scenes and it's hard to customize it to your needs and really have that control and for the agent SDK I find it leads a bit more towards that crew Ai and Lang chain level of abstraction and so it's very easy to use as we saw it's pretty powerful I do like it more than crew aai

**[0:28:35]** and Lang chain but like let's go to the handoffs for example it was so easy to set up handoffs like we saw in our code like you can see in this example but what if I want to handoff to multiple agents or if I want custom rules in

**[0:28:47]** place before a handoff takes place or maybe after a handoff takes place I don't really see how I can do all of that and I'm sure I'm missing some things like maybe specifically it's easy to have something run before a handoff but I just don't see it here for

**[0:29:03]** everything and another big thing that the agent SDK is missing is human in the loop and that's something that L graph does so well being able to before you call a specific tool or execute a specific agent actually seek approval from the human through the command line or a user interface or whatever before

**[0:29:21]** that action is taken and I don't really see how to do that like how would you have a human approve an agent handoff I don't think that's possible in the frame work here and another thing that pantic AI focuses on a lot that they don't do here is testing having a mock llm or

**[0:29:35]** mock tools being able to really validate that your agents are working well without using a real llm and if you go to the pantic AI documentation I won't show it here but they cover that in such great detail that you don't see anything for testing your agents or evaluating

**[0:29:50]** your agents in this documentation like you do for pantic AI so I don't think this is mature yet compared to pidan Ai and L graph but it is brand new so maybe they'll do more over time but in general I just think that it's missing some key things I didn't feel like I had that

**[0:30:07]** level of control and customizability that I really would want for those full production applications that I want to be building with my AI agents and going back to the code here I thought it was really nice coding with this framework I I enjoyed it I found it fun I felt like

**[0:30:21]** I built something that was pretty neat with just a few hours of prep for this video was pretty good but I don't feel like I could extend this to that full travel agent I maybe want to build I would probably rather use pantic AI or L graph so just my two cents but again

**[0:30:36]** very curious what you think as well so let me know in the comments what you think of the open aai Agent SDK personally I think it's awesome how simple it is to use to build these agentic systems but I still don't really have that level of customizability and

**[0:30:50]** control that I want that I get with some of these other Frameworks but also this framework is brand spanking new and so I'm going to be following it closely because I'm sure they're going to be adding in a lot more features over the upcoming months and so I'm still going

**[0:31:03]** to be using pantic Ai and Lan graph but watching this closely I think it could be a big deal so if you appreciated this content you're looking forward to more things AI agents I would really appreciate a like and a subscribe and with that I will see you in the next

**[0:31:16]** video
