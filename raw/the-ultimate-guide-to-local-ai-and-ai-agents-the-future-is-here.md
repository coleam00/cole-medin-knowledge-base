---
type: raw-transcript
title: "The Ultimate Guide to Local AI and AI Agents (The Future is Here)"
youtube_id: mNcXue7X8H0
url: https://www.youtube.com/watch?v=mNcXue7X8H0
slug: the-ultimate-guide-to-local-ai-and-ai-agents-the-future-is-here
published: 2025-06-11
duration: ""
fetched_at: 2026-07-21
immutable: true
---

## Transcript

Welcome to the video that I have put the most effort into creating by far on my channel to date. This is the local AI master class and we're going to dive into everything you need to know about local AI. What it is, why it's so important for you no matter what you are

building with AI. How you can run your own large language models and self-host your own infrastructure. How you can build 100% private and offline AI agents and deploy them to the cloud in a secure way. I have everything that you need to get started here even if you haven't done anything with local

AI before and I take things pretty far. There is a lot of value packed into this for you. So buckle up, enjoy the ride and follow along as well. So, first things first let's start with an agenda for the master class. There are so many things that I cannot wait to share with

you. And I have very detailed chapters for this YouTube video so you can easily navigate between everything that I'm going to show you. I just want to make it super easy for you to get exactly what you want out of this master class. Nothing more, nothing less. We'll start by diving into what

is local AI and I have a quick demo to make this very very hands-on. And then with that, we'll get into the why. Why local AI? Why should you care about it? Why do I believe so firmly that it is the future of AI? I'll dive into all my reasoning there. And then

we'll get into hardware requirements because these local LLMs are beasts and you have to have specific hardware to be able to run them. So I'll dive into all that based on different large language models and some alternatives as well. Then we'll get into all of the tricky stuff. There are a few things

that are usually pretty daunting for people. So I want to break down those barriers just to make you super confident running your own local LLMs and infrastructure. And then with that, we'll get into how you can use local AI anywhere. Because Olama and other solutions for running your own large language models, they

are OpenAI API compatible. I'll get into what that means when we get to this point. But basically, any agents that you already have running with Python or N8N whatever. If you're using OpenAI or Gemini or Enthropic, you can very easily swap them to use local AI instead. So you can turn your existing

agents into ones that are 100% offline, free, and private. And then with that, we will get into the local AI package. This is a set of services that I've curated for you to run your entire local AI infrastructure like your UI, your database, your large language models, and a lot more. This is

where we really start to build out our full infrastructure. I'll walk you through setting up the local AI package getting into the nitty-gritty details to make sure that you have everything set up at this point. And then once we have that set up, we can dive into building a fully local AI agent

with N8N. And then we'll transition that same agent into Python as well. So that you'll see once we have the local AI package set up, how you can build a 100% offline and private agent both with no code and with code. And then we'll take those agents and deploy them to the cloud,

specifically on the Digital Ocean platform. But I'll walk you through a process that you can use no matter the cloud provider that you are using. and we'll deploy things in a very secure way both for the package for our infrastructure and the AI agent itself. And then last, I want to end with

some additional resources just to make sure you have everything that you need to take this master class forward and really use this to build any AI agent that you could possibly want 100% local. And also, if you are interested in mastering more than just local AI, but building entire AI agents in a

local AI environment or even with cloud AI, definitely check out dynamis.ai. AI. This is my community for early AI adopters just like yourself. And a big part of this community is the AI agent mastery course where I dive super deep into my full process for building AI agents. I'm talking planning and prototyping

and coding and using AI coding assistance and building full frontends for our AI agents and securing things and deploying things. There's a lot more coming soon for this course as well. I'm very actively working on it. And a big part of this course is the complete agent that I build throughout it. I

build both with cloud AI and local AI. And so this master class will help you get very very comfortable with local AI. But when it comes to building complex agents and really getting deep into building out agents, then you definitely want to check out the AI agent mastery course here in Dynamis.AI. So

with that, let's get back to the master class, diving into what local AI is all about. Let's start by laying the foundation. What is local AI in the first place? Well, very simply put local AI is running your own large language models and infrastructure like your database and your UI entirely on your

own machine 100% offline. So when you think about when you typically want to build an AI agent, you need a large language model maybe like GPT4.1 or Claude 4 and then you need something like your database like Superbase and you need a way to create a user interface. you have all these different

components for your agent and typically you're using APIs to access things that are hosted on your behalf. But with local AI, we can take all of these things completely in our own control running them ourselves. So this is possible through open-source large language models and software. So everything is running on your own

hardware instead of you paying for APIs. So we run the large language model ourself on our own machine instead of paying for the OpenAI API for example. And so for large language models, there are thousands of different open source large language models available for us to use in a lot of different ways.

And some of these you've probably heard of before, like Deepseek R1, Quen 3 Mistral 3.1, Llama 4. These are just a couple of examples of the most popular ones that you've probably heard of before. We'll be tinkering around with using some of these in this master class. And then we also have open-source

software. So all of our infrastructure that goes along with our agents and LLMs, things like Olama for running our LLMs, Superbase for our database, N8N for our no/ lowode workflow automations and open web UI to have a nice user interface to talk to our agents and LLMs. And we'll dive into using all

of these as well. Now, because local AI means running large language models on our own computer, it's not as easy as just going to claw.ai AI or chatgbt.com and typing in a prompt. We have to actually install something, but it still is very easy to get started. So, let me show you right

now with a hands-on example. So, here we are within the website for Olama. This is just.com. I'll have a link to this in the description of the video. This is one of the open- source platforms that allows us to very easily download and run local large language models. And so, you just have

to go to their homepage here and click on this nice big download button. You can install it for Windows, Mac or Linux. It really works for any operating system. Then once you have it up and running on your machine, you can open up any terminal. Like I'm on Windows here so I'm in

a PowerShell session and I can run Olama commands now to do things like view the models that I have available on my machine. I can download models and I can run them as well. And the way that I know how to pull and run specific models is I can just go to this

models tab in their navigation and I can browse and filter through all of the open source LLMs that are available to me like DeepSeek R1. Almost everyone is familiar with DeepSeek. It just totally blew up back in February and March. We have Gemma 3, Quen 3, Llama 4, a few of them that

I mentioned earlier when we had the presentation up. And so we can click into any one of these like I can go into DeepSeek R1 for example and then I have the command right here that I can copy to download and run this specific model in my terminal. And there are a lot

of different model variants of DeepSeek R1. So we'll get into different sizes and hardware requirements and what that all means in a little bit, but I'll just take one of them and run it as an example. So I'll just do a really small one right now. I'll do a 1.5 billion parameter large

language model. And again, I'll explain what that means in a little bit. I can copy this command. It's just lama run and then the unique ID of this large language model. So I'll go back into my terminal. I'll clear it here and then paste in this command. And so first it's going to

have to pull this large language model. And the total size for this is 1.1 GB. And so it'll have to download it. And then because I used the run command, it will immediately get me into a chat interface with the model once it's downloaded. Also, if you don't want to run it right

right away, you just want to install it, you can do Olama pull instead of Olama run. And then again, to view the models that you have available to you installed already you can just do the Olama list command like I did earlier. And so, right now I'll pause and come back once it's

installed in about 30 seconds. All right, it is now installed. And now I can just send in a message like hello. And then boom, we are now talking to a large language model. But instead of it being hosted somewhere else and we're just using a website, this is running on my own infrastructure,

the large language model and all the billions of parameters are getting loaded onto my graphics card and running the inference. That's what it's called when we're generating a response from the LLM directly within this terminal here. And so I can ask another question like um what is the best GPU right now? We'll

see what it says. So it's thinking first. This is actually a thinking model. Deepseek R1 is a reasoning LLM. And then it gives us an answer. It's top GPU models today. 3080 RX6700. Obviously, we have a training cutoff for local large language models just like we do with ones in the cloud like

GPT. And so the information is a little outdated here, but yeah, this is a good answer. So we have a large language model that we're talking to directly on our machine. And then to close out of this I can just do control D or command D on Mac. And if I do list,

we have all the other models that you saw earlier, plus now this one that I just installed. So these are all available for me to run again just with that Olama run command. And it won't have to reinstall if you already have it installed. Run just installs it if you don't have it

yet already. So that is just a quick demo of using Olama. We'll dive a lot more into Olama later, like how we can actually use it within our Python code and within our N8N workflows. This is just our quick way to try it out within the terminal. Now, to really get into why

we should care about local AI now that we know what it is, I want to cover the pros and cons of local AI and what I like to call cloud AI. That's just when you're paying for things to be hosted for you, like using Claude or Gemini or using the cloud version of

N8N instead of hosting it yourself. And I also want to cover the advantages of each because I don't want to sugarcoat things and just hype up this master class by telling you that you should always use local AI. That is certainly not the case. There is a time and place for both of

these categories here, but there are so many use cases where local AI is absolutely crucial. You have no idea how many businesses I have talked to that are willing to put tens of thousands of dollars into running their own LLMs and infrastructure because privacy and security is so crucial for the things that

they're building with AI. And that actually gets into the first advantage here of local AI, which is privacy and security. You can run things 100% offline. The data that you're giving to your LLMs as prompts, it now doesn't leave your hardware. It stays entirely within your own control. And for a lot of

businesses, that is 100% crucial especially when they're in highly regulated industries like the health industry, finance, uh even real estate. Like there's so many use cases where you're working with intellectual property or just really sensitive information. You don't want to be sending your data off to an LLM provider like Google or OpenAI

or Enthropic. And so as a business owner, you should definitely be paying attention to this if you are working with automation use cases where you're dealing with any kind of sensitive data. And then also if you're a freelancer, you're starting an AI automation agency, anything where you're building for other businesses you are

going to have so many opportunities open up to you when you're able to work with local AI because you can handle those use cases now where they need to work with sensitive data and you can't just go and use the OpenAI API. And that is the main advantage of local AI. It is

a very big deal. But there are a few other things that are worth focusing on as well. Starting with model fine-tuning, you can take any open- source large language model and add additional training on top with your own data. Basically making it a domain expert on your business or the problem that you

are solving. It's so so powerful. You can make models through fine-tuning more powerful than the best of the best in the cloud depending on what you are able to fine-tune with depending on the data that you have. And you can do fine-tuning with some cloud models like with GPT, but your options are

pretty limited and it can be quite expensive. And so it definitely is a huge advantage to local AI. And local AI in general can be very coste effective including the infrastructure as well. So your LLMs and your infrastructure. You run it all yourself and you pay for nothing besides the electricity bill if

it's running on your computer at your house or if you have some private server in the cloud. You just have to pay for that server and that's it. There's no N8N bill, no Superbase bill, no OpenAI bill. You can save a lot of money. It's really, really nice. And on top of that

when everything is running on your own infrastructure, the agents that you create can run on the same server, the same place as your infrastructure. And so it can actually be faster because you don't have network delays calling APIs for all your different services for your LLMs and your database and things like that.

And then with that, we can now get into the advantages of cloud AI. Starting with it's a lot easier to set up. There's a reason why I have to have this master class for you in the first place. There are some initial hurdles that we have to jump over to really have everything

fully set up for our local LLMs and infrastructure. And you just don't have that with cloud AI because you can very simply call into these APIs. You just have to sign up and get an API key and that's about it. So, it certainly is easier to get up and running and there's less

maintenance overall because they are hosting things for you. Superbase is hosting the database for you. OpenAI is hosting the LLM for you. So, you don't have to manage things on your own hardware. With Local AI, you have to apply patches and updates if you have a private server in the cloud. You have

to manage your own hardware if you're running on your own computer, making sure that it's on 24/7 if you want your database on 24/7, that kind of thing. It's just less maintenance with cloud AI. And then probably the biggest advantage of cloud AI overall is that you have better models available to you.

Claude 4 sonnet or opus for example is more powerful than any local AI that you could run. So we have this gap here and this gap was a lot bigger at one point even a year ago. The best local LLMs absolutely crushed the best local LLMs and that gap is starting to diminish.

And so I really see a future where that gap is diminished entirely and all the best local LLMs are actually on par with the best cloud ones. That's the future I see. That's why I think that cloud that's why I think that local AI is such a big deal because the advantages of

local AI, those are just going to get more prevalent over time when businesses realize they really want private and secure solutions. And then the advantages of cloud AI, I think those are actually going to diminish over time. That's the key. minimal setup less maintenance. Well, those advantages are going to go away as

we have platforms and better instructions and solutions to make the setup and maintenance easier for local AI and we have the gap that's continuing to diminish between the power of these LLMs. All these advantages are going to actually go away and then it'll just completely make sense to use local AI honestly probably

for like every single solution in the future. That's really what I see us heading towards. And then the last advantage to cloud AI which also I think will go away over time is that you have some features out of the box like you have memory that's built directly into chat GPT. Gemini has

web search baked in even when you use it through the API like these kind of capabilities that are out of the box that you have to implement yourself with local AI maybe as tools for your agent and you can definitely do that but it is nice that these things are out of the

box for cloud AI. So those are the pros and cons between the two. I hope that this makes it very clear for you to pick right now for your own use case. Should I implement local AI or cloud AI? A lot of it comes down to the security and privacy requirements for your

use case. Now, the next big thing that we need to talk about for local AI is hardware requirements. Cuz here's the thing large language models are very resource inensive. You can't just run any LLM on any computer. And the reason for that is large language models are made up of billions or even

trillions of numbers called parameters. And they're all connected together in a web that looks kind of like this. This is a very simplified view with just a few parameters here. But each of the parameters are nodes and they're connected together. The input layer is where our prompt comes in and our prompt is

fed through all these hidden layers and then we have the output at the end. This is the response we get back from the LLM. But like I said, this is a very simplified view. GPT4, for example, like you can see on the right hand side, is estimated to have 1.4 trillion parameters. And

so, if you want to fit an entire large language model into your graphics card, you have to store all of these numbers. And even though we can handle gigabytes at a time in our graphics cards through what is called VRAMm, storing billions or trillions of numbers is absolutely insane. And so that's why

large language models, you actually have to have a pretty good graphics card if you want to run some of the best ones. And so looking at Olama here, when we see these different sizes going back to their model list, like 1.5 billion parameters or 27 billion parameters, there are different sizes for the

local LLMs. Obviously, the larger a local LM that you are running the more performance you are going to get, but you are going to be limited to what you are capable of running with your graphics card or your hardware. So with that in mind, I now want to dive into the nitty-gritty details

with you so you know exactly the kind of models that you can run, the kind of speeds you can expect depending on your hardware. And if you want to invest in new hardware to run local AI, I've got some recommendations as well. So there are generally four primary size ranges for large language

models based on the speed and the power that you are looking for. You have models that are around seven or 8 billion parameters. Those are generally the smallest that I'd recommend trying to run. There are a lot of smaller LLMs available like 1 billion parameters or three billion parameters but I'm so unimpressed

when I use those LLMs that I don't really want to focus on them here. 7 billion parameters is still tiny compared to the large cloud AI models like Claude or GBT, but you can get pretty good results with them for just simple chat use cases. And so for these models, assuming a Q4

quantization, which I'll get into quantization in a little bit, it's basically just a way to make the LLM a lot smaller without hurting performance that much, a 7 billion parameter model will need about four to 5 GB of VRAM on your graphics card. And so if you have something like a 3060 Ti

from Nvidia with 8 GB of VRAM, you can very comfortably run a 7 billion parameter model and you can expect to get very roughly around 25 to 35 tokens per second. A token is roughly equivalent to a word. And so your local large language model at 7 billion parameters with this graphics card

