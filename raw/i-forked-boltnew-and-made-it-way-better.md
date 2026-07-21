---
type: raw-transcript
title: "I Forked Bolt.new and Made it WAY Better"
youtube_id: 3PFcAu_oU80
url: https://www.youtube.com/watch?v=3PFcAu_oU80
slug: i-forked-boltnew-and-made-it-way-better
published: 2024-10-13
duration: "0:19:30"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** if you are interested in Ai and you haven't heard of bolt. new at this point I hate to break it to you but you are probably living under a rock bolt. new is a really powerful and open source llm web development platform where you can create and deploy full stack

**[0:00:14]** applications right in the browser with the help of AI and it is a game Cher significantly better than just using CLA or vzer or other similar tools and in my experience the amount that bolt. new speeds up my full stack development is truly unmatched and don't get me wrong

**[0:00:30]** it is far from perfect I'm not going to try to say that you don't have to be good at coding anymore to make something that is truly production ready but it is a fantastic coding assistant that will get you started with anything that you want to make however there are two big

**[0:00:45]** problems that I have with bolt. new first of all you have a limited usage of the platform just like you would with something like Claud or vzer it is the worst when you're in the middle of coding an app with AI and you're forced to just stop second with bolt. new you

**[0:00:59]** don't get to pick the llm that you use it is always clae 3.5 Sonet and don't get me wrong clae 3.5 Sonet is a fantastic llm but what if I want to use GPT or what if I want to use a local llm that is fine-tuned for coding so I pay

**[0:01:14]** literally nothing you can see that it is not always ideal to use the exact same model every time no matter how good that model is I have great news though because I have fixed both of these problems by forking bolt. new running it locally on my computer and extending the

**[0:01:30]** platform so I'm not just limited to one llm anymore and I am super excited about what I've been able to do with this already so allow me to show you what I did and show you how you can do exactly the same thing okay so before I show you

**[0:01:44]** what I built and unveil it to you I want to show you bolt. new very very briefly and then talk about how because it's open source I'm able to Fork it and change it myself so here we are in the website bolt. new and you just prompt the AI with whatever you want to build

**[0:01:59]** or you can select one of these um pre-selected options right here so I can just select one of these and it's going to go ahead and give me all of the chat output on the left side and then on the right side it's going to give me the

**[0:02:11]** entire full stack project all the code and I can preview it as well once it is done writing everything so this is the standard UI for bolt and how you're able to build full stack apps really really easily and any kind of things that you need to correct um you just do that on

**[0:02:25]** the left side here just kind of like you would in a chat widget with something like Claud or v0 so is a very beautiful platform easy to use really powerful and it is also open source so going to the GitHub right here you can download all of the code for bolt. new and run it on

**[0:02:40]** your own computer and that's what I'm going to do here but on top of that what makes it even better is you can extend this application because you have access to all the source code and so there's a really nice read me here for you to check out in this GitHub repo I'll link

**[0:02:53]** this in the description so you can check this out and then also they have a page if you click right here on how to clone this yourself and run it on your computer so these are the instructions that I followed and I'm going to have something similar in my own repo for my

**[0:03:07]** forked version of bolt that I will also have Linked In the description of this video so everything that I am about to unveil to you here I have available for you in my GitHub to download so that you can overcome the problems that I talked about at the start of this video all

**[0:03:21]** right so let's take a look at what bolt. new actually looks like when you download it yourself and run it so when you pull the git repo follow all the instructions to run bolt. new yourself you're going to have a UI that looks like this it's a little bit different

**[0:03:34]** than what we see on the actual bolt. new website because they've touched up some things to make their UI look better but you're going to have the exact same functionality here so take a look at this andrain this in your brain because this is the default open source version

**[0:03:47]** of bolt. new now I'm going to go over to the version that I have built right now all right you see the difference there let me go back and then I'm going to go back to my version there is one simple difference but it makes all the world a

**[0:04:00]** difference for how robust this application is and if you didn't catch it it's the fact that we have this drop down here where we can select the large language model that we want to use to work with bolt. new a bunch of different models here from anthropic open AI Gro

**[0:04:16]** and I have Integrations with olama for a bunch of different models that are specifically for coding like quen 2.5 coder the Deep seat coder find code llama regular code llama so many different models literally any local model that you can run with ol Lama you can have in this platform now and when I

