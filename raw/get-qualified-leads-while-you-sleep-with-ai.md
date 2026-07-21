---
type: raw-transcript
title: "Get Qualified Leads While you Sleep with AI"
youtube_id: 1I0PvfHjaRE
url: https://www.youtube.com/watch?v=1I0PvfHjaRE
slug: get-qualified-leads-while-you-sleep-with-ai
published: 2024-10-11
duration: "0:18:38"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** a lot of people have a lot of ideas of ways to use AI but I'm going to be honest a lot of them are just a waste of time or straight up impractical one use case though that is tried and true and really necessary for any business is a

**[0:00:14]** lead generation agent that sits on your website and runs the front end of your business while you sleep I'm talking lead qualification answering any questions suggesting products or resources and collecting contact information for follow-ups this is a very common use of AI so there are a lot of platforms out there already for you

**[0:00:34]** to build these kind of Agents the problem is most of these platforms are straight up just not good so you might as well just build the agent yourself with something like NN or Lang chain instead they just aren't good enough and don't provide you the customizability that you really need however there are

**[0:00:51]** definitely some platforms out there that you're going to want to check out before you just go ahead and build a lead gen agent yourself I'm going to show you today an example of one of these platforms called chatlink I'll show you with catling how you can build a full

**[0:01:04]** lead generation agent suited to your needs that is going to be sitting on your website and qualifying your leads and answering any questions that they have with a rag knowledge base I am stoked to show you this when we go through it you'll really see what I mean

**[0:01:18]** when I say that building this kind of agent yourself is not trivial you can really use chatlink to build the perfect lead genen agent for your business so without further Ado let's dive in so to get started with chatlink all you have to to do is go to chat link. and then

**[0:01:32]** click on start for free there is a really generous free tier that they offer so you can build a couple of chat Bots and have dozens of conversations with them to really make sure that the lead gen agent you can build on the platform suits your needs but I'm pretty

**[0:01:45]** confident and will because I've been on this platform building a couple of Agents already and it has been working beautifully for me so once you are signed in you're going to be brought to a dashboard that looks like this they have a lot of resources here on the left

**[0:01:58]** hand side for you a couple of things I want to call out really quick is they have API documentations you can literally manage your agents and your knowledge bases and your conversations and everything through the API and they have a road map where you can see all the things that they are currently

**[0:02:11]** building for the platform suggestions that they're taking in and you can submit your own suggestions as well when you sign in and so this is a really evolving platform it's something important that I wanted to call out uh but we are here to actually build a lead gen agent so let's go ahead and do that

**[0:02:27]** now to create your agent within your project all you have to do is go to the top my agents Tab and then click on create chatbot and there are going to be three options that you are presented with here you can build an AI chatbot which is going to be more of like a

**[0:02:41]** basic chatbot that isn't necessarily geared towards lead generation a basic lead generation chatbot which is going to not leverage AI so just be more like standard questions that you would answer or you can have a lead generation plus AI chat bot that is going to actually have more of an intelligent interaction

**[0:02:57]** with the user as you are qualifying them and giving them any kind of recommendations and things like that you can also start from scratch if you want and so these are all just templates but I would honestly suggest going going with this template right here that's what I started with and it really helped

**[0:03:12]** me get a good understanding of catling very very quickly so that I could build my lead gen agent in just minutes and so I already have one built so I'm going to go reference this so that you can see in a much smoother way how I set everything

**[0:03:24]** up because if I built it from scratch it'll probably take a lot longer so I'm going to go ahead and click on this lead gen chat bot that I have already built and tested and I will go to the first tab that we want to care about here

**[0:03:35]** which is the Builder this is going to be your node workflow Builder kind of similar to something like vector shift or voice flow if you've heard of those platforms where you have a start to your workflow this is when the message first comes in and then you do everything that

**[0:03:49]** we see right here that I'll explain in a little bit that then leads to the very end of the workflow right here and that is when your chat within the widget actually ends and so this entire workflow represents an entire conversation and we have things like looping here to make it so that we can

**[0:04:05]** ask any number of questions to our agent um so that the users can get the answers that they need all right so before I start showing you the chat bot that I built I want to talk a little bit about how you actually build your workflows within chatlink so any kind of action