will get about 25 to 35 words per second out on the screen to you being streamed out. And then if you use much more powerful hardware like a 3090 to run a 7 billion parameter model then you'll just jack up the speed a lot more. So that's 7 billion or 8 billion parameters.

Another very common size is something around 14 billion parameters. This will take about 8 to 10 GB of VRAM. And so just a couple of options for this. You have the 4070Ti which is usually 16 GB of VRAM or you could go as low as 12 GB of VRAM with the 3080 Ti.

And you could expect to get about 15 to 25 words per second. And then this is where you start to get into basic tool calling. So I find that when you are building with a 7 billion parameter model, they don't do tool calling very well. So you can't really build that powerful of

agents around a 7 billion parameter model. But once you get to something around 14 billion parameters that's when I see agents being able to really accept instructions well around tools and system prompts and leveraging tools to do things on our behalf. That's when we can really start to use LLMs to make things

that are agentic. And then the next big category of LLMs is somewhere between 30 and 34 billion parameters. You see a lot of LM that fall in that size range. This will typically need 16 to 20 gigabyt of VRAM. And so a 3090 is a really good example of a graphics card that

can run this. It has 24 GB of VRAM. I actually have two 3090s myself. And I'll have a link to my exact PC that I built for running local AI in the description of this video. So I have two 3090s, which we'll need in a second for a 70 billion parameter, but one

is enough for a 32 billion parameter model. And then also Macs with their new M4 chips are very powerful with their unified memory architecture. So if you get a Mac M4 Pro with 24 GB of unified memory, you can also run 32 billion parameter models. Now the speed isn't going to be the

best necessarily, and again, this does depend a lot on your computer overall, but you can expect something around 10 to 15, maybe up to 20 tokens per second. and 32 billion parameters is when you really start to see LLMs that are actually pretty impressive. Like 7 billion and 14 billion, they are disappointing

quite a bit. I'll be totally honest. Especially when you try to use them with more complicated agentic tasks. 32 billion when you start to get into this range is when I I'm actually genuinely impressed. I'm like, "Oh, this is actually pretty close to the performance of some of the best cloud AI." And

then 70 billion parameters. This is going to take about 35 to 40 GB of VRAM for most consumer GPUs like 3090s and 4090s even 5090s. It's not actually enough VRAM. And so this is when you have to start to split a large language model across multiple GPUs which solutions like Olama will actually

help you do this right out of the box. So it's not this insane setup even though it might feel kind of daunting like oh I have to split the layers of my LLM between GPUs. It's not actually that complicated. And so 23090s, 24090s, that will be necessary. Um, or you could have more

of like an enterprisegrade GPU like an H100. So Nvidia has a lot of these non-consumer grade GPUs that have a lot more VRAMm to handle things like 70 billion parameter models. And the speed won't be the best if you're using something like 23090s especially because performance is hurt when you have to split

an LM between GPUs. You could expect something like 8 to 12 tokens per second. And this is obviously if you have the most complex agents that you're really trying to match the performance of cloud AI as much as possible, that's when you'd want to use a 7 billion parameter model. And then if

you're investing in hardware to run local AI, I have a couple of quick recommendations here. And a lot of this depends on the size of the model that's going to be good enough for your use case. And so I'll dive into some alternatives for running local AI directly if you want to do

testing before you buy infrastructure. I'll get into that in a little bit, but recommended builds. If you want to spend around $800 to build a PC, I'd recommend getting a 4060Ti graphics card and then 32 GB of RAM. If you want to spend $2,000, I'd recommend either getting a PC with a 3090

and 64 GB of RAM or getting that Mac M4 Pro with 24 GB of unified memory. And then lastly, if you want to spend $4,000, which is about what I spent for my PC, then I'd recommend getting two 3090 graphics cards, and I got both of mine used for around $700 each. Um,

and then also getting 128 GB of RAM, or you can get a Mac M4 Max with 64 GB of unified memory. So, I wanted to really get into the nitty-gritty details there. So, I know I spent a good amount of time diving into super specific numbers, but I hope this is, really, helpful,

for, you., No matter, the large language model or your hardware you now know generally where you're at for what you can run. So, to go along with that information overload, I want to give you some specifics, individual LLMs that you can try right now based on the size range that you know will

work for your hardware. So, just a couple of recommendations here. The first one that I want to focus on is Deepseek R1. This is the most popular local LLM ever. It completely blew up a few months ago. And the best part about DeepSeek R1 is they have an option that fits into each

of the size ranges that I just covered in that chart. So they have a 7 billion parameter, 14, 32, and 70. The exact numbers that I mentioned earlier. And then there is also the full real version of R1, which is 671 billion parameters. I'm sorry though, you probably don't have the hardware to

run that unless you're spending tens of thousands on your infrastructure. So, probably stick with one of these based on your graphics card or if you have a Mac computer, pick the one that'll work for you and just try it out. You can click on any one of these sizes here. And then here's

your command to download and run it. And this is defaulting to a Q4 quantization which is what I was assuming in the chart earlier. And again, I will cover what that actually means in a little bit here. The other one that I want to focus on here is Quen 3. This is a

lot newer. Quen 3 is so good. And they don't have a 70 billion parameter option, but they do have all the other um sizes that fit into those ranges that I mentioned earlier. Like they got 8 billion, 14 billion, and 32 billion parameters. And the same kind of deal where you click on

the size that you want and you've got your command to install it here. And this is a reasoning LLM just like DeepSeek R1. And then the other one that I want to mention here is Mistral Small. I've had really good results with this as well. There are less options here but you've got

22 or 24 billion parameters, which is going to work well with a 3090 graphics card or if you have a Mac M4 Pro with 24 GB of unified memory. Really, really good model. And then also, there is a version of it that is fine-tuned for coding specifically called Devstrol, which is a another

really cool LLM worth checking out as well if you have the hardware to run it. So, that is everything for just general recommendations for local LMS to try right now. This is the part of the master class that is going to become outdated the fastest because there are new local LMS coming out

every single month. I don't really know how long my recommendations will last for. But in general, you can just go to the model list in Olama, search for the ones finds one that has the size that works with your graphics card and just give it a shot. You can install it and run

it very easily with Olama. And the other thing that I want to mention here is you don't always have to run open- source large language models yourself. You can use a platform like Open Router. You can just go to open router.ai, sign up, add in some API credits. You can try these open

source LLM yourself. Maybe if you want to see what's powerful enough for your agents before you invest in hardware to actually run them yourself. And so within Open Router, I can just search for Quen here. And I can go down to Quen and I can go to 32 billion. They have a free

offering as well that doesn't have the best rate limits. So I'll just go to this one right here Quen 3 32B. So I can try the model out through open router. They actually host it for me. So it's an open- source non-local version, but now I can try it in my agents to

see if this is good. And then if it's good, it's like, okay, now I want to buy a 3090 graphics card so that I can install it directly through um Olama instead. And so the 32 billion quen 3 is exactly what we're seeing here in open router. And there are other platforms like

Grock as well where you can run these open source large language models um not on your own infrastructure if you just want to do some testing before beforehand or whatever that might be. So I wanted to call that out as an alternative as well. But yeah, that's everything for my general recommendations for

LLMs to try and use in your agents. All right, it is time to take a quick breather. This is everything that we've covered already in our master class. What is local AI? Why we care about it? Why it's the future and hardware requirements. And I really wanted to dive deep into this stuff

because it sets the stage for everything that we do when we actually build agents and deploy our infrastructure. And so the last thing that I want to do with you before we really start to get into building agents and setting up our package is I want to talk about some of the tricky

stuff that is usually pretty daunting for anyone getting into local AI. I'm talking things like offloading models quantization environment variables to handle things like uh flash attention, all the stuff that is really important that I want to break down simply for you so you can feel confident that you have everything set up

right that you know what goes into using local LLMs. The first big concept to focus on here is quantization. And this is crucial. It's how we can make large language models a lot smaller so they can fit on our GPUs without hurting performance too much. We are lowering the model precision here. And

so what basically what that means is we have each of our parameters, all of our numbers for our LLMs that are 16 bits with the full size, but we can lower the precision of each of those parameters to 8, four, or two bits. Don't worry if you don't understand the technicalities of that.

Basically, it comes down to LLMs are just billions of numbers. That's the parameters that we already covered. And we can make these numbers less precise or smaller without losing much performance. So, we can fit larger LLMs within a GPU that normally wouldn't even be close to running the full-size model. Like with 32

billion parameter LLMs, for example, I was assuming a Q4 quantization like four bit per parameter in that diagram earlier. If you had the full 16 bit parameter for the 32 billion parameter LLM, there's no way it could fit on your Mac or your 3090 GPU, but we can use quantization to make it

possible. It's like rounding a number that has a long decimal to something like 10.44 instead of this thing that has like 10 decimal points, but we're doing it for each of the billions of parameters, those numbers that we have. And so just to give you a visual representation of this, you can also

quantize images just like you can quantize LLMs. And so we have our full scale image on the lefth hand side here comparing it to different levels of quantization. We have 16 bit, 8 bit, and 4bit. And you can see that at first with a 16- bit quantization, it almost looks the same. But

then once we go down to 4bit, you can very much see that we have a huge loss in quality for the image. Now with images, it's more extreme than LLMs. when we do a 8 bit or a 4bit quantization, we don't actually lose that much performance like we lose a lot of quality

with images. And so that's why it's so useful for us. And so I have a table just to kind of describe what this looks like. So FP16, that's the 16bit precision that all LMS have as a base. That is the full size. The speed is obviously going to be very slow because the

model is a lot bigger, but your quality is perfect compared to what it could be. I mean, obviously that doesn't, mean, that, you're, going to, get perfect answers all the time. I'm just saying it's it's the 100% results from this LLM. And then going down to a Q8 precision, so it's half the

size. The speed is going to be a lot better. And the quality is nearperfect. So it's not like performance is cut in half just because size is. You still have the same number of parameters. Each one is just a bit less precise. And so you're still going to get almost the same results.

And then going down to a Q4 4bit, it's a fourth the size. It's going to be very fast compared to 16 bit. And the quality is still going to be great. Now, these numbers are very vague on purpose. There's not a huge way to for me to like qualify exactly the difference especially

because it changes per LLM and your hardware and everything like that. So, I'm just being very general here. And then once you get to Q2, um the size goes down a lot. It's going to be very very fast, but usually your performance starts to go down quite a bit once you go down

to a Q2. And then like the note that I have in the bottom left here, a Q4 quantization is generally the best balance. And so when you are thinking to yourself, which large language model should I run? What size should I use? My rule of thumb is to pick the largest large language

model that can work with your hardware with a Q4 quantization. That is why I assumed that in the table earlier. And then also like we saw in Olama earlier, it always defaults to a Q4 quantization because the 16 bit is just so big compared to Q4 that, most, of the, LLMs, you, couldn't,

even run yourself. And a Q4 of a 32 billion parameter model is still going to be a lot more powerful than the full 7 billion parameter or 14 billion parameter because you don't actually lose that much performance. So that is quantization. So just to make this very practical for you, I'm back here

in the model list for Quen 3. We have all these models that don't specify a quantization, but we can see that it defaults to Q4 because if I click on any one of them, the quantization right here is a Q4 KM. And don't worry about the KM. That's just a way to group

parameters. You have KS, KM, and KL. It's kind of outside of the scope of what really matters for you. The big thing is the Q4 like the actual number here. So Q4 quantization is the default for Quen 332B and really any model in Olama. But if we want to see the other quantized

variants and we want to run them, you can click on the view all. This is available no matter the LLM that you're seeing in Olama. Now we can scroll through and see all the levels of quantization for each of the parameter sizes for Quen 3. So, if I scroll all the way down,

the absolute biggest version of Quenti that I can run is the full 16bit of the 235 billion parameter Quen 3. And it is a whopping 470 GB just to install this. And there is no way that you're ever going to lay hands on infrastructure to run this unless you're working for a very

large enterprise. But I can go down here, let's say, to 14 billion parameters and I can run the Q4 like this. So, you can click on any one that you want to run. Like let's say I want to run Q8. I can click on this and then I have the command to pull

and run this specific quantization of the 14 billion parameter model. So each of the quantized variants they have a unique ID within Olama. So you can very specifically choose the one that you want. Again my general recommendation is just to go with also what Olama recommends which is just defaulting to Q4. Like

if I go to DeepSec R1, you can see that also defaults to Q4 no matter the size that I pick. But if you do want to explore different quantizations, you want to try to run the absolute full model for maybe something smaller like 7 billion or 14 billion, you can definitely do that

through a lama and really any other provider of local LLMs. So that is everything for quantization. It's important to know how that works but yes, generally stick with a Q4 of the largest LLM that you can run. The next concept that is very important to understand is offloading. All offloading is is splitting

the layers for your large language model between your GPU and your CPU and RAM. It's kind of crazy, but large language models don't have to fit entirely in your GPU. All large language models can be split into layers, layers of the different weights and you can have some of it running on your

GPU. So, it's stored in your VRAM and computed by the GPU. And then some of the large language models stored in your RAM, computed by the CPU. Now, this does hurt performance a lot. And so generally, you want to avoid offloading if you can. You want to be able to fit everything in

your GPU, which by the way, the context, like your prompts for your local LLMs, that is also stored in VRAM. And so, sometimes you'll see what happens when you have very long conversations for a large language model that barely fit in your GPU. That'll actually tip it over the edge. So, it starts

to offload some of it to the CPU and RAM. So keep that in mind when you have longer conversations and all of a sudden things get really slow, you know that offloading is happening. Sometimes this is necessary though as context grows. And if you're only offloading a little bit of the LLM or

a little bit of the conversation, whatever to the CPU and RAM, it won't affect performance that much. And so sometimes if you're trying to squeeze the biggest size you can into your machine for an LLM, you can take advantage of offloading to run something bigger or have a much larger conversation. Just know

that usually it kind of sucks. Like when I have offloading start to happen, my machine gets bogged down and the responses are a lot slower. It's really not fun, but it is possible. And fun fact, by the way if your GPU is full and your CPU and RAM is full, you can actually

offload to storage, like literally using your hard drive or SSD. That's when it's like incredibly slow and just terrible. But just fun fact, you can actually do that. Now, the very last thing that I want to cover before we dive into some code setting up the local AI package, and building out some

agents is a few very crucial parameters, environment variables for Olama. So, these are environment variables that you can set on your machine just like any other based on your operating system. And Olama does have an FAQ for setting up some of these things, which I'll link to in the description as well. But

yeah these are a bit more technical, so people skip past setting this stuff up a lot, but it's actually really, really important to make things very efficient when running local LLMs. So the first environment variable is flash attention. You want to set this to one or true. When you have this set to

true, it's going to make the attention calculation a lot more efficient. It sounds fancy but basically large language models when they are generating a response, they have to calculate which parts of your prompt to pay the most attention to. That's the calculation. And you can make it a lot more efficient without losing

much performance at all by setting up the flash attention, setting that to true. And then for another optimization just like we can quantize the LLM itself, you can also quantize or compress the context. So your system prompt, the tool descriptions, your prompt and conversation history, all that context that's being sent to your

LLM, you can quantize that as well. So Q4 is my general recommendation for quantizing LLMs. Q8 is the general recommendation for quantizing the context memory. It's a very simplified explanation, but it's really, really useful because a long conversation can also take a lot of VRAM just like larger LLM. And so it's good

to compress that. And then the third environment variable this is actually probably the most crucial one to set up for Olama. There is this crazy thing. I don't know why Olama does it, but by default, they limit every single large language model to 2,000 tokens for the context limit which is just tiny

