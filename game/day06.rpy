
label day06_start:
    scene 3nextday with fade
    $renpy.pause(3, hard=True)
    if lisa_path == True:
        jump lisa_day06
    else:
        jump work_day06


label lisa_day06:
    scene black with fade
    "Early in the morning you called Lisa and agreed to meet each other for lunch near the local Park."
    "Undoubtedly you had something to discuss."
    scene 6lisasteet00 with dissolve
    play music "music/7 - Just Happy.ogg"
    mc "{i}Um. Aside from Jade's sudden appearance, I think last night with Lisa was perfect.{/i}"
    mc "{i}I hope she feels the same way.{/i}"
    mc "{i}Judging by the tone in her voice over the phone, she's very positive.{/i}"
    mc "{i}That's a good sign.{/i}"
    "You went to the meeting place and began waiting for her."
    scene 6lisasteet01 with dissolve
    mc "{i}There she is! Right on time.{/i}"
    ls "Hello, [mc]."
    ls "You won't believe it, but I've already been missing you!"
    mc "Just like I missed you."
    "Lisa came up and kissed you."
    scene 6lisasteet03 with dissolve
    "..."
    scene 6lisasteet01a with dissolve
    ls "Hee hee. I'm glad."
    mc "{i}Mmm... It's great that she's so open with me.{/i}"
    mc "{i}Especially after how embarrassed she was last night.{/i}"
    mc "Seems like you're in a good mood."
    scene 6lisasteet02 with dissolve
    ls "Well, I guess you could say that."
    mc "Let me guess, your conversation with Jade went well?"
    ls "Very well! She understood perfectly and even wished us good luck."
    mc "Good to hear."

    if jacob_knows_about_lisa == True:
        scene 6lisasteet02a with dissolve
        ls "It's funny, but it looks like the whole band knows about our relationship now."
        ls "And I can't help but notice that I like it."
        mc "Me too."
    else:
        scene 6lisasteet02a with dissolve
        ls "And I think you should probably tell Jacob about our relationship as soon as possible, so he doesn't run into awkward situations like Jade."
        mc "Yeah, you're probably right."
        ls "Undoubtedly."

    scene 6lisasteet02b with dissolve
    ls "You know, when I joined the band, I had no idea where it would lead."
    mc "And yet, here we stand. Together."
    ls "Hmm... In that case, are we officially a couple now?"
    mc "It would appear so."
    scene 6lisasteet01a with dissolve
    ls "Heh. I like that!"
    mc "Yeah, me too."

    scene 6lisasteet04 with dissolve
    ls "Maybe we should get something to eat, because I'm starving."
    mc "{i}That's right, she managed to slip away from the University just for lunch.{/i}"
    mc "{i}We don't have much time.{/i}"
    mc "How about a bite to eat outdoors?"
    ls "Sounds good."
    mc "Okay, then let's go. There's some not far from here."
    ls "Lead the way, skipper!"
    stop music fadeout 3.0
    scene black with fade
    "A few minutes later."
    scene 6lisasteet05 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    "Just outside the park, you and Lisa spot a mobile hot dog cart."
    mc "{i}Great! It's in the same place as usual.{/i}"
    scene 6lisasteet06 with dissolve
    "You approached the vendor, studied the menu, and made your order."
    mc "Just to warn you, even if you don't like hot dogs, you're gonna love these."
    "Vendor" "Of course she'll love them! Frankly, everyone here is crazy for my wieners!"
    ls "Mmm... Okay, you've managed to intrigue me."
    ls "But where are we going with these hot dogs?"
    mc "Haven't you guessed yet? We go to the Park."
    ls "Oh... I don't know why I didn't think of that."
    mc "Don't worry."
    scene black with fade
    "After a while."
    scene 6lisasteet07 with dissolve
    ls "Man, this place is so cool!"
    ls "Birdsong. Fresh air. Sun. It's beautiful!"
    mc "Don't forget about the great company."
    ls "Ha ha! Well, of course! Great company is the most important thing here."
    ls "And without that company, none of this would be as interesting."
    scene 6lisasteet08 with dissolve
    "Suddenly, to your surprise, a gray cat jumped out from behind a tree."
    mc "{i}Wow... He's fast.{/i}"
    scene 6lisasteet09 with dissolve
    "The cat slowed its approach and stopped in front of Lisa."
    ls "Why are you looking at me like that, buddy?"
    mc "You know, I don't think he's looking at you, he's looking at your hot dog."
    ls "Hm? It's true!"
    ls "He must have smelled it."
    mc "Yeah, the lil guy must be hungry."
    scene 6lisasteet10 with dissolve
    "Still staring at the food, the cat lay down on the grass and began wagging its tail."
    mc "{i}This cat probably gets fed here often, so he picked up a few tricks.{/i}"
    scene 6lisasteet11 with dissolve
    ls "Well, I guess I don't have a choice. We'll have to feed the poor lil guy."
    mc "{i}And the trick has worked once again.{/i}"
    mc "Just be careful. I wouldn't want him to bite you."
    ls "Hee hee. Don't worry, [mc], animals love me."
    mc "I hope so."
    scene 6lisasteet12 with dissolve
    "Lisa pulled the frank out of the bun and beckoned the cat to her."
    ls "Come on, buddy, don't be shy. We both know that's what you want."
    scene 6lisasteet13 with dissolve
    "Cat sniffs."
    "..."
    mc "Look, he's debating on whether or not to eat it."
    mc "That little shit."
    ls "Heh. What did you expect? It's a cat! They're all so picky."
    scene 6lisasteet14 with dissolve
    "Very slowly, the cat carefully began to bite the sausage."
    ls "Attaboy. Good kitty."
    ls "Eat, take your time."
    mc "{i}Yeah, he eats for free and that makes him a nice cat.{/i}"
    scene 6lisasteet15 with dissolve
    ls "Look, he likes this sausage."
    mc "No doubt. It's the best fast food in the area."
    ls "I'm sure he appreciated that."
    mc "You betcha."
    scene 6lisasteet16 with dissolve
    "Cat quickly ate the food Lisa offered and made a very strange pose."
    mc "I'm not an expert on cat behavior, but I think he likes you."
    ls "Yep. Probably because I just fed him."
    mc "Probably."
    ls "So, buddy, you want me to stroke your back?"
    scene 6lisasteet17a with dissolve
    "Cat" "Mew!"
    scene 6lisasteet15 with dissolve
    ls "Wow! [mc] did you see that?! It's like he understood me!"
    mc "Yeah, I saw."
    mc "Smart cat."
    scene 6lisasteet17 with dissolve
    "Lisa began to slowly stroke the cat on the back, to which he closed his eyes and purred loudly."
    ls "Hee hee. Look at him, looks like he's enjoying himself."
    mc "{i}Hmm... Looks like he's not the only one.{/i}"
    mc "{i}True, I can't tell which of the pair is enjoying it more.{/i}"
    ls "Come here."
    scene 6lisasteet18 with dissolve
    "Lisa took the cat in her arms and began to squeeze it."
    "To your surprise, he didn't even resist."
    ls "Nice kitty. Very nice."
    scene 6lisasteet19 with dissolve
    ls "Hey, [mc], you want to pet the kitty?"
    ls "I don't think he'll mind."
    mc "{i}Judging by the look he's giving me, I'm not sure.{/i}"
    mc "{i}Though...{/i}"
    menu:
        "{color=#66FF33}Pet the cat":
            $ goodpoint += 1
            $ RPls += 2
            mc "Why not?"
            mc "But if he scratches me, it's your fault. OK?"
            ls "Ha! Nope! If he bites you, it's your fault."
            mc "All right, all right, give it here."
            scene 6lisasteet20 with dissolve
            "Lisa released the cat to the ground and gently prodded him in your direction."
            ls "Don't be afraid of him."
            mc "I'm not afraid of him."
            ls "Emm... Actually, I was talking to the cat, not you."
            mc "Oh..."
            ls "Yeah."
            mc "{i}Okay, be a good kitten and please don't bite me.{/i}"
            if cheat_point >= 5:
                stop music fadeout 1.0
                scene 6lisasteet21 with dissolve
                "As soon as your hand was near the cat, he arched and loudly hissed at you."
                "Cat" "Sshhhhhh!!!"
                mc "Okay, looks like he doesn't like me."
                play music "music/6 - Positive Mood.ogg"
                ls "Strange, why did he make so much noise?"
                mc "Who knows?"
                scene 6lisasteet24a with dissolve
                ls "That's too bad... But at least you tried."
                mc "Yep... Tried."
                "..."
                scene 6lisasteet25 with dissolve
                "Suddenly, the cat twitched his ears, looked away from you, and departed as quickly as it had appeared."
                mc "{i}What an asshole!{/i}"
            else:
                scene 6lisasteet22 with dissolve
                "With a little care, you ran a hand through the soft fur of a cat."
                "Cat" "Puuurrr... Purr... Purr..."
                mc "Look, he seems to like it!"
                scene 6lisasteet24 with dissolve
                ls "Well, of course! I told you he was good."
                mc "Yep. Looks like you were right."
                ls "Hehe. Naturally."
                ls "I'm a very smart girl. You should listen to me more often."
                mc "Heh. Whatever you say."
                scene 6lisasteet23 with dissolve
                "You turned your attention back to your furry new friend."
                mc "{i}Let's scratch behind your ear.{/i}"
                "Cat" "Puuurrr... Purr... Purr..."
                "..."
                mc "{i}Um. That's nice.{/i}"
                scene 6lisasteet25 with dissolve
                "Suddenly, the cat twitched his ears, looked away from you, and departed as quickly as it had appeared."
                mc "{i}What an asshole!{/i}"

        "Refuse Lisa's offer ":
            $ badpoint += 1
            mc "I'm sorry, but I don't think that's a good idea."
            mc "I'm not very good with cats."
            ls "Well, whatever."
            scene 6lisasteet20 with dissolve
            "Lisa stopped stroking the cat and let him go to the ground."
            mc "{i}Um. Why is he studying at me?{/i}"
            "..."
            scene 6lisasteet25 with dissolve
            "Suddenly, the cat twitched his ears, looked away from you, and departed as quickly as it had appeared."

    scene 6lisasteet26 with dissolve
    ls "Oh... guess he's bored of our company."
    ls "That's a little sad."
    mc "Or he smelled another snack nearby and decided to not miss his chance."
    scene 6lisasteet27 with dissolve
    ls "You're right, with that little glutton, we can't rule that out as an option."
    "..."
    scene 6lisasteet27a with dissolve
    ls "Ummm... [mc]. Since we're alone again, I wanted to talk to you about what happened yesterday..."
    mc "{i}Well... She's embarrassed again.{/i}"
    mc "Of course, I'm listening."
    scene 6lisasteet27b with dissolve
    ls "The thing is, my roommate is away for two days on business..."
    mc "So..."
    scene 6lisasteet27a with dissolve
    ls "And we were pretty rudely interrupted yesterday, so if you want..."
    "..."
    scene 6lisasteet27b with dissolve
    ls "If you want, come to my place tonight. We can continue where we left off before."
    mc "{i}Wow... That's really good news!{/i}"
    mc "With pleasure."
    scene 6lisasteet27 with dissolve
    ls "Great!"
    ls "And I think my allotted time is running out. I'm sorry, but I have to get back to the University."
    mc "It's okay, I understand."
    ls "In that case, I'll see you tonight?"
    mc "Certainly."
    scene 6lisasteet28 with dissolve
    "..."
    scene 6lisasteet27 with dissolve
    ls "Bye."
    stop music fadeout 3.0
    scene black with fade
    "A few hours later."
    jump work_day06


