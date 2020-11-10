
label day07_start:
    $ emma_sex = False
    scene black with fade
    "..."
    play music "music/6 - Positive Mood.ogg"
    scene 7dream00 with dissolve
    ls "Mmm... Not bad..."
    ls "It's so big, It surprises me every time."
    jd "Really... Big..."
    scene 7dream01 with dissolve
    ls "Hee hee! It's nothing, wait till you try it..."
    ls "I'm sure you'll like it."
    mc "No doubt, Jade, it's gonna be cool."
    scene 7dream02 with dissolve
    ls "Mmmmm..."
    mc "Oooohhh... Yeah...."
    jd "It... Is it really that great?"
    scene 7dream03 with dissolve
    mc "You betcha."
    mc "I can see you're turned on already."
    jd "..."
    scene 7dream04 with dissolve
    mc "Come here, and I'll take care of you too."
    jd "Oh... Okay."
    ls "Mmmmmhh... Mmmmmmhhhhh... Mmmmhhhh..."
    mc "Oh yeah, you girls are both great!"
    scene 7night01 with dissolve
    mc "Oh yeah... You're great..."
    em "{i}Hmm? Is he mumbling in his sleep?{/i}"
    em "{i}That's funny... I never noticed him do that before.{/i}"
    em "{i}However, I need to stay focused.{/i}"
    scene 7night02 with dissolve
    em "Mmmm..."
    em "{i}Hell, I'm starting to get turned on...{/i}"
    em "Mnnnghh... Mnnnggghh... Mmhhhh..."
    scene black with fade
    "..."
    mc "{i}Mmmm... That's nice...{/i}"
    scene 7night03a with dissolve
    "An unexpected wave of pleasure made you open your eyes."
    mc "{i}Oh... What is going on here?{/i}"
    scene 7night03 with dissolve
    mc "{i}Mmm... Emma? What is she doing here?{/i}"
    em "You're awake."
    em "It's a pity I disturbed such a sweet dream..."
    stop music
    play sound "music/music_stop.wav"
    mc "{i}Hey!!! What the fuck is she doing?!{/i}"
    stop sound fadeout 3.0
    scene 7night04 with vpunch
    "With a sharp movement, you pulled away from the girl and stared her down."
    em "Hey... Why did you jump away from me?"
    mc "..."
    mc "Why did I jump? Are you fucking serious right now?!"
    scene 7night05 with dissolve
    play music "music/8 - Intro Music.ogg"
    "The playful smile vanished from Emma's face."
    em "Okay, I see someone woke up in a bad mood."
    mc "Oh really?! What gave you that idea?!"
    scene 7night06 with dissolve
    em "Ummm.... Look, what I just did..."
    em "Don't think bad of me. It was just a way of saying thank you for letting me stay at your place tonight."
    em "So if you don't mind, we can continue..."
    scene 7night07 with dissolve
    "The girl's hand again moved to your dick."
    scene 7night08 with vpunch
    mc "Don't. Even. Think. About it."
    "The echo of your words filled the room."
    scene 7night05 with dissolve
    mc "{i}I think I was able to relay the seriousness of my intentions.{/i}"
    em "..."
    "Emma's confidence began to melt away."
    mc "{i}Yes, I can say with certainty that she didn't expect that reaction from me.{/i}"
    mc "{i}However, despite her extremely seductive appearance, I need to decide what to do next.{/i}"
    menu:
        "Be calm (+Good point)":
            $ goodpoint += 1
            mc "{i}I better stay sharp and keep a cool head.{/i}"
            scene 7night08 with dissolve
            mc "Now, listen to me carefully, Emma. Because I'm not gonna say it again."
            mc "Don't think because I'm a man, I'd be happy for any casual hookup."
            mc "We haven't dated in a long time, and I won't let you get away with things like that."
            mc "Especially when someone tries to use me without my permission."
            mc "I hope you understand me."
            scene 7night10 with dissolve
            em "..."
            mc "{i}Either she's a very good actress or she really feels guilty. At least that's how it appears.{/i}"
            mc "{i}But I have to make sure.{/i}"
            mc "I don't hear an answer. Do you understand me?"
            scene 7night10a with dissolve
            em "I understand."

        "Be angry (+Bad point)":
            $ badpoint += 1
            mc "{i}I wish I knew how to stay calm when this shit happens!{/i}"
            scene 7night08 with dissolve
            mc "I don't know what's happened to you since we broke up, but now you've made a big mistake."
            mc "And what the fuck did you expect when you came into my bed without asking?!"
            mc "How could anyone in their right mind do that? I don't understand."
            scene 7night08a with dissolve
            mc "What if I was dating someone? Or maybe I don't want to? OR MAYBE I'M JUST TIRED AND WANT TO SLEEP!"
            scene 7night10 with dissolve
            em "..."
            mc "{i}Either she's a very good actress or she really feels guilty. At least that's how it appears.{/i}"
            mc "{i}Ugh... After those words, I feel a bit better.{/i}"
            scene 7night10a with dissolve
            em "Sorry, I understand."

    scene 7night09 with dissolve
    "The girl quickly adjusted her bra strap, hiding her hard nipples from you."
    mc "{i}I'm a little sorry that she hides such beauty because of it... But now I must remain adamant.{/i}"
    scene 7night09a with dissolve
    "..."
    scene 7night10 with dissolve
    em "I'm sorry, I really didn't have ill intentions."
    em "I was just in such a lousy mood... I don't know... I just wanted to spend the night with you, like old times."
    em "But now I realize it was a stupid idea."
    scene 7night10a with dissolve
    em "I better go..."
    scene 7night11 with dissolve
    "Emma got out of bed and headed out of the room."
    mc "{i}Hmm... Even though she was reckless, I have to admit, she still looks stunning.{/i}"
    mc "{i}Damn... Maybe I shouldn't have treated her so roughly?{/i}"
    mc "{i}No, I still think she was being stupid, but I don't like the way this conversation ended.{/i}"
    mc "{i}Especially after she explained herself.{/i}"
    mc "{i}So should I let her go on such a bad note?{/i}"
    stop music fadeout 3.0
    menu:
        "Let her go":
            play music "music/8 - Intro Music.ogg"
            scene 7night12 with dissolve
            mc "{i}It's better to let her go.{/i}"
            mc "{i}She's not a fool, and she knows very well that she deserved a scolding.{/i}"
            mc "{i}Let this be a lesson to her. Next time, she needs to think before she does that shit.{/i}"
            scene 7night18 with dissolve
            "Without another word, Emma quietly left the room."
            mc "{i}Yeah, that's much better.{/i}"
            scene black with fade
            "You lay back on the bed."
            scene 7night19 with dissolve
            mc "{i}Hell, after all this fuss, I should try to get some sleep...{/i}"
            mc "{i}Quite a task. Especially after I saw my ex half naked.{/i}"
            mc "{i}Okay, stop thinking about it. Bedtime.{/i}"
            scene 7night20 with dissolve
            "You rolled over on your side and soon fell asleep."
            stop music fadeout 3.0
            "The night passed quickly, and this time no one bothered you."
            jump day07_morning
        "{color=#66FF33}Say you're not angry":
            play music "music/Maxim Nick - Falling Down.mp3"
            scene 7night12 with dissolve
            mc "{i}Fuck...{/i}"
            mc "{i}I don't know why, but after everything that's happened, I have a really bad feeling. Like I need to tell her something else.{/i}"
            mc "{i}I mean, Emma used to do this before. Except I used to like it, and now...{/i}"
            mc "{i}Now things are a lot more complicated between us.{/i}"
            mc "..."
            mc "{i}Damn, I'll try to talk to her again, then we'll see what happens.{/i}"
            scene 7night12a with dissolve
            mc "Emma, wait..."
            "After you spoke, the girl stopped."
            mc "I didn't want to raise my voice at you. It's just... It's just that this whole situation was such a surprise for me."
            mc "I hope you understand that."
            scene 7night14 with dissolve
            "You noticed the faint smile on her lips."
            scene 7night13 with dissolve
            em "No worries. I understand."
            em "In fact, I might have guessed how you'd react."
            em "After all, you've never liked surprises before."
            em "Although when it came to sex, you'd never complain."
            scene 7night15 with dissolve
            "Emma turned to face you, and you finally got a better look at her."
            mc "{i}Damn, she's in pretty good shape right now.{/i}"
            em "But I told you the truth, I was really lonely..."
            em "You know... That feeling is still there."
            scene 7night17 with dissolve
            "Emma's hand slid smoothly over her flat tummy and ended up right in her panties."
            em "Mmmm...."
            mc "{i}Ooh... She clearly knows what she wants...{/i}"
            scene 7night16 with dissolve
            em "Well, if you get lonely tonight, too, you know where to find me."
            em "I hope to see you soon..."
            scene 7night18 with dissolve
            "Without another word, Emma quietly left the room."
            scene black with fade
            "Some time later."
            scene 7night19 with dissolve
            mc "{i}Yeah... I think I just got seduced.{/i}"
            mc "{i}And I have to admit, it's not easy to fall asleep when there's a hot girl who wants to have sex with you on the other side of the wall.{/i}"
            mc "{i}Even if it's your ex...{/i}"
            "..."
            mc "{i}Looking back at our past, it's hard to say which of us was responsible for our breakup.{/i}"
            mc "{i}As much as I'd like to think she was the cause , it's not true.{/i}"
            mc "{i}We had a fight over some bullshit.{/i}"
            mc "{i}It was such a small and stupid reason that I can't even remember what it was.{/i}"
            mc "{i}In the end, she was very angry and didn't want to put up with me. I wasn't much better... I felt a banal stubbornness.{/i}"
            mc "{i}And here we are, lying separated from each other by just some wall.{/i}"
            mc "{i}So, what should I do?{/i}"

            menu:
                "Try to sleep":
                    mc "{i}Fuck it! She's obviously up to something, and I definitely don't want to be a part of it.{/i}"
                    scene 7night20 with dissolve
                    "You rolled over on your side and soon fell asleep."
                    "The night passed quickly, and this time no one bothered you."
                    stop music fadeout 3.0
                    jump day07_morning
                "{color=#66FF33}Go to Emma":
                    mc "{i}What the hell! I've always been in favor of having a good time, so why not?{/i}"
                    stop music fadeout 3.0
                    jump day07_emmasex