compared to, you know, Gemini being 1 million tokens and Claude being 200,000 tokens. Like, they handle very, very large prompts. And a lot of local large language models can also handle large prompts. But Olamo will limit you to default to 2,000 tokens. And so you have to override that yourself with this environment

variable. And so generally I recommend starting with about 8,000 tokens to start. You can move this all the way up to something like 32,000 tokens if your local large language model supports that. And if you view the model page on Alama, you can see the context link that's supported by the LLM. But

you definitely want to, you know, jack this up more from just 2,000 because a lot of times when you have longer conversations, you're going to get past 2,000 tokens very, very quickly. So, do not miss this. If your large language model is starting to go completely off the rails and ignore your system

prompt and forget that it has these tools that you gave it, it's probably because you reached the context length. And so, just keep that in mind. I see people miss this a lot. And then the very last environment variable, uh, probably the least important out of all these four but if you're running

a lot of different large language models at once and you're trying to shove them all in your GPU, a lot of times you can have issues. And so in Olama, you can limit the number of models that are allowed to be in your memory at a single time. With this one typically you

want to set this to either one or two. Definitely set this to just one if you are using large language models that are basically fit for your GPU. like it's going to fit exactly into your VRAM and you're not going to have room for another large language model. But if you are running

more smaller ones and maybe you could actually fit two on your GPU with the VRAM that you have you can set this to two. So again, more technical overall, but it's very important to have these right. And we'll get into the local AI package where I already have these set up in the

configuration. And then by the way, this is the Olama FAQ that I referenced a minute ago that I'll have linked in the description. And so there's actually a lot of good things to read into here. um like being able to verify that your GPU is compatible with Olama. How can you tell if

the model's actually loaded on your GPU? So, a lot of like sanity check things that they walk you through in the FAQ as well. Also talking about environment variables, which I just covered. And so, they've got some instructions here depending on your OS how to get those set up. So, if there's anything

that's confusing to you, this is a very good resource to start with. So, I'm trying to make it possible for you to look into things further if there's anything that doesn't quite make sense for what I explained here. And of course, always let me know in the comments if you have any questions

on this stuff as well, especially the more technical stuff that I just got to cover because it's so important even though I know we really want to dive into the meat of things, which we are actually going, to, do, now., All right,, here, is everything that we have covered at this point. And

congratulations if you have made it this far because I covered all the tricky stuff with quantization and the hardware requirements and offloading and some of our little configuration and parameters. So, if you got all of that the rest of it is going to be a walk in the park as we start to

dive into code getting all of our local AI set up and building out some agents. You understand the foundation now that we're going to build on top of to make some cool stuff. And so, now the next thing that we're going to do is talk about how we can use local AI anywhere.

We're going to dive into OpenAI compatibility and I'll show you an example. We can take something that is using OpenAI right now transform it into something that is using OAMA and local LLM. So, we'll actually dive into some code here. And I've got my fair share of no code stuff in this master

class as well, but I want to focus on both because I think it's really important to use both code and no code whenever applicable. And that applies to local AI just like building agents in general. So, I've already promised a couple of times that I would dive into OpenAI API compatibility, what it

is, and why it's so important. And we're going to dive into this now so you can really start to see how you can take existing agents and transform them into being 100% local with local large language models without really having to touch the code or your workflow at all. It is a beautiful

thing because OpenAI has created a standard for exposing large language models through an API. It's called the chat completions API. It's kind of like how model context protocol MCP is a standard for connecting agents to tools. The chat completions API is a standard for exposing large language models over an API. So you

have this common endpoint /v1/hatcompletions along with a few other ones that all of these providers implement. This is the way to access the large language model to get a response based on some conversation history that you pass in. So, Olama is implementing this as of February. We have other providers like Gemini is

OpenAI compatible. Uh, Grock is Open Router, which we saw earlier. Almost every single provider is OpenAI API compatible. And so, not only is it very easy to swap between large language models within a specific provider, it's also very easy to swap between providers entirely. You can go from Gemini to OpenAI or OpenAI

to O Lama or OpenAI to Grock just with changing basically one piece of configuration pointing to a different base URL as it is called. So you can access that provider and then the actual API endpoint that you hit once you are connected to that specific provider is always the exact same and the

response that you get back is also always the exact same. And so Olama has this implemented now. And I'll link to this article in the description as well if you want to read through this because they have a really neat Python example. It shows where we create an OpenAI client and the only

thing we have to do to connect to Olama instead of OpenAI is change this base URL. So now we are pointing to Olama that is hosted locally instead of pointing to the URL for OpenAI. So we'd reach out to them over the internet and talk to their LLMs. And then with Olama, you

don't actually need an API key because everything's running locally. So you just need some placeholder value here. But there is no authentication that is going on. You can set that up. I'm not going to dive into that right now. But by default, because it's all just running locally, you don't even need an

API key to connect to Olama. And then once we have our OpenAI client set up that is actually talking to Olama, not OpenAI, we can use it in exactly the same way. But now we can specify a model that we have downloaded locally already through Lama. We pass in our conversation history in

the same way and we access the response like the content the AI produced the token usage like all those things that we get back from the response in the same way. They've got a JavaScript example as well. They have a couple of examples using different frameworks like the Versell AI SDK and Autogen.

Really any AI agent framework can work with OpenAI API compatibility to make it very easy to swap between these different providers. like Pyantic AI, my favorite AI agent framework, also supports OpenAI API compatibility. So you can easily within your Pantic AI agents swap between these different providers. And so what I have for

you now is two code bases that I want to cover. The first one is the local AI package, which we'll dive into in a little bit. But right now, we have all of the agents that we are going to be creating in this master class. So I have a couple for N8N that

are also available in this repository. And then a couple of scripts that I want to share with you as well. And so the very first thing that I want to show you is this simple script that I have called OpenAI compatible demo. And so you can download this repository. I'll have this linked

in the description as well. There's instructions for downloading and setting up everything in here. And this is all 100% local AI. And so with that I'm going to go over into my windsurf here where I have this OpenAI compatible demo set up. So I've got a comment at the top reminding us what

the OpenAI API compatibility looks like. We set our base URL to point to Olama hosted locally and it's hosted on port 11434 by default. So I can actually show you this. I have Ola running in a Docker container, which we're going to dive into this when we set up the local AI package,

but you can see that it is being exposed on port 11434. And by the way, you can see the 127.0.0.1 in that URL that I have highlighted here, that is synonymous with localhost. And so this right here, you could also replace with 127.0.0.1. Just a little tidbit there. It's not super important. I

just typically leave it as localhost. And then you can change the port as well. I'm just sticking to what the default is. And then again, we don't need to set our API key. We can just set it to any value that we want here. We just need some placeholder even though there is

no authentication with a llama for real unless you configure that. So that's OpenAI compatibility. And the important thing with this script here is I have two different configurations here. I have one for talking to OpenAI and then one for OALMA. So with OpenAI, we set our base URL to point to api.openai.com. We

have our OpenAI API key set in our environment variables. So you can just set all your environment variables here and then rename this to env. I've got instructions for that in the readme of course. And then going back to the script, we are using GPT4.1 nano for our large language model. There's something

super fast and cheap. And then for our Lama configuration, we are setting the base URL here, localhost1434 or just whatever we have set in our environment variables. Same thing for the API key. And then same thing for our large language model. And what I'm going to be using in this case is Quen

314B. That is one of the large language models that I showed you within the Olama website. Definitely a smaller one compared to what I could run, but I just want to run something fast. And very small large language models are great for simple tasks like summarization or just basic chat. And that's what

I'm going to, be, using, here, just, for, a, simple demo. And so whether it's enabled or not, this configuration is just based on what we have set for our environment variables. And the important thing here is the code that runs for each of these configurations just as we go through this demo is

exactly the same. We are parameterizing the configuration for the base URL and API key. So we are setting up the exact same OpenAI client just like we saw in the Olama article but just changing the base URL and API key. And so then for example when we use it right here it's client.hat.comp

completions.create create calling the exact, same, function, no matter, if, we're using OpenAI or Olama. And then we're handling the response in the same way as well. And so I'll go back to my terminal now. And so I went through all the steps already to set up my virtual environment, install all of my

dependencies. And so now I can run the command OpenAI compatible demo. And now it's, going to, present, the, two configuration options for me. And so I can run through OpenAI. So we'll go ahead and do that first. And these two demos are going to look exactly the same, but that is the point.

And so we have our base URL here for OpenAI. We have a basic example of a completion with GPT4.1 Nano. There we go. So this is the model that was used. Here are the number of tokens. And this is our response. And then I can press enter to see a streaming response now

as well. So we saw it type out our answer in real time. And then I can press enter one more time. This is the last part of the demo. Just say multi-turn conversation. So we got a couple of messages here in our conversation history. So very nice and simple. The point here is

to now show you that I can run this and select Olama now instead and everything is going to look exactly the same and all of the code is the same as wallet. It is only our configuration that is different. And so it will take a little bit when you first run this because

Olama has to load the large language model into your GPU. And so going to the logs for Olama, I can show you what this looks like here. And so when we first make a request when Quen 314B is not loaded into our GPU yet, you're going to see a lot of logs come

in here and we'll and you'll have this container up and running when you have the local AI package which we'll cover in a little bit. So it shows all the metadata about our model like it's Quen 314b. Uh we can see here that uh we have a Q4 KM quantization like we saw

in the Olama website. Uh what other information do we have here? There's just so much to to digest here. Um, yeah, another really important thing is we have the uh context link. I have that set to 8,192 just like I recommended in the environment variables. And then we can see that we offloaded

all of the layers to the GPU. So I don't have to do any offloading to the CPU or the RAM. I can keep everything in the GPU, which is certainly ideal, like I said, to make sure this is actually fast. And then when we get a response from quen 314b we are calling

the v1/hatcompletions endpoint because it is openi API compatible. So that exact endpoint that we hit for openai is the one that we are hitting here with a large language model that is running entirely on our computer in Olama. And so the response I get back, it's actually a reasoning LLM as well. So

we even have the thinking tokens here, which is super cool. And so we got our response. It's just printing out the first part of it here just to keep it short. And then I can press enter. And we can see a streaming demo as well. And it's going to be a lot faster

this time because we do already have the model loaded into our GPU. And so that first request when it first has to load a model is always the slower one. And then it's faster going forward once that model is already loaded in our GPU. And then as long as we don't swap to

another large language model and use that one, then it will remain in our GPU for some time. And so then all of our responses after are faster. And then we just have the last part of our demo here with a multi-turn conversation. So we can see conversation history in action as well, just

not with streaming here. Um, and and everything's a bit slower with this large language model because it is a reasoning one. And so you can certainly if you want faster uh inference, you can always use a non-reasoning local LLM like Mistl or Gemma for example. So that is our very simple demo showing

how this works. I hope that you can see with this and again this works with other AI agent frameworks like eggno or pideantic AI or crew AI as well like they all work in this way where you can use openAI API compatibility to swap between providers so easily so you don't have to

recreate things to use local AI and that's something so important that I want to communicate with you because if I'm the one introducing you to local AI I also want to show you how it can very easily fit into your existing systems and automations. All right. Now, we have gotten to the part

of the local AI master class that I'm actually the most excited for because over the past months, I have very much been pouring my heart and soul into building up something to make it infinitely easier for you to get everything up and running for local AI. And that is the local AI package.

And so, right now, we're going to walk through installing it step by step. I don't want you to miss anything here because it's so important to get this up and running, get it all working well. Because if you have the local AI package running on your machine and everything is working, you don't

need anything else to start building AI agents running 100% offline and completely private. And so here's the thing. At this point, we've been focusing mostly on Olama and running our local large language models. But there's the whole other component to local AI that I introduced at the start of the master class for

our infrastructure. things like our database and local and private web search, our user interface agent monitoring. We have all these other open-source platforms that we also want to run along with our large language models and the local AI package is the solution to bring all of that together curated for you to install

in just a few steps. So, here is the GitHub repository for the local AI package. I'll have this linked in the description below. Just to be very clear, there are two GitHub repos for this master class. We have this one that we covered earlier. This has our N8N and Python agents that we'll

cover in a bit, as well as the OpenAI compatible demo that we saw earlier. So, you want to have this cloned and the local AI package as well. Very easy to get both up and running. And if you scroll down in the local AI package, I have very comprehensive instructions for setting up

everything, including how to deploy it to a private server in the cloud which we'll get into at the end of this master class, and a troubleshooting section at the bottom. So, everything that I'm about to walk you through here there's instructions in the readme as well if you just want to circle back

to clarify anything. Also, I dive into all of the platforms that are included in the local AI package. And this is very important because like I said, when you want to build a 100% offline and private AI agent, it's a lot more than just the large language model. You have all of the

accompanying infrastructure like your database and your UI. And so I have all that included. First of all, I have N8N that is our low/noodeode workflow automation platform. We'll be building an agent with N8N in the local AI package in a little bit once we have it set up. We have Superbase for our

open- source database. We have Olama. Of course, we want to have this in the package as well for our LLMs. Open Web UI, which gives us a chat GPT like interface for us to talk to our LLMs and have things like conversation history. Very, very nice. So, we're looking at this right here.

This is included in the package. Then we have Flowwise. It's similar to N8N. It's another really good tool to build AI agents with no slash low code. Quadrant, which is an open- source vector database. Neo4j which is a knowledge graph engine and then seir xng for open-source completely free and private web search

caddy which this is going to be very important for us once we deploy the local AI package to the cloud and we actually want to have domains for our different services like nn and open web UI and then the last thing is langfuse this is an open- source LLM engineering platform it helps

us with agent observability now some of these services are outside of the scope for this local AI master class. I don't want to spend a half hour on every single one of these services and make this a 10-hour video. I will be focusing in this video on N8N, Superbase, Olama Open WebUI, CRXNG,

and then Caddy once we deploy everything to the cloud. So, I do cover like half of these services. And the other thing that I want to touch on here is that there are quite a few things included here. And so you do need about 8 GB of RAM on your machine or your

cloud server to run everything. It is pretty big overall. And so you can remove certain things like if you don't want Quadrant and Langfuse for example you can take those out of the package. More on that later. It doesn't have to be super bloated, you can whittle this down to what you need.

But yeah, there's a lot of different things that go into building AI agents. And so I have all of these, services, here, so, that, no matter what you need, I've got you covered. And so with that, we can now move on to installing the local AI package. And these instructions will work for

you on any operating system, any computer. Even if you don't have a really good GPU to run local large language models, you still could always use OpenAI or Anthropic, something like that, and then run everything else locally to save on costs or just to have everything running on your computer. And so there

are a couple of prerequisites that you have to have before you can do the instructions below. You need Python so you can run the start script that boots everything up. Git or GitHub desktop so you can clone this GitHub repository, bring it all onto your own machine. And then you want Docker or

Docker Desktop. And so I've got links for all of these. Docker and Docker Desktop we need because all of these local AI services that I've curated for you, they all run as individual Docker containers that are all combined together in a stack. And so I'll actually show you this is the end result

once we have everything up and running within your docker desktop. You have this local AI docker compos stack that has all of the services running in tandem like superbase and reddus and nitn and flowwise caddy neo4j. All of these are running within this stack. That is what we're working towards right now. And

so make sure you have all these things installed. I've got links that'll take you to installing no matter your operating system. Very easy to get all of this up and running on your machine. Then we can move on to our first command here, which is to clone this GitHub repository, bringing all of

this code on your machine so you can get everything running. And so you want to open up a new terminal. So I've got a new PowerShell session open here. Going to paste in this command. And I'm going to be doing this completely from scratch with you. So you clone the repo and then

