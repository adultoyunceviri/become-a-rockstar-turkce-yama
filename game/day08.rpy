
label day08_start:
    scene black with fade
    "Some time later."
    play music "music/6 - Positive Mood.ogg"
    scene 8beach01 with dissolve
    ls "So you decided to take us to the beach? Is that why we went to change?"
    mc "Yeah, something like that."
    ls "Hmm... And from your confident tone, I thought you'd come up with something big for us."
    mc "Don't worry, it's only the first stop of the evening. And the place we're going is really cool. You will like it there."
    mc "By the way, I've prepared a surprise for you and Jade later. So I advise you to be patient."
    ls "Really... That sounds very intriguing."
    mc "Trust me, you're gonna love it."
    scene 8beach05 with dissolve
    mc "{i}But in order to make this surprise happen I still need to call one person. That conversation may be uncomfortable.{/i}"
    mc "{i}However, that's my problem. The girls don't need to know about it.{/i}"
    scene 8beach02 with dissolve
    jd "By the way... I heard there are parties on this side of the beach on weekends."
    jd "..."
    jd "I take it we're heading to one of them now?"
    scene 8beach03 with dissolve
    mc "You're right."
    mc "For the most part they only happen once or twice a month. And we were lucky tonight is one of those nights."
    mc "Just a year ago, I was a frequent guest at these parties myself."
    mc "If they are like I remember, this will be a great start to our evening."
    ls "Mmmm... really? Then I'll take you at your word!"
    mc "You won't regret it."
    scene black with fade
    "A few minutes later."
    scene 8beach04 with dissolve
    mc "Here we are."
    mc "{i}Yeah... Looks like nothing's changed here. There are still a lot of girls, alcohol, and nice music.{/i}"
    ls "Um... So this is one of your beach parties."
    ls "At first glance it looks quite fun!"
    jd "..."
    jd "Yeah, it is pretty lively here."
    scene 8beach06 with dissolve
    mc "Ahem! May I have your attention... Before we start the party, I'd like to say something."
    "..."
    mc "{i}Okay, they seem to be listening.{/i}"
    mc "It's been a difficult week. A lot of rehearsals, a lot of nerves, and a lot of time spent. But now it's all over."
    mc "We just had our first gig and we handled it perfectly."
    mc "So I hope you're in a good mood, because we're here to have a good time."
    scene 8beach07 with dissolve
    ls "Well said, [mc]. We all deserve a little break."
    mc "That's true. And I'm sorry about all the theatrics, I just thought you needed to hear that."
    ls "Hehe. We heard."
    scene 8beach08 with dissolve
    "After walking down the beach a little, you looked around and stopped near a large fire."
    "Right in front of the campfire sat a guitarist who was playing a very light and calm melody."
    mc "{i}Yeah... It's exactly the way it was in the past.{/i}"
    scene 8beach09 with dissolve
    ls "Mmmm... Actually It's pretty nice here."
    jd "I agree."
    jd "At first I thought this place would be very loud, but... It actually seems kind of cozy."
    mc "I'm glad you like it."
    mc "How about we grab some drinks and sit by the fire?"
    ls "I'm in!"
    stop music fadeout 3.0    
    jd "Me too."
    play music "music/13 - Hope is Still Living.ogg"    
    scene 8beach10 with dissolve
    "You all sat down by the fire and started talking about anything that came to mind."
    "After a whole day on your feet it was all very relaxing."
    mc "{i}I guess I was right to bring Lisa and Jade here.{/i}"
    mc "{i}As for the second half of the evening, I had planned to spend it with the girls on my older brother Marcus's yacht.{/i}"
    mc "{i}Why did I choose a boat?{/i}"
    mc "{i}Because there was absolutely everything that we would need: alcohol, a Jacuzzi, and other opportunities for a pleasant evening.{/i}"
    mc "{i}Except, to make that happen, I need to call Marcus first.{/i}"
    mc "{i}But, I will get to that later.{/i}"
    if lisa_path == True:
        scene 8beach11 with dissolve
        "You hugged Lisa and listened to the guitar playing in the background."
        ls "I wish this moment could last forever."
        mc "Yes, Lisa... I'd like that, too."
        scene black with fade
        "You two spend a while enjoying the atmosphere."
    scene 8beach12 with dissolve
    ls "I don't mean to be a bore and ruin this wonderful moment, but have you thought about what the future holds for us?"
    jd "What steps should we take to make our band successful?"
    ls "No, I understand that we need to keep rehearsing and writing our songs, but what else are we supposed to do?"
    scene 8beach13 with dissolve
    ls "Any ideas, [mc]?"
    mc "In short, we have to become popular."
    mc "We need to record our album, keep playing live, and put our songs on the internet."
    mc "That, and everything else popularity entails."
    scene 8beach14 with dissolve
    jd "Sounds like a very difficult task. And very expensive."
    mc "Well, no one said it would be easy."
    scene 8beach13 with dissolve
    ls "Do you think we can make it?"
    menu:
        "You don't know":
            mc "I wish I knew the answer to that."
            ls "So you don't know?"
            mc "I don't."
            mc "Anything could happen to us."
            mc "We could become legends who will be remembered in a hundred years, or just a small rock band who play gigs around the city."
            scene 8beach12 with dissolve
            ls "You think so?"
            ls "Well, then we should definitely hope for the best."
        "{color=#66FF33}Say something encouraging":
            $ RPjd += 1
            $ RPls += 1
            mc "{i}I don't know the answer, but I'd better tell the girls something reassuring.{/i}"
            mc "It won't be easy, but I think we have a chance to really make it."
            ls "Hmm... If you say that, I believe it."
    scene 8beach15 with dissolve
    ls "By the way... That guitarist who was playing decided to take a break."
    mc "{i}Oh... I can already guess where this is going.{/i}"
    ls "Why don't we ask him to borrow his guitar?"
    scene 8beach13 with dissolve
    mc "I'll go and ask, but only if Jade plays."
    scene 8beach14 with dissolve
    jd "Me?"
    mc "Yep, that's right."
    jd "But why don't you play it yourself?"
    mc "Well, you're the guitarist in our band. And, to be honest, I wouldn't mind listening to you right now."
    scene 8beach17 with dissolve
    jd "You would like to listen me?"
    scene 8beach14 with dissolve
    mc "Of course. You're one of the most talented musicians I know."
    mc "Watching you play the guitar is always lovely."
    scene 8beach16 with dissolve
    ls "He's right, Jade. You're an amazing guitarist."
    ls "And we want you to play us some tunes!"
    ls "Right here and now."
    scene 8beach17a with dissolve
    jd "Thank you guys, that's very nice."
    jd "If [mc] will bring me the guitar, then I will definitely play something for you."
    mc "That's what we wanted to hear!"
    scene 8beach18 with dissolve
    "As you promised, you went to borrow a guitar for Jade."
    mc "Hey, buddy, great job!"
    "{color=#ADFF2F}Guitarist{/color}" "Oh... Thanks, man."
    mc "Listen, while you're taking a break, would you mind if we borrowed your guitar?"
    mc "We'd like to play something on it."
    scene 8beach18a with dissolve
    "{color=#ADFF2F}Guitarist{/color}" "Oh, do you play?"
    mc "Yes, I can."
    mc "But I'm not taking it for me, I'm taking it for the raven-haired beauty behind me. She is a very talented guitarist."
    "{color=#ADFF2F}Guitarist{/color}" "That's great! You guys should come over here, so more people can hear you."
    "{color=#ADFF2F}Guitarist{/color}" "People are getting pretty tired of listening to just me playing. A little variety would be great."
    mc "Hmm... More people? That's not such a bad idea."
    mc "{i}After our gig in the club, this feels like child's play.{/i}"
    scene 8beach19 with dissolve
    "You invited Lisa and Jade here and explained what your new friend had told you."
    jd "Hmm... If everyone else wants to hear it, I don't mind at all."
    jd "I like to play music for people."
    mc "{i}This is another example of what a nice girl Jade is.{/i}"
    mc "{i}She definitely has her secrets, but that doesn't make her any less charming.{/i}"
    scene 8beach20 with dissolve
    "A few seconds later, Jade begins to play a very nice melody that perfectly suits the beach mood."
    mc "{i}Damn, she's as good as ever.{/i}"
    "You notice how most of the conversations around you have become quieter, and people have started to listen to Jade more and more."
    scene 8beach22 with dissolve
    mc "You know, since we're here anyway, you could sing something, too."
    mc "I think they would like to hear your duo."
    ls "Do you really think so?"
    mc "I am sure of it."
    scene 8beach21 with dissolve
    "{color=#ADFF2F}Guitarist{/color}" "Oh! Does your friend sing well?"
    mc "Yeah, she's one of the best."
    "{color=#ADFF2F}Guitarist{/color}" "Then she should join. I'm sure everyone would like that."
    scene 8beach22 with dissolve
    mc "Well, now that I'm not the only one asking, you definitely have to do it."
    scene 8beach23 with dissolve
    ls "Hehe. Well, since you're all so insistent, I guess I just don't have a choice."
    ls "But only if Jade doesn't mind."
    scene 8beach20 with dissolve
    "..."
    scene 8beach20a with dissolve
    jd "I don't. Join in."
    mc "That's great!"
    scene 8beach20 with dissolve
    "At Lisa's request, Jade changed the tune and the duo began their performance."
    scene 8beach26 with dissolve
    "The sounds of Lisa's melodious singing began to draw even more people to us."
    "By looking at the faces of many of the bystanders, you could tell the song Jade and Lisa performed impressed more than a few people."
    "It was their own little victory."
    stop music fadeout 3.0    
    scene black with fade
    "Some time later."
    play music "music/2 - Bad.ogg"    
    "Lisa and Jade finished their song and the crowd began to disperse all over the beach."
    scene 8beach27 with dissolve
    ls "Well, what did you think? How were we?"
    mc "Ha! Are you seriously asking?"
    mc "Did you see the huge crowd that just surrounded you two?"
    mc "They were all gathered just to listen to the two of you."
    ls "Hehe, I know. I saw that."
    ls "But your opinion is more important to me than the crowd's."
    mc "{i}Huh? That's very nice to hear. But what should I tell them?{/i}"
    menu:
        "You liked Jade's performance":
            $ RPjd += 1
            mc "Want my opinion? That was awesome. But I especially liked Jade's performance."
            jd "Oh... Thank you [mc]."

        "You liked Lisa's performance":
            $ RPls += 1
            mc "Want my opinion? That was awesome. But I especially liked your singing."
            ls "Thank you [mc]. But in this case, I think Jade's performance deserves no less praise."
            mc "You're right."

        "{color=#66FF33}They both performed well":
            $ RPjd += 1
            $ RPls += 1
            mc "Want my opinion? That was awesome. You both did a great job."
            ls "Thank you [mc]."
            jd "Yes, thanks."

        "They could have done better":
            mc "You did well, but I think you could have done even better."
            ls "Oh... Maybe you're right."

    scene 8beach29 with dissolve
    "{color=#ADFF2F}Guitarist{/color}" "I don't know who you guys are, but that was awesome!"
    "{color=#ADFF2F}Guitarist{/color}" "We have these parties twice a month, we would be happy to have you back any time."
    scene 8beach28 with dissolve
    jd "Thank you for inviting us."
    jd "And thanks for letting me play your guitar, I liked its sound."
    "{color=#ADFF2F}Guitarist{/color}" "Any time."
    stop music fadeout 3.0
    scene black with fade
    "You were at this beach party for a while, until you decided it was time to move on."
    mc "{i}But in order to move on, I need to call Marcus first.{/i}"
    play music "music/8 - Intro Music.ogg"
    scene 8beach24 with dissolve
    mc "{i}What can I say about Marcus?{/i}"
    mc "{i}He was just as talented in business as my older sister Julia. But his nature was much more complex.{/i}"
    mc "{i}He was very cunning and always looking out for his own benefit.{/i}"
    mc "{i}Not that I blamed him for it. After all, it's a cruel world where you have to fight for your place, but...{/i}"
    mc "{i}But sometimes Marcus just didn't know when to stop.{/i}"
    scene 8beach25 with dissolve
    "You dial his number and wait for him to pick up."
    "{color=#483D8B}Marcus{/color}" "Hello?"
    mc "Marcus, this is [mc]. Hope I didn't wake you."
    "{color=#483D8B}Marcus{/color}" "Hm? [mc]? I wasn't expecting your call. I'm awake."
    mc "Listen... I need one small favor from you."
    "{color=#483D8B}Marcus{/color}" "Ha! We haven't talked in almost a few months, and yet you call at midnight asking me for a favor."
    "{color=#483D8B}Marcus{/color}" "You're not wasting any time, bro."
    mc "..."
    "{color=#483D8B}Marcus{/color}" "Okay, okay... What is it?"
    mc "I wanted to spend some time on your boat."
    "{color=#483D8B}Marcus{/color}" "Spend time on the boat? You're not going anywhere, are you?"
    mc "Of course not. I just want to hang out there with my friend."
    mc "{i}I better not tell him there's three of us.{/i}"
    "{color=#483D8B}Marcus{/color}" "Hmm... probably with a girlfriend... I guess it's okay."
    "{color=#483D8B}Marcus{/color}" "But what would I get out of it?"
    scene 8beach25a with dissolve
    mc "Oh, come on, don't be a jerk, it's a very simple favor."
    "{color=#483D8B}Marcus{/color}" "Hey, didn't anyone ever teach you how to negotiate? What you're doing now isn't working."
    mc "{i}Damn, he's right. I need to be a little nicer. Marcus doesn't owe me anything.{/i}"
    scene 8beach25 with dissolve
    mc "Yeah, sorry, you're right..."
    mc "What do you want in return?"
    "{color=#483D8B}Marcus{/color}" "Well, now we are talking!"
    "{color=#483D8B}Marcus{/color}" "..."
    mc "So what do you want, Marcus?"
    "{color=#483D8B}Marcus{/color}" "I don't know. Nothing comes to mind at the moment."
    "{color=#483D8B}Marcus{/color}" "..."
    "{color=#483D8B}Marcus{/color}" "Let's just say you'll owe me a small favor. Agreed?"
    scene 8beach25a with dissolve
    mc "{i}Hmm... Marcus can be completely unpredictable. In the future, he may ask for something insignificant, or something very valuable.{/i}"
    mc "{i}Regardless, I'll agree to his deal.{/i}"
    scene 8beach25 with dissolve
    mc "Okay, deal."
    "{color=#483D8B}Marcus{/color}" "That's great! Then you can use my boat today."
    "{color=#483D8B}Marcus{/color}" "You do remember where it is on the dock, don't you?"
    mc "Yes, I do. Thanks."
    "{color=#483D8B}Marcus{/color}" "Hey, [mc]..."
    mc "Yes?"
    "{color=#483D8B}Marcus{/color}" "If you break anything in there, you'll be working as my secretary. Got it?"
    mc "Yeah, yeah. I get it."
    "{color=#483D8B}Marcus{/color}" "Haha. Well, great! Good luck to you tonight."
    mc "Yeah, good night to you too."
    scene 8beach24 with dissolve
    mc "{i}Well, it didn't go as badly as I thought.{/i}"
    stop music fadeout 3.0
    jump day08_julia_father


label day08_jane_and_julia:
    scene black with fade
    play music "music/7 - Just Happy.ogg"
    "At the same time at Julia's Office."
    "Knock! Knock!"
    sis "Come in!"
    scene 8juliawork01 with dissolve
    jn "Hey, are you busy right now? Shall we go to lunch?"
    "..."
    jn "Julia? Hello?"
    scene 8juliawork02 with dissolve
    sis "What? Oh yeah! Lunch... Hang on a second."
    sis "In fact, come here, you should see this for yourself."
    scene 8juliawork03 with dissolve
    "Jane approached the table and looked at the monitor."
    jn "Um... What have you got there?"
    "..."
    jn "Ha! Is that what I think it is?"
    sis "Yeah, it's my little brother's band playing Saturday night."
    scene 8juliawork04a with dissolve
    jn "Well, it's a real gig, who would have thought..."
    sis "Yeah, looks like he's on the right track."
    sis "By the way, I was at the gig myself, but I didn't think anyone would put it online."
    jn "Well, it's the twenty-first century, now everything is posted online."
    sis "Yeah."
    "..."
    scene 8juliawork05 with dissolve
    jn "Hmm... And these guys are pretty good!"
    jn "Maybe with time they will turn into a great rock band."
    scene 8juliawork04 with dissolve
    sis "It was even better live. They really brought the heat!"
    jn "Hmm... And their vocalist... She sounds like a pretty good singer."
    sis "Yeah, I don't know where the guys found her, but she's got talent."
    scene 8juliawork05a with dissolve
    jn "[mc] did well, too. It's obvious he gave it his best."
    "The change in Jane's expression did not go unnoticed by Julia."
    scene 8juliawork06 with dissolve
    sis "Okay... I haven't said anything thus far, but now I have to ask."
    sis "What's going on between you two?"
    stop music fadeout 1.0
    scene 8juliawork07 with dissolve
    jn "What?! What are you talking about?"
    sis "I'm serious, Jane."
    jn "There's nothing between us. You're obviously confused right now."
    scene 8juliawork08 with dissolve
    sis "Not likely."
    sis "In my position, I need to be observant, and you know very well that I'm good at my job."
    sis "I've been noticing certain changes in you and my brother for some time now. And now it is especially noticeable."
    sis "So tell me, girl, what's going on between you two?"
    "..."
    scene 8juliawork07a with dissolve
    jn "Eh... I can't hide anything from you... But I suppose you have a right to know."
    sis "Yes, I do."
    jn "Well, to tell you the truth, I don't know what's going on between us. It all started when you went on that business trip..."
    scene black with fade
    "Some time later."
    play music "music/7 - Just Happy.ogg"
    scene 8juliawork11 with dissolve
    sis "Yeah... What a story."
    sis "You didn't waste any time while I was away."
    jn "I'm sorry, I didn't think this was gonna happen..."
    scene 8juliawork09 with dissolve
    sis "You do know that he got off to you a few years ago, right?"
    jn "Course I do. At that time, only a blind man wouldn't have noticed."
    sis "Um... What an interesting life it is. He liked you back then, and now you like him."
    jn "..."
    sis "But why didn't you tell me about it?"
    scene 8juliawork10 with dissolve
    jn "Because I had no idea how you'd react to that."
    jn "Besides, your brother and I are simply... We're just having a good time. That's all. Nothing more."
    sis "Are you sure that's all?"
    jn "Yeah."
    scene 8juliawork11 with dissolve
    sis "You sure?"
    scene 8juliawork09 with dissolve
    jn "I am sure. We're from completely different worlds."
    jn "He's an aspiring musician who spends all his time on music, and I am a workaholic in a large developing company."
    jn "We're too different."
    scene 8juliawork09a with dissolve
    sis "But maybe that's what you need right now. Maybe your type isn't the white collar man you always imagined, but a regular guy with a guitar?"
    jn "But that's stupid, and you know it."
    sis "Who knows? Many successful relationships are built on stupidity."
    scene 8juliawork10 with dissolve
    jn "Is that his older sister talking now, or is it my friend?"
    sis "I'm telling you that as your friend. And somewhere deep down, you know I'm right."
    jn "..."
    scene 8juliawork12 with dissolve
    sis "Anyway, think about it."
    sis "And now let's go get something to eat... I'm starving."
    jn "That's a great idea!"
    jn "Let's go."
    stop music fadeout 3.0
    jump day08_meeting


label day08_julia_night:
    scene 8sis01 with dissolve
    play music "music/Maxim Nick - Falling Down.mp3"
    "*RING*"
    mc "{i}Hmm... I wonder who that could be at this hour?{/i}"
    scene 8sis02 with dissolve
    "You opened the front door and saw Julia on the doorstep."
    mc "Um... Hey, Sis..."
    mc "What are you doing here so late?"
    scene 8sis03 with dissolve
    sis "I was on my way home from work, and I realized there was something you and I need to talk about."
    mc "{i}She wants to talk about something? That's very unusual at this hour.{/i}"
    mc "{i}This doesn't bode well.{/i}"
    mc "Okay, no problem, come on in."
    scene 8sis04 with dissolve
    sis "I hope I didn't take you away from anything important."
    mc "No, I wasn't doing anything."
    mc "Besides, I always have time for you."
    sis "Glad to hear it."
    scene 8sis05 with dissolve
    mc "So, what's so important that you want to talk about?"
    sis "Well... I wanted to talk to you about your relationship with Jane."
    scene 8sis05a with dissolve
    mc "My, uh...  Wait, uh... You're talking about..."
    sis "You don't have to pretend anymore. I know about you two, and about your dirty little secret."
    mc "So you found out about everything..."
    mc "{i}Yeah, well... As I thought, it was just a matter of time.{/i}"
    scene 8sis05 with dissolve
    mc "So how did you find out about all this?"
    sis "It doesn't really matter now."
    mc "Doesn't matter? If it doesn't matter, then I'm not sure what does."
    scene 8sis07 with dissolve
    sis "What matters, my dear brother, is how you're gonna deal with all of this."
    sis "What are your intentions toward my friend?"
    mc "What are my intentions? Um... Are you serious?"
    scene 8sis06c with dissolve
    sis "Oh, yeah, I'm more than serious."
    mc "{i}I guess she's not kidding...{/i}"
    mc "{i}What am I supposed to say to her?{/i}"
    menu:
        "{color=#66FF33}You are serious about Jane":
            $ jane_date = True
            scene 8sis05 with dissolve
            mc "Actually, I really like Jane."
            sis "Huh? So that's how..."
            scene 8sis06b with dissolve
            "For a while, Julia thought about it."
            mc "{i}Damn it... I have no idea what she's about to say.{/i}"
            scene 8sis07a with dissolve
            sis "Well, who'd have thought it would turn out this way?"
            sis "You and Jane... Wow!"
            mc "I'm glad you're having fun, but it's actually very serious to me."
            sis "Um... Yeah, sorry."
            "..."
            scene 8sis06 with dissolve
            sis "Well, I guess this could all be very interesting..."
            mc "..."
            sis "Okay, I'll help you!"
            mc "Um, um... You'll help us? What can you help us with?"
            sis "I'm gonna help make sure you don't screw this up."
            scene 8sis06b with dissolve
            sis "I'm not quite sure I need to get involved, but I can't just leave you two idiots on your own."
            scene 8sis06 with dissolve
            sis "Especially since you're my brother, and she's my best friend."
            sis "So..."
            scene 8sis07a with dissolve
            sis "I've already talked to Jane about it, and I can tell you she has no idea what to do now. "
            mc "{i}Wow. Jane doesn't know what to do... I'm sure that doesn't happen to her very often.{/i}"
            sis "Anyway, if you're really interested in her, you should take the initiative."
            mc "Makes sense."
            scene 8sis07 with dissolve
            sis "As you may have noticed, Jane's always busy with work. You could say that her life has become a routine."
            sis "You're gonna have to try brighten up her dull, gray days with some color, if you know what I mean."
            mc "Um... Do you have anything specific in mind?"
            scene 8sis06 with dissolve
            sis "Nothing special. Just add some good old romance to her life. She misses it a lot."
            scene 8sis07 with dissolve
            sis "Oh yeah, and try to be gentle with her. You shouldn't rush things now."
            mc "Okay, so how am I supposed to do all this?"
            scene 8sis06a with dissolve
            sis "Do I have to make it up for you myself? You have a good imagination, you'll think of something."
            sis "I know there's a romantic hiding in your little narcissistic soul. Pull him out and show her what you can do."
            scene 8sis05 with dissolve
            mc "{i}Hmm... Brighten up her gray days with color?{/i}"
            mc "Well, I think I can do that."
            sis "That's great!"
            sis "And like I said, don't overdo it. I don't want you to have any problems."

        "You don't know yet":
            scene 8sis05 with dissolve
            mc "It's hard to say when you're pushing me like this."
            scene 8sis06c with dissolve
            sis "Well, think hard. I'm in no hurry."
            mc "{i}Hell, looks like she's not gonna give up.{/i}"
            scene 8sis05 with dissolve
            mc "I don't really know that myself. We are attracted to each other, but I wouldn't say it's love."
            mc "It's more like a simple attraction."
            scene 8sis06b with dissolve
            sis "Well then... Maybe you shouldn't continue with this relationship."
            mc "What makes you think that?"
            scene 8sis05 with dissolve
            sis "If you're not sure about her, it says a lot."
            sis "A man in love acts differently. And without that spark... I'm not sure you can do it."
            sis "Besides, if it ends badly and you have a breakup, I don't want you to fight every time you see each other."
            sis "And since she's my best friend and you're my brother, you'll see her often."
            sis "I don't know about you, but I don't need that headache."
            scene 8sis05a with dissolve
            mc "{i}She's as smart as ever.{/i}"
            mc "Maybe you're right."
            scene 8sis06 with dissolve
            mc "Of course I'm right."
            mc "And I'm glad we cleared that up right away."

        "It's nothing serious":
            scene 8sis05 with dissolve
            mc "To tell you the truth, I'm not sure that my relationship with her is really going anywhere."
            scene 8sis06b with dissolve
            sis "Hmm... So that's what you think."
            "..."
            scene 8sis06c with dissolve
            sis "I talked to Jane, and she hasn't made up her mind about you either."
            scene 8sis06b with dissolve
            sis "Well, if that's what you both think, maybe it's for the best."
            sis "I don't think you should continue this relationship. For both of your sakes."
            mc "Yeah, I guess you're right."
            scene 8sis06c with dissolve
            sis "Okay. I'm glad we cleared that up."

    scene 8sis06 with dissolve
    sis "Well, I guess that's all I wanted to talk about."
    sis "I won't keep you any longer."
    mc "You sure about that? Why don't you stay for a cup of tea?"
    scene 8sis06a with dissolve
    sis "Thanks for the offer, but I really have to go."
    mc "Okay, whatever you say."
    if jane_date == True:
        scene 8sis10 with dissolve
        sis "Although, you know... I think I know which restaurant you could take her to. When I get home, I'll send you the name."
        sis "But I'm warning you, it's not going to be cheap."
        sis "And one more thing..."
        sis "Jane's gonna have the day off tomorrow. I suggest you make the most of that opportunity."
        scene 8sis08 with dissolve
        sis "I hope you know what you're doing, [mc]."
        mc "Yeah... I hope so too."
        scene 8sis09 with dissolve
        mc "{i}Yeah, well... If this keeps up, I'll have to sell my kidney soon.{/i}"
        mc "{i}I've used almost all the money I left home with... And that was in just one month.{/i}"
        mc "{i}It wasn't that much, but still...{/i}"
        mc "{i}Okay, I think if I cut my future expenses, I should have enough money for this restaurant.{/i}"
        mc "{i}Probably...{/i}"
    else:
        scene 8sis08 with dissolve
        sis "I hope you know what you're doing, [mc]."
        mc "Yeah... I hope so too."
    if jane_date == True:
        scene black with fade
        "Right after you got the name of the restaurant, you decided to call Jane and ask her out."
        mc "{i}I hope she agrees.{/i}"
        scene 8sms10 with dissolve
        jn "Hello? [mc]?"
        mc "Hey, Jane. Sorry to call you so late."
        jn "It's okay. I wasn't asleep yet."
        jn "Did you want something?"
        mc "Yeah, I was wondering if you had any plans for tomorrow."
        jn "For tomorrow?"
        jn "Tomorrow I have the day off, so my plan was to spend all day in bed."
        jn "Why do you ask?"
        mc "{i}Well, here comes the moment of truth.{/i}"
        mc "I wanted to invite you to a restaurant to have dinner and discuss what has been going on between us."
        jn "Hmm... The truth is, I wanted to talk to you about it as well."
        "For a while, there was silence on the phone."
        jn "Okay! Why not? Tomorrow is great!"
        mc "{i}Okay, great!{/i}"
        jn "Send me the address of this restaurant and we'll meet there tomorrow."
        mc "That's perfect. See you tomorrow, Jane."
        jn "See you tomorrow, [mc]."
    stop music fadeout 3.0
    if rosa_path == True:
        jump day08_rosa_day02
    if jane_date == True and rosa_path == False:
        jump day08_jane_date
    else:
        jump day08_home_sms



