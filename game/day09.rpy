
label day09_start:
    scene black with fade
    "Next morning."
    if jane_date_offer == True:
        jump day09_jane
    elif selina_path == True or rosa_path == True:
        jump day09_selina_phone
    else:
        jump day09_jacob


label day09_jane:
    scene black with fade
    "Julia and Jane's office."
    play music "music/6 - Positive Mood.ogg"
    scene 9jane01 with dissolve
    sis "Come on, Jane, I want to know what happened between you two yesterday."
    sis "I heard a rumor it was a romantic date right here in the office. Is it true?"
    jn "Hmm? I thought you were old enough not to believe rumors."
    scene 9jane02a with dissolve
    sis "Even though you say so, something tells me there's some truth to it."
    sis "So... Tell me about it."
    scene 9jane03 with dissolve
    jn "There's nothing to talk about."
    scene 9jane02a with dissolve
    sis "You're saying one thing, but I can tell from your face that it's not true."
    scene 9jane03 with dissolve
    jn "..."    
    scene 9jane03b with dissolve
    jn "And how the hell did you even know about this?"
    scene 9jane02a with dissolve
    sis "I have my own ways. And don't change the subject."
    scene 9jane03b with dissolve
    jn "Actually, you're the one who's changing the subject right now. I’ll ask you again, how did you find out about this?"
    scene 9jane02 with dissolve
    sis "If you're really interested, I looked at the visitors' log from yesterday and compared all the data. Happy?"
    jn "You wouldn't have guessed it all just from these trivia."
    sis "Well... I also saw what time you turned off the alarm yesterday and used your exit pass. It wasn't hard."
    scene 9jane01 with dissolve
    jn "Seriously? Did you really check it all out? When did you just have time to do all these things?"
    sis "This morning. Don't ask why, I was bored."
    scene 9jane03a with dissolve
    jn "Just bored, huh? Whatever you say, Sherlock."
    sis "So are you gonna tell me how you're doing with my brother, or am I gonna have to get that information out of you?"
    scene 9jane03 with dissolve
    jn "..."
    scene 9jane02a with dissolve
    sis "Okay... If you keep your mouth shut, we'll go out for a drink tomorrow night, and then you'll definitely tell me everything."
    scene 9jane03a with dissolve
    jn "Hey, that's a sneaky trick!" 
    scene 9jane02a with dissolve
    sis "Mm-hmm. It's a sneaky trick, but it always works."
    scene 9jane03a with dissolve
    jn "Okay, I agree, we'll discuss it tomorrow night. But remember, you will pay for everything."
    stop music fadeout 2.0
    sis "Deal."
    if nicole_plus == True:
        play sound "music/knock.mp3"
        scene 9jane04a with vpunch
        "Knock, knock!"
        jn "Hmm? Are you expecting someone?"
        sis "I don't think so."
        sis "Let's see who it is."
        sis "Come in!"
        scene 9jane04 with dissolve
        play music "music/6 - Positive Mood.ogg"
        n "Julia, I'm sorry I showed up so suddenly, but I have some important news."
        "..."
        n "Oh... I see you're busy..."
        scene 9jane05 with dissolve
        jn "It's okay, I was just about to leave."
        n "Well, actually, you better stay. I found something that you both might find interesting."
        scene 9jane06 with dissolve
        jn "What do you mean? And what is that folder you're holding in your hands?"
        scene 9jane04 with dissolve
        n "It'll be a lot easier if I show you."
        scene 9jane07 with dissolve
        n "I've been checking your company's financial statements for the past year over the last week and as a result I came across something very unusual."
        n "Checking the numbers, I realized that a lot of them don't match."
        n "Look, these are official documents of one of your suppliers' firms. At first glance, everything looks quite normal, but in fact it is not."
        n "Pay attention to these two little columns."
        scene 9jane09 with dissolve
        sis "Wait a minute... What is this? The amount of money for the goods in them is obviously overstated."
        scene 9jane07 with dissolve
        n "That's exactly what it is."
        n "The numbers themselves aren't too big, but they're very often repeated."
        n "If you sum up all these costs over the past couple of years, the amount of money you have been cheated on is quite significant."
        scene 9jane08 with dissolve
        jn "How the hell did we miss that?"
        sis "..."
        n "Well, it was all done very cleverly, albeit quite simply."
        scene 9jane09 with dissolve
        sis "We're not gonna let this go. We need to contact our lawyers and start acting."
        n "Yeah, I think so, too."
        scene 9jane11 with dissolve
        sis "Well, that's an amazing job, Nicole. I'm impressed."
        n "Thank you."
        scene 9jane10 with dissolve
        jn "And when did you do all this?"
        n "I did some things in the evenings and some things during lunch breaks."
        sis "Like I said, it's an amazing job."
        scene 9jane11a with dissolve
        jn "You know... Tomorrow night, Julia and I were gonna go out for a drink after work."
        jn "We don't usually meet our employees outside of office hours, but after all you've done today, I'm totally obliged to ask you to come with us."
        jn "Of course, only if you want to."
        scene 9jane12 with dissolve
        n "If you're inviting me, I don't mind."
        jn "Okay, great! Then we have a deal."
        scene black with fade
        "After discussing all the details of the case again, Nicole left Julia's office."
        scene 9jane13 with dissolve
        sis "You really think it's a good idea to take her with us?"
        jn "Who knows? She is smart, attentive and working hard. I like her."
        sis "Yeah, me, too."
        "..."
        scene 9jane13a with dissolve
        sis "And you know who brought her into our company?"
        jn "Oh, no, just don't start again..."
        sis "Ha ha! Okay, okay! I won't."
        scene 9jane13 with dissolve
        jn "Since we're done here, I have to get back to work."
        sis "And I need to call the lawyers."
        stop music fadeout 3.0
    scene black with fade
    "In the meantime."
    if selina_path == True or rosa_path == True:
        jump day09_selina_phone
    else:
        jump day09_jacob    


label day09_selina_phone:
    scene black with fade
    "You were sitting on your couch and were busy playing guitar."
    scene 9music01 with dissolve
    play music "music/7 - Just Happy.ogg"
    mc "{i}Okay... Now let's try this.{/i}"
    mc "{i}Yeah, not bad... Not bad at all! And now-{/i}"
    scene 9phone01 with dissolve
    "*Sound of a new message!*"
    mc "{i}Hmm?{/i}"
    scene 9phone02 with dissolve
    mc "Hello."
    s "Hey, [mc]!"
    mc "Oh... Selina. Didn't expect to hear from you."
    s "I hope I'm not distracting you from anything."
    scene 9phone03 with dissolve
    mc "No, not at all! Besides, I will always have time for you."
    s "Mmm... Glad to hear it."
    mc "So-"   
    if selina_broke_up == False:
        scene 9phone04 with dissolve
        s "I'm a little ashamed to admit it, but I really wanted to hear your voice."
        scene 9phone02 with dissolve
        mc "{i}Huh. What a nice reason to call.{/i}"
        mc "You can call me anytime you want to hear my voice."
        scene 9phone04 with dissolve
        s "It's a deal."
        s "And by the way, since we're dating now, why don't we spend some time together?"
        mc "Sounds good. When and where?"
        s "How about today, in about an hour?"
        mc "Wow! You're really quick!"
        scene 9phone04a with dissolve
        s "Well, I'm at work right now, and if you're not too busy, we could have lunch together."
        mc "Say no more, just give me the address"
        s "Okay, great! Record..."
        stop music fadeout 3.0
        jump day09_selina_hospital
    else:
        scene 9phone04a with dissolve
        s "The truth is, I'm calling at Rosa's request."
        scene 9phone02 with dissolve
        mc "{i}Rosa's request?{/i}"
        mc "Okay, uh... I'm listening."
        scene 9phone04a with dissolve
        s "The thing is that the painting that we posed for recently, will be shown in two days at one major city exhibition."
        mc "Like, for real?"
        s "Yeah. Don't even ask me how Rosa managed to make a deal with the organizers in such a short time, I don't know it myself."
        scene 9phone02 with dissolve
        mc "{i}Probably because of her connections. But it doesn't matter now.{/i}"
        mc "Apparently, she wanted it very badly."
        scene 9phone04a with dissolve
        s "That was definitely one of the reasons"
        s "Anyway, there's gonna be a lot of paintings and a few of them will belong to my mom."
        "..."
        s "She wants us both to be there. I hope you will accept this invitation?"
        scene 9phone03 with dissolve
        mc "I don't mind, just tell me when and where."
        s "In two days. If you want, you can come over and we'll go together."
        mc "Yeah, it's gonna be a lot easier. Deal."
        s "See you then, [mc]."
        mc "See you."
        stop music fadeout 3.0
        jump day09_jacob
    
label day09_selina_hospital:
    if _in_replay:
        $ setReplay()
    scene 9selina01 with fade
    play music "music/12 - The Moose.ogg"
    "Some time later, you were standing outside the hospital where Selina worked."
    mc "{i}The atmosphere here is very pleasant. I like it.{/i}"
    mc "{i}Maybe I should text her.{/i}"
    scene 9selina02 with dissolve
    mc "\"I'm outside, waiting for you.\""
    mc "{i}I hope she doesn't keep me waiting long.{/i}"
    scene black with fade
    "Few minutes later."
    scene 9selina03 with dissolve
    mc "{i}There she is!{/i}"
    "With a gentle gait, Selina came down the stairs of the hospital."
    scene 9selina04 with dissolve
    s "Thank you for coming."
    mc "Hello to you, too."
    scene 9selina05 with dissolve
    s "Mmmm..."
    mc "{i}Oohhhh... I like this greeting.{/i}"
    scene 9selina06 with dissolve
    s "It's good to see you."
    mc "Believe me, it's mutual."
    mc "By the way, I don't know why, but I imagined you'd come out in your medical robe."
    scene 9selina06a with dissolve
    s "Haha! Sorry to upset you, but I changed my clothes."
    mc "No, it's actually a lot better that way."
    scene 9selina07 with dissolve
    s "Really?"
    mc "You bet! You look amazing!"
    s "You have no idea how nice it is to hear you say that."
    scene 9selina07a with dissolve
    s "The weather outside is lovely... Can we take a little walk? I know one very nice, quiet place here."
    mc "Sure, lead the way."
    scene 9selina08 with dissolve
    s "Listen, uh... I wanted to ask you, what do you know about art exhibitions."
    mc "Art exhibitions? Why do you ask me that?"
    scene 9selina08a with dissolve
    s "This is about my mom."
    if rosa_path == True:
        s "The fact is that the painting that we recently posed for will be shown at one major city exhibition in two days."
        mc "Like, for real?"
        s "Yeah. Don't even ask me how she managed to make a deal with the organizers in such a short time, I don't know it myself."
        mc "Apparently, she wanted it very badly."
        s "That's for sure."
        s "Anyway, my mom talked me into going there with her..."
        mc "{i}I think I already know what she's gonna ask me about.{/i}"
        s "...and I want you to come with us. I just can't do it alone."
    else:
        s "The thing is that in two days there will be a large city exhibition of paintings, which will feature several of her works."
        s "She made me promise to go with her."
        s "I want you to keep me company there. I just can't do it alone."
    scene 9selina10 with dissolve
    "Soon you came to a quiet place near the hospital that Selina had talked about earlier."
    mc "So you're saying this event is in two days?"
    s "Yeah, it's gonna be in the evening."
    s "You and I are just gonna have to show up there, and then we're free to go."
    s "So, what do you say?"
    scene 9selina09 with dissolve
    mc "As far as I know, I'm not doing anything that day. You can count me in."
    mc "We're not gonna miss each other there."    
    s "So you're definitely going to go there?"
    mc "You have my word."
    scene 9selina11 with dissolve
    s "Thank you, [mc], that means a lot to me."
    mc "{i}Damn, she's so cute right now.{/i}"
    mc "It's okay, I'm actually curious about going there myself."
    scene 9selina12 with dissolve
    "Selina moved closer to you."
    s "You know... I didn't just decide to invite you here."
    mc "Mmm... And what do you want to do?"
    s "Oh, I think you've been guessing that from the start."
    mc "Maybe."
    scene 9selina13 with dissolve
    s "Mmmm... Yes..."
    mc "{i}Even with that unusual story of our acquaintance, she's still my little redheaded beast.{/i}"
    scene 9selina14 with dissolve
    "Your palm slipped up Selina's thigh smoothly."
    s "Ahh..."
    stop music fadeout 3.0
    scene 9selina15 with dissolve
    "..."
    play sound "music/cough.wav"
    "{color=#DC143C}Karen{/color}" "Ahem!"
    scene 9selina17 with dissolve
    play music "music/8 - Intro Music.ogg"
    "You and Selina immediately stopped kissing and noticed an unexpected guest."
    mc "{i}Who the hell is this? A friend of Selina's?{/i}"
    scene 9selina16 with dissolve
    mc "{i}But judging by her face, she may not be.{/i}"
    s "What are you doing here?"
    scene 9selina18 with dissolve
    "{color=#DC143C}Karen{/color}" "I'm sorry, I didn't know you weren't alone here."
    "{color=#DC143C}Karen{/color}" "I just wanted to talk to you. In private."
    scene 9selina19 with dissolve
    s "You can talk, I have nothing to hide from [mc]."
    "{color=#DC143C}Karen{/color}" "Are you sure?"
    "..."
    "{color=#DC143C}Karen{/color}" "Um... Okay..."
    "{color=#DC143C}Karen{/color}" "The thing is, I've been wanting to make up with you for a long time-"
    scene 9selina21 with vpunch
    s "No!"
    "{color=#DC143C}Karen{/color}" "Selina, at least hear me out."
    s "I said no! I'm not going to put up with you, and I'm not going to listen to you. Not after what you did!"
    scene 9selina18a with dissolve
    "{color=#DC143C}Karen{/color}" "Come on, how long can you stay angry?  We were best friends."
    mc "{i}Best friends? Ohh... I think I understand now who it is, and what is going on here.{/i}"
    scene 9selina21 with dissolve
    s "Exactly, we were friends! But you ruined it all."
    scene 9selina20 with dissolve
    s "Now do us both a favor and get out of here."
    scene 9selina18 with dissolve
    "{color=#DC143C}Karen{/color}" "But, uh..."
    scene 9selina21 with dissolve
    s "Leave!"
    scene 9selina18a with dissolve
    "{color=#DC143C}Karen{/color}" "Okay... I get it."
    scene 9selina22 with dissolve
    "Without saying another word, Selina's former friend left you alone."
    scene 9selina23 with dissolve
    s "I'm sorry you had to hear that... But, Lord! I hate that bitch so much."
    mc "Let me guess, that was the Karen you told me about?"
    s "Yes... It was her."
    s "I don't like liars and traitors more than anything else."
    if lisa_path == True or jane_date_offer == True or anna_sex == True:
        "Suddenly, you felt the ominous cold running down your back." 
    scene 9selina24 with dissolve
    s "But let's not talk about bad things!"
    s "Can't we just continue where we left off?"
    mc "Wait a minute, you really want to go on after what just happened?"
    s "And you don’t?"
    mc "Okay, fair enough."
    stop music fadeout 3.0
    scene 9selina25 with dissolve
    "You looked around and didn't find a single living soul around you."
    scene 9selina25a with dissolve
    play music "music/15 - Deep Mood.ogg"
    s "We don't have much time, so leave it to me."
    mc "Huh. Whatever you say."
    scene 9selina26 with dissolve
    "You noticed how Selina's palm ended up on your thigh."
    mc "Looks like you've decided to act smoothly."
    s "Yeah. Smooth, but determined..."
    scene 9selina27 with dissolve
    "Next thing you know, the fly on your pants was open."
    scene 9selina28 with dissolve
    s "Mmmm... Looks like someone's already on fire."
    mc "Well, there are people around here, so yeah, it's all a little exciting."
    s "Huh. Then keep an eye that nobody sees what we're doing, and I'll take care of the rest."
    show 9selina000
    "Selina's fingers gently touched your dick."
    s "Wow... It seems to be getting even harder."
    mc "Given what you're doing, it's hard to blame him for that."
    pause
    scene 9selina30 with dissolve
    s "In that case, maybe we should do something more effective?"
    mc "Oh... It's high time."
    scene 9selina31 with dissolve
    "Selina took your cock in her hand and slowly started wanking you off."
    scene anim56 with dissolve
    s "Mmmm... How do you like it?"
    mc "Yes... That's much better. Go on."
    s "Hee-hee. Whatever you say."
    mc "{i}Hell, if we weren't near the hospital, I'd be ripping all her clothes off right now...{/i}"
    mc "{i}I need to restrain myself.{/i}"
    pause
    scene 9selina32 with dissolve
    s "Oh... I see you can't keep your naughty hands to yourself."
    s "In that case..."
    scene 9selina33 with dissolve
    s "...we'll do it like this."
    scene 9selina34 with dissolve
    mc "Oohh..."
    s "I see you're much better off like this."
    scene anim57 with dissolve
    "Selina's hands started moving faster."
    mc "{i}Oohhhh... Her face is so close.{/i}"
    mc "{i}Jeez, I want to kiss her so badly...{/i}"
    mc "{i}I feel like she wants it too.{/i}"
    pause
    scene 9selina36 with dissolve
    s "Mmmm..."
    scene 9selina36a with dissolve
    mc "{i}It's so nice.{/i}"
    scene 9selina36 with dissolve
    "..."   
    scene 9selina35 with dissolve
    s "It doesn't look like I can do this with my hands alone."
    mc "{i}That's for sure.{/i}"
    scene 9selina37 with dissolve
    "A moment later, you felt Selina's hot tongue touching your dick."
    scene anim58 with dissolve
    mc "Yes... There you go, baby."
    mc "{i}It feels like she doesn't care where we are.{/i}"
    mc "{i}All she cares about is my dick.{/i}"
    mc "{i}And what's more, she's just as keen on it as I am.{/i}"
    pause
    scene 9selina38 with dissolve
    s "Mmm... And now let's try to do this."
    scene anim59 with dissolve
    mc "Yeah, it's so nice, Selina."
    mc "{i}She's very good at it.{/i}"   
    mc "{i}If this keeps up, I won't be able to hold out long.{/i}"
    pause
    scene 9selina37 with dissolve
    s "{i}Mm-hmm... He's doing pretty well. Maybe I should stop being cautious.{/i}"
    scene anim60 with dissolve
    "Selina took all your dick in her mouth and started sucking it as hard as she could."
    mc "{i}Oh, yeah, that's another thing!{/i}"  
    s "Mmmpphh.... Mmmmphh.... Mmmmphh..."
    mc "{i}It's so good... Perhaps just a little more and I will definitely come.{/i}"
    mc "{i}The only question is, should I warn Selina or not?{/i}"  
    pause
    menu:
        "Come in her mouth":            
            mc "{i}Oh... I don't think she'd be mad if I came in her mouth.{/i}"
            scene 9selina40 with dissolve
            mc "{i}A little more... A little more and I...{/i}"
            scene 9selina40a with flash
            mc "{i}Aaahhh!{/i}"
            scene 9selina40a with flash
            mc "{i}Yeeesss...{/i}"
            "..."
            scene 9selina41 with dissolve
            s "You know, actually, you should have warned me."
            mc "I'm sorry, it was so nice that I just didn't have time to..."
            s "It's okay, I'm not offended."
        "Come on her face":
            mc "{i}Oh... Perhaps it's better to warn her about it.{/i}"
            mc "Selina, I'm gonna..."
            s "Are you coming?"
            mc "Yes."
            scene 9selina39 with flash
            mc "{i}Aaahhh!{/i}"
            scene 9selina39a with flash
            mc "{i}Yeeesss...{/i}"
            mc "Ugh... It was amazing."
            scene 9selina39b with dissolve
            s "Yeah, I can see how much you liked it."
            scene 9selina41 with dissolve
    s "Wait a minute, I need to get myself cleaned up."
    stop music fadeout 3.0
  
    $ renpy.end_replay()
    if not persistent.day09selina:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day09selina = True

    mc "Of course."
    scene black with fade
    "One minute later."
    scene 9selina41a with dissolve
    play music "music/6 - Positive Mood.ogg"
    s "Well, that's it, my lunch is coming to an end."
    s "Too bad we don't have more time right now. I wouldn't give up the reciprocal service..."
    mc "Wait, is your lunch break over?"
    s "It's just a couple of minutes left."
    mc "Hmm... Maybe you could be a little late. "
    scene 9selina11 with dissolve
    s "Alas, but we're very strict about being late."
    mc "That sucks."
    s "Yeah."
    scene 9selina42 with dissolve
    s "Well, if you don't mind, let's just sit together for a minute."
    mc "You can sit with me as long as you want."
    s "Mm-hmm... Thank you, [mc]."
    mc "You're welcome."
    stop music fadeout 3.0
    scene black with fade
    "Soon after, Selina went back to work at the hospital."
    jump day09_jacob
   
label day09_jacob:
    scene black with fade
    "You decided that as long as you had free time before your shift at the bar, you could see Jacob."
    mc "{i}As far as I'm aware, he's supposed to be at his father's workshop at this time.{/i}"
    "Some time later."
    scene 9jacob00 with dissolve
    play music "music/10 - Street's.ogg"
    mc "{i}Here I am. This is where Jacob moonlights in his spare time.{/i}"
    mc "{i}I don't think it's gonna be hard to find him here.{/i}"
    scene 9jacob00a with dissolve
    mc "{i}Yeah, I was right, there he is.{/i}"
    mc "Hey, man!"
    scene 9jacob00b with dissolve
    j "[mc]?"
    j "Haha! Dude, what are you doing here?"
    mc "Well, you're the one who usually comes to me, but today I decided to pay you back. Especially since we haven't seen each other for a such long time."
    j "That's for sure. It's cool that you stopped by!"
    scene 9jacob01 with dissolve
    mc "Um... I can see from your dirty clothes that you have a lot of work to do."
    j "Yeah, there's a lot to do here."
    j "My father's been pissing me off with more and more responsibilities."
    mc "That's tough."
    j "Yeah..."
    scene 9jacob01b with dissolve
    j "But enough talk about my problems. Tell me, what brings you here?"
    mc "Yes... The thing is, I had an idea to get the whole band together. What do you say to that?"
    j "Are you kidding me? I'm all for it! I think the other guys will agree too."
    mc "Okay, great. How about we meet this time outside the rehearsal room? "
    j "I don't see any reason to be against it."
    mc "Are you free tomorrow?"
    scene 9jacob02 with dissolve
    j "Tomorrow? Let me think..."
    j "Yeah, probably."
    mc "You sure about that?"
    scene 9jacob01b with dissolve
    j "Absolutely! I will never miss this meeting."
    mc "Okay, that's awesome."
    j "Uh-huh."    
    scene 9jacob01 with dissolve
    j "So, have you decided where we're gonna go?"
    mc "I have a few options, but how about a pizza place?"
    j "Mmmm... Not a bad choice. I haven't eaten a pizza in ages."
    scene 9jacob03 with dissolve
    "{color=#FFFFFF}Worker{/color}" "Hey, Jacob, stop talking! Come on, I need your help."
    j "Okay, I'll be right there."
    scene 9jacob04 with dissolve
    j "I'm sorry, but you heard him, I have to go to work."
    mc "Yeah, yeah, it's okay. I have to go too. I have a shift at the bar today."
    j "Got it. Then I'll see you tomorrow, bro."
    mc "Yeah, see you tomorrow."
    mc "{i}Well, it's time to go to the club.{/i}"
    stop music fadeout 3.0
    jump day09_work