label day07_emmasex:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    if lisa_path == True:
        $ cheat_point += 5
    scene 7emma01 with dissolve
    $ emma_sex = True
    play music "music/Maxim Nick - Smooth Light.ogg"
    "You jumped out of bed and headed out of the room."
    mc "{i}Ha! She didn't even close the door behind her.{/i}"
    mc "{i}What a cocky little devil.{/i}"
    scene 7emma02 with dissolve
    "After you went into the living room, you saw a very naughty picture."
    mc "{i}Like she said, she's waiting for me...{/i}"
    mc "{i}Am I that predictable?{/i}"
    scene 7emma03 with dissolve
    "Emma seductively leaned back on the couch and beckoned you with her hand."
    em "What are you standing there for? Come closer, I won't bite."
    em "Well, unless you want me to. Hee hee."
    mc "{i}Oh... I feel like it's gonna be a very interesting night.{/i}"
    scene 7emma04 with dissolve
    "A second later, you were standing in front of your ex-girlfriend."
    em "Mmm... How strange to see you naked again."
    mc "Trust me, the feeling is mutual."
    em "You look different, though... Have you been pumping up?"
    mc "Heh, that's unlikely. But thank you for the compliment..."
    scene 7emma05 with dissolve
    mc "I can't help but notice that you've gotten prettier yourself since we last met."
    mc "{i}Especially your ass.{/i}"
    em "Oh... An exchange of compliments... I approve!"
    em "But let's not waste time."
    scene 7emma06 with dissolve
    "Emma's soft hand touched your cock..."
    show anim31
    "...and then began to move smoothly back and forth."
    em "Yeah, that's exactly what we need right now."
    em "You should know how much I want to feel him inside me right now..."
    mc "{i}Mmmm... If only she knew how much I wanted it.{/i}"
    mc "{i}But all in good time.{/i}"
    scene 7emma07 with dissolve
    "At the same time the second girl's hand undid her bra and dropped it to the floor."
    mc "{i}Wow, it's time to see those charms that are hiding underneath.{/i}"
    scene 7emma08 with dissolve
    mc "{i}Yeah... Superb.{/i}"
    "Before you, flaunted a half-naked girl looking at you with a lustful expression."
    mc "{i}Well, now I'm sure I didn't come here for nothing.{/i}"
    mc "{i}I just had to see it!{/i}"
    scene 7emma09 with dissolve
    em "Mmm... I hope you missed my pussy, ' cause she totally missed you."
    mc "Heh. You can be sure of that."
    mc "Now, turn around."
    scene 7emma10 with dissolve
    "Emma obediently complied with your request and displayed her beautifully formed ass."
    mc "Now let's get rid of this useless piece of cloth."
    em "Hee hee. I don't mind at all."
    scene 7emma10a with dissolve
    mc "{i}Yeah... Just a little more...{/i}"
    "You quickly pulled the panties from the girl and threw them to rest near the bra."
    scene 7emma11 with dissolve
    mc "{i}Oh, I forgot how great her ass is!{/i}"
    mc "{i}Almost perfect...{/i}"
    mc "{i}But stop staring at her, it's time to start the fun.{/i}"
    stop music fadeout 1.0
    scene 7emma12 with dissolve
    "With your right hand you went down to Emma's pussy, and then began to caress her."
    play music "music/1 - Atmosphere.ogg"
    em "Aaahhh... Mmm.... Yeah..."
    mc "Looks like someone's already wet."
    em "Oh, you can't blame me for that... Now go on!"
    mc "{i}Hmm... I don't see the point in dragging it out, let's get right to the hot stuff.{/i}"
    scene 7emma13 with dissolve
    "You got down on your knees and put the head of your dick in."
    em "Oh... So you decided to start without foreplay?"
    mc "You made it very clear that you don't need any right now."
    scene 7emma15 with dissolve
    "A moment later you made a push forward and your cock was entirely inside your ex-girlfriend."
    em "Aahhhh!!!"
    mc "{i}Oh yeah... She squeezes me so tight...{/i}"
    scene 7emma14 with dissolve
    "Giving in to the sexual impulses, you and Emma began to move faster."
    em "Aahhh! That's right... Yes!!!"
    em "Don't stop!"
    mc "Ohhh... That's great..."
    scene 7emma16 with dissolve
    "Emma arched harder, making her ass seem even more seductive."
    em "Fuck me! Fuck me harder, [mc]! AAAHHHH!!"
    show anim38
    em "Yes... Yes... This is amazing..."
    mc "{i}Fuck, her moans are so arousing. I just can't stop.{/i}"
    mc "Take that!"
    em "Aaaahhhh.... Yeeesss..."  
    show anim39
    em "Haa... Haa... your cock is... Cool!"
    em "I... you're deep."      
    mc "{i}Nice.{/i}"    
    mc "{i}However, it still wouldn't hurt to change positions...{/i}"
    mc "Baby, let's try lying down."
    scene 7emma17 with dissolve
    "Emma understood you perfectly."
    em "Mmm... Come on, baby, I'm waiting."
    mc "{i}Ooh... She knows exactly what I want.{/i}"
    scene 7emma18 with dissolve
    em "..."
    scene 7emma18a with dissolve
    em "Ooohh, yeah.... That's right..."
    scene 7emma19 with dissolve
    "You noticed Emma was biting her lip, barely able to hold back her moans."
    mc "{i}Yes... Not only does she have a great ass, but the rest of her body...{/i}"
    show anim33
    "Holding up the girl's leg, you began to fuck Emma from behind with all your might."
    em "Hah... Hah... Come on, [mc]... I want you to go deeper!"
    mc "Then take it!"
    em "Haa... Hah... Hah!"
    mc "{i}Ooh... Her whole body is squirming...{/i}"
    mc "{i}She's driving me crazy!{/i}"
    scene 7emma21 with dissolve
    "Almost imperceptibly for each other, you again changed position, and this time Emma was on top."
    show anim32
    em "Ahhhh.... Aahhhh... Yeah..."
    em "God, this is so good!"
    em "[mc]... Make... Make me cum!"
    mc "{i}Oh, if she's asking for it...{/i}"
    mc "{i}I have to accelerate!{/i}"
    scene 7emma22 with flash
    "Soon you felt shaking waves of pleasure sweep over Emma's body."
    em "Yeah... Yeah!!!"
    scene 7emma22 with flash
    em "Haa... Haa... Haa..."
    scene black with fade
    "A few seconds later."
    scene 7emma22a with dissolve
    em "Oh, [mc]... It was..."
    em "Not bad."
    mc "Huh? Are you kidding me? Just, not bad?"
    em "Eh, pretty good?"
    mc "{i}Ha! She's mocking me. What an asshole!{/i}"
    scene 7emma23 with dissolve
    "The next second you turned to face the girl, and are suddenly smothered in her soft breasts."
    em "Oh, you seem ready to go on..."
    mc "{i}She's asking!{/i}"
    mc "I'll show you what \"not bad\" is. You won't forget this for a long time."
    scene 7emma25 with dissolve
    "Emma's face came closer, and you could feel her heavy breathing."
    em "I forgot how tough you can be sometimes..."
    em "Well, maybe this will help you a little."
    scene 7emma26 with dissolve
    "Your lips merge to form a long kiss."
    em "Mmmm...."
    mc "{i}Yeah... That feels good.{/i}"
    scene 7emma26a with dissolve
    mc "{i}She kisses as well as ever.{/i}"
    em "Mmm..."
    scene 7emma24 with dissolve
    em "I hope you enjoyed it... Now, let's continue!"
    mc "Yep. Get your knees on the couch and bend over."
    em "Mmm... Okay."
    scene 7emma28 with dissolve
    "As soon as Emma was in position on the couch, you put a cock in her pussy and continued to pound her."
    show anim30
    em "Aaahhh... Hah... Hah... Aaah..."
    mc "How do you like that? You like the way I fuck you?!"
    em "Aaahhh... God, Yes... Ahh..."
    em "I fucking love it!!!"
    em "Now shut up and keep moving."
    mc "{i}Huh... I love the way she acts...{/i}"
    scene 7emma29 with dissolve
    mc "Emma... I'm cumming..."
    em "Ahhh.... Aaahhh.... I understand..."
    scene 7emma30 with dissolve
    "The girl leaned back on the sofa and spread her legs apart."
    scene 7emma31 with dissolve
    em "Mmm... Come on, [mc]..."
    em "I want you to cum on me!"
    mc "{i}Oooh... That's what I was going to do anyway.{/i}"
    scene anim34 with dissolve
    "You came closer to Emma and started jerking off."
    mc "Haaah... Haaah... Haaah..."
    em "Come on, baby..."
    mc "Aaahhh... Haaah... Haaah..."
    em "Show me what you got."
    em "Cum right on me. Come on!"
    mc "Oh... Take that!!!"
    scene 7emma33 with flash
    em "Oh!"
    scene 7emma33 with flash
    mc "Oh yeah... Finally...."
    scene 7emma34 with dissolve
    "..."
    em "Oho... Your semen is so hot."
    em "But you got me covered in it!"
    mc "Heh, that's what you wanted."
    scene 7emma35 with dissolve
    em "Oh, don't worry, I liked it."
    mc "Great."
    em "Yeah, that's great. But still, could you find me a couple of napkins?"
    mc "Heh. Sure, wait a minute..."
    stop music fadeout 2.0
    scene black with fade
    "Some time later."
    scene 7emma36 with dissolve
    em "Uhhh... That was awesome!"
    em "I even felt like it was somehow calming."
    mc "Yes, I thought so too."
    em "By the way, was it just me, or did you learn some new tricks?"
    mc "Who knows, maybe."
    scene 7emma36a with dissolve
    play music "music/Maxim Nick - It's okay (final).mp3"
    "..."
    "You were both silent for a while, until Emma broke the silence again."
    em "Well, I guess that's all."
    mc "Yeah..."
    em "Good night then?"
    mc "{i}Hmm? I feel bad that she has to sleep on the couch now...{/i}"
    mc "{i}Especially after what we just had.{/i}"
    mc "{i}Fuck it!{/i}"
    scene 7emma37 with dissolve
    "In one deft movement you threw the blonde on your shoulder."
    em "Hey! What are you doing?!!! Let me go!"
    mc "Well, no, after everything that's just happened, you're not gonna sleep on that hard couch."
    "Emma's fluttering subsided."
    scene 7emma39 with dissolve
    em "Where should I sleep then?"
    mc "{i}Heh, she's playing dumb.{/i}"
    em "Hey!!! [mc]!"
    scene 7emma38 with dissolve
    mc "I think you already know that."
    mc "Now shut up and I'll take your pretty ass to my room."
    em "..."
    mc "Well done, you can obey when you want."
    scene black with fade
    "Some time later."
    scene 7emma42 with dissolve
    em "Mmmm... I have to admit, sleeping in your bed is going to be a lot nicer than sleeping on that hard couch."
    mc "I knew you'd appreciate it."
    em "Yes... You know me well."
    scene 7emma40 with dissolve
    em "Hey, [mc] you want to talk about what just happened between us?"
    mc "Not now... Let's just enjoy a good night. OK?"
    em "Yeah, sure..."
    scene 7emma41 with dissolve
    em "And the evening was really good."
    mc "Yeah."
    mc "{i}I just wish we didn't have to deal with this tomorrow.{/i}"
    mc "{i}Yeah... I feel like it's gonna be a real headache.{/i}"
    mc "{i}But it will be tomorrow.{/i}"

    $ renpy.end_replay()
    if not persistent.day07emma:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day07emma = True

    scene 7emma43 with dissolve
    "You and Emma fell asleep hugging."
    stop music fadeout 3.0
    "There was a new day ahead of you."
    jump day07_morning


label day07_morning:
    scene 7city01 with dissolve
    "Next morning."
    scene 7morning01 with dissolve
    play music "music/7 - Just Happy.ogg"
    "You felt the warm sunlight shine on your back and shoulders."
    mc "Mmmm..."
    scene 7morning01a with dissolve
    mc "{i}Hm? Seems it's already morning.{/i}"
    mc "{i}Damn, it came fast.{/i}"
    scene 7morning03 with dissolve
    "Sleepily rubbing your eyes, you slowly got out of bed."
    if emma_sex == True:
        scene 7morning02 with dissolve
        mc "{i}Um. Where did Emma go?{/i}"
        mc "{i}Although, come to think of it, she always was an early riser. No wonder she's already awake.{/i}"
        mc "{i}I should check where she is...{/i}"
        mc "{i}But first, the toilet. Emma can wait.{/i}"
    else:
        mc "{i}Perhaps after yesterday, I'd better check on my guest.{/i}"
        mc "{i}But first, the toilet. Emma can wait.{/i}"
    scene black with fade
    "You quickly threw on some clothes and went to the bathroom."
    scene 7morning04 with dissolve
    "Opening the door to the bathroom, you witnessed someone brushing her teeth."
    scene 7morning05 with dissolve:
        ypos -1.7
        ease 8 ypos 0.0
    mc "{i}Wow, she's wearing nothing but panties.{/i}"
    mc "{i}Very hot, by the way.{/i}"
    mc "{i}...{/i}"
    scene 7morning06 with dissolve
    em "Oh, [mc] you're awake!"
    em "I'm sorry I took the bathroom. I won't be long, I promise."
    mc "Yeah... Yeah... Sure."
    mc "{i}Hell, she looks even better in daylight.{/i}"
    scene 7morning07 with dissolve
    "Your gaze moved lower."
    mc "{i}Mmm... Yes, by the light of day, definitely better.{/i}"
    scene 7morning06 with dissolve
    em "[mc]?"
    scene 7morning04 with dissolve
    mc "Oh, sorry... I was thinking."
    em "Yeah... Sure."
    mc "Anyway, you can take your time. I'll mind my own business for now."
    em "Thank you!"
    scene 7morning08 with dissolve
    "You closed the door behind you and thought."
    mc "{i}It's all strange and unusual... And a little sexy.{/i}"
    mc "{i}However, when she comes out, I'll have to remind her to move out by tonight.{/i}"
    mc "{i}I shouldn't let her live here.{/i}"
    stop music fadeout 3.0
    play sound "music/doorbell.wav"
    "DING-DING!"
    scene 7morning08a with dissolve
    stop sound fadeout 3.0
    mc "{i}Huh?{/i}"
    "..."
    mc "{i}Of course... With Murphy's Law, someone has to come when my ex is in the bath.{/i}"
    mc "{i}Well, thank you universe! You once again decided to complicate my life.{/i}"
    play sound "music/doorbell.wav"
    "DING-DING!!!"
    mc "I'm coming!"
    scene 7morning09 with dissolve
    stop sound fadeout 3.0
    play music "music/9 - You Can Make the Sound.ogg"
    "You opened the front door and saw Jacob in front of you."
    j "Hey, bro! I'm sorry I didn't tell you I was coming."
    mc "Yeah, Hello to you too..."
    mc "{i}Well, perhaps I'd better get him out of here as soon as possible to avoid any lengthy conversation.{/i}"
    mc "{i}Not that I'm afraid he'll see Emma, but it's better to avoid it if possible.{/i}"
    mc "Hey, you know my phone works, right?"
    j "Of course I know! But the news that I have is better reported in person."
    mc "{i}Hmm... What kind of news is that?{/i}"
    mc "Okay, I'm interested."
    mc "Can we go talk on the roof? I'll take a couple of beers with us."
    j "On the roof?"
    j "Of course, why not? That's a good idea."
    scene 7morning10 with dissolve
    stop music fadeout 3.0
    "That's when you heard the bathroom door start to open."
    mc "{i}Fuck...{/i}"
    scene 7morning11 with dissolve
    "As if nothing had happened, Emma came out in one towel and looked in our direction with interest."
    mc "{i}It's hard to know if she chose this moment to come out on purpose or by accident.{/i}"
    mc "{i}In any case, now there's no avoiding an unpleasant conversation.{/i}"
    scene 7morning12 with dissolve
    j "Emma..?"
    j "What the hell are you doing here? Didn't you and [mc] break up?"
    scene 7morning13 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    "The girl came closer and stood next to you."
    em "Jacob! What a meeting..."
    em "It's been a long time since we've seen each other."
    scene 7morning14 with dissolve
    j "Yes, it is... Uhh..."
    j "Wait a minute! What the hell is going on here?"
    j "[mc] what is she doing here?"
    mc "{i}I'd better explain it to Jacob myself. Who knows what she might say to him.{/i}"
    scene 7morning13a with dissolve
    mc "Relax, man, it's a lot simpler than you're thinking."
    mc "As it turned out, Emma ran away from home and had no alternative but to come to me last night."
    mc "Of course, I couldn't put her out on the street in the middle of the night."
    mc "And now she will get dressed and look for a new home, because my generosity is not infinite."
    scene 7morning15 with dissolve
    "You turned to your ex and looked at her hard."
    mc "Am I right?"
    mc "{i}I hope she's smart enough to back me up...{/i}"
    em "Eh..."
    em "As much as I'd like to stay here and talk to you, it's just as [mc] said."
    scene 7morning15a with dissolve
    em "It was good to see you again, Jacob."
    em "I won't take up any more of your time, and I'll go and change."
    scene 7morning16 with dissolve
    "Absolutely shameless, Emma took off her towel and went into the living room."
    scene 7morning17 with dissolve
    mc "{i}Wow... What the hell is she doing?{/i}"
    em "Oh... It's so hot in here..."
    scene 7morning18 with dissolve
    mc "{i}What a devil!{/i}"
    scene 7morning19 with dissolve
    "You and Jacob watched her for a moment."
    mc "{i}Mmmmm... Perhaps it's time to stop staring, I'm not alone here.{/i}"
    scene 7morning20 with dissolve
    j "Damn... Man, your ex is hot..."
    mc "{i}Yeah, you can't argue with that.{/i}"
    scene 7morning21 with dissolve
    j "But I hope you're not sleeping with her."
    j "You know, better not answer that... I don't want to know."
    j "I just suggest you get rid of her as soon as possible."
    mc "{i}Oh, Jacob, trust me, I'm working on it.{/i}"
    j "I'm no expert at this sort of thing, but even I know that casual encounters with exes rarely lead to anything good."
    if jacob_knows_about_lisa == True:
        j "Plus, you're Dating Lisa. And if she finds out about it, it's obviously not going to be good for your relationship."
        j "Or for our band..."
    else:
        j "You can be sure of that."
    mc "Yep... I think I agree with you on that."
    mc "Okay, let's go to the roof, we'll talk there."
    mc "I want to hear what you had to tell me in person so badly..."
    scene 7morning21a with dissolve
    j "Oh yeah! You'll never believe what I've done!"
    j "Anyway, listen..."
    stop music fadeout 3.0
    jump day07_roof