label work_day06:
    scene black with fade
    "Today was your shift at the bar, so you went in to work as usual."
    play music "music/1 - Atmosphere.ogg"
    scene 6work01 with dissolve
    "Entering the bar, you stumbled into Anna and a man you've never seen before."
    mc "{i}Hm? Who's that? An unfamiliar face.{/i}"
    "You heard the echoes of their conversation."
    a "...in that case, if you have any questions, you can always contact me."
    "Man" "Don't worry, ma'am, I've got it covered."
    mc "{i}Looks like a new employee. And judging from recent events, we can assume that this is the new security guard.{/i}"
    mc "{i}Well, in that case, good-bye, old Tom. You knew exactly what you were doing when you decided to cheat on your boss right under her nose.{/i}"
    scene 6work02 with dissolve
    a "Oh... [mc]! I didn't see you come in."
    "Man" "..."
    mc "{i}This guy doesn't look surprised at all. Apparently he spotted me earlier.{/i}"
    scene 6work03 with dissolve
    a "Since you're here, let me introduce our new security guard, Vincent."
    a "[mc] this is Vincent, Vincent this is [mc]."
    scene 6work02 with dissolve
    a "[mc] is a bartender, and also started working here recently. I think you'll find a common language."
    scene 6work04 with dissolve
    "After Anna introduced you, you shook hands."
    scene 6work05 with dissolve
    v "Nice to meet you, [mc]. I hope we get along."
    mc "{i}Wow, he's got a strong grip!{/i}"
    scene 6work04 with dissolve
    mc "The pleasure is mine."
    mc "{i}Thankfully this guy's not as creepy as Tom. At least at first glance.{/i}"
    mc "{i}That's good.{/i}"
    scene 6work06 with dissolve
    a "Okay, boys, I'm sure you'll get to know each other."
    a "In the meantime, [mc], can you follow me to the office? There's something we need to discuss."
    mc "{i}I think I already know the subject.{/i}"
    mc "Sure. No problem."
    a "Okay, then let's go."
    scene 6work07 with dissolve
    "..."
    mc "{i}Hmm... Pleasant view.{/i}"
    mc "{i}I'm sure she knows that, though.{/i}"
    mc "{i}...{/i}"
    mc "{i}Hey! Stay awake! Don't keep the girl waiting.{/i}"
    stop music fadeout 3.0
    scene black with fade
    "Few minutes later."
    scene 6work08 with dissolve
    play music "music/15 - Deep Mood.ogg"
    if anna_sex == True:
        "When you entered Catherine's office, you felt a sense of déjà vu."
        mc "{i}The last time we came in here with Anna, we ended up having sex.{/i}"
        mc "{i}But I don't think it'll go the same way, this time.{/i}"
        scene 6work09 with dissolve
        a "So, [mc], I think you already know what I wanted to talk to you about."
        mc "I think so."
        a "Good."
        scene 6work09c with dissolve
        a "I think what happened between us that night was a mistake. Very nice, but still a mistake."
        a "I was upset about breaking up with Tom, and you just wanted to comfort me. Thank you for that, but let it be over."
        mc "Really..."
        a "I'm sorry, but I'm smart enough to know now that romance at work is never a good idea."
        mc "{i}What am I supposed to say to her?{/i}"
        menu:
            "She's right, it was a mistake":
                $ anna_colleague = True
                mc "I have to agree with you."
                mc "We better stop this before it goes too far."
                scene 6work09a with dissolve
                a "Well, I'm glad you agree with me."
                a "That's all I wanted to clear up. Now you can get back to work. We're opening soon."
                mc "Of course."
            "{color=#66FF33}You want to give this relationship a try":
                mc "{i}Um. This isn't the first time she's tried to get off the hook.{/i}"
                mc "{i}Don't think you'll get away that easily.{/i}"
                mc "Ahem... I understand your reasons, but I think you're making a hasty decision."
                scene 6work09a with dissolve
                a "Oh really?"
                mc "Exactly. Please, let me explain."
                a "Okay, I'm listening."
                mc "The thing is, we've only known each other for a short time, so I don't know much about you... And yet, I'm wise enough to know that I absolutely do not want to lose a unique girl like yourself."
                a "[mc] I already told you..."
                mc "Wait, I didn't finish."
                scene 6work09b with dissolve
                a "Okay, go ahead."
                mc "We've only socialized at work. Neither of us have seen the other in everyday routines. As I see it, that leaves a certain impression."
                mc "I'm not suggesting anything serious right now, but how about we go out tomorrow afternoon just for a coffee."
                mc "And if you decide then that you're not interested, so be it. We'll just be conventional colleagues."
                mc "Well, what do you say to that?"
                scene 6work09c with dissolve
                a "Hmm... Drink one non-binding coffee?"
                mc "Exactly."
                a "Okay. I agree."
                mc "That's great!"
                scene 6work09a with dissolve
                a "Okay, now you need to get back to work. We're opening soon."
                mc "I'm leaving."
    else:
        $ anna_colleague = True
        "When you went into Catherine's office, you felt a sense of déjà vu."
        mc "{i}It's probably just my imagination.{/i}"
        scene 6work09 with dissolve
        a "So, [mc], I think you already know what I wanted to talk to you about."
        mc "I think so."
        a "Good."
        scene 6work09c with dissolve
        a "Last time I saw you, I was a little off. You understand the circumstances."
        mc "Certainly. I'm sorry about Tom."
        a "Yes, thanks."
        scene 6work09b with dissolve
        a "Actually, I'd like to keep that moment of weakness between us. OK?"
        mc "Sure, no problem."
        scene 6work09a with dissolve
        a "Well, I'm glad you agree with me."
        a "Okay, now you need to get back to work. We're opening soon."
        mc "Of course."

    scene 6work10 with dissolve
    "The last thing you saw when you left Catherine's office was Anna sprawled out in the boss's chair."
    mc "{i}Heh. As far as I know, Catherine's coming back tomorrow.{/i}"
    mc "{i}It looks like Anna's last day sitting in this position.{/i}"
    mc "{i}Catherine should be pleased after such an impressive performance.{/i}"
    stop music fadeout 3.0
    scene black with fade
    "You went back down to the bar and started your shift."
    if lisa_path == True:
        jump lisa_night_day06
    if lisa_path == False and anna_colleague == True:
        "Next day."
        jump work_day06v
    else:
        jump coffee_anna_day06

