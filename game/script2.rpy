label version_04:
    scene black with fade
    "Next Morning."
    play music "sounds/background2.mp3"
    scene v4_morning1 with fade
    pause 5
    scene v4_morning2 with fade
    mc "YAWN!"
    mc "{i}What a lovely morning.{/i}"
    mc "{i}Last night was really fun.{/i}"
    mc "{i}Even though I wasn't happy about having to come back home, for obvious reasons, I'm actually having a really good time."
    scene v4_morning3 with fade
    mc "{i}I wonder if [vn1] is in the pool this morning as well...{/i}"
    mc "{i}I can't see her, but isn't that Robin?{/i}"
    scene v4_morning4 with fade
    rb "I envy you, Daisy. You get to wake up in this amazing house that has a huge swimming pool every morning."
    ds "Yeah, I guess it's not bad..."
    scene v4_pool_animation with fade
    rb "Not bad? You have no idea how lucky you are."
    rb "I wish my parents were rich just like your family..."
    ds "Your family might not be rich, but your mother is a really lovely and sweet person."
    ds "Also, your father really cares about you and loves you."
    ds "If you ask me, you are the lucky one."
    rb "I don't know, maybe..."
    scene v4_morning3 with fade
    mc "{i}I haven't had the chance to properly meet her in person. Perhaps I should go down there and say hi.{/i}"
    scene black with fade
    stop music
    mc "..."
    scene v4_morning5 with hpunch
    mc "ARGH!"
    mc "MY HEAD!"
    mc "IT- IT HURTS... SO MUCH."
    mc "{i}What is this feeling? I- I don-{/i}"
    scene v4_bodyswap_animation with fade
    $renpy.pause(17.0, hard= True)
    scene black with vpunch
    mc "{i}ARGH!{/i}"
    mc "{i}...{/i}"
    mc "{i}Huh?{/i}"
    mc "Where am I?"
    mc "What's going on?"
    ds "What are you talking about?"
    scene v4_morning28 with hpunch
    mc "Daisy?!"
    ds "Yes?"
    mc "But... I was in my... and you were with the-"
    ds "Are you okay, Robin?"
    mc "I'm not sure-"
    mc "Wait! Who?"
    mc "Did you just call me... Robin?"
    ds "Yes. Why are you acting weird all of a sudden?"
    scene v4_morning27 with hpunch
    $renpy.pause(0.8, hard=True)
    scene v4_morning28 with hpunch
    $renpy.pause(0.8, hard=True)
    scene v4_morning6 with hpunch
    mc "WHAT THE-"
    ds "Seriously, what's going on with you?"
    mc "B-but HOW?"
    mc "WHY! I MEAN..."
    scene v4_morning7 with fade
    ds "Robin just calm down and talk to me, what's going on?"


    menu:
        "Freak Out Even More.\n{color=#999999}This Will End The Body-Swap Scene!!!{/color}":


            jump v4_bodyswap1
        "Calm Down And Control Yourself":
            if robin_swap == False:
                $ robin_swap = True
            jump v4_bodyswap2

label v4_bodyswap1:
    mc "I'm not Robin."
    ds "What the fuck are you talking about, Robin?"
    with vpunch
    mc "I TOLD YOU! I AM NOT ROBIN!"
    ds "Is this some kind of joke? If it is, it's not funny."
    mc "{i}What the hell is going on? Is this...{/i}"
    mc "{i}Is this one my powers? I can possess other people?{/i}"
    mc "{i}I need to stay calm. Last time, I didn't control my emotions and I wasn't able to control my power.{/i}"
    mc "I'm sorry Daisy, I'm feeling a little dizzy."
    ds "It must be the sun. Today is hotter than usual."
    mc "Yes, that must be it..."
    mc "{i}I must relax and try to focus. Maybe if I try hard enough I can go back to my own body...{/i}"
    scene black with fade
    mc "{i}Yes, exactly like that. I need to relax and take a deep breath...{/i}"
    mc "..."
    mc "I will just-"
    scene black with hpunch

    ukn "[mc]!"
    ukn "[mc], please wake up!"
    mc "Huh?"
    scene v4_morning16 with fade

    am "[mc]!"
    mc "A- Amber?"
    play music "sounds/background1.mp3"
    am "Thank god you're awake."
    mc "ARGH! MY HEAD HURTS SO MUCH!"
    mc "{i}I did it! It worked! Now, I need to play the fool...{/i}"
    mc "Wha- What happened to me?"
    am "I don't know. I just woke up and you were lying on the floor."
    am "Are you okay? Should I call an ambulance?"
    mc "No. I'll be fine."
    mc "I just need to-"
    mc "ARGH!"
    mc "I just need to get back to my bed."
    am "Are you sure?"
    mc "Yes."
    am "I should call Vanessa."
    mc "NO!"
    am "Why?"
    mc "It's not a big deal, there's no need to make her worry."
    mc "I guess I'm still a bit hungover from last night."
    am "I'm not sure about that. I think she needs to know and I think you need to go to the hospital."
    menu:
        "Get Angry":
            $ amber_rlt -= 1
            jump v4_angry1
        "Stay Calm":
            jump v4_calm1
label v4_angry1:
    with vpunch
    mc "THAT'S ENOUGH AMBER!"
    scene v4_morning17 with fade
    mc "I JUST NEED YOU TO-"
    mc "Just help me up so I can get to my bed."
    am "Okay. I'm sorry."
    scene v4_morning18 with fade
    mc "{i}GOD! My head is killing me!{/i}"
    am "Better now?"
    mc "Yes, thank you. I'm sorry for yelling at you."
    mc "You were just trying to help me, and-"
    am "It's okay, [mc]."
    mc "..."
    am "I have to go back to the city, but if you want me to stay..."
    mc "No, go ahead. I'll be fine, don't worry."
    am "If you say so..."
    am "Be sure to rest. If it doesn't improve, please go to the hospital."
    mc "Alright."
    am "Bye, [mc]."
    mc "Goodbye."
    stop music
    scene black with fade
    jump v4_afternoon

label v4_calm1:
    mc "There is nothing to worry about, I assure you."
    scene v4_morning17 with fade
    mc "Just help me up so I can get to my bed."
    scene v4_morning18 with fade
    am "Better?"
    mc "Yes. Thank you, Amber."
    mc "I'm sorry to make you worry about me, but I'm fine. I promise you."
    am "Are you sure?"
    mc "Yes, I'm sure. I just need some rest, that's all."
    mc "Please don't say anything to [vn1]. There's no need to trouble her over this."
    am "Okay."
    am "I have to go back to the city, but if you want me to stay..."
    mc "No, go ahead. I'll be fine, don't worry."
    am "If you say so..."
    am "Be sure to rest. If it doesn't improve, please go to the hospital."
    mc "Alright."
    scene v4_morning19 with fade
    am "Bye, [mc]."
    mc "Goodbye."
    stop music
    scene black with fade
    jump v4_afternoon


label v4_bodyswap2:
    mc "{i}I can't believe this! It must be a dream! Yes, that's the only explanation.{/i}"
    mc "This can't be real!"
    ds "What can't be real?"
    mc "I'm sorry, I have to go to the bathroom. Be right back!"
    ds "Wai-"
    scene v4_morning8 with fade
    play music "sounds/cafe.mp3"
    mc "Okay... I need to calm down."
    mc "I- I am in Robin's body?"
    mc "Wait... does that mean she's also in my body?"
    mc "What the FUCK is going on?"
    scene v4_morning20 with fade
    mc "Is this one of my powers? Taking control of someone else's body?"
    scene v4_morning9 with fade
    mc "Okay, [mc]. Just breathe and calm down."
    mc "I need to control my emotions in order to control my power."
    mc "Even though this is SO weird at the moment, the power to take over another person's body could be really useful..."
    scene v4_morning10 with fade
    mc "So, this is what having breasts feels like..."
    mc "She has really big ones, too."
    mc "Ohh! NO, NO, NO!"
    mc "I can't, I shouldn't..."
    mc "... or should I?"
    menu:
        "Touch Her(Your) Breasts":
            $ mc_evil +=1
            jump v4_breasts1
        "Touch Her(Your) Pussy":
            $ mc_evil +=1
            jump v4_pussy1
        "Try To Focus And End This Madness!":
            mc "Okay. I just need to stay calm and focus. I can do this!"
            $ mc_good +=1
            jump v4_mcwakeup
