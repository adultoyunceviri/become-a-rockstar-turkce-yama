
label day10_start:
    scene black with fade
    "Next morning."
    "Like you promised Julia on the phone, first thing in the morning you went to the hospital."
    play music "music/8 - Intro Music.ogg"
    scene 10hospital01 with dissolve
    if selina_path == True:
        mc "{i}Who would have thought that of all the hospitals in this city, my father would be put in the same place where Selina works. That's a curious coincidence.{/i}"
    else:
        mc "{i}That's the hospital where my father was placed. I still can't believe it happened to him.{/i}"
    mc "{i}Well, I don't have to wait outside, though. Julia should be there by now.{/i}"
    if selina_path == True and selina_broke_up == False:
        stop music fadeout 1.0
        scene 10selina01 with dissolve
        play music "music/6 - Positive Mood.ogg"
        "When you approached the hospital reception, you noticed Selina."
        mc "{i}Hmm. I didn't even think about whether she was working today.{/i}"
        mc "{i}Although... I'm not thinking straight about this whole thing right now.{/i}"
        mc "{i}I should say hello to her.{/i}"
        mc "Selina?"
        scene 10selina02 with dissolve
        s "[mc]?!"
        s "Oh, wow! What a wonderful encounter!"
        mc "Yeah... I'm sorry I didn't warn you about being here."
        scene 10selina03 with dissolve
        s "It's okay. And to tell you the truth, this is a very nice surprise."
        mc "Yeah, good to see you too."
        s "Uh... You know, it's pretty loud in here. How about we talk somewhere more quiet?"
        mc "{i}Well, I guess I have time for that.{/i}"
        mc "Sure, why not."
        scene 10selina03a with dissolve
        s "Sorry, Elsa, I'll talk to you later. Okay?"
        "{color=#90EE90}Elsa{/color}" "Yes, of course, no problem."
        scene 10selina04 with dissolve
        s "Come on, let's go!"
        mc "Yes, let's go."
        scene 10selina05 with dissolve
        "Selina took you to one of the rooms that was empty."
        s "Yeah, this place is good."
        scene 10selina05a with dissolve
        s "No one's gonna bother us here."
        mc "{i}She seems to be in a very good mood.{/i}"
        scene 10selina06 with dissolve
        "You walked over to Selena and put your arm around her waist."
        mc "I gotta say, you look great in that white coat."
        s "Hehe. Thank you."
        scene 10selina07 with dissolve
        "The next second, you kissed."
        s "Mmm..."
        mc "{i}Her kisses are always very nice.{/i}"
        mc "{i}Too bad I don't have much time right now.{/i}"
        scene 10selina08 with dissolve
        s "Oh... What a warm welcome. I loved it."
        mc "Believe me, it's a mutual feeling."
        s "Hee-hee. I really hope so!"
        scene 10selina09 with dissolve
        s "All right, let's not stand in the middle of the room and go sit down somewhere."
        scene 10selina10 with dissolve
        s "So, what brings you to our hospital at this early hour?"
        s "Did you plan on giving me a surprise or-"
        mc "I wish I was here for that reason, but that's not the point. My father had a seizure last night and the paramedics brought him here."
        scene 10selina11 with dissolve
        s "Oh, my God... I hope he's okay."
        mc "Well, I don't know much yet. But my sister said on the phone that the danger was over."
        scene 10selina12 with dissolve
        s "So, that's how it is. Then I'm glad it's all taken care of."
        mc "Yeah. I'm here to see him."
        s "I see."
        s "And what about you? Are you all right?"
        scene 10selina10 with dissolve
        mc "I don't know. I guess I am."
        mc "To tell you the truth, he and I rarely got along. But all this... It all happened so suddenly."
        mc "Yesterday he was the king of the world, one of the most influential people of this city, and now he just lies here like an ordinary patient."
        scene 10selina12 with dissolve
        s "We are all equal before disease."
        mc "Yeah. It's a lot to think about."
        scene 10selina13 with dissolve
        s "Well, at least you don't have to worry about his treatment. We have one of the best hospitals in the city."
        s "If your father is here, he's in good hands."
        scene 10selina14 with dissolve
        mc "Yeah, I guess that's good. And thank you for your support, it means a lot."
        s "Anytime."
        mc "Well, I should probably get going. See you later."
        s "Yeah, well... See you later."
        scene 10selina15 with dissolve
        "When you went to the door, you suddenly felt Selina give you a big hug from behind."
        mc "{i}She's so sweet. And she really cares about me.{/i}"
        scene 10selina16 with dissolve
        s "If you need to talk or help in any other way, you know I'm always there for you."
        mc "Thank you."
        stop music fadeout 3.0
        scene black with fade
        "You asked the hospital administrator for father's room number and went there."
        play music "music/8 - Intro Music.ogg"
    else:
        scene 10selina01a with dissolve
        "You asked the hospital administrator for father's room number and went there."
    scene 10hospital02 with dissolve
    "At the entrance to the room, you saw Julia."
    mc "{i}I wonder who she's talking to so loudly.{/i}"
    mc "{i}Whoa. Wait a minute, that's... Yeah, that's right. This is Marcus, my older brother.{/i}"
    scene 10hospital03 with dissolve
    sis "Wait, Marcus. [mc] is here."
    mar "What?"
    scene 10hospital03a with dissolve
    sis "Take a look."
    mar "That's right."
    mar "What a surprise, our little brother decided to come after all."
    mc "Why does that surprise you?"
    scene 10hospital04 with dissolve
    mar "Well, after what Julia told me recently, I had my doubts about it."
    mc "{i}I wonder what she told him.{/i}"
    mar "But it's good to have you here."
    mc "Of course, family is family. And if you mean my little disagreement with father, it doesn't matter now."
    sis "That's right. We're really glad you're here."
    scene 10hospital07 with dissolve
    mar "Hm... Disagreements aren't important? What mature words. I didn't expect to hear them from you."
    mar "Looks like a life without father's money had a positive impact on you."
    mc "{i}I don't really like this conversation.{/i}"
    mc "I don't know why you're telling me all this now, but I didn't come here to discuss my personal life."
    sis "He's right, Marcus. Leave your squabbles at least for today."
    scene 10hospital08 with dissolve
    mar "It wouldn't hurt him to hear the truth from his older brother. Especially since it was a compliment."
    sis "Marcus."
    mar "You're right, though... We'll save this conversation for later."
    scene 10hospital09 with dissolve
    mar "Okay, I'm gonna take a walk. If anything happens, call me."
    sis "Okay."
    scene 10hospital10 with dissolve
    mc "So... You said on the phone that father had a seizure. How is he now?"
    sis "He's better. The doctors fixed him up pretty well, and now he's resting in the ward."
    mc "That's good. But what's all this about, anyway?"
    "..."
    mc "Julia?"
    scene 10hospital05a with dissolve
    sis "Dad didn't tell you this, but he has had a very rare and dangerous disease for six months now."
    sis "I don't want to burden you with details, but this is a very serious disease and in most cases it's untreatable."
    scene 10hospital06a with dissolve
    mc "Wait, wait, wait... You're saying he's been sick with some shit for six months and I don't know anything about it?!"
    scene 10hospital05a with dissolve
    sis "Very few people know about it."
    scene 10hospital06b with dissolve
    mc "Yes, but you can't hide things like that!"
    mc "Besides, I'm his son, and I probably should have known about it!"
    scene 10hospital06c with dissolve
    mc "{i}Damn, maybe I should just calm down a little. I don't know why, but this news has pissed me off.{/i}"
    scene 10hospital10 with dissolve
    mc "Okay... What about Marcus? Does he know about this?"
    sis "Only me, Marcus and Mom know."
    scene 10hospital06 with dissolve
    mc "Then why not tell everybody about it? What's with the secrets? And why didn't you tell me anything yourself?"
    scene 10hospital06a with dissolve
    mc "I thought we trusted each other."
    scene 10hospital11 with dissolve
    sis "I'm sorry, but Dad made me swear not to say anything. I was only doing what he wanted me to do."
    sis "If you asked me to do something like that, I would do the same."
    scene 10hospital06c with dissolve
    mc "Okay... I got it."
    mc "{i}Looks like there's no point in being mad at Julia about it. She did what she thought was right.{/i}"
    scene 10hospital10 with dissolve
    mc "You said something about this disease not being curable. What does that mean?"
    sis "The thing is that treatment only helps in thirty percent of cases. So all we can do now is hope for the best."
    mc "{i}Well... It's not a good prospect.{/i}"
    scene 10hospital05 with dissolve
    sis "Okay, I think that's enough questions. If you want to know anything else, you better ask Dad yourself."
    sis "Especially since he wanted to talk to you himself."
    sis "Oh yeah, and try to go easy on him, he's not fully recovered yet."
    stop music fadeout 3.0
    scene 10hospital06 with dissolve
    mc "All right, I'll do what I can."
    play music "music/6 - Positive Mood.ogg"
    scene 10father01 with dissolve
    "You walked into your father's room and witnessed him talking to the doctor."
    "{color=#DC143C}Karen{/color}" "Considering all the circumstances, you'd better stay here for a couple more days, or even better, the whole week."
    "{color=#DC143C}Karen{/color}" "Also, from this day on, you will need to be examined at least three times a month. Believe me, it's all in your best interest."
    f "Thanks, I hear you."
    scene 10father01a with dissolve
    "..."
    mc "{i}I think they've noticed me.{/i}"
    mc "Excuse me, is this a bad time?"
    f "No, it's okay."
    scene 10father02 with dissolve
    f "Sorry, Doc, could you leave us alone for a minute?"
    scene 10father03 with dissolve
    "{color=#DC143C}Karen{/color}" "Uh... yeah, sure. I'll come back later."
    "{color=#DC143C}Karen{/color}" "Take your time."
    scene 10father04 with dissolve
    "As you walked inside the room, you noticed the doctor's attentive look in your direction."
    if selina_path == True:
        mc "{i}Hey, I know this doctor. I mean, that's Selina's ex-friend. And it looks like she recognized me, too.{/i}"
        mc "{i}I hope she's a better doctor than friend.{/i}"
    else:
        mc "{i}Hmm. Why is she looking at me like that?{/i}"
    scene black with fade
    "The doctor left the ward, leaving you and your father alone."
    scene 10father05 with dissolve
    f "I'm glad you're here, [mc]."
    f "Given all our recent disagreements, I don't think it was easy for you."
    mc "And yet here I am."
    f "Yes, you are."
    scene 10father06 with dissolve
    mc "So... Are you okay?"
    f "Yeah, I'm okay. As much as possible the day after a seizure, anyway."
    f "Although I could use a glass of whiskey right now."
    mc "I think the doctors will mind."
    f "Yes, they would."
    mc "{i}Man, it's so weird to see father without his usual expensive suit, tie and everything else that comes with it.{/i}"
    mc "{i}And he looks very different himself. There's no hard core, there's no steadfastness, and there's no hardness in the eye. Right now, he's just a regular patient.{/i}"
    scene 10father10 with dissolve
    mc "I heard from Julia that you wanted to talk to me about something. Is that true?"
    scene 10father07 with dissolve
    f "Yes. I wanted to talk to you about everything that happened after you decided to live on your own."
    mc "{i}Eh, I hope this isn't just another lecture.{/i}"
    f "The thing is, I always thought the main thing in our lives was what you'd leave behind - our legacy."
    f "But when you lie in this room, in the hospital, you rethink a lot. So I realiz-"
    scene 10father07b with dissolve
    f "Cough! Cough!"
    scene 10father07 with dissolve
    f "So I realized that my legacy is not a business or a corporation, and as banal as it sounds, it's you - my children."
    mc "{i}Okay, that was unexpected.{/i}"
    scene 10father07a with dissolve
    f "And I... I want to apologize for all the bad things I did to you. And I want to make it up to you."
    scene 10father07 with dissolve
    f "Even though I'm not going to cancel our deal, I promise to respect your decision to be a musician."
    scene 10father08 with dissolve
    f "So, are we making up?"
    mc "{i}What an interesting outcome.{/i}"
    mc "{i}Maybe I should really make up with him. After all, he didn't do anything really bad.{/i}"
    mc "{i}Rather, all the bad things he's done have inspired me to move forward.{/i}"
    mc "{i}Besides, looking back on this moment in ten or twenty years, I wouldn't want to regret anything.{/i}"
    mc "{i}So what should I do?{/i}"
    stop music fadeout 3.0
    menu:
        "Shake his hand(+Good points/+Father friend)":
            $ day10_father_friends = True
            $ goodpoint += 1
            scene 10father09 with dissolve
            play music "music/6 - Positive Mood.ogg"
            mc "Yeah, we make up."
            f "Good. Okay."
        "Ignore(+Bad point)":
            $ badpoint += 1
            scene 10father10 with dissolve
            play music "music/8 - Intro Music.ogg"
            mc "I appreciate your decision to make up, but let's not be hasty."
            mc "You're saying that only now, under the influence of the moment. Let's see how things work out and see if you change your mind when you get out of the hospital."
            scene 10father07 with dissolve
            f "I guess it's fair."
    scene 10father06 with dissolve
    mc "Now, if that's all you wanted to talk about, I'd better go. Get better."
    f "Yes, yes, of course. Thank you again for coming."
    scene 10father11 with dissolve
    "You left your father's ward in a very thoughtful mood."
    mc "{i}Yeah... What an odd conversation we had. But I hope I did the right thing.{/i}"
    stop music fadeout 3.0
    scene black with fade
    "When you walked into the hospital corridor, you ran into Julia again."
    scene 10hospital11 with dissolve
    play music "music/7 - Just Happy.ogg"
    sis "How was it?"
    mc "{i}Huh. Right to the point?{/i}"
    scene 10hospital06 with dissolve
    mc "Well, to tell you the truth, it went pretty well."
    if day10_father_friends == True:
        mc "I kind of made up with him."
        scene 10hospital05 with dissolve
        sis "Oh, really?"
        mc "Yeah, I didn't see that coming either. But that's the way it is."
        sis "Well, that's good."
    else:
        mc "I talked to him for a while and we cleared up some things. Let's see how it goes from here."
    scene 10hospital10 with dissolve
    mc "Now, if you don't mind, I have to go. I have a lot to do today."
    mc "You know, you don't have to be here yourself anymore. The doctors will take care of him."
    scene 10hospital11 with dissolve
    sis "Thanks for the offer, but I'll stay here for a while."
    mc "Okay, do what you want."
    mc "{i}That's her problem, she cares not only about me, but about our whole crazy family.{/i}"
    mc "{i}Even though Julia is devilishly clever, that part of her personality I still don't understand.{/i}"
    if nicole_plus == True and jane_date_offer == True:
        scene 10hospital12 with dissolve
        sis "Oh, Nicole, you're just in time."
        mc "{i}What? Is Nicole here?{/i}"
        scene 10hospital13 with dissolve
        n "Julia. I brought the documents you asked for."
        mc "{i}Now I get it.{/i}"
        sis "Well done! You helped me out a lot."
        n "No problem, it's my job."
        scene 10hospital14 with dissolve
        mc "Hello, Nicole."
        n "[mc]."
        mc "{i}Huh. She's very restrained, as always.{/i}"
        scene 10hospital15 with dissolve
        n "I heard about what happened to your father. I hope he's okay."
        scene 10hospital17 with dissolve
        sis "He's gonna have to spend some time in the hospital, but, yeah, he's fine."
        scene 10hospital15 with dissolve
        n "That's good."
        scene 10hospital16 with dissolve
        "Nicole gave Julia a big red file of documents."
        scene 10hospital15 with dissolve
        n "If that's all you needed from me, I'd rather go back to the office."
        scene 10hospital19 with dissolve
        mc "That's funny, I was gonna leave, too."
        scene 10hospital18 with dissolve
        n "Hmm? If you want, I can give you a ride."
        mc "{i}That would be very convenient.{/i}"
        scene 10hospital19 with dissolve
        mc "If I'm not distracting you from anything, that'd be great."
        scene 10hospital18 with dissolve
        n "I think I have time to give my boss's brother a ride. If she doesn't mind, of course."
        scene 10hospital17 with dissolve
        sis "No problem. Take him where he asks, and then you can go to the office."
        sis "It's not an easy day, I think Jane will need your help."
        scene 10hospital15 with dissolve
        n "I got you."
        n "Let's go, then, [mc]."
        mc "Yep."
        scene 10hospital20 with dissolve
        mc "So today is a tough day for you, huh?"
        n "It's not a big deal. Just a little more meetings than usual."
        mc "Oh, I see."
        stop music fadeout 3.0
        scene 10hospital21 with dissolve
        "The last thing you saw when you left the hospital was Marcus talking to your father's doctor."
        jump day10_nicole_car
    elif nicole_plus == False and jane_date_offer == True:
        scene 10hospital11a with dissolve
        sis "[mc], I wanted to ask you a favor."
        mc "Yeah?"
        sis "Could you take this folder to my office?"
        sis "You'd be very helpful."
        mc "Okay, no problem at all."
        mc "{i}I'll meet with Jane at the same time.{/i}"
        scene black with fade
        "Soon you said goodbye to Julia and went to her office."
        stop music fadeout 3.0
        scene 10hospital21 with dissolve
        "The last thing you saw when you left the hospital was Marcus talking to your father's doctor."
        jump day10_jane_office
    else:
        scene black with fade
        "Soon you said goodbye to Julia and went home."
        stop music fadeout 3.0
        scene 10hospital21 with dissolve
        "The last thing you saw when you left the hospital was Marcus talking to your father's doctor."
        if lisa_path == True:
            jump day10_lisa_start
        elif lisa_path == False and selina_path == True or rosa_path == True:
            jump day10_home_phone
        else:
            jump day10_rehearsal



label day10_nicole_car:
    scene black with fade
    "Few minutes later."
    play music "music/10 - Street's.ogg"
    scene 10nicole01 with dissolve
    n "So, where do you want me to take you? Right to your house?"
    mc "Yeah, if that's fine with you."
    n "It's no problem."
    scene 10nicole02 with dissolve
    n "By the way, I heard that your relationship with Jane is going really well."
    n "Congratulations."
    mc "Really? Is that what she told you?"
    n "No, but I try to keep up with office rumors."
    mc "{i}Oh, wow. I didn't think they had any office rumors. Not to mention the fact that they'd involve me.{/i}"
    scene 10nicole03 with dissolve
    mc "Hmm. I didn't know you were interested in those things."
    scene 10nicole03a with dissolve
    n "Usually I'm not. But it becomes an exception when it involves one of my bosses."
    scene 10nicole03 with dissolve
    mc "It's interesting."
    mc "Perhaps you could share some interesting office rumors with me then?"
    scene 10nicole03a with dissolve
    n "Mmm... Maybe I could."
    n "But what do I get for it?"
    scene 10nicole04 with dissolve
    "*Phone call*"
    n "Sorry, it's Jane. I have to take this."
    mc "Yeah, sure."
    scene 10nicole05 with dissolve
    n "Hello. Yes, it's me."
    n "Yeah, I gave her all the documents."
    "{cps=15}...{/cps}"
    n "Hmm? How urgent?"
    scene 10nicole06 with dissolve
    n "But Julia told me-"
    n "No, I get it. I'll be right there."
    mc "{i}I think something went wrong.{/i}"
    scene 10nicole07 with dissolve
    n "Shit. That changes things."
    scene 10nicole07a with dissolve
    n "Look, I know I have to take you home, but I need to get to the office right now."
    n "The lawyers got here a little early, and I should be there."
    mc "So you're going to the office?"
    n "Yes... I'm sorry."
    scene 10nicole08 with dissolve
    mc "Okay, then I'll go with you. I'll see Jane at the same time."
    n "You're sure?"
    mc "Yep."
    n "So everything's okay, then?"
    mc "Yeah, it's okay."
    n "Thank you for understanding."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    jump day10_jane_office


