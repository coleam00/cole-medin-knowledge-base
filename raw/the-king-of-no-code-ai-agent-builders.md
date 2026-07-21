---
type: raw-transcript
title: "The KING of No Code AI Agent Builders?!"
youtube_id: 0c05ijEmk2g
url: https://www.youtube.com/watch?v=0c05ijEmk2g
slug: the-king-of-no-code-ai-agent-builders
published: 2024-11-08
duration: "0:19:16"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** when it comes to building my AI agents I need control of all the tiny details after all that's how you truly make an AI agent that fits your needs and is production ready the big problem is it is hard to find platforms out there that make it easy to build agents without

**[0:00:16]** code and still give you that level of control so a lot of times I just resort to custom coding my agents when I don't necessarily need to and so I lose a lot of time but recently I have had the pleasure of building a few AI agents with voice flow a no code platform that

**[0:00:32]** makes it so easy to build AI agents all the while still having the control you need to manage your rag pipeline how the AI agent handles different conversations the Integrations with your different tools adding in custom code if you want you get the point it is a fantastic

**[0:00:48]** platform so I jumped on the opportunity to collaborate with voice flow for this video voice flow agents can be turn into an embeddable chat widget on your website or an API endpoint so deploying them is really easy and customizable on top of that there are a lot of features

**[0:01:03]** on the platform for debugging monitoring and analyzing agents in production and so the voice flow team has really proven to me that they have a good head on their shoulders when it comes to making their platform Enterprise level so in today's video I'll show you how to build

**[0:01:17]** a simple AI agent with voice flow and integrate it with a basic ending end workflow that I made to send messages in slack the point here is to show you at a very basic level how you can integrate voice flow with really any service that you want and that's really important

**[0:01:31]** because that's really what makes an AI agent an agent we'll even use autod Dev our bolt. new Fork to create a front-end for our chat bot a lot of really exciting stuff so let's go ahead and dive right into it all right so I'm here in the homepage for voice flow and in

**[0:01:45]** one simple sentence the mission of voice flow is to be the brain between your front end and your back end and I have a really good example and I'm going to show you here that ties into it well because my front end is going to be a simple react app that I make with autod

**[0:01:58]** Dev or bolt. new fork and then my backend my single service for this basic example is going to be an n8n workflow and so in your case it's going to be something similar where you have a website and you have a bunch of different services in the backend like

**[0:02:11]** slack or Google drive or different AI agents that you have hosted and you need something in the middle to connect those two together and that is exactly what voice flow is it gives you an AI agent that has understanding of your different tools and can direct the conversation

**[0:02:26]** for the users of your agent and so let's go ahead and dive right into the platform now you can get started for free really really easily just click on the nice big blue button in the center of their homepage create your account and then that'll bring you to this

**[0:02:38]** dashboard right here where you can create your first agent now I am not going to dive into every single detail of voice flow and all the different features that they have because there is certainly a lot but if you are interested in that and you really want to use voice flow to build your AI

**[0:02:52]** agents I would highly suggest checking out the course that they link to right here in the dashboard so you click on this right here you'll go to their documentation where there are a lot of phenomenal videos to get you started with really robust use cases within the platform as well all these videos are

**[0:03:07]** made by Daniel which I actually met with him personally really cool guy he knows his stuff and he will help you get started with building whatever you want within voice flow and as you go through this documentation I really think you'll see why You' want to choose voice flow

**[0:03:21]** over another platform like building everything in n8n or using something like flow wise because compared to n8n a lot of this is easier to get set up like your rag pipeline for example getting your knowledge based set up in NN is a hassle and then as far as pricing goes

**[0:03:35]** it's actually more competitive in pricing compared to something like flow wise unless of course you're setting up flow wise yourself locally and hosting it and dealing with all that so yeah just a great platform in terms of cost and what it can do for you again still giving you that level of control that

**[0:03:49]** you really need so back in the main dashboard let's go ahead and create our first voice flow agent so I'll click on new agent in the top right and then just give it a name of n8n agent and then what you can do right out the gate is

**[0:04:02]** that you can import a web page to kick off the knowledge base for the agent super super cool you can do the homepage of Your Business site so it has an information to answer questions for users that kind of thing I'll just go with the default voiceflow dcom so I'll