I'm just going to change my directory into local AI package, which was just created from this get clone command. So those are the first two steps. The next thing is we have to configure all of our environment variables. And believe it or not, this is actually the longest part of the process. And

once we have this taken care of, it's a breeze getting the rest of this up and running. But there's a lot of configuration that we have to set up for our different services like credentials for logging into our Superbase dashboard or Neo4j. Uh things like our Superbase um anonymous key and private key.

All these things we have to configure. And so within our terminal here, you can do code dot to open this within VS code or windsurf. Open this in windsurf. You just want to open up this folder within your IDE and the specific IDE that you use. Really doesn't matter. You just want to

get to this.env.example here. I'm going to copy it and then I'm going to paste it. And then I'm going to rename this toenv. So we're taking the example. example, turning it into av file. So you want to make sure that you copy it and rename it like this. Then we can go ahead

and start setting all of our configuration. And I'll even zoom in on this just so that it's very easy for you to see everything that we are setting up here. So, first up, we have a couple of credentials for N8N. We have our encryption key and our JWT secret. And it's very easy

to generate these. In fact, we'll be doing this a couple of times, but we'll use this open SSL command to generate a random 32 character alpha numeric string that we're going to use for things like our encryption key and JWT secret. And so OpenSSL is a command that is available for you by

default on Linux and Macs. You can just open up any terminal and run this command and it'll spit out a long string that you can then just paste in for this value. For Windows, you can't just open up any terminal and use OpenSSL, but you can use Git Bash, which is going to

come with GitHub Desktop when you install it. And so, I'll go ahead and just search for that. If you just go to your search bar on your bottom left on Windows and search for Git Bash, it's going to open up this terminal like this. And so, I can go ahead and copy this

command, go in here and paste it in. And then I can run it. And then, boom, there we go. This is I know it's really small for you to see right now. I'm going to go ahead and copy this because this is now the value that I can use for my encryption key.

And then you want to do the exact same thing to generate a JWT secret. And then the other way that you can do this if you don't want to install git bash or it's not working for whatever reason you can use Python to generate this as well. So I can just copy this

command and then I can go into the terminal here and I can just paste this in. And so it's going to just like with OpenSSL generate this random 32 character string that I can copy and then use for my JWT secret. There we go. And so I am going to get in the

weeds a little bit here with each of these different parameters but I really want to make sure that I'm clear on how to set up everything for you so you can really walk through this step by step with me. And like I said setting up the environment variables is the longest part by

far for getting the local AI package set up. So if you bear with me on this, you get through this configuration, you will have everything running that you need for local AI for the LLMs and your infrastructure. So that's everything for N8N. Now we have some secrets for Superbase. And there are some

instructions in the Superbase documentation for how to get some of these values. So it's this link right here, which I have open up on my browser. So we'll we'll reference this in a little bit here. But first, we can set up a couple of other things. The first thing we need to define

is our Postgress password. So, Supphabase uses Postgress under the hood for the database. And so, we want to set a password here that we'll use to connect to Postgress within N8N or a connection string that we have for our Python code whatever that might be. And this value can be really anything that

you want. Just note that you have to be very careful at using special characters like percent symbols. So if you ever have any issues with Postgress, it's probably because you have special characters that are throwing it off. U that's something that I've seen happen quite a few times. And so like I said,

I want to mention troubleshooting steps and things to make sure that it is very clear for you. So for this Postgress password here, I'm just going to say test Postgress pass. I'm just going to give some kind of random value here. Just end with a couple of numbers. I don't care that I'm

exposing this information to you because this is a local AI package. These passwords are for services that never leave my computer. So, it's not like you could hack me by connecting to anything here. And then we have a JWT secret. And this is where we get into this link right here in the

Superbase docs. And so they walk you through generating a JWT secret and then using that to create both your anonymous and your service role keys. If you're familiar with Superbase at all, we need both of these pieces of information. The anonymous key is what we share to our front end. This is our

public key. And then the service role key has all permissions for Superbase. We'll use this in our backends for things like our agents. And so you can just go ahead and copy. You can go ahead and copy this JWT secret. And then you can paste this in right here. This is 32 characters

long just like the things that we generated with OpenSSL. I'm just going to be using exactly what Superbase tells me to. And then what you can do with this is you can select the anonymous key. Click on generate JWT and then I can copy this value and then I will paste this for

my anonymous token. And so I'm just replacing the default value there for the anonymous key. And then going back and selecting the service key, I'm going to generate that one as well. So it looks very similar. They'll always start with ey, but these values are different if you go towards the end. And

so I'll go ahead and paste this for my service ro key. Boom. There we go. All right. And then for the Superbase dashboard that we'll log into to see our tables and our SQL editor and authentication and everything like that, we have our username here, which I'm just going to keep as superbase.

And then for the password, I can just say test superbase pass. I'll just kind of use that as my common nomenclature here for my passwords cuz I don't really care what that is right now. And then the last thing that we have to set up is our pooler tenant ID. And it's not

really important to dive into what exactly this means. Just know that you can set this to really anything that you want. Like I typically will just choose four digits here like 1,00 for my pooler tenant ID. So that is everything that we need for superbase. And actually most of the configuration is for

superbase. Then we have Neo4j. This is really simple. You can leave Neo4j for the username and then I'll just say test Neo4j pass for my password here. So you just set the password for knowledger graph and even if you're not using Neo4j you still have to set this but yeah it just takes

two seconds. Then we have langfuse. This is for agent observability. We have a few secrets that we need here. And for these values they can really just be whatever you want. It doesn't matter because these are just passwords just like we had passwords for things like Neoforj. So I can just say test

click house pass. Um and then I can do test mo pass. And um I mean it really doesn't matter here. Random Langfuse salt. I'm just doing completely whack values here. You probably want something more secure in this case, but um I'm just doing something as a placeholder for now. Um yeah, that there

we go. Okay, good. And then then, the, last, thing, that, we, need for Langfuse is an encryption key. And this is also generated with OpenSSL like we did for the N8N credentials. And so I'll go back to my git bash terminal. And again, you can do this with Python as well. I'll just

run the exact same command. I'll get a different value this time. And so I'll go ahead and copy that. You could technically use the same value over and over if you wanted to but obviously it's way more secure to use a different value for each of the encryption keys that you generate with

OpenSSL. So there we go. That is our encryption key. And that is actually everything that we have to set up for our environment variables when we are just running the local AI package on our computer. Once we deploy it to the cloud and we actually want domains for our different services like open

web UI and N8N then we'll have to set up caddy. So this is where we'll dive into domains and we'll get into this at the end of the master class here. But everything past this point for environment variables is completely optional. You can leave all of this exactly as it is and everything

will work. Most of this is just extra configuration for superbase. So, Superbase is definitely the biggest service that's included in this list of, you know, curated services for you. And so, there's a lot of different configuration things you can play around with if you want to dive more into this. You can definitely

look at the same documentation page that we were using for the Superbase Secrets. And so, you can scroll through this if you want to learn more um like setting up email authentication or Google authentication. um diving more into all of those different configuration things for Superbase if you want to dive more into

that. I'm not going to get into all of this right now because the core of getting Superbase up and running we already have taken care of with the credentials that we set up at the top um right here. And so that these are these are just the base things and so that's what

we'll stick to right now. So that is everything for our environment variables. So then going back to our readme now which I have open directly in windsurf now instead of my browser we have finished our configuration and I do have a note here that you want to set things up for caddy if

you're deploying to production. Obviously we're doing that later not right now like I said and so with that we are good to start everything. Now before we spin up the entire local AI package there is one thing that I want to cover. It's important to cover this before we run things. If you

don't want to run everything in the package cuz it is a lot like maybe you only want to use half of these services and you don't want Neo4j and Langfuse and Flowwise right now. There are two options that you have. The easiest one right now is to go into the docker compose file.

This is the main file where all of the services are curated together and you can just remove the services that you don't want to include. So, for example, if you don't want Quadrant right now, cuz it is actually one of the larger services. It's like 600 u megabytes of RAM just having this

running, you can search for Quadrant, and you can just go ahead and delete this service from the stack like that. Boom. Now I don't have Quadrant. It won't spin up as a part of the stack anymore. And then also I have a volume for Quadrant. So, you can remove that as well. Volumes,

by the way, is how we are able to persist data for these containers. So if we tear down everything and then we spin it back up we still are going to have our open web UI conversations and our N8N workflows everything in Superbase, like all that is still going to be saved because

we're storing it all in volumes. So we can do whatever the heck we want with these containers. We can tear them down. We can update them, which I'll show you how to do later. We can spin it back up. And all of our data will always be persisted. So you don't have to

worry about losing information. And you can always back things up if you want to be really secure, but I've never done that before and I've been updating this package for months and months and months and all of my workflows from 6 months ago are still there. I haven't lost anything. And so that's

just a quick caveat there for how you can remove services if you want. And then another thing that we don't have available yet but I'm very excited to, you know, kind of talk about this right now. It's in beta right now. We are creating me and one other guy uh that's actually on

my Dynamist team. Um Thomas, he's got a YouTube channel as well. He's a great guy. We're working together on this. He's actually been putting in most of the work creating a front-end application for us to manage our local AI package. And one of the big things with this is that we're going to

make it possible for you to toggle on and off the services that you want to have within your local AI package. So you can very much customize the package to the services that you want to run. So you can keep it lightweight just to the things you care about. Also, we'll be able

to manage environment variables and monitor the containers. Not all of this is up and running at this point, but this is in beta. We're working on it. I'm really excited for this. So, not available yet, but at once this is available, this will be a really good way for you to customize the

package to your needs. So, you don't have to go and edit the docker compose file directly. So, that's something that I just wanted to get out of the way now. But, we can start and actually execute our package now. Get all these containers up and running. So the command that you run to

start the local AI package is different depending on your operating system and the hardware that you have. So for example, if you are an Nvidia GPU user you want to run this start services.py script. This boots up all of the containers and you want to specifically pass in the profile of GPU NVIDIA.

This is going to start Ola in a way where the Olama container is able to leverage your GPU automatically. And then if you are using an AMD GPU and you're on Linux then you can run it this way. Which by the way, unfortunately, if you have an AMD GPU on Windows, you aren't

able to run O Lama in a container. And it's the same thing with Mac computers. Unfortunately, like you see right here you cannot expose your GPU to the Docker instance. And so if you are an AMD GPU on Windows or running on Mac, you cannot run Olama in the local AI package. You

just have to install it on your own machine like I already showed you in this master class and then you'll just run everything else through the local AI package and they can actually go out to your machine and communicate to Olama directly. So just a small limitation for Mac and AMD on Windows.

But if you're running on Linux or an Nvidia GPU on Windows like I'm using, then you can go ahead and run this command right here. So if you can't run a GPU in the Olama container, then you can always just start in CPU mode or you can run with a profile of none.

This will actually make it so that Olama never starts in the local AI package. So you can just leverage the Olama that you have already running on your computer like I showed you how to install already. So, just a couple of small caveats that I really want to hit on there. I need

to make sure that you're using the right command. And so, in my case, I'm Nvidia on Windows. So, I'm going to copy this command. Go back over into my terminal. I'll just clear it here. So, we have a blank slate. And I'll paste in this command. And so, it's going to do quite

a few things initially. First, it's going to clone the Superbase repository because Superbase actually manages the stack in a separate place. And so, we have to pull that in. Then there's some configuration for CRXNG for our uh local and private web search. And then I have a couple of warnings here saying that

the Flowwise username and password are not set, which by the way for that if you want to set the Flow Wise username and password, it's optional, but you can do that if I scroll down right here. So you can set these values, those will actually make those warnings go away but you can

also ignore them, too. So anyway, I just wanted to mention that really quickly. But now what's happening here is it starts by running all of the Superbase containers. And so there's quite a bit that goes into Superbase like I said. So we're running all of that. It's getting all that spun up. And

then once we run all of these, it's going to move on to deploying the rest of our stack. And if you're running this for the very first time, it will take a while to download all of these images. They're not super small. There's a lot of infrastructure that we're starting up here. And

so it'll take a bit. You just have to be patient. maybe go grab your coffee or make your next meal, whatever that is. And then everything will be up and running once you are back. And so yeah, now you can see that we are running the rest of the containers here. Um, and

so we'll just wait for that to be done. And then I'll show you what that looks like in Docker Desktop as well. And so I'll give it a second here just to finish. Uh, looks like my terminal glitched a little bit. Like I was scrolling and so it kind of broke it a

bit. But anyway, everything is up and running now. It'll look like this where it'll say all of the containers are healthy or running or started. And then if I go into Docker Desktop and I expand the local AI compost stack, you want to make sure that you have a green dot for everything

except for the Olama pull and N8N import. These just run once initially and then they go down because they're responsible for pulling some things for our local AI package. And so yeah, I've got green dots for everything except for two right here. Now I'm leaving this in here intentionally actually because there is

a bug with Superbase specifically if you are on Windows. So you'll see this issue where the Superbase pooler is constantly restarting and that also affects N8N because N8N relies on the Superbase pooler. So it's constantly restarting as well. If you see this problem, I actually talk about this in the troubleshooting section of

the readme. If you scroll all the way down, if the Superbase pooler is restarting, you can check out this GitHub issue. And so I linked to this right here, and he tells you exactly which file you want to change. It's this one right here. So it's docker volumes poolerpooler.exs. And you need to

change the file to end in lf. And so I'll show you what I mean by that. I'll show you exactly how to do this. It's like a super tiny random thing, but this has tripped up so many people. So I want to include this explicitly in the master class here. So you want

to go within the superbase folder within docker volumes and then it's within pooler and then we have pooler.exs and basically no matter your IDE you can see the crlf in the bottom right here. You want to click on this and then change it to lf and then make sure that you save this

file. Very easy to fix that. And then what you can do is you can run the exact same command to spin everything up again. And so I'm going to do this now. It's going to go through all the same steps. It'll be faster this time because you already have everything pulled. And this,

by the way, is how you can just restart everything really quickly if you want to enforce new environment variables or anything like that. So I want to include that explicitly um for that reason as well. And I'll go ahead and close out of this. And and while this is all restarting the other

thing that I want to show you in the readme is I also have instructions for upgrading the containers in the local AI package. So when N8N has an update or Superbase has an update, it is your responsibility because you're managing the infrastructure to update things yourself. And so you very simply just have

to run these three commands to update everything. You want to tear down all of the containers and make sure you specify your profile like GPU Nvidia and then you want to pull all of the latest containers and again specifying your profile. And then once you do those two things, you'll have the most

up-to-date versions of the containers downloaded. So you can go ahead and run the start services with your profile just like we just did to restart things. Very easy to update everything. And even though we are completely tearing down our containers here before we upgrade them we aren't losing any information because we are

persisting things in the volumes that we have set up at the top of our Docker Compose stack. And so this is where we store all of our data in our database and and workflows. All these things are persisted. So we don't have to worry about losing them. Very easy to upgrade things and

you still get to keep everything. You don't have to make backups and things like that unless you just want to be ultra ultra safe. So now we can go back to our Docker desktop and we've got green dots for everything now since we fixed that pooler.exs issue. The only thing that we don't

have green dots for is the N8N import and then we have our Olama pull as well because like I said those are the two things that just have to run at the beginning and then they aren't ongoing processes like the rest of our services. So, we have everything up and running. And if

there is anything that is a white dot besides Olama pull or n import or if there's anything that is constantly restarting just feel free to post a comment and I'll definitely be sure to help you out. And then also check out the troubleshooting section as well. One thing that I'll mention really quick

is sometimes your N8N will constantly restart and it'll say something like the N8N encryption key doesn't match what you have in the config. And the big thing to keep in mind for that is you want to make sure that you set this value for the encryption key before you ever run it for

