
label day11_start:
    scene nextday with fade
    $renpy.pause(3, hard=True)
    scene black with fade
    "Most of the next day you spent rehearsing for the upcoming gig."
    "Only after you were fully confident that the band is ready you allowed yourself a short break."
    "Suddenly, your thoughts were interrupted by Jacob's voice."
    play music "music/7 - Just Happy.ogg"
    scene 11start01 with dissolve
    j "Hey, guys, since tomorrow's gonna be a tough day, I have a huge offer for you!"
    scene 10rehearsal12 with dissolve
    mc "What kind of offer?"
    scene 10rehearsal06a with dissolve
    j "Hehe. How about we take a break for the rest of the day?"
    scene 10rehearsal11 with dissolve
    mc "Yeah, but we have a break right now. Isn't that enough?"
    scene 10rehearsal06a with dissolve   
    j "No! You misunderstood me. I'm talking about a real hangout! Rest with a capital R!"
    j "And I have one very good option for it."
    scene 11start02 with dissolve
    j "While you were sitting here idling, Barry called me and invited us to his house."
    mc "{i}Hmm. I saw him talking to someone on the phone, but I didn't know it was Barry.{/i}"    
    scene 11start03 with dissolve
    ls "Barry? That guy with the fancy mansion where we went to the party?"
    mc "Yeah, that's right. That's him."
    ls "He seemed like a great guy."
    scene 11start03b with dissolve
    ls "But I'm not sure if we need another big party like that. At least not today."
    scene 10rehearsal06 with dissolve
    j "You don't have to worry about that. Unlike last time, there'll be no one else there but us."
    j "So, me and [mc] will meet our friend, and you guys can swim in the pool or sunbathe."
    j "Everyone will find something to do."
    scene 11start03a with dissolve
    mc "Actually, that's a good idea. We could really use some fun before tomorrow."
    scene 10rehearsal06a with dissolve
    j "Haha! That's right! I knew you'd understand me! I hope the others don't mind, too."
    j "Besides, if we go there, I will invite my new girlfriend with us, and you all will meet her."
    j "Well, all but [mc], of course. He already knows her."
    scene 11start03 with dissolve
    ls "Hold on... Are you talking about that blue-haired girl? I think her name was Ruby, right?"
    scene 11start02 with dissolve
    j "Yep! That's her."
    j "As you may know, we went on a date a couple of days ago, and I can confidently say that she's just adorable."
    j "I think I almost fell in love with her."
    scene 10rehearsal11 with dissolve
    mc "Considering how easily you fall in love with almost every girl, we didn't even doubt that, man."
    scene 10rehearsal06b with dissolve
    j "Hey! Maybe I had some failures in love before, but now I know it's a sincere feeling."
    j "And what's most important, that feeling is mutual."
    scene 11start04 with dissolve
    jd "If that's true, then we're very curious to see the girl who managed to charm you so easily."
    scene 11start02 with dissolve
    j "Oh, I'm sure you'll see her many times from now on."
    j "Besides, I already invited her to our gig tomorrow."
    scene 11start03 with dissolve
    ls "Huh. You're not wasting any time."
    scene 11start03a with dissolve
    mc "Okay, if everyone agrees with Jacob's proposal, then I suggest we go home and change. And in about an hour, we'll meet up at Barry's."
    mc "Is everybody okay with that?"
    scene 11start03 with dissolve
    ls "Yeah, I'm okay."
    scene 11start04 with dissolve
    jd "I'm okay with that, too."
    scene 10rehearsal06a with dissolve
    j "Well, then what are we waiting for? Let's go!"
    stop music fadeout 2.0
    scene black with fade
    "Soon you packed your stuff and went outside."
    play music "music/10 - Street's.ogg"
    scene 11start05 with dissolve
    mc "So... Let's do as we agreed. Go home, settle things, and then meet at Barry's."
    mc "You do remember where he lives, don't you?"
    jd "Yes, I do."
    mc "Okay, just checking."
    scene 11start07a with dissolve
    j "Oh, yeah! Remember that he has a pool. Make sure you bring your swimsuits!"
    scene 11start06a with dissolve
    jd "Don't worry, we won't forget."
    scene 11start06 with dissolve
    ls "*Giggle* And I'd love to take a swim in the pool!"
    scene 11start07 with dissolve
    mc "I like your optimism."
    scene 11start06 with dissolve
    ls "Mmm... Thanks!"
    scene 11start07 with dissolve
    mc "Okay, then let's not stay here any longer. See you soon."
    scene 11start06 with dissolve
    jd "See you later."
    ls "Yeah, I'll see you guys there."
    stop music fadeout 2.0
    jump day11_father


label day11_father:
    scene black with fade
    "Same time across town."
    play music "music/8 - Intro Music.ogg"
    scene 11father01 with dissolve
    "{color=#DC143C}Karen{/color}" "Look, I know I promised to discharge you in a week, but it's better if you stay here a bit longer and-"
    f "Thank you, Doc, but I'm okay."
    scene 11father02 with dissolve
    "{color=#DC143C}Karen{/color}" "Yes, you may be feeling better now, but with your illness there's always the risk of subsequent attacks."
    f "I hear you and I've taken that into account."
    "{color=#DC143C}Karen{/color}" "..."
    "{color=#DC143C}Karen{/color}" "Okay, but then, in addition to the medication, I would advise you to stick to the diet I told you about, as well as less stress and more rest."
    f "Less stress and more rest. Okay, I got it."
    "{color=#DC143C}Karen{/color}" "Uh... Then that's all I can do for you."
    "{color=#DC143C}Karen{/color}" "I hope I won't see you here again soon."
    f "Yes, I hope so, too."
    scene 11father03 with dissolve
    f "Don't get me wrong, Doc, I'm not going to risk my health for nothing."
    f "If I feel any worse, I'll ask for your help right away."
    f "Thank you again for your work, now I'll go."
    stop music fadeout 2.0
    scene black with fade
    "A few minutes later."
    play music "music/9 - You Can Make the Sound.ogg"
    scene 11father04 with dissolve
    f "{i}It's so good to be out again in the fresh air.{/i}"
    f "It's beautiful..."
    scene 11father04a with dissolve
    f "{i}If I understand correctly, my new assistant should wait for me somewhere near the parking lot.{/i}"
    f "{i}I hope he's not late. I'd hate to fire the poor guy right after I hired him.{/i}"
    scene 11father04b with dissolve
    "..."
    scene 11father05 with dissolve
    f "{i}Huh?{/i}"
    f "{i}What a surprise.{/i}"
    f "What are you doing here?"
    scene 11father05a with dissolve
    sis "And hello to you, too."
    sis "I just thought I'd take you out of here on my own."
    scene 11father05 with dissolve
    f "My new assistant was supposed to pick me up. Where is he?"
    scene 11father06 with dissolve
    sis "I contacted him and said I'd do it myself. He didn't mind."
    f "You got him out of his own work... Well, of course he didn't mind."
    scene 11father06a with dissolve
    sis "Hey, hey! What's with the grumbling, aren't you glad to see me?"
    f "Of course I'm glad."
    sis "That's great! Then get in the car and I'll drive you back home."
    f "Maybe you want me to drive?"
    scene 11father07 with dissolve
    sis "You better not argue and get in the car, or you'll take the bus."
    f "All I did was suggest..."
    sis "Yeah, I know."
    scene 11father07a with dissolve
    sis "But actually, in case you haven't noticed, I'm an adult now and I know how to drive. So let's just drop the subject."
    f "Well, if you say so. Then let's go."
    scene 11father08 with dissolve
    sis "By the way, what did the doctor tell you?"
    f "She told me to keep a certain diet, get some rest and less stress."
    sis "Hmm... Sounds reasonable. I suggest you follow these tips."
    f "I'll do what I can."
    sis "Okay, good."
    play sound "music/car_engine.mp3"
    scene 11father09 with dissolve
    "*Engine sound*"
    sis "All right, now I'm going to take you home."
    f "I appreciate it."
    scene 11father10 with dissolve
    "..."
    f "By the way, how are you doing with your business?"
    scene 11father10a with dissolve
    sis "Well... That's a pretty hard question."
    f "I'm in no hurry."
    sis "Yes... Yes, indeed. Okay, then listen..."
    scene black with fade
    "Some minutes later."
    scene 11father11 with dissolve
    sis "...so our growth in the last two months was just over five percent."
    f "Hmm. I didn't even realize you were doing so well."
    sis "And yet it is true."
    sis "You taught me everything. So I guess part of my success lies with you."
    f "That's good to hear."
    scene 11father14 with dissolve
    sis "Yeah."
    if day10_father_friends == True:
        scene 11father15 with dissolve
        sis "By the way, I heard that you and [mc] made up? Is it true?"
        scene 11father12 with dissolve
        f "It's hard to call it a full peace agreement. But we're taking steps in that direction."
        scene 11father15 with dissolve
        sis "That is great news!"  
        sis "You guys fought for so long about all that stuff, that I was starting to worry you might even stop talking to each other all together." 
        scene 11father11 with dissolve
        sis "You know, on this occasion, I have a special offer for you..."   
    else:
        scene 11father15 with dissolve
        sis "By the way, I heard that you tried to make up with [mc]? Is it true?"
        scene 11father12 with dissolve
        f "Yeah, but it didn't work out."
        scene 11father15a with dissolve
        sis "Hmm... I'm sorry to hear that."
        scene 11father11 with dissolve
        sis "But, you know, I have one good suggestion to help you solve this problem..."   
    
    f "What is it?"
    sis "Did you know he's having a gig tomorrow?"
    f "No, I didn't know that."
    sis "Well, there you go."
    sis "Since the doctor told you to rest more, how about we go there tomorrow? I'll even keep you company."
    scene 11father13 with dissolve
    f "I don't think that's a good idea."
    scene 11father15 with dissolve
    sis "Oh, come on!"
    sis "I've already been to his first show and I know what it is. I promise, it'll be fun."
    sis "You'll also see the reason you fought all this time."
    if day10_father_friends == False:
        sis "And you might even be able to make up." 
    sis "It wouldn't hurt you to get some air anyway."
    sis "So, what do you think?"
    scene 11father13 with dissolve
    f "..."
    scene 11father16 with dissolve
    f "Okay, I'll think about it."
    sis "Perfect! That's all I'm asking."
    stop music fadeout 2.0
    scene 11father10a with dissolve
    "The car rushed forward even faster, while the man and the woman continued their conversation."
    jump day11_home


label day11_home:
    scene black with fade
    "You used your free time to go home and change."
    play music "music/6 - Positive Mood.ogg"
    scene 11phone01 with dissolve
    mc "{i}Yeah, that's much better.{/i}"
    scene 11phone02 with dissolve
    mc "{i}But it looks like I still have some time.{/i}"
    mc "{i}Hmm... Maybe I should text somebody?{/i}"
    scene 11phone03 with dissolve
    "You sat on the bed and got your phone."
    $day11_phone_texts_anna=False
    $day11_phone_texts_lisa=False
    $day11_phone_texts_jane=False
    $day11_phone_texts_selina=False
    menu day11_phone_texts:
        "Text Anna" if anna_sex == True and anna_colleague == False and day11_phone_texts_anna==False:
            mc "{i}Given our new relationship with Anna, maybe I should ask how she's doing.{/i}"
            mc "{i}Yes, definitely.{/i}"
            mc "\"Hello, beauty. How's your day?\""
            "{cps=15}...{/cps}"
            a "\"Hello, [mc]!\""
            a "\"I was just about to go to the club.\""
            mc "\"So is this a bad time?\""
            a "\"I always have time for you. ;)\""
            mc "\"Awesome!\""
            a "\"Yeah... But it's too bad we can't meet up today.\""
            mc "\"That's for sure... I'd like to see you now.\""
            a "\"Hmm... This can be remedied.\""
            a "\"One moment.\""
            "{cps=15}...{/cps}"
            "*You have been sent an image*"
            scene 11phone04a with dissolve
            mc "{i}Wow... It's just that wow...{/i}"
            menu:
                "Approach the image":
                    scene 11phone04 with dissolve:
                        linear 6.0 yalign 1.0
                        linear 6.0 yalign 0.0
                        repeat 1
                    mc "{i}How lucky I am to have such a hot girlfriend.{/i}"                   
                "Leave it as it is":
                    "..."    
            scene 11phone03 with dissolve
            mc "\"I have no words. You're just amazing.\""
            a "\"Haha! Thank you.\""
            mc "\"What about tomorrow? Will you be able to come to my gig?\""
            a "\"I'm sorry, but I have a shift tomorrow, too.\""
            a "\"But if you want, you can perform in our club. I'll clear the hall for you. :D\""
            mc "\"lol\""
            mc "\"Maybe next time.\""
            a "\"Yeah.\""
            mc "\"Okay, I won't keep you any longer. It was nice chatting with you. XOXO\""
            a "\"Nice chatting with you, too. XOXO\""
            a "\"Bye, [mc].\""
            mc "\"Yeah, bye.\""
            scene 11phone03a with dissolve
            mc "{i}Hmm. I think it worked out pretty well.{/i}"
            mc "{i}And now I can go to Barry's with a clear conscience.{/i}"
            $day11_phone_texts_anna=True
            jump day11_phone_texts
        "Text Jane" if jane_date_offer == True and day11_phone_texts_jane==False:
            mc "{i}Given our new relationship with Jane, maybe I should ask how she's doing.{/i}"
            mc "{i}Yes, definitely.{/i}"
            mc "\"Hello, beauty. How's your day?\""
            "{cps=15}...{/cps}"
            jn "\"Mmm... Hello to you, too.\""
            jn "\"I'm doing pretty well, just got home from work. Now changing. Wanted to take a bath.\""
            mc "\"I wish I could take a bath with you right now. ;)\""
            jn "\"It's a very tempting offer, but I don't think you'll be able to get here fast enough.\""
            jn "\"Although... Here's a photo for you.\""
            "{cps=15}...{/cps}"
            "*You have been sent an image*"            
            scene 11phone05a with dissolve
            mc "{i}Wow... It's just that wow...{/i}"
            menu:
                "Approach the image":
                    scene 11phone05 with dissolve:
                        linear 6.0 yalign 1.0
                        linear 6.0 yalign 0.0
                        repeat 1
                    mc "{i}I still can't believe we're dating.{/i}"                   
                "Leave it as it is":
                    "..."    
            scene 11phone03 with dissolve               
            mc "\"Have I told you how beautiful you are?\""
            jn "\"Yes, but I wouldn't mind hearing it as often as possible.\""
            mc "\"Okay, you're beautiful.\""
            jn "\"Thank you, [mc].\""
            mc "\"What are you planning for tonight?\""
            jn "\"Brought a bunch of papers from work. I'm gonna need to check them all. It's boring.\""
            mc "\"Sorry to hear that.\""
            jn "\"That's fine.\""
            jn "\"What about you?\""
            mc "\"Promised I'd go to an old friend's place with my band. There's a gig tomorrow. Everybody needs some good rest.\""
            jn "\"Good for you. I hope you will rock tomorrow.\""
            mc "\"Will you come?\""
            jn "\"I'd like to, but I don't think I can. We're signing a new contract. I have to be there when it's signed.\""            
            mc "\"T_T\""  
            jn "\"I'll definitely come next time.\""
            mc "\"That's a promise?\""  
            "{cps=15}...{/cps}"             
            jn "\"Yes.\""
            mc "\"Then it's great! :D\"" 
            "{cps=15}...{/cps}"                
            jn "\"Sorry, but I'm gonna go. The tub is running over.\""
            jn "\"Have a good time. XOXO\""
            mc "\"Thanks. XOXO\""              
            mc "\"And I think you work too hard. Try to get some rest today.\""  
            jn "\"I'll try.\""
            mc "\"Goodbye, then.\""      
            jn "\"Bye.\""
            scene 11phone03a with dissolve
            mc "{i}Hmm. I think it worked out pretty well.{/i}"
            mc "{i}And now I can go to Barry's with a clear conscience.{/i}"
            $day11_phone_texts_jane=True
            jump day11_phone_texts
        "Text Selina" if selina_path == True and selina_broke_up == False and day11_phone_texts_selina==False:
            mc "{i}Given our new relationship with Selina, maybe I should ask how she's doing.{/i}"
            mc "{i}Yes, definitely.{/i}"
            mc "\"Hello, beauty. How's your day?\""
            "{cps=15}...{/cps}"
            s "\"Hey [mc]!\""
            s "\"I'm at the mall with my mom. We're trying on new clothes.\""
            s "\"Because of the divorce, she decided to refresh her wardrobe.\""
            mc "\"Oh, then can I see what you're wearing?\""
            s "\"Mmm... Only if you say please.\""
            mc "\"Pleeeease.\""
            s "\"*Giggle* Wait a minute.\""
            "{cps=15}...{/cps}" 
            "*You have been sent an image*"  
            scene 11phone07a with dissolve          
            mc "{i}Wow... It's just that wow...{/i}"
            menu:
                "Approach the image":
                    scene 11phone07 with dissolve:
                        linear 6.0 yalign 1.0
                        linear 6.0 yalign 0.0
                        repeat 1
                    mc "{i}I'm so damn lucky to be dating this girl.{/i}"               
                "Leave it as it is":
                    "..."
            scene 11phone03 with dissolve        
            mc "\"I just have to tell you how much that skirt suits you!\""
            s "\"You only liked the skirt? :(\""
            mc "\"Huh! Is someone fishing for compliments?\""
            s "\"Yep. :D\""
            mc "\"Well... Then you'll have to send me the photo just of you. With no clothes on.\""
            s "\"You're so sly!\""
            mc "\"Haha. Okay, don't worry, you're the prettiest girl in the world.\""
            s "\"Yes, I am! And thanks.\""
            "{cps=15}...{/cps}"
            s "\"Oh, sorry, gotta run. Mom's calling.\""           
            mc "\"Okay, have fun shopping.\""
            s "\"Thank you, [mc]! And bye.\""     
            mc "\"Bye.\""
            scene 11phone03a with dissolve
            mc "{i}Hmm. I think it worked out pretty well.{/i}"
            mc "{i}And now I can go to Barry's with a clear conscience.{/i}"
            $day11_phone_texts_selina=True
            jump day11_phone_texts
        "Text Lisa" if lisa_path == True and day11_phone_texts_lisa==False:
            mc "{i}I know I just hung out with her, but I miss her already.{/i}"
            mc "{i}Yeah, I should definitely text her.{/i}"
            mc "\"Hello, beauty. Did you get home yet?\""
            "{cps=15}...{/cps}"
            ls "\"Yeah. Just started changing.\""
            mc "\"Changing? How curious.\""
            ls "\"And what's curious about that?\""
            mc "\"Everything.\""
            mc "\"My imagination has already begun to paint the most spicy pictures.\""
            ls "\"Huh?\""
            ls "\"Then what will your imagination say about this?\""
            "{cps=15}...{/cps}"
            "*You have been sent an image*"  
            scene 11phone06a with dissolve          
            mc "{i}Wow... It's just that wow...{/i}"
            menu:
                "Approach the image":
                    scene 11phone06 with dissolve:
                        linear 6.0 yalign 1.0
                        linear 6.0 yalign 0.0
                        repeat 1
                    mc "{i}I'm so damn lucky to be dating this girl.{/i}"               
                "Leave it as it is":
                    "..."
            scene 11phone03 with dissolve
            mc "\"Okay. Reality is much, MUCH better.\""
            ls "\"*Giggle* That's what I thought.\""
            ls "\"Now stop distracting me and get dressed yourself.\""
            ls "\"See you in half an hour at Barry's.\""
            mc "\"Yeah, I'll meet you there. XOXO\""
            ls "\"Just don't be late! XOXO\""
            mc "\"It's a deal.\""
            scene 11phone03a with dissolve
            mc "{i}Hmm. I think it worked out pretty well.{/i}"
            mc "{i}And now I can go to Barry's with a clear conscience.{/i}"
            $day11_phone_texts_lisa=True
            jump day11_phone_texts
        "Continue":
            scene 11phone03a with dissolve
            mc "{i}Although, given the traffic jams, it's better to go right now.{/i}"
            mc "{i}Yes, definitely.{/i}"

    stop music fadeout 2.0
    jump day11_pool_party_pt01


