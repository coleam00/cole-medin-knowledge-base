---
type: raw-transcript
title: "AI Agents Can Now Build Their Own UI in Real Time (Personalized to You)"
youtube_id: MD8VQzvMVek
url: https://www.youtube.com/watch?v=MD8VQzvMVek
slug: ai-agents-can-now-build-their-own-ui-in-real-time-personalized-to-you
published: 2026-02-04
duration: "0:15:18"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** Let me show you something really quick. What you're looking at right here is a personalized dashboard that was generated for me based on a bunch of research that my second brain did. Nothing is preconfigured here. It generated the entire layout and chose all of the components completely on the

**[0:00:16]** fly. So, we're using an agent for ultra personalization. This is all thanks to generative UI, which if you haven't heard of or used generative UI before, you, my friend, are in for a treat. For the simplest explanation possible, generative UI is the idea that we're going to give our agent the ability to

**[0:00:33]** decide the layout and the components for our front end. And with how powerful agents are becoming these days, this is definitely the direction that we are heading. I'm pretty sure in the near future when you go to amazon.com or google.com, exactly what you see is going to look a lot different than the

**[0:00:50]** next person because it's going to be personalized to how you use the application and your interests. For example, with this application that I built to demo generative UI for you, all I have to do is paste in any kind of research that my agent did. And then it's going to decide the layout and the

**[0:01:04]** components that it thinks is optimal to share this information with me in a more concise way, extracting insights as well. And besides it looking really, really nice, the most beautiful part about this is every single time it generates a dashboard, it's going to be custom to the specific input. And so

**[0:01:22]** here's another example. This dashboard looks completely different because it's optimized to what it thinks I want to see. And that's something that I can optimize in the prompts for the agent as well. And the important thing to keep in mind here is this that I built for you

**[0:01:34]** is just a single use case to show you the power of generative UI. This really is the future of software. And so we'll get into why that's the case, how generative UI works exactly. I'll even get into the architecture that I've built for this application so you can

**[0:01:48]** see how to incorporate it for yourself. And I know there's quite a bit that goes into the tech stack here, but I'll break it down nice and simple for you. And of course, this project to demonstrate generative UI, I'll have as a GitHub repo linked in the description. It is a

**[0:02:00]** really good starting point for you to understand generative UI and even build on top of this to create your own application. I put a lot of work into designing a really solid tech stack here. So, I'll get into this more in a little bit, but we have our Pantic AI

**[0:02:15]** agent. This is the agent running in the back end that is choosing the components and designing the layout. And then for our generative UI protocol, we're using A2UI from Google. This is the specification exactly how does the agent define the components that we're going to render in our front end. And so we

**[0:02:34]** send this over to our front end and we're using the protocol AGUI. I've covered this on my channel before, but this is our way to very easily connect our agent to our front end. And so I know it's a little bit confusing here because we have two protocols. A2UI is

**[0:02:50]** for specifying the components and the standard there. AGUI is for connecting our agent running through an API with our front end. And we're using Copilot Kit because Copilot Kit makes it super easy to build these really interactive front-end apps and it integrates directly with all of the other parts of

**[0:03:08]** our tech stack. And so we take the requests from the agent. this is what we want to render and then we create those as React components to make that beautiful dashboard that we're displaying to the user in the end. And so we'll get more into how this works,

**[0:03:20]** but the first thing that I want to cover with you is generative UI at a higher level. Why is this so powerful and exactly how can you use it for yourself? So we've already covered the most basic definition of generative UI, right? It's allowing agents to play a role in

**[0:03:35]** determining what appears on the screen, how information is structured, and in some cases, like in our case, even how the layout is composed. We're giving a lot of control over to the agent versus most agentic applications right now, the agent is just assigning information to display in a preconfigured layout. And

**[0:03:52]** so, this takes things to the next level. There's a lot of use cases for this. Even chat applications, think about Slack bots, Discord bots. When we're talking to an agent, a lot of times it's more useful for us to understand what the agent is telling us if we have

**[0:04:06]** visuals, not just text responses. So, being able to render components in the middle of a conversation with generative UI and making it custom to our conversation. Now, that is powerful. And then we have the idea of co-creator workspaces. This is more like what I built for my use case. And so, this is

**[0:04:23]** where you're working with an agent. So, the canvas displays outputs and previews. it becomes this shared working space where our AI generated UI appears and evolves and so dashboards they literally have this as the example and that's exactly what I built. So just trying to get some ideas flowing for you

**[0:04:42]** of the kinds of applications you can build with this. I think e-commerce stores is another really good example where you have these recommendation algorithms that learn each user and not only is it going to recommend certain products but change the entire layout to focus on what it thinks the user should

