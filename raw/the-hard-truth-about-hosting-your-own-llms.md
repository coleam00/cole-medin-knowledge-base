---
type: raw-transcript
title: "The HARD Truth About Hosting Your Own LLMs"
youtube_id: EMuBqcO048E
url: https://www.youtube.com/watch?v=EMuBqcO048E
slug: the-hard-truth-about-hosting-your-own-llms
published: 2024-09-25
duration: "0:14:45"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** running your own large language models locally is all the rage right now there are dozens of incredibly powerful llms that you can download and self-host now and running your own llms means that you don't have to pay per token as you are using your AI and you don't have to send

**[0:00:16]** your data to another company they are fantastic for scaling your business and keeping your data protected and while they can't compete with the best close Source models like 01 and Claw 3.5 Sonet they still abs absolutely kick butt with the right setup however there are some hard truths that you and I have to face

**[0:00:36]** that you will quickly realize when you try to use the more powerful local llms like llama 3.1 on your own Hardware I can guarantee that the first time you try to use a local llm it is going to take you much longer than you thought to get a response and sometimes you won't

**[0:00:53]** even get a response because you'll get a timeout and in that case your computer straight up is not good enough to use the model at all and that my friend reveals the hard truth running the more powerful local llms requires insanely powerful Hardware I'm talking gpus that cost at least two grand just to be able

**[0:01:12]** to run the weakest version of llama 3.1 and that's not even to mention all the electricity costs that you're going to have to pay to run this thing 247 you could also go with GPU machines running in the cloud but those can cost more than a dollar per hour that adds up

**[0:01:28]** really really quick and that's even on the low end and this is a big problem because on one hand you and I we want to use local llms they give us the most flexibility privacy and ability to scale because we aren't paying per token but on the other hand running the more

**[0:01:43]** powerful llms locally can cost hundreds or thousands of dollars up front and local llms are actually the most affordable when you really start to scale but getting to that point with them is absolutely painful I have seen this problem this contention play out with many businesses as they start to

**[0:02:02]** integrate AI so I have developed a simple but effective strategy for this that I want to reveal to you now here is the premise of the strategy unless you're willing to put in a large initial investment running local AI right off the bat is not realistic that's what you

**[0:02:19]** and I just covered but what you can do is pay per token with these same self- hostable models in an incredibly cheap way and then later on when the Price Is Right scale to hosting these exact same models yourself in your own Hardware that way you're only paying the big

**[0:02:36]** bucks when it makes sense and you don't even have to switch your llm which that can have a lot of unintended consequences for your application so in this video allow me to show you both sides of this strategy here first starting with paying per token and then going to hosting your llm yourself and

**[0:02:53]** there is an exact calculable time when it makes sense to make the switch and I will cover that as well the way that you start this strategy so you aren't paying thousands Upfront for local llms is with one of my favorite AI services on the entire planet Gro Gro is your way to pay

**[0:03:09]** per token for super fast openly available llm inference and it is insanely cheap oftentimes it's actually free if your requirements are light enough because grock has an awesome and indefinite free tier and I also just want to say that I'm not sponsored by grock in any way their platform is just

**[0:03:26]** the best for Speed and price when it comes to this kind of thing and so that's why I'm including grock specifically in this strategy instead of another service or being more generic all right so now we get to the fun part because I'm going to very quickly show

**[0:03:39]** you around Gro I'm going to show you how easy it is to use how powerful it is and also how affordable it is as well and then we'll dive into what it looks like for you to make that decision to eventually switch from grock to hosting your own llms what that looks like and

**[0:03:53]** when exactly you would make that choice so I'm going to give a quick overview here just give you a lot of value very very quickly so I'm here on the grock website it's just gro.com and they boast their speeds immediately because they literally have this chat window on their

**[0:04:07]** homepage where you can talk to grock I'm not sure which llm this uses under the hood but just see how fast this is I'll enter in just a random prompt that I have here it spits out the answer really fast and then tells you exactly how quick it is

**[0:04:21]** 1,200 tokens per second that is insane just for reference one word is about 1.25 tokens and so this is about 1,000 words per second roughly that is incredibly fast much much faster than most llms out there and it's also insanely easy to use so if I scroll down on their homepage