the first time. Otherwise, it's going to generate some random default value and then if you change this later, it won't match with what it expects. And so, yeah, my big recommendation is like make sure you have everything set up in your environment variables before you ever run the start services for the first

time. This should be run once you have your environment variables set up. Otherwise, you risk any of these services creating default values that then wouldn't match with the keys and things that you set up later. And so with that, we can now go into our browser and actually explore all of these local

AI services that we have running on our computer now. Now over in our browser, we can start visiting the different services that we have spun up. Like here is N8N. You just have to go to localhost port 5678. It'll have you create a local account when you first visit it. And then you'll

have this workflow view that should look very familiar to you. if you have used NAND in the past. And then we have open web UI localhost port 8080. This is our chat GPT like interface where we can directly talk to all of the models that we have pulled in our Olama container. Really

really neat. And then we have local host port 8000 for our Superbase dashboard. The signin definitely isn't pretty compared to the managed version of Superbase. But once you enter in your username and password that you have set for the environment variables for the dashboard, then you have the very typical view where we

have our tables and we've got our SQL editor. Everything that you're familiar with with Superbase. And that's the key thing with all these different services. They all will look the exact same for you pretty much., Um, like, another, one, for example, if I go to localhost um port 3000, we have languages. This

is for agent observability and monitoring. And this is something I'm not going to dive into in this master class. Like I said, I'm not covering all the services. But yeah I just want to show that like every single one of these pretty much you can access in your browser. And by the way

the way that we know the specific port to access for each of these services is by taking a look at either what it tells us in Docker Desktop. So like we can see that Neo4j is um let's see, we have port 7474. For uh CR XNG, it's port 8081. For Flowwise, it's port

3001. What's one that we've seen already? Um, let me Yeah, like Open Web UI is port 8080. So the port on the left is the one that we access in our browser. And then the port on the right is what's mapped on the container. So, when we visit port 8080 on our computer,

that goes into port 8080 on the container. And that's what we have exposed. The other way that you can see the port that you need to use is just by taking a look at this docker compose file. And you don't need to have like a super good understanding of this docker compose file.

But if you want to customize your stack or even help me by making contributions to local AI package, this is the main place to make changes. And so for example, I can go down to flowwise and I can see that the port is 3001. Or if I go down to let's say N8N,

we can see that the port is 5678. And so the port is always going to be there somewhere in the service that you have set up. Like for the Langfuse worker, it's 3030. That's more of a behind-the-scenes kind of service. But let me just find one more example for you here. Um yeah,

like Reddus for example is 6379. So you can see the ports in the Docker Compose as well. I just want to call it out just to at least get you a little bit comfortable and familiar with the Docker Compose file in case you want to customize things. But the main thing is just

leveraging what you see here in Docker Desktop. Last thing in Docker Desktop really quickly, if you want to bring more local large language models into the mix, you can do it without having to restart anything. You just have to find the Olama container in the Docker Compose stack. Head on over to the

exec tab. And now here we can run any commands that we'd want. We're directly within the container here. And we can use Lama commands just like we did earlier on our host machine. And so for example, I ran Lama list already. So I can see the large language models that have already been

pulled in my Olama container. If I want to pull more, I can just do Olama pull and then find that ID for the model I want to use on the Olama website. And like I said, you don't have to restart anything. If I pull it here it's now in the container and I

can immediately start using it in Open Web UI or N8N. We'll see that in a little bit. And so that's just really important because a lot of times you're going to want to start to use different large language models and you don't want to have to restart anything. The ones that are brought

into the machine by default is it's determined by this line right here. So if you want to change the ones that are pulled by default, I just have Quinn 2.57B instructs like a really small lightweight one that I have brought into your Lama container by default. Uh if you want to add in

different ones, you can just update this line right here to include multiple Olama pulls. And so that way you can bring in Quen 3 or Mistral 3.1 small whatever you want. This is just the one I have by default. And then all the other ones that you saw in my list here I've

pulled myself. All right. Now that we have the local AI package up and running, it is time to build some agents. Now, we get to use our local AI package to actually build out an application. And so, I'm going to start by introducing you to Open Web UI, and we'll use it to

talk to our Olama LLM. So, we have an application kind of right out of the box for us. Then I'll dive into building a local AI agent with N8N even connecting it to Open Web UI. So we have this custom agent that we built in N8N and then we immediately have a really

nice UI to chat with it. And then we'll transition to Python building the exact same agent in Python as well. Like I said, I want to focus on both no code and code to really make this a complete master class so that whether you want to build with N8N or Python, you can

see how to connect to our different services that we have running locally like Superbase and CRXNG and Open Web UI. So we'll cover all of that and then I'll get into deployments after this. But yeah, let's go ahead right now focus on open web UI and building out some agents. So, back over

in Open Web UI remember this is localhost port 8080. You want to set up your connection to Olama so we can start talking with our local LLMs in this nice interface. And so bottom left, go to the admin panel then go to settings and then the connections tab. Here we can set up

our connections both to OpenAI with our API key, which we're not going to do right now, but then also the Olama API. This is what we want to set up. Now, usually by default, this value is just localhost. And this is actually wrong. This is something that is so important to understand. And

this will apply when we set up credentials in N8N and Python as well. When you are within a container, localhost means that you are referencing still within the container. Open web UI needs to reach out to the Olama container, not itself. So localhost is not correct here. This is generally the default just

because open web UI assumes that you're running on your machine and so then you would also have Lama running on your machine. So local host usually works when you're outside of containers. But here we have to change this. This is super important to get right. And so there are two options we have.

If you are running on a Mac or AMD on Windows and you want to use Lama running on your machine not within a container, then you want to do host.doccker.in. This is the way in docker to tell the container to look outside to the host machine where you're running the containers and you're

running separately. Very important to know that. And then if you are running Olama in the container like I am doing. I have Ola running in my Docker desktop. You want to change this to Olama, you're specifically calling out the service that is running the Olama container in your Docker Compose stack. And the

way that we know that this is the name specifically is because we just go back to our allimportant Docker Compose file. Olama. So whenever there's an X and a dash, you just ignore that. It's just the thing after it. So, ola is the name of our service running the container. And then if

we wanted to connect to something else like flow-wise, flow-wise is the name of the service. Open WebUI it's open- web UI. All of these tople keywords, these are the names when we want our containers to be talking to each other. And all of this is possible because they are within the same Docker

network. And so I'll just show you that so you know what I'm talking about here. If I go back to Docker Desktop, we have this local AI compos stack. All of these containers can now communicate internally with each other by referencing the names like Reddus or CRXNG. So, we'll be seeing that a

lot when we're building out our agents as well. So, I wanted to spend a couple minutes to focus on that. And so, you can go ahead and click on save in the very bottom right. I know my face is covering this right now, but you have a save button here. Make sure you

actually do that. Um, and for this API key, I don't, know why, it's, asking, me, to, fill, it out. I don't really care about connecting to open AI. So I'll just put some random value there and click save. And then boom, there we go. We are good. And then a lot of times

with open web UI, it also helps to refresh otherwise it doesn't load the models for some reason. So I just did a refresh of the site here. Control F5. And then now we can select all of the local LLMs that we have pulled in our Olama container. And so for example, I can

do Quinn 2.57B. That's the one that I just have by default. I can say hello. And it's going to take a little bit cuz it has to load this model onto my GPU just like we saw with quen 3 earlier. But then in a second here we'll get a response. And there are

actually multiple calls that are being done here. We have one to get our response, one to get a title for our conversation on the lefth hand side. And then also if you click on the three dots here, you can see that it created a couple of tags for this conversation. So couple of

things that are fired off all at once there. And I can test conversation history. What did I just say? So yeah, I mean everything's working really well here. We have chat history, conversation history on the lefth hand side. There's so much that we get out of the box. And so I wanted to

show you this really quickly. Now we can move on to building an agent in N8N. And I'll even show you how to connect it to Open Web UI as well through this N8N agent connector. Really exciting stuff. So let's get right into it. So I'm going to start really simple here by building

a basic agent. The main thing that I want to focus on is just connecting to our different local AI services. So I am going to assume that you have a basic knowledge of N8N here because this is not an N8N master class. And so I'm starting with a chat trigger so we can

talk to our agent directly in the UI. We'll connect this to open web UI in a bit as well. And then I want to connect an AI agent node. And so what we want to do is connect for the chat model and then local superbase for our conversation history, our agent memory. And

so for the chat model I'm going to do lama chat model. I'm going to create brand new credentials. You can see me do this from scratch. The URL that you want for the base URL is exactly the same as what we just entered into open web UI. And so if you are running

Olama on your host machine like an AMD on Windows or you are running on a Mac or you just don't want to run the Olama container then it is host.doccker.in. And then if you are referencing the Olama container, we just reference Olama. That's the name of the service running the Olama container in

our stack. And then the port is 11434 by default. And you can test this connection. So it'll do a quick ping to the container to make sure that we are good to go. And I'll even show you what that looks like. So right here in my Olama container, I have the logs up.

And the last two requests were just a simple get request to the root endpoint. We have two of those right here. And if I click on retry and I go back to the logs, boom, we are at three now. So it made three requests. So it's just making that simple ping each time

to make sure the container is available. And so I'm going to go ahead and click on save and then close out. So now we have our credentials and then we can automatically select the model that we have loaded now in our container. And so just to keep things really lightweight I'm going to

go with the 7 billion parameter model right now from Quen 2.5. Cool., All right., So, that, is, everything that we need to connect Olama. It is that easy. And then we could even test it, right, now., So,, I'm, going to, go, ahead and save this workflow. And I'm going to just say hello.

And uh we don't need the conversation history or tools or anything at this point. We're already getting a response here from the LLM. It's working on loading the model into my GPU as we speak. And so there we go. We got our answer looking really good. Cool. So now we can add memory

as well. So I'm going to add Postgress because remember Superbase uses Postgress under the hood. And then I'm going to create brand new credentials here. And this is actually probably the hardest one to set up out of all of the credentials for connecting to our local AI service. And so I'm going to

show you what the Docker Compose file looks like just that it's clear how I'm getting these different values. And so I'll point out all of them. So the first one for our host it is DB because this is the name of the specific Superbase service that we have that is the underlying Postgress

database. And I can show you how I got that really quick. If you go to the superbase folder that we pull when we run that start services script, I go to docker and then docker compose. If I search for db and there's quite a few dependencies on db here. So let me find

the actual reference to it. Where is db? Here we go. So yeah, it's really short. Uh db is the name of our service that actually is the superbase DB. So this is the container name that this is what you'll see in docker desktop. But then this is the underlying service that we want

to reference when we have our containers communicating with each other. Like in this case we have our N8N container talking to our superbase database container. And then the database and username are both going to be Postgress. Those are the values that we have by default. If you scroll down a bit in thev

you can see these right here. The Postgress database is Postgress and the user is also Postgress. And you can customize these things but these are some of the optional parameters that I didn't touch in the setup with you. And so you can just leave those as is. Now the Postgress password, this is

one of them that we set. That was the first superbase value that we set there. Make sure you have that from what you have in thev. And then everything else you can kind of leave as the defaults here. The port is going to be 5432. So that is everything for setting up our

connection to Postgress. You can test this connection as well. And then we can move on to adding in some tools and things like that as well. But yeah, this is like the very first basic version of the agent that I wanted to show you. And hopefully with this you can see how no

matter the service that you have running in the local AI package. It's very easy to figure out how to connect to it both with the help of N8N because N8N always makes it really easy to connect to things. Then also just knowing that like you just have to reference that service name that

we have for the container in the Docker Compose stack. That's how we can talk to it. So you could add in quadrant or you could add in language. Like you can connect anything that you want into our agent here. And so now we have conversation history. Next up, I want to show you

how to build a bit more of a complicated agent with N8N using some tools. And then also I'm going to show you how to connect it to Open Web UI. And so right now this is a live demo. Instead of connecting to one of the Olama LLMs, I'm going straight to N8N. I

have this custom N8N agent connector. And so we are talking to this agent that I'll show you how to build in a little bit. This one has a tool to use CRXNG for local and private web search. This is one of the platforms that we have included in the local AI package. And

so this response is going to take a little bit here because it has to search the web. And the response that it generates with this question is pretty long. Like there we go. Okay. So we got the answer. It's pretty long. But yeah we are able to search the internet now with a

local agent. N8N connected to open web UI. We're getting pretty fancy here. And we also have the title that was generated on the left. And then we have the tags here as well. And so the way that this all works, I'm going to start by explaining how we can connect N8N to Open

Web UI. And this is just crucial. Makes it so easy for us to test agents locally as we are developing them. And so if you go to the settings and the admin panel in the bottom left and go to functions, open web UI has this thing called functions which gives us the ability

to add in custom functionality kind of as like custom models that we can then use like you saw with the N8N agent connector. And so what I have here is this thing that I call the N8N pipe. And I'll have a link to this in the description as well. I created this myself

and I uploaded it to the open web UI directory of functions. And so you can go to this link right here. You can even just Google the N8N pipe for open web UI. And then you click on this get button. It'll just have you enter in the URL for your open web UI.

So I can just like paste in this right here. Click on import to open web UI and it'll automatically redirect you to your open web UI instance. So you'll have this function now. And we don't have to dive, into, the, code, for, all, how how, all of this works. I worked pretty hard

to create this for you. Uh actually quite a while ago I made this. And the thing that we need to care about is configuring this to talk to our N8N agent. And so if you click on the valves, the setting icon in the top right, there are a few values that we have

to set. And so now I'm going to go over to showing you how to build things in N8N. Then all of this will click and it'll make sense. I right now looking at these values, you're probably like, how the heck do I get all of these? But don't worry, we'll dive into all

of that. But first, let's go into our N8N agent. I'll explain how all of this works. So, first of all, we have our chat trigger that gives us the ability to communicate with our agent very easily in the workflow. We have a new trigger now for the web hook. And so this is

turning our agent into an API endpoint. So, we're able to talk to it with other services like open web UI. And so to configure the web hook here you want to make sure that it is a post request type. And then you can define a custom path here. Whatever you set here is

going to determine what our URL is. So we have our test URL. And then also if you toggle the workflow to active this is really important. The workflow in N does have to be active. Then you have access to this production URL. And this is actually the first value that we need to

set within the valves for this open web UI function. We have our N8N URL. And because this is a container talking to another container, we don't actually want to use this localhost value that it has here for us. We want to specify N8N because N8N again is the name of the service running

the N8N container in our Docker Compose stack. So N8N port 5678. And then this is the custom URL that we can determine based on this. And then the other thing that we want to do is set up header authentication. We don't want to expose this endpoint without any kind of security. And so

we want to set up some authentication. And so you can select header off from the authentication dropdown. And then for the credentials here, I'll just create brand new ones to show you what this looks like. The name needs to be authorization with a capital A. This has to be very specific. The name

in the top left and the name of your credentials. This can be whatever you want, but this has to be authorization. And then the value here the way that we want to format this is it's going to be bearer and then the and then a space and then whatever you want your bearer

token to be. So this is what you get to define, but it needs to start with a bearer capital B and a space. And then whatever you type after bearer space, this goes in as the NAN bearer token. So you don't include a bearer space here because that it's just assumed that it's

going to be like that. It's going to be prefixed with that. So you just type in like test off is what I have. So my bearer token is bearer test off like that. And then this is what I enter in for this field. Now I already have mine set up. So I'm just

going to go ahead and close out of this. And then the last thing that we have to set up for the web hook. And don't worry, this is the node that we spend the most time with. You want to go to the drop down here and change this to respond using the respond