label day07_roof:
    scene black with fade
    "Some time later."
    scene 7roof04 with dissolve
    play music "music/3 - Dream With U.ogg"
    mc "Wait, wait a minute!"
    mc "Let me see if I got you right."
    mc "Did a friend of yours invite our band to perform in his club with other groups of newcomers? And it all takes place this weekend?"
    mc "Did I miss anything?"
    j "Well, basically, that's the gist of it."
    scene 7roof02 with dissolve
    mc "Damn... But you do realize we're not ready for that yet?"
    mc "There are only two and a half songs in our repertoire... And those are very far from perfect."
    mc "..."
    mc "How did your friend even know about us?"
    scene 7roof01 with dissolve
    j "I told him about us."
    j "Besides, I recorded our last rehearsal on my phone and showed him a little bit."
    j "You might be surprised, but he liked it. Very much."
    mc "Huh... You didn't waste any time."
    mc "Why didn't you tell us?"
    j "Ha! How was I supposed to know it would lead to anything?"
    mc "{i}Ain't that the truth.{/i}"
    mc "{i}But still...{/i}"
    scene 7roof06 with dissolve
    mc "I repeat, Jacob, we're not ready. And it's very unlikely that we will have time to prepare. I mean, there are only a few days left until the weekend."
    mc "Plus, we don't know if the girls have any plans for that day."
    scene 7roof03 with dissolve
    j "Hey, Hey! [mc] stop for a second."
    mc "..."
    scene 7roof03a with dissolve
    j "In addition to us there will be three more bands of newcomers, so everything is fine. We'll make it."
    j "And the girls... Trust me, they'll find the time. I'm sure."
    j "This is a good chance, which is no better and no worse than others. It's in our interest to not pass on this opportunity..."
    scene 7roof02 with dissolve
    mc "{i}Um... Well, if you think about it, Jacob is not a fool and knows what he's talking about.{/i}"
    mc "{i}Maybe it's worth a try.{/i}"
    scene 7roof04 with dissolve
    mc "Okay."
    mc "But we'll have to be very well prepared. I don't want to screw up my first gig."
    j "Heh, trust me, none of us want that!"
    scene 7roof03 with dissolve
    j "Oh, yeah, I have some things to finalize tomorrow, so if you want, you can come with me and have a look at this club."
    j "It's called Purple Orchid."
    mc "{i}Yeah... What a name. Sounds like some brothel.{/i}"
    mc "Well, that sounds interesting. I'm in."
    j "Great. Then we'll tell Lisa and Jade about it at rehearsal."
    mc "Yeah, that's probably best."
    "..."
    scene 7roof05 with dissolve
    mc "Then I suggest we drink to a brighter future."
    j "And simply better \"For us!\""
    mc "For us!"
    stop music fadeout 3.0
    scene black with fade
    "After spending some more time with Jacob, you agreed to meet later at rehearsal."
    "Right after that, you headed back to your apartment."
    jump day07_breakfast

label day07_breakfast:
    scene 7breakfast01 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "Once inside the apartment you came across a very unusual situation, Emma was cooking."
    mc "{i}Wow... Looks like she didn't waste any time.{/i}"
    mc "{i}She's so into cooking, she didn't even notice me.{/i}"
    mc "Ahem."
    scene 7breakfast02 with dissolve
    em "Oh, [mc]?"
    em "Sorry, I didn't see you."
    em "I hope you don't mind that I raided your fridge to make us breakfast."
    scene 7breakfast03 with dissolve
    "You looked down at the stove."
    mc "No... Of course not."
    mc "In fact, it's a pleasant surprise."
    scene 7breakfast02a with dissolve
    em "Mmm... Thanks."
    em "Sit down at the table, everything will be ready soon."
    mc "Whatever you say."
    scene 7breakfast04 with dissolve
    "You sat down and began to watch Emma with curiosity."
    mc "{i}Hmm... I can't get rid of the strange feeling that somewhere in all this is a very big catch, I haven't noticed yet.{/i}"
    scene 7breakfast05 with dissolve
    mc "{i}The thing is, Emma's acting like she's the perfect girl right now.{/i}"
    mc "{i}She's smart, beautiful and very kind. Great combination of normal human qualities, if you ask me.{/i}"
    mc "{i}Except that's not how I remember her from our past relationship... Not at all.{/i}"
    scene 7breakfast06 with dissolve
    em "Breakfast is ready!"
    em "I hope you like it."
    mc "{i}Oh, maybe I'm just being paranoid. After all, who says people don't change?{/i}"
    scene 7breakfast07 with dissolve
    "Emma put the plates on the table and sat across from you."
    mc "Thanks."
    scene 7breakfast09 with dissolve
    em "You're welcome. It wasn't difficult at all."
    mc "{i}Damn... She's so sweet right now.{/i}"
    if emma_sex == True:
        "For a second, you remembered the events of last night."
        mc "{i}And the sex last night was really, really good...{/i}"
    else:
        mc "{i}I almost stopped being mad at her for what she did last night...{/i}"
    scene 7breakfast08 with dissolve
    em "You already know what I'm going to do today, so what are your plans?"
    mc "I guess I'll only have one thing to do until the weekend - rehearsal with the band."
    em "Eh... That's harsh."
    mc "Well, I wouldn't say that. Turns out, this Saturday, our band will have a concert. There'll be a lot to do..."
    scene 7breakfast10 with dissolve
    em "Mmm... Now that's interesting."
    em "Concert... Very good! It took you a long time to get to this point, now he's your first big step."
    mc "Yeah, probably."
    em "And what kind of place? Big, small, how many people?"
    mc "I don't know... A small club called Purple Orchid. Or something."
    em "Heh. The name sounds more like a strip club."
    mc "Yeah... I had a similar thought."
    scene 7breakfast11 with dissolve
    "You and Emma started Breakfast while you were still making small talk."
    scene black with fade
    "A few minutes later."
    scene 7breakfast11 with dissolve
    mc "Ahem... Look, Emma, I want to ask you a question..."
    scene 7breakfast09 with dissolve
    em "Yeah, sure, ask me."
    mc "I want to know why you came to me last night."
    mc "I can believe you had a fight with your friends and even your parents, but why didn't you stay at some hotel? I don't understand."
    scene 7breakfast09a with dissolve
    em "I'm not rich enough to live in a hotel."
    mc "You're not, but your family is."
    scene 7breakfast09b with dissolve
    em "This... Uhh..."
    mc "{i}She seems lost in thought.{/i}"
    scene 7breakfast09a with dissolve
    em "Like I said, I'm not rich. Not anymore."
    mc "{i}Huh? What does that mean? Really...{/i}"
    mc "Did something happen? If you want, you can tell me."
    em "I'm sorry, but I don't want to talk about it..."
    mc "{i}Really..{/i}"
    mc "Um... Okay, if that's what you want, fine."
    scene black with fade
    "Some time later."
    scene 7breakfast12 with dissolve
    "When Breakfast was over, you got up from the table."
    mc "Thanks for the breakfast, it was delicious."
    em "Don't mention it. What are you going to do now?"
    mc "Well, like I said, I have to go to rehearsal."
    em "I understand."
    mc "One more thing, Emma... I don't mean to be rude, but when I get home tonight, I'll hope you've found somewhere else to stay."
    scene 7breakfast13 with dissolve
    "When you said what you wanted, you went to the exit."
    "..."
    em "[mc]..."
    scene 7breakfast13a with dissolve
    "You stopped."
    mc "Yes?"
    scene 7breakfast14 with dissolve
    em "..."
    em "No. It's nothing."
    mc "{i}Um... She's obviously worried about something.{/i}"
    mc "{i}But if she doesn't want to talk about it, it's better to leave her be.{/i}"
    scene 7breakfast14b with dissolve
    em "Good day."
    mc "Yeah, you too. Bye."
    em "Bye."
    scene black with fade
    "You left Emma alone."
    stop music fadeout 3.0
    scene 7breakfast14 with dissolve
    em "{i}...{/i}"
    if emma_sex == True:
        em "{i}Well, it went a lot better than I thought it would.{/i}"
    else:
        em "{i}Well, all things considered, it's not that bad.{/i}"
    scene black with fade
    "A few days ago."
    scene 7flashback01 with dissolve
    play music "music/8 - Intro Music.ogg"
    em "You know, I came here out of curiosity, even though it seemed very strange."
    em "But now..."
    em "Now that you've told me all this, I think it's crazy."
    em "No, you really want me to have some unthinkable effect on your son? Are you sane?"
    scene 7flashback02 with dissolve
    f "Take your time."
    f "I'm not offering you anything illegal. In fact, I think it would be good for both of you."
    f "If you can convince him to stay in the family and work for me, trust me, you'll both be well off for the rest of your lives."
    f "And in your current position, money certainly wouldn't hurt."
    scene 7flashback03 with dissolve
    em "{i}What the hell?! How the hell did he know that?{/i}"
    em "{i}Although... With his resources, it's no problem to find out about my family's bankruptcy.{/i}"
    em "{i}Besides, I remember [mc] talking about his father as a control freak. Is that what I'm seeing now?{/i}"
    em "{i}It's pretty creepy.{/i}"
    scene 7flashback04 with dissolve
    f "Emma. I'm not asking you to give me your answer right here and now."
    f "Go somewhere. Clear your head. And think about everything."
    f "If you want, you can even meet with my son, and evaluate whether or not if you'll do it."
    f "If you agree, you'll send me your answer in an email. And if not... You can just forget about everything."
    f "The only thing I'm asking you to do is not tell him."
    "The man came out from behind the Desk and stood in front of Emma."
    scene 7flashback05 with dissolve
    em "Eh... But you know it's wrong."
    em "Shouldn't you, as a father, support him and all that?"
    em "And now it looks like we're plotting something stupid here."
    em "I've seen this on TV, and this kind of stuff rarely ends well."
    scene 7flashback06 with dissolve
    f "Listen to me, girl. We're not here on TV, we're here in real life. And in real life, we often make difficult decisions."
    f "And often these decisions are not known to anyone but ourselves. You know what I'm getting at?"
    em "..."
    f "Of course you understand."
    f "Besides, who knows when the next time you'll have such a good opportunity to get back on your feet?"
    em "{i}That slippery bastard.{/i}"
    scene 7flashback06a with dissolve
    f "That's all I wanted to say to you, and now you can go."
    f "My new assistant will give you a number where you can reach me."
    scene 7flashback07 with dissolve
    "Emma was lost in thought when she left this office."
    em "{i}Damn... This guy's crazy, but...{/i}"
    em "{i}...but maybe it's worth a try.{/i}"
    em "{i}After all, [mc] is not a bad guy, and we used to like each other, and we broke up because of some completely stupid stuff.{/i}"
    em "{i}Eh... Nice work, Emma. What a mess you just got yourself into.{/i}"
    stop music fadeout 3.0
    scene black with fade
    "Now."
    scene 7breakfast14 with dissolve
    "..."
    scene 7breakfast15 with dissolve
    "Emma pulled out her phone and started to text something."
    em "{i}... And send.{/i}"
    scene 7breakfast16 with dissolve
    em "{i}That's it.{/i}"
    scene 7breakfast15 with dissolve
    em "{i}Congratulations to you, Emma... You just sold your conscience.{/i}"
    em "{i}...{/i}"
    scene black with fade
    "Some time later."
    jump day07_rehearsal

