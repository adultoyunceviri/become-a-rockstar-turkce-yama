
label day05_start:
    scene black with fade
    "Next morning."
    play music "music/6 - Positive Mood.ogg"
    scene 5father01 with dissolve
    "As planned last night, first thing in the morning you went to your father's company."
    mc "{i}I need to solve this problem before it goes too far.{/i}"

    if father_enemy == True:
        mc "{i}He crossed the line this time, and I'm not going to let him get away with it.{/i}"
    else:
        mc "{i}It would be better this time around if father was more compliant, because our relationship is not on the best of terms as is.{/i}"

    "Ahead at the reception desk you noticed an old friend, an employee of your father's company - Donna."
    "You know as a matter of fact that this girl had been working here for almost four years and knows everything that's going on here."
    scene 5father02 with dissolve
    "{color=#BC8F8F}Donna{/color}" "Well, well, look who I see in front of me! Is that [mc]?"
    mc "{i}It seems she's in a good mood as usual. I don't know how she does it, considering who the fuck she's working for...{/i}"
    "{color=#BC8F8F}Donna{/color}" "Hey, why haven't you visited me for so long? I miss you, by the way."
    "{color=#BC8F8F}Donna{/color}" "I hope you're not in trouble."
    mc "Heh. Good to see you too, Donna. And I'm fine, more or less."
    mc "Thanks for asking."
    scene 5father03 with dissolve
    "{color=#BC8F8F}Donna{/color}" "Well, that's great! In that case, is there anything I can help you with?"
    mc "Yeah, I was wondering if my dad was here."
    scene 5father03a with dissolve
    "{color=#BC8F8F}Donna{/color}" "Hm..."
    "{color=#BC8F8F}Donna{/color}" "As far as I know, he should be at a meeting now."
    scene 5father03 with dissolve
    "{color=#BC8F8F}Donna{/color}" "But I don't think it'll last long. You can wait in his office."
    mc "Thanks, Donna, that's what I'll do."
    scene 5father04 with dissolve
    "Without wasting time, you took the Elevator and immediately went to his office."
    mc "{i}It'll be over soon enough...{/i}"

    stop music fadeout 3.0
    play music "music/8 - Intro Music.ogg"

    scene 5father05 with dissolve
    "When you came to the office, you immediately noticed your father's assistant."
    mc "{i}It seems that Donna has already managed to warn her. I could have guessed it myself.{/i}"
    mc "{i}But I should bear in mind that Donna doesn't make friends with just anyone. I wonder how Nicole earned her trust...{/i}"
    scene 5father06 with dissolve
    n "[mc]."
    n "I hope you didn't come here because of what I told you last night."
    mc "Well, actually, I came here because of that."
    "Nicole came closer to you."
    scene 5father07 with dissolve
    n "Um... This is not your best decision."
    "The girl carefully studied your face, giving you the impression that she can read your thoughts."
    n "It seems that you're determined."
    mc "That's right. I'd better get this over with before something goes wrong."
    mc "Of course, I don't want you to get in trouble for this, but my life is more important to me than yours."
    scene 5father08 with dissolve
    n "I understand..."
    n "Is there any way I can convince you to not talk to your father about this?"
    mc "{i}Although she doesn't show it, she seems nervous.{/i}"
    mc "{i}However, that's not surprising. This case is directly related to her future career.{/i}"
    mc "I know this isn't the best news for you, but no, I've already decided."
    scene 5father08a with dissolve
    n "I see."
    n "In that case, do as you like."
    scene 5father09 with dissolve
    "Without another word, Nicole left you alone."
    "..."
    mc "{i}And why do I feel like an asshole even though I'm completely innocent here?{/i}"
    mc "{i}Okay, I gotta get this over with.{/i}"

    stop music fadeout 3.0
    play music "music/15 - Deep Mood.ogg"

    scene 5father10 with dissolve
    "You went into the office and looked around."
    mc "{i}Nothing has changed here since my last visit.{/i}"
    mc "{i}Although that shouldn't be surprising, since it was only a month ago.{/i}"
    mc "{i}Oh, just think, it's only been a month of independent life, yet it feel like it's been a hundred years.{/i}"
    scene 5father11 with dissolve
    "Soon you sat down at your father's workplace and began to wait for him."
    mc "{i}Well, at least the chair's comfortable.{/i}"
    stop music fadeout 3.0
    scene black with fade
    "Some time later."

    play music "music/8 - Intro Music.ogg"

    scene 5father12 with dissolve
    f "[mc]? You didn't tell me you were coming over."
    f "What are you doing here?"
    mc "Well, it seems that showing up at each other's workplaces without an invitation is a family habit."
    f "That's possible. But you didn't answer my question."
    f "Given your natural stubbornness, I doubt you've decided to accept my offer to work for this company."
    f "And by the looks of you, you're not here to ask me for money."
    scene 5father13 with dissolve
    f "So I repeat my question, why are you here?"
    mc "It's simple. I want you to stop meddling in my affairs once and for all."
    scene 5father13a with dissolve
    f "Meddling in your Affairs? What do you mean?"
    mc "Come on! You don't have to act surprised! I'm well aware of your clandestine manipulation of my personal life."
    mc "And you know what... That's low even by your standards."
    mc "You gave me your word that you would let me live my life if I could, and now you're breaking it."
    mc "Not to mention the fact that you forbade that rest of the family to communicate with me."
    scene 5father13 with dissolve
    f "You don't understand..."
    mc "Oh no, I understand perfectly!"
    mc "When I'm just starting to get on with my life, you show up out of nowhere and try to mess it all up."
    mc "I just can't understand, is this how things are handled in our family?"
    scene 5father13a with dissolve
    f "..."
    scene 5father14 with dissolve
    f "How did you find out about this?"
    mc "Are you for real? Is that all you care about?"
    f "Of course not! But will my excuses help either one of us now?"
    mc "Well, at least I agree with you on something today. You can keep your excuses to yourself. You did what you thought was right. I get that."

    if father_enemy == True:
        mc "And now I'm telling you to never interfere in my life again."
        mc "And if you don't stop, I'm gonna give you a life where your personal and business's reputation goes down so fast, you won't even have time to figure out why it happened."
        mc "I hope we understand each other."
    else:
        mc "And now I'm telling you, if you try that trick again, you and I are going to be in big trouble."
        mc "I wouldn't dare make things as simple as they are this time. I hope we understand each other."

    f "I hear you."
    mc "That's great. I'm gonna go now..."
    scene 5father14a with dissolve
    f "Wait a minute."
    mc "What is it?"
    f "Before you go, I want to clarify something."
    scene black with fade
    "Suddenly, your father called his assistant into the office."
    scene 5father15 with dissolve
    n "Sir, you wanted to see me?"
    f "Yes I did..."
    f "And I think you already know what's going on here."
    n "..."
    f "Of course you're smart enough to know that."
    scene 5father16 with dissolve
    f "You're fired."
    f "I want you and your things out of this building by tonight."
    f "You understand me?"
    scene 5father17 with dissolve
    "You noticed how for a brief moment the mask of indifference on Nicole's face cracked."
    mc "{i}Even though she knew all the risks she'd taken yesterday, the news had clearly stunned her.{/i}"
    n "I..."
    scene 5father17a with dissolve
    n "Yes, sir... I understand you."
    f "Good, now leave us."
    scene 5father18 with dissolve
    "Nicole left, leaving you alone with your father."
    mc "{i}Holy shit! I'm sure he did it in front of me for a reason.{/i}"
    mc "{i}He wants me to feel guilty? Or just wants to see my reaction?{/i}"
    mc "{i}But then how should I react?{/i}"

    menu:
        "Be indifferent":
            scene 5father19a with dissolve
            mc "I don't really understand what you wanted me to see with this scene."
            mc "If you still don't understand, I spit on you, on this girl, and on your whole business."
            scene 5father19 with dissolve
            f "Your composure proves once again that you are perfect for our company."
            f "Here you are waiting for impressive results, why don't you understand?"
            mc "No interest."
            f "Eh... Okay, I understand."
            f "I won't interfere in your life anymore. This time for sure."
            f "But remember, my offer still stands."
            mc "Yeah, whatever."
            scene black with fade
            "You left your father's office and walked away from this building as quickly as possible."

        "{color=#66FF33}Stand up for Nicole":
            $ nicole_plus = True
            scene 5father19a with dissolve
            mc "Why the fuck are you acting like an asshole? What's wrong with this girl?!"
            scene 5father19 with dissolve
            f "Hm? You really don't understand why I did it?"
            mc "{i}Sure I do...{/i}"
            f "She either told you my intentions, which means she betrayed my trust. Or she couldn't handle a simple errand, which is why you found out about all this."
            f "Me, as her employer, find neither option as satisfactory."
            scene 5father19a with dissolve
            mc "{i}Yes... Everything is more than clear. She's either incompetent to him or he can't trust her.{/i}"
            mc "{i}And he absolutely doesn't care that this whole situation and all his instructions regarding me are completely inappropriate.{/i}"
            mc "{i}However, I don't care. I don't want to stay here any longer.{/i}"
            scene 5father19 with dissolve
            f "[mc] I won't interfere in your life anymore. This time for sure."
            f "But I want you to know that my offer still stands."
            mc "Yeah, whatever."

    stop music fadeout 3.0

    if nicole_plus == False:
        jump day05_chat
    else:
        jump nicole_day05