label lisa_night_day06:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    scene black with dissolve
    "Few hours later."
    "After you finished your shift, you said goodbye to your colleagues and headed over to Lisa's."
    scene 6lishome00 with dissolve
    play music "music/8 - Intro Music.ogg"
    mc "{i}Here I am.{/i}"
    mc "{i}I still can't believe that Lisa decided to invite me over, and even with a faint hint of sex.{/i}"
    mc "{i}Okay, better not slow down now.{/i}"
    "Knock knock!"
    scene 6lishome01 with dissolve:
        ypos -1.90
        ease 8 ypos 0.0
    "The front door opened and before your eyes is Lisa in a very unusual outfit."
    mc "{i}Wow... Just wow...{/i}"
    mc "Lisa, you look just... Just... Amazing!"
    ls "Huh! I can tell by your slack jaw."
    ls "But thanks for the compliment anyway."
    scene 6lishome02 with dissolve
    ls "Please, come inside."
    mc "Yes, certainly."
    mc "{i}Hell, I'm not sure if I'm seeing right, but it's like she's glowing...{/i}"
    scene 6lishome03 with dissolve
    "Heading in, you can't help but admire the beautiful ass on your girl."
    mc "{i}But really! This is my girlfriend now.{/i}"
    mc "{i}And I can't help but notice that the short plaid skirt and sexy pantyhose really suit her.{/i}"
    mc "{i}I can't wait to get them off her.{/i}"
    scene 6lishome04 with dissolve
    "Suddenly Lisa stopped by the white chair."
    mc "{i}Hm?{/i}"
    scene 6lishome05 with dissolve
    ls "Come on, feel free to sit right here."
    mc "Why is that?"
    ls "Just do what I ask, and I promise you won't regret it."
    mc "Ummm... Okay."
    scene 6lishome06 with dissolve
    "As requested by Lisa, you sat in the chair, and felt her lay a hand on your shoulder."
    mc "Okay, tell me, what do you want to do with me here?"
    ls "Mmmm... Don't rush things."
    mc "{i}Ooh... Has she decided to play games with me?{/i}"
    scene 6lishome07 with dissolve
    ls "You know, I've been thinking a lot about what happened last night, and I realized that I was being selfish."
    mc "What do you mean?"
    scene 6lishome08 with dissolve
    ls "I mean, you gave me pleasure, and I left you completely unsatisfied..."
    ls "It was very wrong. Especially now that you're my boyfriend."
    mc "{i}Okay, I'll be happy to play along.{/i}"
    mc "Well, I can't argue with that. When I said goodbye to you, I was really on edge."
    scene 6lishome07 with dissolve
    ls "You poor thing."
    ls "But don't worry, today I will try to correct that mistake."
    mc "Heh. Can't wait."
    scene 6lishome09 with dissolve
    "Lisa stood right in front of you and gave you a big smile."
    ls "What was it you told me yesterday?"
    ls "Relax and enjoy."
    mc "{i}Oh yeah... I like where this is going!{/i}"
    scene 6lishome10 with dissolve
    "The next moment, Lisa's mini skirt slid down her beautiful legs and dropped to the floor."
    mc "{i}She looks so good in those black panties!{/i}"
    scene 6lishome11 with dissolve
    "Slightly shaking her hips, the girl began to approach you."
    scene 6lishome12 with dissolve
    mc "You know, you're turning me on more and more with every second."
    ls "Mmmm... Wait, there'll be more."
    mc "Huh! You've got me intrigued!"
    mc "{i}Yeah, let's see what happens next...{/i}"
    scene 6lishome13 with dissolve
    "Without taking her eyes off you, Lisa slowly knelt down."
    mc "{i}Hell, from the look on her face, she likes it as much as I do!{/i}"
    mc "{i}I wonder how many more surprises she's going to give me...{/i}"
    scene 6lishome14 with dissolve
    "She seductively dropped to all fours and began to crawl towards you like a cat."
    "Her hand started to slowly slide up your pant leg."
    mc "{i}Mmmm... Nice.{/i}"
    scene 6lishome15 with dissolve
    ls "I'm really sorry I left you without sweets yesterday..."
    ls "I hope I can make things right tonight."
    mc "Maybe, but you'll have to try hard!"
    ls "Hee hee! I'm sure."
    scene 6lishome16 with dissolve
    "Only a few centimeters now separated Lisa from the goal."
    "Her little fingers slid smoothly to the fly on your pants."
    mc "{i}Come on, baby, just a little more...{/i}"
    scene 6lishome17 with dissolve
    "The girl's hands groped your dick through the jeans and started to stroke it."
    ls "Mmm... Is it me or is your friend starting to get bigger?"
    mc "He's just waking up baby."
    ls "Perfect! Then let's take a look at him."
    "Lisa quickly pulled your pants off, and her eyes immediately fell on your cock."
    scene 6lishome18 with dissolve
    ls "Wow..."
    ls "He looks even bigger up close."
    mc "{i}So I wasn't the only one staring at the other on the beach...{/i}"
    mc "He's just so damn glad to see you."
    scene 6lishome19 with dissolve
    "Lisa's hot fingers lay on the trunk of your cock and gently began to feel it."
    mc "{i}Oh yeah... Now it's getting nice.{/i}"
    scene 6lishome20 with dissolve
    ls "I hope you don't mind if I work here for a while."
    mc "He's all yours."
    ls "Mmmm... Perfect..."
    scene 6lishome21 with dissolve
    "Now you could see the girl's entire palm wrapped around your cock."
    mc "{i}Ohhh... It's like she's stretching it out, going further and further every second.{/i}"
    mc "{i}And the look in her eyes... It's hypnotizing.{/i}"
    scene 6lishome22 with dissolve
    mc "{i}Oh yeah!{/i}"
    "You felt Lisa's wet tongue touch the head of your dick."
    ls "Mmmm... I hope you're enjoying it."
    mc "I am..."
    ls "Hee hee. Good..."
    scene 6lishome23 with dissolve
    "Feeling confident that she was doing well, Lisa continued her work."
    mc "{i}Ooooh... I struggle to not just shove my dick down her throat.{/i}"
    mc "{i}But I should just let her work. I don't want to rush things...{/i}"
    mc "{i}Moreover, it looks like this girl has a plan.{/i}"
    stop music fadeout 3.0
    scene 6lishome24 with dissolve
    ls "Mmmmm..."
    "Lisa pressed her soft lips to your dick, while still stroking you with her hand."
    mc "{i}Yeah... I've been waiting for this!{/i}"
    mc "Yeah, baby, don't stop..."
    scene 6lishome25 with dissolve
    "To your surprise, Lisa stopped."
    mc "Ummm.... Something wrong?"
    ls "No... Not really."
    scene 6lishome26 with dissolve
    play music "music/15 - Deep Mood.ogg"
    "The next moment, the girl was on your lap."
    mc "Oh... that was unexpected."
    "Your hands immediately fell on her body, stroking her slender waist and hips."
    mc "Are you teasing me?"
    ls "Heh. Maybe just a little bit."
    scene 6lishome27 with dissolve
    mc "{i}Okay, let's get rid of this piece of fabric and take a look at your beautiful breasts...{/i}"
    scene 6lishome27a with dissolve
    "..."
    scene 6lishome28 with dissolve
    mc "{i}That's much better.{/i}"
    mc "You know, you're so beautiful, I'm a little jealous of your boyfriend."
    ls "Huh! Although, he doesn't have best sense of humor, he was lucky to find a smart and beautiful girlfriend. Can't argue with that."
    scene 6lishome29 with dissolve
    "Your hand quietly moved to Lisa's chest and began to gently massage it."
    ls "Aaahhh..."
    mc "{i}Uhhh... Looks like this part of her body is very sensitive.{/i}"
    ls "I see you're eager to continue..."
    mc "Well, of course! Someone told me I should just relax and enjoy myself."
    scene 6lishome30 with dissolve
    ls "I'm sorry I'm so slow, it's just a little unusual for me..."
    mc "{i}Looks like she's not used to being so proactive... Well, in that case...{/i}"
    mc "Enough talk! I'll take the lead."
    scene 6lishome30a with dissolve
    ls "Hey! That's not what I meant!"
    mc "{i}Judging by your smile, it is what you meant.{/i}"
    mc "No more objections. Come here, baby."
    scene 6lishome31 with dissolve
    "You picked up Lisa and carried her towards the sofa."
    mc "Now you're going to show me what you were going to do."
    ls "Hee hee hee! [mc], what are you doing! Let me go, I can walk myself!"
    scene 6lishome32 with dissolve
    mc "I don't doubt it, but I want to carry you a little."
    mc "You wouldn't refuse me that request, would you?"
    ls "No... Of course not."
    "..."
    scene 6lishome32a with dissolve
    ls "Ummm... [mc]."
    mc "Yes?"
    ls "Kiss me."
    mc "With pleasure."
    scene 6lishome33 with dissolve
    "Your lips met in a kiss, and you felt Lisa's gentle tongue."
    mc "{i}Yes... I'll never get tired of that.{/i}"
    scene 6lishome34 with dissolve
    "There you stood in the middle of the room making out with a nude beauty, huge boner hanging out."
    mc "{i}Amazing day.{/i}"
    ls "Mmmm..."
    mc "{i}Perhaps it's time to move on to the next step...{/i}"
    scene 6lishome32 with dissolve
    ls "Wow... that was very nice."
    mc "Yes, I agree."
    scene 6lishome32a with dissolve
    ls "Now tell me what you want most right now, and we'll see if I can make it happen."
    scene 6lisafj01 with dissolve
    "You lay Lisa on the sofa and studied her gorgeous body."
    mc "{i}Tempting offer... What do I want from you?{/i}"

    $ question06a = False
    $ question06b = False
    $ question06c = False
    $ question06d = False

    menu lisa_sex_day06:
        "Handjob" if question06a == False:
            scene 6lisafj01 with dissolve
            mc "I want your cute little hands on my dick to continue what they were doing before."
            scene 6lisafj01a with dissolve
            ls "Mmm... I think that can be arranged."
            mc "Then what are we waiting for?"
            ls "Ha! Really."
            scene 6lisafj01b with dissolve
            ls "Come here, babe, I'll take care of you..."
            mc "Can't wait."
            scene 6lisahj01 with dissolve
            "The next moment you were lying across from each other, your cock firmly clamped in Lisa's hand."
            mc "{i}Uhhh... She seems determined.{/i}"
            ls "Maybe we shouldn't keep your big dick bored any longer."
            mc "That's true."
            ls "Ohhh... You naughty boy!"
            show anim11
            "The girl's hand began to confidently masturbate your cock, while her hypnotizing gaze was directed straight into your eyes."
            mc "{i}Ohhh... What a thrill...{/i}"
            ls "Mmm... I think it might be a good idea to add a little stimulation here..."
            mc "{i}(Hey... What does she mean?){/i}"
            ls "Use your imagination."
            mc "Oh... Ahh..."
            ls "You probably can't see from here, but my pussy's already wet..."
            ls "Mmm... Just imagine how your big cock gets in there and starts fucking me with all your might."
            mc "Ohhhh... Go on, don't stop!"
            ls "Yes... You move your hips, and my lingering moans grow louder and louder."
            ls "I don't know how much more I can take..."
            mc "Oh... I think I'm going to cum too!"
            scene 6lisabj07a with dissolve
            "Lisa quickly fell closer to your dick and began to masturbate you even more."
            show anim24
            ls "Come on, baby, give all you've got! Fill me with your sperm!"
            mc "Aaahhh!!!"
            mc "I almost..."
            ls "I'm ready... Come on! Cum!!!"
            mc "Oh, fuck, yes! Here it comes!!!"
            scene 6lisabj07 with flash
            mc "Ooooooh... yes..."
            ls "..."
            scene 6lisabj08a with dissolve
            ls "You did good, babe."
            mc "Thanks to you."
            ls "Hehe. That's true."
            "..."
            ls "But it looks like you're still full of energy..."
            ls "Maybe you'd like to try something else?"
            $ question06a = True
            $ question06d = True
            jump lisa_sex_day06

        "Footjob" if question06b == False:
            scene 6lisafj01 with dissolve
            mc "You know, I've always liked your pretty feet."
            scene 6lisafj01a with dissolve
            ls "Ha! Are you for real?"
            mc "Yep."
            ls "It's a little weird, but why not?"
            scene 6lisafj01b with dissolve
            ls "Come here, babe, I'll take care of you..."
            mc "Can't wait."
            scene 6lisafj02 with dissolve
            "You sat down beside Lisa, gently grabbed her left foot and began to massage."
            ls "Mmm... So you like my legs... Right?"
            mc "You have no idea how much."
            ls "Hee hee! Judging by that big boner, I have a pretty good idea."
            scene 6lisafj03 with dissolve
            "The next moment, Lisa grabbed her chest, as her foot gently touched your cock."
            mc "{i}Yeah... That's hot...{/i}"
            ls "Mmm... Do you want me to continue?"
            mc "Yeah, baby, don't stop..."
            scene 6lisafj04 with dissolve
            ls "Oooh.... Your dick is so big..."
            ls "You probably want me to cheer him up a little."
            mc "I do..."
            scene 6lisafj06 with dissolve
            "Lisa lay flat on her back, and wrapped both her feet around your penis."
            mc "{i}That's better...{/i}"
            ls "Mmm... and now to get things moving..."
            show anim12
            mc "Ohhh... Yeah..."
            ls "Your cock is so hard and hot..."
            ls "Don't hold back..."
            mc "{i}(Mmmm... I'm not sure I can hold back right now...){/i}"
            mc "{i}(It feels good...){/i}"
            mc "Ohh!.... Oooohhh..."
            ls "Baby, if you want, we can change positions... I can do it from behind..."
            mc "Aahhh... I like your ingenuity..."
            ls "Hee hee! I'm glad!"
            scene 6lisafj07 with dissolve
            "Lisa turned turned over, her cute ass facing you."
            mc "{i}(I don't know where she learned that, but it's cool...){/i}"
            ls "Now let's start round two."
            show anim22
            ls "Mmm... How do you like my feet?"
            mc "God, they're great..."
            ls "Hee hee! That's good..."
            mc "Yes! Like this!!!"
            mc "Baby, just don't stop."
            ls "I won't."
            mc "Ooohhh, I think... I don't think I can hold out for long..."
            ls "Don't be shy, you can cover me in your thick cum."
            ls "I want it..."
            mc "{i}(Oh, what is she doing to me?..){/i}"
            mc "Lisa, almost..."
            ls "Come on! Let it out! Cum on me!!!"
            ls "Do it right on my butt."
            mc "Since you're asking for it..."
            scene 6lisafj08 with dissolve
            mc "Aaaahhhh!!!"
            scene 6lisafj08a with flash
            mc "Ooooooh... yes..."
            scene 6lisafj08b with flash
            "..."
            mc "{i}(Uhh... That was fucking awesome.){/i}"
            scene 6lisafj09 with dissolve
            ls "Wow... I think that went well!"
            ls "But it looks like you're still full of energy..."
            mc "Thanks to you."
            ls "Maybe you want to try something else?"
            $ question06b = True
            $ question06d = True
            jump lisa_sex_day06

        "Blowjob" if question06c == False:
            scene 6lisafj01 with dissolve
            mc "I can't help but notice that I really liked the feeling of your tongue on my cock."
            scene 6lisafj01a with dissolve
            ls "Mmmm... That's not surprising."
            ls "You want to feel my tongue there again?"
            mc "I'm sure you already know the answer."
            ls "Yeah, I do."
            scene 6lisafj01b with dissolve
            ls "Come here, babe, I'll take care of you..."
            mc "Can't wait."
            scene 6lisabj01 with dissolve
            "While you were making yourself comfortable, Lisa quickly moved to the end of the sofa."
            ls "Wow! I see your cock is all ready for battle."
            mc "He's been ready ever since I walked into your home."
            ls "Mmm... Interesting..."
            scene 6lisabj02 with dissolve
            "The girl smoothly fell to your dick and gently touched him with her pretty face."
            "You felt her hot breath on your cock."
            ls "You know, this makes me so horny..."
            mc "{i}Ohhh... And you should know how it turns me on.{/i}"
            scene 6lisabj03 with dissolve
            "Without taking her eyes off you, Lisa picked up your cock and began to smoothly crank it."
            ls "You seem to like my tongue..."
            mc "I do."
            ls "It really likes you, too."
            scene 6lisabj04 with dissolve
            "Lisa's wet tongue slowly licked the head of your cock and then began to slide up and down."
            mc "Oh yeah... It feels good..."
            ls "Mmmmm..."
            mc "Go on..."
            scene 6lisabj04a with dissolve
            ls "Perhaps it's time to move on to something more intimate, you think?"
            mc "{i}Damn, it's like she's reading my mind.{/i}"
            mc "Ahhh... Yeah, put it in your mouth..."
            show anim16
            ls "Mmmm..."
            mc "{i}Yes! Finally!!!{/i}"
            mc "{i}This girl is so hot...{/i}"
            mc "Yes, suck that dick! Yessss..."
            ls "Mmmm mmmmph mmmps..."
            mc "{i}(Trait... despite her modesty, Lisa is surprisingly good at everything.){/i}"
            ls "Mmm hmmm..."
            mc "What a thrill... This is crazy!"
            ls "Mmmmmmph gagggguu aaaauu..."
            scene 6lisabj05 with dissolve
            mc "Lisa, almost..."
            mc "Lisa, I think I'm gonna cum."
            ls "Mmmmmmmppppphhhsss...."
            scene 6lisabj06 with dissolve
            mc "{i}Oooohhh... She doesn't stop...{/i}"
            mc "{i}Looks like I'm gonna have to cum in her mouth... Wow!{/i}"
            scene 6lisabj06a with dissolve
            mc "Oh, fuck, yes! Here it comes!!!"
            scene 6lisabj09 with flash
            mc "Yeeeessss!!!"
            ls "..."
            mc "Damn... It was something."
            scene 6lisabj10 with dissolve
            "Lisa raised her head, and you immediately realized that her mouth is full of your sperm."
            mc "{i}Oh, I think I went a little overboard.{/i}"
            scene 6lisabj11 with dissolve
            "..."
            scene 6lisabj12 with dissolve
            "..."
            mc "Wow."
            scene 6lisabj13 with dissolve
            ls "That's it. I hope you enjoyed it."
            mc "{i}Yeah...{/i}"
            ls "But it looks like you're still full of energy..."
            mc "Thanks to you."
            ls "Maybe you want to try something else?"
            $ question06c = True
            $ question06d = True
            jump lisa_sex_day06

        "Finish" if question06d == True:
            mc "No, I think I'm done for the day."
            
    stop music fadeout 1.0
    scene 6lishome35 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "Exhausted, you and Lisa wearily lounge on the sofa."
    ls "So, did I make it up to you for yesterday?"
    mc "She asked with a sly smile on her face."
    ls "Come on!"
    mc "Ha ha ha!"
    scene 6lishome36 with dissolve
    mc "To be honest, I still can't believe I found such an amazing girlfriend."
    ls "Mmm... Yeah, you sure got lucky with me."
    mc "Ha ha! That's so true."
    scene black with fade
    "Some time later."
    scene 6lishome37 with dissolve
    ls "Ummm... I guess it's time to say goodbye."
    ls "Thank you for coming to see me today."
    mc "Thank you. I had a great time."
    ls "Yep."
    mc "And I hope we're close enough to see this game through to the end next time."
    scene 6lishome37a with dissolve
    "..."
    mc "{i}She seems lost in thought.{/i}"
    "..."
    scene 6lishome37 with dissolve
    ls "I think I've gotten to know you well enough for that..."
    mc "{i}Wow! I like that answer!{/i}"
    mc "Great!"
    mc "Until next time, then."
    ls "Until next time."

    $ renpy.end_replay()
    if not persistent.day06lisa:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day06lisa = True    

    scene black with fade
    stop music fadeout 3.0
    "In high spirits, you went home."
    "There was a new day ahead of you."
    if anna_colleague == True:
        "Next day."
        jump work_day06v
    else:
        jump coffee_anna_day06
  