**[0:04:57]** buy. We're going to see a lot of that in the future. And the other thing that's really important to understand with generative UI is there's actually a spectrum of how much control we're giving to the agent versus the programmer. So, we have three categories here. We got static UI, declarative UI,

**[0:05:12]** and open-ended UI. And I know that might sound a little bit like word salad right now, but don't worry, we'll get into this and it's important. And declarative UI, this is what I'm the most interested in. I think this is the most innovative and really what's following Google's A2

**[0:05:25]** UI specification where the agent will pick components from a library and then send that off for the front end to display dynamically. So starting with static generative UI, this is the most classic and we see this all the time throughout the web right now. So we're using the agent to really just decide

**[0:05:42]** the information to display. So it's not picking the components to render. It's not defining the layout. It's just saying like, okay, this is the temperature in New York City right now. So the agent is fetching this information but it's not deciding anything else in our UI. Then on the

**[0:05:57]** complete opposite end of the spectrum we have open-ended generative UI. And this is where the agent decides not just the components and layouts but it literally generates all of the code for the HTML, CSS, JSX, whatever on the fly to render in the front end. And so it is the most

**[0:06:14]** flexible. But obviously security and performance are a big concern here because really we're just rendering completely arbitrary content. So I don't know about you, but I wouldn't be very comfortable with my agent generating the entire UI on the fly for my users in an application. And so that's what leads us

**[0:06:32]** to the option in the middle, declarative generative UI. And so this is what I'm very interested in. It's the idea of we have a preconfigured library of components that the agent can choose from. So it can say I want this one, this one, this one. Let's put it in this

**[0:06:48]** layout and then here are the parameters. This is the exact data, the numbers and text to display. And so it still has a lot of freedom around what kind of interface we generate, but it's going to be within bounds that we get to control through the component library and the

**[0:07:03]** prompting for our agent. And I will say there are definitely pros and cons to these different kinds of generative UI. And so that's why it's important for us to choose a tech stack that is Gen UI agnostic. That's a tongue twister for me for some reason. But yeah, we have AGUI

**[0:07:18]** as our protocol. Like I said, for connecting our agents to our front end, it's going to work no matter if it is static, open-ended, or declarative GenUI. And then Copilot Kit as our front-end framework to render everything and work with our agent. This is also going to work no matter what. And so the

**[0:07:33]** use case that I'm showing you and what I'm most interested in is that in the middle we're picking from a component library, but we really can build any kind of application with this text stack. All right. So now that you know how generative UI works at a high level,

**[0:07:47]** I want to get more into my use case and really explain the text stack to you and how each layer communicates with each other because this will really drive home exactly how generative UI works. And then I promise I won't get too in the weeds, but I want to show you the

**[0:08:01]** code at least a little bit to help you understand how our agent has this component library to pick from and how we have this contract with the front end. So it knows what kind of components can it expect and exactly how does it render those. And so the first thing

**[0:08:16]** here of course is we have our input. This is the AI research that we've done with an agent that we want to extract the insights and the TLDDR from. And so I'll show you an example really quick here. So this is the homepage for my second brain research dashboard. I of

**[0:08:31]** course have been following along with all the developments with OpenClaw, otherwise known or previously known as Claudebot. And so I've been doing a lot of research with agents. This is one example of a markdown document that I had. And so I can just go ahead and send this in. Boom. There is the input. And

**[0:08:46]** now we instantly have the process triggered here where there's an agent working behind the scenes right now selecting the components and the layout. And take a look at that. Now we're 40% complete because it has classified the document. And so this is really how we're defining the layout. And now after

**[0:09:02]** that, it's going to select the individual components from the library. And so going back to our diagram here, we'll let this keep generating behind the scenes. The reason I care about this use case in the first place is because I've really been suffering from I'll call it markdown fatigue recently. I

**[0:09:18]** know it's a really silly thing, but as I'm using my second brain doing a lot of research with my agents, there's just always these walls of text that I have to parse through. As much as I try to keep my agents concise in their generations, I've just gotten so sick of

**[0:09:32]** reading through Markdown. That's what actually inspired me to build out this use case so I have these dashboards to extract insights a lot faster. And so, generative UI solves the problem here because it also adapts the content to what I need to know. And then if I ever

**[0:09:47]** think that the dashboard doesn't give me what I think I should know, then I just have to adjust the prompt for the agent. So it's really really flexible and I can evolve the system over time. It's just like the principles that I teach for agentic coding. And so we have our

**[0:09:59]** podantic agent in the back end. It takes this input and it defines the layout and the components just like we saw it starting to do in our browser. And so whenever it decides to generate a component, it's going to output a specific JSON. This is following the A2