label day10_jane_office:
    if nicole_plus == True:
        play music "music/12 - The Moose.ogg"
        scene 10office01 with dissolve
        mc "Do you know where I can find Jane?"
        n "It's lunchtime, which means she has to be at the coffee machine."
        mc "Really?"
        n "Well, it's usually the case."
        mc "Hmm. You've learned other people's habits pretty well."
        n "Thank you, but I'm just observant."
        mc "Uh-huh. Useful quality."
        scene 10office02 with dissolve
        "After walking a few more meters, you ran into Jane."
        mc "{i}Right by the coffee machine, just like Nicole said.{/i}"
        scene 10office03 with dissolve
        "You noticed that Jane is singing some kind of tune."
        jn "La-la-la-la..."
        mc "{i}Wait... That's our tune from that YouTube video!{/i}"
        mc "{i}That's the surprise.{/i}"
        scene 10office04 with dissolve
        n "Like I said, it's her lunch break."
        mc "Yeah, thanks, I get it."
        scene 10office05 with dissolve
        "When Jane heard our voices, she turned around."
        jn "[mc]? What a meeting."
        mc "It's nice to see you, Jane."
        jn "Yeah, nice to see you, too."
        scene 10office06 with dissolve
        mc "I see you're drinking coffee... Do you mind if I join you?"
        jn "I don't know what you're doing here, but I don't see why not."
        mc "Okay, great."
        scene 10office07 with dissolve
        jn "Oh, right, Nicole, the lawyers are waiting for you in your office."
        jn "I'd be glad if you'd solve things with them as soon as possible."
        scene 10office08 with dissolve
        n "Um... yeah, sure. I'll get to work right away."
        jn "Good."
        mc "{i}Looks like Nicole's gonna be busy and unlikely to join us.{/i}"
    else:
        play music "music/12 - The Moose.ogg"
        scene black with fade
        "Soon you came to Julia's office."
        "Then you handed the documents to her secretary and went looking for Jane."
        scene 10office02 with dissolve
        "After walking a few more meters through the office, you ran into her."
        mc "{i}I think she's on lunch break.{/i}"
        scene 10office03 with dissolve
        "You noticed that Jane is singing some kind of tune."
        jn "La-la-la-la..."
        mc "{i}Wait... That's our tune from that YouTube video!{/i}"
        mc "{i}That's the surprise.{/i}"
        mc "That's a great tune."
        scene 10office05 with dissolve
        "When Jane heard your voice, she turned around."
        jn "[mc]? What a meeting."
        mc "It's nice to see you, Jane."
        jn "Yeah, nice to see you, too."
        scene 10office06 with dissolve
        mc "I see you're drinking coffee... Do you mind if I join you?"
        jn "I don't know what you're doing here, but I don't see why not."
        mc "Okay, great."

    scene black with fade
    "A few minutes later."
    scene 10office09 with dissolve
    jn "So, why don't you tell me why you came here?"
    mc "Does it have to be a reason to see a girl you like?"
    jn "Hmm. That's funny."
    jn "Now tell me, why did you really come here?"
    scene 10office11 with dissolve
    mc "Hey, that's actually the truth!"
    jn "Oh, really?"
    mc "I swear."
    jn "Okay, I'll believe you this time."
    mc "Thanks, I guess."
    "..."
    mc "By the way, while I'm here, can you share what you've prepared for this Friday?"
    scene 10office10 with dissolve
    jn "Ha! Can't you just be patient?"
    mc "Come on, give me a little hint! It'll be enough."
    jn "And ruin your whole surprise?"
    mc "Hey, but I know you want to talk about it yourself."
    scene 10office12 with dissolve
    jn "Okay, let's just say that we'll be alone in that place."
    jn "And there will also be a very relaxing atmosphere."
    mc "{i}The two of us and a relaxing atmosphere? I'm in!{/i}"
    mc "Well, now you've intrigued me even more."
    jn "Patience is a virtue."
    mc "Yeah, I know."
    scene 10office10 with dissolve
    jn "Now, if you'll excuse me, I have to get back to work."
    mc "Already?"
    jn "Yeah. We got a lot to do here, you know."
    mc "I see."
    scene 10office13 with dissolve
    mc "Well, it was damn good talking to you."
    jn "Yes, it was mutual."
    scene 10office14 with dissolve
    mc "See you Friday, pretty girl."
    jn "I look forward to it."
    stop music fadeout 3.0
    scene black with fade
    "After saying goodbye to Jane, you left her office."
    if lisa_path == True:
        jump day10_lisa_start
    elif lisa_path == False and selina_path == True or rosa_path == True:
        jump day10_home_phone
    else:
        jump day10_rehearsal


label day10_lisa_start:
    scene black with fade
    if day09_lisa_jade_lewd == True:
        mc "{i}After everything that happened last night, I just had to go to Lisa's and check on her.{/i}"

    else:
        mc "{i}After such a busy morning, I just wanted to go to Lisa's and see her face.{/i}"
    play sound "music/knock.mp3"
    "Knock-knock!"
    scene 10lisa01 with dissolve
    stop sound fadeout 3.0
    play music "music/6 - Positive Mood.ogg"
    p "Oh, [mc]... I didn't expect to see you."
    p "You must be looking for Lisa."
    if day09_lisa_jade_lewd == True:
        mc "Yeah. I tried calling her, but she's not answering the phone..."
        mc "I'd like to talk to her."
    else:
        mc "Yeah. I hope she's here."
    p "Mm-hmm."
    if day09_lisa_jade_lewd == True:
        scene 10lisa02 with dissolve
        p "I don't know what happened between you two yesterday, but she's not herself this morning."
        p "And the worst part is, she tells me nothing. That's not like her at all."
        mc "{i}Uh, I guess that's all because of what happened between us and Jade last night.{/i}"
        mc "{i}When you do something stupid like that when you're drunk and then you get sober... Yes... Things get more complicated.{/i}"
        mc "I have some thoughts about that."
    mc "Mind if I talk to her?"
    scene 10lisa03 with dissolve
    p "Yes, of course. Wait here, I'll call her."
    mc "Okay."
    scene 10lisa03a with dissolve
    "Penny went after Lisa."
    scene 10lisa04 with dissolve
    if day09_lisa_jade_lewd == True:
        mc "{i}I have no idea how Lisa feels right now, but I hope I can convince her that nothing terrible happened yesterday.{/i}"
        mc "{i}As for me, it was just amazing.{/i}"
        mc "{i}Except for a slight hangover and that call from Julia.{/i}"
        mc "{i}Although, I've already sent Lisa a message that my father is fine.{/i}"
        scene 10lisa05 with dissolve
        "You noticed how the door to ger room open, and Lisa's disturbed face looked out."
        mc "{i}She looks like she's either feeling guilty right now or she just doesn't know how to act with me.{/i}"
        scene 10lisa06 with dissolve
        ls "[mc]..."
        mc "Lisa."
        scene 10lisa07a with dissolve
        ls "Em... I'am... About yesterday..."
        ls "I was totally inappropriate and-"
        mc "{i}Yeah, she's definitely feeling a little out of place right now.{/i}"
        mc "{i}I need to help her.{/i}"
        mc "Wait... Let me tell you first."
        scene 10lisa07 with dissolve
        ls "Um... Yeah... Sure... If that's what you want."
        mc "Thank you."
        mc "First of all, I want to say that neither you nor I should regret what happened yesterday."
        mc "We both wanted it, and it was... It was a really nice experience."
        scene 10lisa07a with dissolve
        ls "Yeah, but-"
        mc "Don't... You'd better come here."
        scene 10lisa08 with dissolve
        "You pulled out your hand, gesturing an invitation."
        ls "Um... Okay."
        scene 10lisa09 with dissolve
        "Like she was afraid you'd pull your hand back, Lisa touched you gently."
        mc "Yeah, that's it."
        scene 10lisa10 with dissolve
        ls "Ha-ha-ha! You're really strong!"
        mc "Oh, yes, I am."
        mc "But the truth is, you're the one who's like feather."
        scene 10lisa11 with dissolve
        ls "So you're not mad about the way I acted?"
        mc "Not at all."
        ls "Phew... You have no idea how happy I am to hear you say that. It's a relief to get that off my shoulders."
        scene 10lisa12 with dissolve
        "You went up to Lisa and gave her a firm hug."
        mc "You can always rely on me."
        mc "Besides, in our last night... um... incident, it's not your fault alone."
        ls "Huh. Yeah, that's right."

    else:
        mc "{i}If you think about it, last night went very well.{/i}"
        mc "{i}Except for a slight hangover and that call from Julia.{/i}"
        mc "{i}Although, I've already sent Lisa a message that my father is fine.{/i}"
        scene 10lisa05a with dissolve
        "You noticed the side door to the room opened and Lisa's smiling face looked out of there."
        mc "{i}She looks like she's in a very cheerful mood right now.{/i}"
        scene 10lisa06a with dissolve
        ls "[mc]! I'm so glad you came!"
        mc "You won't believe it, but I've already missed you."
        scene 10lisa09 with dissolve
        "You stretched out your hand in a gesture of invitation and Lisa immediately touched it."
        mc "Now come here!"
        scene 10lisa10 with dissolve
        ls "Ha-ha-ha! You're really strong!"
        mc "Oh, yes, I am."
        mc "But the truth is, you're the one who's like feather."
        scene 10lisa11 with dissolve
        ls "I'm glad you came here. And I'm glad your dad's okay."
        mc "Yeah, thank you."
        scene 10lisa12 with dissolve
        "You went up to Lisa and gave her a firm hug."
        mc "{i}It's so nice just to be around her.{/i}"

    scene 10lisa13 with dissolve
    ls "So, since you're here, what would you like to do?"
    mc "Hmm... Let me think about it..."
    scene 10lisa14 with dissolve
    p "Ahem!"
    scene 10lisa15 with dissolve
    if day09_lisa_jade_lewd == True:
        p "Looks like you've solved all your problems, and now you're having a good time."
    else:
        p "You seem to be having a good time."
    mc "{i}Oh... I didn't even notice how Penny got here.{/i}"
    scene 10lisa16 with dissolve
    p "Don't think I'm watching you or anything like that. I just wanted to remind you that you're not the only one here."
    scene 10lisa17 with dissolve
    mc "Is she always so weird?"
    scene 10lisa17a with dissolve
    ls "Usually not, but lately she's had bad luck with boys, so she's always so irritated."
    scene 10lisa16 with dissolve
    p "Hey, I'm not irritated!"
    scene 10lisa18 with dissolve
    ls "If you say so."
    mc "Don't worry, Penny, I'm sure you'll find somebody soon."
    scene 10lisa19 with dissolve
    p "And when did you become such a disgustingly sweet couple? You only met a month ago."
    scene 10lisa18 with dissolve
    mc "Isn't it obvious? We're just good with each other."
    ls "Yeah, no need to be jealous."
    scene 10lisa19 with dissolve
    p "Anyway, I'm glad you're doing okay."
    p "Now, I think I'll just leave you two alone and go get some air."
    scene 10lisa20 with dissolve
    mc "Bye, Penny."
    ls "See you later."
    p "Yeah, well... Just don't do anything stupid here."
    play sound "music/door.wav"
    "..."
    scene 10lisa21 with dissolve
    ls "Looks like we're alone now."
    mc "Mm-hmm."
    ls "Shall we sit down?"
    mc "I'd love to."
    if day09_lisa_jade_lewd == True:
        scene 10lisa22 with dissolve
        mc "Look, I feel like we need to talk to Jade. And we better do it as soon as possible."
        mc "Well, you know, like normal adults usually do."
        mc "Just to avoid any embarrassing situations and other misunderstandings that might happen in the future."
        scene 10lisa23a with dissolve
        ls "Yeah, like adults who've done something dumb."
        scene 10lisa22 with dissolve
        mc "Something like that. Besides, remember how worried you were about it, and imagine how Jade could feel right now."
        scene 10lisa23 with dissolve
        ls "Uh... Damn, you're right. We need to see her as soon as possible."
        mc "Yeah, it's better that way. Let me call her and make an appointment."
        scene 10lisa24 with dissolve
        "You took out your phone and started dialing Jade's number."
        scene 10lisa25 with dissolve
        ls "Um... You're sure you can do this, right?"
        ls "And what happens if she doesn't pick up the phone?"
        scene 10lisa26 with dissolve
        mc "Look, if you want to do it yourself, please. Here's the phone."
        ls "No, no! Thanks, but it better be you."
        mc "Yeah, that's what I thought."
        scene 10lisa27 with dissolve
        mc "Hello. Jade?"
        jd "Yes."
        mc "It's me, [mc]."
        jd "Yeah, I recognized your number."
        scene 10lisa28 with dissolve
        mc "Okay. Do you mind meeting me and Lisa today?"
        jd "Sure, why not. Where and when?"
        mc "{i}I like how easy it is to talk to her.{/i}"
        scene 10lisa27 with dissolve
        mc "In a cafe. I'll text the place to you. And as for time, will you be free in an hour?"
        jd "I will."
        mc "Great! Then we'll meet you at the cafe in an hour."
        jd "Deal."
        scene 10lisa24 with dissolve
        mc "Hmm. That was surprisingly easy."
        scene 10lisa23a with dissolve
        ls "She seems to have reacted a lot better than I thought."
        mc "Well, I guess that's good."
        ls "Yeah, I guess so."
        scene 10lisa23b with dissolve
        ls "Looks like we've sorted out all the important stuff."
        stop music fadeout 3.0
        mc "Actually, we still have one thing left... Come here!"
        jump day10_lisa_sex
    else:
        scene 10lisa22a with dissolve
        "You and Lisa talked about everything for a while, joking and laughing."
        stop music fadeout 3.0
        "Until one moment..."
        jump day10_lisa_sex

label day10_lisa_sex:
    if _in_replay:
        $ setReplay()
    play music "music/2 - Bad.ogg"
    scene 10lisa29 with dissolve
    "With a gentle tug, you pulled Lisa in your direction."
    ls "Hey! What are you doing?!"
    scene 10lisa30 with dissolve
    mc "That's better."
    ls "So why did you do it?"
    mc "Do I need a reason to cuddle up my girlfriend?"
    ls "Um... I guess not."
    scene 10lisa31 with dissolve
    "Lisa gently touched your face."
    ls "I like it when you act so confident."
    mc "Oh, really?"
    ls "Yeah."
    scene 10lisa32 with dissolve
    mc "{i}She's so cute now. I can't believe I got a pretty girl like her.{/i}"
    scene 10lisa33 with dissolve
    ls "Ah... Your hands are so warm."
    mc "{i}It's so hard to resist that look.{/i}"
    scene 10lisa34 with dissolve
    "You put your hand a little lower..."
    ls "Mmm... I see you're still assertive."
    scene 10lisa35 with dissolve
    ls "Aaah.... Um.... Mmmmm...."
    mc "{i}It's so sexy.{/i}"
    stop music fadeout 1.0
    play sound "music/music_stop.wav"
    scene 10lisa36 with vpunch
    "Suddenly, Lisa jumped up."

    if day09_lisa_jade_lewd == True:
        ls "Hey... I see what you're trying to do! But have you forgotten that we have to meet with Jade soon?"
        scene 10lisa37 with dissolve
        mc "Don't worry, we still have plenty of time. We'll get there on time."
    else:
        ls "Hey... I see what you're trying to do. But didn't you forget that Penny could be back any minute?"
        scene 10lisa37 with dissolve
        mc "Don't worry, she left a short while ago. We still have plenty of time."

    mc "Besides, from what I just saw, you want it, too."

    if day09_lisa_jade_lewd == True:
        scene 10lisa38 with dissolve
        "You came closer to her."
        ls "Yeah, but what if Penny comes back?"
        mc "Don't worry, she just left. We'll make it."
    else:
        scene 10lisa38 with dissolve
        "You came closer to her."
        mc "We wanted to do it yesterday, but we didn't. So why not now?"

    play music "music/1 - Atmosphere.ogg"
    scene 10lisa39 with dissolve
    "Without wasting any more time, you started kissing Lisa."
    ls "Mmmm... Yes...."
    scene 10lisa40 with dissolve
    "A second later, you sat a girl down right on the table."
    ls "Ah... We have to be more careful."
    mc "Believe me, I will be very careful with you."
    scene 10lisa41 with dissolve
    "You slowly spread the girl's legs."
    ls "It's... It's so exciting."
    mc "Yeah, it is."
    scene 10lisa42 with dissolve
    mc "{i}Now, let's move this strip of fabric to the side.{/i}"
    scene 10lisa42a with dissolve
    mc "Yeah, like that."
    ls "Oh, God... Stop looking so closely."
    scene 10lisa43 with dissolve
    mc "Huh. Relax, I'll warm you up a little."
    ls "Mm... Okay..."
    scene anim88 with dissolve
    "Your fingers started sliding slowly up and down Lisa's pussy."
    ls "Haahh... Hahhhaa.... Hhahahh..."
    "Her breathing got heavy and her body started wriggling in tune with your movements."
    mc "{i}She's so hot right now...{/i}"
    pause
    scene 10lisa44 with dissolve
    ls "If you want to... I think we can continue."
    mc "{i}She's right, I should remember we don't have much time.{/i}"
    scene 10lisa45 with dissolve
    mc "In that case, we'll take that t-shirt off you. I want to see what's under it."
    ls "But there's nothing underneath it."
    mc "Exactly."
    scene 10lisa46 with dissolve
    ls "Oh..."
    mc "{i}What a gorgeous view.{/i}"
    scene 10lisa47 with dissolve
    "..."
    scene 10lisa48 with dissolve
    "You didn't even notice how your hands ended up on Lisa's breasts."
    ls "Mmm... I see you like my boobs..."
    mc "Yeah, they're perfect."
    scene 10lisa49 with dissolve
    ls "Aahhh!"
    mc "{i}Shit... I think I'm pretty excited already.{/i}"
    scene 10lisa50 with dissolve
    "A second later, your lips closed in a kiss."
    scene 10lisa51 with dissolve
    mc "{i}Oohh... Looks like it's not just me.{/i}"
    scene anim89 with dissolve
    ls "Mmm.... Ahh.. Mmmnnn..."
    mc "{i}God, I can feel her body heat and even her heart beating right from here. It's so arousing.{/i}"
    pause
    scene 10lisa52 with dissolve
    "Lisa pinned you even harder."
    scene anim90 with dissolve
    ls "Mmmnnn.... Aaahh.. Mmm..."
    "..."
    pause
    scene 10lisa53 with dissolve
    mc "It's a good time to-"
    ls "Yeah, I know..."
    scene 10lisa54 with dissolve
    "Lisa's hand slipped down your body and landed right on your crotch."
    ls "Your cock is already so hard."
    mc "Yeah."
    scene 10lisa55 with dissolve
    ls "Oh... I forgot how big it is."
    ls "And so hot..."
    mc "{i}I can't stand it anymore. It's time to finally fuck that cutie!{/i}"
    scene 10lisa56 with dissolve
    "You put your dick in and you started moving."
    scene anim91 with dissolve
    ls "Aaahh.... Yeah.... It's so good..."
    mc "{i}Oh, yeah, I agree with that, that's fucking nice.{/i}"
    ls "Aaahhhh... Aaaahhh..... Aaaahhhh..."
    pause
    scene anim92 with dissolve
    mc "{i}Her pussy is squeezing my dick so hard...{/i}"
    ls "Oohhh... Don't stop! You're amazing!"
    pause
    scene 10lisa57 with dissolve
    mc "{i}Oohh... Probably best to change positions...{/i}"
    scene 10lisa58 with dissolve
    ls "Aah! What are you doing?"
    mc "It's okay... I just want you to lie sideways."
    scene 10lisa59 with dissolve
    "Lisa moved closer to you."
    ls "With pleasure."
    scene 10lisa60 with dissolve
    mc "{i}Oh, yeah! Round two!{/i}"
    scene anim93 with dissolve
    mc "Baby, you're amazing!"
    ls "Aahhhh... Yeah!!! This is so awesome!!!"
    ls "I'm almost... I'm coming!!!"
    pause
    scene 10lisa61 with flash
    ls "AAAAHHH!!! YESSS!!!"
    mc "{i}Oohh... Damn it, I'm already at the limit!{/i}"
    menu:
        "Cum outside":
            scene 10lisa62 with flash
            mc "Yeah... I'm cumming!"
            scene 10lisa62a with flash
            "*Heavy breathing sounds*"
        "Cum inside":
            scene 10lisa63 with flash
            mc "Yeah... I'm cumming!"
            scene 10lisa63a with flash
            "*Heavy breathing sounds*"
    scene 10lisa64 with dissolve
    mc "It was certainly worth it."
    ls "Yeah, and the risk of getting caught made it even more exciting."
    mc "That's true."
    ls "Okay, now we need to clean up."
    $ renpy.end_replay()
    if not persistent.day10lisa:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day10lisa = True    
    stop music fadeout 3.0
    scene black with fade
    "Few minutes later."

    if day09_lisa_jade_lewd == True:
        scene 10lisa65 with dissolve
        play music "music/6 - Positive Mood.ogg"
        mc "Well, now that we've taken care of that, we can go meet Jade."
        ls "I hope we're not too late for that."
        mc "I don't think so."
        scene 10lisa66 with dissolve
        ls "Okay, but if something goes wrong, it's all your fault!"
        mc "Hah! It's a deal."
        mc "Oh, yeah, before we go..."
    else:
        scene 10lisa65 with dissolve
        play music "music/6 - Positive Mood.ogg"
        mc "Well, now that we've taken care of that, we can do anything we want."
        mc "Why don't we go for a walk?"
        ls "Sure, why not."
        mc "Oh, yeah, before we go..."

    scene 10lisa67 with dissolve
    ls "Mmm... Still not enough for you?"
    mc "Just wanted to tell you how much I like you."
    ls "Yeah... I like you, too."
    scene 10lisa68 with dissolve
    "..."
    scene 10lisa66 with dissolve
    ls "Shall we go?"
    mc "Yes, let's go."
    stop music fadeout 3.0
    if day09_lisa_jade_lewd == True:
        jump day10_jade
    elif selina_path == True or rosa_path == True:
        "After walking around town with Lisa for a while, you said goodbye to each other, and you came home."
        jump day10_home_phone
    else:
        jump day10_rehearsal