label day07_rehearsal:
    scene 7train01 with dissolve
    play music "music/12 - The Moose.ogg"
    "You leisurely walked down the street when you saw a bike rush past."
    "Oddly enough, you quickly recognized the driver and passenger."
    scene 7train02 with dissolve
    ls "Uh-ha-ha!!! It's sooo cool!"
    mc "{i}Heh. Someone seems to be having a lot of fun.{/i}"
    mc "{i}I didn't even know Jade had a motorcycle.{/i}"
    mc "{i}I don't know much about her, though.{/i}"
    scene 7train03 with dissolve
    "Looking closer, you realized that both girls were in a very good mood."
    mc "{i}Uh, I'm even a little envious of their ease.{/i}"
    scene 7train04 with dissolve
    "A few moments later, the bike turned at the intersection and was right in front of you."
    scene 7train05 with dissolve
    ls "Ta-da!"
    mc "Wow... That was a spectacular entrance."
    ls "Hehe. Not only spectacular, but also very fun!"
    mc "{i}And they became close friends in such a short period.{/i}"
    mc "Yeah, I noticed that too."
    jd "Hello, [mc]."
    mc "Hi Jade, Lisa."
    ls "Hello!"
    if lisa_path == True:
        scene 7train07 with dissolve
        "While Jade was busy with the bike, Lisa came forward and hugged you tight."
        ls "Good to see you, [mc]."
        mc "You too."
    else:
        "..."
    scene 7train06 with dissolve
    ls "So... Do you know what kind of surprise Jacob has in store for us?"
    mc "{i}Of course he hasn't told them yet, but he's already been scheming.{/i}"
    mc "{i}Well, I won't spoil the surprise.{/i}"
    mc "All in due time."
    scene 7train08 with dissolve
    ls "That's how it is... So everyone knows except me and Jade?"
    mc "Hey, don't make me look guilty! You'll find out soon enough."
    ls "Mmm... Okay."
    jd "Shall we go inside?"
    mc "Yes, let's go. Jacob's probably already here."
    scene 7train09 with dissolve
    ls "Hey, [mc] this surprise... Well, is it nice?"
    mc "For the most part, Yes."
    ls "Eeehh... For the most part? How's that?"
    mc "Patience, my young Padawan. You'll find out soon enough."
    jd "..."

    scene 7train10 with dissolve
    "Entering the rehearsal room, you immediately noticed Jacob."
    j "Hey... I see you weren't in too much of a hurry."
    j "I've been waiting for you."
    mc "Well, no one asked you to come early."
    j "Okay, okay, I get it."
    scene 7train11 with dissolve
    j "So, you guys ready to hear the big headline of the day?"
    ls "Come on, get on with it already!"
    j "Heh, then listen..."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 7train12 with dissolve
    play music "music/16 - Bright Colors.ogg"
    mc "...thus, we have only a few days to prepare properly."
    j "Well, we hope that everyone can find time for Saturday night."
    mc "Yes, sorry we didn't warn in advance, but we also just found out about it only today."
    mc "So yeah..."
    scene 7train15 with dissolve
    ls "No problem! I'll be free on Saturday, and ready to rock."
    mc "{i}Heh. I never doubted her.{/i}"
    scene 7train13 with dissolve
    j "That's the spirit! Keep it up!"
    j "What about you, Jade?"
    scene 7train16 with dissolve
    jd "I'm in."
    mc "{i}Yeah, that's why I like her. As always, short and clear.{/i}"
    scene 7train15a with dissolve
    mc "Okay, it's really cool that you all agree, but I think you also understand that we're going to have to be well prepared."
    mc "We'll have to do our best."
    scene 7train16a with dissolve
    jd "What do you suggest?"
    scene 7train15a with dissolve
    mc "It's simple. Until Saturday, I suggest we gather here every day and rehearse."
    scene 7train14 with dissolve
    j "But remember, this is only a temporary necessity."
    j "If someone needs to leave early or late, no problem. We all understand."
    "However, you were lucky and everyone agreed."
    scene 7train15b with dissolve
    ls "Okay, after that news, I can't wait to get started."
    ls "I hope you don't mind."
    "..."
    ls "Great!"
    scene 7train17 with dissolve
    "You agreed to Lisa's proposal, and in just a few minutes the rehearsal began."
    "You couldn't help but notice that after this sudden news, the guys seemed to light up with overflowing energy."
    scene 7train18 with dissolve
    "You turned your attention towards Jade."
    mc "{i}Looks like she's always down for playing guitar.{/i}"
    mc "{i}I expected nothing less from her.{/i}"
    scene 7train19 with dissolve
    "Then you looked at Lisa, and she caught your eye."
    mc "{i}Oh, yeah, her voice is amazing.{/i}"
    mc "{i}I can't believe she never sang in any band before.{/i}"
    scene 7train20 with dissolve
    mc "{i}Hell, Jacob and I are pretty good, too.{/i}"
    mc "{i}We're lucky to be together.{/i}"
    "And you liked that."
    scene 7train17 with dissolve
    stop music fadeout 3.0
    "You continued your rehearsal."
    scene black with fade
    "Some time later."
    "You took a break during where everyone decided to relax a little."
    scene 7train20a with dissolve
    mc "{i}Hmm... While everyone has nothing to do, I think this is a good opportunity to talk with the guys separately.{/i}"
    mc "{i}So, Jade's out on the street right now, Jacob's listening to music, and Lisa's going to play pool.{/i}"
    mc "{i}Who should I start with?{/i}"

    $ day07_q01 = False
    $ day07_q02 = False
    $ day07_q03 = False
    $ day07_photo01 = False

    menu day07_menu01:
        "Talk to Jacob" if day07_q01 == False:
            play music "music/9 - You Can Make the Sound.ogg"
            $ day07_q01 = True
            mc "{i}It might be nice to talk to Jacob right now.{/i}"
            mc "{i}And to be honest, I really wonder what he's so enthusiastically listening to.{/i}"
            scene 7train47 with dissolve
            mc "Hey, melomaniac, what are you listening to?"
            j "One second..."
            j "Okay... I'm listening."
            mc "{i}Hmmm, now I'm even more interested.{/i}"
            scene 7train48 with dissolve
            j "Sorry, what were you asking me?"
            mc "I wanted to know what you were listening to so intently."
            scene 7train48a with dissolve
            j "Oh, that."
            j "I found a few songs on the internet of one of bands with whom we're performing together with this weekends."
            j "I was interested to see how they were."
            mc "Sounds interesting... What's your verdict?"
            scene 7train49 with dissolve
            j "Why don't you listen to them yourself?"
            mc "{i}Is it really that good?{/i}"
            mc "Okay, give me the headphones."
            scene 7train50 with dissolve
            "You put the headphones on and started listening."
            mc "{i}Hmm... Is it me or is this music really just mediocre? Who knows...{/i}"
            mc "{i}But the singer leaves much to be desired. And pretty much blows.{/i}"
            scene 7train51 with dissolve
            "You took the headphones and gave it some thought."
            mc "{i}I didn't think that these newcomers would have such a different music quality.{/i}"
            mc "{i}However, I probably shouldn't jump to conclusions. I need to hear them again.{/i}"
            scene 7train50 with dissolve
            "..."
            scene black with fade
            "Some time later."
            scene 7train52 with dissolve
            mc "Okay, if you want my opinion, we're way ahead of these guys."
            mc "It's kind of weird that your buddy asked them to perform."
            scene 7train53 with dissolve
            j "Phew! I thought I was the only one who thought that!"
            mc "No, man, you're not."
            mc "But that doesn't mean we don't have to rehearse."
            j "Of course!"
            j "You should always be ready for anything. You always have to be the best."
            scene 7train54 with dissolve
            mc "{i}Yep... You always have to be the best.{/i}"
            "..."
            stop music fadeout 3.0
            mc "{i}Okay, maybe I should talk to the girls.{/i}"
            jump day07_menu01

        "Talk to Lisa" if day07_q02 == False:
            play music "music/10 - Street's.ogg"
            $ day07_q02 = True
            mc "{i}I think I should keep Lisa company.{/i}"
            mc "{i}It's better to play together, not alone.{/i}"
            scene 7train27 with dissolve
            "When you got closer, you knew you were just in time."
            mc "{i}Ooh... I'm already anticipating an epic game.{/i}"
            mc "Lisa."
            scene 7train27a with dissolve
            ls "Mmm... [mc]? Do you want something?"
            mc "Yeah, something like that."
            scene 7train28 with dissolve
            mc "I haven't played pool in a thousand years. Do you mind if I join?"
            ls "Interesting offer. Why not?"
            if lisa_path == True:
                ls "If you want to play, then how about a wager, and the loser does what the winner asks?"
                mc "{i}Did she just make me a wager?{/i}"
                scene 7train29 with dissolve
                mc "Someone seems very confident today."
                ls "Heh. For your information, I'm pretty good at this game!"
                mc "{i}In that case, it'll be interesting.{/i}"
                scene 7train30 with dissolve
                ls "You know, if you're scared, you should just say no. I would understand."
                mc "Are you trying to intimidate me? Very interesting."
                mc "I agree."
                ls "Hehe. That's great!"
            else:
                scene 7train29 with dissolve
                ls "I'll start first"
                mc "I don't see why not."
                scene 7train30 with dissolve
                ls "Mmm... I can hear the condescension in your voice."
                ls "For your information, I'm pretty good at this game!"
                mc "Heh. Then it'll be interesting."
                ls "Certainly."

            scene 7train31 with dissolve
            "Lisa put the cue to the table and prepared to strike."
            ls "Just don't cry when you lose..."
            mc "Haha. Well now, those are fighting words!"
            "While the girl was focusing on the game, you didn't miss the opportunity to study her a little closer."
            scene 7train32 with dissolve
            mc "{i}Hmm... She looks really pretty in that outfit.{/i}"
            if lisa_path == True:
                mc "{i}Although... I'd rather see her naked.{/i}"
            else:
                mc "{i}Okay, better not stare at her so hard, or she might notice.{/i}"
            scene 7train33 with dissolve
            "Meanwhile, Lisa took her first shot."
            scene 7train33a with dissolve
            "..."
            scene 7train33b with dissolve
            "All the balls immediately scattered on the table..."
            scene 7train34 with dissolve
            "..and only red slowly rolled into the hole."
            scene 7train34a with dissolve
            "..."
            ls "Hehe. That's it!"
            mc "Not bad. Not bad."
            mc "What's next?"
            scene 7train35 with dissolve
            ls "And now the next strike..."
            mc "{i}Hmm... I should note that she is clearly not a beginner.{/i}"
            mc "{i}However, she's no professional.{/i}"
            "The girl took aim and struck the side of the yellow ball..."
            scene 7train36 with dissolve
            "Unfortunately for her, it stopped just a few millimeters from the border of the nearest hole."
            scene 7train36a with dissolve
            mc "Looks like you're out of luck this time."
            ls "..."
            mc "{i}Ummm... I hope she didn't think I was gloating.{/i}"
            mc "{i}Although... Looks like Lisa's anger isn't directed at me right now.{/i}"
            scene 7train37 with dissolve
            "The girl stood with the cue clamped in her hands and angrily stared down the white ball."
            mc "You know, you look like you're trying to kill that ball with your eyes."
            ls "Even if I'm trying, it isn't working..."
            mc "Well, I'm sure if he had legs, he'd have run away by now."
            scene 7train38 with dissolve
            ls "Don't laugh at me. I'm very angry right now."
            mc "Yeah, it's hard not to see that with your pouty expression."
            "..."
            scene 7train38a with dissolve
            "The angry expression on Lisa suddenly disappeared, replaced by a sweet smile."
            ls "Oh come on!"
            mc "I like you better when you're having fun."
            scene 7train38b with dissolve
            ls "Come on... Now it's your turn."
            mc "{i}Really.{/i}"
            scene 7train39 with dissolve
            "You took a stance and took steady aim."
            if lisa_path == True:
                mc "{i}I think I can win it now. Especially if I play with determination.{/i}"
                mc "{i}On the other hand, this game is important to her for some reason... Maybe I should give her a win. Maybe it'll make her happy.{/i}"
                mc "{i}So the choice is mine. What should I do?{/i}"
                menu:
                    "Let her win":
                        $ RPls += 1
                        mc "{i}It's just a game... If it makes her feel better to win, I'm not averse to losing.{/i}"
                        "You hit the ball and missed... Game on."
                        scene black with fade
                        "Few minutes later."
                        scene 7train40 with dissolve
                        ls "Hooray! I won! I'm awesome!"
                        mc "Yeah, yeah, you're awesome... Congratulations."
                        ls "Hee hee. Don't worry, maybe next time you'll have enough skill to defeat me."
                        mc "..."
                        scene 7train40b with dissolve
                        ls "So now, about that wager..."
                        mc "I'm listening."
                        ls "Hmm... Let me think..."
                        ls "How about a kiss?"
                        mc "Huh? Just a kiss?"
                        ls "Yep."
                        mc "With pleasure!"
                        scene 7train43 with dissolve
                        "You went to Lisa and put your arm around her shoulder."
                        mc "You know, I was gonna ask for that when I won."
                        ls "So we're thinking in the same direction... Then you shouldn't have let me win."
                        mc "{i}How did she know that?{/i}"
                        scene 7train44 with dissolve
                        "Before you could say anything else, Lisa kissed you."
                        ls "Mmmm..."
                        mc "{i}Yeah, it was definitely worth it.{/i}"
                        scene 7train45 with dissolve
                        "Your hands slid down the girl's waist..."
                        scene 7train46 with dissolve
                        ls "Hey-Hey! We'd better stop here, we're not alone."
                        mc "{i}She's right. I got carried away.{/i}"
                        mc "Yeah."
                        scene black with fade
                        "Soon you ended the conversation with Lisa."
                        mc "{i}Okay, maybe I should talk to the other guys.{/i}"

                    "{color=#66FF33}Play seriously":
                        mc "{i}She got me pretty excited. I'm going to play seriously.{/i}"
                        "You hit the ball and hit the hole... Game on."
                        scene black with fade
                        "Few minutes later."
                        scene 7train40a with dissolve
                        ls "Ummm... Congratulations, you've won."
                        mc "Don't worry, you played very, very well."
                        ls "Yeah, I guess you're right."
                        "..."
                        ls "So, what are you gonna have me do?"
                        mc "{i}I don't think I need to get too cocky... It's best to ask for something simple.{/i}"
                        mc "Hmm... How about..."
                        menu:
                            "Kiss":
                                $ RPls += 2
                                mc "My wish is to receive a kiss from the beauty that stands before me."
                                scene 7train40b with dissolve
                                ls "Really?"
                                mc "Yep."
                                ls "You probably won't believe me, but that's what I was gonna ask for!"
                                ls "So we're thinking in the same direction..."
                                scene 7train43 with dissolve
                                "You walked up to Lisa, put your arm around her shoulder."
                                mc "I think that's great."
                                ls "Yeah."
                                scene 7train44 with dissolve
                                "The next moment you kissed."
                                ls "Mmmm..."
                                mc "{i}Yeah, it was definitely worth it.{/i}"
                                scene 7train45 with dissolve
                                "Your hands slid down the girl's waist..."
                                scene 7train46 with dissolve
                                ls "Hey-Hey! We'd better stop here, we're not alone."
                                mc "{i}She's right. I got carried away.{/i}"
                                mc "Heh. You got lucky this time."
                                ls "Hee hee."

                            "{color=#66FF33}Hot photo":
                                $ RPls += 2
                                $ day07_photo01 = True
                                mc "How about you take some hot photos and send them to me?"
                                scene 7train41 with dissolve
                                ls "Are you serious?"
                                mc "Yes, I'm serious."
                                ls "But I can't do it right here and now."
                                mc "And no one's telling you to do it now."
                                mc "Send it when you can."
                                scene 7train40b with dissolve
                                ls "You're a pervert, Mr. [mc]!"
                                mc "Heh. Trying my best."
                                scene 7train46 with dissolve
                                ls "Okay, I get it. A wager is wager."
                                ls "Wait for the photo tonight."
                                mc "Deal."

                            "Nothing":
                                mc "You're lucky today, I forgive your debt."
                                scene 7train41 with dissolve
                                ls "Oh... I wasn't expecting that..."
                                ls "Thanks anyway."
                                mc "Don't mention it."

                        scene black with fade
                        "Soon you ended the conversation with Lisa."
                        stop music fadeout 3.0
                        mc "{i}Okay, maybe I should talk to the other guys.{/i}"
            else:
                mc "{i}I think I'm quite capable of winning.{/i}"
                mc "{i}Okay, let's see what she can do.{/i}"
                scene black with fade
                "A few minutes later."
                scene 7train40a with dissolve
                ls "Ummm... Congratulations, you've won."
                mc "Don't worry, you played very, very well."
                ls "Yeah, I guess you're right."
                scene 7train41 with dissolve
                ls "But you know, it's not over."
                ls "I'll take revenge someday! You'll see."
                mc "Heh. I look forward to it."
                scene black with fade
                "Soon you ended the conversation with Lisa."
                stop music fadeout 3.0
                mc "{i}Okay, maybe I should talk to the other guys.{/i}"

            jump day07_menu01


        "Talk to Jade" if day07_q03 == False:
            $ day07_q03 = True
            mc "{i}I think this is a great chance to have a little chat with Jade.{/i}"
            mc "{i}We're in the same band, but we don't know much about each other. It's time to fix that.{/i}"
            scene 7train21 with dissolve
            play music "music/13 - Hope is Still Living.ogg"
            "You went outside, and a cold wind met your face."
            mc "{i}We've been in there for a bit... It's getting dark outside.{/i}"
            mc "{i}Okay, where's that uncommunicative guitarist?{/i}"
            scene 7train22 with dissolve
            "Twisting your head around, you almost immediately noticed who you were looking for."
            mc "{i}Looks like she came out for a smoke.{/i}"
            "..."
            mc "{i}Hell, I don't know why, but in this entourage, she looks like the hero of some lyrical novel.{/i}"
            scene 7train23 with dissolve
            "A second later, Jade saw you and nodded gently, as if inviting you."
            mc "{i}Well, I won't say no.{/i}"
            scene 7train24 with dissolve
            mc "Enjoying a nice evening?"
            jd "Just Smoking."
            mc "I see... Do you mind if I stand here for a while?"
            jd "Feel free to join."
            scene 7train25 with dissolve
            "..."
            scene 7train25a with dissolve
            mc "You know, I just realized that you and I barely know each other."
            mc "How about we fix that?"
            jd "..."
            jd "If that's what you want, fine."
            mc "Don't get me wrong, I just wanted to ask you a few questions so I could understand you better."
            jd "Okay, I don't mind."
            jd "What do you want to know about me?"
            mc "Hmm..."
            scene 7train26 with dissolve
            mc "This isn't your first band, is it?"
            jd "It's not."
            mc "What went wrong before, if you're with us now?"
            scene 7train26a with dissolve
            jd "..."
            scene 7train26 with dissolve
            jd "It's hard to say."
            jd "I guess we were too different."
            jd "Someone was engaged in music for the sake of music, and someone else for entirely other reasons."
            scene 7train25a with dissolve
            mc "Really..."
            mc "{i}I'm not sure I can do much more than that, though...{/i}"
            mc "And what do you think of our band?"
            scene 7train26a with dissolve
            jd "It's different."
            scene 7train26 with dissolve
            jd "But I like it."
            mc "Huh... Good to hear."
            scene 7train25 with dissolve
            mc "Okay, I think we should get back."
            jd "You go, I'll come later."
            mc "Whatever you say."
            stop music fadeout 3.0
            jump day07_menu01

    scene black with fade
    "Soon you returned to rehearsal."
    "After a while, you went home."
    jump day07_home