**[0:04:19]** you want to take or user input you want to handle an HTTP request you want to make for a custom agent anything that you want to do in catling you do it with the widgets that you have here on the left hand side so I'm going to start by

**[0:04:30]** going to the blocks here because this is where you perform all the actions that'll show in a little bit here um like sending a message a hardcode a message or getting an AI response or putting buttons on the widget for the user to click and so for example if I

**[0:04:45]** want to just send a hard-coded message at the start of a conversation I'll take the text block here drag it in and then drag the start to this new block and then I'll enter in something like hi there we go all right so I can save this bot now and then click on preview bot

**[0:04:59]** and then this conversation is going to begin right away with the bot saying hi nice and simple and so then I can go on to capture text as well so I can have this within the same block here so it'll say Hi and then wait for the user

**[0:05:12]** response and I can put that in a new variable um like I could say user response and then create a new variable and then I can use this later on in another node that I would connect for the second node here and so I could say something like an AI response I can drag

**[0:05:26]** this in right here and I can say that the question is um I can say user asked let's say user question or let me scroll down user response right here and then boom we now have our prompt for the AI so that is how you set up custom

**[0:05:41]** variables and how you connect the nodes together anything that you want to do you're going to do within the blocks here and there's so many things you can do here like HTTP requests or sending an email or doing conditions to handle different types of responses from users uh you can have buttons here um for

**[0:05:56]** things like when you want them to just say yes or no whatever that might be uh you can view all your variables on the left- hand side set your configuration for your AI like their knowledge based for the settings which includes what model you use there is so much

**[0:06:08]** customization here and things you can do you can set up your workflows to do essentially anything that you could want so starting right off the bat we have our greeting here and you'll see this in the template as well if you load it it really makes it clear how we have the

**[0:06:20]** different stages of our conversation within the greeting here we have this block where we display an image and then we have two different messages here so each one of the elements that you put with in one of these lighter gray boxes here is going to be a individual message

**[0:06:35]** that is sent in the chat widget to the user so first we send an image which I just have this blank right now but I'm just having this here to show that you can start off with an image like your logo or something like that and then we'll send a couple of greeting messages

**[0:06:47]** that come one at a time into the chat platform when the user first opens it up and then we ask them a question and so as an example for this lead gen chatbot I'm just going to be an AI Consulting agency so this is kind of the services I

**[0:07:01]** offer actually um where I have like you know solution development one-on-one Consulting pre-made agents all this good stuff and so we ask the user which one of these are you interested in and again this is just an example you can very easily see how you could fit this to

**[0:07:15]** your own needs and changing up all of the wording and the options here and so once they select one of these options and I'll show a demo of this in a little bit it's going to be fed into a variable so one thing that's really neat within chatlink is any of the inputs or out out

**[0:07:30]** puts from any of these widgets here can be put into a custom variable that you set up so in this case the user's choice is put into selected service name as a variable and then we're going to actually reference that and then prompt to the large language model in the next

**[0:07:45]** node and so we say the lead is interested in this service and then follow up with them with a couple of questions that will help us understand their needs more and so we prompt the user through a message and then we capture their output and we put that in

**[0:08:00]** the first question answer variable and so now we're going to use that in the next Noe as well so we're constantly capturing what the user says and including that in the next prompt so that our agent actually has context around what the user is saying so we can

**[0:08:12]** qualify them better and answer their questions better and so in the next prompt I'm just going to say here that um there kind of is conversation history so I don't necessarily have to include all this information here but I just want this to be nice and robust so I I

**[0:08:25]** again repeat the service that they're interested in and then I tell them what has happened the conversation so far like the user responded with this to your questions that you asked and now follow up with one more question so this is just an example of how you can have a

**[0:08:39]** little bit of a qualification process here where you have just a couple of questions that you want to ask the user to understand their needs more and again we'll capture their text and this time put it in a variable called second question answer and then we go on to a

**[0:08:53]** prompt here where we thank them for answering our questions so this is kind of the end of this little demo qualification process and now we want to ask them if they have any questions and so we throw that in the chat there and then instead of asking them for free

**[0:09:06]** form input we're going to have a couple of buttons here and like these are the kind of things that you can't just Implement in n8n really easily you can't just have these kind of like multi select options and all this looping and stuff within the n8n chat widget this is

