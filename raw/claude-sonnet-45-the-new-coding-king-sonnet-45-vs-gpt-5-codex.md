---
type: raw-transcript
title: "Claude Sonnet 4.5 - The New Coding King? (Sonnet 4.5 vs. GPT 5 Codex)"
youtube_id: P-0fm8ljl0I
url: https://www.youtube.com/watch?v=P-0fm8ljl0I
slug: claude-sonnet-45-the-new-coding-king-sonnet-45-vs-gpt-5-codex
published: 2025-09-29
duration: "0:11:15"
fetched_at: 2026-07-21
immutable: true
---

## Transcript

**[0:00:00]** The new king of AI coding is here. Enthropic just released Claude Sonnet 4.5 and it is looking really, really good. I know that benchmarks don't tell us the entire story, but right now Sonnet 4.5 is at the top of the charts, even beating out previous anthropic models like Opus 4.1, and it is

**[0:00:19]** apparently better than GBT codecs from OpenAI, which has been absolutely crushing it recently. Now, the big question is, is it actually better in practice? And so I'm going to be testing live with you in this video, building out the exact same implementation with both Sonnet 4.5 in Cloud Code and GPT5

**[0:00:38]** codecs in codecs. So more on that in a little bit. Really excited for that. And then for our other benchmarks, Sonnet 4.5 is now leading in aentic tool use. And compared to Opus 4.1, we have some massive strides in computer use. Almost a 20% jump, which is really exciting.

**[0:00:56]** Definitely a lot more with computer use coming in the near future here. Now, we also have the official Claude Code version 2.0. So, a lot of improvements they've made with Claude Code, of course, being powered by Sonnet 4.5 by default now. And you can still switch to the old Opus 4.1 if you want. They also

**[0:01:14]** added a VS Code extension. And they've been making improvements to their Cloud Code SDK, which they're now calling the Claude agents SDK. So if you want to build custom agentic experiences using cloud code, this is the ticket for you. So yeah, a lot of improvements that they've been making across the board.

**[0:01:31]** Anthropic has been pumping out a ton of content on their YouTube channel today. So they're going hard with their new Sonnet 4.5. And so with that, let's actually do a test here. I want to see how Sonnet 4.5 compares to GPT5 codecs when working on a new feature in an

**[0:01:47]** existing complex codebase. All right, take a look at this. On the left side, I've got Codeex running with GBT5 codecs for the LLM. And then for Cloud Code on the right hand side, I'm running the shiny new Sonnet 4.5. And I'm actually really curious what the results of this

**[0:02:04]** test is because I'm running this live with you. I did not do a dry run of this and a lot of people have been switching over to Codeex from Claude Code and so I'm really curious if Sonnet 4.5 is enough to bring everyone back. And I know that one single test really isn't

**[0:02:20]** enough to tell, but I'm just trying to get my feet wet here with you, seeing what kind of results that we get. Executing on the exact same requirements document that I have to build a Stripe integration into an existing agentic application. And so this is one of the

**[0:02:34]** applications that I have built out for the Dynamis community. It's a chat GBT like interface to talk to a rag agent behind the scenes. So I'm just giving a really simple demo here. And I already have the Stripe integration built out in a different branch in Git. But yeah, we

**[0:02:50]** can buy our tokens here. So I can go in and enter in a fake credit card information because this is just using the Stripe test account here. So I thought this is just going to be a really nice demo for comparing our two models now. So I'll go ahead and buy

**[0:03:03]** some tokens here just so you can see how this works exactly. I can go to my chat here and now I have my updated token balance and then when I send in another message, it deducts the tokens automatically. So this is like a little overview of what we're looking to build

**[0:03:16]** here with both cloud code and codeex. And I picked this use case specifically because it's not trivial, but it's also not going to take 2 hours for this implementation to complete. It's the perfect balance here where generally I've seen claude sonnet 4 mess up on the little things but still mostly get it

**[0:03:35]** right. And so we can see how that compares now with GBT 5 codecs and sonnet 4.5. So without further ado, let's go ahead and kick off the instruction set for both of our coding agents. And so they're both working on a different version of the repositories. They're not stepping on each other's

**[0:03:52]** toes. And also they're working on something that is pre-stripe integration. So this is the goal that we're working towards that I demoed earlier. They're working on a codebase that doesn't have this whole thing set up yet. So we'll go ahead and see how they perform. And I'll just show you

**[0:04:05]** really quickly the instruction set they're working with here. So I've showed PRPs on my channel before. It's basically just a structured approach to define our AI coding workflow. And so the command that we just executed, it's going to load our feature requirement, think through the implementation, break it down into tasks, and then handle that

**[0:04:23]** task by task. That's what we're executing right now in both codeex and claude code. And so I'll pull up both of these again. I'll go ahead and pause the video and then come back once we have the first attempt for both our coding agents and we'll see the results. All

**[0:04:38]** right, I'm back mid execution because I want to show you how things are going in cloud code and codeex while we are in the middle of building the application. So we've got codeex on the lefth hand side doing a lot of stuff with the database right now. It is failing to run

**[0:04:53]** a lot of these commands which is not looking the best for codecs and it's a lot slower to do things like read through my files in general. Claude sonnet 4.5 on the other hand has been blazing through this implementation. Now, in the end, what matters the most is code quality, but speed is nice as

**[0:05:09]** well. And it definitely seems like Sonnet is really, really fast, especially with new 4.5. And then going into Archon here, we can see the task list for both Codeex and Claude Code. Claude has gotten through quite a bit already. So, it just finished the front-end purchase components for Stripe