label day07_home:
    scene 7city03 with dissolve
    play music "music/2 - Bad.ogg"
    "When you made your way near home, the street was getting quite dark."
    mc "{i}I hope Emma took my advice and moved out. Otherwise...{/i}"
    mc "{i}Better not think about it.{/i}"
    scene black with fade
    "When you entered the apartment, the first thing you did was check out the living room, only to find..."
    scene 7phone01 with dissolve
    "Nobody."
    "..."
    mc "{i}So... She left.{/i}"
    if emma_sex == True:
        mc "{i}To be honest, I'm a little sad about it.{/i}"
        mc "{i}Ugh... What a stupid thought!{/i}"
    else:
        mc "{i}That's great!{/i}"
    scene 7phone02 with dissolve
    "Upon closer inspection, you noticed a small notebook on the table with something written on it."
    mc "{i}What's this?..{/i}"
    scene 7phone03 with dissolve
    "You sat on the couch, took the notebook and started reading it."
    em "{i}Hello [mc].{/i}"
    em "{i}I'm sorry I chose such an odd way to say goodbye... But you know me, I have my quirks.{/i}"
    em "{i}Most likely, when you read this, I'll have already packed my things and left. But I wanted to thank you again for letting me stay.{/i}"
    if emma_sex == True:
        em "{i}And for the night we spent together. It was really nice.{/i}"
    else:
        em "{i}And for enduring my strange behavior.{/i}"
    em "{i}Ummm... I do not want to delay this tedious writing, so I will be brief.{/i}"
    em "{i}I was lucky and found a good place to stay. Now I'm going to stay with my friend for a while. So things are getting better.{/i}"
    em "{i}Oh yeah!{/i}"
    em "{i}You can swear at me, but I thought I'd stop by for your first gig. I just can't not do it! It's all very intriguing.{/i}"
    em "{i}Moreover, you yourself told me when and where it will be.{/i}"
    em "{i}Well, that's all for sure... I wish you luck.{/i}"
    em "{i}Kisses, Emma.{/i}"
    "..."
    mc "{i}Yeah...{/i}"
    stop music fadeout 3.0
    scene black with fade
    "At the same time, on the other side of town."
    scene 7sister01 with dissolve
    play music "music/7 - Just Happy.ogg"
    sis "{i}Aahhh... It's good to finally be in a warm bath...{/i}"
    sis "{i}After all the work fuss, this is definitely the best moment of the day.{/i}"
    sis "{i}I'd like some...{/i}"
    scene 7sister03 with dissolve
    "Julia opened her eyes and turned her head to the right."
    sis "{i}Yes.{/i}"
    sis "{i}What's missing is a glass of good wine.{/i}"
    scene 7sister04 with dissolve
    "She slowly took the glass in hand and swirled it in the air."
    sis "Mmm..."
    sis "{i}Bringing wine here was definitely a good idea.{/i}"
    scene 7sister05 with dissolve
    "..."
    "Julia drank some wine and put the glass back."
    scene 7sister02 with dissolve
    sis "{i}That's so good...{/i}"
    sis "{i}Now, I think I might call someone and have a chat, or I'm gonna fall asleep here.{/i}"
    scene 7sister07 with dissolve
    "The girl lazily turned around, and reached for the phone."
    sis "{i}It's so far away...{/i}"
    scene 7sister06 with dissolve
    "..."
    scene 7sister11 with dissolve
    sis "So... Who should I call?"
    "..."
    sis "Why don't I call my little brother first."
    scene black with fade
    "At the same time."
    scene 7phone03 with dissolve
    mc "{i}Yeah...{/i}"
    scene 7phone04 with dissolve
    "The phone on the table suddenly rang."
    scene 7phone04a with dissolve
    "BIP-BIP!!!"
    mc "{i}Julia?{/i}"
    mc "{i}I wonder what she wants.{/i}"
    scene 7phone05 with dissolve
    mc "Hello."
    sis "Hello, [mc]"
    sis "I wanted to know how you were after last night."
    mc "After last night?"
    mc "Um... Actually quite good. Maybe even better. What about you?"
    scene 7sister08 with dissolve
    sis "Me?"
    sis "Well, aside from all the clutter at work, not bad."
    mc "Heh, glad to hear that."

    if jane_path == True and RPjn >= 8 and jane_massage == True:
        scene 7phone06 with dissolve
        mc "And Jane? Did you see her today?"
        sis "Thanks for the reminder. Somehow she seemed different today..."
        mc "How's that?"
        sis "I don't know... I just haven't seen her in such good spirits in such a long time."
        mc "{i}Damn, is that all because of me? How nice to hear that.{/i}"
        mc "Is it any wonder? Yesterday you closed a big business deal."
        scene 7sister10 with dissolve
        sis "That may be so, but I'm not sure it has anything to do with work."
        sis "And whatever happened was after I left you two last night..."
        sis "Tell me what you did to my friend."
        scene 7phone05 with dissolve
        mc "I didn't do anything to her! Really!"
        mc "We had a little chat, then went home."
        sis "Okay. If you don't want to tell me the truth, I'll find out in time..."
        mc "{i}Man, I don't like where this is going...{/i}"
        mc "{i}And I don't think Jane would be thrilled if Julia found out.{/i}"
        mc "{i}Although, to be honest, I'm not sure about anything right now.{/i}"
        scene 7phone06 with dissolve
    else:
        scene 7phone06 with dissolve
        mc "What about Jane?"
        sis "Well, as far as I know, she's fine. We've been working together all day..."
        sis "Mmm... Probably in a hot bath right now, too."
        mc "Hey, are you in the tub right now?"
        scene 7sister10 with dissolve
        sis "Ehh... Forget it! I didn't tell you that."
        mc "Huh! Whatever you say."
        mc "I forgot."
        sis "Well done."
        scene 7phone05 with dissolve

    mc "By the way, since you called, I wanted to tell you something important."
    mc "This Saturday my band will be performing in a nightclub."
    scene 7sister09 with dissolve
    sis "Wow! That's really big news."
    mc "Yep. So if you have time, be sure to drop by. I'll text you the address."
    sis "It won't be easy, but I'll definitely find a way to free myself for that evening."
    mc "That's great!"
    scene 7phone05 with dissolve
    mc "Oh... And I warn you, there's gonna be a lot of newbies, so be prepared for some terrible music too. All groups will perform three songs."
    scene 7sister08 with dissolve
    sis "Well, in any case the main thing is it's a start!"
    mc "That's true."
    sis "See you Saturday then, [mc]."
    mc "Yeah, see you there."
    scene 7sister11 with dissolve
    sis "{i}Who would have thought, the first performance...{/i}"
    sis "{i}Well done brother.{/i}"
    if day07_photo01 == True:
        scene 7phone04 with dissolve
        "Just as you were on the phone with Julia, the phone rang with a new text."
        mc "{i}I'm in great demand today.{/i}"
        scene 7phone07 with dissolve
        mc "{i}Let's see what we got...{/i}"
        mc "{i}A photo with a message from Lisa?{/i}"
        mc "{i}Oh yeah! She lost that wager.{/i}"
        mc "{i}I'm so excited...{/i}"
        "You opened the photo and went full screen."
        scene 7photo01 with dissolve
        ls "I hope you like it, perv."
        mc "{i}After that message, I need to respond.{/i}"
        mc "Oh, yeah, I loved it."
        mc "I'm kind of sorry I'm not with you right now..."
        scene 7photo02 with dissolve
        "Lisa sent a new photo."
        ls "I'm kind of sorry, too..."
        ls "I think after our show, we'll have a good chance to be together."
        mc "Can't wait."
        scene 7photo03 with dissolve
        ls "Goodnight, [mc]."
        mc "Goodnight, Lisa."
        scene 7phone04 with dissolve
        "..."
        mc "{i}Well... That's it for now.{/i}"
        mc "{i}And maybe Lisa's right, it's time to go to bed.{/i}"

    else:
        scene 7phone04 with dissolve
        mc "{i}That's it for now.{/i}"
        mc "{i}And now it's time to go to sleep.{/i}"

    stop music fadeout 3.0
    scene 7city03 with fade
    "Night came."
    scene black with fade
    "There was a new day ahead of you."
    jump day07_club


label day07_club:
    scene 7city01 with fade
    "Next day."
    scene 7newclub01 with dissolve
    play music "music/10 - Street's.ogg"
    "The first thing you planned for today was to go with Jacob to club Purple Orchid."
    "You've never heard of this club before, but Jacob convinced you it was pretty good."
    scene 7newclub02 with dissolve
    mc "Well, is there anything more specific you can tell me about this club?"
    j "What else is there to say? Club as in a club."
    j "Not too cool, not too creepy... Quite ordinary."
    j "You'll see for yourself."
    mc "{i}Okay, I guess all I can do is hope for the best.{/i}"
    scene 7newclub03 with dissolve
    j "Here we are."
    mc "Umm..... Why don't we go in the front?"
    j "To tell you the truth, I don't know why, but Oliver told me to come here."
    mc "{i}As far as I can tell, Oliver is the friend who gave us the gig.{/i}"
    mc "{i}It'll be interesting to meet him.{/i}"
    scene 7newclub04 with dissolve
    j "Well? Ring the doorbell?"
    mc "Yeah, sure."
    mc "The sooner we deal with this, the better."
    scene black with fade
    "As soon as you rang the bell, the door opened immediately..."
    scene 7newclub05 with dissolve
    "{color=#FFA07A}Oliver{/color}" "Well, well! Look who it is! It's Jacob... Long time no see, man."
    j "Hey, pal. I'm glad you called us."
    "{color=#FFA07A}Oliver{/color}" "Well, after your video, I just had to."
    scene 7newclub06 with dissolve
    "{color=#FFA07A}Oliver{/color}" "And this, I believe, is your friend [mc]."
    mc "It's nice to meet you."
    "{color=#FFA07A}Oliver{/color}" "The pleasure is mine."
    scene 7newclub05a with dissolve
    "{color=#FFA07A}Oliver{/color}" "Okay, guys, we're all busy people here, so let's get down to business. Come inside."
    scene 7newclub07 with dissolve
    "You followed Oliver."
    "{color=#FFA07A}Oliver{/color}" "So, as I told Jacob, we'll pay you for your performance, but not much."
    "{color=#FFA07A}Oliver{/color}" "You have to understand, you are beginners and the performance will only be two-three songs."
    "{color=#FFA07A}Oliver{/color}" "And if all goes well, It might be possible to set you up with a few more gigs."
    scene 7newclub08 with dissolve
    "Oliver opened the door to the main hall and gestured an invitation."
    "{color=#FFA07A}Oliver{/color}" "If you're interested, come and look around."
    mc "Yeah, that sounds good."
    scene 7newclub09 with dissolve
    "You walked forward and your eyes immediately fell on a small stage."
    mc "{i}Hmm... For such a small club, it looks pretty dignified.{/i}"
    mc "{i}I can easily imagine [band_name] here.{/i}"
    mc "{i}Yes... This place is perfect for us.{/i}"
    scene 7newclub10 with dissolve
    "While you gazed thoughtfully at the scene, Jacob was engaged in a discussing organizational matters."
    "..."
    mc "{i}Okay, stop dreaming already. Time to get busy.{/i}"
    scene 7newclub11 with dissolve
    j "Oh, [mc] you're just in time."
    j "To sum it up, it's Saturday night, and if we don't mess up, we'll get paid."
    j "I'll tell you the rest of the details later."
    mc "Okay."
    scene 7newclub12 with dissolve
    "{color=#FFA07A}Oliver{/color}" "[mc] I see you've looked around... So, what do you say?"
    mc "It's pretty good. I like it."
    "{color=#FFA07A}Oliver{/color}" "That's great!"
    "{color=#FFA07A}Oliver{/color}" "In that case, I think we have an agreement."
    scene 7newclub13 with dissolve
    "You shook hands and said goodbye."
    scene 7newclub14 with dissolve
    "Discussing different nuances of preparation, you and Jacob left the club."
    j "As you can see, it's not as bad as it might have seemed."
    mc "Yes, perhaps, if we try, everything will go very well."
    j "That's what I'm talking about."
    scene 7newclub15 with dissolve
    j "And of course, you and I need to appear confident to set an example for the girls. Lisa and Jade don't have to worry about that."
    mc "I know. Everything will be fine."
    j "Well, that's all right then."
    j "Come on, we have a lot to do today."
    stop music fadeout 3.0
    scene black with fade
    "Few hours later."
    jump day07_selina_meeting


label day07_selina_meeting:
    scene 7city02 with dissolve
    "Evening. After rehearsal."
    scene 7selina01 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    "Everyone called it a little early today."
    "Not because someone didn't want to rehearse anymore or was busy, but because you didn't want to burn out."
    "It happens when you do one thing for too long without a break. And that could make things go wrong."
    "On this occasion, you decided to leave early and have a little rest."
    scene 7selina02 with dissolve
    "Just outside your home, you noticed Selina."
    mc "{i}I think she's so glued to the phone right now, she didn't even notice me.{/i}"
    mc "{i}Hmm... Maybe we should have a little chat? Or should I go home and go to bed early?{/i}"
    scene 7selina03 with dissolve
    mc "{i}What should I do?{/i}"
    menu:
        "{color=#66FF33}Talk to Selina":
            mc "{i}I don't see any reason not to talk to the red-haired beast.{/i}"
            mc "{i}Besides, I haven't seen her in a while.{/i}"
            scene 7selina05 with dissolve
            mc "You know when you're on the phone, sometimes you should look up?"
            s "Oh... [mc]. What a meeting."
            mc "Yeah."
            mc "Good to see you."
            s "Yeah, me too. And I'll try to heed your advice."
            scene 7selina07a with dissolve
            s "You know... You could text me more often."
            s "I feel like we haven't seen each other for ages."
            mc "Ha ha! I'm sorry, it's my fault."
            mc "There's been a lot going on lately..."
            scene 7selina07 with dissolve
            s "I totally understand... I've been having a lot of trouble at work myself lately."
            s "The crowds of patients, arrogant colleagues, and a completely insane schedule."
            s "Can you imagine?"
            scene 7selina06 with dissolve
            mc "And when was the last time you relaxed?"
            s "When was the last time we met?"
            mc "Wow..."
            s "Yeah, imagine."
            "..."
            scene 7selina07 with dissolve
            mc "Anyway, it's good to see you, and I won't keep you any longer."
            mc "Good luck."
            scene 7selina08 with dissolve
            if selina_sex_day05 == True:
                s "You know... If you want, you can drop by my place in half an hour, and we can relax together."
                s "I think it would be good for both of us right now."
                mc "Very tempting offer."
                s "Oh yeah, it is."
                stop music fadeout 3.0
                scene black with fade
                "Having said all that she wanted, Selina headed towards her apartment."
                mc "{i}Hmm... So I have to be there in half an hour?{/i}"
                mc "{i}I'm in!{/i}"
                jump day07_selina_sex
            else:
                s "Well, have a good evening, [mc]."
                mc "Yeah, you too."
                stop music fadeout 3.0
                scene black with fade
                "You finished talking to Selina and went home."
                jump day07_concert


        "Go home":
            mc "{i}I'm too tired for idle chatter.{/i}"
            mc "{i}I'd better go home and rest.{/i}"
            scene 7selina04 with dissolve
            "Trying not to attract too much attention, you head to the apartment."
            stop music fadeout 3.0
            mc "{i}...{/i}"
            jump day07_concert


