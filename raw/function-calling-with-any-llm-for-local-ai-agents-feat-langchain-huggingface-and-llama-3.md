---
type: raw-transcript
title: "Function Calling with ANY LLM for Local AI Agents (Feat. LangChain, HuggingFace, and Llama 3)"
youtube_id: PPDsrvuPhWQ
url: https://www.youtube.com/watch?v=PPDsrvuPhWQ
slug: function-calling-with-any-llm-for-local-ai-agents-feat-langchain-huggingface-and-llama-3
published: 2024-07-10
duration: "0:15:57"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** function calling is one of the most powerful pieces of the latest and greatest large language models like GPT and Claw it's what allows them to seamlessly interact with external services on your behalf through functions that you create to interact with your CRM to book meetings on your calendar to search the web for you all

**[0:00:18]** these super powerful things that make these AI applications truly AI agents now the problem is if you want to use a lightweight and local model like meta's Llama Or Microsoft's file you lose out on all this power because they don't have function calling built in like the big players like GPT and clad luckily

**[0:00:38]** for you today I'm going to show you how to implement custom function calling so you can have all of this power in any model you want no matter how small it is you can build super Nimble AI agent applications that can be run anywhere and so you don't have to be relying on

**[0:00:51]** those big players all the time like GPT and Claude so let's dive right into the code so I'm going to give you guys a lot of bang for your buck today by going through the code pretty quickly so if you're curious about things that I don't go into detail with uh with streamlet or

**[0:01:04]** laying chain anything like that I've got other videos on my channel where I go into those things in a lot more detail today I'm going to f Focus mostly on the stuff related to the custom function calling and the local models which by the way I'm going to get those from

**[0:01:17]** hugging face today and the main model I'm going to be using is a lightweight version of meta's llama 3 you'll see that in the code in a little bit uh which Speaking of the code just like all the other videos on my channel I have a link to the GitHub in the description of

**[0:01:30]** this video where you can pull all this code and follow along with everything that I got here today and so the folder is going to be local LM tool calling I have an example environment variable file and also requirements. text file with all the python packages so you have

**[0:01:45]** everything you need to follow along and have the exact same environment and code as me and so with that let's go ahead and dive in and break this down piece by piece so the first thing we're going to do is we're going to import all of the Python packages that we need there's

**[0:02:00]** quite a bit here but don't worry we'll get into this and explain the purpose of everything that I have here first thing I'm going to do is get our environment variables into the script and that's going to include things like our model and our hugging face API tokens so you

**[0:02:14]** need all these things you can follow along with this example environment variable file makes it very easy for you to figure out what you need here next up we're going to define the model and that is going to be based on the llm model environment variable and default to that

**[0:02:27]** lightweight version of meta's llama that I mentioned earlier uh next we're going to set up everything related to assana so Asana is a task management platform and because we need this AI agent to interact with an external service to really be an AI agent I chose to use ASA so the tool

**[0:02:46]** that we're going to use today just going to be one for demonstration purposes is the ability for our local AI agent to create tasks for us in a sauna and so this function here takes a task name and a due date and I'm not going to get into

**[0:03:01]** the code and great detail here but it'll run this to create a task for us and so we can chat with the large language model and say hey I need to mold on by Saturday and we can go into a sauna and actually validate that it creates a task

**[0:03:13]** for us by invoking this function and so we'll get into that in a little bit more later when we Define our tools uh but first what we need to do here is Define a function to get the local model for us and I'm going to use streamlets cache resource decorator

**[0:03:29]** because we don't want to redefine this model every time stream streamlit reruns our python application uh because that would get really expensive especially for redefining local models and getting those up and running every single time so I have the option for GPT here just because I want to compare the

**[0:03:45]** performance of GPT to local models for this custom function calling setup U but if you don't have GPT in the model then you'll be using hugging face so hugging face endpoint is how you use their serverless API to use these models quickly but if you want to truly truly

**[0:04:02]** run a model locally it takes a lot of resources on your computer and a while to download it but you can swap it out for this code right here huggingface pipeline. from model ID and then you will actually have the model running locally on your laptop and so to make

**[0:04:15]** things quick for me right now I'm using the hugging face endpoint but it's very easy to take any model you could run this way and have it run on your computer with this code right here so super important there uh next up what we're going to do is we're going to start defining the

**[0:04:29]** tool tools and getting that ready to inject in our prompt and so this dictionary here is going to define a mapping between the function name and the actual function object in our python script and you can easily expand this with any other functions that you want to add in if you were to add more than