label nicole_day05:
    play music "music/2 - Bad.ogg"
    scene 5father20 with dissolve
    "Walking along one of the corridors, to your surprise you saw something that made you slow down."
    mc "{i}Nicole? Looks like she's packing.{/i}"
    mc "{i}Damn, she's so unlucky to have run into our family. If she worked with normal people, none of this would have happened...{/i}"
    scene 5father21 with dissolve
    "Suddenly, you had an interesting thought in your head."
    mc "{i}But I know a person who has her own company and appreciates hard work.{/i}"
    mc "{i}The only question is, is there anything I can do about it?{/i}"
    stop music fadeout 1.0
    play sound "music/knock.mp3"
    scene black with fade
    "Knock knock!"
    scene 5father22 with dissolve
    play music "music/2 - Bad.ogg"
    n "[mc]? What are you doing here?"
    mc "Can I talk to you about something? It won't take long."
    n "I don't want to talk to you right now. Not with you, not with your father, not with anyone else."
    mc "{i}She seems angry... But that's not surprising.{/i}"
    mc "I understand why you're angry, but you always seemed rational enough to not get emotional. Especially when this conversation is about your future career."
    scene 5father23 with dissolve:
        ypos -0.25
        ease 6 ypos 0.0
    "Nicole sat on the edge of the table and looked at you with her completely indifferent look."
    n "All right, I'm listening."
    mc "{i}Um... She doesn't seem to have much faith in me saying something important.{/i}"
    scene 5father24a with dissolve
    mc "First of all, I want to say that I don't like this whole situation any more than you do. But I think I may have a less painful solution."
    n "..."
    mc "Okay, I'll go straight to the point."
    mc "The thing is, I'm on good terms with my sister, Julia. And she, along with her friend Jane, have a company-"
    scene 5father24 with dissolve
    n "Yeah, I know who they are and what they do."
    scene 5father24a with dissolve
    mc "Well, that makes things easier."
    mc "If you want, I can put in a good word for you."
    mc "You have to admit, all things considered, it's a good offer. And Julia and Jane are good leaders."
    scene 5father24 with dissolve
    n "Okay. What do I owe you for that?"
    mc "What makes you think I'm gonna ask you for something in return?"
    n "Because I wasn't born yesterday and I understand how everything works in this world."
    n "So, what do I owe you for this?"

    menu:
        "You don't owe me anything":
            $ goodpoint += 1
            $ RPn += 2
            mc "You got into all this trouble because of me and my dad, so it's the least I can do for you."
            n "Really..."
            scene 5father25 with dissolve
            "Nicole stretched out her hand, indicating that she accepted your offer."
            n "Well, if that's true, I want to thank you. Sincerely."
            n "It's very rare in our time to meet anyone with such respectability."
            scene 5father26 with dissolve
            mc "Any time."
            "..."
            mc "{i}Oh, I can already feel how Jane and I will have a very interesting conversation soon...{/i}"

        "You'll owe me a favor":
            $ badpoint += 1
            $ nicole_favor = True
            mc "Nothing at the moment, but you owe me a favor in the future."
            n "Yeah, that's what I was saying."
            scene 5father27 with dissolve
            "Nicole came right up to you, and then she put her hand on your shoulder."
            n "You know, maybe your dad's right after all. You really have a business acumen."
            n "Besides, you're the only one who came out of this situation today as a winner."
            scene 5father28 with dissolve
            n "But don't worry, I actually like that trait in men."
            n "I look forward to returning the favor."
            mc "Yes... Me too..."

    stop music fadeout 3.0

    scene black with fade
    "Few hours later."

    play music "music/8 - Intro Music.ogg"

    scene 5janework01 with dissolve
    "For a while, you waited for Jane to finish her work to be able to listen to you."
    jn "So... I'm done. Can you tell me what's so urgent that you wanted to talk to me about?"
    mc "First of all, thank you for listening to me."
    scene 5janework02 with dissolve
    jn "That's not a problem. Nice to see a new face in the midst of all the bustle of work."
    jn "But let's get to the point. I don't have as much time as I'd like..."
    mc "Yeah, I noticed that already."
    mc "But you could say that's part of why I'm here."
    jn "Really?"
    mc "Yeah..."
    scene black with fade
    "You briefly told Jane the story of Nicole and waited for her reaction."
    scene 5janework02b with dissolve
    jn "Wait a minute... Let me see if I understand you correctly. You're asking me to hire this girl to work for Julia and me?"
    mc "Something like that."
    mc "She used to work for my dad, and he, as you know, doesn't hire anybody. Besides, with your crazy pace of work, you could use a good assistant."
    jn "Look, [mc], this isn't a charity office, and we don't hire just anybody. You understand that?"
    scene 5janework02a with dissolve
    mc "I'm not asking you to hire her. Just get her an interview."
    mc "If you like her, you'll hire her, and if you don't... If not, then the hell with her."
    scene 5janework02c with dissolve
    jn "Why do I need all this trouble?"
    mc "Because she's good, and she's undeservedly out of a job. And thanks to the efforts of my father, she got into the black list of employers."
    scene 5janework02b with dissolve
    jn "Exactly!"
    jn "Even if I miraculously take this girl to work for me, your father won't let it go. With his connections, he'll quickly find a way to ruin my life..."
    mc "Nothing like that. If your company hires her, he won't do anything to you."
    scene 5janework03 with dissolve
    jn "Explain what you mean."
    mc "Sure."
    scene 5janework02a with dissolve
    mc "It's part of your company, but it's also Julia's, right?"
    jn "Naturally."
    mc "That's it. My father would never go against his daughter's company."
    scene 5janework02b with dissolve
    jn "But he went against you."
    scene 5janework02a with dissolve
    mc "This whole situation with me was much more complicated ... But he treats Julia well. I would even say very well."
    mc "She, like all my other relatives, followed in his footsteps. He respects that."
    mc "In addition, the family business, which for him is above all."
    scene 5janework02c with dissolve
    jn "Um... Sounds reasonable."
    mc "Yes."
    mc "And if you give Nicole a chance, I'll be sure to find a way to thank you."
    scene 5janework02 with dissolve
    jn "Oh, so you're gonna owe me? Now it's getting a lot more interesting."
    mc "I knew you couldn't resist that argument."
    scene 5janework02d with dissolve
    jn "Ha! You think too highly of yourself, kid."
    jn "However, tell this girl to come visit me. I'll see if she's worth the effort..."
    mc "Thanks. You won't regret this."
    jn "Hope so."
    "Immediately after those words, Jane stood up and walked over to you."
    scene 5janework04 with dissolve
    jn "Since you're here, you'll be interested to know that Julia's coming back from her trip in three days."
    mc "{i}Wow... I haven't seen her in a while. It'll be necessary to see her.{/i}"
    mc "Three days? I'll keep that in mind. Thanks for telling me."
    jn "Don't mention it."

    if jane_massage == True:
        scene 5janework05 with dissolve
        jn "And [mc]... I hope you're smart enough to keep our massage sessions a secret."
        mc "{i}Not that I'm going to tell her, but being extra careful doesn't hurt.{/i}"
        mc "Of course, you can count on me."
        jn "Good."
        mc "Although you know... I'm not averse to a couple more sessions like that."
        scene 5janework06 with dissolve
        jn "Huh!"
        jn "I'll think about your offer."
        jn "And now it's time for you to go."
        mc "You're right. See you!"
    else:
        jn "And now it's time for you to go."
        mc "You're right. See you!"
    stop music fadeout 3.0
    jump day05_chat


