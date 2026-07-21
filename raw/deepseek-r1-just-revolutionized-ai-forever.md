---
type: raw-transcript
title: "DeepSeek R1 Just Revolutionized AI Forever"
youtube_id: -GmEIqi0yNE
url: https://www.youtube.com/watch?v=-GmEIqi0yNE
slug: deepseek-r1-just-revolutionized-ai-forever
published: 2025-01-22
duration: "0:21:08"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** one of the hottest things with AI right now is reasoning models these are llms that are able to think to themselves before giving a final answer to the user and you get some insane results with this kind of setup there are a lot of reasoning llms already out there like 01

**[0:00:16]** and 03 from open Ai and qwq and open source version from quen and now deep seek is getting in on this game they have just released an incredible new open-source reasoning llm called R1 and they have a bunch of different versions so you can actually go and run a

**[0:00:34]** variation yourself or get something that is literally more powerful than open AI 01 Claude 3.5 son it basically every llm out there there's so much hype about this model right now so I had to go and check it out myself I was actually planning on making a different video for

**[0:00:50]** today but I tried on R1 I'm now bought into the hype and I'm going to show you exactly why that's the case and this isn't just going to be another video like other YouTubers out there I'm going to talk about how you can run R1 yourself and we're going to use it in

**[0:01:04]** bolt. DIY which is our open source AI coding assistant to show the power of it making an incredible app really really fast so let's dive right into it so here we are in the official blog release for deep seeks R1 here on their website and I'm going to quickly cover this just to

**[0:01:21]** talk about the benchmarks and the pricing and then we will dive into how to run deep seek R1 yourself and test it out as an AI coding assistant with bolt. DIY so first of all we see immediately that this is a fully open source model and it is MIT licens so you can use this

**[0:01:38]** commercially completely freely which is just absolutely incredible and it is a thinking model so in this diagram that we see right here or kind of just this example from their chat platform you can see that it thinks through its response before it gives us the final answer and

**[0:01:54]** you can go and play with this right now you can go to chat. deep seek.com and have a chat gbt like interface playing around with R1 so I'll have a link to this as well as all the other resources I'm covering here in the description but yeah you just go to their chat platform

**[0:02:08]** enable deep think and then when you ask it a question you'll see here that this kind of grade out text right here is it thinking to itself before it then gives us the final answer in more bolded text that we'll see in just a second here and this kind of reasoning approach always

**[0:02:23]** gives better answers maybe not always but almost always give better answers and that's why we're seeing so much hype right now around models like 1 03 qwq and now R1 but R1 honestly it seems to be performing better than all of those other reasoning models and then also any

**[0:02:39]** regular llm as well so absolutely fantastic and yeah we can look at the benchmarks right here so take this with a grain of salt because benchmarks aren't always the most trustworthy and this is provided right here on the Deep seek blog so they obviously have a reason to be a bit biased but just take

**[0:02:55]** a look at how incredible this is and we'll also see later on that it's very much backed up when we we test it with bolt. DIY but yeah I'll zoom in here so you can get the full picture very clearly We've Got Deep seek R1 on the Le

**[0:03:06]** hand side here and then it's being compared to 01 01 mini and their original best model which was deep seek V3 and just look at the performance here it performs as well sometimes better sometimes a little bit worse than 01 in every Benchmark absolutely incredible because it is a smaller model it's open

**[0:03:27]** source and they've got versions you can run yourself and it is way cheaper so it's just so cool to see how insanely powerful it is so yeah let me get out of this and I'll go back over to the blog here cuz the other thing that is extremely cool with R1 this is what

**[0:03:42]** actually makes it so you can run the model yourself is they took their competitors let me zoom in on this little bit here this is just is so cool they took their competitors quen and llama and they made smaller versions of R1 based on those models so they're

**[0:03:57]** basically fine-tuned added in all the R1 reasoning to these models like quen and llama so you can download these yourself on oama hugging face I'll show you how to do that in a bit so you have all the power of this insane reasoning model right on your computer and the coolest

**[0:04:12]** thing is even their 14 billion parameter model right here their quen version is on par with 01 mini which is incredible because a 14 billion parameter model is generally pretty underwhelming when it's not this one and usually it's not even close to something like 01 mini and this

**[0:04:31]** kind of model almost anyone can run on their computer 14 billion parameters it's of course a lot in the grand scheme of things but relative to so many other models that we see um like you know Llama 70b Or Claude Haiku or Claude Sonet those models are so much bigger so

**[0:04:48]** this is just incredibly cool and the other thing to note is that if we go down to the pricing rate here just look at how cheap this is 55 cents for every million input tokens and then $219 for every million output tokens and if those numbers don't mean a ton to you just