label day11_pool_party_pt01:
    scene black with fade
    "Some time later, when you were on your way to Barry's house, you accidentally ran into Jade and Lisa."
    play music "music/12 - The Moose.ogg"
    scene 11poolparty00 with dissolve      
    ls "Hey, that's [mc]! We're here!"
    mc "{i}Huh. What a coincidence.{/i}"    
    scene 11poolparty00a with dissolve
    ls "Hello again!"
    mc "Yeah, hey."
    mc "It's a good thing we met here. We can go inside together."
    jd "It's really going to be better that way."
    jd "Lisa and I don't know this guy very well, so it's a lot easier if we're with you."
    mc "Yeah... I guess so."
    mc "Okay. You better tell me, are you ready?"
    scene 11poolparty00b with dissolve
    ls "I'm ready!"
    ls "But I just want to say that I'm in the mood for an easy time. I need to be fresh tomorrow."
    mc "{i}I guess that's pretty reasonable. After all, unlike us, her main instrument is her own voice.{/i}"
    scene 11poolparty00c with dissolve
    jd "I agree with Lisa."
    jd "Tomorrow is a big day. It's better for us to be fresh."
    mc "{i}So half of our band is on  easy vacation today. Well, so be it.{/i}"    
    scene 11poolparty00a with dissolve
    mc "You guys can do whatever you want, but I'm gonna have a real good time tonight."
    ls "Hmm... Whatever you say. Just don't get too drunk."
    mc "Huh. Believe me, I can hold my drink."
    ls "Mm-hmm. I hope so."
    scene 11poolparty01 with dissolve
    ls "Wow... It's like we were here just yesterday."
    jd "Only the last time we were here at night."
    mc "If you ask my opinion, it was a great night."
    if day09_lisa_jade_lewd == True:
        scene 11poolparty02 with dissolve
        ls "Um... Do you remember what we did on that balcony?"
        mc "I bet we'll never forget that."
        jd "I think we better focus on the current moment."
        ls "Ahem... Yeah, right."
    mc "Okay, let's just go inside. They must be waiting for us."
    play sound "music/doorbell.wav"
    scene black with fade
    "You rang the doorbell, and in a few moments Barry opened the door."
    stop sound fadeout 2.0
    scene 11poolparty03 with dissolve
    b "Whoa! You guys are finally here! It's so good to see you!"
    b "[mc]."
    mc "You look good, man."
    b "Yeah, it's mutual."
    scene 11poolparty04 with dissolve 
    b "And if I remember correctly, your names are Lisa and Jade. Is that right?"      
    ls "Yeah, that's right. And thank you for inviting us."
    jd "Yes. Thanks."    
    scene 11poolparty03 with dissolve
    b "Haha! You're welcome! [mc]'s friends are my friends."
    scene 11poolparty03a with dissolve
    b "Hmm... Wait a minute, shouldn't Jacob be with you?"
    mc "As you can see, there are only three of us."
    scene 11poolparty06 with dissolve
    jd "He'll probably come a little later with his new girlfriend."
    scene 11poolparty03a with dissolve
    b "Oh... That's right! He mentioned her on the phone."
    b "It'll be interesting to see his new passion."
    scene 11poolparty05 with dissolve
    ls "Believe me, we can't wait to meet this blue-haired seductress ourselves."
    scene 11poolparty03 with dissolve
    b "Haha! I have no doubt about that."
    scene 11poolparty07 with dissolve
    b "Okay, we've had a lot of chitchat here. Don't stand on the doorstep, go in the backyard. That's where we're hanging out right now."
    mc "{i}Did he say \"we\"?{/i}"
    mc "{i}But didn't Jacob say there wouldn't be anyone here but us?{/i}" 
    mc "{i}Although... Perhaps Barry meant his girlfriend, Stella?{/i}" 
    mc "{i}Yeah, that's gotta be it.{/i}" 
    mc "Then let's not stay here any longer. Come on, let's go."
    stop music fadeout 2.0
    scene black with fade
    "You followed Barry and after a few moments you were in his backyard."
    play music "music/10 - Street's.ogg"
    scene 11poolparty08 with dissolve
    ls "Wow! I almost forgot how awesome your place is!"
    jd "It may just be my imagination, but it feels like even the sun is brighter here."
    b "Heh! That's for sure! The sun's blazing here."
    mc "Yeah... Perfect weather to lie down by the pool for a while."
    ls "If you ask my opinion, the most important thing is not the place, but the company with which you spend time."
    b "Well said!"
    mc "Yeah, it's true."
    scene 11poolparty08a with dissolve
    mc "{i}Hey, wait a minute...{/i}"
    mc "{i}Right there... Don't tell me it's...{/i}" 
    scene 11poolparty09 with dissolve
    "There was no doubt, near the other end of the pool you saw Stella and your ex-girlfriend."
    "It seemed like they enthusiastically talked about something."
    mc "{i}Yeah, that's definitely Emma. I had no idea she would be here.{/i}"
    mc "{i}I don't even know if it's good or bad.{/i}" 
    if lisa_path == True and emma_sex == True:
        mc "{i}But given my relationship with Lisa and what happened between me and Emma not so long ago, that's definitely bad.{/i}"
        mc "{i}If I don't want to see a disaster here, I'll have to be as careful as possible.{/i}"
    scene 11poolparty11 with dissolve
    b "By the way, you ladies can go and get changed for now."
    scene 11poolparty12 with dissolve
    ls "Oh... Yeah, that's a good idea."
    ls "Where can we do that?"
    scene 11poolparty11 with dissolve
    b "Pick any spare room on the second floor and then come back."
    scene 11poolparty12 with dissolve
    ls "Okay, we'll be back soon."
    scene 11poolparty13 with dissolve
    "Jade and Lisa went upstairs and left you and Barry alone."
    scene 11poolparty09 with dissolve
    "Right after that, Stella and Emma noticed you."
    scene 11poolparty09a with dissolve
    mc "{i}They look so tempting in those swimsuits.{/i}" 
    if emma_sex == True:
       mc "{i}Especially Emma.{/i}"
    scene 11poolparty16 with dissolve
    st "Hey! [mc]! It's so great that you came!"
    st "Hurry up and come here!"
    mc "Haha. Thank you! We'll be right with you."
    b "Yeah, hold on one minute, baby."
    scene 11poolparty14 with dissolve
    b "Um... Sorry, I completely forgot about your relationship with Emma. I hope you don't mind her being here today."
    b "She became quite good friends with Stella. I hope you don't have a problem with that."
    mc "It's okay, we're all adults, we'll try to act normal."
    b "You're sure?"
    mc "Yeah, no problem."
    mc "Although next time, I'd like to know about such surprises in advance."
    b "Huh. I totally understand you."
    mc "Yeah..."
    b "Okay, enough standing here, we're already being stared at. Let's go and say hi."
    mc "Yeah, let's go."
    scene 11poolparty15 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    "After taking a few steps to the girls, you unwittingly looked at Emma."
    mc "{i}Man, even with everything that's happened between us, I still can't deny that girl's beauty.{/i}"
    if emma_sex == True:
        mc "{i}She's gorgeous.{/i}" 
        scene 11poolparty17 with dissolve
        "Suddenly for everyone, Emma rushed into your arms."
        em "[mc]!"
        mc "{i}Hey, what the hell?!{/i}"
        scene 11poolparty18 with dissolve
        em "I had no idea you'd be here. This is a very nice surprise!"
        mc "Um... Yeah, you can't argue with that, it's really a surprise."
        menu:
            "Check her out":
                scene 11poolparty20 with dissolve
                "You carefully move your eyes down."
                mc "{i}Wow... This swimsuit looks even better up close.{/i}" 
                scene 11poolparty19 with dissolve
                mc "{i}And the back of it looks just as good.{/i}"
                mc "{i}She's definitely in shape.{/i}" 
            "Focus on the conversation":
                mc "{i}It's better if I concentrate on the conversation.{/i}"
        scene 11poolparty21 with dissolve
        mc "Hey, let's not forget that we're not alone here."
        scene 11poolparty21a with dissolve
        em "Yeah, you're right."
        em "I'm sorry for such a strong reaction."
        em "Considering everything that happened between us, it was inappropriate."
        mc "It's okay."
        scene 11poolparty21 with dissolve
        em "It's just... I just want you to know that it's good to see you again."
        mc "Yeah, it's good to see you, too."
        scene 11poolparty22 with dissolve
        "Moments later, Emma silently stepped aside."
        st "I'm impressed."
        st "It's so cool that after everything that's happened between you two, you get along so well with each other."
        scene 11poolparty24 with dissolve
        b "Yes... Come to think of it, these two have quite the story."
        scene 11poolparty25 with dissolve
        em "I think you're exaggerating."
        em "There have never been any conflicts between us before, it's just that our relationship was a bit confusing."
        scene 11poolparty23 with dissolve
        mc "Ahem! Let's not stir up the past."
        mc "We are gathered here today to enjoy the present. And it looks like a great day to me."
        scene 11poolparty24a with dissolve
        b "Whatever you say, dude. Let's enjoy the present."
    else:
        scene 11poolparty22 with dissolve
        st "You know, even though we've only recently met, I feel like we've known each other a long, long time."
        st "It's funny, but with Emma, I felt exactly the same way."
        scene 11poolparty24 with dissolve
        b "Is it me, or did you say the same words to me on our second date?"
        scene 11poolparty22 with dissolve
        st "It's just your imagination."
        scene 11poolparty24 with dissolve
        b "Yeah, that's what I thought."
        scene 11poolparty23 with dissolve
        mc "Even if we don't know each other that well, I'd be happy to fix that."
        st "Oh, I'm looking forward to it!"
        mc "And, Emma, it's good to see you here, too."
        scene 11poolparty25 with dissolve
        em "It's mutual, [mc]."
        scene 11poolparty24a with dissolve
        b "Hmm... It's cool that after everything you've had, you get along so well."
        scene 11poolparty25 with dissolve
        em "It's okay. We have no reason to be mean to each other."
        mc "I agree."
    
    stop music fadeout 2.0
    play sound "music/doorbell.wav"
    scene 11poolparty26 with vpunch
    "*Ding-dong!*"
    stop sound fadeout 2.0
    b "Oh... That must be Jacob."
    b "I'll go let him in."
    mc "No problem, man."
    scene 11poolparty27 with dissolve
    "Barry left, leaving you with Stella and Emma."
    scene black with fade
    "You talked to girls about stuff for a while."

    if day09_lisa_jade_lewd == True:
        "Same time in the house."
        play music "music/8 - Intro Music.ogg"
        scene 11girlstalk01 with dissolve
        ls "I can't believe you picked the same room where we and [mc]... *cough*"
        ls "Well, you remember very well what the three of us were doing here."
        jd "I didn't choose this room on purpose, it was the first one I saw."
        ls "*Giggle* Relax, I'm just teasing you."
        scene 11girlstalk02 with dissolve
        ls "By the way, have you thought about this whole situation we're in?"
        scene 11girlstalk03 with dissolve
        jd "Which one?"
        scene 11girlstalk02 with dissolve
        ls "Well, this whole triple relationship thing."
        scene 11girlstalk03a with dissolve
        jd "Oh, that one... Yes, I've been thinking about it a little bit."
        scene 11girlstalk03 with dissolve
        jd "But first, I'd like to know your opinion."
        jd "After all, it was you guys who got me into this."
        scene 11girlstalk05 with dissolve
        ls "That's fair enough."
        ls "To be honest, I'm a bit of a jealous person, so this is a very difficult topic for me."
        ls "The thing is, I like [mc] and you a lot. Although, he likes you and me, too."
        ls "There's probably something kinky about all this, but it really turns me on."
        scene 11girlstalk04 with dissolve
        ls "Uhh... But I can't deny the fact that this is all getting too confusing."
        ls "I think we should come up with some rules."
        scene 11girlstalk03 with dissolve
        jd "That's probably a good idea."
        ls "You think so?"
        jd "Definitely."        
        scene 11girlstalk04 with dissolve
        ls "We need to make sure that there will be no jealousy or misunderstandings between us. Because otherwise, we'd better stop this whole thing right now."
        ls "Personally, I wouldn't want the people I care about making secrets behind my back."
        scene 11girlstalk07a with dissolve
        ls "You're not going to do that to me, are you?"
        scene 11girlstalk06 with dissolve
        jd "A-absolutely not! There's no way I-"
        scene 11girlstalk07 with dissolve
        ls "Haha! Relax, I know you're not that kind of person."
        scene 11girlstalk05 with dissolve
        ls "But still, I don't want any secrets between us."
        ls "Even if you suddenly decided to... *cough* have fun with [mc] alone, then after that, you'll have to tell me about it."
        scene 11girlstalk07a with dissolve
        ls "It's the only way to do it."
        ls "And, of course, that goes for me, too. I will stick to my own rules."
        ls "So, what do you think?"
        scene 11girlstalk08 with dissolve
        jd "I think you came up with a good idea."
        jd "If we're honest with each other, everything will be fine."
        scene 11girlstalk07 with dissolve
        ls "Exactly! And everyone will be happy!"
        scene 11girlstalk08 with dissolve
        jd "Yes... I agree."
        scene 11girlstalk09 with dissolve
        ls "That's great! And now that we're finished here, let's go to the others."
        ls "It's time for fun!!!"
        jd "Mm-hmm... That's right."
        stop music fadeout 2.0
        scene black with fade
        "One minute later."

    play music "music/12 - The Moose.ogg"
    scene 11poolparty28 with dissolve
    st "Oh, look, I think we got new faces here."
    em "If I'm not mistaken, they came with [mc]."
    mc "Hmm?"
    scene 11poolparty29 with dissolve
    "Dressed in swimsuits, Lisa and Jade were headed your way and talking about something very funny."
    mc "{i}So Emma noticed that we came together. That's interesting.{/i}"
    mc "{i}But now I need to introduce them to each other officially.{/i}"
    scene 11poolparty30 with dissolve
    mc "Emma, Stella, meet my friends and members of the music band [band_name] Lisa and Jade."
    st "Nice to meet you guys."
    st "Since I have already seen the video of your last gig, you can consider me as one of your fans."
    ls "*Giggle* We always welcome new fans!"
    ls "It's also very nice to meet you too."
    jd "Yes, it's very nice to meet you. Stella. Emma."
    em "It's mutual."
    scene 11poolparty32 with dissolve
    ls "So, what are you guys doing here?"
    scene 11poolparty31 with dissolve
    em "There are many choices. You can swim in the pool, you can sunbathe, or you can go inside and get yourself something to drink."
    em "Now, if you'll excuse me, I want to go sunbathe."
    em "I'd really appreciate it if you wouldn't bother me for a while."
    mc "{i}Is it just me, or did she sound pretty cold?{/i}"
    scene 11poolparty36 with dissolve
    ls "Um... Yes, of course. You don't have to worry, we won't bother you."
    scene 11poolparty31 with dissolve
    em "Thank you."
    scene 11poolparty33 with dissolve
    mc "Hey, is everything okay?"
    scene 11poolparty34 with dissolve
    em "Everything's fine, just a sudden headache."
    em "But don't worry, I think my martini will help me with that."
    mc "Hmm. Whatever."
    mc "{i}I wonder if it's some form of jealousy, or is she really in a bad mood?{/i}"
    scene 11poolparty35 with dissolve
    "Emma wore sunglasses, layed down on the sunbed, and began slowly sipping her drink."
    mc "{i}Looks like she's doing pretty well.{/i}"
    scene 11poolparty36 with dissolve
    ls "Um... I don't know why, but I don't think she likes me."
    scene 11poolparty37 with dissolve
    mc "Just ignore her. Sometimes she can be a pain in the ass."
    scene 11poolparty32 with dissolve
    ls "Really? Seems like you know a lot about her."
    ls "How did you guys meet?"
    scene 11poolparty37a with dissolve
    mc "Oh... Well, that's not a simple question."
    mc "At first we lived in the same neighborhood and went to the same school, and then-"
    stop music fadeout 2.0
    scene 11poolparty38 with dissolve
    b "Here we are!"
    play music "music/7 - Just Happy.ogg"
    mc "{i}Barry got here just in time.{/i}"
    mc "{i}It's not that I'm afraid to talk about my old relationship with Emma, but I would like to postpone that moment as long as possible.{/i}" 
    j "I hope we haven't missed anything interesting?"
    b "You're just in time, the other guys just got here."
    j "Awesome!"
    ru "If so, let's not keep them waiting. Come on!"
    b "Yeah, let's go."
    scene 11poolparty39 with dissolve
    j "Hey, guys! It's good to see you all again! Like I told you, I didn't come alone."
    mc "Yeah, well... We can see that."
    mc "{i}I should give Jacob credit, he found himself a very pretty girlfriend.{/i}"  
    scene 11poolparty40 with dissolve
    j "Okay, I want you to meet Ruby."
    ru "Nice to meet you guys. Jacob has told me a lot about you."
    mc "Oh, believe me, he told us as much about you too."
    scene 11poolparty40a with dissolve
    ru "Really?! And what exactly did he say about me?"
    mc "{i}Wow, she's pretty curious.{/i}"
    mc "Basically, he said how great you are and how lucky he was to find you."
    ru "Oh... That's very nice to hear."
    scene 11poolparty41 with dissolve
    j "But it's pure truth! Look at this beautiful girl. Can anyone resist her at all?"
    ru "Oh, come on, stop it."
    j "No, no, I'm talking very seriously. When I met you, I became the happiest man on the planet."
    ru "Right after me."
    j "Huh. We'll consider you and I equally happy."
    ru "Mmm... It's a deal."
    scene 11poolparty42 with dissolve
    ls "You have such a lovely relationship. I'm very happy for you."
    ru "Oh, thank you! But we'll try not to confuse you with our silly talk."
    ls "Don't worry about it, we're used to Jacob's fooling around. But at least now it's heading in the right direction."
    j "Hey, I can hear you!"
    ls "Uh-huh, I know that."
    "{cps=15}...{/cps}"
    jd "We heard you were coming to our gig tomorrow. Is that true?"
    ru "Absolutely!"
    ru "I love music, and I think there's nothing better than listening to it live. Not to mention, that my new boyfriend is in a rock band."
    ru "So tomorrow, I'll be cheering you on from the audience."
    ls "Sounds good."
    scene 11poolparty43 with dissolve
    st "Barry, I think many of our guests will be thirsty in this heat."
    st "Why don't you take one of the boys and bring a case of beer?"
    scene 11poolparty43a with dissolve
    b "I was just thinking about that myself."
    st "Yeah, sure."
    scene 11poolparty44 with dissolve
    b "[mc], while everyone is chatting, shall we go inside for a beer?"
    mc "For a beer?"
    b "Yeah, it's a big box. Let's bring it here together."
    mc "Oh, sure, why not."
    b "Okay, great. Let's go."
    stop music fadeout 2.0
    scene 11poolparty45 with dissolve
    "You and Barry went to the house."
    play music "music/8 - Intro Music.ogg"
    scene 11poolparty46 with dissolve
    b "Okay, here's our small gold chest."
    mc "Huh. What a name you came up with for it."
    b "Doesn't sound good?"
    mc "Nah, it's okay. After all, it's not the title that matters, it's the content that matters."
    b "That's for sure! Then how about we have a bottle right here?"
    mc "It's a good offer. I'm in!"
    b "Haha! Great!"
    scene 11poolparty47 with dissolve
    b "Then let's take two bottles from here."
    scene black with fade
    "Barry gave you a bottle of beer."
    scene 11poolparty48 with dissolve
    b "Cheers to the meeting!"
    mc "To the meeting, bro."
    scene 11poolparty49 with dissolve
    b "So, what's new with you? Are you dating anybody now?"
    mc "{i}What should I say to him?{/i}"
    menu:
        "You're dating Anna" if anna_sex == True and anna_colleague == False:
            mc "Who am I dating?"
            mc "On my new job, I have a boss, a hottie, and somehow I happen to be having an affair with her."
            scene 11poolparty49c with dissolve
            b "Wow, are you dating your boss? That's pretty exciting."
            mc "Yeah, I guess... I've never had that kind of experience before."
            b "I can imagine you've stayed more than once after your shift to do... *cough* extra work with her..."
            mc "Haha! I can neither confirm it nor deny that."
            scene 11poolparty49 with dissolve
            b "Huh. I see."
            b "Well, happy for you!"
            mc "Thanks, man."

        "You're dating Jane" if jane_date_offer == True:
            mc "Who am I dating?"
            mc "Do you remember my big sister's best friend? Her name was Jane."
            scene 11poolparty49a with dissolve
            b "That stunning hottie who was blowing off guys left and right? Of course I remember her."
            scene 11poolparty49 with dissolve
            b "And why do you ask-"
            scene 11poolparty49b with dissolve
            b "Wait! No way!"
            b "Don't tell me you and her are together now?"
            mc "Yep. That's right."
            scene 11poolparty49c with dissolve
            b "Haha! Goddamn it, I can't believe you managed to charm that girl!"
            b "I mean, she's a fucking sex bomb, and she is also awesomely smart. You're so lucky."
            mc "Yeah, I'm well aware of that myself."
            scene 11poolparty49 with dissolve
            b "If Stella wasn't dating me right now, I would definitely be jealous of you..."
            scene 11poolparty49c with dissolve
            b "But I wish you good luck with her!"
            mc "Yes, I could use some luck right now."

        "You're dating Lisa" if lisa_path == True:
            $ day11_barry_knows_about_lisa = True
            mc "Who am I dating?"
            mc "Well, actuality, you've already met my new girlfriend."
            scene 11poolparty49a with dissolve
            b "Hmm? I already know her?"
            mc "Yeah."
            scene 11poolparty49 with dissolve
            b "Is it someone from our past?"
            mc "Nope."
            b "Hmm... Sorry, but no one comes to my mind."
            mc "I'll give you a hint, it's is our rock band's vocalist."
            scene 11poolparty49b with dissolve
            b "No fucking way! You and Lisa?!"
            mc "Yep."
            scene 11poolparty49c with dissolve
            b "Haha! Holy shit! I didn't even think about that."
            b "Does Jacob know about this?"
            if jacob_knows_about_lisa == True:
                mc "Yeah, I already told him."
            else:
                mc "I didn't tell him about it, but I wouldn't be surprised if he figured it out."
            b "Well, that's news."
            scene 11poolparty49 with dissolve
            b "Aren't you afraid of the situation that if you have conflicts, your whole band might fall apart?"
            mc "Yeah, we know that. But we took that risk anyway."
            mc "It's hard to describe in words, but we're attracted to each other like magnets."
            scene 11poolparty49c with dissolve
            b "Well, anyway, I'm happy for you!"
            mc "Thanks, man."

        "You're dating Selina" if selina_path == True and selina_broke_up == False:
            mc "Who am I dating?"
            mc "There's this girl who lives next door to me and works as a doctor at a local hospital."
            mc "She's young, redheaded and very pretty."
            scene 11poolparty49a with dissolve
            b "Doctor? And a redhead? How fascinating."
            scene 11poolparty49 with dissolve
            b "I know a few girls like that, and they're all completely crazy. No exceptions."
            mc "Well, at first she seemed to me like you just described your acquaintances. But when I got to know her a little better, I realized she was completely different."
            mc "She's a very sweet and sincere girl."
            b "Really?"
            mc "Yeah, she's really cool."
            scene 11poolparty49c with dissolve
            b "Well, I guess there are exceptions to any rule."
            b "Anyway, I'm happy for you, man!"
            mc "Haha. Thanks."

        "You date a few girls at once" if lisa_path == True and selina_path == True and anna_sex == True and jane_date_offer == True:
            mc "To tell you the truth, it's very complicated. I'm dating a few girls at once right now."
            scene 11poolparty49b with dissolve
            b "Seriously?"
            mc "Yeah..."
            b "Dude! Not cool. Not cool at all."
            mc "I know that very well myself, and that makes me feel like a real asshole."
            scene 11poolparty49c with dissolve
            b "Huh. I bet you do."
            b "Aren't you afraid that somehow they'll find out about each other?"
            mc "I'm trying to stay confident, but it's kinda hard."
            mc "Besides, I have a strong feeling this isn't going to end well."
            scene 11poolparty49 with dissolve
            b "Well, it usually doesn't."
            mc "Yeah."
            mc "Okay, I'd rather not think about it right now and not spoil my mood."
            scene 11poolparty49a with dissolve
            b "Yeah, it's a good option..."
            b "But I wouldn't advise you to drag it out. It's better to solve this right now before you get in any trouble."        
            mc "Yeah, I'll think about it myself."

        "You're alone":
            mc "No, I'm not dating anyone right now."
            scene 11poolparty49c with dissolve
            b "Huh. I see. So you're a proud loner."
            b "When the glory of a famous rock star is ahead of you, it's better to stay free. In that case, hot girls will never leave you alone."
            mc "Exactly!"
            b "Huh. Cool."

    scene 11poolparty50 with dissolve
    b "Okay, we're talking too much. Let's take this beer case and go to the others."
    stop music fadeout 2.0
    scene black with fade
    "A few minutes later."
    play music "music/10 - Street's.ogg"
    scene 11poolparty51 with dissolve
    "When you went back to the pool, you noticed that the girls were already sunbathing."
    mc "{i}Wow... I can't even see straight from such a crowd of beauties.{/i}"  
    ls "Finally you're back. Jacob was looking for you."
    mc "{i}Jacob? I wonder what he wanted?{/i}"  
    scene 11poolparty57 with dissolve
    j "Hey! Guys, I'm here!"
    j "While you were walking around, I decided not to waste any time and pulled out the volleyball net that Stella told me about."
    j "How about a game of water volleyball?"
    mc "{i}Huh. They really didn't waste any time here.{/i}"
    scene 11poolparty58 with dissolve
    j "So, i hope you don't mind a little sports competition?"
    j "I didn't just pull that net out for nothing, did I?"
    scene 11poolparty60 with dissolve
    "You put up a case of beer and thought."
    scene 11poolparty63 with dissolve
    b "Well, it's not such a bad idea."
    b "There are exactly eight of us. That makes four on four."
    scene 11poolparty59a with dissolve
    j "That's right, dude! This is gonna be awesome! We'll split up into two teams and have a small friendly match."
    j "It's much better than just laying around drinking beer."
    j "All we have to do is convince the girls to join us."
    scene 11poolparty52 with dissolve
    ru "I don't need to be convinced. If Jacob plays, so do I."
    ru "But only on the condition that we will be on the same team."
    scene 11poolparty59a with dissolve
    j "Of course we're on the same team, babe! You and I are the best team you could ever dream of."
    scene 11poolparty61 with dissolve
    mc "{i}Hmm. I was a little skeptical about Jacob's new love at first, but it looks like these two really fit together.{/i}"
    mc "{i}And that's great. Despite all his fidgeting, Jacob has earned a strong happy relationship.{/i}"
    scene 11poolparty65 with dissolve
    b "Perfect! Now there's three of us!"  
    scene 11poolparty54 with dissolve
    ls "If you're really going to play, I'll join you too."
    ls "It'll be nice to stretch out a little in the water."
    b "Excellent, that's four."
    scene 11poolparty55 with dissolve
    st "So you really want to play this stupid game?"
    st "Why don't you just lie here in the sun and do nothing?"
    scene 11poolparty65 with dissolve
    b "Well, no, my dear Stella, you can't get rid of me so easily."
    b "I know you play well, which means you'll be on my team."
    b "Am I right?"
    scene 11poolparty64 with dissolve
    st "Yeah, yeah... What am I going to do if my boyfriend is so stubbornly selfish."
    scene 11poolparty65 with dissolve
    b "Haha. Thank you, you won't regret it."
    scene 11poolparty64 with dissolve
    st "Yes, I really hope so."
    scene 11poolparty53 with dissolve
    jd "Um... I'm not a good volleyball player, but if everyone agrees, I'd be happy to play too."
    b "Great! One more player!"
    scene 11poolparty65 with dissolve
    b "What about you, Emma?"
    b "You're not gonna turn us down for this game, are you?"
    scene 11poolparty56 with dissolve
    em "Well... That's a very interesting proposal."
    em "I think I'll play."
    em "But only if I'm on a team with [mc]. Is that okay?"
    b "Deal!"
    em "Then count me in."
    scene 11poolparty62 with dissolve
    b "So what about you, [mc]?"
    b "As you can see, everyone has already agreed."
    b "Will you be captain of the second team?"
    scene 11poolparty62a with dissolve
    mc "Huh? Are you trying to tell me that you and Jacob will be on the first one?"
    b "Well, yeah. The first team is me, Stella, Jacob and Ruby. And second, you and all the other girls."
    mc "It doesn't seem very balanced."
    b "Oh, come on! You're not afraid of a little competition, are you?"
    mc "{i}Did he just dare me?{/i}"
    scene 11poolparty59 with dissolve
    j "If Barry and I are together, victory is almost in the bag."
    scene 11poolparty66 with dissolve
    ls "Don't bite off more than you can chew."
    ls "I'm pretty sure we and [mc] will still be able to surprise you."
    mc "{i}She speaks very confidently. Maybe she's good at volleyball.{/i}"
    scene 11poolparty62a with dissolve
    b "So, you're in?"
    scene 11poolparty67 with dissolve
    mc "{i}Hmm... On the one hand, the opposing team will be very strong and the chance to lose to them is quite high.{/i}"
    mc "{i}But, on the other hand... It`s just a game. So why not?{/i}"
    scene 11poolparty67a with dissolve
    mc "Goddamn it, why not!"
    mc "I'm in."
    b "Haha! That's great!"
    scene 11poolparty68 with dissolve
    j "You do realize that in the current scenario you have no chance of winning, right?"
    ru "Don't say that, after all, there are four of them and us."
    b "Yeah, well, mathematically speaking, our chances are equal, but as for practice... Heh. We'll see."
    scene 11poolparty69 with dissolve
    mc "You talk too much. Let's see how you will act in the game."
    ls "That's right. With this game we will teach you a good lesson in manners!"
    em "Besides, it's very naive to think that you'll win just because you have two boys on the team."
    jd "..."
    scene 11poolparty68 with dissolve
    st "Okay, let's not argue and just start playing."
    scene 11poolparty70 with dissolve
    "Your team started to take their side of the pool."
    mc "Okay, ladies, before we start, I suggest we discuss our strategy."
    mc "Gather around me."
    scene 11poolparty71 with dissolve
    "A few seconds later, you stood next to each other with a tight ring."
    mc "So, first of all, we must admit that there are very good players on their side."
    mc "I take it Jade is new to this game?"
    jd "Yeah, that's right."
    jd "I know the rules, but I don't have much experience. Don't count on me too much."
    mc "Okay, I hear you. We'll figure something out."
    mc "What about the rest?"
    scene 11poolparty72 with dissolve
    ls "In high school I spent two years playing volleyball, so I have some good experience in this game."
    ls "Although we didn't play in water back then, but... But that's nothing. It's still the same thing."
    mc "Okay, that's really good."
    mc "And what about you, Emma?"
    em "Well... I'm not a professional, but I can play. You can count on me."
    mc "Okay, I got it."
    scene 11poolparty73 with dissolve
    b "Hey, hey! How long are you gonna be whispering over there?! We're waiting for you here, by the way."
    j "Yes, guys, let's get started."
    scene 11poolparty74 with dissolve
    ls "Actually, we're just about done and ready to kick your arrogant asses."
    scene 11poolparty75 with dissolve
    st "Oh, I see someone's taking it very seriously."
    st "Then I'll have to do my best, too."
    scene 11poolparty74 with dissolve
    ls "Huh? Didn't you call the game stupid a couple of minutes ago?"
    scene 11poolparty75 with dissolve
    st "Mmm... I guess your enthusiasm was very contagious."
    st "And now let's get started!"
    "*Cheerful screams from all sides*"
    scene 11poolparty76 with dissolve
    "Stella threw the ball in the air..."
    scene 11poolparty77 with vpunch
    "...and hit him!"
    "The game has begun."
    stop music fadeout 2.0
    scene black with fade
    "Some time later."
    "In a completely unthinkable way your score was leveled and the next point was to decide the game."
    play music "music/8 - Intro Music.ogg"
    scene 11poolparty78 with dissolve
    mc "Okay, so far we've been doing pretty well, which means we should play just like before."
    mc "Emma and Jade, you have a long line of defense."
    em "Whatever you say, cap."
    jd "Yeah, we got it."
    mc "And you, Lisa, you're gonna-"
    ls "I'll take over Barry."
    "{cps=15}...{/cps}"
    mc "Are you sure? He's a very serious player."
    ls "I know he plays great, but you can count on me."
    mc "{i}She's proved herself pretty good in this game, which means she has a very good chance against him.{/i}"
    mc "Okay, you're blocking Barry."
    mc "And I will act on circumstances."
    scene 11poolparty79 with dissolve 
    ru "Looks like it's my turn to serve."
    ru "Is everyone ready?"
    j "Crush them, babe!"
    mc "Yeah, we're ready. Go ahead."
    ru "Okay."
    stop music fadeout 2.0
    scene 11poolparty80 with dissolve 
    "The next second, Ruby made a serve."
    play music "music/11 - Pop Energy.ogg"
    scene 11poolparty77 with vpunch
    $renpy.pause(0.2, hard=True)
    scene 11poolparty81 with dissolve
    "Emma took the serve right away."
    scene 11poolparty83 with dissolve
    "The ball flew to the opponent's side."
    scene 11poolparty82 with dissolve
    "And then, you noticed Barry trying to end it with one sharp move."
    mc "{i}Fuck! He's fast, I'm not sure if Lisa can take that ball.{/i}"
    menu:
        "Leave the ball to Lisa (+Lisa)":
            $ RPls += 1
            $ goodpoint += 1
            mc "{i}I should trust her. She's an experienced player and she has to deal with it on her own.{/i}"
            scene 11poolparty84 with dissolve
            "With lightning speed, Lisa rushed for the ball."
            ls "I'll catch it!!!"
            scene 11poolparty84a with vpunch
            $renpy.pause(0.5, hard=True)
            scene 11poolparty83 with dissolve
            "The ball soared high into the sky and you have the perfect chance to score the next point."
            mc "{i}I knew she could do this!{/i}"
            mc "{i}Now it's my turn.{/i}"
            scene 11poolparty86 with vpunch
            "You hit the ball with all your strength..."
            play sound "music/water_splash.wav"
            scene 11poolparty87 with dissolve
            "..."
            scene 11poolparty88b with dissolve
            ls "Hey, did we... Did we really win?"
            mc "Yeah, we won."               
            scene 11poolparty89 with dissolve
            ls "Hahaha! We won! Yay, victory!!!"
            ls "We are awesome!!! We're the best!!!"
            scene 11poolparty88 with dissolve
            ls "That ball, you saw it, right?!"
            ls "At first I thought I wouldn't have time to hit it, but then... Then I hit it, and you... That spike!"
            ls "WOW! That's just a bomb!"
            mc "Haha! Okay, relax, it's over."
            ls "Phew... Yes... I need to calm down..."
            scene 11poolparty90 with dissolve
            "You looked back and realized that even Emma and Jade were happy about this sudden victory."
            em "Haha! We did a great job, girl!"
            jd "Yes... It was a good game."
            scene 11poolparty91a with dissolve
            "But somebody else wasn't so happy about it."
            b "Okay, congratulations. You win. You did good."
            ru "Yeah, it was a nice game."
            j "Uh... This is so sad. The victory was so close."
            scene 11poolparty92a with dissolve
            em "This will be a lesson to you! Next time, try not to underestimate your opponents."
            scene 11poolparty93a with dissolve
            b "Yeah, yeah, we already figured that out."
            b "Now let's finish up here and take a break."

        "Try to take the ball yourself":
            $ badpoint += 1
            mc "{i}It's better not to take any chances and do it myself.{/i}"
            scene 11poolparty85 with dissolve
            "At the same time, you and Lisa rushed for the ball."
            ls "I'll catch it!!!"
            mc "{i}Damn it, she's right in my way!{/i}" 
            play sound "music/water_splash.wav"                       
            scene 11poolparty87 with dissolve
            "..."
            mc "{i}Fuck!{/i}"
            scene 11poolparty88a with dissolve
            ls "And what was that? I told you, I'm taking over Barry."
            mc "{i}She's right, it's my fault.{/i}"             
            mc "Yeah, sorry... It's just reflexes."
            ls "Well, congratulations, now we've lost."
            scene 11poolparty91 with dissolve
            "You noticed that the opposing team is already celebrating their victory."
            b "Well done, guys!"
            j "Yeah, man, we won!"
            st "Good game, Ruby."
            ru "You played great, too."
            scene 11poolparty92 with dissolve
            em "All right, all right, we get it, you win. Congratulations to you."
            em "Now let's finish this show and move on to sunbathing."
            scene 11poolparty93 with dissolve
            b "Don't be mad, Emma. You played great, too."
            scene 11poolparty92 with dissolve
            em "It doesn't matter."             
            scene 11poolparty93 with dissolve
            b "Okay, you're right. Let's go get some rest."

    stop music fadeout 2.0
    scene black with fade
    "When it was over, everyone split up into small groups and started doing their own thing."
    play music "music/6 - Positive Mood.ogg"
    scene 11poolparty95 with dissolve
    "Jacob and Ruby went into the house to talk to each other alone."
    scene 11poolparty94 with dissolve
    "Emma was swimming in the pool."
    scene 11poolparty96 with dissolve
    "And the rest of the guys were sitting next to each other, drinking alcohol and having fun talking about something."
    scene black with fade
    "It's time to decide what I should do."
    mc "{i}Where should I go? Should I Swim with Emma or join the guys?{/i}"
    menu:
        "Join Emma" if not emma_sex:
            stop music fadeout 2.0
            jump day11_emma_sex
            
        "{color=#66FF33}Join Emma{/color}" if emma_sex:
            stop music fadeout 2.0
            jump day11_emma_sex
            
        "Join the guys":
            "After some thought, you decided to join the guys."
            stop music fadeout 2.0
            jump day11_pool_party_pt02