label day07_selina_sex:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    if lisa_path == True:
        $ cheat_point += 5
    $ selina_path = True
    scene 7selina09 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "Like Selina said, be there in half an hour."
    "That's enough time for you to get cleaned up and take a shower."
    mc "{i}Ooh... Only now do I realized how much I missed that redhead.{/i}"
    mc "{i}Okay, it's time to fix that.{/i}"
    scene black with fade
    "You rang the bell and waited."
    scene 7selina09 with dissolve
    s "It's open!"
    "Her voice sounded like it was coming from another room."
    mc "{i}That's interesting.{/i}"
    scene 7selina10 with dissolve
    "You went inside and looked around."
    mc "{i}Okay, that's not how I pictured things.{/i}"
    s "I'm in the bedroom, come here."
    mc "{i}I take it back, that's exactly how I imagined it.{/i}"
    scene 7selina11 with dissolve
    "You walked down the hall and made your way into the bedroom."
    mc "{i}Heh. What a pleasant surprise.{/i}"
    mc "Well, Hello again."
    scene 7selina12 with dissolve
    "Selina began to turn slowly in your direction."
    mc "{i}And what pretty lingerie she's wearing.{/i}"
    scene 7selina13 with dissolve
    s "Ahhh... You weren't in too much of a hurry."
    mc "I think I came just in time."
    s "Mmmm... You're very confident."
    scene 7selina14 with dissolve
    s "I like it."
    mc "{i}I never doubted that.{/i}"
    scene 7selina15 with dissolve
    "The girl slowly sat on the bed and stared at you."
    "..."
    s "Okay, strip."
    mc "Whoa, just like that, right to the point?"
    scene 7selina24 with dissolve
    s "I already told you, I just need to get fucked right now."
    s "So, will you do me that favor?"
    s "Or do you want us to have a chat, a cup of tea and a game of chess?"
    scene 7selina16 with dissolve
    "At the same time, Selina stood up and began to take off her panties."
    mc "Ha! You know just how to press the right buttons."
    s "Yeah, call me anytime."
    scene 7selina17 with dissolve
    "..."
    mc "{i}I'm so glad to see that tight ass again.{/i}"
    scene 7selina18 with dissolve
    "Soon the red panties were on the floor, opening a view for an even more attractive sight.."
    mc "{i}Oh yeah... Every second is better and better.{/i}"
    scene 7selina19 with dissolve
    "Selina flopped down on the bed spreading her graceful legs to the sides."
    s "Hehe. I hope you have a lot of energy today, because I'm going to squeeze you dry."
    mc "{i}We'll see which one of us gets dry here.{/i}"
    scene 7selina20 with dissolve
    "Lowering your eyes, you were able to see the girl's pussy in all its glory."
    s "Hey! Don't sleep!"
    scene 7selina21 with dissolve
    "The next moment, the underwear that was hanging on her leg was flying straight at you."
    mc "{i}What an asshole!{/i}"
    scene 7selina22 with dissolve
    "Easily snatching them from the air, you smiled indulgently."
    mc "You think you're funny, huh?"
    scene 7selina24 with dissolve
    s "Oh yeah, I thought so!"
    "You could tell she was teasing."
    mc "{i}Well, in that case, now is the time to act.{/i}"
    scene 7selina23 with dissolve
    "You took off your shirt and approached that red-haired devil."
    s "Mmmm... Finally."
    stop music fadeout 3.0
    scene 7selina25 with dissolve
    "A few seconds later, you and Selina were lying in the middle of the bed, kissing."
    play music "music/15 - Deep Mood.ogg"
    s "Mmmm..."
    mc "{i}I'd better take my time and warm this horny girl up first.{/i}"
    scene 7selina26 with dissolve
    "Your right hand touched Selina's tummy and gently began to slide down."
    mc "{i}And a little lower...{/i}"
    s "Mmmm..."
    scene 7selina26a with dissolve
    "...until it was inside her wet pussy."
    s "Aahhhh.... Aahhhh...."
    show anim35
    "Taking advantage of the girls temporary confusion, your fingers began to fuck her."
    s "Aaaahhhh.... Haaah... Hhhaaaaa..."
    "Not forgetting to kiss Selina, you gradually began to increase the speed of your movements."
    s "Mmmm...."
    s "Yes, [mc]... A little more... Just a little more!"
    "You noticed that the girl's body began to squirm in time with your movements."
    stop sound fadeout 3.0
    scene 7selina27 with flash
    "Selina's pussy clenched, and she let out a long moan."
    s "Oooohhhh!!! Yeah!!!!"
    mc "{i}Whoa! Did she cum already?{/i}"
    scene 7selina28 with dissolve
    "Your partner's heavy breathing broke through the silence."
    s "Haaah... Haaah... Haaah..."
    s "It was... Amazing..."
    scene 7selina29 with dissolve
    mc "I didn't think I could make you cum so fast."
    s "I've told you I've been like this since we last met..."
    mc "{i}Well, in that case, it's not so surprising.{/i}"
    scene 7selina30 with dissolve
    s "You don't think that's all? Do you?"
    s "We're just getting started."
    mc "{i}Looks like she's already plotting something...{/i}"
    mc "{i}However, I can let her take the initiative, or I can be in charge.{/i}"
    mc "{i}I think she'll be satisfied with both options.{/i}"
    menu:
        "Let Selina lead":
            mc "Oh, yeah, you're right, we're just getting started."
            mc "And it seems to me that you already have an idea on how we should continue this?"
            s "Hee hee. You have no idea how many different ideas I have."
            s "But I think we should only try a couple of them this time."
            scene 7selinanice01 with dissolve
            "Selina leapt up from the bed."
            s "Now, you have exactly three seconds to take your pants off, otherwise I'm putting my clothes back on."
            mc "{i}I'd like to know what she means by that, but... I'll try to play along.{/i}"
            "Without saying a word, you dropped your pants on the floor."
            scene 7selinanice02 with dissolve
            mc "Okay... What will you do with me next?"
            s "What I will do next is..."
            scene 7selinanice03 with dissolve
            "Selina grinned and threw you on the bed."
            s "Next I'll take care of you!"
            s "Just be nice."
            scene 7selinanice04 with dissolve
            mc "Ha ha! Not bad!"
            mc "I like your perseverance."
            scene 7selinanice05 with dissolve
            s "Mmmm... I'm sure you like a lot of things about me."
            s "Get ready, because tonight will be an evening of ecstasy."
            mc "{i}Oh, yeah, she definitely likes to feel in charge.{/i}"
            scene 7selinanice06 with dissolve
            "You lowered your gaze."
            s "Hehe. I think your cock is ready."
            mc "He's been ready since I walked in the door."
            s "Oh... Then let's not keep him waiting any longer."
            scene 7selinanice07 with dissolve
            "Selina rose a little higher, and then..."
            scene 7selinanice07a with dissolve
            "...one precise movement, she fell on your cock."
            scene 7selinanice08 with dissolve
            s "Oh yeah... That's exactly what I needed."
            mc "{i}Mmmm... I can't disagree with that.{/i}"
            mc "{i}Her pussy is so hot...{/i}"
            scene 7selinanice09 with dissolve
            "The girl's hips began to move slowly."
            s "Aaaahhhh.... Aahhhh..... Aaahhh..."
            mc "Yeah, baby, like that... Very good...."
            scene 7selinanice11 with dissolve
            "Looking at the tits bouncing up and down, your hands begin to reach for them."
            mc "{i}The real crime would be to not touch them.{/i}"
            scene 7selinanice11a with dissolve
            s "Aaahhhh... Mmmm..."
            mc "{i}Damn, they look so huge from here... And so soft.{/i}"
            scene 7selinanice10a with dissolve
            mc "Ohh!... What are you doing?"
            s "I want to pick up the pace a little..."
            s "Do you mind?"
            mc "Of course not."
            scene 7selinanice10 with dissolve
            "A couple seconds later, Selina is already in full force jumping on your dick."
            s "Aaahhh.. Yeah... Yeah!! Yeah!!!"
            show anim27
            s "Well.... Ahhh... Do you like it?"
            mc "Baby, you're just amazing...."
            s "Aaahhh.. Aahhh... Yeah... I like it when you praise me."
            s "Praise me more!"
            mc "{i}I think the depraved beast's lost her mind.{/i}"
            mc "{i}But why not?{/i}"
            show anim28
            mc "Aaahhhh... You're a real goddess!"
            s "Yeah... I'm the best!"
            mc "{i}Ohhh, mmm... Her pussy squeezes my cock so tight...{/i}"
            mc "{i}It feels so good...{/i}"
            s "Damn... Your cock is so fat!"
            s "Aaahhh... I think I could ride like this forever! Aaahhh..."
            scene 7selinanice13 with flash
            s "Yeeeesss... Yeeeeeesssss!!!!"
            "Selena's body went weak and her movements slowed down."
            stop sound fadeout 3.0
            scene 7selinanice13a with dissolve
            s "Haaahh... Haaahh... Haaah..."
            mc "Hey, why did you stop?"
            scene 7selinanice14 with dissolve
            s "Haaah... Haaah... Haaahh..."
            s "Sorry, I need to catch my breath..."
            mc "Nope! Someone promised me a lot of fun!"
            "..."
            mc "{i}Looks like she needs a little help...{/i}"
            show anim36
            "You grabbed the girl by her ass and began to force her down."
            s "Aahhhh... [mc].... Aahhhh..."
            mc "Yeah, baby... Take that!"
            s "Mmmmm..."
            s "I can't... I just can't...."
            mc "Then come here."
            scene 7selinanice15 with dissolve
            "You had to kiss her to make her quiet for a while."
            s "Mmmm..."
            scene 7selinanice15a with dissolve
            "..."
            mc "{i}Ohh!... I think I'm about to cum...{/i}"
            scene 7selinanice16 with dissolve
            mc "A little more... Oh..."
            mc "A little more... And..."
            scene 7selinanice16a with flash
            mc "Ooohhh... Yeeeessss!"
            scene 7selinanice16b with flash
            "..."
            scene 7selinanice17 with dissolve
            s "Huh... You're finally done."
            s "You have a lot of stamina..."
            mc "Yeah... But it was fucking awesome."
            scene 7selinanice18 with dissolve
            "Selina pressed her hot body against you."
            s "Mmmm... Now do you see how much I've missed you?"
            mc "Yeah."
            mc "But, you know, if it makes these moments so pleasurable, I'm willing to let you miss me for awhile."
            scene 7selinanice19 with dissolve
            s "Don't, just don't joke about it."
            "..."
            mc "Sorry, I won't do it again."
            s "Good to hear."
            scene black with fade
            "Few seconds later."

        "Take control of the situation":
            mc "Oh, yeah, you're right, we're just getting started."
            mc "Now turn over onto your stomach."
            s "Ohh... What you up to?"
            mc "Just do what I say."
            s "Okay."
            scene 7selinabad01 with dissolve
            "You quickly pulled off your pants and ended up on top of Selina."
            s "Is it me or is your cock touching my ass right now?"
            mc "Well done, you got it right..."
            scene 7selinabad02 with dissolve
            s "Hey, what do you mean?"
            mc "{i}You'll know.{/i}"
            scene 7selinabad03 with dissolve
            "You pointed the head of your cock at Selina's ass."
            s "Hey! Hey, what are you doing?!"
            s "You're putting it in the wrong way!"
            scene 7selinabad03a with dissolve
            s "Ow!!!"
            scene 7selinabad03 with dissolve
            mc "{i}That's right.{/i}"
            scene 7selinabad03a with dissolve
            mc "{i}Let's start slowly so she doesn't get too hurt.{/i}"
            mc "{i}Besides, I doubt this is her first experience.{/i}"
            scene 7selinabad04 with dissolve
            s "Ahhhh.... Please be careful!"
            mc "I'll move as I please... You understand me?!"
            scene 7selinabad03 with dissolve
            s "Aaahhh..."
            scene 7selinabad03a with dissolve
            mc "I said, do you understand me?!"
            scene 7selinabad05 with dissolve
            "Selina's entire body sank onto the bed, and she closed her eyes."
            s "Aaahhh..."
            s "Yes... Yes, I understand..."
            scene 7selinabad05a with dissolve
            "..."
            mc "That's a good girl."
            mc "Now I'm going to start moving faster..."
            mc "{i}Ohhh... I have to be careful, I shouldn't go too far.{/i}"
            show anim37
            "Focusing on the moans of the girl, you started to pick up speed."
            s "Mmmmm... Your cock is so hot."
            mc "{i}Damn, she's squeezing my dick so tight... How cool!{/i}"
            s "Aaahhh! Aahhhh! Aaaahhh!"
            s "It's... So weird... But it is nice."
            s "Ohh... What a big dick you have."
            mc "Yeah, baby, take that!"
            scene 7selinabad06 with dissolve
            "Moving faster and faster, you noticed that Selina had already begun to get into it."
            s "Yeah... Yeah, baby.... Fuck me harder!"
            mc "{i}You want harder? I can arrange that!{/i}"
            scene 7selinabad06a with dissolve
            "With one abrupt movement you drove your cock balls deep into Selina's ass."
            s "AAAHHH!!!"
            s "..."
            s "Oh my God! Your cock is so deep.."
            mc "Okay, now get on your knees."
            s "But...?"
            mc "I said get up!"
            s "Aaahhh... Okay."
            scene 7selinabad07 with dissolve
            mc "{i}Time for another round.{/i}"
            show anim29
            s "Mmm...."
            s "Yeeeesss... Please don't stop!"
            s "Aaaahhhh.. More! I want more!!!"
            mc "{i}Jesus, her screams are so arousing.{/i}"
            s "Aaaahhhh... Aaaahhhhh... Aaaahhhh!!!"
            s "I love this!"
            scene 7selinabad08 with dissolve
            mc "Well, do you want more?!"
            s "Yes... Yes I do!"
            s "Fuck... Fuck me harder [mc]!"
            scene 7selinabad09 with dissolve
            "You put your arm around Selina's waist and lifted her up."
            mc "{i}She seems to know what I want from her.{/i}"
            scene 7selinabad10 with dissolve
            s "Aaahhh... Ahhhh... What are you waiting for?"
            s "Kiss me already!"
            mc "{i}I waited for her to say it.{/i}"
            scene 7selinabad11 with dissolve
            s "Mmm..."
            "Selina's tongue deftly caressed your lips while you fucked her ass."
            s "Aaaahhhh... Yess..."
            scene 7selinabad12 with dissolve
            "Your attention was drawn to the girl's tits bouncing up and down."
            scene 7selinabad12a with dissolve
            "Obeying a fleeting desire, your hand slipped over Selina's body and grabbed her breasts."
            s "Mmmm..."
            mc "{i}They are so soft... It's amazing!{/i}"
            scene 7selinabad13 with dissolve
            mc "{i}Ohhh... I think I'm at my limit.{/i}"
            mc "{i}I'm not gonna last that long.{/i}"
            mc "{i}Where should I cum?{/i}"
            menu:
                "Cum inside":
                    mc "{i}Aaahhh... I wanna cum inside!{/i}"
                    scene 7selinabad14 with flash
                    mc "{i}Ohh.... It feels good...{/i}"
                    scene 7selinabad14 with flash
                    "..."
                    scene 7selinabad15 with dissolve
                    mc "{i}Yeah... Very good.{/i}"
                "Cum outside":
                    mc "{i}Aaahhh... It's better if I cum on that pretty ass.{/i}"
                    scene 7selinabad16 with dissolve
                    "You pulled out your cock and could no longer hold out, and began to cum."
                    mc "{i}Aaaahhhh... Yeeeess!!!{/i}"
                    scene 7selinabad17 with flash
                    mc "{i}It's so good...{/i}"
                    scene 7selinabad18 with flash
                    "..."
                    mc "{i}Yeah... Very good.{/i}"

                    scene 7selina32 with dissolve
                    "..."
                    s "Wow... It's like I was born again..."
                    mc "Yes, I have the same feeling."
                    "..."

    scene 7selina33 with dissolve
    s "Well, it's time for the next round."
    mc "{i}Hell, it looks like she really decided to squeeze me dry.{/i}"
    mc "{i}Okay, let's see which one of us gets tired first.{/i}"
    mc "With pleasure."
    stop music fadeout 3.0
    scene black with fade
    "An hour later."
    scene 7selina31 with dissolve
    play music "music/1 - Atmosphere.ogg"
    s "Haah... Haah... Haah..."
    "Completely exhausted you lay on the bed and looked at the ceiling."
    s "Hey... Would you like something to drink?"
    mc "No, thanks... I'd better lie down for a while..."
    s "Huh. I understand that sentiment perfectly."

    $ renpy.end_replay()
    if not persistent.day07selina:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day07selina = True

    scene 7selina34 with dissolve
    "Looking around the room, you noted the presence of some very unusual paintings on the walls."
    scene 7selina34a with dissolve
    mc "{i}What curious things.{/i}"
    mc "{i}Hmm... Come to think of it, I have noticed paints, canvases and other devices for drawing scattered about the apartment.{/i}"
    mc "{i}And if Selina works at the hospital, where does all that come from?{/i}"
    scene 7selina33 with dissolve
    mc "Selina."
    s "Yes?"
    mc "Where did you get all these paintings? Someone you know into art?"
    scene 7selina35 with dissolve
    s "Oh, you mean those things on the walls?"
    mc "Yep."
    s "It's my mom."
    mc "Uh... Are you for real?"
    scene 7selina36 with dissolve
    s "Hey! Not in the sense that she is depicted on them, but in the fact that she painted them."
    s "My mother is a professional artist."
    mc "Of course, I thought so."
    s "Yeah, right..."
    mc "Very... Unusual work, I tell you."
    scene 7selina36a with dissolve
    s "Ha! That's an understatement."
    s "She has some strange thing with the fact that the model should be in its natural beauty."
    s "As a result, half of them either sit in some strange pose naked, or they just fuck..."
    mc "Hm... What strange modern art."
    s "Yeah, you don't have to tell me."
    scene black with fade
    "After talking for a while about the little things, you began to say goodbye."
    scene 7selina37 with dissolve
    s "Are you sure you don't want to stay?"
    s "In the morning we could repeat the wonderful events of this evening."
    mc "Sorry, I have a lot to do tomorrow."
    mc "Besides, you said yourself your mother should be back soon."
    s "Yeah, that's true."
    s "If I understood you right, you're preparing for a debut gig?"
    mc "Yep."
    mc "If you want, you can come on Saturday and watch."
    scene 7selina37a with dissolve
    s "I'm sorry, I can't this weekend. Work."
    mc "That's too bad."
    s "Yeah... Trust me, I would love to see you rock out on stage."
    mc "Then maybe next time?"
    scene 7selina37 with dissolve
    s "Let's hope so."
    scene 7selina38 with dissolve
    s "Now come here. I won't let you go without a kiss goodbye."
    mc "{i}Oh, yeah, without a kiss, good-bye isn't good-bye.{/i}"
    scene 7selina39 with dissolve
    "..."
    scene 7selina40 with dissolve
    s "See you later, [mc]."
    mc "See you later."
    stop music fadeout 3.0
    jump day07_rosa