label v4_breasts1:
    mc "This is weird..."
    mc "But, I'll do it. I'll touch my breasts...? I mean her breasts...?"
    mc "Alright, here goes..."
    scene v4_morning11 with hpunch
    mc "Wow!"
    mc "It feels... different."
    mc "She has really nice pair of breasts. She must have massive back pain all the time."
    menu:
        "That's Enough I Should Stop":
            jump v4_focus
        "This Bikini Top Is Really Unconfortable...":
            jump v4_breasts2
label v4_breasts2:
    scene v4_morning12 with hpunch
    mc "Look at them, they look amazing."
    mc "My nipples feel kind of cold, tough."
    mc "Well... when you think about it, we have that in common."
    mc "Maybe I can massage them just a little."
    mc "Yes, to make sure her nipples and breasts stay warm."
    mc "I don't want her to catch a cold because of me..."
    menu:
        "That's Not That Good Of An Excuse.":
            jump v4_focus
        "Go For It!":
            $ mc_evil += 1
            jump v4_breasts3
label v4_breasts3:
    scene v4_bathroom_animation with fade
    mc "This is so awkward..."
    mc "Yes, like that. Slowly..."
    mc "What the fuck am I saying?"
    scene v4_morning25
    mc "This is getting way too weird..."
    menu:
        "Stop":
            jump v4_focus
        "Touch Her (Your) Pussy.":
            jump v4_pussy2

    scene black with fade
label v4_focus:
    mc "It's time to stop!"
    scene v4_morning9 with fade
    mc "I need to focus and stay as calm as possible in order to control my power."
    mc "I'll just close my eyes and take a deep breath..."
    scene black with fade
    mc "Stay calm."
    mc "..."
    mc "And..."
    scene v4_morning9 with hpunch
    mc "...SHIT!"
    mc "Okay, let's try this again..."
    mc "Focus, [mc]."
    mc "You can do this!"
    mc "Take a deep breath and empty your mind."
    scene black with fade
    jump v4_mcwakeup
label v4_mcwakeup:
    stop music
    scene black with fade
    ukn "[mc]!"
    ukn "[mc], please wake up!"
    mc "Huh?"
    scene v4_morning16 with fade
    am "[mc]!"
    play music "sounds/background1.mp3"
    mc "A- Amber?"
    am "Thank god you're awake."
    mc "ARGH! MY HEAD HURTS SO MUCH!"
    mc "{i}I did it! It worked! Now, I need to play the fool...{/i}"
    mc "Wha- What happened to me?"
    am "I don't know. I just woke up and you were lying on the floor."
    am "Are you okay? Should I call an ambulance?"
    mc "No. I'll be fine."
    mc "I just need to-"
    mc "ARGH!"
    mc "I need to go to my bed."
    am "Are you sure?"
    mc "Yes."
    am "I should call Vanessa."
    mc "NO!"
    am "Why?"
    mc "It's not a big deal, there's no need to make her worry."
    mc "I guess I'm still a bit hungover from last night."
    am "I'm not sure about that. I think she needs to know and I think you need to go to the hospital."
    mc "{i}She is not gonna let this go, isn't she?{/i}"
    menu:
        "Get Angry":
            $ amber_rlt -= 1
            jump v4_angry2
        "Stay Calm":
            jump v4_calm2
label v4_angry2:
    with vpunch
    mc "THAT'S ENOUGH AMBER!"
    mc "I JUST NEED YOU TO-"
    mc "Just help me up so I can get to my bed."
    am "Okay. I'm sorry."
    scene v4_morning17 with fade
    mc "{i}GOD! My head is killing me!{/i}"
    scene v4_morning18 with fade
    am "Better now?."
    mc "Yes, thank you and I'm sorry about yelling at you."
    mc "You were just trying to help me and-"
    am "It's okay [mc]."
    mc "..."
    am "I have to go back to the city but if you want me to stay..."
    mc "No you can go. I'll be fine don't worry about me."
    am "If you say so..."
    am "Be sure to rest and if you don't start to get better, please go to a hospital."
    mc "Alright."
    am "Bye, [mc]."
    mc "Goodbye."
    jump v4_afternoon
    scene black with fade
label v4_calm2:
    mc "There is nothing to worry about, I assure you."
    mc "Just help me up so I can get to my bed."
    scene v4_morning17 with fade
    am "Okay..."
    scene v4_morning18 with fade
    am "Better?"
    mc "Yes. Thank you, Amber."
    mc "I'm sorry to make you worry about me, but I'm fine. I promise you."
    am "Are you sure?"
    mc "Yes, I'm sure. I just need some rest, that's all."
    mc "Please don't say anything to [vn1]. There's no need to trouble her over this."
    am "Okay."
    am "I have to go back to the city, but if you want me to stay..."
    mc "No, go ahead. I'll be fine, don't worry."
    am "If you say so..."
    am "Be sure to rest. If it doesn't improve, please go to the hospital."
    mc "Alright."
    scene v4_morning19 with fade
    am "Bye, [mc]."
    mc "Goodbye."
    jump v4_afternoon

label v4_pussy1:
    mc "Am I really going to do this?"
    mc "This is so weird..."
    scene v4_morning13 with fade
    mc "..."
    scene v4_morning14 with fade
    mc "..."
    scene v4_morning15 with hpunch
    mc "SHIT this feels..."
    mc "So..."
    mc "Fucking weird."
    mc "I've taken things too far. I should stop."
    menu:
        "Stop":
            jump v4_focus
        "Touch Her(Your) Breasts":
            jump v4_breasts4
label v4_breasts4:
    mc "Though... maybe I can touch her breasts, too... Just a little."
    mc "Alright, here goes."
    scene v4_morning11 with hpunch
    mc "Wow!"
    mc "It feels... different."
    mc "She has really nice pair of breasts. She must have massive back pain all the time."
    menu:
        "That's Enough I Should Stop":
            jump v4_focus
        "This Bikini Top Is Really Unconfortable...":
            $ mc_evil += 1
            jump v4_breasts5
label v4_breasts5:
    scene v4_morning12 with hpunch
    mc "Look at them, they look amazing."
    mc "My nipples feel kind of cold, tough."
    mc "Well... when you think about it, we have that in common."
    mc "Maybe I can massage them, just a little."
    mc "Yes, to make sure her nipples and breasts stay warm."
    mc "I don't want her to catch a cold because of me..."
    menu:
        "That's Not That Good Of An Excuse.":
            jump v4_focus
        "Go For It!":
            $ mc_evil += 1
            jump v4_breasts6
label v4_breasts6:
    mc "Now that I REALLY think about it, I have to massage them to protect Robin's health."
    scene v4_bathroom_animation with fade
    mc "Yes, like that. Slowly..."
    mc "What the fuck am I saying?"
    mc "This is getting way too weird..."

    jump v4_focus
    scene black with fade
label v4_pussy2:
    mc "Before I end this, maybe I can touch her pussy, too... Just a little bit."
    mc "Alright, here it goes."
    scene v4_morning13 with fade
    mc "..."
    scene v4_morning14 with fade
    mc "..."
    scene v4_morning15 with hpunch
    mc "SHIT this feels..."
    mc "So..."
    mc "Fucking weird."
    mc "I took things too far. I need to end this."
    jump v4_focus
label v4_afternoon:
    scene black
    stop music
    play sound "sounds/cellphone.ogg"
    mc "..."
    scene v4_afternoon1 with fade
    play sound "sounds/cellphone.ogg"
    mc "Damn you phone..."
    mc "Shit! I was supposed to go to SID headquarters this morning!"
    scene v4_afternoon2 with fade
    mc "Hello."
    hr "Where are you?"
    mc "Home..."
    hr "You were supposed to be here in the morning, what happened? Is everything okay?"
    mc "It happened again."
    hr "So, you used your power..."
    mc "Yes. But, this time, it was different."
    mc "I felt enormous side effects this time."
    hr "Don't worry. You're still unable to control your power, so these things may happen from time to time."
    mc "I'm worried. What if I hurt myself or someone else?"
    hr "I'm sure you have many questions. We can discuss it once you're here."
    mc "Alright. I'll see you soon."
    scene black with fade
    mc "{i}Maybe Daisy and Robin are still at the pool.{/i}"
    scene v4_afternoon4 with fade
    mc "{i}They're not, but [vn1] is here, as always.{/i}"
    play music "sounds/cafe.mp3"
    mc "Hey."
    scene v4_afternoon5 with fade
    vn "Oh! Hello, [mc]."
    vn "Are you going to join me this time?"
    mc "Sorry, but I can't. I have things to do."
    vn "About those 'things'..."
    vn "...You are going out a lot ever since the day you returned and you never gave me an answer about what you're up to."
    vn "You didn't just return home to visit us, did you?"
    mc "..."
    vn "So, you still don't want to talk about it. Alright, honey. I'm not gonna force you. If you ever want to talk to me about anything, I'm here for you."
    mc "Thanks. I have to go now."
    vn "Wait. Before you go, there is something I want to ask you."
    vn "Could you please put on some sunscreen on my back? Today is really hot and I don't want to get a sunburn."