label day08_boat:
    scene black with fade
    "On the docks by the beach."
    play music "music/Maxim Nick - It's okay (final).mp3"
    if lisa_path == True and RPjd >= 2:
        scene 8pier01b with dissolve
        "You walked with Lisa and Jade looking for the right spot on the dock."
        mc "Don't worry. As far as I can remember, we're almost there."
        scene 8pier01bb with dissolve
        "The girls have been holding on to you tighter."
        ls "It's okay, [mc]. We are in no hurry."
        jd "Yeah... It's very nice to walk around here."

    if lisa_path == False:
        scene 8pier01c with dissolve
        "You walked with Lisa and Jade looking for the right spot on the dock."
        ls "What kind of boat are we looking for here?"
        mc "Don't worry. As soon as I see her, I'll tell you right away."
        scene 8pier01cc with dissolve
        mc "{i}Hmm... And since when did they get along so well?{/i}"
    if lisa_path == True and RPjd < 2:
        scene 8pier01a with dissolve
        "You walked with Lisa and Jade looking for the right spot on the dock."
        mc "Don't worry. As far as I can remember, we're almost there."
        scene 8pier01aa with dissolve
        "Lisa squeezed your hand tighter."
        ls "It's okay, [mc]. We are in no hurry."

    scene 8pier02 with dissolve
    "Having walked around the dock for a while, you finally found the boat you were looking for."
    mc "{i}Yeah, that's her. Exactly how I remember her.{/i}"
    mc "Well, ladies, let me introduce you to our next vacation spot. Our ship to Athens!"
    mc "{i}I hope I was able to convey the importance of this moment.{/i}"
    scene 8pier03 with dissolve
    ls "Wow! Is this really your brother's boat?"
    mc "It is. And tonight it is all ours."
    ls "Awesome!"
    ls "When you first mentioned that we were looking for a boat, I imagined something much smaller."
    ls "But it's not even a boat, it's a yacht!"
    mc "{i}She says that, but she hasn't even seen the inside yet.{/i}"
    mc "Do you have something to say, Jade? You're very quiet."
    scene 8pier03a with dissolve
    jd "It's impressive."
    jd "I've never been in anything like this before."
    ls "It's gonna be the first time tonight, girl. Hehe."
    mc "Okay, let's not stay out here too long. Let's get on board."
    scene black with fade
    "You showed the girls where to get on board."
    scene 8pier04 with dissolve
    ls "I was wondering, what are we gonna do here?"
    ls "We're not going anywhere, are we?"
    mc "{i}Why does everyone think I want to go somewhere on this boat?{/i}"
    scene 8pier05 with dissolve
    mc "Don't worry, im sure we'll find something to do right here."
    mc "Besides, our first stop will be the minibar."
    scene 8pier04 with dissolve
    jd "Um... Looks like you've already thought this through."
    mc "Of course! Follow me."
    scene 8pier06 with dissolve
    "You climbed the stairs and entered the main cabin."
    ls "Wow! I didn't expect so much space in here."
    jd "I have to agree with Lisa. This yacht looks much bigger on the inside."
    scene 8pier07 with dissolve
    "You went inside and stopped by the minibar."
    mc "So, do you have any drink preferences?"
    mc "There's vodka, whiskey, champagne and a lot more. Hell, there's even non-alcoholic beer here! What do you think?"
    ls "We'll let our bartender decide for us."
    mc "Wise choice, ma'am."
    scene 8pier08 with dissolve
    mc "I guess I'll just pick something that's not too strong."
    mc "Better go with the champagne."
    scene 8pier09 with dissolve
    mc "It's insanely expensive, but who cares?"
    ls "Hehe. Excellent!"
    jd "Maybe we shouldn't take anything expensive. We didn't pay for it."
    scene 8pier09a with dissolve
    mc "Don't worry, Jade. Tonight we can do anything."
    mc "Now let's move on."
    scene black with fade
    "A few moments later."
    scene 8pier10 with dissolve
    ls "Awesome! There's a Jacuzzi here!"
    mc "{i}She's so adorable.{/i}"
    jd "Oh, wow."
    scene 8pier11 with dissolve
    "..."
    scene 8pier10 with dissolve
    mc "Hehe. I told you, today we deserve to relax."
    scene 8pier12 with dissolve
    "Before you knew it, Lisa and Jade were by the hot tub."
    ls "This night just turned from a great night into a legendary night!"
    jd "Hey, why don't we try it right away?"
    ls "Oh! I see you're interested too!"
    jd "..."
    scene 8pier13 with dissolve
    "While the girls were talking, your attention was drawn to more exciting things."
    mc "{i}They both look great!{/i}"
    scene 8pier14 with dissolve
    mc "{i}And now I'm gonna see them both in bikinis.{/i}"
    scene 8pier15 with dissolve
    ls "So, [mc], can we use this thing?"
    mc "Of course. That's why we're here."
    ls "Hooray!"
    scene 8pier16 with dissolve
    "Lisa and Jade started quickly stripping off their clothes."
    mc "{i}What a wonderful sight.{/i}"
    scene 8pier17 with dissolve
    mc "{i}I can't believe it's just the three of us on this boat.{/i}"
    mc "{i}But something tells me the fourth member of our band is having an even better time.{/i}"
    scene 8pier18 with dissolve
    "A minute later, the girls had taken off all their clothes and were left in bikinis."
    scene 8pier19 with dissolve
    ls "Why aren't you undressing?"
    ls "We're not going in without our host."
    mc "Mm-hmm... That's nice to hear."
    jd "Take your clothes off."
    mc "{i}Hmm... Coming from Jade, that sounded more like an order...{/i}"
    scene 8pier21 with dissolve
    "As soon as you took your shirt off, you noticed that Lisa and Jade were whispering quietly about something."
    mc "{i}That's interesting.{/i}"
    scene 8pier20 with dissolve
    mc "Is something wrong?"
    ls "We saw the way you looked at us when we undressed."
    ls "Now it's our turn to look at you and talk about you. Hehe."
    mc "Huh? You won't scare me so easily."
    stop music fadeout 3.0    
    jd "Oh, trust us, we know that..."
    play music "music/6 - Positive Mood.ogg"    
    scene 8pier22 with dissolve
    "As soon as you undressed, the girls got into the hot tub."
    mc "I see you're not wasting any time."
    ls "Well, you invited us here. It wouldn't be polite to keep you waiting."
    scene 8pier23 with dissolve
    ls "Aaaahhhhh... It feels so good in here!"
    ls "I feel like I'm about to melt."
    jd "[mc], you should have warned us you had such a nice surprise for us."
    mc "Maybe. But you have to agree that it was a good surprise."
    jd "..."
    scene 8pier24 with dissolve
    ls "Come on, Jade! The surprise is great!"
    jd "Yes... I guess you're both right."
    scene 8pier25 with dissolve
    ls "Of course we're right!"
    ls "In fact, if it weren't for [mc], I don't know what we'd be doing tonight."
    jd "Yes... I guess..."
    ls "He's the only reason we're having such a good time tonight."
    ls "That's what we should drink to!"
    scene 8pier26 with dissolve
    mc "Hmm... Two beautiful girls want to drink to me?"
    mc "What a lovely day today."
    ls "Hehe!"
    scene 8pier27 with dissolve
    "You opened the champagne..."
    scene 8pier28 with dissolve
    "Poured it into glasses and gave them to Lisa and Jade."
    scene 8pier29 with dissolve
    jd "Thank you."
    ls "Yes, thank you, [mc]."
    "You took your glass and sat down next to the girls."
    scene 8pier30 with dissolve
    mc "Okay, so..."
    ls "To the best bass player in the world! To [mc]!"
    jd "To [mc]!"
    mc "Huh. To [mc]!"
    play sound "music/bottle.wav"
    scene 8pier31 with dissolve
    "*Clinking of glasses*"
    scene 8pier32 with dissolve
    "..."
    scene 8pier33 with dissolve
    ls "Mm-hmm... This champagne is really nice."
    ls "How much did you say it cost?"
    scene 8pier34 with dissolve
    jd "I don't think he mentioned the price."
    mc "Believe me, it's better if you don't know."
    scene 8pier35 with dissolve
    ls "Huh? Well, if you say so, I won't insist."
    ls "Let's talk about something, shall we?"
    scene black with fade
    "You've been drinking champagne for a while, joking and talking about everything."
    scene 8pier37 with dissolve
    ls "Um... Guys, I don't want to spoil the mood, but I think we're out of booze."
    mc "{i}Not surprising, the way we have been drinking.{/i}"
    scene 8pier38 with dissolve
    mc "That's okay. I think there was another bottle."
    mc "Wait a minute, I'll get it."
    jd "Um... Are you sure we can have it?"
    mc "Don't worry, my brother won't even notice it. For him, it's insignificant."
    if lisa_path == True:
        scene 8pier36 with dissolve
        ls "I'll keep you company. I want to take a little walk."
        mc "{i}Hmm... Is it just me or is she a little drunk?{/i}"
        scene 8pier38 with dissolve
        mc "Sure, if you want to. Let's go."
        mc "Jade, will you wait for us here?"
        jd "No problem. I'll just have a smoke."
        scene 8pier39a with dissolve
        "You and Lisa got out of the Jacuzzi and then went to the inner cabin of the yacht."
        stop music fadeout 3.0
        jump day08_boat_lisa
    else:
        scene 8pier36 with dissolve
        ls "We'll wait here for you."
        mc "Of course, no problem."
        scene 8pier39 with dissolve
        "You got out of the Jacuzzi and went inside the yacht."
        stop music fadeout 3.0
        jump day08_boat_jade

label day08_boat_lisa:
    if _in_replay:
        $ setReplay()
    scene 8pierlisa01 with dissolve
    ls "You know... I wanted to come with you for a reason."
    mc "Mm-hmm. And what was your reason?"
    ls "Hehe. Wait till we go a little further and I'll show you..."
    scene 8pierlisa02 with dissolve
    play music "music/1 - Atmosphere.ogg"    
    "You went into the cabin."
    mc "I think I know what you wanted to show me."
    ls "You know?"
    mc "Oh, yeah! I do."
    scene 8pierlisa03 with dissolve
    "You hugged Lisa from behind and pressed her firmly against you."
    ls "Aaahh..."
    scene 8pierlisa04 with dissolve
    mc "I think there's some very dirty thoughts in that pretty head."
    ls "What if there are? You wouldn't mind that, would you?"
    mc "{i}She's trying to tease me.{/i}"
    scene 8pierlisa05 with dissolve
    "You turned her around and looked into her eyes."
    mc "I would be crazy if I did."
    ls "How nice to hear that."
    scene 8pierlisa06 with dissolve
    "The next moment, your lips were locked together in a passionate kiss."
    ls "Mmmm..."
    scene 8pierlisa07 with dissolve
    "Your hands began to slide slowly down Lisa's back, sinking closer and closer to her tight ass."
    ls "Mmmm... [mc]..."
    mc "{i}Damn! This is so hot!{/i}"
    scene 8pierlisa08 with dissolve
    "You picked Lisa up..."
    ls "Ahh!"
    scene 8pierlisa09 with dissolve
    "...and set her on a table nearby."
    ls "Where'd you get all that energy? Hehe."
    scene 8pierlisa10 with dissolve
    "Another kiss."
    mc "{i}Oh my God, her tongue is so nice.{/i}"
    scene 8pierlisa11 with dissolve
    "While you were kissing Lisa, your hands started massaging her soft breasts."
    mc "{i}Her nipples are already hard.{/i}"
    scene 8pierlisa12 with dissolve
    "Suddenly Lisa pulled away."
    "*Heavy breathing*"
    ls "We need to stop, Jade's waiting outside."
    mc "But didn't you want to show me something?"
    scene 8pierlisa12a with dissolve
    ls "Hmm... You're right, I can't just let you go."
    scene 8pierlisa13 with dissolve
    "Lisa jumped off the table and hugged you tightly."
    ls "I think you're gonna love what I'm about to do..."
    mc "{i}Oohhhh... I think I'm already guessing.{/i}"
    scene 8pierlisa14 with dissolve
    "Lisa sank gracefully down to her knees, and her hands rested on your thighs."
    scene 8pierlisa15 with dissolve
    ls "Well, well, well! Let's see what we have here..."
    "She pulled your underwear down with one sudden move."
    scene 8pierlisa16 with dissolve
    ls "Ahhhh... There he is."
    scene 8pierlisa17 with dissolve
    ls "I forgot how big it was."
    mc "I don't mind reminding you as often as I can. Hehe."
    scene 8pierlisa18 with dissolve
    "Lisa's warm hand is gently holding your dick."
    ls "First, let's cheer him up a little bit."
    show anim42
    mc "Aaahhhhh... yeah... That's good..."
    ls "Mm-hmm... Too bad we don't have much time."
    ls "I'd really like to feel that big, fat dick inside me right now."
    mc "{i}Oohhhh... Her dirty talk is turning me on so much.{/i}"
    ls "Say, [mc], would you like to fuck me now?"
    mc "Ahhhhh... yes..."
    ls "Mm-hmm... great..."
    scene 8pierlisa19 with dissolve
    ls "I think it's time for us to speed up a little bit."
    scene 8pierlisa20 with dissolve
    "Lisa's soft tongue touched your dick."
    mc "{i}That feels good, but I want more.{/i}"
    scene 8pierlisa21 with dissolve
    "Keeping an eye on your facial expression, Lisa kept licking your dick."
    mc "Oohhhhhh... Stop teasing me, put it in your mouth."
    ls "Mm-hmm... okay."
    scene 8pierlisa22 with dissolve
    "Lisa stuck the head of your dick in her mouth and started tickling the underside gently with her hot tongue."
    mc "{i}I don't know where she learned that, but it's really fucking nice.{/i}"
    show anim55
    "Lisa finally took your dick in her mouth and started sucking it."
    mc "{i}Oohh... And this is even better.{/i}"
    ls "Mmmm... mmmmph.... mmmph..."
    mc "{i}Much better!{/i}"
    scene 8pierlisa25 with dissolve
    mc "Aaahhh... yeah... That's it, baby."
    mc "{i}Her tongue feels so good on my dick.{/i}"
    scene 8pierlisa26 with vpunch
    ls "Mhhh... Hnnnngggg..... Mhhh..."
    mc "Yeah! Yeah! That's it!"
    scene 8pierlisa24 with dissolve
    mc "Don't get distracted, you're doing great."
    ls "Mmmmhhh... Mhhhgg...."
    scene 8pierlisa27 with dissolve
    mc "{i}Too bad we don't have much time.{/i}"
    scene 8pierlisa29 with dissolve
    mc "Come on, baby, you're doing great!"
    ls "Mmmm... mmmmph.... mmmps..."
    scene 8pierlisa28 with dissolve
    mc "{i}Oohhhh... If she keeps sucking so hard, I'm gonna cum soon...{/i}"
    ls "Mm-hmm... Come on, [mc]. We have to finish..."
    scene 8pierlisa30 with dissolve
    "Lisa took your dick out of her mouth and started jerking it off."
    mc "Lisa, I'm gonna..."
    ls "Come on! Come on! Cover me with your hot cum!"
    scene 8pierlisa30a with flash
    mc "Aaaahhhh! Yeah!"
    scene 8pierlisa30a with flash
    mc "YEEESS!"
    scene 8pierlisa31 with dissolve
    ls "Oh... You really covered my face."
    mc "Isn't that what you wanted?"
    ls "Hehe. Very much so."
    ls "But now I have to get myself cleaned up."
    mc "{i}She's right. It's a miracle that Jade hasn't caught us yet.{/i}"
    stop music fadeout 2.0
    $ renpy.end_replay()
    if not persistent.day08lisa:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day08lisa = True

    scene black with fade
    "Some time later."
    play music "music/10 - Street's.ogg"
    scene 8pierlisa32 with dissolve
    "You cleaned yourselves up, took a bottle of champagne, and went back to Jade like nothing ever happened."
    scene 8pierlisa33 with dissolve
    mc "{i}There she is.{/i}"
    mc "{i}I think we made it in time. She's still smoking.{/i}"
    scene 8pierlisa34 with dissolve
    jd "Hm?"
    jd "You guys weren't in too much of a hurry."
    scene 8pierlisa35 with dissolve
    mc "Um... Sorry, Lisa and I had a little chat and lost track of time."
    ls "Yeah, it was an interesting conversation."
    mc "{i}Hell, she can barely hold back a smile.{/i}"
    scene 8pierlisa36 with dissolve
    jd "Too bad I couldn't get involved."
    ls "Uh... Couldn't get involved in what?!"
    jd "In the conversation, of course."
    ls "Oh... Well, yeah. Right."
    jd "And what did you think I meant?"
    ls "Um... nothing! Nothing at all! Haha."
    mc "{i}...{/i}"
    scene 8pierlisa37 with dissolve
    jd "Do you mind if we go inside? It's getting a little chilly out here."
    mc "Oh, yeah, of course. Let's go inside, I think we can find something to do."
    jd "Thank you."
    stop music fadeout 3.0
    jump day08_never_have_i_ever


label day08_boat_jade:
    scene black with fade
    "Some time later."
    scene 8pierjade01 with dissolve
    "Returning to the girls with the champagne, you were shocked by what you saw."
    mc "{i}Huh?{/i}"
    scene 8pierjade02 with dissolve
    "Lisa and Jade were kissing like they'd forgotten anyone else in the world existed."
    ls "Mmmm..."
    scene 8pierjade03 with dissolve
    mc "{i}Uh... Am I dreaming or is this really happening?{/i}"
    scene 8pierjade04 with dissolve
    ls "Aaahhh..."
    jd "Mmmm..."
    scene 8pierjade04a with dissolve
    "..."
    scene 8pierjade03a with dissolve
    mc "{i}Hell, who'd have thought?{/i}"
    mc "{i}Jade seemed so quiet to me, but as soon as I turned my back, she put the moves on our lovely Lisa.{/i}"

    scene 8pierjade08 with dissolve
    "*Heavy breathing*"
    ls "We need to stop, he'll be back soon."
    menu:
        "Let them know about your presence":
            $ goodpoint += 1
            scene 8pierjade11 with dissolve
            mc "Actually, I'm already here."
            scene 8pierjade09 with dissolve
            "The girls' heads turned abruptly in your direction."

        "Don't say anything":
            $ badpoint += 1
            mc "{i}I think I can watch them for a while. After all, you don't get to see this every day.{/i}"
            scene 8pierjade08 with dissolve
            jd "Just a little more."
            ls "Mmm... you like to take risks..."
            scene 8pierjade06 with dissolve
            "Jade pulled Lisa in and kissed her again."
            scene 8pierjade05 with dissolve
            mc "{i}Damn, I'm so jealous of them right now.{/i}"
            scene 8pierjade08a with dissolve
            "The girls' heads turned abruptly in your direction."
            mc "{i}I guess I was spotted after all. Not that I was hiding...{/i}"
            scene 8pierjade09 with dissolve
            "..."
    play music "music/10 - Street's.ogg"
    scene 8pierjade09a with dissolve
    "Lisa's cheeks began quickly turn pink."
    scene 8pierjade10 with dissolve
    ls "Aw... It's not what you think... We're just..."
    ls "We're just..."
    jd "Relax, Lisa, I think he's already figured it out."
    mc "{i}Maybe I should calm Lisa down a little before she has a heart attack.{/i}"
    scene 8pierjade11 with dissolve
    mc "Don't worry Lisa, Jade is right."
    mc "We're all adults here, and there's nothing wrong with what you guys were doing."
    mc "Honestly, I liked seeing it. What guy wouldn't?"
    scene 8pierjade12 with dissolve
    ls "Oh... So, everything's okay, right?"
    mc "Of course."
    ls "Ugh... I was so scared that I almost went completely sober."
    scene 8pierjade11 with dissolve
    mc "You know, I think we've sat out here long enough, so why don't we go inside?"
    jd "I'm in."
    ls "Yeah, me too."
    stop music fadeout 3.0
    jump day08_never_have_i_ever