to web hook node. very important because then at the end of our workflow and we get the response from our agent, we're going to send that back to whatever requested our API which is going to be open web UI in this case. And so that's everything for our configuration for the web hook.

Now the next thing that we have to do is we have to determine is open web UI sending in a request to get a response for our main agent or is it just looking to generate that conversation title or the tags for our conversation? Because like we were looking at earlier, I'm going

to close out of this for now and go back to a conversation, our last conversation here. We get our main response, but then also there is a request to an LLM to create a very simple title for our conversation and the tags that we can see in the top right. And so our

N8 workflow actually gets invoked three separate times for just the first message in a new conversation. And so we need to determine, are we getting a main response? Like should we go to our main agent or should we just go to a simple LLM that I have set up here to help generate

the tags or title? And so the way that we can determine that is whenever Open Web UI is requesting something like a title for a conversation, it always prefixes the prompt with three pound symbols, a space, and then the word task. And so we can key off of this. If the prompt starts

with this, and that prompt just is coming in from our web hook here. If it does start with it, then we're just going to go to this simple LLM, we're just going to be using Quen 2.514b instruct. We have no tools, no memory or anything like our main agent because we're just very

simply going to generate that title or the tags. And I can even show you in the execution history what that looks like. So in this case, we have our web hook that comes in. The chat input starts with the triple pound and task. And so sure enough, we are deeming it to be

a metadata request is what I'm calling it. And so then it then goes down to this LLM that is just generating some text here. We just have this JSON response with the tags for the conversation technology hardware and gaming. So we're asking about the price of the 5090 GPU. And then we do

the exact same thing to also generate the title GPU specs. And so exactly what we see here is the title of this last conversation. So I hope that makes sense. And then if it doesn't start with task and the triple pound and so it's actually our request. Then we go to our main

agent. We don't want our main agent to have to handle those super simple tasks. You can also just use a really tiny LLM. Like this would be the perfect case to actually use a super tiny LLM like um even like DeepSec R1 1.5B. You could because it's just such a simple task. Otherwise

though we are going to go to our main agent. And so I'm not going to dive into like all these nodes in a ton of detail, but basically we are are expecting the chat input to contain the prompt for our agent. And the way that we know to expect chat input specifically is

because going back to the settings for the function here with the valves, we are saying right here chat input. So you want to make sure that the value that you put in here for input matches exactly with what you are expecting from our web hook. And so chat input is the one that

I have by default. So you can just copy me if you want. Then we go into our agent where we're hooked into Olama and we've got our local superbase. I already showed you how to connect up all this and that looks exactly the same. The only thing that is different now is we

have a single tool to search the web with CRXNG. So it's a web search tool. I have a description here just telling it what is going to get back from using this tool. And then for the workflow ID, this is if I go to add a node here and I just go for

uh workflow tools, call N8N workflow tool. So this is basically taking an N8N workflow and using it as a tool for our agent. So this is the node that we have right here. But then I'm referencing the ID of this N8N workflow. So this ID because I'm going to just call the subworkflow

that I have defined below. And again, I don't want to dive into all the details of NAN right now and how this all works, but the agent is going to decide the query. What should I search the web with? It decides that and then it invokes this sub workflow here where we have

our call to CR XNG. So the name of the container service in our docker and compost stack is just CR XNG and it runs on port 8080. And then if you look at the CXNG documentation, you can look at how to invoke their API and things like this. So I'm just doing a

simple search here and then there are a few different nodes because what I want to do is I want to split out the search and actually I can show you this by going to an execution history where we're actually using this tool. So take a look at this. So in this case the

LLM decided to invoke this tool and the query that it decided is current price of the 5090 GPU. So this is going along with the conversation that we had last in open web UI. we get some results from CRXNG, which is just going to be a bunch of different websites. And so, we

don't have the answer quite yet. We just have a bunch of resources that can help us get there. And so, I'm going to split out. So, we have a bunch of different websites. We're going to now limit to just one. I just want to pull one website right now just to keep it

really, really simple because now we're going to actually visit that website. I'm going to make an HTTP request to this website, which yeah, I mean, if it's literally an Nvidia official site for the 5090, like this definitely has the information that we need. We're going to make a request to it, and then

we're also going to use this HTML node to make sure that we are only selecting the body of the site. So, we take out all the footers and headers and all that junk. So, we just have the key information. And then that is what we aggregate and then return back to our AI

agent. So it now has the content, the core content of this website to get us that answer. That is how we invoke our web search tool. And then at the very end, we're just going to set this output field. And that's going to be the response that we got back either from like

generating a title or calling our main agent. And this is really important. the output field specifically whatever we call it here we have to make sure that that is corresponding to this value as the last thing we have to set for the settings for our open web UI function. So output here has

to match with output here because that is what we're going to return in this respond to web hook. Whatever open web UI gets back it's getting back from what we return right here. So that is everything for our agent. I could probably dive in quite a bit more into explaining how this all

works and building out a lot more complex agents, which I definitely do with local AI in the Dynamis AI agent mastery course. So check that out if you are interested. I just wanted to give you a simple example here showing how we can talk to our different services like Olama, Superbase, and Seir

XNG. And then also open web UI as well. So once you have all these settings set, make sure of course that you click on save. It's very, very important. These two things at the bottom don't really matter, by the way. But yeah, click on save once you have all of the settings there.

And then you can go ahead and have a conversation with your agent just like I did when I was demoing things before we dove into the workflow. And by the way this NAN agent that works with Open Web UI, I have as a template for you. You can go ahead and download that

in this GitHub repository where I'm storing all the agents for this masterass. So we have the JSON for it right here. You can go ahead and download this file. Go into your N8N instance. Click on the three dots in the top right once you've created a new workflow. Import from file and then

you can bring in that JSON workflow. You'll just have to set up all your own credentials for things like Lama and Superbase and CRXNG. But then you'll be good to go and you can just go through the same process that I did setting up the function in open web UI and it'll be

with like 15 minutes you'll have everything up and running to talk to N8N in open web UI. Next up I want to create now the Python version of our local AI agent. And so this is going to be a onetoone translation. Exactly what we built here in NN, we are now going to

do in Python. So I can show you how to work with both noode and code with our local AI package. And so this GitHub repo that has the N workflow we were just looking at and that OpenAI compatible demo we saw earlier, this has pretty much everything for the agent. So most of

this repository is for this agent that we're about to dive into now with Python. And in this readme here, I have very detailed instructions for setting up everything. And a lot of what we do with the Python agent, especially when we are configuring our environment variables, it's going to look very similar to

a lot of those values that we set in N8N. Like we have our base URL here, which you'd want to set to something, you know, like HTTP lama port 11434. We just need to add this /view one which I guess is a little bit different but yeah, I've got instructions here for setting

up all of our environment variables, our API key, which you can actually use OpenAI or Open Router as well with this agent, taking advantage of the OpenAI API compatibility. This is a live example of this because you can change the base URL, API key, and the LLM choice to something from Open Router

or OpenAI, and then you're good to go immediately. It's really, really easy. We will be using Olama in this case, of course, though. And then you want to set your superb basease URL and service key. You can get that from your environment variables. Same thing with CRXNG with that base URL. We'll set

that just like we did in N8N. We have our bearer token like in our case was test off. It's just whatever comes after the bearer and the space. And then the OpenAI API key you can ignore. That's just for the compatible demo that we saw earlier. This is everything that we need for

our main agent now. And so we're using a Python library called fast API to turn our AI agent into an API endpoint just like we did in N8N. And so fast API is kind of what gives us this web hook both with the entry point and the exit for our agent and then

everything in between is, going to, be, the, logic, where, we, are using our agent. And I'm going to be using paidantic AI. It's my favorite AI agent framework with Python right now. Makes it really easy to set up agents and we'll so we'll dive into that here. And I don't want to get

into the nitty-gritty of the Python code here because this isn't a master class on specifically building agents. I really just want to show you how we can be connecting to our local AI services. This agent is 100% offline. Like I could cut the internet to my machine and still use everything here. So

we create our Superbase client and the instance of our fast API endpoint. I have some models here that define the the requests coming in, the response going out. So we have the chat input and the session ID just like we saw in N8N. And then the output is going to be this output

field. And so that corresponds to exactly what we're expecting with those settings that we set up in the function in open web UI. So this Python agent is also going to work directly with open web UI. And then we have some dependencies for our Pantic AI agent because it needs to have an

HTTP client and the CRXNG base URL to make those requests for the web search tool. And then we're setting up our model here. It's an OpenAI model, but we can override the base URL and API key to communicate with Olama or Open Router as well like we will be doing. And then we

create our Pantic AI agent just getting that model based on our environment variables. I've got a very simple system prompt and then the dependencies here because we need that HTTP client to talk to CR XNG. And then I'm just allowing it to retry twice. So if there's any kind of error that comes

up, the agent can re retry automatically, which is one of the really awesome things that we have in Pyantic AI. And then I'm also creating a second agent here. This is the agent that is going to be responsible like we have in NADM for handling the metadata for open web UI like conversation

titles and tags for our conversation. And so it's an entirely separate Asian because we just have a another system prompt. In this case, I'm just doing something really simple here. Uh we don't have any dependencies for this agent because it's not going to be using the web search tool. And then for the

model, I'm just using the exact same model that we have for our primary agent. But like I shared with N8N, you could make it so that this is like a much smaller model, like a one or three billion parameter model because the task is just so basic or maybe like a 7 billion

parameter model. So you can tweak that if you want. Just for simplicity sake, I'm using the same LLM for both of these agents. And then we get to our web search tool. So in Pantic AI, the way that you give a tool to your agent is you do at@ and then the name

of your agent and then tool and then the function that you define below this is now going to be given as a tool to the agent. And then this description that we have in the doc string here that is given as a part of the prompt to your agent. So it knows when

and how to use this tool. And so the exact, you know, details of how we're using CRX and G here, I won't dive into, but it is the exact same as what we did in N8N where we make that request to the search endpoint of CRX andG. We go through the page results

here. We limit to just the top three results or I could even change this to make it even simpler and just the top result. So we have the smallest prompt possible to the LLM. And then we get the the content of that page specifically. And then we return that to our AI agent

with some JSON here. So now once it invokes this tool, it has a full page back with information to help answer the question from the user. It has that web search complete now. And then we have some security here to make sure that the bearer token matches what we get into our API

endpoint. So that's that header authentication that we set up in N8N. So this part right here where we're verifying the header authentication that corresponds to this verify token function. And then we have a function to fetch conversation history to store a new message in conversation history. So both of these are just making

requests to our locally hosted superbase using that superbase client that we created above. And then we have the definition for our actual API endpoint. And so in N8N we were using invoke N8N agent for our path to our agent. So this was our production URL. In this fast API endpoint, our endpoint is

slashinvoke python agent. And then we're specifically expecting the chat input and session ID. So that is our um chat request request type right here. And then sorry I highlighted the wrong thing. We have our response model here that has the output field. So we're defining the exact types for the inputs and the

outputs for this API endpoint. And then we're also using this verify token to protect our endpoint at the start. And then the key thing here, if the chat input starts with that task then we're going to call our metadata agent. And so it's just going to spit out the title or the tags,

whatever that might be. Otherwise, we're going to fetch the conversation history, format that for Pyantic AI, store the user's message so that we have that conversation history stored, create our dependencies so that we can communicate with CRXNG, and then we'll just do agent.run. We'll pass in the latest message from the user, the

past conversation history and the dependencies that we created. So it can use those when it invokes the web search tool and then we just get the response back from the agent and we'll you can print that out in the terminal as well and then we'll just store it in superbase and then return

the output field. So I'm going kind of fast here. I there definitely a lot more videos on my channel where I break down in more detail building out agents with podantic AI and turning them into API endpoints and things like that. Um but yeah, just going a little bit faster here. here. And

then the last thing is with any kind of exception that we encounter, we're just going to return a response to the front end saying that there was an issue and then specifying what that is. And then we are using Ubicorn to host our API endpoint specifically on port 8055. So that is everything

for our Python agent exactly the same as what we set up in N8N. And now going to the readme here, I'll open up the preview. The way that we can run this agent, we just have to open up a terminal just like we did with the OpenAI compatible demo. I've got instructions here

for um setting up the database table, which this is using the same table as the one in N8N and N8N creates it automatically. So, if you have already been using the N8N agent you don't actually have to run this SQL here. Um, and then you want to obviously set up your environment variables

like we covered. Uh, open your virtual environment and install the requirements there. And then you can go ahead and run the command python main.py. And so this will start the API endpoint. So it'll just be hanging here because now it's waiting for requests to come in on a port 8055. And so what

I can do is I can go back to open web UI. I can go to the admin panel functions. Go to the settings. I can now change this URL. So everything else is the same. I have my bearer token, the input field, and the output field the same as N8N. The only thing

I have to change now is my URL. And so I know this is an N8N pipe and I have N8N in the name everywhere, but this does work with just any API endpoint that we have created with this format here. And so I'm going to say for my URL, it's actually going to

be host.doccker.in because I have my API endpoint for Python running outside on my host machine. So I need my open web UI container to go outside to my host machine. And then specifically the port is going to be 8055. And then the endpoint here, I'm going to delete this web hook here because

it's invoke-python- agent., Take, a, look, at, that., All right. Boom. So I'm going to go ahead and save this. And then I can go over to my chat. And it says n agent connector here still. But this is actually talking to my Python agent now. So I'll go ahead and start by asking

it the exact same question that I asked the N8N agent. And I do have this pipe set up to always say that it's calling nan, but this is indeed calling our Python API endpoint. And we can see that now. So there we go. We got all the requests coming in, the response from

the agent, and then also the metadata for the title and the tags for the conversation. Take a look at that. So we got our title here. We have our tags, and then we have our answer. It's a starting price of $2,000, which it's a lot more right now. The starting point, the starting

price is kind of misleading, but like yeah, this is a good answer. and it did use CRXNG to do that web search for us. This is really really neat. Now, the last thing that we want to do for our Python agent before we can work on deploying things to the cloud, to a

private server in the cloud is we want to containerize it. Now, the reason that we want to do this, and this is the Docker file that I have set up to turn our Python agent into a container just like our local AI services, is if we have our agent containerized, then we can

have it communicate within the Docker network just like we have our different local AI services communicating with each other. Because right now running directly with Python to communicate with Olama, for example we need our URL to be localhost, not Olama. Remember, you can only use the specific name of the container service when

you are within the docker compose stack. And so we'd have to actually say localhost right now. But if we add the container for the agent into the stack as well, then we can communicate directly within the private network. Like I can say lama and then for sir xng I could use this URL

instead. Right now we have to actually use localhost port 8081. And so it's really nice for security reasons and just to make your deployment um in a nice package to have the agents that you're running in the same network as your infrastructure. And so that's what we're going to do right now. And

so within the read me that I have for instructions on setting up everything. I have the instructions that we follow to run things with Python. I also have the instructions to run it with Docker. And so all you want to do is run this single command. It's actually very easy because I have

this Docker file set up to turn our agent into a container and I've got security and everything taken care of. We're running it on port 8055 just like we did with Python. And then I have this very simple Docker Compose file. It's just a single service that we're going to tack on to

all of the other services that we already have running for the local AI package. And I'm calling this one the Python local AI agent. And so we're using all of our environment variables from our ENV just like we did with the local AI package. And then what I have at the top here

is I am including the docker compose file for the local AI package. So that just kind of solidifies the connection there. Otherwise, you'll get this kind of weird error that says there are orphaned containers when you run this, even though they aren't actually. And so this is optional. You'll just get an orphan