label v4_sunscreen1:
    mc "Of course."
    vn "Thank you, sweetheart."
    scene v4_afternoon6 with fade
    $ renpy.pause(1.3, hard=True)
    scene v4_afternoon7 with fade
    vn "Okay, I'm ready."
    mc "..."
    scene v4_afternoon8
    mc "{i}Her skin is so beautiful and smooth{/i}"
    vn "Your hands are so big and warm, [mc]. I can't believe how much you've grown. I still remember playing with you in the pool when you were just a little kid."
    vn "You were so cute and tiny."
    mc "Yes, those days were really fun. Olivia was too afraid to get in the pool. [eg1] had a tough time teaching her how to swim."
    vn "She was always a late bloomer, unlike Daisy."
    mc "Daisy was so brave and stupid. I remember her first time in the pool, she dove in without any hesitation and almost drowned."
    vn "And you jumped in the pool after Daisy to save her, but you weren't that good a swimmer. Eugene had to drag you both out of the pool."
    vn "I aged 10 years in just a few seconds that day."
    mc "..."
    scene v4_afternoon9 with fade
    vn "Let me untie this knot in my bikini top."
    vn "It will keep it from getting in your way."
    mc "{i}Wha-{/i}"
    scene v4_afternoon10
    vn "That's better."
    mc "Umm..."
    vn "What are you waiting for, honey? Keep going."
    mc "Okay."
    scene v4_afternoon_animation1 with fade
    vn "Much better."
    vn "Can you go little lower, honey?"
    mc "Sure."
    scene v4_afternoon_animation2 with fade
    mc "Is it good?"
    vn "Yes, sweetheart. Thank you so much. Today is hotter than usual. I was just about to go back inside."
    mc "I should put some lotion on your legs too, then. I don't want you to get sunburn."
    vn "That would be great."
    scene v4_afternoon_animation3 with fade
    mc "{i}Her legs are so firm and and smooth at the same time.{/i}"
    scene v4_afternoon_animation4 with fade
    mc "You have really soft skin, [vn1]."
    vn "Well, thank you, honey. I'm taking care of my body, as it is my temple."
    vn "Having someone who notices that is a good change around here."
    mc "I'm sure the girls also aware, but they are probably jealous of you."
    vn "Why would they be jealous of me? They're both young and beautiful."
    mc "Yes, they are, but you are on a different level, [vn1]."
    vn "You really think so?"
    mc "Yes."
    vn "Well, aren't you the sweetest?"
    scene v4_afternoon10 with fade
    vn "I think that's enough, honey."
    mc "Alright."
    vn "Thank you so much, [mc]."

label v4_office1:
    stop music
    play music "sounds/street.mp3"
    scene v4_office1 with fade
    mc "{i}Oh! Allison is here, too...{/i}"
    mc "Hello."
    scene v4_office2 with fade
    hr "Welcome, [mc]. Please have a seat."
    scene v4_office6 with fade
    mc "I'm sorry for being late, but it was a weird morning."
    scene v4_office3
    hr "Yes, you mentioned that on the phone. What happened, exactly?"
    scene v4_office6
    mc "I don't really know. I'd just woke up, got out of bed, took a look out the window, then I felt this sudden pain in my head."
    mc "I couldn't see or hear anything for a while. When I regained my senses, I realized that I had used my power again."
    scene v4_office3
    hr "And that power is...?"
    scene v4_office6
    mc "Sorry, I'm not telling you that."
    scene v4_office4
    al "If you keep important details to yourself, how are we going to help you, [mc]?"
    al "I know you don't trust us, especially me... But, you need to believe us when we are telling you our main goal is to help you."
    scene v4_office3
    hr "Yes, [mc]. She is right. I know you have mixed feelings towards Allison but she was only doing her job. You have to understand that."
    scene v4_office4
    al "My job was to protect you, and it still is."
    scene v4_office6
    mc "Look, I want to trust you, believe me. That would make things much easier for me, but your main job is not to protect me. Your sole purpose is to keep secrets. That's why the government pays you."
    mc "You can't expect me to trust you right away. I will let you help me and in exchange, I will help you, but there will be boundaries."
    mc "I know you can't tell me everything about [eg1]'s experiments or this other world, just like I can't tell you everything about my powers."
    mc "We need time to trust each other, and I am willing to give you as much time as you want. I expect the same thing from you."
    scene v4_office3
    hr "Fair enough, but you must know this. We may not have enough time to prepare for what's coming. I suggest you reach some conclusions, and do it soon.."
    hr "Okay, then. Time to start your training."
    hr "Allison will take you to our training dojo. We will work on your close combat skills."
    scene v4_office4
    al "Let's go."
label v4_training:
    stop music
    scene v4_training1 with fade
    play music "sounds/background2.mp3"
    hr "We are gonna start by testing your basic skills. Your training partner will be Allison."
    scene v4_training19
    al "I need to see what you are capable of, therefore we will start with sparring."
    scene v4_training1
    hr "I must warn you, [mc]. Allison is the best when we are talking about close combat. She can be deadly when she is serious."
    hr "If I were you, I wouldn't try anything reckless while facing her."
    scene v4_training19
    al "Relax, [mc]. She is just exaggerating."
    mc "..."
    al "If you are ready, let's start with a warm up."
    mc "Okay."
    scene v4_training2 with fade
    al "You don't have to follow my lead during the warm up. Do what you feel comfortable with."
    mc "Okay."
    scene v4_training3 with hpunch
    mc "Wow!"
    $ renpy.pause(1.0, hard=True)
    scene v4_training4 with fade
    al "15, 16, 17..."
    mc "You are stronger than you look, Allison."
    al "23, thanks, 25..."
    scene v4_training5 with fade
    mc "..."
    al "You can try something similar to this by sitting down and separating your legs in front of you."
    mc "Yes, that's probably a good idea. I don't see myself being able to do that."
    al "You can also do this, in time, with the proper training methods."
    al "Alright. That's enough for the warm up."
    scene v4_training7 with fade
    mc "I don't know about this..."
    scene v4_training8
    al "Don't worry, I will be careful."
    mc "No. I mean... I don't want to hurt you. I'm still angry with you, but I don't want to punch you in the face."
    scene v4_training6
    hr "Trust me, [mc]. You have nothing to worry about."
    mc "Are you sure?"
    scene v4_training8
    al "Just go for it, [mc]."
    mc "Alright."
    scene v4_training7
    pause 1.0
    scene v4_training9 with vpunch
    $ renpy.pause(0.8, hard=True)
    scene v4_training7
    $ renpy.pause(0.8, hard=True)
    scene v4_training9 with vpunch
    $ renpy.pause(0.8, hard=True)
    scene v4_training10
    al "C'mon, this can't be the best you can do."
    scene v4_training7
    $ renpy.pause(0.8, hard=True)
    scene v4_training9 with vpunch
    $ renpy.pause(0.8, hard=True)
    scene v4_training10
    al "Looks like I expected too much from you."
    mc "Don't push me, Allison."
    al "Or what? What are you gonna do?"
    scene v4_training6
    hr "Control your anger, [mc]. Losing your cool in the field can get you killed."
    scene v4_training10
    al "Yes, [mc]. Control your anger and keep hitting me like a little girl."
    stop music
    mc "You really want me to HIT YOU?!"
    scene v4_training11
    $ renpy.pause(1.2, hard=True)
    scene v4_training12
    $ renpy.pause(1.2, hard=True)
    scene v4_training13 with hpunch
    $ renpy.pause(1.5, hard=True)
    scene v4_training14 with hpunch
    $ renpy.pause(1.2, hard=True)
    mc "Argh!"
    scene v4_training20
    hr "Great job on controlling your temper, [mc]."
    scene v4_training14
    al "You can't let your emotions run wild. Your anger toward me lead to your defeat."
    scene v4_training15
    al "I could break your neck or strangle you if I wanted to."
    al "Luckily for you, I'm not your enemy."
    mc "Argh... Really? What are you? My friend?"
    al "Yes, [mc], I am. This may have started as a mission, but after spending so much time with you, you became the only friend I've ever had."
    mc "..."
    scene v4_training16
    al "As your friend, I will teach you everything I know so you can be safe and protect your family."
    al "Also {i}I'm sorry.{/i}"
    mc "WHAT? ARGH!"
    al "I said I'm sorry."
    mc "Umm, maybe we can talk after you've let go of me? Having a friendly chat in this position is kinda tough..."
    al "Oh! Right..."
    scene v4_training17 with fade
    $ renpy.pause(1.0, hard=True)
    scene v4_training18
    mc "Haruka wasn't kidding when she said you're the best."
    al "Thanks."
    al "Your stance and footwork were pretty good, but you need to learn to keep your emotions in check."
    al "It's also the key to controlling your powers. A calm mind is essential for our line of work."
    mc "{i}She is right. I need to focus and stay calm, just like this morning when I was able to control my power.{/i}"
    al "This time I will attack you and you will defend yourself. Watch my body movements and try to guess where will the attack come."
    al "I will go easy on you, but if you mess up, you will get hurt."
    mc "Alright. Bring it on."
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
init:
    $ block_count = 0
    $ hit_count = 0