label day11_emma_sex:
    if _in_replay:
        $emma_sex=True
        $ setReplay()
    "After some thought, you decided to join Emma."
    play music "music/2 - Bad.ogg"
    scene 11emma01 with dissolve
    "When you got to her, you realized that she was enjoying the silence."
    mc "I see you're having a good time."
    scene 11emma02 with dissolve
    em "Hmm? Did you say something?"
    mc "I was impressed with how well you're settling in here."
    em "Oh, that..."
    em "Well, it's pretty good here. You can finally relax and forget about all the problems."
    em "Exactly what I need right now."
    scene 11emma03 with dissolve
    mc "Do you mind if I join you? We can relax together."
    em "That's an interesting offer. I don't see any reason to object it."
    mc "Okay, thanks."
    scene 11emma06 with dissolve
    if emma_sex == True or _in_replay:
        mc "You know, for some reason, I remembered how happy you were when you saw me today."
        mc "It was a bit weird, but at the same time it was very nice."
        mc "What's got into you?"
        scene 11emma07 with dissolve
        em "Oh, come on! Don't pretend to be stupid, you've got it all figured out."
        mc "Maybe... But I'd like to know what you think about it."
        scene 11emma07a with dissolve
        em "What do I think about it?"
        "..."
        em "I don't know. Really."
        em "Probably it's just scraps of my old feelings. Something inside me still loves you... Like I used to."
        em "I know it sounds ridiculous, especially since we're both responsible for our breakup. But still, it is..."
        mc "{i}It was very frank.{/i}"
        mc "{i}But for me, it's hard to say how I feel about it.{/i}"
        em "Uh... Sorry, but I need a drink."
        scene 11emma04 with dissolve
        "Emma reached for a glass of martini."
        scene 11emma05 with dissolve
        em "Yeah, that's much better."
        mc "{i}She looks a little tense about this conversation.{/i}"
        mc "{i}Maybe I should cheer her up.{/i}"
        menu:
            "Cheer up Emma (Emma scene)":
                scene 11emma08 with dissolve
                mc "Hey. I think you're pushing yourself too hard about this."
                mc "How about a moment of relaxation? Forget about the past and enjoy the current moment."
                mc "Just like the old times."
                scene 11emma09 with dissolve
                "You swam up close to Emma and gave her a gentle hug."
                em "Did you know you're giving very strange unambiguous signs?"
                em "I'm a bit confused about how I should react to it."
                scene 11emma10 with dissolve
                em "Especially when our friends are around."
                mc "Well, I think they're in the middle of a conversation right now and aren't paying attention to us."
                em "So what do you suggest?"
                scene 11emma11 with dissolve
                "You pressed tight against Emma and your hands slipped down on her perfect waist."
                em "Mmm... I think I'm starting to guess."
                scene 11emma12 with dissolve
                mc "Don't tell me you don't like it."
                em "I won't."
                mc "That's what I thought."
                scene 11emma13 with dissolve
                "Emma turned around and hugged you."
                em "Seems like you're in a good mood to be acting so cocky today."
                mc "Who knows, maybe you're right."
                scene 11emma14 with dissolve
                em "Hey, what are you doin'?"
                mc "Just... this."
                scene 11emma15 with dissolve
                "You pulled Emma's swimsuit apart, freeing up her gorgeous breasts."
                mc "{i}Still as good as ever.{/i}"
                scene 11emma16 with dissolve
                em "Huh?"
                em "What did you just do...?"
                play sound "music/water_splash.wav"
                scene 11emma17 with vpunch
                "Emma jumped into the water, so now you could see only the top of her head."
                mc "{i}I think she's trying to know if any of the guys saw it.{/i}"
                mc "Relax, they're not looking at us."
                scene 11emma18 with dissolve
                em "Hey!"
                em "You know you're an asshole, don't you?"
                mc "I thought it might cheer you up a little."
                em "Now I'll show you what will cheer me up. Come here!"
                scene 11emma19 with dissolve
                "Emma rushed after you."
                mc "Haha! Catch me first."
                em "You know I'm a good swimmer. I'll catch you up in no time."
                scene 11emma20 with dissolve
                "Suddenly you felt your back hit the edge of the pool."
                em "*Evil laugh* Someone seems to have miscalculated his escape trajectory and fallen into a trap."
                mc "And what are you going to do with me?"
                em "Oh, don't worry, I'll think of something."
                scene 11emma21 with dissolve
                "You made sure the other guys are still paying no attention to you."
                scene 11emma22 with dissolve
                em "Are you worried that everyone will notice what we do? But didn't you start all this?"
                mc "Maybe. But I don't know what will come to your mind."
                em "That's true... You don't know that..."
                scene 11emma23 with dissolve
                "The girl came closer to you."
                em "And what am I supposed to do with you... Hmm... Let me think."
                em "Perhaps I should punish you in a way that you'll remember it for a very long time."
                em "And you know what? I know such an option..."
                stop music fadeout 2.0
                scene 11emma24 with dissolve
                "The next thing you know, Emma kissed you."
                mc "{i}Oohh... This is a punishment I like.{/i}"
                play music "music/1 - Atmosphere.ogg"
                scene 11emma25 with dissolve
                "..."
                scene anim146 with dissolve
                em "Mmmm..."
                pause
                scene 11emma26 with dissolve
                "Unable to hold back, your kiss was getting hotter and hotter."
                mc "{i}I hope we don't regret it.{/i}"
                scene anim148 with dissolve
                "Meanwhile, your hands have already moved to your ex's boobs."
                mc "{i}Oh... It's really turning me on.{/i}"
                scene anim147 with dissolve
                "As if feeling how horny you got, Emma started rubbing her whole body against your dick."
                em "Haah... Haah... Haah..."             
                pause
                scene 11emma27 with dissolve
                mc "{i}Damn, I'm getting a huge boner from this.{/i}"
                mc "{i}But I have to keep it together.{/i}"
                scene 11emma28 with dissolve
                "Suddenly the girl stopped."
                mc "{i}What? Why would she...?{/i}"
                scene 11emma29 with dissolve
                em "I was wondering when you'd show up."
                em "Mmm... How I missed him so much."
                scene 11emma30 with dissolve
                em "You know, if I really wanted to get back at you, I would definitely leave you here with this giant boner."
                em "But you're lucky I'm a very kind girl."
                mc "Yeah, I'm very lucky."
                scene 11emma31 with dissolve
                "You felt Emma's small fingers touch the tip of your dick."
                mc "{i}Oohh... It almost gave me the goosebumps.{/i}"
                scene 11emma32 with dissolve
                "She didn't waste any time and immediately took the whole process seriously."
                scene anim150 with dissolve
                mc "{i}Oh, yeah... Emma is very good at handjobs.{/i}"
                em "Do you like it?"
                mc "Yeah... But keep your voice down..."
                em "*Giggle* You're right."
                pause
                scene 11emma34 with dissolve
                "You've decided to return the favor to Emma."
                scene anim149 with dissolve
                em "Ahh! What are you...?"
                mc "Shh... Just keep going..."
                em "Mmm... Okay..."
                pause
                scene anim151 with dissolve
                mc "Ohh... It's so nice..."
                em "Yeah, baby, I know it."
                mc "{i}Man, with so many people around, this moment becomes even more exciting.{/i}"
                mc "{i}But still... I think I should go a little further myself.{/i}"
                pause
                scene 11emma35 with dissolve
                "You moved the bottom of Emma's swimsuit, which gave you a great view."
                em "Wait, you don't want to do it right here, do you?"
                mc "No, I'll just warm you up with my hands."
                em "Oh, good."
                scene anim152 with dissolve
                mc "{i}Yes... Her pussy's very hot.{/i}"
                em "Ahh... It's not bad... But... Stop teasing me, [mc]!"
                mc "Yeah... Sure..."
                pause
                scene anim153 with dissolve
                "You took advantage of the moment and started fucking Emma with your fingers."
                em "Oh, fuck... Yes!!!"
                mc "Keep your voice down!"
                em "Mmm... I'm sorry... But it feels so good."
                mc "Yeah, I know."
                pause
                scene 11emma36 with dissolve
                "Some time later, Emma's breathing increased, and she made a very quiet moan."
                em "Aaahhh!.. Mmmm..."
                mc "{i}Yeah, she came.{/i}"
                mc "{i}Looks like this whole situation has turned her on a lot harder than I thought.{/i}"
                scene anim151 with dissolve
                mc "{i}Phew... I'm pretty much at my limit myself.{/i}"
                pause
                scene 11emma37 with dissolve
                mc "Emma, I'm gonna..."
                em "Got it."
                scene 11emma38 with dissolve
                "The girl immediately dived into the water and took your dick in her mouth."
                mc "{i}Yeah, I'm almost...{/i}"
                scene 11emma39 with flash
                mc "Aaahhh.... Yeesss!"
                scene 11emma40 with flash
                mc "{i}It's so good.{/i}"
                "..."
                scene 11emma41 with dissolve
                "Emma came out of the water, and you noticed how sperm trickle is flowing out of her mouth."
                scene 11emma41a with dissolve
                "..."
                scene 11emma41b with dissolve
                em "The work is done and the pool is still clean."
                mc "Right... You were quick to figure it out. Well done."
                stop music fadeout 2.0                
                em "*Giggle* That's for sure."
                play music "music/2 - Bad.ogg"
                scene 11emma42 with dissolve
                em "Okay, we've been here way too long. I think we should get out."
                mc "Yeah, if we stay here a little longer it might seem suspicious."
                em "Mm-hmm. I'll go first."
                scene 11emma43 with dissolve
                em "You know, [mc], I loved spending some time with you."
                em "We'll have to do it again sometime."
                mc "Yeah... Maybe you're right."
                $ renpy.end_replay()
                if not persistent.day11emma:
                    $ renpy.notify(['SAHNE KILIDI ACILDI'])
                    $ persistent.day11emma = True                    
                scene 11emma44 with dissolve
                mc "{i}I don't know what got into me when I started this whole game.{/i}"
                mc "{i}We must have been very lucky that everything went so smoothly and nobody saw what we did.{/i}"
                mc "{i}But it doesn't matter anymore.{/i}"
                stop music fadeout 2.0                
                mc "{i}Now I can go and check on what the other guys are doing.{/i}"
                jump day11_pool_party_pt02

            "Leave things as they are" if not _in_replay:
                mc "{i}No, l don't want to open old wounds.{/i}"
                $ renpy.end_replay()
                scene 11emma06 with dissolve
                mc "How about we go for a swim?"
                scene 11emma03 with dissolve
                em "Sorry, but I'd rather stay here."
                em "But the whole pool is yours, so go ahead."
                mc "Huh. Thank you for your permission."
                em "You're welcome."
                stop music fadeout 2.0
                scene black with fade
                "After chatting a little more with Emma, you went to the other guys."
                jump day11_pool_party_pt02
    else:
        scene 11emma06 with dissolve
        mc "How about we go for a swim?"
        scene 11emma03 with dissolve
        em "Sorry, but I'd rather stay here."
        scene 11emma04 with dissolve
        "Emma reached for a glass of martini."
        scene 11emma05 with dissolve
        em "Yeah, that's what I needed."                
        scene 11emma03 with dissolve
        em "But the whole pool is yours, so go ahead."
        mc "Huh. Thank you for your permission."
        em "You're welcome."
        stop music fadeout 2.0
        scene black with fade
        "After chatting a little more with Emma, you went to the other guys."
        jump day11_pool_party_pt02