label day08_never_have_i_ever:
    scene 8boat01 with dissolve
    play music "music/6 - Positive Mood.ogg"
    "A minute later, you walked into the cabin and sat down on the couch."
    mc "So we still have one bottle of expensive champagne left..."
    mc "Does anyone have any idea what we're gonna do with it?"
    scene 8boat02 with dissolve
    ls "How about we play a game or something?"
    ls "And before you ask, no, I`m not talking about the Spin the Bottle."
    scene 8boat03 with dissolve
    jd "Looks like you already have an idea."
    jd "Care to share with the rest of us?"
    scene 8boat02 with dissolve
    ls "The idea is pretty simple... How about the game \"Never Have I Ever\"?"
    mc "Ha! Interesting choice."
    mc "But do you really want to play that game?"
    ls "Yeah, why not? We played it all the time in high school."
    mc "Wow, we're looking at a professional player."
    scene 8boat04 with dissolve
    ls "Hehe! You bet! I'm sure it'll be fun."
    ls "So, are we gonna play, or do you have any other ideas?"
    mc "I don't mind."
    mc "Jade, what about you?"
    scene 8boat03 with dissolve
    jd "If you're gonna play, I'm gonna play with you."
    scene 8boat04 with dissolve
    ls "Okay, great! Then we're all for it!"
    mc "{i}Looks like Lisa's really excited.{/i}"
    mc "{i}Although there's a good chance it's just the alcohol.{/i}"
    scene 8boat02 with dissolve
    ls "Just in case, I'll remind you of the rules."
    ls "The first player says a simple statement about something they have never done before starting with \"Never have I ever\". Anyone who, at some point in their life, has done the thing the first person said, must drink."
    ls "I hope everybody understands?"
    "We had no questions."
    scene 8boat12a with dissolve
    ls "And since I'm the one who suggested this game, why don't I start first?"
    mc "Mm-hmm... It seems someone has decided to play seriously."
    ls "Hehe. Get ready, soon all your secrets will be revealed."
    scene 8boat13 with dissolve
    ls "And I think I'll start with something easy."
    ls "My first question will be..."
    ls "Okay, so, uh... What am I gonna come up with... What am I gonna..."
    scene 8boat14 with dissolve
    ls "Aha! I got it!"
    ls "Never have I ever been on a plane before."
    mc "{i}Hmm... Looks like she really decided to start with a harmless question.{/i}"

    menu:
        "{color=#66FF33}Drink":
            $ drunk_point += 1
            scene 8boat08 with dissolve
            "You drank first..."
            scene 8boat07 with dissolve
            "...and right after you, Jade."
            scene 8boat10 with dissolve
            jd "If you're interested, it was a school trip to Europe. It was great."
            scene 8boat09a with dissolve
            ls "And what about you, [mc]? Where did you fly to?"
            scene 8boat14a with dissolve
            mc "My parents flew a lot because of their work, and they took me with them. That's why I've been to a lot of places."
            mc "Well, I hope I'll get to visit a lot more places in the future."
            scene 8boat09a with dissolve
            ls "Huh. Lucky you!"

        "Don't":
            scene 8boat07 with dissolve
            "This time it was just Jade who drank."
            scene 8boat10 with dissolve
            jd "If you're interested, it was a school trip to Europe. It was great."
            scene 8boat09a with dissolve
            ls "That's interesting... And you [mc]? You didn't go anywhere either?"
            mc "Yeah, pretty much."
            ls "Thank God I'm not the only one."
            scene 8boat14a with dissolve
            mc "Don't worry, once our band gets popular, you'll get tired of flying in planes."
            scene 8boat09a with dissolve
            ls "Huh. I hope so!"

    scene 8boat12a with dissolve
    ls "Well, that was a good start to the game!"
    scene 8boat09 with dissolve
    ls "Okay, now it's Jade's turn."
    ls "I hope you thought of something already."
    jd "Yeah, I got it."
    scene 8boat10 with dissolve
    jd "Never have I ever made money by performing on the street."
    menu:
        "{color=#66FF33}Drink":
            $ drunk_point += 1
            scene 8boat08 with dissolve
            "..."
            scene 8boat09a with dissolve
            mc "{i}Looks like I drank alone this time.{/i}"
            ls "Wow... You have made money performing on the street? Will you tell us the story?"
            scene 8boat14a with dissolve
            mc "Actually, the story is pretty simple."
            mc "Jacob and I were playing music outside the mall once."
            mc "We weren't even playing for the money, it was just for fun."
            mc "But, it turns out the two of us made about 20 bucks that day."
            mc "It was a very interesting experience."
            scene 8boat09a with dissolve
            ls "Huh... I'd like to see that."
            jd "Yeah, me, too."
        "Don't":
            "..."
            scene 8boat09 with dissolve
            ls "Alas, it looks like you didn't get anyone."
            jd "Hmm..."
            jd "Well, next time I'll try something more interesting..."
            ls "Hehe! I can't wait."

    scene 8boat05 with dissolve
    ls "Well, it looks like it's your turn [mc]."
    jd "Hmm... I think it will be interesting."
    mc "{i}So, what should I ask them?{/i}"
    menu:
        "{color=#66FF33}Never have I ever read an erotic novel":
            $ drunk_point += 2
            scene 8boat14a with dissolve
            mc "Never have I ever read an erotic novel."
            scene 8boat06 with dissolve
            "Lisa drank first..."
            scene 8boat07 with dissolve
            "...and then Jade followed suit."
            scene 8boat09a with dissolve
            mc "Wow... So you both like to read dirty books? How interesting."
            scene 8boat12 with dissolve
            ls "Hey, there are actually a lot of good books in that genre!"
            mc "Yeah, I'm sure there are."
            ls "Oh, come on!"
            scene 8boat09 with dissolve
            ls "Especially since Jade reads that kind of literature, too. Isn't that right?"
            scene 8boat10 with dissolve
            jd "Well, to be honest, I tried to read them out of curiosity."
            jd "Nothing special, I guess."
            scene 8boat12b with dissolve
            ls "Oh... Well, okay... If you want to know, I'm not ashamed of it at all!"
            mc "{i}Yeah, your pink cheeks say otherwise.{/i}"

        "Never have I ever sung in the shower.":
            $ drunk_point += 2
            scene 8boat14a with dissolve
            mc "Never have I ever sung in the shower."
            scene 8boat06 with dissolve
            "Lisa drank first..."
            scene 8boat07 with dissolve
            "...and then Jade followed her."
            scene 8boat12 with dissolve
            ls "Yeah, well, I sing a lot in the shower. And it's actually really fun."
            ls "It's kind of weird that you don't do it yourself, [mc]..."
            scene 8boat09 with dissolve
            ls "What about you, Jade?"
            scene 8boat10 with dissolve
            jd "I don't sing in the shower often, but I love to sing different melodies..."
            jd "That counts, doesn't it?"
            mc "{i}I'm not sure it's the same thing, but since she already drank, so be it.{/i}"

        "Never have I ever had a crush on a teacher":
            scene 8boat14a with dissolve
            mc "Never have I ever had a crush on a teacher."
            "..."
            scene 8boat09a with dissolve
            ls "Nope. All our teachers were too old and weird, so you were wrong!"
            jd "I didn't have anything like that either."
            scene 8boat05 with dissolve
            mc "{i}Oh... I'm a little sorry I made such a mistake with that question.{/i}"

    scene 8boat12a with dissolve
    ls "Okay, it's my turn again."
    ls "And perhaps after the first round it's time to ask some spicier questions."
    mc "Heh, show us your wild fantasies. You can ask anything you want."
    ls "Hehe. It's good that you're so confident."
    scene 8boat14 with dissolve
    ls "Never have I ever seen a woman perform a striptease before."
    menu:
        "{color=#66FF33}Drink":
            $ drunk_point += 1
            scene 8boat08 with dissolve
            "First you drank..."
            scene 8boat07 with dissolve
            "... then Jade followed you."
            scene 8boat11 with dissolve
            "This time, the dark-haired guitarist was in no hurry to share her story."
            mc "{i}Perhaps I should start?{/i}"
            scene 8boat09a with dissolve
            mc "Well, it's not really a big deal. It's just that my friends and I used to go to strip clubs sometimes."
            mc "If you're wondering, it was only two or three times."
            ls "Well, I was expecting something like that."
            ls "But it's still interesting..."
            scene 8boat09 with dissolve
            ls "What about you, Jade?"
            scene 8boat10a with dissolve
            jd "Basically the same story."
            jd "Nothing special."

        "Don't":
            scene 8boat07 with dissolve
            "This time it was just Jade who drank."
            scene 8boat11 with dissolve
            jd "..."
            mc "{i}Jade seems to be in no hurry to share this story.{/i}"
            scene 8boat09a with dissolve
            ls "It's weird... I was sure that [mc] had definitely seen a woman perform a striptease."
            scene 8boat12a with dissolve
            ls "Looks like somebody's dodging the question."
            mc "I am sure you meant a striptease at a strip club, right? Then no, I haven't."
            scene 8boat12 with dissolve
            ls "Um... Okay."
            scene 8boat09 with dissolve
            ls "What about you, Jade?"
            scene 8boat03 with dissolve
            jd "I went to one once with my friends."
            jd "Nothing special."

    scene 8boat09 with dissolve
    ls "Okay, now it's your turn again, Jade."
    scene 8boat10 with dissolve
    jd "Okay..."
    jd "Never have I ever swam naked at the beach."
    if lisa_path == True:
        mc "{i}Wow... What an interesting question.{/i}"
        mc "{i}After that night with Lisa following the Naked Park concert, I have to drink.{/i}"
        scene 8boat08 with dissolve
        "First you drank..."
        scene 8boat06 with dissolve
        "... then Lisa followed you."
        scene 8boat03 with dissolve
        jd "Wow... You both just drank... How interesting."
        scene 8boat12b with dissolve
        ls "It's not what you think... um... well..."
        scene 8boat14a with dissolve
        mc "Relax, Lisa, I think we can let Jade draw her own conclusions."
        mc "Besides, it's not that important, because now it's my turn to ask a question again."
    else:
        "..."
        scene 8boat09 with dissolve
        ls "Looks like you missed on that one."
        jd "Hmm... Too bad."
        scene 8boat14a with dissolve
        mc "Now it's my turn again."

    scene 8boat05 with dissolve
    mc "{i}Hmm... What should I ask them?{/i}"
    menu:
        "Never have I ever kissed my best friend":
            $ drunk_point += 1
            mc "Never have I ever kissed my best friend."
            scene 8boat07 with dissolve
            "This time it was just Jade who drank."
            scene 8boat09 with dissolve
            ls "Huh! Not bad!"
            mc "{i}Yeah... If it keeps going like this, we'll learn a lot about her.{/i}"
            scene 8boat11 with dissolve
            jd "Well, that was a long time ago... in high school."
            jd "And if you don't mind, I don't want to talk about it."
            scene 8boat09 with dissolve
            ls "Okay, we won't force you."
            "..."
            jd "Thank you."

        "Never have I ever danced in an elevator":
            $ drunk_point += 1
            mc "Never have I ever danced in an elevator."
            scene 8boat06 with dissolve
            "Only Lisa drank this time."
            mc "{i}I don't doubt it for some reason.{/i}"
            scene 8boat12 with dissolve
            ls "Oh, come on! I won't even go into detail about it."
            ls "Everyone has to have done it at least once! There's no way!"
            mc "Huh. As you can see, Jade and I haven't done it."
            ls "Pfft. Well, okay... You're just nerds."

        "Never have I ever sent someone a sexy selfie":
            mc "Never have I ever sent someone a sexy selfie."
            if day07_photo01 == True:
                $ drunk_point += 2
                scene 8boat06 with dissolve
                "Lisa drank first..."
                scene 8boat07 with dissolve
                "...and then Jade drank after her."
                scene 8boat09a with dissolve
                mc "Wow... Aren't you guys full of surprises!"
                scene 8boat12b with dissolve
                ls "Hey! Like you didn't ask me to send them to you."
                mc "Huh... That's true."
                mc "And I can tell you that they were amazing."
                scene 8boat12a with dissolve
                ls "It's okay. Next time you'll be the one to send them to me. And that's not up for debate!"
                mc "Well, I can't argue with you right now. Haha!"
                ls "That's exactly what I'm saying."
                scene 8boat10 with dissolve
                jd "How interesting."
                jd "You two are so close already..."
                scene 8boat09 with dissolve
                ls "What about you? Who did you send your selfies to?"
                scene 8boat10a with dissolve
                jd "Um... In this case, I would prefer not to answer that question."
                jd "I hope you don't mind."
                mc "{i}I'm not surprised about that for some reason.{/i}"

            else:
                $ drunk_point += 1
                scene 8boat07 with dissolve
                "This time it was just Jade who drank."
                scene 8boat09 with dissolve
                ls "Hehe! Not bad!"
                mc "{i}Yeah... If it keeps going like this, we'll learn a lot about her.{/i}"
                scene 8boat10a with dissolve
                jd "Um... In this case, I would prefer not to answer that question."
                jd "I hope you don't mind."
                mc "{i}I'm not surprised about that for some reason.{/i}"

        "{color=#66FF33}Never have I ever kissed somone of the same gender":
            mc "{i}It's gonna be a very simple.{/i}"
            mc "Never have I ever kissed someone of the same gender."
            scene 8boat06 with dissolve
            "Lisa drank first..."
            scene 8boat07 with dissolve
            "...and then Jade drank after her."
            scene 8boat09a with dissolve
            ls "That wasn't fair, [mc]."
            mc "..."
            scene 8boat09 with dissolve
            jd "You know, Lisa, I don't think he get what he saw out of his head."
            ls "That's right!"
            scene 8boat12a with dissolve
            ls "So what do you say? Did you like it?"
            ls "You want to see us kiss again?"
            menu:
                "{color=#66FF33}Yes":
                    mc "Why not?"
                    mc "It's always nice to see two pretty girls kissing."
                    ls "Mm-hmm. Absolutely."
                    scene 8boat09 with dissolve
                    ls "Jade?"
                    jd "If that's what you want, then..."
                    scene 8boat12a with dissolve
                    stop music fadeout 3.0
                    ls "Let's show him how to do it."
                    scene 8boat15 with dissolve
                    "Jade gently wrapped her hands around Lisa's face and moved closer to her."
                    "For a while, they looked into each other's eyes in silence..."
                    scene 8boat16 with dissolve
                    "...and then their soft lips pressed together."
                    show anim54
                    mc "{i}Wow... I'm watching something beautiful right now.{/i}"
                    "..."
                    mc "{i}And I can safely say it's very hot.{/i}"
                    scene 8boat16b with dissolve
                    "Soon the girls finished kissing and stayed silent for a while."
                    "At this point, you could have sworn they both liked it, too."
                    scene 8boat17 with dissolve
                    play music "music/8 - Intro Music.ogg"
                    ls "Well, what do you say, [mc]? I hope you enjoyed it?"
                    jd "I can guess by his open mouth that he did."
                    ls "Hehe! That's for sure!"
                    stop music fadeout 3.0
                    jump day08_boat_night
                "No":
                    mc "Thanks for the offer, but you don't have to do that."
                    scene 8boat12 with dissolve
                    ls "Wow... What amazing restraint you have."
                    ls "But If you don't want to see it..."
                    stop music fadeout 3.0
                    jump day08_boat_night

    if lisa_path == True:
        scene 8boat12a with dissolve
        ls "And now it's my turn again!"
        scene 8boat13 with dissolve
        ls "What am I gonna come up with... What am I gonna ... Aha!"
        scene 8boat14 with dissolve
        ls "Never have I ever kissed a girl."
        scene 8boat08 with dissolve
        "First you drank..."
        scene 8boat07 with dissolve
        "... and then Jade drank after you."
        scene 8boat09 with dissolve
        ls "Whoa! I knew [mc] would drink, but I didn't think Jade would drink too..."
        scene 8boat11 with dissolve
        jd "..."
        scene 8boat12 with dissolve
        ls "Damn, that's why I love this game! There's always someone surprising you."
        mc "{i}Yeah, well... Not that I didn't expect anything like that, but it was very interesting.{/i}"
        scene 8boat09 with dissolve
        ls "So, Jade, who was the lucky lady who fell under your spell?"
        mc "Hey, if you don't want to, you don't have to answer."
        scene 8boat03 with dissolve
        jd "It's okay."
        jd "It was my high school friend. At the time, we were often fooling around together."
        mc "{i}Um... Did it sound like it wasn't just kissing in there?{/i}"
        mc "{i}Although, uh... What do I even know about Jade?{/i}"
        mc "{i}This isn't the first time I've asked myself this question, but now I'm particularly interested.{/i}"
        mc "{i}Does she like guys or girls? Or both?{/i}"
        mc "{i}Maybe I should ask her that.{/i}"
        mc "{i}I think now that we're so drunk, this is the best time to find out the answer to that question.{/i}"
        menu:
            "Ask about Jade's sexual preferences" if drunk_point >= 4:
                scene 8boat14a with dissolve
                mc "{i}Hell, why not?{/i}"
                mc "Jade... Can I ask you one very personal question?"
                scene 8boat10 with dissolve
                jd "Ask."
                scene 8boat14a with dissolve
                mc "The question of your sexual preferences."
                jd "..."
                mc "Do you like guys or girls?"
                ls "[mc]."
                scene 8boat10a with dissolve
                jd "Well, there's actually no secret to that."
                jd "I'm bisexual."
                mc "Huh."
                "..."
                scene 8boat09 with dissolve
                ls "So you like both men and women? Is that right?"
                jd "In general, yes."
                ls "Umm..."
                jd "What?"
                scene 8boat12b with dissolve
                ls "No, nothing..."
                scene 8boat03 with dissolve
                jd "It's okay, you can ask."
                scene 8boat12b with dissolve
                ls "Um... purely hypothetically... Do you think another girl could like me?"
                scene 8boat03 with dissolve
                jd "What do you mean?"
                scene 8boat09 with dissolve
                ls "Well, I know guys like me, but I've always wondered... er... Am I the type of girl that other girls like?"
                mc "{i}Oh... Looks like somebody's had too much to drink...{/i}"
                jd "I can't speak for anyone else, but you're very attractive... I would definitely like you."
                scene 8boat12b with dissolve
                ls "Whoa! That's awesome..."
                ls "But it's also super weird."
                scene 8boat03 with dissolve
                jd "Well, you asked."
                scene 8boat15a with dissolve:
                    ypos -1.90
                    ease 12 ypos 0.0
                "Maybe it's because of the alcohol, or maybe it's the sight of the two beauties in bikinis in front of you, but this whole conversation has stirred your imagination."
                "And now there's a very enticing picture forming."
                "...a second later, however, Lisa's voice startled you."
                scene 8boat09a with vpunch
                ls "[mc]!"
                mc "Ah?! What? I'm sorry. I was just thinking..."
                scene 8boat09 with dissolve
                ls "Shit, Jade, I think you're right. He's already starting to imagine all sorts of naughty things."
                mc "{i}Did Jade say something? Wait... naughty things?{/i}"
                mc "Hey! Actually, I didn't think of anything like that."
                scene 8boat12 with dissolve
                ls "Oh, really?"
                mc "{i}Oh, what good is it to lie about that now?{/i}"
                mc "Okay, okay! Maybe just a little bit? You know I have a very lively imagination."
                scene 8boat12a with dissolve
                ls "Mm-hmm... very lively imagination?"
                ls "And what did you have time to imagine?"
                ls "Was it really me and Jade kissing? Or something even naughtier?"
                mc "{i}What's gotten into her?{/i}"
                ls "You know, I was wondering... Would you like to see how we would kiss?"
                mc "{i}I don't know if she's making fun of me, or if she's serious?{/i}"
                ls "A hot kiss between your girlfriend and her friend..."
                ls "So... Do you want to see it?"
                mc "{i}Damn it... What am I supposed to say to that?{/i}"
                menu:
                    "{color=#66FF33}Yes":
                        $ jade_kiss = True
                        scene 8boat14a with dissolve
                        mc "{i}Oh, I hope it's not some kind of trap.{/i}"
                        mc "I'm sure it would be very hot."
                        ls "Mm-hmm. Absolutely."
                        scene 8boat09 with dissolve
                        ls "Jade?"
                        jd "Um... If that's what you want, and [mc] doesn't mind, then..."
                        ls "Oh, I'm sure he doesn't mind at all."
                        ls "Besides, we're just fooling around."
                        scene 8boat12a with dissolve
                        ls "Let's show him that reality can be as good as his imagination."
                        stop music fadeout 3.0
                        scene 8boat15 with dissolve
                        "Jade gently wrapped her hands around Lisa's face and moved closer to her."
                        "For a while, they looked into each other's eyes in silence..."
                        scene 8boat16 with dissolve
                        "..and then their soft lips pressed together."
                        show anim54
                        mc "{i}Wow... I'm watching something beautiful right now.{/i}"
                        "..."
                        mc "{i}And I can safely say it's very hot.{/i}"
                        scene 8boat16b with dissolve
                        "Soon the girls finished kissing and kept silent for a while."
                        "At this point, you could have sworn they both liked it, too."
                        scene 8boat17 with dissolve
                        play music "music/8 - Intro Music.ogg"
                        ls "Well, what do you say, [mc]? I hope you enjoyed it?"
                        jd "I can guess by his open mouth that he did."
                        ls "Hehe! That's for sure!"

                    "No":
                        scene 8boat14a with dissolve
                        mc "Well, no. You're all mine."
                        scene 8boat12 with dissolve
                        ls "Hehe! That's for sure!"

            "Don't ask":
                mc "{i}Maybe I should mind my own business. It's better if we just keep playing.{/i}"
    else:
        "..."
    stop music fadeout 3.0
    jump day08_boat_night


label day08_boat_night:
    scene black with fade
    "Some time later."
    scene 8boat12 with dissolve
    play music "music/6 - Positive Mood.ogg"
    ls "Okay, I think we've had enough to drink tonight. Can we just sit here and talk about something?"
    scene 8boat03 with dissolve
    jd "I agree. It is better to stop now."
    scene 8boat13 with dissolve
    ls "Oh, by the way, can we take a selfie as a memory?"
    mc "That's a great idea, Lisa."
    scene 8boat20 with dissolve
    "You took your phone out and got ready to take a picture."
    mc "Smile at the camera!"
    play sound "music/photo.wav"
    scene 8boat20a with flash
    mc "Done!"
    "..."
    ls "Hey, [mc], did you accidentally press the filter there?"
    mc "Oh... Shit, I think so."
    ls "Yeah, you can see that."
    jd "You know, I like it even better."
    jd "Especially that stylish pink hair."
    ls "Huh, I like that hair too, by the way!"
    mc "But I don't like it."
    ls "Don't delete that picture, [mc]! Keep it!"
    jd "Yeah, [mc], don't delete it."
    mc "Okay, okay!"
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    stop sound
    if jade_kiss == True and RPjd >=2 and lisa_path == True:
        scene 8boat19 with dissolve
        "Sitting comfortably on the couch, you continued to talk..."
        "Your night was coming to an end."
        "After a while, you were all starting to fall asleep."
        jump day08_lisa_sex
    if lisa_path == False:
        scene 8boat19a with dissolve
        "Sitting comfortably on the couch, you continued to talk..."
        "Your night was coming to an end."
        "After a while, you were all starting to fall asleep."
        jump day08_night_alone
    else:
        scene 8boat19b with dissolve
        "Sitting comfortably on the couch, you continued to talk..."
        "Your night was coming to an end."
        "After a while, you were all starting to fall asleep."
        jump day08_lisa_sex


label day08_night_alone:
    scene black with fade
    "..."
    scene 8lisanight01 with fade
    $renpy.pause(0.1, hard=True)
    scene 8lisanight01 with fade
    "Suddenly you woke up in the middle of the night."
    mc "{i}Uh... It seems we all fell asleep.{/i}"
    mc "{i}I need to check on the girls.{/i}"
    "You looked around."
    scene 8lisanight06a with dissolve
    mc "{i}Oh... Here they are. They fell asleep hugging.{/i}"
    mc "{i}Yeah, well... It's pretty cute.{/i}"
    mc "{i}But I should stop staring at them. I'd better go back to sleep.{/i}"
    scene 8lisanight01 with fade
    "You lay down in the same spot you were sleeping."
    scene 8lisanight01 with fade
    $renpy.pause(0.1, hard=True)
    scene black with fade
    "Your eyelids closed quickly, and you plunged back into the kingdom of Morpheus."
    jump day08_jacob