**[0:09:20]** really something that is more robust that a platform like chatlink can provide you so the user will select here whether or not they have questions and if they don't have any questions then we'll go on to the part where we collect their contact information so we'll actually collect their name and email

**[0:09:33]** and that's going to be stored within a contact record in chatlink which is super cool um and then if they do actually have questions then we'll go to the next stage where we prompt them to ask a question and then we'll answer it based on our rag knowledge base and I'll

**[0:09:47]** show that in a little bit as well and so we'll answer their question and then loop back and ask if they have a question again so you can repeat this process over and over to make sure that you answer all the questions that this lead has so that there're are qualified

**[0:10:00]** and now they're happy with their answers and you've got yourself a good lead and then finally they'll select no at some point and then we'll collect their contact information and say thanks include their name and then you'll get back to them soon or whatever that this message is all this is very very

**[0:10:14]** customizable this is just a simple demo that I built for you to understand the robustness of catling and so I'll click save and I'll demo this in a little bit here but I want to quickly show the knowledge base and some of the customizations for the appearance as

**[0:10:27]** well and so going on to the next tab here for the knowledge base it is really really neat because there are a few different resources that you can use that you can ingest for your rag so the first thing is you can just give it a link which is super cool so if I click

**[0:10:42]** on new data source in the top right here I can give it a website link so it'll crawl the website and take all this information add it to its knowledge base U you can also do a Sit map which is really really good for something like an e-commerce store because it could

**[0:10:54]** literally go through all the URLs for your different products and understand every single one of them to answer questions about any of your products really really powerful you can also do a custom URL list up to 2,000 links you can include for rag you can upload documents you can include just raw text

**[0:11:11]** if you just want to free form whatever you want to be in the knowledge and then what I did here is I had a list of FAQs and so I just have a question answer repeated many many times to answer common questions about my AI consulting services so I can kind of just show you

**[0:11:24]** that really quick my knowledge base right here it's just really basic I have three FAQs I just answer a few common questions and this works really really well like when someone asks you know something related to what um is entailed within my one-on-one Consulting sessions the answer will match this very very

**[0:11:41]** well um so I've been really impressed um and then the last thing I want to show before we demo this is the appearance there are so many things that you can do to customize your chat widget to actually match your branding and that is super important and something that is

**[0:11:53]** missing from building these widgets within n8n or other platforms where you can build these kind of Le gen agents and so yeah it's really cool all of the options you can have for styling and you know like changing the image that you see for the person for the AI um so yeah

**[0:12:08]** I just love that um and then you can also see all the conversations that are happening with your Bot right here um which is really cool it'll even tie it to the user we can have like their email and phone and all that saved and so it's almost like a CRM where all the people

**[0:12:20]** that come in and fill out the form and interact with your agent are available to you to then follow up with when they put in their contact information like I showed at the end of my workflow which is so so cool um and then what we can now do is actually embed this into our

**[0:12:34]** website and the way that we do that is with the website widget integration it also integrates with zapier if you use that I really wish they had n8n as well but you could integrate with zapier for when they fill out contact information but for embedding this on your website

**[0:12:48]** there are three different options you can have a floating chat where it's like that little widget in the bottom right that someone clicks on very common on websites or you can have it inline or full screen so it's actually a part of your web page at self and not just a

**[0:13:00]** floating widget um and so for my example right here I'm actually going to just show the floating chat because that's really the most common so you just click on this option right here and then you take the script tag that you can embed into really any website builder so they

**[0:13:13]** have a couple of different integration guides for things like Shopify or WordPress or Wix um but really you could do this with go high level you could have this in a custom nextjs site just anywhere you can embed this kind of script tag here and so I'm going to copy

**[0:13:26]** this and then I'm going to go into an online h HTML editor CU I'm just going to show you that you can literally do it anywhere by just doing it in an online HTML editor because if I can show you you can do it here hopefully that'll prove that you can do it literally

**[0:13:39]** anywhere so I'm going to paste in this script code right here run it um and then sure enough I got this chat widget now that I have in the right side all right so I moved myself over to the left so that we can see this whole chat here