label day10_jade:
    scene black with fade
    "Some time later."
    scene 10cafe01 with dissolve
    play music "music/3 - Dream With U.ogg"
    ls "She's in no rush at all. We were supposed to meet twenty minutes ago. "
    ls "Maybe she won't come."
    mc "I don't know. She said she'd be here. You have to be patient."
    ls "Arrr... I'm patient!"
    mc "{i}Yeah, I can see that.{/i}"
    scene 10cafe02 with dissolve
    mc "You know, I think I know how to brighten up the time."
    ls "Um... How's that?"
    scene 10cafe03 with dissolve
    mc "Come closer."
    ls "Hmm? Are you serious? You didn't have enough of what happened at my place?"
    scene 10cafe04 with dissolve
    "Your hand moved under the table and lay down on the girl's thigh."
    scene 10cafe05 with dissolve
    ls "Jeez, why do you have so much lust in you?"
    mc "Hey, it's not my fault you have this effect on me!"
    ls "So it's all my fault, huh?"
    mc "Mm-hmm."
    ls "Of course it is."
    scene 10cafe06 with dissolve
    ls "Oh, look! It's Jade!"
    mc "What?"
    scene 10cafe07 with dissolve
    "You turned your head and saw Jade coming in to the cafe."
    mc "{i}Indeed, Jade.{/i}"
    scene 10cafe08 with dissolve
    ls "Hey! Hey!"
    mc "Hi, Jade. We were starting to worry you weren't coming."
    mc "Take a seat."
    scene 10cafe09 with dissolve
    jd "Yes... Sorry for being late. I was picking up my bike from repairs."
    mc "Oh, so that stupid inscription was painted over?"
    scene 10cafe09a with dissolve
    jd "Yeah, he's great again. Almost as good as new."
    mc "{i}She's clearly happy with it.{/i}"
    mc "Well, that's good to hear."
    scene 10cafe10 with dissolve
    "Jade sat opposite you."
    jd "So... There was something you wanted to talk to me about?"
    ls "Yes... To tell you the truth, we wanted to talk to you about last night."
    scene 10cafe11 with dissolve
    mc "We just wanted to make sure that what happened did not affect our future relationship in any way."
    mc "Don't get us wrong, it was cool... It was really cool..."
    scene 10cafe14 with dissolve
    ls "AHEM! Yes... But the thing is, we don't want it to hurt our band."
    ls "Well... You know."
    scene 10cafe12 with dissolve
    jd "I think I understand."
    ls "You do?"
    jd "Yes, and I totally agree with you."
    mc "{i}Hmm. She was a lot easier than Lisa.{/i}"
    scene 10cafe14 with dissolve
    ls "So we're good, then?"
    scene 10cafe13 with dissolve
    jd "Absolutely. You don't have to worry about it."
    scene 10cafe12a with dissolve
    jd "It's not going to be easy to forget some stuff, though."
    scene 10cafe12 with dissolve
    jd "But I'll try."
    mc "Great!"
    scene 10cafe15 with dissolve
    jd "You know... When I came to audition for your band, I didn't know I'd meet such cool guys like you."
    jd "I'm glad it worked out that way. And I'm glad we're together."
    mc "{i}Hmm? That sounded a bit ambiguous, but still very optimistic and even pleasant.{/i}"
    scene black with fade
    "You were drinking coffee for a while and talking about your next show until Jade started packing."
    scene 10cafe16 with dissolve
    jd "It was great to see you again, but I gotta go."
    jd "See you tomorrow at rehearsal."
    mc "See you, Jade."
    ls "Yeah, bye!"
    scene 10cafe17 with dissolve
    mc "Well, it looks like it turned out really well."
    ls "Yeah, that's for sure."
    ls "Looks like I was the one who worried about it the most out of the three of us."
    scene 10cafe03 with dissolve
    mc "It's okay, you don't have to worry anymore."
    ls "Yes... You're right."
    stop music fadeout 3.0
    scene black with fade
    "After sitting together for a few more minutes, you said goodbye to each other and went about your business."
    if lisa_path == False and selina_path == True or rosa_path == True:
        jump day10_home_phone
    else:
        jump day10_rehearsal



label day10_home_phone:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "That same night."
    scene 10phone01 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "You spent your free time on the social networks and other joys of the Internet."
    mc "{i}Hmm. Since I've had some free time, maybe I should text somebody?{/i}"
    $day10_selina_text=False
    $day10_rosa_text=False
    menu day10_rosa_selina_text:
        "Text Selina" if (selina_path == True and selina_broke_up == False  and day10_selina_text==False) or _in_replay:
            mc "{i}I saw Selina at the hospital this morning. Maybe I should text her?{/i}"
            mc "{i}Yes, definitely!{/i}"
            mc "\"Hey. What are you doing?\""
            "{cps=15}...{/cps}"
            s "\"Hey. I'm home, watching TV.\""
            s "\"How are you?\""
            mc "\"I think fine. Thanks for asking.\""
            s "\"No problem. :P\""
            "{cps=15}...{/cps}"
            s "\"You're alone?\""
            mc "\"Yeah. Why do you ask?\""
            s "\"I'm thinking about coming to you right now.\""
            mc "\"Really?\""
            s "\"Yeah. You okay with that?\""
            mc "\"Sure, why not. I'll be waiting for you.\""
            s "\"Okay, send me the apartment number, and I'll be with you soon. XOXO\""
            mc "\"Deal.\""
            stop music fadeout 3.0
            scene black with fade
            "Some time later."
            play sound "music/doorbell.wav"
            scene 10selinahome01 with dissolve
            "*Doorbell*"
            mc "{i}It must be Selina.{/i}"
            play sound "music/Door.wav"
            scene 10selinahome02 with dissolve:
                linear 6.0 yalign 1.0
                linear 6.0 yalign 0.0
                repeat 1
            play music "music/9 - You Can Make the Sound.ogg"
            s "I hope it's not too late."
            mc "Um... It's perfect."
            s "Oh, great."
            scene 10selinahome03 with dissolve
            s "So this is where you live. Looks pretty good."
            mc "Yes, thanks. Come on in."
            scene 10selinahome04 with dissolve
            s "Mmm..."
            mc "{i}Her kisses are always so nice.{/i}"
            scene 10selinahome05 with dissolve
            s "I'm so glad we met."
            mc "Yeah, me too."
            scene 10selinahome06 with dissolve
            s "So, do you have any idea what we're gonna do?"
            mc "Hmm... I thought you said you were watching TV at home?"
            s "Yep."
            mc "First I think we could watch a movie, and then... And then, who knows."
            scene 10selinahome07 with dissolve
            mc "Oh... Wait. Let me walk you into the living room first."
            s "Heh. That's where you should have started."
            mc "That's for sure."
            scene 10selinahome08 with dissolve
            mc "To tell you the truth, this is my father's apartment. But he kind of gave it to me for a while."
            mc "So now I'm the host here."
            s "It's interesting."
            scene 10selinahome09 with dissolve
            mc "And this is where I spend most of my time at home."
            s "Wow... Looks awesome."
            mc "Thank you."
            scene 10selinahome10 with dissolve
            s "I've already had so many different ideas about how to relax here..."
            mc "Will you share them with me?"
            s "Not now... But very soon."
            mc "Huh. If you say so."
            scene 10selinahome11 with dissolve
            mc "You can sit on the couch for now, and I'll get us something to drink."
            s "Oh, that's a good idea."
            scene 10selinahome12 with dissolve
            mc "What are you drinking? I have wine, beer and whiskey."
            s "I could use a cold bottle of beer."
            mc "Excellent choice!"
            s "Yes... Thank you."
            scene 10selinahome13 with dissolve
            s "Um... Since we're going to watch a movie, I want to show you one of my favorites."
            mc "Yeah, and what's this movie about?"
            s "Cyberpunk. The grim world of the future. The main character is a very cool specialist, who finds himself among a pile of fateful beauties."
            scene 10selinahome14 with dissolve
            mc "Sounds intriguing. You must have good taste."
            s "I promise you won't regret it when you see this movie."
            mc "Well, then, that's what we'll see."
            scene 10selinahome15 with dissolve
            mc "Here come two bottles of cold beer. Just like you wanted."
            s "Perfect! Now bring it here!"
            mc "One moment, I'll just turn off the lights."
            stop music fadeout 3.0
            scene 10selinahome16 with dissolve
            "{cps=15}*Click*{/cps}"
            scene 10selinahome16a with dissolve
            play music "music/Maxim Nick - Smooth Light.ogg"
            s "Oh, yeah! That's much better."
            scene 10selinahome17 with dissolve
            "You gave Selina a bottle of beer and sat next to her."
            mc "You know, it's so unusual to spend time with you for something so ordinary."
            s "Why?"
            mc "I don't know. Usually when we meet, we're either not alone or we're always in a hurry. And now... It's so calm and relaxing."
            s "I know. I like that, too."
            mc "Well, in that case, I suggest we drink to a good evening!"
            scene 10selinahome18 with dissolve
            "*Ring*"
            s "To a good evening!"
            scene 10selinahome19 with dissolve
            mc "Well now, let's see this movie you like so much."
            s "For sure, it's just awesome. Not to mention an awesome ending!"
            mc "Hey-hey! No spoilers!"
            s "Huh. Okay, no spoilers."
            scene 10selinahome21 with dissolve
            "You got comfortable and started watching the movie."
            scene black with fade
            "A few minutes later."
            scene 10selinahome20 with dissolve
            mc "How interesting, there's musicians in it too. Cool!"
            s "Yeah, that lady's a good one."
            scene black with fade
            "Some more time later."
            scene 10selinahome22 with dissolve
            mc "{i}Whoa, this actress is a real beauty! I'm a little jealous of that main character.{/i}"
            scene 10selinahome23 with dissolve
            s "Mmm... And now my favorite spicy scenes!"
            mc "Is it just me, or does someone like the hottest movies?"
            scene 10selinahome23a with dissolve
            s "Well, I'm not that shy, so... Yeah, I like them."
            s "And what about you?"
            mc "Hmm. I usually like spicy scenes in real life, but they look good on TV too."
            scene 10selinahome24 with dissolve
            s "So you like spicy scenes in real life?"
            mc "Very much."
            s "You probably mean something like that."
            stop music fadeout 3.0
            scene 10selinahome25 with dissolve
            "The next moment, Selina was right above you."
            s "Mmm..."
            mc "Yes... These scenes are the best."
            scene 10selinahome26 with dissolve
            play music "music/15 - Deep Mood.ogg"
            "Your hands slipped smoothly down the girl's hips and stopped right on her butt."
            mc "{i}I love her firm ass.{/i}"
            scene 10selinahome27 with dissolve
            mc "I guess we'll see the movie next time?"
            s "It's like you're reading my mind right now."
            mc "Heh. Who knows, maybe I do."
            s "Then why don't you guess what I want you to do now?"
            scene 10selinahome28 with dissolve
            "..."
            scene 10selinahome28a with dissolve
            "..."
            scene 10selinahome29 with dissolve
            mc "Did I guess?"
            s "Mmm... No, but it was a very nice try."
            s "I wanted to do this."
            scene 10selinahome30 with dissolve
            "Selina had fun putting you on your back."
            mc "Oh, I see you have a lot of energy."
            scene 10selinahome31 with dissolve
            s "You have no idea how much."
            mc "I guess I don't have to imagine, I'll see it soon enough."
            s "Hee-hee. You're right."
            scene 10selinahome32 with dissolve
            s "Now let's get these shorts off you."
            scene 10selinahome32a with dissolve
            "{cps=15}...{/cps}"
            scene 10selinahome33 with dissolve
            s "Wow! Are you that horny already?"
            mc "I guess so."
            scene 10selinahome34 with dissolve
            mc "When I have such great boobs hanging right in front of my eyes, there's no other option."
            s "Flatterer!"
            scene 10selinahome35 with dissolve
            "The girl leaned back and started taking off the rest of her clothes."
            mc "Oh, I see you decided not to waste time."
            s "I just want to get to the point as soon as possible."
            scene 10selinahome36 with dissolve
            "Before you knew it, your dick was in Selina's soft hands."
            scene anim94 with dissolve
            s "Oh, yes... Your dick is so hard and hot..."
            mc "{i}Oohh... Damn, she jerks me off so skillfully.{/i}"
            mc "{i}It's just fucking great.{/i}"
            s "Yeah, I see you like it..."
            pause
            scene 10selinahome37 with dissolve
            "The girl came closer to you, and your dick was right next to her pussy."
            scene anim96 with dissolve
            s "Now let's try to make this."
            s "How's that? Do you like it?"
            mc "Ah... Oh, yeah... It's really good..."
            pause
            scene anim95 with dissolve
            s "Mmm... I knew you'd like this..."
            mc "{i}Hey, she's already moaning with pleasure.{/i}"
            pause
            scene 10selinahome38 with dissolve
            "Suddenly Selina stopped."
            mc "Hey... Why did you stop-"
            scene 10selinahome39 with dissolve
            s "That's why."
            mc "{i}Oh, um... This is just awesome.{/i}"
            scene 10selinahome40 with dissolve
            s "Okay, time to start."
            "You felt Selina's fingers touch your dick and then point it right at her pussy."
            scene 10selinahome41 with dissolve
            s "Ohh... Oh, yeah... It feels so good to have your big cock inside!"
            mc "Believe me, baby, it's mutual."
            scene 10selinahome42 with dissolve
            s "Mmm... I hope you're ready to show me all you're capable of?"
            mc "{i}Absolutely!{/i}"
            scene 10selinahome43 with dissolve
            "You wrapped both hands around the girl and started to fuck her hard."
            scene anim97 with dissolve
            s "Aaaahhh... Aaaahhh... Aaaahhh..."
            mc "{i}Ohh... Her moaning turns me on so much.{/i}"
            s "Aahhhh... Yeah... Yeah... Fuck me!!! Just don't stop!!!"
            pause
            scene 10selinahome44 with dissolve:
                linear 6.0 yalign 1.0
                linear 6.0 yalign 0.0
                repeat 1
            s "Yeah!!! Yeah!!!!"
            scene 10selinahome45 with dissolve
            "A few seconds later, Selina was already jumping on your dick."
            scene anim98 with dissolve
            s "Yes... Like this... Very good!"
            s "Do you like it?"
            mc "Baby, you're amazing..."
            pause
            scene 10selinahome46 with dissolve
            s "Aahh... Aaaahhh.... Aaaahhhh...."
            scene anim100 with dissolve
            mc "{i}Her boobs just keep bouncing in front of my eyes.{/i}"
            mc "{i}Fuck, I'm barely holding back.{/i}"
            pause
            scene 10selinahome47 with dissolve
            s "YEEESSS!!!!"
            "Selina's body went weak and her movements slowed down."
            mc "{i}Oh, no, I'm not done yet.{/i}"
            scene 10selinahome48 with dissolve
            "With one quick move you picked up the girl and started fucking her as hard as you could."
            scene anim99 with dissolve
            mc "Haahh.. Haahh... Haaahh!!!"
            mc "{i}I... already... almost...{/i}"
            pause
            scene 10selinahome49 with dissolve
            "..."
            scene 10selinahome49a with flash
            mc "Yeeess!!!"
            scene 10selinahome49a with flash
            mc "CUMMING!!!!"
            scene 10selinahome50 with dissolve
            "*Heavy breathing sounds*"
            s "I need... I need to visit you more often to watch TV."
            mc "Definitely."
            stop music fadeout 3.0
            scene black with fade
            "Some time later."
            play music "music/8 - Intro Music.ogg"
            "You cleaned yourself up, and Selina started going home."
            scene 10selinahome51 with dissolve
            s "Well, that's it."
            mc "Yeah."
            mc "You sure you don't want to stay with me tonight?"
            mc "We could have a little more fun in the morning."
            s "I'd love to, but I really have to go."
            scene 10selinahome52 with dissolve
            s "It was nice to see you, [mc]."
            mc "Yeah, nice to see you, too."
            mc "See you around."
            s "Bye."
            $ renpy.end_replay()
            if not persistent.day10selina:
                $ renpy.notify(['SAHNE KILIDI ACILDI'])
                $ persistent.day10selina = True
            scene black with fade
            "Soon after saying goodbye to Selina, you went to bed very happy."
            stop music fadeout 3.0
            "There was a new day ahead of you."
            $day10_selina_text=True
            jump day10_rosa_selina_text
            jump day10_rehearsal

        "Text Rosa" if (rosa_path == True and day10_rosa_text == False) or _in_replay:
            mc "{i}It's been a while since we last met with Rosa. Maybe I should text her?{/i}"
            mc "{i}Yes, definitely.{/i}"
            mc "{i}But how should I start this dialogue?{/i}"
            mc "\"Hello, beauty. How are you spending your evening?\""
            "{cps=15}...{/cps}"
            r "\"Hello, [mc].\""
            r "\"Alas, I'm busy with routine. Picking up things from the wardrobe I brought back from my ex-husband.\""
            mc "\"Oh... It's a big deal.\""
            r "\"Not really. I'd rather spend the evening in more pleasant company.\""
            mc "\"So why not?\""
            mc "\"I'm alone right now.\""
            r "\":)\""
            r "\"Tempting offer, but not today.\""
            mc "\":(\""
            r "\"Don't be upset.\""
            r "\"I know what might cheer you up a little.\""
            mc "\"And what is that?\""
            "{cps=15}...{/cps}"
            "{cps=15}...{/cps}"
            scene 10phone03 with dissolve
            mc "{i}Wow...{/i}"
            menu:
                "Approach the image":
                    scene 10phone02 with dissolve:
                        linear 6.0 yalign 1.0
                        linear 6.0 yalign 0.0
                        repeat 1
                    mc "{i}Yeah, that MILF is a real bomb.{/i}"
                "Leave it as it is":
                    "..."
            scene 10phone01 with dissolve
            r "\"So, what do you think?\""
            mc "\"I can tell you that this photo not only lifted my spirits, but also something else.\""
            r "\"Well, I can't give you more than that right now.\""
            mc "\"You're breaking my heart.\""
            "{cps=15}...{/cps}"
            r "\"Okay, okay... Anyway, I wanted to suggest that we meet up sometime next week.\""
            mc "\"I like that! :D\""
            r "\"Yes.\""
            r "\"Now, if you'll excuse me, I have some work to do.\""
            mc "\"Okay. Have a good night.\""
            r "\"You, too. ;)\""
            mc "{i}Hmm. I think it worked out pretty well.{/i}"
            mc "{i}And it looks like I'm going to see her next week!{/i}"
            mc "{i}It's definitely good.{/i}"
            $ renpy.end_replay()
            stop music fadeout 3.0
            scene black with fade
            "After spending some more time on the Internet, you went to bed."
            "There was a new day ahead of you."
            $day10_rosa_text=True
            jump day10_rosa_selina_text
            jump day10_rehearsal