label day05_chat:
    play music "music/7 - Just Happy.ogg"
    scene black with fade
    "As soon as you got home, there was a video call on your laptop."
    scene stream00 with dissolve
    mc "{i}Hm?{/i}"
    mc "{i}Video conference? Lisa, Jacob and Jade online?{/i}"
    mc "{i}That's interesting.{/i}"
    scene 5chat01 with dissolve
    mc "Hey, guys!"
    mc "What's the occasion?"
    scene 5chat04 with dissolve
    j "Hey, man! You came just in time!"
    j "We talked about renting a new rehearsal room."
    scene 5chat02 with dissolve
    ls "The thing is, Jade's aunt found us a good option, but we need to see it today."
    scene 5chat01 with dissolve
    mc "So what's the problem? Let's go see it."
    scene 5chat03 with dissolve
    jd "They can't. Everyone's busy."
    scene 5chat05 with dissolve
    mc "Ha! So I understand correctly that you want me to go?"
    scene 5chat05a with dissolve
    ls "Please please please!"
    ls "You know, if I could, I'd love to go."
    scene 5chat05b with dissolve
    j "Man, I wouldn't have a problem going either, but I just can't today."
    mc "All right. I don't mind."
    scene 5chat05 with dissolve
    mc "Jade, you with me?"
    jd "Yes."
    mc "Then, if we like the room, I'll send you a photo and you tell us whether we take it or not."
    j "I agree!"
    jd "[mc] I'll give you the address."
    mc "Okay, shoot..."
    "Jade started to dictate it to you."
    stop music fadeout 3.0
    jump new_rep_day05


label new_rep_day05:
    play music "music/10 - Street's.ogg"
    scene black with fade
    "Some time later."
    "Like you agreed with Jade, you went to the address she gave you."
    scene 5newrep01 with dissolve
    mc "{i}Um... It takes a little longer to get here, but the area is much friendlier.{/i}"
    mc "{i}I wonder how things are with the room itself.{/i}"
    mc "{i}This time I would like to choose something more decent.{/i}"
    scene 5newrep02 with dissolve
    mc "{i}Oh, there's Jade!{/i}"
    mc "{i}I hope she wasn't waiting long for me.{/i}"
    scene 5newrep03 with dissolve
    jd "[mc]."
    mc "Hey, Jade. I hope I'm not too late."
    jd "It's okay. I just came."
    mc "Nice."
    mc "I didn't know you smoked, by the way."
    jd "What?"
    scene 5newrep03a with dissolve
    jd "Oh, this?"
    jd "Stupid habit, I can't get rid of it."
    "Jade threw the cigarette and again looked at you."
    scene 5newrep04 with dissolve
    jd "Come on, we don't have much time."
    mc "Of course I'm right behind you."
    scene black with fade
    "Few minutes later."
    scene 5newrep05 with dissolve
    mc "{i}So this is the room aunt Jane found us.{/i}"
    mc "{i}To me it looks very good!{/i}"
    scene 5newrep06 with dissolve
    jd "What do you think?"
    mc "I like it."
    jd "Yep. And only twice as expensive as your last rehearsal room."
    mc "Well, for a neighborhood like this, it's almost free. Your aunt found us a good deal."
    jd "However, if we take it, we'll have to furnish it ourselves."
    mc "I don't think that's gonna be a problem."
    mc "Maybe you haven't heard, but Lisa is studying to be a designer. Surely she'll not give up such practices."
    jd "I understand."
    "..."
    mc "Wait till I send some pictures to the guys? They asked me."
    jd "Yes. I'll wait by the window."
    mc "Okay."
    scene black with fade
    "After taking some quick photos, you sent them to Lisa and Jacob."
    "You weren't surprised when they said they were okay with it, too."
    scene 5newrep07 with dissolve
    "Meanwhile, you turned your attention back to Jade."
    mc "{i}Hmm... She looks pretty good today.{/i}"
    mc "Jade."
    "..."
    mc "Jade!"
    scene 5newrep07a with dissolve
    jd "What?"
    jd "Sorry, I was thinking."
    mc "Never mind."
    mc "Good view?"
    scene 5newrep07b with dissolve
    jd "Yes... Very good."
    scene 5newrep07a with dissolve
    jd "I assume you're done here?"
    mc "Yep."
    jd "What did the others say?"
    mc "They loved it. I think this place is good for us."
    jd "Okay, I'll pass on your words to aunt and take care of the paperwork."
    mc "Awesome! How soon can we bring our stuff here?"
    jd "I think tomorrow."
    mc "Okay, good."
    mc "Until tomorrow, then."
    jd "Yeah."
    scene 5newrep07b with dissolve
    jd "You go, I'll stay here a little longer."
    mc "Whatever you say."

    stop music fadeout 3.0
    play music "music/3 - Dream With U.ogg"

    scene black with fade
    "You left Jade alone with her thoughts and you went outside."
    "PIP-PIP!!!"
    scene 5nextdoor00 with dissolve
    mc "{i}Um... Call from... Selina?{/i}"
    mc "{i}Wow.{/i}"
    scene 5nextdoor00a with dissolve
    mc "Hello."
    s "Hey, it's me..."
    mc "Hey."
    s "I was coming home from work and I thought of you."
    s "Do you want to meet up, maybe take a little walk?"
    menu:
        "{color=#66FF33}Yes":
            mc "Sure, why not?"
            s "Wonderful!"
            s "Then will you pick me up in about an hour?"
            mc "Deal."
            stop music fadeout 3.0
            s "Okay, I'll wait for you."
            jump selina_day05

        "No":
            mc "Sorry, I'm busy right now."
            s "Oh... I understand..."
            s "In that case, I'm sorry to bother you."
            mc "It's okay. Bye."
            s "Bye."
            scene black with fade
            "That same night, you arranged for Jacob to meet you the next morning and take things from the last rehearsal room to the new one."
            "Another day awaits you."
            stop music fadeout 3.0
            jump newreproom_day05

label selina_day05:
    play music "music/6 - Positive Mood.ogg"
    scene black with fade
    "Some time later."
    "You went to Selina's apartment and rang the doorbell."
    play sound "music/doorbell.wav"
    scene 5nextdoor02 with dissolve
    "To your surprise, instead of Selina, Rosa opened the door."
    r "Oh, [mc], good to see you. You came for Selina?"
    mc "Ummm.... Yeah, actually, we agreed I'd pick her up."
    scene 5nextdoor01 with dissolve
    r "Mmm... Are you going on a date with my daughter?"
    menu:
        "You're just friends":
            $ RPr += 2
            mc "Nothing like that. We're friends."
            r "Whatever you say. After all, it's up to you to decide what kind of relationship you have."

        "You have a date":
            mc "I guess you could say that."
            r "Well, I'm glad she's dating such a nice young man."
            mc "Ahem... Yes, thanks."

        "{color=#66FF33}You have a complicated relationship":
            $ RPr += 2
            mc "To tell you the truth, we have a very complicated relationship."
            mc "Perhaps even so much so, that I don't know what to properly call it."
            r "That youth..."
            r "I hope that everything will become clear soon."
            mc "Yeah, I hope so, too."

    "..."
    mc "So, can you call Selina?"
    scene 5nextdoor01a with dissolve
    r "Sorry, but you're out of luck, you just missed each other by a minute."
    mc "Oh... Really."
    r "Don't worry, she should be back soon."
    r "You can go inside and wait for her."
    mc "{i}I don't know why, but I'm a little uncomfortable being alone with Rosa...{/i}"
    mc "{i}But it would be wrong to refuse her offer.{/i}"
    mc "Yeah, thanks..."
    scene 5nextdoor03 with dissolve
    mc "Can I ask where Selina went exactly?"
    r "I think she left something in her car and went to get it."
    r "I thought it was a phone?"
    mc "Oh, okay."
    scene 5nextdoor04 with dissolve
    r "Please sit down."
    mc "Sure."
    scene 5nextdoor05 with dissolve
    r "So, [mc], how are you? How about your health?"
    mc "{i}Ooh... So many questions.{/i}"
    mc "My health? Why are you asking that?"
    scene 5nextdoor07 with dissolve
    r "The last time I saw you, you ran off so suddenly, citing your poor health, which is why I was worried about you."
    scene 5nextdoor05 with dissolve
    mc "Oh that!"
    mc "Thanks for asking, I'm fine."
    r "That's very good."
    "..."
    mc "How are things going with you? I hope you're all right too."
    scene 5nextdoor07a with dissolve
    r "Everything is complicated... But I don't like to complain about my life."
    mc "Did something happen to you?"
    scene 5nextdoor07b with dissolve
    r "At the moment, Selena's father and I are going through a divorce. That's the reason I'm here now."
    mc "Sorry to hear."
    scene 5nextdoor05 with dissolve
    r "Don't worry, our marriage has outlived its usefulness. It's time to try something new."
    mc "{i}Is it me, or did that sound a little ambiguous?{/i}"
    mc "Is there anything I can help you with?"
    r "Of course, maybe you can..."
    scene 5nextdoor06 with dissolve
    "Rosa laid her soft palm on you."
    mc "{i}Whoa whoa! What's that?!{/i}"
    "You felt like a little mouse in front of a snake that slowly began to take you in."
    scene black with fade
    "Before you could react, the sound of a turning lock rang through the front door, and Selina appeared on the doorstep."

    stop music fadeout 3.0
    play music "music/4 - Ready to Drive.ogg"

    scene 5nextdoor08 with dissolve
    s "[mc]! You came!"
    s "Sorry to keep you waiting."
    mc "No problem."
    r "I hope you don't mind that while you were gone I had a little chat with [mc]."
    scene 5nextdoor06 with dissolve
    "..."
    scene 5nextdoor09 with dissolve
    "Imperceptibly Rosa removed her palm from your hand and as if nothing had happened and continued to smile."
    scene 5nextdoor10 with dissolve
    s "I hope you didn't put too much pressure on him, mom."
    r "Oh, no. We had a great talk. Isn't that right, [mc]?"
    mc "Yeah, kinda."
    s "Heh. I can imagine that."
    s "Well, [mc], can we not waste time and get going?"
    mc "Sure."
    scene 5nextdoor10a with dissolve
    mc "It was nice talking to you Rosa."
    r "That's mutual."
    r "I'll be glad to see you again [mc]."
    scene 5nextdoor11 with dissolve
    "You and Selina head toward the exit while exchanging greetings."
    stop music fadeout 3.0
    if RPr >= 2:
        "You could literally feel Rosa's gaze upon you."
        scene 5nextdoor12 with dissolve
        r "{i}There's no point in getting upset over nothing, Rosa. Soon you'll have a piece of that sweet pie.{/i}"
        r "{i}In the meantime, let the kids have a good time.{/i}"
    jump day05_park