**[0:04:33]** go over my code changes for this I'll show you how you can do that as well and it is just so so awesome so if I don't want to use the default Cloud 3.5 Sonet I can select gbt 40 and I can you know just select one of these pre-built

**[0:04:46]** options here to build an app for me and so yeah like you can see right here it looks pretty much exactly the same as the actual bolt. new website but this is indeed running local host so it is on my computer and so it's entirely private to me obviously besides sending my data to

**[0:05:01]** GPT right now but I can switch that to a local model and I'll show that in a little bit as well and so yeah it's all really nice and fast and working perfectly we built this to-do uh app really really easily so I'll say test and test two all right looking good nice

**[0:05:16]** yeah so it gives me the preview we have all the code here and this is looking really really nice and another really neat feature within this that I built is that I can change my model at any point and so in the very next message I can say oh I actually want to use quen 2 .5

**[0:05:30]** Cod or 7B as well and as long as I have oama running with this model already installed I can go ahead and use quen 2.5 Cod or B one thing I will say is that the weaker models that are you know smaller like 7even billion parameters they don't seem to always work the best

**[0:05:46]** with the web container sometimes when you tell it to start a project it won't even spin up the web container um so sometimes you will encounter weird things like that where it does make sense to just use the larger models but you can still get some really really

**[0:05:59]** good results with the tiny and mighty models like quen 2.5 Cod or 7B so I can even like kind of just have like a followup here and say uh make this to-do app with just HTML CSS um and JS and so I'm going to use this model running right now on my

**[0:06:15]** computer it's only 7 billion parameters compared to the you know hundreds of times more for GPT 40 and yep got my fans wor in so it's going ahead and it's uh yeah making this app so sometimes it'll operate well within the web container sometimes won't but it is

**[0:06:31]** still really really cool yeah it looks like it is so yeah creating the index.html and it'll go through and create each one of these files here and then hopefully be able to see it in the preview all right here we go it took a little bit because I am running this

**[0:06:42]** model locally but it created the HTML CSS and JavaScript files and put them in my web container here now the preview looks a little bit Jank so you can definitely tell that this is a 7 billion parameter model that's doing everything here because the prompts behind the scenes for bolt. new are actually

**[0:06:59]** massive which is why some of these smaller models can't handle it as well um so yeah I mean like it it doesn't really work but what I can do is I can take the HTML I'll copy this I'll go into this JS fiddle that I have here uh

**[0:07:12]** then I will take my script my JavaScript and then I will take my Styles as well and we'll see if this works within a JS fiddle and boom it does all right so I got a task here and I can mark it as complete so this is actually even better

**[0:07:25]** than what GPT made in the web container which is super cool yeah look at this this all right like it's a little unfortunate that the smaller model doesn't work as well within the web container bolt. new but it is just amazing that I'm able to use a model

**[0:07:38]** locally to build this kind of thing that's actually working really well so this is so so awesome um and then yeah like I said I could literally switch to another model for the next chat here so I have a bunch from GPT bunch of options from anthropic we have a bunch of grock

**[0:07:53]** models here if you wanted to use like llama 3.1 or 3.2 and then all of these olama models that are local for coding specifically um and there are some really really powerful ones here like deep seat coder 236b if you have a machine that can actually run this you

**[0:08:09]** could probably get better results with this model than using Cloud 3.5 Sonic with the bass bolt. new and not even to mention that you can fine-tune these models as well there's just so many possibilities that open up when you aren't limited to using Cloud 3.5 Sonet and that's why I'm so stoked about

**[0:08:25]** having all this available to me in this local forked version of bolt. new and so yeah I think that's pretty much all that I want to showcase here now I also want to really quickly show you how I actually made this possible and how you can run this yourself because all of

**[0:08:40]** this code in my Fork version is in a link to the description of my video and so you can very easily just download this and run it yourself and if you're using a local model with oama you're going to pay for nothing have unlimited credits and have a lot of power right on

**[0:08:53]** your computer so here we are in my visual studio code with my forked repo up and when you visit the link in the description of this video to my version of bolt. new you'll have the remme right here which is going to have all the instructions for you to download this