label v4_minigame:
    scene v4_minigame1 with fade
    nr "Watch Allison's movements and try to guess where she will attack."
    nr "You have to block 6 of her attacks."
    nr "Also, you can't let her hit you more than 3 times."
    nr "Good luck."
    play music "sounds/thief.mp3"

label v4_minigamea:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'v4_menu_slow1'
    scene v4_minigame1
    $ renpy.pause(0.7, hard=True)
    scene v4_minigame2
    show screen countdown
    show screen buttonc
    show screen buttonb
    show screen buttong
    $ renpy.pause(5.0, hard=True)
label v4_minigameb:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'v4_menu_slow2'
    scene v4_minigame1
    $ renpy.pause(0.7, hard=True)
    scene v4_minigame5
    show screen countdown
    show screen buttona
    show screen buttond
    show screen buttonh
    $ renpy.pause(5.0, hard=True)
label v4_minigamec:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'v4_menu_slow1'
    scene v4_minigame2
    show screen countdown
    show screen buttonc
    show screen buttonb
    show screen buttong
    $ renpy.pause(5.0, hard=True)
label v4_minigamed:

    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'v4_menu_slow3'
    scene v4_minigame8
    show screen countdown
    show screen buttoni
    show screen buttonj
    show screen buttone
    $ renpy.pause(5.0, hard=True)
label v4_minigamex:


    $ block_count+=1
    hide screen countdown
    hide screen buttona
    hide screen buttonb
    hide screen buttonc
    hide screen buttond
    hide screen buttone
    hide screen buttonf
    hide screen buttong
    hide screen buttonh
    hide screen buttoni
    hide screen buttonj
    scene v4_minigame3 with hpunch


    al "Nice!"
    if block_count < 3:
        jump v4_minigamed
    elif block_count == 3:
        jump v4_minigameb
    elif block_count == 4:
        jump v4_minigamed
    elif block_count == 5:
        jump v4_minigamed
    elif block_count > 3 and block_count <6:
        jump v4_minigameb
    elif block_count == 6:
        jump v4_minigame_end

label v4_minigamey:
    $ block_count+=1
    hide screen countdown
    hide screen buttona
    hide screen buttonb
    hide screen buttonc
    hide screen buttond
    hide screen buttone
    hide screen buttonf
    hide screen buttong
    hide screen buttonh
    hide screen buttoni
    hide screen buttonj
    scene v4_minigame6 with hpunch

    al "Nice!"
    if block_count < 6:
        jump v4_minigamea
    elif block_count == 4:
        jump v4_minigamed
    elif block_count == 5:
        jump v4_minigamed
    elif block_count == 6:
        jump v4_minigame_end
label v4_minigamez:
    $ block_count+=1
    hide screen countdown
    hide screen buttona
    hide screen buttonb
    hide screen buttonc
    hide screen buttond
    hide screen buttone
    hide screen buttonf
    hide screen buttong
    hide screen buttonh
    hide screen buttoni
    hide screen buttonj
    scene v4_minigame9 with hpunch


    al "Nice!"
    if block_count < 6:
        jump v4_minigamea
    elif block_count == 4:
        jump minigameb
    elif block_count == 6:
        jump v4_minigame_end






label v4_menu_slow1:
    hide screen countdown
    hide screen buttona
    hide screen buttonb
    hide screen buttonc
    hide screen buttond
    hide screen buttone
    hide screen buttonf
    hide screen buttong
    hide screen buttonh
    hide screen buttoni
    hide screen buttonj
    scene v4_minigame4 with vpunch
    $ hit_count += 1
    mc "Argh"
    al "C'mon! Focus! You can do better!"
    if hit_count < 3:
        jump v4_minigameb
    elif hit_count == 3:
        jump v4_minigame_end2
label v4_menu_slow2:
    hide screen countdown
    hide screen buttona
    hide screen buttonb
    hide screen buttonc
    hide screen buttond
    hide screen buttone
    hide screen buttonf
    hide screen buttong
    hide screen buttonh
    hide screen buttoni
    hide screen buttonj
    scene v4_minigame7 with vpunch
    $ hit_count += 1
    mc "Argh"
    al "C'mon! Focus! You can do better!"
    if hit_count < 3:
        jump v4_minigamea
    elif hit_count == 3:
        jump v4_minigame_end2

label v4_menu_slow3:
    hide screen countdown
    hide screen buttona
    hide screen buttonb
    hide screen buttonc
    hide screen buttond
    hide screen buttone
    hide screen buttonf
    hide screen buttong
    hide screen buttonh
    hide screen buttoni
    hide screen buttonj
    scene v4_minigame10 with vpunch
    $ hit_count += 1
    mc "Argh"
    al "C'mon! Focus! You can do better!"
    if hit_count < 3:
        jump v4_minigamec
    elif hit_count == 3:
        jump v4_minigame_end2

label v4_minigame_end:
    hide screen countdown
    hide screen buttonb
    hide screen buttonc
    hide screen buttona
    hide screen buttond
    al "Well done!"
    jump v4_allison_takedown1
label v4_minigame_end2:
    if hit_count <= 3:
        $ hit_count =0
    if block_count <= 6:
        $ block_count = 0
    al "Is that all you got?"
    al "C'mon you can do better! Let's go again!"
    jump v4_minigamea
label v4_allison_takedown1:
    scene v4_minigame11 with fade
    al "Not bad, [mc]. Not bad at all."
    al "As you can see, when you focus hard enough and control yourself, you can do-"
    stop music
    play music "sounds/sexscene1.mp3"
    mc "{i}She is distracted. This could be a chance to make her pay for tackling me!{/i}"
label v4_allison_takedown2:
    scene v4_minigame12 with hpunch
    mc "..."
    al "What the-"
    scene v4_training6 with fade
    hr "Interesting..."
    hr "He wasn't supposed have enough skill to catch her of guard and take her down like that."
    scene v4_minigame12
    mc "Now we're even!"
    al "You think so?!"
    scene v4_minigame13
    mc "{i}She is really flexible!{/i}"
    scene v4_minigame14
    al "You might have an edge for being strong as a man, but strength means nothing aganist to superior skill!"
    scene v4_minigame15 with vpunch
    al "See? In the end, I'm the one who is on top!"
    mc "As much as I like the view, I am not planning to let you be on top of me like that."
    al "Oh yeah? What are you gonna do about it then?"
    mc "For such an experienced agent, you surely underestimate me a lot, Allison."
    scene v4_minigame17 with vpunch
    al "Shit!"
    al "{i}He is moving exactly like me. How is that even possible?{/i}"
    mc "What were you saying about being on top?"
    al "You think you can hold me down like that?"
    mc "Yes!"
    scene v4_minigame16
    al "{i}I can't shake him off! He wasn't even able to touch me few hours ago, how the hell was he able adapt to my movements this quickly?{/i}"
    with hpunch
    stop music
    hr "That's enough!"
    scene v4_training6 with fade
    hr "Both of you, come here."
    scene v4_training1 with fade
    play music "sounds/background1.mp3"
    hr "You did pretty well, [mc]. In fact, you were able to surpass your current capabilites."
    mc "What's that supposed to mean?"
    hr "Because of the super gene, you have the unique ability to absorb information, physical abilites, and techniques from others you come into physical contact with."
    scene v4_training19
    al "I see! That makes sense."
    mc "Really? That makes sense?"
    scene v4_training21
    hr "Let me simplfy it for you to understand."
    hr "Thanks to the super gene, your body is acting like a sponge that absorbs special abilites, knowledge, etc."
    hr "But, there is more."
    mc "More?"
    scene v4_training1
    hr "Theoretically, you have the potential to command multiple superpowers, if you get a chance to absorb them."
    mc "Wow! That's sounds amazing!"
    mc "But, wait! How many potential super powers are there exactly?"
    hr "Well... We don't know exactly how many super powers there are. As you already know, most of the test subjects were failures."
    hr "You, Daisy, and Olivia are the only surviving test subjects that we are aware of."
    hr "Prof. Donovan kept other's identites secret, even from us."
    scene v4_training19
    al "I guess he never completely trusted our organization..."
    scene v4_training21
    hr "Anyway..."
    hr "We don't know the whereabouts of any of the test subjects, but you have the potential to find all of them."
    hr "You see, the super gene you possess is rather special one. If every one of you with a super-gene were a pack of wolves, you would be the alpha among them."
    mc "So, you're saying that I can sense others with the super gene?"
    mc "If what you are saying is true, how come I haven't been able to sense anything weird about Daisy or Olivia?"
    hr "That's because you haven't yet realized your true potential. You need to train your mind and body to gain full control your power."
    mc "I see."
    mc "I have a question, though. How was I able to absorb Allison's knowledge and skills?"
    mc "I didn't do anything special or feel anything strange."
    scene v4_training1
    hr "It's actually pretty simple. All you have to do touch that person for a certain amount of time."
    hr "Longer periods of contact means more power and knowledge."
    hr "On the other hand, we are not sure how absorbing a superpower actually works."
    hr "The only person who can figure that out is you."
    mc "You're not suggesting that I involve my family in this, are you?"
    hr "I am not suggesting anything. It's completely up to you. If you find someone other than your sisters who has a super-gene, it's completly fine by me."
    mc "..."
    hr "I think that's enough for today. You should go home and get some rest."
    hr "I'll see you tomorrow."
    mc "Alright. See you."