label day11_pool_party_pt02: 
    play music "music/7 - Just Happy.ogg"
    scene 11poolparty96 with dissolve
    "When you came to your friends, you realized that they were chatting about your next gig."
    b "Yes, of course. If Stella and I work out, we'll definitely try to get there."
    st "Oh, it'll be interesting to see your songs live."
    scene 11lisa03 with dissolve
    mc "Hmm... Is it me, or have you decided to honor our gig with your presence?"
    scene 11lisa03b with dissolve
    b "Ah, [mc]!"
    b "Yeah, you got that right. Lisa and Jade invited us to see you and your performance tomorrow."
    scene 11lisa03bb with dissolve
    mc "That's cool, I wanted to invite you to come myself today."
    mc "Oh, by the way, do you mind if I join you in your conversation?"
    scene 11lisa03b with dissolve
    b "He's asking. Of course, bro!"    
    scene 11lisa01 with dissolve
    jd "You can sit in my seat, I was just about to go smoke."
    scene 11lisa03 with dissolve
    mc "{i}She wanted to go for a smoke?{/i}"
    mc "{i}Hmm... Maybe I should go with her? This way we can talk, and I might even find out a little bit more about her and her past.{/i}"
    mc "{i}Or should I stay with Lisa?{/i}"
    menu:
        "Stay with Lisa":
            mc "{i}I'd better stay with Lisa and the guys.{/i}"
            mc "Yes, thank you."
            scene 11lisa02 with dissolve
            jd "No problem."
            scene black with fade
            "A moment later, Jade left you."
            scene 11lisa05 with dissolve
            mc "So, if our friends will be in the audience tomorrow, we'll have to do our best. Don't you think so?"
            ls "*Giggle* You don't have to worry, I always give a hundred when I sing."
            mc "Huh. I had no doubt about you."
            scene 11lisa07 with dissolve
            b "Speaking of music..."
            b "Maybe Lisa doesn't know about it, but once upon a time, me, [mc] and Jacob were in the same band."
            b "It'll be very interesting to see how much progress you have made since then."
            scene 11lisa06 with dissolve
            ls "Yeah, [mc] told me about it."
            ls "And for that matter, I think we'll find a way to surprise you."
            scene 11lisa07 with dissolve
            b "Great! Can't wait to see it."
            if lisa_path == True and day11_barry_knows_about_lisa == True:
                scene 11lisa07a with dissolve
                st "Ahem... I wanted to clarify something with you two. Is it true you're dating?"
                scene 11lisa06 with dissolve
                ls "Yep! We're a couple."
                scene 11lisa07b with dissolve
                st "Oh..."
                scene 11lisa06a with dissolve
                mc "What? Does that surprise you?"
                scene 11lisa07b with dissolve
                st "I don't know. You've been acting so normal this whole day..."
                st "I suppose if Barry hadn't told me about it, I would never have noticed."
                scene 11lisa06a with dissolve
                mc "Hmm... And how were we supposed to behave?"
                scene 11lisa07c with dissolve
                st "Well, like all couples."
                st "You saw how Jacob and Ruby behaved. Throughout the entire day, it was like they were stuck together."
                mc "{i}Well, it's no wonder the first days of a relationship are always the most passionate.{/i}"
                scene 11lisa08 with dissolve
                mc "So you think we should have done something like this?"
                ls "[mc]?"
                scene 11lisa09 with dissolve
                "*Kiss*"
                ls "Mmmm..."
                scene 11lisa10 with dissolve
                mc "Is that better?"
                ls "Personally, it's definitely better for me."
                scene 11lisa11 with dissolve
                b "*Cheerful laugh* Much better, bro!"
                st "All right, all right! I got it! Please, no more public displays of your feelings."
                mc "Huh. If you say so."
                stop music fadeout 2.0
            jump day11_pool_party_pt03


        "{color=#66FF33}Go with Jade{/color}":
            mc "{i}I better go with Jade. A short walk wouldn't hurt me anyway.{/i}"
            mc "{i}Yeah, that's definitely a good idea.{/i}"
            scene 11lisa03a with dissolve
            mc "Hey, if you don't mind, I'll go with you."
            scene 11lisa02 with dissolve
            jd "Why? Don't you want to stay here?"
            scene 11lisa03a with dissolve
            mc "Yes, but I also wanted to take a little walk. I hope it's okay with you."
            scene 11lisa02 with dissolve
            jd "Well, If you want to."
            mc "All right, then let's go. I know a good place."
            jd "Okay."
            stop music fadeout 2.0
            scene 11lisa04 with dissolve
            "Since you've been here many times, you knew the perfect place for it."
            "You started a casual conversation and lead her on."
            play music "music/13 - Hope is Still Living.ogg"
            scene 11jade01 with dissolve
            "Soon you came to a quiet corner full of green."
            mc "Let's sit here."
            jd "Yeah. It looks good here."
            scene 11jade02 with dissolve
            jd "So, you mind if I smoke?"
            mc "Of course, that's why we came here."
            jd "Yes, of course."
            scene 11jade04 with dissolve
            "Jade pulled out a cigarette."
            scene 11jade05 with dissolve
            "And smoked it."
            scene 11jade08a with dissolve
            mc "You know, you are pretty quiet today. Even by your standards."
            scene 11jade06 with dissolve
            jd "Is that so?"
            scene 11jade08a with dissolve
            mc "Yeah, at least I thought so."
            mc "Are you okay?"
            scene 11jade06 with dissolve
            jd "Yeah, I'm fine."
            scene 11jade07 with dissolve
            "Jade took a long drag on her cigarette."
            scene 11jade06b with dissolve
            jd "I just found out that an old friend of mine who once taught me how to play guitar looked at our last gig on the Web."
            scene 11jade08 with dissolve
            mc "Oh, really?! And what did this friend say?"
            scene 11jade09 with dissolve
            jd "Actually, she was very happy about it."
            mc "Huh? That's awesome, right?"
            jd "Yes... Yes, it is."
            scene 11jade06a with dissolve
            jd "I haven't seen her in a while, but we're still in touch."
            jd "If it wasn't for her, I wouldn't be making music right now."
            "You heard the sound of gratitude in her voice."
            scene 11jade08 with dissolve
            mc "By the way, I just realized that I don't know why you decided to play guitar at all."
            mc "Will you tell me your story?"
            scene 11jade06 with dissolve
            jd "My story?"
            scene 11jade08a with dissolve
            mc "Yeah. All I know about you is that you've been playing guitar for years and doing it almost every day. But that's all."
            mc "It's time to shed some light on your past."
            mc "It's not some kind of super secret, is it?"
            scene 11jade06a with dissolve
            jd "No. Of course not."
            jd "It's just... I'm rarely asked to do that."
            scene 11jade08 with dissolve
            mc "Well, I've always wondered what makes people do music. What's their path."
            scene 11jade06b with dissolve
            jd "Yeah, I know what you mean."
            jd "If you really want to know, then perhaps I should start this story from the beginning."
            stop music fadeout 2.0 
            mc "I'm listening."
            scene 11jadefb01 with dissolve
            play music "music/14 - Live Again.ogg"
            jd "At first, my family was almost no different from many other young families."
            jd "I had a loving father and mother. The three of us lived in a small house and everything was just wonderful."
            scene 11jadefb02 with dissolve
            jd "That time I remember as one of the happiest in my life."
            jd "But as you probably know, nothing lasts forever."
            scene 11jadefb03 with dissolve
            jd "In time I began to notice that my parents started to argue with each other more often."
            jd "Sometimes they'd fight over nothing."
            jd "Their relationship was more and more like a relationship of strangers than a happy married couple."
            scene 11jadefb02 with dissolve
            jd "And then everything changed."
            scene 11jadefb04 with dissolve
            jd "My Dad started to distance himself from us."
            jd "And then he just left and never came back."
            scene 11jadefb05 with dissolve
            jd "And then Mom and I were alone."
            mc "I'm really sorry..."
            jd "It's okay. Whatever happened, happened."
            scene 11jadefb06 with dissolve
            jd "Mom had a hard time with the breakup, and she started drinking to stop the pain."
            jd "At first I thought it was only temporary, but..."
            scene 11jadefb07 with dissolve
            jd "Time passed, and only the amount she drank changed."
            jd "Our relationship became more stressful, and I tried to spend as little time at home as possible."
            scene 11jadefb08 with dissolve
            jd "That's when I met Olivia."
            jd "She was an ordinary street musician who played for a handful of coins near a city cafe."
            jd "By her appearance, she was not much different from many other artists. But once you heard her music, it was immediately clear that she had an extraordinary talent."
            jd "Her music was magnificent."
            scene 11jadefb09 with dissolve
            jd "I'd come to the cafe where she'd play every night and listen to her from a distance."
            jd "And then, one day, I got up the courage to go over, and  introduce myself."
            scene 11jadefb10 with dissolve
            jd "To my surprise, she accepted me well, and we became friends very quickly."
            scene 11jadefb11 with dissolve
            jd "The next time I went to see her, we started performing together."
            jd "She used to sing and play guitar. I sang-along and danced next to her."
            jd "Olivia was a very kind woman and she loved children, so she seemed happy when I was around."
            jd "She liked it."
            scene 11jadefb12 with dissolve
            jd "Unfortunately, despite Olivia's outstanding talent, we earned almost nothing."
            scene 11jadefb13 with dissolve
            jd "And since we had plenty of free time, sometimes, between songs, she started teaching me to play guitar."
            jd "Her lessons were hard, but even so, I enjoyed them. And after many lessons, I played better and better."
            jd "And that's when she saw a  bright spot in my soul which she still sees to this day."
            scene 11jadefb14 with dissolve
            jd "That's when I felt happy again."
            scene 11jadefb15 with dissolve
            jd "Sadly, some time later, Olivia was offered a good job in another city, and despite our performances, she could not refuse the offer."
            jd "It was a hard goodbye, but I knew it was necessary."
            "{color=#008000}Olivia{/color}" "I'm sorry about what happened. But I really have to leave now."
            "{color=#008000}Olivia{/color}" "Take this guitar as my gift to you, and don't forget what I taught you."
            scene 11jadefb16 with dissolve
            "{color=#008000}Olivia{/color}" "I'm sure you'll become a great musician in the future. Much more talented and successful than me."
            "{color=#008000}Olivia{/color}" "Just promise me you'll keep practicing it."
            jd "I promise."
            "{color=#008000}Olivia{/color}" "I'm glad about that, and now, goodbye."
            scene 11jadefb17 with dissolve
            jd "And then I was alone again."
            jd "It was hard, but unlike the last time I had music. Music helped me to cope with sadness, loneliness and pain."
            jd "That's why I'm doing it."
            jd "The teacher believed in me, and I will never let her down."
            scene 11jade06b with dissolve
            jd "That's how I learned to play the guitar."
            scene 11jade07 with dissolve
            "..."    
            scene 11jade08a with dissolve
            mc "I'm sorry that you separated from your teacher so rapidly."
            scene 11jade08 with dissolve
            mc "But you still keep in touch. That's very good."
            scene 11jade06a with dissolve
            jd "Yes... Yes, I guess so. Thanks to the Internet, I've started talking to her again. This is really nice."
            mc "Yes, it is..."
            mc "{i}Well, I guess I'll find out about her last band next time.{/i}"
            mc "{i}Although, what I've learned about her now is a good start. I'm sure in time she'll reveal herself to me even more.{/i}"
            stop music fadeout 3.0
            scene 11jade03 with fade
            "Soon Jade finished smoking, and you just sat there and talked about all kinds of stuff."
            play music "music/8 - Intro Music.ogg"
            if day09_lisa_jade_lewd == True:
                scene 11jade10 with dissolve
                "Suddenly, Jade was wary."
                jd "Did you hear that?"
                mc "Hear what?"
                jd "I don't know, some really weird sound. It's like somebody's screaming."
                mc "No, I haven't heard anything."
                scene 11jade11 with dissolve
                jd "Hmm... I think I know where it came from."
                jd "Why don't we go and see? Maybe somebody's in trouble."
                menu:
                    "Check with Jade (Jade scene)":
                        scene 11jade12 with dissolve
                        mc "Okay, if you really think you heard something, let's go check it out."
                        jd "Thank you, [mc]."
                        mc "No problem."
                        stop music fadeout 2.0
                        jump day11_jade_sex
                    "Ignore the noise":
                        scene 11jade12 with dissolve
                        mc "You're imagining things, Jade. We'd better go back to the others, they're probably waiting for us."
                        jd "Yeah, I guess you're right."
                        jd "Since we're all done here, let's go."
                        scene 11jade13 with dissolve
                        jd "By the way... Thank you for keeping me company."
                        mc "No problem. It's been really interesting chatting with you."
                        jd "Yeah, it was interesting talking to you, too."
                        stop music fadeout 2.0
                        scene 11jade14 with fade
                        "Still keeping this conversation, you went back to the pool."
                        jump day11_pool_party_pt03
            else:
                mc "Okay, I think we've been here long enough. We'd better go back to the others, they're probably waiting for us."
                jd "Yeah, I guess you're right. Since we're all done here, let's go."
                scene 11jade13 with dissolve
                jd "By the way... Thank you for keeping me company."
                mc "No problem. It's been really interesting chatting with you."   
                jd "Yeah, it was interesting talking to you, too."  
                stop music fadeout 2.0
                scene 11jade14 with fade
                "Still keeping this conversation, you went back to the pool."
                jump day11_pool_party_pt03        


label day11_jade_sex:
    if _in_replay:
        $ setReplay()
    play music "music/9 - You Can Make the Sound.ogg"
    scene 11jade15 with dissolve
    "With a sure step, Jade took you somewhere towards the bushes."
    mc "If memory serves me, there is nothing in this side but trees, bushes and other greenery."
    jd "Maybe so, but that's where the sound was coming from."
    mc "I believe you, I'm just saying what I know."
    stop music
    play sound "music/music_stop.wav"
    scene 11jade16 with vpunch
    "Suddenly, you heard a loud woman moaning."
    mc "{i}What the fuck?{/i}"
    jd "Now you've heard that too?"
    mc "Well, yeah... Come on, let's take a look."
    play music "music/6 - Positive Mood.ogg"
    scene 11jade17 with dissolve    
    "Trying not to make too much noise, you both leaned forward to see the source of the unusual noise."
    scene 11jade18 with dissolve
    mc "And what are we looking for?"    
    jd "Shhh. Just keep your eyes on the window."
    mc "Window?"
    scene 11jade19 with dissolve
    "Having looked at it better, you're literally stunned."
    mc "Wait a minute... This is..."
    jd "Yeah, that's Jacob and Ruby."
    jd "I think they want to have sex."
    mc "Holy shit..."
    scene 11jade21 with dissolve
    "Right in front of you, Jacob was caressing his new girlfriend."
    mc "{i}So that's why they decided to get some privacy. I should have known about that.{/i}"
    scene 11jade20 with dissolve
    mc "Hey, maybe we shouldn't be looking at this. Don't you think so?"
    jd "Yeah, I guess so."
    scene 11jade22 with dissolve
    "Yet despite your own words, you and Jade continued to watch your friends without any shame or embarrassment."
    ru "Aahhh... Mmmm..."
    j "Baby, keep your voice down..."        
    scene 11jade23 with dissolve
    mc "{i}This is so weird...{/i}"    
    mc "{i}But at the same time, watching it with Jade is quite exciting.{/i}"
    scene 11jade24 with dissolve
    mc "Hey, I think we both admitted that spying on them is wrong."
    mc "And yet you still look."
    scene 11jade24b with dissolve
    jd "So are you."
    mc "Ahem... Yeah, but..."
    mc "I just don't understand, who in their right mind would fuck in a room with such big windows?"
    jd "In their defense, it's all bushed up here."
    mc "Yeah, but we saw them after all. So they didn't get much help from these bushes."
    scene 11jade24a with dissolve
    jd "In case you haven't forgotten, we were here last week, too..."
    mc "Yes, I remember. But we were on the second floor, and there was loud music all around."
    jd "Yeah, I guess we were a little more careful."
    scene 11jade17 with dissolve 
    "You accidentally turned your eyes on Jade and her pretty ass."
    mc "{i}And what the hell am I thinking about right now.{/i}"
    scene 11jade25 with dissolve 
    "Meanwhile, the activity behind the glass was getting hotter and hotter."
    j "Yeah, babe, your tongue is awesome!"
    j "Don't stop."
    jd "I had no idea Ruby could be so lewd."    
    scene 11jade26 with dissolve
    mc "{i}Wow, that's a good view.{/i}"
    mc "It's true... who would have thought."
    jd "Looks like you're getting pretty excited about this too."
    mc "Huh? What are you talking about?"    
    scene 11jade27 with dissolve
    "You turned your gaze on Jade, and realized that she's looking right into your groin area."
    mc "Um... Yeah, well, you're right, that really turned me on."
    scene 11jade27a with dissolve
    jd "Is it hard for you?"
    mc "Hard? What do you mean?"
    scene 11jade28 with dissolve
    "Suddenly, Jade touched your dick with her hand and looked you in the eye."
    jd "This one. It's obviously got bigger."
    jd "If it's hard for you, I can... Help you with that problem."
    mc "{i}Did I hear it or did she really say that?{/i}"
    scene 11jade29 with dissolve
    jd "Don't be so surprised, we've done this a couple of times before."
    mc "Yes, but we were with Lisa then."
    jd "She won't mind if I help you with that."
    mc "How do you know about that?"
    jd "We talked about it. As long as we don't hide anything from each other, it'll be fine."
    mc "{i}I had no idea they were talking about it.{/i}"
    stop music fadeout 2.0
    scene 11jade30 with dissolve
    jd "So, what? Shall I ask you again? Or are we just gonna forget about everything and go back to everyone else?"
    mc "Hell, no! We're staying here! And I think you already know my answer. You don't have to ask anymore."
    jd "Yeah, I think I get you."
    play music "music/1 - Atmosphere.ogg"
    scene 11jade31 with dissolve
    "The next second, Jade passionately kissed you."
    mc "{i}Oohh... She is very determined.{/i}"
    scene 11jade32 with dissolve
    mc "{i}But I kind of like it.{/i}"
    scene anim154 with dissolve
    jd "Mmmm..."
    pause
    scene 11jade33 with dissolve
    "Before you knew it, your hands were massaging Jade's breasts."
    "She wasn't wasting her time, though, and she was gently stroking your dick."
    scene 11jade34 with dissolve
    "Then you felt the girl's hand climb into your trunks and started acting even more confidently."
    mc "And you're much more aggressive than last time."
    jd "Really?"
    mc "Definitely."
    scene 11jade35 with dissolve
    jd "Maybe I'm just in a good mood today."
    mc "Oh... I like this mood."
    jd "Yeah, I've noticed that."
    scene 11jade37 with dissolve
    mc "{i}Her boobs look particularly tempting right now.{/i}"
    mc "Come here."
    scene 11jade36 with dissolve
    "Feeling that the sexual tension had increased again, you fell for the impulse and kissed Jade again."
    jd "Mmmm... You're pushy, too."
    scene 11jade38 with dissolve
    "At the same time as she kissed you, she didn't forget to jerk you off."
    scene anim157 with dissolve
    mc "{i}It's a lot different from what we had last time, but it's still very cool.{/i}"
    mc "{i}Oohh... And it's really satisfying.{/i}"
    jd "Mmmm... Ahh...."
    scene 11jade39 with dissolve
    "Meanwhile, Jade's panties had already slipped down a little bit, so you could see her nice pussy."
    scene 11jade40 with dissolve
    "Suddenly, Jade turned around"
    scene anim156 with dissolve
    jd "Ahh... I think we forgot about our sweet couple in the house."
    jd "Maybe we should see what they're doing there."
    mc "Yeah... Let's see..."
    pause
    scene 11jade41 with dissolve
    jd "Oh, we noticed them in time. Looks like they're done with foreplay."
    mc "{i}Damn, I can't help but notice that Ruby has an amazing ass.{/i}"
    scene 11jade42 with dissolve
    ru "Ahh... I never thought we'd do this so soon."
    ru "But I'm really glad about it."
    j "We're both crazy about each other. There's no point in dragging with what we both want."
    scene 11jade44 with dissolve
    "The next moment, Ruby literally saddled Jacob's dick."
    j "Aahhhh... Baby, it feels so good inside you..."
    scene 11jade45 with dissolve
    ru "Aaaahhh... Aaaahhh.... Aaaahhh!"
    mc "{i}Yeah, they definitely enjoy each other.{/i}"
    scene 11jade43 with dissolve
    "For some time, you were silently watching your friends fuck."
    mc "{i}I can feel Jade's heartbeat getting a little faster and her breath getting deeper.{/i}"
    scene anim155 with dissolve
    jd "Oh... Sorry, I almost forgot about you."
    mc "Mmm... It's okay."
    jd "Your dick's already so hard."
    jd "You know... If you don't mind, I'd like to...."
    mc "What?"
    jd "I'd like to feel your cock inside me."
    mc "Huh. You wanna have sex in front of them?"
    jd "Why not? It'll be even more exciting."
    pause
    scene 11jade46 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1  
    "You took Jade by the shoulders while she grabbed your dick and pointed him at her pussy."
    mc "{i}Oh... She's already wet. Looks like this whole situation turned her on.{/i}"
    scene 11jade47 with dissolve
    jd "I put it in, [mc]..."
    scene 11jade48 with dissolve
    jd "Aahhh.... Mmmnn!"
    mc "Be quiet, we don't want them to see us."
    jd "..."
    mc "Yeah, that's better."
    scene 11jade49 with dissolve
    mc "{i}Oh, yeah! Now we're definitely gonna have fun!{/i}"
    scene anim159 with dissolve
    jd "Ahh... Aaah.... Aaahh...."
    jd "Your dick... It's so... So big and hot..."
    mc "It's all because of you."
    pause
    scene anim160 with dissolve
    "You started fucking Jade harder."
    jd "Ahh! Aaah!! Aaahh!!!"
    mc "Now, baby, I want you to bend a little lower..."
    jd "Mmm... What for?"
    mc "Shh... Just do it."
    jd "Okay..."
    pause
    scene 11jade50 with dissolve
    mc "Yeah, that's much better."
    scene anim161 with dissolve
    jd "Aaaahhhhh... Aaaahhhhh.... Aaahhhh...."
    mc "You know, you're just so... So sexy right now."
    jd "Ahh... Shut up."
    pause
    scene anim162 with dissolve
    mc "{i}From this angle, her ass looks really good.{/i}"
    jd "If you want... If you want, you can move faster."
    mc "I think I can do that."
    pause
    scene anim163 with dissolve
    jd "Yeesss... That's it!"
    mc "{i}If I keep fucking her like this, I'll cum soon.{/i}"
    scene 11jade51 with dissolve
    mc "Hey, Jade, let's change positions."
    jd "Ahh... If that's what you want."
    scene 11jade52 with dissolve
    "You picked up a girl's leg and you started fucking her sideways."
    mc "I had no idea you were so flexible."
    jd "Mmm..."
    scene 11jade53 with dissolve
    "*The sounds of moaning and heavy breathing*"
    scene anim158 with dissolve
    jd "I'm almost... I'm almost at the limit."
    mc "Come on, baby... Just hang on a little longer, and we can end up together."
    pause
    scene 11jade55 with dissolve
    "You turned your head towards the window and realized you weren't the only ones ready to finish."
    j "Oh my God, Ruby, I can't take it anymore. I'm gonna..."
    ru "You can come right on me!"
    scene 11jade56 with dissolve
    j "Yeeesss!!!"
    scene 11jade56a with dissolve
    ru "Ooh... I don't know what to say..."
    j "Yeah."
    mc "{i}Well, now I'm definitely ready.{/i}"
    scene 11jade54 with dissolve
    jd "[mc], if you want, you can come inside..."
    mc "What?"
    jd "It's okay, you can do this."
    mc "{i}What the fuck? If that's what she wants, then why not?{/i}"
    mc "Okay."
    scene 11jade57 with dissolve
    "Couldn't hold back anymore, you started coming inside Jade."
    mc "Aaahhhh...!"
    scene 11jade57a with flash
    mc "Awesome!"
    scene 11jade57a with flash
    jd "Oh, God!"
    mc "{i}Looks like I wasn't the only one who enjoyed the moment.{/i}"
    stop music fadeout 2.0
    scene 11jade58 with dissolve
    "The next second, Jade fell exhausted on the grass."
    play music "music/6 - Positive Mood.ogg"
    scene 11jade59 with dissolve
    mc "Hey, are you okay?"
    scene 11jade58 with dissolve
    jd "Yes... It was, uh... I'm sorry, I just need a little breath."
    mc "Oh, I see."
    scene 11jade60 with dissolve
    "You looked out the window again and noticed that Jacob and Ruby were already dressed and ready to leave."
    mc "{i}I guess we should go too.{/i}"
    scene 11jade59 with dissolve
    mc "Well... If you're feeling better, should we go?"
    jd "Yes... I'm almost ready."
    $ renpy.end_replay()
    if not persistent.day11jade:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day11jade = True      
    scene black with fade
    "A few minutes later."
    scene 11jade61 with fade
    "Soon you and Jade headed back to your friends."
    mc "I hope they didn't forget about us."
    jd "We'll see."
    mc "As for Lisa and your conversation, I guess we'll have to tell her about what happened here?"
    jd "Don't worry, I'll do it."
    mc "Huh? You sure?"
    jd "Absolutely."
    mc "Well, so be it."
    stop music fadeout 2.0
    jump day11_pool_party_pt03