label day07_rosa:
    scene black with fade
    play music "music/6 - Positive Mood.ogg"
    "You barely managed to leave the apartment and enter the hallway before you noticed Rosa."
    scene 7rosa01 with dissolve
    mc "{i}What a coincidence.{/i}"
    mc "{i}This redheaded family never ceases to amaze me with how often I run into them...{/i}"
    scene 7rosa02 with dissolve
    r "[mc] what a pleasant surprise to see you here!"
    mc "Um... I guess..."
    mc "I was here visiting Selina, but now I'm going home."
    r "I understand."
    scene 7rosa03 with dissolve
    "For a second, your eyes went down."
    mc "{i}Come to think of it, she's a very seductive madam.{/i}"
    mc "{i}Come on, [mc]! Pull yourself together!{/i}"
    scene 7rosa04a with dissolve
    r "[mc], Selina told me you're a musician. Is it true?"
    mc "Yeah, that's right."
    r "You may not know this, but I'm an artist and a professional painter."
    mc "Yes, I've just seen your work... Very impressive."
    scene 7rosa04 with dissolve
    r "Oh... Thank you. It's always nice to see someone like your work."
    r "But I wanted to ask you a little favor. As one artist to another."
    mc "Of course, if there's anything I can do..."
    scene 7rosa05 with dissolve
    r "That's good! The thing is, I need a model to pose for me. Purely on a temporary basis, of course."
    mc "Ehhh... "
    r "Don't worry, all you have to do is be present."
    mc "I'm not sure I'm up to it..."
    r "Just the opposite! You're perfect for the part. Believe me, I have an eye for this."
    mc "{i}Ha! What a strange proposal.{/i}"
    mc "{i}What am I supposed to say to that?{/i}"

    menu:
        "{color=#66FF33}Agree":
            $ rosa_path = True
            mc "{i}I don't know if it's a good idea, but to see a picture of myself portrayed by a professional...{/i}"
            mc "{i}Sounds very interesting.{/i}"
            mc "You know... Why not?"
            mc "I'm sure it'll be an interesting experience."
            scene 7rosa04 with dissolve
            r "Of course! I'll be sure you won't regret it."
            mc "Let's hope so."
            stop music fadeout 3.0
            scene black with fade
            "You exchanged phone numbers with Rosa and went home."
            "Next week you were supposed to meet with this red-haired artist."

        "Refuse":
            mc "{i}I don't know... I'm not sure I want to after everything Selina's told me about her art.{/i}"
            mc "I'm sorry, but I'm going to decline the offer."
            mc "Nothing personal, I just don't see myself in that role."
            scene 7rosa04b with dissolve
            r "Oh... I understand."
            r "Too bad you don't want to."
            r "But it was worth a try."
            mc "Of course."
            stop music fadeout 3.0
            scene black with fade
            "You said goodbye to Rose and went home."

    "There was a new day ahead of you."
    jump day07_concert


label day07_concert:
    scene black with fade
    "The next few days passed so quickly that you almost didn't notice them."
    scene 7city03 with dissolve
    "The day of the gig. Evening."
    scene 7rock01 with dissolve
    play music "music/2 - Bad.ogg"
    "You were in a hurry."
    mc "{i}Damn, I was almost late because of that stupid bus.{/i}"
    mc "{i}But I got here.{/i}"
    mc "{i}I don't even want to think about what would happen if I was late.{/i}"
    scene 7rock02 with dissolve
    "Soon you were near the familiar back door to the Purple Orchid."
    mc "{i}Ugh... I need to catch my breath.{/i}"
    scene 7rock03 with dissolve
    "Before you could press the doorbell, the door swung open."
    "{color=#4682B4}Security{/color}" "Oh... You must be a musician."
    mc "Yeah."
    scene 7rock03a with dissolve
    "{color=#4682B4}Security{/color}" "Then, come in."
    "{color=#4682B4}Security{/color}" "Most of you are here."
    "{color=#4682B4}Security{/color}" "You can go through the staff door."
    mc "Okay. Thanks, man."
    scene 7rock04 with dissolve
    "You walked past the security and found yourself in a dark room."
    mc "{i}They did a good job here.{/i}"
    "There were guys from other bands you didn't recognize."
    mc "{i}Soooo... Where are my dummies?{/i}"
    "You went ahead."
    scene 7rock05 with dissolve
    j "Hey! You were almost late bro!"
    mc "{i}Here comes the first one.{/i}"
    mc "But not late."
    j "Yeah, right."
    mc "So, you're here, where's the female half of our band?"
    scene 7rock06 with dissolve
    j "Heh. Turn around and see for yourself."
    mc "Well, if you say so..."
    scene 7rock07 with dissolve
    "Having done exactly as Jacob instructed, you froze."
    mc "Wow..."
    ls "Hm? Is that all you have to say after almost being late?"
    jd "Don't push him, Liz... Let him come to his senses."
    scene 7rock08 with dissolve
    mc "Damn... You guys look amazing!"
    j "Heh. I told them the same thing."
    j "Even if people don't like our music, they won't care. When these two beauties are before you, it's gonna be difficult to think straight."
    ls "Come on, guys!"
    ls "It was Jade who chose our costumes."
    jd "..."
    mc "{i}Good choice, Jade. Very good!{/i}"
    scene 7rock09 with dissolve
    ls "In any case... [band_name] is playing in the middle of the lineup, so we still have time."
    mc "Heh. I'm saved."
    ls "Yep."
    scene 7rock10 with dissolve
    mc "If we're playing in the middle of the show, that's great news."
    mc "The audience will be warmed up by other bands, but still not tired yet."
    jd "That's true. That is the perfect time."
    scene 7rock11 with dissolve
    j "That's great!"
    j "With this opportunity, we just have to do everything right."
    j "Well? Don't you agree?"
    scene 7rock11a with dissolve
    mc "Yes... We should be on our A game."
    stop music fadeout 3.0
    "..."
    scene black with fade
    "Some time later."
    scene 7rock12 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "Contrary to your assumptions, your turn up on stage took longer than expected."
    mc "{i}It's taking so long...{/i}"
    "You could see that everybody had their own way of dealing with the anxiety."

    scene 7rock13 with dissolve
    "Jade smoked one cigarette after another in silence."
    mc "{i}It seems that helps her to cope with the growing excitement.{/i}"
    mc "{i}I can't blame her, I wouldn't mind a cigarette myself.{/i}"
    scene 7rock14 with dissolve
    "At first you even wanted to come over and cheer her up, but then you changed your mind."
    mc "{i}I think she just wants to be alone right now.{/i}"
    scene 7rock15 with dissolve
    "..."
    mc "{i}And if that's what she wants, so be it.{/i}"

    scene 7rock16 with dissolve
    "Meanwhile, Lisa was carving tracks in the floor pacing nervously around the room"
    mc "{i}It seems that our main star is the most nervous.{/i}"
    scene 7rock17 with dissolve
    "She tightly clenched a bottle of coke and quietly hummed to herself."
    mc "{i}I wouldn't be surprised if this is how she remembers the words of her own songs.{/i}"
    scene 7rock18 with dissolve
    "..."
    mc "{i}Unlike Jade, maybe I should cheer her up.{/i}"
    scene 7rock19 with dissolve
    "You went to Lisa and sat down next to her."
    mc "How are you? Worried?"
    ls "No, I'm totally fine."
    mc "Come on, I can see you're worried. You don't have anything to be concerned about."
    scene 7rock20 with dissolve
    ls "Yes? And why do you think that?"
    mc "Because your voice is amazing. It's one of those things I'm 100 percent sure of."
    mc "You can take that to the bank."
    scene 7rock20a with dissolve
    ls "Well, if that's what you believe... And what about our songs?"
    mc "Heh... Songs are good, too! You'll see soon enough."
    "..."
    scene 7rock20b with dissolve
    ls "Thank you for supporting me [mc]."
    if lisa_path == True:
        mc "It's my responsibility to take care of you, since you are my girlfriend."
        ls "Heh. That's right."
        scene 7rock20c with dissolve
        ls "And mine is to take care of you..."
        ls "And I've already have some thoughts about what we're going to do with you after this gig..."
        mc "Hey, don't tease me!"
        scene 7rock20b with dissolve
        ls "Haha, okay. I won't."
        "..."
        scene 7rock20 with dissolve
        ls "Hey, look."
        "Lisa pointed in Jacob's direction."
    else:
        mc "We are a responsible band and we have to take care of each other."
        ls "Sounds good."
        mc "Yeah."
        "..."
        scene 7rock20 with dissolve
        ls "Hey, look."
        "Lisa pointed in Jacob's direction."
    "..."

    scene 7rock21 with dissolve
    "The last member of your band was busy beating out a rhythm on the table with his drumsticks."
    mc "{i}Looks like he decided to warm up a bit.{/i}"
    mc "{i}Maybe I should go check on him.{/i}"
    scene 7rock20 with dissolve
    mc "I'm sorry, I'll be a bit."
    ls "Yeah, sure."
    scene 7rock23 with dissolve
    mc "The show hasn't started yet, and you're already beating your stick."
    scene 7rock24 with dissolve
    j "Heh, just fighting the anticipation as best I can."
    mc "Yeah... I understand that. Waiting for something important is always hard."
    j "Exactly!"
    mc "Okay, I'll ask you straight... You ready?"
    scene 7rock23a with dissolve
    j "Of course. I'd think no less than you."
    mc "Great, that's what I wanted to hear."
    j "Yep... Now, if you don't mind, I'll get back to my business."
    scene 7rock22 with dissolve
    "Jacob again drummed on the table."
    mc "Well, I won't bother you anymore."
    stop music fadeout 3.0

    scene black with fade
    "At the same time, across the hall."
    scene 7rock25 with dissolve
    play music "music/8 - Intro Music.ogg"
    "{color=#808000}Guy #1{/color}" "I'm telling you, she has a crush on me... Blondes love me!"
    "{color=#BC8F8F}Guy #2{/color}" "Sure, have you ever seen yourself in a mirror?"
    "{color=#808000}Guy #1{/color}" "Hey, watch your mouth, asshole."
    scene 7rock26 with dissolve
    "{color=#BC8F8F}Guy #2{/color}" "Wait a minute... Is it just me or that Jade sitting there?"
    "{color=#808000}Guy #1{/color}" "Huh? Who the fuck is Jade?"
    "{color=#BC8F8F}Guy #2{/color}" "Come on, look forward!"
    scene 7rock26a with dissolve
    "{color=#808000}Guy #1{/color}" "Hm?"
    scene 7rock27 with dissolve
    "{color=#808000}Guy #1{/color}" "Wow! You're right!"
    "{color=#808000}Guy #1{/color}" "What a surprise."
    "{color=#808000}Guy #1{/color}" "Let's go say hello to an old friend."
    "{color=#BC8F8F}Guy #2{/color}" "Yeah."
    scene 7rock28 with dissolve
    "{color=#808000}Guy #1{/color}" "Well,well! Look who we have here. Is it really the great guitarist Jade?"
    "{color=#BC8F8F}Guy #2{/color}" "Hey, since when did she become great?"
    "{color=#808000}Guy #1{/color}" "That was sarcasm, asshole."
    "{color=#808000}Guy #1{/color}" "You're familiar with the concept of sarcasm, right?"
    "{color=#BC8F8F}Guy #2{/color}" "Don't call me an asshole, asshole."
    scene 7rock29 with dissolve
    jd "Derek, Michael..."
    jd "Are you performing here tonight, too?"
    scene 7rock30 with dissolve
    "{color=#808000}Derek{/color}" "Ha! She's asking!"
    "{color=#BC8F8F}Michael{/color}" "We're the big finale, right after [band_name]."
    scene 7rock30a with dissolve
    "{color=#808000}Derek{/color}" "Hey, we've seen everyone but them... So is that her band?"
    "{color=#BC8F8F}Michael{/color}" "Holy shit, that's true!"
    "{color=#BC8F8F}Michael{/color}" "Did miss \"I'm not like the rest\" find herself someone she likes?"
    "{color=#808000}Derek{/color}" "Really..."
    scene 7rock31 with dissolve
    "{color=#808000}Derek{/color}" "What kind of suckers decided to let you in their band?"
    "{color=#808000}Derek{/color}" "Do they even know who you really are, huh?!"
    scene 7rock29a with dissolve
    jd "..."
    jd "They know everything they need."

    scene 7rock32 with dissolve
    j "[mc] I'm not imagining this right now, and those two dudes are annoying Jade, right?!"
    mc "Looks like you're right."
    mc "We need to figure this out before it goes too far."
    scene 7rock33 with dissolve
    stop music fadeout 3.0
    j "Hey, guys, what the hell is going on here?!"
    j "If you have any problems with Jade, you can tell us about them too. I'm sure we can deal with it quickly."
    scene 7rock34 with dissolve
    "{color=#808000}Derek{/color}" "Who the fuck are you to tell me who I can talk to and can't talk to?!"
    j "I'm the one who's gonna kick your ass if you keep that attitude going."
    j "You understand me?!"
    scene 7rock35 with dissolve
    "{color=#808000}Derek{/color}" "Looks like someone here is a bit too arrogant."
    "{color=#808000}Derek{/color}" "Maybe it's time to put you where you belong."
    j "You can try."
    scene 7rock36 with dissolve
    "{color=#FFA07A}Oliver{/color}" "Hey, what the hell is going on here! Stop fighting!"
    mc "{i}And now the authority intervenes.{/i}"
    scene 7rock37 with dissolve
    play music "music/8 - Intro Music.ogg"
    "{color=#FFA07A}Oliver{/color}" "If that shit happens again in my club, I'll throw you both out. I don't care who started it."
    "{color=#FFA07A}Oliver{/color}" "I hope all understood me?!"
    scene 7rock38 with dissolve
    "{color=#808000}Derek{/color}" "Relax, boss, we were just messing around."
    "{color=#808000}Derek{/color}" "Isn't that right, Michael?"
    "{color=#BC8F8F}Michael{/color}" "Yes... Uhh... We're gonna be quiet."
    scene 7rock39 with dissolve
    "{color=#808000}Derek{/color}" "Sorry, guys..."
    mc "{i}He said it too easily...{/i}"
    "{color=#808000}Derek{/color}" "Before the gig, we're all a little nervous."
    "..."
    mc "We don't care about your nerves, just apologize to jade, and we're done."
    "{color=#808000}Derek{/color}" "Hmm... Okay."
    scene 7rock40 with dissolve
    "{color=#808000}Derek{/color}" "No offense, Jade, I was just messing with you. Hope you're not angry."
    "{color=#808000}Derek{/color}" "Anyway, good luck with the show."
    "{color=#BC8F8F}Michael{/color}" "Yeah, good luck."
    scene 7rock41 with dissolve
    jd "Yes... Thank you."
    jd "Good luck to you too."
    scene 7rock37 with dissolve
    "{color=#FFA07A}Oliver{/color}" "Well, that's different."
    scene 7rock37a with dissolve
    "{color=#FFA07A}Oliver{/color}" "All right, [band_name], get on stage."
    "{color=#FFA07A}Oliver{/color}" "You're up."
    stop music fadeout 3.0
    mc "{i}Finally.{/i}"
    jump day07_rock