label v4_mc_allison_talk:
    stop music
    play music "sounds/background2.mp3"

    scene v4_allison_mc1 with fade
    al "[mc], can we talk?"
    mc "Alright. Let's talk."
    al "First of all, I want to apologize. Again. You have to understand that protecting you was my priority. You are a really important asset to our world, and we couldn't let anyone hurt you."
    mc "Yes, I get that. I am another tool for you guys to use."
    scene v4_allison_mc8
    mc "You will train me, show me how things are done in this new world that I'm about to enter, and maybe after you're done with me, you'll make me disappear forever."
    mc "Or, perhaps you don't want to protect me at all. Maybe your organization is scared that I'll lose control and cause destruction all around me."
    mc "Your motive doesn't really matter to me anymore. I need you and you need me, at least for now..."
    mc "As long as our interests don't conflict with each other, we're good."
    al "You're right. It wasn't just about protecting you. We kept an eye on you because we also wanted to be sure that you wouldn't lose control and hurt people around you."
    scene v4_allison_mc1
    al "I was given two orders: to watch your every move in order to protect you and to..."
    mc "Yes..."
    al "And to make sure you don't lose control and become a danger to the people around you. If you did, I was to restrain you by any means necessary..."
    mc "Are my powers really that dangerous? I mean... Is there any chance for me to lose control?"
    al "To be honest, we're not so sure about that. Everything about you is new to us. The only person who can really help you with that was [eg4]."
    mc "I see. If there isn't anything else..."
    scene v4_allison_mc8
    al "..."
    al "There is one more thing."
    scene v4_allison_mc3
    al "I know you won't trust me anytime soon. Heck, you might never ever trust me again."
    al "I just want you to know that..."
    al "...this may have started as a mission, but after spending so much time with you, you become something more to me."
    scene v4_allison_mc4
    al "I've never had friends. All I known is how to be a spy. My only purpose in life were the details of my next mission. Until I met you."
    al "You were always so open and honest with me. My job taught me how to lie and how to tell if someone is lying to me and you've never lied to me despite the fact that all I did was deceiving to you."
    scene v4_allison_mc8
    al "There were so many times that I wanted to tell you everything."
    mc "Yet you didn't."
    al "Yes, because I was afraid."
    mc "Afraid of what?"
    al "I was afraid of losing my only friend."
    mc "..."
    mc "Do you know why I've been ignoring you ever since I've learned about you and SID?"
    al "No."
    mc "Because I lost my only friend and one of the best people I've ever met."
    mc "I had only one purpose in my life before I met you. I wanted to learn the truth about [eg1]."
    mc "You were one of the few things in my life that gave me some joy and happiness."
    scene v4_allison_mc2
    al "I'm sorry, [mc]. I really am..."
    al "I know things never will be the same between us, but can you at least give me one more chance?"
    al "I am not saying that you should forgive me right away. All I'm asking is one more chance to redeem myself."
    menu:
        "Give Her One More Chance.":
            if forgive_allison == False:
                $forgive_allison = True

            $allison_rlt += 1
            jump v4_mc_allisontalka
        "Tell Her You Need More Time To Think About It.":
            jump v4_mc_allisontalkb
label v4_mc_allisontalka:
    scene v4_allison_mc2
    mc "Okay. I will give you another chance but, it doesn't mean that I will forgive you that easily."
    scene v4_allison_mc4
    al "Thank you so much, [mc]."
    al "I really appreciate that."
    scene v4_allison_mc3
    menu:
        "Hug Her":
            $allison_rlt +=1
            jump v4_mc_allisontalka1
        "Say Goodbye":
            jump v4_mc_allisontalka2
label  v4_mc_allisontalka1:
    scene  v4_allison_mc7 with fade
    al "..."
    scene v4_allison_mc5 with fade
    al "I still can't believe you pinned me down like that. Don't let that confuse you by the way. I'm still a superior fighter in this building."
    scene v4_allison_mc6 with fade
    mc "Yes, for now..."
    al "Is that so? Next time we are sparing, I won't go easy on you."
    al "I'll see you tomorrow, [mc]. Take care of yourself."
    mc "Thanks, Allison."
    scene black with fade
    jump v4_olivia_mc1
label v4_mc_allisontalka2:
    scene v4_allison_mc4
    al "I still can't believe you pinned me down like that. Don't let that confuse you by the way. I'm still a superior fighter in this building."
    scene v4_allison_mc3
    mc "Yes, for now..."
    scene v4_allison_mc4
    al "Is that so? Next time we are sparing, I won't go easy on you."
    mc "I'm looking forward to it."
    al "I'll see you tomorrow, [mc]. Take care of yourself."
    scene v4_allison_mc3
    mc "Thanks, Allison."
    scene black with fade
    jump v4_olivia_mc1

label v4_mc_allisontalkb:
    scene v4_allison_mc1
    mc "I don't think it's gonna be that easy, Allison. I still need some time to think about it."
    mc "I understand your situation completely, but a lot of things have happened during the last couple of days."
    mc "We should keep things professional. That would make things easier for me, at least for now..."
    scene v4_allison_mc2
    al "I understand..."
    mc "Thank you."
    mc "I'll see you tomorrow."
    scene v4_allison_mc1
    al "Bye..."
    scene black with fade
    jump v4_olivia_mc1