label day09_work:
    scene black with fade
    "Some time later."
    "You came to work, changed your clothes and headed straight to the bar."
    scene 9work01 with dissolve
    play music "music/6 - Positive Mood.ogg" 
    "When you were at the bar, you noticed a new security guard."
    mc "{i}And he's having a good time here, even poured himself a drink.{/i}"
    mc "{i}If memory serves me right, his name is Vincent.{/i}"
    mc "Hey, Vincent."
    scene 9work02 with dissolve
    v "What? Oh... It's you, [mc]."
    v "Sorry, I didn't notice you showed up."
    mc "Huh. Very strange, considering your position."
    scene 9work05a with dissolve
    v "I'm not on duty yet, so I took some liberties."
    scene 9work03 with dissolve
    mc "Yeah, I already noticed that."
    scene 9work04 with dissolve
    v "Yes... I'm sorry I used the bar without permission."
    v "Nobody was here, so I thought it would be okay if I poured myself a drink."
    mc "Don't worry about it. Better tell me what you're drinking."
    scene 9work03 with dissolve
    v "You mean that stuff?"
    v "Honestly, I don't even know what it is. I found it in the farthest, dustiest drawer."
    scene 9work04 with dissolve
    v "But don't worry, judging by the label, it's something very, very cheap."
    mc "Cheap and old? I see you like to take risks."
    scene 9work05 with dissolve
    v "Take a risk? Well, maybe just a little bit."
    v "But this stuff is so strong, I didn't even drink it."
    mc "Wise decision."
    scene 9work06 with dissolve
    "You walked into the bar and started getting ready for work."
    v "Hmm... Do you always come here so early? The opening will be in half an hour."
    mc "Yeah, I guess it's just-"
    stop music fadeout 3.0
    scene 9work06a with dissolve
    a "No! No! I already told you."
    mc "{i}I recognize that voice.{/i}"
    scene 9work07 with dissolve
    "You and Vincent noticed Anna coming down the stairs."
    scene 9work08 with dissolve
    a "What the hell do you think I should do now?"
    a "No, I told you it wouldn't work like that!"
    mc "{i}It seems like this phone call went really wrong for her.{/i}"
    scene 9work09 with dissolve
    play music "music/6 - Positive Mood.ogg"
    v "Looks like our boss isn't in a good mood today."
    mc "I guess you might be right about that."
    scene 9work10 with dissolve    
    a "Don't you dare hang up on me, I'm not done with you yet!"
    a "Hello? Hello?!"
    scene 9work11 with dissolve
    a "What an asshole!"
    scene 9work11a with dissolve
    a "God, I don't like unreliable people at all!"
    mc "{i}Wow, I wonder who screwed her up so bad.{/i}"
    scene 9work12 with dissolve
    "Anna's heavy eyes fell on a lonely glass on the bar."
    mc "{i}Oh, shit, I should have taken it away.{/i}"
    scene 9work13 with dissolve
    "The girl took a glass of alcohol in her hands and brought it to her lips."
    mc "{i}Huh?{/i}"
    scene 9work13a with dissolve
    "You didn't have time to blink before the glass was empty."
    scene 9work14 with dissolve
    "..."
    scene 9work15 with dissolve
    "*heavy sigh*"
    a "Ooh! That's some strong stuff, isn't it?"
    scene 9work14 with dissolve
    "..."    
    scene 9work16 with dissolve
    a "Hey, stop looking at me like that! I’ve had an extremely lousy day."
    mc "{i}Yeah, we can see that.{/i}"   
    mc "Did something happen?"
    scene 9work16a with dissolve
    a "Did something happen?"
    a "There's been a disaster, that's what happened! The jerk DJ just said he wasn't coming to his shift!"
    mc "{i}Oh... It seems to be a very unpleasant situation.{/i}"
    mc "{i}Especially for the manager who runs this whole place, that is, for Anna.{/i}"
    scene 9work17 with dissolve
    a "You know, I wouldn't even be mad at that idiot if he told me beforehand."
    a "But no! Why would he do that? It's better to call and say so twenty minutes before his shift. Probably decided to make me feel bad about it."
    a "Gosh, I'm so annoyed with unreliable people like him."
    scene 9work09 with dissolve
    v "Can't you just find someone to replace him?"
    scene 9work17 with dissolve
    a "Half an hour before the opening? I might as well start looking for a unicorn."
    "..."
    scene 9work18 with dissolve
    a "Wait a minute... I have an idea!"
    a "[mc]! You're a musician, please tell me you could replace him?"
    mc "Who? A unicorn?"
    a "DJ, of course!"
    mc "Uh... Actually, not every musician knows how to use a DJ's remote control."
    scene 9work18a with dissolve
    a "Oh, so you don't know?"
    mc "I didn't say that."
    mc "A long time ago I used to have some experience with this stuff at several house parties."
    mc "But we're talking about something more professional, right?"
    scene 9work18b with dissolve
    "Anna's thinking."
    a "Yeah, that's true..."
    scene 9work19 with dissolve
    a "Look, I know this whole situation is very uncomfortable, but I don't have any other choice right now. I need your help."
    a "Besides, today is a weekday and we shouldn’t be that busy."
    mc "{i}It's like this fact will make this job easier.{/i}"
    a "Just tell me, can you handle it? I wouldn't ask you to do that if it wasn't something very important."
    mc "Well... Purely hypothetically I think I can handle it, but..."
    scene 9work20
    a "Excellent! I knew I could count on you!"
    mc "Hey! Wait, don't be in a hurry to be happy."
    scene 9work20a with dissolve
    a "Uh...? What do you mean?"
    mc "Please don't think I don't want to help you, but if I'll be in charge of the music, who's gonna work at the bar?"
    mc "Like you said, there's not much time left before the opening. I'm not sure you'll be able to find a replacement for me in such a short time."
    scene 9work20 with dissolve
    a "Mm-hmm... Don't worry about it. I'll replace you myself."
    mc "{i}She?{/i}"
    a "This isn't the first time I'm gonna take over for one of the bartenders."
    mc "{i}This option somehow didn't even occur to me.{/i}"
    mc "So... you will really take over for me?"
    scene 9work18 with dissolve
    a "Haha! Didn't expect me to know how to do that?"
    mc "Actually, no."
    scene 9work21 with dissolve
    a "It may surprise you guys, but at the beginning of my career in this club I often had to work for the staff. Including the bartenders."
    mc "Impressive."
    a "Thank you."
    scene 9work22 with dissolve
    a "Okay, [mc], I'm gonna go change into work clothes. In the meantime, try to get the equipment sorted out, alright?"
    mc "Yeah, I'll try."
    a "Great!"
    stop music fadeout 3.0
    scene 9work23 with dissolve
    play music "music/8 - Intro Music.ogg"
    v "Yeah, well... I don't envy you, buddy."
    v "That's why when someone at work asks you if you know how to do something that is not part of your job, always say no."
    mc "That's a bit cynical."
    v "You say it's cynical, and I say it's practical. It will also save you a lot of time and nerves."
    if anna_sex == True:
        mc "Maybe so, but I have a slightly different situation here."
        scene 9work23a with dissolve
        v "Huh? Right! I forgot that you sleep together."
        mc "What? What makes you think that?" 
        v "Relax, I'm the only one who knows about this. And I don't care."
        mc "And what gave us away?"
        v "Let's not go into detail and just assume I'm very observant."
        mc "Well, If you say so."
    else:
        mc "Maybe so, but now it's too late to change anything."
        mc "Besides, maybe I'll get credit for it."
    scene 9work24 with dissolve
    v "Anyway, good luck with the DJ stuff."
    v "And I hope you know what you're doing, because if things go wrong, you'll take responsibility."
    mc "{i}Yeah, well... He's probably right about that.{/i}"
    v "Well, I'd better get to work, too, before somebody asks me to wear food and drink trays here."
    mc "Yeah, good luck."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 9work25 with dissolve
    mc "{i}So that's where I'm gonna be working today.{/i}"
    mc "{i}What a mess.{/i}"
    scene 9work26 with dissolve
    mc "{i}Shit, I have no idea where to start.{/i}"
    mc "{i}Okay, let's try to remember everything from the basics...{/i}"
    scene black with fade
    "A little more time later."
    scene 9work27 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    mc "{i}Okay, this one here... Yes, it seems to be good!{/i}"
    a "Oh, I see you've got almost everything figured out."
    scene 9work27a with dissolve
    mc "That's too much to say. It was pretty hard to understand how things work here. But I think I can do it."
    scene 9work27b with dissolve
    a "Awesome! You just have no idea how much you've helped me out."
    a "Catherine would have killed me if this whole situation hadn't been resolved." 
    scene 9work28 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    $ renpy.pause(delay=16)
    a "Well, what do you think? How do I look in my new bartender uniform?"
    mc "You look amazing. I think somebody's gonna get a lot of tips today."
    a "Haha! I could use a little extra cash."
    scene 9work29 with dissolve
    if anna_sex == True and anna_colleague == False:
        mc "Hmm... Don't you think I deserve some award for all these difficulties?"
        a "Ha ha! I see you are an enterprising man."
        scene 9work30 with dissolve
        a "And what would you like to get as your reward?"
        mc "{i}It's a pity that the opening will be in a couple of minutes, otherwise it wouldn't even be a question.{/i}"
        a "How about a kiss?"
        scene 9work30a with dissolve
        "A moment later, you and Anna's lips met together."
        a "Mmm..."
        scene 9work31 with dissolve
        a "Is that enough?"
        mc "It's definitely a good start, but..."
        a "Ha! Are you saying that's not enough for you?"
        mc "Yep."
        scene 9work33 with dissolve
        a "Okay, even though we have a little time left, as your manager, I have to motivate you for further work."
        mc "Well said!"
        scene 9work32 with dissolve
        "Anna went to the bar and gracefully curled her back."
        mc "{i}Ugh! I can't wait to see what she's up to!{/i}"
        mc "{i}Although... Maybe I should take part in it myself.{/i}"
        menu:
            "Be a part of the show (+Bad point)":
                $ badpoint += 1
                mc "{i}Yeah, I just can't stay out of it.{/i}"
                scene 9work34 with dissolve
                "You went up to Anna and put your hand on her waist."
                a "Hey, what are you doing?"
                mc "Shhhh.... Just relax."
                scene 9work35 with dissolve
                "..."
                scene 9work35a with dissolve
                mc "There you go."
                scene 9work36 with dissolve
                a "Ah!"
                scene 9work37 with dissolve
                a "Very brave of you to do this to your boss."
                mc "I don't think my boss is against it at all."
                a "Mm-hmm... She must like you very much if she didn't fire you for it."
                mc "Definitely."
                scene 9work38 with dissolve
                "Your hand is lying gently on Anna's firm ass."
                scene anim68 with dissolve
                a "Ahhhh... Please be gentle."
                mc "Whatever you say, baby."
                mc "{i}Anna's skin feels so soft... So I would stroke this beauty all day long.{/i}"
                a "Aaahhh... Come on, [mc]... Finish up, we have to go back--"
                stop music
                play sound "music/music_stop.wav"
                scene 9work44 with vpunch
                k "Anna. [mc]."
                scene 9work44a with vpunch
                "At the same moment, you and Anna stood at attention"
                mc "{i}Fuck, I hope she didn't notice anything.{/i}"
                k "..."


            "Just watch (+Good point)":
                $ goodpoint += 1
                mc "{i}No, I guess it's better not to get cocky in this situation and just keep watching.{/i}"
                scene 9work39 with dissolve
                "Anna sat on a chair and smiled widely."
                a "I hope you're happy that you made me do this."
                mc "Actually, you haven't done anything yet, but yes, I am! Hehe!"
                scene 9work40 with dissolve
                "The girl slowly started unbuttoning her vest."
                scene 9work40a with dissolve
                a "You want to see the rest of it?"
                mc "Of course I want to!"
                a "Mm-hmm... Then look carefully."
                scene 9work41 with dissolve
                a "Ta-da!"
                mc "{i}Oh... What an amazing view... There's no bra on her.{/i}"
                scene 9work42 with dissolve
                a "You know, you're lucky your boss lets you stare at her like that."
                mc "I think my boss likes it just as much as I do."
                scene 9work41 with dissolve
                a "Hehe! Maybe."
                scene anim69 with dissolve
                a "How about this?"
                mc "Uh... It's so good, almost hypnotizing."
                a "Haha! What a strange effect."
                a "Okay, I guess it's time to wrap this up, before-"
                stop music
                play sound "music/music_stop.wav"                
                scene 9work43 with vpunch
                k "Anna. [mc]."
                scene 9work43a with dissolve
                mc "{i}Fuck! I stared at Anna's breasts so intently that I didn't notice Catherine at all.{/i}"
                k "..."

        scene 9work45 with dissolve
        play music "music/8 - Intro Music.ogg"
        k "Have you dealt with our little problem?"
        a "Y-yeah, everything's fine now. Turns out [mc] is quite capable of replacing our DJ today."
        k "That's really good news. You've helped us out a lot, [mc]."
        scene 9work46 with dissolve
        k "Anna, make sure he's paid a bonus for this."
        mc "Yes... Ahem... She has already taken care of it."
        scene 9work46a with dissolve
        k "Well, that's good. If you need anything, I'll be in my office."
        scene black with fade
        "A few moments later."
        scene 9work47 with dissolve
        a "Oh, my God! My heart almost went to my heels when she said my name."
        mc "Yeah, that was close. But I didn't think she noticed anything."
        a "Probably. Because otherwise... Otherwise, I'm even afraid to imagine what would’ve happened here."
        a "Okay, I don't want any more surprises like that. We'd better get to work."
        mc "I agree."
    else:
        mc "Well, in that case, I wish you luck."
        a "Yeah, a little bit of luck wouldn't hurt either of us today."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 9work48a with dissolve
    play music "music/10 - Street's.ogg"
    "Very soon the club was filled with visitors, and you and Anna started your new duties."
    "To your surprise, you did a good job as a DJ."
    mc "{i}After all, It's not some complicated science, so it's not that hard to handle it.{/i}"
    scene 9work48 with dissolve
    "Anna, meanwhile, had no difficulty serving her clients, not yielding to the most skilful bartender."
    mc "{i}She wasn't lying when she said she was already in that position.{/i}"
    "Everything was going well."
    scene black with fade
    "Few hours later. End of shift."
    scene 9work49 with dissolve
    mc "Oh, here comes the best bartender in the world!"
    a "And the best DJ! Hehe!"
    mc "Yeah."
    mc "I think you and I did a pretty good job today, huh?"
    a "Oh, yes, we did!"
    a "If you want to know, I have hardly noticed the difference between your music and those so-called professional DJs who usually perform here."
    mc "{i}Huh. Either these guys perform so badly, or I'm pretty good at it.{/i}" 
    if anna_sex == True and anna_colleague == False:
        mc "{i}However, now I'm interested in a completely different question.{/i}"
        scene 9work50b with dissolve
        mc "Don't you think that even though we've decided to start a relationship, we spend so little time together?"
        scene 9work50a with dissolve
        a "Yeah, I guess... But apparently you have an idea?"
        scene 9work50b with dissolve
        mc "Yes, actually, I do."
        mc "How about we get together tonight and watch a movie? Or can we do something else..."
        scene 9work50 with dissolve
        a "Something else? Haha! Very tempting offer."
        mc "Then we have a deal?"
        a "Mm-hmm... Yes, I think so."
        scene 9work50a with dissolve
        a "Oh... One more thing. Catherine asked me to tell you to come into her office before you go."
        mc "Catherine?"
        mc "{i}I wonder what she wants from me.{/i}"
        mc "Okay, I hear you."
        mc "Will you wait for me? I'll be quick."
        a "Of course, I have to finish something here, too."
    else:
        scene 9work50b with dissolve
        mc "Do you need help cleaning up?"
        a "No, you don't have to. You've done enough for me today."
        a "Now you can go home."
        mc "Well, whatever you say."
        scene 9work50a with dissolve
        a "Hey, [mc]..."
        mc "Yes?"
        scene 9work50 with dissolve
        a "Thanks again for helping me today."
        mc "No problem."
        if jane_date_offer == True:
            scene black with fade
            "Soon you went home."            
            jump day09_home_night
        else:
            scene black with fade
            "Soon you went home."
            "There was a new day ahead of you."
            jump day09_pizza
    stop music fadeout 3.0
    scene black with fade
    "Like Anna told you, you went to Catherine's office."
    scene 9aw00 with dissolve
    "Suddenly you noticed a familiar face at the door of her office."
    mc "{i}Hey, what the fuck. Isn't that our old security guard and Anna's ex-boyfriend?{/i}"
    scene 9aw01 with dissolve
    t "Long time no see, kid."
    mc "..."
    scene 9aw02 with dissolve
    "..."
    mc "{i}I wonder why he came here.{/i}"
    play sound "music/knock.mp3"
    scene black with fade
    "Knock, knock!"
    k "Come in."
    scene 9aw03 with dissolve
    play music "music/15 - Deep Mood.ogg"
    mc "Catherine. You wanted to see me?"
    k "Ah, come on in, you're just in time."
    scene 9aw04 with dissolve
    k "If I get this right, you've helped Anna out a lot today."
    mc "Sort of. But it wasn't hard at all."
    k "Glad to hear it."
    scene 9aw04a with dissolve
    k "I know you're tired and want to go home, but I can't help but ask if you're okay here. Do you get along with your colleagues?"
    mc "{i}She wants to know how I'm doing?{/i}"
    mc "{i}I guess any good boss should periodically ask his staff about these things.{/i}"
    mc "Well, it's pretty good. Thank you for asking."
    k "Good... Very good."
    scene 9aw05 with dissolve
    k "Mind if I ask you one more question? It may seem a little unusual to you, though."
    mc "Um... Okay. No problem. Ask."
    k "Tell me, are you okay with Anna as a manager?"
    mc "{i}It's a really unusual question.{/i}"
    mc "Well, we get along well with each other, so my answer is yes."
    scene 9aw06 with dissolve
    "Catherine moves closer to you."
    k "And that week when I wasn't here? Was everything okay at the club?"
    mc "Wait a minute... Does this conversation have anything to do with that former security guard, Tom?"
    scene 9aw07 with dissolve
    k "Why did you ask about that?"
    mc "Because he was fired just after that very week. And also because I just saw him here on the way out."
    k "You're very aware."
    k "And yes, that's kind of why I'm asking you."
    scene 9aw08 with dissolve
    k "Don't get me wrong, there's no one more reliable than Anna for me personally. I just want to understand this whole situation."
    mc "Oh... I understand."
    mc "Then, if you ask me, Anna did the right thing. Tom was fired for a reason."
    k "Okay, I hear you."
    k "Is there anything else you want to tell me?"  
    mc "Um... Like what? "
    scene 9aw08a with dissolve
    k "Well... No means no."
    scene 9aw09 with dissolve
    "..."
    scene 9aw10 with dissolve
    k "Thank you for talking to me, [mc]. You can go now."
    k "Oh, yeah, if you don't mind, ask Anna to come over."
    mc "Yes, of course."
    scene black with fade
    "You walked out of Catherine's office and went back to the bar."
    mc "{i}Perhaps I should warn Anna about these weird questions.{/i}"
    scene 9aw11 with dissolve
    k "You're telling me you're okay with Anna..."
    scene 9aw11a with dissolve
    "*Click*"
    k "Yes... I can see that for myself."
    scene 9aw12 with dissolve
    k "And what should I do with you both?"
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    "You were sitting at the bar waiting for Anna to come back from Catherine's office."
    scene 9work51 with dissolve
    play music "music/8 - Intro Music.ogg"
    a "[mc]."
    scene 9work51a with dissolve
    mc "Oh, you're back."
    mc "How'd it go?"
    scene 9work52a with dissolve
    a "What? Oh, yeah. Yes, everything is fine."
    mc "Hmm? Are you sure? You look a little distracted."
    a "No, it's okay. Really."
    mc "Okay, whatever."
    mc "So, who’s place are we going to tonight? Your place or mine?"
    scene 9work52 with dissolve
    a "You know, let's not do this today."
    mc "Eh... Why?"
    mc "Is this because of Catherine?"
    scene 9work53 with dissolve
    a "No, she had nothing to do with it. I just changed my mind."
    mc "{i}I don't think I can believe it. Something clearly happened in that office, which is why her mood changed so dramatically.{/i}"
    mc "{i}I'm not sure I'm gonna get anything out of this right now, though.{/i}"   
    mc "Okay, if that's what you really want..."
    scene 9work52a with dissolve
    a "Thank you for understanding. And now, it would be better if we went home."
    mc "Yeah."
    mc "{i}Hmm... And what was that?{/i}"
    stop music fadeout 3.0
    scene black with fade
    "Still thinking about what just happened, you went home."
    if jane_date_offer == True:
        jump day09_home_night
    else:
        scene black with fade
        "There was a new day ahead of you."
        jump day09_pizza

label day09_home_night:
    scene black with fade
    "The same night. Julia's apartment."
    play music "music/6 - Positive Mood.ogg"
    scene 9julia01 with dissolve
    "*Sound of a new message!*"
    scene 9julia01a with dissolve
    sis "Hmm?"
    scene 9julia05 with dissolve
    sis "[mc]?"
    scene 9julia02 with dissolve
    sis "Hello."
    mc "Hey, sis. I'm sorry for calling so late, I hope I didn't wake you."
    sis "No, it's okay, I was watching TV."
    mc "Got it... The thing is I'm calling you about a very sensitive issue. I wanted to talk to you about Jane."
    scene 9julia03 with dissolve
    sis "Jane? What about her?"
    mc "The thing is, she and I had some kind of a date in your office the other day, but..."
    scene 9julia03a with dissolve
    sis "A date at the office?! I knew it!"
    mc "Um... I'm sorry, what?"
    scene 9julia03b with dissolve
    sis "Ahem... Never mind. Keep talking."
    mc "Okay."
    scene 8sms10 with dissolve
    mc "Well, it went pretty well, but I'm still afraid that if I don't do something about it, my relationship with her could get very confusing..."
    mc "I'd sort it out myself, but I don't want to look too obsessive in front of Jane. You know?"
    mc "That's why you have to help me."
    scene 9julia04 with dissolve
    sis "Help you? What do I get for it?"
    mc "Hey, aren't you the one who said that we couldn't do it without your help?"
    sis "I did, and I think I was already guiding you in the right direction."
    mc "Hmm... Then how about a little bribe? For example, a ticket to my next gig?"
    scene 9julia03 with dissolve
    sis "Well, you have to admit, that's not gonna be enough."
    mc "Come on, Julia! I know it's gonna be trivial for a relationship master like you."
    scene 9julia03a with dissolve
    sis "Oohh... Bribery and flattery, I see you've put everything you've got into it."
    mc "This is very important to me."
    scene 9julia03b with dissolve
    sis "Uh, okay... I think I can help you."
    mc "Great!"
    scene 9julia04 with dissolve
    sis "Tell me, are you working tomorrow night?"
    mc "Well, yeah, why?"
    sis "I think Jane and I will probably stop by your club."
    if anna_sex == True and anna_colleague == False:
        mc "Wait, wait! I don't think that's a good idea."
        scene 9julia03 with dissolve
        sis "You want me to help you, don't you?"
        scene 8sms10 with dissolve
        mc "Yeah, but-"
        sis "Then no objections!"
        mc "{i}Oh, man... I don't like the idea at all.{/i}"
        mc "{i}But maybe I'm winding myself up.{/i}"
    else:
        scene 8sms10 with dissolve
        mc "Uh... You think that's a good idea?"
        sis "Just trust me, okay?"
    mc "Okay, if you really think it's necessary, let's just keep it that way."
    scene 9julia02 with dissolve
    sis "That's good, then. Now, if you don't mind, I'll get back to my business."
    mc "Have a good night, sis."
    sis "Yeah, yeah. See you tomorrow."
    mc "See you tomorrow."
    stop music fadeout 3.0
    jump day09_pizza