label day11_pool_party_pt03:    
    scene 11partyend01 with fade
    "Time was ticking."
    scene 11partyend02 with dissolve
    "You were having fun with friends, drinking alcohol, swimming in the pool and just sunbathing."
    scene 11partyend03 with dissolve
    "Soon it was evening."
    play music "music/8 - Intro Music.ogg"
    scene 11partyend04 with dissolve
    b "Hey, guys, I know we've done a lot of things today, but how about we go inside?"
    b "We could turn on the music and sit in the living room."
    scene 11partyend05 with dissolve
    ru "Um... Sorry, Barry, but I think I'll pass."
    ru "It's been a lot of fun with you, but it's better if I go home now."
    scene 11partyend06 with dissolve
    j "What? Are you going home already?"
    j "But isn't it too soon?"
    scene 11partyend07 with dissolve
    ru "I'm sorry, but I have some family business in the morning. Besides, I promised you I'd go to your gig."
    ru "Well, there's a lot to do."
    j "That's too bad, but I get it."
    scene 11partyend08 with dissolve
    ls "I hate to spoil your fun, but I'm going home, too."
    ls "Tomorrow is a big day and I have to be fresh."
    scene 11partyend09 with dissolve
    jd "So do I."
    jd "In fact, we should all go home early to be full of energy tomorrow."
    mc "That's a shame."
    scene 11partyend10 with dissolve
    mc "What about you, Emma? Are you staying?"
    em "Me?"
    scene 11partyend11 with dissolve
    "You noticed how Emma was thinking for a few seconds."
    scene 11partyend11a with dissolve
    em "Sorry, I wish I could stay... I really do... But I agree with the girls, and I'll go too."
    em "I have to work a shift tomorrow morning."
    mc "Okay, I get it." 
    em "Yeah..."
    scene 11partyend12 with dissolve
    b "Hmm... So it's just me Jacob, [mc] and Stella."
    b "That's interesting."
    scene 11partyend13 with dissolve
    st "Don't be so sure about that."
    st "I'd rather leave you boys alone and go upstairs to get some sleep."
    scene 11partyend14 with dissolve
    b "You're sure?"
    scene 11partyend13 with dissolve
    st "Yeah, I'm sure. I'm a little sleepy, so I don't want to ruin your evening with my boringness."
    st "Besides, you three probably have a lot to talk about."    
    scene 11partyend12a with dissolve
    b "Well, in that case, it's just us. Damn, just like the old times!"
    mc "{i}Yes, it brings back memories... It's been a long time since the three of us have spent time together.{/i}"
    scene 11partyend13 with dissolve
    st "Hey, before you go and keep drinking, don't forget to escort girls out first."
    scene 11partyend14 with dissolve
    b "Uh... Yeah, sure, that's what I was planning to do."
    stop music fadeout 2.0
    scene black with fade
    "Couple minutes later."
    play music "music/6 - Positive Mood.ogg"
    scene 11partyend15 with dissolve
    mc "I know you've already decided to go home, but I can't help but ask if there's any way we can convince you to stay?"
    mc "It would be very sad if all the ladies left us at once."
    scene 11partyend16 with dissolve
    ls "As tempting as this offer is, we've already made a decision."
    ls "But thank you anyway."
    scene 11partyend15 with dissolve
    mc "Well, it was worth a shot."
    scene 11partyend17 with dissolve
    em "It was a great day, Barry. Thank you for inviting me."
    b "Of course! I was just glad you came by."
    em "Yeah."
    em "And it was also nice to see you again, [mc]."
    mc "Yeah, it's mutual."
    scene 11partyend17a with dissolve
    em "With you, too, Lisa, Jade."
    ls "Umm... Yeah, sure."
    jd "Bye, Emma."
    scene 11partyend18 with dissolve
    "Without saying another word, Emma went home."
    scene 11partyend19 with dissolve
    ls "Uh... I don't think she liked us."
    ls "And I have no idea why she reacted so strangely to me."
    scene 11partyend23 with dissolve
    b "In fact, you girls do that a lot."
    b "You're offended by nonsense or you're just acting really weird. And we, guys, have to figure out for ourselves what's causing this behavior."
    b "And sometimes you don't even understand each other!"
    b "So what are we supposed to do in that case?"
    mc "{i}Looks like it hit him on a nerve.{/i}"
    scene 11partyend23a with dissolve
    mc "Okay, never mind, Liz. Looks like she's just in a bad mood today."
    scene 11partyend19 with dissolve
    ls "Yeah, probably."
    scene 11partyend20 with dissolve
    "You turned your head to the side and saw Jacob saying goodbye to Ruby."
    ru "Call me tomorrow morning. I want to know that our plans are still in place."
    j "Of course, babe, you can be sure of it."
    ru "Okay... See you tomorrow, then."
    scene 11partyend21 with dissolve
    "..."
    j "Yes... Goodbye..."
    scene 11partyend22 with dissolve
    ru "Goodbye, guys! I'll see you at your gig tomorrow!"
    mc "Bye, Ruby."
    ls "Yeah, see you tomorrow!"
    "*Farewell shouts!*"
    scene 11partyend24 with dissolve
    "Right after that, you said goodbye to the other girls and now you were silently looking at their backs."
    b "Well... I have to say, you found some cool girls in your band."
    mc "Yeah. We picked the best."
    j "And the most talented ones!"
    b "Yes, they're talented... That's for sure."
    scene 11partyend25 with dissolve
    b "Okay, looks like we're all alone here."
    b "Don't you think it's time to celebrate?"
    j "Haha. That's a good idea!"
    stop music fadeout 2.0
    scene black with fade
    "Some time later you gathered in the living room and started drinking and talking to each other."
    play music "music/3 - Dream With U.ogg"
    scene 11partyend26 with dissolve
    mc "You know, it's cool that we're all together like this, but..."
    mc "But if we just keep sitting here and drinking, then I should have gone home with the girls."
    b "Huh? What's your point?"
    mc "I mean, we need to do something. We need some action."
    scene 11partyend29 with dissolve
    j "That's right! We just have to go out. Who knows when the next time we'll get together like this?"
    scene 11partyend27 with dissolve
    b "Hmm... If you think about it, it's not such a bad idea. And I even have thoughts about where we're gonna go."
    mc "Oh, really?"
    b "Yes, definitely."
    scene 11partyend26 with dissolve
    mc "Why don't you share your idea with us?"
    b "Nah, I won't. Let it come as a surprise to you."
    j "Come on, Barry. Just tell us. There's no point in these secrets."
    scene 11partyend28 with dissolve
    b "Hey, where's your spirit of adventure?"
    b "I promise you'll love this place. Just grab your stuff and let's go there right now."
    scene 11partyend29 with dissolve
    j "I don't know what he's talking about, but I'm already interested."
    j "Let's have a drink and go."
    scene 11partyend30 with dissolve
    b "To a glorious night!"
    mc "Let's have a good time!"
    j "Haha. Yes! Let's hang out!"
    play sound "music/bottle.wav"
    scene 11partyend31 with dissolve
    "*Bottle ring*"
    stop music fadeout 2.0
    jump day11_sclub_pt1


label day11_sclub_pt1:
    scene black with fade
    "Some time later."
    play music "music/2 - Bad.ogg"
    scene 11sclub01 with dissolve
    mc "So... Remind me again why, of all the places in this huge city, we decided to go to a strip club?"
    j "Cause that's cool, man! Does there have to be some other reason?"
    b "That's right. It's also just because we can do it."
    mc "Yeah, right. One reason is better than the other."
    scene 11sclub02 with dissolve
    b "But that's the way it is. Besides, it's a great place to sit in our purely male company."
    scene 11sclub01 with dissolve
    j "Yea, It's the girls' fault for leaving us so early."
    mc "Do you remember that you started dating your girlfriend just a couple of days ago?"
    scene 11sclub03 with dissolve
    j "Hey, [mc], don't be a nerd. It's not like I'm gonna cheat on her or anything."
    j "We're just gonna sit and drink surrounded by beautiful ladies."
    mc "Yeah, beautiful naked ladies."
    j "Hehe. Exactly!"
    scene 11sclub01 with dissolve
    b "Okay, since we're here anyway, it's too late to turn back."
    mc "Well, I guess you're right."
    j "That's another thing! Let's go."
    scene 11sclub04 with dissolve
    mc "You know, I feel like the last time we got together like this was a hundred years ago."
    b "Yes... Time flies fast."
    j "And that's why we need to make this evening special!"
    b "Hehe! That's a really good idea!"
    mc "{i}Hey, wait a minute... Isn't that-{/i}"
    scene 11sclub05 with dissolve
    v "Well, well, Isn't that [mc]?"
    mc "{i}Yeah, that's definitely him.{/i}"
    scene 11sclub06 with dissolve
    mc "Vincent? Hey, man! What are you doing here?"
    v "What am I doing here? What does it look like? I work here."
    scene 11sclub05 with dissolve
    mc "Huh. I never thought you'd be part-working in a place like this."
    v "And I never thought I'd meet you here."
    mc "That's a fair point."
    scene 11sclub07a with dissolve
    b "You guys seem to know each other?"
    mc "Yeah, you could say that. Vincent and I work at the same club."
    b "It's such a small world."
    scene 11sclub07 with dissolve
    v "It's true."
    scene 11sclub08 with dissolve
    j "Hey, guys, I get it, you met someone you know and you want to talk and discuss the news and stuff..."
    j "But don't forget the reason for what we came here for. Okay?"
    scene 11sclub09 with dissolve
    j "Now, sesame, open up!"
    "*Sounds of music*."
    scene 11sclub09a with dissolve
    j "Hehe. All right! I can feel the atmosphere of depravity that's out there."
    j "So? How long do I have to wait for you?"
    scene 11sclub07a with dissolve
    v "Hmm... Sounds like your friend is very determined."
    scene 11sclub07b with dissolve
    b "Yes... When he drinks, he becomes a little unpredictable."
    v "Unpredictable? Should I expect some trouble from him?"
    b "Ehh... No, it's nothing like that. Unpredictable in a good way."
    v "Okay, I'll take your word for it."
    scene 11sclub07a with dissolve
    b "All right, I guess I'll go too. Catch up with us, [mc]."
    mc "Yeah, I'm right behind you."
    scene 11sclub10 with dissolve
    "Jacob and Barry went inside."
    scene 11sclub11 with dissolve
    mc "Anyway, it was good to see you. See you later!"
    v "Yes, of course."
    v "Oh yeah, [mc], one more thing..."
    mc "Huh?"
    scene 11sclub12 with dissolve
    if anna_sex == True:
        v "Given your relationship with Anna, I don't know if I'm supposed to tell you this, but..."
        v "If you want to get \"extra service\" here, you should ask Jasmine."    
        v "But, as you know, you will have to pay extra for this."
    else:
        v "Let me tell you something, if you want \"extra service\" here, you should ask Jasmine."
        v "But, as you know, you will have to pay extra for this."
    mc "{i}Hmm... Jasmine? I'll keep that in mind.{/i}" 
    mc "Okay, I hear you. Thank you for the tip."
    scene 11sclub13 with dissolve
    v "No problem. Have a nice evening."
    mc "Yeah, thanks again. I'll see you around."
    v "Of course."
    stop music fadeout 2.0
    scene black with fade
    "You said goodbye to Vincent and ran to catch up with your friends."
    play music "music/3 - Dream With U.ogg"
    scene 11sclub14 with dissolve
    mc "{i}Phew.. Lucky they didn't go too far.{/i}"
    j "Heh. Welcome to the realm of vice and lewdness!"
    b "Dude, no need to be so dramatic, it's just a strip club."
    j "Hey, don't ruin it for me."
    mc "Relax, guys, better let's take a look around here."
    scene 11sclub15 with dissolve   
    j "Whoa..."
    b "Yeah, it's really good."
    mc "{i}Hmm... And there aren't many people here.{/i}"
    scene 11sclub16 with dissolve
    "Looking around the room, you immediately noticed some pretty women."
    scene 11sclub17 with dissolve
    "One of them was on stage right now and was doing some totally crazy dancing."
    scene 11sclub17a with dissolve
    "..."
    scene 11sclub17b with dissolve
    "..."
    scene 11sclub18b with dissolve
    "The other one was walking around the hall, carrying drinks and, as if by accident, showing off her magnificent shapes."
    scene 11sclub18 with dissolve
    "..."
    scene 11sclub18a with dissolve
    "..."
    scene 11sclub19 with dissolve
    "And the third girl was looking at you."
    scene 11sclub20 with dissolve
    "Then with a confident look, she was heading right to us."
    scene 11sclub21 with dissolve
    "{color=#EE82EE}Woman{/color}" "It's so nice to see new faces in our place, especially attractive one."
    mc "{i}Oh, this lady is very good at communicating with clients.{/i}"
    scene 11sclub22 with dissolve
    mc "{i}Not to mention the fact that thanks to her appearance, she literally captures all eyes.{/i}"
    scene 11sclub21 with dissolve
    "{color=#EE82EE}Woman{/color}" "I hate to brag, but you won't find girls better than ours anywhere in this town."
    "{color=#EE82EE}Woman{/color}" "I think you'll like it here."
    scene 11sclub23 with dissolve
    "{color=#EE82EE}Woman{/color}" "Okay, let me escort you to a separate table."
    "{color=#EE82EE}Woman{/color}" "Just follow me."
    scene 11sclub24 with dissolve
    "Only now you've noticed that while she was talking, none of the three of you have said a word."
    scene 11sclub25 with dissolve
    b "It's not for nothing that we chose this place. It's perfect for us."
    mc "You know... I think I agree with you."
    b "Huh. After we saw all these beauties, I'd be surprised if you said otherwise."
    scene 11sclub25a with dissolve
    j "Hey, maybe we shouldn't keep that pretty girl waiting for us, huh?"
    mc "Yeah, that's right. Come on, let's go."
    stop music fadeout 2.0
    scene black with fade
    "A few minutes later."
    play music "music/12 - The Moose.ogg"
    scene 11sclub26 with dissolve
    "You were placed at the table, then you ordered drinks and start watching the girl on stage."
    "{color=#EE82EE}Woman{/color}" "By the way, I didn't get a chance to introduce myself. My name is Jasmine."
    scene 11sclub27 with dissolve
    mc "{i}So it was her extra service Vincent mentioned.{/i}"
    mc "{i}I must admit, she's really nice.{/i}"    
    mc "I'm [mc]."
    jsm "Mmm... That's a powerful name."
    mc "Um... Yeah, thank you."
    jsm "Okay, [mc], let me tell you a little bit about the local girls."
    scene 11sclub28 with dissolve
    jsm "That dancer by the pole your friends are staring at is Fiona."
    scene 11sclub29 with dissolve
    mc "She seems very skilled."
    jsm "Oh, you can be sure we're all very talented here."
    jsm "But she is one of our most flexible. She's young and very gifted."
    scene 11sclub30 with dissolve
    mc "{i}And right now I see two of her biggest gifts.{/i}"
    mc "{i}If it was a beauty contest, I'd think hard about which one of these girls to give first place.{/i}"
    scene 11sclub31 with dissolve
    mc "{i}Especially after such hypnotizing movements.{/i}"
    scene 11sclub32 with dissolve
    mc "{i}Or like this one.{/i}"
    scene 11sclub33 with dissolve
    "Still continuing her sexy dance, the girl slowly descended to the floor and spread her legs."
    mc "So it's Fiona. I remembered her."
    scene 11sclub34 with dissolve
    j "Damn, that girl's really hot!"
    j "Keep up the pace, babe!"
    scene 11sclub27 with dissolve
    jsm "Yeah, that was Fiona."
    jsm "And that girl who was carrying the drinks is Becky."
    jsm "She's a skilled dancer, too. But when we don't have enough staff, she combines it with a waitress position."
    mc "That's interesting."
    mc "Becky, Fiona and Jasmine. Very tempting trio."
    jsm "That's right, we are."
    scene 11sclub35 with dissolve
    b "Hey, guys, you don't need to be shy about expenses today."
    b "I'm the one who brought us all together, which means I'm the one paying for everything. So you can go ahead and order everything you want."
    mc "{i}Given my current finances, it's a really good offer.{/i}"
    scene 11sclub36 with dissolve
    "As soon as Fiona finished her dance, she and her friend Becky headed to your table."
    fi "We see you boys are having a good time here."
    bk "Yeah, how about ordering a lap dance?"
    scene 11sclub37 with dissolve
    jsm "Mmm... I think it's time for me to join in, too."
    jsm "And to make it easier for you to choose, I'll do this..."
    scene 11sclub38 with dissolve
    "Jasmine started slowly pulling off her bra."
    jsm "Yes... It's much better this way..."
    scene 11sclub39 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    "A few seconds later, Jasmine stood in front of you half-naked."
    mc "{i}Wow! That lady is a real bomb.{/i}"
    scene 11sclub41 with dissolve
    fi "Hey, don't forget about us boys."
    bk "If you want, you can try a dance from each of us. We have plenty of time."
    fi "*Giggle* That's for sure."
    stop music fadeout 2.0
    scene 11sclub44 with dissolve
    mc "{i}Yes... It's not an easy decision. Every one of them is super hot.{/i}"
    mc "{i}And yet, who should I choose?{/i}"

    $ day11_stripper_01 = False
    $ day11_stripper_02 = False
    $ day11_stripper_03 = False

    menu day11_stripper_choice:
        "Jasmine" if day11_stripper_01 == False:
            $ day11_stripper_01 = True
            play music "music/11 - Pop Energy.ogg"
            mc "I choose Jasmine."
            scene 11sclub40 with dissolve
            jsm "Mmm... I promise you won't regret it."
            mc "Well, I really hope not."
            scene 11sclub45 with dissolve
            "In just a few moments, the girl was right in front of you."
            jsm "Well, let's start..."
            scene 11sclub46 with dissolve
            "Jasmine leaned closer to you, so you could smell a slight unobtrusive smell of her perfume."
            "Her knee stopped right next to your groin, and her hands started sliding slowly up your body."
            jsm "Let me show you what I can do..."
            scene 11sclub47 with dissolve
            mc "{i}She's even better up close.{/i}"   
            jsm "So, what do you think? Do you like it?"
            mc "Mmm... I must say, the beginning is very intriguing."
            scene 11sclub48 with dissolve
            "You gripped Jasmine for her big, firm ass."
            jsm "Ohh... Someone has very naughty hands."
            mc "{i}Yes... It feels really nice.{/i}" 
            scene 11sclub49 with dissolve
            jsm "I saw the way you looked at my boobs. Did you like them that much?"
            mc "Yeah... Your boobs are amazing."
            jsm "Then how about this...?"
            scene 11sclub50 with dissolve
            "The girl gently pulled your face to her breast."
            jsm "*Cheerful laugh* Yeah... I see you like it."
            jsm "But let's try one more thing."
            scene 11sclub52 with dissolve
            "Jasmine turned around, showing you a great view of her ass."
            mc "{i}Looks very seductive.{/i}" 
            scene 11sclub51 with dissolve
            jsm "I hope you've enjoyed it, because we have to finish now."
            mc "{i}Shit... Time flew by so fast.{/i}" 
            scene 11sclub53 with dissolve
            jsm "Well, that's it. Did you like it?"
            mc "Yeah... That was impressive."
            jsm "Glad to hear it."
            scene 11sclub54 with dissolve
            jsm "But, you know... If it wasn't enough, I could put on a private show for you."
            jsm "In that way, I could give you a little more freedom than here."
            jsm "For an extra fee, of course."
            jsm "So, what do you think? Are you interested in this?"
            mc "{i}And here's that extra service Vincent was talking about.{/i}" 
            scene 11sclub57 with dissolve
            "You noticed that no one would notice if you disappeared from here for fifteen or twenty minutes."
            scene 11sclub49 with dissolve
            mc "{i}What am I gonna say to her?{/i}" 
            menu:
                "Agree to a private show (Jasmine scene)":    
                    mc "That's a very tempting offer. I agree."
                    jsm "Mmm... Great, then follow me."
                    scene 11sclub55 with dissolve
                    "Jasmine took you to the back of the strip club."
                    scene 11sclub56 with dissolve
                    jsm "Take a look at this, it seems like your friends are having fun over there."
                    scene 11sclub57 with dissolve
                    "..."
                    scene 11sclub58 with dissolve
                    mc "Yeah, they fell in love with this place."
                    jsm "And what about you?"
                    mc "So far, I like it too, but I want to see what happens next..."
                    scene 11sclub56 with dissolve
                    jsm "Quite reasonable."
                    jsm "Then it's my job to make you like us even more."
                    jsm "It's not an easy task, but you can be sure I can handle it."
                    scene 11sclub58 with dissolve
                    mc "Huh. I'm all excited."
                    stop music fadeout 2.0
                    jump day11_sclub_sex
                "Refuse":
                    mc "Thank you for the offer, but I'll pass."
                    jsm "Well, as you wish. If you need anything, you know where to find me."
                    "..."
                    scene 11sclub44 with dissolve
                    mc "{i}Well, that wasn't bad.{/i}"
                    mc "{i}But maybe I should try a lap dance from another girl?{/i}"
                    stop music fadeout 2.0
                    jump day11_stripper_choice

                "Save for later":
                    mc "It's a very tempting offer, but first I want to try a lap dance from other girls."
                    jsm "Mm-hmm... I see. Just don't make me wait too long."
                    mc "Deal." 
                    scene 11sclub44 with dissolve
                    mc "{i}Well, that was pretty good.{/i}"
                    mc "{i}Now I should try a lap dance from another girl.{/i}"
                    stop music fadeout 2.0
                    jump day11_stripper_choice           

            
        "Fiona" if day11_stripper_02 == False:
            $ day11_stripper_02 = True
            play music "music/11 - Pop Energy.ogg"
            mc "I choose Fiona."
            scene 11sclub42 with dissolve
            fi "Good choice, babe."
            mc "I hope so."
            scene 11sclub59 with dissolve
            "In a few moments, the girl leaned right in front of your face."
            fi "Rest assured, I will take good care of you."
            mc "I like the way it sounds."
            scene 11sclub60 with dissolve
            fi "*Giggle* You're gonna like it even better now."
            scene 11sclub61 with dissolve
            "Fiona bent over you, which is why her huge boobs were right under your nose."
            mc "That's an interesting start."
            scene 11sclub62 with dissolve
            "The girl turned around, and her leg slightly touched your dick."
            fi "Now we're gonna shake you up a little bit."
            scene 11sclub63 with dissolve
            "A few seconds later, she completely fell to your knees."
            fi "And let's do this..."
            scene 11sclub63a with dissolve
            $renpy.pause(0.5, hard=True)   
            scene 11sclub63 with dissolve     
            fi "Oh... I can feel something moving in your pants. How curious."
            scene 11sclub63a with dissolve
            $renpy.pause(0.5, hard=True)   
            scene 11sclub63 with dissolve               
            mc "{i}You bet! It's hard to hold yourself together when her ass is so close.{/i}"
            scene 11sclub64 with dissolve
            "Fiona started rubbing even harder."
            mc "{i}Oh, that's so hot.{/i}"
            scene 11sclub65 with dissolve
            fi "Mmm... If you want, you can touch me anywhere you want."
            fi "Grab my boobs."
            scene 11sclub66 with dissolve
            fi "Yeah... Like that..."
            fi "Do you feel how fast my heart is beating?"
            "Even though you couldn't feel her heart beating, it was great."
            scene 11sclub67 with dissolve
            fi "Ah... I see you you're really into this. Did you really like me that much?"
            mc "You're really very good."
            fi "Oh, thanks."
            scene 11sclub68 with dissolve
            fi "It's a shame we're running out of time..."
            fi "I wouldn't mind doing it again sometime."
            mc "{i}Shit... She's right. Time flew by so fast.{/i}" 
            scene 11sclub69 with dissolve
            fi "So, baby, did you enjoy it?"
            mc "Yeah, it was great."
            fi "That's good, I tried really hard."
            fi "I'd love for you to come here some other time, and then we can... Um... To continue where we left off..."
            mc "Absolutely."
            scene 11sclub44 with dissolve
            mc "{i}Well, that was pretty good.{/i}"
            mc "{i}But maybe I should try a lap dance from another girl?{/i}"
            stop music fadeout 2.0
            jump day11_stripper_choice

        "Becky" if day11_stripper_03 == False:
            $ day11_stripper_03 = True
            play music "music/11 - Pop Energy.ogg"
            mc "I choose Becky."
            scene 11sclub43 with dissolve
            bk "Excellent. You're going to love what you're about to experience."
            mc "I'm ready."
            scene 11sclub70 with dissolve
            "After a few seconds, the girl was standing right in front of you in a very seductive pose."
            mc "{i}Wow... And she's got some pretty outstanding shapes.{/i}"
            mc "{i}I really want to see what she'll do next.{/i}"
            scene 11sclub71 with dissolve
            bk "It's not often that young boys like you come to our place."
            bk "You can lean back and relax. Becky will do everything for you."
            mc "{i}I suppose that's what I'll do.{/i}"
            scene 11sclub72 with dissolve
            "The girl threw her back out and slowly started rubbing her ass against your groin."
            bk "Mmm... If you want, you can touch more than just my legs."
            scene 11sclub73 with dissolve
            mc "{i}Yeah... She's right, there are much more exciting places here.{/i}"
            bk "Ahh... That's what I was talking about."
            mc "{i}Damn, I'm getting a huge boner from this chick.{/i}"
            scene 11sclub74 with dissolve
            "Becky pressed her back against you, and you felt the heat coming from her."
            mc "How about you turn around and face me?"
            bk "With pleasure."
            scene 11sclub75 with dissolve
            "She turned towards you, so your eyes immediately stuck to her huge boobs."
            mc "Oh... You're so hot."
            scene 11sclub76 with dissolve
            bk "People often tell me that."
            bk "And what do you like the most? My boobs or my ass?"
            scene 11sclub77 with dissolve
            "The next second, both your hands ended up on her ass."
            bk "Oh... You don't have to say anything, I think I already know the answer."
            scene 11sclub78 with dissolve
            bk "Yeah... There you go, don't be shy. Touch as much as you want."
            mc "{i}Her skin is so smooth. It's almost perfect.{/i}"             
            mc "{i}If it wasn't for my boner, I'd be ready to enjoy it forever.{/i}" 
            scene 11sclub76 with dissolve
            bk "It's been a pleasure dancing for you, but our time is running out."
            mc "{i}Shit... She's right. Time flew by so fast.{/i}" 
            scene 11sclub79 with dissolve
            bk "Hope you enjoyed it, honey."
            mc "Everything was great. Thank you, Becky."
            bk "Come anytime. You're always welcome."
            scene 11sclub44 with dissolve
            mc "{i}Well, that was pretty good.{/i}"
            mc "{i}But maybe I should try a lap dance from another girl?{/i}"
            stop music fadeout 2.0
            jump day11_stripper_choice

        "That's enough" if day11_stripper_01 == True or day11_stripper_02 == True or day11_stripper_03 == True:
            scene 11sclub44 with dissolve
            mc "Well, that was good. But I guess that'll be enough."
            mc "We'd better get some more drinks."
            stop music fadeout 2.0
            jump day11_sclub_pt2  

        "Accept Jasmine's offer (Jasmine scene)" if day11_stripper_01 == True:
            scene black with fade
            "You went up to Jasmine and agreed to her extra offer."
            play music "music/8 - Intro Music.ogg"
            scene 11sclub55 with dissolve
            "A few seconds later Jasmine took you to the back of the strip club."
            scene 11sclub56 with dissolve
            jsm "Take a look at this, it seems like your friends are having fun over there."
            scene 11sclub57 with dissolve
            "..."
            scene 11sclub58 with dissolve
            mc "Yeah, they fell in love with this place."
            jsm "And what about you?"
            mc "So far, I like it too, but I want to see what happens next..."
            scene 11sclub56 with dissolve
            jsm "Quite reasonable."
            jsm "Then it's my job to make you like us even more."
            jsm "It's not an easy task, but you can be sure I can handle it."
            scene 11sclub58 with dissolve
            mc "Huh. I'm all excited."
            stop music fadeout 2.0
            jump day11_sclub_sex

        "Don't choose anybody":
            mc "Sorry ladies, but I'm fine as it is."
            b "Whatever, dude."
            stop music fadeout 2.0
            jump day11_sclub_pt2                  
    "..."
    jump day11_sclub_pt2


