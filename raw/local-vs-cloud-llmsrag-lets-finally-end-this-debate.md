---
type: raw-transcript
title: "Local vs. Cloud LLMs/RAG - Let's FINALLY End this Debate"
youtube_id: W5X34-QmdEQ
url: https://www.youtube.com/watch?v=W5X34-QmdEQ
slug: local-vs-cloud-llmsrag-lets-finally-end-this-debate
published: 2024-09-11
duration: "0:10:15"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** I have been building AI agents with rag tool calling and all the bells and whistles for over a couple of years now and sometimes I'll go with local self-hosted Solutions like llama 3 for my llm and chroma for my Vector database while other times I'm going to use

**[0:00:16]** manage services like CLA for my llm and pine cone for rag but recently a lot of what I've seen on YouTube is people saying that you have to go local with your AI solution or it is completely bust and I can't go a day without seeing this right now and I'm sure it's the

**[0:00:32]** same for you as well and these people they have a very strong argument and I'll get into that in a little bit but there is a lot of nuance to this and that is what I need to dive into today so you and I we need to talk about this

**[0:00:44]** right now because there are a couple of very key clarifications that I want to make that'll help you make a very informed decision about your AI Tech stack and this is super super important because whether or not you choose local or managed services for your AI app is

**[0:00:59]** going to entire change your text stack and the directory of your application and also I just want to say I know that there are a lot of opinions out there on this and so I would really appreciate if you leave a comment letting me know what you think after you hear me out on this

**[0:01:13]** all right so first let's actually talk about what a good Tech stack would look like for both local and managed services this is really important because I want to paint a clear picture for you what technologies you'd actually be using when you go down either path now keep in

**[0:01:26]** mind that this solution is one of many there are so many different options that you have both for local or managed but what I'm about to cover here is just a really honest suggestion that will work for most use cases all right so starting with the local Tech stack I want to kick

**[0:01:41]** it off right away with Docker because this is a super important service you need Docker to guarantee that you have a sound infrastructure when you are self-hosting everything in this list here next up we've got olama for the large language model because you can use olama to host a very wide variety of

**[0:01:59]** llms so such as llama 3.1 70b next up we've got quadrant for the vector database and then superbase a self-hosted version for authentication and postgress and you could also use PG Vector as an extension of postgress if you want to use that for rag instead of quadrant next up we've got n8n for the

**[0:02:19]** no code workflow automations and then finally redis for caching and then for the manage services Tech stack a lot of the names are going to look quite similar to what we saw for the local stack and there's a good reason for that that I'll get into in a little bit but

**[0:02:34]** starting off with the llm we have Claude GPT or Gro a good variety here because it really does depend on your use case then we have pine cone or quadrant for the vector database a hosted super base for postgress and authentication again you can use PG Vector here to replace

**[0:02:53]** Pine coner quadrant for rag then we have Cloud n8n for your no code workful automations and then redis doio for your posted redis caching so keep these text acts in mind because I'm going to be referencing them as I go down a decision tree to help you pick whether or not

**[0:03:08]** your AI solution is going to be using a lot of local or a lot of managed Services all right so with that in mind we can dive into this beautiful decision tree diagram that I've made for you to help you figure out which route you want to go down for your AI app I'll even

**[0:03:22]** have a link in the description of this video to this diagram so you can feel free to download it and change it yourself on draw.io and even share what you've change because I don't promise to have the perfect solution and so I know that there might be some things that you

**[0:03:34]** would disagree on and maybe want to change up so feel free to do that the other thing that I want to mention before we dive in is that a really common approach for a lot of businesses is to go hybrid and what I mean by that is some of their things like maybe their

**[0:03:48]** caching and their Vector database will be through manage services while other things like their llm will be selfhosted now this is a really really good approach and the reason I don't cover that in this diagram here is because going on the two extremes of all local or all managed Services just paints a

**[0:04:05]** simpler picture for you so it's really good just to talk about it in those terms in this video but just keep in mind that a hybrid approach is really really solid but in general you still need to decide if you're going to be more local or more managed Services

**[0:04:19]** hence why I'm covering it like this in this video so at the top of this diagram we have you and you are trying to decide if you want to go with manage services or local for your AI application now the first question you want to ask yourself is is what I am building just a simple

**[0:04:34]** proof of concept and the reason this is so important is because manage services are so much quicker to get up and running for what you are trying to build so when you're trying to just make a proof of concept you want to go with managed Services because you want to