label day09_pizza:
    scene black with fade
    "Next day."
    "As you agreed with Jacob and the other band mates, you were supposed to meet together at the pizza place."
    scene 9pizza01 with dissolve
    play music "music/16 - Bright Colors.ogg"
    "This time, you're one of the first to show."
    ls "Heeey, [mc]! I'm here!"
    ls "Come here!"
    scene 9pizza02 with dissolve
    mc "Hey, pretty girl."
    ls "Hehe! Hello to you too!"
    ls "Come sit next to me."
    mc "Sure."
    if lisa_path == True:
        scene 9pizza03 with dissolve
        "You sat next to Lisa and kissed her right away."  
        ls "Mmm..."
        mc "Oh... How much I missed that."
        scene 9pizza04 with dissolve
        ls "I missed you, too."
    else:
        scene 9pizza04 with dissolve
        "..."
    ls "So..."
    scene 9pizza05 with dissolve
    mc "You seemed to need time to figure out your studies. So, is everything okay now?"
    ls "I guess so, except for the fact that I almost lost my mind when I closed all my debts. But now I can say that everything is okay."
    scene 9pizza04 with dissolve
    ls "Now I'm ready to go back to our rehearsals!"
    mc "That's great!"
    ls "Yeah. And frankly, I can't wait to plunge into this whole musical life again."
    mc "I like your attitude."
    ls "Thanks."
    scene 9pizza04a with dissolve
    ls "Oh, by the way, while I was buried in my books, I had some ideas for a new song."
    mc "I hope it's not connected to studying and science and stuff like that."
    scene 9pizza04 with dissolve
    ls "What, you mean, these things aren't popular right now?"
    mc "In music? Well... Not really."
    scene 9pizza04b with dissolve
    ls "Hehe! Don't worry, that's not what my new song is about."
    mc "Oh, and what is it about then?"
    scene 9pizza04c with dissolve
    ls "Same as usual. Love, youth, parties, and everything related to it."
    mc "Ah! An eternal set of themes for a young musician. I approve! I'd be damn glad to hear that song."
    ls "Okay, you'll be the first to hear this song when I'm done."
    mc "Deal."
    scene 9pizza06 with dissolve
    j "Well, well!"
    j "Look, Jade, they're so into this conversation, they didn't even notice us."
    ls "Then you shouldn't be late!"
    j "Fair enough."
    mc "All right, guys, sit down and let's order something. I'm dying for pizza!"
    scene 9pizza07 with dissolve
    "Soon Jacob and Jade joined you, and all together, you started discussing the menu."
    "A few minutes later, you made your order, and kept talking about everything in the world."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 9pizza08 with dissolve
    play music "music/6 - Positive Mood.ogg"
    j "And I'm telling you, we just need to create fan pages with our band on the internet right now."    
    j "It's the only way to be popular now."
    j "Well, only if you don't do some completely insane stuff."
    scene 9pizza13 with dissolve
    mc "I agree with Jacob. Any road to popularity now lies through the Web."
    scene 9pizza09 with dissolve
    j "I knew you'd back me up, buddy!"
    scene 9pizza10 with dissolve
    jd "Look, I don't think any of us have any doubts about this. But wouldn't it be better to distribute the areas of responsibility in this case?"
    jd "In other words, who and for what will be responsible? At least at first."
    scene 9pizza09b with dissolve
    j "I'm in charge of the creative part!"
    scene 9pizza10a with dissolve
    jd "If you want, I can try to take over the financial role. The accounting and everything connected with it."
    scene 9pizza13 with dissolve
    mc "You sure about that? It's not as simple as it may seem."
    scene 9pizza10a with dissolve
    jd "Don't worry, I have some experience with things like that."
    scene 9pizza12 with dissolve
    ls "And if anything, you can always count on our help!"
    jd "Yes... Thank you."
    scene 9pizza13a with dissolve
    mc "Hmm... If everybody takes on some responsibilities, I can take the management. I think I can handle it."
    scene 9pizza11b with dissolve
    ls "Um... Then what should I do?"
    scene 9pizza08 with dissolve
    "*silence*"
    scene 9pizza11c with dissolve
    mc "You, Lisa, will be our main star. The face of our band."
    scene 9pizza11a with dissolve
    ls "And how is that?"
    mc "{i}She's seems interested in it.{/i}"
    mc "As far as I know, you've got more subscribers on social media than all of us combined."
    scene 9pizza11c with dissolve
    ls "Yeah, but I never really got into it."
    mc "And now, with our help, you will."
    scene 9pizza11a with dissolve
    ls "Okay. Sounds like fun, I'm in!"
    scene black with fade
    "Some time later."
    scene 9pizza09 with dissolve
    j "By the way, I have two more bits of news. One is good, and the other is... The other is just okay."
    j "What news should I start with?"

    $ question01_day09a = False
    $ question01_day09b = False    
    menu question01_day09:
        "Good one" if question01_day09a == False:
            scene 9pizza13a with dissolve
            if question01_day09b == False:
                mc "Start with the good one."
            else:
                mc "And the second bit of news?"
            scene 9pizza09c with dissolve
            j "Okay."
            j "I know we haven't been able to celebrate together since our last gig..."
            scene 9pizza11 with dissolve
            ls "By the way, it didn't work out just because of you."
            scene 9pizza09a with dissolve
            j "Yes... Yes, I know. Thank you for reminding me."
            scene 9pizza11 with dissolve
            ls "You're welcome."
            scene 9pizza09c with dissolve
            j "However, an old friend of mine and [mc] is throwing a party in two days, and he invited all of us."
            scene 9pizza13a with dissolve
            mc "Who exactly are we talking about?"
            scene 9pizza09b with dissolve
            j "About Little Barry."
            scene 9pizza11 with dissolve
            ls "Little Barry?"
            scene 9pizza11a with dissolve
            mc "Don't be fooled by that nickname. He weighs as much as Jacob and I put together."
            scene 9pizza13 with dissolve
            mc "Damn, it's been a while since I've seen him! So you're saying he's having a party in two days?"
            scene 9pizza09 with dissolve
            j "Yep! A whole bunch of people are coming. We just have to be there!"
            scene 9pizza13 with dissolve
            mc "I agree with you. I think we should all go there. This guy really knows how to throw a party!"
            scene 9pizza11a with dissolve
            ls "In two days? I think I can go."
            scene 9pizza13a with dissolve
            mc "What about you, Jade?"
            scene 9pizza10a with dissolve
            jd "I think I can go, too."
            scene 9pizza09 with dissolve
            j "That's great! That's where we'll all have fun together!"
            $ question01_day09a = True
            if question01_day09b == False:
                mc "{i}Okay, now I want to know what the second bit of news is.{/i}"           
            jump question01_day09

        "The usual news" if question01_day09b == False:
            scene 9pizza13a with dissolve
            if question01_day09a == False:
                mc "Start with the usual one."
            else:
                mc "And the second bit of news?"
            scene 9pizza09c with dissolve
            j "Okay."
            j "Tomorrow morning, we'll have to go to the club where we performed, pick up the fee and talk to the owner. I think he wanted to discuss something."
            mc "So."
            scene 9pizza09a with dissolve
            j "I'd go and find out myself, but I have a job tomorrow..."
            j "Besides [mc] has now taken on the role of manager... That's why..."
            mc "{i}What a smartass!{/i}"
            scene 9pizza13a with dissolve
            mc "Okay, okay, I get it! I'll do it myself."
            scene 9pizza09 with dissolve
            j "Great! I knew I could count on you, bro!"
            scene 9pizza10 with dissolve
            jd "I'm not busy tomorrow. If you want, I can go with you."
            scene 9pizza13 with dissolve
            mc "I'd love any company."
            scene 9pizza11c with dissolve
            ls "Damn, I'd go with you, too, but I've got college."
            mc "Don't worry, Jade and I will handle this."
            scene 9pizza10a with dissolve
            jd "So we'll meet tomorrow morning?"
            mc "Yeah."
            $ question01_day09b = True
            if question01_day09a == False:
                mc "{i}Okay, now I want to know what the second bit of news is.{/i}"
            jump question01_day09

    stop music fadeout 3.0
    scene 9pizza08 with dissolve
    "After a little more chat with the guys, you remembered you had to go to work."
    scene 9pizza13a with dissolve
    mc "Okay guys, it’s been fun, but I gotta go."
    scene 9pizza11b with dissolve
    ls "Already?"
    mc "Sorry, but duty calls."
    scene 9pizza13 with dissolve
    mc "I'll see you all later!"
    "Bye, [mc]! See you later, bro. Bye."
    if jane_date_offer == True:
        jump day09_work_with_jane
    elif anna_sex == True and jane_date_offer == False:
        scene black with fade
        "The whole next night you were working at the club as usual, but to your surprise, you haven't been able to talk to Anna."
        "It became obvious that she was avoiding you."
        mc "{i}I don't know what's gotten into her, but if this keeps up, I'm gonna have to do something about it.{/i}"
        "Soon you finished your shift and went home. The day was coming to an end."
        jump day09_home_jade
    else:
        scene black with fade
        "You've been working at the club all night."
        "Soon after your shift ended, you came home."
        "There was a new day ahead of you."
        jump day09_home_jade

label day09_work_with_jane:
    scene black with fade
    "Some time later. Club."
    play music "music/10 - Street's.ogg"
    scene 9bar01 with dissolve
    "You didn't have a lot of work to do, so you had time to think about a lot of things."
    if anna_sex == True:
        mc "{i}Anna's been avoiding me all day, and it's clearly connected to the night she went to see Catherine.{/i}"
        mc "{i}I don't know what's gotten into her, but if this keeps up, I'm gonna have to do something about it.{/i}"
        mc "{i}And that's not all the trouble that's supposed to happen to me today.{/i}"
        mc "{i}Julia has to come here with Jane.{/i}"
        "..."
        mc "{i}Yeah, well... Maybe it's a good thing that Anna is avoiding me.{/i}"
    scene 9bar01a with dissolve
    "Suddenly you noticed a group of girls you've been waiting for."
    mc "{i}There they are...{/i}"
    if nicole_plus == True:
        scene 9bar02 with dissolve
        mc "{i}Uh... I can't help but notice that they look stunning.{/i}"
        mc "{i}But how did Nicole end up in this company?{/i}"
        sis "And remember, Nicole, since you're here with us, imagine we're just three friends who decided to get together."
        jn "Yeah, that's our old rule at these meetings. Not a word about work."
        n "Hmm... I think I can handle it."
        sis "Well, that's great!"
        scene 9bar03 with dissolve
        mc "{i}Oh... I think Julia noticed me.{/i}"
        scene 9bar03a with dissolve
        sis "Nicole, would you grab us a table, please? Jane and I need to go say hello to someone."
        n "All right, no problem."
        mc "{i}Yeah, definitely noticed.{/i}"
    else:
        scene 9bar02a with dissolve
        mc "{i}Uh... I can't help but notice that they look stunning.{/i}"        
    scene 9bar04 with dissolve
    mc "What are the two most beautiful girls in this city doing in this little bar?"
    sis "Hello, brother."
    jn "Hey, [mc]."
    jn "Believe it or not, Julia chose this bar by accident."
    sis "Hey, that's the truth! And as you can see, I didn't miss it at all."
    jn "Yeah, that's for sure."
    scene 9bar05 with dissolve
    if nicole_plus == True:
        sis "Well, now I've said hello, I think I'm gonna go back to Nicole. But I think you two have something to discuss."
    else:
        sis "Well, now I've said hello, I think I'm gonna take a table for Jane and I. But I think you two have something to discuss."
    sis "It was nice to see you, [mc]."
    mc "Yeah. Don't drink too much, sis."
    scene 9bar05a with dissolve
    "Julia's gone, leaving you with Jane."
    jn "So..."
    mc "Yeah..."
    jn "So this is where you work right now?"
    mc "Well, it's more like a part-time job. But yes..."
    "..."
    mc "{i}Hell, I don't know why, but this whole conversation isn't working out at all.{/i}"
    mc "{i}Maybe I should remind her of our last conversation where she promised to think about our relationship. Or maybe I should postpone it for later?{/i}"
    menu:
        "Talk about your relationship":
            mc "{i}Still, it's better to know everything now. I don’t know when I’ll get a better time than this.{/i}"
            scene 9bar08 with dissolve
            mc "Look, Jane, while you're here, I was wondering if you thought about what we talked about last time."
            scene 9bar08a with dissolve
            jn "Oh... You are talking about..."
            jn "Yeah, I've been thinking about it, but I haven't decided anything yet."
            jn "And I already told you I need more time. I thought you understand that."
            mc "Yes, of course."
            jn "Okay."
            "..."
            jn "I think I'm gonna go back to the girls."
            mc "{i}Yeah, well... It doesn't seem to have gone well.{/i}"

        "{color=#66FF33}Postpone the conversation about the relationship":
            $ RPjn += 1
            mc "{i}No, I guess I shouldn't push her right now. In the end, she came here to have fun.{/i}"
            scene 9bar08 with dissolve
            mc "Look, I feel like I'm distracting you from your long-awaited break."
            jn "No, you're not distracting me at all..."
            scene 9bar05a with dissolve
            mc "No, no! You came here to have fun with your friends, and I don't want to distract you from that."
            mc "If you want, we'll talk later, but in the meantime, you should get back to them."
            mc "{i}I hope that sounded sincere.{/i}"
            scene 9bar08 with dissolve
            jn "Okay, I'll do that... And thank you for not pushing."
            mc "No problem."

    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    if nicole_plus == True:
        scene 9bar09 with dissolve
    else:
        scene 9bar09a with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "{i}Hmm... Looks like the girls are having fun.{/i}"
    mc "{i}Although considering how much time they spend in the office it's even good. I'm sure with their work schedule such bar hikes aren't that common.{/i}"
    mc "{i}But I still can't believe Julia brought them here.{/i}"
    "..."
    mc "{i}Well, stop staring, I've got to get on with my business.{/i}"
    scene black with fade
    "A little more time later."
    if nicole_plus == True:
        scene 9bar11 with dissolve
        n "[mc]."
        mc "Oh, Nicole."
        mc "You look great."
        n "Um... Thank you."
        mc "I have to say, I didn't expect to see you in a company like this."
        n "Yeah, it's a little unusual for me, too."
        mc "Can I get you something?"
        n "A glass of champagne, please."
        scene 9bar12 with dissolve
        mc "Here you go."
        n "Thank you."
        scene 9bar14 with dissolve
        mc "So, where's Jane and Julia now?"
        n "They've gone dancing."
        mc "Okay, I see."
        scene 9bar10 with dissolve
        "You looked at the dance floor."
        jn "Whoo-hoo!"
        mc "{i}Well, like I said, they're working hard, so it's no wonder they're relaxing.{/i}"
        scene 9bar14 with dissolve
        mc "And why didn't you join them?"
        scene 9bar14a with dissolve
        n "You sound just like your sister."
        n "I'll tell you what I said to her, dancing is not for me."
        mc "You sure about that?"
        n "Definitely."
        mc "Well, as you wish."
        scene 9bar13 with dissolve
        "..."
        scene 9bar14 with dissolve
        n "It's unusual for Julia to choose this place by accident today. It's all because of Jane, isn't it?"
        mc "Yeah, probably..."
        n "You two aren't doing so well?"
        mc "Not quite."
        mc "I've tried a lot of things, but I can't go beyond a certain level with her."
        n "Hmm... I'm not very good at giving advice, but I think it's best if you to not push her now. This is a very important step for her."
        mc "An important step? Why is that?"
        scene 9bar14a with dissolve
        n "You really don't know that, do you?"
        n "Not only are you as different as day and night, but you're her best friend's little brother. Not to mention the fact that she's just older than you."
        mc "Well, if you look at it that way-"
        scene 9bar14 with dissolve
        n "But that's the way she looks at it."
        mc "Okay, I hear you. Thank you for the advice."
        n "You're welcome. And good luck."
        scene 9bar13 with dissolve
        "..."
    else:
        scene 9bar10 with dissolve
        "You looked at the dance floor."
        jn "Whoo-hoo!"
        mc "{i}Well, like I said, they're working hard, so it's no wonder they're relaxing.{/i}"
    stop music fadeout 3.0        
    scene black with fade
    "Some time later."
    play music "music/10 - Street's.ogg"
    if nicole_plus == True:
        scene 9bar15 with dissolve
        mc "Wait... You're leaving now?!"
        sis "Yeah. You didn't think we'd be here till closing, did you? We have to get to work tomorrow morning."
        sis "But if you're interested, we had a great time."
        sis "Bye, brother."
        n "See you later, [mc]."
        scene 9bar16 with dissolve
        "..."
        mc "{i}Hmm?{/i}"
        scene 9bar17 with dissolve
        sis "Jane, are you coming?"
        scene 9bar18 with dissolve
        jn "Yes, you go ahead, I'll catch up with you later."
        scene 9bar17 with dissolve
        sis "..."
        sis "Okay."
    else:
        scene 9bar15a with dissolve
        scene 9bar15 with dissolve
        mc "Wait... You're leaving now?!"
        sis "Yeah. You didn't think we'd be here till closing, did you? We have to get to work tomorrow morning."
        sis "But if you're interested, we had a great time."
        sis "Bye, brother."
        scene black with fade
        "Julia left you and Jane alone."    
    scene 9bar08 with dissolve
    jn "You didn't think I'd leave without talking to you, did you?"
    mc "No, but I was beginning to worry about it."
    jn "Haha! No, I wouldn't do that to you."
    scene 9bar06 with dissolve
    jn "You know, I've been thinking a lot about us lately."
    jn "I've been thinking about how we spend our time, how we feel about each other, and what will happen to us next."
    mc "And what did you decide?"
    "..."
    jn "Free up your Friday night next week."
    mc "What for?"
    jn "For a date of course. I'll tell you everything right there."
    mc "{i}Hmm... It's definitely a good sign. If she wanted to turn me down, she wouldn't have asked me out on any dates.{/i}"
    scene 9bar07 with dissolve 
    "You put your palm on Jane's hand."
    mc "Okay, but after this date, you can't get away from me anymore."
    jn "Mm-hmm... If everything goes well, you may well be right."
    scene 9bar08 with dissolve
    jn "Now, goodbye."
    mc "Yeah, goodbye."
    stop music fadeout 3.0
    scene black with fade
    "Soon you finished your shift and went home. The day was coming to an end."
    jump day09_home_jade

