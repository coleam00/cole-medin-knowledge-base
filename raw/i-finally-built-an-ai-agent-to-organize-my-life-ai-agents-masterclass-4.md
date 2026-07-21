---
type: raw-transcript
title: "I FINALLY Built an AI Agent to Organize my Life - AI Agents Masterclass #4"
youtube_id: s3SY_2a3Woo
url: https://www.youtube.com/watch?v=s3SY_2a3Woo
slug: i-finally-built-an-ai-agent-to-organize-my-life-ai-agents-masterclass-4
published: 2024-07-14
duration: "0:13:20"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** today we're going to take the AI agent we've been working on to create tasks for us in a sauna and turn it into a fullblown task management AI agent this thing is seriously powerful and has potential to Save hours and hours of work now what does that entail exactly

**[0:00:15]** well I'm just going to go ahead and show you I typically wait until the end of my video to show the code that I create for the master class but guys this Sana chatbot is insane I need to show it to you now so you can see the power of what

**[0:00:26]** we're about to build this thing is so great that originally I created it just to demonstrate AI agent topics to you guys but I'm literally going to start using this now to manage my days and so this hooks into ASA which is my favorite task management platform and it can do

**[0:00:42]** literally anything that I need to do in ASA it can create projects for me which is the highest level of organization of tasks in as sauna it can search through projects it can search for tasks across projects it can create tasks delete them update them mark them as complete

**[0:00:58]** anything I need to do to manage my day can do with this chat bot that interacts with a sauna for me it is so cool so let me go ahead and just show you guys some of the really powerful things that it can do um so one thing that you do a lot

**[0:01:09]** with AI is you have it help you with research and so I can ask it something like what are the top 10 Technologies to learn as a software developer getting into Ai and it'll give me a nice list here I don't know if I'll necessarily agree with it but just for demonstration

**[0:01:22]** purposes I mean you do this a lot where you're going to ask AI for a list of something but now I can take this a lot further something you can't just do a g gbt I'm going to say okay great now create a project in a sauna for me

**[0:01:36]** called AI learning put each of these uh 10 texts as a task to learn them all due by Wednesday boom there we go a very complex ask from the AI here because it has to make a project go into it create the tasks for each of these Technologies

**[0:01:57]** and actually create a title for each task and determine the due date based on the date of what the current date is that I gave it and when next Wednesday is going to be and it has to do all of that with a single prompt that I give it

**[0:02:10]** and so it takes a little bit here because it has to go into a sauna and do all these things but you're going to see here that it will do it flawlessly it even gives me a link to every single task that it creates within this new uh

**[0:02:22]** AI learning project that it made as well and so we can actually go over to is now and see what it looks like and so there's a new project here AI learning I click into this and boom there we go we got a task for each of the technologies

**[0:02:35]** that it suggested to learn uh from that little research that we did with the AI and so now I can go ahead and knock these out mark them as complete or I can continue to use the As chapot and manage all of this for me all right so even

**[0:02:50]** continuing on here I can say something like okay thank you I have learned python now so now we're going to actually ask it without even really being explicit to mark this task as complete so it says great job learning python the task Learn Python has been marked as complete and your SAA

**[0:03:08]** project great and we'll we'll check that out a little bit but now I want to say I don't want to learn um mathematics and statistics anymore you probably should but this is just for demonstration purposes so I want to actually delete the task for me there you go it's been

**[0:03:25]** removed and so I don't want to have to explicitly say that I want it to delete that task um but using natural language it can pick up on the fact that I do want to do that and so it takes that action for me which is super sweet uh

**[0:03:38]** create another task but also if you want to you can explicitly say like create another task to um learn GPT something like that learn how to use the API and let's wait a little bit get the response boom there we go it's added to my AI learning projects let's go back

**[0:03:56]** over to isana and check out all of these things so first of all Learn Python boom that is marked as complete uh we no longer see learn mathematics and statistics because it removed that one and then we have the new task of learn GPT and so using this chatbot I'm able

**[0:04:12]** to do literally anything where I don't actually have to use the Asana UI which is great I still might want to use it but I can also just have conversations with my AI agent and have it do things for me for task management it is so so powerful so let's go ahead and dive into

**[0:04:27]** how we actually create this all right so now we get to actually dive into the code and soup up our AI agent so that it can manage everything in a sauna for us so the code that you're looking at right here this is a about what we had in the

**[0:04:38]** last Master Class video where we have a streamlet UI with a chatot using GPT or Cloud that can create tasks in auna for us so we have the tool to create a sauna tasks just that one right now we have the function with prompting AI with all the streaming that we set up and then we

**[0:04:55]** have the main function that defines the streamlit UI and now we get to create a bunch of of new tools to go along with this one to do all the different things in a sauna that I demonstrated just a little bit ago and so the first thing to

**[0:05:08]** say like usual there's going to be a link to the GitHub for this code in the description of the video so you can go ahead and check that out the folder for this master class video specifically is for task management agent uh like usual I have an example environment variable

**[0:05:23]** file it's a basically the same except we're working in a whole ASA workplace now instead of just a single project so this environment variable is different keep that in mind if you're following along and then like usual the requirements. text file as well so you have all the python packages and the

**[0:05:37]** versions you need for those too the version of a sauna did change a little bit as well so keep that in mind uh you need to upgrade a sauna from what we had in the last video otherwise the deletion of tasks will not work with one of the

**[0:05:49]** tools We'll add so another important thing to keep in mind so with that we can go ahead and get started the first thing that we're going to do is we're going to create a new variable that's assigned to the workplace ID that we have as an environment variable so

**[0:06:02]** before we just had the project ID and we are creating all of our tasks in that one project but now we need to go a step higher to the whole workplace because we can manage different projects within our workspace now and so that's something important to keep in mind we also souped