**[0:13:52]** so like I showed it earlier in the workflow it starts with these specific messages that are sent out to the user and then it asks a question where we click on one of those buttons to say which service we are interested in so I'm going to say I'm interested in

**[0:14:04]** one-on-one Consulting sessions and then it's going to go to my model which I selected GPT 40 mini in this case I'll actually show that really quick here um just so you can see where to set that so if I go into the Builder here and I click on the settings and go to the um

**[0:14:20]** settings for my AI my model is gbt 4 mini and you can even set the model individually Within These specific nodes or just use the global which would be set to what I had here which is GPT 40 mini and so going back to the the chat here it generates a couple of questions

**[0:14:38]** just like I told it to and so I can give some answers so I'm going to pause and come back when I have these answers all right so nice and simple I just said I am looking to build a sales agent that qualifies my leads and has knowledge of

**[0:14:48]** my products I have an e-commerce business selling Sports clothing so I'm going to give the answers here and it's now going to follow up with one last question because that's exactly what I set up in my workflow so there we go thank you for sharing one more question

**[0:15:00]** what are the specific criteria questions that you want your sales agent to use when qualifying leads it's honestly a really good question and you can leave this up to AI to generate or you could be more specific in the prompt for what kinds of questions the power is in your

**[0:15:13]** hands with the chatlink here so I'm going to pause and come back again when I've typed out my answer here all right so I typed out just some kind of random here I just say I want to know uh what the lead is interested in buying and what sports they play and so this is the

**[0:15:25]** last question that my agent will ask and then it's going to ask me if I have any questions so there we go thank you for answering my questions you have any others so right now I'll say yes I do and um I'm just going to ask a question

**[0:15:35]** that I know needs to be answered through the rag knowledge base and so what questions you have for me I'll say what is involved in the one onone sessions all right so now it should pretty much take what I have in the FAQ because the question pretty much matches exactly

**[0:15:51]** with what we have in Rag and sure enough it is a Consulting session it is a hour long focuses on questions you have about integrating AI in your business business if you're interested in having multiple sessions we'll dive into specific AI Solutions you are building this is exactly right and it doesn't just do it

**[0:16:06]** word for word either it really customizes it to the conversation but this has exactly the information that I put in uh for rag there so this is awesome so I'll say I don't have any more questions so I'll say no here and then now it'll say perfect we'll be in

**[0:16:18]** touch and it just wants a name and email so I'll say my name is kadine my email is col yahoo.com all right boom boom and there we go I will get back to you soon all right and that is the end of the chat that works so so good and so I'll

**[0:16:32]** even go back into here we'll check out this conversation that we just had so you can see here we go this is exactly what we had one-onone Consulting sessions the sales agent for qualifying leads all right all right looking good and we also have their contact information so it's kind of like a CRM

**[0:16:48]** here um yeah it's just working so so well and one thing that I want to call out let me go back to the workflow here this is just like the last Golden Nugget that I want to give you is when you're creating these pipelines here it is so

**[0:16:59]** so easy to customize things as much as you could possibly need when you go into the blocks here you can send messages you can send images as a message or audio um and you can have like conditions here if statements that will send different things based on responses

**[0:17:13]** you can even have an HTTP request and so you can include your like headers and body so if you have like API keys or query parameters you can hook into any API you could possibly need so if you have some custom agent that's hosted with like n8n or Lang serve you could

**[0:17:28]** interact with that as a part of this workflow and it can be like a specific part of the conversation too so like literally any customizations that you would need you were able to do it with something like an HTTP request and there's just yeah so many options here

**[0:17:41]** um there's even like zenes Integrations it's so so cool um and you have like all the variables that you can manage here on the Le hand side as well so it's just super super robust any kind of agent that you'd want to build for lead generation you can do it in chatlink I

**[0:17:55]** truly hope that at this point you can see the usefulness of using a platform like chat bling to build powerful and customizable agents for your website for lead generation this is especially useful if you run a sort of business like an e-commerce store an agency or a Consulting business you're a busy person

**[0:18:12]** and you don't have the time to build this kind of robust agent for lead generation and so it makes sense to use a platform like chatlink on top of this you don't really lose on any customizability and it's not like You' need the solution to be local anyway

**[0:18:25]** because this kind of front-facing chatbot is not going to have any private data so if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