label day09_home_jade:
    scene black with fade
    "Next morning."
    play sound "music/doorbell.wav"
    "Ding-dong!"
    mc "{i}Damn, who could it be so early?!{/i}"
    play sound "music/Door.wav" 
    scene 9jade01 with dissolve
    play music "music/7 - Just Happy.ogg"
    "..."
    mc "Jade?"
    mc "What are you doing here so early?"
    jd "..."
    scene 9jade03 with dissolve
    mc "Hellooo? Jade."
    scene 9jade02 with dissolve
    jd "Do you realize you're standing here without a T-shirt?"
    mc "Yeah, I forgot to wear it. Is it important?"
    scene 9jade04 with dissolve
    jd "Ahem... No... I guess it's not."
    jd "I hope you haven't forgotten, but you and I were supposed to go to the club today."
    mc "No, I remember. I just didn't think we'd go there so early."
    scene 9jade02a with dissolve
    jd "Um... It's too early?"
    scene 9jade03 with dissolve
    mc "Well, yeah. I wanted to call you in about an hour or two."
    scene 9jade02a with dissolve
    jd "Oh, I'm sorry, I thought the sooner we got through this, the better."
    jd "I'll come by later."
    scene 9jade03a with dissolve
    mc "Hold on! Don't fuss. Come on in, have some coffee with me, and then we'll go."
    scene 9jade05 with dissolve
    "Jade went to your apartment and modestly looked around."
    mc "Come on, sit down. Make yourself at home."
    jd "Okay." 
    scene 9jade06 with dissolve
    mc "Want some coffee?"
    jd "Yes, I wouldn't mind."
    mc "Okay, just a minute."
    scene 9jade07 with dissolve
    mc "Is there anything else you want? I had cookies somewhere."
    jd "No, one coffee will be enough."
    mc "As you wish."
    scene 9jade08 with dissolve
    mc "Here you go. Be careful it's hot."
    jd "Thanks."
    scene 9jade09 with dissolve
    "For a second, you looked down."
    mc "{i}Hmm... Not bad.{/i}"
    scene 9jade11 with dissolve
    mc "So, uh... Since it's just the two of us sitting here, do you mind if I ask you a few questions?"
    jd "Sure, ask."
    mc "Why did you decide to come with me?"
    scene 9jade12 with dissolve
    jd "I'm in charge of the finances, remember?"
    mc "I do. But I don't understand why you chose those responsibilities."
    jd "Well, I'm pretty good with numbers. For me It seemed easy enough."
    mc "Huh. Fair enough."
    scene 9jade10 with dissolve
    jd "And what about you? Why did you decide to take over as a manager?"
    mc "{i}That's a good question.{/i}"
    menu:
        "Everything else was taken":
            mc "I guess that's because everything else was taken."
            jd "Fair enough."
        "I'm good at this part":
            mc "My whole family is managers and businessmen. I'm good at this role."
            jd "How interesting."
        "You don't know why":
            mc "Honestly, I don't know why I offered myself in that role."
            jd "Hmm... Then let's hope you don't have any trouble with that."
            mc "Yeah."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 9jade13 with dissolve
    play music "music/12 - The Moose.ogg"
    jd "Are you sure we're not gonna be late?"
    mc "Nope. The last time Jacob and I went there, it was about the same time."
    jd "Oh, okay."
    mc "Shall we get a cab?"
    scene 9jade14 with dissolve
    jd "Cab? Why do we need it?"
    mc "What do you mean, why?"
    scene 9jade15 with dissolve
    mc "Oh!"
    "..."
    mc "Wait a minute, you really want us to ride this bike together?"
    jd "Well, yeah, why not?"
    mc "Um... I don't know."
    scene 9jade16 with dissolve
    "You came closer, and got a good look at it."
    mc "{i}Yes... That's a really nice thing. And it's very, very expensive.{/i}"
    scene 9jade17 with dissolve
    mc "Hmm... Okay, I don't mind, but only if I drive."
    jd "Not a chance! I'll be driving and I'll be the only one. This is not up for discussion."
    jd "Now get on the back."
    mc "{i}Looks like she really cares about her bike.{/i}" 
    mc "{i}But I can't blame her for that. If I were her, I would treat it the same way.{/i}"
    scene 9jade18 with dissolve
    mc "Yeah, well... I've never been driven by a girl on a motorcycle before."
    jd "Everything happens for the first time. Get on."
    mc "All right, then!"
    scene 9jade20 with dissolve
    mc "Mmm... Actually, it's pretty comfortable."
    jd "Of course it is. And now I advise you to hold on to me tighter."
    mc "It won't be difficult."
    scene 9jade19 with dissolve
    jd "Ohh..."
    mc "I'm sorry, did I hold you too tight?"
    jd "No, it's okay. Now let's go."
    stop music fadeout 3.0
    play sound "music/moto.mp3"
    scene 9jade21 with dissolve
    "*engine sound*"
    mc "Hehe! Let's go!"
    stop sound fadeout 3.0
    scene black with fade
    "Some time later, you arrived at your destination."
    scene 9jade22 with dissolve
    play music "music/6 - Positive Mood.ogg"
    jd "So, how was the ride? I hope it wasn't shaking too much?"
    mc "Are you kidding me? I loved it!"
    jd "You see, you were worried for nothing."
    mc "Yep."
    mc "All right, let's go. You said yourself, the sooner we start, the sooner we'll be done."
    scene 9jade23 with dissolve
    mc "Any thoughts on what they're gonna tell us?"
    jd "Maybe they want to offer another gig?"
    mc "Hmm... You're thinking very optimistic."
    jd "Maybe."
    scene 9jade24 with dissolve
    "Soon you were at the club, and the security guard showed you where to find the general manager, Oliver."
    jd "It's just like that night."
    mc "Yeah... But there are almost no people here."
    scene 9jade25 with dissolve
    mc "{i}Almost.{/i}"
    mc "{i}Hell, I recognize these weird guys.{/i}"
    mc "{i}Looks like they have something to do with Oliver, too.{/i}"
    scene 9jade26 with dissolve
    mc "Hey, if you want, we can talk to him after they leave."
    jd "No, it's okay. Let's go."
    scene 9jade27 with dissolve
    "{color=#FFA07A}Oliver{/color}" "...if everything goes smoothly, and if the second band agrees, you can expect to get paid well..."
    scene 9jade27a with dissolve
    "{color=#FFA07A}Oliver{/color}" "Oh, there they are."
    "{color=#FFA07A}Oliver{/color}" "You guys are just in time."
    scene 9jade28 with dissolve
    d "Well, well! Look who's here, it's an old friend of ours, Jade."
    jd "Hello, Derek. Michael."
    scene 9jade31 with dissolve
    "{color=#FFA07A}Oliver{/color}" "All right, folks, let's say hello to each other later. Now let's talk about the business."
    mc "Okay, we're listening."
    scene 9jade29 with dissolve
    "{color=#FFA07A}Oliver{/color}" "Again, for those of you who just got here."
    "{color=#FFA07A}Oliver{/color}" "A good friend of mine is looking for musicians to perform at his student club next weekend."
    "{color=#FFA07A}Oliver{/color}" "He liked your bands, and he wants you to be the one to do it."
    "{color=#FFA07A}Oliver{/color}" "Of course, you're gonna get paid for this."
    "{color=#FFA07A}Oliver{/color}" "But I'd like to warn you right away that since there will be fewer bands this time, the time of your performance will be longer."
    "{color=#FFA07A}Oliver{/color}" "So, what would you say to this?"
    scene 9jade33 with dissolve
    d "Hell, of course we're in!"
    mi "If you want, we can even do it alone."
    scene 9jade31 with dissolve
    "{color=#FFA07A}Oliver{/color}" "I like this energetic attitude, but either your bands are performing together, or no one is performing. These are the conditions."
    "{color=#FFA07A}Oliver{/color}" "Now what about you, [band_name]? Do you agree?"
    mc "{i}Hmm... I guess that's not such a bad offer.{/i}"
    scene 9jade32 with dissolve
    mc "I need to know if all my guys are free that day, but we'll probably give a positive answer."
    scene 9jade30 with dissolve
    "{color=#FFA07A}Oliver{/color}" "Okay, great! Just great!"
    "{color=#FFA07A}Oliver{/color}" "Then I'll give your contacts to my friend and he'll call you in the next few days."
    "{color=#FFA07A}Oliver{/color}" "Now come on, I'll give you your fee for your last gig."
    stop sound fadeout 3.0
    scene black with fade
    "Some time later. Near the club."
    scene 9jade34 with dissolve
    play music "music/10 - Street's.ogg"
    mc "Congratulations, you were right, this guy did offer us a new gig."
    jd "Honestly, I was a little surprised myself."
    mc "And yet your intuition hasn't let you down."
    mc "Any other thoughts on this whole new venture?"
    jd "Well... It seems like a good offer. But you did the right thing, that you decided to clarify whether everyone would be free on that day."
    mc "It seemed like an obvious decision to me. I don't want any surprises."
    jd "Yeah, that's the way it's supposed to be."
    scene 9jade35 with dissolve
    jd "Hm?"
    jd "[mc], look."
    scene 9jade36 with dissolve
    "Cat" "Meow!"
    mc "A cat."
    jd "Yeah."
    "Cat" "Meow!"
    jd "I think he wants to be petted."
    mc "And I think he just wants to eat."
    jd "I don't exclude that option."
    scene 9jade35 with dissolve
    jd "I'll pet him."
    mc "Just make sure he doesn't scratch or bite you. Who knows what he might be sick with?"
    jd "Don't worry, I'll be careful."
    scene 9jade37 with dissolve
    "Jade started petting the cat."   
    if lisa_path == True:
        mc "I know it's just a coincidence, but I saw exactly the same cat when I was in the park with Lisa a week ago."
    else:
        mc "Maybe it's just my imagination, but I feel like I've seen this cat before."
    mc "Hey, buddy, you're not following me, are you?"    
    jd "I don't think so. It's probably just an ordinary street cat. They often look like each other."    
    mc "Yeah, I guess so."
    scene 9jade39 with dissolve
    mc "So you like cats, huh?"
    jd "I like all the animals... Although I like dogs a little bit more."
    mc "I get it."
    jd "And which animal do you like?"
    menu:
        "Dogs":
            mc "I like dogs the most, too."
            jd "Huh. What an interesting coincidence."
            mc "Don't tell me."
        "Cats":
            mc "Well, my preferences here are pretty commonplace. I like cats."
            scene 9jade38 with dissolve
            "You noticed how the stray cat looked at you carefully."
            mc "Yeah, yeah, you furry asshole. I like cats, are you happy?"
            "Cat" "Meow!"
        "Fish":
            mc "Are the fish animals?"
            jd "Well, in some way they are."
            mc "Then I like fish. They are beautiful and easy to take care of. Perfect pets."
            jd "Huh. How unusual."
            mc "Don't tell me."
        "Hamsters":
            mc "Don't laugh, but my favorite animals are hamsters."
            jd "Hamsters? How unusual."
            mc "Yeah... I don't know why I like these little furry assholes so much."
    scene 9jade40 with dissolve
    "..."
    jd "I'm sorry to have to leave him like this."
    mc "Don't worry about him. He's been used to street life for a long time, so he'll be fine."
    scene 9jade40a with dissolve
    jd "I guess you're right."
    mc "Yeah. Come on. Let's go."
    stop sound fadeout 3.0
    scene 9jade41 with dissolve
    mc "Now that we're done here, what are you gonna do?"
    jd "I don't even know..."
    play music "music/8 - Intro Music.ogg"    
    scene 9jade41a with dissolve
    d "Don't slow down, man, or they'll go away."
    mi "Don't slow down yourself!"
    scene 9jade42 with dissolve
    d "Hey, are you guys leaving already? I thought we were gonna talk to each other as fellow musicians who will be performing together."
    mc "{i}Hell, I don't want to see their faces so badly.{/i}"
    mi "Yeah, folks, can we talk about this?"
    scene 9jade43 with dissolve
    jd "Sorry, but we're in a hurry."
    scene 9jade42
    d "Bullshit! You are in no hurry!"
    play sound "music/cat.mp3"
    scene 9jade44 with dissolve
    "*cat hiss*"
    scene 9jade45 with dissolve
    d "What the fuck?!"
    play sound "music/cat.mp3"
    scene 9jade44 with dissolve
    "*strong cat hissing!!!*"
    scene 9jade46 with dissolve
    play sound "music/cat2.mp3"    
    d "Fuck off, you stupid cat!"
    "Cat" "MEOW!!!"
    mc "{i}I didn't fucking want to get involved, but that asshole really got me.{/i}"
    scene 9jade48 with dissolve
    mc "Hey, man, what the fuck are you doing?!"
    scene 9jade49 with dissolve
    d "Hmm? Doing what?"
    scene 9jade48 with dissolve
    mc "I'm saying, why did you kick that cat?"
    scene 9jade49 with dissolve
    d "Why do you care? Or are you some kind of crazy Greenpeace guy?"
    scene 9jade48 with dissolve
    mc "And what if I am?"
    stop music fadeout 1.0
    scene 9jade49a with dissolve
    "..."
    scene 9jade51 with dissolve
    play music "music/8 - Intro Music.ogg"
    d "Pfft, relax! You shouldn't worry about it. Besides, I didn’t even hit it."
    scene 9jade50 with dissolve
    jd "Jeez, Derek, you haven't changed at all. Still the same insolent, spoiled and narcissistic type."
    mc "{i}Wow. It's not like Jade to say that about someone.{/i}"
    mc "{i}Apparently, he got to her pretty bad.{/i}"
    scene 9jade51a with dissolve
    d "Why on earth would I have to change? Believe it or not, I like who I am."
    d "Narcissistic, spoiled... And everything else that you said there."
    mc "{i}Perhaps she forgot adjective - narrow-minded.{/i}"
    d "In general, we just wanted to discuss the details of our gig with you, but now I have no desire to do so."
    scene 9jade47 with dissolve
    jd "Trust me, it's mutual."
    scene 9jade51a with dissolve
    d "Well, whatever."
    scene 9jade52 with dissolve
    d "See you next weekend, [band_name]."
    mi "Yeah, so long, losers."
    scene 9jade53 with dissolve
    mi "Hey, are you really gonna let them get away with this shit? That's not like you at all."
    d "Relax, man. We're performing together, remember?"
    d "We're colleagues now."
    mi "So what's the point?"
    d "You're such an idiot!"
    mi "Hey! You're an idiot yourself."
    d "If they can't perform next weekend, our band won't be needed there. We need these guys for this gig."
    mi "Yeah, but it's only gonna last until the gig, right? And after that..."
    scene 9jade54 with dissolve
    d "That's right, my friend. That's right."
    d "Right after the gig, we're all on our own."
    stop music fadeout 3.0
    scene black with fade
    "You waited until Derek and Michael got out of the alley."
    scene 9jade55 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Man, these guys are creepy."
    jd "Yeah, it's always been hard with them."
    mc "Is that why you left their band?"
    jd "Well, that was definitely one of the reasons."
    scene 9jade56 with dissolve
    mc "And what were the others?"
    jd "It's not as simple as it sounds."
    mc "{i}I don't even know what could be simpler.{/i}"
    stop music
    play sound "music/music_stop.wav" 
    scene 9jade57 with vpunch
    jd "What the hell?!"
    mc "{i}What the fuck?!{/i}"
    scene 9jade58 with dissolve
    play music "music/Maxim Nick - Falling Down.mp3"
    "Jade gently pushed her hand over the surface of the motorcycle."
    mc "{i}Looks like the scratches are deep. Someone spared no effort when he did it.{/i}"
    mc "{i}Why am I talking to someone, though? I know exactly what kind of freaks did it.{/i}"
    scene 9jade59 with dissolve
    "..."
    scene 9jade59a with dissolve
    mc "{i}Oh, shit, she looks like a puppy got hit by a bus right in front of her.{/i}"
    jd "Why do you think they did it?"
    mc "Because they're jerks, and these people don't need a reason."
    jd "But that's... Wrong."
    mc "Yes, it is."
    scene 9jade60 with dissolve
    "With a very upset look, Jade sat right on the curb."
    mc "{i}It hurts to look at it. Perhaps I need to cheer her up somehow.{/i}"
    mc "Mind if I sit next to you?"
    jd "Go ahead."
    scene 9jade62a with dissolve
    jd "I know it's just a stupid scratch and nothing really bad happened, but... But it's still a shame."
    mc "Hey, don't let those assholes get in your head."
    scene 9jade61 with dissolve
    mc "Besides, I'm not sure if, you know, but Jacob works at the workshop. If you ask him, he'll help you fix it."
    jd "Really?"
    mc "Don't even doubt it."
    scene 9jade62 with dissolve
    jd "That' s really good."
    mc "There you go, you're almost smiling!"
    scene 9jade62b with dissolve
    jd "I'm not!"
    mc "Yes you do! You should only see your smiling face right now."
    scene 9jade62 with dissolve
    jd "Thank you, [mc]."
    mc "Sure."
    if jade_kiss == True and RPjd >=2:
        scene 9jade64 with dissolve
        "Suddenly, Jade leaned over and looked right into your eyes."
        "And then..."
        scene 9jade67 with dissolve
        "...she kissed you."
        mc "{i}What's that?!{/i}"
        menu:
            "Stop that kiss":
                mc "{i}Hell, while it's nice, it's better to end it.{/i}"
                scene 9jade67a with dissolve
                "You've pulled away from Jade."
                "..."
                scene 9jade68 with dissolve
                jd "I'm sorry... I don't know what came over me. It was a mistake."
                "..."
                mc "{i}I don't need to put any pressure on her right now.{/i}"
                mc "Relax, you're just a little tired and upset."
                scene 9jade65 with dissolve
                jd "Yeah, yeah, that's right. That's what it is."
                jd "I'm sorry again about the whole scene."
                mc "It's okay."
                scene 9jade69 with dissolve
                jd "Okay, I think we should stop sitting here. Come on, I'll take you home."
                mc "{i}I'm not sure that's a good idea right now. I need some time to think things over.{/i}"
                mc "Thanks for the offer, but this time I'll get home on my own."
                jd "Hmm? Is it because I kissed you?"
                mc "What? No! Of course not!"
                jd "You're sure?"
                mc "Absolutely."
                jd "Oh, well okay then."
                scene 9jade70 with dissolve
                jd "Thank you for everything you said to me today [mc]."
                mc "You're welcome. And have a good ride."
                scene 9jade71 with dissolve
                "Soon Jade left."
                mc "{i}Ehh... What was that? And what's more important, how do i have to behave next to her from now on?{/i}"
                stop music fadeout 3.0
                mc "{i}Yeah... Questions.{/i}"
                scene 9jade72 with vpunch
                "Man" "Hey, kid, what the hell are you doing on the curb? People are actually walking here!"
                mc "Uh... I'm sorry."
                "Man" "What an ill-mannered young man!"
                "Man" "I didn't allow myself to do that when I was your age, and I didn't even-"
                mc "{i}Oh, my God, I'd better get out of here before this grandpa pisses me off.{/i}"

            "{color=#66FF33}Answer a kiss":
                $ jade_path = True
                mc "{i}What the hell, it's too good to end it right now.{/i}"
                scene 9jade66 with dissolve
                jd "Mmm..."
                mc "{i}Yes... It's hard to resist.{/i}"
                scene 9jade67a with dissolve
                "A few seconds later, Jade stopped."
                "..."
                scene 9jade68 with dissolve
                jd "I'm sorry... I don't know what came over me. It was a mistake."
                mc "Ahem! Very pleasant mistake."
                jd "Yes, I guess so..."
                scene 9jade65 with dissolve
                jd "Please don't tell Lisa about this."
                mc "Don't worry, I won't."
                jd "Thank you."
                scene 9jade69 with dissolve
                jd "Okay, I think we should stop sitting here. Come on, I'll take you home."
                mc "{i}I'm not sure that's a good idea right now. I need some time to think things over.{/i}"
                mc "Thanks for the offer, but this time I'll get home on my own."
                jd "Hmm? Is it because I kissed you?"
                mc "What? No! Of course not!"
                jd "You're sure?"
                mc "Absolutely."
                jd "Oh, well okay then."
                scene 9jade70 with dissolve
                jd "Thank you for everything you said to me today [mc]."
                mc "You're welcome. And have a good ride."
                scene 9jade71 with dissolve
                "Soon Jade left."
                mc "{i}Ehh... What was that? And what's more important, how do i have to behave next to her from now on?{/i}"
                stop music fadeout 3.0
                mc "{i}Yeah... Questions.{/i}"
                scene 9jade72 with vpunch
                "Man" "Hey, kid, what the hell are you doing on the curb? People are actually walking here!"
                "Man" "What an ill-mannered young man!"
                "Man" "I didn't allow myself to do that when I was your age, and I didn't even-"
                mc "{i}Oh, my God, I'd better get out of here before this grandpa pisses me off.{/i}"

    else:
        scene 9jade63 with dissolve
        "Suddenly, Jade leaned over and put her head on your shoulder."
        scene 9jade63a with dissolve
        jd "You don't mind if we sit like this for a bit?"
        mc "Sure. I'm in no hurry."
        scene 9jade63 with dissolve
        "..."  
        scene 9jade69 with dissolve
        jd "Okay, I think we should stop sitting here. Come on, I'll take you home."
        mc "Thank you, but this time I'm probably gonna get home on my own."
        jd "Hm? You're sure?"
        mc "Absolutely."
        jd "Oh, well okay then."
        scene 9jade70 with dissolve
        jd "Thank you for everything you said to me today [mc]."
        mc "You're welcome. And have a good ride."
        stop music fadeout 3.0    
    
    scene black with fade
    "A few minutes later, you were on your way home."
    if selina_path == True or rosa_path == True:
        jump day09_neighbors
    else:
        "You spent the rest of the night perfecting your bass guitar playing."
        "There was a new day ahead of you."
        jump day09_lisa_home

label day09_neighbors:
    scene black with fade
    "When you got home, you changed clothes and went to Rosa and Selina."
    "That's the day you were supposed to go with them to the city's fine arts exhibition."
    mc "{i}I think I'm just in time.{/i}"
    play sound "music/doorbell.wav"
    "Ding-dong!"
    s "Just a minute, I'm coming!"
    play sound "music/Door.wav"
    scene 9neighbors01 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    s "Oh, [mc]! You came just in time!"
    s "I see you're well dressed for this occasion."
    mc "Well, I couldn't go to such a responsible event in my usual clothes."
    mc "And I see you look pretty sophisticated today, too."
    scene 9neighbors04 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    $ renpy.pause(delay=16)  
    s "Do you like it?"
    mc "Of course I do!"
    if selina_broke_up == False:
        scene 9neighbors02a with dissolve
        s "Mm-hmm... I love it when you praise me."
        mc "Any time."
        s "I think you deserve a kiss for such a good start to the evening."
        scene 9neighbors02 with dissolve
        s "Mmmm..."
        mc "{i}Though this kiss is really short, it is very pleasant.{/i}"
        scene 9neighbors02a with dissolve
        s "Yeah, that's much better!"
        s "Now let's go inside."
    else:
        scene 9neighbors03 with dissolve
        s "Thank you, [mc]."
        s "Now, don't stand in the hallway and come inside."
        mc "Huh. Right."
    scene 9neighbors05 with dissolve
    "When you got to the apartment, Selina immediately told you that you'd have to wait some time."
    mc "{i}I was too naive when I thought they were ready... I guess I was in a hurry with my conclusions.{/i}"
    mc "{i}....{/i}"
    scene 9neighbors06 with dissolve
    r "Ahem!"
    mc "{i}Oh, they're finally finished.{/i}"
    mc "{i}Damn, how hot Selina's mom is! If I didn't know who she really was, I'd probably assume it was her older sister.{/i}"
    scene 9neighbors07 with dissolve
    if rosa_path == True:
        r "Thank you for accepting my invitation, [mc]. I think you'll like what you'll see today."
        mc "{i}Is it just me or did it sound a little ambiguous?{/i}"
        mc "{i}Okay, I need to answer her.{/i}"
        mc "No problem. I was too interested to give it up."
        r "I'm glad to hear that."
    else:
        r "Thank you for keeping Selina company. I don't know why, but she feels uncomfortable at such events."
        s "Mom!"
        mc "No problem. I'm interested in going to this exhibition myself. Not to mention such a pleasant company."
        r "I'm glad to hear that."
    scene 9neighbors08 with dissolve
    s "I don't want to interrupt your sweet exchange of courtesies, but maybe we'll just go."
    r "I didn't know you were in such a hurry."
    s "I'm not, I just want to get this over with."
    r "Well, I'm ready to go now."
    scene 9neighbors08a with dissolve
    r "What about you [mc]?"
    mc "I've been ready since I got here."
    s "Okay, great! Then if no one has any urgent business left, let's go."
    stop music fadeout 3.0
    scene black with fade
    "A few minutes later, you went outside."    
    scene 9neighbors09 with dissolve
    play music "music/10 - Street's.ogg"
    "As it turned out in the course of further conversation, it was Rosa who was to take you to this gallery."
    mc "Wow, what a great car! Looks like painting is a very profitable occupation these days?"
    r "Only if you're really good at it. Otherwise, you'll only get a used bike."
    scene 9neighbors09a with dissolve
    s "My mother and I often disagree, but even I can confirm that she is a very popular painter."
    s "You'd be surprised how many fan groups and fan sites dedicated to her and her work exist on the Web."
    mc "That's interesting."
    scene 9neighbors10 with dissolve
    r "How long are you gonna stand there and talk? You just rushed me."
    s "Yeah, yeah, we're coming."
    scene 9neighbors09a with dissolve
    s "Hey, you mind if we both sit in the backseat?"
    mc "Um... Sure, I don't see any reason to be against it."
    s "Okay, great. Let's go!"
    scene 9neighbors12a with dissolve
    "You and Selina got into the car, and the three of you went to the exhibition."
    scene 9neighbors11 with dissolve
    s "Oh, yeah, I'd like to warn you both that I'm probably gonna have to leave a little early today."
    mc "What? Why?"
    s "Alas, but I have an evening shift at the hospital."
    mc "Hmm... Hard everyday medical work?"
    s "Yeah, something like that."
    scene 9neighbors11a with dissolve
    r "I still don't understand why you chose such a boring profession for yourself."
    s "Well, not everybody in this family wants to paint other people's naked asses. Someone wants to benefit society."
    r "Yeah, yeah... We have to understand that someone wants to treat these naked asses."
    s "I'm glad you realize that."
    scene 9neighbors12 with dissolve
    s "By the way, [mc], what do you think about that? Which profession do you like more?"
    mc "{i}Yeah, well... What an uneasy question.{/i}"
    menu:
        "An artist's profession":
            $ RPr += 1
            mc "I'd be lying if I said I didn't respect the profession of doctor. But still, I'm more attracted to creativity."
            mc "So yes, I like the profession of an artist a little bit more."
            scene 9neighbors11a with dissolve
            r "It's nice to know you have a similar opinion with me, [mc]."
            s "Pfft! You can say whatever you want, but the next time you two have a stomach ache, the first thing you do is run to do an X-ray, not a stomach drawing."
            mc "Huh. Can't argue with that."
        "The doctor's profession":
            $ RPs += 1
            mc "Despite the fact that I am a musician myself and have great respect for all creative professions, I believe that the profession of doctor is much more important than music and fine arts."
            scene 9neighbors11a with dissolve
            r "Very tactful answer, [mc]."
            mc "Thanks, I guess."
    stop music fadeout 3.0
    scene 9neighbors13 with dissolve
    "Continuing to talk on various topics, you soon arrived at the venue of the exhibition."
    r "Well, here we are. Everybody out."
    if selina_broke_up == True:
        scene 9neighbors14a with dissolve
    else:
        scene 9neighbors14 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "So this is where this famous gallery is located?"
    r "That's right. All the biggest events in the life of fine arts are usually held here."
    r "Many young artists can only dream that their work would become part of an exhibition like this one."
    mc "What about your paintings? Have they been to this gallery before?"
    r "Yeah, it's happened a couple of times."
    s "Mom's being modest, she's a regular guest here."
    mc "{i}First the fan groups and fan sites on the internet, and now this. It seems like Rosa is a celebrity in some way.{/i}"
    r "Okay, enough standing here, let's get in there."
    scene 9neighbors15 with dissolve
    "The next moment, the three of you went inside the gallery."
    mc "{i}Well, I hope this evening goes well.{/i}"
    stop music fadeout 3.0
    jump day09_exhibition