label day10_rehearsal:
    scene 10rehearsal01 with dissolve
    play music "music/16 - Bright Colors.ogg"
    "All the next day, your band spent rehearsing."
    "To be ready to perform by the weekend, you did your best."
    scene black with fade
    "Some time later."
    "End of rehearsal."
    scene 10rehearsal02 with dissolve
    mc "Nice rehearsal, man!"
    j "Yeah, right!"
    j "I was rehearsing this weekend, by the way."
    scene 10music01 with dissolve
    mc "{i}Yeah, I can imagine that.{/i}"
    mc "{i}Despite his carelessness, this guy takes everything about music very seriously.{/i}"
    scene 10rehearsal02 with dissolve
    mc "Awesome, I didn't miss a chance to rehearse at home either."
    j "Sweet!"
    scene 10rehearsal03a with dissolve
    jd "Don't think you guys are the only ones. I've been playing guitar at home a few hours every day for years."
    jd "It's become a good habit."
    scene 10music03 with dissolve
    mc "{i}I knew Jade was serious about this stuff, but I didn't know how much.{/i}"
    mc "{i}Well, that's impressive.{/i}"
    scene 10rehearsal03 with dissolve
    ls "Hey, hey, I was actually rehearsing, too."
    mc "Oh, really?"
    ls "Absolutely!"
    scene 10music02 with dissolve
    mc "{i}Knowing her habit of singing in the shower, I can imagine how those rehearsals went.{/i}"
    mc "{i}Although, we have to understand that this girl has a natural talent and a terrific voice.{/i}"
    mc "{i}She is the star of our band.{/i}"
    scene 10rehearsal04 with dissolve
    j "Heh. It doesn't look like they're joking."
    mc "Yeah, we all did our best."
    mc "And to be honest, I like the results we've had."
    mc "I think we should do another rehearsal this week and we'll be ready for the next gig."
    j "Yeah, that's right."
    scene black with fade
    "A few minutes later."
    scene 10rehearsal05 with dissolve
    j "Oh, I forgot to tell you guys, but I have to leave early today."
    j "I have a date."
    mc "You have a date?"
    mc "Would it happen to be the blue-haired beauty we met at the party?"
    scene 10rehearsal06a with dissolve
    j "Yeah, that's the one! And I want to tell you that she's just adorable."
    j "I can't remember the last time I felt so strongly about a girl."
    scene 10rehearsal08 with dissolve
    ls "So that's who you left us for."
    scene 10rehearsal06 with dissolve
    j "Hey, you gotta understand, this girl could easily be the one and only for me."
    scene 10rehearsal08 with dissolve
    ls "Okay, okay, whatever you say."
    if lisa_path == False:
        ls "And if you're leaving, Jade and I will go, too."
        scene 10rehearsal09 with dissolve
        "You noticed when she said those words, the girls held hands."
        mc "{i}Hmm. What does that mean? Have they really started dating?{/i}"
        scene 10rehearsal06b with dissolve
        mc "{i}This little gesture doesn't seem to have escaped Jacob's attention.{/i}"
        scene 10rehearsal07 with dissolve
        j "Hey, why are you two holding hands so nicely? Are you two dating or something?"
        scene 10rehearsal10 with dissolve
        jd "Sooner or later, we'll have to tell them everything."
        ls "Yes, yes... I know."
        scene 10rehearsal10a with dissolve
        ls "Anyway, you're right, Jacob. Jade and I are dating now."
        mc "{i}Huh. That's how it is.{/i}"
        scene 10rehearsal06c with dissolve
        j "Whoa, whoa, whoa! Are you serious?! You are?! Two girls?!"
        scene 10rehearsal10 with dissolve
        jd "You seem to have surprised him a lot."
        ls "Yes, I did."
        scene 10rehearsal06b with dissolve
        j "Wait... And did you, [mc], know about this?"
        scene 10rehearsal11 with dissolve
        mc "Well, I had my suspicions about it, but this is the first that I've heard it."
        scene 10rehearsal07 with dissolve
        j "Holy shit."
        mc "{i}Yes, in a way, I agree with him.{/i}"
        scene 10rehearsal10a with dissolve
        ls "We really don't know what's gonna come out of this."
        ls "But you can be assured that this will not affect our band in any way."
        scene 10rehearsal09 with dissolve
        mc "{i}I wish I could believe that. But life is a complicated thing, and you can never talk about such things with absolute certainty.{/i}"
        mc "{i}Anyway, Jacob and I have no choice but to accept their decision.{/i}"
        scene 10rehearsal06a with dissolve
        j "Okay, this is all really interesting, but like I said, I have a date to go on."
        scene 10rehearsal08 with dissolve
        ls "Yeah, we're gonna go too."
        ls "What about you [mc]?"
        mc "I think I'll stay here a little longer."
        ls "Okay, as you wish."
        scene 10rehearsal14 with dissolve
        "Soon the guys said goodbye to you and went on their own business."
        scene 10rehearsal13 with dissolve
        mc "{i}Well... I'm alone now.{/i}"
        mc "{i}And since I have more free time, I'd rather rehearse a little more.{/i}"
        scene 10rehearsal13a with dissolve
        "..."
        scene 10rehearsal13b with dissolve
        "*Music Sounds*"
        stop music fadeout 3.0
        scene black with fade
        "After rehearsing for a while, you went home."
        if anna_sex == True and anna_colleague == False:
            "There was a new day ahead of you."
            jump day10_anna_start
        elif anna_sex == False and jane_date_offer == True:
            jump day10_jane_date
        elif anna_colleague == True and jane_date_offer == True:
            jump day10_jane_date            
        else:
            "You had a weekend ahead of you."
            jump day11_start

    elif day09_lisa_jade_lewd == True:
        ls "Have a good date."
        scene 10rehearsal11 with dissolve
        mc "Yeah, man, good luck with that hottie."
        scene 10rehearsal06a with dissolve
        j "Thanks. Hehe."
        j "I think, after what you said, I have to make it perfect."
        j "Well, I'm off."
        stop music fadeout 3.0
        scene 10rehearsal14a with dissolve
        "Soon you said goodbye to Jacob, and he went to meet his new dream."
        stop music fadeout 3.0
        jump day10_threesome

    else:
        ls "And if you're leaving, I'm going, too. I have some things left to do."
        scene 10rehearsal11 with dissolve
        mc "Okay, so I guess we'll just finish this rehearsal right now."
        "There was no objection."
        stop music fadeout 3.0
        scene black with fade
        "Soon you all said goodbye to each other and went home."
        if anna_sex == True and anna_colleague == False:
            "There was a new day ahead of you."
            jump day10_anna_start
        elif anna_sex == False and jane_date_offer == True:
            jump day10_jane_date
        elif anna_colleague == True and jane_date_offer == True:
            jump day10_jane_date
        else:
            "You had a weekend ahead of you."
            jump day11_start