label day05_park:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    scene black with fade
    "Half an hour later."
    play music "music/12 - The Moose.ogg"
    scene 5park01 with dissolve
    "For a while, you and Selena were talking about nothing, joking and just teasing each other."
    s "Heh, so it turns out you're not only a great lover, but also a good conversationalist!"
    s "You're very easy to talk to."
    mc "I'll take that as a compliment."
    s "Ha ha! Isn't a guy supposed to compliment a girl he likes?"
    mc "Well, things are very unusual between you and me. First was sex, and only then dates."
    scene 5park02a with dissolve
    s "That's right..."
    scene 5park02b with dissolve
    s "Many people tell me that it's not easy with me."
    s "That I'm weird, that I'm impossible to communicate with, that I like to piss people off..."
    scene 5park02a with dissolve
    "..."
    mc "{i}Looks like I brought up a bad topic... I need to do something to cheer up Selina.{/i}"
    mc "What fools."
    mc "All those people just don't understand what they're missing. As for me, that's your main feature!"
    mc "And I don't give a damn what those nerds are saying."
    scene 5park02d with dissolve
    s "Do you really think so?"
    mc "Yes."
    scene 5park02c with dissolve
    s "Hee hee. Thanks."
    s "What about you? Doesn't anyone tell you that?"
    s "As far as I know, not everyone likes the career of a musician."
    mc "I'd be lying if I said it wasn't true. But my own opinion is more important to me than the opinions of others."
    scene 5park02 with dissolve
    s "So you're staying true to your dream?"
    s "Sounds pretty cool."
    scene 5park02c with dissolve
    mc "That's probably true. In a sense, being a musician means being a dreamer."
    mc "And I like that!"
    scene 5park02a with dissolve
    s "Yeah... But in the medical field things are somewhat different."
    mc "I can imagine."
    scene 5park02 with dissolve
    s "Listen, [mc], how about we take a little walk?"
    mc "With pleasure."
    scene black with fade
    "Some time later."
    scene 5park03 with dissolve
    "Keen on a walk in the Park, you and Selena did not notice how you were in the oldest part of it."
    s "Hey, don't you think we wandered into the wrong place?"
    mc "Yeah, you're probably right."
    mc "This is the old part of the Park, there's practically no one here."
    scene 5park04 with dissolve
    s "Nobody ever comes?"
    mc "{i}Heh, I could swear I know that lustful look.{/i}"
    mc "Yep."
    s "You probably already know what I'm thinking, don't you?"
    mc "About something very vulgar, dirty, but at the same time pleasant?"
    s "Hee hee. Precisely!"
    scene 5park05 with dissolve
    s "And it seems that there really is no one..."
    mc "Can't argue with that."
    s "So how about fooling around a bit in the fresh air?"
    s "Or are you afraid we might get caught?"
    stop music fadeout 3.0
    menu:
        "{color=#66FF33}Fool around with Selena":
            play music "music/8 - Intro Music.ogg"
            if lisa_path == True:
                $ cheat_point += 5
            $ RPs += 5
            $ selina_sex_day05 = True
            scene 5park06 with dissolve
            "You slide your hand onto Selina's ass."
            mc "Does it look like I'm afraid?"

        "Refuse":
            play music "music/8 - Intro Music.ogg"
            mc "I'm sorry, but today I pass."
            scene 5park06a with dissolve
            s "Oh... Are you serious?"
            mc "Yeah."
            s "It's very strange to hear that from a guy."
            s "Are you not in the mood today or is it something else?"
            mc "Just not today."
            s "Um... If you say so."
            scene black with fade
            "Soon after, you and Selina leave the Park."
            "You clearly thought Selina was upset by your decision."
            $ renpy.end_replay()
            "..."
            "Later that night, you arranged for Jacob to meet you the next morning and move the last things from the old rehearsal room to the new one."
            "There was a new day waiting for you."
            jump newreproom_day05

    scene 5park07 with dissolve
    s "Mmm... No, it doesn't..."
    s "And I like that!"
    mc "Yeah, me too."

    scene 5park09 with dissolve
    "In the next second, Selina headed into the Park, where there was a small group of trees."
    s "Well, do you think this quiet place would be good enough for you and me?"
    mc "{i}Quiet? You can see through from almost all sides!{/i}"
    mc "{i}She's a risky girl.{/i}"
    mc "{i}However, very few people come through here.{/i}"
    scene 5park08 with dissolve
    s "So what are you gonna say?"
    mc "I'll say this place is as good as any!"
    s "Hee hee!"
    s "I was sure that's what you'd say."
    mc "Really?"
    s "Yep!"
    scene 5park10 with dissolve
    s "Can anyone resist this?"
    scene 5park10a with dissolve
    "..."
    mc "{i}Uhh... Indeed, it is difficult to resist.{/i}"
    "You stepped forward and touched Selina's butt with your hand."
    scene 5park11 with dissolve
    s "Mmmm... Yes..."
    s "You like what you feel, don't you?"
    mc "{i}It's so soft and pleasant to the touch...{/i}"
    s "Now imagine what else lies ahead."
    s "Imagine fucking me as hard as you can right here in the clearing..."
    s "Imagine my loud moans..."
    mc "All right, enough talking!"
    mc "Come here."
    scene 5park12 with dissolve
    "You pulled Selina towards you and gave her a big kiss."
    s "Ohhh... Good start."
    mc "{i}Exactly!{/i}"
    "At the same time as you kissed Selena, your hands were all over her body."
    scene 5park13 with dissolve
    s "Mmm... [mc] I think your big guy's asking to come out."
    mc "Help him with that?"
    s "Hee hee!"
    s "With pleasure."
    scene 5park14 with dissolve
    "Selina sank lower and slowly unzipped the fly on your pants."
    mc "{i}Yeah... Now I remember just how much I really missed this red-haired girl!{/i}"
    scene 5park15 with dissolve
    s "Well, well! And who's hiding in here?"
    "You felt Selina touch your dick."
    s "Mmm... He's exactly the way I remember him."
    show day5_bj
    "The girl slowly began to masturbate your cock."
    mc "Oh yeah... That's good."
    s "Hee hee!"
    s "Be ready to have a lot of fun today, because I'm going to squeeze you completely dry."
    mc "Know... I'm not against that at all..."
    mc "Just don't stop!"
    scene 5park17 with dissolve
    s "Mmm... Your cock is so hot."
    s "I can't wait to feel it in my pussy..."
    s "And you?"

    stop music fadeout 3.0

    scene 5park18 with dissolve
    "The next moment, you felt Selina's soft lips on the tip of your cock."
    mc "Ohhh... Go on..."
    play music "music/15 - Deep Mood.ogg"
    show anim10
    s "Mmmm... Like this?"
    s "Mmppphhh... Mpphhhhh... Mmmmphhhh...."
    mc "Yes! Keep it up."
    mc "{i}Oooohhhh... That's good.{/i}"
    s "Mmhmm... Mpphh... Mmhmm...."
    scene 5park20 with dissolve
    mc "Just don't stop, baby!"
    mc "{i}Damn, that's one of the best blowjobs I've ever had...{/i}"
    scene 5park19 with dissolve
    s "How does it feel, babe?"
    s "It feels good, doesn't it?"
    mc "Amazing..."
    s "Hee hee! Yeah, I'm pretty damn good at it."
    mc "{i}All right! It's time to get to the main event!{/i}"

    stop sound fadeout 1.0

    scene 5park21 with dissolve
    "You lifted Selena to her feet, and then noticed how your cock was right in front of her pussy."
    s "Ooh... Looks like someone's ready to play big now!"
    scene 5park22 with dissolve
    "Selina lifted her orange top and began gently massaging her firm breasts."
    s "Mmm... I think it would be much better this way..."
    scene 5park23 with dissolve
    "The girl leaned on a tree behind her, revealing a stunning sight."
    s "What are you waiting for?"
    s "Don't you want to put your big cock in my pussy?"
    s "I've been eager to continue our fun."
    scene 5park24 with dissolve
    mc "You talk too much..."
    s "Mmm... Really?"
    mc "Yes... And now you get what you want..."
    s "I'm waiting... Ohhh!"
    scene 5park25 with dissolve
    "With one swift movement, you were inside Selina."
    mc "{i}Yes... Much better now!{/i}"
    s "Oooh... Yes..."
    s "Now... It really feels good..."

    show anim7
    s "Aaahhh... Yes... Yeah!!"
    s "God, that feels so good!"
    mc "{i}Hell, I think she's screaming too loud...{/i}"
    s "Nhaa.. Nhaa..."
    s "Come on, come on! Fuck me harder!"
    s "Yes, Yes! like this!!!"
    s "Aaahhh... Aaahhh..... Aaahhh!!!"
    s "Don't stop! Your cock is amazing!!!"
    "..."
    scene 5park26 with dissolve
    mc "{i}Ohhh... And yet this girl is still a depraved beast.{/i}"
    mc "{i}How did I get in touch with her?{/i}"
    scene 5park27 with dissolve
    "Just to shut her up for a little while, you kissed her again."
    mc "{i}It's so cool that my thighs move by themselves...{/i}"
    s "Mmmm..."
    mc "Now let's change our position."
    scene 5park28 with dissolve
    "Without saying another word, you turned Selina's back on you and take her from behind."
    s "Yeah, baby... That's better!!!"
    mc "Be quiet! We're still in the Park, in case you forgot!"
    scene 5park28a with dissolve
    s "Mmm... I'm sorry, but I can't help myself..."
    mc "{i}Though it's disturbing to realize that we can be heard, at the same time it's nice to hear such words from the girl you're having sex with.{/i}"
    scene 5park29 with dissolve
    "Under accelerated movements she leaned harder on the tree."
    show anim8
    s "Aaahhh... Aaahhh..... Aaahhh!!!"
    s "Come on, [mc], fuck me harder!!! Even harder!!!"
    mc "{i}Oooohhh... Now she's behaving like a real nymphomaniac...{/i}"
    mc "{i}But somehow I like it all...{/i}"
    mc "Take that! Take that!!!"
    s "Mmmm... Yeeeesss...."
    s "Please, just don't stop!"

    scene 5park29 with dissolve
    "Suddenly, you and Selina heard a very strange sound in the distance."
    scene 5park29a with dissolve
    "..."
    mc "{i}What the fuck?!{/i}"

    play sound "music/steps.wav"

    scene 5park29b with dissolve
    "..."
    mc "{i}WHAT THE FUCK?????!!!!!{/i}"
    "A jogging girl made you both visibly tense."
    scene 5park30 with dissolve
    "Another surprise was the fact that at the same moment Selina's pussy abruptly tightened, making you almost come."
    mc "{i}HOLY SHIT!!!!!!!!!!!!{/i}"
    "For some time the two of you stood there, while the athlete quietly withdrew further and further."
    mc "{i}Ugh... We almost got caught...{/i}"
    mc "{i}All right, let's get this over with!{/i}"

    show anim9
    "You picked up Selena with your hands and started fucking her like hell."
    s "Waaaah! Why are you?!"
    mc "..."
    s "Ahhh... Ahhh... Ahhh...."
    s "And you... you're very strong..."
    mc "Yeah."
    scene 5park31 with dissolve
    s "A little more! A little more and I'll come!!!"
    s "Oooohhhh... Ooohh... Ohhh..."
    mc "{i}Fuck, I'm holding on with the last of my strength!{/i}"
    scene 5park31a with dissolve
    s "[mc]... [mc], I can't take it anymore!"
    s "I'm cumming!!!"

    stop music fadeout 3.0

    scene 5park31 with dissolve
    s "AAAHHHH! YES!"
    mc "{i}Shit, I think I'm cumming too!{/i}"
    scene 5park32 with flash
    mc "Yeah!!! How cool!"
    scene 5park32 with flash
    s "Mmmm...."
    "..."

    play music "music/8 - Intro Music.ogg"

    scene 5park33 with dissolve
    s "Ugh... That was cool..."
    s "I'm starting to feel like every time we have sex it's getting better and better."
    mc "Huh. I can't say I don't like it!"
    s "Hee hee. Me too!"
    scene black with fade
    "A minute later."
    scene 5park34 with dissolve
    "You and Selina cleaned yourselves up."
    s "Here, now we look much better!"
    mc "Yep. And how about we get out of here?"
    s "Good idea."

    scene 5park35 with dissolve
    "Holding hands, you and Selina exit the Park."
    mc "{i}Yes, we had an interesting walk!{/i}"
    "..."

    $ renpy.end_replay()
    if not persistent.day05selina:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day05selina = True

    stop music fadeout 3.0
    scene black with fade
    "Later that night, you arranged for Jacob to meet you the next morning and move the last things from the old rehearsal room to the new one."
    "There was a new day waiting for you."
    jump newreproom_day05