label day09_exhibition:
    scene black with fade
    "Some time later."
    scene 9exhibition01 with dissolve
    play music "music/3 - Dream With U.ogg"
    s "Wow, there's a lot of people here."
    r "Yeah, I guess most of the visitors are already here. Although there will undoubtedly be those who will show up later."
    s "Yeah, whatever you say... Better tell us, what are we going to do here?"
    scene 9exhibition02 with dissolve
    r "I suggest we split up for a while."
    r "I need to go say hello to a couple of people I know. In the meantime, you guys can walk around and look at the works of local artists."
    r "Maybe you'll find something interesting for yourself."
    scene 9exhibition01 with dissolve
    s "Okay, that's what we're gonna do."
    mc "Then we'll see you later."
    r "Yeah, I'll find you."
    scene 9exhibition03 with dissolve
    "Selina grabbed your hand and walked you through the gallery."
    s "How about we start on the left side of the hall?"
    mc "I haven't been here before, so I'll trust your instincts."
    s "Great decision!"
    scene 9exhibition04 with dissolve
    "You've got the first painting in your path."
    s "So, what do you think of it?"
    mc "I like this composition. The colors are bright. The strokes are wide."
    s "Huh. You say that as if you really understand something about it."
    s "Personally, all I see here is a sexy woman's ass."
    mc "Well, the truth is, so am I."
    s "Hehe! I knew it."
    s "Let's go see the next painting."
    scene 9exhibition04a with dissolve
    s "What about this one? Just be honest."
    mc "Honestly, it's a little too conceptual."
    mc "Not to mention that creepy face."
    s "Hmm... I agree with you there it looks really creepy."
    s "Let's move on."
    scene 9exhibition04b with vpunch
    mc "{i}OH, MY GOD!{/i}"
    mc "{i}What the fuck is this?!{/i}"
    mc "Can anyone in their right mind call this art?"
    scene 9exhibition05 with dissolve
    s "And what don't you like about it? There is a girl. There is nudity. Everything is exactly as you like it!"
    mc "Nope. No, no! I definitely don't like it."
    s "Ha! You're so picky."
    s "Okay, let's see what the next painting is... Maybe it will help us forget this... thing."
    mc "I hope so."

    if rosa_path == True:
        scene 9exhibition06 with dissolve
        mc "Hmm... And this painting I like very much."
        s "Yeah."
        s "The models look especially good here."
        mc "Especially the female model."
        s "Yes, I kinda agree with that."
        mc "{i}Huh, what a smart-ass!{/i}"
        scene 9exhibition08 with dissolve
        s "In fact, it's kinda weird to look at my half-naked self with so many people around..."
        scene 9exhibition07 with dissolve
        s "I'm not sure I'd have the guts to come here without you."
        mc "Then I'm glad you're with me."
        s "Yeah, me too."
        scene 9exhibition09 with dissolve
        s "On the other hand, though... All this turns me on a little bit."
        mc "Really?"
        s "Well, yeah. Think how many people have seen us naked against each other today."
        mc "{i}I guess I won't bore her with the fact that we were actually dressed.{/i}"

    else:
        scene 9exhibition06a with dissolve
        mc "Hmm... And this painting I like very much."
        s "You might be surprised, but my mother painted it."
        mc "Really?"
        s "Yep."
        scene 9exhibition08 with dissolve
        s "Honestly, it's a little strange to see your mom paint naked people, and everyone around admires it..."
        scene 9exhibition07 with dissolve
        s "Imagine if she'd painted us like that."
        mc "I think we'd look great together."
        s "Mm-hmm... Perhaps..."
        scene 9exhibition09 with dissolve
        s "Now that you've said so... I think it would be really hot."
        mc "Oh, really?"
        s "Think about how many people would see us naked against each other."
        mc "{i}Okay, I guess I'll have to admit it would be really hot.{/i}"
  
    s "You know, I had an idea... How about we find some quiet place and then..."
    r "There they are!"
    stop music fadeout 3.0
    scene 9exhibition10 with dissolve
    "..."
    mc "{i}They're fucking out of time!{/i}"
    scene 9exhibition11 with dissolve
    play music "music/8 - Intro Music.ogg"
    r "Catherine, Bob, here you can see my latest painting."
    if rosa_path == True:
        r "And so fortunate, you can see the people who served as models next to it."
    else:
        r "And so fortunate that you can see my daughter Selina next to it."
    mc "{i}Wait a minute... Is that Catherine?!{/i}"
    scene 9exhibition12 with dissolve
    mc "{i}Holy shit! It's really her.{/i}"
    mc "{i}That's who I didn't expect to see here. As well as did not suspect that she is a connoisseur of painting.{/i}"
    scene 9exhibition12a with dissolve
    mc "{i}And I think she noticed me, too.{/i}"
    k "[mc]? Didn't expect to meet any of my employees here."
    mc "Yeah, the same goes for me."
    scene 9exhibition13 with dissolve
    r "Wait, you two know each other?"
    k "You could say so. This young man works as a bartender in my club."
    r "Huh. How small this world is."
    k "Truly, it is so."
    mc "{i}Is it just me or is there too much redhead here?{/i}"
    scene 9exhibition15 with dissolve
    s "Um... I'm sorry to interrupt you, but [mc] and I were just about to... Emm... We wanted to go somewhere."
    s "So excuse us, but we'll go."
    scene 9exhibition17 with dissolve
    r "Wait, stay with us. I'm sure we'll find some common themes to talk about."
    scene 9exhibition16 with dissolve
    s "Thank you, but we've already made up our minds. Right, [mc]?"
    scene 9exhibition14 with dissolve
    r "Yeah, what do you think, [mc]?"
    mc "Emmm..."
    mc "{i}Damn it! I don't know why, but I feel like this decision will become very important. I need to think carefully.{/i}"
    stop music fadeout 3.0
    $day09_wt_selina=False
    $day09_wt_rosa=False
    "Mod allows to play both scenes here"
    menu selina_or_rosa:
        "Go with Selina" if selina_broke_up == False and day09_wt_selina == False:
            $day09_wt_selina=True
            mc "{i}What's there to think about, though? I've already decided everything for a long time.{/i}"
            mc "I'm sorry, but we've already made a deal with Selina."
            scene 9exhibition17a with dissolve
            r "Oh... I understand."
            r "Well, it's okay."
            scene 9exhibition16 with dissolve
            s "Shall we go?"
            mc "Yeah."
            scene 9exhibition18a with dissolve
            "Together with Selina, you went to the least crowded place in this building."
            jump day09_selina_sex

        "Stay with Rosa" if rosa_path == True and day09_wt_rosa == False:
            $day09_wt_rosa=True
            mc "{i}As much as I'd like to spend time with Selina, I think it'll be just as interesting here.{/i}"
            mc "I think I'm gonna stay here for a while."         
            scene 9exhibition16a with dissolve
            s "Eh, are you sure?"
            mc "Yeah, sorry."
            s "Ohhhh... Okay... Then I'll just go for a walk alone."
            mc "{i}I think she was counting on another answer.{/i}"
            mc "Why don't you stay too?"
            s "I don't want to."
            scene 9exhibition18 with dissolve
            "Without saying another word, Selina left you."
            scene 9exhibition17 with dissolve
            play music "music/6 - Positive Mood.ogg"
            r "Don't worry about her, she's a little tired of this exhibition."
            mc "Yeah, I guess so."
            scene 9exhibition19 with dissolve
            "{color=#00BFFF}Bob{/color}" "I don't want to offend anybody, but I've got to get away, too."
            "{color=#00BFFF}Bob{/color}" "See you later, Rosa. Catherine."
            r "See you later, Bob."
            scene 9exhibition20 with dissolve
            r "Everybody's gone too fast. I hope it's not because of my painting."            
            mc "I don't think you have any reason to worry about it. Your work is one of the best I have seen here so far."
            r "Thank you."
            scene 9exhibition21 with dissolve
            r "You might be surprised, but at first, this picture was supposed to look completely different..."
            mc "{i}I think Rosa's telling more to Catherine now than to me.{/i}"
            mc "{i}I can listen to her, or I can take advantage of this moment a little differently.{/i}"
            menu:
                "Listen to Rosa (+Good point)":
                    $ goodpoint += 1
                    r "Originally it should have been only [mc], but suddenly Selina decided to keep him company."
                    r "It surprised me a little at first, but then I thought, why not?"
                    k "That's interesting."
                    scene 9exhibition24 with dissolve
                    k "But I still don't understand how you two know each other."                    
                "Check out their look (+Bad point)":
                    $ badpoint += 1
                    scene 9exhibition22 with dissolve
                    "You leaned back a little and looked a little lower."
                    mc "{i}Mmmm.... What a wonderful view.{/i}"
                    "..."
                    mc "{i}But it's better not to stare and get back to the conversation.{/i}"
                    scene 9exhibition24 with dissolve
                    k "It was very interesting, Rosa."
                    k "But I still don't understand how you two know each other."    
            mc "{i}I'd rather answer this time.{/i}"
            mc "I met Rosa through Selina."          
            k "Through Selina? So, you are friends with her or...?"
            mc "We haven’t known each other long, but I guess you could call us friends."
            k "I see."
            scene 9exhibition23 with dissolve
            mc "And what about you? Do you like painting too?"
            k "Not as much as Rosa. Although in a way I can be called a connoisseur."
            scene 9exhibition25 with dissolve
            r "I'd say a connoisseur with excellent taste!"
            k "Oh, thank you."
            mc "{i}Huh. If Rosa talks about it, I'm starting to guess what her preferences are.{/i}"
            mc "{i}And I didn't expect that.{/i}"
            scene 9exhibition12 with dissolve
            k "Well, I guess I'll go too."
            k "It was nice to see you, Rosa. [mc]."
            r "I'll see you around."
            mc "Yeah, see you."
            scene 9exhibition25a with dissolve
            "..."
            scene 9exhibition26 with dissolve
            r "Looks like it was a very unexpected meeting for both of you."
            mc "Yes... I guess it is."
            mc "But I'm more interested in the fact that this is the first time we've been alone in the entire evening."
            r "Oh, it's true."
            scene 9exhibition27 with dissolve
            "Rosa's palm touched your chest gently."
            r "I hope you remember how our last meeting ended?"
            mc "Oh, yeah, I remember perfectly well how we were interrupted at the most interesting part."
            scene 9exhibition28 with dissolve
            "Rose came close to you."
            r "In that case, I hope you're ready to finish what we've started?"
            mc "That was a rhetorical question, wasn't it?"
            r "Huh. Exactly."
            scene 9exhibition28a with dissolve
            r "But it'll be a little later."
            r "Now let's just walk through the gallery."
            stop music fadeout 3.0
            scene black with fade
            "You and Rose have been walking around the exhibition for some time, while she was enlightening you about contemporary art."
            scene 9exhibition29 with dissolve
            play music "music/8 - Intro Music.ogg"
            r "...this is the work of one of my colleagues, who now..."
            s "There you are! I couldn't find you for so long."
            scene 9exhibition30 with dissolve
            r "Oh, Selina."
            r "I'm sorry, babe, we got a little carried away. I hope you're okay?"
            s "Yeah, I'm fine."
            s "I just wanted to tell you that I have to go to the hospital now. So..."
            r "Yeah, we get it. Work is work."
            s "Uh-huh."
            scene 9exhibition31 with dissolve
            s "Anyway, it was nice seeing you, [mc]. Bye, Mom."
            mc "Bye!"
            r "Bye, sweetie."
            scene 9exhibition32 with dissolve
            "..."
            scene 9exhibition33 with dissolve
            r "So..."
            mc "We're alone again."
            mc "And I think I've had enough art for today."
            r "Oh, really?"
            mc "Yeah."
            mc "How about a change of scenery?"
            r "I'd love to."
            stop music fadeout 3.0
            jump day09_rosa_sex


label day09_selina_sex:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "Some time later."
    scene 9selinasex01 with dissolve
    play music "music/1 - Atmosphere.ogg" 
    "You didn't even notice before you were in the public toilet."
    s "Ohhhh... I see you took my words seriously."
    mc "When a girl says she's horny, how can I do otherwise?"
    mc "Look, there's no one here."
    s "How lucky we are."
    mc "Yeah, now come here."
    scene 9selinasex02 with dissolve
    s "Ah!"
    s "Kiss me."
    mc "That's what I was going to do."
    scene 9selinasex02a with dissolve
    "The next moment, your lips and tongues touched."
    s "Mmmm..."
    mc "{i}Oh, yeah... These soft lips are the best.{/i}"
    scene 9selinasex03 with dissolve
    s "Ohhhh... I think I got even more turned on."
    mc "Trust me, you're not the only one."
    scene 9selinasex03a with dissolve
    s "We don't have much time, but... Have you ever done it in a place like this?"
    scene 9selinasex04 with dissolve
    "You followed Selina's look."
    mc "In such a place? Definitely not."
    scene 9selinasex03 with dissolve
    s "That's what I thought."
    s "But we don't want anyone to see us, do we?"
    "Selina walked into the stall."
    scene 9selinasex05 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    $ renpy.pause(delay=10)
    mc "{i}Well, how can I resist that?{/i}"
    scene 9selinasex06 with dissolve
    s "All right, come here, baby."
    mc "I can't say no to such a bad girl."
    scene 9selinasex07 with dissolve
    s "Whoo! So I'm a bad girl?"
    mc "Wouldn't it be good to offer to do it in a place like this?"
    mc "You're a very, very bad girl."
    scene 9selinasex08 with dissolve
    "You slammed the door behind you."
    s "And what do you want to do with your bad girl?"
    mc "First, we're gonna see how badly you're corrupted..."
    mc "Stand in front of the door and raise your dress."
    scene 9selinasex09 with dissolve
    s "Mm-hmm. Like this?"
    mc "Yes, that's right."
    scene 9selinasex10 with dissolve
    mc "Transparent panties? How interesting."
    mc "Looks like somebody guessed what might happen to us today."
    scene 9selinasex11 with dissolve
    s "Hehe! I am a very bad girl. Of course I was counting on it."
    mc "Don't think if you admit it, you'll get off easy..."
    scene 9selinasex12 with dissolve
    mc "{i}Now let's get rid of this.{/i}"
    scene 9selinasex12a with dissolve
    mc "Yeah, like this..."
    mc "{i}Ooh! What a great ass she has.{/i}"
    scene 9selinasex13 with dissolve
    "You touched Selina's firm buttocks with your hands."
    s "Aaahhh... Your hands are so rough."
    mc "Hehe. But your ass is very smooth."
    scene 9selinasex13a with dissolve
    mc "{i}And now I'm gonna grab her a little bit.{/i}"
    scene 9selinasex13 with dissolve
    s "Mmm..."
    scene 9selinasex13a with dissolve
    s "..."
    scene 9selinasex13 with dissolve
    s "Stop... Stop teasing me..."
    scene 9selinasex11a with dissolve
    s "We don't have much time, remember?"
    mc "{i}Shit, she's right.{/i}"
    mc "Well, then, let's not delay your punishment."
    s "Mm-hmm... Yes... Punish me!"
    scene 9selinasex14 with dissolve
    "You pressed a girl against the door and made her bend her back."
    mc "Yes... That's what I wanted!"
    scene 9selinasex15 with dissolve
    mc "..."
    scene 9selinasex16 with dissolve
    mc "I hope you're ready for what happens next, because your punishment starts right now."
    s "Mmmm... Yes... I'm ready."
    s "Do it!"
    scene 9selinasex16a with vpunch
    s "Aaahhh!"
    scene 9selinasex17 with dissolve
    s "Yes... That's what I needed."
    mc "{i}Ohhh... Even though it was a little harsh, it was also very pleasant.{/i}"
    mc "{i}And now it's time to go on...{/i}"
    scene 9selinasex19 with dissolve
    "With a hard and determined move, you started fucking Selina."
    scene anim81 with dissolve
    s "Mmm... Yes.... Yes!"
    s "That's so good..."
    mc "Bad girl, Selina, like being fucked in a dirty toilet?"
    s "Ohhh... Ohhh..."
    mc "I don't hear an answer?!"
    s "Mmmm... Yes!"
    mc "Yes what?!"
    s "I like... I like to be fucked here..."
    pause
    scene 9selinasex18 with dissolve
    "Selina's moans got louder."
    scene anim80 with dissolve
    s "Aaaahhh... Aaahhh... Aaah...."
    mc "{i}Her pussy is squeezing my dick so hard... It just feels amazing.{/i}"
    s "Yes... Like this... Punish me harder, [mc]!"
    mc "{i}Oohhhh... If she wants me to fuck her harder, I'm in.{/i}"
    pause
    scene 9selinasex18 with dissolve
    "You've started moving faster."
    scene anim80a with dissolve
    s "Aaaahhh! Mmmmmm!"
    s "It's so good... Just great!"
    mc "{i}Yeah... She's right, it's so fucking good...{/i}"
    s "I want to... I want to feel your dick deeper!"
    mc "{i}Damn, her screams are getting too loud.{/i}"
    mc "{i}I'd better try to change pose.{/i}"
    pause
    scene 9selinasex20 with dissolve
    "You grabbed Selina's leg with one hand, and the other still kept holding her ass."
    s "Mm-hmm... It's like you're reading my mind... It's so much better."
    scene anim82 with dissolve
    s "Ohh!!!! A little more!!!"
    s "Mmm..."
    s "[mc]... This is a... It's amazing!"
    mc "{i}Ooh... I'm not gonna last that long...{/i}"
    pause
    stop music fadeout 3.0
    scene 9selinasex21 with dissolve
    "You grabbed the girl's arms and you started fucking her until suddenly..."
    play sound "music/Door.wav"
    scene 9selinasex22 with dissolve
    "Until suddenly you heard the toilet door open."
    scene 9selinasex25 with dissolve
    mc "Shhh... Not a sound..."
    s "Mm-hmm."
    scene 9selinasex23 with dissolve
    play music "music/8 - Intro Music.ogg"
    r "So what do you really think of my painting?"
    mc "{i}Oh no, it can't be the one I'm thinking of!{/i}"
    k "Do you really need my opinion?"
    mc "{i}And Catherine with her?!{/i}"
    play sound "music/water.wav"
    scene 9selinasex24 with dissolve
    r "Absolutely. We've known each other for so long that I'm always sure of your assessment."
    k "You already know what I'm gonna say. Are you asking for compliments?"
    r "Only if the painting really deserves it."
    scene 9selinasex26 with dissolve
    k "That's a great work, Rosa. As always."
    if rosa_path == True:
        k "But I was more surprised that your daughter decided to participate in this little project."
        scene 9selinasex27 with dissolve
        r "Yes... I was surprised, too."
        r "I used to joke about asking her to pose for my work, but it never went any further than that..."
        k "Until now."
        r "Yes, until now."
        k "And what changed?"
        r "Well, you saw she wasn't alone in the painting. How about that kind of reason?"
        k "[mc]?"
        r "Yeah. "
        k "Oh, that's interesting."
        r "Don't tell me."
        r "Isn't that what youth is for?"
    else:
        k "By the way, I didn't expect to see my employee here."
        scene 9selinasex27 with dissolve
        r "Yes... I was surprised, too."
        k "How do you two know each other?"
        r "Through Selina."
        k "Are they friends, or...?"
        r "The truth is, I don't know what kind of relationship they're in. Selina doesn't share it with me."
        k "I see what you mean."

    k "Shall we go back?"
    r "Yes, let's go."
    stop music fadeout 3.0
    scene black with fade
    "You heard one of the women's footsteps freeze at your stall door."
    play sound "music/heart.mp3"
    scene 9selinasex28 with dissolve
    mc "{i}Geez, Selina's pussy is squeezing my dick so hard right now.{/i}"
    mc "{i}A little more and I'm sure I'll... I will definitely come.{/i}"
    scene 9selinasex29 with dissolve
    mc "{i}And I'm not the only one. I feel like Selina is holding on to it too.{/i}"
    "..."
    scene 9selinasex30 with dissolve
    r "Hmm..."
    k "Rosa, are you coming?"
    scene 9selinasex30a with dissolve
    r "Mm?"
    r "Uh... Yes! Yes, of course."
    r "I thought I heard something. But it was probably nothing."
    stop sound fadeout 3.0
    scene black with fade
    "As soon as you heard Rosa and Catherine go outside the restroom, you couldn't hold back any longer."
    menu:
        "Come outside":
            scene 9selinasex31 with dissolve
            "You barely got your dick out of Selina."
            scene 9selinasex31a with flash
            "And immediately started to come."
            scene 9selinasex31a with flash
            mc "Ohh yesss..."

        "Come inside":
            scene 9selinasex32 with dissolve
            "You started to come right inside Selina."
            scene 9selinasex32a with flash
            mc "Ohh yesss..."
            scene 9selinasex32a with flash
            s "Aahh!"
    scene black with fade
    "Some time later."
    scene 9selinasex33 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Dear Lord, that was the most extreme sex I've ever had."
    s "A little more and we'd..."
    s "No, I'm even afraid to think what could have happened."
    mc "Well, it looks like we're in luck this time."
    scene 9selinasex34 with dissolve
    s "Although, you know... I wouldn't mind doing it again sometime."
    mc "You're such a pervert!"
    s "Hehe!"
    mc "Okay, let's get back to the exhibition."
    s "Yeah, come on."
    stop music fadeout 3.0

    $ renpy.end_replay()
    if not persistent.day09selina2:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day09selina2 = True

    jump day09_exhibition_part02

    
label day09_exhibition_part02:
    scene black with fade
    "Some time later."
    scene 9exhibition29a with dissolve
    play music "music/8 - Intro Music.ogg"
    r "...it's the work of one of my colleagues, who now..."
    s "There's my mom. Again tells someone about these paintings..."
    s "Ahem!"
    scene 9exhibition30a with dissolve
    r "Oh, Selina. [mc]."
    r "I'm sorry, we got a little carried away here. I hope you're okay?"
    s "Yeah, we're fine."
    s "I just wanted to tell you that I've got to get to my shift at the hospital. So..."
    r "Yeah, I get it. Work is work."
    r "And what about you, [mc]?"
    mc "I think I should go home too. Tomorrow will be a hard day."
    scene 9exhibition31a with dissolve
    s "So I'll see you at home, mom."
    mc "Goodbye, Rosa."
    r "Goodbye."
    stop music fadeout 3.0
    scene black with fade
    "Soon after, you said goodbye to Selina, you went home."
    "There was a new day ahead of you."
    menu:
        "Rosa scene" if day09_wt_rosa==False:
            jump selina_or_rosa
        "Continue":
            pass
    jump day09_lisa_home
    

label day09_rosa_sex:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "Some time later. Hotel room."
    scene 9rosa01 with dissolve
    play music "music/1 - Atmosphere.ogg"
    r "Aahh..."
    mc "{i}Oh, yeah, I finally got to her! Nothing can stop us now!{/i}"
    scene 9rosa02 with dissolve
    r "Mm-hmm. How insatiable you are..."
    mc "{i}My head's almost out of it, and my body's acting on its own.{/i}"
    r "Oohhhh... Wait, wait, take your time..."
    scene 9rosa03 with dissolve
    "Rosa took your hand and led you to the bed."
    r "I like your enthusiasm, but we have plenty of time."
    mc "Even though you say so, I can barely contain myself."
    r "Oh, that wild youth!"
    scene 9rosa04
    "As if Rosa had remembered something very important, she stopped abruptly."
    mc "Um... Everything okay?"
    scene 9rosa05 with dissolve
    r "Is your phone with you?"
    mc "Yes, of course."
    r "Get it out, please."
    mc "Why?"
    r "Don't ask questions and just do it."
    mc "Okay."
    scene 9rosa06 with dissolve
    "Still a little confused, you got the phone."
    r "Now turn it off."
    mc "{i}That's what it's all about.{/i}"
    "Like Rosa asked, you turned off your cell phone."
    mc "It's done."
    scene 9rosa07 with dissolve
    r "Well, that's great! I don't think we need it now."
    mc "Yeah, but-"
    r "I don't want anyone to bother us this time."
    mc "{i}Nice reinsurance.{/i}"
    mc "Okay, fair enough."
    scene 9rosa08 with dissolve
    "Rosa put your phone on the table."
    scene 9rosa09 with dissolve
    r "Okay, that's it. Now we're sure we won't be disturbed."
    r "And now let's go and see how strong the bed is here."
    mc "{i}Haha! I like the confidence she's in!{/i}"
    scene 9rosa10 with dissolve
    r "Well, what do you think? Looks pretty good."
    mc "{i}I'm not interested in the bed right now, I'm more interested in who I'm going to be on it right now.{/i}"
    scene 9rosa11 with dissolve
    "Rosa bent down gracefully and slowly ran her hand over the bed surface."
    r "Mmmm... So soft."
    scene 9rosa12 with dissolve
    mc "{i}I'm not sure if she's doing it on purpose or not.{/i}"
    mc "You know, while you're smoothing out that sheet, I get a great view from here."
    scene 9rosa13 with dissolve
    r "You can watch as much as you like, I don't mind."
    mc "That's probably the best answer I could get."
    scene 9rosa14 with dissolve
    "Rosa turned over to you and pulled out her beautiful legs in your direction."
    r "Instead of just watching, why don't you do something more effective?"
    mc "Yes... I know what you mean."
    scene 9rosa15 with dissolve
    mc "Let's start with the small things."
    scene 9rosa15a with dissolve
    r "Mmm... Not bad."
    r "Not bad at all!"
    scene 9rosa16 with dissolve
    r "You know... I think I'll help you a bit."
    scene 9rosa16a with dissolve
    r "That's much better, isn't it?"
    scene 9rosa17 with dissolve
    "The next thing you know, you went ahead."
    r "Yeah, I see you liked it!"
    mc "You have no idea how much."
    scene 9rosa17a with dissolve
    r "Ohh!"
    mc "{i}Mm-hmm... Her boobs are amazing.{/i}"
    r "I think I can imagine now."
    r "Wait a minute, I'll help you."
    scene 9rosa18 with dissolve:
        linear 2.0 yalign 1.0
        linear 2.0 yalign 0.0
        repeat 1
    $ renpy.pause(delay=8)
    r "Let's take off this useless dress."
    mc "{i}Oh, my God, this is so hot.{/i}"
    scene 9rosa19 with dissolve
    "..."
    scene 9rosa19a with dissolve
    r "That's it!"
    scene 9rosa21 with dissolve
    r "Oh! I see you didn't waste any time either."
    mc "Decided to be with you on equal terms."
    scene 9rosa20 with dissolve
    r "No matter how hard you try, baby, I don't think we're gonna be on an equal footing tonight."
    mc "{i}What does she mean by that?{/i}"
    mc "{i}Although... To hell with it! What matters now is something completely different.{/i}"
    scene 9rosa22 with dissolve
    "You walked up to Rosa and gently hugged her by her waist."
    r "Oohhhh... Nice touch."
    mc "{i}Her whole body is so hot.{/i}"
    scene 9rosa23 with dissolve
    "Your hands started caressing her smooth skin."
    r "Mmm...."
    mc "{i}Now let's try something else.{/i}"
    scene 9rosa24 with dissolve
    mc "I'm sorry, but I just can't resist your gorgeous breasts."
    r "Huh... You can do whatever you want with them."
    scene 9rosa24a with dissolve
    r "Aahhh!"
    mc "{i}Mmm... Her nipples are already excited. Nice!{/i}"
    scene 9rosa24b with dissolve
    "..."
    scene 9rosa25 with dissolve
    r "Although, you know, I changed my mind... Let's finish with these games and get to the main thing."
    mc "I'm all for it!"
    scene 9rosa26 with dissolve
    "With a gentle move, you put Rosa on the bed."
    r "Haha! That was sudden!"
    mc "But I can see from your face that you liked it."
    r "Maybe..."
    scene 9rosa27 with dissolve
    mc "Then let's keep going."
    r "Well, go ahead."
    scene 9rosa28 with dissolve
    mc "Looks like we have one last obstacle left."
    mc "Let's get rid of it."
    scene 9rosa28a with dissolve
    mc "{i}Oh, yeah, now I'm totally in.{/i}"
    "You threw off your pants and ended up in front of Rosa on the bed."
    scene 9rosa29 with dissolve
    r "Wow! I see your dick is already hard."
    scene anim61 with dissolve
    mc "{i}Let's have a little fun.{/i}"
    r "Aahhh..."
    r "It's so big and hot... I can't wait to feel it inside..."
    r "It's time to start, don't you think?"
    pause
    scene 9rosa29a with dissolve
    r "Yes... There you go..."
    scene 9rosa30 with dissolve
    r "Now put it in me and show me what you can do."
    mc "How can I say no when a woman asks me to do that?"
    scene 9rosa31 with dissolve
    "The next thing you know, you put your dick in Rosa and started moving."
    scene anim62 with dissolve
    r "Aaahh! Haahh! Aah!"
    r "{i}God, I missed having sex with a young man so much.{/i}"    
    r "{i}This whole game was definitely worth it.{/i}"
    r "{i}Ohh... Now I will definitely squeeze this boy dry.{/i}"
    r "Mmmm... You're doing great... Just don't stop!"
    pause
    scene anim63 with dissolve
    mc "{i}Damn, she's so good!{/i}"
    r "Mmmm... There you go, baby... Yes..."
    mc "{i}Her body is so sexy... And the way her boobs bounce...{/i}"
    mc "{i}It's driving me crazy!{/i}"
    r "Aah! Aah! Haaah!"
    scene 9rosa33 with dissolve
    "Giving in to the new desire, you grabbed Rosa's breasts."
    mc "{i}Oh, yeah... It's insanely nice.{/i}"
    mc "{i}But enough thinking about myself, I have to show her what I can do.{/i}"
    stop music fadeout 3.0
    scene 9rosa32 with dissolve
    "You started fucking Rose as hard as you could."
    r "Aaahhh! Mmmmm!!! Wait a minute... [mc]!"
    r "Hold on!"
    scene 9rosa34 with flash
    "Suddenly, Rosa went up and moaned loudly."
    r "Aaaahhhh!!!! Yeah!!!!"
    scene 9rosa35 with flash
    r "Yeesss..."
    mc "{i}Did she cum?{/i}"
    mc "{i}Wow! I think I'm really good today!{/i}"
    scene black with fade
    "Few seconds later."
    scene 9rosa36 with dissolve
    play music "music/15 - Deep Mood.ogg"
    r "Aaahhhhh... It was a hell of a pleasure..."
    r "But don't think it's gonna end so easily. It's just that I haven't had good sex in a long time."
    mc "I wasn't thinking..."
    scene 9rosa37 with dissolve
    "Rosa grabbed your dick."
    r "Good, because we're just getting started."
    r "Now, come here."
    scene 9rosa38 with dissolve
    r "Mmmnn..."
    scene 9rosa39 with dissolve
    "You didn't even realize that Rosa was on top of you." 
    scene anim64 with dissolve
    mc "{i}Oh, my God, she wrapped her hips around me so tightly...{/i}"
    mc "{i}And these sexy pelvic movements... I can barely think straight.{/i}"
    r "Mmmnn.... Mnnh!"
    pause
    scene 9rosa40 with dissolve
    "Rosa's got you on the bed."
    mc "Whoa!"
    r "You didn't expect me and you to switch roles? Haha!"
    scene 9rosa41 with dissolve
    r "Relax."
    r "Just lie back and enjoy it, I'll take care of everything."
    mc "Oohhhh... I have no doubt about it."
    scene 9rosa42 with dissolve
    mc "{i}If she wants to be on top, I'm ready.{/i}"  
    scene anim65 with dissolve
    r "That's great!"
    mc "{i}Mm-hmm... I think she's getting a lot of pleasure out of that pose.{/i}"
    mc "{i}But I get it myself as much as she do.{/i}"
    r "Haaah! Haaaah! Haaaah!"
    r "Your dick... It's still so hard! Amazing!"
    pause
    scene 9rosa43 with dissolve
    mc "{i}What a fucking view I have here.{/i}"
    scene anim66 with dissolve
    mc "Come on, baby... Don't stop!"
    r "Haha! Who said... That I' m going to do that?!"
    r "Mmmm... A little more! More!!!!!"
    mc "{i}I think I can't just lie down like that anymore!{/i}"
    pause
    scene 9rosa44 with dissolve
    "You grabbed Rosa's ass and started moving in tune with her movements."
    r "Aahhh..."
    scene 9rosa45 with dissolve
    "Gradually, you started moving faster."
    scene 9rosa46 with dissolve
    r "You're... Are you coming soon?"
    mc "I' m almost..."
    r "Okay, great!"
    scene 9rosa47 with dissolve
    "With your hands around Rose, you fucked and kissed her at the same time."
    r "Mmmm...."
    mc "I can't hold it anymore."
    scene 9rosa48 with dissolve
    "Rosa leaned back and grabbed your dick."
    r "I'll help you with that."
    scene 9rosa49 with dissolve
    mc "{i}Damn it, I'm on the verge!{/i}"
    scene anim67 with dissolve
    r "Come on, baby, you've been holding back a long time."
    r "I want to see you come."
    mc "Haaaah! I almost..."
    r "Come on, come right at me! Fill me with your sperm!"
    pause
    scene 9rosa50 with flash
    mc "Yeeess!!!"
    scene 9rosa50 with flash
    "..."
    scene 9rosa50a with dissolve
    r "Wow! What a shot!"
    r "Amazing."
    mc "Oh, yeah, it is."
    scene 9rosa51 with dissolve
    r "So... Did you like it?"
    mc "I'm sure it was one of the best nights of my life."
    r "Mm-hmm. I'm glad."
    r "Now, let's clean this mess."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    play music "music/8 - Intro Music.ogg"
    scene 9rosa52 with dissolve
    mc "Are you sure you don't want to stay here tonight?"
    mc "Then you and I could have had a little more fun."
    scene 9rosa53 with dissolve
    r "Although it's a very tempting offer, I already told you I should be home in the morning."
    r "I don't want Selina to suspect anything."
    mc "I understand that."
    "..."
    mc "So what happens to us next?"
    mc "I don't mind repeating that one day."
    scene 9rosa54 with dissolve
    r "Let this evening remain a little secret between you and me."
    r "And what about the next time, then... We will be in touch."
    mc "Deal."

    $ renpy.end_replay()
    if not persistent.day09rosa:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day09rosa = True


    scene 9rosa53 with dissolve
    r "Well, see you later, [mc]."
    mc "See you later, Rosa."
    stop music fadeout 3.0
    scene black with fade
    "Soon after, you went home."
    "There was a new day ahead of you."
    menu:
        "Selina Scene" if day09_wt_selina==False:
            jump selina_or_rosa
        "Continue":
            pass
    jump day09_lisa_home
    