**[0:05:03]** look at this graph right here the numbers cannot lie the benchmarks could be a bit biased I'm going to give at that of course but with the pricing here I mean this is very clear-cut it is just so much cheaper to use R1 compared to even 01 mini but then also it has as

**[0:05:18]** good a performance as 01 and it is dozens and dozens of times cheaper just absolutely incredible and then compared to other models like Claude 3.5 Sonet it is still cheaper than those even $3 for every million um input tokens here so such an affordable model absolutely incredible and I show CLA 3.5 Sonet here

**[0:05:38]** um just because we're going to be comparing R1 to this model as a coding assistant in a bit I'll also have a link in the description to this Benchmark this is one that I haven't seen thrown around on YouTube or the rest of the internet as much but this is also a very

**[0:05:51]** cool Benchmark just going into a bit more detail than the other one on the Deep seek blog so absolutely phenomenal all right so let's talk about the different versions of deep seek R1 and how you can run most of them on your own computer so we're here right now in the

**[0:06:06]** olama page for deep seek R1 this is one of the platforms where we can run these models ourselves and I'll show hugging face in a little bit as well so to install olama you just go to their homepage here ama.com super easy to install for any operating system and

**[0:06:20]** then you can instantly within a terminal like I'll show in a little bit run any of these models that we're going to be talking about right here so when you go to the Deep seek R1 page you can see the tag here for all the different versions of this model it comes in so many

**[0:06:34]** different sizes and the biggest one here the 671 billion parameter version this is the most powerful one that you're going to be using if you're going through the Deep seek or open router API and it is a whopping 400 GB super super big and this is a Q4 quantization so

**[0:06:52]** it's not even the biggest version of this model that you could download but even with this 400 GB version of this size here it's still way too big to run on your computer unless you're investing tens or hundreds of thousands into your setup so generally you want to go with

**[0:07:08]** some of these smaller versions but like we saw even the 14 billion parameter version which almost anybody could run on their computer is on par with 01 mini it is absolutely insane the kind of power that we can get and we can download it and run it right here

**[0:07:22]** through AMA and if you scroll down in the AMA page you can see for all the different sizes of these models what they are based based on so like for the 1.5 billion parameter it's based on quen for the 8 billion it's based on llama we see quen for most of them and then llama

**[0:07:37]** for the 70 billion as well then they got the benchmarks just like we seeing in the blog post and so what I can do right here if I want to run the 14 billion parameter version download it on my computer I just select that like I already have selected right here and

**[0:07:50]** then I copy this command and then assuming I already have Ama installed I just have to go into a terminal paste this command and it'll install it if I'm running this for the first time otherwise it sends me right into the chat right here so I can ask it a

**[0:08:02]** question like make me a fast API endpoint just something super generic here cuz I just want to show what the output looks like so it's going to have this thinking tag at the start so everything that we see here until the ending thinking tag is not what it's

**[0:08:18]** producing as a final response to the user this is just it thinking to itself so if you're building an AI agent where you only want to display the final output for example you would just take the output from the llm and then remove everything that is Within These thinking

**[0:08:32]** tags so you can see this is the end tag right here and then everything that we get after that is the final response from the user so it's very similar to what we saw on the Deep seek chat platform also very similar to what you'll see with other reasoning models

**[0:08:44]** like 01 or qwq so that's running it on AMA it was that easy to bring it onto my computer and now I could use this model right within bolt. DIY which we're going to be using later to test R1 as an AI coding assistant you can also install

**[0:09:00]** through hugging face as well I know a lot of people love olama but then a lot of other people like using other platforms like LM studio and llama CPP as well and you can do all that through hugging face and it actually wasn't the most intuitive for me to find how I

**[0:09:14]** could install it for LM studio and llama CPP uh through hugging face here so I wanted to show you that really quick so if you go to the main R1 page in hugging face which I'll have Linked In the description and you scroll down a little bit here you'll see all the different

**[0:09:28]** distilled versions that we just saw in ama right here and so I can click on the download link to bring me to this page in hugging face so let me do that and then before I even click on use this model you can see right here that for

**[0:09:41]** local apps there's only VM what I can do is click on quantizations there's 43 models available here and then the one that I'd recommend selecting here is the one from UNS sloth doesn't really matter a ton you could use the LM Studio One as well um but I'll just click on this one right

**[0:09:57]** here so it's the version of quen 14 billion parameter the one that I just installed with AMA I'll click on this and then now if I click on use this model boom there we go we instantly have access to install it for LM studio and llama CPP as well and you're going to

**[0:10:12]** have a very similar process to installing it for old llama just like we saw right here uh running it in the terminal so that's how you install it through hugging face as well that can also work with bolt. DIY uh but now it is time to test this out in bolt. DIY so