label newreproom_day05:
    scene black with fade
    "As you had agreed earlier, you and Jacob met by the old rehearsal place."
    play music "music/7 - Just Happy.ogg"
    scene 5move01 with dissolve
    j "Ooh! I can't believe we finally loaded the last of it!"
    mc "Yep. For some reason I thought there'd be much less."
    j "Yeah, I can't argue with that."
    "..."
    mc "You know, it's really strange to see this place so empty."
    j "Yeah, I totally understand."
    j "We've spent no more than a month here, and yet it feels like a lot longer."
    "..."
    scene 5move02 with dissolve
    mc "Do you think the girls had time to buy some decor?"
    j "I don't know."
    j "Lisa wanted to buy something like posters and other useless designer stuff."
    mc "I don't think those are useless."
    mc "After all, she is a future designer and has an eye for details."
    j "Heh. You know I'm an old-school person. Until I see it with my own eyes, I'll stick with my opinion."
    scene 5move03 with dissolve
    j "Come on."
    j "We'll still have to unload it."
    mc "You don't regret not hiring movers for this?"
    j "Pfft... Not a bit! We can handle this on our own."
    j "Especially since we've already done half the work."
    scene 5move04 with dissolve
    "..."
    mc "Yeah."
    mc "Half the work is already done..."

    stop music fadeout 3.0

    scene black with fade
    "Some time later."

    play music "music/16 - Bright Colors.ogg"

    scene 5rep00 with dissolve
    j "Look, looks like the girls are here."
    mc "Yeah, they're surprisingly fast."
    j "Hey everyone!"
    scene 5rep00a with dissolve
    ls "There they are. Guys, we were just thinking about you."
    j "Heh heh."
    mc "How are you? Bought everything you wanted?"
    ls "Yep. We have everything we need with us."
    jd "We're ready."
    j "Great, then I don't see the point in dragging this out. Let's go."
    ls "Agreed. The sooner we start, the sooner we finish."
    scene 5newrep05 with dissolve
    "You went up to your future rehearsal room and took another good look at it."
    ls "Remember this room, guys, because by the end of the day, you won't recognize it."
    j "Heh. Come on, show us your voodoo!"
    scene 5rep01 with dissolve
    "Soon, under the strict guidance of Lisa, you began to bring the furniture and arrange the decor exactly as she said."
    "You and Jacob brought the heaviest things, while Lisa and jade put the carpet on the floor and hung pictures on the walls."
    scene 5rep02 with dissolve
    "Every minute, every hour the room that until recently stood with bare walls, more and more began to look like a normal room for a comfortable pastime."
    scene 5rep03 with dissolve
    "You also didn't forget to arrange breaks for rest."
    "Ordering pizza and drinks, you congregated in the center of the room and chatted on a variety of topics."
    scene 5rep04 with dissolve
    "After a while, you took a step back from work and realized that everything is almost finished."
    "..."
    stop music fadeout 3.0
    mc "{i}Hmm... We were quite efficient!{/i}"

    scene 5rep05 with dissolve
    play music "music/6 - Positive Mood.ogg"
    ls "Looks like we're done here."
    "..."
    ls "Well, what do you think about this?"
    mc "It wasn't easy, but I think we did our best."
    jd "I like everything too."
    j "Yep. It's a bit like our last rehearsal room, but it looks a lot cooler."
    j "I have to admit, Lisa, you know your stuff."
    mc "He's right, Lisa. All that beauty came from you."
    scene 5rep07 with dissolve
    ls "Ummm... Though it’s nice to hear and everything, but it seems to me that it's the merit of everyone here."
    scene 5rep08 with dissolve
    j "I'm not arguing. In this situation, we too, are great!"
    scene 5rep07a with dissolve
    ls "That's what I wanted to hear."
    scene 5rep09 with dissolve
    jd "The truth is, when I saw this place, I didn't even think it could turn into something like this."
    jd "We make a good team."
    scene 5rep08 with dissolve
    j "Well, since Jade said it, it really is."
    j "Not to mention, we did everything with our own hands in just one day!"
    j "Hell, maybe we should open a design Agency instead of doing music?!"
    scene 5rep07a with dissolve
    ls "Huh! Nope! I didn't sign up for this!"
    "..."
    scene 5rep07b with dissolve
    ls "Hey... [mc], why are you so silent?"
    scene 5rep08a with dissolve
    j "Yeah, buddy, everything okay?"
    scene 5rep06 with dissolve
    mc "I don't know, guys... It just seems so unreal."
    mc "It seems only yesterday Jacob and I were hanging out in that shabby little room together, and today the four of us are in this gorgeous place."
    mc "Our band is assembled and ready, there is a place for rehearsals. Hell, we even started writing songs!"
    mc "That sounds really cool to me."
    scene 5rep08 with dissolve
    j "You bet!"
    j "And imagine what will happen in a couple of months? A year?"
    j "There's a real heat ahead of us."
    scene 5rep07b with dissolve
    ls "I think you're getting ahead of yourself, boys."
    ls "Before we become really good musicians, we have to go through a lot of rehearsals."
    scene 5rep09 with dissolve
    jd "Relax, Lisa. Let the boys dream a little."
    scene 5rep08 with dissolve
    j "Heh heh."
    j "This is what we dream for now, but soon everything will change. Trust me!"
    mc "As you say, dude."
    scene black with fade
    "A few minutes later."
    "You notice that after work, each of them decided to relax."
    scene 5rep10 with dissolve
    mc "{i}Looks like Jacob's thinking about something serious.{/i}"
    mc "{i}However, I have something to discuss with him and now seems to me a pretty good time.{/i}"
    mc "Hey, man, what's on your mind?"
    scene 5rep11 with dissolve
    j "I'm thinking about taking over the world."
    mc "Oho. A serious topic for reflection."
    j "It is!"
    scene 5rep11a with dissolve
    mc "Do you mind if I take your mind off these heavy thoughts for a while?"
    j "Sure, say what you want."

    menu day05_question01:
        "{color=#66FF33}Tell Jacob about your relationship with Lisa." if lisa_path == True:
            $ jacob_knows_about_lisa = True
            $ RPls += 1
            $ RPj += 1
            mc "{i}Hell, I have no idea how he's gonna react to all this, but it's better to tell him right away.{/i}"
            mc "I don't know how to tell you this, but I'll tell you anyway..."
            mc "Lisa and I decided to start dating."
            scene 5rep11b with dissolve
            j "Are you for real? You and her?"
            mc "Yep."
            scene 5rep11a with dissolve
            j "Wow! No, I mean, I've noticed that there's something between you, but I didn't really think about it."
            mc "We just started dating, so I didn't get a chance to tell you before."
            j "Wow! You guys don't waste any time..."
            mc "Hope you don't mind?"
            scene 5rep11d with dissolve
            j "What?! I mind? Why would I mind that?"
            j "Of course not! It was just a little unexpected, that's all."
            mc "{i}Ugh... I was a little afraid of his reaction, but I knew he'd support me.{/i}"
            mc "I understand. I didn't realize I liked her right away."
            j "I see..."
            j "Are you getting serious with her?"
            menu:
                "{color=#66FF33}It's serious":
                    $ RPj += 2
                    $ RPls += 2
                    mc "Yeah, you could say that."
                "I don't know yet":
                    mc "I don't know yet."
                    mc "It's just starting to happen."
            scene 5rep11a with dissolve
            j "Well, man! In that case, I can only wish you good luck."
            mc "Heh. Thanks."
            j "What about Jade? She knows that?"
            mc "Not yet."
            mc "I think Lisa will tell her later."
            j "Well, that's reasonable. They seem to get along well."
            scene 5rep11c with dissolve
            j "Look at them talking to each other like they're best friends."
            scene 5rep12 with dissolve
            mc "{i}Hmm... He's right. Recently, they have become noticeably closer.{/i}"
            mc "Who knows, maybe soon they will become best friends?"
            j "We'll see."
            "..."

        "Keep your relationship with Lisa a secret" if lisa_path == True:
            mc "{i}I don't think this is the right time to tell Jacob about my relationship with Lisa.{/i}"
            mc "{i}I'd better ask him what he thinks of our band.{/i}"
            mc "I wanted to ask you, what do you think of our band?"
            scene 5rep11d with dissolve
            j "The band?"
            j "Hmm... Let me think."
            scene 5rep11a with dissolve
            j "If my memory serves me, I've already said that we're waiting for worldwide fame, crowds of fans and everything else that comes with rock stars?"
            mc "Said more than once."
            j "Then you know I'm not likely to add anything new to that."
            mc "No kidding. Do you really think so?"
            scene 5rep11b with dissolve
            j "You want to know what I really think?"
            mc "Yes, I do."
            "..."
            scene 5rep11d with dissolve
            j "I don't think it'll be easy for us. Not easy at all."
            j "There are so many great bands out there that perform in Nightclubs and waste their talent in vain, which is why I try to think only about the good."
            mc "Yeah, you can't argue with that. Only a few ever make it to true fame."
            j "Well, in that case, it's good that we like to make music, isn't it?"
            j "Because if we don't succeed in the end, then at least we'll get pleasure from this process."
            mc "You know, when you're optimistic, I like you better."
            scene 5rep11a with dissolve
            j "Heh heh. I'll remember that."
            mc "Yeah."

    if lisa_path == False:
        mc "I wanted to ask you, what do you think of our band?"
        scene 5rep11d with dissolve
        j "The band?"
        j "Hmm... Let me think."
        scene 5rep11a with dissolve
        j "If my memory serves me, I have already said that we are waiting for worldwide fame, crowds of fans and everything else that comes with rock stars?"
        mc "Said more than once."
        j "Then you know I'm not likely to add anything new to that."
        mc "No kidding. Do you really think so?"
        scene 5rep11b with dissolve
        j "You want to know what I really think?"
        mc "Yes, I do."
        "..."
        scene 5rep11d with dissolve
        j "I don't think it'll be easy for us. Not easy at all."
        j "There are so many great bands out there that perform in Nightclubs and waste their talent in vain, which is why I try to think only about the good."
        mc "Yeah, you can't argue with that. Only a few ever make it to true fame."
        j "Well, in that case, it's good that we like to make music, isn't it?"
        j "Because if we don't succeed in the end, at least we'll get pleasure from this process."
        mc "You know, when you're optimistic, I like you better."
        scene 5rep11a with dissolve
        j "Heh heh. I'll remember that."
        mc "Yeah."

    scene black with fade
    "Some time later."
    scene 5rep13 with dissolve
    j "Uhhh... Okay, people, I gotta go."
    j "I guess we'll meet here next time, but in rehearsal?"
    ls "Seems so."
    scene 5rep13a with dissolve
    jd "I'll go home too."
    jd "It was nice spending time with you."
    j "What about you [mc]? You with us or-"
    if lisa_path == True:
        jump day05_lisa
    else:
        mc "Yes, I'll come with you."
        jd "And you Lisa?"
        ls "Same."
        j "Great, then let's go!"
        scene 5rep14a with dissolve
        "Talking about everything, you went home."
        stop music fadeout 3.0
        "There was a new day waiting for you."
        jump day06_start