label day07_rock:
    scene black with fade
    "You remember the following events most clearly."
    scene 7concert01 with dissolve
    play music "music/3 - Dream With U.ogg"
    "Your band went on stage and met the crowd."
    "[band_name] was ready to rock."
    scene 7concert02 with dissolve
    "And most importantly, you were ready to rock."
    mc "{i}Yeah... There's quite a few people here today.{/i}"
    mc "{i}And it looks like this really is the beginning of a new journey.{/i}"
    scene 7concert03 with dissolve
    "You looked at Lisa."
    mc "{i}She seems pretty confident.{/i}"
    mc "{i}So there's nothing to fear.{/i}"
    scene 7concert04 with dissolve
    ls "HEY-HEY!!! I hope everyone is in a good mood?!"
    "The crowd cheered."
    ls "Great!"
    ls "You don't know us yet, but believe me, today you will remember the band [band_name]!"
    "The crowd cheered again."
    mc "{i}Damn... She's copying the style of the Naked Park vocalist.{/i}"
    mc "{i}Not entirely, of course, but there's definitely something similar about it.{/i}"
    mc "{i}And I like it!{/i}"
    scene 7concert03 with dissolve
    ls "Okay, guys now let's get started!"
    scene 7concert05 with dissolve
    "In the next moment, loud music poured from the speakers."
    "Your music."
    "Jade masterfully played the guitar..."
    scene 7concert06 with dissolve
    "You complement it with your bass."
    "And Jacob set a steady rhythm on the drums."
    "Everything was going just perfect."
    stop music fadeout 3.0
    scene black with fade
    "At the same time in the hall."
    scene 7concert07 with dissolve
    play music "music/11 - Pop Energy.ogg"
    "..."
    em "{i}I can't believe [mc] is actually on stage.{/i}"
    em "{i}After all these years, after all this talk about music, it really happened...{/i}"
    em "{i}It's so incredible, and I'm happy for him.{/i}"
    scene 7concert08 with dissolve
    "Emma noticed a familiar figure in the crowded room."
    em "{i}Wait a minute... Is that Julia?{/i}"
    em "{i}Hell, she's all I need here.{/i}"
    sis "Emma! What a meeting!"
    scene 7concert09 with dissolve
    em "{i}I'd say what an unpleasant meeting.{/i}"
    em "How could you recognize me in this crowd?"
    scene 7concert10 with dissolve
    sis "It wasn't hard at all, I just followed the smell of poison."
    sis "And here I am, with you."
    em "..."
    sis "And I also know why you're here..."
    scene 7concert11 with dissolve
    em "I don't know what you mean, but you're wrong about me."
    em "I'm here to support [mc]."
    scene 7concert10 with dissolve
    sis "That sounds very convincing."
    sis "But you know why I don't believe you? Because a little bird told me that you were at my father's office building a few days ago."
    sis "Admit it, that's a very big coincidence."
    em "{i}...{/i}"
    scene 7concert12 with dissolve
    "Meanwhile, the crowd was making more and more noise."
    "There was no doubt, they liked this music and this band."
    scene 7concert13 with dissolve
    "Man #1" "Holy shit! This chick rocks!"
    "Man #2" "Hey, shut up, I'm making a video."
    "Girl #1" "Shut up, both of you, let me hear the music!"
    scene 7concert14 with dissolve
    sis "Looks like people like [band_name]."
    em "Yes... It would seem so..."
    sis "So maybe you should follow their example."
    sis "They each worked on themselves for a long time to get those results."
    sis "And you want to ruin it..."
    scene 7concert15 with dissolve
    em "{i}I don't know how she knows all this, but it makes sense.{/i}"
    em "{i}I guess I just got... caught up in it.{/i}"
    em "{i}What I'm doing here, what their father asked me to do... This is bullshit.{/i}"
    em "{i}Maybe I should stop before I do something stupid that I'll regret.{/i}"
    em "{i}Arrrr! How I hate it!{/i}"
    scene 7concert16 with dissolve
    if emma_sex == True:
        em "You're right, but not about everything."
        em "Your father is clearly a jerk, but..."
        em "But that doesn't mean I don't like [mc]."
        em "And believe me, I don't care what you think."
        em "Tell him I was here and I enjoyed his gig."
    else:
        em "You're right... This is wrong."
        em "Tell [mc] I was here and I enjoyed his gig."
        em "I promise you, you will never see me again."
    scene 7concert17 with dissolve
    "Without another word, Emma walked away."
    scene 7concert17a with dissolve
    "..."
    scene 7concert18 with dissolve
    em "{i}He wanted to make me dance to his tune...{/i}"
    em "{i}How about that, asshole?{/i}"
    scene 7concert18a with dissolve
    "..."
    em "{i}Yes... That's much better.{/i}"
    em "{i}I wish I could see his face when he reads this.{/i}"
    scene black with fade
    "At the same time, backstage."
    scene 7concert19 with dissolve
    "{color=#BC8F8F}Michael{/color}" "Hmm... These guys aren't as bad as I thought they'd be."
    "{color=#808000}Derek{/color}" "Yeah, maybe..."
    "{color=#808000}Derek{/color}" "That red-haired chick is really good."
    "{color=#BC8F8F}Michael{/color}" "Ha! I recognize that tone..."
    "{color=#BC8F8F}Michael{/color}" "You seem to like her."
    scene 7concert20 with dissolve
    "{color=#808000}Derek{/color}" "Look at her. How can someone not like such a hotty?"
    "{color=#BC8F8F}Michael{/color}" "Yeah, you're right, there's definitely something about her."
    "{color=#808000}Derek{/color}" "So true."
    scene 7concert21 with dissolve
    "{color=#808000}Derek{/color}" "I have to meet her."
    "{color=#808000}Derek{/color}" "I'm sure we'll find a lot to talk about."
    "{color=#808000}Derek{/color}" "Maybe not only talk..."
    stop music fadeout 3.0
    jump day07_end

label day07_end:
    scene black with fade
    "Some time later."
    "Right after the gig."
    scene 7end01 with dissolve
    play music "music/4 - Ready to Drive.ogg"
    j "Did you fucking see how people cheered for us at the end?!"
    mc "Yeah... They seemed to like us a lot."
    ls "I agree! That was awesome!"
    mc "Hey, be careful or you'll get used to it."
    ls "I don't see anything wrong with that."
    mc "Hehe. Me neither."
    scene 7end02 with dissolve
    j "What do you think, Jade?"
    j "How'd you like the show, how does it feel after?"
    jd "It was... Awesome."
    mc "You see, if Jade says it's awesome, then you know it's true."
    "Having fun talking to each other, you went outside."
    scene 7end03 with dissolve
    mc "{i}Hey! It's Julia! So she came, too.{/i}"
    mc "{i}And she already made friends with someone...{/i}"
    mc "Julia."
    scene 7end04 with dissolve
    sis "Oh, there you are."
    mc "Here I am."
    scene 7end04a with dissolve
    sis "Sorry, Aki, I have to go."
    "{color=#DB7093}Aki{/color}" "No worries."
    "{color=#DB7093}Aki{/color}" "Good luck."
    sis "You too."
    scene 7end05 with dissolve
    sis "Well, you guys put the heat on! It was just amazing."
    mc "{i}I should introduce my sister, because not everyone here knows her.{/i}"
    mc "Lisa, Jade, let me introduce you to my older sister, Julia."
    scene 7end09 with dissolve
    ls "Oh, very nice to meet you!"
    if lisa_path == True:
        ls "[mc] has told me a lot about you. I hope we get along!"
        sis "Wow, she's really quick. I like this one."
    else:
        ls "We're glad you came here today."
        sis "How could I miss this?"
    scene 7end10 with dissolve
    jd "It's nice to meet you."
    mc "{i}As always, short and clear.{/i}"
    scene 7end06 with dissolve
    sis "It's mutual, girls."
    sis "And thank you for keeping an eye on these two goons. You can be sure you are the brightest stars in this band."
    mc "{i}Heh. As always, my sister wants to make a good impression.{/i}"
    scene 7end05 with dissolve
    j "Hey, we're still here, too."
    sis "You guys did great, too. Keep it up!"
    mc "Yeah, thanks for that."
    scene 7end11 with dissolve
    sis "By the way, Jacob, the girl I was just talking to really liked the drummer from [band_name]."
    sis "I hope you understand what I'm getting at."
    scene 7end07 with dissolve
    j "Uhh... Are you serious?!"
    sis "Very serious."
    scene 7end07a with dissolve
    j "Ooookay... Point taken. Thanks for the tip."
    j "Guys, wish me luck."
    sis "Good luck."
    mc "Good luck, bro."
    scene 7end08 with dissolve
    "The next moment, you witnessed Jacob roll up to a girl named Aki."
    mc "{i}Hmm... that's not so bad.{/i}"
    mc "{i}She seems to really like him.{/i}"
    mc "{i}Isn't this our first groupie?{/i}"
    scene 7end06 with dissolve
    sis "Okay, guys, as much as I want to be here with you guys, I have to go."
    mc "You sure? We wanted to go out now and celebrate."
    mc "You could join us."
    scene 7end12 with dissolve
    sis "I'm sorry, but I have a very important case to take care of in the morning."
    sis "I hope you understand."
    mc "Do what you must. See you then."
    sis "Yeah, see ya."
    scene black with fade
    "You said goodbye to Julia and went to check on Jacob."
    scene 7end13 with dissolve
    mc "Hey, man, we're gonna go."
    mc "You coming?"
    scene 7end13a with dissolve
    j "What?"
    j "Ahhh... Are you leaving?"
    mc "Yes we are."
    j "Shit, man, I'm sorry, but I'm probably gonna be here a little longer."
    mc "You sure? If you want, you can join the rest of us."
    scene 7end13b with dissolve
    j "No way. We're waiting for Aki's sister, and then..."
    j "Ahem!.. Basically, go without me."
    mc "{i}Oho. Looks like someone's having a very pleasant evening.{/i}"
    mc "{i}I'm a little jealous.{/i}"
    mc "Whatever, man."
    mc "See you then."
    j "Yeah, bye."
    scene black with fade
    "A few seconds later."
    scene 7end14 with dissolve
    mc "Well, girls, you probably heard it yourself."
    mc "It seems the three of us are the only ones left."
    ls "Pfft... If that's what Jacob wants, let him hang out with that blond slut."
    ls "I have a suggestion. How about we celebrate tonight in a way that makes him jealous?"
    mc "Given the circumstances, that's not going to be easy."
    scene 7end15 with dissolve
    ls "Who says we're looking for easy ways?"
    ls "Don't you agree with me, Jade?"
    scene 7end16 with dissolve
    jd "Totally agree."
    jd "Let's hang out."
    scene 7end17 with dissolve
    "You gently hugged Lisa and Jade and smiled broadly."
    mc "You know what, I have a couple of really good ideas about where this is going."
    mc "Trust me, you won't forget this evening for a long time."
    ls "Then what are we waiting for? Let's go!"
    stop music fadeout 3.0
    jump day08_start