label day09_lisa_home:
    scene black with fade
    "Party day."
    "After talking to the band on the phone, you arranged for Jacob and Jade to get to the party venue on their own, and you and Lisa to go together."
    play sound "music/doorbell.wav"
    "Ding-dong!"
    ls "Just a minute! I'm coming!"
    "Lisa opened the door, and you saw her."
    play sound "music/Door.wav"     
    scene 9lisa01 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    $ renpy.pause(delay=10)
    play music "music/9 - You Can Make the Sound.ogg"
    mc "Wow."
    scene 9lisa02 with dissolve
    mc "You know, you look amazing in those cute socks and panties and a T-shirt, but..."
    mc "But aren' t we supposed to go now?"
    ls "Hehe. Sorry, I guess I just lost track of time."
    scene 9lisa03 with dissolve
    ls "Come on in. I'll change quickly and we'll go."
    mc "Eh, okay."  
    scene 9lisa04 with dissolve
    if lisa_path == True:
       mc "Nice ass."
       ls "Haha. You're such an asshole!"
       mc "Hey, actually, that was a compliment."
       ls "Yeah, yeah, I get it."
    else:
        mc "{i}Mmm... What a nice ass.{/i}"
    scene 9lisa05 with dissolve
    ls "Okay, can you wait here a bit? I'll be ready in a minute."
    if lisa_path == True:    
        scene 9lisa06 with dissolve
        "Lisa came up to the wardrobe with clothes and started dressing up without being shy about you."
        mc "By the way, I wanted to ask you something. Are you sure you can go to the gig next weekend?"
        scene 9lisa08 with dissolve
        ls "You don't have to worry about me, I totally agree."
        scene 9lisa07 with dissolve
        mc "Oh, that's awesome."
        mc "Then next week we'll start rehearsals again."
        scene 9lisa08 with dissolve
        ls "Yeah, sounds good."    
        mc "Hey, Lisa."    
        scene 9lisa09 with dissolve
        ls "Yes?"
        mc "Mmmm... Nothing, I just wanted to see your gorgeous body."
        scene 9lisa10 with dissolve
        ls "So that's how it is. You like to look at girls when they change, don't you?"
        mc "Nope, just you. I don't need any other girls."
        ls "Huh. That's a good answer."
        scene 9lisa10a with dissolve
        ls "But I can see where your eyes are headed... Maybe I should cheer you up a little?"
        mc "Sounds very intriguing."
        scene anim70 with dissolve
        "You're completely focused on the girl's breasts."
        ls "You like watching me playing with my breasts?"
        mc "Yep..."
        ls "You probably want to touch it yourself, don't you?"
        mc "Very much so. Come here."
        ls "Okay."
        pause
        scene 9lisa12 with dissolve
        "Lisa slowly climbed onto the bed and ended up right in front of you."
        scene 9lisa13 with dissolve
        mc "{i}She's so close.{/i}"
        mc "{i}I can't resist her.{/i}"
        scene 9lisa15 with dissolve
        "The next moment, you kissed her."
        ls "Mmmm..."
        scene 9lisa14 with dissolve
        "..."
        scene 9lisa16 with dissolve
        ls "Let's just finish this before we go too far."
        ls "Like you said, we're running out of time."
        mc "I wouldn't mind staying a little longer if we took the time like I think..."
        scene 9lisa16a with dissolve
        ls "It's a lovely offer, but it's not gonna work that way."
        scene 9lisa17 with dissolve
        mc "What? Why not?"
        ls "I already gave you a reason. We have to go."
        scene 9lisa18 with dissolve
        ls "But if all goes well, maybe at the end of the evening we'll continue where we left off."
        mc "Mm-hmm... Okay."
        mc "But next time, we're gonna get this done."
  
    scene black with fade
    "Some time later."

    scene 9lisa19 with dissolve
    ls "Well, I've changed! What do you think? How do I look?"
    mc "Looks good. But to be more specific, I need you to turn around."
    ls "Hehe. Why not?"
    scene 9lisa19a with dissolve
    ls "That's it! Look as much you want."
    mc "Yeah, you look great."
    scene 9lisa20 with dissolve
    ls "Thanks."
    ls "And stop lying on the couch. Let's go!"
    scene 9lisa21 with dissolve
    "Discussing stuff with each other, you went to a party."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    jump day09_paty_part01