label day05_lisa:
    if _in_replay:
        $ setReplay()
    stop music fadeout 2.0
    mc "I think I'll stay here for a while."
    jd "And you Lisa?"
    ls "I'll go a little later too."
    j "Well, whatever."
    scene 5rep13b with dissolve
    j "Jade, can I walk you out?"
    scene 5rep13c with dissolve
    jd "Only if you want to."
    j "Great, then let's go!"
    stop music fadeout 3.0
    scene 5rep14 with dissolve
    play music "music/9 - You Can Make the Sound.ogg"
    "Jade and Jacob are gone, leaving you and Lisa alone."
    "..."
    ls "Looks like we're alone..."
    mc "Yes."
    scene 5rep15 with dissolve
    "Feeling a little tired after a difficult day, you sat down on the sofa with great pleasure."
    mc "{i}Yeah... That's nice...{/i}"
    scene 5rep16 with dissolve
    ls "[mc]..."
    mc "Mmm?"
    mc "{i}You notice that Lisa wants to ask you something, but she seems embarrassed.{/i}"
    mc "Don't be shy. You can talk to me about anything you want."
    scene 5rep16a with dissolve
    ls "Hey! I'm actually not shy!"
    mc "Oh really? From the outside it looks like it."
    ls "Nothing like that."
    ls "Would I do this if I was shy?"
    scene 5rep17 with dissolve
    "Suddenly, Lisa pounces on you and gives you a kiss."
    mc "{i}Mmm... Her lips are so soft...{/i}"
    mc "Okay, okay, you're definitely not shy, but what's the matter?"
    scene 5rep18 with dissolve
    ls "I wanted to know if you told Jacob about us."

    if jacob_knows_about_lisa == True:
        mc "Yeah, I did."
        scene 5rep18b with dissolve
        ls "Really?!"
        mc "Of course!"
        mc "Why are you so surprised? Did you doubt me?"
        ls "Not a bit! I knew you wouldn't let me down!"
        scene 5rep18 with dissolve
        ls "And how did he take it?"
        mc "Normally. I would even say, good."
        scene 5rep18b with dissolve
        ls "Wow! In that case, you deserve another kiss..."
        scene 5rep19 with dissolve
        mc "{i}Mmmm...{/i}"
        mc "{i}I guess I'll never get tired of kissing this pretty girl.{/i}"
        scene 5rep18b with dissolve
        ls "Did you enjoy it?"
        mc "I do."
        mc "Now come here!"
    else:
        mc "Not yet."
        scene 5rep18a with dissolve
        ls "Oh... I see."
        ls "But didn't you spend all day with Jacob today?"
        scene 5rep18c with dissolve
        ls "Or are you ashamed of our relationship?"
        mc "Of course not!"
        mc "The truth is, I don't know why I'm delaying this conversation..."
        mc "But it's definitely not because of you. And that doesn't mean I'm ashamed of our relationship!"
        mc "Now come here!"

    scene 5rep20 with dissolve
    "You grabbed Lisa in your arms and put her next to you."
    ls "Wow... Why are you so cuddly all of a sudden?"
    mc "I wanted to squeeze you a little."
    ls "[mc], that's so childish."
    scene 5rep21 with dissolve
    mc "How am I supposed to say no to something so sweet?"
    ls "Flatterer."
    mc "Ha! Don't tell me you don't like those words."
    ls "..."
    mc "I thought so."
    scene 5rep22 with dissolve
    ls "You know, I'm getting hot in here."
    mc "{i}Hm? Is she serious or is she teasing me?{/i}"
    ls "Do you mind if I take off my jacket?"
    mc "Sure."
    scene 5rep23 with dissolve
    "Lisa took off jacket and threw it aside."
    ls "Ugh... It's much better now."
    mc "{i}I can't disagree with that.{/i}"
    scene 5rep24 with dissolve
    "..."
    ls "Hey, why are you looking at me like that?"
    mc "Because you're so beautiful."
    ls "Oh really?"
    scene 5rep25 with dissolve
    "Without saying a word, you threw Lisa on the couch."
    ls "Aaahh...."
    mc "You're the most beautiful girl I've ever met."
    scene 5rep26 with dissolve
    ls "Mmmm..."
    ls "Those words are hard to resist."
    scene 5rep27 with dissolve
    "Your hands slide all over Lisa's body and stop on her chest."
    mc "{i}Wow... This is amazing...{/i}"
    mc "{i}She's not even trying to take my hands off.{/i}"
    mc "{i}Maybe she's not against continuing?..{/i}"
    stop music fadeout 3.0
    scene 5rep28a with dissolve
    ls "[mc]..."
    mc "{i}Man, I think I jumped the gun a little bit.{/i}"
    ls "Sorry, I don't think I'm ready..."
    mc "{i}Maybe it's better to be a little softer today.{/i}"
    mc "Okay. I hear you."

    play music "music/Maxim Nick - Falling Down.mp3"

    scene 5rep28 with dissolve
    ls "R-really?"
    mc "Of course!"
    mc "But you can have fun without going over a certain line."
    scene 5rep29 with dissolve
    ls "Mmm... I think I know what you mean..."
    ls "One minute."
    scene 5rep30 with dissolve
    "..."
    scene 5rep30a with dissolve
    "..."
    scene 5rep30b with dissolve
    "..."
    scene 5rep30c with dissolve
    "..."
    mc "{i}Oh yeah...{/i}"
    scene 5rep31 with dissolve
    "Lisa jumped on top of you and smiled slyly."
    ls "Maybe you should get rid of the extra clothes, too..."
    mc "{i}Damn, she's so sexy in that black lingerie...{/i}"
    mc "{i}I can't wait to get it off her.{/i}"
    scene 5rep32 with dissolve
    "Slowly with her hands on your torso, the girl began to aggressively paw at your t-shirt."
    mc "I really don't think we're gonna need any clothes here."
    "You threw the shirt aside and immediately moved closer to Lisa."
    scene 5rep33 with dissolve
    mc "{i}Mmm... I've waited so long for this.{/i}"
    "..."
    mc "{i}And judging by her insistent actions, I wasn't the only one waiting...{/i}"
    scene 5rep34 with dissolve
    "Your hands are drawn to the latch of her bra all by themselves."
    mc "{i}A little more...{/i}"
    scene 5rep35a with dissolve
    "*Click*"
    mc "{i}Got it!{/i}"
    scene 5rep36 with dissolve
    "Contrary to your expectations, Lisa immediately covered her Breasts."
    mc "Is something wrong?"
    ls "I am... Ummm....."
    ls "Sorry, probably just a habit."
    mc "Everything is fine. Just be yourself."
    scene 5rep36a with dissolve
    ls "You know, you treat me so well that every second I spend with you makes me feel better and better."
    mc "That's the whole point. We have to trust each other."
    ls "I trust you."
    scene 5rep37 with dissolve
    "Lisa leaned back, showing you her gorgeous Breasts."
    ls "But now you can see for yourself."
    mc "Yeah, I see."
    mc "{i}Oh God... I have to control myself. Must hold!{/i}"
    mc "{i}But how hard it is...{/i}"
    scene 5rep38 with dissolve
    "You bend down right in front of a half-naked girl and gradually began to get closer to her."
    mc "{i}I think she's beginning to open up to me.{/i}"
    mc "{i}And now it's time to give her pleasure. Something she'll never forget.{/i}"
    scene 5rep39 with dissolve
    ls "Aaahhh..."
    mc "{i}Her Breasts are so firm... Surprisingly so.{/i}"
    mc "Try to relax and have fun."
    stop music fadeout 3.0
    ls "..."
    ls "Okay."
    play music "music/1 - Atmosphere.ogg"
    scene 5rep40 with dissolve
    "With smooth movements you began to slide your hand lower and lower."
    mc "{i}Is it me or has her breathing accelerated?{/i}"
    scene 5rep40a with dissolve
    "..."
    mc "{i}Definitely accelerated.{/i}"
    mc "{i}And despite this, she's ready to continue...{/i}"
    scene 5rep41 with dissolve
    "One deft movement, you put your hand in Lisa's panties and immediately felt her wet pussy."
    ls "Mmmmm... Ahh..."
    mc "{i}Oh yeah... She's gonna love this.{/i}"
    mc "{i}Fuck, that turns me on!{/i}"
    show day5_hj
    "At the same time caressing and kissing her, you noticed how Lisa began to move her pelvis to the rhythm of your fingers."
    ls "Mmmm... Mmmm... Mmmm...."
    mc "{i}Oh, she definitely likes that.{/i}"
    scene 5rep43 with dissolve
    ls "Aaahhh... [mc], that's right... It feels good..."
    ls "Please don't stop!"
    mc "I'm not."
    scene 5rep44 with dissolve
    "You noticed how Lisa's free hand started rubbing her Breasts."
    ls "Ohh!.... Oooohhh... Yeeeessss..."
    mc "{i}Perhaps I should speed things up a bit.{/i}"
    scene 5rep45 with dissolve
    ls "Yeeeeessss!!! [mc], Yeeeessss!!!"
    ls "I think I'm..."
    scene 5rep46 with flash
    ls "AAAAHHHH!!!!"
    "Lisa's body arched, and from her lips broke a lingering moan."
    scene 5rep46 with flash
    ls "YEEEESSSS!!!"
    stop sound fadeout 2.0
    scene 5rep48 with dissolve
    "The next moment, she collapsed onto the sofa, completely exhausted."
    mc "{i}What an orgasm. I envy her...{/i}"
    mc "You okay?"
    ls "Give me a minute... to catch my breath..."
    mc "Please, take your time."
    scene 5rep47 with dissolve
    mc "{i}Damn, she's so beautiful.{/i}"
    mc "{i}I still can't believe what's going on between us.{/i}"
    stop music fadeout 3.0
    scene 5rep48 with dissolve
    mc "Well? Are you better now?"
    scene 5rep48a with dissolve
    ls "Much better!"
    mc "{i}Oh, look at her, she's all flushed.{/i}"
    ls "[mc] I don't know where you learned it, but that was amazing!"
    mc "I'm glad you liked it."
    scene 5rep49 with dissolve
    "Still breathing heavily, Lisa took a sitting position and looked you in the eye."
    mc "You sure you're all right?"
    ls "A hundred percent."
    ls "But do you mind if I put my jacket on?"
    mc "{i}Are you shy again? Or something I don't understand?{/i}"
    mc "That's fine with me."
    scene 5rep50 with dissolve
    "..."
    scene 5rep51 with dissolve
    play music "music/Maxim Nick - It's okay (final).mp3"
    ls "I'm sorry, I just don't feel at ease otherwise."
    mc "Okay."
    mc "{i}Hmm... I should note that her appearance is no less sexy now than if she was naked.{/i}"
    ls "Umm... [mc]! Wake up!"
    mc "{i}Fuck, I guess I was staring at her again.{/i}"
    mc "I'm sorry, I can't help it."
    ls "Heh."
    ls "It's okay. I even like it when you look at me like that."
    mc "{i}Hmm... I don't think she'd have told me that before.{/i}"
    scene 5rep52 with dissolve:
        ypos -1.75
        ease 8 ypos 0.0
    "Suddenly, Lisa stood and turned her back on you."
    mc "{i}What a beautiful ass! I feel like I'll never get tired of looking at her.{/i}"
    mc "What are you up to?"
    ls "You'll see."
    scene 5rep53 with dissolve
    ls "Do you mind if I take it?"
    ls "I promise I'll be very careful!"
    mc "Of course, take it."
    ls "Hee hee. Thanks."
    scene 5rep54 with dissolve
    mc "I didn't know you could play the guitar."
    ls "I can't."
    ls "However, one tune, I can definitely do."
    mc "Okay, you intrigued me."
    scene 5rep55 with dissolve
    "Lisa sat on the corner chair and slowly began to strum the melody."
    mc "Hell, I thought when you had a microphone in your hand, it was sexy, but this..."
    mc "This is a completely new level."
    scene 5rep56 with dissolve
    ls "Glad you appreciate it."
    ls "Now just listen..."
    "The guitar once again filled the entire room with music."
    "..."
    mc "{i}Of course, she's still a beginner - even the deaf would say so, but somehow this sight is still mesmerizing.{/i}"
    mc "You know, looking at you with a guitar in your hand, I was thinking maybe we should switch places?"
    mc "You'll play the bass and I'll sing."
    scene 5rep57 with dissolve
    ls "Ha! You can try it, but believe me, singing is not as easy as it appears."
    mc "{i}She doesn't think that's gonna stop me now, does she?{/i}"
    mc "You don't think I can do it?"
    ls "Try it if you want to."
    mc "I'll try."
    ls "Come on!"
    scene 5rep58 with dissolve
    "You went to the microphone and picked it up."
    mc "And if I succeed, what will we do?"
    ls "Mmmm... I don't know."
    ls "I want to hear it first!"
    scene 5rep59 with dissolve
    "Adjusting to Lisa's tune, you started singing."
    ls "That's quite good! With your vocal skills and my guitar playing, we can easily perform in the subway or at children's parties."
    mc "Having fun, right?"
    ls "You betcha!"
    "Between the terrible music and the lousy voice you began to approach each other closer and closer."
    scene 5rep60 with dissolve
    ls "Mmm... What now?"
    mc "I have a really good idea. Now we-"
    stop music
    play sound "music/music_stop.wav"
    scene 5rep61 with vpunch
    jd "OH!"
    scene 5rep62 with dissolve
    mc "{i}Jade?{/i}"
    scene 5rep62a with dissolve
    "..."
    scene 5rep62 with dissolve
    "..."
    mc "{i}Fuck...{/i}"
    scene 5rep62b with dissolve
    mc "No need to jump to conclusions."
    mc "I'll explain everything."
    scene 5rep63 with dissolve
    play music "music/8 - Intro Music.ogg"
    jd "Umm..."
    jd "We're all adults here, you don't have to explain anything to me."
    jd "I just came to pick up a cell phone that I left here."
    scene 5rep64 with dissolve
    "Paying attention to Lisa, you noticed how quickly her face blushes."
    scene 5rep64a with dissolve
    ls "W-wait!!! [mc] is right, we can explain!"
    ls "Really?!"
    mc "{i}It doesn't seem to be any need for explanation, but it's worth it to say.{/i}"
    scene 5rep62b with dissolve
    mc "Jade, I'm sorry about this stupid show, but Lisa's right."
    mc "Please stay a minute."
    scene black with fade
    "Few minutes later."
    scene 5rep65 with dissolve
    mc "...that's why we're dating, and that's why you saw us like this."
    scene 5rep66 with dissolve
    jd "Even though you didn't have to explain anything to me, I get it."
    ls "Thank God!"
    jd "Now, if you don't mind, I'll take what I came for."
    scene 5rep66a with dissolve
    "..."
    scene 5rep66 with dissolve
    jd "Sorry again for disturbing you at such a... Uhh... Important moment..."
    jd "I'm gonna go now."
    scene 5rep65 with dissolve
    ls "Wait, we're going with you!"
    mc "{i}Looks like Lisa's still uncomfortable, which is why she wants to get out of here.{/i}"
    mc "{i}It's understandable.{/i}"
    jd "Okay."
    scene black with fade
    "Minute later."
    scene 5rep68 with dissolve
    mc "That's pretty much it."
    ls "[mc] do you mind if I go with Jade tonight?"
    mc "Of course I don't mind at all."
    mc "{i}Let the girls have a little privacy.{/i}"
    "..."
    mc "In that case, see you soon."
    jd "Bye."
    ls "See you!"

    $ renpy.end_replay()
    if not persistent.day05lisa:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day05lisa = True    

    scene black with fade
    "Nodding goodbye to the girls, you went home."
    stop music fadeout 3.0
    "There was a new day waiting for you."
    jump day06_start