label day11_sclub_sex:
    if _in_replay:
        $ setReplay()
    $ day11_sclub_sex = True
    scene black with fade
    "You followed Jasmine into a small room."
    play music "music/1 - Atmosphere.ogg"
    scene 11stripsex01 with dissolve
    jsm "Welcome to the room where fulfilled all wishes."
    mc "Sounds promising."
    jsm "And it really is."
    jsm "Now get inside, we don't have much time."
    scene 11stripsex02 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    "Just a few moments later, you stood in front of Jasmine and closely looked at her."
    jsm "How about we start with something easier?"
    mc "I hope the easier doesn't mean worse?"
    jsm "Believe me, you're not my first client here. And none of them left here unsatisfied."
    scene 11stripsex03 with dissolve
    "The girl got down on her knees and with very skillful movements started unbuttoning your pants."
    jsm "Just... like this..."
    scene 11stripsex03a with dissolve
    jsm "I see your dick's already up. That means my dance has done its job."
    jsm "This is good."
    scene 11stripsex04 with dissolve
    jsm "Now let's focus on your big cock."
    scene anim164 with dissolve
    "Jasmine's hot fingers tightened your dick and started moving."
    mc "{i}Oh, yeeesss... Finally!{/i}"
    jsm "Now I'm gonna squeeze you dry."
    pause
    scene 11stripsex04a with dissolve
    "You could see how a girl's gorgeous breasts rise in tune with her movements."    
    scene anim165 with dissolve
    jsm "You don't have to hold back, sugar. I can see how you feel."
    mc "Less words and more action."
    jsm "Oh... I think somebody likes to be in command. How interesting."
    pause
    scene 11stripsex05 with dissolve
    "With her free hand, Jasmine wrapped her boobs around her, making them look even bigger."
    scene anim166 with dissolve
    mc "{i}Fuck, that's really nice... But we shuold continue.{/i}"
    mc "Enough foreplay, I want you to work with your mouth."
    jsm "Mmm... Of course, the client's wishes are above all."
    pause
    scene 11stripsex06 with dissolve
    "The girl opened her mouth and touched the head of your dick with her tongue."
    mc "{i}I can feel her hot breath. This is so awesome.{/i}"
    mc "Now take him in your mouth."
    scene 11stripsex07 with dissolve
    "Jasmine gently wrapped her lips around your dick while still working with her tongue."
    scene anim167 with dissolve
    jsm "Mmmnnnhhh.... Mmmmnnnhhh.... Mmmmnnnhh...."
    mc "Yes... Now this is getting really interesting."
    mc "Come on, I know you can take it deeper."
    jsm "Mmmnnnh... Okay..."
    pause
    scene 11stripsex08 with dissolve
    "The girl submitted to your words, and soon all your dick was in her mouth."
    scene anim168 with dissolve
    mc "{i}Oh... She's a real pro at this.{/i}"
    jsm "Mmmnnnhhh.... Mmmmnnnhhh.... Mmmmnnnhh...."
    mc "Yeah... Don't stop... Suck it harder."
    pause
    scene 11stripsex09 with vpunch
    "The girl showed all her skills and almost totally gulped your dick."
    mc "Fuck, I don't think I can hold much longer."
    scene 11stripsex10 with dissolve
    "Jasmine stopped sucking and started jerking you off again."
    jsm "You held out pretty long, sugar."
    jsm "I like how endurance you are."
    scene 11stripsex11 with dissolve
    jsm "You don't have to hold back anymore, just cum right into my face."
    scene anim169 with dissolve
    mc "That's exactly what I wanted to do..."
    mc "But don't think you'll get rid of me so easily."
    jsm "Don't worry, we still have time..."
    jsm "Now, you'd better concentrate on this moment and come."
    mc "I'm almost..."
    pause
    scene 11stripsex11a with flash
    mc "Aaahhh..!"
    scene 11stripsex11a with flash
    mc "Fuck, take it!!!"
    scene 11stripsex11b with dissolve
    "..."
    mc "{i}Yeah... I feel much better now.{/i}"
    scene 11stripsex12 with dissolve
    jsm "Good shot."
    jsm "Let me clean up, and we'll continue where we left off."
    mc "All right."
    scene black with fade
    "A few minutes later."
    scene 11stripsex13 with dissolve
    "You were sitting on the couch and ready for a new dose of pleasure."
    scene anim170 with dissolve    
    jsm "I saw you and your friends staring at my boobs. All men react to them that way."
    jsm "But only a few people get that kind of service from me."
    mc "Oh... So I'm one of those few?"
    jsm "Oh, yeah... You are one of them."
    pause
    scene 11stripsex14 with dissolve
    mc "That's good, because as soon as I saw them, I wanted to fuck them."
    scene anim171 with dissolve
    jsm "Ah... You're such a bad boy."
    mc "{i}Her breasts are so big and firm... It's really nice.{/i}" 
    jsm "And what else did you want to do when you saw me?"
    mc "I think you can imagine that yourself..."
    pause
    scene 11stripsex15 with dissolve
    "Suddenly, Jasmine stopped and reached out to you."
    jsm "Tell you a secret, I like bad boys like you."
    jsm "And now..."
    scene 11stripsex16 with dissolve
    "She gave you a kiss."
    jsm "Mmm... Yes..."
    mc "{i}Man, that's really nice.{/i}" 
    scene 11stripsex15 with dissolve
    jsm "That was pretty good."
    mc "Yes, but... That's enough games. It's time to get to the point."
    jsm "If you say so."
    scene 11stripsex17 with dissolve
    "Jasmine turned her back on you and slowly started taking off her last clothes."
    jsm "You're right, now's the time to get to the point."
    scene 11stripsex18 with dissolve
    mc "{i}So now I will see her completely naked... Can't wait!{/i}"
    scene 11stripsex19 with dissolve
    "The girl was finally fully naked."
    mc "Wow! You've got an amazing ass!"
    jsm "Mmm... thanks, sweetie."
    scene 11stripsex20 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    mc "{i}And not just ass... Her whole body looks like it's from the cover of a glossy magazine.{/i}" 
    mc "{i}I'm so glad I agreed to her offer.{/i}"
    jsm "And if you like my butt so much, how about you try something else."
    scene 11stripsex21 with dissolve
    "Jasmine came close to you and started rubbing her ass on your dick."
    scene anim172 with dissolve
    mc "{i}She knows what she's doing. There's a real skill in her movements.{/i}" 
    mc "Oh... You really know how to please a man."
    jsm "Well, of course."
    pause
    scene 11stripsex22 with dissolve
    jsm "But this is all just one big foreplay."
    mc "Yes, that' s right. And now it's time to move on."
    mc "Now I want you to jump on my dick."
    jsm "Mmmm... Okay."
    scene 11stripsex23 with dissolve
    "Jasmine gently grabbed your cock..."
    jsm "Yeah, I think he's ready now."
    jsm "Now don't move, I'll do everything by myself."
    scene 11stripsex24 with vpunch
    "With a gentle, yet quick move, she put him in her pussy."
    mc "Ohh... Yes!"
    scene anim174 with dissolve
    "The girl started riding right in your lap."
    jsm "Um... I hope... you're enjoying this..."
    mc "{i}Oh, yeah, I do enjoy that.{/i}" 
    pause    
    scene anim173 with dissolve
    jsm "Aaahh.... Aaaahhh.... Aaaahhh..."
    mc "Come on, babe, don't stop."
    pause
    scene anim192 with dissolve
    "Jasmine sped up her moves."
    "..."
    pause
    scene anim175 with dissolve
    mc "{i}Fuck, I can watch this forever.{/i}" 
    mc "You're moving well, but how about changing our position?"
    jsm "Aahhh... If that's what you want."
    pause
    scene 11stripsex26 with dissolve
    "You took Jasmine by the hips and started moving on your own."
    scene anim176 with dissolve
    "At first, your moves were slow."
    jsm "Aaahh.... Aaaahhh.... Aaaahhh..."
    jsm "If you want... If you want, you can fuck me harder."
    mc "Yes... I know."
    pause
    scene 11stripsex27 with dissolve
    jsm "Mmm... Then what are you waiting for?"
    jsm "Harder! Fuck me harder!!!"
    mc "{i}Well, if she's asking me like that, how can I say no to her?{/i}" 
    scene 11stripsex28 with dissolve
    "Jasmine spread her legs, making it easier for you to move."
    scene anim177 with dissolve
    jsm "Aaahh! Aaaahhh! Aaaahhh!"
    mc "{i}Oohh... It's so nice, I don't think I can hold out much longer.{/i}" 
    mc "How's that? Are you feeling better now?"
    jsm "Yes!!! Now just keep fucking me!"
    pause
    scene 11stripsex29 with flash
    "You felt Jasmine's pussy squeeze tight for a moment, and her mouth was moaning."
    jsm "Aaahhh!"
    mc "{i}I need to speed up, I'll come soon myself!{/i}" 
    scene 11stripsex30 with dissolve
    jsm "Oh, God... You're not done yet?!"
    mc "Shut up, I'm about to..."
    scene 11stripsex31 with dissolve
    mc "I almost..."
    scene 11stripsex32 with flash
    mc "Yeah!!! I'm coming!!!"
    scene 11stripsex32 with flash
    "*Heavy breathing sounds*"
    scene 11stripsex33 with dissolve
    jsm "Haah... ah... That was... Fascinating..."
    jsm "Usually I don't come from clients, but today... It's been really good."
    mc "I'm glad we both enjoyed it."
    jsm "Yeah. But our time is up, so you should go."
    mc "Yes."
    stop music fadeout 2.0
    scene black with fade
    "A few minutes later, you paid off the girl and went back to your friends."
    scene 11stripsex34 with dissolve
    jsm "It's been a nice evening. Come back and see us again, [mc]."
    jsm "We'll always be happy to have such a good client."
    mc "Yeah, sure."
    $ renpy.end_replay()
    if not persistent.day11jasmine:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day11jasmine = True        
    play music "music/3 - Dream With U.ogg"
    scene 11stripsex35 with dissolve
    b "Hey, dude, where have you been? We've been looking for you everywhere."
    mc "I was in the bathroom."
    mc "I hope I didn't miss anything."
    b "Of course you missed it! You missed a few drinks!"
    b "Now you're gonna have to catch up with us. So sit down and drink!"
    mc "Haha! Got it, man."
    stop music fadeout 2.0
    
    if day11_stripper_02 == False or day11_stripper_03 == False:
        jump day11_stripper_choice
    jump day11_sclub_pt2

 
label day11_sclub_pt2:
    scene black with fade
    "Dozen shots later."
    play music "music/6 - Positive Mood.ogg"
    scene 11sclub80 with dissolve
    j "And guess what, I told Ruby I don't want to drag this out, and that we should have sex right here and now."
    scene 11sclub80a with dissolve
    j "But you know what the coolest part is?"
    mc "Uh-uh... What?"
    j "She was all for it!"
    j "Man, I'm telling you, we're made for each other!"
    mc "Good for you."
    j "Yeah, I'm glad for that, too."
    scene 11sclub81 with dissolve
    j "Okay, I think we're lost track of time chatting, let's have another drink. "
    mc "I feel like I've had enough."
    scene 11sclub81a with dissolve
    j "No! No! No excuses! Drink!"
    mc "Okay, okay, but this shot will be the last one."
    scene 11sclub82 with dissolve
    "You reached for another shot." 
    scene 11sclub83 with dissolve
    "With a sharp move, you drank it..."
    scene 11sclub84 with dissolve
    "...and leaned on the back of the couch."
    stop music fadeout 2.0
    scene 11sclub84a with dissolve
    "The world started spinning around you, but you didn't care anymore."
    scene 11sclub84b with dissolve
    "You fell into the darkness."
    scene black with fade
    "Some time later."