label day08_lisa_sex:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "..."
    ls "[mc]."
    ls "[mc], wake up..."
    scene 8lisanight01a with fade
    $renpy.pause(0.1, hard=True)
    scene 8lisanight01a with fade
    play music "music/Maxim Nick - Smooth Light.ogg"
    mc "{i}Mm-hmm... Lisa?{/i}"
    mc "What's... Did we all fall asleep?"
    scene 8lisanight02 with dissolve
    "Lisa looked excitedly off to the side..."
    mc "What's going on?"
    scene 8lisanight03 with dissolve
    ls "Shh... Keep your voice down, Jade is still asleep."
    ls "We don't want to wake her up, do we?"
    scene 8lisanight06 with dissolve
    "You looked around and saw Jade sleeping."
    mc "{i}Looks like Lisa's right, our guitarist is sleeping soundly.{/i}"
    scene 8lisanight03 with dissolve
    ls "Come on, let's go."
    scene 8lisanight04 with dissolve
    "Lisa took your hand and led you somewhere."
    mc "{i}Doesn't look like she's still drunk.{/i}"
    mc "{i}Okay. This is getting interesting.{/i}"
    scene 8lisanight05 with dissolve
    ls "I hope you're awake already."
    mc "Yes...  Looks like I'm up now."
    ls "Okay, great."
    scene 8lisanight07 with dissolve
    "A few seconds later you were out in the open air."
    mc "{i}Hmm... It's hard to say what's on her mind right now, but she seems to be in a great mood.{/i}"
    scene 8lisanight07a with dissolve
    ls "Yes... This place is perfect."
    mc "{i}Oh... If this is going where I think it is, it's gonna be a great end to this day.{/i}"
    scene 8lisanight08 with dissolve
    "Lisa turned around and motioned for you to come closer."
    ls "You know, it was a great night."
    mc "Yeah, I think so, too."
    ls "But I know how to make it even better."
    scene 8lisanight09 with dissolve
    "Lisa put her hands behind her back..."
    scene 8lisanight09a with dissolve
    "...and untied the top of her swimsuit."
    mc "{i}Damn... I love it.{/i}"
    scene 8lisanight10 with dissolve:
        ypos -1.90
        ease 12 ypos 0.0
    "Before you knew it, you had a half-naked Lisa in front of you with a very playful expression on her face."
    mc "{i}Wow.{/i}"
    scene 8lisanight11 with dissolve
    "Trying not to show impatience, you started to approach her slowly."
    ls "Come on, [mc], I thought you'd be more enthusiastic."
    mc "Haha, now I'm gonna show you so much enthusiasm that you won't forget it for a long time."
    scene 8lisanight12 with dissolve
    "You immediately hugged Lisa and started kissing her neck."
    ls "Aaahhh..."
    scene 8lisanight13 with dissolve
    "Your hands slipped smoothly up her waist..."
    scene 8lisanight14 with dissolve
    "...and stopped at her delightfully soft breasts."
    mc "{i}I can feel her warmth, and smell her sweet scent. Oh my God, it feels so good.{/i}"
    scene 8lisanight15 with dissolve
    "While your hands gently caressed Lisa's breasts, your lips met hers."
    mc "{i}Damn it... She has such a nice tongue.{/i}"
    scene 8lisanight16 with dissolve
    ls "[mc]... I want it."
    ls "I want to do it right here under the stars."
    mc "Mm-hmm. My lady's wish is my command."
    ls "Hehe, you're such a gentleman."
    scene 8lisanight17 with dissolve
    mc "{i}And now it's time to get rid of that last piece of clothing.{/i}"
    scene 8lisanight17a with dissolve
    "You pulled the tie on Lisa's bottoms and they fell to the floor."
    scene 8lisanight17b with dissolve
    "..."
    scene 8lisanight17c with dissolve
    mc "{i}Yeah... How long have I waited for this moment.{/i}"
    mc "{i}I can finally see that beautiful ass again.{/i}"
    scene 8lisanight18 with dissolve
    "Right in front of you stood Lisa, completely naked."
    ls "[mc], you're looking at me so closely... It makes me uncomfortable."
    mc "You shouldn't be embarrassed. You look so incredibly sexy."
    scene 8lisanight19 with dissolve
    ls "Mm-hmm... Such compliments are always welcome."
    mc "Believe me, you deserve every one of them."
    mc "And besides the compliments, I think you'll be okay with this, too..."
    scene 8lisanight20 with dissolve
    "You pushed Lisa gently forward, and she put her hands on the Jacuzzi."
    ls "Hey, what are you doing?"
    mc "This evening in the cabin, you gave me something..."
    mc "Now it's my turn to pay you back."
    scene 8lisanight21 with dissolve
    "Lisa sat on the edge of the hot tub and smiled widely."
    ls "Mm-hmm... I like the way you think."
    ls "Please continue."
    scene 8lisanight22 with dissolve
    "You knelt down and gently placed your hands on her thighs."
    scene 8lisanight23 with dissolve
    mc "{i}There's her cute pink pussy.{/i}"
    ls "Uh... I hope you know what you're doing."
    mc "You'll see for yourself now."
    scene 8lisanight24 with dissolve
    "When your fingers started to caress Lisa's pussy, she barely held her first groan."
    ls "Aaahh!"
    ls "Mm-hmm.... yes, [mc]..."
    scene 8lisanight25 with dissolve
    mc "{i}She's soaked down here. She seems to be enjoying herself.{/i}"
    "You noticed that her breathing has gotten heavier, and she slowly started to move her hips in time with your movements."
    ls "Aaahhh... Aaaahhhh... Aaaahhh..."
    scene 8lisanight26 with dissolve
    ls "Ughh... we... We need to try to be quiet... Jade is sleeping just inside."
    mc "Then why don't you keep your moaning down?"
    ls "Mmmm..."
    scene 8lisanight27 with dissolve
    mc "{i}Let's take it up a notch.{/i}"
    ls "Aaaahhh... Aaaahhh... Aaaahhh..."
    scene 8lisanight28 with dissolve
    mc "{i}Yeah... She's obviously enjoying this.{/i}"
    ls "Aahhh... just like that!! Yes..."
    scene 8lisanight29 with dissolve
    "Suddenly you felt Lisa's legs tighten around you, and she unconsciously pressed you into her."
    scene 8lisanight30 with dissolve
    "..."
    show anim49
    ls "[mc]... This is a... It's amazing!"
    ls "Aaaahhh... Aaahhh.... Aaaahhhh...."
    mc "Mmmm...."
    ls "Please continue... Do not stop."
    ls "Oohhhhhh... a little more... A little more and I'll cum!"
    scene 8lisanight31 with flash
    ls "Yeesss! Yeeeess!!!"
    "Lisa's muscles were tense, and her whole body began to shake."
    scene 8lisanight31 with flash
    "..."
    scene 8lisanight32 with dissolve
    ls "Haa... Haa.... Haa..."
    ls "I don't know where you learned that, but it was amazing."
    ls "Uhh..."
    ls "Give me a minute to breathe, and we can continue."
    mc "Take your time."
    scene black with fade
    "A minute later."
    scene 8lisanight33 with dissolve
    ls "I still can't believe this is happening."
    ls "But I'm really excited about it."
    mc "Yeah, me too."
    scene 8lisanight34 with dissolve
    "Lisa came closer and hugged you tightly."
    "You felt her hot body pressing against you."
    scene 8lisanight35 with dissolve
    "She moved behind you and pressed her soft breasts into your back."
    mc "{i}Damn it... I've got a raging hard-on right now.{/i}"
    scene 8lisanight36 with dissolve
    ls "I think I need to check on your big guy."
    ls "I hope he's still got some energy after the last time?"
    scene 8lisanight37 with dissolve
    mc "Why don't you check it out for yourself?"
    mc "I warn you, he's very tough."
    scene 8lisanight38 with dissolve
    ls "Let's see..."
    "Lisa's hand slowly slipped over your stomach and ended up in your underwear."
    scene 8lisanight39 with dissolve
    ls "Hehe. Yeah, now I see that your dick is definitely ready."
    ls "Mmm... It's so hot and hard."
    scene 8lisanight40 with dissolve
    "Lisa pulled your underwear off and, still holding her body tightly against you, started slowly jerking you off."
    show anim41
    mc "{i}Even though her hands are so small, it feels insanely good.{/i}"
    mc "Oh, yeah... It's so good..."
    ls "Mm-hmm... I'm glad you're having fun."
    mc "Yes... Yes, I am."
    scene 8lisanight41 with dissolve
    "Suddenly Lisa stopped."
    mc "Hey... Why did you stop?"
    ls "We don't want it to end this early, do we?"
    scene 8lisanight42 with dissolve
    ls "Besides, I'm gonna make both of us feel a lot better now."
    mc "Yeah... I think so too."
    scene 8lisanight43 with vpunch
    "Lisa turned her back to you and slapped her ass with both hands."
    ls "Come here, baby... I want to feel your big dick inside me."
    mc "{i}Trust me, honey, you're not the only one who wants that.{/i}"
    scene 8lisanight44 with dissolve
    mc "{i}Damn... How long have I wanted to do this?{/i}"
    mc "{i}And now she's practically begging me to fuck her.{/i}"
    scene 8lisanight45 with dissolve
    ls "Mmmm..."
    mc "{i}Well, it's time.{/i}"
    scene 8lisanight46 with dissolve
    "You got closer and grabbed Lisa's ass."
    ls "Ahh!"
    ls "Be gentle with me."
    mc "I'll try."
    scene 8lisanight47 with dissolve
    mc "{i}Ohhhh... Her pussy is so wet.{/i}"
    mc "{i}How exciting.{/i}"
    scene 8lisanight47a with dissolve
    ls "Mmmm..."
    ls "Don't tease me, [mc]. Just put your dick in me."
    scene 8lisanight48 with dissolve
    mc "How about you say please?"
    scene 8lisanight48a with vpunch
    "Without waiting for you, Lisa pushed her hips back and slid your dick inside her."
    ls "Aaaahhhhhh... You're welcome!"
    scene 8lisanight49 with dissolve
    mc "{i}Ohhh... My little rebel.{/i}"
    show anim43
    ls "That feels so good."
    mc "Yes, baby, take it!"
    mc "{i}Fuck... She's so tight. I could really get used to this.{/i}"
    ls "Ooohhh... Your dick is so big!"
    ls "It's filling up my little pussy so good!"
    scene 8lisanight50 with dissolve
    "You took Lisa by the hand and pulled her even harder onto your dick."
    ls "Aaahhh... aaahhhh... aaahhhh..."
    scene 8lisanight51 with dissolve
    ls "Oh my God, that feels so good!"
    mc "{i}Yes... I agree with her on that. It's really fucking good.{/i}"
    scene 8lisanight52 with dissolve
    "You could practically feel the heat coming off of the beautiful girl in front of you. It was extremely arousing."
    ls "Aaahhh... aaaaahhhhhhh.... aaaaahhhhhh..."
    scene 8lisanight53 with dissolve
    ls "Aaahhh... [mc], what are you doing?"
    mc "It's just... Just enjoy it."
    mc "{i}She has such delightfully soft breasts and such a tight ass.{/i}"
    scene 8lisanight54 with dissolve
    ls "Mm-hmm... please... [mc]... not so fast... Otherwise I won't be able to hold back my moans."
    scene 8lisanight55 with dissolve
    "..."
    show anim40
    "Strange as it may seem, Lisa's words had the opposite effect. You grabbed Lisa's tits and started fucking her even harder."
    ls "Aaaahhhh!!! Aaaahhhhh!!! Aaaahhhhh!!!"
    ls "[mc]! [mc]! [mc]!"
    mc "Ooohhhh... Yesss... Take that! Take that!"
    scene 8lisanight56 with dissolve
    ls "I... I want to see your face."
    mc "{i}Ohhhh... Well, if that's what she wants, I don't mind.{/i}"
    scene 8lisanight57 with dissolve
    "You turned Lisa around and hugged her tight."
    mc "{i}Damn it... She's so beautiful.{/i}"
    scene 8lisanight60 with dissolve
    ls "..."
    mc "{i}She's just looking at me.{/i}"
    scene 8lisanight58 with dissolve
    mc "{i}I don't think I'm gonna make it much longer.{/i}"
    mc "We better continue."
    ls "Ah... yes... right..."
    scene 8lisanight59 with dissolve
    "The next thing you know, you picked Lisa up and started bouncing her up and down."
    show anim47
    mc "{i}She's so light.{/i}"
    ls "Aaaahhh... Aaaahhh..."
    ls "Fuck, your dick is so fucking deep..."
    mc "Oh yeah... I know..."
    show anim48
    ls "Aaahhhhhh... This is so good!"
    mc "Mmmm..."
    ls "Haa... Haa... your cock is... so nice!"
    scene 8lisanight61 with dissolve
    ls "[mc]... I'm going to cum soon..."
    mc "{i}That will be her second time.{/i}"
    mc "{i}She's enjoying this as much as I am.{/i}"
    stop sound fadeout 2.0
    scene 8lisanight62 with dissolve
    ls "Aaahhh... Aaahhhh!!!"
    ls "I'm almost..."
    if jade_kiss == True or _in_replay:
        scene 8lisanight68 with dissolve
        jd "{i}Mmmm...{/i}"
        jd "{i}Those two are so hot... I can't stop.{/i}"
    scene 8lisanight63 with flash
    ls "Aaaahhh... Yeeess!!!"
    scene 8lisanight63 with flash
    "..."
    scene 8lisanight64 with dissolve
    ls "Wow... I don't think my legs are gonna hold me up after such a strong orgasm."
    ls "What about you?"
    ls "Are you gonna come?"
    scene 8lisanight65 with dissolve
    "Without saying a word, you set Lisa on her knees in front of you and started stroking your dick."
    if (jade_kiss == True and RPjd >=2) or _in_replay:
        scene 8lisanight69 with dissolve
        jd "{i}Aaahhh... Aaahhhh... Aaaahhh.....{/i}"
        jd "{i}How nice.{/i}"
        scene 8lisanight70 with dissolve
        "..."
        show anim51
        ls "Ohh... I see you're almost there."
        ls "Come on, baby. Give me everything you've got."
        jd "{i}Come on, [mc]... Cum right on Lisa.{/i}"
        jd "{i}Mm-hmm... Come on! Cum all over that pretty face!{/i}"
    scene 8lisanight66 with flash
    mc "Oooohhh! YEESSS!!!"
    scene 8lisanight66 with flash
    mc "Oh, God, that feels so good..."
    scene 8lisanight67 with flash
    ls "Oh!"
    ls "Hell, that's the second time you've cum on my face today."
    mc "I'm sorry, but it's very exciting."
    ls "Ha ha ha! It's okay. Actually, I kind of like it."
    if (jade_kiss == True and RPjd >= 2) or _in_replay:
        scene 8lisanight71 with dissolve
        jd "{i}Oh... I think they're done.{/i}"
        jd "{i}I need to get out of here before they see me.{/i}"
        scene 8lisanight72 with dissolve
        "..."
    stop music fadeout 1.0
    scene black with fade
    "A few minutes later."
    play music "music/Maxim Nick - It's okay (final).mp3"
    scene 8lisanight73 with dissolve
    ls "It was an amazing evening, [mc]."
    ls "I can't think of any way it could have been better."
    mc "Yeah, me either."
    mc "Shall we go to bed now?"
    ls "Yeah, I guess so. I don't think I can do any more today."
    scene 8lisanight74 with dissolve
    ls "And you're a monster, [mc]! I can barely walk."
    mc "Hehe. I warned you that you'd remember this night."
    stop music fadeout 3.0

    $ renpy.end_replay()
    if not persistent.day08lisa2:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day08lisa2 = True

    jump day08_jacob


label day08_rosa_day01:
    scene black with fade
    play music "music/3 - Dream With U.ogg"
    "As you and Rosa agreed on over the phone, a few hours later you were standing at the entrance of her studio."
    mc "{i}Uh... I don't know why, but I'm a little nervous.{/i}"
    mc "{i}Come on, [mc], focus! It's just a small part-time modelling job. There is no reason to worry.{/i}"
    mc "{i}Well, apart from one redheaded lady who obviously has plans for you.{/i}"
    "..."
    "You rang the doorbell and started waiting."
    scene 8rosaart01 with dissolve:
        ypos -1.90
        ease 12 ypos 0.0
    "The door opened and you saw Rosa in front."
    mc "{i}Damn it... She looks amazing.{/i}"
    scene 8rosaart02 with dissolve
    r "Oh... It's you, [mc]! Thank you so much for coming."
    mc "Well, I promised you. And I'm used to keeping my promises."
    r "Mm-hmm... Handsome and responsible. What good qualities."
    mc "Um... Yes, thank you."
    r "By the way, you're just in time. All my students are already here."
    mc "{i}Students? Did she say students?{/i}"
    scene 8rosaart03 with dissolve
    r "Now, please, come inside, don't be shy."
    mc "Yes, of course."
    scene 8rosaart04 with dissolve
    r "I'm happy to welcome you to my little art studio."
    r "I've been painting here for years. I hope you like this place."
    "The first thing you noticed was the abundance of paintings and other works of art."
    mc "Wow. There is so much stuff here."
    r "Yeah, a lot of my old paintings are here. Newer works are usually at exhibitions or with my clients. "
    scene 8rosaart05 with dissolve
    mc "{i}It's not that bad here. To some extent it can even be called a creative disorder.{/i}"
    mc "{i}Rosa must be spending a lot of time here.{/i}"
    scene 8rosaart06 with dissolve
    mc "{i}And this chatty couple looks like Rosa's so-called students.{/i}"
    mc "{i}Hmm... They look quite normal.{/i}"
    scene 8rosaart07 with dissolve
    mc "{i}Just like this girl who is reading some fashion magazine.{/i}"
    mc "{i}I don't know why, but when I heard about her students, I imagined things a little differently.{/i}"
    mc "{i}But maybe it's for the best.{/i}"
    scene 8rosaart09 with dissolve
    r "So, [mc], as you can see, there aren't that many people here."
    mc "Well, quantity doesn't always mean quality, does it?"
    r "That's a good way to put it. It definitely fits our situation."
    r "Well, let me introduce you to everyone."
    scene 8rosaart08 with dissolve
    r "Ahem! Guys, I'm gonna ask you all to stop what you're doing and come over here."
    r "I'd like to introduce you to our model for today."
    r "That's [mc] and he's a very good friend of mine. Try to make a good impression on him."
    scene 8rosaart10 with dissolve
    "The students nodded silently, agreeing with the words of Rosa, and began to look at you with interest."
    mc "{i}Damn it... I feel like I'm in a zoo.{/i}"
    mc "{i}Not just as a visitor, but as an exhibit.{/i}"
    mc "{i}Maybe I should say hello to them to get rid of this awkward silence.{/i}"
    mc "Hey, everybody. I hope everyone is having a good day?"
    "Rosa's students gave me a sluggish welcome."
    scene 8rosaart09 with dissolve
    r "Don't mind them, they're a little shy."
    mc "Okay, then."
    mc "And what do I have to do?"
    r "First, I want to ask you to take off your shirt. Today the students will try to paint your naked torso."
    mc "Naked torso?"
    r "Yeah, I hope that won't be a problem."
    mc "{i}Actually, I was expecting something like that, so should I be surprised?{/i}"
    mc "No, it's okay. I don't mind."
    scene 8rosaart12 with dissolve
    "Rosa pointed you to a place where you could undress."
    r "I'm sorry, but we don't have locker rooms or wardrobes here, so you can put your stuff right on the stool."
    mc "Okay, that's fine with me."
    scene 8rosaart11 with dissolve
    "On the way, you stopped for a while near a lot of paintings on the wall."
    mc "{i}Even I, a man who doesn't know anything about modern painting, understand that Rosa definitely has talent.{/i}"
    mc "{i}Except, as well as at Selina's house, most of her paintings show very explicit things.{/i}"
    mc "{i}Maybe that is just her style.{/i}"
    scene 8rosaart13 with dissolve
    "You decided not to waste any more time, and started changing."
    mc "Did I get it right that only your students are going to paint today?"
    scene 8rosaart14 with dissolve
    r "That's right. I've promised to bring them a new male model for a long time now, and you were such a good opportunity."
    r "I hope you don't mind."
    mc "{i}So Rosa isn't gonna paint me? That's a pity.{/i}"
    mc "Sure, it's okay."
    scene 8rosaart15 with dissolve
    mc "I was just curious to see you at work."
    r "Oh, really?"
    r "I don't really mind you being my model, but I'm not used to working with my students."
    r "However, if you have a free evening tomorrow, you can come here at the same time. I think you and I will find something to do."
    mc "{i}What a tempting offer. I don't have to be a genius to catch a certain implication. {/i}"
    scene 8rosaart16 with dissolve
    "Rosa took you to the center of the studio, where the model was supposed to be."
    mc "Can I ask you one more question?"
    r "Sure, ask."
    mc "Why do you like to paint alone?"
    scene 8rosaart17 with dissolve
    "Rosa came closer to you."
    r "Well, it's pretty simple."
    r "I've been used to working alone for a long time. It's usually easier for me to focus."
    scene 8rosaart18 with dissolve
    "Suddenly you felt Rosa's soft hands on your shoulders."
    mc "{i}Whoa... Doesn't look like she's shy about anything.{/i}"
    mc "{i}Not to mention the fact that we are surrounded by her students.{/i}"
    scene 8rosaart19 with dissolve
    mc "{i}I'd even say she's being cocky.{/i}"
    r "So, what do you think? Since we're on the subject, I hope you'll keep me company tomorrow and be my personal model?"
    scene 8rosaart18 with dissolve
    mc "{i}Hell, I feel like I'm in the middle of a hunter's scope right now.{/i}"
    mc "{i}I guess I'll just have to pull myself together and answer her.{/i}"
    scene 8rosaart20 with dissolve
    mc "I don't see any reason not to."
    r "Good answer. I knew I was right about you."
    r "But maybe we should get started... My students are waiting for us."
    scene 8rosaart21 with dissolve
    "You looked up and saw that Rosa's students were ready a long time ago."
    mc "{i}Is it me, or have they been watching us with interest all this time?{/i}"
    mc "{i}Oh, man, somehow all this just feels... strange.{/i}"
    scene 8rosaart22 with dissolve
    r "Okay, guys, let's not keep our guest waiting. You can get to work."
    r "If anyone has any questions or other difficulties, do not hesitate to ask me."
    mc "{i}Damn it... I didn't ask Rosa how long it would take.{/i}"
    scene 8rosaart24 with dissolve
    r "It's gonna take some time [mc]. Try not to move too much."
    mc "{i}It's like she just read my mind.{/i}"
    mc "Okay, I'll try."
    r "Great."
    scene 8rosaart25 with dissolve
    "Soon all of Rosa's students started working."
    mc "{i}This will probably take a long time.{/i}"
    mc "{i}A very, very long time.{/i}"
    mc "{i}Well, I knew what I was getting myself into.{/i}"
    scene black with fade
    "A few hours later."
    scene 8rosaart26 with dissolve
    r "Okay, guys, time is running out. Finish your work."
    r "And please don't make me repeat myself."
    r "[mc], you can go get dressed for now. Then come and see what my disciples have painted."
    scene 8rosaart23 with dissolve
    mc "Sounds interesting."
    r "Oh, I don't think they'll disappoint you."
    mc "Huh. Now I'm even more interested."
    scene black with fade
    "A few minutes later."
    scene 8rosaart27 with dissolve
    "As Rosa said earlier, you reviewed all the works of her disciples and now you are near the last of them."
    "Despite the fact that each painting was different from the others, it was obvious that each of these young artists was talented in their own way."
    r "Well, what do you think? Do you like it?"
    "Like any other creative person, you understood that feedback means a lot to any artist."
    scene 8rosaart28 with dissolve
    mc "What am I gonna say?"
    mc "I'll say wow! Just awesome! I don't know what you teach them here, but they know their craft well."
    "From the look on Rosa's face, you know she's very happy with your answer."
    scene 8rosaart27 with dissolve
    "Girl" "Um... Thank you."
    mc "You're welcome."
    scene 8rosaart29 with dissolve
    r "Yes, [mc], thank you."
    r "And I hope you're not too tired after today."
    mc "Of course not. I would say that it was... a very interesting experience."
    r "I'm glad you think so."
    r "And, of course, I'm expecting you tomorrow at the same time."
    mc "Oh, yeah, of course."
    stop music fadeout 3.0
    scene black with fade
    "Soon you said goodbye to Rosa and her students and went home."
    "..."
    if jane_path == True and RPjn >= 8 and jane_massage == True:
        "This evening."
        jump day08_julia_night
    else:
        jump day08_rosa_day02