label day09_paty_part01:
    scene 9party01 with dissolve
    play music "music/12 - The Moose.ogg"
    ls "Wow... Looks like the party's in full swing. I can hear the sound of music from here."
    mc "Huh. The louder the better!"
    ls "I'll agree with you on that."
    mc "Let's go inside before we miss everything."
    scene 9party02 with dissolve
    "You noticed Little Barry at the front of the house. The same guy who threw this party and was your old friend."
    mc "{i}Hell, he's changed a lot since we last met.{/i}"
    mc "Barry? Is that really you?!"
    scene 9party03 with dissolve
    "{color=#808000}Barry{/color}" "[mc]?!"
    "{color=#808000}Barry{/color}" "Fucking hell, you're here, aren't you? Damn good to see you, buddy!"
    scene 9party04 with dissolve
    mc "Haha! It's mutual, man!"
    mc "What the hell happened to you? I don't recognize you at all."
    mc "How much did you lose? Twenty, thirty kilograms?"
    scene 9party07 with dissolve
    "{color=#808000}Barry{/color}" "Twenty-five, to be precise."
    "{color=#808000}Barry{/color}" "Now I'm trying to keep an eye on what I eat."
    mc "That's really awesome. You look great."
    "{color=#808000}Barry{/color}" "Yeah, thanks."
    scene 9party05 with dissolve
    "{color=#808000}Barry{/color}" "And who is this beautiful stranger next to you?"
    if lisa_path == True:
        mc "Oh, it's Lisa. She's my girlfriend."
    else:
        mc "Oh, it's Lisa. She's a close friend of mine."
    "{color=#808000}Barry{/color}" "Well, then, it's nice to meet you, Lisa."
    "{color=#808000}Barry{/color}" "Friends [mc], my friends."
    scene 9party06 with dissolve
    ls "Nice to meet you, too, Barry."
    scene 9party05 with dissolve
    "{color=#808000}Barry{/color}" "Oh, let me introduce you to my girlfriend Stella."
    scene 9party08 with dissolve
    "{color=#6A5ACD}Stella{/color}" "Hey, guys."
    "{color=#6A5ACD}Stella{/color}" "I hope you're in a good mood, because we're rocking out here today."
    mc "You don't have to worry about us, we're here for the same reason."
    "{color=#6A5ACD}Stella{/color}" "Okay, great."
    scene 9party05 with dissolve
    mc "It's just like old times."
    "{color=#808000}Barry{/color}" "That's right!"
    "{color=#808000}Barry{/color}" "By the way, Jacob's already here. And I'll tell you in confidence that he came here with one dark-haired hottie."
    scene 9party06 with dissolve
    ls "It's probably Jade."
    scene 9party05 with dissolve
    "{color=#808000}Barry{/color}" "Yes! I think that's how he introduced her."
    mc "So they're already here. That's great!"
    "{color=#808000}Barry{/color}" "Anyway, I'm not gonna keep you guys any longer. Go inside and have fun."
    mc "That's what we'll do."
    scene 9party07a with dissolve
    "{color=#808000}Barry{/color}" "Hey, [mc]."
    mc "Yes?"
    "{color=#808000}Barry{/color}" "Find me later, okay?"
    mc "No problem, man."

    scene 9party09 with dissolve
    "You walked into the yard."
    ls "Hmm... Looks like this Barry is a great guy."
    mc "Yeah, he is."
    scene 9party11 with dissolve
    mc "He even played guitar with me and Jacob a long time ago."
    ls "Really?"
    mc "Yeah."
    mc "But then he started to devote more time to his studies and gave up music completely."
    ls "That's a shame."
    mc "It's okay. As far as I know last year he went to one of the best colleges in this country. So... He's doing great."
    scene 9party10 with dissolve
    mc "Okay, let's leave the memories. I can't wait to see this party with my own eyes."
    ls "Yeah... I gotta say, your friend's house is huge!"
    ls "I wonder what's inside."
    mc "Let's find out."
    stop music fadeout 3.0
    scene black with fade
    "A minute later."
    scene 9party12 with dissolve
    play music "music/6 - Positive Mood.ogg"
    ls "Wow! There are so many people here... And everyone is busy with something."
    mc "Same as usual. Someone gets slowly drunk, and someone takes a moment and looks for a pair for the evening."
    scene 9party13 with dissolve
    ls "What do you like to do in times like this?"
    mc "Me? Well, I like to combine."
    scene 9party13a with dissolve
    if lisa_path == True:
        ls "Mm-hmm... It's good you don't have to look for a pair tonight."
        mc "That's for sure. The hottest girl at this party is already mine."
        ls "Precisely! Hehe. And now let's find Jacob and Jade."
    else:
        ls "That's interesting. So that's what you do at parties like this?"
        mc "If I was alone, maybe... But today we are relaxing as a band."
        ls "Precisely! Hehe. And now let's find Jacob and Jade."
    scene black with fade
    "After walking around the house, you decided to go to the backyard where the loud music came from."
    scene 9party14 with dissolve
    mc "{i}These guys are pretty well settled in here.{/i}"
    ls "Hey, does that guy at the DJ desk look familiar to you?"
    mc "Hm?"
    stop music fadeout 3.0
    "..."
    mc "Wait a minute... This is..."
    play music "music/Maxim Nick - Life Calls You.ogg"
    scene 9party16a with vpunch
    j "LETS ROCK!!! HAHAHAH!!!"
    mc "Yeah, it's definitely Jacob."
    ls "He's not hard to recognize here."
    mc "Shall we go say hi to him?"
    ls "Um... Are you sure we should bother him right now? He seems very passionate about what he does."
    mc "Alas, but we don't have much choice."
    scene 9party18 with dissolve
    j "Oh! You're finally here! Cool!"
    mc "Hey, man."
    ls "Hello, Jacob."
    j "Hey, hey!"
    scene 9party19 with dissolve
    ls "I didn't know you'd be a DJ here."
    scene 9party20 with dissolve
    j "What? No! I was just asked for a little favor."
    j "There's another person coming to replace me soon."
    mc "So you're just here for a while, huh?"
    j "Yeah, kind of."
    scene 9party19 with dissolve
    ls "And where is Jade now?"
    scene 9party20 with dissolve
    j "She was here somewhere."
    scene 9party15 with dissolve
    "You turned your head around."
    j "No, not here."
    scene 9party17 with dissolve
    j "And there she is! Sitting there talking to someone by the pool."
    mc "{i}I'll have to say hello to her later.{/i}"
    scene 9party20 with dissolve
    j "Oh! By the way, check out what I have here!"
    stop music fadeout 3.0
    scene 9party20a with dissolve
    "..."
    play music "music/11 - Pop Energy.ogg"
    scene 9party20b with dissolve
    j "Ta-da!"
    mc "Huh? What is this?"
    j "That's my personal cup I'm drinking from tonight."
    scene 9party21 with dissolve
    "..."
    scene 9party22 with dissolve
    j "Ahhh! Great stuff!"
    mc "Didn't you happen to have a letter of commendation or a medal attached to this thing?"
    scene 9party22b with dissolve
    j "Yeah, yeah, very funny."
    j "Just before I got here, it hit me that I had to have my own feature."
    j "Well, you know! A feature!"
    mc "Isn't it enough that you're here today as a DJ?"
    scene 9party22 with dissolve
    j "Nah, that's not what it is! The feature should be different..."
    mc "What's it supposed to be like?"
    j "One that everybody here can remember me even a month after this party."
    mc "Oh, wow."
    mc "Like if everybody remembers the moron with the cup, right?"
    scene 9party20b with dissolve
    j "Exactly!"
    scene 9party22 with dissolve
    "..."
    scene 9party22a with dissolve
    j "Wait a minute... Did you just call me a moron?"
    mc "Never mind, man. Now you're the most special person here, you have your own cup!"
    scene 9party22b with dissolve
    j "That's right! And you can't spoil my wonderful mood with such cruel words."
    mc "Okay, better tell me, how long are you gonna stay behind the DJ desk?"
    scene 9party22c with dissolve
    j "Well, um... I'm gonna have to stand here for a bit. But, I think I'll be replaced soon."
    scene 9party23 with dissolve
    ls "It's interesting to be here with you, guys, but I'm gonna go say hello to Jade. Find us when you're done."
    mc "{i}Oh... She stood so quietly here that I even forgot about her presence.{/i}"
    mc "Okay, I'll find you later."
    ls "Deal."
    stop music fadeout 3.0
    scene 9party24 with dissolve
    j "What about you? What are you going to do now?"
    mc "I'm not sure yet. Maybe I'll find Barry, or-"
    play music "music/8 - Intro Music.ogg"
    scene 9party25 with dissolve
    "{color=#EEE8AA}Drunk guy{/color}" "Heeeey!"
    "{color=#EEE8AA}Drunk guy{/color}" "Dudes, what's up?"
    j "Hmm? It's okay."
    scene 9party26 with dissolve
    "{color=#EEE8AA}Drunk guy{/color}" "Awesome! Haha!"
    "{color=#EEE8AA}Drunk guy{/color}" "Hey... Don't tell that dude from behind, but he really sucks as a DJ. Haha!"
    mc "{i}Considering how loudly you said it, I think Jacob heard it himself.{/i}"
    mc "{i}But it doesn't look like he's angry about it.{/i}"
    mc "{i}I gotta get rid of this weirdo.{/i}"
    mc "You need something?"
    scene 9party26a with dissolve
    "{color=#EEE8AA}Drunk guy{/color}" "Yeah, man, pass me that drink over there."
    scene 9party27 with dissolve
    mc "{i}Hmm... Looks like he's already drunk as hell.{/i}"
    mc "{i}What should I do? Should I give him a drink or just send him the fuck out?{/i}"

    $ day09_drink = False
    $ day09_beer = False
    $ day09_whiskey = False
    
    menu:
        "Give him a beer":
            $ goodpoint += 1
            $ day09_beer = True
            mc "{i}I don't care. If he wants a drink, I'll just give him a bottle of beer.{/i}"
            scene 9party28 with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "Oh! Thanks, man, you just saved me."
            scene 9party29 with dissolve
            "..."
            scene 9party30 with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "Yeah, um... Now it's cool!"
            mc "Okay, if that's all you wanted, why don't you just get out of here?"
            "{color=#EEE8AA}Drunk guy{/color}" "Yeah, I'll see you around!"
            mc "{i}And I hope not.{/i}"
            scene 9party31 with dissolve
            "..."
            scene 9party32 with dissolve
            j "Hey, shouldn't bartenders stop people when they get too drunk?"
            mc "I'm not at work today."
            j "Fair enough."

        "Give him whiskey":
            $ goodpoint += 1
            $ day09_whiskey = True
            mc "{i}In this state, he's unlikely to notice the difference between beer and whiskey.{/i}"
            mc "{i}He'll know before he talks badly about my friends.{/i}"
            scene 9party28a with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "Oh! Thanks, man, you just saved me."
            scene 9party29a with dissolve
            "..."
            scene 9party30a with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "Yeah, um... Now it's cool!"            
            mc "{i}Wow! He really didn't notice the difference.{/i}"
            mc "Okay, if that's all you wanted, why don't you just get out of here?"
            "{color=#EEE8AA}Drunk guy{/color}" "Yeah, I'll see you around!"
            mc "{i}And I hope not.{/i}"
            scene 9party31 with dissolve
            "..."
            scene 9party32 with dissolve
            j "Haha! Did you see that?! He didn't even notice what you gave him!"
            mc "Yeah. Hopefully next time he'll think before he acts like an asshole."  
            j "I'd be surprised if he'd even remember this night."
            mc "That's his own problem."

        "Send him the fuck out":
            $ badpoint += 1
            $ day09_drink = True
            mc "{i}Better send him away before he does anything wrong.{/i}"
            scene 9party26a with dissolve
            mc "You've had enough of the booze. Go to sleep."
            scene 9party26b with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "I didn't ask you for advice!"
            "{color=#EEE8AA}Drunk guy{/color}" "I'm gonna go find it myself..."            
            scene 9party31 with dissolve
            "..."
            scene 9party32 with dissolve
            j "You're tough on him."
            mc "I don't know... I didn't like him."
            j "Yeah, me neither." 
    
    "..."
    mc "By the way, isn't it time for you to get back to the music?"
    scene 9party32a with dissolve
    j "I guess so. But I think I still have some time to drink with my bro."
    mc "I got the hint."
    scene 9party27 with dissolve
    "You took a bottle of beer off the counter."
    scene 9party33 with dissolve
    mc "Cheers!"
    j "Yeah, cheers!"
    stop music fadeout 3.0
    scene 9party16 with fade
    "Some time later, Jacob went back to the DJ console."
    mc "{i}Okay, looks like we're in the middle of a party. Where should I go first?{/i}"

    $ day09_lr01 = False
    $ day09_lr02 = False
    $ day09_kitchen = False
    $ day09_bathroom_01 = False
    $ day09_bathroom_02 = False
    $ day09_party_jacob = False

    $ day09_emma_hand_positive = False

    menu day09_party_roam:
        "Go to the living room" if day09_lr01 == False:
            $ day09_lr01 = True
            mc "{i}Let's see what's going on in the living room.{/i}"
            scene 9partylr01 with dissolve
            play music "music/16 - Bright Colors.ogg"
            "When you got there, you noticed Lisa and Jade had fun talking to each other at the end of the room."
            mc "{i}Looks like they're having a good time.{/i}"
            mc "{i}I'm gonna go check on them.{/i}"
            scene 9partylr02 with dissolve
            ls "Oh, you finally decided to join us!"
            mc "How could I not go over to the two most attractive girls at this party?"
            mc "Hello, Jade."
            jd "Hello."
            if jade_path == True:
                mc "{i}Hmm... She's acting completely relaxed, like that kiss didn't happen yesterday.{/i}"
                mc "{i}But it's probably for the best.{/i}"
            mc "So, I see you're having a good time here."
            scene 9partylr05 with dissolve
            jd "Sort of."
            jd "Lisa talked about how you went to the Naked Park concert."
            ls "And that was fucking cool! Haha!"
            scene 9partylr06 with dissolve
            ls "By the way, [mc], do you know if Jacob's finished his DJ work?"
            mc "Maybe I'm not sure."
            ls "If he is, get his ass over here!"
            ls "He's the one who invited us all to this party. It's not cool if he's out there alone now."
            mc "Okay, I'm gonna go see where he is."
            ls "Awesome!"
            jd "We'll be waiting for you here."
            stop music fadeout 3.0
            scene black with fade
            "I guess I could do a little more walking around the house or I could look for Jacob."
            jump day09_party_roam

        "Go to the kitchen" if day09_kitchen == False:
            $ day09_kitchen = True
            mc "{i}Let's see what's going on in the kitchen.{/i}"
            scene 9partyhome01 with dissolve
            play music "music/12 - The Moose.ogg"
            mc "{i}Oh, I think Barry and his girlfriend are here.{/i}"
            mc "{i}I guess I could talk to them a little longer this time. Especially since Barry asked me to find him.{/i}"
            scene 9partyhome02 with dissolve
            "{color=#808000}Barry{/color}" "Oh, [mc], you got here on time. I was just telling Stella about our school adventures."
            "{color=#808000}Barry{/color}" "Come on, join us!"
            mc "Sure, why not?"
            scene 9partyhome03 with dissolve
            "{color=#6A5ACD}Stella{/color}" "Looks like you, Jacob and Barry were close friends. He spoke very well of you."
            mc "Yeah, I guess that's what it is."
            mc "Too bad that smartass went to the other side of the country to study. Otherwise, the stories he told you would be much more."
            scene 9partyhome04 with dissolve
            "{color=#808000}Barry{/color}" "That's right! I suggest we drink to this meeting!"
            "{color=#6A5ACD}Stella{/color}" "And also for getting to know each other."
            "{color=#808000}Barry{/color}" "Then to the meeting and to the acquaintance!"
            mc "Huh. I'm with you!"
            stop music fadeout 3.0
            scene 9partyhome05 with dissolve
            "*ring*"
            scene black with fade
            "Some time later."
            scene 9partyhome06a with dissolve
            play music "music/6 - Positive Mood.ogg"
            "{color=#808000}Barry{/color}" "So, I heard a rumor that your band recently had your first gig. Is that true?"
            mc "Yeah, you could say that."
            mc "We, and a few other new bands like us, performed on the same stage. Can you imagine what was going on there?"
            "{color=#808000}Barry{/color}" "Oh, too bad I missed that."
            scene 9partyhome06 with dissolve
            "{color=#6A5ACD}Stella{/color}" "So how'd it go?"
            mc "Actually, considering all the circumstances, it was pretty good. At least much better than I imagined."
            mc "If you try hard enough, you can even find the video from that night on the Internet."
            "{color=#808000}Barry{/color}" "I'm definitely gonna find it and watch it."
            scene 9partyhome07 with dissolve
            "Suddenly you felt somebody's palm lying on your shoulder."
            mc "{i}What's that?!{/i}"
            scene 9partyhome08 with dissolve
            em "Hey, [mc]."
            mc "Emma?"
            em "Mind if I join you?"
            scene 9partyhome09 with dissolve
            "Without waiting for an answer, Emma sat next to you."
            mc "I didn't know you were gonna be at this party."
            em "Why not? Barry is my friend, too."
            mc "Yeah, I know, it's just... It's just that we rarely see each other."
            em "Yeah..."
            scene 9partyhome10 with dissolve
            mc "But let's not talk about the sad things! Tell me, how are you doing?"
            mc "Last time we met, you left me a note saying you were gonna live with a friend."
            scene 9partyhome19 with dissolve
            em "Yeah, we still live together."
            em "And I had to get a terrible job as a waitress to pay my rent."
            em "Can you imagine that? I am a waitress!"
            scene 9partyhome10 with dissolve
            mc "Huh. This is quite surprising."
            scene 9partyhome20 with dissolve
            em "Alas, but after the bankruptcy of my father's company and the quarrel with my parents, I had to adapt."
            scene 9partyhome19a with dissolve
            em "But I'm trying to keep a positive attitude!"
            scene 9partyhome11 with dissolve
            em "By the way, how about a drink?"
            mc "Sure, why not?"
            mc "We should ask if Barry and Stella will join us."
            em "Um... I don't think they have time for that right now."
            mc "Hm?"
            scene 9partyhome12 with dissolve
            em "Look for yourself."
            scene 9partyhome13 with dissolve
            mc "Oh..."
            scene 9partyhome14 with dissolve
            mc "{i}They didn't waste time for nothing.{/i}"
            "{color=#6A5ACD}Stella{/color}" "Mmmm..."
            scene 9partyhome14a with dissolve
            "..."
            if emma_sex == True:
                scene 9partyhome15 with dissolve
                "Suddenly you felt Emma's hand in your hip."
                mc "{i}Hey, what the hell...?{/i}"
                menu:
                    "Push her hand":
                        mc "{i}I don't like it at all.{/i}"
                        scene 9partyhome15a with vpunch
                        "..."
                        scene 9partyhome16a with dissolve
                        mc "Don't do that again. Do you understand me?"
                        em "Y-yeah... I'm sorry."
                        scene 9partyhome19 with dissolve 
                        em "I guess I'd better go."
                        mc "Yeah."
                        scene 9partyhome21a with dissolve 
                        "Emma left."
                    "{color=#66FF33}Don't do anything":
                        $ day09_emma_hand_positive = True
                        mc "{i}Mmmm... And it's even nice.{/i}"
                        scene 9partyhome15b with dissolve
                        "..."
                        scene 9partyhome16 with dissolve
                        em "I missed you, [mc]."
                        mc "{i}Those words were sincere.{/i}"
                        mc "Yeah, I missed you, too."
                        scene 9partyhome15 with dissolve
                        "..."
                        scene 9partyhome09 with dissolve
                        em "Hey, I think you and I wanted a drink?"
                        mc "Yeah, right!"
                        scene 9partyhome17 with dissolve
                        "*ring*"
                        scene black with fade
                        "Some time later."
                        scene 9partyhome21 with dissolve
                        em "Okay, it was nice to talk to you, [mc]."
                        em "Find me later, okay?"
                        mc "Yeah."
                        scene 9partyhome21a with dissolve 
                        "Emma left."
            else:
                em "Hey, I think you and I wanted a drink?"
                mc "Yeah, right!"
                scene 9partyhome17 with dissolve
                "*ring*"
                scene black with fade
                "Some time later."
                scene 9partyhome21 with dissolve
                em "Okay, it was nice to talk to you, [mc]."
                em "Maybe I'll see you around."
                mc "Yeah."
                scene 9partyhome21a with dissolve 
                "Emma left."  
            stop music fadeout 3.0
            scene black with fade
            "I think I'd better go somewhere else, too."
            jump day09_party_roam


        "Go to the bathroom" if day09_bathroom_01 == False:
            $ day09_bathroom_01 = True
            play music "music/8 - Intro Music.ogg"
            mc "{i}It feels like the beer you have been drinking is asking for outside. You have to go to the bathroom.{/i}"
            "You opened the bathroom door and froze."
            play sound "music/Door.wav" 
            scene 9partybathroom01 with dissolve
            mc "{i}Wow... Looks like it's occupied. But why didn't they close the door?{/i}"
            "{color=#FF69B4}Girl{/color}" "Mmmm..."
            scene 9partybathroom02 with dissolve
            "{color=#FF69B4}Girl{/color}" "Wait, Charlie, the door!"
            "{color=#00BFFF}Man{/color}" "Dude, what the fuck! You see, this place is occupied!"
            play sound "music/doorclose.wav" 
            scene 9partybathroom03 with vpunch
            mc "{i}Okay, I get it, I'll come back later.{/i}"
            stop music fadeout 3.0
            scene black with fade
            mc "{i}Better go somewhere else.{/i}"
            jump day09_party_roam

        "Find Jacob" if day09_lr01 == True and day09_party_jacob == False and day09_bathroom_01 == True and day09_kitchen == True:
            $ day09_party_jacob = True     
            scene black with fade
            mc "{i}Looks like it's been long enough for Jacob to finish his stuff. I'll try to find him. {/i}"                
            "You went to the backyard."
            scene 9partyjacob01 with dissolve
            play music "music/10 - Street's.ogg"
            j "Heeey! There you are!"
            mc "Oh, I was looking for you, too."
            mc "I see you're still walking around with that stupid thing."
            scene 9partyjacob02 with dissolve
            j "In fact, I already told you I like this cup."
            mc "Yeah, yeah, I know, it' s just..."
            stop music fadeout 3.0
            "{color=#EEE8AA}Drunk guy{/color}" "Oh, come on! I can see that you're here alone anyway." 
            "{color=#4682B4}???{/color}" "What do you care?"
            scene 9partyjacob03 with dissolve
            play music "music/8 - Intro Music.ogg"
            j "Hey, isn't that the drunk guy who came up to us recently?"
            mc "Yeah, that's him."
            scene 9partyjacob04 with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "Just one kiss and I'll go. Honestly!"
            "{color=#4682B4}???{/color}" "I'm not gonna kiss you! Just leave me alone!"
            "{color=#EEE8AA}Drunk guy{/color}" "You'll like it, you'll see!"
            scene 9partyjacob05 with dissolve
            j "Is it me or is this guy acting like an asshole again?"
            mc "You're right about that."
            mc "Let's go help this girl get rid of him."
            scene 9partyjacob06 with dissolve
            j "Hey, is everything okay? Is this guy bothering you?"
            "{color=#4682B4}???{/color}" "What? Are you his friends?"
            mc "No. We were just there and decided you could use some help."
            if day09_beer == True or day09_whiskey == True:
                scene 9partyjacob07 with dissolve
                "{color=#EEE8AA}Drunk guy{/color}" "Oh, they're my bros!"
                "{color=#EEE8AA}Drunk guy{/color}" "I missed you guys so damn much! Where the hell have you been?!"
                mc "Look, no offense, man, but maybe you should go somewhere else, huh?"
                scene 9partyjacob07a with dissolve
                "{color=#EEE8AA}Drunk guy{/color}" "Oh, no problem. I was just about to go inside. Will you come with me?"
                mc "You go ahead, we'll catch up with you."
                "{color=#EEE8AA}Drunk guy{/color}" "Awesome! See you in there!"
                stop music fadeout 3.0
                scene 9partyjacob07b with dissolve
                "{color=#EEE8AA}Drunk guy{/color}" "Hey, dudes... Leave me to drink..."
                play music "music/6 - Positive Mood.ogg"

            else:
                scene 9partyjacob08 with dissolve
                "{color=#EEE8AA}Drunk guy{/color}" "Hey, it's you again! This is the second time I've seen you today."
                scene 9partyjacob09 with dissolve
                j "Yeah, you and your drunk face are getting to us."
                stop music fadeout 3.0
                scene 9partyjacob08 with dissolve
                "{color=#EEE8AA}Drunk guy{/color}" "Okay, that's it! You asked for a fight yourself."
                play music "music/5 - Adrenaline Fight.ogg"
                scene 9partyjacob09 with dissolve
                j "Don't interfere, guys, I can handle him myself."
                mc "You sure?"
                j "You bet! He's barely standing on his feet."
                scene 9partyjacob10 with dissolve
                "The drunk guy ran to Jacob with his fists."
                mc "{i}I feel like it's gonna be an exciting show.{/i}"
                stop music
                play sound "music/music_stop.wav"
                scene 9partyjacob11 with dissolve
                "..."
                scene 9partyjacob12 with dissolve
                "{color=#EEE8AA}Drunk guy{/color}" "*LOUD CRY!!!*"
                play sound "music/water_splash.wav"
                scene 9partyjacob13 with vpunch
                "..."
                scene 9partyjacob14 with dissolve
                j "Huh? That's it?"
                scene black with fade
                "The drunk guy was quickly pulled out of the pool and immediately escorted out."
                play music "music/6 - Positive Mood.ogg"
                scene 9partyjacob15 with dissolve
                j "Hey, did you see that? I didn't even have time to do anything, the guy fell into the water himself."                
                mc "You could brag and say it's your new contactless combat technique."
                j "Yeah, and if you don't stop joking, I'll use it on you."
                mc "Haha. Okay."
                mc "{i}We need to check on the girl.{/i}"
            scene 9partyjacob16 with dissolve
            mc "Are you okay?"
            "{color=#4682B4}???{/color}" "Thanks, guys. This jerk seems like he's out of his mind."
            "{color=#4682B4}???{/color}" "If you hadn't shown up, I don't even know what would have happened..."
            mc "Don't worry, if it wasn't us, somebody else would have escorted this idiot out."
            scene 9partyjacob16a with dissolve
            j "By the way, I don't think we know each other."
            j "My name is Jacob, and next to me [mc]."
            mc "Hey."
            scene 9partyjacob17 with dissolve
            "{color=#4682B4}???{/color}" "Hi. My name is Ruby."
            mc "{i}And she's pretty cute.{/i}"
            ru "I'm sorry, uh... I'd really like to stay and talk to you, but I was looking for my friend."
            j "Yeah, yeah, we get it."
            scene 9partyjacob18 with dissolve
            ru "Thank you again for your help!"
            scene 9partyjacob19 with dissolve
            "*kiss*"
            scene 9partyjacob20 with dissolve
            ru "It was nice meeting you. [mc]. Jacob."
            mc "Yeah, it was nice to meet you."
            scene 9partyjacob21 with dissolve
            ru "I really like you guys. I hope we'll meet again sometime."
            mc "{i}Um... Is it me or did it sound like some form of flirting?{/i}"
            scene 9partyjacob22 with dissolve
            j "Yeah. So are we."
            stop music fadeout 3.0
            scene black with fade
            "Soon Ruby left, leaving you alone with Jacob."
            scene 9partyjacob23 with dissolve
            play music "music/9 - You Can Make the Sound.ogg"
            j "Dude, I think I just fell in love!"
            mc "Yeah, that girl is really nice."
            mc "But what happened to those two asian girls? It seems you were thrilled with them."
            scene 9partyjacob23a with dissolve
            j "Ah! Screw them! Our \"relationship\" is over."
            mc "Eh, what's happened?"
            j "I saw their new photos online with another drummer."
            mc "Photos?"
            j "Yeah, very spicy photos."
            mc "Oh... I'm sorry, dude."
            scene 9partyjacob24 with dissolve
            j "I don't give a damn! I got everything I wanted from those short relationships, so it's okay."
            j "Now I'm open to new proposals."
            mc "For someone like Ruby?"
            j "That's right!"
            scene 9partyjacob24a with dissolve
            j "Damn it... It's a shame she's already gone."
            mc "You know, I don't think she's gotten far."
            scene 9partyjacob24 with dissolve
            j "Do you think I should catch up with her?"
            mc "If you really like her, you shouldn't miss this chance."
            scene 9partyjacob24b with dissolve
            j "I guess that's exactly what I'm gonna do! Thanks for the advice, dude!"
            scene 9partyjacob25 with dissolve
            j "Hold on, you blue-haired beauty, I'm on my way to you!"
            mc "{i}Oh, one minute he's focused and serious, the other minute he's acting like a clown.{/i}"
            scene 9partyjacob26 with dissolve
            "You put your eyes down."
            mc "{i}He ran away and left his stupid cup... Looks like he's serious this time.{/i}"
            stop music fadeout 3.0
            "..."
            scene black with fade
            "Okay, there's nothing else to do here."    
            jump day09_party_roam             
        
        "Go to the bathroom" if day09_party_jacob == True and day09_whiskey == True and day09_bathroom_02 == False:
            $ day09_bathroom_02 = True
            scene black with fade
            play music "music/8 - Intro Music.ogg"
            mc "{i}Hopefully, for once, the bathroom will be available.{/i}"
            play sound "music/Door.wav" 
            scene 9partybathroom04 with dissolve
            mc "{i}Oh, shit, not this guy again!{/i}"
            mc "{i}Whoa! Does he have the same bottle of whiskey I gave him on the floor? Ha!{/i}"
            scene 9partybathroom05 with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "Heeey! Dude, it's you again!"
            "{color=#EEE8AA}Drunk guy{/color}" "I'm sorry, uh... I'm a little busy right now..."
            mc "Yeah, I can see that."
            "{color=#EEE8AA}Drunk guy{/color}" "Just a minute, I'm gonna clear this place up soon."
            mc "You know, you can take your time-"
            "{color=#EEE8AA}Drunk guy{/color}" "Ohhhh... No... Not again..."
            scene 9partybathroom06 with dissolve
            "{color=#EEE8AA}Drunk guy{/color}" "*HORRIBLE SOUNDS*"
            play sound "music/doorclose.wav" 
            stop music fadeout 3.0
            scene 9partybathroom03 with vpunch
            mc "{i}Oh, my God. I hope I can forget it.{/i}"
            mc "{i}I think it's best to get the hell out of here.{/i}"
            jump day09_party_roam

        "Go back to Lisa and Jade" if day09_party_jacob == True and day09_lr02 == False:
            $ day09_lr02 = True
            scene black with fade
            "It's time to get back to Lisa and Jade."
            scene 9partylr02 with dissolve
            play music "music/6 - Positive Mood.ogg"
            mc "Here I am again."
            ls "Um... Where's Jacob? I thought you guys would come back together."
            mc "I don't know how to tell you this."
            mc "Well, he ran after some girl, so he won't be here for a while."
            scene 9partylr08 with dissolve
            ls "Seriously? He left us again?!"
            ls "Jeez, this is starting to get annoying!"
            mc "I could be wrong, but this time it seems serious."
            ls "I'm pretty sure he takes every skirt around him seriously."
            scene 9partylr04 with dissolve
            jd "Come on, Liz, stop grumbling. He's a guy, so let him have fun."
            scene 9partylr08a with dissolve
            ls "Hmm... Well, if that's what you two think, then okay."
            if lisa_path == True:
                scene 9partylr08b with dissolve
                ls "Besides, even if Jacob isn't here, the important thing is that [mc] is here!"
                scene 9partylr03 with dissolve
                "Lisa stepped towards you and kissed you hard."
                scene 9partylr08b with dissolve
                ls "Yes... I feel much better now!"
            scene 9partylr07 with dissolve
            jd "By the way, don't you think it's getting too loud in here?"
            scene 9partylr08 with dissolve
            ls "Ehh... I hope it's not because of me."
            scene 9partylr07 with dissolve
            jd "No, of course not. Just... My head is already buzzing with all this talking and music."
            scene 9partylr07a with dissolve
            mc "If you want, we can go upstairs. It seems to be quieter there."
            jd "If you don't mind, let's do it."
            scene 9partylr08b with dissolve
            ls "Okay, let's go."
            if day09_emma_hand_positive == True:
                scene black with fade
                "You felt the phone in your pocket vibrate."
                scene 9partylr09 with dissolve
                mc "{i}A message from... Emma?{/i}"
                em "\"I can't find you. I'm waiting on the second floor in the back room down the hall.\""
                mc "{i}That's interesting.{/i}"
                mc "{i}And what should I do? Should I go with Lisa and Jade, or should I meet with Emma?{/i}"
                $day09_wt_emma=False
                $day09_wt_lisa_jade=False
                menu emma_lisa_jade:
                    "Meet Emma (Emma scene)" if day09_wt_emma==False:
                        $day09_wt_emma=True
                        mc "{i}I'm not sure what Emma wants from me, but I'm very interested.{/i}"
                        scene 9partylr08b with dissolve
                        ls "Is everything okay?"
                        mc "Yeah, it's no big deal."
                        mc "You go upstairs for now, and I'll find you later."
                        scene 9partylr08 with dissolve
                        ls "Oh... Okay."
                        ls "Then find us when you're done with your business."
                        mc "Yeah, okay."
                        jump day09_emma_lewd

                    "Stay with Lisa and Jade (Lisa/Jade scene)" if day09_wt_lisa_jade==False:
                        $day09_wt_lisa_jade=True
                        mc "{i}No way! There's nothing to think about, I'm staying with Lisa and Jade.{/i}"
                        scene 9partylr08b with dissolve
                        ls "Is everything okay?"
                        mc "Yeah, it's no big deal."
                        scene 9partylr10 with dissolve
                        mc "Wait, I'm gonna grab some booze and let's go."
                        ls "That's a great plan! Hehe!"
                        jump day09_lisa_jade_lewd
            
            scene 9partylr10 with dissolve
            mc "Wait a minute, I'm gonna grab some booze and let's go."
            ls "That's a great plan! Hehe!"
            stop music fadeout 3.0
            jump day09_lisa_jade_lewd
            