label coffee_anna_day06:
    scene black with fade
    "Next morning."
    "You were sitting in a cafe waiting for Anna to show up."
    scene 6anncof01 with dissolve
    play music "music/7 - Just Happy.ogg"
    "Suddenly, at the entrance to the coffee shop you spot a familiar face."
    mc "{i}There's the one I'm waiting for...{/i}"
    mc "{i}Hmm, in casual clothes she looks very different.{/i}"
    mc "{i}But I kind of like it.{/i}"
    scene 6anncof02 with dissolve
    mc "{i}Noticed me.{/i}"
    mc "{i}And judging by her smile, she's in a good mood.{/i}"
    mc "{i}But in order to please this girl a good mood isn't enough. I feel like I'm gonna have to work really hard.{/i}"
    scene 6anncof03 with dissolve
    "Anna slowly walked across the half-empty room to your table and sat down opposite."
    scene 6anncof04 with dissolve
    a "Hey, [mc] hope I didn't keep you waiting too long?"
    mc "Hey. Not at all."
    mc "And I have to say, you look amazing."
    a "Ha! You flatter me as usual..."
    a "But it's still very nice. Thanks."
    a "So..."
    scene 6anncof06 with dissolve
    mc "Ahem... I hope you don't mind that I ordered a coffee while waiting for you."
    scene 6anncof05 with dissolve
    a "Of course not."
    a "To tell you the truth, I could use a little cheer up myself right now."
    mc "{i}Hmm... I know several ways to cheer you up, but coffee is not the most appealing on that list.{/i}"
    scene black with fade
    "Anna made an order and soon she had a cup of coffee as well."
    scene 6anncof07 with dissolve
    a "So, [mc], I'm really pleased with your attention to my person, as well as the fact that you invited me here... But tell me, what is all this?"
    a "You already know my negative view on workplace romances. This is a bad idea."
    a "And I don't want to make the same mistake twice."
    mc "{i}Well, there she goes again about that mistake of hers...{/i}"
    mc "{i}I think my only chance of convincing her would be some serious step. Put something worth risking in there for her.{/i}"
    mc "{i}In that case, I'll have to go all-in.{/i}"
    mc "Well, if you're really that concerned about this, then I can just quit my job."
    mc "I wouldn't want to, but my desire to date you is far greater than my desire to stay working in your establishment."
    scene 6anncof07a with dissolve
    a "You're joking now, right?"
    mc "Does it look like that?"
    a "I am... Uh... I don't understand..."
    scene 6anncof07c with dissolve
    mc "What's so confusing about that? I said what I thought."
    mc "If working together is a problem for you, we can easily fix that."
    mc "In the end, my main activity is music, and other jobs fall to the wayside."
    scene 6anncof07a with dissolve
    a "Hey, that's not what I meant when I said \"Dating\" at work!"
    a "And you certainly don't have to quit because of that."
    mc "..."
    mc "Well, what do you say? I remember you liked being with me last time."
    scene 6anncof07b with dissolve
    "..."
    a "What if you and I don't make it?"
    mc "What if it works out? We won't know if we don't try."
    mc "But if we do try, then we definitely won't have regrets in the style of \" and what could have been?\"."
    stop music fadeout 1.0
    "..."

    if anna_sex == True:
        scene 6anncof07 with dissolve
        a "Oh, I hope I won't regret it later... But I think I'm ready to try."
        play music "music/6 - Positive Mood.ogg"
        mc "{i}Damn, I'm good!{/i}"
        a "I hope you're happy about that."
        mc "You have no idea how much."
        scene 6anncof08 with dissolve
        a "Okay, okay, I believe you."
        a "Now let's talk about something else and have some coffee."
        mc "With pleasure."
        scene 6anncof09 with dissolve
        a "So you're a musician, huh?"
        mc "Yep. A rising star, you might say."
        a "And I already told you I like musicians..?"
        "You immediately struck up a casual conversation and got to know each other a little better."
    else:
        scene 6anncof07d with dissolve
        a "I'm sorry, but I don't think I want to."
        a "And if you want, you can quit, but that won't solve anything."
        mc "{i}Fuck...{/i}"
        a "I hope you understand."
        mc "Yes, certainly."
        play music "music/6 - Positive Mood.ogg"

    scene black with fade
    "Some time later."
    "BIP-BIP!!!"
    scene 6anncof10 with dissolve
    a "Sorry, it's my phone reminder."
    a "I have to get ready for work soon."
    mc "{i}And she's not the only one...{/i}"

    if anna_sex == True:
        scene 6anncof11 with dissolve
        a "You know... If we've decided to date now, why not take advantage of the remaining time in a more pleasant way?"
        mc "{i}I understood her right, didn't I? She means sex?{/i}"
        mc "You mean..."
        a "Oh, Yes. That's what I meant."
        a "Come on. I live near here. We should have enough time..."
        mc "I love your determination."
        a "Just determination?"
        mc "Huh. You want to go through the whole list?"
        a "Mmmm... Better if you come over, you can show me by example."
        mc "{i}Oh, man, I think I'm starting to fall in love...{/i}"
        stop music fadeout 3.0
        scene black with fade
        "You paid for the coffee and went home with Anna."
        "Some time later."
        jump anna_home_day06
    else:
        stop music fadeout 3.0
        scene black with fade
        "Soon you left the cafe and went to work."
        jump work_day06v

label anna_home_day06:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    scene 6ah00 with dissolve
    if lisa_path == True:
        $ cheat_point += 5

    play music "music/8 - Intro Music.ogg"
    a "Well, welcome to my humble apartment."
    mc "And from the entrance I can already say that I like it."
    a "Heh. Good to hear."
    a "Just a minute, I'll turn on the light..."
    scene 6ah01 with dissolve
    "As Anna had said, she turned on the light and then..."
    mc "Uhh... What are you doing?"
    a "..."
    "Her black top flew to the floor."
    scene 6ah02 with dissolve
    a "What do you mean? Didn't you want to have fun?"
    mc "Oho... You don't like to waste time."
    a "Yep. I advise you do the same."
    a "Now come to my bedroom, we don't have much time."
    scene 6ah03 with dissolve
    "Sexually waying her hips, the half-naked girl led you to the next room."
    mc "{i}Okay, [mc], stop hesitating, get her!{/i}"
    scene 6ah04 with dissolve
    "Throwing off your t-shirt on the move, you went into Anna's bedroom and stumbled at the sight of the next scene."
    mc "{i}She's wearing nothing but panties... How cool!{/i}"
    a "Well? Do you like what you see?"
    "Without a word, you came closer."
    scene 6ah05 with dissolve
    mc "{i}Damn, it makes her look even better.{/i}"
    mc "I'd love to see you completely naked even more."
    scene 6ah06 with dissolve
    "Anna's hand touched your body."
    a "Mmmm... So you and I have similar thoughts."
    a "And now..."
    scene 6ah07 with dissolve
    "The girl leaned back on the bed, showing you all her gorgeous Breasts, flat tummy and black panties."
    mc "...now let's get rid of the rest of the clothes."
    a "Yeah... That's what I was going to say..."
    mc "So you and I are on the same page... That's interesting."
    scene 6ah08 with dissolve
    "Imitating her unhurried manner, you knelt down and gently moved your hands up her thighs."
    mc "{i}Now we'll see what's hiding here...{/i}"
    scene 6ah09 with dissolve
    "With careful movements, you took Anna's panties..."
    mc "{i}Just like this.{/i}"
    scene 6ah10 with dissolve
    "...and then gently pulled them off her."
    mc "{i}She's perfect.{/i}"
    scene 6ah11 with dissolve
    a "Well, now you got what you wanted... I'm completely naked."
    mc "{i}That's not all I wanted.{/i}"
    a "But if you're still thinking about what to do next, I'll give you a hint."
    scene 6ah12 with dissolve
    "Anna lifted her legs, revealing an excellent view of her wet pussy."
    a "I think I could use your help here."
    mc "How about you ask me nicely?"
    a "Mmmm... Well, ple-a-ase, [mc]."
    mc "How can I refuse you after that?"
    a "Hee hee!"
    stop music fadeout 1.0
    scene 6ah13 with dissolve
    a "Aaaahhhh!"
    play music "music/15 - Deep Mood.ogg"
    a "Yeah... That's right..."
    mc "{i}Looks like I started out good.{/i}"
    a "Yes, [mc], right here... Yessss..."
    scene 6ah14 with dissolve
    "You noticed how Anna's breathing became heavier, and she barely moves her pelvis to the beat of your movement."
    a "Mmmm... I don't know where you learned that, but don't stop..."
    mc "{i}Hell, I'm pretty horny myself.{/i}"
    scene 6ah15 with dissolve
    a "Aahhhh... Ahhhh... Aaahhh...."
    a "Just like this... Yes!!!"
    mc "{i}Now I'm going to put on a little speed.{/i}"
    scene 6ah16 with dissolve
    "Suddenly you felt Anna's legs close to your neck, and she unconsciously presses you to her."
    a "Damn, that's amazing!.."
    mc "{i}Perhaps it's time to join the game itself.{/i}"
    scene 6ah17 with dissolve
    stop sound fadeout 1.0
    a "Oh... What?"
    a "Why did you stop? I'm almost..."
    mc "Don't worry, we've still got time. Get in front."
    scene 6ah18 with dissolve
    "She climbed completely on the bed and put her ass on display."
    a "Mmm... Something like that?"
    mc "Yeah, like that."
    a "Good... Now stop playing and fuck me. Fuck me with all your strength!"
    mc "{i}Looks like she's ready...{/i}"
    "You took off your pants and got onto the bed next to her."
    scene 6ah19 with dissolve
    mc "{i}Oh... She's so beautiful...{/i}"
    mc "{i}And now the fun begins.{/i}"
    "You put your arms around her and moved her to you."
    scene 6ah20 with dissolve
    a "Ahhh..."
    mc "I see your pussy's ready."
    a "Ready... Fuck me, stop wasting time!"
    mc "{i}I like the fact that now she asks me to fuck her, although two hours ago she just wanted to stay colleagues.{/i}"
    mc "Good..."
    scene 6ah21 with dissolve
    mc "Now let's put that dick in your horny pussy."
    a "Yes! Stick your dick in!"
    mc "Take that!"
    scene 6ah22 with dissolve
    a "Aaaahhhh.... Yeeesss..."
    a "That feels so good."
    mc "{i}Ohhh... I agree with her, it's really nice.{/i}"
    mc "{i}Plus she's so hot.{/i}"
    scene 6ah23 with dissolve
    "Picking up the pace, you began to fuck your boss."
    mc "{i}Fuck... I can really get used to this.{/i}"
    a "Aaahhhh... Aahhhh... Ahhhh...."
    scene 6ah24 with dissolve
    a "[mc], this... Just... Amazing!!!"
    mc "Yeah, baby... You'll remember that for a long time..."
    a "Mmmm... Shut up and keep fucking me.... Yessss..."
    scene 6ah25 with dissolve
    a "Take me harder! I know you want to!"
    a "Yeah... Just like this..."
    mc "{i}These moans make me want to fuck her harder and harder.{/i}"
    show anim18
    "Succumbing to the attraction you accelerate."
    mc "Take that! Take that!!!"
    a "Haa... Haa... your cock is... Cool!"
    a "I... you're deep."
    mc "{i}Damn, she smells good...{/i}"
    mc "{i}I want to taste her lips!{/i}"
    scene 6ah26 with dissolve
    "Feeling the heat of her body underneath, you began eagerly to kiss her."
    a "Mmmm.... Mmmm...."
    a "Don't stop!"
    show anim21
    "At the same time you caressed the girl's tongue, and drove your cock into her pussy."
    mc "{i}Oh, I could do this forever.{/i}"
    scene 6ah28 with dissolve
    mc "Baby, let's change positions."
    a "Ohhh.. Whatever you say... I'm ready..."
    scene 6ah29 with dissolve
    "The next moment you were behind Anna."
    a "Aaahhh!!!"
    mc "{i}Her Breasts are so firm...{/i}"
    a "Yesss..."
    scene 6ah30 with dissolve
    "Suddenly Anna wrapped her free hand around you and looked straight into your eyes."
    a "Ohhhh... If you continue to be so good in bed, I'll be obligated to give you a promotion."
    mc "Then be sure we get to Catherine's position at this rate."
    a "Mmmm... I like your ambition."
    scene 6ah31 with dissolve
    mc "{i}Oh, I'm not sure I'll last much longer...{/i}"
    a "Aaaahhhh... Aahhhh!!!"
    mc "{i}And it looks like it's not just me.{/i}"
    mc "Last pose..."
    show anim19
    "You grabbed the girl's leg and began to fuck her with one last effort."
    a "A little more! A little more and..."
    mc "{i}Uhhh... Hold on, [mc]!{/i}"
    mc "{i}You gotta make that bitch cum!{/i}"
    stop sound fadeout 3.0
    a "Aaaahhhh!!! YEAH!!!"
    scene 6ah32 with flash
    a "Yeeesss..."
    scene 6ah32 with flash
    stop sound fadeout 1.0
    "..."
    mc "Fuck I was almost cumming myself."
    scene 6ah33 with dissolve
    a "Come here, baby..."
    a "Cum, cum on me!"
    mc "Since you're asking for it..."
    scene 6ah34 with dissolve
    "In one motion, you put your cock in your boss's mouth and almost immediately finished."
    mc "{i}How nice!{/i}"
    a "Mmmmmmph gagggguu aaaauu..."
    mc "{i}Why don't I give her a little help?{/i}"
    scene 6ah35 with dissolve
    "With one hand, you grabbed Anna's head and accelerated the pace."
    mc "Suck it, baby... You're doing great..."
    a "Mmmmmmph... Mmmph... Mmmppppphhhh..."
    mc "I'm almost done."
    scene 6ah36 with dissolve
    "You let go of Anna's head and started jerking off right on her Horny face."
    show anim20
    mc "Ohhh... I hope you're prepared, because I'm about to explode..."
    a "Cum on my face, honey... I'm ready.."
    mc "{i}Ohhh.... I hope you're really ready.{/i}"
    a "Mmmm... Come on! Come on!"
    stop sound fadeout 3.0
    mc "Aahhhh! Take it!"
    stop music fadeout 1.0
    scene 6ah37 with flash
    mc "...."
    scene 6ah38 with flash
    "..."
    play music "music/8 - Intro Music.ogg"
    mc "Awesome..."
    a "Oh... Looks like you really went overboard."
    mc "Heh. I warned you."
    a "I'm not complaining..."
    mc "{i}Yeah, right.{/i}"

    $ renpy.end_replay()
    if not persistent.day06anna:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day06anna = True

    scene black with fade
    "Some time later."
    "You and Anna got some rest and cleaned up."
    scene 6ah39 with dissolve
    a "You know, maybe starting to date you wasn't such a bad idea."
    mc "I'm glad you understand that now."
    a "Yep. Better late than never."
    a "And yet, [mc], at work, let's keep it a secret for now."
    scene 6ah40 with dissolve
    mc "You don't want Catherine to know?"
    a "Not yet."
    mc "Well, let it be so..."
    a "Thank you! I knew I could count on you!"
    mc "Yeah."
    mc "By the way, not that I don't like looking at your pretty ass, but we should get going..."
    a "You're right."
    stop music fadeout 3.0
    scene black with fade
    "Some time later, the two of you went to work."
    jump work_day06v