label day08_rosa_day02:
    scene 3nextday with fade
    $renpy.pause(3, hard=True)
    scene black with fade
    play music "music/9 - You Can Make the Sound.ogg"
    "Like you and Rosa agreed yesterday evening, you went back to her studio."
    mc "{i}I don't know why, but this time I'm almost more nervous than yesterday.{/i}"
    mc "{i}I don't know how Rosa does it, but she has a very strange effect on me.{/i}"
    mc "{i}But enough of this useless shit, it's time to act.{/i}"
    "..."
    "You rang the doorbell and started waiting."
    scene 8rosaart30 with dissolve:
        ypos -1.90
        ease 12 ypos 0.0
    "A few seconds later, the door opened and you saw Rosa show up."
    mc "{i}Oh, my God. Is that really Rosa?{/i}"
    mc "{i}She looks completely different today. She is so hot.{/i}"
    scene 8rosaart31 with dissolve
    r "Hello, [mc]."
    mc "Yeah, hello."
    r "Don't just stand there, come on in."
    scene 8rosaart32 with dissolve
    "You walked into the studio and looked at the woman in front of you again."
    r "[mc]? Is everything okay? You look kind of weird."
    mc "Um... Yes... I'm sorry, but I just have to say, you look amazing in that outfit."
    scene 8rosaart33 with dissolve
    r "Oh... Are you really talking about this old thing?"
    mc "{i}If she calls that old, I wouldn't mind looking at something newer.{/i}"
    mc "Well, it looks great on you anyway."
    scene 8rosaart34 with dissolve
    "You knew from Rosa's face that the compliment was right on target."
    r "You're such a flatterer!"
    mc "No, no! It's just the truth."
    r "Okay, I hear you. Thank you very much."
    scene 8rosaart35 with dissolve
    "After exchanging compliments, you went into the studio."
    "This time, you noticed that it was just the two of you."
    scene 8rosaart36 with dissolve
    r "Well, I guess we don't have to waste any more time, and we can get right to the point."
    mc "To the point?"
    scene 8rosaart37 with dissolve
    "Your eyes slipped quickly over Rosa's gorgeous breasts."
    scene 8rosaart36 with dissolve
    r "Yeah, to painting."
    r "You can go undress for now, and I'll get the paints and other tools ready."
    mc "Sounds like a plan."
    scene 8rosaart12 with dissolve
    mc "{i}Yeah, well... same stool.{/i}"
    scene 8rosaart38 with dissolve
    "When you took your clothes off, you could feel Rosa's keen eye on you."
    r "You know, I didn't tell you this before, but I haven't had a male model in practice in a long time."
    r "I usually only paint girls. Sometimes couples. But men are very rare."
    mc "If that's true, why did you decide to invite me?"
    r "I suppose you could call it inspiration? Or maybe it's a thirst for change? Choose whichever you prefer."
    mc "{i}What an unusual reason.{/i}"
    scene 8rosaart39 with dissolve
    r "Mm-hmm... You have a very good physique."
    mc "Well, I'm trying to keep myself in shape. But thanks for the compliment."
    r "Yes... It's perfect for my next scene."
    scene 8rosaart39a with dissolve
    "Rosa looked at you again."
    r "Unlike my students, I'm used to working with a more open nature, so you'll have to take off the rest of your clothes."
    scene 8rosaart40 with dissolve
    mc "You mean I need to take my pants off, too?"
    scene 8rosaart39 with dissolve
    r "No, [mc], I mean absolutely everything."
    mc "Oh... everything."
    mc "{i}And why am I not surprised at all?{/i}"
    scene 8rosaart41 with dissolve
    r "That's exactly what I'm saying. Everything."
    mc "Well, it's not that I'm embarrassed about my body. I just wanted to clarify."
    r "Well, that's great!"
    stop music fadeout 1.0
    "Suddenly there was a doorbell ringing."
    scene 8rosaart42 with dissolve
    r "Hmm? How strange. I wasn't expecting anyone right now."
    r "[mc], wait a minute, I'll check to see who's there."
    mc "Of course, no problem."
    mc "{i}Looks like my pants are gonna stay on for a while.{/i}"
    scene 8rosaart43 with dissolve
    "Rosa opened the front door and you heard a very familiar voice."
    "{color=#A0522D}???{/color}" "Wow, you're dressed up today. What's the occasion?"
    r "What are you doing here? I thought you had an evening shift at the hospital tonight? "
    mc "{i}Okay... I think I'll come take a closer look.{/i}"
    scene 8rosaart44 with dissolve
    play music "music/6 - Positive Mood.ogg"    
    s "Well, it's still a few hours before my shift. You don't mind me stopping by, do you?"
    r "Honey, you came here at a bad time..."
    "Rosa didn't have time to say anything else because Selina noticed you."
    scene 8rosaart45 with dissolve
    s "[mc]? What are you doing here?"
    s "Wait a minute... Just don't tell me she's captured you, and now you're gonna be her model?"
    mc "{i}And she's a guesser.{/i}"
    mc "Well, you're actually right."
    scene 8rosaart46 with dissolve
    "The next second Selina walked into the studio and hugged you tight."
    s "It's so good to see you."
    mc "Yeah, you too."
    scene black with fade
    "A few minutes later."
    scene 8rosaart47 with dissolve
    s "Hmm... So you're here as a model for my mom?"
    mc "A part-time model."
    s "Well, yeah... A part-time model."
    s "And where are all the other students?"
    mc "We're alone here."
    s "What do you mean, alone?"
    scene 8rosaart48 with dissolve
    r "This is our second session. This time it's just me who will paint him."
    s "Just you?"
    r "Yes."
    r "Now, could you please leave my workshop? You know very well that I am used to working alone."
    s "So if I leave now, it'll be just the two of you...?"
    scene 8rosaart49 with dissolve
    "For a while, Selina thought about it."
    mc "{i}She doesn't seem to be happy about the news.{/i}"
    scene 8rosaart50 with dissolve
    s "Okay! You won't believe this, but I have a great idea!"
    s "Mom, how about instead of one model, you have two today?"
    s "I'm volunteering!"
    mc "{i}Whoa! That was quite unexpected.{/i}"
    mc "{i}Is that jealousy? Or am I missing something?{/i}"
    scene 8rosaart51a with dissolve
    r "Baby, are you sure you want to do this? You know I paint for the general public. Many people will see this picture."
    mc "{i}Rosa seems a little surprised, too.{/i}"
    scene 8rosaart48 with dissolve
    s "Yeah, I'm sure. Besides, you invited me to pose for you more than once."
    s "So why not do it today?"
    r "Yes, but..."
    r "I don't know what to say."
    s "Don't say anything, just paint us together."
    scene 8rosaart51 with dissolve
    r "That's not like you at all. But if that's what you really want, I don't see any reason to say no."
    r "And since you want to pose for me today, we'll probably make our exhibit a little softer than I planned."
    scene 8rosaart48 with dissolve
    s "Oh, no problem. What do I have to do?"
    r "First, I want you to take off your top."
    scene 8rosaart53 with dissolve
    "Without further ado, Selina went to undress."
    mc "{i}Oh, man... When I came here today, I certainly didn't expect this.{/i}"
    mc "{i}I don't even know how to react to all this.{/i}"
    scene 8rosaart54 with dissolve
    s "I hope this painting will be the best of all your works."
    r "Don't worry, baby, I'll do my best."
    scene 8rosaart55 with dissolve
    s "That's good..."
    mc "{i}I don't know why, but I'm feeling a little nervous again.{/i}"
    mc "{i}Not to mention the fact that this whole situation seems super weird to me.{/i}"
    scene 8rosaart56 with dissolve
    "Carefully covering her chest with her arm, Selina turned to you."
    s "Well... I hope everyone is ready?"
    r "You don't have to be shy about your body, we're all adults here. That's what art is all about."
    mc "{i}Rosa isn't the kind of person who's embarrassed about nudity.{/i}"
    scene 8rosaart57 with dissolve
    s "Who's embarrassed here?!"
    s "I'm perfectly fine."
    r "Hmm... Well, if you say so."
    scene 8rosaart58 with dissolve
    "Despite the fact that Selina tried to look impassive, you could see how she turned a little red."
    mc "{i}She doesn't seem as crazy as usual. Even if it's just a little bit, I think she feels out of place too. {/i}"
    mc "{i}Maybe I should cheer her up a little bit.{/i}"
    scene 8rosaart59 with dissolve
    mc "You know, Selina, you don't have to be shy, you look amazing."
    mc "I don't know much about painting, but I'm already proud to be in the same painting with such a beautiful girl."
    r "..."
    scene 8rosaart58 with dissolve
    s "Oh... Thank you very much, [mc]."
    scene 8rosaart60 with dissolve
    r "Okay, that's enough of that... Let's get to work."
    r "Follow me."
    scene 8rosaart61 with dissolve
    "Rosa took you to the same place you posed yesterday."
    r "First of all, I want you to take it seriously."
    r "Now we'll find you an interesting position, and then I'll begin working."
    r "So, [mc], your task now is to embrace Selina from behind and portray something like attraction to her."
    r "Is that clear?"
    mc "Honestly, not really."
    r "Don't worry, if anything, I'll fix you up. Now get started."
    scene 8rosaart62 with dissolve
    s "Well, I'm sure it's very different from your regular job. And from making music, too."
    mc "That's an understatement."
    s "Hehe. Then let's make this experience unforgettable."
    mc "{i}I'm sure I couldn't have forgotten this day even if I wanted to.{/i}"
    scene 8rosaart63 with dissolve
    r "Selina! [mc]! Please be a little more serious."
    s "Um... I'm sorry, Mom."
    mc "Ahem... Sorry, Rosa."
    "..."
    r "It's okay."
    r "So, [mc], first try to take Selina by the shoulders."
    scene 8rosaart64 with dissolve
    mc "Something like that?"
    r "Mmmm, not quite."
    r "I need more life in this scene. More expression."
    r "Selina, try putting your arm around him, too."
    scene 8rosaart65 with dissolve
    "Selina obeyed her mother's command."
    s "Is this good?"
    r "Not exactly."
    r "[mc], put your free hand on Selina's waist."
    mc "{i}Damn it... Despite the slight nervousness, all these touches of a half-naked girl are starting to turn me on.{/i}"
    scene 8rosaart65a with dissolve
    "..."
    scene 8rosaart65b with dissolve
    "You looked at Rosa in silence, trying to catch her thoughts."
    r "No, no, and no. None of this works."
    scene 8rosaart66 with dissolve
    s "Shit, Mom, we don't understand you at all. What do you want from us?"
    s "Can you describe it normally, or at least show it to me?"
    r "Oh, okay."
    r "Selina, step aside for a second. I'll take your role."
    scene 8rosaart67 with dissolve
    r "Okay, [mc], I want you to hug me just like you hugged Selina."
    mc "Um... Are you sure about this?"
    r "Yeah, you don't have to worry about it."
    mc "Okay... I can do that."
    scene 8rosaart68 with dissolve
    "Like Rosa asked you to, you hugged her from behind right in front of her half-naked daughter."
    r "Yes... It's not bad."
    mc "{i}Yeah, it's not bad at all!{/i}"
    scene 8rosaart69 with dissolve
    r "Now, I want you to grab my chest with your left hand."
    mc "Are you serious?"
    r "I'm very serious."
    mc "{i}Well, since she's asking for it, I'll just have to do it.{/i}"
    scene 8rosaart69a with dissolve
    "..."
    mc "{i}Oh my God. Her breasts are so soft.{/i}"
    r "Mm-hmm... Yeah, that's it. Excellent. I think you've got the very essence."
    mc "{i}I think I've got more than just the essence...{/i}"
    scene 8rosaart70 with dissolve
    "You felt Rosa's large breasts rise in time with her calm breathing."
    mc "{i}How the hell does she stay so calm?{/i}"
    scene 8rosaart71 with dissolve
    "Not to mention the way her round ass is pressed against your dick."
    mc "{i}A little more and she'll definitely feel my boner.{/i}"
    scene 8rosaart72 with dissolve
    r "What do you say, [mc]? Isn't that much better?"
    mc "Yeah, I guess so."
    r "Do you remember that position?"
    scene 8rosaart73 with dissolve
    s "Mom! We get it, you can go back to your canvas and paint."
    s "I'll take your place."
    mc "{i}Selina obviously didn't like what she saw.{/i}"
    r "Whatever you say, honey."
    scene 8rosaart74 with dissolve
    "Selina quickly took her mother's place, and now you're touching her naked breasts."
    mc "{i}I can't even say which one of these redheaded devils is hotter.{/i}"
    mc "{i}One thing I can say for sure is, the effect on my dick is the same.{/i}"
    mc "{i}And it's not like Selina doesn't like it.{/i}"
    r "Okay. Now try to stay still. I'm starting to paint."
    scene 8rosaart75 with dissolve
    "Soon Rosa started working."
    mc "{i}This will most likely take a very long time...{/i}"
    mc "{i}I hope I can handle it.{/i}"
    scene black with fade
    "A few hours later."
    scene 8rosaart76 with dissolve
    r "Okay, guys, I think I'm done."
    r "You can see the result of our work together."
    mc "{i}Finally!{/i}"
    scene 8rosaart77 with dissolve
    "You and Selina came up to the new painting and looked at it for a while."
    mc "{i}Wow, Rosa's work is impressive. Perhaps even so much that I wouldn't mind buying it myself.{/i}"
    mc "{i}But I'm not sure I can afford it.{/i}"
    scene 8rosaart78 with dissolve
    s "So, what do you say [mc]? Do you like it?"
    mc "That's a painting I definitely like."
    s "Ha ha ha! I thought you'd like it."
    s "If the picture shows a naked girl, the guys usually have enough to like."
    mc "Hey! Can you blame us for that?"
    s "Mmm..."
    scene 8rosaart79 with dissolve
    r "Well, I heard what [mc] said. What about you, Selina?"
    r "Do you regret posing for me?"
    scene 8rosaart80 with dissolve
    s "I never thought I'd see myself in one of your paintings before."
    s "And that's not what I imagined when I came to your studio today. But if we're being honest, then..."
    s "I have no regrets at all."
    s "It's a very good painting, Mom. You did a great job."
    scene 8rosaart79 with dissolve
    r "Thank you, honey."
    r "And since we're done, I think it's time for you to get dressed."
    scene 8rosaart80 with dissolve
    s "Oh... Yeah. Right. I've been standing there without my top for so long that I almost forgot about it."
    scene black with fade
    "A few minutes later."
    scene 8rosaart81 with dissolve
    s "Okay, Mom, even though it was all very interesting, I think it's time for us to go."
    r "Yes, of course. Thank you both for being part of this work."
    r "I'm gonna show this painting to some of my friends in the art world. I think they'll like it."
    mc "Tell me later what they think of it?"
    r "Yes, sure."
    scene 8rosaart82 with dissolve
    s "By the way, [mc], there's more than an hour left before my shift at the hospital. Shall we take a walk for a while?"
    s "I'd like to talk to you about something."
    mc "Of course, I don't mind."
    s "Okay, great!"
    scene 8rosaart83 with dissolve
    r "See you later, [mc]."
    r "And don't be late for work, Selina."
    s "Don't worry, Mom."
    r "Okay."
    scene black with fade
    "Soon you and Selina left Rosa's studio."
    stop music fadeout 3.0
    jump day08_selina_flashback


label day08_selina_flashback:
    if rosa_path == True:
        scene black with fade
        play music "music/8 - Intro Music.ogg"
        "A few minutes later, you found a quiet place on the street where you decided to sit and talk."
        scene 8selina01 with dissolve
        s "What a crazy day, huh?"
        mc "Don't tell me."
        mc "If someone had told me this morning about how this day would go, I wouldn't have believed them."
        mc "Your mother surprised me a lot."
        s "Well... My mom's a pretty eccentric person. But I'm used to it."
        "..."
    else:
        scene black with fade
        play music "music/8 - Intro Music.ogg"
        "A few hours later, you arrived at the place where Selina wanted to meet."
        scene 8selina01 with dissolve
        "You said hello to each other and sat down at one of the tables nearby."

    mc "What did you want to talk to me about?"
    scene 8selina02 with dissolve
    s "Yes... You see, the thing is... I wanted to tell you something."
    mc "{i}Okay... This is not a very encouraging start.{/i}"
    s "First of all, I wanted to say that I like you very much."
    mc "{i}Well, maybe I was wrong.{/i}"
    s "But that's not all. Because I like you, I want to tell you something. "
    s "Something that's really bothering me right now."
    mc "I'm not sure what you mean, but go on."
    scene 8selina03 with dissolve
    s "It might be easier if I told you about the day we met."
    s "Please, just listen to this story..."
    mc "Okay. I'm listening."
    stop music fadeout 3.0
    scene black with fade
    "The day you met Selina."
    play music "music/10 - Street's.ogg"
    scene 8selinafb01 with dissolve
    s "It all started that day early in the morning."
    s "I woke up at my house in bed as usual..."
    scene 8selinafb02 with dissolve
    s "As soon as I opened my eyes, I felt the sun shining right in my face."
    scene 8selinafb03 with dissolve
    s "Maybe I should make it clear here that I usually only sleep in my panties."
    s "An old habit I don't want to get rid of."
    scene 8selinafb04 with dissolve
    s "Still a little sleepy, I went through the living room to the bathroom."
    s "It's pretty weird, but at that point something caught my attention on the street."
    scene 8selinafb05 with dissolve
    s "Without a second thought, I went up to the window and took a better look."
    scene 8selinafb06 with dissolve
    s "It was a cat."
    s "A little gray ball of fur that was lounging on the warm steps under the sun."
    scene 8selinafb07 with dissolve
    s "At the time, I thought it was a very nice sight."
    s "And then I noticed a glare in the window across the street."
    scene 8selinafb08 with dissolve
    s "And when I raised my head, then-"
    mc "Then you saw me."
    scene 8selinafb08a with dissolve
    s "That's right. There was some guy standing there staring at me through binoculars."
    s "At first I was so surprised that I couldn't find anything better than just smiling back."
    scene 8selinafb09 with dissolve
    mc "You gotta be kidding me. I thought you did it on purpose."
    mc "Besides, you looked so confident..."
    s "Oh, no! Believe me, I panicked terribly at that moment."
    mc "Wow..."
    scene 8selinafb10 with dissolve
    s "Anyway, as soon as I woke up a little bit, I ran away from the window."
    mc "Oh, man... Now that you've told me that, I feel very ashamed."
    scene 8selinafb11 with dissolve
    s "Don't blame yourself."
    s "I didn't realize it then, but, deep down, I actually secretly liked it."
    scene 8selinafb12 with dissolve
    s "And yet, we can say that that was our first meeting."
    scene 8selina01 with dissolve
    mc "Hmmm..."
    mc "It's a little unusual, but I still don't understand why you're telling me this."
    scene 8selina04 with dissolve
    s "But that's not the whole story."
    mc "Oops... I'm sorry I interrupted you. Go on."
    s "Yeah..."
    scene 8selinafb13 with dissolve
    s "A few hours after this incident, I came to work."
    s "I walked into the doctor's locker room."
    scene 8selinafb14 with dissolve
    s "My best friend, Karen, was there."
    s "She and I never kept any secrets from each other, so we could talk about anything."
    s "And then, during our conversation, we talked about that morning's incident."
    scene 8selinafb15 with dissolve
    s "Karen, you're not gonna believe what happened to me today."
    s "Some pervert was watching me from the window across the street."
    s "All while I was in just my panties."
    scene 8selinafb16 with dissolve
    "{color=#DC143C}Karen{/color}" "Is this that big window in the building across from your living room?"
    s "Yeah, that's the one."
    "{color=#DC143C}Karen{/color}" "Wasn't there some old man who used to bring all kinds of women home.?"
    s "Well, now there's a young guy living there."
    "{color=#DC143C}Karen{/color}" "Is he good looking?"
    scene 8selinafb17 with dissolve
    s "How would I know?! I didn't even get a good look at him."
    scene 8selinafb16 with dissolve
    "{color=#DC143C}Karen{/color}" "Doesn't mean he's not good looking."
    scene 8selinafb17 with dissolve
    s "You can imagine that I wasn't in the mood for that. My heart dropped into my stomach when I saw him."
    "{color=#DC143C}Karen{/color}" "Ha ha ha! That sounds just like you!"
    s "At first I thought he'd leave right away, but it was like he wasn't embarrassed at all to be caught, and he just kept staring."
    scene 8selinafb16 with dissolve
    "{color=#DC143C}Karen{/color}" "So what did you do next?"
    scene 8selinafb17a with dissolve
    s "I... um..."
    s "I kind of panicked and just waved at him."
    "{color=#DC143C}Karen{/color}" "Ha ha ha!!! "
    scene 8selinafb17 with dissolve
    s "Hey, don't laugh at me!"
    scene 8selinafb18 with dissolve
    "{color=#DC143C}Karen{/color}" "And that's what your problem is, Selina."
    "{color=#DC143C}Karen{/color}" "I'm telling you, try to make things easier on yourself. Just try to be a little more relaxed."
    "{color=#DC143C}Karen{/color}" "Take me for example!"
    s "Oh, uh... Maybe you're right, and I really should be more relaxed."
    scene 8selinafb19 with dissolve
    "{color=#DC143C}Karen{/color}" "Of course I'm right!"
    "{color=#DC143C}Karen{/color}" "Now let's go... If I'm late again, Dr. Gates will definitely kill me."
    scene 8selinafb20 with dissolve
    s "I'll see you at lunch?"
    "{color=#DC143C}Karen{/color}" "Yeah, I'll meet you in the cafeteria."
    stop music fadeout 3.0    
    scene black with fade
    "Some time later, during Selina's lunch break."
    scene 8selinafb21 with dissolve
    play music "music/6 - Positive Mood.ogg"    
    "{color=#DC143C}Karen{/color}" "...and you can imagine this patient being all orange. Although he didn't even notice it himself."
    "{color=#DC143C}Karen{/color}" "No wonder his wife cheated on him."
    "..."
    "{color=#DC143C}Karen{/color}" "Selina, are you even listening to me?"
    scene 8selinafb21a with vpunch
    "{color=#DC143C}Karen{/color}" "Selina!"
    scene 8selinafb22 with dissolve
    s "Ah?! What's that?!"
    s "I'm sorry, I was thinking a little bit."
    scene 8selinafb23 with dissolve
    "{color=#DC143C}Karen{/color}" "Yeah, right. I'm not blind. I see where you were looking."
    "{color=#DC143C}Karen{/color}" "And I have a pretty good idea what you were thinking."
    scene 8selinafb24 with dissolve
    "{color=#DC143C}Karen{/color}" "You were thinking about a handsome guy in a white coat."
    s "What are you talking about? I was looking in a completely different direction."
    "{color=#DC143C}Karen{/color}" "Your lips say no, but your eyes say yes."
    scene 8selinafb25 with dissolve
    "{color=#DC143C}Karen{/color}" "You know, if you're really interested in this doctor, why don't you just go up to him and ask him out?"
    s "I don't know... I'm not sure. Maybe next time?"
    scene 8selinafb23 with dissolve
    "{color=#DC143C}Karen{/color}" "Here we go again! As usual, you put everything off for later."
    scene 8selinafb26 with dissolve
    s "That's not true!"
    "{color=#DC143C}Karen{/color}" "If it isn't true, then go over there and talk to him. Right now."
    s "Well, I can't just... What if he wants to be alone now?"
    scene 8selinafb25 with dissolve
    "{color=#DC143C}Karen{/color}" "What if, while you're thinking about doing it or not, a brick falls on him?"
    s "Uh... What brick?"
    "{color=#DC143C}Karen{/color}" "I mean, you always think too much about hypotheticals, and then you just make excuses."
    "{color=#DC143C}Karen{/color}" "Better listen to me and just do it."
    "{color=#DC143C}Karen{/color}" "There are only two options for what happens next: either he says yes or no."
    s "But..."
    scene 8selinafb23 with dissolve
    "{color=#DC143C}Karen{/color}" "Oh my God... Okay! Okay! Let's go talk to him together."
    stop music fadeout 3.0    
    scene black with fade
    "A minute later."
    scene 8selinafb27 with dissolve
    play music "music/10 - Street's.ogg"    
    "{color=#DC143C}Karen{/color}" "Good afternoon, you and I work together, but we don't know each other very well. How about we fix that?"
    "{color=#808000}Dr. Brown{/color}" "Um... Yes, of course. Why not?"
    "{color=#DC143C}Karen{/color}" "You're Dr. Brown, aren't you?"
    scene 8selinafb28 with dissolve
    "{color=#808000}Dr. Brown{/color}" "That's right. Dr. Brown. Pediatrics."
    "{color=#808000}Dr. Brown{/color}" "And you, if I remember correctly, Karen and Serena."
    scene 8selinafb30 with dissolve
    s "Selina. My name is Selina."
    scene 8selinafb31 with dissolve
    "{color=#808000}Dr. Brown{/color}" "Oh... I'm sorry, I guess I got your name mixed up."
    scene 8selinafb30 with dissolve
    s "That's okay."
    scene 8selinafb29 with dissolve
    "{color=#DC143C}Karen{/color}" "You know, Mr Brown, my friend and I wanted to go out for a drink after work today. Would you like to keep us company?"
    "{color=#808000}Dr. Brown{/color}" "Very tempting offer. I'm not busy after work."
    "{color=#DC143C}Karen{/color}" "Well, that's great! Then we'll see you after work?"
    scene 8selinafb32 with dissolve
    "{color=#808000}Dr. Brown{/color}" "Sure, I'll see you after work."
    "{color=#808000}Dr. Brown{/color}" "And if that's all, I have to go. Unfortunately, my lunch break is over."
    s "We won't keep you any longer, Dr. Brown."
    "{color=#808000}Dr. Brown{/color}" "Nice talking to you. Good day, ladies."
    scene 8selinafb33 with dissolve
    s "Until we meet again."
    "{color=#DC143C}Karen{/color}" "Mm-hmm... I can't wait to see him again."
    scene 8selinafb34 with dissolve
    "{color=#DC143C}Karen{/color}" "And this doctor of yours, he looks even better up close. Maybe I should hit on him myself."
    s "Hey! That's not funny at all."
    "{color=#DC143C}Karen{/color}" "Ha ha ha! Yes, it is funny! But don't worry, it's just a joke."
    "{color=#DC143C}Karen{/color}" "Okay. Our lunch break is also over. It's time to get back to work."
    s "Yeah... It's time."
    stop music fadeout 3.0
    scene black with fade
    "A few hours later."
    scene 8selinafb35 with dissolve
    play music "music/8 - Intro Music.ogg"
    s "{i}Damn, it's the end of the shift. Where the hell is Karen? We were supposed to go for a drink with Dr. Brown.{/i}"
    s "{i}I hope she's not in trouble.{/i}"
    scene 8selinafb36 with dissolve
    s "Hey, Elsa, have you seen Karen?"
    "{color=#90EE90}Elsa{/color}" "Hmm... I'm not sure, but I think she went somewhere towards the archives. Check there."
    s "Thanks."
    "{color=#90EE90}Elsa{/color}" "No problem."
    scene 8selinafb37 with dissolve
    s "{i}What the hell is she doing in the archives?{/i}"
    s "{i}I need to find her soon and get out of here. I don't want to stay here a minute longer.{/i}"
    scene 8selinafb38 with dissolve
    "Selina opened the door to the archives and walked in."
    s "{i}Yeah, I think I can already hear Karen's voice.{/i}"
    stop music fadeout 1.0
    scene 8selinafb39 with dissolve
    "After only a few steps, Selina froze in place."
    s "{i}What the... fuck...{/i}"
    scene 8selinafb40 with dissolve
    s "{i}Oh my God! It's Karen and Dr. Brown.{/i}"
    "{color=#DC143C}Karen{/color}" "Ahhhh... yes... right here..."
    s "{i}Are they fucking?!{/i}"
    scene 8selinafb41 with dissolve
    "{color=#DC143C}Karen{/color}" "Mmm..."
    scene 8selinafb41a with dissolve
    "..."
    scene 8selinafb42 with dissolve
    "{color=#DC143C}Karen{/color}" "Get off."
    "{color=#808000}Dr. Brown{/color}" "Baby, what are you doing?"
    "{color=#DC143C}Karen{/color}" "I said get off!"
    scene 8selinafb43 with dissolve
    "{color=#DC143C}Karen{/color}" "Selina, It's not what you think."
    "{color=#DC143C}Karen{/color}" "Wait a minute, let me explain everything to you."
    "{color=#DC143C}Karen{/color}" "We're just..."
    scene 8selinafb46 with dissolve
    s "Before you try to explain anything to me, at least cover your naked tits."
    s "Jesus, this is ridiculous."
    scene 8selinafb45 with dissolve
    "Karen immediately closed her robe."
    scene 8selinafb45a with dissolve
    "..."
    scene 8selinafb47 with dissolve
    "{color=#DC143C}Karen{/color}" "Selina... Don't make me look like a villain right now."
    "{color=#DC143C}Karen{/color}" "I didn't get any further than kissing with him anyway."
    "{color=#808000}Dr. Brown{/color}" "What the hell is going on here?"
    scene 8selinafb44 with dissolve
    s "You know, I don't care anymore."
    s "I thought you were my friend, but it turns out you're not."
    s "Do what you want. Fuck him right here if you want. If you want, you can even play chess. I don't give a shit."
    s "I'm gonna go."
    scene 8selinafb48 with dissolve
    "{color=#DC143C}Karen{/color}" "Selina, wait!"
    "{color=#DC143C}Karen{/color}" "Selina..."
    scene black with fade
    "Some time later."
    scene 8selinafb49 with dissolve
    play music "music/Maxim Nick - Falling Down.mp3"
    "..."
    s "Home sweet home."
    scene 8selinafb50 with dissolve
    "Selina slammed the door behind her and gently put her bag on the floor."
    scene 8selinafb51 with dissolve
    "She leaned against the door wearily and sighed heavily."
    "Her best friend's traitorous deed still made her heart break."
    scene 8selinafb52 with dissolve
    "The girl slowly slid down onto the cold, wooden floor."
    "Soon the first quiet sobs broke the silence."
    scene 8selinafb53 with dissolve
    "Tears begin to spill from her eyes."
    "Here, alone, she was finally able to let her feelings out."
    "Selina cried."
    "..."
    scene 8selina04a with fade
    s "Well, you know what happened next..."
    scene black with fade
    "Some time later."
    scene 8selinafb54 with dissolve
    s "I was lying on the couch reading some book trying to distract myself. I can't say I was getting distracted, but at least I tried."
    scene 8selinafb55 with dissolve
    s "And then I saw the glare in the window across the street again."
    s "And you know, at that moment, Karen's words came through my head that I needed to be more open and liberated."
    s "At first it pissed me off, but then I calmed down and thought, \"Why not?\""
    scene 8selinafb56 with dissolve
    s "I stood by the window, took my shirt off and beckoned you with my hand."
    s "At the time, I just wanted to tease you a little bit."
    s "But imagine my surprise when, ten minutes later, someone rang my doorbell."
    scene 8selinafb57 with dissolve
    "DING!"
    s "At first, I was terrified..."
    scene 8selinafb58 with dissolve
    s "...but then I thought about it."
    s "Even though I only saw you from afar, you didn't look like a murderer or a psychopath."
    s "Not that I knew what one of those would look like, but still."
    s "Besides, you seemed to be pretty cute to me."
    scene 8selinafb59 with dissolve
    s "So I took a chance and opened the door."
    scene 8selinafb60 with dissolve
    mc "And that's when you saw me."
    s "And you saw me."
    s "Then you asked me something dirty and..."
    scene 8selinafb61 with vpunch
    mc "And you slammed the door right in my face."
    mc "Yeah, I remember that very well."
    scene 8selinafb62 with dissolve
    s "The truth is, I panicked again at the time."
    s "It was all too fast. Too weird."
    scene 8selinafb63a with dissolve
    s "But then I remembered Karen's confident face again, and all she said was..."
    s "How easily she always got what she wanted, and how easy it was to have everything."
    scene 8selinafb63 with dissolve
    s "Then I said to myself, \"I want the same.\""
    s "And then... Then all my fear disappeared."
    scene 8selinafb64 with dissolve
    s "Next thing I knew, I just took my clothes off."
    scene 8selinafb65 with dissolve
    "..."
    scene 8selinafb66 with dissolve
    s "I got a big smile on my face."
    scene 8selinafb67 with dissolve
    s "And then I just opened the door for you."
    s "And what happened, happened."
    "..."
    stop music fadeout 3.0
    scene 8selina01 with dissolve
    mc "Wow, now that's a story."
    mc "I remember all the events of that day in a completely different way."
    mc "However, I still don't fully understand the reason why you wanted to tell me this story."
    scene 8selina04 with dissolve
    play music "music/13 - Hope is Still Living.ogg"
    s "The thing is, I'm not really as crazy as you might think I am."
    s "Before I met you, I had no idea I was capable of such bold and crazy things."
    s "But I liked it. Being near you, I could feel really alive."
    s "I'm not saying that all my behavior was some kind of act. No, rather, it was just a piece of the real me."
    s "A piece that, until I met you, I had kept hidden deep inside."
    s "And now that I realize I really like you, I want something more than just sex without a commitment."
    s "I know this conversation could ruin everything, but it's the only way I can do it."
    s "Tell me, would you like to have a serious relationship with me?"
    mc "{i}Now that's a real question!{/i}"
    mc "{i}Really, what do I want?{/i}"
    menu:
        "{color=#66FF33}You want a serious relationship with Selina":
            scene 8selina05 with dissolve
            "You put your hand on Selina's and smiled."
            mc "Of course I want a serious relationship with you."
            scene 8selina06 with dissolve
            s "R-really?"
            mc "Yeah, of course."
            mc "Actually, I want it even more now than before."
            s "That's amazing! I felt sure you would."
            scene 8selina07 with dissolve
            "Selina jumped on her feet and kissed you hard."
            s "Mmm..."
            mc "{i}Now I'm even more sure that I made the right choice.{/i}"
            scene 8selina08 with dissolve
            s "Um... I'm glad we had such a good chat."
            s "But like I said earlier, I have a shift coming up, so I can't stay here any longer."
            mc "It's okay, I get it."
            s "Call me later?"
            mc "Yes, of course."
            s "Bye, [mc]."
            mc "Bye, Selina."

        "You need to think this through":
            $ selina_broke_up = True
            scene 8selina01 with dissolve
            mc "It's all so sudden, I guess I just need a couple of days to think about it."
            scene 8selina04a with dissolve
            s "Oh... Of course, I understand."
            mc "Are you sure you're okay?"
            scene 8selina06 with dissolve
            s "Everything's fine."
            s "Anyway, I'm glad we talked."
            s "But like I said earlier, I have a shift coming up, so I can't stay any longer."
            mc "It's okay, I get it."
            scene 8selina08 with dissolve
            s "Call me later?"
            mc "Yes, of course."
            s "Bye, [mc]."
            mc "Bye, Selina."
    stop music fadeout 3.0
    if jane_date == True:
        jump day08_jane_date
    else:
        jump day08_home_sms