label day11_sclub_pt3:
    scene black with fade
    j "Hey, is it me, or did he pass out?"
    b "What? Are you serious?"
    b "Haha! You're right!"
    j "Well... Looks like somebody's had enough booze for today."
    b "Yeah, we gotta get him out of here."
    j "Hey, [mc], let's go."
    mc "Yeah... I'm coming..."
    scene 11sclub85 with fade
    scene black with fade
    $renpy.pause(0.1, hard=True)
    play music "music/9 - You Can Make the Sound.ogg"
    scene 11sclub85 with fade
    "The moment you opened your eyes, you suddenly realized you were at the exit of a strip club."
    j "Come on, man, let's go outside now and you'll feel better."
    mc "Okay..."
    scene 11sclub86 with dissolve
    v "What's wrong with him?"
    scene 11sclub87 with dissolve
    j "What does it look like? Just a little drunk."
    scene 11sclub86 with dissolve
    v "Yes, I can see that."
    v "Do you need any help?"
    scene 11sclub87 with dissolve
    j "Nah, thanks for the offer, but we got it under control."
    scene 11sclub87a with dissolve
    j "He'll get better outdoors, and we'll go hang out again!"
    scene 11sclub88 with dissolve
    v "..."
    v "No, it won't happen. He's had enough for today."
    v "He should go home."
    scene 11sclub90 with dissolve
    mc "It's all right... I'm gonna call a taxi and they're gonna pick me up right from here..."
    j "Haha! Dude, you can barely hit the buttons!"
    mc "Shh! It's okay... I'm almost done..."
    stop music fadeout 3.0
    scene 11sclub91 with dissolve
    "*Phone call*"
    mc "Come on... Pick up the phone..."
    "*Phone call*"    
    if nicole_plus == True:
        scene black with fade
        "At the same time, a few blocks away."
        play music "music/8 - Intro Music.ogg"
        scene 11nicphone01 with dissolve
        "At a nightclub table."
        scene 11nicphone02 with dissolve
        "{color=#F0FFFF}Man{/color}" "And I told him that if he wanted a cheaper car, he could go to some other car dealership."
        "{color=#F0FFFF}Man{/color}" "You're not gonna believe this, but I've never seen such cocky customers before."
        n "Yeah, I can imagine."
        scene 11nicphone03 with dissolve
        n "{i}Dear God, he's been telling me these stories for an hour now. Why are they all so boring?{/i}"
        n "{i}Uh... It's your fault, Nicole. You should've found someone more appropriate for tonight.{/i}"
        scene 11nicphone04 with dissolve
        "{color=#F0FFFF}Man{/color}" "......."
        scene 11nicphone02 with dissolve
        n "{i}Hmm? Is it just me, or did he just ask me something?{/i}"
        n "{i}Damn it, he's waiting for an answer.{/i}"
        n "{i}I have to tell him something, or he'll know I wasn't listening.{/i}"
        scene 11nicphone03a with dissolve
        n "Yeah, sure, you're absolutely right."
        scene 11nicphone04a with dissolve
        "The man's face showed a satisfied expression, and he continued his monologue."
        scene 11nicphone03 with dissolve
        n "{i}Okay, looks like it worked.{/i}"
        n "{i}But now I have to listen to him again...{/i}"
        n "{i}No, I can't do it anymore. I have to get out of here right now...{/i}"
        stop music fadeout 2.0
        scene 11nicphone05 with dissolve
        "*Phone Calling*"
        n "{i}Huh? And who's that?{/i}"
        scene 11nicphone06 with dissolve
        n "Wait a minute, I need to answer."
        "{color=#F0FFFF}Man{/color}" "Um... Yes, of course"
        play music "music/2 - Bad.ogg"
        scene 11nicphone07 with dissolve
        n "Hello?"
        mc "Is that a taxi?"
        n "Taxi?"
        scene 11sclub91 with dissolve
        mc "Yes, I need a taxi."
        "..."
        n "[mc]? Is that you?"
        scene 11sclub92 with dissolve
        mc "Eehhh... You're Nicole!"
        mc "Wow! I didn't know you part-time operators in taxis."
        n "Are you drunk?"
        mc "Hey, I'm not drunk - you're drunk!"
        n "..."
        scene 11sclub91 with dissolve
        mc "Well... Maybe just a little bit."
        n "[mc], are you all right in there?"
        scene 11sclub92a with dissolve
        mc "I'm totally fineee! Sorry, I probably just called the wrong place."
        n "Wait!... Ahem... Are you alone now?"
        mc "Huh? Nope, I'm with friends, and we're going to hang out."
        n "But didn't you just call a taxi to go home?"
        scene 11sclub91 with dissolve
        mc "Oh... Oh, yeah, right."
        n "Tell me where you are."
        scene 11sclub92 with dissolve
        mc "Where? Hmm... I'm not even sure... Outside some strip club."
        mc "I think it's one block from your place of work."
        n "I think I know where you are."
        mc "You do?"
        n "Yes."
        scene 11sclub91 with dissolve
        mc "But why do you ask?"
        n "I want to pick you up."
        scene 11sclub92 with dissolve
        mc "What?! Really? You don't have to. I can-"
        n "It's okay. Stay where you are, I'll be right there soon."
        scene 11sclub91 with dissolve
        mc "Eh... Okay, you volunteered it. I'll wait for you here."
        scene 11sclub90 with dissolve
        mc "Wow, that's a conversation."
        scene 11nicphone08 with dissolve
        n "Sorry, Greg, but my friend got into trouble. I need to pick him up."
        scene 11nicphone09 with dissolve
        "{color=#F0FFFF}Greg{/color}" "What? Wait... Are you sure he needs your help?"
        "{color=#F0FFFF}Greg{/color}" "Maybe he can handle himself."
        scene 11nicphone08 with dissolve
        n "Sadly, but if I don't get to him now, I'm sure he'll get in trouble."
        n "Sorry again, but I'll go."
        scene 11nicphone09 with dissolve
        "{color=#F0FFFF}Greg{/color}" "Yes, I understand... I'm sorry about what happened."
        scene 11nicphone10 with dissolve
        "With a slight smile on her face, Nicole headed for the exit."
        "{color=#F0FFFF}Greg{/color}" "I'll call you again sometime! Okay?"
        n "I highly doubt that."
        stop music fadeout 2.0
        scene 11sclub90 with fade
        mc "Okay, looks like I'm about to be picked up."
        play music "music/7 - Just Happy.ogg"
        j "Hmm... Maybe it's for the best."
        scene 11sclub93 with dissolve
        b "Hey, guys, sorry I'm a little late, but all these hotties just kept me from going out."
        j "Yeah, whatever."
        b "Anyway, I took a bottle of water. Maybe [mc] will get a little better with it."
        scene 11sclub94 with dissolve
        mc "Thanks, man. I'm dying of thirst."
        scene 11sclub95 with dissolve
        "A few seconds later, you've started eagerly swallowing water."
        mc "Ahh... This is so good!"    
        j "Yeah, we can see that."
        scene 11sclub96 with dissolve
        b "Phew! What a night. It's almost like the good old days."
        scene 11sclub97 with dissolve
        mc "Yeah. Crazy day."
        scene 11sclub98 with dissolve
        j "By the way, [mc], who did you just call? Who is this Nicole?"
        scene 11sclub97a with dissolve
        mc "Oh, that... A friend of mine from my sister's work."
        scene 11sclub96 with dissolve
        b "From whose work?"
        scene 11sclub97 with dissolve
        mc "Forget it. Everything is okay."
        scene 11sclub98 with dissolve
        j "So she should pick you up soon?"
        scene 11sclub97a with dissolve
        mc "Yeah, kind of... Could you wait for her with me?"
        scene 11sclub96 with dissolve
        b "Hmm... Okay. I hope it doesn't take too long."
        stop music fadeout 2.0        
        scene black with fade
        "A few minutes later."
        play music "music/9 - You Can Make the Sound.ogg"
        scene 11clubn01 with dissolve
        mc "All right, guys, looks like my escort finally arrived."
        b "Hey, that's a nice car."
        j "And the girl's driving is really good too."
        b "Definitely."
        scene 11clubn02 with dissolve
        mc "Okay, I'm out of here. Have a good night."
        b "See ya tomorrow, man."
        j "Do not oversleep tomorrow morning! We have a big day."
        mc "Yeah, yeah... I remember..."
        scene 11clubn03 with dissolve
        "Swaying from side to side, you went to the car."
        scene 11clubn04 with dissolve
        mc "Hellooo, beauty! How much it would cost me to ride a home?"
        scene 11clubn05 with dissolve
        "..."
        scene 11clubn05a with dissolve
        n "Just get inside before I change my mind. And try not to make any unpleasant surprises in here."
        scene 11clubn06 with dissolve
        mc "Hey, even though I had a few drinks, I'm still holding myself together."
        scene 11clubn05a with dissolve
        n "Yeah, I can see in what condition you are."
        n "It's a good thing I was there to pick you up."
        scene 11clubn06 with dissolve
        mc "Huh? Then I'm lucky."
        scene 11clubn05a with dissolve
        n "Yes, you are."
        n "Now, as I said, get in here and try to keep it together."
        scene 11clubn06 with dissolve
        mc "No problem! Hehe."
        scene 11clubn07 with dissolve
        mc "Wow! Your car is so comfortable."
        n "I'm glad you like it."
        mc "Uh-huh."
        scene 11clubn08 with dissolve
        mc "Ah! If only you knew what an epic day it was! Friends, booze, girls... Everything was just great!"
        n "Sounds like fun."
        mc "Yes, it was!"
        scene 11clubn09 with dissolve
        mc "Hmm. By the way, I have to say, you look great today."
        mc "It doesn't look like you came here from home."
        scene 11clubn10 with dissolve
        n "I never said I was home."
        mc "Oh, yeah. Right."
        scene 11clubn11 with dissolve
        n "Okay, I think we're done here. Shall we go?"
        mc "Yeah, let's go!"
        play sound "music/car_engine.mp3"
        scene 11clubn11a with dissolve
        "*Engine sound*"
        scene 11clubn12 with dissolve
        mc "Hey, don't you think it's too quiet in here? Maybe we should put on some music."
        n "Don't touch that, please."
        mc "Um... Okay, sorry."
        n "It's fine, just keep it down a bit, I had a really bad night."
        mc "Got it."
        scene 11clubn13 with dissolve
        mc "Oh! Look, there's a 24-hour diner! Let's stop, I'm starving."
        n "I thought you wanted to go home?"
        mc "Yeah, but I want to eat much more than I want to go home."
        mc "Besides, my fridge is probably empty right now. And waiting for delivery is too long."
        scene 11clubn14 with dissolve
        n "Eh, okay. But only for a few minute."
        mc "Deal!"
        stop music fadeout 2.0
        jump day11_nicole_dinner
    else:
        scene 11sclub90 with dissolve
        mc "Shit... No one's picking up the phone."
        play music "music/2 - Bad.ogg"
        scene 11sclub89 with dissolve
        v "Enough of this. I'll call a cab for you myself."
        mc "You do?"
        v "Yeah, just try not to do anything stupid."
        scene 11sclub93 with dissolve
        b "Hey, guys, sorry I'm a little late, but all these hotties just kept me from going out."
        j "Yeah, whatever."
        b "Anyway, I took a bottle of water. Maybe [mc] will get a little better with it."
        scene 11sclub94 with dissolve
        mc "Thanks, man. I'm dying of thirst."
        scene 11sclub95 with dissolve
        "A few seconds later, you've started eagerly swallowing water."
        mc "Ahh... This is so good!"    
        j "Yeah, we can see that."
        scene 11sclub96 with dissolve
        b "Phew! What a night. It's almost like the good old days."
        scene 11sclub97 with dissolve
        mc "Yeah. Crazy day."
        scene 11sclub98 with dissolve
        j "So you're gonna go home now?"
        scene 11sclub97a with dissolve
        mc "I drank too much. It's better to do it right now."
        mc "I'm gonna go home, get some sleep and everything will be great again."
        scene 11sclub98 with dissolve
        j "Well, it's probably for the best."
        scene black with fade
        "Some time later, a cab came up to you. You said goodbye to your friends and jumped into it."
        scene 11sclub99 with dissolve
        "You gave your address, and the cab driver took you home right away."
        scene 11sclub100 with dissolve
        mc "{i}Wow...{/i}"
        "Thoughts ran slowly through your head, but you were happy with that night."
        "And yet, you had the feeling that tomorrow was going to be a very important day."
        mc "{i}Uh, I should stop thinking about it...{/i}"
        stop music fadeout 2.0
        scene black with fade
        "Some time later, a taxi driver dropped you off outside your house and drove off into the night city."
        "You went to your apartment."
        "There was a new day ahead of you."
        jump day11_rivals_band


label day11_nicole_dinner:
    scene black with fade
    "Some time later."
    play music "music/6 - Positive Mood.ogg"
    scene 11diner01 with dissolve
    "You were sitting at the cafeteria table eating burgers in silence."
    "The effect of alcohol was fading."
    n "So, how are you?"
    scene 11diner01a with dissolve
    mc "Yes, thank you, I feel much better now. The food and coffee are really refreshing."
    mc "And I'm sorry about my behavior in the car."
    scene 11diner02a with dissolve
    n "It's fine, I'm not angry."
    n "You were drunk, and now you're feeling sober. It's okay."
    scene 11diner01a with dissolve
    mc "Anyway, thanks for picking me up. I don't think I would be able to continue this evening at the same pace."
    scene 11diner02 with dissolve
    n "Judging by how quickly you came to your senses, you're a lot stronger than you think."
    scene 11diner01a with dissolve
    mc "Yeah, maybe. But I wouldn't want to test it in practice."
    scene 11diner02 with dissolve
    n "So, what was the occasion for such a big drink?"
    scene 11diner04b with dissolve
    mc "An occasion? Well, there wasn't really much of an occasion."
    scene 11diner04 with dissolve
    mc "I just met some old friends and we decided to remember the good old days. And then I didn't even realize how we ended up in a strip club."
    mc "The thing is that tomorrow we will have a new gig, so we decided to have a good time before it."
    scene 11diner02 with dissolve
    n "Strip club? It's a pretty interesting way to hang out."
    scene 11diner04 with dissolve
    mc "Hey, don't judge me! It wasn't just me who made the decision where to go."
    scene 11diner02 with dissolve
    n "If you say so."
    scene 11diner01a with dissolve
    mc "So what about you?"
    mc "Based on your clothes, I can assume you were somewhere in a public place."
    mc "Besides, you came to get me real quick, which means you were somewhere nearby."
    scene 11diner03b with dissolve
    n "If you're really interested, I was on a date at a nightclub."
    scene 11diner04 with dissolve
    mc "A date? That's interesting."
    mc "Then why did you drop everything and go save my drunk ass?"
    scene 11diner03b with dissolve
    n "Let's just say this date left a lot to be desired."
    scene 11diner04c with dissolve
    mc "Well, I'm sorry to hear that."
    scene 11diner03 with dissolve
    n "It's okay. In fact, you did me a big favor with your call. I'm not sure if I could stand this guy for even a few more minutes."
    n "I used to always think I was a bore myself. But I stopped thinking that today."
    scene 11diner04 with dissolve
    mc "No way, you're definitely not a bore."
    mc "I will be honest with you, you have a certain charm. You're so quiet... So mysterious. I really like you!"
    scene 11diner02 with dissolve
    n "Oh, thank you."
    scene 11diner01a with dissolve
    mc "By the way, if you're so sick of this date guy, why didn't you just leave him?"
    scene 11diner02a with dissolve
    n "Why didn't I leave? Yes, that's a good question..."
    scene 11diner03a with dissolve
    "Nicole was thinking for a moment."
    scene 11diner03b with dissolve
    n "I'm not sure, but it's probably because I expected to have sex tonight."
    stop music fadeout 1.0
    scene 11diner04c with dissolve
    mc "Whoa."
    scene 11diner02a with dissolve
    n "Don't do that."
    play music "music/6 - Positive Mood.ogg"
    scene 11diner04a with dissolve
    mc "Don't do what?"
    scene 11diner02a with dissolve
    n "You don't have to react like that to what I'm saying."
    n "Sex is just a biological necessity. By fulfilling this need, it is much easier to concentrate on what is really important to you."
    mc "{i}Oh, wow. Even with all her weirdness, I didn't expect this.{/i}"
    scene 11diner04 with dissolve
    mc "To concentrate? On what, for example?"
    scene 11diner03 with dissolve
    n "On work, of course."
    mc "{i}Well, yeah, sure... Given how much workaholic she is, I could have guessed it myself.{/i}"
    scene 11diner03a with dissolve
    n "Besides, if things keep going like this, I'm going to want to smoke again soon. And I really don't want that."
    scene 11diner01a with dissolve
    mc "Well, in that case, I feel twice as sorry for you. Looks like your evening didn't go exactly as you planned."
    scene 11diner03b with dissolve
    n "Yeah, I guess so..."
    scene 11diner03a with dissolve
    n "Although... If you think about it..."
    scene 11diner05 with dissolve
    "You noticed how Nicole's eyes changed. Now she was looking at you with some kind of interest."
    n "Hey, how about helping each other?"
    scene 11diner06 with dissolve
    mc "Uh... What?"
    mc "You're not talking about what I was just thinking right now, are you?"
    scene 11diner05 with dissolve
    n "You got it right. That's exactly what I'm talking about."
    scene 11diner04c with dissolve
    mc "Wait, wait a minute... Am I still too drunk, or did you really ask me to fuck you just now?"
    scene 11diner03b with dissolve
    n "Not in such vulgar words, but yes."
    scene 11diner03 with dissolve
    n "That way I can concentrate on work, and you can concentrate on your gig tomorrow. In the end, everyone is happy."
    if jane_date_offer == True:
        scene 11diner04c with dissolve
        mc "But you know I'm still dating Jane, right?"
    else:
        scene 11diner04a with dissolve
        mc "I don't know what to say to that."
    scene 11diner03b with dissolve
    n "Relax, I'm not asking you for a relationship or anything like that."
    n "You can think of it as a joint sport we'll never tell anyone about."
    scene 11diner04 with dissolve
    mc "A joint sport? Ha! That's a great comparison you got there."
    scene 11diner05 with dissolve
    n "Call it whatever you want. But tell me, do you agree?"
    stop music fadeout 1.0
    scene 11diner04b with dissolve
    mc "{i}What a great offer. What do I have to answer her?{/i}"
    menu:
        "Accept her offer (Nicole scene)":
            $ day11_nicole_sex = True
            play music "music/9 - You Can Make the Sound.ogg"
            scene 11diner04 with dissolve
            mc "You know what... Yes, I agree!"
            scene 11diner05 with dissolve
            n "Good. So I was right about you."
            scene 11diner07 with dissolve
            "Suddenly, you felt Nicole's barefoot stretch under the table in your direction."
            scene 11diner09 with dissolve
            mc "{i}Hey, what the hell?!{/i}"
            scene 11diner08 with dissolve
            "And then, she gently touched your dick."
            mc "Huh. Don't tell me you decided to do it right here?"
            scene 11diner10 with dissolve
            n "Of course not, I just wanted to test you."
            scene 11diner04a with dissolve
            mc "Test me? What do you mean?"
            scene 11diner10 with dissolve
            n "Oh, don't worry, you passed the test."
            scene 11diner08 with dissolve
            n "Judging from your enlarged cock, I can assume you're full of energy today."
            n "This is very good."
            scene 11diner04 with dissolve
            mc "Well, of course, otherwise I wouldn't have taken you up on your offer."
            scene 11diner10 with dissolve
            n "All right, how about you move into my house and get to the main part?"
            scene 11diner04 with dissolve
            mc "She's seriously asking me! Let's go!"
            scene 11diner11 with dissolve
            "Having a good time talking to each other, you and Nicole went back to her car."
            stop music fadeout 2.0
            scene black with fade
            "Some time later."
            jump day11_nicole_sex

        "Refuse":
            play music "music/9 - You Can Make the Sound.ogg"
            scene 11diner04c with dissolve
            mc "Sorry, but I'm not interested."
            scene 11diner05a with dissolve
            n "Hmm. That's a shame."
            n "In this case, I guess I'll have to go on a few more dates."
            scene 11diner04c with dissolve
            mc "Yeah, I guess so..."
            scene 11diner03b with dissolve
            n "I'd appreciate it if this conversation would just stay between us."
            scene 11diner04a with dissolve
            mc "Yeah, you don't have to worry about that."
            scene 11diner02a with dissolve
            n "Okay."
            n "Finish up here, and I'll take you home."
            scene 11diner04a with dissolve
            mc "Uh-huh. Let's go."
            scene 11diner11a with dissolve
            "You and Nicole quietly went back to her car."
            stop music fadeout 2.0
            scene black with fade
            "Some time later, she dropped you off at your house and drove off into the night city."
            "You went to your apartment."
            "You turned around a long time before you fell asleep. You couldn't give up on the idea that tomorrow would be a very important day."      
            jump day11_rivals_band

    "..."