**[0:04:14]** create the agent and it'll parse through that page right out the gate create the vectors for it train the agent and then kick it all off for you and bring you into the agent dashboard once it is set up all right so 20 30 seconds later we have the agent set up and we're brought

**[0:04:28]** to the dashboard with the default Fe view here of our knowledge base you can see that first page that was ingested as our first data source and that's one thing I really appreciate about voice flow here is that they make the knowledge base a Forefront of the agent

**[0:04:41]** dashboard because that's a really important part about really any AI agent is being able to have that rag pipeline so it has an internal knowledge base for things like your e-commerce products for example if you're building an e-commerce chatbot and so also if I click on add data source in the top right here you

**[0:04:55]** can ingest different URLs a whole site map so it can understand the structure of your website and adjust all those pages you can upload a file insert plain text and they have an integration with zenes as well so very robust for the knowledge base and then also you have

**[0:05:10]** workflows and so workflows this is where you define the operations for the agent how the conversation flow actually happens and this chat widget that we have here in the bottom right that you can also use as an API endpoint if you don't want to have your agent as a chat

**[0:05:23]** widget and so clicking into one of these right here I'll click on edit workflow and this is where you can kind of see how you have this drag and workflow Builder similar to something like n8n or vector shift or flow wise where you have all these different actions that dictate

**[0:05:36]** how the conversation goes so you can get a response from the AI for example uh you can just send a raw message so you just drag it into here type in the message that you want it to send like hello and if you want to you can bring

**[0:05:48]** it into the middle of the conversation like this and so after you open up the widget it'll say hi there I'm your new AI agent and then it'll say hello and then it listens for a trigger which is how we invoke different tools and I'll get into that in a little bit and so

**[0:06:01]** when you listen for a response from the user you can have them select from a couple of hardcoded buttons you can capture specific input to store in variables so if you're looking for certain information before you call a tool you do it with this so there's a lot of features built into the platform

**[0:06:17]** specifically for helping AI agents understand and get the information that they need to call certain tools and that's what I really really love about voice flow and there's a lot of different logic nodes as well development nodes so you can create a custom function with JavaScript within voice flow and use that as a node U API

**[0:06:35]** endpoints knowledge based search custom actions there's so much they have available here so really you can do anything in the platform especially because you can integrate with any service through API end points like what I'm going to do with my n8n workflow and so let me go back here and show you a

**[0:06:51]** couple of other things so in the content tab here you there's so many things I'm not going to dive into a ton of details here I just want to call out a couple of really neat things first of all you have components so these are basically like workflows that you can add within

**[0:07:04]** workflows and so reusable components is a really important part of building really any system and so components is the way to do that within voice flow they also have variables and so anything that you might want to store throughout a conversation like a clarifying question that the agent asked to a user

**[0:07:21]** you can store that in a variable and reference that later on as well and so you have this entire set of context in a conversation that you can reference in any prompt to the AI for any tool call that you make to an external API it's just really really robust and we'll see

**[0:07:35]** this in a little bit as well and then you can also create custom functions which is so so cool because you can use JavaScript to really make anything that you want and then like I showed it a little bit ago use that as a node in any workflow super super cool next up we get

**[0:07:51]** to intents and entities and this is where we get to really Define the tools for our agent and telling our agent when to invoke these specific tools so there's a lot of different sample stuff that's created here in this agent but this is where I'm going to start and

**[0:08:07]** really build my custom agent and show you how to set up tools to interact with an n8n workflow all right so here is the game plan first of all I'm going to create an intent right here and that is basically the instructions to the AI agent to understand when to use a tool

**[0:08:22]** so that's an intent then we will create a workflow that defines what we actually do for the tool like sending the slack message through interacting with the n8n workflow API endpoint and then I'll dive into triggers and all the different nodes that go into creating this workflow so it's really going to be a

**[0:08:39]** nice concise compact example of using a bunch of different cool things in voice flow to work with an NN workflow and so first of all let us create an intent and this is where we Define so I'll click on new intent in the top right this is where we Define when and how to use this

**[0:08:54]** tool and so send a slack message I'll just give a simple name here and then description this tell tells the agent when to use the tool so I'll say trigger this intent when the user wants support or to send a slack message and then for the utterances this is where we give the