label day08_jane_date:
    if rosa_path == True:
        scene black with fade
        "Some time later."
        "After seeing Rosa and Selina, you barely made it to your date with Jane on time."
        "..."
    scene 8janedate01 with dissolve
    play music "music/10 - Street's.ogg"
    "You were standing outside the restaurant where you planned your date with Jane."
    mc "{i}I think Julia mentioned that I should be gentle with Jane. Maybe that's not such a bad idea.{/i}"
    mc "{i}Besides, I have to show her that I'm a very reliable person.{/i}"
    mc "{i}Well... I feel like it's not gonna be a simple date.{/i}"
    "A second later, you noticed a girl you knew from afar."
    scene 8janedate02 with dissolve:
        ypos -1.90
        ease 12 ypos 0.0
    mc "{i}Wow... Just wow!{/i}"
    mc "{i}Looking at this beauty, I think my heart is beating faster.{/i}"
    scene 8janedate03 with dissolve
    "As soon as Jane got closer, you greeted her with a hug."
    jn "Oh... It's good to see you too, [mc]."
    mc "The feeling is mutual."
    scene 8janedate04 with dissolve
    mc "And I can't help but notice that you look absolutely stunning."
    jn "Thank you."
    jn "I see you've decided to wear something more classic today, too. I like it."
    mc "Yeah, thank you, too."
    mc "Based on the time, I think our table should be ready by now. Shall we go inside?"
    jn "I'd love to."
    scene 8janedate05 with dissolve
    jn "I've wanted to go to this restaurant for a long time. It's a good thing I finally got the chance."
    jn "Especially with such pleasant company."
    scene 8janedate06 with dissolve
    "You went inside the restaurant and waited for a while."
    jn "Yes... You can see right away that this is a very nice place."
    mc "{i}And it's very expensive. But it does not matter now. {/i}"
    mc "I decided to invite such a special girl to a place befitting her beauty and status."
    scene 8janedate07 with dissolve
    jn "Mmm... Someone decided to overwhelm me with compliments today?"
    mc "You deserve every one of them."
    jn "Hehe. It's nice, but don't overdo it."
    mc "Deal."
    scene black with fade
    "Soon the waiter took you and Jane to your table."
    "The waiter took your order and you were alone again."
    scene 8janedate08 with dissolve
    jn "Well, I have to say, this whole date was a little unexpected."
    jn "I thought our relationship was a little different."
    mc "That's why I invited you here."
    mc "I think we've started things off on the wrong foot. And because of that, everything between us became very confusing."
    scene 8janedate09 with dissolve
    jn "Oh, really?"
    jn "What kind of relationship do you think we should have?"
    menu:
        "I want a serious relationship":
            $ RPjn += 1
            mc "I want you and I to have a serious relationship."
            scene 8janedate09b with dissolve
            jn "Don't you think that's moving a bit quickly?"
            jn "I'm not saying it's a bad goal to have, but you know it's not that simple."
            mc "I know it's not easy. But, you have to admit it, it is a good goal."
            scene 8janedate09 with dissolve
            jn "Yeah, maybe so."

        "I want to keep things between us as they are":
            mc "I want to keep things between us as they are."
            scene 8janedate09b with dissolve
            jn "Don't get me wrong, I like the way you and I usually spend time, but..."
            jn "Weren't you just talking about how we got off on the wrong foot?"
            mc "I'm sorry, I guess I just lost track."
            scene 8janedate09 with dissolve
            jn "That's okay."

        "{color=#66FF33}I want our relationship to move forward":
            $ RPjn += 3
            mc "I want our relationship to move forward, to develop with us."
            mc "And, of course, I don't want us to hide from anyone."
            scene 8janedate09a with dissolve
            jn "I know what you mean, and I agree with that."
            mc "That's nice to hear."

    scene 8janedate10 with dissolve
    "A few minutes later, you got your order."
    jn "Mm-hmm... Looks delicious."
    mc "Bon Appetit."
    jn "Yeah, Bon Appetit."
    scene 8janedate11 with dissolve
    "You've started eating."
    mc "{i}Her dress is so revealing that I almost can't help but stare.{/i}"
    menu:
        "{color=#66FF33}Focus on the food":
            $ RPjn += 2
            mc "{i}No! Today I need to make a good impression on Jane. And staring at her chest obviously won't help it.{/i}"
            scene 8janedate12 with dissolve
            jn "You know, I didn't really know what to expect from this date, but..."
            mc "{i}Did she just call it a date?{/i}"
            jn "But I really like spending time with you."
            mc "Believe me, that feeling is mutual."
        "Focus on Jane's dress":
            mc "{i}I don't think anything bad is gonna happen if I look at it with one eye.{/i}"
            scene 8janedate11a with dissolve
            "..."
            mc "{i}Ohhh... She is as sexy as ever.{/i}"
            scene 8janedate12 with dissolve
            jn "Did you see something you like?"
            mc "{i}Fuck... I think she noticed out where I was looking.{/i}"
            mc "{i}Let's see if I can get out of this.{/i}"
            mc "Oh, come on! How could anyone in their mind take their eyes off such beauty?"
            jn "God, you're such a child."
    scene black with fade
    "You and Jane had a little chat about trivial things and finished eating."
    scene 8janedate13 with dissolve
    jn "How about some wine?"
    mc "I'd love to."
    jn "Mm-hmm... Would you like to make a toast?"
    menu:
        "To love":
            $ RPjn += 1
            mc "I suggest a toast to love."
            scene 8janedate13b with dissolve
            jn "Wow. That's a little sudden."
            mc "Well, love is a universal thing. How many songs and poems were written about it. And how many more songs and poems will there be."
            mc "Anyway, we all need love."
            scene 8janedate13a with dissolve
            jn "Yeah, I guess you're right."

        "{color=#66FF33}To a lovely evening":
            $ RPjn += 2
            mc "I suggest we drink to this beautiful evening."
            scene 8janedate13a with dissolve
            jn "Mm... I like this evening, but I don't mind if it gets any better."
            mc "Let's hope so."

        "To Jane":
            mc "I suggest we drink to the girl sitting across from me."
            scene 8janedate13b with dissolve
            jn "Oh... To me?"
            mc "Yeah, to you, exactly."
            mc "For your beauty, for your strong character. To you."
            jn "Hmm. Thank you."

    scene 8janedate14 with dissolve
    "*The clinking of glasses*"
    stop music fadeout 3.0
    scene black with fade
    "Some time later."
    scene 8janedate15 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Looks like the evening's coming to an end."
    jn "Yes... No wonder I wanted to come here, I liked this restaurant very much."
    mc "Yes, there's a very pleasant atmosphere here."
    mc "But I guess we'd better get going, huh?"
    jn "Yeah, as much as I'd like to sit here, I'm going to have a rough day tomorrow."
    jn "I have to be fresh in the morning."

    scene black with fade
    "You paid the bill and you were ready to leave this place."

    if RPjn >= 14:
        scene 8janedate16 with dissolve
        "Talking about everything in the world, you took Jane by the hand, and went outside."
        "You were both in a good mood."
    else:
        scene 8janedate16a with dissolve
        "Talking about everything in the world, you went outside."

    scene 8janedate17 with dissolve
    if RPjn >= 14:
        jn "It was an amazing evening, [mc]."
        jn "I don't remember the last time I went on such a good date."
        jn "Thank you for everything."
        mc "Thank you for that. But without you, it wouldn't have been possible."
        scene 8janedate20 with dissolve
        jn "Mm-hmm... You're such a romantic."
        mc "Huh. It's not for nothing that I play music."
        jn "That's for sure."
        mc "{i}I think it's the perfect time for the final step on this date.{/i}"
        scene 8janedate18 with dissolve
        "The next thing you know, you stepped towards Jane and kissed her."
        jn "Mmmm..."
        mc "{i}She doesn't seem to mind at all.{/i}"
        scene 8janedate19 with dissolve
        "Your hands gently landed on Jane's shoulders."
        mc "{i}She's so beautiful.{/i}"
        scene 8janedate20 with dissolve
        jn "Yes... It was definitely a beautiful evening."
        jn "We'll have to do it again sometime."
        mc "For sure."
        mc "I'll call you."
        jn "Yeah."
        jn "Well, now I really have to go."
        jn "Bye."
        mc "Until next time."
        scene black with fade
        "Your date with Jane was over."
        mc "{i}Seems like everything went great. It definitely makes me happy.{/i}"

    else:
        jn "I had a good time, [mc]."
        jn "Thank you for inviting me."
        mc "Thank you for that. But without you, it wouldn't have been possible."
        scene 8janedate20a with dissolve
        jn "[mc], about this whole meeting..."
        jn "Like you said, things have gotten too complicated between us lately..."
        jn "Let's not rush into our relationship yet."
        mc "{i}I think I just got politely dumped.{/i}"
        mc "{i}As sad as it may be, maybe it was my fault, too.{/i}"
        mc "Yes... I understand that."
        scene 8janedate20 with dissolve
        jn "Okay, thanks again for the evening, but I think I should go."
        jn "Bye."
        mc "Yeah, bye."
        scene black with fade
        "Your date with Jane was over."
        mc "{i}Oh, I can tell from her behavior that this date didn't go well.{/i}"
        mc "{i}Too bad I can't do anything about it.{/i}"
    stop music fadeout 3.0
    jump day08_home_sms

label day08_home_sms:
    scene black with fade
    play music "music/8 - Intro Music.ogg"
    "The same night at your house."
    scene 8sms04 with dissolve
    if RPjn >= 14:
        mc "{i}Hmm... I don't think I should stop after just one date with Jane.{/i}"
        mc "{i}Even though it was successful, it doesn't mean we're dating now.{/i}"
        mc "{i}If we're using analogies, I've only put our relationship in check, and now I have to put it in checkmate.{/i}"
        mc "{i}And for that, I'll need some help...{/i}"
        if nicole_plus == True:
            $ nicole_help_jane = True
            scene black with fade
            "At the same time, on the other side of town."
            scene 8sms05 with dissolve
            "..."
            scene 8sms05a with dissolve
            "*Sound of a new message*"
            scene 8sms06 with dissolve
            n "Hm?"
            n "Who the hell is this...?"
            scene 8sms07 with dissolve
            n "[mc]?"
            n "He wants me to help him with something?"
            "*Sound of a new message*"
            n "Oh, that's what it is."
            scene 8sms08 with dissolve
            n "How interesting."
            scene 8sms04 with dissolve
        else:
            mc "{i}I hope Julia agrees to do it.{/i}"
    "*Sound of a new message*"
    mc "{i}A message from Lisa?{/i}"
    ls "\"Hi. Got time to chat?\""
    if lisa_path == True:
        scene 8sms01 with dissolve
        mc "\"Hi. I do. I thought you'd be busy studying?\""
        ls "\"I have some free time.\""
        mc "\"I miss you.\""
        ls "\"I miss you too. I hope to get things sorted out soon so we can see each other again.\""
        mc "\"Take your time. Studying is important.\""
        ls "\"I know. LOL\""
    else:
        mc "\"Yeah. Lying on the couch, looking at the phone.\""
        ls "\"So am I.\""
    scene 8sms02 with dissolve
    ls "\"I was wondering if you've had a whole bunch of strangers follow you on instagram?\""
    mc "\"Maybe a few people, why?\""
    ls "\"Not sure.\""
    ls "\"I think I've got some fans.\""
    mc "\"LOL. You're popular now.\""
    ls "\"I know, right?\""
    scene 8sms03 with dissolve
    ls "\"BTW, I also got a text from one of the guys who started arguing with us before the show.\""
    ls "\"An old friend of Jade's.\""
    mc "\"I hope you told him to fuck off.\""
    ls "\"You bet! I don't want anything to do with him.\""
    mc "\"That's the right thing to do. He's weird.\""
    if lisa_path == True:
        mc "\"Besides, why do you need other guys when you have me?\""
        ls "\"Yup.\""
        ls "\"Wish you were here.\""
        scene 8sms04 with dissolve
        mc "\"Me too.\""
    scene 8sms04 with dissolve
    ls "\"Okay, I'm gonna keep reading books. XOXO\""
    mc "\"See you.\""
    ls "\"Yeah. See you.\""

    if rosa_path == True:
        scene black with fade
        "You kept surfing the internet until you noticed an unread message from Rosa."
        scene 8sms04 with dissolve
        mc "{i}I wonder how come I didn't notice it? Let's see what it says...{/i}"
        r "\"Come to my studio tomorrow at the same time.\""
        mc "{i}Huh? That was very unexpected.{/i}"
        mc "{i}I think I'll answer her.{/i}"
        mc "\"Why?\""
        "..."
        "..."
        mc "{i}There's no answer.{/i}"
        mc "{i}Hmm.{/i}"
        mc "{i}Given how our meeting went today, I have an idea of what she wants.{/i}"
        mc "{i}But do I want that? Especially after that conversation with Selina?{/i}"
        menu:
            "{color=#66FF33}Agree to meet":
                mc "{i}Nothing bad will happen if I check it out.{/i}"
                mc "{i}It's never too late to say no anyway.{/i}"
            "Give it up":
                $ rosa_broke_up = True
                mc "{i}I don't think I want to go to Rosa's studio after everything that happened with Selina today.{/i}"
                mc "{i}It wouldn't be right.{/i}"
    stop music fadeout 3.0
    if nicole_help_jane == True and rosa_path == False:
        scene 3nextday with fade
        $renpy.pause(3, hard=True)
        jump day08_nicole
    if nicole_help_jane == True and rosa_broke_up == True:
        scene 3nextday with fade
        $renpy.pause(3, hard=True)
        jump day08_nicole
    if rosa_path == True and rosa_broke_up == False:
        scene 3nextday with fade
        $renpy.pause(3, hard=True)
        jump day08_rosa_day03
    else:
        jump day09_start