label v4_olivia_mc1:
    stop music
    play music "sounds/background1.mp3"
    scene v4_mc_olivia1 with fade
    mc "{i}Olivia! Where's she off to...?{/i}"
    scene v4_mc_olivia2 with fade
    mc "Hey."
    scene v4_mc_olivia3
    ol "Hello, [mc]."
    scene v4_mc_olivia2
    mc "Where are you going?"
    scene v4_mc_olivia3
    ol "I'm going to meet with Trevor."
    ol "You know... The guy I've been talking to for a while now."
    scene v4_mc_olivia2
    mc "Oh! You mean your online boyfriend."
    mc "You said you're going to 'meet' with Trevor not to go 'see' him."
    mc "All this time you've been talking to this guy and you've never actually seen him in person before?"
    scene v4_mc_olivia4
    ol "Yes..."
    ol "I know It sounds weird, but Trevor didn't mind the fact that we haven't met in person yet, and neither do I."
    mc "I see..."
    scene v4_mc_olivia2
    mc "So, you have no idea what does he look like."
    scene v4_mc_olivia3
    ol "No, I know what he looks like. He sends me a few pictures every time we talk."
    init:
        define beyaz = Fade(1.0, 0.0, .75, color="#fff")
        define beyaz1 = Fade(3.0, 0.0, .75, color="#fff")

    ol "He is tall, strong, gentle, and really handsome."
    scene v4_mc_olivia7 with beyaz
    ol "He loves computer games, just like me, his favorite food is pepperoni pizza, just like me, and his favorite movie is Harry Potter, jus-"
    mc "Just like you..."
    scene v4_mc_olivia3 with beyaz
    ol "Yes!"
    scene v4_mc_olivia2
    mc "{i}This guy is a perfect match for her. It's so perfect that I am almost not gonna believe he really exists...{/i}"
    mc "Listen, Olivia. Is it really a good idea to meet with this guy."
    scene v4_mc_olivia3
    ol "What do you mean?"
    scene v4_mc_olivia2
    mc "You know how things are in online dating stuff. People lie to each other all the time."
    scene v4_mc_olivia3
    ol "I already know that [mc], but he is not one of them."
    scene v4_mc_olivia2
    mc "How can you be so sure?"
    scene v4_mc_olivia3
    ol "It's not about being so sure. It's about believing."
    scene v4_mc_olivia2
    mc "Olivia, you're a smart person. I know you can take care of yourself, but when it comes to your social life... the way you think and behave is, umm, how should I say it? It's not like your usual self."
    mc "That's why I'm so concerned about this meeting."
    mc "{i}There's also this unknown organization targeting me and the people around me. Blind dates and secret meetings are far too dangerous.{/i}"
    scene v4_mc_olivia3
    ol "[mc], we've already talked about this. You don't have to worry about me. I can take care of myself. I just need your trust and support. I'm going to meet Trevor. It's really important to me for two reasons..."
    ol "First off, I really like him and I feel like he is my soulmate."
    scene v4_mc_olivia4 with dissolve
    ol "Secondly, I have to do this because I need to stop being afraid of meeting new people. I want to be like you and Daisy. I want to do new things with new people."
    mc "I understand..."
    scene v4_mc_olivia3
    ol "Thank you so much, [mc]."
    scene v4_mc_olivia5
    ol "I won't be late. We're just going out for coffee, that's all."
    scene v4_mc_olivia6
    mc "{i}I don't like this at all. I don't know if I'm just being paranoid, but considering everything that's happened the last couple of days...{/i}"
    mc "{i}It's better be safe than sorry. I'm gonna follow her and see if this guy really is who he claims to be...{/i}"
    scene v4_street1 with fade
    stop music
    mc "..."
    scene v4_street2 with fade
    ukn "Hi, there."
    ol "Hello?"
    ukn "You look even better in person, Olivia."
    ol "Umm..."
    tr "It's me. Trevor."
    scene v4_street3 with fade
    ol "Oh! Really?"
    ol "You look nothing at all like the pictures you've sent me."
    scene v4_street4 with fade
    tr "I know, you must be thinking: 'He's one of those freaks who uses a fake profile to lure young women'."
    tr "I can assure that's not my intention. All the pictures I've sent are actually me... Just, me when I was in my twenties."
    scene v4_street3
    ol "I see..."
    scene v4_street4
    tr "Look at you getting all nervous and shy. You really are the same person that I've been talking to for the last couple of months."
    scene v4_street3
    ol "Listen, umm... Sir? I'm sorry, but I don't think what you're doing is appropriate. I'm sure you are not a bad person, but you've been lying to me all this time about who you really are."
    scene v4_street4
    tr "Please, call me Trevor."
    tr "Yes, you are absolutely right, but I only ask you to give me a chance to show you who really I am."
    tr "I know that I shouldn't have lied to you, but as soon as I saw your profile I fell in love with you, then I felt this sudden agonizing feeling inside me..."
    tr "I knew that a guy like me had no chance with an amazing and beautiful girl like you..."
    tr "That's when I decided to pretend I was in my 20s, and pretended that I was into all of the things that are popular with people your age."
    scene v4_street3
    ol "So, the things about video games, favorite food, and movie-"
    tr "Sadly, all of them were lie."
    scene v4_street5
    tr "Please, Olivia. Give me at least one chance to prove myself. Let's go somewhere nice and I'll show you how much a lovely person I can be."
    scene v4_street6 with fade
    ol "I don't know..."
    ol "I think this was a mistake."
    scene v4_street7 with fade
    mc "{i}That dude looks nothing like what Olivia says. I think it's time for me to intervene!{/i}"
    scene v4_street8 with fade
    ol "I should go, but I wish you the best of luck. I'm sure if you stop pretending and lying to people, eventually you will find someone actually likes you for who you really are."
    scene v4_street9 with hpunch
    tr "Not so fast!"
    tr "All I'm asking is for you to give me a chance to redeem myself. Why do you act so selfish and stuck-up?"
    ol "Hey! Let go of me!"
    scene v4_street10
    tr "Shit! I'm sorry Olivia. I didn't mean to hurt or scare you."
    ol "I'm leaving now. I don't want to see you or hear from you ever again!"
    tr "YOU CAN'T JUST WALK AWAY FROM ME, YOU LITTLE BITCH!"
    ol "..."
    scene v4_street11 with hpunch
    play music "sounds/thief.mp3"
    mc "THAT'S ENOUGH!"
    tr "Who the hell are you?!"
    scene v4_street12 with hpunch
    ol "[mc]?!"
    scene v4_street11
    tr "You know this guy?"
    ol "Yes, he is-"
    mc "YES! She knows me."
    mc "I know what's going on here and I will give you this one chance to walk away."
    scene v4_street13 with fade
    tr "Look boy, I don't know who you think you are, but I suggest you get the fuck out of here before you get hurt."
    mc "Listen, you fucking old pervert. Not only is Olivia extremely important to me, so much so that I would do anything to protect her, but I'm also a police officer."
    scene v4_street14
    tr "..."
    tr "And where is your badge to prove it?"
    mc "Well... It's not on me at the moment, but-"
    scene v4_street15 with hpunch
    tr "I've heard enough."
    tr "I will leave for now, but I'm sure we will meet again, Olivia."
    tr "And you! I will let it slide just this once, but if you ever come between me and Olivia again, I will kick your ass. Did you understand?"
    scene v4_street16
    mc "..."
    scene v4_street17 with hpunch
    mc "You're not going anywhere!"
    scene v4_street18
    mc "You think I'll just let you go after everything you said?"
    mc "You will forget about Olivia and never, EVER bother her again."
    mc "If I ever see you again, I will fucking kill you. Do you understand me? No one, I mean NO ONE in the fucking world can do any harm to this girl as long as I'm alive!"
    tr "Look at you, talking all big and confident."
    tr "I think I have to teach you a lesson, boy!"
    scene v4_street19
    ol "NO, STOP!"
    scene v4_street21 with vpunch
    menu:
        "Slap His Ugly Face":
            jump v4_slap1
        "Punch Him":
            jump v4_punch1
label v4_slap1:
    scene v4_street22
    $ renpy.pause(2.0, hard=True)
    scene v4_street23 with hpunch
    tr "ARGH!"
    scene v4_street24
    mc "Don't force me, old man! I won't hold back!"
    scene v4_street25
    ol "That's enough [mc]. Let's just go, please."
    mc "..."
    scene v4_street26 with hpunch
    ol "[mc], look out!"
    scene v4_street27 with hpunch
    tr "I AM GOING TO KILL YOU!"
    scene v4_training12 with beyaz
    $ renpy.pause(0.8, hard=True)
    scene v4_training13 with dissolve
    $ renpy.pause(0.8, hard=True)
    scene v4_street28 with hpunch
    $ renpy.pause(2.0, hard=True)

    scene v4_street29 with hpunch
    tr "ARGH!"
    scene v4_street30 with dissolve
    stop music
    ol "OH GOD!"
    scene v4_street31 with dissolve
    mc "..."
    scene v4_street32 with fade
    play music "sounds/background2.mp3"
    mc "It's okay, now. You can relax. It's over."
    scene v4_street33 with vpunch
    ol "[mc] {i}*sob*...{/i} I was so scared!"
    scene v4_street34 with fade
    ol "I don't know what would've happened if you hadn't shown up {i}*sob*...{/i}"
    mc "Everything is alright now. I've always got your back. I won't let anyone harm you."
    ol "Thank you! {i}*sob*{/i} Thank you so much!"
    mc "Let's go home."
    ol "{i}*sob*{/i} Okay..."
    scene v4_street35 with fade
    ol "..."
    scene v4_street36
    mc "???"
    scene v4_street37
    $ renpy.pause(1.5, hard=True)
    scene v4_street38
    $ renpy.pause(2.0, hard=True)
    jump v4_night