**[0:09:10]** agent examples of what the user might say that would necessitate the use of this tool and so I'll add an example here I'll just say I need support and then I can give another one like I need to send a slack message and then you can also use AI to generate more utterances

**[0:09:27]** here just so you don't have to think through all these different examp examples and yeah these look really good so that now defines when and how to use this tool and so the last thing that we have to do here is add a required entity because whenever we want to invoke a

**[0:09:40]** tool like this na workflow to send a slack message there's typically input variables like in this case we need to know what message we actually want to send within slack so just some string that def defines the text that we send in and so that is what an entity is it

**[0:09:56]** is essentially an input variable and so I'll say slack message as my name and then for the data type you can Define certain types like email or age I'll just do a custom because it's just a default string and then I'll just say for a synonym message here and so now

**[0:10:11]** this is going to Define an entity so now before I invoke this tool the AI agent needs to have a value for slack message and so it will intelligently interface with the user get that value before it ever even thinks about calling this tool and also if you had a tool for like

**[0:10:28]** booking an appointment for for example maybe you need to know the name of the meeting and when to meet and who the guests are of the meeting you can have multiple different entities here and the agent will have that conversation with the user getting all those values and

**[0:10:42]** only continuing when it has every single one of these required entities here and this is the kind of power that voice flow gives you that other AI agent no code platforms don't they're focus on intents and the customization around it and the examples you can give to help it

**[0:10:58]** understand when to use these tools it's just so so powerful and it works so incredibly well and what you can do is even preview here so I can Define some sort of utterance as in just what the user said and then it'll tell me what tool it thinks it should have used based

**[0:11:16]** on that user message and so in this case I can say I want to book a demo and if I click Send it'll say oh yeah you wanted to use the book a demo intent um the reason I didn't do a send a slack message intent is because you have to to

**[0:11:29]** set up a workflow using this intent uh for the tool definition before the preview will actually pull in this intent so I'll show that right now here so we have this intent it's looking good there's even customization you can do around like you can Define the AI model

**[0:11:43]** that chooses what tool to use you can change the prompt if you really want it's not really recommended that you touch this but it's just so cool the level of control that voice flow gives you that's just one of the examples to go along with what I was saying earlier

**[0:11:55]** that it really gives you that control still even though you're not custom coding anything and so now what I'll do is I'll create a workflow that defines this tool so I'll click on new workflow in the top right and I'll say this is a send a slack message tool and the

**[0:12:10]** description doesn't really matter it's optional because it's the intent that defines and tells the a agent when to use the tool it's not the description right here so I'll create the workflow and then for my trigger for this workflow that is where I can add my intent so you can add it events as well

**[0:12:24]** but I'll add the intent of sending a slack message and keep in mind that this this is only ever going to be triggered once the agent actually knows what message to send in slacks we can assume at this point that that slack message variable is filled in with what they

**[0:12:39]** want to send and so what I'm going to do is immediately just make that API call so I'm going to do the dev and then API and it's going to be a post request to my n8n agent I'm not going to go into a lot of details of n8n I have so many

**[0:12:53]** videos on na on my channel already but over to my very basic workflow right here that makes a request to slack I have this web hook trigger and within it I have this production URL so I'm going to copy that go back in here paste it here and then for the headers I have a

**[0:13:11]** authorization Bearer token so the header values authorization and then the bearer is Bearer and then I have this test off credential here where the bearer token is just test off so I'm going to um remove this once I upload the video obviously you're not going to be able to

**[0:13:25]** just use my workflow and spam my slack U but it's just bear test off and so this is just whatever Bearer token that you set up within your NN workflow or you could obviously not have any credentials as well if you wanted so I'm going to have that set up I got the workflow

**[0:13:40]** saved and active and now for the body I expecting the value of message for the input to this workflow so if I click into my slack node right here it's going to send message attribute of the body as that slack message and the value here I'm going to use the curly brackets for

**[0:13:58]** variables and I'm sending in slack message so again when this intent is triggered the slack message is a required entity so the agent will have already figured out at this point what the message is to send in slack and so I'm using it right here and I can even

**[0:14:14]** send a request here a sample request and just say for the message test message so I'll click generate and boom there we go it triggered my N8 end workflow if I go to the executions we can see an execution from just now and if we go into my slack Channel there we go it