**[0:06:17]** up our create Assa task function to accept a project ID as a parameter as well so that our bot can create tasks in different projects and so that's the one change to this tool other than that the one to create tasks asks is exactly the same as what we had

**[0:06:32]** before so now we get to go ahead and actually create our new tools our shiny new tools the first one we're going to create is a tool to get our projects in our ASA workspace and so you can see here that it uses that variable that is based on the workspace ID environment

**[0:06:50]** variable and a couple other parameters here and then we just fetch that again just using the Asana SDK so the setup here is very similar between all the different tools here where we create our options invoke the assana API and then either return the response as a string

**[0:07:06]** or the error message as a string and then we have a doc string just like we have with our create a task function which tells the AI agent how to use this function when to use it and what kind of parameters to give which in the case of

**[0:07:21]** get aana projects is none we don't need any parameters there and it even tells the agent how exactly it's going to get the response from invoking this function so it knows what to expect what information it's going to get very exactly out of calling this tool all right so the next tool we're going to

**[0:07:40]** add is the one to create an ass project and so ass projects themselves just like tasks and have due dates optionally and so we have that and then we have the project name as well and so I'll go ahead and create the body to get that data and then create that project within

**[0:07:56]** the workspace we have here nice and easy the next one we have is to get assaa tasks and so this one this has to be once the agent knows what project to search within because we are getting the tasks from a specific project ID and then just like with creating or getting

**[0:08:14]** the projects rather getting the tasks this tool also tells the AI through the doc string exactly what information it's going to get for each task so it knows what to expect when it calls this tool so we get the options here and then we invoke the API again and return the

**[0:08:28]** result which is including all the tasks in an array now one thing to note here is that this does not handle pagination if you have more than 50 asaa tasks in one project and won't return all of them it's very easy to use the Asana SDK to handle pagination because you get like a

**[0:08:44]** token for the next page that you can reinvoke the task Fetch and so if you wanted to really really soup this up you can do that I just wanted to keep this function simple for now so that is getting as tasks the next one we have is updating Assa tasks and so given the ID

**[0:09:00]** of a single task and a data dictionary it will update the task based on what we have in data and so this one is actually really cool function because data is a very generic variable um but we can tell it in the doc string exactly how to format this data dictionary and even

**[0:09:18]** with something kind of vague like this where we have to be very descriptive and need something very specific for this object the agent still does really well with this which I think is super cool and so this data dictionary is used to either update the um completion status

**[0:09:33]** of the task like true or false is it completed or not as well as the due date and so I can actually say like hey I don't want this to be due on Wednesday anymore can you push it out to Friday I had other things come up and it'll be

**[0:09:43]** able to do that as well for any tasks that you give it very very nice the next thing we're going to do is add a tool to delete a task and so this one's really simple you just give it the ID of a task and so at this point either you're going

**[0:09:56]** to give an ID directly or much more likely is you're going to have it search through tasks in a project so that it has all the information like the ID like you fetch here and then you tell it to delete that one and it would correlate that information it has previously with

**[0:10:10]** all the tasks and their IDs with the name of the one you specifically want to delete map those and then use the ID to call this function and delete the task like we saw earlier with the mathematics and statistics uh learning step that we deleted in Assa earlier so that is our

**[0:10:27]** delete task and so now what we're going to do here in our mapping of available functions is we're just going to start adding all these tools here boom boom boom boom there we go all right so now we have all of the names of functions mapped to the actual object the function

**[0:10:42]** object in the script just like we have with the create a sauna task and that is literally it we don't have to do anything else in our function of prompt Ai and the reason for that is we dynamically fetch all the tools that are available through this mapping and then

**[0:10:55]** we bind that into our chatbot so it's so nice how easy is to add these tools all of the work really goes into creating these functions and then defining the dock string in a way that allows the AI to understand properly when and how to use these functions this honestly is the

**[0:11:12]** most important part of the prompt to the AI is these dock strings because if it doesn't know how to use these tools well it's going to use them when it shouldn't and it won't use them when it should and so this is really really important um and so yeah the very last thing that

**[0:11:25]** we're going to do here is just add on to the system prompt here because we want to give a little bit instruction to the agent on how to manage all of the information it's going to be receiving about projects and tasks and so one thing for example you never give IDs to

**[0:11:38]** the user since those are just for you to keep track of one thing that it likes to do without this added to the system prompt is when it lists out all the tasks or projects it gives the IDS of them as well and as a user just using a

**[0:11:50]** chatbot you don't necessarily want to see those IDs and so this is just to give an example of how you can add things into the system prompt to help that deal with all the information it receives from these tools and what to actually give to the user and so with

**[0:12:04]** that we are absolutely done and you can go ahead and run this just like we did before with the streamlit Run command and you can play with the chatbot go through the things that I demonstrated earlier and take it much much further as well because this can do so much for you

**[0:12:18]** so I'm literally going to be using this every day it is just fantastic so that is everything for the AI agent to manage all your tasks it's super powerful already but we're going to continue to make it even more powerful to the rest of the master class so just a little bit

**[0:12:31]** of a teaser for what's coming next we're going to dive into rag which is retrieval augmented generation it's taking external knowledge and bringing it into a chat bot so taking your files in Google Drive or your database and feeding that information into the AI based on what it thinks it needs to give

**[0:12:48]** better responses to the user and so what we're going to be developing in this master class is basically what we're going to do is make it possible to record a meeting upload it to Google Drive create a transcript of it and then take action items from that transcript

**[0:13:02]** and create tasks in auna with it and so we're going to be connecting everything we're building with regg with the S chatbot in a sing that is even more powerful so I hope you're looking forward to that if you found this video useful I would really appreciate a like

**[0:13:15]** and a subscribe and with that I will see you in the next one