**[0:09:08]** and run it yourself and so let me scroll down to that section right here I have the prerequisites listed just like the bolt. new readme has listed and then these instructions I'll have to update a little bit once I actually have this repo published but you'll clone the URL

**[0:09:22]** that's custom to my Fork version and then you'll install all the packages and then you will open your EnV example file and set each of your environment variables here for your different API Keys now note that you only have to set these API keys if you want to use these

**[0:09:41]** models specifically so if you're only looking to use GPT or Gro you could just set those keys um so there's some flexibility there as well and then for old llama since it's going to be running locally on your computer you don't have to set any API key there obviously

**[0:09:53]** because you're going to just directly connect to AMA running on your Local Host um and so that's all you have to do and then pretty much you just run the pnpm Run Dev command and you'll have your version of bolt. new with all the llms available to you running on your

**[0:10:08]** computer just like that the last thing that I will say here is that you're going to need the Google Chrome Canary browser to run this um which isn't really a big deal it's a very easy to install browser just like Chrome is and it's a good web development browser to

**[0:10:21]** have anyway and so you'll have that up and running you set all your environment variables here you'll be good to go and you're going to have the exact same UI that I just showed you where you're able to select your model and then interact with bolt to create your full stack

**[0:10:34]** applications now I also want to spend some time and quickly show you how I was able to change bolt. new in this way I think it's a really cool lesson for you to see how you can change applications when you Fork them and also it's nice to know how you could extend this to use

**[0:10:49]** other models or even entirely different providers if you want to use a different service for your llms and so let's go ahead and dive right into that and so first of all this structure of this repo right here it's a very standard front-end structure so if you are

**[0:11:02]** familiar with frontend application development with like nextjs or view react whatever it might be this should look pretty standard to you the first file that I want to call out is this constants file that is in the utils folder because this is where I have defined the default model which I'm

**[0:11:17]** keeping to the exact same as the regular bolt. new model quad 3.5 Sonic default providers obviously anthropic and then I have this big list of models here and this is where I Define everything that is available in that dropdown that I showed you earlier for all the models

**[0:11:33]** that we can use to generate our full stack apps and so each one of the items in this list is just an object where we have the name of the model that's the actual model ID that the respective uh API needs to know what model you're referring to then we have the label what

**[0:11:48]** we display in the drop-down and then the provider and this is important because that determines which API key the backend will actually fetch to invoke a request to this llm so it is so so easy to add add new models to this setup here because if there's a new model from

**[0:12:02]** olama for example that I want to add I just copy one of the records already here I specify the the new model ID from AMA and then give it a new label and that is everything I have to do to add a new model obviously for olama you need

**[0:12:16]** to install AMA and pull the new model but that is also very easy to do you just go to ama.com click on download and then they have their repository of models here in their Library where you can search for any model that you'd want to download and then they have the

**[0:12:29]** command for you to run in your terminal to pull that model as well so once You' run this have it on your computer it is instantly available for you to now use in this forked version of bolt. new really really nice one thing I will say though for a lot of these smaller models

**[0:12:44]** some of them just don't work very well with bolt. new so a lot of this is experimental I haven't tested every single one of these models with bolt. new um but just know that like because of context limitations and weaker models not being able to handle as much context

**[0:12:58]** sometimes you do have to play with this a little bit to see which models work the best for you but a lot of these olama local models that are fine-tuned for coding are very very powerful and there's all these options from like Gro anthropic and open AI as well and then

**[0:13:11]** if you want to add a whole new provider like something like fireworks or together AI I'll show how to do that in a little bit as well that is everything for the models and how you can extend that I spent a little bit of extra time on that just because this is probably

**[0:13:22]** the most important part of something that you would actually be the most likely to change once you pull everything that I have for you here okay so moving moving on the rest of this is going to be a little bit more Technical and I'm just going over this very

**[0:13:34]** quickly in case you are curious under the hood how I made all this happen and so there's a few different components that I had to modify here and some things in the back end and so go through these each one at a time and I'm not going to explain everything in a lot of

**[0:13:47]** detail but there's a lot of work that I put in behind the scenes to make this work so I'm just going to show it at a very high level so first of all in the main chat component that we have in the front end here there was no concept of a