**[0:04:43]** here and I go down yep right here it just shows you how all you have to do to work with grock is you have to replace the base URL within your open aai instance with the grock API like it says right here and then add in your grock

**[0:04:58]** API key and then you just switch it out your model right here it is just so so easy like just 10 lines of code they show you right here all you have to do is PIP install open Ai and then boom this is your code and you're now working

**[0:05:09]** with grock and with Lang chain it's even easier because you have to just uh pip install this Lang chain grock package set your grock API key in the environment variable and then you have access to this chat grock instance that you can import from Lang chain grock you

**[0:05:24]** can Define your model any other parameters like the temperature and now you can do an lm. invoke do stre whatever you'd usually do in Lang chain so it's just so easy to get started with grock here as well and then I also love n8n put out a lot of content on it so

**[0:05:38]** I'll show you that really quick as well so in your n workflow you'll typically have a tools agent node when you're working with large language models in n and then for the chat model here I'll just click on this you can see that grock is one of the options supported so

**[0:05:54]** no custom integration you can use grock right off the bat with n8n all you have to do for your credentials here is put in your grock API key just like we saw with code and then boom you have access to all of the models within grock super super nice and easy and so with that I

**[0:06:11]** wanted to talk about the price for grock as well so we'll go over here and look at this for llama 317b it is 59 cents per million tokens and so what that equates to is for every $1 you get 1.69 million tokens that is actually EX extremely affordable compared to any

**[0:06:31]** Clos Source model really all the powerful ones like GPT 40 and Claw 3.5 Sonic and then even comparing to other services that offer llama 3.1 like together for example they have their light version of llama 3.1 70b that actually is technically a little bit cheaper but if you want to go turbo to

**[0:06:51]** even come close to matching the speeds of llama 3.1 with grock then you're going to be paying more and so together AI it's a fine service I've used it before I like it uh but it just shows how insanely affordable grock is it is just amazing so there we go in just a

**[0:07:07]** few minutes you now know how to use grock what the pricing looks like and also how fast it really is one thing that I do want to mention here with Gro is it still is another company that is hosting the llm for you so it's not quite the same as local AI in terms of

**[0:07:22]** your data privacy but it is still a lot better than sending your data to a close Source model like GPT or CLA that's going going to train the model on your data and eventually theoretically regurgitate it back out to other people so it's still much better to use

**[0:07:38]** something like Gro with llama but keep that in mind that if you're developing a proof of concept using Gro because you don't want to pay for self-hosting your llm you might want to use mock data for things that's really really private just as you are building out your application

**[0:07:51]** and then once you scale and you're running things locally then you can work with your private data and not have to worry about anything so with that we can now dive into the next step of this strategy all right so I have my calculator up right now because we are

**[0:08:05]** going to be doing some napkin math to figure out exactly when it makes sense for you to switch from paying per token with a service like grock to hosting your own llm because eventually it will get to the point when you scale your business that paying for token is more

**[0:08:20]** expensive than just paying for the hardware now one thing that I want to mention is that I'm going to be covering what it looks like to pay for a GPU machine in the cloud to run your l because you can technically build a computer and have it in your house or a

**[0:08:34]** data center but you have to deal with maintenance paying for electricity it's harder to upgrade when the next level of gpus come out in a half a year or a year and so generally it's a lot more flexible to just pay for something in the cloud and that's generally what I

**[0:08:47]** would recommend and so that's what I'm going to be focusing on right now there are a lot of services out there to get GPU machines a couple that I want to highlight here is runp pod which is what I'm on right now and then also digital ocean I'm not not affiliated with either

**[0:09:00]** of them but I use both of them and so that's kind of my recommendation of just where you'd want to start when looking for somewhere to host your llms in the cloud now digital ocean is actually pretty pricey and they don't have a ton of options I know that they are

**[0:09:14]** expanding this in the future just because I've done some research since I like digital ocean so much um but in the meantime runpod actually has much more competitive pricing you can just kind of look at some comparisons here for like an h100 just like they have right here