label day08_julia_father:
    scene black with fade
    play music "music/14 - Live Again.ogg"
    "At the same time, on the other side of town."
    scene 8father01 with dissolve
    "Julia walked into a house she hadn't been in in a very long time."
    sis "{i}I need to get this done soon. I do not want to stay in this house for a second longer than I have to.{/i}"
    scene 8father02 with dissolve
    "A moment later, a maid came out to meet her."
    "{color=#BDB76B}Maid{/color}" "Miss Julia, is there anything I can do for you?"
    sis "Where is he?"
    "The maid immediately knew who she meant."
    scene 8father03 with dissolve
    "{color=#BDB76B}Maid{/color}" "Eehh..."
    "{color=#BDB76B}Maid{/color}" "He's in his office."
    "{color=#BDB76B}Maid{/color}" "But, ma'am, he asked not to be disturbed."
    scene 8father02 with dissolve
    "Ignoring her words, Julia moved on."
    sis "It's getting late. You can be done for today."
    "{color=#BDB76B}Maid{/color}" "Yes, ma'am."
    scene 8father04 with dissolve
    "The doors to the office opened and Julia walked in on the owner."
    sis "{i}Yeah, that's where he's hiding.{/i}"
    scene 8father05 with dissolve
    "..."
    scene 8father06 with dissolve
    "The man slowly pulled away from the book and looked at the guest."
    f "Since when is it common in our family to barge into other people's offices?"
    scene 8father07 with dissolve
    sis "And since when is it customary in our family to interfere in other people's lives without permission?"
    f "..."
    scene 8father06 with dissolve
    f "It's late, what are you doing here, Julia?"
    sis "Hmm? Is this how you greet your guests?"
    scene 8father08 with dissolve
    f "I asked a question. Please answer it."
    sis "I'm here to talk. And I don't think this conversation will be pleasant."
    scene 8father09 with dissolve
    sis "Guess who I just saw?"
    f "I have no idea."
    sis "I'll give you a hint, her name is Emma. Does that ring any bells?"
    f "No, I don't remember her."
    scene 8father11 with dissolve
    sis "Oh, come on, that's enough! I know what kind of deal you offered her in exchange for messing with [mc]."
    sis "And don't tell me it's not true."
    scene 8father10 with dissolve
    f "Ugh... Maybe I should fire Donna. She talks too much."
    if nicole_plus == True:
        f "Although if I fire her, you're gonna take her with you, right?"
        scene 8father09 with dissolve
        sis "If you're still mad about me hiring Nicole, I don't care."
        scene 8father10 with dissolve
        f "I'm not mad. On the contrary, Nicole is a very good employee."
        sis "Good? Then why did you fire her?"
        f "Because her moral values are more important to her than her devotion to me or to you. I advise you to remember that."
        scene 8father09 with dissolve
        sis "I don't see anything wrong with that."
        f "And yet it is a problem."
    else:
        sis "That's exactly what you shouldn't be doing.  She's the only one in your crazy company who can still think straight."
    scene 8father10a with dissolve
    f "Okay, as for this little deal, you caught me. I talked to this Emma."
    f "As you can see, it was totally in vain."
    scene 8father09a with dissolve
    sis "Tell me, since when did you start using schoolgirls in your manipulations?"
    sis "That's low, even by your standards."
    scene 8father10a with dissolve
    f "I was very gentle, and I didn't force her to do anything."
    scene 8father09 with dissolve
    sis "Jesus Christ... This is crazy."
    "..."
    scene 8father10 with dissolve
    f "Did you tell [mc] about all this?"
    sis "Not yet."
    f "Don't."
    scene 8father09 with dissolve
    sis "And why shouldn't I?"
    scene 8father10 with dissolve
    f "Because then he'll definitely hate me."
    sis "What difference does it make? You fight with him all the time."
    f "If you tell him, this time things will change completely."
    scene 8father09a with dissolve
    sis "Don't you care?"
    scene 8father10 with dissolve
    f "If I didn't care, I wouldn't lift a finger for him."
    scene 8father09a with dissolve
    sis "So you really believe you're doing this for his own good?"
    "..."
    scene 8father10a with dissolve
    f "What about you? I know you're very much like me, you like to know everything and control everyone."
    f "Are you saying you're okay with what he does?"
    scene 8father09 with dissolve
    sis "It doesn't matter what I want, it matters what he wants. We must respect his decision."
    stop music fadeout 1.0
    scene 8father12 with vpunch
    f "And if he wanted to shoot himself, would you respect his decision too?"
    scene 8father13 with dissolve
    f "*Cough*"
    f "*Cough**Cough**Cough*"
    scene 8father14 with dissolve
    "Julia's formidable expression was replaced by an anxious one."
    sis "Is it getting worse?"
    scene 8father15 with dissolve
    "He took a handful of pills off his desk..."
    scene 8father16 with dissolve
    "...and drank them all with a glass of scotch at once."
    scene 8father17 with dissolve
    f "I'm... *Cough*... I'm fine."
    f "Don't change the subject."
    scene 8father14 with dissolve
    play music "music/8 - Intro Music.ogg"
    sis "Okay..."
    sis "With the suicide example, you're obviously reaching, it's not the same thing."
    scene 8father17 with dissolve
    f "But what he's doing now is almost financial suicide. All I wanted to do was try to keep him out of it."
    sis "Okay, I get it."
    sis "Let's leave it for now."
    scene black with fade
    "Julia sighed wearily and sat down in the chair opposite him."
    sis "Now tell me how you're doing..."
    stop music fadeout 3.0
    jump day08_boat



label day08_nicole:
    scene 7city02 with fade
    "Julia and Jane's office."
    scene 8janeoffice02 with dissolve
    play music "music/15 - Deep Mood.ogg"    
    "You were walking around your sister's office looking for Nicole."
    mc "{i}Looks like the lights are still on in her office. That's good, so she's here.{/i}"
    scene 8janeoffice03 with dissolve
    mc "{i}There she is. Still working.{/i}"
    mc "{i}I'm surprised my father decided to fire her. This girl is a very responsible employee.{/i}"
    mc "{i}Okay, stop standing there. I need to talk to her.{/i}"
    scene 8janeoffice04 with dissolve
    "*Knock, knock, knock.*"
    n "Hm?"
    mc "Hi. Can I come in?"
    scene 8janeoffice05 with dissolve
    "Nicole stretched out on the chair, flexing her tired muscles."
    n "[mc], you've come..."
    mc "Of course."
    mc "Well, did you do as I requested?"
    scene 8janeoffice06 with dissolve
    n "You don't have to worry, the mission is complete."
    mc "{i}Hmm. Despite the late hour, she looks very cheerful.{/i}"
    mc "Wait a minute... What's that in your hand? Is it a lollipop?"
    scene 8janeoffice07 with dissolve
    n "This one?"
    n "Well, when I started working here, I decided to quit smoking. And this is a small substitute for cigarettes."
    n "I think it's working so far."
    mc "You have a very creative mind."
    scene 8janeoffice08 with dissolve
    n "Thank you, but you didn't come here to talk about me."
    mc "Well, one thing doesn't preclude the other."
    n "Yeah, I guess so."
    menu:
        "{color=#66FF33}Ask her how she's doing":
            $ goodpoint += 1
            $ RPn += 1
            scene 8janeoffice10 with dissolve
            mc "Looks like this job is good for you. You look very energetic."
            n "I'm trying to find the pros in everything."
            n "Although this company is not as big as the one I used to work for, it has a very high potential."
            n "Julia and Jane are doing great."
            mc "Glad to hear it."
        "Get to the point":
            $ badpoint += 1
            scene 8janeoffice10 with dissolve
            "..."
    mc "What about Jane, is she still here?"
    scene 8janeoffice09 with dissolve
    n "Yeah, she's got to be here somewhere."
    mc "And Julia?"
    n "No."
    mc "Okay, I see..."
    mc "Well, it was good to see you. And thank you for agreeing to help me."
    n "Well, after all the trouble with your father, it was the least I could do for you."
    mc "And yet, you've helped me out a lot."
    scene 8janeoffice11 with dissolve
    n "Hey, [mc]."
    mc "Yes?"
    "..."
    scene 8janeoffice11a with dissolve
    n "Have a nice time with Jane."
    mc "..."
    stop music fadeout 3.0
    scene black with fade
    "After some thought, you left Nicole's office."
    mc "{i}The way she looked at me at the end of our conversation...{/i}"
    mc "{i}It was... very unusual.{/i}"
    mc "{i}Did she want to tease me? Cheer me up? Or was she just having fun?{/i}"
    mc "{i}Okay, I don't need to get into this right now. I have more important things to do.{/i}"
    jump day08_jane_office

label day08_jane_office:
    if _in_replay:
        $ setReplay()
    if nicole_plus == False:
        scene 7city02 with fade
        "Julia and Jane's office."
    if lisa_path == True:
        $ cheat_point += 5
    scene 8janeoffice12 with dissolve
    play music "music/1 - Atmosphere.ogg"
    "You found Jane in one of the office lounges."
    mc "{i}Looks like she's reading something.{/i}"
    scene 8janeoffice13 with dissolve
    mc "Guess who?"
    "..."
    jn "[mc]."
    jn "And if you want to know how I figured it out, it wasn't hard to guess. You walk like an elephant."
    mc "Hey, actually, I did it on purpose! I didn't want you to spill your coffee on your documents."
    jn "Hmm. Okay, let's pretend I believed you."
    scene 8janeoffice14 with dissolve
    jn "Now tell me, what are you doing here at this late hour?"
    jn "If you're looking for Julia, she's already gone home."
    mc "Actually, I was looking for you."
    scene 8janeoffice15 with dissolve
    jn "Me?"
    mc "Yeah, you."
    jn "But what for?"
    mc "Actually, I wanted to give you a little surprise."
    mc "I hope you're not too busy to look at it."
    scene 8janeoffice16 with dissolve
    "Jane gently held your hand."
    jn "Hmm... I think the job can wait a little bit."
    jn "Show me what your surprise is."
    scene 8janeoffice17 with dissolve
    mc "If you want to see it, follow me."
    jn "I hope it's not too far away."
    mc "No. It's just around the corner."
    scene 8janeoffice18 with dissolve
    jn "In that case, let's go."
    jn "I'd love to see what you've prepared for me."
    scene black with fade
    "A few minutes later."
    scene 8janeoffice19 with dissolve
    jn "Huh? Isn't that a corporate yoga room in front of us?"
    mc "Yeah. But my surprise is waiting for you there."
    jn "It's a bit odd, but I'll trust you."
    mc "You can go straight ahead. I'm sure you'll like it."
    scene 8janeoffice20 with dissolve
    "Jane went inside and looked around."
    jn "Oh, my God. Is this a candlelight dinner?"
    mc "Yes, it is."
    jn "When did you get all this ready?"
    mc "Well, I have my methods."
    jn "Mm-hmm... What a mysterious answer."
    scene 8janeoffice22 with dissolve
    jn "And yet, this is the second romantic evening you're giving me."
    jn "You seem to take us seriously."
    mc "You can call me a hardheaded idiot, but I'll arrange a thousand more of these nights for you."
    scene 8janeoffice22a with dissolve
    jn "You're not an idiot at all... I would even call you a romantic."
    jn "Okay... It's a... It's really nice. Thank you, [mc]."
    mc "You're welcome. Now have a seat."
    scene 8janeoffice23 with dissolve
    jn "Do you mind if I take off my shoes?"
    jn "It won't be very comfortable here in heels."
    mc "Oh, yeah, of course."
    scene 8janeoffice24 with dissolve
    "..."
    jn "Uhhh... Yeah, that's much better."
    scene 8janeoffice21 with dissolve
    jn "I see you're well prepared. Good food and a bottle of red wine..."
    mc "Classic."
    jn "Yeah, a win-win combination."
    scene 8janeoffice25 with dissolve
    "Jane sat on a little pillow by the table and looked at you with interest."
    jn "How did you even come up with the idea of doing all this?"
    mc "It wasn't hard to come up with that."
    mc "You spend so much time at work, I've decided to combine business with pleasure."
    mc "You need to relax more often."
    scene 8janeoffice26 with dissolve
    "Jane picked up some cream on her finger from the plate."
    scene 8janeoffice27 with dissolve
    jn "Relax more often?"
    scene 8janeoffice28 with dissolve
    "..."
    scene 8janeoffice28a with dissolve
    jn "Maybe you're right..."
    scene 8janeoffice29 with dissolve
    jn "Then how about we relax a little here and now? Right on this very floor."
    mc "What about dinner?"
    jn "First you and I will have some fun, and then we can have dinner. No objections allowed."
    mc "{i}I like the way she thinks!{/i}"
    scene 8janeoffice30 with dissolve
    jn "Now, come here. You deserve it."
    mc "{i}Yes, ma'am!{/i}"
    stop music fadeout 2.0
    scene 8janeoffice31 with dissolve
    jn "Mmm..."
    play music "music/15 - Deep Mood.ogg"
    mc "{i}Oohhhh... It seems she is very determined.{/i}"
    scene 8janeoffice32 with dissolve
    "Jane's hand slipped up your chest."
    scene 8janeoffice32a with dissolve
    jn "Let's get rid of this."
    scene 8janeoffice33 with dissolve
    "Before you know it, Jane was already straddling you with a happy smile."
    jn "Your whole body is so muscular... And it feels very nice."
    mc "I wouldn't mind seeing more of your body, either."
    scene 8janeoffice34 with dissolve
    jn "Mmmm... I think that can be arranged."
    jn "I hope you're watching carefully."
    mc "You can be sure of that."
    scene 8janeoffice35 with dissolve
    jn "Now let's unbutton some buttons..."
    scene 8janeoffice36 with dissolve
    mc "{i}Oh, yeah, I love it!{/i}"
    scene 8janeoffice37 with dissolve
    mc "{i}Such a gorgeous woman should drive men crazy. I still don't understand why she's been alone for so long.{/i}"
    mc "{i}But now I'm not letting her go...{/i}"
    scene 8janeoffice38 with dissolve
    jn "So, do you like what you see?"
    mc "Oh yeah, you are driving me crazy!"
    scene 8janeoffice39 with dissolve
    "With one sudden move, you pushed yourself up off the floor and grabbed Jane by the waist."
    jn "Aaahh!"
    jn "[mc], don't be so impatient..."
    scene 8janeoffice40 with dissolve
    mc "It's hard to stay calm when you've got such a gorgeous girl on top of you."
    jn "Mmm-hmm... You're such a flatterer!"
    scene 8janeoffice41 with dissolve
    mc "{i}Now let's get rid of this.{/i}"
    scene 8janeoffice42 with dissolve
    "Jane's bra started slowly slipping off her shoulders."
    scene 8janeoffice43 with dissolve
    jn "Is that better?"
    mc "Much better!"
    jn "Okay... And now let's start the next step."
    scene 8janeoffice44 with dissolve
    "With one swift move, Jane unzipped your pants and freed your dick."
    jn "Yes... There he is..."
    jn "He's gotten so hard so fast."
    scene 8janeoffice45 with dissolve
    jn "Now let's taste him."
    mc "{i}Oh my God, her aroused voice gives me the goosebumps.{/i}"
    scene 8janeoffice46 with dissolve
    mc "Oohh... yes... keep going."
    jn "Mmm... tastes so good."
    scene 8janeoffice47 with dissolve
    jn "Uh... Is it me or is he getting bigger?"
    jn "Then I should get serious..."
    scene 8janeoffice48 with dissolve
    "..."
    show anim50
    "Jane took your dick in her mouth and started sucking it."
    jn "Mmhhhhh.... Nnnggghh.... Nnngghhh..."
    mc "{i}Oohhhhhh... She sucks so hard. It feels amazing.{/i}"
    mc "Oh, yeah, baby! Suck it, don't stop!"
    jn "Mmhhhhh... Nnnggghh... Nnngghhh!"
    scene 8janeoffice49 with dissolve
    "..."
    jn "Uh... All right, enough games."
    scene 8janeoffice50 with dissolve
    "Unexpectedly, Jane got back on her feet."
    mc "What are you doing?"
    scene 8janeoffice51 with dissolve
    jn "It's time for us to both have some fun."
    mc "{i}Oh, I see. She decided to undress completely.{/i}"
    scene 8janeoffice52 with dissolve
    mc "Nice underwear!"
    jn "Ha! Shut up! What's underneath it is what's important."
    scene 8janeoffice53 with dissolve
    mc "{i}It's hard to argue with that.{/i}"
    mc "{i}No more preludes or distractions.{/i}"
    scene 8janeoffice54 with dissolve
    jn "[mc]."
    jn "It's time to have some real rough sex."
    scene 8janeoffice55 with dissolve
    "You stepped up to Jane and immediately started caressing her."
    jn "Ahh!"
    scene 8janeoffice56 with dissolve
    mc "{i}My head's barely thinking straight. I just obey my instincts.{/i}"
    mc "{i}Time to fuck her.{/i}"
    scene 8janeoffice57 with dissolve
    mc "I want you so badly right now. Do you want me?"
    jn "Yeah, I want you."
    jn "Now stop teasing! Stick your dick in me."
    mc "{i}I love the way she asks me to do that.{/i}"
    scene 8janeoffice58 with dissolve
    "You heard a quiet groan coming from Jane."
    jn "Aaahhh..."
    mc "{i}Her pussy is so tight.{/i}"
    scene 8janeoffice59 with dissolve
    jn "It's so nice to have you inside me..."
    show anim44
    mc "{i}It's time to start moving.{/i}"
    jn "Yes! Take me, [mc]..."
    mc "{i}How nice it is when she moans like that...{/i}"
    jn "Don't stop! Please fuck me!"
    scene 8janeoffice60 with dissolve
    "You grabbed Jane's breasts and you started moving even faster."
    mc "Aaahhhhh... Aaahhh... Yeah, baby..."
    scene 8janeoffice61 with dissolve
    jn "Oh [mc]! AAH!"
    scene 8janeoffice62 with dissolve
    jn "Haaah... Haaah... [mc], I want to be on top now."
    mc "{i}Why not?{/i}"
    scene 8janeoffice63 with dissolve
    jn "Yeah... That's it."
    jn "Just lie there and enjoy it."
    scene 8janeoffice64 with dissolve
    "..."
    scene 8janeoffice65 with dissolve
    jn "AAH! AAH! Mmm...."
    mc "{i}Is it me or is this her favorite position?{/i}"
    show anim45
    jn "Aaahhhh... Aaaahhh... Aaahhh..."
    mc "{i}What a magnificent view.{/i}"
    scene 8janeoffice67 with dissolve
    jn "Aaahhhhh... Aaahhh... Take my hand."
    jn "Yeah, um... There you go..."
    show anim46
    jn "Now give me your other hand..."
    jn "Aaahhhh... Aaaahhh... Aaahhh..."
    stop sound fadeout 1.0
    jn "Aahhh! YES! I'm coming!"
    scene 8janeoffice66 with flash
    jn "YES!!!"
    scene 8janeoffice66 with flash
    "..."
    scene 8janeoffice69 with dissolve
    jn "Oh my God, come here, let me kiss you..."
    mc "Mmmm..."
    mc "I think I'm gonna come soon, too."
    jn "Okay."
    scene 8janeoffice70 with dissolve
    mc "Yeah.. A little more! Don't stop!"
    jn "Haaahhhhh... Huh haahhhh... Hhhaaahhh..."
    scene 8janeoffice71 with dissolve
    mc "Aahhhh!"
    scene 8janeoffice71 with flash
    ".."
    stop music fadeout 2.0
    scene 8janeoffice72 with dissolve
    "*The sound of heavy breathing*"
    jn "I see you've enjoyed yourself."
    mc "Huh. As if you didn't like it!"
    jn "Fair enough."

    $ renpy.end_replay()
    if not persistent.day08jane:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day08jane = True

    scene black with fade
    play music "music/1 - Atmosphere.ogg"
    "Soon you cleaned yourself up and opened the bottle of wine."
    scene 8janeoffice73 with dissolve
    mc "What do you think? Did you like my surprise?"
    jn "It was, uh... It was..."
    jn "It's hard for me to describe how good it was."
    mc "I'm glad to hear that."
    scene 8janeoffice74 with dissolve
    jn "Tell me, [mc], what are you planning on doing next?"
    mc "What are you talking about?"
    jn "I'm talking about whether you want to take our relationship to the next level."
    jn "Do you really want more than we have now?"
    menu:
        "{color=#66FF33}You want more":
            $ jane_date_offer = True
            scene 8janeoffice75 with dissolve
            mc "Yeah, I want something more between us."
            "..."
            jn "Okay... I hear you."
            mc "What are you gonna say to that?"
            jn "It's a big decision. I hope you don't mind if I think it over a little bit."
            mc "{i}Hmm... Looks like her business habits are coming out.{/i}"
            mc "Of course you can think about it."
            mc "Just not too long."
            jn "Haha. Whatever you say."
        "You're okay with this":
            scene 8janeoffice75 with dissolve
            mc "It's hard to tell. When we sit like this, I don't want to change anything."
            jn "I understand... It's really nice."
    mc "Maybe some more wine?"
    jn "I'd love some!"
    scene black with fade
    "Some time later."
    scene 8janeoffice76 with dissolve
    jn "Well, that was a great night. But now it's time to say goodbye."
    mc "Yeah, it was nice seeing you."
    jn "Believe me, it's mutual."
    if jane_date_offer == True:
        scene 8janeoffice77 with dissolve
        jn "And about your offer..."
        jn "I'll call you as soon as I make a decision."
        mc "It's a deal."
    jn "I'll see you then."
    mc "Yes, see you."
    stop music fadeout 3.0
    jump day09_start