**[0:10:15]** UI protocol. And so I've talked about this a little bit already, but essentially it defines like, okay, here's the ID for the component. Here is the name of the component. So the front end knows what to render. And then we have the children. So that helps define the layout as well. And then another

**[0:10:30]** thing that I'm not showing here is the props. And so for any component that we have in the front end, there's certain text numbers that we have to display. So the agent is deciding those as well, just like it would with static generative UI. And so the agent is going

**[0:10:44]** to come up with a bunch of these JSON configurations, all the components that it wants to send in, and then we're going to be streaming that to our front end through AGUI. So what we have here is a standard for events that the agent is going to emit to keep this real-time

**[0:11:00]** sync between our backend and our front end. And we saw that just now in the dashboard, the percentage went from zero to 40%, because the agent said, "Hey, I've started my run. I'm beginning to generate the dashboard." So we display that in our front end. And then it

**[0:11:12]** decides the layout and it moves on to generating the components. And so we update the progress in the front end. And I'm not doing it here, but we could also theoretically stream these components. So we watch the dashboard being built in real time. In my case, I'm just waiting for everything and

**[0:11:27]** displaying it all at once, but that would be possible as well. We have this really dynamic sync thanks to AGUI. And then of course, Copilot Kit makes that really easy to render everything. And it has that direct integration with AGUI and Pideantic AI as well. And so all

**[0:11:41]** this together just makes this really seamless experience of being able to have the front end connected directly to the agent. And this would be hundreds or even thousands of lines of code if I wasn't using Copilot Kit, AGUI, and Pideantic AI. And going into the code just a little bit here. I promise I'll

**[0:12:00]** stay high level. I just want to show you how we have this sort of contract between the backend and the front end. So we're giving the agent options. here are all of the different components that you can render. And so, as a part of our system prompt to the agent, we're

**[0:12:14]** describing when we wanted to use these different components and exactly how to define things like the props, what are the the text and numbers that you want to display in each component. And so, telling it what it has access to plus the system prompt is how we're guiding

**[0:12:28]** the agent for generating these components. And as a part of the system prompt, we're also describing to it the A2 UI specification. This is exactly how you output a component with the name, the props, the ID, that kind of thing. And then we have the same sort of

**[0:12:43]** contract in the front end. And so all of the same components are called out here, but in the front end, we have the actual JSX that we're going to render when the agent chooses that component as well as the props for the data that it wants to display. And so for every single one of

**[0:12:58]** the components here, I have it defined in this AGUI folder, just keeping it really nice and organized. And I won't show you all of these obviously, but I do have one of them right here. And just to show you how simple it is, it really is just a basic React component, but

**[0:13:12]** it's the agent that decides when we render this. And it decides all the values. Like for this table component, it decides here's the headers, here's the rows, this is the title and the the subtitle. And it's even optional. Like it decides all of that. It's the front end's job to receive the layout and the

**[0:13:28]** component requests and then map that to all these components that is going to generate. And it's not like we absolutely need Pantank AI or Copilot Kit to do this. I could use a different agent framework. You don't even really need to use AGUI. I don't need C-Pilot kit. I could even use a different

**[0:13:45]** specification besides A2UI. But man, does this text stack together just make it so easy for me to build these applications. I've been working on some other proof of concepts, building out this one in particular. It has been a blast and it just works so incredibly well. And so I know there's quite a few

**[0:14:01]** things that we got going on here, but together it makes these really powerful applications that and I really just do see this as the future of software. So let's actually go back to our dashboard here. So this is what we saw the start of the generation and now here we go.

**[0:14:15]** This is generated dynamically for us. We saw this appear in real time. And I know that like spacing and things is not perfect. This is more of just a demonstration for you. But I'm still just blown away by the kinds of things that we're able to generate here. It

**[0:14:29]** looks so so good. And by the way, this has actually helped me quite a bit with my research on on Claudebot or I guess I should say OpenClaw. And then also this alternative called Nano Claw, which I might cover in a video on my channel soon. So that's another really

**[0:14:43]** interesting alternative to OpenClaw. But anyway, I digress. you can see how easy it is to get sucked into the research you're doing with your agents. But for this video here, I really hope that you found it helpful with generative UI, understanding how it works, why it's so powerful, how you can build with it

**[0:14:59]** yourself. And I really do encourage you to take the template that I have linked in description and check it out yourself. And I will be doing more content on generative UI. And so if you're looking forward to that or just more content on building agents in general, I would really appreciate a

**[0:15:13]** like and a subscribe. And with that, I will see you in the next
