---
type: raw-transcript
title: "ChatGPT Users BE AWARE of this Major Weakness"
youtube_id: uB9cgB6Of9k
url: https://www.youtube.com/watch?v=uB9cgB6Of9k
slug: chatgpt-users-be-aware-of-this-major-weakness
published: 2023-05-22
duration: "0:09:32"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** everyone in the past year has been flipping out over how powerful GPT is and what it can do for them but really these AI models like GPT are far from perfect there's a lot of inaccuracies that they have still because of a lot of key weaknesses the biggest one being the

**[0:00:16]** training cut off so today I want to talk to you guys about the training cut off what it is why it's the biggest weakness for GPT and other AI models ways that you can get around it and the implications of this weakness on the future of AI and how AI will develop to

**[0:00:31]** overcome this weakness as well as some other ones so first of all let's get into what is the training cutoff and the way you can actually learn about it and understand what the cutoff is for GPT is you can actually ask gbt so let's go to this example now where I simply ask it

**[0:00:48]** what is your training cut off and it says it is September of 2021 and explains what that means is it's trained on data from September 2021 and earlier and it doesn't have an idea what you're talking about anything after that such as current events like if you ask it

**[0:01:03]** about a current event it isn't going to be able to give you any information on that because the AI model is stuck at a point in time where it's trained it has all the past knowledge but nothing in the future and so this is the biggest weakness because there are a lot of

**[0:01:16]** times where you need current up-to-date information about modern events like the example I gave or when you're writing code a lot of times you're working with libraries and tools that have a lot of updates since September of 2021 and you're not able to use GPT to help you

**[0:01:31]** with those libraries or tools because it gives you outdated information when you ask for help and so I actually have a really good example right here where I've asked it to help me make a Discord bot with the discord.js library now this is the most popular library for creating

**[0:01:48]** Discord Bots and the most up-to-date version right now is version 14. however that came after September of 2021 and so right here in this example I'm asking it to help me make a Discord bot and it gives me some really nice code right here it's just this really simple bot

**[0:02:05]** that when you type in the pink men it responds with pong just a funny little bot to demonstrate my example here and so it gives me really good detail of the code and explaining it telling it what telling me what I have to do with the bot token for example so it's a really

**[0:02:20]** good response overall however if I ask it what discord.js version are you using for this application it tells me that it's actually using version 12. so it's not even version 13. certainly not version 14 and version 13 was actually released before September 2021 so it's able to rewrite the code and work with

**[0:02:41]** that more up-to-date version but if I want to work with the newest version of this Library I cannot do so because it came out after September of 2021 and so if I ask it specifically please tell me how to write this with version 14 it says it can and it references its

**[0:02:58]** training cutoff of September 2021 just like it said right here that its training cutoff is September of 2021 and so this isn't the worst thing in the world you can still easily run a Discord bot on version 13 and I've even done so because I wanted help from GPT you can

**[0:03:13]** imagine a scenario where you are trying to incorporate a library into an existing code base where you require that library to be the most up-to-date version to really work with the other code and other libraries and tools that you're using but if you use the most up-to-date version something that came

**[0:03:27]** out after September 2021 there's nothing you can do you can't use GPT for help and you're entirely reliant on the documentation for that Library just like the good old days which is fine and a lot of times you can work with that but GPT is extremely powerful tool I'm

**[0:03:41]** talking about the greatest weakness here but overall it is a very powerful tool and so we want to be able to use it for things like working with libraries so that we don't have to look and scramble through the documentation to get the examples and extrapolate from that what

**[0:03:53]** we need to do in our own code and so this really is a great weakness and going back to the document station here looking at discord.js we can see they have an entire article here on just how to upgrade from version 13 to 14 because there are a ton of breaking changes and

**[0:04:10]** so we can't just take the version 13 discord.js code from chat GPT we can't just take this right here copy it put it in and then upgrade discord.js to version 14 because likely everything's just gonna break you're gonna have to go through this list and understand all the