label work_day06v:

    play music "music/1 - Atmosphere.ogg"
    scene 6wwork01 with dissolve
    a "...I have no idea what it's like."
    mc "Well, I don't have much experience playing guitar in public yet, but I'm trying to fill that gap."
    a "In that case, next time you just have to play me something!"
    mc "Heh. Okay why not..."
    scene 6wwork02 with dissolve
    "While in the middle of a casual conversation with Anna, you noticed a familiar figure approaching out of your peripheral."
    "..."
    scene 6wwork03 with dissolve
    k "Anna, [mc] good evening."
    mc "{i}Of course! Anna warned me that Catherine would be here today.{/i}"
    mc "{i}I was starting to forget how gorgeous she is.{/i}"
    scene 6wwork04 with dissolve
    mc "Good evening."
    a "Good to see you, Catherine."
    a "I hope all the business is taken care of?"
    k "Yeah, it's all right for now."
    k "If you're free, I'd like to talk to you in my office."
    scene 6wwork05 with dissolve
    a "Of course, we were just finishing up here."
    k "Okay, then let's go, we have a lot to do today."
    a "Of course, I'm right behind you."
    scene 6wwork06 with dissolve
    a "Uhhh... I'm sorry, [mc], but I'm not sure I'll see you again today."
    mc "Too much work?"
    a "Yeah, apparently."
    a "What about you? Heading home after work?"
    mc "Oh, yeah, I finally get a good night's sleep."
    a "Well, good luck with that."
    mc "You too."
    scene black with fade
    stop music fadeout 3.0
    "You and Anna went about your business."
    "A work shift and a new day was awaiting you."
    jump sister_day06