container warning that you can ignore. But if you don't want to have that warning, you can include this right here. You just have to make sure that this path corresponds to the path to your docker compose in the local AI package. So in my case, I just had to go up to directories

and then go into the local AI package folder. So yeah, you this is optional but I want to include this here just to make things in tiptop shape for you. So yeah, this is the docker compose. And then what we can do now is I'll go back over to my terminal and I

will paste in this command. And what this will do is it will start or restart my Python local AI agent container. And make sure that you specify this here because if you don't then it's going to try to rebuild the entire local AI package because we have this include. So very important you

want to just rebuild or build for the first time this agent container. And so I'll go ahead and run this and it's going to give me those flow-wise warnings. So I don't have my username and password set, but remember we can ignore those. But anyway, it's going to build the Python local AI

agent container here. And there's a couple of steps that it has to do. It has to update some internal packages and then also install all of the pit packages we have for our Python requirements for things like fast API and Pantic AI. So it'll take a little bit to complete usually just a

minute or two. And so I'll go ahead and pause and come back once this is done. And there we go. Your output should look something like this. It goes through all the build steps and then it says that the container is started at the bottom. And this is now in our local AI

Docker Compose stack. So going back over to Docker Desktop. It'll take a little bit to find it here because there are so many services that we have here. But if we scroll down okay, there we go. At the bottom here we have our Python local AI agent waiting on port 8055 just like

when we ran it directly with Python, but now it is within a container that is directly within our stack. And so now, like I was saying, this is super important, so I'm hitting on it again. Now when we set up our environment variables for our container, we are going to be referencing the

service names of our different local AI services like circ or lama instead of localhost. And so this whole like localhost versus host.docer.ernal versus using the service name, that's the thing I see people get tripped up on the most when they're configuring different things in a Docker environment like the local AI package. That's

why I'm spending a good amount of time really hammering that in because I want you to get it right. And of course, if you have any issues that come up with this, just let me know. I'd love to help walk you through what exactly your configuration should look like. And so we have

our agent now up and running in a container. And I'm not going to go and demo this again right now because the next thing that we're going to move into doing and then I'll give a final demo here is deploying everything to a private server that we have in the cloud. All right.

So, we have really gotten through all of the hard stuff already. So, if you have made it this far, congratulations. you really have what it takes to start building AI agents with local AI now and the sky is the limit for what you can accomplish. And so the last thing that I want

to really focus on here in this master class is taking everything that we've been building on our own computer with our infrastructure and our agents and deploying it to a private machine in the cloud because then we can have our entire infrastructure and agents running 24/7. We don't have to rely on having

our own computer up all the time. It's really nice to have it there because then we can also share it with other people as well. So local AI is still considered local as long as it's running on a machine in the cloud that you control. And so this is not just going to

open AAI or Superbase and paying for their API. This is still us running everything ourselves on a private server. That's what I'm going to show you how to do right now. And this process that I cover with you is going to work no matter the cloud provider that you end up choosing. And

there are some caveats to that that I'll explain in a little bit. But yeah, you can pick from a lot of different options. So the cloud platform that we will be deploying to today is Digital Ocean. I use Digital Ocean a lot. It's where I deploy most of my AI agents. So I

highly recommend it. And the best part about Digital Ocean is they have both GPU machines if you need to have a lot of power for your local LLMs and they have very affordable CPU instances. If you want to deploy everything for the local AI package except Olama, you can definitely go a more

hybrid route if you don't want to pay a lot because these GPU instances in the cloud can be pretty expensive like one, two, even $5 per hour. So, what you can do with a hybrid setup is deploy everything in the local AI package. So at least, you, have, all, that, locally, and you're

not paying for those subscriptions. But then you could still use something like OpenAI, Open Router or Anthropic for your LLMs. So, Digital Ocean gives us the ability to do both and we'll dive into that when we set things up. Another really good option for GPU instances is Tensor Do. Tensor Do is not

as nice looking to me as Digital Ocean. I generally feel like I have a better experience with Digital Ocean, but I have deployed the local AI package to Tensor Do before on a 4090 GPU that they offer for 37 cents an hour. It's very affordable for GPU instances. And so, this is a

good platform as well. And then also if you're okay with not running Olama on a GPU instance, like you just want a very affordable, way, to, host, everything, in a local AI package except the LLMs, then you can use Hostinger. Hostinger is another really really good option. super super affordable like $7 a

month for a KBM2 which I'd recommend getting if you want to deploy everything except Olama because the requirement for the local AI package except for running the more resource intense local LLMs is you have to have 8 GB of RAM. So don't get a cloud machine that has four or 2 GB. You

want to have 8 GB of RAM then you'll be good to go. So you can literally do it for $7 a month through Hostinger and it's going to be something like $28 a month through Digital Ocean unless you want a GPU instance. So I just want to spend a couple minutes talking about

different platform options. The one thing I will say is that the local AI package runs as a bunch of Docker containers, right? And so what you have to avoid is using a platform like RunPod. So RunPod is a platform for running local AI. The problem is when you pay for a GPU instance,

you don't actually get the underlying machine. You're just sshing into a container. So you're accessing a container. And I'll just save you the pain right now. It is so hard and basically impossible to run Docker containers within Docker containers. So, you really can't run the local AI package on RunPod. There are other

platforms as well like Lambda Labs is another one that I've used before. not for the local AI package for other things but this also runs containers like you're accessing a container so you can't do the local AI package vast.ai AI is another option, but this also is you're renting a GPU, but it's

you're accessing a container. So, you again can't run the local AI package. And so based on the platform that you choose you have to make sure that you are accessing the underlying machine when you rent a GPU instance like Digital Ocean is the one that I will be using. You could use a

GPU instance through the Google cloud or Azure or AWS if you want to go more enterprise. Those all give you access to the underlying machine. It's your own private server just like we have in Digital Ocean. So you can use that to deploy the local AI package and the agent that we built

with Python. So that's what we're going to do right now. So once you are signed into Digital Ocean and you have your profile and billing set up and you have a project created or you can just use the default one, now we can go ahead and create our private server in the cloud

to host the local AI package and our agent. And so you can click on create in the top right. And there are two options here. If you want a CPU instance, so that hybrid approach where you're hosting everything except for the LLMs, you can select a droplet. Otherwise, what we're going to be

doing right now so I can demo the full full thing is we will create a GPU droplet. Now, these are going to be more expensive. Like I said like running an H100 GPU is $3.40 an hour. It's pretty expensive. But like I said at the start of this master class I know so

many businesses that are willing to put tens of thousands of dollars per year into running their own infrastructure and LLMs. And that biggest cost that contributes to that being tens of thousands of dollars is having a GPU droplet that is running 247 in the cloud. So the hybrid approach I definitely recommend if

you don't want to pay more, you could go as low as $7 a month with Hostinger. So, there's a very wide range of options for you depending on what you want to pay hosting the package, LLMs, and your agents. And the other thing I will say is that if you want to, you

could just create this instance for a day and poke around with things and then tear it down. So, you only have to pay, you know, like 20 bucks or something like that. So there's a lot of different options for flexibility here. And so, I'm going to pick the Toronto data center because there's

more options for GPUs available here and it's relatively close to me. And then for the image, I'll select AI/ML ready and it's recommended because you get the Linux bundled with all the required GPU drivers and it does run the Ubuntu distribution of Linux. And so this process that I'm going to walk you

through for deploying local AI package to the cloud is going to work for any Ubuntu instance that you have running on AWS or Hostinger or Tensor Do. It's just a very standard distribution of Linux. And then for the GPU, there are a couple of different options that we have here with Digital Ocean.

H100 is an absolute beast. 80 GB of VRAM, so it could easily run Q4 large language models, over a 100 billion parameters, even 240 GB of RAM. So, I'm not going to run this one. I'm just kind of pointing out that this is an absolute beast. I think the one that I'm going

to choose here is going to be the RTX 6000 ADA. So, it's 48 GB of VRAM. So, this is enough to run 70 billion parameters or smaller of LLMs at a Q4 quantization and it comes with 64 GB of RAM and it's going to be about $1.90 per hour. So, I'm going to

select this and then I have an SSH key that is created already. If you don't have an SSH key, then you can click on this button to add one. And then you can follow the instructions on the right hand, side, here., No matter, your, OS,, they got instructions to help you out. You

just have to paste in your public key and then give it a name. So, I've got mine added already. And then the only other thing that I really have to select here is a unique name. So, I'll just say local AI package. And I'll just say GPU because I already have the regular

version just deployed on a CPU instance. And then for my project, I will select Dynamis. I can add it along with my other instance that I've got up and running. And there we go. So now I can go ahead and just click on create GPU droplet. It is that easy to get our

instance ready for us to access it and start installing everything and getting everything up and running just like we did on our computer. And so I'll go ahead and pause and come back once our machine is created in just a few minutes. And boom, there we go. Just after a minute, we have

our GPU droplet up and running. And so the one thing I will say is I had to request access to create a GPU instance on the Digital Ocean platform. However, they approved it in less than 24 hours. So, it's very easy to get that if you do want to create a GPU instance.

Otherwise, you can just create one of their normal droplets, one of their CPU instances. Now, before we connect to this machine the one thing that you want to take note of is the public IPv4 address. We'll use this to set up subdomains in a little bit. And so, this is how we get

to it for a GPU droplet. For a CPU droplet, it looks a little bit different. You'll usually see the IPv4 somewhere at the top right here. And so, take note of that. Save it for later. We'll be using that in a little bit. And then to connect to our droplet, we can either

do it through SSH with our IPv4 and the SSH key that we set up when we configured this instance or we can access the web console. For a CPU instance, usually you go to like an access tab and then you can launch the web console. For the GPU instance, I can just click

this to launch it right here. So we have a separate window that comes up and boom we now have access to our instance. It is that easy to get connected. And now we can go through the same process that we did on our computer to install the local AI package. Now there are

some different steps that we have to take and that's why I'm including this at the end of the master class especially. Um so if you scroll down in the read me here there are some specific instructions for deploying to the cloud. And so you have to make sure that you have a Linux

machine preferably on the Ubuntu distribution which is that is what we are using. And then there are a couple of extra steps. And so the first thing that we have to set up is our firewall. We have to open up a couple of ports so that we can access our machine from the

internet. Set up our subdomains for things like N8N and Open Web UI. And so you want to take this command UFW enable. I'll just go ahead and paste it in. And so we are going to and you can just type Y to continue here. It's going to disrupt SSH connections, but we don't

really care. So UFW enable. So we're enabling the firewall. And then you want to copy this command to allow both ports 80 and 443. And so 80 is HTTP and then 443 is HTTPS. And then you can just do the last command here, UFW reload. So now we have those ports available for

us to communicate with all of our services. And so this is the entry point to Caddy. Caddy is the service in the local AI package that is going to allow us to set up subdomains for all of our services. is and so any kind of communication to our droplet is going to go

through caddy and then caddy will distribute to our different services based on the port or the subdomain that we are using. So this is called a reverse proxy. You've probably heard of like EngineX or traffic before. Caddy is something very much like that. And it also makes it so that we can get

HTTPS so we can have secure endpoints set up automatically and it manages that encryption for us. It's a very beautiful platform. So, let me scroll back down to the specific steps for deploying to the cloud. There is a quick warning here about how Docker manages ports and things, but this is as secure

as we possibly can make it. So trust me, we've put a lot of effort and I actually had someone from the Dynamis community, um, Benny right here. He actually helped me a lot with security for the local AI package. So, thank you Benny, for helping out with that. We're really making sure that

because local AI like the whole thing is like you want to be private and secure and so we're making sure that this package handles all the best practices for that. So very much top of mind for us. Um and then we can go ahead and go through the usual steps for setting up

the local AI package. The only other thing we have to do that's unique for cloud is we have to set up a records for our DNS provider so we can have our subdomain set up for our different services. So we'll get into that in a little bit. But first I just want to

get the local AI package up and running. And so I'm going to go ahead and paste this command here to clone the repository. Git comes automatically installed with our GPU droplets. And then I can change my directory into the local AI package. And let me zoom in on this a little bit here

so it's very easy for you to see because now then what I want to do is I want to copy the.env.ample file to a new file called. So then if I do an ls command so we can see all the files that are available in our directory. We I guess it doesn't show

um I do ls- a there. Now we can see the env.env.example. example. And so now I can do nano.env. This is going to give us a basically a text editor directly in the terminal here so that we can set all of our environment variables just like we did with the local AI package

on our computer. So this time I'm not going to go into the nitty-gritty details of setting up all these environment variables because it is the exact same process. In fact, you can literally reuse all of the secrets that you already set up when you hosted it on your own computer as long as

those are actually secure. Like I know a lot of times you might just do some kind of placeholder stuff when it's just running on your computer and then you want it more secure in the cloud. So make sure you have real values for everything, but yeah, you can reuse a lot of the

same things. Um though for best security practice, you probably do want to make everything different. But yeah, the one thing that I want to focus on with you here that does change is our configuration for Caddy. Now that we are deploying to the cloud, we want to have subdomains for our different services.

And, so, like, NN, for example,, we, want, to set the host name for that. You want to do the same thing for N8N open web UI superbase and then your let's encrypt email. Obviously you want to uncomment that as well because this is the email that you want to set for your SSL

encryption. And so I'm just going to do coal dynamis.ai. And you can just set this to whatever email that you want to use. And so basically what you want to do here is just uncomment the line for each of the services that you want to have subdomains created for. So, if you're also

using Flowwise, which I'm just not in this master class here, but if you are, then you want to uncomment this line as well. If you're using Langfuse then you uncomment this line. I'm going to leave them commented right now just for simplicity sake. The two that I would generally recommend not uncommenting ever

is Olama and CRXNG. We don't really want to expose them through a subdomain because we're just going to use them as internal tooling for our agents and applications that we have running on this server. So, we want to keep those nice and private. But for everything that we do want to expose that

is protected with a username and password like N8N open web UI and superbase we can uncomment those. And so we got that set up now. But we have to obviously provide real values for them as well. And so for example I'm just going to say nyt for YouTube dynamis and then I'll do.

So you want to define your exact URL that you want to have for this domain. Obviously, it has to be a domain that you control because we'll go and we'll set up the records in the DNS in a little bit. And so, I'll do the exact same thing for open web UI. So,

it's open web UI and I'm just doing YT because I already have the local AI package hosted on my domain. And so, I can't do just open web UI because it's already taken. So, open web UIT.dynamis.ai. And then finally, for Superbase, it'll be superbaseyt.dynamis.ai. Boom., All right., There, we, go., So,, go ahead

and take care of this. set up the rest of your environment variables and then we can go ahead and move on. And the way that you exit out of this and save your changes is you do controll X or command X on Mac, type Y and then hit enter. So again that is

controll X then type Y then press enter. That is how you exit out. And so now if I do a cat of the env this is how you can print it out in the terminal. So we can verify that the changes that we made like everything for caddy is indeed made. So do

that. Also change all the other environment variables, as, well., I'm, going to, do, that off camera and come back once that is taken care of. All right. So my environment variables are all set. Now the very last thing we have to do before we start all of our services is we need to

set up DNS. And so remember, copy your IPv4 address and then head on over to your DNS provider. And so this process is going to look very similar no matter the DNS provider that you have. Like I'm using NameCheep here. A lot of people use Hostinger or Bluehost. You are able to with

all these providers go to something that is usually called like advanced DNS or manage DNS and then you can set up custom A records here which we're going to do to set up a connection for all of our subdomains to the IPv4 of our digital ocean droplet or whatever cloud provider you are