label day10_threesome:
    if _in_replay:
        $ setReplay()
    scene 10threesome01 with dissolve
    play music "music/8 - Intro Music.ogg"
    mc "Looks like it's just the three of us left."
    ls "Mm-hmm."
    jd "..."
    scene 10threesome02 with dissolve
    "Suddenly you felt Lisa fall on you."
    mc "Hey, what are you doing?"
    ls "Me? Nothing."
    ls "We rehearsed so long, I just want to get some rest..."
    "..."
    scene 10threesome03 with dissolve
    ls "You know... I feel like we've known each other for a hundred years."
    ls "I mean, we only became friends a month ago, and I can't imagine what it's like to live without you."
    ls "I guess you might think I'm saying something stupid right now, huh?"
    scene 10threesome04 with dissolve
    jd "I wouldn't say so."
    jd "When a small group works closely on something very important for all its members, it usually brings them closer together."
    scene 10threesome05 with dissolve
    mc "Maybe so, but I think there's some deeper connection between us."
    scene 10threesome06 with dissolve
    ls "Yeah, well, when we were drunk a few days ago, we felt that connection fully... It was... Yeah, it was..."
    "You thought you could see Lisa's cheeks turn pink."
    mc "{i}I can guess what she's thinking right now.{/i}"
    mc "{i}And I can't get that picture out of my head either.{/i}"
    scene 10threesome07 with dissolve
    "Following some primitive instinct, your hands discreetly started massaging the girl's breast."
    ls "Mmm..."
    mc "{i}It feels so good...{/i}"
    "..."
    mc "{i}Wait, what the fuck am I doing?! We're not the only ones here.{/i}"
    scene 10threesome08 with dissolve
    "You turned your head towards Jade and you froze."
    mc "{i}Huh?{/i}"
    scene 10threesome08a with dissolve
    mc "{i}It seems this lustful mood isn't just in me.{/i}"
    "And then..."
    stop music fadeout 1.0
    scene 10threesome09 with vpunch
    ls "Whoa, whoa! What's going on?!"
    ls "Don't you think we've been through this before?"
    scene 10threesome10 with dissolve
    play music "music/8 - Intro Music.ogg"
    ls "You don't want this to happen again, do you?"
    "{cps=15}...{/cps}"
    "You and Jade didn't say anything."
    scene 10threesome11 with dissolve
    "Lisa got up abruptly."
    ls "You guys serious?"
    scene 10threesome12 with dissolve
    "You felt the looks of both girls on you."
    mc "{i}I know they both want it as much as I do. They're just afraid to say it out loud.{/i}"
    scene 10threesome11 with dissolve
    mc "{i}Now it's up to me.{/i}"
    scene 10threesome13 with dissolve
    "Without saying a word, you got up and headed for Lisa."
    ls "Hey... What are you up to?"
    scene 10threesome14 with dissolve
    "And then you kissed her."
    ls "Ah.... Mmmmm...."
    scene 10threesome15 with dissolve
    ls "Do you really want to do this?"
    mc "I do."
    ls "Okay... I hear you."
    mc "What about you?"
    ls "Yes... I think I want that, too."
    scene 10threesome16 with dissolve
    mc "Jade?"
    scene 10threesome17 with dissolve
    jd "Yes?"
    mc "{i}She knows what's gonna happen next, but she still hasn't committed to it.{/i}"
    mc "{i}I need to give her a little push.{/i}"
    scene 10threesome18 with dissolve
    mc "There's no need to be shy anymore."
    "..."
    jd "You're right."
    scene 10threesome19 with dissolve
    "Jade took your hand gently."
    mc "{i}It's hard to imagine that this is really happening.{/i}"
    mc "{i}Let's hope none of us will regret it in the future.{/i}"
    scene 10threesome20 with dissolve
    jd "When we're all sober, it's different..."
    mc "But you want to, right?"
    jd "Yes, I do."
    scene 10threesome21 with dissolve
    mc "Then come here."
    stop music fadeout 3.0
    jd "..."
    scene 10threesome23 with dissolve
    play music "music/1 - Atmosphere.ogg"
    "The next second, your lips met in a kiss."
    mc "{i}Oh... I can't believe I'm doing this right in front of Lisa.{/i}"
    scene 10threesome22 with dissolve
    jd "Mmmm...."
    mc "{i}Damn, it's so hot in here.{/i}"
    scene 10threesome24 with dissolve
    ls "Hey, hey, lovebirds! Aren't you forgetting someone?"
    "You and Jade stopped kissing and turned to Lisa."
    scene 10threesome25 with dissolve
    mc "{i}Yeah, she definitely knows how to get attention alright.{/i}"
    mc "And you're very determined."
    ls "Absolutely!"
    scene 10threesome26 with dissolve
    mc "{i}Man, she looks really tempting right now.{/i}"
    scene 10threesome27 with dissolve
    ls "And since we're talking about determination..."
    ls "Jade, is it just me, or are you wearing too many clothes right now?"
    scene 10threesome28 with dissolve
    ls "Let's get this off of you."
    jd "Hey... I could have done it myself."
    scene 10threesome28a with dissolve
    ls "Relax, I'm just helping."
    scene 10threesome28b with dissolve
    ls "Mmm... That's perfect."
    scene 10threesome29 with dissolve
    ls "Well, what do you think? How do we look?"
    mc "You're both delicious."
    ls "Hehe. Okay, great."
    jd "..."
    scene 10threesome30 with dissolve
    "Lisa and Jade hugged each other and lured you in with their hands."
    ls "So, what are you waiting for?"
    jd "Come to us, [mc]."
    mc "As you wish."
    scene 10threesome31 with dissolve
    "As soon as you walked up to the girls, you noticed them reaching for their brassieres."
    "*Click*"
    scene 10threesome31a with dissolve
    "The next thing you know, they're naked from the waist up."
    mc "{i}Oh, yeah... This is awesome.{/i}"
    scene 10threesome32 with dissolve
    ls "Is there anything you want to tell us? Hmm?"
    mc "Yeah..."
    mc "You are the most dazzling beauties I have ever seen."
    jd "Thank you."
    ls "Yeah, thanks, [mc]."
    scene 10threesome33 with dissolve
    "Lisa and Jade's palms began to gently stroke your whole body."
    jd "Oh... I think he's pretty excited already."
    ls "That fast?"
    ls "Well, that's to be expected, though."
    jd "[mc]... Can you kiss me again?"
    mc "{i}I'd love to.{/i}"
    scene 10threesome34 with dissolve
    "You kissed Jade and you felt Lisa's soft breasts clinging to your back."
    jd "Mmmm...."
    mc "{i}Oh, God... It's all so unreal, I can hardly think of anything anymore.{/i}"
    scene 10threesome35 with dissolve
    ls "I suggest we make this moment even more interesting."
    ls "Like..."
    scene 10threesome35a with dissolve
    ls "...this!"
    ls "Heh. That's great."
    scene 10threesome36 with dissolve
    "You stopped kissing Jade and lowered your gaze below."
    mc "{i}Wow... What a great ass Jade has!{/i}"
    scene 10threesome36a with dissolve
    ls "Uh... What a firm butt!"
    ls "I like it."
    scene 10threesome37 with dissolve
    ls "Hey, I think you guys got too attached to each other up there."
    mc "{i}Yeah, she's right. Now would be a good time to continue.{/i}"
    scene 10threesome38 with dissolve
    ls "Jade, come here."
    ls "Let's get this guy's pants down and see what he's hiding there."
    jd "Yes... Let's see..."
    scene 10threesome39 with dissolve
    "Both girls got down on their knees."
    mc "You know, I'd be happy to show you what I'm hiding."
    scene 10threesome40 with dissolve
    ls "Um... It feels hard as a rock."
    ls "Great."
    scene 10threesome41 with dissolve
    "The girls pulled your pants down and stared at your dick with admiration."
    jd "I forgot how huge it was..."
    ls "Yeah... And now imagine how nice it would be to feel it inside you."
    jd "Ohh..."
    scene 10threesome42 with dissolve
    "Jade's fingers reached carefully for your dick."
    jd "Is it okay if I-"
    scene 10threesome43 with dissolve
    ls "Don't worry, you can grab it harder!"
    ls "Believe me, he'll enjoy it."
    mc "{i}It's so weird. Usually so calm, Jade gets so timid when it comes to sex.{/i}"
    scene anim101 with dissolve
    ls "And now we're gonna move our hand like this..."
    mc "Yes... Go on..."
    ls "You see that? He likes it!"
    jd "Yeah."
    pause
    scene anim102 with dissolve
    ls "Now just a little faster."
    mc "{i}Fuck... That feels so good.{/i}"
    mc "{i}I think I could get used to it.{/i}"
    ls "Okay, now let's try something else...."
    pause
    scene 10threesome44 with dissolve
    "The next moment, you felt Lisa's moist tongue start sliding all over your dick."
    scene anim103 with dissolve
    ls "Mmm..."
    mc "Yeah, you guys... You guys are awesome!"
    pause
    scene anim104 with dissolve
    mc "{i}Jade's lips are so soft.{/i}"
    mc "Ah... Guys, I think we should go a little further."
    mc "I want you to take it all in your mouth."
    pause
    scene 10threesome41 with dissolve
    ls "You want us to give you a proper blowjob?"
    mc "Oh, yes, I do!"
    ls "No problem."
    jd "Which one of us should start first?"

    $ day10_lisa_bj = False
    $ day10_jade_bj = False

    menu day10_bj:
        "Lisa" if day10_lisa_bj == False:
            if day10_jade_bj == True:
               mc "Now let Lisa suck it."
            else:
               mc "Let Lisa."
            $ day10_lisa_bj = True
            scene 10threesome48 with dissolve
            "Lisa touched the head of your dick with her tongue."
            jd "Show us the best you can do."
            ls "Mmmnn...."
            scene 10threesome49 with dissolve
            mc "Ohh... Yes, baby, that's it..."
            scene anim106 with dissolve
            "Lisa started sucking your dick."
            ls "Mmmnnnnn.... Mnnh.... Mnnnhh...."
            mc "{i}Jade also started helping her with her tongue.{/i}"
            mc "Ohhh... Just don't stop..."
            mc "{i}It's so hot. I can even feel their breath.{/i}"
            ls "Mmmnnnnn.... Mnnh.... Mmmnh...."
            pause
            jump day10_bj

        "Jade" if day10_jade_bj == False:
            if day10_lisa_bj == True:
               mc "Now let Jade suck it."
            else:
               mc "Let Jade."
            $ day10_jade_bj = True
            scene 10threesome45 with dissolve
            "Without saying a word, Jade touched the head of my cock with her tongue."
            ls "Mmm... this is so hot."
            mc "Now take it in your mouth."
            scene 10threesome46 with dissolve
            mc "Ohh.... Yeah... Like this..."
            jd "Mmmnn...."
            mc "Now, deeper."
            scene 10threesome47 with dissolve
            jd "Mmmnnnnn.... Mnnh.... Mmmnh...."
            scene anim105 with dissolve
            mc "{i}Despite all her shyness, she sucks amazingly.{/i}"
            mc "Yeah, baby... Don't stop!"
            jd "Mmmnnnnn.... Mnnh.... Mmmnh...."
            pause
            jump day10_bj

    scene 10threesome50 with dissolve
    mc "{i}If they continue to suck so hard, I'm gonna come soon.{/i}"
    jd "Mmnnn...."
    ls "Come on, Jade... Suck on him harder! He's almost at the edge!"
    scene 10threesome51 with dissolve
    jd "Ah... It's your turn..."
    ls "Yes... Give it here."
    ls "Mmmnnnnn.... Mnnh.... Mmmnh...."
    mc "Girls, I'm coming..."
    scene 10threesome52 with dissolve
    "Feeling you can't hold back anymore, you pulled out your dick and started jerking off."
    scene anim107 with dissolve
    ls "Come on... Are you coming?"
    jd "Ah... Come on, [mc]... We're ready."
    mc "Ohhh... I'm almost-!"
    pause
    scene 10threesome53 with flash
    mc "Yeeeessss!!!"
    scene 10threesome53 with flash
    "..."
    scene 10threesome53a with dissolve
    "You came so hard, you sprayed sperm all over their faces."
    jd "Wow..."
    ls "Yeah, wow..."
    scene 10threesome54 with dissolve
    ls "Looks like we did a good job."
    jd "Definitely."
    ls "Which one of us was better?"
    mc "You both were great."
    scene 10threesome54a with dissolve
    ls "Hmm?"
    jd "On your face... I'll help."
    scene 10threesome55 with dissolve
    ls "Ha-ha! What are you doing?"
    jd "Um... Relax... I'll clean it up."
    scene 10threesome55a with dissolve
    ls "Ah! Then I'll help you, too!"
    ls "Don't move..."
    jd "Um.... Yes... Here."
    scene 10threesome56 with dissolve
    "Licking each others faces off turned into a very hot lesbian kiss."
    mc "{i}This spectacle makes my dick stand up again.{/i}"
    scene 10threesome57 with dissolve
    "Meanwhile, the kiss was getting even hotter."
    scene anim108 with dissolve
    mc "{i}They seem to have gotten really into each other.{/i}"
    pause
    scene 10threesome58 with dissolve
    mc "Ladies, what you're doing right now is very sexy, but can we continue?"
    mc "Jade, can you take the rest of Lisa's clothes off?"
    jd "Oh, sure."
    scene 10threesome59 with dissolve
    "Lisa leaned back on the floor."
    ls "Is that what you're up to, wanting to undress me?"
    mc "Yeah, we want to see you in all your glory."
    scene 10threesome60 with dissolve
    jd "You don't mind?"
    ls "Go ahead."
    scene 10threesome61 with dissolve
    "Jade grabbed Lisa by her shorts..."
    scene 10threesome62 with dissolve
    "...and then pulled them right off along with her panties with one move."
    mc "Mmm... What a stunning view."
    scene 10threesome63 with dissolve
    mc "Don't you think so, Jade?"
    scene 10threesome64 with dissolve
    jd "Yes... it is."
    mc "{i}Judging from the look on her face, she clearly enjoys what's going on here.{/i}"
    scene 10threesome65 with dissolve
    ls "By the way, is it me, or is Jade the only one in clothes now?"
    "You focused your eyes on a girl's ass."
    scene 10threesome65a with dissolve
    mc "That's right!"
    mc "We need to change this right now."
    jd "I get the hint."
    scene 10threesome66 with dissolve
    "Moments later, Jade started pulling off her black panties."
    ls "A little more..."
    scene 10threesome67 with dissolve
    mc "Yes, that's it."
    scene 10threesome68 with dissolve
    mc "{i}She's naked... It's the first time I've seen Jade naked!{/i}"
    mc "{i}Wow... It's just wow.{/i}"
    jd "Would you stop looking at me so closely?"
    "You realized the whole time you were staring at her."
    jd "And isn't it time we started the main part?"
    mc "Right!"
    scene 10threesome69 with dissolve
    "The girls hugged each other and turned to you."
    mc "{i}Damn, I feel like I can look at them forever.{/i}"
    scene 10threesome70 with dissolve
    ls "I hope you're strong enough for both of us?"
    mc "Don't you even doubt it!"
    ls "Fine, then I'll be first!"
    scene black with fade
    "A few seconds later."
    scene 10threesome71 with dissolve
    ls "Aaahhh...."
    jd "Just a little more, Lisa."
    ls "Yes, I know... But his dick is so big..."
    scene 10threesome71a with vpunch
    ls "Ohh... Oh, yeah... Oh, that's good."
    jd "There you go, good girl."
    mc "{i}Looks like Jade's starting to enjoy it.{/i}"
    scene 10threesome72 with dissolve
    "While Lisa started jumping on your dick, Jade started fondling everything else with her tongue."
    scene anim109 with dissolve
    ls "Aaahh.... Aaaaahhhh.... Aaaahhhh..."
    mc "{i}Oohh... What a good start.{/i}"
    pause
    scene anim110 with dissolve
    "Lisa began to move faster."
    ls "Aaahh.... Yeah... Yeah..."
    mc "{i}Fuck, these moans are really turning me on.{/i}"
    pause
    scene 10threesome73 with dissolve
    jd "Mmmmmhh... Nnnghh..."
    scene 10threesome74 with dissolve
    "You felt like Jade stopped."
    jd "You're moaning so loud..."
    ls "Ahh... I'm sorry, but it feels so good! Aaah..."
    scene 10threesome75 with dissolve
    "Jade headed in your direction."
    scene 10threesome76 with dissolve
    jd "Um... Do you mind if I, uh..."
    mc "If you what?"
    "..."
    mc "Come on, ask."
    jd "If I sit on top of you?"
    mc "Huh... Okay, why not."
    jd "Thanks."
    scene 10threesome77 with dissolve
    "Jade stood right in front of your head."
    mc "{i}From here, I can see her wet pussy.{/i}"
    mc "{i}I'll try to show her all I can do.{/i}"
    scene 10threesome79 with dissolve
    "The girl came down and you immediately embraced her juicy ass."
    scene anim112 with dissolve
    jd "Ohh!! Um..."
    mc "{i}She moves in tune with my movements.{/i}"
    jd "Don't stop, [mc]... Keep going again! [mc]"
    pause
    scene 10threesome79 with dissolve
    ls "Haahh... Haaah... Having fun over there?"
    scene 10threesome80 with dissolve
    ls "Hey... Jade, how about we turn around in one direction?"
    jd "Um... Yeah... Let's do this..."
    scene 10threesome82 with dissolve
    ls "I just want to kiss your lips right now."
    jd "Then why are you hesitating?"
    ls "Really, why?"
    scene 10threesome81 with dissolve
    "After a few seconds, each of you became busy with the other."
    scene anim111 with dissolve
    ls "Mmm..."
    jd "*Heavy breathing*"
    mc "{i}I won't last long.{/i}"
    pause
    scene 10threesome83 with dissolve
    mc "Oohhhh... I'm almost..."
    ls "Me too!"
    ls "Let's come together!"
    scene 10threesome83a with vpunch
    mc "Coming!"
    scene 10threesome83b with flash
    mc "Yeeeesss!!!!"
    scene 10threesome84 with flash
    "You felt Lisa's pussy squeeze even harder."
    ls "Aaaahhhhhh!!!"
    scene 10threesome78 with flash
    jd "Aaaahhh!!! Yeeeesss!!!"
    scene 10threesome85 with dissolve
    ls "Haah... Haaah... Haaah..."
    ls "That was awesome."
    jd "Yeah..."
    mc "{i}Is it just me, or did the three of us cum together?{/i}"
    mc "{i}Does that even happen?{/i}"
    scene black with fade
    "A few minutes later."
    scene 10threesome86 with dissolve
    mc "All right, you guys ready for round two?"
    ls "Yeah, and from your huge boner, we can see you're ready, too."
    mc "Yeah."
    mc "And now it's Jade's turn."
    jd "Mine?"
    ls "It's yours."
    scene 10threesome87 with dissolve
    jd "So this time we'll get to the end?"
    mc "You can be sure of that."
    ls "Okay, enough talk, get down on the table and let [mc] fuck you!"
    jd "Okay."
    scene 10threesome88 with dissolve
    ls "Come on, [mc]... Put your dick in her."
    ls "Look how much she wants it."
    ls "You want it, don't you, Jade?"
    jd "Yeah..."
    ls "Speak louder!"
    jd "Yes! I want that cock!"
    ls "That's what I thought."
    scene 10threesome89 with dissolve
    ls "Yes... There you go."
    scene 10threesome89a with vpunch
    jd "Aaahhh!"
    scene 10threesome90 with dissolve
    mc "{i}Yes... She definitely likes it.{/i}"
    scene anim113 with dissolve
    jd "Aaahh!!! Aaaahhh!!! Aaaaahhhh!!!"
    ls "Look at how loud she's moaning!"
    mc "{i}Uhhh... Looks like Lisa enjoys teasing Jade.{/i}"
    mc "{i}But I kind of like it.{/i}"
    pause
    scene 10threesome91 with dissolve
    "You turned your head to Lisa's side, and you realized that she was masturbating looking at you."
    scene anim114 with dissolve
    jd "Aaahh... A little more... A little more..."
    ls "[mc], you hear her asking for more!"
    mc "{i}Man, this commanding tone is driving me crazy.{/i}"
    pause
    scene anim115 with dissolve
    jd "Aahhh... Yeah... It's so nice..."
    mc "Yes, very nice."
    pause
    scene 10threesome92 with dissolve
    ls "Mmm... I'm tired of standing here alone."
    ls "Do you mind if I join the fun?"
    mc "Of course. Get on the table."
    scene 10threesome93 with dissolve
    "The girl started climbing the table."
    scene 10threesome94 with dissolve
    "A few seconds later, Lisa settled right next to Jade."
    scene anim116 with dissolve
    "Her hands were gently rubbing her friend's chest."
    ls "Oh... Her heart's beating so fast right now."
    jd "Aahhh... Aaahhhh... Aaahhhh..."
    ls "Jade, I want to try something... I hope you figure out what to do."
    pause
    scene 10threesome95 with dissolve
    ls "There you go!"
    scene anim117 with dissolve
    ls "Use your tongue properly, you hear?"
    jd "Um... Mm-hmm... Mmmm..."
    mc "Oh, you girls!"
    pause
    scene 10threesome96 with dissolve
    "..."
    scene anim118 with dissolve
    "You've accelerated your moves."
    ls "Aahhh... Yes... Lick me harder!!!"
    jd "Mmmm!!! Mmmm!!!! Mmmm!!!!"
    pause
    scene 10threesome98 with dissolve
    "All of a sudden, you and Lisa are facing each other."
    ls "Kiss me."
    mc "Yes."
    scene 10threesome99 with dissolve
    "The next moment, your lips touched."
    scene anim119 with dissolve
    ls "Mmmnnn..."
    mc "{i}What a naughty tongue she's got.{/i}"
    pause
    scene 10threesome97 with dissolve
    "All this time, Jade was licking Lisa's pussy just like she's used to."
    scene anim120 with dissolve
    mc "{i}Oh... I can barely hold back.{/i}"
    mc "{i}I can't take it anymore!{/i}"
    scene 10threesome100 with dissolve
    "You stopped kissing Lisa and started jerking off."
    mc "Aahhhhhh... I'll just... A little more!"
    ls "Um... Come on, [mc]."
    jd "Oh... Don't hold back."
    scene 10threesome100a with flash
    mc "{i}Come on!!!{/i}"
    scene 10threesome100a with flash
    mc "Aaaahhh!"
    scene 10threesome101 with dissolve
    "*Heavy breathing sounds*"
    jd "Wow... His sperm is so warm."
    ls "Hehe. It's true."
    scene 10threesome102 with dissolve
    mc "Ladies, I gotta tell you, that was really cool!"
    scene 10threesome103 with dissolve
    ls "I agree."
    ls "And I think we'll have to do it again sometime."
    ls "What do you think about that, Jade?"
    jd "Yeah, um... I don't mind at all."
    scene 10threesome102 with dissolve
    mc "Excellent!"
    stop music fadeout 3.0
    mc "And now it's time to clean up."
    scene black with fade
    "A few minutes later you got dressed and were ready to leave this place."
    scene 10threesome104 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Hey, when you're standing so nicely wrapped in each other's arms, I start to envy you."
    ls "Mmm... Maybe you mean you're starting to get jealous?"
    mc "Maybe I am."
    scene 10threesome105 with dissolve
    jd "You don't have to worry about that."
    ls "Jade's right, we all like each other here."
    scene 10threesome106 with dissolve
    ls "Besides, after everything that's happened here, you should be the least jealous person in the world."
    scene 10threesome107 with dissolve
    ls "Now, to calm you down..."
    "The girls started slowly hugging you from different sides."
    ls "We're gonna do this."
    scene 10threesome108 with dissolve
    "*Kiss*"
    mc "{i}Heh, I guess I really don't have to worry about that.{/i}"
    scene 10threesome109 with dissolve
    mc "{i}After all, I am now the happiest man on Earth.{/i}"
    $ renpy.end_replay()
    if not persistent.day10lisajade:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day10lisajade = True    
    stop music fadeout 3.0
    scene black with fade
    "Soon after, you said goodbye to each other and went home."
    "You marked one thing for yourself, it was the best rehearsal of your life."
    if anna_sex == True and anna_colleague == False:
        jump day10_anna_start
    elif anna_sex == False and jane_date_offer == True:
        jump day10_jane_date
    elif anna_colleague == True and jane_date_offer == True:
        jump day10_jane_date        
    else:
        "You had a weekend ahead of you."
        jump day11_start