**[0:04:49]** build something quick and scrap it quick if it ends up not actually being right for your business and if you're spending all the time getting things up and running locally you're wasting that time when really you're trying to figure out does this thing actually me versus can I

**[0:05:01]** actually build this full production application that can scale and handle all of my requirements even if you are dealing with sensitive data there are still a lot of ways to mock data or take sensitive parts out when you're building a proof of Concepts you can still very much test it as much as you would need

**[0:05:18]** on top of that the reason that I had my local and managed Tex Stacks have so many similar names is because you want to make it easy for yourself to start a POC with managed services but then migrate over to local if you figure out that yes this is right for me and now I

**[0:05:33]** want to bring this into a production application and so keep that in mind as if you Technologies are right it can be really easy to go from a POC with managed services to a production application using more local things if you don't want to be building just a

**[0:05:48]** simple proof of concept then we ask ourselves this next question and it is is your data sensitive because at this point you are not building a POC we've established that in this route of the decision but if your data is sensitive and you're building a production application then

**[0:06:05]** hands down you want to go local for pretty much everything and the reason for this is you don't want your sensitive data being fed into a public llm like GPT where it's trained on that data and could potentially regurgitate it to users later on it is not ideal

**[0:06:19]** that applies to other things as well like if you have a database in the cloud a little bit of a different way but it still does and so it's a pretty simple decision at that point to go local if your data is sensitive now if your data is not sensitive there are still a

**[0:06:34]** couple of decisions that we have to make here the first one is do you need the latest and greatest technology and when you're building a proof of concept that's where you can test this you can figure out can I get away with using a local model like llama 3.1 or do I need

**[0:06:49]** something really really powerful like CLA 3.5 Sonet to handle the complexities of my user requests so you figure that out and you test it when you're building your proof of concept and if you do need the latest and greatest typically you have to go with managed Services because

**[0:07:05]** the compute resources for the most powerful LMS like Claude and gp4 are just so intense that you can't really run it locally and so if you have advanced tool calling or really specific structured output requirements things that the local models fail with then you're pretty much forced to go with

**[0:07:22]** managed Services if you have something that complex now if you don't have something that complex you test in your POC you're like oh yeah I this works really really well with llama 370b or a mistro model or something like that then you go on to this next question here so

**[0:07:37]** at this point you're still considering between local and managed services and what you want to ask yourself is are you scaling your app to more than 1,000 users because here's the thing if you're not scaling your app super super heavily going with managed Services can actually be cheaper and at this point we've

**[0:07:54]** already established that we don't have sensitive data so no sensitive data and you're not going to scale your app a lot go with manage services because the initial overhead of getting a cloud instance to host your local llm rag whatever it is is actually going to be more expensive and the main reason for

**[0:08:12]** that is just the generous free tiers that services like pine cone or super base offer to you to make manage services actually cheaper until you scale now if you actually are going to scale and get to thousands and thousands of users that's when it can be very very

**[0:08:27]** cost effective to go local and so as long as you have the knowledge or the desire to learn the knowledge to host things locally then you should definitely go local in this case so even if you don't have sensitive data if you want to scale the heck out of your app

**[0:08:41]** it is going to be more cost effective to go local but there are also a lot of companies that they just want the convenience of manage services and again as long as you don't have sensitive data like we've established in this part of the decision tree then it's okay those

**[0:08:54]** companies they go manage services they make it work for them they have to pay more for the convenience but it happens to work pretty well for a lot of companies so at this point this is the entire decision tree you can very easily just start at the STP ask yourself these

**[0:09:08]** questions and get to an answer of either local or managed services so I hope that diagram was really really helpful for you to make an informed decision I really really want to re-emphasize here that I know there are a lot of different opinions on when to use local and when

**[0:09:24]** to use manage services there are even a lot of different opinions on things like what actually defines sensitive data so I had to keep that in bag because I don't want to just impose my own opinion on that a lot of different businesses have different requirements for things

**[0:09:36]** and what actually makes something sensitive and so please feel free to share in the comments what your thoughts are on this I would love to hear what you think about this and when you think you should go local or not go local in general going local is a really good

**[0:09:50]** idea especially because of how much more powerful the local models like llama have gotten more recently and so I'm definitely going to be making a lot more content on my channel up and coming for things like local Rag and local llms and getting all that hosted so if you're

**[0:10:06]** interested in that and if you found this diagram helpful I would really appreciate a like and a subscribe and with that I will see you in the next video