using. And so I'm going to go ahead and click on add new record. It's going to be an A record for the host. It's going to be the subdomain that I want. So, N8NYT for example. And then for the IP address, I just paste in the IPv4 of my Digital Ocean GPU droplet.

And then I'll go ahead and click on the check here to save changes. And then I'll just go ahead and do the same thing for open web UIT. I can't forget the YT. There we go. And then for you, it might be more than just three, but for me, the only other one

that I have here right now is Superbase because I'm just keeping it very, very simple. So, superbase yt and then paste in the IP again. Okay, there we go. Boom., All right,, so, we, have, all, of, our records set up. And it's very important to do this before you run things for the

first time because otherwise Caddy gets very confused. It tries to use these subdomains that you don't actually have set up yet. And so take care of that. Then we can go back into our instance here and run the last command. And so going back to the readme here, if I scroll all the

way down to deploying to the cloud, there is a specific parameter that you want to add. This is very important for deploying to the cloud because when you select the environment of public, it's going to close off a lot more ports to make this very very secure. So any of the services that

you access from outside of the droplet, it has to go through caddy. So we use the reverse proxy as the only entry point into any of our local AI services. This is how we can make things as airtight as possible. We have security in mind like I said. And so make sure that

you run this command with the environment specified. We didn't do this locally because when we are running things locally, we don't care about security as much because it's not like our machine is accessible to the internet like a cloud server is. And so it defaults to the environment of private which just doesn't

do as much security stuff. And so go ahead and run this. And then of course make sure that you're using the correct profile. So if you're using just a CPU instance with a regular droplet or hostinger or whatever, you'd want to change this to CPU instead of GPU Nvidia. But in our case,

because we are paying the $2 an hour for a killer GPU droplet. I can go ahead and run this command with the profile of GPU Nvidia. Now, I left this error in here intentionally because I want to show you what it looks like. If you get unknown shorthand flag p-p, that means that

you don't actually have docker compose installed. And this happens for some cloud providers. And there's a very easy fix for this that I want to walk you through. So you can even test this. Just docker compose. It'll say that compose is not a docker command. And so going back to the readme here,

I have a couple of commands that you just have to run if this happens to you. This is at the bottom of the deploying to the cloud section of the readme. So you can just copy these one at a time, bring them into your droplet or your machine wherever you're hosting it, and

go ahead and run them. And so I'm just going to do this off camera really quickly. I'm just going to copy each of these into my droplet. It's very easy. You can just run all of these. They're really fast as well. So none of them are going to take very long. This is

just going to get everything ready for you so that Docker Compose is a valid command. So you can then run the start services script. So there, we, go., All right., I, went, ahead, and ran all of those. I'll clear my terminal again and then go back to the main command here to start

our services. Boom., All right., So, now, we, pulled everything from Superbase, set up our CRXNG config. Now we are pulling our Superbase containers. So again, same process is running on our computer where it'll pull Superbase, it'll run everything for Superbase, then it'll pull and run everything for the rest of our services. So

I'll pause and come back once this is all complete. And boom, there we go. We have all of our services up and running. You should see green check marks across the board like this. We are good to go. And we don't have Docker Desktop, so it's not as easy to dive into the

logs for our containers. But one quick sanity check that you can do just in the terminal is run the command docker ps- a. This will give you a list of all of our containers that are running here. We can make sure that all of them are running, that we don't see any that

are constantly restarting or ones that are down. So we do have two that are exited, but these are Nit and import and the Olama pull. These are the two that we know should be exited. Just make sure that everything is good to go. Then we can head on over to our browser. And

because we have DNS set up already, we configure Caddy. We can now navigate to our different services. Like I can go to nadnyt.dynamus.ai. And boom, there we go. It's having us set up our owner account or um we can just go to open web ui yt.dynamis.ai. Boom. And there is our open web

UI. All right. So I'll go ahead and get started. Uh, we'll have to create our account. I'll do this off camerara, but yeah, you just create your first-time accounts for everything. And then we'll do the same thing for let's do superbaseyt.dynamus.ai. And boom, there we go. So, all of our services are up

and running. And so now we can log into these and create our accounts and we can interact with our agents and bring them in. We can work with Llama in the same way. And so let's go ahead and do that. I'll just go ahead and create these accounts off camera. So, I've got

my accounts created for N8N and then also open WebUI. And you can do the same for all the other accounts you might have to create for things like Langfuse as well. And then within Open Web UI, we'll go to the admin panel, settings, connections. Make sure that your Olama API is set correctly

to reference the service Olama. Usually this will default to localhost or host.docer.in internal. So you can get that there. You have to set the OpenAI API key as well, just to any kind of random value. It's just a little bug in open web UI. Then click on save and then you can go

back and your models will be loaded. Now, now, one thing I found with Open Web UI, after you change the Olama base URL, you have to do a full refresh of the website. Otherwise you'll get an error when you use the LLM. So, just a really small tangent there, a little tidbit there,

but yeah we'll go ahead and select the model that's pulled by default. And you can pull other ones into your Llama container as well, like we already covered. You don't have to restart things. So, let's run a little test. I'll just say hello, and we'll see if we can load the model now.

And boom, look at how fast that was, because we have a killer GPU instance right now. I could run much larger LLMs if I wanted to. Um so yeah, let's see. What did I just say? All right, we'll do another test here. And yeah, look at how fast that is. It's blazing fast

because everything is running locally on the same infrastructure. There's no network delays., And, so, we, have a, powerful, GPU, no network delays. We get some blazing fast responses from these LLMs right now. And so I don't want to go and test everything with N8N again. But what I do want to show you

how to do right now is take the Python agent that we have in this repository and deploy this onto the cloud as well. Adding it into the local AI Docker Compose stack just like we did on our computer, but now hosting it all in the cloud. So that's the very last thing that

I want to cover with you for our cloud deployment. And so just like with the local AI package, we can follow the instructions here in the readme to get everything up and running on our machine. And so the first thing we have to do is we need to clone our repository. And so

I'm going to copy this command, go back over into my terminal here for my instance. And I step back one directory level by the way. So I'm now at the same place where I have the local AI package so we can run them side by side. So I'll paste this command to clone

automator agents. And then I can cd into it. And then I also want to change my directory within the Python local AI agent specifically. And so now doing an ls- a we can see the enenv.ample. So I'm going to just like we did before copy this and turn it into aenv. And then

I can do nano.env. And there we can edit all of our environment variables. And so because we're running this in the docker container attaching it to the local AI stack. The way that I referenced was going to be just calling out the service name. So port 111434 /v1. And then the API key.

It's just that placeholder there for lama for the LLM choice. If I want to get the exact ID of one that I already had pulled I'll actually show you how to do this really quick. So, I'm going to do controlx y enter to save and exit. And then the way that you can

execute a container, it's docker exec-it and then the name of our container which is lama. We already have this running. And then /bin/bash. And so what this is going to do is now instead of being within our machine, we are within our Olama container. And so now I can run the command Olama

list and then I can see the LLMs that I have available to me. So I have Quen 2.57B. So I'm going to go ahead and copy this ID. I don't have it memorized. So this is my way to go and reference it really quickly. And then this is also how you can access

each of your containers when you don't have Docker Desktop. You just do docker exec-it the name of your container and then bin /bash. So kind of like how we had that exec tab in docker desktop. And then once I'm done in here I can just do exit. And now I'm back within my

host machine, my GPU droplet. So that's another little tidbit, another golden nugget I wanted to give you there. But yeah, we'll go back into our environment variables here. And I have that ID for quen 2.57b copied. So I'll paste that in. And boom, there we go. And then for our superbase URL, it's

going to, be, http, col, back, slashbackslash and then it is kong. So I guess that I should have been more clear on this when I set things up locally. So I'll be sure to update the documentation for this but, it's, going to, be, Kong, port, 8000 because Kong is the service that we

have in Superbase specifically for the dashboard. And then the service key well, I'm just going to go ahead and get that from my local AI package because I have this set up in environment variables. And so I just have to go and reference my environment variables here to get my service ro key.

And boom there we go. Okay. So I'm going to go ahead and paste this in. And um now I'm just going to delete this instance after. I don't really care that I'm exposing this right now. And then for the CRNG base URL, HTTP CRXNG 8080. And then for my bearer token, I just

have it set to test off. And then we don't need to set the OpenAI API key because that was just for the OpenAI compatible demo earlier. So that is all of my configuration for this container. I got to be really clear on this. I'll update the docs for this. But uh otherwise we

are looking good for our environment variables. So controll x y enter to save. You can do a cat.env just for that sanity check to make sure that everything's saved. We are looking good. All right., And, so, now, within, the, readme here, so I'll go back to the instructions. We did all this already.

We changed our directory. We set up our environment variables and configured them. Now we need to run this stuff in our SQL editor in Superbase. This is how we can get our table set up because we haven't run things with N8N first. So we don't have this table created already. And so now

I just have to sign into Superbase here. So I've got my username which is Superbase. And then I'm just copy and pasting the username and password that I have um that I have set here in my environment variables. And so I'll go to my SQL editor and go back here. I know I'm

moving kind of quick here, but I got these instructions laid out in the readme. I'm going to paste this like that and go ahead and click on run. And then boom, there we go. So now if I go into tables and search for NN we have NN chat histories, a new currently, empty,

table., All right, looking good. And then going back after we do that, now we can run the agent. So I just have to take this command right here and then I'll go back to my droplet. And the one thing that I mentioned earlier, but I want to cover again. If I go into

the uh hold on, I need to change my directory back. So automator agents and then python local AI. If I go into my docker compose, you have to make sure that the include path is, correct., And, so,, I'm, going to, update this by the time you get your hands on it here where

it's just going to be going two levels back. That's what we need to do. So, make sure that we reference the right path to the local AI package on our machine and then crl + x y enter to save. That's because we have to go back from Python local AI agent then back

from the automator agents directory, and then within that same directory, we have the local AI package. So, we're good to go. Now, I can go ahead and paste in the command here to build our agent and include it in the local AI stack. And so, it's going to have to build everything. Takes

a minute like we saw already. So, I'll pause and come back once this is done. And all right, there we go. About 30 seconds later and we are good to go. So, now I can do the docker ps- a again. And this time if I look through this list very carefully, take a

little bit here, I should be able to see my Python agent. There we go. Local AI, Python, local AI agent. And it starts with local AI because it is a part of that docker compose stack. And by the way, I can do docker exec-it. And then I can do python-lo agent bin bash.

I can I can run this as well. And then what I can do is if I do a print env command, I can see all the environment variables that are set within this container. That's everything that we set up in the env. So I'm being very comprehensive with this master class, showing you

how you can tinker around with different things like accessing your containers and seeing the environment variables, making sure that everything that we specified in thev is actually taking effect here. And sure enough, it is. So we are looking good. So I'll go ahead and exit. We're back in our root machine now. We

have our container up and running and also it's running on port 8055. And so now we can go back to open web UI within uh open webyt.dynamus.ai and we can set up our pipe. And so I'm going to go to the admin panel functions. We don't have a function here. So I have

to import it. And so what I can do I'll actually do this here. I'll just Google you can literally Google np pipe open web UI. And it'll bring you to the one that I have here. You just have to sign into open web UI. I'll click on get. And then this time for

my URL instead of being something on local host, I'm going to copy my actual subdomain here. So import to open web UI and then boom, we have our pipe. So I'll click on save, confirm, and then within the valves here, I can set all of my values. So I'll just click on default

for all of these so I can get a starting point here. And then yeah chat input is good output is good the bearer token is test off and then for my URL it's going to be http colon and then it's going to be uh the name of my service python local aai agent

port 8055. Let me get that right. 8055 and then slashinvoke- python- agent. I believe I have this memorized. I think we are good there. So I'm going back if I clear this and run a docker ps- a it is indeed called um python local AI agent that is the name of our service

so open web UI is able to connect to the agent directly with this name because we are deploying it in the same docker network and so I think, we, are, looking, good, all right, so I'm, going to, go, ahead, and, click, on, save all right and then go back and start a new

chat and then also like I said a lot of times, it, helps, just, to, refresh, open UI completely open web UI completely completely., All right,, there, we, go., And then now instead of Oh, I have to actually enable. Let me go back to the admin panel. Functions, you have to make sure this

is ticked on. Um, so that we have the pipe enabled. Now going back here and I'll refresh as well. We've got our pipe selected. And now I can say hello. And there we go. Super super fast. We got a response from our Python agent. Take a look at that. And then also going

into my database here, you can see that I have all these messages in the NAN chat histories table. We'll take a look at that. All right. And then we can also ask it to do web search. I can say like what is the latest LLM from um Anthropic for example. So it has

to do a quick Seir XNG search leveraging that. Uh latest is Claude Opus 4. All right. And man that was so fast. We have no network delays now because everything is running on the same network and we have an absolute killer GPU. So this is so cool. Also, one thing that I want

to mention is sometimes depending on your cloud provider, CRXNG will not start successfully. There's one thing you have to do. It's just a really small tidbit. If you run into this issue where the CRXNG container is constantly restarting, what you want to do is go to your local AI package and then run

the command chmod 755 SER XNG. That's the Seir XNG folder. And so the CRXNG folder is responsible for storing the configuration that we have for CRXNG by default. Sometimes you don't have permissions to write this file and it needs to do so. So I'm going to update the troubleshooting to include this. But

yeah, just a small tidbit. And then you can just go ahead and run the command to start everything again. Um, obviously you have to go back one directory then you can run this um and restart everything. That easy to restart things to make changes take effect for your package and then you'll be

good to go. So yeah, we have everything working here. So this is pretty much it for the master class. Now we have our local AI package up and running with an agent and the network as well. We're communicating to it within Open Web UI directly. There is so much that we have gotten

through now. So congratulations for making it this far. All right, I'm going to be totally honest. This was very hard to make this master class, but it was so worth it. And I hope that you got a lot out of this. We really covered it all. All the way from starting with what

is local AI and why we should care about it to deploying it on our machine, building agents, deploying it to the cloud, and configuring everything with DNS. Like man, we basically did everything you could possibly need to get the foundation laid out to build anything that you want with local AI and local

AI agents. And so the very last thing that I want to cover here is just a couple of additional resources that I have for you now that you know how local AI works and how to get it set up. You want to dive into building more complex agents with it now. And so

there's a few things that I want to call out for you. So starting with my YouTube channel, I have a lot of videos on my channel diving more specifically into building more complex AI agents with local AI. And the main resource that I want to point you to right now if you really

want to go deeper into building agents with local AI is the ultimate N8N rag AI agent template local AI edition. And so this is using the local AI package and I dive really deep into rag and local AI which was outside of the scope of this master class because that's more about building

agents versus setting up local AI. But this is a great video to dive into. Um and then also I got to call out the Dynamus community again because man, I put so much effort into building local AI into a core part of this course here. And so, like I said at the start

of this master class, when I build the full agent out throughout the AI agent mastery course, local AI is an option the entire time and I show exactly how to set up everything for local AI using the local AI package. Like, I really have this ingrained into everything in Dynamus and in my

YouTube channel. This local AI package is the core of everything that I do with local AI. So great resources for you. With that, that is everything that I have for this master class. So I know this is my third time saying it, but congratulations if you made it this far. You now have

what it takes to really build anything that you want with local AI and you can use these additional resources to go much further as well. So I hope to see you in the Dynamist community. Let me know in the comments if you have any questions on anything that I dove into here because

I know that it is a lot a lot to digest, but I'm trying my best to make it as digestible as I possibly can. So with that, if you appreciated this master class and you're looking forward to more things local AI or AI agents I'd really appreciate a like and a subscribe. And

with that, I will see you in the next