**[0:10:28]** I'm going to take the most powerful version of the model the 671 billion parameter through the Deep seek API you could also use open router and I'm going to build a relatively complex app with this to show how powerful it is and show that it actually kicks clae 3.5 Sonet in

**[0:10:45]** the butt so we're going to build the same thing with CLA 3.5 Sonet as well and just see that the Deep seek Reasoner is actually a good amount better it's so cool all right so at this point we've talked a lot about R1 without actually showing how powerful it is and that's

**[0:10:58]** what I'm going to do right now with a simple demonstration in bolt. DIY so this is our open-source AI coding assistant that is based on bolt. new so it's essentially the open source version of bolt. new and you can use pretty much any large language model you could

**[0:11:13]** possibly want so I can even go through AMA and I can use all of the models that I downloaded including my distilled versions of R1 that I just showed downloading through hugging face and olama but in this case because I want to use the most powerful version of R1 I'm

**[0:11:29]** going to be going right through the Deep seek API and what we're going to be building today is a chat interface to work with an n8n AI agent that I have built right here for my automator live agent studio so this is kind of a base agent just a super simple example here

**[0:11:45]** of an agent that I can hit through an API endpoint and we're going to with a single prompt I'm going to oneshot this pretty much just build a full front end for us to have conversation and chat history management talking to that API endpoint in n8n and and we're going to

**[0:12:00]** be comparing it to Cloud 3.5 Sona as well just so you can see how well R1 does and then how much even other really good llms like Sonet can fall apart when we have more complex requests for apps like this so this chat app that I'm going to build right here with R1 I

**[0:12:17]** actually built something very similar in one of the previous videos on my channel using lovable so generally when you use a platform like lovable or bolt. new you get a bit better performance than using bolt. DIY because they are optimizing for a single llm which is Claude 3.5

**[0:12:34]** Sonet and Sonet is usually the king of AI coding and so I created this app that works really really well and it has all the Integrations with superbase that I'll show a little bit when I show you the full prompt that we're going to be using here um but it doesn't look the

**[0:12:47]** best honestly like it has all the functionality here I can send messages and I can go through the conversation history um but it doesn't look the best I mean you can't even distinguish between my messages and the messages from the agent um the toggle doesn't really look the best here and it just

**[0:13:02]** leaves kind of a blank bar like things don't look the best and so what we're about to build with R1 is going to look even better than what we can build with lovable and I've never really been able to truly say that with bolt. DIY but this is the first time that we have a

**[0:13:16]** model so impressive with R1 that I can actually say that with confidence and so this prompt right here this is what we're going to be using to build our chat interface to work with our n8n agent so I'll have a link to this in the description of the video it's very

**[0:13:30]** similar to The Prompt we used in my last video to build what we just saw with lovable the only things that I changed a little bit is the URL because I'm using an n8n agent instead before I was using something that I had running locally with python but the rest of it is

**[0:13:43]** generally the same so I'm telling it how to work with the API for the N agent I'm giving it my superbase public credential and the project URL so never ever give sensitive information to an llm this is my public key in superbas so that's why I'm able to show it here and feed it

**[0:14:00]** into the llm and then I'm telling it how to understand the conversations through the messages table and then also giving it some features that I want so I go into this prompt a lot more depth in my other video but right here I'm just showing you very quickly what I have

**[0:14:13]** building something that's actually reasonably complex like this is something that a lot of llms are going to completely fall apart making but R1 is going to kick it in the butt and then even saying here at the end that I want super base authentication so I took all

**[0:14:26]** this right here I'm just going to copy this and then I'm going to go into my bolt. DIY full screen it again paste this in I'm going to take out the header at the top here and I'm just going to use this right away for my prompt so

**[0:14:37]** this is going through deep seek you could use open router as well and I could run things locally like I showed earlier at the AMA I just want to use the best model here so let's go ahead and send this in right away so I also have some settings selected here if you

**[0:14:51]** go into bolt. DIY and go to the settings pane um you can see that was in the bottom left by the way I think my face is covering that but if you go to the features here I have all of these features enabled so you can copy my

**[0:15:02]** settings if you want using the um Auto selection of a code template is usually a good way to get a better project right out the gate so I recommend using those settings but anyway you can see here that under the hood it is already starting creating our app so I'm going

**[0:15:14]** to pause and come back once our one is done creating our full application so just a minute later we now have our full application ready for us to try out and as promised this is a single shot so this is the prompt that I have right here that I just showed you in the

**[0:15:30]** Google Doc we've got the template that it chose and then it just added on a few files install all the dependencies and then ran the application for me this entire thing only took 9,000 tokens and So based on the pricing that we saw earlier this is multitudes less than a