label sister_day06:
    scene 3nextday with fade
    $renpy.pause(3, hard=True)
    scene black with fade
    play music "music/9 - You Can Make the Sound.ogg"
    "Your sister was supposed to be back in town today, so right after rehearsal, you decided to pay her a visit."
    scene 6julia06 with dissolve
    "Upon checking your sister's office, you found it empty."
    mc "{i}I need to ask one of her employees where she is.{/i}"
    mc "{i}Although... I could combine business with pleasure. I'll go to Jane's office and check with her.{/i}"
    mc "{i}But damn, it's been a long time since I've seen Julia.{/i}"
    mc "{i}I wonder if she's all right...{/i}"

    if nicole_plus == True:
        scene 6julia06a with dissolve
        "Almost halfway to your destination, you noticed a familiar face."
        n "[mc]."
        mc "Nicole..."
        mc "{i}Well, since she's here anyway, I can ask her about everything.{/i}"
        mc "I was looking for my sister, Julia. Do you know where she might be?"
        n "She's in a meeting... Maybe I can help you."
        mc "{i}Fuck, I keep running into these meetings. I'm so \"lucky\".{/i}"
        mc "No, I just wanted to talk to her. Privately."
        scene 6julia06b with dissolve
        n "Well, while she's busy, you can wait in my office."
        mc "{i}Hmm... Why not?{/i}"
        mc "Thanks for the offer."
        n "Don't mention it."
        scene black with dissolve
        "You went inside and sat across from Nicole."
        scene 6julia07a with dissolve
        mc "This office seems smaller than the one you had in my father's company?"
        n "It's just a temporary measure."
        n "As soon as I show my usefulness to this company, I think I'll procure something more suitable."
        mc "{i}Ha! She's pretty confident.{/i}"
        mc "Then I wish you good luck."
        n "Thanks, but I won't need it. I already have everything I need."
        mc "{i}Like I said, she's pretty confident.{/i}"
        mc "Okay..."
        scene 6julia07 with dissolve
        mc "The truth is, I'm glad to see you here."
        n "Well, it happened because of you."
        if nicole_favor == True:
            n "And, of course, I still remember that I owe you a favor."
            mc "Yep. I'll let you know as soon as I need it."
        mc "But as you said yourself, you're only here because of your skills and experience. Besides, I'm sure Jane gave you a hard test at the interview."
        n "Compared to what your father had, it was pretty simple."
        mc "{i}Hmm... What did the old man have for her that would make the Workaholic's interview seem simple?{/i}"
        mc "That's possible."
        "..."
        scene 6julia08 with dissolve
        mc "So, now you work here... What do you think about all this?"
        n "I haven't had time to form an opinion yet. Too soon."
        mc "{i}I think you look a lot happier now. Or, maybe it's just me.{/i}"
        mc "Still."
        n "..."
        scene 6julia08a with dissolve
        n "So far, I'm satisfied."
        mc "Well, that sounds good to me!"
        n "Yes... Yeah, that's probably good."
        stop music fadeout 3.0
    else:
        scene black with dissolve
        "When you caught one of the employees, you realized Julia was in a meeting."
        scene 6julia11a with dissolve
        mc "{i}Well, in that case, I'll have to wait for her.{/i}"
        mc "{i}I hope it won't be long...{/i}"


    scene black with fade
    "Same time in another part of the building."
    scene 6julia01 with dissolve
    play music "music/6 - Positive Mood.ogg"
    sis "...so, thanks to this deal, our profits should increase by twenty-five percent."
    sis "So you can have a good time tonight. You all deserve it."
    sis "But be prepared for the big changes that await us next week. I warn you, this applies to all departments of the company."
    sis "After all, the greater the profit, the greater the responsibility."
    scene 6julia02 with dissolve
    sis "That's all I wanted to tell you."
    sis "And if none of you have any questions, I'm not detaining any of you. I will see you tomorrow."
    scene black with fade
    "Minute later."
    scene 6julia03 with dissolve
    jn "Great performance, girl."
    jn "I think after that meeting, you've found a good way to shake up that sleeping hornet's nest."
    sis "Let's hope they understand."
    sis "Because of this deal, we're already understaffed. I wouldn't want to have to fire anyone."

    if nicole_plus == True:
        scene 6julia04 with dissolve
        jn "Speaking of new employees..."
        jn "I hope you're not angry that I hired your father's former assistant."
        scene 6julia05 with dissolve
        sis "Angry? No. Of course not."
        sis "If you think you can use this girl, I don't mind."
        sis "My father always chose the best assistants for himself."
    else:
        scene 6julia04 with dissolve
        jn "Speaking of new employees..."
        jn "I could really use a good assistant right now."
        scene 6julia05 with dissolve
        sis "Not just you, Jane. I could use a competent assistant myself."
        sis "You know... I think I'll go to human resources tomorrow and ask."

    scene 6julia04 with dissolve
    jn "Great!"
    jn "Once we figure out all the new working hours, can discuss how we'll celebrate the new deal?"
    sis "Good idea..."
    stop music fadeout 3.0

    if nicole_plus == True:
        scene black with fade
        "Few minutes later."
        "Nicole's Office."
        scene 6julia08a with dissolve
        play music "music/9 - You Can Make the Sound.ogg"
        n "We had a good talk, [mc], but I think you should go."
        mc "What?"
        scene 6julia09 with dissolve
        n "Look back."
        n "Looks like the meeting's over."
        scene 6julia10 with dissolve
        "You turned around and saw your sister with Jane."
        mc "{i}Oh, there's Julia! Great!{/i}"
        mc "{i}And it looks like she noticed me too.{/i}"
        scene 6julia08 with dissolve
        mc "Thanks for letting me wait here. I'll be going. Bye."
        n "Sure, see you later."
        scene 6julia11 with dissolve
        "You walked out of the office and into the hallway."
    else:
        scene black with fade
        "Few minutes later."
        play music "music/9 - You Can Make the Sound.ogg"
        scene 6julia11a with dissolve
        mc "{i}Oh, there's Julia! Great!{/i}"

    mc "Julia!"
    sis "[mc]?! What are you doing here?"
    mc "I heard you were back in town today, so I thought I'd surprise you. It's been so long..."
    scene 6julia12 with dissolve
    "..."
    sis "You're right, it's a really good to see you."
    mc "{i}Oh, it's only now that I realized just how much I missed her.{/i}"
    "..."
    scene 6julia13 with dissolve
    sis "You know, Jane and I were just on our way to my office. Come with us, we'll talk there."
    mc "Of course, I don't mind at all."
    sis "And by the way, you remember my friend Jane, don't you?"
    scene 6julia13a with dissolve
    jn "I think he remembers me... While you were away, we ran into each other a couple of times.."
    mc "Yeah, right."
    scene 6julia13 with dissolve
    sis "Well, that's great! Then let's go."
    scene black with dissolve
    "You followed the girls into Julia's office."
    scene 6julia14 with dissolve
    "Before you knew it, you realized that you were under the scrutiny of both girls."
    mc "{i}Uh... Somehow this became uncomfortable.{/i}"
    mc "Something wrong?"
    sis "On the contrary, everything is just fine."
    jn "You may not have heard, but our company is celebrating."
    mc "Oh... In that case, congratulations?"
    sis "Yes, thanks."
    scene 6julia15 with dissolve
    "Still feeling some tension in the air, you sat down on the couch."
    mc "I hope I'm not distracting you with my visit."
    "..."
    scene 6julia16a with dissolve
    "At the same time, both girls sat on either side of you."
    scene 6julia18 with dissolve
    sis "Opposite. I think you're on time."
    sis "Jane and I were just deciding where we were going to celebrate after work today. Why don't you join us?"
    scene 6julia17 with dissolve
    jn "I agree with this proposal."
    jn "I think it would make things more interesting..."
    mc "{i}Yeah, interesting.{/i}"
    scene 6julia16 with dissolve
    sis "Well, what do you say?"
    sis "Jane and I have already chosen a restaurant, so you could have some good company and first-class food."
    sis "Is there anything else you need for a good evening?"
    mc "{i}It's not like I have a choice. But I really like the sound of this.{/i}"
    mc "In that case, ladies, I'd be happy to join you."
    scene 6julia18 with dissolve
    sis "That's great! Then let's not waste time."
    sis "Come to my house, I need to change, and we can catch up on everything on the road."
    mc "Sure, let's go."
    scene 6julia19 with dissolve
    sis "I'll meet you there, Jane."
    jn "Yes, indeed. Just don't be late."
    mc "So..."
    stop music fadeout 3.0
    scene 6julia20 with dissolve
    play music "music/10 - Street's.ogg"
    mc "Hmmm... I see you bought yourself a new car."
    sis "Yeah, I thought I'd treat myself."
    mc "That's a good way to do it."
    sis "I knew you'd appreciate it."
    scene 6julia21 with dissolve
    sis "What about you?"
    sis "You don't regret giving up the family business?"
    mc "You know, in all the time I've been living on my own, I haven't regretted my decision for a second."
    scene 6julia23 with dissolve
    sis "If everything is as wonderful as you say it is, I'm happy for you."
    mc "Thanks, sis... It really means a lot to me."
    sis "Yeah, when you're famous, write me a song. I'll brag to my friends later."
    mc "Ha! I'll dedicate a whole album to you."
    sis "Mmmm... Sounds good. I could agree to that."
    scene 6julia22 with dissolve
    sis "Okay, enough talking, you better buckle up."
    mc "Whatever you say, boss."
    sis "Let's go."
    stop music fadeout 3.0

    scene black with fade
    "Some time later."
    scene 6julia24 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Wow, it's been a long time since I've been here."
    sis "Yeah, how long has it been since your last visit? A few months?"
    mc "Something like that."
    sis "Well, not much has changed in that time."
    mc "That's not surprising, considering how much time you spend at work."
    mc "You should get more rest."
    sis "Actually, that's what we're gonna do tonight."
    mc "You're right."
    scene 6julia25 with dissolve
    "After a quick look around, you settled back on the couch."
    sis "Wait for me, I'll go change."
    mc "Of course, no problem. Just try not to take too long."
    sis "Can't promise anything!"
    scene 6julia26 with dissolve
    "Julia went into the bedroom, leaving you alone."
    "..."
    sis "[mc]."
    mc "{i}Oh, she likes to talk. Even when she's busy.{/i}"

    if father_enemy == True:
        sis "I heard you and dad had a big fight."
        scene 6julia27 with dissolve
        mc "Trust me, he started this."
        sis "I don't doubt that. But it seems things have gone much further than your usual disagreements."
        sis "You made a real enemy out of him this time."
        mc "Like I said, he deserved it."
        sis "I understand..."
        scene 6julia26 with dissolve
        "..."
        sis "By the way..."
        mc "{i}Oh, there it is.{/i}"

    sis "I wanted to see how you were doing with your personal life. Are you seeing anyone right now?"
    mc "{i}What a difficult question...{/i}"
    mc "{i}What should I tell her?{/i}"

    menu:
        "Say you're dating (+Good point)":
            $ goodpoint += 1
            $ sis_question01 = True
            mc "{i}Perhaps I can tell her about it. Sometimes she gives good advice.{/i}"
            scene 6julia27 with dissolve
            mc "It's a little more complicated than it sounds, but you could say, yes. I'm dating someone."
            "..."
            scene 6julia28 with dissolve
            sis "Well, well! I need to hear more about this!"
            sis "Tell me."
            mc "{i}What the?!{/i}"
            scene 6julia29 with dissolve:
                ypos -1.90
                ease 8 ypos 0.0
            mc "{i}Damn, Julia's in great shape...{/i}"
            mc "{i}Okay, don't stare, it's your sister after all!{/i}"
            scene 6julia30 with dissolve
            sis "Why the silence? Say something already."
            mc "You know you're standing in front of me in your underwear right now, right?"
            sis "So what? I'm not naked."
            "..."
            sis "Or are you embarrassed?"
            mc "Don't bother me, go get dressed!"
            sis "Heh. Okay."
            scene 6julia31 with dissolve
            sis "But don't think you'll get rid of me so easily."
            sis "Anyway, you're going to tell me everything."
            mc "Yeah, we'll see."

        "Say you're single (+Bad point)":
            $ badpoint += 1
            mc "{i}Perhaps there's no need to tell her about it.{/i}"
            scene 6julia27 with dissolve
            mc "I'm alone right now, and please, let's not talk about it anymore."
            sis "Pfft... You're boring!"
            mc "Yeah, whatever you say."
            mc "You better do whatever it is you're doing. People are waiting for you here, by the way."

    scene 6julia32 with fade
    "..."
    mc "{i}Silence.{/i}"
    mc "{i}That's much better.{/i}"
    scene black with fade
    "Some time later."

    scene 6julia34 with dissolve
    sis "[mc]."
    sis "[mc] you're not asleep are you?"
    mc "Sorry, I just closed my eyes for a bit."
    sis "Yeah, let's pretend I believed you..."
    mc "{i}She can be a real pain at times.{/i}"
    scene 6julia33 with dissolve
    sis "What do you think? How do I look?"
    mc "Fishing for compliments?"
    sis "That's possible."
    mc "Well, you look amazing. As always."
    sis "Mmmm... Thanks, bro!"
    scene 6julia35 with dissolve
    sis "Now get your ass off the couch. We promised Jane we wouldn't be late."
    mc "Hey, but you were the one who took so long to pick out a dress!"
    sis "Excuses are for losers, [mc]. I thought you learned that lesson well."
    mc "Oh, please don't start with those fatherly lessons..."
    sis "Then get up."
    scene 6julia36 with dissolve
    mc "Okay, okay, I hear you."
    sis "This is great."
    scene 6julia37 with dissolve
    "Talking about stuff, you and Julia went out."
    if sis_question01 == True:
        sis "So you're dating someone..."
        sis "Come on, tell me, who is this poor girl that can stand you?"
        mc "Heh. Not this time, sis..."
    else:
        sis "So you're not dating anyone right now..."
        sis "Strange, I thought that as soon as you caught the smell of freedom, you'd find yourself with a dozen passions."
        mc "Who said I didn't find them?"
        sis "Ha! You're a womanizer!"

    stop music fadeout 3.0
    scene black with fade
    "Some time later."

    scene 6julev01 with dissolve
    play music "music/13 - Hope is Still Living.ogg"
    mc "Hmm... I've never been to this restaurant before."
    sis "It only opened recently, but has become very popular."
    mc "Yep. I noticed that there's a very attractive atmosphere here."
    scene 6julev02 with dissolve
    mc "But I'm afraid with my current financial situation, I won't be able to afford it."
    mc "Like most of the places I used to visit."
    scene 6julev03 with dissolve
    sis "In that case, you're lucky to have your favorite sister with you today."
    sis "But in the future, I still advise you to not to get used to it."
    scene 6julev02 with dissolve
    mc "Deal."
    sis "By the way, look who's downstairs."
    scene 6julev04 with dissolve
    "You looked down from the balcony, and your eyes met Jane walking down the street."
    mc "{i}Oho... She looks great.{/i}"
    mc "{i}But despite that gorgeous dress, I wouldn't mind seeing her naked...{/i}"
    scene 6julev03a with dissolve
    sis "Hey, stop staring at her so greedily! She's my friend after all."
    mc "Heh. Excuse me. Now I'll just stare at you."
    sis "That's different!"
    scene 6julev05 with dissolve
    "Waitress" "Sorry for the delay, your table is ready."
    "Waitress" "Please follow me."
    mc "{i}About time...{/i}"
    scene 6julev06 with dissolve
    "You followed the waitress until you stopped at a small table in the corner."
    "..."
    scene 6julev07 with dissolve
    "Waitress" "Please sit down."
    "Waitress" "As soon as you decide on the order, I'll come to you."
    "Waitress" "I wish you a good time."
    scene 6julev08 with dissolve
    mc "Quite a nice girl..."
    scene 6julev09 with dissolve
    sis "Yep. I saw you staring at her ass."
    mc "Hey! I was just looking ahead."
    sis "Of course."
    scene 6julev08 with dissolve
    mc "Actually, I work in the service industry myself. She's almost like my co-worker."
    scene 6julev09 with dissolve
    sis "Really."
    sis "Heh. I forgot you're a bartender now..."
    sis "I should come by and have a drink sometime."
    mc "I'd love to get you a drink on the house."
    stop music fadeout 3.0
    scene 6julev10 with dissolve:
        ypos -1.90
        ease 8 ypos 0.0
    jn "Mmm... Looks like someone's having a good time."
    mc "{i}Here comes Jane.{/i}"
    mc "{i}And, damn it, again, she looks gorgeous!{/i}"
    scene 6julev11 with dissolve
    play music "music/8 - Intro Music.ogg"
    mc "Jane, you came just in time. We just sat down."
    sis "Come on, join us, girl. There's plenty of room."
    jn "Thanks."
    scene 6julev12 with dissolve
    "Jane sat down beside Julia and immediately joined the conversation."
    jn "You won't believe what just happened."
    jn "I've been approached twice on the way here."
    sis "That's not entirely surprising, considering how great you look today."
    mc "Julia's right, the only strange thing is that it was only two guys."
    jn "Who said there were only two of them?"
    sis "Whoo... Looks like someone is very popular with the guys today!"
    mc "{i}Hmm... I don't really like this topic. Perhaps we can change it.{/i}"
    mc "Hey, can we order already?"
    scene 6julev13 with dissolve
    jn "Agreed. Let's make an order, and then we'll talk about everything."
    jn "So... Since we're celebrating tonight, I hope everyone drinks."
    scene black with fade
    "Some time later."
    scene 6julev14 with dissolve
    jn "...just think about how much time and effort it took us to successfully close this deal."
    jn "And these brainless investors take it all for granted... Aarrrr! I hate them!"
    mc "{i}Oh, I'd almost forgotten how much I loved her stories about work...{/i}"
    scene 6julev15 with dissolve
    sis "It was... Educational."
    mc "{i}Heh, sis is always very delicate in her choice of words.{/i}"
    sis "Now, let's drink to the completed deal. You and I did our best."
    scene 6julev16 with dissolve
    jn "Yeah, I'm sorry about that boring story... I guess I just needed to vent."
    jn "I support your toast, Julia. To the completed deal!"
    scene 6julev17 with dissolve
    "Peering into the glass raised by Jane, your eyes accidentally slipped to her breasts."
    mc "{i}What a lovely view.{/i}"
    mc "{i}I wouldn't mind seeing what's under those clothes...{/i}"
    scene 6julev18 with dissolve
    "Suddenly you felt Jane kick you under the table."
    mc "{i}Fuck!{/i}"
    scene 6julev19 with dissolve
    jn "[mc] you seem lost in your thoughts."
    jn "We're actually having a celebratory toast here."
    jn "Will you join us?"
    mc "{i}Hell, from that look, I can tell she saw where I was staring...{/i}"
    mc "{i}Fuck.{/i}"
    scene 6julev20 with dissolve
    mc "Ahem... I beg your pardon."
    mc "And of course, let's drink to the completion of your deal!"
    mc "Given all the time and work you put into your work, you ladies fully deserve it."
    sis "Hurray!!"
    scene 6julev19 with dissolve
    jn "Well said. Thanks."
    scene 6julev14 with dissolve
    stop music fadeout 3.0
    "For a while you shared stories, drank and just had fun."
    scene black with fade
    "Two hours later."
    scene 6julev21 with dissolve
    play music "music/10 - Street's.ogg"
    sis "Ooh... Great time guys! We'll have to do it again sometime."
    jn "Mmm... Agreed. It turned out really well."
    jn "Did you like it, [mc]?"
    mc "Name a time and a place, and I'll be there."
    jn "Ha! I like your attitude."
    scene 6julev22 with dissolve
    sis "Man, looks like the cab hasn't arrived yet."
    sis "Sucks."
    sis "Wait a minute, I'll catch us something."
    scene 6julev23 with dissolve
    "While Julia was catching a cab, you and Jane faced each other."
    mc "It's a good evening..."
    mc "I don't want it to end so early."
    jn "Yeah, me neither."
    "..."

    if jane_path == True and RPjn >= 8 and jane_massage == True:
        scene 6julev24a with dissolve
        jn "You know, back at the restaurant, I saw you looking at me at the table."
        mc "{i}I thought so.{/i}"
        mc "About that... Sorry, I didn't mean to. You just looked so good that I-"
        scene 6julev24 with dissolve
        jn "No need to apologize. I kind of liked it."
        mc "{i}Mmm... I expected something like that from her.{/i}"
        "The next words came out of you without a second thought."
        mc "Then how about we continue this evening? Just you and me."
        "..."
        jn "Hmm... Tempting offer."
        jn "What do we say to Julia?"
        mc "Well, she doesn't need to know."
        scene 6julev25 with dissolve
        sis "Hey, do any of you guys need a ride?"
        mc "Thanks for the offer, but I'll get home on my own."
        sis "What about you, Jane?"
        mc "{i}Yeah, what about you, Jane?{/i}"
        scene 6julev26 with dissolve
        jn "I think I'll get home myself. There's no need to force the taxi driver to make such a big detour around the city."
        sis "As you wish."
        scene 6julev27 with dissolve
        sis "[mc]."
        mc "Yes?"
        sis "Look after her, please. Ok?"
        mc "You don't have to worry about her, she's in good hands."
        sis "All right, good night, then."
        scene 6julev26 with dissolve
        mc "Good night."
        jn "See you tomorrow, Julia."
        scene 6julev29 with dissolve
        "You and Jane watched as Julia drove off."
        mc "{i}That's it...{/i}"
        scene 6julev28 with dissolve
        jn "Looks like it's just you and me."
        mc "Yep."
        mc "And where are we going? You or me?"
        jn "We're going to my place."
        mc "Well, the lady's wish is my command."
        stop music fadeout 3.0
        jump jane_home06
    else:
        scene 6julev24a with dissolve
        jn "However, any fun comes to an end sooner or later."
        jn "Julia and I have a lot to do at work tomorrow, and I need to be fresh."
        mc "I understand."
        scene 6julev25 with dissolve
        sis "Hey, do any of you guys need a ride?"
        mc "Thanks for the offer, but I'll get home on my own."
        sis "What about you, Jane?"
        scene 6julev26 with dissolve
        jn "Why not. Thanks."
        sis "Great!"
        scene 6julev27a with dissolve
        sis "Good night, [mc]."
        jn "Yeah, night."
        scene 6julev26a with dissolve
        mc "See ya."
        scene 6julev29 with dissolve
        "You silently watch as the girls leave."
        mc "{i}That's it...{/i}"
        scene 6julev28a with dissolve
        mc "{i}Oh, I should probably get home...{/i}"
        mc "{i}Yes, definitely.{/i}"
        stop music fadeout 3.0
        jump end_d06