label day10_anna_start:
    scene black with fade
    "That night, you decided to confront Anna."
    "You had to find out why she's been acting so strange the past few days."
    scene 10anna01 with dissolve
    play music "music/10 - Street's.ogg"
    v "Ma'am, this is the third time I've told you that I haven't seen the man you're telling me about."
    "{color=#FFC0CB}Girl{/color}" "Yeah, but he's got to be around here somewhere..."
    scene 10anna02 with dissolve
    v "I'm sorry, but I have other things to do. Look for him yourself."
    "{color=#FFC0CB}Girl{/color}" "Uh... okay."
    scene 10anna03 with dissolve
    v "I didn't know you were working today, [mc]."
    mc "Actually, I'm not. I came here to talk to Anna."
    scene 10anna03a with dissolve
    v "Hm... Came here on your day off to talk to your girlfriend? That's interesting."
    v "As far as I know, she should be in the boss's office right now."
    mc "What about Catherine? Is she here?"
    v "She's not here yet. And she'll probably be very late today."
    mc "I got it. Thanks for your help, man."
    v "No problem."
    scene 10anna06 with dissolve
    "You went up to Catherine's office looking for Anna."
    mc "{i}Yeah, just like Vincent said, she's here.{/i}"
    mc "{i}It doesn't look like she's doing anything, which means she's not gonna be able to get out of this conversation.{/i}"
    scene 10anna07 with dissolve
    a "Hey, [mc]! What are you doing here? Isn't it your day off?"
    mc "Yeah, sorry to come unannounced, but I wanted to talk to you about something."
    scene 10anna08 with dissolve
    "Anna took her phone away and jumped off the boss's desk."
    a "Sure, what's on your mind?"
    mc "{i}She's in a good mood. That's obviously gonna be good for me."
    scene 10anna09 with dissolve
    mc "To tell you the truth, I wanted to talk to you about what's going on between us right now. You've been avoiding me all the time lately."
    a "Well, actually, it's not like that-"
    mc "Wait, please, let me finish."
    a "Um... Uh, okay."
    scene 10anna10 with dissolve
    "You gently held the girl's hands and continued."
    scene 10anna11 with dissolve
    mc "I want you to know that I like you very much. And I know that you like me, too. But your behavior just knocks me off the table."
    mc "And I think it started after you talked to Catherine."
    mc "Please tell me what happened between you two. You and I are gonna take care of all this together. You have my word on that."
    scene 10anna12 with dissolve
    a "Actually, it's not as simple as you think..."
    mc "I understand, but that's why I want to help you. I mean, to help both of us."
    scene 10anna12a with dissolve
    a "I... I..."
    "For a brief moment, Anna thought."
    scene 10anna13 with dissolve
    a "To hell with it! You're right, I'm sick of keeping it all to myself. Let's go!"
    scene 10anna14 with dissolve
    "The girl grabbed your hand tight and pulled you with a confident look."
    mc "Hey, where are we going?"
    a "I need some fresh air. Now."
    stop music fadeout 3.0
    scene black with dissolve
    "A few minutes later."
    scene 10anna15 with dissolve
    play music "music/8 - Intro Music.ogg"
    mc "I didn't know you smoked."
    a "I usually don't, but right now I just need a cigarette."
    mc "{i}This is so weird. Anna's clearly not one of the timid ten, but when it comes to Catherine, she gets very twitchy and hesitant.{/i}"
    scene 10anna16 with dissolve
    "..."
    scene 10anna16b with dissolve
    a "You were right. I was acting so out of the ordinary just because I talked to Catherine."
    a "She knows about us."
    scene 10anna16a with dissolve
    a "What's more, we got caught on one of her security cameras. The one right in her office."
    mc "Oh..."
    mc "{i}So that's why she decided to talk outdoors. Clever girl.{/i}"
    scene 10anna16 with dissolve
    "..."
    scene 10anna16b with dissolve
    a "Yeah. I knew about that camera, but the night it happened, I was too depressed and completely forgot about it..."
    a "Catherine usually doesn't have the habit of looking at the cameras from her office, but because she hasn't been to the club for a week and because of that jerk Tom, she did look at them."
    a "Well, you can imagine exactly what she saw."
    mc "Yeah, I think I can guess."
    scene 10anna16 with dissolve
    "..."
    scene 10anna16a with dissolve
    a "Yeah."
    a "Anyway, she was aware that I was dating Tom, and when she found out that I was going to date you now, she wasn't happy about it."
    scene 10anna17 with dissolve
    mc "{i}Yeah, well, I guess as the boss, Catherine's view is understandable.{/i}"
    mc "{i}That's why people say having a relationship where you work is a bad idea.{/i}"
    scene 10anna18 with dissolve
    mc "{i}Because if something happens, and the couple eventually breaks up, it'll be very, very hard for those people to work together. If they can at all.{/i}"
    scene 10anna20 with dissolve
    a "Anyway, Catherine offered me two options: either she fires you or we stop seeing each other."
    mc "{i}So it was an ultimatum. That sucks.{/i}"
    a "As you can see, I didn't have much of a choice."
    mc "That's an understatement."
    mc "{i}Hmm... The easiest way out of this situation for me would be to quit right here and now. But something tells me that option should be left as a last resort.{/i}"
    scene 10anna19 with dissolve
    mc "How about this: at work, you and I will act exclusively as colleagues, and outside work, we will act as we want."
    a "Huh. I don't think that would be enough to change Catherine's attitude. Besides, sooner or later, she's gonna find out, and it's only gonna get worse."
    a "You have to understand that I have invested too much time and energy into this place, and it means a lot to me."
    a "If I lie to Catherine, I'm not sure she'll ever forgive me."
    mc "{i}So this is how it works... Then the only option comes to mind is-{/i}"
    mc "You know, then I'll talk to her myself."
    scene 10anna21a with dissolve
    a "I'm not sure that's a good idea."
    mc "Don't worry, I'll keep a close eye on what I say. Besides, I have some experience with this type of person."
    scene 10anna21 with dissolve
    a "You do?"
    mc "Yeah."
    a "Okay, if you really think it's gonna help, I don't mind."
    mc "Is she coming here today?"
    a "Yeah, she said she'd be here by the end of the evening."
    mc "Then I'll wait for her somewhere at the club."
    a "Great, that's what we'll do."
    scene 10anna22 with dissolve
    "Anna gently kissed you on the cheek."
    scene 10anna23 with dissolve
    a "I hope you can work it out."
    mc "It's gonna work out."
    a "Heh. Okay, just don't overdo it."
    scene 10anna24 with dissolve
    mc "Yeah... I'll try..."
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 10anna04 with dissolve
    mc "{i}Hmm... Catherine's in no rush to work today.{/i}"
    mc "{i}Hope I don't have to wait too long for her.{/i}"
    scene black with dissolve
    "A little more time later."
    scene 10anna05 with dissolve
    "You noticed Catherine heading upstairs."
    mc "{i}Oh... I almost missed her.{/i}"
    mc "{i}Looks like it's time for a tough conversation. Uh, I hope it goes well.{/i}"
    scene 10anna25 with dissolve
    play music "music/13 - Hope is Still Living.ogg"
    "When you walked into Catherine's office, you noticed she was busy reading some book."
    scene 10anna26 with dissolve
    k "[mc]. What are you doing here?"
    mc "{i}Okay, there's nowhere to back down. It's now or never.{/i}"
    scene 10anna27 with dissolve
    mc "First of all, I want to say that I didn't come here as your employee, but rather as a concerned person."
    k "What an unusual start to a conversation. Go on."
    mc "{i}Shit... I'm pissed off by her imperturbability.{/i}"
    mc "Yes... The thing is, I want to talk to you about your recent conversation with Anna."
    scene 10anna28 with dissolve
    k "That's weird. Thought you would come to talk about it together."
    mc "{i}Huh. So she expected this kind of conversation?{/i}"
    mc "Then what's the point of all this? Why all the difficulties and ultimatums?"
    scene 10anna29 with dissolve
    "Catherine stands up."
    k "I don't know what Anna told you, but I'll warn you right away that I didn't threaten her with anything. Not by firing her or anything else."
    k "All I did was talk to her."
    mc "{i}She may not have threatened to fire Anna, but she threatened to fire me.{/i}"
    mc "Yes, I'm already aware of your conversation."
    scene 10anna30 with dissolve
    k "Then you should know why I don't like it."
    mc "Look, let's be adults, and do this: Anna and I will continue to date, but we will ensure that our relationship does not affect the work."
    mc "And if we don't, I'll quit."
    scene 10anna31 with dissolve
    "Suddenly Catherine stepped in your direction and gently touched your chin with her hand."
    k "Very interesting."
    scene 10anna32 with dissolve
    k "But your offer is denied."
    scene 10anna33 with dissolve
    "..."
    scene 10anna34 with dissolve
    mc "What? But why?!"
    scene 10anna35 with dissolve
    k "Why?"
    k "Because you don't know her at all."
    scene 10anna36 with dissolve
    k "Yeah, she likes you. But you're not the kind of guy she needs."
    k "Believe me, I know that. In the long run, you two don't stand a chance."
    mc "I appreciate your opinion, but that's not for you to decide."
    scene 10anna37 with dissolve
    k "..."
    scene 10anna38 with dissolve
    k "Please take a seat."
    mc "What? Um... Thank you, but I'd rather stand."
    k "I insist. Otherwise, we should end this conversation right now."
    mc "{i}Okay, I'll do what she wants.{/i}"
    scene 10anna39 with dissolve
    "You sat in one of the chairs across from Catherine."
    mc "So, can you explain why you're so principled about my relationship with Anna?"
    k "Like I said, you're not right for each other."
    mc "Yeah, I've heard that before. Can't you add a little more specificity?"
    scene 10anna40 with dissolve
    k "I've seen you work in a bar, and I've seen you look at other girls."
    mc "{i}Really? Did she realize that we don't fit together just by looking at us? This is bullshit.{/i}"
    if selina_path == True or rosa_path == True:
        scene 10anna40a with dissolve
        k "Besides, I saw you in the company of Rosa and her daughter. Believe me, that told me a lot."
        mc "{i}Damn it, I knew that meeting would cost me a lot.{/i}"
    scene 10anna41 with dissolve
    k "On the other hand... Even though you're not one of the kind of guys that's right for Anna..."
    k "You're one of the guys that's right for me."
    mc "{i}Huh?!{/i}"
    mc "Hey, hey! This is some kind of joke, right?"
    scene 10anna42 with dissolve
    k "No jokes. You're young, you're in a rock band and just like other musicians you're not looking for a serious relationship? Are you?"
    mc "Uh... I don't know. I never plan ahead."
    k "But I know."
    scene 10anna43 with dissolve
    k "I can't promise you love until the coffin, but we'll have a couple of fun nights together. So, what do you think?"
    k "Just tell Anna that your relationship is over."
    k "I'm pretty sure she'll understand it and won't be sad for long."
    mc "{i}Man... Catherine always seemed so cold, but now she's completely different. I don't get it.{/i}"
    mc "{i}And wasn't that the main motivator why she told Anna to forbid our relationship?{/i}"
    mc "{i}What should I do in this situation?{/i}"
    stop music fadeout 3.0
    menu:
        "Refuse her (Anna scene)":
            scene 10anna44 with vpunch
            play music "music/8 - Intro Music.ogg"
            mc "No way!"
            mc "Ahem... I mean, um... You're a very beautiful woman and all, but it's not right. I just can't do this to Anna."
            scene 10anna40a with dissolve
            k "Really? That's not what I expected."
            mc "I can' t do anything about it."
            mc "As I said earlier, I'm going to date Anna. And after what I just heard, I don't care about your opinion anymore."
            mc "And now I'm leaving."
            scene 10anna45a with dissolve
            "Leaving Catherine's office, you could feel her thoughtful gaze on you."
            mc "{i}I hope I did the right thing.{/i}"
        "Agree with her":
            $ day10_catherine_offer = True
            scene 10anna44a with dissolve
            play music "music/8 - Intro Music.ogg"
            mc "I feel like a real scumbag right now, but you're right. I'm not looking for a serious relationship right now."
            k "Excellent."
            k "Now all you have to do is tell Anna that you couldn't change my mind and you have to break up."
            scene 10anna40a with dissolve
            k "And then I think you and I should meet this weekend."
            mc "Sounds intriguing."
            k "Oh, believe me, it is."
            k "Now if we're done, you can go."
            scene 10anna45 with dissolve
            "Leaving Catherine's office, you felt her sly eyes on you."
            mc "{i}I hope I did the right thing.{/i}"
    scene 10anna46 with dissolve
    stop music fadeout 3.0
    "You came out of Catherine's office and sighed with relief."
    mc "{i}Well... That wasn't an easy conversation.{/i}"
    mc "{i}Now I' ve got to find Anna.{/i}"
    scene 10anna47 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "To your surprise, Anna was much closer than you thought."
    mc "Ahem!"
    scene 10anna48 with dissolve
    a "Oh! You're finally finished!"
    a "You've been gone a long time."
    scene 10anna49 with dissolve
    "The girl put the pen and notebook aside."
    scene 10anna50 with dissolve
    a "So, how'd it go? Did you manage to change her mind?"
    mc "{i}She seems pretty worried.{/i}"
    if day10_catherine_offer == True:
        mc "{i}I hate to disappoint her, but I have to do it.{/i}"
        mc "Sorry, I tried, but it didn't work out. Catherine was very stubborn in her decision."
        scene 10anna51a with dissolve
        a "Oh... That's a shame. But I'm sure you tried your best."
        a "So we have to break up?"
        mc "Yes... At least for a while."
        a "I understand."
        mc "{i}Great, now I feel even more guilty...{/i}"
        stop music fadeout 3.0
        scene black with fade
        "Soon you said goodbye to Anna and went home."
        if jane_date_offer == True:
            jump day10_jane_date
        else:
            "You had a weekend ahead of you."
            jump day11_start
    else:
        mc "{i}But now I can make her happy.{/i}"
        mc "You can congratulate me, I did it!"
        scene 10anna51 with dissolve
        a "Oh, my God! Is it really true?!"
        mc "Yep."
        mc "It wasn't easy, but thanks to my natural charm I was able to get the right result."
        scene 10anna52 with dissolve
        "Without saying a word, Anna rushed into your arms."
        a "You're amazing!"
        scene 10anna53 with dissolve
        "And then she kissed you."
        mc "{i}Mmm... I love this gratitude.{/i}"
        scene 10anna54 with dissolve
        a "You know, to tell you the truth, I wasn't sure if you could do it. But now... Now I'm just ready to explode with joy!"
        mc "And I'm glad that you are glad."
        a "Mmm... That is so sweet."
        scene 10anna55 with dissolve
        a "Now, if you wait a little longer, I'll finish the work so we can go to my place and have a great time for the rest of the night."
        mc "Sounds like a great plan!"
        a "Yeah, it is."
        mc "Well, then I'm all for it."
        a "You won't regret it!"
        stop music fadeout 3.0
        jump day10_anna_street

label day10_anna_street:
    scene black with fade
    "Some time later."
    "After Anna's shift was over, you went to her house."
    scene 10annastreet01 with dissolve
    play music "music/2 - Bad.ogg"
    a "So this weekend your band will rock at this student bar?"
    mc "Yeah, something like that."
    a "I know the owner of that place. I can tell you with confidence, he's a stingy guy."
    mc "Well, so far, we don't have much choice where to sing."
    scene 10annastreet02 with dissolve
    a "Um... Perhaps someday you could do a show at our club?"
    mc "Huh. If that happens, it'll be fun."
    a "Definitely!"
    scene 10annastreet02a with dissolve
    "Suddenly, Anna froze."
    stop music fadeout 1.0
    a "Oh."
    mc "Is something wrong?"
    scene 10annastreet03 with dissolve
    play music "music/8 - Intro Music.ogg"
    "After following where Anna is looking, you stopped, too."
    mc "{i}Hey, what the hell is this guy doing here?{/i}"
    scene 10annastreet04 with dissolve
    "He noticed you, too."
    t "Anna... And you..."
    scene 10annastreet05 with dissolve
    "Tom slowly turned his gaze down."
    mc "{i}I don't really like this.{/i}"
    scene 10annastreet06 with dissolve
    a "What the fuck are you doing here, Tom?!"
    a "I told you, it's over between us! You ruined it yourself!"
    scene 10annastreet07 with dissolve
    t "Listen, baby, but I just wanted to talk to you."
    a "Hey! Stay away from me!"
    t "Baby, you don't understand--"
    scene 10annastreet08 with dissolve
    mc "Didn't you hear what she said? Stay away from her."
    mc "Leave!"
    scene 10annastreet09 with dissolve
    "{cps=15}...{/cps}"
    scene 10annastreet10 with dissolve
    t "You shouldn't have done that. This doesn't fucking concern you at all!"
    stop music fadeout 3.0
    scene 10annastreet11 with vpunch
    "The next moment, you felt a sharp blow to the jaw."
    scene 10annastreet12 with dissolve
    play music "music/5 - Adrenaline Fight.ogg"
    "As soon as you realized what was happening, you noticed that the next blow was coming at you."
    menu:
        "Counterattack (+Bad point)":
           $ badpoint += 1
           mc "{i}Let's see how he likes my fist.{/i}"
           scene 10annastreet14 with dissolve
           "Tom dodged with ease..."
           scene 10annastreet15 with vpunch
           "...and hit you again with all his strength."
           scene 10annastreet16 with dissolve
           mc "{i}Fuck! It hurts so much...{/i}"
           mc "{i}This guy's dangerous. I need to be careful.{/i}"
           scene 10annastreet18 with dissolve

        "Block (+Good point)":
           $ goodpoint += 1
           mc "{i}I don't think I can do anything but block.{/i}"
           scene 10annastreet13 with vpunch
           "You were lucky to block your attacker's strike."
           scene 10annastreet17 with dissolve
           mc "You wanna fight, no problem."
           mc "{i}This guy's dangerous. I need to be careful.{/i}"
           scene 10annastreet18a with dissolve
    t "I didn't like you from the start."
    mc "Yeah, it was mutual."
    scene 10annastreet19 with dissolve
    t "Do you really think you even have a chance in a fight against me?"
    t "Now I'm gonna beat the shit out of you."
    stop music
    play sound "music/music_stop.wav"
    scene 10annastreet20 with vpunch
    a "STOP! QUICKLY STOP THIS SHIT!!!"
    mc "{i}What the fuck?! A gun?! Where the hell did she get it?!{/i}"
    scene 10annastreet21 with dissolve
    play music "music/8 - Intro Music.ogg"
    t "Hey, hey! Calm down, we were just fooling around. No one would get hurt. You know me."
    a "That's the problem, I know you a lot better than I'd like to know you."
    a "Now get out of here!"
    a "And if I ever see you here again, I'm gonna put some extra holes in your ass. {size=45}Do you understand me?!{/size}"
    scene 10annastreet22 with dissolve
    t "Yes... Yes... I got it! You'll never see me again."
    a "Get out!"
    scene 10annastreet23 with dissolve
    "With a scared look back, Tom hurried as far away from you as possible."
    mc "{i}It seems Anna scared him pretty good.{/i}"
    stop music fadeout 3.0
    mc "{i}Oh, man, I'm confused myself.{/i}"
    scene 10annastreet24 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Hey, what was that?"
    a "Hmm? In case you hadn't noticed, I chased that jerk away."
    a "But you can rest assured that I appreciate your impulse to protect me."
    mc "Yeah, well... Thanks, I guess."
    mc "But where did you get that gun?"
    scene 10annastreet25 with dissolve
    a "You mean this thing?"
    mc "Yeah, that thing."
    scene 10annastreet25a with dissolve
    a "Well, I'm a very fragile girl who often comes home from work late at night. You know, I must have some kind of self-defense."
    mc "Right. For some reason, I didn't even think about it."
    mc "But maybe you should put it away before anyone else sees it."
    a "Yeah, I guess so."
    scene 10annastreet26 with dissolve
    "Anna hid the gun in her tiny bag."
    mc "{i}I wonder how it even fits in there.{/i}"
    scene 10annastreet27 with dissolve
    mc "Heh. You happen to be a very dangerous girl."
    a "Yes, I am! So the next time you want to fight with me, make sure you keep it in your head."
    mc "Haha. I'll remember that."
    scene 10annastreet28 with dissolve
    mc "Ouch!"
    "You felt a sharp pain where Tom hit you."
    scene 10annastreet29 with dissolve
    a "Oh, does it hurt bad?"
    mc "Don't worry, I'm fine."
    a "Yeah, I can see that."
    scene 10annastreet29a with dissolve
    a "All right, come on in, I'll take care of you."
    mc "Well, I don't mind that."
    scene 10annastreet30 with dissolve
    "Anna gently wrapped her hand around you and took you to her apartment."
    mc "Hey, actually, it doesn't hurt that much."
    a "Shut up and let's go."
    mc "Huh. Whatever you say, commander."
    stop music fadeout 3.0
    jump day10_anna_home