**[0:04:45]** one tool to this code so I only have one tool to make this simple right now but I set it up in a way where it's very easy to have two three 5 10 15 tools you could go crazy with this um and it doesn't take much more work because now

**[0:04:59]** what we do is we go through every single tool and we create a description where we have the name of the function that maps to the doc string so this code right here will actually fetch the dock string from the function which gives the AI all the context it needs it

**[0:05:12]** understands what this function is used for how to call it the arguments that it needs and what their types are and then also what it returns and so with this it's going to know everything it needs to know related to this tool when to use it and how to use it and so now that we

**[0:05:27]** have the tool descriptions ready we can inject these into a part of the prompt that will include with the system prompt and so I'm not going to dive into the prompt here but it took me a while to craft this let me just tell you because what we need to do here is we need to tell

**[0:05:43]** the AI specifically how to return a response to us we can't just have it spit out raw text because we have to understand when it wants to use a tool and what arguments to use for each tool and we want to make it possible to invoke multiple tools with one prom so

**[0:05:57]** there's a lot of work that goes in here and so we can do this using Lang chain a parser which is basically going to take the AI response and make sure it conforms to a specific Json schema and this schema is going to be uh with two keys here we have tool calls which is

**[0:06:14]** going to be a list of tool calls which where each tool call has the name and the arguments and then also a Content object which is just going to have the raw text to give back to the user so if it needs to make any tool calls this

**[0:06:27]** array will be populated otherwise it'll be empty if we don't need to invoke a tool and then if we don't need to invoke a tool we also will have the content here to give something back to the user and so as a part of the system text um what we have here for the system

**[0:06:42]** prompt for the AI is helping understand how to spit out something that conforms with the schema and then we'll use the schema to validate the response uh from the AI and I'll show that in a little bit as well and then all we need to do to pass in the tool descriptions here is

**[0:06:59]** dump this array into the system prompt and now it understands all the tools that we have here and this is how we really just inject the custom functions into this whole setup with our local AI agent and so that's about it that I'll go into for the system text here the

**[0:07:18]** next thing that we want to do is start defining the function to actually prompt our local AI agent and so we give it a list of messages um we're going to have a little bit of recursion here for retrying if the AI doesn't doesn't conform to the schema with its output

**[0:07:32]** and so we want to have a little bit of safety around having it not recurse forever and so that's what this variable is used for and then also local models sometimes will hallucinate and think they need to invoke the same tool call more than once and so I'm going to build

**[0:07:45]** up an array of the tool calls it's already made so that it doesn't make the same call twice and create two of the same as task for me for example you'll see that a little bit as well uh so the first thing we're going to do is we're

**[0:07:56]** going to say hey if we have recursed too many times just raise an exception so I don't Loop forever and then what I'm going to do is I'm going to Define that parser that I mentioned earlier and so it's using Lane chains Json output parser passing in this schema right here

**[0:08:11]** so we're telling it this is exactly the Json that the AI response has to match otherwise it will throw an error um and so when we invoke our chatbot here which by the way is using chat hugging face or chat open aai if we're using a GPT model if there is an error here that is

**[0:08:29]** caused by the fact that the AI output does not match the parser schema then we're going to just do that recursion that I mentioned earlier where we increment nested calls and we just retry again and so the the power of this is if we don't fail here AI response this

**[0:08:46]** variable is guaranteed to be a Json object that has the tool calls and it has the content nothing more nothing less it is a beautiful thing because now we have this Json object where we got rid of all the worry of large language models with their hallucinations and

**[0:09:01]** their inconsistencies we know now we have an object that we can work with with the name and argument for all the tool calls that might be there and the way that we check there are tool calls is we just check to see if the tool calls array if the length is greater

**[0:09:14]** than zero because if we actually have tool calls here then this array will not be empty so we'll have objects that have the name and arguments so we're going to use that to actually call those functions and So within this if statement here if we do have tool calls

**[0:09:28]** we're going to Loop through every single tool call and again we know that those exist or at least is an empty array because we have this parer here and So within the tools here we know we have name and arcs absolutely for sure so we don't even have to have any error

**[0:09:42]** handling here so we get the tool name we get the function that we want to invoke by using uh this mapping of name to the actual function object and then we go ahead and invoke that tool get the output and then add the result of it as a message which is kind of like a

**[0:09:58]** thought that the AI has for itself not to display to the user but just so it knows that it it made this tool call and this is the result of invoking that tool and then we just added the list of invoked tools here because that way we're not going to be invoking the same

**[0:10:13]** tool more than once again just because local models will sometimes hallucinate with that kind of thing because they're not as powerful as the big players like GPT or Cloud that's okay because we can work around that and make this work by just having a couple of extra checks