**[0:05:25]** for the tokens. Now, it's working on the display components. And then Codeex, they just finished the database schema changes. Now, working on some of the backend stuff with Stripe. So, they're both chugging along pretty well. Definitely a difference in speed though here. So, I'll come back again once we

**[0:05:41]** have the full implementation. We'll see who knocked it out of the park the best. There we go. Cloud code with Sonnet 4.5 has finished the implementation and it did it in 15 minutes. The entire Stripe implementation. It was very, very impressive. I actually did this exact same build with Opus 4.1 in the past and

**[0:06:00]** it took 35 minutes to build the whole thing. So more than two times faster now with 4.5. Now I verified the output before I even ran anything. I knew it made a couple of mistakes, just small things with the URLs between the front end and the back end. So I had to

**[0:06:16]** correct that. So it wasn't quite a oneshot, but it was really, really close. So I set up my environment and restarted my containers here. So now we have the same application that we saw earlier, but instead of the previous one that I built with Opus 4.1, this is the

**[0:06:31]** version now built with a Sonnet 4.5. Take a look at this. The UI is pretty nice. Maybe it could be a little bit better in the top right here, but still pretty good. And I send in a message. I don't have any tokens yet. Please purchase more to continue. So I'll go

**[0:06:45]** ahead and buy some tokens. And instead of buying in line, it actually brings me to a Stripe checkout here. I don't really know which one's necessarily better, but I mean this is certainly a good implementation as well. So, I have my test stripe running here. So, I'll just go ahead and enter in some fake

**[0:07:00]** credit card information. Again, have to enter in a little bit more cuz it's a checkout here. There we go. All right. Pay for my tokens in the sandbox environment. And boom, there we go. Current tokens 250. Go back to chatting. And now I'll send in a message just

**[0:07:15]** hello for a quick test and see if we get a response. There we go. All right, how can I assist you today? Looks like the token count did not update though. So, if I refresh my page, now it goes 249. So, a little bit of an issue there.

**[0:07:29]** Looks like I just have to iterate one more time to make everything perfect. But yeah, that's just two iterations and we have this full Stripe integration built into Claude Code. And meanwhile, Codeex is still going. this entire time as I did some updates even to like fix up the URLs and stuff. Codeex has been

**[0:07:49]** going for over a half hour now. And so I'm going to pause again and come back once codeex is done. But so far it's really really disappointing me. Actually, it looks like it's been going for almost an hour now because I gave it a lot of time. I took a break in between

**[0:08:06]** Claude being done and me doing these little fixes here and re-recording this. And so yeah, it's been going on for over an hour. So, Codeex seems pretty disappointing here. Sonnet 4.5 is doing a really good job. All right, I finally got Codeex to finish. It took 1 hour and

**[0:08:23]** 20 minutes in total for the implementation while Sonnet 4.5 took 15 minutes. So, the speed pretty disappointing. It seemed to do a lot of weird things where like after it would edit a file, it would reread the file to make sure the changes were made. things like that that again might be specific

**[0:08:39]** to codecs running on Windows, but I really wasn't happy with that. So anyway, I did the same thing with cloud code where I gave it a couple of chances. I iterated a couple of times with some similar issues it had around environment setup. This time more with some Docker things specifically. So I

**[0:08:55]** got that all squared away. I have the containers running in codecs again. And so let's go back over to the site and take a look at what we got. So first thing that I noticed, the UI isn't quite as nice. I mean, it'd be easy to fix that. So, that's totally fine. Let's see

**[0:09:08]** if we can purchase our tokens. So, purchase tokens. Okay, looking really good. And we even have a token history. Doesn't seem to be perfect here, but it's definitely cool that we have that. So, let's go ahead. I'll purchase $20 worth of tokens here. I'll select this and okay, nice. I think I do actually

**[0:09:26]** prefer this than going to a separate checkout page. So, so far the actual results with using Codeex is pretty good. I hate how long I had to wait, but I mean it did a pretty good job with the implementation. Things aren't perfect yet. Like the transaction history and

**[0:09:40]** the UI, but it's still pretty solid. Yeah, there we go. Payment successful. We have 600 tokens. The current balance isn't quite right because that's actually my old balance. So, things to be improved here. But yeah, our token balance is updated. I can send in a message here and it'll deduct a token

**[0:09:56]** from our agent. I might have to refresh the page for it to refresh here. Okay. So yeah, not quite perfect there either. So there's like three or four issues that we have to fix here. So not quite as good of an implementation as cloud code. This is why this is the perfect

**[0:10:11]** use case cuz it's not trivial. We see these problems as it messes up on things, but also like it does a good enough job where we can have a full presentation demonstrating the mistakes versus just the application crashing, right? So yeah, this is pretty good. And I can go in and reset my tokens down to

**[0:10:26]** zero and we can make sure that we are not able to send a message. Yep. Okay. So, this is working really good. So, overall, I would say that Claude Sonnet 4.5 was faster by a lot and better by a decent amount. Codeex is still really solid and I do think that we're going to

**[0:10:44]** get to a point really quick where it will catch up to Claude Code. However, with Sonnet 4.5, they're definitely winning the race right now. So, I hope that you found this comparison interesting, very exciting what we've got happening right now with Sonnet 4.5 continuing to push the LLM race further.

**[0:11:01]** So, if you appreciated this video and you're looking forward to more things on large language models and building agents and AI coding, I would really appreciate a like and a subscribe. And with that, I will see you in the next