label day10_anna_home:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "Some time later."
    play sound "music/water.wav"
    scene 10annahome01 with dissolve
    "{cps=15}...{/cps}"
    scene 10annahome02 with dissolve
    stop sound fadeout 3.0
    "{cps=15}...{/cps}"
    scene 10annahome03 with dissolve
    mc "{i}Uh, shit... That jerk hits really hard.{/i}"
    mc "{i}I hope there's no bruising.{/i}"
    scene 10annahome04 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    "You felt Anna's warm palm lying on your shoulder."
    a "How are you? Everything okay?"
    mc "Yes... Just needed a little refreshing."
    a "That's good."
    scene 10annahome05 with dissolve
    "The girl leaned softly on your back with her whole body."
    a "I'm glad you were here with me today."
    a "God only knows what would happen if I were alone with Tom."
    scene 10annahome06 with dissolve
    a "Thank you, [mc]."
    mc "I did what I had to."
    a "It's so... But I want you to know how much I appreciate it."
    scene 10annahome07 with dissolve
    "Anna's elegant leg wrapped around your waist."
    mc "Mmm... Someone seems to be in a playful mood right now?"
    mc "I like that."
    scene 10annahome08 with dissolve
    "With one sharp move, you picked up Anna in your arms."
    a "Hee-hee! What are you up to?!"
    mc "Don't worry, I'll take you to a better place in a second."
    scene 10annahome09 with dissolve
    "You took the girl out of the bathroom and stopped."
    mc "So... Where should I take you? Maybe straight to the bedroom?"
    scene 10annahome10 with dissolve
    a "Mmm... Tempting offer, but you better take me there."
    mc "That way?"
    scene 10annahome11 with dissolve
    "You looked where Anna was pointing."
    a "Uh-huh. That way."
    mc "Well, the lady's wish is the law."
    scene 10annahome12 with dissolve
    "A few seconds later, you put your girlfriend on the floor right by the couch."
    a "Yes... This is exactly what we need."
    mc "Oh, really?"
    scene 10annahome13 with dissolve
    a "Absolutely."
    a "Now, you can make yourself comfortable here. I think you'll like what happens next."
    mc "Ha! This is getting interesting."
    scene 10annahome14 with dissolve
    "Keeping your eyes on Anna, you slowly sat down on the couch."
    mc "{i}What a beautiful view.{/i}"
    mc "{i}And I feel like I'm about to see a lot more.{/i}"
    stop music fadeout 3.0
    scene 10annahome15 with dissolve
    a "I hope you're paying attention."
    mc "You can be sure of that."
    scene 10annahome16 with dissolve
    play music "music/15 - Deep Mood.ogg"
    "Anna slowly lowered the top of her dress, revealing a view of her chic naked breasts."
    mc "{i}Oh, yeah... This was definitely worth taking one in the face for.{/i}"
    scene 10annahome17 with dissolve
    a "From your smiling face, I can tell you like what you see."
    mc "Heh. Can you blame me?"
    scene 10annahome18 with dissolve
    a "Then how about this?"
    mc "Oh... I think this room's getting hotter and hotter every second."
    scene 10annahome19 with dissolve
    mc "Also, I think my pants are getting really, really tight right now."
    a "Mmm... Maybe I can help you with that."
    scene 10annahome20 with dissolve
    "Gracefully swaying her hips, Anna headed to your direction."
    scene 10annahome21 with dissolve
    mc "You look even hotter in these heels."
    a "That's good..."
    scene 10annahome22 with dissolve
    a "You don't have to hold back. I know your naughty hands are already impatient to start acting."
    mc "{i}She's definitely right about that.{/i}"
    scene 10annahome23 with dissolve
    "You gently touched Anna's leg with your hands and moved your palms over her soft skin."
    "And then..."
    scene 10annahome24 with dissolve
    "And then... Pulled her toward you."
    a "Ah!"
    scene 10annahome25 with dissolve
    a "There's no need to be in such a hurry. I'm not going anywhere, you know that."
    mc "But didn't you tell me that I shouldn't hold back?"
    a "Oh, you're a sly one."
    scene 10annahome26 with dissolve
    "Your hands crawled up Anna's waist and gently stopped on her firm breasts."
    mc "{i}Yes... What a fucking pleasure.{/i}"
    scene 10annahome27 with dissolve
    mc "{i}A little more...{/i}"
    a "Ah... What are you..."
    scene 10annahome28 with dissolve
    a "Um... Yes... Like that..."
    mc "{i}How long I've waited for this!{/i}"
    scene 10annahome29 with dissolve
    a "Oh... I have to say, I like your aggression."
    a "But don't think you're the only one here who wants it?"
    scene 10annahome30 with dissolve
    "The next moment, Anna wrapped her arms around you and kissed you hard."
    scene anim121 with dissolve
    a "Mmm... Yes... Mmm... Like this..."
    mc "{i}It feels so good... I can't stop.{/i}"
    pause
    scene 10annahome31 with dissolve
    mc "{i}And it looks like I'm not the only one who's turned on so much.{/i}"
    scene 10annahome32 with dissolve
    "{cps=15}...{/cps}"
    scene 10annahome33 with dissolve
    mc "It was..."
    a "Yes... I know... I missed that, too."
    scene 10annahome34 with dissolve
    a "Now how about we continue?"
    mc "I'd love to."
    scene 10annahome34a with dissolve
    a "Yes... I can see your big guy's ready."
    a "But above all..."
    scene 10annahome35 with dissolve
    "Anna stood up."
    a "Get rid of any clothes that might disturb us."
    scene 10annahome36 with dissolve
    "She pulled her panties down, uncovering her perfect ass."
    mc "{i}Her body is just gorgeous.{/i}"
    scene 10annahome37 with dissolve
    mc "Oh, yeah... So far, I like everything."
    scene 10annahome38 with dissolve
    a "Hee-hee. And since I'm not wearing clothes anymore, I'll help you with those, too."
    mc "I'm all yours."
    scene 10annahome39 with dissolve
    "Anna arched her back and lightly touched your chest."
    scene 10annahome40 with dissolve
    a "Undo the zipper..."
    mc "Come on, stop teasing me... Just a little more."
    scene 10annahome41 with dissolve
    a "I know, I know. Till we got to the bottom of it."
    mc "{i}At last.{/i}"
    scene 10annahome42 with dissolve
    "Anna pulled your pants off you and stared at your dick."
    mc "{i}Ohh... I can feel her hot breath.{/i}"
    scene 10annahome43 with dissolve
    a "Um... We need to cheer him up a little."
    scene 10annahome43a with dissolve
    mc "{i}Oh... Her fingers are so warm.{/i}"
    a "Okay, let's start slowly..."
    scene 10annahome44 with dissolve
    "The girl's palm wrapped around your dick and started jerking you off confidently."
    scene anim122 with dissolve
    mc "{i}Ahh... Ahh...{/i}"
    a "Yeah... Like this... Great..."
    a "Now let's do this..."
    pause
    scene 10annahome45 with dissolve
    "Anna's lips touched the head of your cock."
    scene 10annahome46 with dissolve
    mc "{i}It's so exciting!{/i}"
    scene anim123 with dissolve
    mc "{i}Ohhh... She uses her tongue so cleverly...{/i}"
    a "Mmm.... Mmmmpphhh... Mmmmpphhh..."
    mc "Baby, take it deeper."
    pause
    scene 10annahome47 with dissolve
    a "Deeper? That's interesting."
    a "But maybe I'll try this first."
    scene 10annahome48 with dissolve
    "{cps=15}...{/cps}"
    scene anim124 with dissolve
    mc "{i}Yeah... That hot tongue is just great.{/i}"
    mc "Ahh... More... Take it all in your mouth..."
    mc "Let's... Do it, baby!"
    pause
    scene 10annahome47 with dissolve
    a "Well, since you're so insistent, I guess I just don't have any other choice."
    scene 10annahome49 with dissolve
    "The next second, your dick was all in the girl's throat."
    scene anim125 with dissolve
    mc "{i}Ahh... It feels amazing.{/i}"
    a "Mmmmphh.... Mmmmpphhh... Mmmmpphhh..."
    pause
    scene anim126 with dissolve
    mc "Come on... Suck it... Suck it harder!"
    a "Mmmmppphhh... Mmmmpphhh.... Mmmmphhh...."
    pause
    scene 10annahome50 with dissolve
    mc "{i}She's doing a great job of it.{/i}"
    mc "{i}I don't think I can hold out much longer.{/i}"
    scene 10annahome51 with dissolve
    "Feeling like you were about to cum, you jumped up on your feet."
    mc "{i}Ooohh... Just a little more!{/i}"
    a "Mmm.... Mmmmpphhh... Mmmmpphhh..."
    scene 10annahome52 with dissolve
    mc "{i}Okay, I can't hold back anymore!!!{/i}"
    mc "{i}Where should I cum?{/i}"
    menu:
        "Cum in her mouth":
            scene 10annahome53 with dissolve
            "With a quick move, you grabbed Anna's head."
            scene 10annahome53a with vpunch
            "And then you put your dick down her throat as deep as you can."
            a "Mmmpphhh! Mmmpphhh!! Mmmpphhh!!!"
            scene 10annahome53a with flash
            mc "Oh yeah!!! Yeah!!!"
            scene 10annahome53a with flash
            mc "CUMMING!!!"
            scene 10annahome56a with dissolve
            a "Oh, my God... You're a real beast."
            mc "Yeah... I'm sorry about that."
            a "Heh. It's okay, I may have liked it."
            mc "You're such a bad girl."
        "Cum on her face":
            scene 10annahome54 with dissolve
            "You took your dick out of her mouth, and you immediately started jerking off."
            a "Come on, baby... Do it right on my face!"
            mc "{i}Ohhhh.... I'm almost!!!!{/i}"
            scene 10annahome55 with flash
            mc "Oh yeah!!! Yeah!!!"
            scene 10annahome55 with flash
            mc "CUMMING!!!"
            scene 10annahome56 with dissolve
            a "Wow... That was intense."
            a "You got me all dirty."
            mc "Well, you asked me to."
            a "Heh. It's okay, I may have liked it."
            mc "You're such a bad girl."
    a "Okay, now I have to get cleaned up."
    stop music fadeout 3.0
    scene black with fade
    "Just a minute later."
    scene 10annahome57 with dissolve
    play music "music/8 - Intro Music.ogg"
    "Absolutely naked, you and Anna stood in the middle of the room hugging each other."
    mc "Have I told you how amazing you are?"
    a "Yeah, but I don't mind hearing it as many times as I can."
    scene 10annahome58 with dissolve
    a "Mmm... I think I could stand with you like this forever."
    scene 10annahome58a with dissolve
    a "But your dick looks like it's ready to continue."
    scene 10annahome59 with dissolve
    "You realized she was right."
    mc "How about a second round?"
    scene 10annahome60 with dissolve
    a "You're asking?"
    a "I'm in!"
    stop music fadeout 3.0
    mc "Heh. I knew you'd say that."
    scene 10annahome61 with dissolve
    play music "music/1 - Atmosphere.ogg"
    "Anna turned her back to you and exposed her ass."
    mc "{i}Um... What a stunning view.{/i}"
    scene 10annahome62 with dissolve
    mc "{i}I think I'm gonna have to warm this thing up a little before we start the main course.{/i}"
    scene 10annahome63 with dissolve
    "You touched Anna's firm butt."
    a "Aahhh... Please, be careful."
    mc "Don't worry, I'll be very careful."
    scene 10annahome64 with dissolve
    "With one sure move, you touched your girlfriend's wet pussy."
    scene anim127 with dissolve
    "...and then you started fucking her with your fingers."
    a "Aaah.... Mmmmm... Yeah..."
    "You noticed her moans getting louder."
    a "Mmm... Don't stop! Yeah! That's it!"
    mc "{i}I think she's ready.{/i}"
    pause
    scene 10annahome66 with dissolve
    a "Ah... What...? Why did you stop?"
    mc "Don't worry, now we'll continue."
    scene 10annahome68 with dissolve
    "You put your dick in Anna's pussy."
    scene 10annahome68a with vpunch
    "And then you made a quick thrust forward."
    scene 10annahome67 with dissolve
    a "Oh, yeah... That feels so good."
    mc "{i}Yeah... I agree with her on that.{/i}"
    scene anim130 with dissolve
    a "Aaahh... Aaaahhh... Aaaahh!"
    a "How much... How much I missed your dick!!! Aahhh!"
    pause
    scene anim132 with dissolve
    mc "{i}And I missed your pussy.{/i}"
    a "Mmm... [mc]... You can go faster!!!"
    pause
    scene anim132a with dissolve
    "You accelerated."
    mc "{i}Yeah, that's even better...{/i}"
    pause
    scene 10annahome65 with dissolve
    "The girl took her hands off the chair and moved them to her knees."
    scene anim129 with dissolve
    mc "{i}I missed that ass... those long legs and hips...{/i}"
    a "Mmm... Harder... Fuck me harder, [mc]!!!"
    pause
    scene anim128 with dissolve
    mc "{i}Oohh... Her pussy is squeezing my dick so hard...{/i}"
    a "Aaahh... More!!! Aaah.... More!!!"
    mc "I want... I want you to get in the chair."
    a "What...? Ohh... I think I figured out what you want."
    pause
    scene 10annahome69 with dissolve
    "The next moment, Anna was in the chair, and you were ready to move again."
    a "Come on... Don't hold back...."
    mc "I wasn't going to."
    scene 10annahome70 with dissolve
    "{cps=15}...{/cps}"
    scene anim131 with dissolve
    a "Aaah.... Um... Yeah..."
    a "Don't stop! Yeah..."
    pause
    scene 10annahome71 with dissolve
    "While still fucking Anna, you grabbed her hand."
    a "Ahh... What are you doing?"
    scene 10annahome72 with dissolve
    "And then you took the other one."
    mc "Everything... Everything's okay."
    scene 10annahome73 with dissolve
    "You held Anna to you."
    scene anim133 with dissolve
    a "Aahhh... Yeah... So good!!!"
    mc "{i}Damn, she's just driving me crazy.{/i}"
    pause
    scene 10annahome73a with dissolve
    "Suddenly you felt an unbridled desire to take her by the breast."
    scene 10annahome74 with dissolve
    a "Aahhhh... Do you... Do you like my boobs?"
    mc "They're magnificent."
    a "I... I'm almost..."
    mc "Yeah, me too..."
    scene 10annahome75 with dissolve
    a "AAAAHHHHHHHH!!!! YESSS!!!!"
    "You felt Anna's pussy squeeze hard."
    mc "{i}Ooohh... hell, I'm going to come, too.{/i}"
    menu:
        "Cum inside":
            scene 10annahome76 with dissolve
            mc "{i}Ooohh... I'm coming too!!!{/i}"
            scene 10annahome76a with flash
            mc "Oooohh!!! Yesss!!"
            scene 10annahome76a with flash
            "..."
            scene 10annahome77 with dissolve

        "Cum outside":
            scene 10annahome78 with dissolve
            "You got your dick out as soon as you could and you started coming right away."
            scene 10annahome79 with flash
            mc "Oooohh!!! Yesss!!"
            scene 10annahome79a with flash
            "..."
            scene 10annahome80 with dissolve

    a "Phew... That was something!"
    mc "Oh, yeah, it's been a long time since I've experienced anything like that."
    a "Mmm... You know, you and I still have a lot of energy. I think we may just have to continue."
    mc "Huh. Indeed!"
    stop music fadeout 3.0
    scene black with fade
    "Two hours later."
    scene 10annahome81 with dissolve
    play music "music/Maxim Nick - It's okay (final).mp3"
    "Only two heavy breaths can be heard in the air."
    a "Haa... Haa... Haa..."
    a "Guess what, my legs are still shaking."
    mc "Ha-ha. This is all your fault!"
    a "I know, I know... and I mean, it was worth it..."
    mc "That's for sure."
    scene 10annahome82 with dissolve
    mc "Hey, so you don't mind if I stay overnight?"
    a "Are you kidding me? After everything that happened between us today?"
    mc "Well, it never hurts to be sure."
    a "Of course you can stay."
    scene 10annahome83 with dissolve
    a "I also want to say that I'm glad you helped me with Catherine. I'm not sure if I could have handled it alone."
    mc "Like I said, if you have a problem, you tell me. We'll deal with them together."
    a "You're so sweet..."
    scene 10annahome84 with dissolve
    "Suddenly, Anna was right above you."
    mc "I thought you didn't have the energy left."
    scene 10annahome85 with dissolve
    a "I did, but only for this.."
    scene 10annahome86 with dissolve
    a "Mmm..."
    mc "{i}Yes... A good kiss.{/i}"
    scene 10annahome85 with dissolve
    a "It was a wonderful day... And now good night."
    scene 10annahome87 with dissolve
    mc "Yes... Good night to you, too."
    "After a while cuddling, you and Anna fell asleep."
    stop music fadeout 3.0
    scene black with fade
    "Next morning."
    scene 10annahome88 with dissolve
    play music "music/7 - Just Happy.ogg"
    "You woke up first, and drank in Anna's peaceful beauty."
    mc "{i}Well... Last night was really special. I had no idea it would go so well.{/i}"
    mc "{i}Even though that lunatic Tom showed up.{/i}"
    scene 10annahome88a with dissolve
    mc "{i}But now I have to go home. I have things to do today.{/i}"
    scene 10annahome89 with dissolve
    "As you pulled your pants up, you noticed that you accidentally woke Anna."
    a "Leaving already?"
    mc "Yeah, sorry, but I gotta go."
    a "That's a shame."
    scene 10annahome90 with dissolve
    a "But last night was just great!"
    mc "Heh. You wouldn't believe it, but I was literally just thinking the same thing."
    a "And not without reason."
    scene 10annahome91 with dissolve
    a "Hey, I hope you and I can do this again soon?"
    mc "Yeah, I'm looking forward to it."
    a "We'll be in touch, then."
    mc "Yeah, we'll be in touch."
    scene 10annahome92 with dissolve
    a "See you, [mc]."
    mc "Bye, Anna."
    $ renpy.end_replay()
    if not persistent.day10anna:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day10anna = True    
    stop music fadeout 3.0
    if jane_date_offer == True:
        jump day10_jane_date
    else:
        "You had a weekend ahead of you."
        jump day11_start