**[0:10:26]** like this and so at this point uh after after we've done all the tool calls we're going to return a response from the AI which is basically just going to be hey you wanted to call this tool here's the result of calling it now create a response for the user based on that so

**[0:10:43]** it' say something like all right dope I went ahead and created your task for mowing the lawn that is due by Saturday July 10th or something like that uh and then also if we don't call a tool at all then we can just return the AI response right away which is going to have that

**[0:10:58]** content that we can give to the user so that's if they say something like hey how's it going where you don't actually need to invoke the tool and so at that point you just have the content that you'd return to the user so that is everything for our prompt AI function uh

**[0:11:11]** now we just have our main function which we're going to start out very simply and go through pretty quickly here so we're going to start our streamlit UI with a title we're going to initialize the session State the messages here with just that first system message to begin

**[0:11:27]** and that has the tool text injected into it which which is going to be where we have all of the work for our custom function calling so this is where we have our tool descriptions the schema it needs to Output all that good stuff that is put in that first system message so

**[0:11:40]** that's how we have that initial context to tell the AI how to do the tool calling and what tools to invoke next up we're going to use uh a couple of streamlet components here to display all of the chat history except for just the thoughts that the AI has for itself so

**[0:11:57]** we're not including those uh then we're going to interact with the user so anytime it the user inputs something in the chat input component we're going to call our prompt AI to get the response and invoking any tools that are required and then just put that response back

**[0:12:11]** into the UI so that is it that is everything for our main function using streamlet and laying chain that is it we are now ready to test out our local model that is augmented with custom function calling so let's go ahead and give this a shot all right I'm here in

**[0:12:26]** my terminal now within the directory local llm tool calling the only command I have to run now to start my local AI agent chatbot is streamlit run and then local agentwith ui. I'll run this and it'll go ahead and kick off a new page in the browser for

**[0:12:41]** me here and it'll even say that I have logged in with hugging face as well so as long as your hugging face API key is correct you'll get this message and then you'll have that page open in the browser we can go ahead and talk to our chatbot so for demonstration purposes I

**[0:12:55]** even have the system message included in the chat bot right now you could definitely hide this by default if you want to just display the conversation between the user and the AI but this just shows us that everything that we put together for the custom function calling is here in the system prompt so

**[0:13:12]** we have the directions on how to give the correct Json output and then we have a list of the tools which is just one in this case but it even has some nice markdown formatting here we have the name of the function and then the dock string that tells us exactly how the

**[0:13:27]** create a sauna task function works and so we can go ahead and we can start talking to our large language model now so we can use llama 3 to create a task in auna for us so I'm going to start with a basic message I'm going to say hi

**[0:13:39]** how can you help me and so this will give us a Json here where the tool calls will be an empty array um and then the content is going to be this text that we see right here so it doesn't make a tool call this point but it tells us how it

**[0:13:55]** can help us and then I can say I need to mow the lawn by Saturday all right and now it should make a task in a sa for us to actually mow the lawn by Saturday so let's see what it says here all right task mow the lawn has

**[0:14:13]** been created in assana and is due on the 13th which is indeed Saturday so perfect llama has made a task for us so let's go ahead and go over to isana and verify that the task was actually created and here we go in masan now in my YouTube

**[0:14:27]** Project Mo the lawn due by Saturday there we go we've done this before with GPT but that was using the GPT function calling we have done this completely from scratch I could switch to Microsoft fi I could switch to any other local model from hugging face or I could use

**[0:14:42]** olama it doesn't matter I have function calling that will work for every single agent now pretty sweet all right there you have it we have taken a local large language model llama 3 that doesn't have function calling enabled by default we've made it happen through custom tooling and so you can get crazy with

**[0:14:58]** this now you can use olama instead of hugging face you can use Microsoft F you can take any model and make it work with function calling now because of just the simple steps that we took just now to make it happen a little fair warning that I want to give here is local models

**[0:15:14]** are not as powerful as GPT and Claw and it definitely can show through function calling there's a lot of hallucinations that can happen here where it won't output the correct J on sometimes sometimes it'll be weird when the way it calls functions so keep that in mind but

**[0:15:28]** as AI gets more more powerful these local models will catch up with their ability to handle these kind of complex prompts and so this is a really important tool to have your tool belt to make any model work with function calling so if you found this helpful in

**[0:15:42]** any way I would really appreciate a like and a subscribe you can also check out the AI agents masterclass series I have on my channel where I dive deep into building powerful applications with agents that's all I got for now thank you for watching I'll see you in the

**[0:15:54]** next one
