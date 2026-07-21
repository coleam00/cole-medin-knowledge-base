---
type: raw-transcript
title: "How to Use GPT4 To Grow on Twitter The Right Way"
youtube_id: 0bSppwVxVr4
url: https://www.youtube.com/watch?v=0bSppwVxVr4
slug: how-to-use-gpt4-to-grow-on-twitter-the-right-way
published: 2023-04-05
duration: "0:11:21"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:01]** [Music] so if you guys have been following AI trends at all in the last year you've definitely heard the buzzword of prompt engineering going around quite a bit now in essence all prompt engineering is is crafting your prompts to the AI like chat CBT in a way where it really

**[0:00:28]** understands what you're looking for and so then it gives you better answers because the really important thing to know for AI is the quality of your output is determined by the quality of your input so for example if you're looking for ideas for YouTube videos and you just tell it give me some YouTube

**[0:00:43]** video ideas it's not going to give you the best response it's going to be on original the video ideas might be kind of jumbled in a large paragraph and in general it's just not going to be fitted to what you want to provide content on and so with product engineering you take

**[0:00:58]** that simple ask of give me YouTube video ideas and you give a context you say these are the kind of videos that I want to create you could give it adjectives to describe what you're looking for like I want your ideas to be original I want them to be

**[0:01:13]** engaging I want them to be very specific to problems that I want to help people solve or something like that and then you can also be very clear in the format you're looking for which is another big thing that's super helpful so instead of it giving a paragraph of here's a few

**[0:01:27]** ideas you can make it give something more useful to you by saying something like give me a list of 10 YouTube video ideas and then along with all the other things that I just mentioned together you've created a prompt that will actually get good results you've now provided good input so you can expect

**[0:01:45]** good output and so as I am building The Branding agency software for kernel branding and leveraging chat gbt for this it's really important to have a good foundation of prompt engineering for all of the work that I'm going to be doing going forward using chat GPT for all my software like for example the

**[0:02:05]** last video that I showed on tweet Genie this application that is allowing you to use chat gbt to get ideas for tweet replies it's important to have good prompts to get good replies for tweets because if you're not careful you're going to get really Bland replies tweets and it's going to use a lot of third

**[0:02:28]** person it's going to use a lot of really cringy hashtags honestly I don't use the word cringy often but a lot of the replies from chat gbt could be quite cringy because it'll use a ton of emojis and a ton of language that humans don't use like hey there exclamation mark when

**[0:02:43]** really no one's ever going to do that in a tweet and so there are certain ways that I want to actually prompt it to be much much better in the way that it just talks on Twitter and so I'm going to show a couple of things I've done specifically with tweet

**[0:02:59]** replies and and what I'm going to be implementing for my props for Tweety right now all right so here we are over at the UI for interacting with Chad gbt I also have a chat gbt plus so I'm going to be using the gpt4 model which is the open

**[0:03:17]** ai's strongest and most recent model that isn't quite available to all the public yet I have to pay just twenty dollars a month to have access to this but I'm gonna I'm gonna experiment with some prompt engineering here and show you what I have done so far for my

**[0:03:33]** prompt engineering for tweet Genie to get better replies to tweets and so what I'm going to start with right here is just grabbing a random tweet off Twitter so I already have my timeline pulled up or Twitter and I'm just going to use this very very basic tweet right here

**[0:03:49]** developers what do you do when your code is building and this is a kind of reply that uh chat gbt can do pretty well with because it's it's generic it's not like it needs to understand a lot of context around a tool or a current event to understand how to reply to this so it's

**[0:04:08]** something good to work with here so I'm going to paste in uh what I have here for a prompt to get an initial reply to the tweet so it says you are an expert at growing Twitter accounts through engaging and insightful tweets and replies so this is the first key point with prompt

**[0:04:27]** engineering you want to always tell chat GPT what it is like in this case I'm telling it you are an expert at growing Twitter accounts through engaging in insightful tweaks and replies and so you're setting the stage for what kind of reply you were expecting by telling it what kind

**[0:04:43]** of quote-unquote person it is and so then I'm saying create an informal and engaging reply without hashtags to this tweet and less than 280 characters so instead of simply saying here's a tweet give me a reply I'm using adjectives like informal and engaging I'm telling it to exclude things like hashtags which

**[0:05:01]** make it kind of cringy like I was saying earlier and then also I'm telling it to do it in less than 280 characters so I don't have to go and edit it to bring it down to within the limit for Twitter replies which is 280 characters and then

**[0:05:14]** here is where I put my tweet so I'm going to go back here copy this over from Twitter bring it in paste it into my prompt here and click enter so at this point it's going to create a response that is decent but there's actually more to my prompt engineering