**[0:13:58]** model in the front end at all because it was all hardcoded in the back end before so I had to add a new state that represents the model and this is what is updated when you select a new model in the dropdown and then to actually pass this model into the back end it's not as

**[0:14:13]** easy as adding a new parameter to the API call that streams the response from the llm because it is using the used chat Hook from the AI SDK from versel and it's not super easy to customize that to add a new parameter so what I actually had to do this took a lot of

**[0:14:30]** work to figure this out I had to add the model into the content of the message from the user itself and then obviously I remove that when I give it to the llm and display it in the front end I'll show that in a little bit as well um but

**[0:14:44]** I use this to give it to the API so it can extract the model and know which API key to get and which model to set up and you can see here that um bolt. new actually did something similar for specifically having file modifications pass to the back end so it's something

**[0:15:01]** that they did and I did something just kind of similar to that for the model itself and then in the base track component um this is where I Loop over the model list and create this drop down here with all the options that we see right above our chat widget and then in

**[0:15:16]** the user message component this is where I replace based on Rex the model with an empty string to remove that so that we don't actually see the model in the user messages in the front end so that is everything for the front end now we have our API endpoint which we hit whenever

**[0:15:33]** we want to get a response from the llm I didn't really have to change anything here I'm just showing that this is kind of the whole entry point to the back end because of what it does at kind of the bottom here is it calls this stream text

**[0:15:45]** function this is what does most of the work to actually get the response from the large language model and that is this function in the Stream text. TS file right here and so right when we get into this function this is where I Loop over the messages is and I extract the

**[0:16:01]** latest model that was specified from the user in the dropdown so I extract the model this is also how we can change the model in the middle of a conversation and I also sanitize these messages so that the model for every user message is obviously not going to be included in

**[0:16:17]** the prompt to the large language model because that would just kind of confuse the llm if the user is giving a model ID for every one of their messages and so that's how we do that now there's just a couple of other things to cover right here first of all when we get the model

**[0:16:32]** the model that we retrieve is going to be based on the provider and also the model ID so this get model function is right here and first of all what we need to do is we need to get the API key based on our environment and the provider and so that is done in this API

**[0:16:48]** key typescript file right here and it's just a simple switch statement so based on the provider if it's anthropic we get the anthropic API key open a the openai API key grock goes to grock and and then the default would be nothing so if we're using oama for example we don't need an

**[0:17:02]** API key so we just return an empty string so that is how we get the API key based on the provider and then we have separate functions here to actually get the model instance based on the provider as well so another switch statement based on the provider we pass in the API

**[0:17:18]** key and the specific model and then we have a function here that is going to use a different Provider from each of this is all from the ver cell AI SDK and so each of these functions is going to work with a specific provider to get any model that you can get based on a Model

**[0:17:35]** ID with that provider specifically and so if you want to extend this platform to use another provider like together AI or fireworks whatever it is you can do that very easily as long as that provider is a package that you can install from the versell AI SDK so I'll

**[0:17:52]** go back to my browser and show you that really quickly here there's some nice documentation that I have up here to show you within the AI SDK docs that talks about the different providers that are supported in the versel AI SDK so all these ones are supported and then it

**[0:18:07]** also says you can use the open AI Provider by uh changing the API key like I did for grock to use grock perplexity or fireworks and there are also open-source providers that are created for olama for example and that's actually what I use so these are all of

**[0:18:22]** the providers that are available to you and if you want to add one of these you just add a new function you'd have to add a new API key in the environment variable file and add a new place to this switch statement as well as this switch statement so it's a little bit

**[0:18:34]** more technical here it's obviously a lot easier to add models to this whole setup for existing providers but I want to get technical here for those of you who care about that and so that that's why I did that here but that is really everything that I had to change so a good amount of

**[0:18:49]** stuff in both the back end and the front end took me a good amount of time so I really hope that you can find a lot of value in this and use it to create some really awesome things for full stack app running locally on your computer I hope

**[0:19:01]** that I truly built something that you'll actually want to use to boost your productivity while coding with llms all the while paying literally nothing if you use local llms and getting to use any model that you could possibly dream of let me know in the comments which local LMS you want me to test out with

**[0:19:16]** bolt. new because I definitely going to create some follow-up content around that in the near future if you appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