**[0:09:28]** it's definitely a lot cheer and also if you want to run something like llama 3.1 70b which is a really classic local llm you typically would only need something like an A40 right here so this is actually the model or the machine that I want to use for my example here for my

**[0:09:46]** napkin math so an A40 it is 39 cents in the secure Cloud to run this with 48 gbt of vram definitely good enough for llama 3.1 70b and so what we're going to do right now is I'm going to walk you through with this calculator step by step how

**[0:10:01]** you can determine exactly when it becomes more expensive to pay per token with Gro and so let's go over to the calculator here so first of all what we want to do is compute how much it costs per month to use that A40 instance with run pod so I'm just going to take

**[0:10:18]** 0.39 because it is 39 cents an hour multiply it by 24 because there's 24 hours in a day and then multiply by 30 CU there's roughly 30 days in a month and that gives us a grand total of $280 a month so you pay a pretty penny a

**[0:10:33]** few hundred a month for this instance but let's do the math and figure out when it makes sense to actually do this instead of go with grock so I'm going to go back to the grock pricing here and we'll take a look at this so for grock for llama 3.1 70b you get

**[0:10:50]** 1.69 million tokens for every $1 that you spend so let's plug that into the calculator here I'm going to clear it completely and I'll add add in this number here so 1, 690,000 tokens per $1 now there are a lot of tokens in your typical prompt especially if you have complex

**[0:11:13]** instructions for your llm or long chat histories or you have rag where you're retrieving multiple big chunks from documents and dumping those into your prompt and so the average prompt is actually like a good solid few thousand tokens even up to like 10 or 20,000 tokens I have seen before and so this is

**[0:11:32]** a really rough estimate but in your use case you will know the average amount of tokens that you have per prompt and that's something that you can actually compute so you can track that in the back end as you're developing your proof of concept and starting to use your

**[0:11:46]** application and bring users on and figure out the average tokens so that you can plug your exact number into this to have a better idea when exactly you would switch from grock to hosting your local LM so I'm going to go with 5,000 as just just a good example here and so

**[0:12:01]** what I'll do is I'm going to divide this number by 5,000 because that is going to tell me the number of prompts that I can make to my llm per $1 you see that here because it's 1,690 th000 tokens per $1 when I divide by the number of tokens per prompt this

**[0:12:21]** is the number of prompts that I can make to my llm per $1 and so now what we're going to do is multiply that by the price of the runp Pod instance because what this is going to give us is it is going to give us the number of prompts

**[0:12:38]** that we can make per month until it gets to the point that runp pod is cheaper so this is the magic number here 94,95 instance to host our llama 317b as long as that instance can keep up with the demand which I'm pretty sure um 48 GB of vram and I think it had like

**[0:13:03]** 80 GB of RAM or something it could probably keep up with the demand of this many prompts per month because if we divide by 30 that is going to give us the number of prompts that we would have per day so if you get to like 3,000 promps per day with your application you

**[0:13:18]** would want to self-host your llm instead and if you think about it let me get back to that number here I'll divide by 30 again I'm not sure why I went away if you think about it that's not actually that many prompts per day if you have three ,000 users on your platform in a

**[0:13:31]** day they could each make one prompt one call to your llm and then it would already be worth it to switch over to hosting your own llm so I hope that makes sense here I know there's a couple of rough numbers that I put in here for examples but you can make this very very

**[0:13:47]** accurate to your use case figure out the instance you want with runp pod the exact pricing for your model in grock how many tokens you have on average per prompt and this can come down to an exact science when you'd make that switch so there you have it that is my

**[0:14:01]** grand strategy for how you can work with local llms effectively to not spend a ton of money up front but eventually scale where you're hosting everything completely and saving thousands and thousands of dollars once you scale your application to thousands and thousands of users now grock pricing is pretty

**[0:14:17]** competitive you can see from my math there that you might want to use it for a very very long time and you might even want to use it for longer just because of the convenience of not having to maintain your own llms but eventually it does do get to the point where it just

**[0:14:31]** makes so much sense and you save so much money so I hope that you found this strategy and all the logic behind it valuable if you did I would really appreciate a like and a subscribe and with that I will see you in the next video