**[0:05:29]** here that I'll show you in a second because I'm not I'm not just done here I'm not happy with what it has created usually at this point so we can see right here the reply is generating oh the anticipation of waiting to or code to build I love to

**[0:05:43]** grab a cup of coffee blah blah blah blah a couple things it wants to do it's all about finding balance and fun while waiting for that sweet sweet compilation so overall this is the decent response but I want to take this further and I want it to actually criticize itself

**[0:06:00]** this is a really important tool under the tool belt of anybody working with AI doing prompt engineering is using what is called the critic model and so I'm going to paste in a large prompt here and then I'll explain everything piece by piece and then we'll call it a day so first you again set the

**[0:06:22]** stage for who it is so now you're no longer a expert at growing Twitter accounts you are a Critic and then I I tell that it's really open about issues and willing to provide feedback on anything because sometimes the AI likes to say oh this is all subjective I don't want to say much here

**[0:06:38]** and then I also uh tell it that it's an expert at growing Twitter accounts they're engaging content so it's setting the stage saying it's a Critic and an expert at Twitter and saying that it critiques replies to tweets and so in this case the tweet that is in

**[0:06:54]** question here is and I'll paste in this exact same tweet as before and then I'll say the reply you are critiquing is and I'll just paste in the reply that it created from my last prom and the reason that I'm kind of doing this from scratch like I'm giving it the same tweet again

**[0:07:10]** is because even though in this UI the chat GPT model recognizes previous context from our conversation like it knows the Tweet I'm talking about if I were to ask it what are we talking about when you use the open AI API for interacting with chat GPT or any of the

**[0:07:29]** AI models it doesn't have that previous context when you make a request to the API the only information it has is what you give it assuming you're not using a fine-tuned model which is something I'll do in a later videos talk about fine-tuning models for your use so

**[0:07:45]** yeah that's why I'm kind of showing you what uh I would do with the API because later when I'm building the Cardinal branding software I'm going to be using the API I'm not going to be using this UI and so every request I make to chat gbt from the API needs to have all the

**[0:08:01]** context within just that request and so I have the reply here and then I say think of feedback on the Tweet reply and think of suggestions for many ways it could be improved and be made more informal as long as it isn't too informal don't be cheesy so I'm telling

**[0:08:19]** it to be critical of itself telling me why this reply sucks basically and how it can make it better and so then I say take your suggestion and rewrite the reply in less than 280 characters without any hashtags so again some of the same context as my first prompt

**[0:08:36]** because I don't want to act like it remembers what I was saying before and so then I say uh you know don't surround in Quotes no hashtags don't include your feedback or suggestions or a label for the reply because what I wanted to spit back is exactly this I

**[0:08:52]** don't want it to have anything else I want to be able to just take what it has here and post it to Twitter of course with any edits that that I might make because the one thing I like to do often is include its feedback and then the

**[0:09:03]** reply smash it all together when really I just want the reply so I'll click enter here and we'll see what it comes up with so a lot of times the first reply can be as good as the second one but more often than not when you go through this whole process of telling

**[0:09:22]** you to critique itself you're forcing it to think step by step through how it can better its own content and it does surprisingly well which can be kind of frustrating like why why does it just do its best on the first try but it's all about guiding the AI into

**[0:09:40]** the response you're looking for and so even though I said don't make it formal make sure it's engaging then my first reply or my first ask for a reply it doesn't fully grasp that until I really tell it to be critical about how it isn't informal enough and then I get

**[0:09:59]** a response that is better so this one waiting for a code to build huh coffee is a classic choice I also tried quick exercises dive into Dev memes or even strum a guitar mixing productivity and Leisure helps pass the time without losing focus all set for that satisfying

**[0:10:14]** compilation moment so I would say it's a bit better for sure compared to the first one it definitely sounds like more human-like especially the first part right here waiting for code to build copies of classic Choice compared to oh the anticipation of waiting for code to build like that first sentence of that

**[0:10:30]** first reply does not sound like it's coming from a human it sounds way too formal honestly and and so I did accomplish my task definitely of guiding the AI into a more informal response so both were decent second one's definitely better and so this is the kind of prompt

**[0:10:47]** engineering that I'm working with for tweet Genies on a building for Cardinal branding and I've got a lot more tips down the pipeline for prompt Engineering in general just how to get the AI to that better response so I'll be making more videos on that uh as we go along in

**[0:11:01]** this series and then also I'll be showing more about the development doing for tweet Genie so thank you everyone for watching I hope you enjoyed and I'll see you in the next episode foreign [Music]