label v4_punch1:
    scene v4_street20 with hpunch
    tr "ARGH!"
    scene v4_street31
    mc "..."
    scene v4_street32 with fade
    stop music
    play music "sounds/background2.mp3"
    mc "It's okay, now. You can relax. It's over."
    scene v4_street33 with vpunch
    ol "[mc] {i}*sob*...{/i} I was so scared!"
    scene v4_street34 with fade
    ol "I don't know what would've happened if you hadn't shown up {i}*sob*...{/i}"
    mc "Everything is alright now. I've always got your back. I won't let anyone harm you."
    ol "Thank you! {i}*sob*{/i} Thank you so much!"
    mc "Let's go home."
    ol "{i}*sob*{/i} Okay..."
    scene v4_street35 with fade
    ol "..."
    scene v4_street36
    mc "???"
    scene v4_street37
    $ renpy.pause(1.5, hard=True)
    scene v4_street38
    $ renpy.pause(2.0, hard=True)
    jump v4_night
label v4_night:

    scene v4_mc_olivia_home1 with fade
    mc "Are you okay?"
    scene v4_mc_olivia_home3
    ol "No..."
    scene v4_mc_olivia_home2
    mc "I'm sorry things didn't work out."
    scene v4_mc_olivia_home3
    ol "It's okay, [mc]. Things like that always happen in online dating..."
    mc "{i}She's about to burst into tears...{/i}"
    scene v4_mc_olivia_home4
    ol "I can't believe I was so stupid. Just thinking about what could've happened there if you haven't shown up in time gives me shivers!"
    scene v4_mc_olivia_home5
    mc "As long as you have me, no one can do any harm to you. Never ever forget that."
    mc "I know I wasn't there for you when you needed me most. I will never forgive myself because of that, but I'll do my best to make it up to you."
    mc "You are not stupid at all. You are a good, kind, and loving person. I don't want you to change because of scumbags like that old bastard."
    scene v4_mc_olivia_home6
    ol "{i}What is this feeling? I feel so calm and safe suddenly.{/i}"
    ol "{i}Is this what having someone dependable and strong in your life feels like?{/i}"
    scene v4_mc_olivia_home7
    ol "Thank you, [mc]. I feel much better now."
    scene v4_mc_olivia_home6
    mc "I'm glad to hear that."
    mc "I love you, Liv."
    scene v4_mc_olivia_home7
    ol "I love you too, [mc]."
    ol "Listen. I don't think I will be able to sleep tonight, so I was thinking maybe we can watch some movies together..."
    scene v4_mc_olivia_home6
    mc "I would love that. In fact, we can watch Harry Potter. If you want to, of course."
    scene v4_mc_olivia_home7
    ol "Are you kidding me? Of course I want to watch Harry Potter!"
    ol "Come to my room around 10 pm."
    scene v4_mc_olivia_home6
    mc "Alright. I'll see you tonight."


label v4_night_maeve:
    stop music
    scene v4_maeve1 with fade
    mc "..."
    scene v4_maeve2 with fade
    mv "It was incredible. I think this boring job will be much more fun, thanks to him."
    mc "Who is she talking to?"
    scene v4_maeve3 with fade
    mv "At first, he doesn't seem like a man who would do things like that, but I couldn't be more wrong."
    mv "Watching them doing it in the middle of living room was so hot!"
    mc "{i}Is she talking about me and Amber?{/i}"
    mv "Oh yes, he got some good moves, but his girlfriend was something else."
    mv "[mc] is so lucky to have someone like her. She has the insatiable desire, but [mc] was more than capable of satisfying her."
    mv "Oh yes! He is big."
    mc "{i}How about that... If I had known that we had an audience, I would've put in much more effort.{/i}"
    mv "Well, he hasn't made a move on me yet, but who knows..."
    mc "{i}Interesting...{/i}"
    mv "Anyway... I should hang up. It's getting late and I have to wake up early tomorrow."
    mv "Bye-bye."
    scene v4_maeve4 with fade
    mv "Having someone other than Daisy who brings some action in this house is kinda good."
    mc "You don't say."
    mv "Wha-"
    scene v4_maeve5 with hpunch
    play music "sounds/cafe.mp3"
    mv "You scared me!"
    mc "Did I, now?"
    mv "Umm. Did you..."
    mc "Yep. I heard everything."
    mv "Oh..."
    scene v4_maeve6
    mv "I- I'm sorry. I was just..."
    mc "You were just...?"
    mv "I- I don't know what to say..."
    scene v4_maeve7
    mc "Let me help you. You were in your room trying to sleep, and you heard some noises coming from the living room."
    mc "Then you saw us and decided to enjoy the show."
    mv "..."
    scene v4_maeve8
    mv "I'm so sorry. I shouldn't have done that."
    scene v4_maeve9
    mv "Please forgive me."
    mc "What do you think will happen if I told [vn2] that you were spying on me while I was with my girlfriend."
    scene v4_maeve7
    mc "You also clearly said that you spy on Daisy from to time to time."
    scene v4_maeve10
    mv "Please, don't say anything to Vanessa. I can't lose this job."
    menu:
        "Try To Use Your Mind Control Powers":
            $ mc_evil +=1
            jump v4_night_maeve_evil1

        "Forgive Her Just This Once":
            $ mc_good +=1
            $ maeve_rlt +=1
            jump v4_night_maeve2
label v4_night_maeve_evil1:
    scene v4_maeve7
    stop music
    mc "{i}This might be a good opportunity to try using my power.{/i}"
    mc "{i}If I remember correctly, I was able to use my powers on Samantha because of the overwhelming anger that I felt.{/i}"
    mc "{i}If I can focus on that feeling, maybe I'll be able use my power willingly this time...{/i}"
    scene v4_maeve8
    mv "Sir?"
    mc "Do not talk. Let me focus..."
    scene v4_maeve7
    mc "..."
    mc "..."
    mc "Argh!"
    scene v4_night_animation1 with fade
    $ renpy.pause(2.0, hard=True)
    scene v4_maeve_evil1 with beyaz1
    mc "YES! I CAN FEEL IT!"
    mc "She looks exactly like Samantha did when I put her in a trance."
    mc "Let's test it."
    mc "Repeat after me: Amy Schumer is the funniest person in the world."
    mv "Amy Schumer is the funniest person in the world."
    mc "Yep, she is definitely under my control. No one in their right mind would say that..."
    mc "Alright. Let's spice things up a little bit."
    play music "sounds/sexscene1.mp3"
    mc "Now, get up and kiss me."
    scene v4_maeve_evil3 with hpunch
    mv "Mhmm."
    scene v4_maeve_evil2 with fade
    mc "{i}Her lips are so soft and delicious.{/i}"
    menu:
        "Touch Her Ass":
            jump v4_night_maeve_evil2
        "Release Her From Your Control":
            jump v4_night_maeve_evil8
label v4_night_maeve_evil8:
    scene black with fade
    mc "I should stop and don't push my luck anymore."
    mc "Forget about everything that happened and go to your room."
    mc "{i}I should change my clothes and go to Olivia's room.{/i}"
    jump v4_movie
label v4_night_maeve_evil2:
    scene v4_maeve_evil4 with fade
    mc "{i}I'm getting really horny. It's just like how I felt when I tried to take things further with Samantha.{/i}"
    mc "{i}Why does the use of my powers have such an effect on me?{/i}"
    scene v4_maeve_evil5
    mc "Look at you. You are so cute."
    menu:
        "Kiss Her One More Time":
            jump v4_night_maeve_evil3
        "Tell Her To Get On Her Knees":
            jump v4_night_maeve_evil4
label v4_night_maeve_evil3:
    scene v4_maeve_evil2 with fade
    $ renpy.pause(2.3, hard=True)
    scene v4_maeve_evil3 with fade
    $ renpy.pause(2.3, hard=True)
label v4_night_maeve_evil4:
    scene v4_maeve_evil5 with fade
    mc "Now, get on your knees and grab my dick."
    scene black with fade
    mc "Start with sucking my balls."
    scene v4_maeve_evil6 with fade
    mc "Wow, you're a natural. It feels so good!"
    mc "Mmmm! OHH! Yes, keep going!"
    mc "Now, start licking my dick."
    scene v4_night_animation2
    mc "YES! Use your tongue more!"
    mc "OHH!"
    mc "It's time for the main event."
    mc "Suck my dick with those beautiful juicy lips!"
    scene v4_maeve_evil7
    mc "Start by sucking the head first!"
    scene v4_maeve_evil8 with fade
    mc "OH GOD! YES!"
    mc "Circle your tongue around my tip."
    mc "Mmm! Good girl."
    mc "Now, take my dick deep in your mouth."
    scene v4_night_animation4 with fade
    mc "GOD, you are so good at this!"
    mc "Keep going like that."
    mv "Hmph! Hmph!"
    mc "I feel like my dick is melting inside of your mouth."
    mc "OHH! AHH!"
    mc "Take my dick deeper in your mouth."
    scene v4_maeve_evil9 with hpunch
    $renpy.pause(0.8, hard=True)
    mc "I said deeper!"
    scene v4_maeve_evil13 with hpunch
    mc "OHH! Hold it like that."
    mc "Breathe through your nose and hold it as much as you can!"
    mc "I think you can go even deeper than that."
    scene v4_maeve_evil12 with hpunch
    mc "SHIT! That hit the spot."
    mc "Whatever you do, do not take my dick out of your mouth!"
    mv "Hmph!"
    mv "HMPH!!!"
    mc "Okay, that's enough."
    scene v4_night_animation5 with fade
    mv "Panting..."
    mc "That was amazing. You managed to hang in there pretty well."
    mc "Break is over. We don't have much time"
    mc "Now give me a deepthroat of your life. Suck my dick like there is no tomorrow!"
    scene v4_night_animation3 with fade
    mc "Yes! Take my dick as deep as you can."
    mc "Harder!"
    mc "AHH!"
    mc "I'm almost there!"
    mc "Don't stop! Harder! Deeper!"
    mc "ARGH I'M CUMMING!"
    scene v4_maeve_evil21 with dissolve
    menu:
        "Cum Inside Of Her Mouth":
            jump v4_maeve_mouth
        "Cum On Her Face":
            jump v4_maeve_face