label day09_lisa_jade_lewd:
    if _in_replay:
        $ setReplay()
    $ day09_lisa_jade_true = True
    scene black with fade
    "You went up to the second floor."
    scene 9partyfun01 with dissolve
    play music "music/3 - Dream With U.ogg"
    mc "Yeah, I think this room's free."
    ls "Finally! I was beginning to think these kissing couples were after me."
    mc "{i}And not just you.{/i}"
    mc "What do you think, Jade? Shall we stay here?"
    jd "Yeah, this place is fine."
    scene 9partyfun02 with dissolve
    ls "Hey, look at the nice bedrooms in this house!"
    ls "And what a gorgeous view from the window."
    scene 9partyfun03 with dissolve
    mc "{i}I wouldn't say there was anything special in this room, but it's pretty well furnished.{/i}"
    scene 9partyfun02 with dissolve
    ls "Okay, I've decided we're gonna go to the balcony and we're gonna drink this bottle!"
    mc "I like this idea."
    jd "..."
    ls "And now..."
    scene 9partyfun04 with dissolve
    ls "Yahoo!!!!!!"
    scene 9partyfun05 with vpunch
    ls "Aaahhh!"
    ls "The bed is so soft... I would love to stay here all night."
    mc "Hey, stop lying around, we wanted to go to the balcony."
    scene 9partyfun06 with dissolve
    ls "Oh, man, just try it yourself! That's really cool."
    ls "I've never seen such soft beds in my life."
    scene 9partyfun07 with dissolve
    mc "{i}Wow...{/i}"
    mc "{i}What a gorgeous view we have here.{/i}"
    scene 9partyfun08 with dissolve
    ls "Hey, why are you so quiet?"
    "..."
    ls "Hellooo?"
    mc "{i}It's weird that Jade hasn't told her anything yet.{/i}"
    mc "{i}Then I'm gonna have to do it myself. Otherwise the consequences can be unpleasant...{/i}"
    mc "Ahem... Lisa... Your vest..."
    ls "What's the vest?"
    scene 9partyfun09 with dissolve
    "..."
    scene 9partyfun10 with vpunch
    ls "Whoa!"
    ls "Stop it! Stop looking at me!"
    ls "Everybody turn around."
    scene black with fade
    "In a few seconds, embarrassment and awkwardness."
    scene 9partyfun11 with dissolve
    ls "You guys are such assholes! Instead of staring at me, you could've said it right away."
    mc "{i}Didn't I tell her?{/i}"    
    ls "You know, if you're so mean, I'm just gonna stay on this bed and not go anywhere."
    mc "{i}Is it just me or is she fooling around?{/i}"
    mc "Come on, Lisa... The balcony will be much better."
    ls "Nope! I told you, I'm not going anywhere! It's your fault."
    scene 9partyfun12 with dissolve
    "You and Jade looked at each other."
    mc "Grab her legs and I'll take her by the arms."
    jd "Okay."
    ls "Hey! Guys, come on! I was just kidding."
    scene 9partyfun13 with dissolve
    ls "Ow! I get it! I'll go myself, just let go!"
    ls "First they stared at me, and then... This!"
    scene 9partyfun14 with dissolve
    mc "Any more fooling around, Jade and I will throw you in the pool. It's right under that window there."
    ls "Okay, I'll be good, just let go."
    scene 9partyfun13 with dissolve
    mc "You're not gonna kick?"
    ls "I won't, I promise you!"
    mc "So, Jade, shall we take her word for it?"
    jd "Yes... I think so, yes."
    scene 9partyfun15 with dissolve
    "A moment later, Lisa was free."    
    ls "Wow! You're such bad guys!"
    ls "I can't believe I'm still friends with you."
    mc "We may be bad guys, but we know how to get things done."
    ls "Huh. That's for sure."
    stop music fadeout 3.0
    scene 9partyfun16 with dissolve
    ls "Okay, enough standing here. Let's go."
    scene 9partyfun17 with dissolve
    play music "music/Maxim Nick - It's okay (final).mp3"
    "You went out on the balcony."
    ls "It's so nice here."
    ls "Fresh air, the night sky..."
    jd "Yeah."
    mc "And also a nice company and a bottle of strong whiskey."
    scene 9partyfun18 with dissolve
    ls "So what are we waiting for? Let's open this bottle!"
    mc "Gladly."
    if jade_path == True or _in_replay:
        scene black with fade
        "Some time later."
        scene 9partyfun19 with dissolve     
        ls "Hahaha! What a story!"
        ls "I never thought your first kiss was like that!"
        mc "Hey, I was just a naive schoolboy at the time! Of course, it didn't work out the way I wanted it to."
        scene 9partyfun20 with dissolve
        ls "Well, at least now you're a great kisser!"
        mc "Oh, yeah?"
        ls "Oh, yes, you are!"
        scene 9partyfun21 with dissolve
        "Like trying to prove it, Lisa leaned over and kissed you."
        ls "Mmmm..."
        scene 9partyfun22 with dissolve
        "You were suddenly carried away by this activity."
        mc "{i}OOohhhh... It's so nice...{/i}"
        mc "{i}I don't want this moment to end.{/i}"
        "..."
        mc "{i}Wait a minute... We are not alone here!{/i}" 
        scene 9partyfun23 with dissolve
        mc "Hey, wait...  Let's be decent, we're not alone here."
        ls "Mmm... What?"
        scene 9partyfun24 with dissolve
        mc "I'm saying we're not alone here."
        ls "Oh... Yeah, that's right... I forgot."
        mc "{i}I suppose alcohol contributed to that.{/i}" 
        mc "{i}Damn it... I'm already drunk myself.{/i}" 
        scene 9partyfun24a with dissolve
        ls "I can't believe I forgot about Jade."
        scene 9partyfun26 with dissolve
        "You barely blinked before Lisa got near Jade."
        ls "You're so beautiful..."
        ls "It would be a shame if no one kissed you now."
        scene 9partyfun28 with dissolve
        "The girls turned their heads in your direction, as if asking you if they should go on."
        stop music fadeout 3.0
        ls "Want to see what happens next?"
        menu:
            "Stop them":
                mc "I think that's enough for today. You are too drunk."
                scene 9partyfun28a with dissolve
                "..."            
                ls "Y-yeah... I guess you're right... It would be better if we stopped now."
                $ renpy.end_replay()
                scene black with fade
                "Soon you finished fooling around and came downstairs."
                jump day09_end
            "{color=#66FF33}Let them continue":
                $ day09_lisa_jade_lewd = True
                mc "{i}Let's see where this goes.{/i}"
                mc "Go on."
                ls "Hehe! I knew you'd say that."
                play music "music/1 - Atmosphere.ogg"
                scene 9partyfun25 with dissolve
                "There was a small moan and the lips of the girls joined."
                mc "{i}Yes... It's very hot.{/i}" 
                scene 9partyfun27 with dissolve
                "Jade's hands moved smoothly onto her friend's ass."
                mc "{i}Wow, our dark-haired beauty isn't wasting her time.{/i}"
                scene 9partyfun26 with dissolve
                ls "Mm-hmm... It was great..."
                ls "But I want to try something else."
                scene 9partyfun29 with dissolve
                jd "Ahh!"
                ls "Hey, [mc], look what I got in my hands!"
                ls "Her boobs are so soft..."
                mc "{i}Even though I like this show, I think it's going too far.{/i}" 
                mc "Lisa, I think you're out of line."
                scene 9partyfun29a with dissolve
                "The girl stopped abruptly."
                ls "I've... Really? Um..."
                scene 9partyfun30 with dissolve
                jd "Wait... It's okay, you can continue what you did..."
                mc "{i}What? Is she serious?!{/i}"
                scene 9partyfun30a with dissolve
                ls "You see, she likes it herself!"
                ls "Then why stop?"
                scene 9partyfun31 with dissolve
                ls "Now, let's see what's hiding under that cute T-shirt."
                scene 9partyfun31a with dissolve
                "..."
                ls "Mmm... Jade's breasts are so beautiful. [mc], don't you think so?"
                mc "Yeah. Very beautiful."
                scene 9partyfun32 with dissolve
                jd "Wait... I changed my mind, let's stop."
                ls "Heh! It's too late to back down."
                ls "Look, if I take the top off myself, it'll make it easier for you, too."
                scene 9partyfun33 with dissolve
                "Lisa's fingers touched the zipper of her vest."
                scene 9partyfun33a with dissolve
                ls "There you go!"
                mc "{i}Is this really happening?{/i}" 
                scene 9partyfun34 with dissolve
                ls "Look at that hungry look in [mc]. He likes what he sees."
                ls "Should we continue?"
                mc "Don't ask me stupid questions."
                ls "That's what I thought. Hehe."
                scene 9partyfun35 with dissolve
                "The distance between the girls is shortened."
                mc "{i}Looks like Jade liked Lisa's tits.{/i}" 
                mc "{i}I can't blame her for that, though. They are beautiful.{/i}" 
                scene 9partyfun36 with dissolve
                ls "Come here, Jade."
                jd "Okay..."
                scene 9partyfun37 with dissolve
                ls "Aaahh..."
                jd "Mmmm..."
                mc "{i}It's just so... Beautiful...{/i}"
                "..."
                mc "{i}But perhaps it's time to remind them of yourself.{/i}"            
                mc "Ahem!!!"
                scene 9partyfun38 with dissolve
                mc "Ladies, it was a very hot scene, but don't forget you are not alone here."
                ls "Oh, yeah?"
                ls "Jade, let's show [mc] that we haven't forgotten about him."
                jd "Yes..."
                scene 9partyfun39 with dissolve
                "The girls started to slowly approach you."
                mc "{i}Right now, they look like lionesses on the hunt.{/i}"
                scene 9partyfun40 with dissolve
                mc "I don't mean to be a nerd and ruin the fun, but won't we all regret it tomorrow?"
                ls "Pfft! What difference does it make... It will be tomorrow."
                mc "{i}For my future safety, I just had to say it.{/i}"
                mc "{i}And now we can have fun at the limit!{/i}"
                scene 9partyfun41 with dissolve
                mc "{i}Oohhhh... Yeah!{/i}"
                mc "{i}How exciting it is to kiss Jade right in front of Lisa...{/i}"
                scene 9partyfun42 with vpunch
                "Suddenly Lisa interrupted your kiss and pushed you to the floor."
                ls "Hey, stop kissing! Let's get down to something more depraved."
                mc "Ooh! I love how determined you are today."
                scene 9partyfun43 with dissolve
                "Lisa and Jade started pulling your clothes off."
                ls "Wait a little longer... You'll like it a lot more."
                scene 9partyfun43a with dissolve
                ls "Oh, yeah!"        
                ls "Look at this, Jade... It's because of us that he has such a huge boner."
                jd "It's so big..."               
                scene 9partyfun44 with dissolve
                ls "Now just try to relax. We'll take care of you."
                mc "I can't wait to see it."
                scene 9partyfun45 with dissolve
                "Lisa's got your penis in both hands and started massaging it slowly."
                scene anim83 with dissolve
                ls "Let's start with something minor..."
                mc "Ohhh... Yes..."
                ls "Must be nice to have two girls please you, huh?"
                ls "You don't have to say anything, I already know the answer."
                mc "{i}Yeah, her graceful hands know exactly what they're doing.{/i}"
                ls "Okay... Now let's try to do this..."
                pause
                scene 9partyfun46 with dissolve
                "Lisa's hot tongue touched your dick's head."
                scene anim84 with dissolve
                ls "Mmmm... It's become so hard... Amazing!"
                mc "{i}Oohhhh... Lisa licks my dick right in front of Jade...{/i}"
                mc "{i}I can even feel her heavy breathing.{/i}"
                mc "{i}That's so hot!{/i}"
                mc "Aaahhhhh... Now take it in your mouth."
                ls "Um... Whatever you say, babe..."
                pause
                scene 9partyfun47 with dissolve
                "The next second, your dick was in Lisa's mouth."
                scene anim85 with dissolve
                ls "Mmmhhhhh... Mmmmhhhhh... Mmmmhhhhh..."
                mc "{i}She sucks so good.{/i}"
                mc "Oohhhh... Go on... Don't stop!"
                mc "It's, uh... It's so nice."
                ls "Mmmmppphhhsss.... Mmmmpphhhhhss... Mmmmppphhhhhss..."
                pause
                scene 9partyfun47 with dissolve
                "Suddenly Lisa stopped."
                scene 9partyfun47a with dissolve
                "..."
                scene 9partyfun47b with dissolve
                ls "I think you and I have gotten too carried away and forgotten about someone."
                mc "Yeah, you're right."
                scene 9partyfun48 with dissolve
                mc "Jade... Why don't you join us?"
                jd "I'm not sure..."
                ls "Come on! Come here!"
                scene 9partyfun49 with dissolve
                "Giving in to Lisa's persuasion, Jade touched your dick gently."
                jd "Like that?"
                mc "{i}She's obviously out of her league. I need to cheer her up.{/i}"
                mc "That's right, be bolder."
                scene 9partyfun50 with dissolve
                "Meanwhile, your hand touched her ass and started caressing her carefully."
                mc "Ohh..."
                ls "Now try touching him with your tongue."
                scene 9partyfun51 with dissolve
                jd "Mmmm..."
                jd "Does it feel good?"
                ls "Don't worry about him, he really feels good about it!"
                ls "Now put it in your mouth..."
                scene 9partyfun52 with dissolve
                "Lisa put her hand on Jade's head and smoothly set her direction."
                scene anim86 with dissolve
                mc "Oohhhh... Yes!"
                mc "{i}She swallows my dick so deeply... It's just a thrill!{/i}"
                jd "Mmmpphhhss... Mmmmpphhhss... Mmmmpphhss..."
                ls "Look at you, you're a good sucker!"
                jd "Mmmpphhhss! Mmmmpphhhss!! Mmmmpphhss!!!"
                ls "Try to take his dick deeper... Let him moan with pleasure..."
                mc "{i}Oohhhh... Jade is really trying her best...{/i}"
                mc "Mmmm... More! A little more!"
                pause
                scene 9partyfun53 with dissolve
                ls "I see you like Jade's mouth."
                ls "What if I join her?"
                mc "Ahhhh... Why don't we check it out?"
                scene 9partyfun54 with dissolve
                "The next thing you know, your girls' little tongues started licking your dick from the top to the bottom."
                scene anim87 with dissolve
                mc "{i}Oh, my God, it's so good...{/i}"
                ls "It's... So... Hard..."
                jd "*heavy breathing*"
                mc "{i}I can't hold back any longer...{/i}"
                mc "{i}Just a little bit more!{/i}"           
                mc "Aaahhhh! I'm coming!"
                scene 9partyfun55 with flash
                mc "{i}Ohhh yeesss!!!!!{/i}"
                scene 9partyfun55 with flash
                "..."
                stop music fadeout 3.0
                scene 9partyfun56 with dissolve
                ls "Haah... haah... haah..."
                ls "Feeling good, don't you?"
                mc "Yeah, I really do."
                jd "It was... great..."
                scene 9partyfun57 with dissolve
                mc "Girls... It was legendary!"
                mc "Maybe we should keep going."
                scene 9partyfun56 with dissolve
                ls "Mm-hmm... I think it would be wrong to stop halfway."
                ls "What do you think, Jade?"
                jd "I'm thinking-"
                play sound "music/knock.mp3"
                scene 9partyfun58 with vpunch
                "*A STRONG KNOCK ON THE DOOR!!!*"
                stop sound fadeout 2.0
                "???" "Hey, guys, get out of there! Party's over!"
                mc "{i}No, no, no, not now!{/i}"
                play sound "music/knock.mp3"            
                scene 9partyfun58 with vpunch
                "*A STRONG KNOCK ON THE DOOR!!!*"
                stop sound fadeout 2.0            
                "???" "Don't make us use the key!"
                mc "{i}Oh, fuck.{/i}"
                scene 9partyfun59 with dissolve
                "Lisa and Jade rushed straight to their clothes."
                mc "{i}Eh... Looks like we're never gonna make it to the top of the list today.{/i}"
                "..."
                mc "{i}Okay, I guess I should get dressed, too.{/i}"

                $ renpy.end_replay()
                if not persistent.day09lisajade:
                    $ renpy.notify(['SAHNE KILIDI ACILDI'])
                    $ persistent.day09lisajade = True

                scene black with fade
                menu:
                    "Meet Emma" if day09_emma_hand_positive==True and day09_wt_emma==False:
                        jump emma_lisa_jade
                    "Continue":
                        pass
                scene black with fade
                "Soon you opened the door and came downstairs."
                jump day09_end
    else:
        stop music fadeout 3.0
        scene black with fade
        "You were drinking and talking for a while until the party came to an end."
        menu:
                "Meet Emma" if day09_emma_hand_positive==True and day09_wt_emma==False:
                        jump emma_lisa_jade
                "Continue":
                        pass
        scene black with fade
        "Soon you opened the door and came downstairs."
        jump day09_end


label day09_emma_lewd:
    if _in_replay:
        $ setReplay()
    scene 9emma01 with dissolve
    "You went upstairs and went to the room where you were supposed to meet Emma."
    mc "{i}I'm still not sure if I'm doing the right thing, but I'm just attracted to her.{/i}"
    scene black with fade
    "Knock knock!"
    play sound "music/Door.wav" 
    scene 9emma02 with dissolve
    play music "music/6 - Positive Mood.ogg"
    em "You're here after all."
    mc "Are you surprised?"
    em "Kind of. I saw that you were with the girls from your band."
    scene 9emma03 with dissolve
    "You walked into the room and closed the door behind you."
    mc "Is that why you sent me the message?"
    em "You mentioned that you were dating someone... I decided not to give you too much trouble."
    mc "Really?"
    em "Is that so hard to believe?"
    mc "No... I think not."
    scene 9emma04 with dissolve
    "Emma fell on the bed."
    mc "Hey, you can't wear shoes on the bed."
    scene 9emma05 with dissolve
    em "Pfft... You sound just like my mom right now."
    "..."  
    em "Okay, if it's that important to you, I'll take them off."
    scene 9emma06 with dissolve
    "Emma unbuttoned the buckles on her boots."
    scene 9emma07 with dissolve
    em "Ah!"
    em "That's even better. Thank you for the advice."
    mc "You're welcome."
    scene 9emma07a with dissolve
    mc "{i}Yeah, well... I have to say, she looks very tempting.{/i}"
    scene 9emma08 with dissolve
    em "So, can we get started?"
    mc "Get started? You mean..."
    em "Exactly. We both know why you're here, and we both want to."
    em "So why beat around the bush after everything we've been through?"
    stop music fadeout 3.0
    mc "{i}It was pretty straightforward... The only question is, do I really want it?{/i}"
    menu:
        "{color=#66FF33}Stay with Emma":
            $ day09_emma_lewd = True
            scene 9emma09 with dissolve
            "You came to the front door."
            em "Wait, where are you going?"
            mc "I'll lock the door. I don't want anyone to interrupt us at the most important moment."
            mc "{i}With my shitty luck, it definitely would have happened.{/i}"
            em "Yeah, you're right, we don't need an audience."
            play music "music/15 - Deep Mood.ogg"
            scene 9emma10 with dissolve
            mc "So that's what we both want?"
            mc "{i}Wow... And when did she get her top down?{/i}"
            em "Yes, we do..."
            scene 9emma11 with dissolve
            em "Even though our lives have gone in different ways, you have to agree that our sex has always been amazing."
            em "So why not spend another good night together?"
            mc "{i}She's right about that. We always knew how to please each other.{/i}"
            scene 9emma12 with dissolve
            mc "I guess I'm crazy if I've been thinking about this for so long."
            mc "How could I say no?"
            em "Hehe. You couldn't."
            scene 9emma13 with dissolve
            em "Let's drop all the clothes we don't need."
            mc "That's a great idea."
            scene 9emma13a with dissolve
            "..."
            scene 9emma13b with dissolve
            em "That's it!"
            mc "{i}She's got an amazing body.{/i}"
            em "And now..."
            scene 9emma14 with dissolve
            "You barely had time to blink when your face was right in front of Emma's chest."
            mc "Ohhhh... What a lovely view."
            em "It's hard to resist that, isn't it?"
            mc "It's just impossible."
            scene 9emma15 with dissolve
            "The next second you kissed Emma."
            scene anim71 with dissolve
            em "Mmmm...."
            mc "{i}Oohhhh... I almost forgot how well she kisses...{/i}"
            pause
            scene 9emma15 with dissolve
            em "Ah!"
            scene 9emma16 with dissolve
            "Your hands are slipping down smoothly."
            mc "{i}Oh, yeah... Great.{/i}"
            scene 9emma17 with dissolve
            em "Looks like your naughty hands are looking forward to the fun."
            mc "How can you blame them for that?"
            em "I cant."
            mc "That's exactly what I'm saying. Now is the time to take it seriously."
            scene 9emma18 with vpunch
            "You pushed Emma to the bed."
            em "Hahahaha! Why are you so suddenly?"
            mc "{i}Uh, I can see her nipples now.{/i}"
            scene 9emma19 with dissolve
            mc "Like you said, we'll get rid of all the clothes."
            scene 9emma19a with dissolve
            mc "Just like that!"
            scene 9emma20 with dissolve
            mc "If only you knew how much my naughty hands missed your fancy body..."
            em "Mm-hmm. If you're wondering, I missed them too."
            scene 9emma20a with dissolve
            "Your palms slipped up the girl's waist and stopped at her tits."
            scene anim72 with dissolve
            em "Aahhh!"
            mc "Yes... Here comes the best part..."
            mc "{i}Her tits are so soft...{/i}"
            em "Mmmm... [mc]..."
            mc "{i}Okay, I'm getting a little too carried away.{/i}"
            pause
            scene 9emma21 with dissolve
            mc "Now, let's get these cute shorts off you."
            scene 9emma21a with dissolve
            mc "{i}Oh, yeah! That's the main part!{/i}"
            scene 9emma22 with dissolve
            mc "Wow..."
            mc "When you're completely naked, you look so cute and innocent."
            scene 9emma23 with dissolve
            em "Oh, but I'm really cute... And as for innocence, then..."
            em "If you bite me, I'll bite you back."
            mc "Haha! Thanks for the heads-up!"
            scene 9emma24 with dissolve
            mc "{i}What an amazing ass she's got there.{/i}"
            mc "{i}Maybe we shouldn't have broken up.{/i}"
            mc "{i}Okay, [mc], don't get your head into this right now.{/i}"
            scene 9emma25 with dissolve
            "Without wasting time, you threw off your clothes."
            em "Come on, come here. I want to feel your dick inside me."
            mc "Everything in due time..."
            scene 9emma27 with dissolve
            mc "{i}Let's start gently with her pussy...{/i}"
            em "Aaahhh... Yes...."
            mc "{i}Then we'll go higher.{/i}"            
            scene 9emma28 with dissolve
            "Your lips stopped at Emma's nipples."
            em "Mmmm... It's so nice..."
            scene 9emma29 with dissolve
            mc "{i}They've become so hard.{/i}" 
            mc "{i}She seems to be enjoying this moment.{/i}"
            scene 9emma30 with dissolve
            em "Haaah... Haah... I don't know where you learned that, but it was great."
            mc "But we're just getting started. The best part is still ahead."
            em "Then what are we waiting for?"
            scene 9emma31 with dissolve
            "You kissed Emma again."
            mc "Yeah, let's start."
            scene 9emma32 with dissolve
            "Moment later you were both on the bed."
            em "Come on [mc], put your dick in my pussy."
            mc "I'd love to."
            scene 9emma33 with dissolve
            em "Mmmm... Yes... Here we go..."
            mc "{i}She's already wet.{/i}"
            mc "{i}And now I'm putting it in.{/i}"
            scene 9emma34 with dissolve
            em "Aaahhh! Your dick is inside!"
            mc "{i}Oh, yeah... She's so tight...{/i}"
            scene 9emma35 with dissolve
            "You grabbed Emma by the legs and started moving."
            scene anim73 with dissolve
            em "Aaahhh.... Ahhh... Aaahh..."
            em "Oh... Your dick... It's so hot."
            mc "{i}She looks so lustful right now. I missed it so much!{/i}"
            pause
            scene anim74 with dissolve
            em "I feel so good... Don't stop!"
            em "Haahhhh!! Haaaahhh!!!"
            mc "{i}It's so nice.{/i}"            
            scene 9emma36 with dissolve
            "Emma wrapped her arms and legs around you."
            scene anim75 with dissolve
            em "Harder... Please fuck me harder!"
            mc "{i}The way she's pressed against me, it just blows my mind.{/i}"
            em "Aaahhh.... Ahhh... Aaahh..."
            pause
            scene anim76 with dissolve
            em "Haahhhh!! Haaaahhh!!!"
            em "More! Fuck me more! [mc]!" 
            mc "Ohh.. Yeah..."           
            mc "It's very good, but I think... I think we need to change the pose."
            em "If that's what you want..."
            pause
            scene 9emma37 with dissolve 
            "You turned Emma on her side."
            em "Mm-hmm... What do you want to do?"
            mc "You'll see."
            scene 9emma38 with dissolve 
            "The next thing you know, you've been driving your dick to Emma and kissing her at the same time."
            scene anim77 with dissolve 
            em "Mmm..."
            mc "{i}Oohhhh... It seems she got more aroused by it.{/i}"
            em "Yeah... Yeah! Harder!"
            mc "{i}Aaahhh... The longer I fuck her, the more I want her.{/i}"
            em "Don't stop, push your dick deeper!"
            pause
            scene 9emma39 with dissolve
            mc "I don't think I'm gonna last long..."
            em "Ahhhh... Then come here."
            mc "{i}Where do I come to?{/i}"
            menu:
                "Come in Emma's mouth":
                    scene 9emma43 with dissolve
                    "Soon your dick was in Emma's mouth."
                    scene anim79 with dissolve
                    em "Mmmmppphhhsss.... Mmmppphhhss.... Mmmphhhss.."
                    mc "Oh, yeah... Suck it, baby! Suck harder!"
                    em "Mmppphhhsss!!! Mmmmppphhss!!! Mmmmppphsss!!!"
                    mc "Just a little more... A little bit more..."
                    mc "I'm coming!"
                    scene 9emma44 with flash
                    mc "Yeeees!!!"
                    scene 9emma44 with flash
                    "..."                    
                    scene 9emma44a with dissolve
                    "..."
                    scene 9emma44b with dissolve
                    "..."
                    scene 9emma44c with dissolve
                    em "I didn't expect so much sperm."
                    mc "I'm sorry?"
                    em "Huh. It's all right."
                    em "Let's get ourselves cleaned up."


                "Come on Emma's face":
                    scene 9emma40 with dissolve
                    "Soon you were right in front of Emma's face."
                    scene anim78 with dissolve
                    em "Come on, [mc]!"
                    em "Give me all your sperm!"
                    mc "Oh yeah... It feels good..."
                    mc "I'm coming!"
                    scene 9emma41 with flash
                    mc "Yeeees!!!"
                    scene 9emma41 with flash
                    "..."                    
                    scene 9emma42 with dissolve
                    em "Mmm... Not bad."
                    em "I didn't expect so much sperm."
                    mc "I'm sorry?"
                    em "Huh. It's all right."
                    em "Let's get ourselves cleaned up."

        "Leave":
            scene 9emma09 with dissolve
            "You came to the front door."
            em "Wait, where are you going?"
            mc "I'm sorry, but I'm not interested."
            $ renpy.end_replay()
            scene 9emma09a with dissolve
            "You left the room and came downstairs."
            menu:
                    "Meet Lisa and Jade" if day09_wt_lisa_jade==False:
                        jump emma_lisa_jade
                    "Continue":
                        pass
            jump day09_end
  

    $ renpy.end_replay()
    if not persistent.day09emma:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day09emma = True

    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 9emma45 with dissolve
    em "Wow. What a night, huh?"
    mc "Don't tell me."
    "..."
    mc "{i}I don't know why, but I'm always sad to say goodbye to her.{/i}"
    mc "I guess that's it?"
    em "Yeah..."
    em "Although if you want a good cup of coffee, I can offer you the café where I work now."
    em "The food's not good, but the coffee's great."
    mc "Sounds very interesting."
    play sound "music/knock.mp3"
    scene 9emma46 with vpunch
    "*A STRONG KNOCK ON THE DOOR!!!*"
    stop sound fadeout 2.0
    "???" "Hey, guys, get out of there! Party's over!"
    mc "{i}Yeah, that's definitely over now.{/i}"
    play sound "music/knock.mp3"            
    scene 9emma46 with vpunch
    "*A STRONG KNOCK ON THE DOOR!!!*"
    stop sound fadeout 2.0            
    "???" "Don't make us use the key!"
    scene 9emma45 with dissolve
    mc "Looks like we should get going."
    em "Yeah."
    scene black with fade
    "Soon you opened the door and came downstairs."
    menu:
                    "Meet Lisa and Jade" if day09_wt_lisa_jade==False:
                        jump emma_lisa_jade
                    "Continue":
                        pass
    jump day09_end
    

label day09_end:
    scene black with fade
    "Same time, Julia's apartment."
    play music "music/Maxim Nick - Falling Down.mp3"
    scene 9end01 with dissolve
    "..."
    scene 9end01a with dissolve
    "Sound of a new message!"
    scene 9end01 with dissolve
    sis "Mmm..."
    scene 9end01a with vpunch    
    "Sound of a new message!!!!"
    scene 9end02 with dissolve
    sis "Hello..."
    sis "Yes... Yeah, it's me..."
    scene 9end03 with dissolve
    sis "What?"
    sis "When?"
    sis "How bad is he?"
    scene 9end04 with dissolve
    sis "Yes... Yes, I get it."
    sis "Okay, I'll tell them."
    if day09_emma_lewd == True:
        scene 9end05a with dissolve
        "You walked with Emma and talked to her."
    elif day09_lisa_jade_true == True:
        scene 9end05 with dissolve
        "You went with Lisa and Jade and talked to them."
    else:
        scene 9end05b with dissolve
        "You were coming home from a party."
    "Sound of a new message!"
    mc "{i}A call? At such a late hour?{/i}"
    scene 9end06 with dissolve
    mc "{i}Julia?{/i}"
    scene 9end07 with dissolve
    mc "Hi! I didn't expect to hear from you so late."
    "..."
    scene 9end07a with dissolve
    mc "What?"
    "..."
    mc "Yes... Yes... I get it."
    scene 9end06 with dissolve
    "..."
    if day09_emma_lewd == True:
        em "Hey, is everything okay?"
        scene 9end08 with dissolve
        mc "My father had a seizure. He was taken to the hospital."
        em "Oh no..."
        mc "All the relatives are going to get together. My sister asked me to come to them in the morning..."
        mc "{i}I feel like tomorrow's gonna be a tough day.{/i}"
        stop music fadeout 3.0
    elif day09_lisa_jade_true == True:
        ls "[mc], is something wrong?"
        scene 9end08 with dissolve
        mc "My father had a seizure. He was taken to the hospital."
        ls "Oh, my God."
        mc "All the relatives are going to get together. My sister asked me to come to them in the morning..."
        mc "{i}I feel like tomorrow's gonna be a tough day.{/i}"     
        stop music fadeout 3.0   
    else:
        mc "{i}I can't believe... My father had a seizure. Now he is in the hospital.{/i}"
        mc "{i}All the relatives are going to get together. Julia asked me to come and see them in the morning...{/i}"
        mc "{i}I feel like tomorrow's gonna be a tough day.{/i}"
        stop music fadeout 3.0

    jump day10_start