label day11_nicole_sex:
    if _in_replay:
        $ setReplay()
    play music "music/2 - Bad.ogg"
    scene 11nicole01 with dissolve
    "Shortly after, you arrived at the underground parking near Nicole's house."
    mc "Hmm... So that's where you live. It's not far from my home."
    scene 11diner13 with dissolve
    n "Yeah, I moved here recently. Still paying for the mortgage and I'll probably be paying for another dozen years."
    mc "I'm sorry to hear that."
    n "It's all right, a lot of people live like this. Besides, I have a good job paying the bills."
    scene 11diner12 with dissolve
    mc "Although I'm a little surprised you decided to bring me to your home and not to some hotel or other place."
    n "Is that a problem?"
    mc "No, nothing like that. It's more like the opposite."
    scene 11diner13a with dissolve
    n "You know you're acting weird, right?"
    mc "Really? I guess the silence makes me a little nervous."
    scene 11nicole02 with dissolve
    "Nicole parked, and you started getting out of the car."
    n "And why is that making you nervous?"
    mc "I don't know. It's just that while we were driving I had time to think and-"
    n "Don't tell me you changed your mind."
    mc "What?"
    mc "No. Of course not."
    scene 11nicole03 with dissolve
    n "Hmm... For that brief moment, you almost scared me."
    mc "Huh, really? I can't even imagine you being scared of anything."
    n "It's just a phrase. But you're right, it's not easy to scare me."
    scene 11nicole04 with dissolve
    n "Don't get me wrong, I know it's all very sudden, but still I don't want to waste time."
    n "That date I told you before, I don't want this situation to happen again."
    scene 11nicole05 with dissolve
    n "So... I'm not wasting my time, am I?"
    mc "{i}Uh, I sure wouldn't want to piss off that dissatisfied workaholic.{/i}"
    scene 11nicole06 with dissolve
    mc "You don't have to worry about that. You're certainly not wasting your time."
    mc "In fact, I wanted to say that I'm barely holding back from doing what we're planning to right here in the parking lot."
    scene 11nicole06a with dissolve
    n "Huh."
    n "In that case, if you wait a little longer, your efforts will be rewarded."
    mc "{i}I still can't believe she offered to have sex with her.{/i}"
    scene 11nicole07 with dissolve
    n "Now follow me, there's something else we need to discuss."
    mc "{i}Something else to discuss?{/i}"
    scene 11nicole08 with dissolve
    mc "What do you mean?"
    n "I want you to understand that everything that will happen today between us is a one-time offer."
    n "After this night, we'll act as if nothing happened. Cause I don't want to get in trouble with my new boss."
    mc "Absolutely. I don't need any trouble either."
    n "Good... I'm glad we understood each other."
    scene 11nicole09 with dissolve
    "Soon you were at the elevator."
    mc "You know, I was suddenly wondering why you turned down a guy from your date, but offered to have sex with me?"
    n "Why?"
    mc "Yeah, why."
    n "Hmm. I would rather not answer this question."
    mc "Oh, come on, just tell me."
    play sound "music/elevator.mp3"
    stop music fadeout 2.0    
    scene 11nicole10 with dissolve
    "*Elevator opening sounds*"
    mc "You're lucky the elevator saved you."
    play music "music/6 - Positive Mood.ogg"
    scene 11nicole11 with dissolve
    n "Do you really want to know why I chose you?"
    mc "Yeah, I'm really curious about that."
    n "Okay, if you really wanna know, I'll answer."
    n "The thing is, you've got a certain amount of charisma and a strong core... And I also like the way you treat me."
    scene 11nicole12 with dissolve
    "Without saying another word, Nicole pressed the elevator button."
    mc "{i}Charisma and the core? That's interesting.{/i}"
    scene 11nicole13 with dissolve
    n "Well, what about you?"
    n "Is there something about me that attracts you?"
    mc "Hmm... I guess there's so many things at once that I can't even pick one."
    scene 11nicole14 with dissolve
    n "Hmph... For such a young guy, you're a really good talker."
    mc "A young guy? You're only five or six years older than me."
    n "If you were a little older, you'd understand that age is an experience."
    mc "Oh, so that's how it works..."
    n "Yes."
    scene 11nicole15 with dissolve
    mc "Well, if you really think so, there's a big surprise waiting for you."
    n "Mmm... Someone seems pretty confident today."
    mc "Believe me, there are very good reasons for that."
    scene 11nicole16 with dissolve
    "You got close to Nicole."
    mc "Let's just say I have some good experience with beautiful women."
    n "Oh, really?"
    mc "Yep. And soon you'll be able to feel it on your own."
    scene 11nicole17 with dissolve
    mc "Although, you know... Maybe I should demonstrate a piece of my inner core right here."
    n "I don't think that's-"
    scene 11nicole18 with dissolve
    "And then you kissed her."
    n "Mmm..."
    scene 11nicole19 with dissolve
    "Without wasting time, your hands started to act."
    scene 11nicole19a with dissolve
    "Your palm slipped smoothly down Nicole's thigh, lifting her skirt."
    mc "{i}She has magnificent legs.{/i}"
    scene 11nicole20 with dissolve
    "Then your hands got a little higher."
    mc "{i}And not just the legs.{/i}"
    scene 11nicole21 with dissolve
    n "I'm impressed with how skillfully you managed to unbutton my blouse. I didn't even notice it."
    mc "Oh, so I was able to impress you? That's good."
    n "Yes, I think so too."
    scene 11nicole22 with dissolve
    n "But that's where we'll stop for now. We'll continue when we get to my apartment."
    n "Don't want the neighbors to notice me like this."
    mc "That's too bad... You look especially hot right now."
    play sound "music/elevator.mp3"    
    scene 11nicole23 with dissolve
    "*Elevator opening sounds*"
    mc "Your floor?"
    n "Yes, let's go..."
    stop music fadeout 2.0
    scene 11nicole24 with dissolve
    "You followed Nicole right to her apartment."
    play music "music/4 - Ready to Drive.ogg"
    scene 11nicole25 with dissolve
    n "Well, here we are."
    mc "{i}Finally. Now we're going to continue where we left off.{/i}"
    scene 11nicole26 with dissolve
    n "Welcome to my humble abode."
    mc "Hmm... It's pretty cozy in here. I like it."
    n "Thank you."
    scene 11nicole27 with dissolve
    n "The apartment isn't big, but as you noticed, it's pretty cozy."
    n "Don't be shy, you can feel at home."
    mc "Huh. I can feel at home?"
    scene 11nicole28 with dissolve
    n "Wait, we've just got here..."
    mc "Hell, no! We won't be distracted anymore. Now you're all mine."
    mc "Now come here."
    scene 11nicole29 with dissolve
    "You grabbed Nicole's waist and lifted her up in the air."
    n "Hey, what are you doing?!"
    mc "Me? Just want to kiss you."
    scene 11nicole30 with dissolve
    "You immediately put the girl on the floor and your lips met with her."
    n "Mmm..."
    mc "{i}Uh... She's a really good kisser.{/i}"
    scene 11nicole31 with dissolve
    n "It was good."
    mc "Yeah, I agree."
    n "But it looks like you haven't turned on enough yet."
    n "Let me help you with that."
    mc "{i}What is she up to?{/i}"
    scene 11nicole32 with dissolve
    "Nicole started slowly pulling off her skirt."
    mc "{i}I see now. And I like where this is going.{/i}"
    scene 11nicole32a with dissolve
    mc "Yes, that's much better."
    mc "{i}She has an amazing ass.{/i}"
    mc "Now let's continue where we left off..."
    scene 11nicole33 with dissolve
    "You kissed her again."
    scene anim178 with dissolve
    n "Aahh... Mmmnnn..."
    "Your hands wrapped around her hot hips and firm ass."
    mc "{i}Oh, my God, that feels so good...{/i}"
    pause
    scene 11nicole34 with dissolve
    "Keeping kissing Nicole, you picked her up."
    mc "{i}Judging by the way she responds to me, she likes it as much as I do.{/i}"
    scene 11nicole35 with dissolve
    "Your hands kept patting the girl's soft butt."
    mc "{i}Perhaps we can move on now. I need to show her the best I can do.{/i}"
    scene 11nicole36 with dissolve
    "Few moments later, you put Nicole on the closest table to you."
    mc "How about we do something more exciting?"
    n "I'd be happy to."
    scene 11nicole37 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    "For a brief moment, you stopped and looked at her."
    mc "{i}Man, she is so sexy in these underwear.{/i}"
    n "Did you see something interesting?"
    mc "Yeah... I saw you."
    scene 11nicole38 with dissolve
    n "How about a small test?"
    mc "Test?"
    n "That's right."
    n "You were bragging a lot as we walked in here... I want to see how good you are at making a girl satisfied."
    mc "Hmm... I think I know what you mean."
    scene 11nicole39 with dissolve
    mc "Then let's start by taking off everything that can stop us."
    n "If you think it's necessary..."
    scene 11nicole39a with dissolve
    "The next second, you put Nicole's heels aside."
    scene 11nicole40 with dissolve
    n "So what are you gonna do next?"
    mc "A little patience, babe, it's just a setup. Pretty soon, we're gonna get to more exciting things."
    n "I'm looking forward to it."
    scene 11nicole41 with dissolve
    "With gentle moves, you grabbed Nicole's panty tips..."
    scene 11nicole41a with dissolve
    "...and then pulled them off."
    mc "What a magnificent view."
    mc "{i}And I especially like her pretty pink pussy.{/i}"
    n "Mmm... I like how confident you are."
    n "Please go on."
    scene 11nicole42 with dissolve
    "You got down on your knees and gently touched her."
    n "I hope you know what to do."
    mc "Don't worry, just lean back and enjoy the moment."
    stop music fadeout 2.0
    scene 11nicole42a with dissolve
    "As soon as your fingers started caressing Nicole's pussy, she immediately made a soft moan."
    n "Aaahh..."
    n " Mmnn... Yes, [mc]... It's a good start, but I want more."
    mc "Of course."  
    play music "music/Maxim Nick - Falling Down.mp3"
    scene 11nicole43 with dissolve
    mc "{i}I'm sure she'll love it.{/i}"  
    scene anim180 with dissolve   
    "You noticed that Nicole's breathing had become heavy and she starts moving in tune with your strokes."
    n "Haah... Haah... Haaahhh...."
    mc "{i}Looking at her, you can tell for sure she's enjoying it.{/i}"
    pause
    scene anim179 with dissolve
    n "Mmm... You were right... You know how to give a girl pleasure."
    n "Yeah... Like this... Just a little more."
    pause
    scene 11nicole44 with dissolve
    "Feeling an upcoming orgasm, you increased your efforts."  
    scene anim181 with dissolve
    n "Aaahhh... Aaahhh.. Aaahhh..." 
    mc "{i}Fuck, her moans are turning me on.{/i}"
    pause
    scene 11nicole45 with dissolve
    "Looking at Nicole's face for just a second, you realize she's enjoying it."
    scene anim182 with dissolve
    n "Yes, [mc]! Just a little more!!!"
    n "Aahhh.. I'm almost..."
    pause
    scene 11nicole47 with flash
    "Suddenly you felt Nicole's legs squeeze around you, and she unconsciously pressed you against her."
    scene 11nicole47 with flash
    n "Mmmmm!!!"
    scene 11nicole48 with dissolve
    "*Heavy breathing sounds*"
    n "..."
    mc "Ahh... Maybe you can say something?"
    n "Sorry, I need some time to catch my breath."
    mc "I see."
    scene 11nicole49 with dissolve
    mc "You know, I thought you were happy. So how about you give me the credit now?"
    n "Mmm... Yeah, you certainly deserve it."
    scene 11nicole50 with dissolve
    n "Just give me a minute to take these clothes off."
    mc "Of course... We certainly won't need it right now."
    scene 11nicole51 with dissolve
    "Just a few seconds later, Nicole was totally naked right in front of you."
    mc "Wow... You look incredible."
    n "Thank you."
    scene 11nicole52 with dissolve
    mc "{i}Damn, I knew she was beautiful, but only now I realized exactly how hot she is.{/i}"
    mc "{i}Okay, I should stop staring at her.{/i}"
    n "It's okay, you can look at me as long as you want. I even like that."
    mc "{i}Huh? Is she reading my mind?{/i}"
    scene 11nicole53 with dissolve
    n "Okay, I think you've waited enough today. You don't have to hold back anymore. It's my turn to make you feel good."
    n "Come here, hon. I'll take good care of you."
    scene 11nicole54 with dissolve
    "Nicole opened her mouth like she was inviting you to do whatever you wanted to her."
    mc "How can I resist such an offer?"    
    scene 11nicole56 with dissolve
    "The moment later, the head of your dick touched her naughty tongue."
    n "Oho... You've got a big one."
    mc "Yes, baby... Now take it in your mouth."
    scene 11nicole56a with dissolve
    "The girl followed your request and put whole your dick in her mouth."
    scene anim183 with dissolve
    "And then she started sucking it."
    mc "{i}Oh, yeah... Her mouth feels so good.{/i}"
    n "Mmmmhhhh... Mmmmhhhh.... Mmmmhhhh..."
    mc "Yeah, baby, take it deeper!"
    pause
    scene 11nicole58 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1
    mc "{i}What a lovely view from here.{/i}"
    mc "{i}This ass, these curves... I could look at them forever.{/i}"
    scene anim184 with dissolve
    n "Mmmmhhpss... Mmhhppsss.... Mmmhhppss..."
    mc "{i}Ugh! She sucks amazing!{/i}"
    mc "Ohh... Don't stop, babe. Just a little more and I'll definitely come."
    pause
    scene 11nicole57 with dissolve
    "You fell for a sudden desire, grab Nicole's head and started to fuck her with all your might."     
    scene anim185 with dissolve
    mc "{i}Fuck! I can't control myself, it feels so good!!!{/i}"
    n "Mmmmhhpss! Mmhhppsss!! Mmmhhppss!!!"
    mc "{i}Oohhhhh... I'M ALMOST!!!{/i}"
    pause
    scene 11nicole59 with dissolve
    "And then you started coming at a girl's mouth."
    scene 11nicole59a with flash
    mc "YEEESSS!!!"
    scene 11nicole59b with flash
    mc "Take it!!!"
    stop music fadeout 1.0
    scene 11nicole60 with dissolve
    "..."
    mc "{i}Oh, fuck... I think I overdid it.{/i}"
    mc "{i}Fuck, fuck, fuck!{/i}"
    scene 11nicole61 with dissolve
    "For some time, Nicole was just staring at you in silence."
    scene 11nicole62 with dissolve
    "..."
    scene 11nicole63 with dissolve
    "Then she did something that almost broke your pattern."
    scene 11nicole64 with dissolve
    n "Mmm..."
    scene 11nicole65 with dissolve
    n "I had no idea you were capable of this... How fascinating."
    play music "music/8 - Intro Music.ogg"    
    mc "{i}Huh?{/i}"
    mc "{i}She liked it?{/i}"
    n "Don't look at me like that. I told you I like a man to have a strong core."
    scene 11nicole66 with dissolve
    "In an instant, you pulled off the rest of your clothes and found yourself right next to her."
    mc "No more games, no more foreplay... Now I'm gonna take you to bed and fuck you properly."
    n "Then what are these words for? Just take me and do it."
    scene 11nicole67 with dissolve
    "You picked up the girl in your arms and pressed her firmly against yourself."
    n "*Cheerful laugh*"
    mc "{i}I've never seen her in this kind of mood before.{/i}"
    scene 11nicole68 with dissolve
    "Throwing Nicole on your shoulder, you headed towards her bedroom."
    n "Hey, I can walk myself."
    mc "Nope. I'll get that sweet ass to the bed personally."
    scene 11nicole69 with dissolve
    n "Mmm... You afraid that I' m gonna run away from you?"
    mc "Huh. I highly doubt you'd be able to do that even if you really wanted to."
    mc "And now..."
    play sound "music/slap.mp3"
    scene 11nicole70 with vpunch
    "*Slap*"
    mc "No more questions."
    scene 11nicole71 with dissolve
    "..."
    mc "That's better."
    stop music fadeout 2.0
    scene black with fade
    "Some time later."
    play music "music/Maxim Nick - Smooth Light.ogg"
    scene 11nicole72 with dissolve
    "You sat patiently on the bed and waiting."
    mc "{i}She's in no hurry...{/i}"
    scene 11nicole73 with dissolve
    "A few seconds later, Nicole came out of the bathroom."
    n "Sorry to keep you waiting, but I wanted to get my makeup clean."
    mc "I told you it wasn't necessary. You've already been very beautiful... Although, you look even better now."
    n "I'm glad you appreciate it."
    scene 11nicole74 with dissolve:
        linear 6.0 yalign 1.0
        linear 6.0 yalign 0.0
        repeat 1 
    "Nicole came closer and touched your dick with her foot."
    n "Are you ready for round two?"
    mc "You can rest assured, I'm full of energy and strength."
    n "Excellent."
    scene 11nicole75 with dissolve
    "Before you knew it, the girl was right on top of you."
    n "And now it's time for sex."
    mc "Yeah, time to have some fun."
    scene 11nicole76 with dissolve
    "You wrapped your hands around Nicole and slowly started to put your dick in her."
    mc "{i}Just a little more...{/i}"
    scene 11nicole77 with dissolve
    n "Aaahhh...."
    n "Oh, god, finally."
    mc "I see you've missed it."
    scene 11nicole76 with dissolve
    n "Mmm... That's why you're here today."
    mc "Let's get started, then."
    scene anim187 with dissolve
    "A few seconds later, Nicole started riding your dick with a happy face."
    n "Aaahh... Aaaahhh... Aaahhhh..."
    mc "{i}Her pussy is awesome. She's squeezing me so tight...{/i}"
    pause
    scene 11nicole78 with dissolve
    "Nicole accelerated."
    scene anim186 with dissolve
    n "Oh, that's really nice..."    
    mc "Oohhhh... Move your hips, baby! Yeah, that's it!"
    n "God, your dick is so big... Ahh..."    
    pause
    scene 11nicole79 with dissolve
    "You fell for a sudden desire and grabbed a girl's breast."
    mc "{i}Her boobs may not be that big, but they're very nice to the touch.{/i}"
    mc "{i}All right, I've had enough of lying down, I should take care of her myself.{/i}"
    mc "You did a good job, but now leave it to me..."
    scene 11nicole80 with dissolve
    "The next second, you turned Nicole on her stomach."
    n "Ah... I'm all yours."
    mc "I like the way it sounds."
    scene 11nicole81 with dissolve
    mc "{i}And I love the way it looks.{/i}"
    scene 11nicole82 with dissolve
    mc "{i}Let's start slowly...{/i}"
    scene anim189 with dissolve
    mc "{i}Oh, fuck, that's so hot.{/i}"
    n "Aahhh... Mmmnn..."
    pause
    scene anim188 with dissolve
    "You started moving faster."
    mc "Do you like it?"
    n "Mmmm... Yes, I do..."
    pause
    scene 11nicole83 with dissolve
    mc "Babe, get up a little."
    n "If you want..."
    scene 11nicole86 with dissolve
    "You grabbed Nicole's boobs and keep fucking her."
    scene anim191 with dissolve
    n "Aahhhh... You've got so much energy in you."
    mc "Yeah... When there's such a hottie next to me, it can't be otherwise."
    mc "{i}Just a little more and I'll come.{/i}"
    pause
    scene 11nicole87 with dissolve
    n "Do you like my boobs that much?"
    mc "Yeah, they're pretty damn good."
    n "Mmm... Kiss me."
    mc "With pleasure."
    scene 11nicole88 with dissolve
    "*Kiss*"
    mc "{i}Shit, I can't hold back anymore. Where do I come?{/i}"
    menu:
        "Cum inside":
            scene 11nicole90 with dissolve
            "Couldn't hold back, you started coming right into Nicole's pussy."
            mc "Aaahhh!"
            scene 11nicole90a with flash       
            mc "Yeeesss!!!"
            scene 11nicole90a with flash
            "..."
        "Cum outside":
            scene 11nicole89 with dissolve
            "Couldn't hold back, you pulled your dick out of Nicole's pussy and started coming."
            mc "Aaahhh!"
            scene 11nicole89a with flash
            mc "Yeeesss!!!"
            scene 11nicole89b with flash
            "..."
    mc "{i}Jesus Christ, that was fucking awesome.{/i}"
    scene 11nicole91 with dissolve
    "A few seconds later, completely exhausted, you and Nicole fell to the bed."
    n "Haahh... Haah... Haah..."
    n "Bringing you to my place was definitely a good idea."
    stop music fadeout 2.0
    mc "Yes, that's for sure."
    play music "music/6 - Positive Mood.ogg"
    scene 11nicole92 with dissolve
    n "So... I assume you're staying the night?"
    mc "Well, It's really late. So if you okay with that, then yeah."
    n "It's okay with me."
    scene 11nicole93 with dissolve
    n "Besides, if you stay, we could do it again in the morning."
    mc "Hey, didn't you say it was just a one-time offer?"
    n "It's true. But it works until you get out of here, so it's okay."
    mc "Huh. That's how it works."
    n "Yes."
    mc "Well, that sounds good to me."
    n "I think so, too."
    scene 11nicole93a with dissolve
    n "And now..."
    mc "Oh... Did you come up with something else?"
    n "Just wanted to say good night to you."
    n "And kiss you."
    scene 11nicole93b with dissolve
    mc "Mmm..."
    mc "Good night to you, too."
    $ renpy.end_replay()
    if not persistent.day11nicole:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day11nicole = True       
    stop music fadeout 2.0
    scene 11nicole94 with fade
    "Hugging each other You and Nicole fell asleep."
    "There was a new day ahead of you."
    jump day11_rivals_band



label day11_rivals_band:
    scene black with fade
    "Same time across town."
    scene 11rivals01 with fade
    scene black with fade
    $renpy.pause(0.1, hard=True)
    play music "music/8 - Intro Music.ogg"
    scene 11rivals01 with fade
    d "{i}Oohh... Shit, that stupid headache.{/i}"
    d "{i}I wonder how long I slept?{/i}"
    scene 11rivals03 with dissolve
    mi "Ah! Our sleeping beauty is finally awake. Did you have any good dreams?"
    scene 11rivals02 with dissolve
    d "Shut up, you idiot!"
    "..."
    d "Hmm? Are you guys still drinking?"
    scene 11rivals03 with dissolve
    mi "Yeah, just a little bit."
    scene 11rivals02 with dissolve
    d "Dude, stop with the booze for today. I need you to at least hit the strings at tomorrow's gig."
    d "You didn't forget the gig, did you?"
    scene 11rivals03 with dissolve
    mi "Relax, I remember."
    scene 11rivals05 with dissolve
    "{color=#F0FFFF}Girl{/color}" "Don't be so rude to him. He kept me company, while my boyfriend screwed everything up and fell asleep."
    scene 11rivals02 with dissolve
    d "Oh, don't start whining again."
    d "Believe it or not, I don't want to argue with you about it."
    scene 11rivals05a with dissolve
    "{color=#F0FFFF}Girl{/color}" "You're such an ass."
    scene 11rivals02 with dissolve
    d "Yeah, yeah, whatever you say, hon."
    scene 11rivals04 with dissolve
    "..."    
    d "You know, I was thinking that tomorrow after the gig, we should celebrate."
    scene 11rivals03 with dissolve
    mi "Yeah? And where do we find the money for that?"
    mi "In case you forgot, we're broke right now. And we won't get paid for our performance until a few days later."
    scene 11rivals04 with dissolve
    d "Yeah, that's true..."
    scene 11rivals06 with dissolve
    "With a thoughtful view, Derek headed toward his girlfriend."
    scene 11rivals06a with dissolve
    d "I think I've got an idea."
    d "Michael, remember when you said your old man had a safe in here? Just get the money out of there."
    scene 11rivals08 with dissolve
    mi "Not a chance! If I do this, he'll kill me for sure."
    scene 11rivals09 with dissolve
    d "Be smart, dude. It's not like we're asking you to take all his money. Just take a little so we can have enough for one night."
    d "And tomorrow, after the gig, we can have a good time with them."
    scene 11rivals08 with dissolve
    mi "No. I still don't think that's a good idea."
    scene 11rivals09 with dissolve
    d "Come on, man! It's gonna be awesome!"
    d "Besides, when we get paid to show, we'll get all the money back."
    scene 11rivals07 with dissolve
    "{color=#F0FFFF}Girl{/color}" "He's right, Michael."
    "{color=#F0FFFF}Girl{/color}" "I mean, we're all friends here. Tomorrow you're gonna pay for us, and next time Derek and I are gonna pay for you."
    "{color=#F0FFFF}Girl{/color}" "You know you can trust us."
    scene 11rivals10 with dissolve
    mi "Well... I don't know."
    scene 11rivals07 with dissolve
    "{color=#F0FFFF}Girl{/color}" "Come on! I'd really appreciate it! Very, very, much."
    scene 11rivals11 with dissolve
    mi "Uhh... Okay, you talked me into it. Wait here, I'll be right back."
    "{color=#F0FFFF}Girl{/color}" "This is awesome! You're amazing, Michael!"
    d "She's right, dude. You're a real bro!"
    mi "Yes, yes, I know that."
    scene black with fade
    "A few minutes later."
    scene 11rivals12 with dissolve
    mi "{i}Okay, if I remember correctly, this combination has to be the right one.{/i}"  
    "*Click*"
    mi "{i}Yes! It worked!{/i}"
    scene 11rivals13 with dissolve
    mi "{i}Wow, that's a lot of stuff. But thank God the money's here, too.{/i}"
    mi "{i}Okay, if I just take a little, my dad probably won't even notice.{/i}"
    scene 11rivals14 with dissolve
    mi "{i}Yeah, that's it. That's more than enough for us.{/i}"
    scene 11rivals15 with dissolve
    "..."
    scene 11rivals16 with dissolve
    mi "{i}Hmm... What else have we got here?"
    mi "{i}Cigars, a camera, documents and...{/i}"
    stop music fadeout 2.0
    scene 11rivals16a with dissolve
    "..."
    scene 11rivals17 with dissolve
    mi "Huh?"
    mi "{i}Is that a gun?{/i}"
    mi "{i}I didn't even know my dad kept it here.{/i}"
    mi "{i}Although, if you think about it, this is where he belongs.{/i}"
    play music "music/13 - Hope is Still Living.ogg"
    scene 11rivals18 with dissolve
    mi "Haha! Awesome!"
    mi "{i}Shit... Is it just me, or is it very heavy? Or does he have ammo in here too?{/i}"
    mi "{i}Whatever, though.{/i}"
    scene 11rivals19 with vpunch
    mi "Hey, you! Don't move!"
    mi "Yes, you! Guns on the floor, hands on your head!"
    mi "Why are you walking around here without permission?!"
    mi "Asking whose permission? Mine, of course!"
    mi "Haha! This is so cool!"
    "..."
    d "Hey, Michael! Are you coming?! We're sick of waiting for you!"    
    scene 11rivals20 with dissolve
    mi "What?"
    d "I said, how long do we have to wait for you?!"
    mi "Ah, yes... On my way!"
    scene 11rivals21 with dissolve
    mi "{i}The gun's a powerful thing after all.{/i}"
    mi "{i}Should I take it with me?{/i}"
    mi "{i}Yes, a gun definitely won't hurt me!{/i}"
    scene 11rivals22 with dissolve
    "..."
    scene 11rivals23 with dissolve
    mi "I feel like tomorrow's going to be a very interesting day!"
    mi "Eh, I wish it had come sooner."
    scene 11rivals24 with dissolve
    "Michael took a bag of stuff and went back to his friends."
    stop music fadeout 2.0
    scene black with fade
    "There was a new day ahead of them."
  
    
    jump day12_start