**[0:15:45]** single penny it was so cheap making this entire thing and I haven't even tested it yet cuz I am that confident that with R1 we can build something that works right out the gate so I'm going to try this with you right now for the very first time so I'm going to click on this

**[0:15:58]** button right here in the top right to open it in a new window so we can get a full screen here and then I already have a test account that I have created uh with my super base here so we'll make sure that the authentication is working and boom there we go it is working and

**[0:16:12]** we got all of the conversation history here um so wow look at this looks so good I mean compared to what we saw with lovable this is this is so much nicer and we can toggle this it looks really good uh we can even see what it looks

**[0:16:25]** like if I put it on mobile view look at that this this looks so good and maybe I need to make it a little bit bigger here there we go like this looks good even on mobile this is beautiful and I can start a new conversation here well I guess

**[0:16:37]** there isn't a button for that so maybe I have to add that I mean it's not going to be perfect I can't expect it to be absolutely perfect here um but if I open up a Let me refresh here because I want to have a blank conversation I guess I

**[0:16:49]** can't do that so let let me just open this back up here and um I'll just say like hello boom and let's see what we get back all right so it's getting a response looks like it duplicates the message which is is yeah a little iffy so there's a couple things we want to

**[0:17:02]** fix but overall this is working so well we instantly got a response from our agent here so I can say what can you help me with and this is updating in real time and as long as I fix a couple little glitches here like this duplicate message and being able to start a new

**[0:17:17]** conversation this is going to be absolutely perfect so all with a single shot with R1 we were able to build this also really quickly before we go over to Claude I just wanted to say that with a couple of messages here I was able to fix all of the issues that we saw so

**[0:17:32]** it's very easy to not just in one shot get something really awesome at first with R1 but continue to iterate with it to fix everything that AI coding system are always going to mess up a little bit here so let me open up the full screen window here and log back into my test

**[0:17:48]** account and then uh I'll show you everything that it fixed so we got all the conversations here on the left hand side still everything still looks good but we had those duplicates earlier so now first of all I can click on new to get a new conversation so we're missing

**[0:18:02]** that before and then I can say something like hello and we'll see that we don't have the duplicate user message anymore so that is fixed as well and there is a log out button we were missing that before so I can log out and get back to this screen so I wanted to not just show

**[0:18:17]** you this final perfect result uh I want to be very Frank that like it's not perfect R1 is not perfect I want to be honest with that but we were still able to do a ton with just one shot had a couple of those issues that I showed but

**[0:18:29]** then we were able to fix them very quick and it's not going to be that easy with sonnet so let's dive right back in and start try building this with sonnet as well so here we are moment of truth let's see how R1 comparison bolt. DIY to the model that basically every AI coding

**[0:18:45]** assistant out there uses wind surf bolt. new lovable they all use Claude 3.5 Sonet so I have the exact same prompt working with the same superbase same NN agent nothing is changed here and so we're going to give it a go and see what it can do and I showed you exactly what

**[0:19:03]** R1 gave me in one shot on my very first try and I did some fixes later but I specifically showed you what it looked like after one shot because that's what we're going to compare it to right now with Claude 3.5 Sonet so I'm going to give it a chance to rip through

**[0:19:17]** everything here I'll pause and come back once we have our app and we'll compare the two here we go Cloud 3.5 Sonet finish this is our result after a single shot prompt and it actually looks decent overall but it does definitely not as nice looking as R1 and we're missing

**[0:19:33]** some things like creating a new conversation and logging out just like we were initially with our one so I can give it a chance with a couple more prompts after like I did but let's test out this one shot first so I can click through the conversations and it really

**[0:19:45]** doesn't look as good it's still working overall um but yeah let's try sending a message here and see what we get so I'll say hi it's spinning getting a response back and nothing happened it did not work with R1 and our first shot we were able to communicate with our NN agent

**[0:20:01]** and here in Claude it didn't work and trust me I did test this a few times beforehand just to make sure that this isn't an unlucky shot with Claude and I can confirm that in general it does mess up with these kind of things quite often and so I can definitely start prompting

**[0:20:15]** it here and saying like hey you messed this up and oh you got to add all the other things that R1 missed as well but in general it's very clear that R1 did much much better so model is absolutely insane compared to everything else that we see out there so I know that was just

**[0:20:30]** a super quick demonstration of R1 but I hope that you can see how powerful this model is and it's just so cool that it's open source and that we're not stuck to just using apis from anthropic or open AI but we can actually run these models ourselves use them through platforms

**[0:20:45]** like open router and get access to all this power for super super cheap so let me know in the comments what you think try out this model yourself and tell me what kind of really cool things you're able to do with it with bolt. DIY and in AI agents that you build yourself if you

**[0:21:00]** appreciated this content I would really appreciate a like and a subscribe and with that I will see you in the next video