label jane_home06:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    if lisa_path == True:
        $ cheat_point += 5
    scene black with fade
    "Some time later you arrived at Jane's place."
    scene 6jh01 with dissolve
    play music "music/1 - Atmosphere.ogg"
    mc "Hmmm... Is it just me, or am I coming to this apartment more and more often?"
    jn "That may be. But I don't advise that you get used to it."
    jn "We're just having a good time. There's nothing more between us."
    mc "{i}We'll see.{/i}"
    scene 6jh02 with dissolve
    jn "And like I said, Julia can't know that."
    jn "I hope we understand each other."
    mc "Believe me, I don't want her to know any more than you do."
    jn "Good."
    scene 6jh03 with dissolve
    jn "I'll go upstairs for a moment, and you can go out on the balcony. Wait for me by the pool."
    mc "{i}I didn't know she had a pool. Pleasant surprise.{/i}"
    mc "You know, I didn't even notice it last time."
    jn "That's not surprising. Last time we were busy with other things."
    mc "That's true."
    scene 6jh04 with dissolve
    "While Jane went to her bedroom, you went out on the balcony."
    "..."
    scene 6jh05 with dissolve
    mc "{i}This is pretty nice.{/i}"
    mc "{i}Yes, the pool's not as big as the one in my parent's home, but I like it.{/i}"
    mc "{i}And with my salary as a bartender, I'd have to save for twenty years to get an apartment like this.{/i}"
    "..."
    mc "{i}Oh, this waiting is killing me. I hope Jane doesn't take long.{/i}"
    scene black with fade
    stop music fadeout 3.0
    "Few minutes later."
    scene 6jh06 with dissolve:
        ypos -1.90
        ease 8 ypos 0.0
    play music "music/Maxim Nick - Falling Down.mp3"
    jn "Ahem..."
    jn "I hope you didn't miss me too much while I was gone."
    mc "{i}Wow...{/i}"
    mc "Well, I wouldn't admit to it."
    scene 6jh07 with dissolve
    "Slowly Jane headed in your direction."
    mc "I see you've decided to change."
    jn "I felt a little stuffy, I hope you don't mind."
    mc "I'm all for it."
    scene 6jh08 with dissolve
    "Jane gently touched your chest."
    jn "That's good."
    jn "But maybe you should get rid of the extra clothes too."
    mc "Those are the best words you can hear from a pretty girl."
    scene 6jh09 with dissolve
    jn "Don't get ahead of yourself, cowboy. Strip down to your underwear."
    jn "I hope you're wearing some?"
    mc "Of course."
    scene 6jh10 with dissolve
    jn "Then I see no reason to delay."
    mc "{i}I see no reason to beat around the bush.{/i}"
    mc "{i}But if that's what you want, I'm ready to play along.{/i}"
    scene 6jh11 with dissolve
    "As Jane hinted, you began to undress."
    scene 6jh12 with dissolve
    "Your shoes quickly flew to the side..."
    scene 6jh13 with dissolve
    "...and then everything else."
    "Until you were only in your underwear."
    scene black with fade
    "Minute later."
    scene 6jh14 with dissolve
    jn "Do you like it here?"
    mc "It's so quiet, it's even soothing."
    mc "I like this."
    jn "When I have a free minute, I usually rest here."
    jn "I haven't told you, but I used to love swimming... I still do."
    mc "{i}So that's why she has such a distinct athletic build.{/i}"
    scene 6jh15 with dissolve
    jn "What about you? Where and how do you relax in your free time?"
    mc "Me? Differently."
    mc "Sometimes I put on headphones and listen to music, and sometimes I play the guitar myself."
    jn "Really."
    scene 6jh15a with dissolve
    "..."
    jn "I hope you don't mind if I take a dip in the water."
    scene 6jh16 with dissolve
    play sound "music/water_splash.wav"
    "Without waiting for your answer, Jane sank into the pool."
    jn "Ohhh... This is awesome!"
    jn "[mc], you can join if you want."
    mc "Heh. Thanks for the offer, but I'd rather just sit here."
    scene 6jh17 with dissolve
    jn "Mmmm... Suit yourself."
    mc "{i}And it offers a very interesting view.{/i}"
    "For a while you watched in silence as the girl swam back and forth with pleasure."
    scene 6jh18 with dissolve
    "It didn't last long, and soon Jane swam to the side and leaned on it."
    jn "Ugh... I love this feeling! I could swim here all day..."
    jn "But perhaps I've had enough for today. It's necessary to know moderation."
    mc "Then welcome to solid ground."
    jn "Thanks."
    scene 6jh19 with dissolve:
        ypos -0.34
        ease 4 ypos 0.0
    "As if in slow motion, you watched Jane climb out of the pool."
    mc "{i}I'm a hundred percent sure she's doing this on purpose.{/i}"
    mc "{i}But damn, she's so hot!{/i}"
    mc "{i}And she knows that.{/i}"
    scene 6jh20 with dissolve
    mc "{i}Not to mention those gorgeous breasts that are now dripping with water.{/i}"
    mc "{i}I feel a little more, and I might just fall in love...{/i}"
    scene 6jh21 with dissolve
    "A few seconds later, Jane was standing right in front of you, smiling slyly at something."
    mc "{i}Oh, yeah, she definitely saw where I was looking.{/i}"
    mc "{i}And more than that, she likes it.{/i}"
    jn "You refused in vain. The water was just amazing."
    mc "Not just water..."
    jn "Mmm..? What do you mean?"
    scene 6jh22 with dissolve
    mc "{i}Oh, like you don't know that.{/i}"
    "Looking at the girl from the bottom up, it was hard not to appreciate her trim figure."
    mc "{i}Stop.{/i}"
    mc "{i}Is it me or is this swimsuit's fabric translucent?{/i}"
    scene 6jh23 with dissolve
    jn "Translucent?"
    mc "{i}Uhh... Did I just say that out loud?{/i}"
    mc "{i}Well, it's too late to deny it.{/i}"
    mc "Maybe just a little."
    scene 6jh24 with dissolve
    jn "Hmm... If so, does it make sense to wear it at all now?"
    jn "Don't you think?"
    mc "{i}Oh, Yes, I think so.{/i}"
    mc "Yes, maybe it would be better without it."
    scene 6jh25 with dissolve
    "Jane's left hand slowly reached for her back."
    jn "If you insist."
    mc "{i}Very insist!{/i}"
    scene 6jh26 with dissolve
    "..."
    "The top of Jane's swimsuit flew to the floor."
    mc "{i}Yes... That's what I wanted.{/i}"
    scene 6jh27 with dissolve
    mc "{i}Her body, her breasts, it's all just perfect.{/i}"
    "For a while, you just looked at each other until Jane broke the silence."
    jn "I saw the way you looked at me. And not for the first time, by the way."
    scene 6jh28 with dissolve
    "The girl pressed both hands against her tits, they seem to get larger."
    jn "Do you like them that much?"
    mc "How can I be blamed for that? Who in their right mind wouldn't like them?"
    scene 6jh29 with dissolve
    jn "What about my other parts?"
    jn "Would you like to see them too?"
    mc "Stupid question. Sure, yeah."
    scene 6jh30 with dissolve
    "With a slight movement, Jane untied the tie on her bottoms, causing them to fall to the floor."
    scene 6jh31 with dissolve
    "..."
    mc "Mmm... Superb. Then I'll take it off too."
    scene 6jh32 with dissolve
    "You and Jane got close and touched each other with gentle movements."
    jn "Your heart is beating so fast."
    mc "That's not surprising at all..."
    mc "Come closer."
    stop music fadeout 3.0
    scene 6jh33 with dissolve
    "The next moment, you kissed the girl in front of you."
    play music "music/Maxim Nick - Smooth Light.ogg"
    jn "Mmmmm... Mmmm...."
    mc "{i}Oh, she's a great kisser... It feels so good.{/i}"
    show anim15
    "You felt Jane's free hand touch your cock..."
    "...and then she started jerking it off."
    mc "{i}Oh yeah... What a great feeling...{/i}"
    jn "Mmmmm..."
    mc "{i}Ohhhh... She's got the magic hands.{/i}"
    stop sound fadeout 1.0
    "Then Jane stopped and pushed you gently toward the chairs."
    scene 6jh35 with dissolve
    mc "What are you-"
    "You don't have time to recover before the girl was already on her knees right in front of your dick."
    mc "That was fast..."
    scene 6jh36 with dissolve
    "Jane grabbed your cock, and then she looked you right in the eye."
    jn "We've already lost a lot of time... Now let's get down to business."
    jn "Only pleasure."
    mc "I like the way you say it."
    scene 6jh37 with dissolve
    jn "Then you'll like this too."
    "Plump lips of the girl touched your dick."
    mc "Oooohhhh... Yeah... Put it in your mouth, baby..."
    scene 6jh38 with dissolve
    "Jane obediently took the tip of your cock in her mouth."
    mc "{i}Mmmm.... Her tongue is so hot.{/i}"
    jn "Mmmm... mmmmph.... mmmps..."
    mc "Don't stop, baby, take it all."
    show anim13
    mc "Aaahhhh... Yeah! That's what I was talking about."
    mc "Baby, you're amazing."
    jn "Mhhh... Hnnnngggg..... Mhhh..."
    mc "Suck it! Keep sucking!"
    mc "{i}Oooohhh... It's cool, but can we try something else?{/i}"
    scene 6jh36 with dissolve
    stop sound fadeout 1.0
    "As if reading your thoughts, Jane stopped."
    $ jane06a = False
    $ jane06b = False
    $ jane06c = False
    $ jane06d = False


    menu jane_sex06:
        "Fuck her tits" if jane06a == False:
            jn "Since you were staring at my breasts so hard today, how about you fuck them?"
            mc "Great idea."
            show anim25
            "The girl put your dick between her huge tits..."
            "...and then she started moving it up and down."
            jn "Oh... Is it nice?"
            jn "Do you like it when I do this?"
            mc "Oooohhhh... Yeah, Great!"
            mc "{i}Damn, the way she looks me in the eye...{/i}"
            mc "{i}How fucking hot is that!{/i}"
            scene 6jh40 with dissolve
            mc "{i}Mmmm... It's cool, but maybe we should try something else.{/i}"
            mc "{i}In the end, it's time to fuck this babe.{/i}"
            mc "Let's get to the real fun."
            $ jane06a = True
            $ jane06d = True
            jump jane_sex06

        "Fuck her sitting" if jane06b == False:
            scene 6jh41 with dissolve
            "The next moment, Jane was riding your cock."
            jn "Aaaahhhh! Yes!"
            jn "How much I missed a good dick!!!"
            show anim26
            "Obeying instincts, the girl began to jump up and down with pleasure."
            mc "{i}Ohhh... Her pussy squeezes my cock so tight...{/i}"
            jn "Aaaahhhh... Aaahhh.... Aaahhh...."
            jn "You go so deep inside me... Ahhh... Wow!!!"
            mc "{i}And those moans, how much they turn me on.{/i}"
            scene 6jh43 with dissolve
            "You put your arm around Jane's waist and started fucking her even harder."
            "The whole time you caress her pussy with your free hand."
            jn "Aaaahhhh... Aahhhh... Aaaahhhh...!!"
            scene 6jh44 with dissolve
            jn "God, almost... Almost there!!!"
            jn "I'm gonna fucking cum!!!"
            mc "{i}Speed up!{/i}"
            scene 6jh42 with flash
            jn "AAAHHHH!!!"
            scene 6jh42 with flash
            jn "Yeah aaaaaah... YEAH!!!"
            mc "{i}Nice.{/i}"
            mc "{i}But while she's recovering, we can try something else.{/i}"
            mc "Change position."
            $ jane06b = True
            $ jane06d = True
            jump jane_sex06

        "Let Jane choose her pose" if jane06c == False:
            scene 6jh45 with dissolve
            "In an instant you were lying on the floor, and Jane was towering over you."
            mc "{i}I think I've said this before, but God, her body is amazing...{/i}"
            jn "Lie still."
            scene 6jh46 with dissolve
            jn "Aaahhh!"
            jn "Good boy."
            mc "{i}Mmmm... Let her feel in charge and have fun...{/i}"
            scene 6jh47 with dissolve
            "Jane closed her eyes and began to ride your cock harder."
            mc "{i}She's definitely getting a kick out of it.{/i}"
            show anim14
            jn "Mmmmm.... Yeah... Yeah...."
            jn "Your cock is amazing!!!"
            jn "Aaahhhh.... So big.... Ahhh.... And so fat!"
            mc "{i}It's so nice to be praised...{/i}"
            show anim17
            jn "Mmm.... Yeah... I feel good!!!"
            mc "Oh... Oh... Go on, don't stop."
            jn "Aahhh! Ohhh! Aaahhh! It's too nice to stop."
            jn "I think... I think I'm going to cum!!!"
            mc "{i}Then it's time for me to take the initiative.{/i}"
            scene 6jh49 with dissolve
            "You took Jane's legs and started fucking her pussy even harder."
            jn "Ahhh! What are you... Aaahhh!"
            jn "Cumming! I'm cumming, [mc]!"
            scene 6jh48 with flash
            jn "AAAHHH!!!"
            scene 6jh48 with flash
            jn "Yeah aaaaaah... YEAH!!!"
            mc "{i}Nice.{/i}"
            mc "{i}But while she's recovering, we can try something else.{/i}"
            mc "Change position."
            $ jane06c = True
            $ jane06d = True
            jump jane_sex06

        "Finish" if jane06d == True:
            scene 6jh50 with dissolve
            "You shoved Jane to the floor and prepared for the final approach."
            mc "{i}I feel like I won't last long.{/i}"
            jn "Oh... [mc], how do you have so much energy?!"
            mc "{i}I'm surprising myself.{/i}"
            scene 6jh51 with dissolve
            "You put your dick in Jane with the last bit of strength."
            jn "Aahh!"
            show anim23
            mc "Mmm.... A little more... Just a little more!"
            jn "Ahh! Aaahhh! Aaaaahhh!!!"
            mc "Baby, I'm cumming soon..."
            jn "..."
            scene 6jh54 with dissolve
            jn "You can... You can cum anywhere you want..."
            jn "I'm on the pill."
            show anim23
            mc "{i}Good news.{/i}"
            menu:
                "Cum inside":
                    mc "{i}Well, since she doesn't mind...{/i}"
                    scene 6jh57 with flash
                    mc "YEEESS!"
                    mc "Yesss..."
                    jn "Mmmm... It feels good..."
                    scene 6jh58 with dissolve
                    "Only your heavy breaths were breaking the silence."
                    mc "Haa haa... Baby, that was something."
                    jn "Yep. And I think my thighs are numb."

                "Pull out":
                    "You quickly took your dick out of Jane and started to cum on her back."
                    scene 6jh55 with flash
                    mc "YEEESS!"
                    mc "Yesss..."
                    jn "Mmmm... It feels good..."
                    scene 6jh56 with dissolve
                    "Only your heavy breaths broke the silence."
                    mc "Haa haa... Baby, that was something."
                    jn "Yep. And I think my thighs are numb."

            scene black with fade
            "Some time later."

    stop music fadeout 1.0
    scene 6jh60 with dissolve
    play music "music/8 - Intro Music.ogg"
    mc "I thought it was a great night."
    jn "Yeah... I liked it myself."
    mc "How about we try something like that again?"
    scene 6jh61 with dissolve
    jn "I don't know... I need time to think about it."
    mc "In that case, I'll leave you to think."
    mc "Let me know when you decide."
    jn "Certainly."
    jn "Goodbye [mc]."
    mc "Goodbye Jane."
  
    $ renpy.end_replay()
    if not persistent.day06jane:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day06jane = True

    stop music fadeout 3.0
    jump end_d06