label day10_jane_date:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "Friday night."
    play music "music/10 - Street's.ogg"
    "That's the day you had a date with Jane."
    "She called you in advance and said she was picking you up in her car."
    scene 10janecar01 with dissolve
    mc "{i}Eh... It's so humiliating to be without my own car.{/i}"
    mc "{i}Alas, with the money I have now, I can't afford it.{/i}"
    mc "{i}I hope this trouble is only temporary.{/i}"
    "..."
    mc "{i}Oh, I think that's Jane!{/i}"
    scene 10janecar02 with dissolve
    "BEEP!"
    mc "{i}Yes, it's definitely her.{/i}"
    scene 10janecar03 with dissolve
    jn "Well, what are you waiting for? Hop on in."
    mc "Whatever you say, beautiful."
    scene 10janecar05 with dissolve
    "You got in a car."
    jn "I hope you didn't wait long for me."
    mc "No, it's okay. I just got out of the apartment."
    jn "All right then, let's go."
    scene 10janecar04 with dissolve
    mc "So... Why don't you tell me where we're going?"
    jn "Nope, I won't."
    mc "Really? You decided to keep the intrigue to the very end?"
    jn "I told you before, I don't want to ruin the surprise."
    jn "Besides, you'll see for yourself very soon."
    mc "Okay, I can't wait."
    scene black with fade
    "For some time you drove around the night lit city and talked about everyday topics."
    "Jane was talking about her business ventures, and you were sharing the news about your band."
    "Everything was going well."
    scene 10janecar06 with dissolve
    jn "Here we are."
    mc "Oh... Already?"
    jn "Uh-huh."
    scene 10janecar07 with dissolve
    "Soon she parked the car and you got out."
    mc "{i}Hmm. I haven't been in the area much.{/i}"
    mc "So what did we come here for?"
    jn "Come on, you'll see."
    mc "Okay."
    stop music fadeout 3.0
    scene black with fade
    "Few minutes later."
    scene 10janedate01 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "I don't know what this place is yet, but it's quite spacious."
    jn "Yeah, there's a lot of room. I'll show you all of it soon."
    jn "And now..."
    scene 10janedate02 with dissolve
    jn "Welcome to your private spa for this evening!"
    jn "A few times a month, I come here with Julia and a few other friends."
    jn "But this time I thought it would be nice to change it up and come here with you."
    scene 10janedate03 with dissolve
    mc "I must say it's a great idea!"
    scene 10janedate04 with dissolve
    jn "I knew you'd like it."
    jn "And since the owner of this place is a very close friend of mine, this whole place is at our disposal tonight."
    scene 10janedate03 with dissolve
    mc "It's even better this way."
    scene 10janedate05 with dissolve
    jn "Come on, I'll show you what it's all about."
    mc "Sure, let's go."
    scene 10janedate06 with dissolve
    jn "Here we have massage tables and sofas for rest."
    mc "Oh, yes, I can already imagine how we're going to use them."
    jn "Mmm... Remember that thought, we'll get back to it later."
    jn "Now, moving forward."
    scene 10janedate07 with dissolve
    jn "By the way, I heard from Julia that you're performing at some bar this weekend."
    jn "Is that true?"
    mc "Yeah, us and another band. This will be our second public gig."
    jn "How exciting."
    jn "Maybe I should come and see, too."
    if lisa_path == True or selina_path == True or anna_sex == True:
        mc "{i}Shit... Given all the circumstances, that's not a good idea.{/i}"
        mc "{i}But I can't tell her that.{/i}"
        mc "It's up to you. But I think it's best if you come to one of the next gigs."
        mc "A place where there'll be fewer drunk students, and it'll be more respectable."
        jn "Hm... Maybe you're right."
    else:
        mc "If you have some free time, that's a very good idea."
        mc "It's always nice to see familiar faces during a gig."
        jn "Hm... I'll remember that."
    jn "Okay, back to our tour."
    scene 10janedate08 with dissolve
    jn "In this room, we have a sauna."
    mc "So it's definitely gonna get hot tonight."
    jn "Hmmph... The hotter the better."
    mc "Huh. That's exactly what I wanted to hear."
    jn "Okay, let's move on."
    scene 10janedate09 with dissolve
    jn "And here we have a large pool."
    jn "And since you and I are alone here tonight, we can swim without prying eyes."
    mc "Sounds great."
    mc "{i}I think Jane said she was swimming.{/i}"
    mc "{i}I can't wait to see her here in a swimsuit... Or better yet, without.{/i}"
    scene 10janedate10 with dissolve
    mc "You know... With everything here, we should have the most relaxing vacation possible."
    jn "Oh, I really hope so."
    scene 10janedate11 with dissolve
    "Jane came closer to you."
    jn "Also, I hope that after a standard massage, swimming and steaming, we will move on to more intimate means of relaxing."
    mc "I like the way you think."
    jn "Yes..."
    scene 10janedate12 with dissolve
    "Jane gently kissed you on the cheek."
    scene 10janedate13 with dissolve
    jn "Now you can go to the locker room and get changed."
    jn "I'll meet you in the sauna in five minutes."
    mc "Deal."
    stop music fadeout 3.0
    scene black with fade
    "One minute later."
    scene 10janedate14 with dissolve
    mc "{i}Jane did a pretty good job of finding us this place and making the evening as good as possible.{/i}"
    scene 10janedate15 with dissolve
    mc "{i}I guess I should do her a favor in return and make this evening truly memorable.{/i}"
    scene 10janedate16 with dissolve
    mc "{i}Well, I'm determined to do my best.{/i}"
    scene black with fade
    "A few minutes later."
    scene 10janedate17 with dissolve
    play music "music/Maxim Nick - Smooth Light.ogg"
    "You were sitting in the sauna waiting for Jane."
    mc "{i}She's not in much of a hurry.{/i}"
    "{cps=15}...{/cps}"
    scene 10janedate18 with dissolve
    "The sauna door slowly opened and Jane entered the room."
    mc "{i}Finally!{/i}"
    scene 10janedate19 with dissolve
    jn "Oh... You're here already."
    jn "Sorry to keep you waiting."
    mc "It's okay."
    mc "While you were gone, I added a little heat."
    mc "I hope the temperature is right?"
    jn "Yeah, I love it."
    mc "Okay, great."
    scene 10janedate20 with dissolve
    "Jane sat down next to you."
    mc "So you come here with Julia and your other friends?"
    jn "Something like that."
    jn "Usually we would gather here at the end of the work week to... Well, you know what for."
    mc "Yeah, I can guess."
    scene 10janedate21 with dissolve
    jn "But if you're worried, no, I've never been here with a guy before."
    mc "Heh. If that's true, then I'm very lucky."
    jn "Yeah, you definitely are."
    scene 10janedate22 with dissolve
    jn "Do you mind if I lie down?"
    mc "Um... Of course, no problem."
    jn "Yeah... I'll relax the muscles."
    scene 10janedate23 with dissolve
    mc "It's been a tough week, huh?"
    scene 10janedate24 with dissolve
    jn "You could say so."
    if nicole_plus == True:
        jn "There were some small problems with suppliers, but thanks to Nicole the big troubles were mitigated."
    else:
        jn "There were some problems with the suppliers, which we didn't notice until it was too late."
    jn "Although, if you don't mind, I really don't want to talk about work right now."
    jn "It's better to bring up more pleasant topics."
    scene 10janedate23 with dissolve
    mc "Pleasant topics? I'm all for it!"
    mc "You know... I think I'll lie down, too."
    scene 10janedate25 with dissolve
    mc "I haven't told you this today, but you look great."
    jn "Thank you."
    mc "Yes... And I also wanted to say that I've missed you so much since we last met."
    scene 10janedate26 with dissolve
    "Jane put her palm on yours."
    jn "That's so sweet."
    jn "I never thought I'd say this, but I missed you too."
    scene 10janedate27 with dissolve
    "Your faces slowly started approaching each other until suddenly..."
    mc "{i}Huh?{/i}"
    scene 10janedate28 with dissolve
    jn "Oh..."
    mc "{i}Good towel. Good.{/i}"
    scene 10janedate29 with dissolve
    "You slowly diverted your gaze from Jane's breast to her face."
    mc "You know, you look a lot better without a towel."
    scene 10janedate29a with dissolve
    jn "I suppose you're right."
    jn "Besides, after everything that's happened between us, I don't think we have anything to be shy about."
    mc "Yeah, screw the towels!"
    jn "Haha. That's right."
    scene black with fade
    "Few minutes later."
    scene 10janedate30 with dissolve
    "You and Jane sat naked and enjoyed the warmth of the sauna."
    jn "Ah... It's so nice here."
    mc "Yeah..."
    scene 10janedate31 with dissolve
    "In spite of your impressive self-control, you were constantly throwing hungry eyes at Jane's naked body."
    mc "{i}Jeez, looking at such beauty, it's hard to hold yourself together.{/i}"
    mc "{i}But it's too soon. It's too soon...{/i}"
    scene 10janedate32 with dissolve
    jn "I see my breasts are giving you a hard time?"
    mc "{i}Damn it, she noticed.{/i}"
    mc "Well, it's not something that bothers me... Rather, it just attracts my gaze."
    jn "Really? It attracts your gaze? Couldn't think of anything better?"
    scene 10janedate34 with dissolve
    mc "I wasn't making that up."
    mc "Your whole body..."
    mc "Fuck! How should I put this... It's so sexy that it works like a magnet for any man's eyes."
    mc "And please don't tell me you didn't know it."
    mc "You're way too smart for that."
    scene 10janedate33 with dissolve
    jn "So many compliments in such a short time..."
    jn "Be careful, or I won't be able to resist your charm."
    mc "Perhaps that's what I'm trying to do?"
    jn "Mmm... Then you're on the right path."
    mc "Well... when you put it that way, all right."
    scene 10janedate35 with dissolve
    "You got close to Jane."
    jn "Yes?"
    mc "How about a kiss?"
    scene 10janedate36 with dissolve
    "*Kiss*"
    scene 10janedate36a with dissolve
    "The small kiss was quickly gaining desire and passion."
    scene 10janedate37 with dissolve
    "..."
    scene anim134 with dissolve
    jn "Mmm..."
    mc "{i}Oh, yeah, that feels so good.{/i}"
    mc "{i}I hate to end it.{/i}"
    pause
    scene 10janedate38 with dissolve
    jn "You're a good kisser."
    mc "Thank you, you too."
    scene 10janedate39 with dissolve
    jn "Oh, you seem a little overexcited."
    mc "Yeah, well... I guess it was just a matter of time."
    scene 10janedate39a with dissolve
    jn "It's okay. Come on, let's go cool down your buddy a little bit."
    mc "Huh? What are you talking about?"
    jn "Have you forgotten? There's a huge pool waiting for the two of us."
    mc "Oh, yeah, right."
    scene 10janedate40 with dissolve
    "Jane grabbed your hand and led you with a confident look."
    mc "So you're taking me straight from the hot sauna to the cold pool?"
    jn "Yeah. And I'm sure you'll like it."
    jn "Besides, it's nice to swim naked."
    mc "I can imagine."
    stop music fadeout 3.0
    scene black with fade
    "A minute later."
    play music "music/2 - Bad.ogg"
    scene 10janedate41 with dissolve
    mc "{i}Here we are.{/i}"
    mc "{i}It's hard to imagine we're the only ones here.{/i}"
    scene 10janedate42 with dissolve
    jn "So, are you ready?"
    mc "Ready for what?"
    jn "To jump in, of course."
    mc "Oh... Then I'll be right behind you."
    jn "Well... If you say so."
    scene 10janedate43 with dissolve
    "For a few seconds, Jane concentrated on her strength."
    jn "Come on, let's do it!"
    scene 10janedate44 with dissolve
    jn "Yahooo!!!"
    play sound "music/water_splash.wav"
    scene 10janedate45 with dissolve
    "Jane entered the water so gracefully and naturally it took your breath away."
    mc "{i}What a great jump.{/i}"
    mc "{i}I knew she was a good swimmer, but I didn't know how much.{/i}"
    scene 10janedate46 with dissolve
    jn "Ahhh! That's good!"
    mc "How's the water?"
    jn "The water is great!"
    scene 10janedate47 with dissolve
    jn "Come on, join me!"
    mc "{i}She seems happy.{/i}"
    mc "Well, since you're asking..."
    scene 10janedate48 with dissolve
    "You ran a few steps and jumped into the pool."
    mc "Wahaahahaaaaa!"
    play sound "music/water_splash.wav"
    scene 10janedate49 with vpunch
    jn "Haha!"
    jn "My God, you splash like a real elephant."
    scene 10janedate50 with dissolve
    mc "Whew! You were right, this is really refreshing!"
    jn "It is."
    scene 10janedate52 with dissolve
    "You noticed Jane was starting to swim closer to you."
    scene 10janedate51 with dissolve
    mc "Hey, what are you up to?"
    jn "I don't know... I just wanted to give you a hug."
    mc "Oh, it's always a pleasure."
    stop music fadeout 3.0
    scene 10janedate53 with dissolve
    play music "music/Maxim Nick - It's okay (final).mp3"
    "Your naked bodies ended up against each other."
    mc "{i}I can feel her hot breath.{/i}"
    mc "{i}It's so hot...{/i}"
    scene 10janedate54 with dissolve
    "You felt Jane's hand touch your dick."
    scene 10janedate53 with dissolve
    jn "Looks like you're still horny."
    mc "Yeah. And I don't care."
    jn "I don't care either."
    scene 10janedate55 with dissolve
    "*Kiss*"
    mc "{i}Her breasts are pressing so tightly against my body.{/i}"
    scene 10janedate56 with dissolve
    "The girl's legs wrapped around your hips."
    mc "{i}Hell, I can't think straight anymore.{/i}"
    mc "{i}Just a little more and I'll definitely explode.{/i}"
    scene 10janedate57 with dissolve
    jn "No... It's too soon."
    mc "{i}It's like she read my mind.{/i}"
    mc "Why?"
    scene 10janedate58 with dissolve
    jn "Because..."
    stop music fadeout 3.0
    play sound "music/water_splash.wav"
    scene 10janedate59 with vpunch
    jn "We're still having fun!"
    mc "Oh, you asshole!"
    jn "Hahah! Catch me if you can!"
    scene 10janedate60 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    "For some time you were playing catch-up and just swimming in the pool."
    "It's been a lot of fun."
    scene 10janedate61 with dissolve
    "But you looked at Jane and her sexy body more than once."
    jn "All right, let's finish."
    mc "Yeah."
    scene 10janedate62 with dissolve
    "Jane slowly started to exit the pool."
    mc "{i}Oh, my God... This ass is perfect!{/i}"
    mc "{i}I don't know if she's doing it on purpose or not, but it's a low blow.{/i}"
    scene 10janedate63 with dissolve
    jn "Hey, what are you stuck in there for? Come on, let's go."
    mc "Yeah, I'm coming."
    scene 10janedate64 with dissolve
    jn "Ahh... That was awesome!"
    mc "I agree."
    mc "Since we're done with the pool, what do we do now?"
    scene 10janedate65 with dissolve
    jn "I suggest we end this evening with your amazing massage."
    mc "Oh, good choice!"
    jn "Haha. Thanks."
    scene 10janedate66 with dissolve
    mc "I'll try to give you a massage you'll never forget."
    mc "Get ready."
    scene 10janedate67 with dissolve
    jn "Mmm... Sounds very intriguing."
    jn "I can't wait to try it again."
    scene 10janedate66 with dissolve
    mc "All right then, let's go."
    stop music fadeout 3.0
    scene black with fade
    "Few minutes later."
    scene 10janemassage01 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "So you decided to end this evening with a massage."
    mc "Have you had this planned from the beginning?"
    jn "Hardly. It just seemed like the most appropriate course of action."
    jn "And didn't you like it?"
    mc "Are you kidding? I love it."
    jn "That's great."
    jn "Now let's pick one of these massage tables."
    scene 10janemassage02 with dissolve
    jn "How about this one?"
    mc "I don't know, they all look the same to me."
    jn "Yes... I guess so. But we have to choose something."
    mc "Then this one's fine."
    jn "Okay."
    scene 10janemassage03 with dissolve
    jn "I don't suppose you mind if I go first?"
    mc "Suit yourself."
    jn "Mmm... I'm all excited."
    scene 10janemassage04 with dissolve
    "Covering herself with a towel, Jane lay on the table."
    mc "Hey, you were just naked, so why'd you close up with a towel now?"
    jn "So you'd be a little less distracted."
    mc "Ha! Fair enough."
    mc "Then I'm starting?"
    jn "Yes, I'm ready."
    scene 10janemassage05 with dissolve
    "First off, you decided to stretch the girl's shoulders."
    jn "Ah... Yes... It's so good..."
    scene 10janemassage06 with dissolve
    "You gently moved your hands down and started massaging her back."
    jn "Mmmm..."
    scene 10janemassage07 with dissolve
    "You moved down further and started massaging Jane's feet and legs."
    jn "Ohh... I don't know how you do it, but your hands are amazing."
    scene 10janemassage08 with dissolve
    "Gently started rubbing her thigh muscles."
    stop music fadeout 3.0
    jn "..."
    scene 10janemassage09 with dissolve
    "Then you moved the towel and started a buttock massage."
    jn "Hey, why are you-"
    mc "Shh... It's okay. Just lie back and enjoy."
    jn "Um... Okay..."
    scene 10janemassage10 with dissolve
    play music "music/15 - Deep Mood.ogg"
    "Your hands were confidently massaging Jane's ass."
    scene anim135 with dissolve
    jn "Aaah.... Mmmm...."
    mc "{i}She's not even trying to muffle those moans and just enjoying the moment.{/i}"
    mc "{i}I envy her a little.{/i}"
    pause
    scene 10janemassage10 with dissolve
    "You stopped."
    scene 10janemassage11 with dissolve
    mc "You know, to continue the massage, you have to flip over."
    mc "{i}I don't think she'll say no.{/i}"
    scene 10janemassage12 with dissolve
    jn "If it's even a quarter as nice as what you were doing, I don't see the problem."
    mc "Believe me, it's even better."
    scene 10janemassage13 with dissolve
    jn "Oh... Then get started."
    mc "Fine, I'll start with your chest."
    jn "..."
    scene 10janemassage16 with dissolve
    "You moved your hands to Jane's breast."
    jn "Mmm..."
    scene 10janemassage15 with dissolve
    mc "{i}Her boobs are so big, they barely fit in my hands.{/i}"
    mc "{i}And they're also incredibly soft.{/i}"
    scene 10janemassage14 with dissolve
    "..."
    scene anim136 with dissolve
    jn "Um... Yeah... Please continue..."
    mc "{i}Judging by her posture, she's already very horny.{/i}"
    mc "{i}Maybe I should go a little further.{/i}"
    pause
    scene 10janemassage17 with dissolve
    mc "I see you love my massage."
    mc "I hope you'll agree if we make it even more intimate?"
    scene 10janemassage18 with dissolve
    jn "You didn't have to ask."
    jn "Just do whatever you think is right."
    scene 10janemassage17 with dissolve
    mc "That's what I wanted to hear."
    scene 10janemassage19 with dissolve
    "The next moment, your hands took up Jane's two most sensitive areas."
    scene anim137 with dissolve
    jn "Ohhhhh! This is... This is so nice!"
    jn "Mmm... Don't stop!"
    mc "{i}Yeah, I'm doing it right.{/i}"
    mc "{i}Now let's do it a little differently...{/i}"
    pause
    scene 10janemassage20 with dissolve
    "You flipped a girl on her stomach and kept fucking her with your fingers."
    scene anim138 with dissolve
    jn "Aaahhh... Aaaahhh.... Aaaahhh...."
    jn "Yes, that's it, more!!! More, [mc]!!!"
    jn "I almost... almost..."
    pause
    scene 10janemassage21 with flash
    jn "Yeeeessss!!!"
    scene 10janemassage21 with flash
    jn "CUMMING!!!!"
    scene 10janemassage22 with dissolve
    "Totally exhausted, Jane was melting on her stomach and breathing heavily."
    jn "Haa... Haa... Haa..."
    scene 10janemassage23 with dissolve
    jn "It was... I just don't have the words."
    mc "Yeah, I can see that."
    jn "Goddamn it, after that I still have to do you a favor in return!"
    scene 10janemassage24 with dissolve
    "As she gathered her strength, Jane lifted up and grabbed your cock with her free hand."
    mc "{i}Whoa... That was unexpected!{/i}"
    scene anim139 with dissolve
    "And then she started jerking you off with smooth strokes."
    mc "{i}It's finally time for pleasure.{/i}"
    mc "{i}Ooh... I must admit, she knows how to make a man feel good.{/i}"
    jn "Come closer, I'll show you what I can do."
    mc "Now that's what I'm talking about it. How could I say no to you?"
    pause
    scene 10janemassage25 with dissolve
    "Jane's hot tongue touched the head of your dick."
    jn "You won't forget this blowjob for a long time."
    mc "{i}God, I'm all excited.{/i}"
    scene anim140 with dissolve
    "You put your cock in the girl's mouth and started moving."
    jn "Mmmmmhhhh.... Mmmmmhhhh.... Mmhhhhh..."
    mc "Yeah, baby... You're really good..."
    pause
    scene 10janemassage26 with dissolve
    "With your free hand, you reached for the girl's pussy."
    mc "Don't think I forgot about you!"
    scene 10janemassage27 with dissolve
    jn "Mmmmmhhhh! Mmmmmhhhh! Mmhhhhh!"
    mc "{i}Oohh... She started sucking even harder!{/i}"
    mc "Now, let's try this..."
    scene 10janemassage28 with dissolve
    "You turned Jane over on her back."
    mc "Yeah, baby, you're doing a great job... Don't stop!"
    jn "Mmmnn... Mnum...."
    scene 10janemassage29 with dissolve
    "A few seconds later, Jane sat before you and jerked you off again."
    scene anim141 with dissolve
    jn "You look like you can't wait to put that fat dick in my pussy."
    mc "Oh... Baby, don't tease me."
    jn "Don't worry, just a little more and you'll have it."
    mc "{i}You don't have to tell me, I already know.{/i}"
    pause
    scene 10janemassage30 with dissolve
    mc "{i}I can't hold it anymore, it's time to fuck this busty beauty.{/i}"
    mc "Baby, get on the table."
    jn "Mmmm... Okay."
    scene 10janemassage31 with dissolve
    "You touched Jane's wet pussy."
    mc "Oh... I've wanted this for a long time."
    jn "Yes... Me too..."
    jn "Now put your cock in!"
    scene 10janemassage32 with vpunch
    jn "Aaahhh!"
    mc "{i}Oh, yeah! It's so good inside her!{/i}"
    scene anim142 with dissolve
    "You started moving."
    jn "Yes, [mc]! Take me..."
    mc "{i}It's so exciting when she moans like this.{/i}"
    jn "There you go... Don't hold back, fuck me harder!"
    pause
    scene 10janemassage33 with dissolve
    "..."
    scene anim143 with dissolve
    mc "Oohh... Yeah, baby... There you go!"
    jn "Aaaahh! Aaaahhh! Aaaahhh!"
    mc "{i}Shit... This table isn't very comfortable.{/i}"
    pause
    scene 10janemassage34 with dissolve
    "While continuing to fuck Jane, you moved your legs to the floor."
    mc "{i}Yeah, that's much better.{/i}"
    scene 10janemassage35 with dissolve
    "You let go of the girl's legs and pulled her closer to you."
    scene anim144 with dissolve
    jn "Aaaahh! Aaaahhh! Aaaahhh!"
    mc "{i}Her pussy is awesome. I just can't stop!{/i}"
    pause
    scene 10janemassage36 with dissolve
    jn "Aah! A little more, [mc]! A little more and I'll..."
    mc "Yeah, me too!"
    scene 10janemassage38 with dissolve
    "..."
    scene anim145 with dissolve
    jn "Mmm... Mmm.... Mmm..."
    mc "{i}I can't hold it anymore. Where should I cum?{/i}"
    pause
    menu:
        "Cum inside":
            mc "{i}I want to cum inside her!{/i}"
            mc "Baby, I'm gonna..."
            "You started cumming right into Jane's hot pussy."
            scene 10janemassage37 with flash
            mc "Yeeesss!!!"
            scene 10janemassage37 with flash
            mc "There you go!!!"
            scene 10janemassage39 with dissolve
            jn "Ooh... I see you decided not to hold back."
            mc "I'm sorry, but it was hard to resist."
            jn "Uh-huh. That's what I thought."

        "Cum outside":
            mc "{i}I want to cum right on her body!{/i}"
            mc "Baby, I'm gonna..."
            scene 10janemassage40 with dissolve
            "You turned Jane on her back and started to cum right on her."
            scene 10janemassage41 with flash
            mc "Yeeesss!!!"
            scene 10janemassage41a with flash
            mc "There you go!!!"
            scene 10janemassage41a with dissolve
            jn "I see you're pleased with yourself."
            mc "Huh. Didn't you like it?"
            jn "You know I liked it."
            mc "Uh-huh. I know."

    stop music fadeout 3.0
    scene black with fade
    "Soon you cleaned yourself up and sat down on the nearby sofas."
    scene 10janemassage42 with dissolve
    play music "music/8 - Intro Music.ogg"
    jn "So... What do you say to our date?"
    jn "Did you like it?"
    mc "You kidding? I loved it!"
    mc "I'm sure it's gonna be hard for me to surpass."
    scene 10janemassage43 with dissolve
    jn "Yeah, you'll have to do your best."
    "..."
    mc "{i}Looks like she's okay with more dates.{/i}"
    mc "Does this mean that you and I are now officially dating?"
    scene 10janemassage44 with dissolve
    "Jane moved closer to you and touched your face."
    jn "I've been thinking about it for a long time, and I'm telling you yes."
    jn "You and I are now officially dating."
    mc "{i}I did it after all!{/i}"
    mc "You wouldn't believe how glad I am to hear that."
    scene 10janemassage46 with dissolve
    "*Kiss*"
    jn "Mmmm..."
    scene 10janemassage45 with dissolve
    jn "Let's hope this works out."
    mc "You can count on me. I'll do everything I can to make sure it does."
    jn "Yes, me too."
    $ renpy.end_replay()
    if not persistent.day10jane:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day10jane = True        
    stop music fadeout 3.0
    scene black with fade
    "After sitting for a while with each other, you said goodbye to Jane and went home."
    "You had a weekend ahead of you."

    jump day11_start