label day08_rosa_day03:
    if _in_replay:
        $ setReplay()
    if lisa_path == True:
        $ cheat_point += 5
    scene black with fade
    play music "music/9 - You Can Make the Sound.ogg"
    "You were standing in front of the door to Rosa's studio."
    "Even though this is the third time you've been here this week, you were really late this time."
    mc "{i}I'm still not sure I did the right thing coming here after talking to Selina.{/i}"
    mc "{i}Oh well... I guess I'm just an idiot whose always trying to create problems for himself.{/i}"
    mc "{i}But the decision has already been made and it's too late to retreat.{/i}"
    "*The doorbell rings*"
    scene 8rosasex01 with dissolve
    r "Oh... [mc]. And I thought you wouldn't come."
    mc "Well, I was a little late in traffic, but-"
    stop music fadeout 3.0
    scene 8rosasex02 with dissolve
    "You didn't have time to finish the sentence before Rosa threw herself at you with a kiss."
    mc "{i}What the hell?!{/i}"
    scene 8rosasex03 with dissolve
    mc "{i}Doesn't matter, though.{/i}"
    scene 8rosasex04 with dissolve
    play music "music/6 - Positive Mood.ogg"
    mc "Wow... that was very unexpected."
    r "Was it?"
    r "We both know why you came here today."
    mc "Well, yeah, but..."
    r "Shhhhh... I don't want to waste the little time we have."
    scene 8rosasex04a with dissolve
    "Rosa lowered her eyes."
    scene 8rosasex05 with dissolve
    mc "{i}Wow! She's pretty fast.{/i}"
    r "Now we're gonna wake your little friend up."
    scene 8rosasex05a with dissolve
    "You swallowed a lump in your throat."
    mc "{i}This view makes my head go round and round.{/i}"
    scene 8rosasex06 with dissolve
    r "Let's not stand in the doorway, and go into the studio."
    mc "Yes... sure..."
    mc "{i}Damn it, I gotta get a grip on myself! Because I'm acting like a complete idiot.{/i}"
    scene 8rosasex07 with dissolve
    r "Oh, yeah! I forgot to ask you something. You didn't tell Selina you were coming here today, did you?"
    mc "No, I didn't."
    r "Well, that's great. I don't want to worry her again..."
    scene 8rosasex08 with dissolve
    "Rosa took your hand and took you with her."
    mc "Are you sure this is a good idea?"
    scene 8rosasex09 with dissolve
    r "To tell you the truth, I don't fully understand your relationship with my daughter. But you don't have to worry about me. I'm not getting between you and her."
    mc "{i}Sounds too good to be true.{/i}"
    mc "{i}Although Selina told me that Rosa was a pretty eccentric person. Maybe she was right after all.{/i}"
    mc "Well, if that's the case, I like it."
    scene 8rosasex10 with dissolve
    r "Then I'll take it that we have a deal. It will remain a little secret between you and me, okay?"
    mc "That's fine with me."
    r "Well, that's great!"
    scene 8rosasex21 with dissolve
    "For a fraction of a second, you thought Rosa was gonna rip all your clothes off. But things started to go a little differently."
    scene 8rosasex11 with dissolve
    r "Now tell me, what do you like better, my breasts or my ass?"
    mc "{i}Wow... Looks like she really doesn't like wasting her time.{/i}"
    menu:
        "You like breasts":
            mc "I like your breasts."
            r "Mm-hmm... What an interesting choice..."
            scene 8rosasex12 with dissolve
            r "Then I'd be happy to show them to you."
            mc "{i}It's getting more and more interesting every second.{/i}"
            scene 8rosasex13 with dissolve
            r "Well, what do you think? Do you like what you see?"
            mc "They're gorgeous."
            scene 8rosasex14 with dissolve
            r "Hehe. Don't be shy, you can touch them."
            mc "{i}I'd love to!{/i}"
            scene 8rosasex15 with dissolve
            "You reached out and grabbed Rosa's breasts."
            r "Aahh..."
            mc "{i}God, she feels so good.{/i}"
            scene 8rosasex16 with dissolve
            r "Mmm... Even though we found out you like women's breasts, I think you'd like to see the whole thing?"
            mc "If a girl offers me that, it would be rude to refuse."
            r "Haha. I like that answer."

        "You like ass":
            mc "I like your ass."
            r "Mm-hmm... What an interesting choice..."
            r "Then I'd be happy to show it to you."
            mc "{i}It's getting more and more interesting every second.{/i}"
            scene 8rosasex17 with dissolve
            "Rosa turned her back to you..."
            mc "{i}It's a good start.{/i}"
            scene 8rosasex18 with dissolve
            "And then she pulled her dress up, giving you a great view of her beautiful ass."
            mc "{i}Oh! The look of those panties and stockings... It's so sexy!{/i}"
            r "Well, what do you think? Do you like what you see?"
            mc "That's just awesome."
            r "Hehe. Don't be shy, you can come closer and touch it."
            mc "{i}I'd love to!{/i}"
            scene 8rosasex19 with dissolve
            "You walked up and ran your hand over Rosa's round ass."
            r "Aaahh..."
            mc "{i}God, that ass is almost perfect.{/i}"
            scene 8rosasex20 with dissolve
            r "Mmm... Even though we found out you like women's asses, I think you'd like to see the whole thing?"
            mc "If a girl offers me that, it's would be rude to refuse."
            r "Haha. I like that answer."

    scene 8rosasex22 with dissolve
    "Rosa started slowly taking her clothes off."
    r "Watch carefully, [mc]."
    mc "Believe me, I'm watching very carefully."
    scene 8rosasex23 with dissolve
    "..."
    scene 8rosasex23a with dissolve
    r "Mm-hmm... How exciting it is to stand naked in front of a handsome man."
    mc "Not more exciting than standing in front of a beautiful naked woman."
    r "Hehe. Yes, you're probably right."
    scene 8rosasex24 with dissolve
    r "Tell me, do you like the look of a naked woman's body?"
    mc "What kind of a question is that? Of course I like it."
    r "I always liked it, too. Not only female, but also male."
    scene 8rosasex26 with dissolve
    r "The naked body always excites our emotions. Causes a variety of desires..."
    mc "{i}Well, what she's doing right now is definitely causes me desire.{/i}"
    r "That's what I'm trying to do as an artist in my paintings."
    scene 8rosasex25 with dissolve
    r "I often try to reflect emotions of passion and lust in my work. They seem to be the most interesting and exciting to me."
    r "And over time, I realized that the best way to reflect them was through personal experience..."
    mc "I think I understand you."
    scene 8rosasex27 with dissolve
    r "You do? That's great!"
    r "Then how about we forget everything else and give in to this lust?"
    mc "{i}Fuck, I don't know what the hell she's got in her head, but that offer is very tempting.{/i}"
    scene 8rosasex28 with dissolve
    "Rosa came closer and put her hand on your shoulder."
    r "Now be a good boy and let me take care of you."
    scene 8rosasex29 with dissolve
    r "Just like this..."
    scene 8rosasex30 with dissolve
    r "Mmmm..."
    mc "{i}Her lips are so soft.{/i}"
    scene 8rosasex31 with dissolve
    "You grabbed Rosa's waist..."
    scene 8rosasex32 with dissolve
    "...and then your hands moved smoothly onto her ass."
    "She was rhythmically rubbing her knee against your crotch."
    stop music fadeout 2.0
    scene 8rosasex33 with dissolve
    "Suddenly, Rosa knelt down on her knees."
    play music "music/Maxim Nick - Smooth Light.ogg"
    scene 8rosasex34 with dissolve
    r "I think you're ready."
    mc "I've been ready for a long time."
    r "I like your spirit."
    scene 8rosasex35 with dissolve
    r "Now let's get your pants down and see what's underneath."
    scene 8rosasex36 with dissolve
    r "Ohhh.. Yes..."
    scene 8rosasex36a with dissolve
    r "That's the kind of big dick I've been waiting for."
    scene 8rosasex37 with dissolve
    r "I hope you have a lot of energy today because I'm not letting you go easily."
    scene 8rosasex38 with dissolve
    "..."
    show anim52
    r "You like it when I do that?"
    mc "Oh, yeah... Keep going..."
    r "You can have fun, but remember, it's just a warm-up."
    mc "Oohhhh... If it's just a warm-up, can we skip straight ahead?"
    mc "I want you to put it in your mouth."
    r "Mm-hmm... I can arrange that."
    scene 8rosasex39 with dissolve
    "Rosa touched her lips to the tip of your dick and kissed it."
    scene 8rosasex40 with dissolve
    r "And now I'm gonna caress him with my tongue."
    scene 8rosasex41 with dissolve
    r "Does it feel good, baby?"
    mc "Oohhh... Yes, it's very good."
    scene 8rosasex42 with dissolve
    "Out of the corner of your eye, you noticed her gorgeous body again."
    mc "{i}I still can't believe this is happening.{/i}"
    scene 8rosasex43 with dissolve
    mc "Ohhhh... Yeah, take it in your mouth."
    scene 8rosasex44 with dissolve
    "..."
    show anim53
    r "Mmhhhh... Mmmhhh... Mmmhhh..."
    mc "Oohhhh... Yeah, suck it, baby... Suck it harder!"
    mc "{i}That's so awesome!{/i}"
    r "Mmhhhh... Mmmhhh... Mmmhhh..."
    scene 8rosasex45 with dissolve
    "..."
    scene 8rosasex46 with vpunch
    mc "{i}Oohhhh... She is taking my dick so deep!{/i}"
    scene 8rosasex45 with dissolve
    "..."
    scene 8rosasex46 with vpunch
    "..."
    scene 8rosasex47 with dissolve
    mc "{i}Nobody's ever sucked me so hard before in my life.{/i}"
    mc "{i}I feel like I'm about to melt.{/i}"
    scene 8rosasex48 with dissolve
    "Suddenly, Rosa stopped sucking and got up."
    r "Uh... What a strong hard-on you have. I can't wait to feel it inside me."
    mc "{i}And I'd like that to happen!{/i}"
    scene 8rosasex51 with dissolve
    "All this time, Rosa has continued jerking you off."
    scene 8rosasex51a with dissolve
    "..."
    scene 8rosasex51 with dissolve
    "..."
    scene 8rosasex49 with dissolve
    "You touched her face with your hand."
    mc "{i}She's so sexy.{/i}"
    scene 8rosasex50 with dissolve
    "..."
    scene 8rosasex50a with dissolve
    "You stuck your finger in her mouth, and she started sucking it right away."
    scene 8rosasex51 with dissolve
    mc "{i}Oohhhh... I'm already at the limit.{/i}"
    scene 8rosasex51a with dissolve
    mc "{i}A little more and I'll cum!{/i}"
    scene 8rosasex52 with flash
    mc "Aaaahhh!"
    scene 8rosasex52 with flash
    "..."
    scene 8rosasex54 with dissolve
    r "Very, very good, [mc]."
    r "You lasted a lot longer than I thought."
    mc "If that's a compliment, thank you..."
    r "Trust me, that's a compliment."
    r "Okay, I'm sure you still have a lot of energy left... Let's start the second round."
    stop music fadeout 1.0
    scene 8rosasex53a with dissolve
    "*Ringtone*"
    play music "music/8 - Intro Music.ogg"
    scene 8rosasex55a with dissolve
    r "What the hell?"
    r "Damn it, not now!"
    mc "{i}What's going on?{/i}"
    scene 8rosasex56 with dissolve
    r "I'm sorry, I have to take this. This is very important."
    mc "Okay."
    scene 8rosasex57 with dissolve
    r "Hello."
    "..."
    r "Yes..."
    r "No, you can't come to me now, I'm busy."
    mc "{i}I don't think this is a very pleasant conversation.{/i}"
    scene 8rosasex58 with dissolve
    r "I don't care if you're almost here already. I told you I was busy right now!"
    "..."
    r "No... No! No!"
    "..."
    scene 8rosasex59 with dissolve
    r "Goddamn it!"
    mc "{i}I can understand from this short conversation that we aren't going to be having sex tonight.{/i}"
    "..."
    scene 8rosasex60 with dissolve
    r "I'm sorry, but I think we're gonna have to finish up for today."
    mc "{i}Fuck, I knew it!{/i}"
    r "My ex-husband will be here soon. There will be some problems with the divorce that need to be solved."
    mc "I understand that."
    mc "{i}Oh, if I'd just come here earlier today...{/i}"
    
    $ renpy.end_replay()
    if not persistent.day08rosa:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day08rosa = True

    scene black with fade
    "A few minutes later."
    scene 8rosasex61 with dissolve
    r "I'm sorry again about what happened."
    mc "Yes... Too bad about that."
    scene 8rosasex62 with dissolve
    r "You know what... Come by our house next week, and I'll try to make it up to you."
    r "Just make sure Selina's not going to be home."
    scene 8rosasex63 with dissolve
    r "I'll show you some of my most candid paintings."
    r "And maybe you and I can come up with an idea for another one of them..."
    mc "Damn, I can't wait!"
    stop music fadeout 1.0
    scene 8rosasex64 with vpunch
    "*Doorbell*"
    r "Eh... Looks like my ex-husband is here."
    play music "music/13 - Hope is Still Living.ogg"
    scene 8rosasex65 with dissolve
    "Rosa opened the front door and a middle-aged man entered the studio."
    mc "{i}So this is Rosa's ex-husband and Selina's father? Somehow he is not very impressive.{/i}"
    mc "{i}I guess he's rich, because otherwise I just don't know how he could have picked up a gorgeous woman like Rosa.{/i}"
    "{color=#66CDAA}Man{/color}" "What are you doing here that you can't let me in?"
    r "None of your business."
    r "Since you're here, let's get this over with."
    scene 8rosasex66 with dissolve
    "{color=#66CDAA}Man{/color}" "Hmm. Who's that? One of your useless students?"
    "{color=#66CDAA}Man{/color}" "Tell him to leave us alone."
    mc "{i}There's something wrong with him if he's acting like an asshole with strangers.{/i}"
    scene 8rosasex67 with dissolve
    r "Oh, my God, shut up already!"
    r "[mc], thank you for coming today, but you can go home. I think this is going to take a while."
    mc "Are you sure about this?"
    r "Yeah, I'm sure it'll be okay."
    mc "{i}Well, if that's what she wants, I won't argue.{/i}"
    scene 8rosasex68 with dissolve
    "Leaving Rosa's studio, you heard the two divorcees fighting behind you."
    mc "{i}Yeah, well... what a night.{/i}"
    stop music fadeout 3.0
    if nicole_help_jane == True:
        scene black with fade
        "Some time later."
        jump day08_nicole
    if nicole_help_jane == False and RPjn >= 14:
        scene black with fade
        "Some time later."
        jump day08_jane_office
    else:
        jump day09_start


label day08_jacob:
    if _in_replay:
        $ setReplay()
    scene black with fade
    "At the same time, on the other side of town."
    scene 8jacob01 with dissolve
    "..."
    play music "music/3 - Dream With U.ogg"
    scene 8jacob01a with dissolve
    "*Girls laughing*"
    scene 8jacob02 with dissolve
    j "We're finally here!"
    "{color=#DB7093}Aki{/color}" "You've been carrying me for so long... You're so strong, Jacob!"
    "{color=#FFD700}Mika{/color}" "Get off him, Aki, or he'll get tired."
    j "Hehe, don't worry, I've got enough energy for a whole stadium of fans."
    j "Now let's go ahead!"
    scene 8jacob03 with dissolve
    "{color=#DB7093}Aki{/color}" "Uh, haha!!! We look like a real plane now!"
    j "See, I told you! It's nothing to me."
    "{color=#FFD700}Mika{/color}" "..."
    scene 8jacob04 with dissolve
    j "Attention! Now, a sharp landing!"
    "{color=#DB7093}Aki{/color}" "Aaaaah!!!! We're all gonna die!"
    j "Not on my watch! Haha."
    scene 8jacob05 with dissolve
    "Contrary to Aki's expectation, Jacob carefully put her on the bed and took a step back."
    "{color=#DB7093}Aki{/color}" "Wow! I think I was saved by the skill of the captain of this plane."
    "{color=#DB7093}Aki{/color}" "What does the hero want in exchange for my salvation?"
    j "Mm-hmm... Let me think about it."
    stop music fadeout 10.0
    scene 8jacob06 with dissolve
    "{color=#FFD700}Mika{/color}" "Hey! Since you've forgotten all about me, I'll remind you myself!"
    j "Wow..."
    "{color=#DB7093}Aki{/color}" "That's not fair, Mika!"
    "{color=#FFD700}Mika{/color}" "Who said anything about fair?"
    scene 8jacob07 with dissolve
    "{color=#DB7093}Aki{/color}" "Jacob, look at me."
    "{color=#DB7093}Aki{/color}" "You and I could play a new game, and it would be much more interesting than the previous one."
    scene 8jacob08 with dissolve
    j "Girls, girls! You don't have to fight over me."
    j "I give you my word as a drummer, I'll take care of both of you."
    scene 8jacob09 with dissolve
    "{color=#FFD700}Mika{/color}" "Mm-hmm... He's so confident. I like it."
    "{color=#DB7093}Aki{/color}" "I think he'll soon have a chance to prove himself. Hehe."
    scene 8jacob10 with dissolve
    "{color=#DB7093}Aki{/color}" "So, Jacob..."
    "{color=#FFD700}Mika{/color}" "...show us what you're worth."
    j "Heh. Then what are you waiting for, come to me!"
    scene 8jacob11 with dissolve
    j "Why don't we start by warming up a little bit?"
    scene 8jacob12 with dissolve
    "{color=#DB7093}Aki{/color}" "I think I know what you mean."
    "{color=#FFD700}Mika{/color}" "Take his pants off, Aki!"
    scene black with fade
    "..."
    scene 8jacob13 with dissolve
    "{color=#DB7093}Aki{/color}" "Mmm... What a concentrated face he has, he seems to be serious."
    "{color=#FFD700}Mika{/color}" "Now we're gonna see how long it takes."
    scene 8jacob14 with dissolve
    j "Less talk, ladies, and more action."
    "{color=#FFD700}Mika{/color}" "Did you hear that, Aki? Let's get to work!"
    scene 8jacob15 with dissolve
    "{color=#DB7093}Aki{/color}" "Nnnggghh... Unnnnhhh.... Mnnnghhh...."
    "{color=#FFD700}Mika{/color}" "You like the way she sucks your dick?"
    j "Aahhhhhh... Yes."
    "{color=#FFD700}Mika{/color}" "Come on, swallow deeper, Aki!"
    scene black with fade
    "..."
    scene 8jacob16 with dissolve
    "{color=#DB7093}Aki{/color}" "Why did you put us in this position?"
    "{color=#FFD700}Mika{/color}" "Aaahhh... Shut up! Let him do what he wants..."
    scene 8jacob17 with dissolve
    j "Your asses are amazing, girls."
    j "We're gonna test them a little bit now."
    scene black with fade
    "..."
    scene 8jacob17a with dissolve
    j "So which one of you wants to be first?"
    "{color=#DB7093}Aki{/color}" "Me! I want this!"
    "{color=#FFD700}Mika{/color}" "Damn you, Aki! I wanted to be the first..."
    scene black with fade
    "..."
    scene 8jacob18 with dissolve
    "{color=#DB7093}Aki{/color}" "Aaahhh... Aaahhh... Aahhhh!"
    "{color=#DB7093}Aki{/color}" "Oh, my God, Mika, this is so cool! His dick is amazing!"
    "{color=#FFD700}Mika{/color}" "I hope you're really enjoying this..."
    scene 8jacob21 with dissolve
    "{color=#FFD700}Mika{/color}" "Come on, Jacob! Show that bitch everything you got!"
    "{color=#FFD700}Mika{/color}" "Let her beg you to fuck her..."
    j "Oohhhh... You guys are just on fire!"
    scene 8jacob22 with dissolve
    "{color=#DB7093}Aki{/color}" "I can't do this anymore! I am at the limit!"
    "{color=#FFD700}Mika{/color}" "Don't listen to her, Jacob. She's really into it."
    "{color=#FFD700}Mika{/color}" "Just keep going!"
    scene black with fade
    "..."
    scene 8jacob19 with dissolve
    "{color=#FFD700}Mika{/color}" "Aaahhhh! Aaahhhhh! Aaahhhhh!!!!"
    "{color=#DB7093}Aki{/color}" "Mm-hmm... Well, Mika, how does his dick feel inside you? Do you like it?!"
    scene 8jacob20 with dissolve
    "{color=#FFD700}Mika{/color}" "Haahhhh! Haahhhh! Shut up!"
    "{color=#DB7093}Aki{/color}" "..."
    "{color=#FFD700}Mika{/color}" "Just, uh... Just don't stop, Jacob!"
    scene black with fade
    j "Oh, uh... I think I'm gonna cum now..."
    scene 8jacob23 with dissolve
    "{color=#DB7093}Aki{/color}" "Now we're gonna help you... Cum on this arrogant dark-haired bitch!"
    "{color=#FFD700}Mika{/color}" "Aaahhh... Yes... Come on, Jacob... You can cum on me."
    scene 8jacob24 with dissolve
    j "Aaahhhh! I'm gonna..."
    "{color=#DB7093}Aki{/color}" "Come on, come on!"
    scene 8jacob25 with flash
    j "AHHH! Yeeess!!!"
    scene 8jacob25 with flash
    "..."
    scene 8jacob26 with dissolve
    "*Heavy breathing*"
    j "Ahhh..."
    "{color=#FFD700}Mika{/color}" "Mm-hmm... Not bad."
    "{color=#DB7093}Aki{/color}" "Uh-huh."
    "{color=#DB7093}Aki{/color}" "But you do realize that this is just the beginning, right?"
    "{color=#DB7093}Aki{/color}" "Everybody's got two minutes off, and then it's my turn!"
    "{color=#FFD700}Mika{/color}" "Heh-heh. Judging by her playful tone, we'll be fucking all night."
    j "{i}Yeah... I hope I have enough strength for both of them.{/i}"

    $ renpy.end_replay()
    if not persistent.day08jacob:
        $ renpy.notify(['SAHNE KILIDI ACILDI'])
        $ persistent.day08jacob = True

    jump day08_morning

label day08_morning:
    play music "music/3 - Dream With U.ogg"
    scene black with fade
    "The next morning."
    scene 8morning01 with dissolve
    ls "Uhhh... You've been sleeping for so long. Jade and I were about to wake you up."
    mc "Um... yes... I guess I was a little exhausted after yesterday."
    ls "It's okay."
    mc "{i}Hell, they look very fresh. No signs of a hangover.{/i}"
    ls "I think it's time we went home."
    mc "Yeah, I get it."
    scene 8morning02 with dissolve
    ls "How about we stop by our rehearsal room today and discuss yesterday's gig and future plans?"
    mc "To tell you the truth, I was going to suggest that myself."
    jd "I'm in."
    ls "That's great!"
    mc "Then I'll tell Jacob about it."
    mc "And I guess that's it."
    scene 8morning01 with dissolve
    jd "See you later, [mc]."
    if lisa_path == True:
        scene 8morning03 with dissolve
        "Lisa came up to you and kissed you goodbye."
        ls "It was a magical night... Thank you for everything."
    else:
        ls "Yeah, I'll see you later..."
    stop music fadeout 3.0
    scene black with dissolve
    "Some time later, you all went home."
    if jane_path == True and RPjn >= 8 and jane_massage == True:
        jump day08_jane_and_julia
    else:
        jump day08_meeting


label day08_meeting:
    play music "music/9 - You Can Make the Sound.ogg"
    scene black with fade
    "A few hours later in the rehearsal room."
    scene 8rroom01 with dissolve
    "When you walked into the room, you noticed Lisa and Jade were already here."
    mc "{i}Lisa's looking at something on the picture board, and Jade's glued to her phone. Only Jacob is missing here.{/i}"
    mc "{i}I sent him a text about the meeting. He's probably just late.{/i}"
    if lisa_path == True:
        scene 8rroom02 with dissolve
    else:
        scene 8rroom02a with dissolve
    mc "Hello again!"
    jd "Hey, [mc]."
    scene 8rroom03 with dissolve
    "Lisa came closer to you and hugged you tight."
    ls "Hi [mc]."
    mc "{i}Looks like she's still in a good mood.{/i}"
    mc "{i}I even envy her a little bit.{/i}"
    scene 8rroom04 with dissolve
    jd "So, [mc], did you call Jacob? Is he coming?"
    mc "Yeah, I sent him a message. He replied that he would be on time."
    jd "So he's just late..."
    scene 8rroom05 with dissolve
    ls "Looks like someone had a really good time last night."
    mc "{i}Ohhhh... I hope he has a good excuse.{/i}"
    mc "Yeah, we're gonna have to wait for him for a while."
    scene black with fade
    "Some time later."
    scene 8rroom06 with dissolve
    "*Front door creak*"
    j "Hey, everybody! Sorry I'm late."
    mc "Wow, you finally decided to show up."
    j "Heh. Don't be in a hurry to fight! I have some very interesting news for you."
    mc "{i}How well he's deflected the subject of the conversation.{/i}"
    ls "What's the news?"
    j "There's no point in explaining, it's better if you see for yourself."
    scene 8rroom07 with dissolve
    "Jacob put you all in front of a laptop and put on a video of your yesterday's gig."
    ls "Wow! For some reason, I didn't even think we could get recorded."
    jd "Hmm... Picture quality is very good. The sound is also good."
    mc "More importantly, this video has several thousand views."
    ls "Ha! He's right!"
    jd "Hey, let's watch the video first."
    scene black with fade
    "A few minutes later."
    scene 8rroom08 with dissolve
    j "Well, what do you think? Have you read the comments already?"
    scene 8rroom10 with dissolve
    jd "There aren't many of them, but most of the comments are praising us."
    jd "I think that's a good sign."
    scene 8rroom09a with dissolve
    ls "Yeah, but some people are very critical."
    ls "Even though it was just our first live performance..."
    scene 8rroom08 with dissolve
    j "Pfft! Don't worry, it's the internet! There are always dissatisfied people on there."
    j "They're ready to compare any newcomers to the legends of the music scene. It's not surprising at all that newcomers can't compete in such a comparison."
    j "Better to look at the positive comments!"
    scene 8rroom09a with dissolve
    ls "Yeah, well, you're right... But for some reason, it's the negative ones that I can't get out of my head."
    scene 8rroom07a with dissolve
    mc "I think you're exaggerating. This is a great first reaction to our band."
    mc "Believe me, it's only gonna get better."
    scene 8rroom09 with dissolve
    ls "You really think so?"
    mc "I'm sure of it."
    ls "Oh... Okay. Then I am more than satisfied!"
    scene black with fade
    "After talking a little more about the video and your plans for the future, you decided that there would be no rehearsals this week."
    "Because of your busy schedule, most of you have a lot of things to deal with."
    "Next week, however, everything would be back to the normal rhythm again."
    "..."
    "Everybody started going home."
    if lisa_path == True:
        scene 8rroom11 with dissolve
        ls "Um... [mc]."
        mc "Yeah, I wanted to talk to you, too."
        ls "I wanted to talk to you about last night..."
        mc "You don't have to say anything. It was amazing."
        scene 8rroom12 with dissolve
        ls "Yeah, it was. And you know... I can't wait for us to do it again."
        mc "Mm-hmm... Is it me, or did someone really enjoy it?"
        scene 8rroom12a with dissolve
        ls "Oh, come on!"
        mc "Actually, I wouldn't mind spending some more time with you either."
        scene 8rroom12b with dissolve
        ls "Yeah... about that."
        mc "Is something wrong?"
        ls "Not exactly. Last week we did a lot of work on these rehearsals."
        mc "Okay."
        ls "Anyway, I've had some problems at school because of all this."
        mc "That sucks."
        ls "Yeah, I know."
        ls "Anyway, I'm gonna have to study hard for the next couple of days. Otherwise, I'll be in serious trouble."
        mc "I understand... Is there anything I can do to help you?"
        scene 8rroom12 with dissolve
        ls "I don't think so."
        ls "But after I've dealt with everything, I could really use your company."
        mc "Huh. Then we have a deal!"
        ls "Well, that's great."
        mc "Then I'll call you."
        ls "Yes, of course."
        mc "See you."
    "..."
    if rosa_path == True:
        scene 8sms09 with fade
        "When you went outside, you heard a new message on your phone."
        mc "{i}Hmm... And who is it?{/i}"
        mc "{i}A message from Rosa.{/i}"
        mc "{i}Hmm? She wants to know if I can come to her art studio today and be a model.{/i}"
        mc "{i}Well, I agreed to it, so why not today?{/i}"
        stop music fadeout 3.0
        jump day08_rosa_day01
    if selina_path == True and rosa_path == False:
        scene 8sms09 with fade
        "When you went outside, you heard a new message on your phone."
        mc "{i}Hmm... And who is it?{/i}"
        mc "{i}A message from Selina.{/i}"
        mc "{i}Looks like she wants to meet today.{/i}"
        mc "{i}I don't see any reason to turn her down.{/i}"
        stop music fadeout 3.0
        jump day08_selina_flashback
    stop music fadeout 3.0
    if jane_path == True and RPjn >= 8 and jane_massage == True:
        jump day08_julia_night
    else:
        jump day08_home_sms