label end_d06:
    scene black with fade
    "You took a taxi and a few minutes later was near your apartment."
    scene 6end01 with dissolve
    play music "music/2 - Bad.ogg"
    "Approaching the front door, in the hallway you noticed a girl with a big bag."
    mc "{i}Stop... Is that who I'm thinking it is?{/i}"
    mc "{i}What the hell is she doing here?!{/i}"
    scene 6end02 with dissolve
    "Hearing your footsteps, she turned round."
    "{color=#DDA0DD}???{/color}" "[mc]."
    mc "{i}Yeah, now there's no doubt about it, it's definitely my ex-girlfriend, Emma.{/i}"
    scene 6end03 with dissolve
    "With a loud cry of joy, the girl threw herself around your neck."
    em "[mc]! Hi! It's so good to see you."
    mc "{i}Happy to see me? What's going on here?!{/i}"
    "You put the girl on the floor and took a step back."
    scene 6end04 with dissolve
    em "Hey, aren't you glad to see me?"
    "..."
    mc "What are you doing here, Emma? Uninvited, and in the middle of the night?"
    em "I wanted to call you, but it looks like your number changed. And you never answered my messages in the social network."
    mc "{i}Probably just missed it.{/i}"
    scene 6end05 with dissolve:
        ypos -1.90
        ease 8 ypos 0.0
    mc "{i}Even though it's only been about six months since we last met, I'd say she's starting to look... Different.{/i}"
    mc "{i}A little more mature or something?{/i}"
    mc "{i}But given her uneasy nature, this isn't too encouraging.{/i}"
    mc "{i}The girl is by no means bad, she was just always very unpredictable.{/i}"
    scene 6end06 with dissolve
    "Your gaze moved lower and came across a large bag with things."
    mc "{i}I don't like this at all...{/i}"
    scene 6end04 with dissolve
    mc "Again, Emma. What are you doing here?"
    scene 6end08 with dissolve
    em "Ummm.... I left home."
    mc "You what?!"
    em "I left home!"
    mc "I heard it the first time, but why?!"
    scene 6end08a with dissolve
    em "Because I'm sick of everyone. Because everyone wants to manipulate me. Because..."
    em "Ehhh..."
    em "I heard you left home, too, and I thought you'd understand me better than anyone."
    em "Believe me, I have nowhere else to go right now."
    mc "I don't know what to say."
    scene 6end07 with dissolve
    em "But I know! Can I stay with you for a couple of days?"
    em "Just until I find another place to live."
    em "Please, please, please!"
    em "At least because of our past relationship."
    mc "{i}Hell, I could throw her out now, but it's dark outside. And where would she go then?{/i}"
    mc "{i}Fuck!{/i}"
    mc "Okay, I'll let you in, but just for one night."
    mc "Tomorrow you'll have to find another place to live. We have a deal?"
    scene 6end09 with dissolve
    em "Hurray!!!"
    em "Thank you-thank you-thank you!"
    em "You won't even notice my presence."
    mc "That would be good."
    scene 6end10 with dissolve
    "Suddenly Emma came up to you and kissed you on the cheek."
    em "I missed you, [mc]."
    scene 6end09 with dissolve
    em "Heh. I'm ready."
    mc "{i}Um. And what was that just now?{/i}"
    scene 6end11 with dissolve
    "You opened the door of your apartment and Emma skipped inside."
    "You also helped with her bag."
    mc "{i}This bag is pretty heavy... How much stuff did she put in it?{/i}"
    scene 6end12 with dissolve
    em "I like it here."
    mc "No doubt, but you better not get used to it."
    em "Whatever you say."
    em "Show me a place to stay."
    scene 6end13 with dissolve
    mc "If only here."
    mc "I'm sorry, but there's only one bed in this apartment."
    em "No problem."
    em "I've been up all day, so I could sleep standing up."
    scene 6end14 with dissolve
    "Emma sat down on the sofa, her eyes a little mysterious."
    "..."
    mc "So what really happened out there, huh?"
    em "Please, let's postpone this conversation until tomorrow."
    "..."
    mc "Okay."
    em "Yeah..."
    em "And [mc]... Thank you. Really."
    "..."
    mc "If you need anything, just ask. I'll be in the next room."
    em "I understand.."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 6end15 with dissolve
    "Night."
    "..."
    scene 6end16 with dissolve
    "Pretty exhausted, you slept soundly in your bed."
    scene 6end17 with dissolve
    "The door to the room opened quietly."
    scene 6end18 with dissolve
    "A small shadow slipped inside."
    scene 6end19 with dissolve
    em "{i}Mmm... He sleeps so soundly.{/i}"
    em "{i}It's even a little cute.{/i}"
    scene 6end20 with dissolve
    em "{i}[mc].{/i}"
    em "{i}You will remember this night for a long time...{/i}"
    "..."
    jump day07_start