label v4_maeve_mouth:
    scene v4_maeve_evil20 with hpunch
    mc "OHHH!"
    scene v4_maeve_evil13 with flash
    $renpy.pause(0.8, hard=True)
    scene v4_maeve_evil13 with flash
    $renpy.pause(0.8, hard=True)
    scene v4_maeve_evil14 with fade
    mc "That was... Panting... Incredible... Panting..."
    mc "Don't spit it out. Swallow it."
    scene v4_maeve_evil15
    $renpy.pause(0.8, hard=True)
    scene v4_maeve_evil16
    mc "Good girl."
    mc "Now, go to the bathroom, clean yourself up and forget everything that happened."
    scene black with fade
    mc "{i}I should change my clothes and go to Olivia's room.{/i}"
    jump v4_movie
label v4_maeve_face:
    scene v4_maeve_evil17 with hpunch
    mc "OHHH!"
    scene v4_maeve_evil17 with flash
    $renpy.pause(0.8, hard=True)
    scene v4_maeve_evil18 with flash
    $renpy.pause(0.8, hard=True)
    scene v4_maeve_evil19 with flash
    mc "That was... Panting... Incredible... Panting..."
    mc "Now, go to the bathroom, clean yourself up and forget everything that happened."
    scene black with fade
    mc "{i}I should change my clothes and go to Olivia's room.{/i}"
    jump v4_movie





label v4_night_maeve2:
    scene v4_maeve7
    mc "I don't know about this..."
    scene v4_maeve8
    mv "Please, I'm begging you."
    scene v4_maeve7
    mc "Fine."
    play music "sounds/park.mp3"
    scene v4_maeve_good1
    mc "But, you will stop spying on Daisy, is that clear?"
    scene v4_maeve_good2
    mv "Yes! I won't ever do that again! Thank you so much!"
    scene v4_maeve_good1
    mc "By the way, I heard your comments about my- ummm... 'performance'."
    scene v4_maeve_good3 with vpunch
    mv "Oh...!"
    scene v4_maeve_good2
    mv "Well... I was..."
    mc "You should know I wasn't giving my all that night. If I would've known that we had an audience, I would've put on a good show for you."
    scene v4_maeve_good3 with hpunch
    mv "WHAT?!"
    mc "I let Amber do most of the work. She did pretty good if you ask me, don't you think?"
    mv "Yes?"
    mc "Are you asking or answering?"
    mv "..."
    mc "What's wrong? Cat got your tongue?"
    mv "Yes, she was pretty good."
    mc "Did you like what you saw?"
    scene v4_maeve_good4
    $ renpy.pause(1.0, hard=True)
    scene v4_maeve_good5
    mv "Well..."
    scene v4_flashback1 with beyaz
    $ renpy.pause(1.5, hard=True)
    scene v4_flashback2 with beyaz
    $ renpy.pause(1.5, hard=True)
    scene v4_maeve_good5 with beyaz
    mv "Yes, you could say that."
    scene v4_maeve_good4
    mc "I'm glad to hear that."
    mc "I would like to talk with you and get to know you more."
    mc "But, that will have to wait. Olivia is waiting for me."
    scene v4_maeve_good5
    mv "Don't worry. I'm sure there is gonna be plenty of time for us to get to know each other."
    mv "I have to be up pretty early tomorrow, so I should get to sleep."
    mv "Good night, Sir."
    scene v4_maeve_good4
    mc "Good night, Maeve, and stop calling me sir, call me [mc]."
    scene v4_maeve_good6 with fade
    mc "{i}Look at that body...{/i}"
    scene v4_maeve_good7 with fade
    mv "{i}Looks like I'll have a lot of fun in this house...{/i}"
    scene black with fade
    mc "{i}I should change my clothes and go to Olivia's room.{/i}"
label v4_movie:
    stop music
    scene v4_olivia_night1 with fade
    mc "..."
    scene v4_olivia_night2 with fade
    play music "sounds/background1.mp3"
    mc "Hey."
    ol "Hey. I was afraid that you aren't gonna show up."
    mc "Are we going to sit here?"
    ol "It's more comfortable than it looks. C'mon, sit."
    mc "Fine."
    scene v4_olivia_night3 with fade
    mc "You're right, it's really comfy."
    ol "Right? And we get to sit really close to each other which is another plus for me, hehe."
    mc "Is that so..?"
    mc "Maybe I prefer to have my comfort zone, maybe I don't want to get close to you? Did you ever consider that?"
    ol "I- I wasn't..."
    mc "Haha, I'm just kidding."
    ol "Idiot..."
    scene v4_olivia_night4 with fade
    mc "I actually really miss this. This... feeling."
    scene v4_olivia_night9
    ol "What do you mean?"
    scene v4_olivia_night5
    mc "I mean I love Daisy and [vn1], but you were always more special for me."
    scene v4_olivia_night9
    ol "Really?"
    scene v4_olivia_night5
    mc "Yes. I love the pure-hearted and warm person you are. Simply sitting next to you, I can feel your love."
    scene v4_olivia_night10
    ol "..."
    mc "Sorry if I made things awkward, I don't usually say stuff like that."
    scene v4_olivia_night11
    ol "..."
    mc "Hey, are you crying?"
    mc "{i}She had a really bad day. I think it's understandable...{/i}"
    scene v4_olivia_night13
    ol "No, I'm not. It just..."
    mc "Just what?"
    scene v4_olivia_night12
    ol "Never mind."
    ol "Thank you, [mc]. For everything."
    stop music
    scene v4_olivia_night4 with dissolve
    $renpy.pause(1.2, hard=True)
    scene v4_olivia_night5 with dissolve
    $renpy.pause(1.4, hard=True)

    scene v4_olivia_night6 with dissolve
    $renpy.pause(1.5, hard=True)
    scene v4_olivia_night7
    ol "..."
    ol "{i}I feel so safe and good when he is with me. I've never felt like this with anyone before...{/i}"
    scene v4_olivia_night8 with fade
    $ renpy.pause(1.5, hard=True)
    scene black with fade
    "Meanwhile..."
label v4_night_portal:
    play music "sounds/sorgu.mp3"
    scene v2end01 with fade
    st "Sir, this is Samantha ready to report."
    ukn "Go on."
    scene v2end02 with fade
    st "SID has started [mc]'s training. As you already know, he has the super-gene. Considering this, we can assume that he will make tremendous progress in a really short time."
    ukn "You're right. Waiting is no longer an option."
    ukn "We have to act fast."
    scene v2end01 with fade
    st "I agree, sir."
    st "What are my next orders?"
    ukn "I'm not the one who is going to give you your new orders."
    ukn "She is..."
    scene v4_portal1 with fade
    st "..."
    st "{i}What is this sound?!{/i}"
    scene v4_portal2 with fade
    st "Who did he send this time?"
    scene v4_portal3 with beyaz1
    st "Argh!"
    scene v4_portal4 with flash
    st "..."
    scene v4_portal6 with fade
    st "I wasn't expecting to see you so soon."
    scene v4_portal5 with fade
    ukn1 "Acceleration of the latest events forced us to act quickly."
    ukn1 "From now on, this is my operation. You are under my command."
    ukn1 "Is that understood?"
    st "Yes..."
    scene v4_portal6 with fade
    st "{i}I forgot how much I hate her!{/i}"
    scene v4_portal5 with fade
    ukn1 "Wery well. Shall we begin?"
    stop music



    jump gameover