**[0:04:29]** different ways that discord.js13 is different from 14 and you're going to have to change your code accordingly and this might take even longer than just starting from the discord.js version 14 documentation and writing the bot entirely from that without using GPT at all so it's not great so why is this the

**[0:04:49]** greatest weakness I think I've already covered that so moving on to the next thing then how do you get around this now there are a lot of ways to do so and a lot of it comes down to fine-tuning your own model which is an entirely separate video now that I'll do in the

**[0:05:03]** future where you can actually give your own key value pairs like here's a question here's an answer and you could take like the entire documentation for discord.js version 14 and have questions and answers based on that documentation to actually train GPT your own custom model to know the discord.js version 14

**[0:05:22]** documentation and write applications Discord Bots for you based on that and I wish I could get into more detail on that but that's something you can do in your own time research how to fine tune a GPT model and so you can do that to get more up-to-date information on a

**[0:05:37]** specific thing that you train it on also the future AI is moving in a direction where this won't be as much of an issue the biggest reason right now why there are training cutoffs and why trading cutoffs are so old like September 2021 that's almost two years ago now at the

**[0:05:54]** time that this video is recorded the reason that it's so old and that there is a training cut off in the first place is because it takes a really long time a lot of money a lot of time a lot of computational resources to train an AI model because of the millions and

**[0:06:08]** billions of parameters that are used to train the model and so going back to the browser here one thing that's going to be happening with AI in the near future is organizations and open source projects people around the world are going to be figuring out how to train

**[0:06:23]** these models with less and less parameters and parameters that's just a fancy way to understand all the different attributes that go into a model to help it understand all the contexts that you're feeding all the data that you're giving it and so we already have one example right here

**[0:06:37]** where meta's AI is trained with 10 times less parameters than other models like GPT and so right now we're already at 10 times less maybe in a couple months we'll be at 100 times less and then a thousand times less and then a million times less and all of a sudden you have

**[0:06:53]** these models that are just as powerful as their precursors like gbt except they can be trained in minutes instead of days and days since the training cut off can be shortened by a long shot here because you can train the model like every single day and so the training cut

**[0:07:08]** off will still exist but it might be hours or days instead of years at this point the training cut off for GPT is already almost a couple of years and so there's a lot of really cool stuff happening with AI Innovation that will make this not as much of an issue so

**[0:07:22]** instead of having to use something like a GPT plug-in for internet searching which by the way is another kind of work around for this you can actually just use the base model because it's going to be trained every single day on data coming in from GitHub repositories and

**[0:07:35]** news articles and all the different data sources from the previous day and the day before that and everything up until the very current day that it's being trained overall this is a really big weakness right now but it won't always be and so it's important as a developer

**[0:07:50]** like myself who wants to always be up to date with libraries and tools it's important to be aware of this training cut off and also to keep up the to date with the research that's going on in models like these that are being trained with fewer parameters and we might get

**[0:08:05]** to the point where we have a like a one day training cut off and so then we'll be able to leverage these tools and not have to worry about working without data documentation on libraries and tools with the models that we're interacting with I cannot wait for that day and

**[0:08:20]** honestly you guys shouldn't want to wait either because this really is the biggest weakness right now especially because when in that example when I was having it create that discord.js code for me it didn't tell me that it was outdated because it really doesn't have a way to know because like really think

**[0:08:36]** about it if there actually hasn't been a version since September 2021 then it is the most up-to-date and sometimes that will be the case for libraries so sometimes GPT will say hey this might be outdated because of the training cut off other times like with this example it

**[0:08:51]** doesn't say anything at all and then we don't even have a way to know and so it's not the best thing so I'm looking forward to AI Innovation I'm going to be providing updates on my channel Channel frequently with AI Innovation on things like this and I look forward to getting

**[0:09:04]** to the point where AI models can be trained so fast and are so powerful that you don't need plugins for internet search you don't need a custom knowledge base for fine tuning you can just take a model and run with it and so yeah stay tuned for that I'm going to be providing

**[0:09:18]** updates here as those things come out so thank you everybody for watching like And subscribe if you found this insightful and if you really learned about the weaknesses of AI models through this video thank you all for watching and I will see you in the next one