**[0:14:30]** sent test message so everything is working good for the connection and now we just want to send a message based on the success or the failure so if the API call was a success then we're going to send a message that says your message was sent in slack and you can also use

**[0:14:45]** AI to generate a more intelligent message as well it's not just hardcoded but I'm just using this as a basic example and then what we want to do is listen for the next message from the user and so essentially all I'm going to do is bring in this Choice component

**[0:14:59]** right here here so this is going to listen for a trigger which is essentially just listening for the next intent which could either be none like just handle the conversation normally or trigger another tool and then I'm going to click on this crl c contrl v to copy

**[0:15:12]** it and drag the failure in here so if it fails to make the API call I'll say your message I'll just say your message failed to send in slack and then I'll just listen for another trigger here so now this workflow is complete and we are able already this like this is super

**[0:15:30]** simple setup we are already able to send a message in slack with this agent now all right so now what I can do to test it is I can click on run in the top right and what this is going to do is give me a debug version of the agent

**[0:15:43]** where it is going to tell me all of the intents all the decisions it makes and all the variables that it sets behind the scenes it's going to give me that information so I can make sure that it's making the right decisions and so first of all when I click Start it jumps to

**[0:15:55]** the start workflow that I showed you earlier where I added in that hello message you can see that right here and so now I'll say I need to send a slack message and this is going to instantly jump over because this is the debug view to that workflow where it recognizes and

**[0:16:09]** needs to send a slack message but again before it makes that call to my nend workflow it needs to know what I actually want to send in slack and so I'll say hi Cole I need help with autod Dev all right so this is my message I want to send and then it's immediately

**[0:16:25]** going to make that API request right here you'll see if it move on and then yep says your message was sent in slack all right so there we go so now we can go over into my slack Channel and there we go hi Cole I need help with autod Dev

**[0:16:38]** all right so it's working perfectly all right so the last big thing that we have to do with our voice blow agent is deploy it and like I mentioned at the start of the video doing that is really easily either as an embeddable chat widget on your site or through an API

**[0:16:51]** endpoint so you just have to click on the publish tab right here and publish your version of the agent and then go to the integration tab here and you have the code for the embed or an API key to use this as an API endpoint and there is

**[0:17:04]** a lot of documentation you can view on how to do that if you want I'm going to keep it really simple and just use the embed code right here so I'll copy this and then go to autod Dev this is my bolt. new Fork that I've covered a lot

**[0:17:15]** on my channel recently that we are building as a community and so I'm going to use this to create a front end basically by telling it just to make a vanilla JS and HTML app with this embed right here and I using my favorite open source model for coding which is deep SE

**[0:17:29]** coder version 2 the 236 billion parameter version I'm doing this through open router so it's not totally free cuz it's not running locally with AMA but it's going to be less than a penny to create this entire application for a rapper for my voice flow agent and so

**[0:17:45]** I'm going to do is pause and come back once this is built all right so like 15 seconds later and deep SE coder has now given us the HTML file for our voice flow agent interface here now there's not a preview for this cuz it's just a raw HTML file it's not served with Vite

**[0:18:00]** but that's totally okay because this doesn't actually work in bolt. new due to a cores issue with the voice flow Ed not going to get into that right now but it's all good because you want to take it out to deploy it anyway so I'm just going to copy this and go into an online

**[0:18:11]** HTML editor here with JS spidle so I'll paste in the HTML click run and then boom welcome to the chat widget I'll open this up and here we go we got our agent just like we saw within the platform itself and so I can say I want to send a slack message and just like

**[0:18:26]** before it's going to ask us what we want to send in slack but it's not debug mode now so we don't see all that intense stuff behind the scenes so this is working absolutely phenomenally and deploying as an API endpoint is pretty easy as well it is just so easy these

**[0:18:39]** days to build any AI agent that you want without code and still have all the control that you need now the AI agent that I built in this video was definitely basic and the N8 and workflow certainly trivial but I hope that you can see how you can take this example

**[0:18:54]** that I showed you here and extend it to work with any N8 and workflow or API endpoint for that m matter so you can build whatever agent you want integrating with any services that you need and so I would definitely recommend checking out voiceflow and just seeing what you can build with it if you

**[0:19:08]** appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
