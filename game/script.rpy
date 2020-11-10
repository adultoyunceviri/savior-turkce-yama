# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#### CHARACTERS ####
init -5:
    define ukn = Character("???", color="#999999")
    define ukn1 = Character("???", color="#ff69b4")
    define mc = Character("[mc]", color="#40e0d0")
    define nr = Character("Narrator", color="#9933ff")
    define al = Character("Allison", color="#ff69b4")
    define am = Character("Amber", color="#ff69b4")
    define dn = Character("Donald", color="#4876ff")
    define er = Character("Earl", color="#4876ff")
    define tf = Character("Thief", color="#4876ff")
    define hr = Character("Haruka", color= "#ff69b4")
    define vn = Character("Vanessa", color= "#ff69b4")
    define ol = Character("Olivia", color= "#ff69b4")
    define ds = Character("Daisy", color= "#ff69b4")
    define eg = Character("Eugene", color="#4876ff")
    define po1 = Character("Police Officer1", color="#4876ff")
    define po2 = Character("Police Officer2", color="#4876ff")
    define po = Character("Police Officer", color="#4876ff")
    define wt = Character("Waitress", color= "#ff69b4")
    define wtr = Character("Waiter", color= "#4876ff")
    define bt = Character("Bartender", color="#4876ff")
    define st = Character("Samantha", color="#ff69b4")
    define mv = Character("Maeve", color="#ff69b4")
    define rb = Character("Robin", color="#ff69b4")
    define tr = Character("Trevor", color="#4876ff")
###--- Text
init -6:
    define mc1 = "[mc]"
    define mc2 = "[mc]"
    define vn1 = "Vanessa" #m
    define vn2 = "Vanessa" #mym
    define vn3 = "Vanessa" #yrm
    define vn4 = "Vanessa" #orm
    define vn5 = "Vanessa" #m
    define vn6 = "Vanessa" #mtr
    define eg1 = "Eugene" #d
    define eg2 = "Eugene Donovan" #f
    define eg3 = "Dr. Eugene Donovan" #d
    define eg4 = "Eugene" #d
    define eg5 = "Dr. Donovan" #d
    define eg6 = "Dr. Donovan" #d
    define eg7 = "DR. DONOVAN"
    define ds1 = "Daisy" #m
    define ds2 = "Daisy" #yrm
    define ds3 = "Daisy" #mym
    define ds4 = "Daisy" #m
    define ds5 = "Daisy" #hrmm
    define ds6 = "Daisy" #hrmm
    define ol1 = "Olivia" #g
    define ol2 = "Olivia" #md
    define ol3 = "Olivia" #s
    define ol4 = "Olivia" #str
    define ol5 = "Olivia" #ys
    define ol6 = "Olivia" #Ys
#### CHARACTERS ####
################################################################################
#### CONDITIONS ####
init -4:

    $ v2_oliviatalk = True
    $ v2_oliviatalk1 = True
    $ v2_oliviatalk2 = True
    $ v2_oliviatalk3 = True
    $ v2_daisytalk = True
    $ v2_daisytalk1 = True
    $ v2_daisytalk2 = True
    $ v2_daisytalk3 = True
    $ v2_vanessatalk = True
    $ v2_vanessatalk1 = True
    $ v2_vanessatalk2 = True
    $ v2_vanessatalk3 = True
    $ v2_everyonetalk = True
init:
    $ daisy_rlt = 0
    $ olivia_rlt = 0
    $ vanessa_rlt = 0
    $ haruka_rlt = 0
    $ maeve_rlt = 0
    $ amber_rlt = 0
    $ allison_rlt = 0
    $ samantha_rlt = 0
    $ robin_rlt = 0
    $ mc_good = 0
    $ mc_evil = 0
    $ v3_ambertalk = True
    $ v3_ambertalk1 = True
    $ v3_ambertalk2 = True
    $ v3_oliviatalk = True
    $ v3_oliviatalk1 = True
    $ v3_oliviatalk2 = True
    $ v3_oliviatalk3 = True
    $ v3_daisytalk = True
    $ v3_daisytalk1 = True
    $ v3_daisytalk2 = True
    $ v3_daisytalk3 = True
    $ v3_vanessatalk = True
    $ v3_vanessatalk1 = True
    $ v3_vanessatalk2 = True
    $ v3_vanessatalk3 = True
    $ v3_everyonetalk = True
    $ v3_everyonetalk1 = True
    $ v3_amberdress = True
    $ v3_daisydress = True
    $ v3_vanessadress = True
    $ v3_oliviadress = True
    $ vanessa_met = False
    $ daisy_met = False
    $ olivia_met = False
    $ amber_met = False
    $ allison_met = False
    $ haruka_met = False
    $ samantha_met = False
    $ robin_met = False
    $ maeve_met = False
    $ forgive_allison = False
    $ robin_swap = False
#### CONDITIONS ####

################################################################################

######## CHARACTER SPRITES ########
#### ALLISON ####

#### SCENES AMBER DOGGY ####




################################################################################

################################################################################

################################################################################




# The game starts here.
image splash = "splash.png"

init -6 python:
    persistent.patch_installed = False
init -5 python:
    if persistent.patch_installed and not persistent.patch_first_time:
        persistent.patch_enabled = True
        persistent.patch_first_time = True
    elif not persistent.patch_installed:
        persistent.patch_first_time = False
        persistent.patch_enabled = False
label start:
    scene black
    menu:
        nr "You must be 18 or over to able to play this game. If you are under 18, you must leave now!"

        "Yes, I'm 18+.":
            jump mcname
        "No, I'm under the age of 18.":
            jump main

label mcname:
    $ mc = renpy.input("Lütfen ana karakterin adını girin veya karakterinize Nicholas adını vermek için enter tuşuna basın.", length=25)
    $ mc = mc.strip()
    if mc == "":
        $ mc="Nicholas"
    menu:
        "Do you want to name the main character [mc] ?"
        "Yes":
            jump scene0
        "No":
            jump start
            return
    $ mc= Character("[mc]", color= "#40e0d0")
label scene0:
    nr "If you already played version 0.1 or 0.2 you can skip to version 0.3."
    nr "Your previous save files might not work or you might have some errors during playing the game."

    menu:
        "Skip To Version 0.2":
            jump sorgu
        "Skip To version 0.3":
            jump v3_mc_dream
        "Start From The Begining":
            jump scene1




label scene1:
    scene black
    with fade

    play music "sounds/narrator.mp3"
    scene prologue1
    with fade


    po1 "Hello, ma'am. Sorry to bother you this late, but we need to speak with you."
    vn "What's going on? What's so urgent that it couldn't wait until tomorrow?"
    po1 "It's your husband, Eugene Donovan. He..."
    vn "He-"
    vn "He what?"
    po1 "He vanished."
    po1 "I mean, he is missing."
    mc "What's going on?"
    mc "There are cops at our door!"
    mc "Did they say something about [eg1]?"
    po2 "He suddenly disappeared while working at his lab."
    vn "What do you mean 'he disappeared'?"
    po2 "We checked the security footage. It was really strange. He was reading something when some sort of light appeared in his lab. About 3 seconds later the security feed went black."
    po2 "When the security feed was back online, he was nowhere to be found. He was just... gone."
    vn "What?"
    po1 "We are so sorry! He seemed to vanish without a trace."
    po1 "There was nothing left behind. We reviewed security footage of the entire facility, but didn't spot him anywhere."
    po1 "During those 3 seconds, he just disappeared. It's almost like he... teleported?"
    vn "(This is exactly what we were afraid of, they're getting ready to start! Dammit, we should've had more time! What am I supposed to do without you, my love?)"
    po1 "Ma'am! Are you okay? Please, say something..."
    vn "Thank you so much for your hard work, officers."
    vn "I'm sure he will return home. There must be some glitch or technical problem with your security system."
    po1 "..."
    po2 "..."
    po1 "You're welcome, Mrs. Donovan."
    po2 "If you need anything, please let us know."
    vn "Of course!"
    scene black
    with fade
    mc "He is gone!"
    mc "Why would he leave us!"
    mc "Why would he leave me..."
    vn "[mc]!"
    scene prologue3
    with fade
    vn "Why are you still up?"
    mc "[vn1]... is he really gone?!"
    vn "(Oh, no! He heard everything...)"
    vn "Of course not, sweetie! Why would he leave us?"
    mc "You don't have to lie! Please, tell me the truth."
    vn "The truth...? {i}sigh{/i}"
    vn "(There is no way I can tell him the truth. He cannot know about Eugene's past... or mine.)"
    vn "Okay, darling. The truth is... Eugene disappeared and the police have no idea how, or why. They're doing their best to find him, but..."
    mc "But... what?!"
    vn "Don't worry, honey. I'm sure the police will find him."
    vn "Okay? Time to go to bed, young man!"
    mc "Yes..."
    stop music fadeout 2.0
    scene black
    with fade
    nr "A MONTH LATER..."
    scene prologue1
    with fade
    play music "sounds/narrator2.mp3"
    po1 "We're sorry to say this, ma'am, but we haven't been able to uncover any leads as to the cause of your husband's disappearance, nor where he might have gone."
    po1 "We have to close the case."
    vn "(That was to be expected.)"
    vn "(It's definitely them...)"
    po2 "Is there anything we can do for you, ma'am?"
    vn "(We need to get ready.)"
    vn "Huh? Did you say something?"
    po1 "I think she's in shock..."
    po2 "Don't be rude! She's just been told that her husband hasn't been found and we're closing the case into his disappearance."
    vn "Thank you for everything, officers."
    po2 "Of course, ma'am."
    scene black
    with fade
    nr "Everyone gathers in the living room..."
    scene prologue2
    with fade
    vn "Kids... I have some bad news for you."
    vn "[eg4]... is no longer with us."
    ds "..."
    ol "Is he... Dead?"
    vn "We don't know. He just dissapeared, but most likely he-"
    mc "'He' what?!"
    vn "[mc]..."
    mc "He's not here. I get that. Maybe he left, or maybe someone took him..."
    mc "No one's said that he's dead..."
    vn "Honey, it's good to have a hope, but..."
    scene prologue4
    with fade
    mc "I promise you."
    mc "I will find out what happened to him."
    mc "I promise, to all of you!"
    vn "Honey, don't make such promises..."
    vn "It will be okay! We can still go on without him..."
    mc "I know we can, but..."
    mc "I have to know the truth!"
    vn "..."
    mc "Olivia, Daisy..."
    mc "I will find the truth."
    vn "..."
    stop music fadeout 2.0
    scene black
    with fade
    play music "sounds/narrator.mp3"
    nr "After losing Eugene, [mc] made it his mission to uncover the truth about him."
    nr "He lost interest in video games, friends, and school."
    nr "He never had any trouble with his studies and exams."
    nr "Upon finishing high school, [mc] decided to enroll at the local police academy."
    nr "Despite receiving top marks in high school, [mc] chose to forgo his future in academia in order to solve the mystery of what happened to Dr. Eugene Donovan."
    nr "And so [mc] set forth with hopes that becoming an officer of the law would increase his odds of discovering the truth behind Eugene's disappearance."
    nr "The real story of [mc] begins now..."
    stop music fadeout 2.0
    scene black
    with fade
    nr "PRESENT DAY"
    scene mcpolicedesk with fade
    play music "sounds/background1.mp3"
    mc "I hope today will be as quiet as usual. I need to keep digging. I need to find some kind of clue as to what happened to [eg1]."
    mc "It's been 12 years..."
    mc "Since the day we lost him..."
    mc "Rather, the day of his mysterious disappearance..."
    mc "To this day, there hasn't been even a single clue as to where he could've gone."
    mc "All authorities have given up on the case."
    mc "Hell, even [vn2] gave up on finding her husband so damn easily!"
    mc "I'd swear she knows something, but she refuses to tell anyone."
    mc "Maybe she thinks she's trying to protect us from something..."
    mc "Nevertheless, I don't give a damn about what the authorities or she think!"
    mc "I will figure this out. I will learn the truth!"
    dn "Hey, bozo!"
    scene black with fade
    mc "Suddenly I feel like the IQ of the room has dropped to almost zero."
    scene mcdonaldtalk with fade
    mc "Oh! Of course."
    scene mcdonaldtalkblur
    show donald with dissolve
    dn "What are you mumbling about?"
    dn "The goverment doesn't pay for you to sit on your ass all day!"
    dn "GET YOUR ASS OUT OF THAT CHAIR!"
    mc "OK! Calm down."
    mc "Officer Donovan. Ready for orders, sir!"
    dn "That's better, rookie."
    dn "I need you and Allison to go to the city."
    dn "All the other officers have real work to do, so you two are out on patrol."
    mc "Going on patrol is also important, and should be done by every officer in this station. You know that, right?"
    dn "SHUT UP AND DO AS I SAY, ROOKIE!"
    mc "(You fat pig.)"
    dn "What was that?"
    mc "I said yes, sir! I will find my partner and we'll go."
    dn "Alright, then."
    hide donald with dissolve
    scene mcdonaldtalk
    scene black with fade
    pause 0.3
    scene mcdonaldtalkblur
    show donald
    dn "Hey! I almost forgot. Get me some of those new flavoured donuts, will you?"
    mc "(You don't need to remind me of that. They basically create a new flavour every month just for your fat ass)"
    mc "Of course, sir. You can count on me!"
    dn "Yes, yes, sure. Now, get to the task I've assigned to you!"
    hide donald with dissolve
    scene mcdonaldtalk
    mc "Damn, I really hate this place! Sucks that it's the best place for me to do research on [eg1]."

    mc "Okay, lets go and see what Allison is up to."
    scene black
    with fade
    stop music fadeout 1.0
    scene allisondesk1 with fade
    play music "sounds/background2.mp3"

    if allison_met == False:
        $ allison_met = True
    mc "There she is."
    mc "Ever since that day, she is the only person that can make me smile."
    mc "Sometimes we give each other a hard time, but that's part of the fun."
    mc "The most important thing is that I know I can trust her, no matter what!"
    mc "I've got an idea."
    scene allisondesk2 with fade
    mc "Officer, what are you doing!? Hurry, evacuate the station!"
    mc "THERE IS A HUGE FIRE! LET'S GO! MOVE IT!"
    scene policestation with fade
    pause 0.8
    scene policestationblur
    show police_allison_surprised_eyes with dissolve
    al "Ehh! What!? What fire? Where?? Shit!!"
    mc "I'm talking about the smoking hot, flame haired inferno in front of me."
    mc "HAHAHAHAHA!"
    hide police_allison_surprised_eyes with dissolve
    show police_allison_serious_eyes with dissolve
    al "FUCK YOU, ASSHOLE! I thought there was an actual fire!"
    mc "I know! It was hilarious!"
    mc "HAHAHA! You should've seen your face! Priceless."
    mc "Okay, okay. Lets just both agree that it was funny and calm down."
    al "Moron."
    hide police_allison_serious_eyes with dissolve
    show police_allison_natural_eyes with dissolve
    al "What the hell do you want, anyway?"
    mc "Fat ass gave us a special misson. Top secret special misson..."
    al "Yeah, yeah, in your dreams! I'll be ready in five then we can go for stupid patrol."
    mc "I'll wait for you on the street."
    al "Alright."
    scene policestation
    pause 0.8
    scene black with fade
    stop music
    mc "Does the word 'five' mean something else in your world? What took you so long?"
    play music "sounds/allison.mp3"
    scene policecar
    al "I needed to use the little girl's room."
    mc "Oh! I see. So, you took a huge shit. Why didn't you say?"
    al "Oh boy, yeah. It was a monster."
    al "Now I have room for donuts and coffee."
    mc "Yeah, let's go get some."
    image earl= "images/Backgrounds/earl.png"
    image earlblr= "images/Backgrounds/earlblr.png"
    scene earl
    with fade
    er "Hey! My favorite customers are here!"
    mc "What's up, Earl? How's business?"
    er "I'm doing pretty good! The wife's pregnant, again."
    al "I am so happy to hear that."
    mc "Congrats, man! If this one is a boy, please name him [mc]."
    scene earlblr
    with fade
    show police_allison_serious_eyes at right with dissolve
    al "Oh god, no! Whatever you do, please don't name your child [mc]."
    mc "Hey! Whats wrong with my name?"
    al "The name itself is fine, but when we add {i}you{/i} to the mix, it's just... how should I say it? The biggest no in the universe!"
    mc "That's not fair! I am adorable, and my name is adorable."
    er "No need to fight, guys. We will name him Earl Jr. If it's a boy, of course."
    mc "Wow. How original."
    al "Shut up, [mc]."
    al "What if it's a girl?"
    er "Well, don't get mad [mc], but..."
    mc "NO!"
    hide police_allison_serious_eyes with dissolve
    show police_allison_surprised_eyes at right with dissolve
    al "YES!"
    mc "HELL NO!!"
    al "YES, YES, YES!!!"
    er "We will name her Allison."
    mc "WHAT!?"
    hide police_allison_surprised_eyes with dissolve
    show police_allison_laugh_eyes at right with dissolve
    al "HAHAHA! YESSS!"
    al "IN YOUR FACE!"
    al "Mr. Earl, you are a truly wise man. Excellent choice."
    mc "Let's just get our donuts and leave."
    er "Hey! Don't get mad, it's just a coincidence."
    er "Allison is my wife's mother's name, so..."
    al "Really?"
    er "(Just go with it, girl!)"
    hide police_allison_laugh_eyes with dissolve
    show police_allison_smile_eyes at right with dissolve
    al "(Oh, I see. Yeah, sure.)"
    al "..."
    er "..."
    al "..."
    hide police_allison_smile_eyes with dissolve
    show police_allison_laugh_eyes at right with dissolve
    al "No, it's not coincidence! He's lying and they're naming their little baby girl after me. He just asked me to go with his little plan to avoid upsetting you, but who cares? HAHAHAHAH!"
    er "HOLY-! Girl, what's your problem?"
    scene earl
    with fade
    mc "See? This is what I have to put up with every day."
    mc "...and you say you will name your daughter after her?"
    er "Well, yes. I've known both of you for a year and Allison is really a good person."
    er "She's a good cop. She's kind and generous, and to top it off, she's a really beautiful woman."
    er "My little girl growing up to be like Allison? She's everything a father could ever hope his little girl would be."
    mc "Oh yeah? Careful what you wish for!"
    scene earlblr
    show police_allison_smile_eyes at right with dissolve
    al "Awww! Earl, that's so sweet!"
    er "Hehe."
    mc "(Wait! Does Earl have a crush on Allison?!)"
    scene earl with fade
    mc "NO WAY!"
    er "What?"
    al "What?"
    mc "Umm... I'm just craving for some donuts. Please just give me some already!"
    er "Oh, alright! There you go, my man."
    er "It's your favorite BAILEY’S SALTED CARAMEL AND ESPRESSO DONUT."
    mc "Ohhh YEAH. That's a donut to die for."
    er "...and for you sweetheart, BLUEBERRY KEY LIME DONUT."
    scene earlblr
    show police_allison_smile_eyes at right with dissolve
    al "Thank you so much, Earl! You make the best donuts on earth."
    er "I got your coffees, too. Black and strong, just like me. Hehe"
    mc "(He is flirting with her.)"
    hide police_allison_smile_eyes with dissolve
    show police_allison_laugh_eyes at right with dissolve
    al "Haha! Earl, you are so funny."
    er "Thanks! (Actually, I wouldn't mind some of your sugar for this black coffee, if you know what I mean.)"
    scene earl with fade
    er "I almost forgot! Say hi to Sgt. Donald and give him these new flavored donuts."
    mc "Thank you so much, man! Here's money for the  donuts and coffee. Take care!"
    er "Thanks, my man. Be careful out there! There are some tough criminals in town."
    mc "Yeah, sure! Like Mrs. Betsy and her vicious chihuahua?"
    er "Yeah, you know it. That bitch is crazy! Hehe."
    al "Thanks, Earl! See you soon."
    er "Good bye, sweetheart. Don't make me miss you too much."
    scene earlblr
    show police_allison_smile_eyes at right with dissolve
    al "Oh! There is no way that'll happen, Earl. With all the sweet cream you got there for me, I will always come back for more, handsome."
    mc "I think my ears are bleeding."
    er "Umm... Yeah... Okay... Bye..."
    scene black with fade
    scene policecarblur with fade
    mc "You little redheaded demon."
    show police_allison_natural_eyes with dissolve
    al "What is it now?!"
    mc "Don't you dare pretend. You know what you did. What the fuck was that?"
    al "Haha. So what? I flirt with him a bit to make him happy, and maybe he will give me free donuts once in a while."
    mc "Oh. He sure wants to give it to you, but not a donut."
    hide police_allison_natural_eyes with dissolve
    show police_allison_laugh_eyes with dissolve
    al "Hahah. Can you blame him?"
    mc "No, but after spending a night with you, I'm sure he will blame himself. Heck, he might even try to commit suicide!"
    hide police_allison_laugh_eyes with dissolve
    show police_allison_serious_eyes with dissolve
    al "Bullshit. I'm hot and you know it."
    mc "Yeah, fine. You're hot."
    al "You're not so bad, either."
    mc "What are you talking about? I am the golden god. All the men want to be like me and all the women want to be with me."
    hide police_allison_serious_eyes with dissolve
    show police_allison_natural_eyes with dissolve
    al "Actually, all the men want to be with you and all the women want to be like you."
    hide police_allison_natural_eyes with dissolve
    show police_allison_laugh_eyes with dissolve
    mc "Go to hell!"
    al "Haha."
    al "Okay, that's enough. Let's keep patrolling and get this over with."
    scene black
    with fade
    scene policecarblur
    mc "As usual, nothing happens."
    al "Yeah. Sometimes I feel lucky that I don't have to risk my life or get into any real danger."
    al "Though, sometimes..."
    mc "You just want to see some action, right?"
    al "Yes! I mean, it's great that this isn't a violent place, but a little action wouldn't hurt now and then."
    mc "You know, when a movie character says a thing like that, something suddenly happens and they get what they asked for."
    al "Oh! You mean comedic timing, like in sitcoms."
    mc "Yes, exactly! Too bad we are not in a movie or a TV show..."
    stop music fadeout 2.0
    al "Yeah..."
    play music "sounds/thief.mp3"
    play sound "sounds/femalescream.mp3"
    ukn "AHHHHHHHHHH!"
    ukn "HEELLLLPPPPPP!"
    ukn "SOMEBODY!"
    mc "No fucking way..."
    show police_allison_natural_eyes with dissolve
    al "Yep. It actually happened."
    hide police_allison_natural_eyes with dissolve
    play sound "sounds/carbreak.mp3" fadein 0.1
    mc "That son of a bitch is trying to steal that woman's bag!"
    mc "Let's go."
    scene theft1
    with fade
    mc "HEY! STOP RIGHT THERE!"
    mc "LEAVE HER ALONE!"
    tf "Oh, shit! Fucking popos."
    ukn "SOMEBODY! PLEASE, HELP!"
    al "He got the bag."
    al "He's running away, I'm gonna shoot him."
    mc "Don't. Too many civilians."
    al "He's running, what are we supposed to do?"
    mc "You stay with her and I'll catch him."
    al "Wait, what?"
    mc "I said stay with her!"
    al "Don't do anything stupid."
    scene theft2
    with fade
    mc "HEY! STOP RUNNING!"
    mc "STAY WHERE YOU ARE OR I'LL SHOOT!"
    tf "GO FUCK YOURSELF, STUPID POPO!"
    mc "For god's sake."
    mc "(Come on lungs and legs, don't let me down now!)"
    mc "Almost got him..."
    tf "SHIT!"
    mc "Got you!"
    scene black
    with fade
    tf "Ouch!"
    tf "Ease up, man."
    scene theft3
    with fade
    mc "Shut up, asshole!"
    mc "You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to an attorney, and to have an attorney present during any questioning. If you cannot afford an attorney, one will be provided for you at government expense."
    tf "I am sorry, can you repeat that again."
    mc "Yeah sure, you have th-"
    mc "Shut your fucking mouth and move!"
    tf "Okay! Okay!"
    scene theftstreet with fade
    scene theftstreetblur
    stop music fadeout 1.0
    show police_allison_serious_eyes with dissolve
    play music "sounds/background1.mp3"
    al "Hey, are you ok?"
    mc "Yeah, I'm fine. This bastard was really fast."
    al "You caught him, though."
    mc "Of course I caught him."
    mc "You know me and my reputation."
    hide police_allison_serious_eyes with dissolve
    show police_allison_natural with dissolve
    al "Your what?"
    mc "Officer, put this scumbag into the car and await further orders."
    hide police_allison_natural with dissolve
    show police_allison_serious_eyes with dissolve
    al "WHAT?!"
    mc "Officer, do as you've been told."
    scene theft4 with fade
    tf "Hey, you are hurting me."
    al "Shut your mouth and get in the fucking car."
    tf "This city's police officers are really mean."
    tf "You know words matter and they can hurt your feelings, right?"
    al "I SAID SHUT YOUR FUCKING MOUTH!"
    scene theftstreetblur with fade
    mc "Ma'am, are you okay? Did he hurt you?"
    show daily_amber_sad2_eyes with dissolve
    ukn "No, he didn't. I'm fine."
    mc "Are you sure? Should we call an ambulance?"
    mc "Dispatch this is [mc], we need an ambulance to-"
    ukn "I'm fine, really! I don't need an ambulance."
    mc "Okay, ma'am, if you say so."
    ukn "Thank you so much officer... umm..."
    mc "[mc]. My name is officer [mc]."
    am "Nice to meet you [mc], my name is Amber."
    if amber_met == False:
        $amber_met = True

    hide daily_amber_sad2_eyes with dissolve
    show daily_amber_sad1 with dissolve
    am "Thank you so much. You are so brave. I... I was really scared."
    scene thefthug with fade
    mc "Hey, hey. Don't cry. It's okay, everything is fine, now. Come here."
    am "Thank you! Thank you, so much."
    am "I don't know what I would've done if you hadn't shown up just then..."
    mc "Officer Allison! Go wait in the car for my orders."
    scene theftstreetblur with fade
    show police_allison_serious_eyes with dissolve
    al "What the fu-"
    mc "Don't make me repeat myself, officer!"
    al "Yes, sir... (You are gonna pay for this, [mc].)"
    hide police_allison_serious_eyes with dissolve
    show daily_amber_sad2_eyes with dissolve
    am "Your partner seems angry. Is everything okay?"
    mc "Yeah, everything is fine. She has some anger management issues."
    am "Oh! Okay, then..."
    am "I don't know what to say. You were so brave. Most of the cops in this town are useless fat pigs."
    hide daily_amber_sad2_eyes with dissolve
    show daily_amber_smile1_eyes with dissolve
    am "I'm glad to see someone like you on the police force."
    mc "Someone like me?"
    am "Yes. I mean, you are young, brave, and handsome! Not to mention you have a really fit, hot body..."
    mc "..."
    hide daily_amber_smile1_eyes with dissolve
    show daily_amber_blush1_eyes with dissolve
    am "..."
    mc "Thanks."
    am "Umm... did I say that last part out loud?"
    mc "Yep."
    hide daily_amber_blush1_eyes with dissolve
    show daily_amber_blush2_eyes with dissolve
    am "Hehe! Okay, now I'm blushing."
    mc "Yes, you are. Don't worry. You look cute when you blush."
    hide daily_amber_blush2_eyes with dissolve
    show daily_amber_blush1_eyes with dissolve
    am "Umm, thanks..."
    hide daily_amber_blush1_eyes with dissolve
    show daily_amber_smile1_eyes with dissolve
    am "I should probably go."
    am "Thank you so much for everything!"
    mc "No need to thank me, I was just doing my job."
    mc "Have a nice day, Amber."
    am "Thanks! Same to you."
    hide daily_amber_smile1_eyes with dissolve
    show daily_amber_natural1_eyes with dissolve
    am "..."
    am "[mc], wait."
    mc "Yes?"
    am "I was thinking, umm..."
    am "If you're free after work, maybe we could grab some coffee?"
    am "I mean, it's just that I want to show my gratitude, and... you know..."
    am "Buy you some coffee."
    mc "Yeah, sure! I would love that."
    hide daily_amber_natural1_eyes with dissolve
    show daily_amber_surprised2_eyes with dissolve
    am "Really?! Wow! That's great!"
    am "Here's my card. I know a great place that makes delicious coffee."
    mc "Sounds wonderful."
    hide daily_amber_surprised2_eyes with dissolve
    show daily_amber_flirt2_eyes with dissolve
    am "Alright, then. I'll see you tonight."
    mc "Can't wait."
    am "Bye."
    mc "Bye."
    scene black
    with fade
    stop music
    scene policecarblur with fade
    play music "sounds/allison.mp3"
    mc "Guess who got a date tonight?"
    al "..."
    mc "This guy!"
    show police_allison_smile_eyes with dissolve
    al "Wow, good for you. Maybe you'll get lucky and finally lose your virginity to that dumb bimbo."
    mc "My, my, will you look at that? Somebody is jealous!"
    hide police_allison_smile_eyes with dissolve
    mc "When I said I wanted some action I didn't mean it like that, but..."
    mc "I'll take what I can get."
    show police_allison_natural_eyes with dissolve
    al "Who, me?! Jealous of you...?"
    hide police_allison_natural_eyes with dissolve
    show police_allison_laugh_eyes with dissolve
    al "HAHAHAHA! Wow! Now, {i}that's{/i} a funny joke."
    al "You should be next host of the Tonight Show after Jimmy Fallon."
    mc "Yeah, but I heard Jay Leno's still hiding somewhere in NBC headquarters waiting for Fallon to die."
    mc "As for your other question? Yes, you {i}are{/i} jealous."
    mc "Your hair has never been this red before! HAHAHA."
    hide police_allison_laugh_eyes with dissolve
    show police_allison_serious_eyes with dissolve
    al "That's ridiculous, [mc]."
    mc "Whatever you say, Allison."
    al "Just drive..."
    hide police_allison_serious_eyes with dissolve
    tf "You guys are a really cute couple."
    tf "You know... I had a girlfriend, too."
    tf "Her name was Anna. She was a little bit older than me and had three children. Two daughters and one son."
    tf "Her son was kinda weird though. He never left the house and had a hard-on all the time."
    tf "Then, suddenly, that Eric guy showed up with his big company, money, and stuff."
    tf "Though, none of that was the reason why Anna dumped me."
    tf "She said 'I got sick of your tiny penis, I want something more. I want everything to be at MAX in my life.'"
    mc "..."
    al "..."
    "SHUT THE FUCK UP!!!!"
    tf "I guess this is not a safe place to share stories and feelings..."
    show police_allison_smile_eyes with dissolve
    al "Can I shoot him? Please?"
    mc "Okay, but I'm not cleaning up the blood this time."
    hide police_allison_smile_eyes with dissolve
    show police_allison_natural_eyes with dissolve
    al "Alright, there's an alley at the corner. Let's go there and finish this sad man's pathetic life."
    tf "What?! No! Please, don't kill me!"
    tf "This is all happening just because I have a tiny penis. Why, god?! Why!?"
    mc "Relax, moron! We're just kidding!"
    hide police_allison_natural_eyes with dissolve
    show police_allison_laugh_eyes with dissolve
    al "What an idiot..."
    tf "..."
    hide police_allison_laugh_eyes with dissolve
    show police_allison_natural_eyes with dissolve
    al "So, [mc]."
    mc "What?"
    al "How come you're not pathetic like him?"
    mc "What are you talking about?"
    al "Clearly having a tiny penis is a really rough situation to handle."
    al "You must have worked so hard to get over your little problem."
    tf "DUDE! You got a tiny penis and still manage to be a cop?"
    hide police_allison_natural_eyes with dissolve
    show police_allison_laugh_eyes with dissolve
    al "HAHAHAHA."
    mc "SHUT THE FUCK UP! BOTH OF YOU!"
    hide police_allison_laugh_eyes with dissolve
    scene black
    pause 1
    scene policecarblur with fade
    mc "Okay, then."
    mc "Please be a doll and give the car keys and donuts to the pig who lives among the people."
    al "What?! Why me?"
    mc "I've got a date tonight. I need to go home and get ready, sweetie."
    show police_allison_serious_eyes with dissolve
    al "Call me sweetie again and see what happens!"
    mc "Calm down, red! You're gonna melt the car!"
    mc "Please? I really need to go. Just go and give these to that fatty."
    hide police_allison_serious_eyes with dissolve
    show police_allison_natural_eyes with dissolve
    al "Fine! Before you go, though..."
    mc "Yes?"
    al "Be a gentleman and don't cum so quickly! Sex is between two people, and you should respect your partner's needs, too. Also, use a condom. We don't want the babies of you and the dumb brown haired bimbo in this world."
    mc "Anything else?"
    al "Let me think..."
    al "Nope, that's it!"
    mc "See you later, Al."
    al "Go get her, tiger!"
    scene black
    stop music fadeout 0.5
    with fade
    play music "sounds/background2.mp3"
    mc "Today was more eventful than usual."
    mc "Although that fucking purple head gave me a really hard time, meeting Amber made it totally worth it."
    $ renpy.movie_cutscene("texting.webm")
    scene texting
    pause
    scene mcgetready with fade
    mc "Okay, I'm ready!"
    mc "It's been a while since I've been out on a date."
    mc "I hope everything goes smoothly..."
    mc "..."
    mc "I don't really have much time, better be on my way!"
    scene black
    with fade
    scene cfarrive with fade
    mc "I think this is the cafe she was talking about."
    stop music fadeout 0.5
    scene cfwait with fade
    mc "There she is."
    scene cfhello with fade
    play music "sounds/cafe.mp3"
    am "Hi, [mc]."
    am "I hope you didn't have any problem finding this place."
    mc "Hello, Amber."
    mc "No, not at all."
    am "Please, have a seat."
    mc "Thanks!"
    scene cfphone with fade
    mc "Wow, you look really beautiful in that dress."
    scene cffacetoface with fade
    am "You really think so? Thanks."
    am "You also look great but, you looked a lot hotter in police uniform."
    scene cfsit with fade
    show dress_amber_blush2_eyes with dissolve
    am "I did it again, didn't I? I said that out loud."
    mc "Haha, yes. It's fine."
    am "..."
    mc"..."
    mc "So..."
    mc "You are {i}really{/i} into men in uniforms, huh?"
    am "No, it's just... I mean..."
    mc "Hahaha, I'm just teasing you..."
    mc "You look really cute when you blush..."
    hide dress_amber_blush2_eyes with dissolve
    show dress_amber_smile2_eyes with dissolve
    am "Oh, you are so bad!"
    mc "You have no idea..."
    am "Hehe!"
    mc "Anyway..."
    hide dress_amber_smile2_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    mc "Let's order some of that delicious coffee you were telling me about."
    am "You're gonna love this coffee. I'm telling you, when I first moved to this city my friends forced me to try it, but my god it was awesome!"
    mc "Wow! Can't wait to taste it."
    scene cforder with fade
    am "Excuse me, miss, we would like to order."
    wt "Of course, ma'am."
    am "We would like to have two of your special coffees."
    am "One regular, and..."
    mc "I'll have regular, too."
    wt "Of course. I'll be back in a bit with your order."
    scene black
    with fade
    wt "Enjoy your coffee."
    am "Thanks."
    mc "Thanks."
    am "..."
    mc "..."
    scene cffacetoface with fade
    am "So? What do you think?"
    mc "Sweet Jesus, it's delicious."
    scene cfsit with fade
    mc "Did they put Scarlett Johansson and Brad Pitt's sweat in this coffee?"
    show dress_amber_laugh1_eyes with dissolve
    am "Hahaha! I know, right?"
    hide dress_amber_laugh1_eyes with dissolve
    show dress_amber_smile1_eyes with dissolve
    am "I'm really glad you liked it as much as I did."
    scene cffacetoface with fade
    mc "So..."
    mc "Tell me a bit about yourself. What do you do for a living?"
    am "Before that... I want to say thank you, again, for saving me from that horrible man."
    mc "Hey, like I said before, you don't need to thank me. It's my duty to protect the people of this city."
    mc "Though I must say, when someone as beautiful as you gets in any kind of trouble, suddenly I feel this incredible power rising from within me."
    nr "It's called having a boner."
    scene cfsit with fade
    show dress_amber_laugh1_eyes with dissolve
    am "Hahaha."
    hide dress_amber_laugh1_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    am "Are you saying there are other girls as beautiful as I am?"
    mc "Of course not! I don't want to start our friendship with lies. You are the most beautiful girl I've ever seen."
    hide dress_amber_natural1_eyes with dissolve
    show dress_amber_smile1_eyes with dissolve
    am "Really? Gosh, you are so sweet, [mc]."
    mc "(Phew, I dodged a bullet there)"
    mc "Thanks!"
    mc "So, back on topic. You were going to tell me about yourself."
    hide dress_amber_smile1_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    am "Oh, yes!"
    am "Well, where do I begin..."
    am "I just recently moved to this city. I was living with my boyfriend, Jason."
    am "We were working together in a clothing store. He was the manager and I was a sales assistant."
    hide dress_amber_natural1_eyes with dissolve
    show dress_amber_serious1_eyes with dissolve
    am "Everything was going great until I found out that bastard son of a bitch was cheating on me with my best friend, Ashley!"
    am "Of course, at first he denied everything. I decided to follow him on his day off and he went straight to Ashley's apartment."
    am "When I knocked at the door, Jason opened."
    hide dress_amber_serious1_eyes with dissolve
    show dress_amber_angry1_eyes with dissolve
    am "Before he could say anything, I punched him in the face."
    mc "What a piece of shit that Jason guy is. You did the right thing. If I were you, I would do the same, or worse."
    am "Damn right, I did the right thing."
    am "After that I packed my stuff and moved here to stay at a friend's place."
    mc "...and as soon as you moved to a new city, you were attacked by a thief."
    hide dress_amber_angry1_eyes with dissolve
    show dress_amber_sad2_eyes with dissolve
    am "Yes, it feels like only bad things have been happening to me lately."
    am "I was just getting ready to start a new life..."
    mc "I'm so sorry to hear that. Luckily, nothing too bad happened today."
    hide dress_amber_sad2_eyes with dissolve
    show dress_amber_smile1_eyes with dissolve
    am "Yes. I was really lucky. Thanks to you, of course."
    scene cffacetoface with fade
    am "So, it's your turn now."
    am "Let's hear the story of [mc], the brave knight."
    mc "Haha, alright."
    mc "You already know that I'm a police officer."
    am "No! You are not {i}just{/i} a police officer. You are a knight, and a really brave one!"
    mc "Haha! Okay, okay, now {i}I'm{/i} gonna blush..."
    mc "Well, I graduated from the police academy about a year ago as the top recruit in my class."
    am "My, my. Top recruit, you say?"
    am "Yet they make you work in this shitty city?"
    mc "Actually, no one made me work here. It was my decision."
    am "Why is that? With the academy background you just mentioned, you should be able to work in any city you want!"
    mc "That's true, and my superiors said the same."
    mc "Though, I have my own reasons for choosing this city."
    am "...and those reasons are?"
    mc "It's kind of personal, and complicated. I'd rather not talk about it."
    am "Oh, of course! I understand."
    mc "Thank you, Amber."
    mc "Anyway..."
    scene black
    with fade
    nr "..."
    nr "30 minutes later..."
    scene cfsit with fade
    mc "Then the Canadian guy says."
    mc "I don't want to be rude, my good sir, but can you please pull your filthy dick out of my wife's ass?"
    show dress_amber_laugh1_eyes with dissolve
    am "Hahahaha!"
    am "That was really good, but also really offensive."
    mc "What? How is it offensive? The Canadian guy was polite till the end. I give him two thumbs up."
    am "I bet. Before he slept with her, that other guy also gave two thumbs up to his wife."
    mc "You were saying that my joke was offensive, right?"
    hide dress_amber_laugh1_eyes with dissolve
    show dress_amber_smile1_eyes with dissolve
    am "Oops, you caught me."
    mc "Well, I am a police officer, so..."
    am "Shit! How did I forget that?"
    mc "Hehe."
    am "..."
    mc "..."
    scene cffacetoface with fade
    am "Maybe we should continue our evening somewhere else."
    mc "What do you have in mind?"
    am "I know a great club. It's not too far from here..."
    mc "No worries, I got a ride."
    am "Oh! Okay, then. Shall we?"
    mc "Of course."
    scene black
    with fade
    stop music fadeout 1.0
    scene bargetsin with fade
    play music [ "sounds/club1.mp3", "sounds/club2.mp3" ] fadeout 1.0 fadein 1.0
    am "Here we are, Seven Deadly Sins."
    mc "Wow, great name for a club."
    am "Yes! It's great, but sometimes it takes forever to get a drink."
    mc "As long as they get me what I want eventually, I don't really mind."
    mc "Can't believe I live close by and never heard about this place."
    am "Maybe you should get out more."
    mc "Yes, maybe I should."
    am "There is an empty table right over there."
    mc "Yes, let's go."
    scene barsit with fade
    mc "I really like this place."
    am "Glad to hear it."
    am "I feel like I want to get drunk tonight. What about you?"
    mc "The night is young, we'll see what happens."
    mc "I'll go get us some drinks. What can I get you?"
    am "I don't know. Surprise me."
    mc "Alright. Be right back."

    scene barbartender
    with fade



    menu:
        bt "Welcome, dude! Which magical potion do you want?"
        "Absinthe":
            jump gameover1

            bt "You got it, man! There you go."
        "Sex On The Beach":

            bt "You got it, man! There you go."
            jump correctpath1
        "Red Wine":

            bt "You got it, man! There you go."
            jump correctpath1
label gameover1:
    scene barbartender with fade
    mc "Thanks."
    scene barsitglass with fade
    mc "Wow, it's been a while since I drank at a club."
    am "How come?"
    mc "Well... for the past couple of years, my attention has been focused on some important research."
    am "It must be really important if it made you abandon your social life."
    mc "Actually, yes. It's really important. Have you ever heard of the scientist Dr. Eugene Donovan?"
    scene barsitblur with fade
    show dress_amber_surprised1_eyes with dissolve
    am "Of course, I have! He was the Einstein of our generation, but about 10 years ago he suddenly disappeared and everyone assumes that he's dead."
    hide dress_amber_surprised1_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    mc "Yes. Everyone but me."
    mc "I don't believe he's dead, and there's something more behind that incident."
    am "You think so, huh?"
    am "Though, why do you care? I mean, he was an important man and everything but, the way you talk about it..."
    am "It seems like this is personal for you."
    mc "More than personal..."
    mc "He adopted me."
    hide dress_amber_natural1_eyes with dissolve
    show dress_amber_surprised1_eyes with dissolve
    am "No way! I heard that he had a family but...?!"
    mc "Yes. My full name is [mc] Donovan."
    mc "I have two sisters, as well. They're also adopted."
    am "All of you were adopted?"
    mc "Yes. When [vn2] thought the time was right, she told us everything. They tried to have children, but unfortunately they were never able to conceive......"
    hide dress_amber_surprised1_eyes with dissolve
    scene bardrink1 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(0.8, hard=True)
    scene barsitglass with fade
    am "Wow, I'm a bit shocked."
    am "It must've been hard for you, growing up in Dr. Eugene's shadow without even having him in your life."
    mc "It was, at first, but after high school I was used to it. All I want is to find the truth about what happened to him."
    am "That explains why you chose to become a police officer."
    mc "Yes, and I picked this city because it has a really low crime rate and that gives me lots of time to do my research."
    scene barsitblur with fade
    show dress_amber_smile1_eyes with dissolve
    am "Oh, it all makes sense now! A successful student like you usually wouldn't be in this city."
    am "Lucky for me, you had your reasons to be here and it saved my life."
    mc "Yes, lucky for you..."
    hide dress_amber_smile1_eyes with dissolve
    show dress_amber_sad2_eyes with dissolve
    am "Umm, sorry. I didn't mean..."
    mc "No, no. It's fine."
    mc "I just... for a moment..."
    hide dress_amber_sad2_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    mc "I was thinking about how my life would be if my he hadn't disappeared."
    am "I don't know about that. What I do know is you are a brave and smart man, and you have a bright future ahead of you."
    mc "Thanks, Amber."
    scene bardrink1 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(0.8, hard=True)
    scene barsitglass with fade
    mc "I think I'm gonna need another drink. Can I get you something?"
    am "Yes, please."
    mc "Okay, be right back."
    scene barbartender
    with fade
    menu:
        bt "Welcome, dude! Which magical potion do you want?"
        "Absinthe":

            bt "You got it, man! There you go."
            jump gameover2


        "Sex On The Beach":



            bt "You got it, man! There you go."
            jump correctpath2

        "Red Wine":


            bt "You got it, man! There you go."
            jump correctpath2

label correctpath1:
    scene barbartender with fade
    mc "Thanks."
    scene barsitglass with fade
    mc "Wow, it's been a while since I drank at a club."
    am "How come?"
    mc "Well... for the past couple of years, my attention has been focused on some important research."
    am "It must be really important if it made you abandon your social life."
    mc "Actually, yes. It's really important. Have you ever heard of the scientist Dr. Eugene Donovan?"
    scene barsitblur with fade
    show dress_amber_surprised1_eyes with dissolve
    am "Of course, I have! He was the Einstein of our generation, but about 10 years ago he suddenly disappeared and everyone assumes that he's dead."
    hide dress_amber_surprised1_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    mc "Yes. Everyone but me."
    mc "I don't believe he's dead, and there's something more behind that incident."
    am "You think so, huh?"
    am "Though, why do you care? I mean, he was an important man and everything but, the way you talk about it..."
    am "It seems like this is personal for you."
    mc "More than personal..."
    mc "He adopted me."
    hide dress_amber_natural1_eyes with dissolve
    show dress_amber_surprised1_eyes with dissolve
    am "HOLY SHIT!"
    am "No way! I heard that he had a family but...?!"
    mc "Yes. My full name is [mc] Donovan."
    mc "I have two sisters, as well. They're also adopted."
    am "All of you were adopted?"
    mc "Yes. When [vn2] thought the time was right, she told us everything. They tried to have children, but unfortunately they were never able to conceive......"
    hide dress_amber_surprised1_eyes with dissolve
    scene bardrink1 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(0.8, hard=True)
    scene barsitglass with fade
    am "Wow, I'm a bit shocked."
    am "It must've been hard for you, growing up in Dr. Eugene's shadow without even having him in your life."
    mc "It was, at first, but after high school I was used to it. All I want is to find the truth about what happened to him."
    am "That explains why you chose to become a police officer."
    mc "Yes, and I picked this city because it has a really low crime rate and that gives me lots of time to do my research."
    scene barsitblur with fade
    show dress_amber_smile1_eyes with dissolve
    am "Oh, it all makes sense now! A successful student like you usually wouldn't be in this city."
    am "Lucky for me, you had your reasons to be here and it saved my life."
    mc "Yes, lucky for you..."
    hide dress_amber_smile1_eyes with dissolve
    show dress_amber_sad2_eyes with dissolve
    am "Umm, sorry. I didn't mean..."
    mc "No, no. It's fine."
    mc "I just... for a moment..."
    hide dress_amber_sad2_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    mc "I was thinking about how my life would be if my he hadn't disappeared."
    am "I don't know about that. What I do know is you are a brave and smart man, and you have a bright future ahead of you."
    mc "Thanks, Amber."
    scene bardrink1 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrink2 with fade
    pause 0.8
    $ renpy.pause(0.8, hard=True)
    mc "I think I'm gonna need another drink. Can I get you something?"
    am "Yes, please."
    mc "Okay, be right back."
    scene barbartender
    with fade
    menu:
        bt "Welcome, dude! Which magical potion do you want?"
        "Absinthe":

            bt "You got it, man! There you go."
            jump gameover2


        "Sex On The Beach":



            bt "You got it, man! There you go."
            jump correctpath2

        "Red Wine":


            bt "You got it, man! There you go."
            jump correctpath2
label gameover2:
    scene barsitglass with fade
    am "Thank you, [mc]."
    mc "You're welcome."
    scene bardrink1 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(0.8, hard=True)
    scene barsitglass with fade
    am "Wow, two absinthe in a row"
    am "I hope I'm not going too fast."
    mc "You'll be fine, don't worry"
    am "Yes, you're right."
    scene black
    nr "A few sips later..."
    scene bardrink1 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(0.8, hard=True)
    scene bardrunk3 with fade
    am "I think I'm drunk..."
    mc "Nah, you're not drunk."
    mc "We're just having fun, that's all."
    scene bardrunk2 with fade
    am "Then tell me something..."
    am "How the hell am I supposed to have fun with an empty glass?"
    am "There is an emergency empty glass situation, Officer Handsome."
    mc "One more drink, coming right up."
    scene barbartender
    with fade
    menu:
        bt "Welcome, dude! Which magical potion do you want?"
        "Absinthe":

            bt "You got it, man! There you go."
            jump badending


        "Sex On The Beach":



            bt "You got it, man! There you go."
            jump correctpath2

        "Red Wine":


            bt "You got it, man! There you go."
            jump correctpath2
label badending:
    scene barsitglass with fade
    am "Yeeyyyy alcohol!"
    am "I feel so hot."
    am "OH WAIT! Of course. My body needs liquid."
    scene bardrink1 with fade
    $ renpy.pause(0.3, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(3, hard=True)
    mc "..."
    mc "..."
    mc "Hey, you might wanna pace yourself a little bit..."
    scene bardrunk3 with fade
    pause 1
    scene bardrunk2 with fade
    am "HEY THERE, LITTLE GREEN CUTIE."
    mc "Huh?"
    am "[mc], look! There's a fairy on your shoulder."
    am "HEY! DON'T LEAVE ME, CUTE LITTLE FAIRY! COME BACK!"
    am "Oh."
    mc "What?"
    am "Nothing."
    mc "Are you okay?"
    am "Yeah, I'm fine. I just... OH GOD!"
    am "I'M GONNA THROW UP!"
    scene black with fade
    nr "Congratulations, Einstein!"
    nr "From now on, Amber will believe that fairies are real."
    nr "Tinkerbell's grandmother would be so proud of you."
    nr "You are a real hero, and you finished the first release of the game without getting laid."
    nr "Game over, clever boy."
    jump badend
label correctpath2:
    scene barsitglass with fade
    mc "..."
    am "..."
    am "I'm sorry, I didn't mean to sour the mood. Let's change the subject."
    mc "Yeah, sure."
    scene bardrink1 with fade
    $ renpy.pause(2, hard=True)
    scene bardrink2 with fade
    $ renpy.pause(2, hard=True)
    scene bardrunk1 with fade
    am "Is it getting hot in here?"
    mc "Nope. Still the same temperature. Maybe you're getting hotter?"
    am "What?! I'm already super hot, why would I need to get even hotter?"
    mc "I didn't mean it like that."
    scene bardrunk2 with fade
    am "Hehe! I know, I'm just screwing with you."
    am "So, [mc], I've been meaning to ask you..."
    am "Umm..."
    mc "Yes?"
    am "Are seeing anyone?"
    mc "No, I don't have a special someone in my life."
    scene bardrunk1 with fade
    am "Hey! That's something we have in common."
    am "Did I tell you about that cheating son of a bitch ex-boyfriend of mine?"
    mc "Yes, you did."
    am "Are you also cheating son of a bitch, [mc]?"
    mc "No, I'm not."
    am "OF COURSE, YOU'RE NOT!"
    scene bardrunk2 with fade
    am "How did I forget? You're the brave knight who saved my life! Hehe, silly me!"
    am "I think I'm starting to get drunk."
    mc "Yes, it seems so. Maybe we should call it a night..."
    scene bardrunk1 with fade
    am "What?! No way! I can drink. Can you please get us more drinks, handsome?"
    mc "Are you sure?"
    am "What are you talking about? Of course, I'm sure. You are really handsome."
    mc "I wasn't asking that, but sure. I'll get us another drink."
    scene bardrunk2 with fade
    am "Thank you, handsome."
    stop music fadeout 2
label breakingpoint:
    play music [ "sounds/club1.mp3", "sounds/club2.mp3" ] fadeout 1.0 fadein 1.0
    scene barbartender with fade
    mc "Wow. She is {i}not{/i} a heavy drinker, that's for sure."
    mc "I think she's had enough to drink for tonight."
    mc "On the other hand, she is a grown woman so..."

    menu:

        bt "Welcome, dude! Which magical potion do you want?"
        "Club Soda":

            bt "Coming right up!"
            jump correctpath3
        "Absinthe":
            bt "Coming right up!"
            jump badending
        "Sex On The Beach":
            bt "Coming right up!"
            jump badending
        "Red Wine":
            bt "Coming right up!"
            jump badending

label correctpath3:
    scene bardrunk3 with fade
    am "Welcome back, handsome."
    am "Is that for me?"
    am "Hey, what is that?! Water?"
    mc "No, it's not. You've already had a lot to drink and I don't think you'd want to throw up in the middle of the club."
    am "Aww, you are so sweet!"
    am "Most of the guys would try to get me drunk just to get in my pants."
    mc "Well, I am not like them."
    scene bardrunk2 with fade
    am "No, you are definitely {i}not{/i} like them..."
    am "So. It's getting really late. Maybe we should go..."
    mc "Yes, maybe we should."
    am "As I recall, your house is really close to club. Right?"
    mc "Yes..."
    am "I don't think I can handle the long ride home."
    mc "You're more than welcome at my place."
    scene bardrunk3 with fade
    am "There he is, ladies and gentlemen."
    am "Our brave knight will save the lady again."
    mc "Okaaaay."
    mc "Let's go to my place then."
    scene bardrunk2 with fade
    am "Lead the way, Your Highness."
    mc "..."
    scene black with fade
    am "You have a lovely place."
    mc "Thanks!"
    mc "Please make yourself comfortable."
    am "Thanks."
    stop music
    scene black with fade
    scene homeambermc with fade
    play music "sounds/background2.mp3"
    am "I had a great time today."
    am "First, you saved me, and then you made my day."
    mc "I had a great time, too."
    mc "I mean, I had no choice."
    mc "I got to spend my day with a super funny, cute, smart, and extremely beautiful woman."
    scene homeambermcblr with fade
    show dress_amber_flirt2_eyes with dissolve
    am "Really? I was with you the whole time and didin't even see her. Hehe."
    mc "You are indeed beautiful, Amber."
    mc "Though, definitely not lucky."
    hide dress_amber_flirt2_eyes with dissolve
    show dress_amber_laugh1_eyes with dissolve
    am "Hahaha."
    am "Well, maybe not for the last couple of weeks."
    hide dress_amber_laugh1_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    am "Though, if you really think about it, if those unlucky events didn't happen, we wouldn't have met each other."
    mc "Yeah, you're right."
    hide dress_amber_natural1_eyes with dissolve
    show dress_amber_blush1_eyes with dissolve
    am "Hey, [mc], about your partner. The redhead."
    mc "Allison?"
    am "Yes, I was wondering if you guys... you know... were ever... intimate?"
    mc "Well, we are really close and-"
    hide dress_amber_blush1_eyes with dissolve
    show dress_amber_blush2_eyes with dissolve
    mc "Oh! You mean 'intimate'."
    mc "No, we're just friends."
    mc "Why do you ask?"
    hide dress_amber_blush2_eyes with dissolve
    show dress_amber_natural1_eyes with dissolve
    am "Because of the way she looked at you while you were talking to me."
    am "She seemed jealous."
    mc "What?!"
    am "Yes, and to be honest, I'm surprised that you spend 5 days a week with that hot chick and never once tried to put the moves on her."
    mc "It's not like that. She {i}is{/i} gorgeous, but she's my partner. I've never seen her that way, and I'm sure it's the same for her."
    am "I wouldn't be so sure about that..."
    mc "What do you mean?"
    am "Nevermind, let's talk about something else."
    scene homeambermc with fade
    am "Do you smell something?"
    mc "Hmm, I don't know..."
    stop music
    scene ambershy1 with fade
    play music "sounds/sexscene1.mp3"
    am "How about now?"
    mc "I smell... strawberry."
    am "Yes, it's my lipstick."
    am "Do you want to find out if it tastes just like it smells?"
    mc "{i}Gulp{/i}..."
    mc "Yes, please."
    scene homekiss2 with fade
    mc "..."
    scene ambershy1 with fade
    am "So?"
    mc "Oh, yes. It definitely tastes like strawberry."
    am "Do you want some more?"
    mc "Yes!"
    scene homekiss2 with fade
    am "Ohh, [mc]! You're a great kisser."
    scene homekiss1 with fade
    mc "That's because your lips are so delicious. I just can't stop kissing them..."
    am "Mmmm."
    am "..."
    scene ambershy1 with fade
    mc "What's wrong?"
    am "..."
    am "Nothing..."
    mc "Then why did you stop?"
    scene ambershy2 with fade
    am "Well..."
    am "I was wondering..."
    mc "Yes?"
    am "Nevermind, it's a stupid idea."
    mc "What is it? C'mon tell me."
    am "Okay..."
    scene ambershy1 with fade
    am "Could you please put your police uniform on?"
    mc "You want me to... what?"
    am "See? I told you that it was a stupid idea."
    mc "..."
    mc "Yes."
    am "You don't have to be so honest all the time. You can say 'No, no, it's not stupid at all.' "
    mc "That wasn't what I was saying yes to..."
    mc "I was saying yes, I can put on my uniform."
    am "Really?"
    mc "Yes, really."
    scene homekiss2 with fade
    mc "..."
    scene ambershy1 with fade
    am "I think I just came a little bit."
    mc "Hehe."
    mc "Be right back."
    scene mcuniform with fade
    mc "What do you think?"
    am "Yep. This time I literally came in my panties."
    mc "You did WHAT?!"
    mc "I can't simply let this slide..."
    mc "Turn around and put your hands on the wall, young lady."
    am "(Oh, I like the way this is going...)"
    am "...but I didn't do anything wrong, Mr. Officer."
    mc "Do as I say, or else..."
    scene search1 with fade
    am "Of course, Mr. Officer. Please, be gentle with me."
    mc "I am gonna search your entire body, now. DON'T. MOVE."
    scene search2 with fade
    am "Sir? Is getting this handsy really necessary?"
    mc "Don't you dare try to tell me how to do my job, young lady."
    scene search3 with fade
    mc "You've got beautiful legs."
    am "Excuse me...?"
    mc "I mean, it looks like you're clean, but I need to be absolutely sure..."
    scene search4 with fade
    am "Please, sir. I didn't do anything wrong...."
    mc "I said don't move, and stop talking."
    scene search5 with fade
    mc "This will make you shut up."
    mc "Go ahead and suck it."
    am "Mmm..."
    mc "I guess there's no choice..."
    mc "Now, turn around and get on your knees."
    am "Yes, sir. Whatever you say."
    scene gun1 with fade
    mc "I usually use my gun as a last resort, but you are such a dirty girl who needs to know her place."
    am "Wow, sir, you've got a really big gun."
    am "Can I touch it?"
    mc "Go ahead."
    scene gun2 with fade
    am "Oh! It's so hot and hard."
    mc "Maybe you can do something about that."
    am "Maybe I can."
    mc "You're really good at this."
    mc "Ohh, yes! Keep stroking it."
    am "Can I taste your gun, officer?"
    mc "Oh, yes. You sure can..."
    scene gun3 with fade
    am "Mmm, it's delicious."
    mc "Ohhh!"
    am "I want more. I want to taste it even more."
    mc "OH GOD!"
    scene amber_blowjob with fade
    mc "It feels so good."
    am "Slurp Slurp"
    mc "Your lips are amazing."
    mc "Keep going! Don't stop..."
    am "Mmmm..."
    mc "I'm gonna cum..."
    am "Slurp Slurp"
    scene gun2
    am "Yes! Cum all over my face!"
    mc "Oh god, I can't hold it anymore."
    init:
        define flash = Fade(.25, 0.0, .75, color="#fff")
    scene gun4 with flash
    pause 0.3
    scene gun4 with flash
    pause 0.5
    scene gun4 with flash
    mc "OHHH YESSS, OH GOD."
    am "MMMM"
    am "..."
    am "Wow, you came so much."
    mc "Holy fuck, Amber!"
    mc "You are amazing."
    am "Hehe. Your uniform really motivated me."
    mc "This was a first for me. I've never worn my uniform during sex, but god was it amazing."
    am "So... I hope your gun has more bullets in it."
    mc "Oh, baby, don't worry about that."
    mc "Because now it's my turn to make you feel good."
    scene black with fade
    mc "Wow, you're soaking wet."
    am "It's because of you. You should take responsibility for that."
    mc "Don't worry, babe. I'll make you feel good."
    scene lick with fade
    mc "I can't wait to taste this sweet juice."
    am "Mmm! Yes! Just like that."
    am "Eat my delicious pussy, [mc]."
    mc "Mmm."
    am "AHHH! GOD, YES!"
    am "That feels soo good."
    am "I want you..."
    am "I want you inside of me."
    am "Put your fucking dick in me."
    mc "Oh, you want it, hm?"
    mc "How bad do you want it?"
    am "More than anything I've ever wanted."
    am "Please, [mc], don't torture me."
    am "I need you."
    scene amber_doggy with fade
    am "OH YESS!"
    mc "Do you like my cock in your tight little pussy?"
    am "OH GOD, YES!"
    am "I love your cock so much"
    am "YES! YES! YES!"
    mc "OH GOD! It feels so good."
    mc "Your pussy is so wet and tight."
    am "Oh yes, [mc]. My pussy is so wet for you."
    am "It longs for your huge cock."
    mc "Oh! Oh god! Yes!"
    menu:
        "Faster":
            jump doggyfast
        "Cow Girl":
            jump cowgirl2
        "Blowjob":
            jump blowjob
        "Cum":
            mc "I AM GONNA CUM!!!"
            jump climax1
label doggy:
    scene amber_doggy
    am "OH GOD, YESS!"
    mc "Your pussy feels so good."
    "..."
    menu:
        "Faster":
            jump doggyfast
        "Cow Girl":
            jump cowgirl2
        "Blowjob":
            jump blowjob
        "Cum":
            mc "I AM GONNA CUM!!!"
            jump climax1
label cowgirl2:
    scene amber_cowgirl2
    mc "God, you're so hot."
    mc "Just like that. Keep going."
    am "Your cock is amazing."
    am "I love it... I love it so much."
    "..."
    menu:
        "Faster":
            jump cowgirl2fast
        "Doggy":
            jump doggy
        "Blowjob":
            jump blowjob
        "Change Angle":
            jump cowgirl1
        "Cum":
            mc "I AM GONNA CUM!!!"
            jump climax1
label cowgirl1:
    scene amber_cowgirl1
    pause
    menu:
        "Faster":
            jump cowgirl1fast
        "Doggy":
            jump doggy
        "Blowjob":
            jump blowjob
        "Change Angle":
            jump cowgirl2
        "Cum":
            mc "I'M GONNA CUM!!!"
            jump climax1
label blowjob:
    scene amber_blowjob
    mc "OH MY GOD! Amber, you are the best."
    mc "Keep sucking go deeper."
    menu:
        "Faster":
            jump blowjobfast
        "Cow Girl":
            jump cowgirl2
        "Doggy":
            jump doggy
        "Cum":
            mc "I'M GONNA CUM!!!"
            jump climax1
label blowjobfast:
    scene amber_blowjobfast
    mc "Oh, yes!"
    menu:
        "Slower":
            jump blowjob
        "Cow Girl":
            jump cowgirl1
        "Doggy":
            jump doggy
        "Cum":
            mc "I'M GONNA CUM!!!"
            jump climax1

label doggyfast:
    scene amber_doggyfast
    am "Keep pounding my firm ass, [mc]!"
    am "Faster! Harder!"
    menu:
        "Slower":
            jump doggy
        "Blowjob":
            jump blowjob
        "Cow Girl":
            jump cowgirl2
        "Cum":
            mc "I'M GONNA CUM!!!"
            jump climax1
label cowgirl2fast:
    scene amber_cowgirl2fast
    mc "You wild, crazy slut."
    mc "Don't you dare stop!"
    mc "OH YES!"
    menu:
        "Slower":
            jump cowgirl2
        "Doggy":
            jump doggy
        "Blowjob":
            jump blowjob
        "Change Angle":
            jump cowgirl1fast
        "Cum":
            mc "I'M GONNA CUM!!!"
            jump climax1
label cowgirl1fast:
    scene amber_cowgirl1fast
    pause
    menu:
        "Slower":
            jump cowgirl1
        "Doggy":
            jump doggy
        "Blowjob":
            jump blowjob
        "Change Angle":
            jump cowgirl2fast
        "Cum":
            mc "I'M GONNA CUM!!!"
            jump climax1



label climax1:
    scene amberclimax with flash
    pause 0.5
    scene amberclimax with flash
    pause 0.6
    scene amberclimax with flash
    pause 0.3
    scene amberclimax with flash
    pause 1.2
    mc "Holy shit, that was amazing!"
    am "God, yes. That was the best sex I've ever had."
    mc "I am glad to hear that..."
    am "..."
    mc "..."
    am "How about you?"
    mc "Meh, I've had better."
    am "How dare you!"
    mc "Haha! Calm down, I was joking."
    mc "It was one of the best sexual experiences I've ever had."
    mc "You were incredible."
    am "Oh, I know."
    mc "You and your smug attitude."
    am "Maybe you should've banged me a little harder."
    mc "Maybe I should've."
    stop music fadeout 2.0
    scene black with fade
    am "I should sleep. I have to be up early."
    mc "Tomorrow is my day off, but I'm pretty worn out after that. I could really use some sleep."
    mc "Goodnight, Amber."
    am "Goodnight, [mc]."
    scene mcphone with fade
    play music "sounds/background1.mp3"
    mc "It's almost 10.00 AM."
    mc "It's been a while since I've slept this well and this long."
    mc "She wasn't kidding about getting up early."
    mc "I was hoping to fool around a little bit more this morning"
    scene mcmorning1 with fade
    mc "I focused so much on [eg1]'s case that I'd forgotten what it's like to have some fun from time to time."
    mc "I should give Amber a call and tell her thanks for reminding me of that."
    stop music
    scene black
    mc "Ouch!"
    mc "What-"
    scene morning2
    mc "What is that?"
    mc "Did something bite me?"
    mc "I... I don't feel so goo-"
    play sound "sounds/falldown.mp3" fadein 0.5
    scene black
    pause 0.7
    scene morning3 with fade
    mc "..."
    scene mcfaint
    mc "..."
    scene mcmorning4 with fade
    mc "..."
    ukn "I'm sorry that we had to meet this way, but it's all for your sake."
    mc "Who are you?"

    scene black with fade
label sorgu:
    show screen button1
    show screen mcStats
    if allison_met == False:
        $ allison_met = True

    if amber_met == False:
        $ amber_met = True

    scene introom01 with fade
    play music "sounds/sorgu.mp3"
    mc "..."
    mc "Ahhhhhhh!"
    mc "Where am I?!"
    mc "Oh, my head hurts so much..."
    hr "Good morning, [mc]."
    mc "What the hell is going on? Who are you?"
    hr "My name is Haruka. I'm a Special Agent with the Secret Intelligence Department."
    if haruka_met == False:
        $ haruka_met = True

    hr "I'm sorry for bringing you here this way, but we had no choice."
    hr "Your life was in danger and we were forced to move quickly."
    scene introom02 with fade
    mc "Just... wait a moment. The last thing I remember..."
    mc "I was at my home."
    mc "I felt something on the back of my neck, and there was a woman at my door."
    hr "As I said, we had to move quickly."
    hr "If we had waited any longer, they would've come to kill you."
    scene introom08 with fade
    hr "I know you must have a lot of questions. I will do my best to answer all of them."
    hr "So, relax and calm down."
    mc "How exactly do you expect me to relax?!"
    mc "You broke into my home, abducted me, and now you're telling me to calm down and relax?!"
    hr "I completely understand how you feel and why you're angry right now."
    hr "I only did what I had to do in order to save your life."
    mc "WAIT!"
    mc "Was Amber abducted, too? She was with me last night but when I woke up-"
    hr "You needn't worry, she was already gone when we arrived at your place."
    mc "Fine. Let's say all those things you're telling me are true."
    mc "Why is my life in danger?"
    mc "Who are these people that are out to get me?"
    mc "What exactly is this Secret Intelligence Department?"
    mc "Though, most importantly..."
    mc "Why should I trust you or believe anything you say?!"
    scene introom03 with fade
    hr "Let's start from the beginning."
    hr "Your life was always in danger."
    hr "Dr. Donovan's disappearance was quite unusual and highly suspect-"
    mc "WAIT!"
    mc "You know about [eg6]'s disappearance?!"
    scene introom03blr with fade
    show haruka1 with dissolve
    hr "Yes. We have information regarding his disappearance."
    hr "Do not worry. I will tell you everything we know."
    hr "After Dr. Donovan's incident, the Secret Intelligence Department started its own investigation into the matter."
    hr "As you are aware, the manner in which Dr. Donovan disappeared was highly unusual. Dealing with abnormal events is our department's specialty."
    hr "After completing our investigation, we were able to reach a definitive conclusion."
    mc "..."
    hr "What I am about to tell you will be difficult to believe, but..."
    mc "Just tell me."
    hr "Dr. Eugene Donovan was captured by unknown assailants who invaded our world from a parallel universe."
    mc "..."
    mc "WHAT?! Do you {i}really{/i} expect {i}me{/i} to believe this bullshit?!"
    hr "Believe it or not, it {i}is{/i} the truth."
    hr "The same group wants to kill you and your family."
    hr "That group kept sending more agents, but we've managed to protect you and your family."
    hr "After you left home to join the police force, we continued to observe you in order to keep you safe."
    hr "I am unsure if I should reveal more about the situation to you."
    mc "What makes you say that?"
    hide haruka1 with dissolve
    show haruka2 with dissolve
    hr "I do not know if you are ready..."
    mc "Ready for what?"
    hr "We are at war, [mc]. We are at war against the parallel universe."
    hr "Dr. Donovan's incident was only the beginning."
    hr "After that, they captured several politicians, scientists, and military leaders from all over the world. This world."
    hr "They already know {i}so much{/i} about us."
    hr "Dr. Donovan was the one who discovered this threat. As far as we are aware, he never shared his discovery with anyone outside of the organization."
    mc "If that's the case, how do {i}you{/i} know all of this?!"
    hr "Dr. Donovan believed that they would come for him. He told me of his discovery and shared with me all of the evidence he had compiled."
    hr "I was just as you are now. I didn't want to believe him."
    mc "All the things you are telling me..."
    mc "About [eg1], this other universe, and the war..."
    mc "I just can't believe them. I mean, how could I?"
    hr "That's why I told {i}her{/i} to join us."
    hr "You can come in, agent."
    mc "..."
    scene introom04 with fade
    mc "!!!"
    al "Hello, [mc]."
    mc "ALLISON!?"
    scene introom05 with fade
    mc "What are you doing here?!"
    mc "What the hell is going on?!"
    hr "I told you that we've been keeping a close eye on you."
    mc "No..."
    mc "Allison, you-"
    mc "You're with them...?"
    mc "No! You and I, we're partners. We're friends..."
    al "I am sorry, [mc]."
    mc "OH GOD!"
    mc "I feel like my head is about to explode."
    hr "I know this is a lot to take in, but you must calm down."
    mc "How did you do it, Allison?"
    mc "Pretending to be my friend... Being there for me whenever I need..."
    mc "Are you telling me all of that was a lie?"
    al "I'm sorry, [mc], but now is not a good time to talk about it."
    al "I will tell you everything when the time is right."
    hr "Thank you, Allison."
    hr "Look, [mc]. I understand that this must be overwhelming for you to try and comprehend."
    hr "However, I need you to be calm and just relax. You are about to learn something very important."
    al "Not just for you, but for all of us."
    mc "Oh, Allison, you-"
    mc "..."
    mc "Okay."
    scene introom06 with fade
    mc "I'll try my best."
    al "..."
    hr "Thank you, [mc]."
    al "You already know that Dr. Donovan was working with the government and the military."
    al "Our President personally gave him an extremely important assignment."
    al "He was tasked with creating super soldiers."
    scene introom07 with fade
    mc "He... what?"
    hr "In order to complete his objective, he gathered a team of scientists. One of those very scientists was Vanessa, as I'm sure you were aware."
    hr "He and his team worked tirelessly around the clock, but were unable to reach a breakthrough."
    hr "While performing research on his assigned task, Dr. Eugene Donovan was also working on a separate, secret project which he did not disclose to anyone. Including his wife, Vanessa."
    hr "He had a theory about the parallel universe and different timelines that we could not see or feel."
    scene introom06 with fade
    al "Are you familar with the term Deja Vu and what it entails, [mc]?"
    mc "Yes."
    al "According to Dr. Donovan, when we feel Deja Vu, what we're actually feeling is a glimpse of ourselves from some sort of alternate timeline, like a parallel universe."
    al "He was certain that there must be a way to see or enter this parallel universe."
    hr "He was correct in his assertion."
    hr "[mc], Dr. Donovan was able to visit the other side where he learned the terrible truth."
    hr "They were already aware of us, and were preparing an assault on us here in this timeline."
    al "Being the target of parallel versions of ourselves was already extremely dangerous, but there was more..."
    al "Their military force and technological development were far more advanced than our own."
    mc "Why would they want to attack us? What is their true motive?"
    scene introom06blr with fade
    show haruka1 at right with dissolve:
        xpos 1750
    show allison1 at left with dissolve:
        xpos 150

    show haruka1 at right:
        ease .5 zoom 1.1 xpos 1750
    hr "Unfortunately, we do not know yet."

    hr "The only person privy to many specifics about the other world is Eugene Donovan."
    hr "That is why they thought he was the most important person to our world, but there was someone they were not aware of."
    hr "That person... is you!"
    hr "[mc], you are our savior."
    show haruka1 at right:
        ease .5 zoom 1.0 xpos 1750
    mc "..."
    mc "Me? How? Why?"
    show allison1 at left:
        ease .5 zoom 1.1 xpos 150
    al "Do you remember Dr. Donovan's main research?"
    mc "Yes, he was tasked with creating super soldiers."
    al "He achieved success in creating super soldiers."
    al "He realised that to able to make someone special, that person must born with some sort of supergene that he and his team created."
    show allison1 at left:
        ease .5 zoom 1.0 xpos 150
    show haruka1 at right:
        ease .5 zoom 1.1 xpos 1750
    hr "Their first success was your sister, Olivia."
    hr "After her, you and your little sister, Daisy."
    show allison1 at left:
        ease .5 zoom 1.1 xpos 150
    al "Technically, they aren't your sisters."
    show allison1 at left:
        ease .5 zoom 1.0 xpos 150
    hr "Olivia and Daisy are {i}not{/i} your biological sisters."
    hr "...but, the three of you {i}are{/i} related."
    hr "All three of you share the same supergene..."
    hr "...and all three of you have special abilities."
    mc "Are you kidding me?"
    hr "I understand that this is difficult to fathom."
    hr "The three of you were the result of Dr. Eugene's research into the supergene. You were all created in a lab."
    hr "Olivia, Daisy, and yourself are all biologically diverse. Your only relation is in the supergene that gives the three of you special abilities."
    show haruka1 at right:
        ease .5 zoom 1.0 xpos 1750
    mc "Are you kidding me?"
    mc "What is this, some kind of caught on camera prank?"
    mc "Do you really think that I would believe any of this bullshit?"
    mc "Supergene, special abilities, a parallel world..."
    mc "You must think that I am really stupid!"
    mc "I heard enough."
    mc "I want to leave now."
    show allison1 at left:
        ease .5 zoom 1.1 xpos 150
    al "You can't leave."
    al "Don't you understand? Why would we lie to you? We need you, because you are also-"
    show allison1 at left:
        ease .5 zoom 1.0 xpos 150
    show haruka1 at right:
        ease .5 zoom 1.1 xpos 1750
    hr "That's enough, Allison."
    hr "If he wishes to leave, let him."
    hr "You don't have to believe us, [mc], because it doesn't matter. What we are telling you is the truth, whether you believe it or not."
    hr "Our base of operations is in the same city as your family's home."
    hr "Go and be with your family. Gather yourself and think about everything we've just told you."
    show haruka1 at right:
        ease .5 zoom 1.0 xpos 1750
    hide haruka1 with dissolve
    hide allison1 with dissolve
    scene introom07 with fade
    mc "Yeah, I'll do that."
    mc "Goodbye."
    stop music fadeout 0.5

label samantha1:
    play music "sounds/street.mp3"
    scene black with fade
    mc "..."
    mc "{i}(I can't believe this.){/i}"
    mc "{i}(What were they thinking? Who would have believed any of this? And Allison...){/i}"
    mc "{i}(She was a spy?){/i}"
    mc "Fuck my life."
    ukn "I can't blame you."
    ukn "Sometimes I say the same thing about my life."
    scene street01 with fade
    mc "What?"
    mc "Who are you?"
    ukn "Hello, [mc]."
    scene street02 with fade
    st "My name is Samantha."
    if samantha_met == False:
        $samantha_met = True
    mc "How do you know my name?"
    st "I know lots of things about you, [mc]."
    st "Those who abducted you weren't being completely honest with you."
    st "If you really want to know the truth, meet me at this address."
    mc "IF YOU GOT SOMETHING TO SAY, SAY IT NOW!"
    st "Calm down! There's no need to yell at me."
    st "Meet me at this address after you visit your family. I'm sure they would love to see you."
    mc "No. You're gonna tell me. Right now."
    st "You are in no position to tell me what to do, [mc]."
    st "I'll see you soon."
    mc "..."
    stop music fadeout 0.5
    scene black with fade
label home1:
    scene home01 with fade
    play music "sounds/background2.mp3"
    mc "It's been a while since I've been back to this old place."
    mc "Everything looks the same."
    mc "Alright, here we go."
    mc "..."
    vn "Olivia, could you get the door?"
    ol "Sorry, [vn1], I'm busy!"
    vn "Daisy!"
    ol "She's in her room, she can't hear you."
    scene black with fade
    vn "Alright..."
    scene home02 with fade
    if vanessa_met == False:
        $ vanessa_met = True
    vn "..."
    mc "Hi, [vn1]!"
    scene home03 with fade
    vn "[mc]! IT'S REALLY YOU!"
    scene home04 with fade
    vn "Oh! I missed you so much, honey!"
    vn "How long has it been since the last time I've seen you?"
    mc "Too long."
    scene home05 with fade
    vn "Oh, look at you! You look great! I almost didn't recognize you..."
    mc "Thanks."
    scene home06 with fade
    vn "Olivia, come here and bring Daisy with you! I have a surprise for you."
    ol "Okay."
    ol "Daisy! Come downstairs, [vn1] says she has a surprise for us!"
    ds "Fine."
    scene home07 with fade
    if olivia_met == False:
        $olivia_met = True
    ol "Okay, I'm here. So, what is this surprise you are talking about?"
    ol "..."
    mc "Hello, Liv."
    mc "Long time, no see."
    ol "[mc]?! I can't believe it! I've missed you so much!"
    scene home08 with fade
    ol "Come here, you asshole."
    mc "Hey, language."
    ol "Oh, shut up! You never called or texted me. You {i}are{/i} an asshole."
    mc "I was busy."
    scene home07 with fade:
        zoom 1.2
    ol "Too busy to spare some time for your family?"
    vn "Alright, that's enough."
    vn "I'm sure he had a good reason."
    ol "Wow. After all this time, you are still the favorite child in this house."
    mc "Are you kidding me? You were always her favorite child. Daisy and I were like a free bonus next to you."
    vn "You know that's not true, [mc]. I love you all equally."
    mc "I know, [vn1]. I'm just kidding around with Olivia."
    scene black
    scene home07 with dissolve:
        size (2500, 1400) zoom 1.3 xoffset -1300
    if daisy_met == False:
        $ daisy_met = True
    ds "..."
    mc "So, who is that beautiful young lady who doesn't give a damn about me?"
    ds "Hello, [mc]."
    mc "..."


    scene home13 with fade:

        xpos 0.7 ypos 1.0 xanchor 0.66 yanchor 0.93 zoom 1.1
        linear 4 yanchor 0.32

    mc "That's it? Just hello?"
    mc "C'mon, give me a hug."
    ds "Thanks, but no."
    mc "Ah. Okay, then."
    scene home07 with fade
    ol "Don't mind her. She's like that towards everyone."
    ol "Classic teenage years."
    mc "Sure, I get that."
    vn "Oh, dinner is almost ready!"
    vn "I am sure you must be hungry."
    mc "Oh, yes, I am, and I miss those meals you used to make so much."
    vn "You are so sweet, [mc]."
    stop music fadeout 0.3
    scene home09 with fade
    play music "sounds/cafe.mp3"
    mc "Everything looks great."
    vn "Thank you, honey! If I had known that you are going to join us for dinner, I've would prepared something special."
    mc "Everything you make for us is special."
    ol "Oh, somebody please shoot me! Hey, [mc]! Where did you learn to be master kiss ass, at Police Academy or long tongue tribe?"
    ds "Hahaha."
    mc "Hey, I'm just being nice."
    vn "...and I appreciate it."
    vn "Enjoy your meal, darling."
    mc "Thank you."
    scene home09blr with fade
    show vanessa1  with dissolve
    vn "So, [mc], tell us about your life. How is work going?"
    mc "..."
    vn "[mc]?"
    mc "Oh, sorry..."
    mc "Everything is going great. My life is quite simple and unexciting. There isn't much to tell."
    vn "Okay. Have you met someone special?"
    mc "Actually, I recently met someone. Her name is Amber."
    hide vanessa1 with dissolve
    show vanessa3 with dissolve
    vn "OH! Really?"
    mc "She's really nice, and so much fun."
    vn "Maybe we will get to meet her someday?"
    mc "Yes, maybe."
    hide vanessa3 with dissolve
    label dinnertalk:
    scene home09
    menu:
        "Talk to Olivia":
            if v2_oliviatalk == True:
                jump olivia
            mc "{i}(I've already spoken to her.){/i}"
            jump dinnertalk

        "Talk to Daisy":
            if v2_daisytalk == True:
                jump daisy
            mc "{i}(I've already spoken to her.){/i}"
            jump dinnertalk
        "Talk to Vanessa":
            if v2_vanessatalk == True:
                jump vanessa
            mc "{i}(I've already spoken to her.){/i}"
            jump dinnertalk
        "That's Enough Talk, Let's Eat":
            if v2_oliviatalk == False and v2_daisytalk == False:
                jump dinner
            "{i}(I haven't spoken to everyone yet.){/i}"
            jump dinnertalk

label olivia:
    menu:
        "How Is Your Life Going?":
            if v2_oliviatalk1 == True:
                jump oliviatalk1
            mc "{i}(I've already asked her that){/i}"
            jump olivia
        "Where Do You Work?":
            if v2_oliviatalk2 == True:
                jump oliviatalk2
            mc "{i}(I've already asked her that){/i}"
            jump olivia
        "Do You Have Anyone Special In Your Life?":
            if v2_oliviatalk3 == True:
                jump oliviatalk3
            mc "{i}(I've already asked her that){/i}"
            jump olivia
        "Talk to someone else":
            if v2_oliviatalk == True:
                $ v2_oliviatalk = False
            jump dinnertalk
label oliviatalk1:
    if v2_oliviatalk1 == True:
        $ v2_oliviatalk1 = False
        scene home12
        mc "How is your life going?"
        scene home12blr with fade
        show olivia2 with dissolve
        ol "My life's okay. I've got a decent job and I have a nice PC that easily runs the latest games."
        mc "You still play video games?"
        ol "Of course, I do!"
        ol "Gamer for life!"
        hide olivia2 with dissolve
        scene home12
        jump olivia


label oliviatalk2:
    if v2_oliviatalk2 == True:
        $ v2_oliviatalk2 = False
        scene home12
        mc "You were always interested in computers and tech stuff."
        mc "I bet your work has something to do with computers."
        scene home12blr with fade
        show olivia3 with dissolve
        ol "Yes! I'm a Software Engineer."
        ol "I work at SID."
        mc "SID?"
        ol "Secret Intelligence Department."
        mc "WHAT?!"
        mc "How? Why...?"
        hide olivia3 with dissolve
        show olivia2 with dissolve
        ol "After graduating from MIT, I received an email inviting me to a job interview. After a one year internship, they finally gave me a full-time job."
        ol "I understand your concern. [vn1] had the same reaction when she heard about SID, but don't worry. My job is really simple and safe."
        mc "..."
        show olivia2 at right with dissolve:
            xpos 1750
        show vanessa1 at left with dissolve:
            xpos 150
        show vanessa1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "Yes, she's been working there for 3 years, and she's really happy there."
        show vanessa1 at left:
            ease .5 zoom 1.0 xpos 150
        mc "As long as you are happy..."
        mc "{i}(I don't like this at all...){/i}"
        hide vanessa1 with dissolve
        hide olivia2 with dissolve
        scene home12
        jump olivia

label oliviatalk3:
    if v2_oliviatalk3 == True:
        $ v2_oliviatalk3 = False
        scene home12
        mc "So, do you have boyfriend?"
        scene home12blr with fade
        show olivia3 with dissolve
        ol "Umm, yes. I do."
        hide olivia3 with dissolve
        show daisy1 at left with dissolve:
            xpos 150
        ds "Yeah, right. Haha."
        show olivia2 at right with dissolve:
            xpos 1750
        show olivia2 at right:
            ease .5 zoom 1.1 xpos 1750
        ol "Shut up, Daisy!"
        show olivia2 at right:
            ease .5 zoom 1.0 xpos 1750
        mc "What's going on?"
        show daisy1 at left:
            xpos 150
        show daisy1 at left:
            ease .5 zoom 1.1 xpos 150
        ds "We've never met this 'boyfriend' she's talking about, that's all."
        show daisy1 at left:
            ease .5 zoom 1.0 xpos 150
        show olivia2 at right:
            ease .5 zoom 1.1 xpos 1750
        ol "Just because you haven't met him yet doesn't mean he doesn't exist!"
        show olivia2 at right:
            ease .5 zoom 1.0 xpos 1750
        mc "Relax, Olivia, I'm sure you have your own reasons for not introducing him to anyone yet."
        ds "I know the reason."
        mc "That's enough, Daisy. You're taking this joke too far."
        ol "Thank you, [mc]."
        hide daisy1 with dissolve
        hide olivia2 with dissolve
        scene home12 with fade
        jump olivia


label daisy:
    menu:
        "You Seem To Really Like Your Phone?":
            if v2_daisytalk1 == True:
                jump daisytalk1
            mc "{i}(I've already asked her that){/i}"
            jump daisy
        "I Really Like Your Style.":
            if v2_daisytalk2 == True:
                jump daisytalk2
            mc "{i}(I've already asked her that){/i}"
            jump daisy
        "Do You Have Any Plans For College ":
            if v2_daisytalk3 == True:
                jump daisytalk3
            mc "{i}(I've already asked her that){/i}"
            jump daisy
        "Talk someone else":
            if v2_daisytalk == True:
                $ v2_daisytalk = False
            jump dinnertalk
label daisytalk1:
    if v2_daisytalk1 == True:
        $ v2_daisytalk1 = False
        scene home11
        mc "You seem to really like your phone."
        mc "Are you texting someone important?"
        ds "Nope, just chatting with some friends and sending some selfies."
        mc "Maybe you'd like to put the phone down for a moment so we can catch up?"
        ds "Don't worry, I can text and talk at the same time."
        mc "That's great to hear."
        vn "Honey [mc] wants to catch up with your life, can you please be nice and show some interest to him?"
        ds "Define some..."
        mc "No, no. It's completely fine."
        jump daisy
label daisytalk2:
    if v2_daisytalk2 == True:
        $ v2_daisytalk2 = False
        scene home09
        mc "I really like your style, Daisy."
        scene home09blr with fade
        mc "Especially your hair color."
        show daisy2 with dissolve
        ds "Thanks..."
        mc "I must say, I'm surprised [vn1] allowed you to change your hair and wear all those piercings."
        show daisy2 at right with dissolve:
            xpos 1750
        show vanessa2 at left with dissolve:
            xpos 150
        vn "I didn't allow any of them."
        hide daisy2 with dissolve
        show daisy3 at right:
            xpos 1750
        show daisy3 at right:
            ease .5 xpos 1750 zoom 1.1
        ds "Well, I didn't ask you in the first place."
        mc "Okay, girls, calm down. I think you look lovely, Daisy."
        ds "Thank you, [mc]. Finally, someone in this fucking family said something nice about me."
        show vanessa2 at left:
            ease .5 xpos 150 zoom 1.1
        vn "Watch your tongue, young lady."
        show daisy3 at right:
            ease .5 xpos 1750 zoom 1.0
        ds "..."
        hide vanessa2 with dissolve
        hide daisy3 with dissolve
        scene home09
        jump daisy
label daisytalk3:
    if v2_daisytalk3 == True:
        $ v2_daisytalk3 = False
        scene home09
        mc "Do you have a particular field you want to major in when you go off to college?"
        scene home09blr with fade
        show olivia1 at right with dissolve:
            xpos 1750
        ol "Who? Daisy? Hahaha!"
        show daisy3 at left with dissolve:
            xpos 150
        ds "What's so funny?"
        mc "..."
        ol "Nothing."
        hide olivia1 with dissolve
        hide daisy3
        show daisy2 with dissolve
        ds "No, [mc]. I haven't really thought about that."
        show daisy2 at right:
            xpos 1750
        show vanessa1 at left with dissolve:
            xpos 150
        vn "I am glad you bring that up, [mc]. I've been telling her that she needs to decide what she wants in her life, but she doesn't take me seriously."
        hide daisy2 with dissolve
        show daisy3 at right with dissolve:
            xpos 1750
        ds "No need to make it personal, [vn1]. I don't take anyone seriously, so it's not only you."
        mc "{i}(Seems like things are a bit tense between [vn1] and Daisy...){/i}"
        hide daisy3 with dissolve
        hide vanessa1 with dissolve
        scene home09
        jump daisy
label vanessa:
    menu:
        "You Look Lovely As Always.":
            if v2_vanessatalk1 == True:
                jump vanessatalk1
            mc "{i}(I've already said that){/i}"
            jump vanessa
        "Are You Still Working At The Same Lab?":
            if v2_vanessatalk2 == True:
                jump vanessatalk2
            mc "{i}(I've already said that){/i}"
            jump vanessa

        "Talk someone else":
            if v2_vanessatalk == True:
                $ v2_vanessatalk = False
            jump dinnertalk
label vanessatalk1:
    if v2_vanessatalk1 == True:
        $ v2_vanessatalk1 = False
        scene home10
        mc "After all this time, you're still as pretty as ever."
        vn "Thank you, honey! You're gonna make me blush."
        vn "Eat as much as you'd like, I made plenty."
        mc "Thanks!"
        jump vanessa
label vanessatalk2:
    if v2_vanessatalk2 == True:
        $v2_vanessatalk2 = False
        scene home10
        mc "Are you still working at the same lab?"
        vn "Yes, honey. After [eg4] vanished, it was really hard for me to maintain the lab. Everyone was working as hard as they could."
        mc "So, who is the new boss?"
        vn "Me. I took over his research {i}and{/i} I started my own research projects."
        mc "{i}(I really want to ask her questions about [eg1]'s research, but I think it's too soon.){/i}"
        mc "That's great! I'm really happy for you, [vn1]."
        vn "Thank you, honey."
        jump vanessa



label dinner:
    scene home09 with fade
    mc "It's been a while since I've eaten something so delicious."
    scene home09blr with fade
    show vanessa1 with dissolve
    vn "Thank you, honey! I hope you aren't always ordering pizza or eating junk food. You should cook for yourself once in a while."
    mc "Of course, I cook for myself. It's just, well... compared to yours, my cooking doesn't really compare."
    vn "Aww, don't say that! If it's not too much to ask, I'd love to eat something you've made sometime."
    mc "Sure. It would be my pleasure."
    hide vanessa1 with dissolve
    scene home09
    vn "Okay, girls, help me to clean up the table."
    ds "Fine..."
    ol "Sure."
    ds "By the way, I invited my friend Robin to spend the night."
    vn "Okay, honey."
    vn "You know she's always welcome here."
    mc "Umm... I'm going to go for a walk for a while. I won't be out too late."
    vn "Okay, honey. Let me give you the spare key, just in case."
    mc "Thanks."
    stop music fadeout 0.5
label park:
    scene later with fade
    $ renpy.pause(2.0, hard=True)
    play music "sounds/park.mp3"


    scene park01 with fade
    mc "{i}(This is the address she gave to me.){/i}"
    mc "{i}(First, Haruka and Allison. Now, this woman.){/i}"
    mc "{i}(They're all trying to manipulate me with their lies.){/i}"
    mc "{i}(If this, what's her name...? Samantha? If she doesn't stop playing bullshit games with me, I'm going lose my patience.){/i}"
    scene park02 with fade
    st "Welcome, [mc]."
    st "I must say I'm a bit surprised. I didn't think you would show up."
    mc "I wasn't sure I wanted to meet you, either, but today's already been really strange, so I thought 'Why the hell not?'"
    st "I'm glad you decided to come."
    st "There are many important things I must tell you."
    st "Please, have a seat."
    st "I know you must have a lot of questions."
    mc "You think?"
    scene park03 with fade
    mc "Today, I was drugged and abducted, found out my partner has been lying to me since the day we met, and..."
    st "Yes?"
    mc "...and that's all."
    st "You missed the part about Dr. Donovan and the parallel universe."
    mc "How do you know about that?"
    scene park03blr with fade
    show samantha1 with dissolve
    st "I know because you're not the only one they've spun this fairy tale for."
    st "That's how their operation works."
    st "First, they watch your every move, then they come for you when they think the time is right."
    st "We were ready to reach out to you, but they were faster than we anticipated and managed to capture you."
    st "Everything you were told about this supposed war with a parallel universe was a lie."
    mc "So, you're telling me they're lying in order to manipulate me?"
    mc "But, why?"
    hide samantha1 with dissolve
    show samantha2 with dissolve
    st "That bit about the super-soldier experiment? That part is actually true."
    st "They wish to recruit you, but only to further their own goals."
    mc "But you're only interested in my well-being, right?"
    st "Yes."
    mc "Yeah, right. I'm sorry, but who were you guys?"
    st "That... I cannot reveal to you yet."
    mc "Alright..."
    mc "If you know everything about me, and everything that happened to me today, I'm sure you must have some idea about what happened to [eg6]."
    hide samantha2 with dissolve
    show samantha1 with dissolve
    st "Actually, yes. We know much about Eugene Donovan and where he might've gone."
    mc "Oh, really, now? That's so wonderful..."
    hide samantha1 with dissolve
    scene park03 with fade
    mc "I have another question for you, if you will indulge me."
    st "Sure, ask me anything."
    stop music
    scene park04 with hpunch
    mc "WHERE THE HELL IS [eg7]?!"
    scene park13 with fade
    mc "FIRST THAT HARUKA BITCH, THEN ALLISON, AND NOW YOU!"
    scene park05 with vpunch
    mc "I'VE HAD ENOUGH."
    mc "STOP FUCKING AROUND WITH ME AND TELL ME THE TRUTH!"
    st "..."
    mc "..."
    mc "HEY! I'm talking to you! Look at me!"
    scene park06 with fade
    st "..."
    mc "{i}(What the hell is going on?){/i}"
    scene park05 with vpunch
    mc "I SAID, LOOK AT ME!"
    scene park07
    mc "That's better."
    mc "Now, start talking."
    st "..."
    mc "Why are you just staring at me?"
    mc "SAY SOMETHING!"
    scene park08 with fade
    st "Something."
    mc "What?"
    mc "I meant something about Dr. Donovan."
    st "His name is Eugene Donovan."
    mc "I already know that."
    mc "What the hell is going on?"
    mc "Why do you suddenly sound like a machine?"
    mc "And the way you're looking at me is really freaking me out."
    mc "..."
    mc "{i}(It's almost like she's in a trance...){/i}"
    mc "Yeah, right! They keep telling me that I have some kind of superpower."
    mc "Maybe my power is mind control? Hahaha."
    mc "So, you still wanna play games with me, huh?"
    mc "Okay, then, take my dick out and stroke it."
    scene parksex01 with fade
    with hpunch
    st "..."
    mc "..."

    mc "Oh shit! What are you doing?!"
    mc "You can't do that here!"
    menu:
        "Stop Her":
            mc "That's enough, stop!"
            $ mc_good += 1
            jump v2_samanthastop
        "Let Her Continue":
            $ mc_evil += 1
            jump v2_samantha1
label v2_samanthastop:
    stop music
    scene black
    play music "sounds/park.mp3"
    mc "..."
    mc "Sit back on the bench."
    scene park08 with fade
    mc "Looks like I really do have some sort of power."
    mc "Unbelievable..."
    mc "Now, you are gonna tell me everything..."
    mc "Who are you working for?"
    mc "What do you want from me?"
    mc "And tell me {i}everything{/i} you know about Dr.Eugene Donovan!"
    scene park09 with fade
    st "Argh!"
    st "My head is killing me."
    st "What happened?"
    st "What's going on?"
    st "What did you do to me?"
    mc "I didn't do anything. You were about to tell me everything you know, remember?"
    st "No, that's not what I remember..."
    scene park10 with fade
    st "Did you...?"
    st "You son of a bitch!"
    mc "Shit!"
    scene park11 with vpunch
    st "Take that!"
    mc "Ahhh!"
    scene park14 with fade
    mc "Stop running! WAIT!"
    mc "Shit, she got away."
    scene black with fade
    mc "What was that flying kick?"
    mc "She's dangerous, for sure..."
    mc "I can't believe that I was about to let her jerk my dick in the middle of the park."
    mc "For some reason, I felt extremely horny for a moment."
    mc "Luckily, I managed to get a grip."
    mc "I should go back and get some rest. It's been a really long day..."
    jump daisyrobin1
label v2_samantha1:
    play music "sounds/sexscene1.mp3"
    scene parksex02 with fade
    mc "{i}(I feel unbelievably horny all of a sudden. What's going on?){/i}"
    scene parksex04 with fade
    mc "That's it, keep going."
    show samantha1m with fade
    mc "Oh!"
    mc "I hope no one sees us."
    scene parksex08 with fade
    mc "Maybe we can do something else..."
    mc "Let's start with licking my dick."
    scene parksex03 with fade
    mc "Wow, she's really doing it!"
    mc "I can really control her mind."
    mc "Yes, just like that. Keep licking it..."
    mc "{i}(What is this feeling!{/i})"
    mc "Use your tongue more."
    mc "Let's spice things up a bit!"
    mc "Put my dick between your tits."
    mc "{i}(Did I actually say that...?){/i}"
    scene parksex07 with fade
    mc "Oh, that's a good girl..."
    show samantha2m with fade
    mc "Move your tits up and down."
    mc "Oh, yes. Keep going..."
    mc "That feels really good."
    mc "{i}(What the hell am I doing? I feel so horny and weird. What is happening to me?){/i}"
    mc "I should probably stop before things get really out of control..."
    menu:
        "Stop":
            mc "I've had my fun, that's enough."
            jump samantha3
        "Continue":
            mc "This feels {i}way{/i} too good to stop now..."
            $ mc_evil += 1
            jump v2_samantha2
label v2_samantha2:
    scene black
    mc "Turn around and bend over."
    mc "I want to fuck your beautiful ass."
    mc "You have a gorgeous ass, Samantha."
    mc "I can't wait to fuck your little brown hole."
    mc "{i}(Oh God! Am I really gonna fuck her ass in the middle of the park?! What's gotten into me?){/i}"
    mc "Here I go."
    scene parksex09 with fade
    mc "OH YES."
    mc "IT FEELS AMAZING."
    show samantha3m with fade
    mc "OH! God YES!"
    mc "Your ass is amazing."
    hide samantha3
    show samantha4m with fade
    mc "I think I am about to cum."
    mc "Get on your knees and open your mouth."
    scene parksex05 with flash
    pause 0.3
    with flash
    pause 0.3
    mc "AHH! YESS! TAKE IT ALL!"
    with flash
    pause 0.6
    mc "Wow! That felt really good."


label samantha3:
    scene black with fade
    stop music
    play music "sounds/park.mp3"
    mc "Sit back on the bench."
    scene park08 with fade
    show screen button1
    show screen mcStats
    mc "Looks like I really do have some sort of power."
    mc "Unbelievable..."
    mc "Now, you are gonna tell me everything..."
    mc "Who are you working for?"
    mc "What do you want from me?"
    mc "And tell me {i}everything{/i} you know about Dr. Eugene Donovan!"
    scene park09 with fade
    st "Argh!"
    st "My head is killing me."
    st "What happened?"
    st "What's going on?"
    st "What did you do to me?"
    mc "I didn't do anything. You were about to tell me everything you know, remember?"
    st "No, I don't remember that."
    scene park10 with fade
    st "Did you...?"
    st "You son of a bitch!"
    scene park11 with fade
    mc "Shit!"
    st "Take that!"
    mc "Ahhh!"
    scene park14 with fade
    mc "HEY!"
    mc "STOP RUNING!"
    mc "What was that flying kick?"
    scene black with fade
    mc "She's dangerous, for sure..."
    mc "For some reason, I felt extremely horny for a moment..."
    mc "Luckily, I managed to get a grip."
    mc "I should go back and get some rest. It's been a really long day..."

label daisyrobin1:
    stop music
    scene black
    $ renpy.pause(1.5, hard=True)
    mc "I still can't believe I have a superpower."
    mc "Things got... complicated. This parallel world thing, some kind of special division, a secret war between two worlds, superpowers..."
    mc "It's all too much to take in right now. I really need to get some sleep."
    mc "I can't think clearly anymore."
    mc "What's that voice?"
    mc "It's coming from Daisy's room."
    play music "sounds/background1.mp3"
    scene daisyrobin12 with fade
    if robin_met == False:
        $ robin_met = True
    mc "Oh, that's right. She said she was inviting her friend Robin over for the night."
    mc "She looks so sweet and cute."
    scene daisyrobin14 with fade
    rb "C'mon! Tell me more about him!"
    scene daisyrobin13
    ds "What else do you want to know?"
    ds "He's a cop, he never calls or visits, and all he cares about is [eg1] and his incident."
    scene daisyrobin14
    rb "Yes, you told me that already."
    scene daisyrobin12
    mc "They are talking about me."
    rb "Is he handsome?"
    ds "I suppose..."
    rb "Is he HOT?!"
    ds "Umm... Ye- I mean NO!"
    rb "Hahaha! He is hot, isn't he?"
    scene daisyrobin13
    ds "What's with you today? You're usually really shy, but today..."
    rb "I don't know! Today feels... a bit different."
    ds "Really? Define different."
    rb "I don't know! It's hard to explain..."
    ds "Perhaps you can show me instead of telling me...?"
    rb "Oh..."
    scene daisyrobin01 with fade
    pause 1.0
    ds "Come here and give me a kiss with your sweet, delicious lips."
    scene daisyrobin02 with fade
    pause 1.0
    rb "You can taste them whenever you want, baby."
    scene daisyrobin03 with vpunch
    mc "OH MY GOD!"
    mc "Is this really happening?"
    scene daisyrobin05
    ds "..."
    rb "..."
    mc "Daisy is a lesbian?"
    mc "I shouldn't watch this."
    scene daisyrobin04
    ds "Mmm"
    scene daisyrobin02
    rb "You're an amazing kisser, Daisy."
    scene daisyrobin03
    ds "You're not so bad, either."
    rb "Hey!"
    ds "Relax, I'm only teasing..."
    scene daisyrobin15 with hpunch
    stop music
    ds "Huh?"
    ds "..."
    mc "Shit! She saw me..."
    ds "{i}(Oh, look who's watching...){/i}"
    scene daisyrobin04 with hpunch
    mc "She's kissing her more passionately."
    mc "Is she doing that on purpose?"
    mc "I should leave, this is wrong..."
    menu:
        "Stop Watching":
            jump v2_daisymc1
        "Keep Watching":
            jump daisyrobin2
label daisyrobin2:
    play music "sounds/sexscene1.mp3"
    scene daisyrobin05 with fade
    $ renpy.pause(1.6, hard=True)
    scene daisyrobin03 with fade
    ds "Take off your clothes, I want to lick those luscious tits!"
    rb "You're in love with them, aren't you?"
    mc "{i}(Can you blame her?){/i}"
    scene daisyrobin07 with fade
    rb "Hey, slow down! You know how sensitive my nipples are."
    ds "Better?"
    rb "Oh! Much..."
    scene daisyrobin06 with fade
    ds "God, I am so jealous of your giant breasts."
    ds "I love playing with them and sucking on them."
    ds "They taste amazing, I could suck on them {i}all{/i} day."
    mc "I can't stop myself from watching."
    mc "This is so wrong, but it's so fucking hot!"
    rb "OH! I would love that. Your lips and tongue on my nipples every day..."
    rb "The thought alone makes me wet."
    scene daisyrobin07
    rb "Mmmm."
    rb "You are incredible, Daisy!"
    rb "Ah Ahhh! Please, don't stop!"
    ds "Mhmmhm."
    ds "I want you to sit on my face."
    ds "I'm going to eat your sweet, wet pussy."
    mc "WOW!"
    scene daisyrobin16 with fade
    rb "It's all yours to eat, lick, or whatever you want."
    show robindaisy with fade
    rb "Ahh! OH GOD, YES!"
    rb "It feels so good!"
    ds "I can't get enough of your delicious pussy, baby."
    rb "Mmm!"
    scene daisyrobin08 with fade
    rb "Don't stop! Almost there!"
    rb "I'm CUMMING!"
    with flash
    pause 0.2
    with flash
    pause 0.3
    rb "OH GOD, YESSS!"
    mc "({i}She's shaking like crazy.{i})"
    with flash
    pause 0.8
    rb "That was amazing, Daisy."
    rb "I'm out of breath."
    scene daisyrobin09 with fade
    stop music fadeout 0.5
    rb "What was {i}that{/i}?! You're always amazing, but that was on a different level than usual..."
    ds "Really?!"
    rb "Yes!"
    scene daisyrobin10 with fade
    ds "{i}(Knowing [mc] was wacthing us might be the reason...){/i}"
    ds "That's because you have an amazingly sexy body, babe."
    ds "And It's been a while since we spent a night together."
    ds "My body was craving you."
    scene daisyrobin11
    rb "You're so sweet, Daisy!"
    rb "I'm so lucky to have you in my life."
    rb "I love you so much!"
    ds "{i}(Here we go again with the 'I love you' stuff...){/i}"
    scene daisyrobin10
    ds "Thank you, sweety. I'm really lucky to have you in my life, too."
    rb "..."
    rb "Yeah..."
    mc "{i}(So that's how it is.){/i}"
    mc "{i}(Robin's in love with Daisy, but Daisy doesn't want to be in a relationship.){/i}"
    scene black with fade
    mc "I feel so tired, aroused, and confused at the same time."
    mc "I should really go to bed."
label v2_daisymc1:
    scene black
    pause 0.7
    scene mcdaisy01 with fade
    mc "I have to try and make sense of everything that I learned today."
    mc "Especially the superpower thing."
    mc "I don't know who to trust."
    mc "Haruka's story sounds more believable now that I know I've got some sort of superpower, but I still need to think about it."
    mc "I'm not sure if I can trust Samantha, either."
    mc "She's definitely dangerous, but I wasn't able to hear her side of the story."
    mc "Then there's Allison..."
    mc "I can't believe she was a spy."
    mc "I don't think I can ever trust her again."
    mc "God, there are so many things to think about."
    mc "I'm way too tired to gather the brain power to piece this puzzle together right now, though."
    mc "I need to sleep."
    scene black with fade
    "..."
    play music "sounds/sexscene1.mp3"
    show mcdaisy02 with fade:

        xpos 0.7 ypos 1.0 xanchor 0.66 yanchor 0.93 zoom 1.0
        linear 6 yanchor 0.35

    pause
    hide mcdaisy02
    show mcdaisy02 with fade:
        xpos 0.7 ypos 1.0 xanchor 0.66 yanchor 0.35 zoom 1.0
    ds "..."
    ds "Looks like he's sleeping."
    ds "After enjoying our little show, he's probably having wet dreams right about now."
    scene mcdaisy03 with fade
    ds "Wow!"
    ds "Well, he might be sleeping, but our little friend here looks awake and ready to play..."
    ds "Hm, calling it 'little' isn't right."
    scene mcdaisy04 with fade
    ds "Oh, no, he is absolutely {i}not{/i} little."
    ds "This is so exciting!"
    ds "I am such a pervert."
    ds "And I {i}love{/i} being a pervert."
    scene mcdaisy08 with fade
    ds "Am I going too far?"
    ds "Maybe... I should stop."
    ds "Ha! Who am I kidding? I'm not gonna stop!"
    scene mcdaisy05 with fade
    ds "I can feel the heat coming from it."
    ds "Almost like it's begging me to touch it."
    ds "It's such a rush! My heart rate is through the roof!"
    scene mcdaisy07 with fade
    ds "Do you want me to touch you?"
    ds "Do you want to feel my soft hands?"
    ds "Oh, yes. You want it, don't you?"
    scene mcdaisy06 with fade
    ds "Oh my god!"
    ds "It's so hard and hot!"
    ds "It's throbbing!"
    scene mcdaisy08 with fade
    ds "I did it."
    ds "I touched his dick."
    ds "I want more."
    mc "..."
    mc "{i}(Hmm? What the hell is going on?){/i}"
    mc "{i}(SHIT! It's Daisy!){/i}"
    mc "{i}(What the hell is she doing?!){/i}"
    mc "{i}(Should I wake up and stop her?){/i}"
    menu:
        "Wake Up":
            jump mcwakeup
        "Pretend To Be Asleep":
            jump v2_mcdaisy2


label mcwakeup:
    scene mcdaisy09 with fade
    ds "..."
    ds "Slowly..."
    ds "Don't want to wake him up..."
    mc "Umm."
    stop music
    scene mcdaisy14 with vpunch
    ds "..."
    mc "Daisy! What are you doing?"
    ds "I-I was- you know..."
    ds "I was just..."
    ds "I gotta go!"
    play sound "sounds/door.mp3"
    scene mcdaisy15 with vpunch

    mc "..."
    mc "That was weird."
    mc "I thought I'd seen enough weird shit today."
    mc "I'm just gonna pretend nothing happened and go back to sleep."
    scene mcdaisy17 with fade
    ds "Oh god!"
    ds "He woke up and caught me."
    ds "What am I gonna do? What if he tells Vanessa?"
    ds "I'm such an idiot!"
    jump v2_samanthaphonecall
label v2_mcdaisy2:
    scene mcdaisy09 with fade
    ds "..."
    ds "Slowly..."
    ds "Don't want to wake him up..."
    scene mcdaisy10 with hpunch
    ds "Wow, look at that monster!"
    ds "Please, [mc], don't wake up!"
    mc "{i}(Oh, I won't. You won't have to worry about that, Daisy.){/i}"
    scene mcdaisy18 with fade
    ds "I can barely get my hand around it!"
    show daisymc1 with fade
    ds "This. Is. So. HOT!"
    mc "{i}(Fucking right, it is!){/i}"
    ds "I wonder how he would feel if he only knew that I was giving him a handjob..."
    scene mcdaisy19 with fade
    mc "{i}(Her face is really close to my dick and her hands feels amazing.){/i}"
    show daisymc2 with fade
    mc "{i}(If she keeps going like that, I won't be able to hold back.){/i}"
    ds "I hope you are dreaming about me and Robin right know."
    ds "Maybe in your dream, while you are fucking Robin from behind, you are letting me watch you two."
    mc "{i}(Oh God! Here it comes.){/i}"
    ds "His dick throbbing like crazy. He is about to cum."
    scene mcdaisy11 with flash
    mc "{i}(OH YESS!){/i}"
    with flash
    pause 0.2
    with flash
    ds "Wow!"
    ds "He came so hard."
    scene mcdaisy12 with fade
    ds "That was fun."
    ds "I think having you back here at home will be way more fun than I expected."
    ds "Good night, [mc]."
    scene mcdaisy13 with fade
    stop music
    mc "That was really weird, but it was {i}so{/i} hot!"
    mc "[ds3] is such a freaking pervert!"
    mc "Maybe I should have woke up and stopped her..."
    mc "Though, I have to admit, that felt great!"
    mc "My entire life is becoming more and more strange by the moment."
    mc "Oh well, time to get back to sleep."
    scene mcdaisy16 with fade
    ds "..."
label v2_samanthaphonecall:
    scene meanwhile with fade
    $ renpy.pause(2.0, hard=True)
    play music "sounds/dark.mp3"
    scene v2end01 with fade
    st "..."
    ukn "Speak."
    st "I made contact with the target, sir. He agreed to meet with me."
    ukn "Go on."
    st "I was about to convince him, but..."
    ukn "Yes?"
    scene v2end02 with fade
    st "Something... happened. I lost myself for a moment. It was like time stopped."
    st "When I regained consciousness, I panicked and fled."
    ukn "So it's as we suspected. He has powers."
    st "Yes, sir. He doesn't seem to know how to manifest his full potential."
    ukn "That's good news, but we should proceed with caution."
    st "SID agents have already reached him, sir."
    ukn "Then we must act faster."
    st "What are my orders, sir?"
    ukn "Lay low and continue observation of the target for now."
    ukn "I would prefer to capture him alive, if possible."
    st "Understood, sir."
    stop music
scene black with fade
pause 1
label v3_mc_dream:
    if allison_met == False:
        $ allison_met = True
    if amber_met == False:
        $ amber_met = True
    if haruka_met == False:
        $ haruka_met = True
    if vanessa_met == False:
        $ vanessa_met = True
    if olivia_met == False:
        $ olivia_met = True
    if daisy_met == False:
        $ daisy_met = True

    if robin_met == False:
        $ robin_met = True
    if samantha_met == False:
        nr "Did you go all the way with Samantha?"
        menu:
            "Yes":
                $ samantha_met = True
                $ mc_evil +=2
            "No":
                $ samantha_met = True
                $ mc_good +=1
    show screen button1
    show screen mcStats
    play music "sounds/sexscene1.mp3"
    mc "..."
    mc "What's going on?"
    scene v3_dream1 with fade
    ds "Good morning, sunshine."
    ds "How did you sleep last night?"
    ds "I'm sure you had {i}many{/i} pleasant dreams, hehe."
    mc "DAISY!"
    mc "What the hell do you think you're doing?!"
    ds "I wasn't sure I gave you enough love and care last night, so I was thinking..."
    ds "... Here I am! Ready to give you all... my... love!"
    mc "{i}All{/i} your love...?"

    mc "..."
    mc "Oh!"
    mc "NO! NO! NO!"
    mc "We can NOT do this! This is wrong! You should stop!"

    ds "Really? You were completely fine with this last night, but {i}now{/i} you suddenly think 'this is wrong!'?"
    mc "I don't know what you are talking about..."
    ds "Yeah, right..."

    ds "I knew you were awake while I was playing with our little friend here, [mc]."
    mc "..."
    ds "I know who you really are behind your 'nice guy' persona, [mc]."
    ds "You are a horny, perverted bastard..."
    ds "Just... like... me!"
    mc "What the-"
    mc "No, I'm not!"
    mc "{i}You{/i} are a freak, that's for sure, but I am {i}not{/i} a perverted bastard!"
    scene v3_dream2 with hpunch
    ds "Oh, really? Then please explain why you have a hard-on while talking to me, [mc]?"
    mc "That's morning wood. I can't help it."
    ds "Well... maybe I can help!"
    menu:
        "Stop Her":
            $ mc_good += 1
            jump v3_mcwakeup1
        "Don't Stop Her":
            $ mc_evil += 1
            jump v3_mcdream1
label v3_mcdream1:
    mc "I don't know..."
    ds "C'mon, [mc]. It's gonna be fun."
    mc "It's just... it's so wrong."
    scene v3_dream1 with fade
    ds "That's exactly what makes this so much fun."
    mc "Oh, Daisy. I can't... I shouldn't..."
    ds "You just relax and let me take care of everything."
    ds "Lay back and enjoy the show."
    scene v3_dreamanimation1 with fade
    mc "..."
    ds "See, doesn't it feel good?"
    mc "Yeah..."
    scene v3_dreamanimation2
    ds "I should've brought Robin with me. I'm sure you could handle two ladies at the same time."
    mc "What!"
    ds "She is a little bit shy, but she always listens to me. I'm certain that I can convince her to join us."

    ds "Maybe I should go get her. Would you want that, [mc]?"
    ds "Would you like to fuck us at the same time?"
    ds "Just think about it."

    ds "You and I can kiss while you fuck Robin's big juicy tits, then Robin and I can lick your cock and suck your balls at the same time."
    mc "Jesus, Daisy!"
    ds "Hahaha! Your dick is throbbing like a fully charged vibrator."
    ds "Oh, you naughty boy. Ever since you saw me with Robin, all you can think about is fucking both of us. Right?"
    ds "I'm sorry, [mc], but for now you only get to fuck me."



    ds "You know, I have only slept with two guys when I was going to high school."
    ds "Most of my sexual partners were girls so, my tiny, wet little hole is really craving for some big, hard dick."
    ds "As a gentleman, you can't let a lovely lady like me suffer since you are a super nice and gentle person, right?"
    mc "I can't resist anymore."
    mc "You are so fucking cute and hot."
    scene v3_dream3 with fade
    mc "I want to be inside of you."
    mc "I want to feel your warmth."
    mc "Take my fucking dick and put it inside of your delicious wet pussy!"
    ds "Oh! Yes! That's the spirit."
    ds "Get ready to ride of your life, [mc]."
    ds "I'm gonna fuck your brains out!"
    scene v3_dream7 with fade
    mc "{i}That's it. I'm going hell for sure...{/i}"
    mc "{i}She is really gonna do it!{/i}"
    mc "{i}One slight move and my dick will enter her tight little hole...{/i}"
    jump v3_mcwakeup
label v3_mcwakeup:
    stop music
    scene black
    mc "???"
    mc "Why did you stop?"
    play sound "sounds/jumpscare.wav"
    scene v3_dream4 with vpunch

    mc "What is that? IS THAT A KNIFE?!"
    ds "Lannisters send their regards!"

    mc "NO! DAISY! STOP!"
    scene black
    mc "AHHHHH!"

    $ renpy.pause(1, hard=True)
    scene v3_wakeup3
    mv "Sir? I heard a scream, is everything okay?"
    mc "..."
    mv "OH GOD!"
    mv "I am {i}so{/i} sorry! I should've knocked first."
    mv "{i}He has a nice sexy body.{/i}"
    mc "Huh?"
    mc "SHIT! Wait, I'm sorry."
    mv "I should go. Again, I'm sorry, sir."
    mc "Wait! Who are you...?"
    scene v3_wakeup2
    mc "Jesus, that was a weird dream."
    jump v3_mcwakeup2
label v3_mcwakeup1:
    stop music
    mc "We shouldn't do this, Daisy."
    mc "That's so wrong."
    ds "I see..."
    scene black
    mc "What is that? IS THAT A KNIFE?!"
    play sound "sounds/jumpscare.wav"
    scene v3_dream4 with vpunch
    ds "Lannister's send their regards!"

    mc "NO! DAISY! STOP!"
    scene black
    mc "AHHHHH!"
    $ renpy.pause(1, hard=True)
    scene v3_wakeup3
    mv "Sir? I heard a scream, is everything okay?"
    mc "..."
    mv "OH GOD!"
    mv "I am {i}so{/i} sorry! I should've knocked first."
    mv "{i}He has a nice, sexy body{/i}"
    mc "Huh?"
    mc "SHIT! Wait, I'm sorry."
    mv "I should go. Again, I'm sorry, sir."
    mc "Wait! Who are you...?"
    scene v3_wakeup2
    mc "Jesus, that was a weird dream."
label v3_mcwakeup2:

    play music "sounds/background2.mp3"
    scene v3_wakeup2
    mc "Ah, what a great way to start the day..."
    mc "I should go to the bathroom and freshen up a bit."
    scene black with fade
    scene v3_maeve_afternoon1 with fade
    mc "..."

    mc "Wow!"
    scene v3_maeve_afternoon2 with fade
    mc "{i}Now {b}that{/b} is a great way to start the day.{/i}"
    mv "Huh?"
    if maeve_met == False:
        $ maeve_met = True
    scene v3_maeve_afternoon1blur with fade
    show maeve_maid_sad2 with dissolve
    mc "I'm so sorry, I didn't know someone was in here!"
    mv "I was about to leave, sir."
    mc "No, wait!"
    menu:
        "I'm Sorry":
            $ mc_good += 1
            $ maeve_rlt +=1
            jump v3_mcsorry
        "Never Barge In My Room":
            jump v3_mcmaeve

label v3_mcsorry:
    hide maeve_maid_sad2
    show maeve_maid_natural1 with dissolve
    mc "About this morning... I am {i}really{/i} sorry, I had no idea my family hired a maid after I moved out."
    mc "I should've also knocked before walking into the bathroom. I'm sorry."
    mv "You don't have to apologize, sir."
    mv "I shouldn't have gone into your room without knocking, It was completely my fault."
    mv "I should go."
    mc "Okay."
    hide mave_maid_natural1
    jump v3_talkeveryone
label v3_mcmaeve:
    hide maeve_maid_sad2
    show maeve_maid_natural1 with dissolve
    mc "About this morning. Never barge in my room like that again."
    hide maeve_maid_natural1
    show maeve_maid_sad2 with dissolve
    mv "It will never happen again, sir."
    mv "I will be more careful."
    mc "Good. Leave now so I can use the bathroom."
    mv "Of course, sir."
    hide maeve_maid_sad2
    jump v3_talkeveryone
label v3_talkeveryone:
    scene black with fade
    mc "What other surprises could possibly be awaiting me today?"
    mc "I should pay a visit to Haruka. I still have so many questions for her."
    mc "Before I do that, let's see what everyone is doing right now."
    scene black


    menu:
        "Go Talk With Daisy":
            if v3_daisytalk == True:
                jump v3_daisytalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone1
        "Go Talk With Olivia":
            if v3_oliviatalk == True:
                jump v3_oliviatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone
        "Go Talk With Vanessa":
            if v3_vanessatalk == True:
                jump v3_vanessatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone
label v3_daisytalk:
    scene black
    scene v3_daisy_afternoon with fade
    mc "There she is."
    mc "After the dream I had, she actually freaks me out a little bit..."
    mc "Good morning, Daisy."
    scene v3_daisy_afternoonblur
    show daisy_daily_natural1 with dissolve
    ds "Hey, [mc], good morning."
    ds "Did you sleep well?"
    mc "Yes."
    mc "..."
    mc "I had a really strange dream though."
    ds "{i}I'm sure you did, hehe.{/i}"
    hide daisy_daily_natural1
    show daisy_daily_smile1 with dissolve
    ds "Do you want to tell me about your 'strange' dream?"
    mc "Well... not really. It was really, really weird."
    ds "C'mon, [mc]. You can tell me anything."
    menu:
        "Tell Her It Was A Sex Dream":
            $daisy_rlt += 1
            jump v3_daisytalka
        "Tell Her It Was A Nightmare":
            jump v3_daisytalkb

label v3_daisytalka:
    mc "I'm not so sure..."
    ds "C'mon, spill it already! You know you can trust me."
    mc "Okay. Well..."
    mc "I had a sex dream."
    hide daisy_daily_smile1
    show daisy_daily_laugh1 with dissolve
    ds "Haha! Really?"
    ds "Aren't you a bit too old to have wet dreams? Hahaha!"
    mc "See you later, Daisy..."
    hide daisy_daily_laugh1
    show daisy_daily_smile2 with dissolve
    ds "No, wait! I was just messing with you! {i}Please,{/i} tell me more."
    mc "What else do you want to know?"
    hide daisy_daily_smile2
    show daisy_daily_flirting2 with dissolve
    ds "Give me some details."
    ds "Who did you see? Which positions did you try? How long did it take?"
    mc "I'm not telling you any of that."
    ds "Why not? I'm not like Olivia. I did lots of stuff with quite a few people, if you know what I mean..."
    mc "Too much information..."
    hide daisy_daily_flirting2
    show daisy_daily_smile2 with dissolve
    ds "Pleaseee, please, please, please...."
    mc "ALRIGHT just SHUT UP!"
    ds "Sorry."
    mc "Well..."
    mc "I'm not gonna tell you who I saw in my dream, but it started weird and ended horribly."
    hide daisy_daily_smile2
    show daisy_daily_natural1 with dissolve
    ds "So it's someone I know for sure, since you don't want to tell me who she was or... who he was!"
    mc "It was a woman, Daisy."
    ds "Hey, I'm not judging. There are so many flavors to taste and everyone should try each of them at least once."
    mc "Well... I know which flavors I like so, no thanks."
    ds "Prude..."
    mc "I think that's enough dream talk."
    ds "..."
    jump v3_daisytalk1
label v3_daisytalkb:
    mc "I had a nightmare. There was, umm... this girl that I know, and she was sitting on top of me."
    hide daisy_daily_smile1
    show daisy_daily_flirting2 with dissolve
    ds "Doesn't sound like a nightmare to me."
    mc "She also had a knife, and she was about to stab me."
    hide daisy_daily_flirting2
    show daisy_daily_angry1 with dissolve
    ds "Boring..."
    mc "It may sound boring to you, but I was almost shitting my pants!"
    ds "Next time you want to tell me any dream you had, it better include some sexy elements, okay?"
    jump v3_daisytalk1
label v3_daisytalk1:
    hide daisy_daily_angry1
    hide daisy_daily_natural1
    mc "Umm... Listen, Daisy, about last night..."
    show daisy_daily_serious1 with dissolve
    ds "What about it, [mc]?"
    mc "I wasn't- It was- You know that I-"
    ds "I'm sorry, I can't understand you."
    menu:
        "I Didn't Meant To Watch.":
            $ daisy_rlt += 1
            jump v3_daisytalk1a
        "It Was A Really Good Show":
            $ daisy_rlt += 2
            jump v3_daisytalk1b

label v3_daisytalk1a:
    if v3_daisytalk == True:
        $ v3_daisytalk = False
        mc "I'm sorry about last night, Daisy."
        mc "I didn't mean to watch you, but I heard some noises and just wanted to check on you two."
        hide daisy_daily_serious1
        show daisy_daily_natural1 with dissolve
        ds "Aww, that's so sweet, [mc]... and also, {b}bite me!{/b}"
        ds "You were enjoying yourself back there."
        mc "No, I wasn't."
        ds "So are you saying that Robin and I aren't hot enough for you?"
        mc "I didn't say that."
        mc "Of course, both of you really hot and beau- oh shit..."
        hide daisy_daily_natural1
        show daisy_daily_laugh1 with dissolve
        ds "Got you!"
        ds "Haha, you should be ashamed of yourself, [mc]."
        mc "Who? Me?"
        mc "What about you..."
        hide daisy_daily_laugh1
        show daisy_daily_serious2 with dissolve
        ds "Yeah? What about me..."
        mc "Nothing..."
        ds "{i}I know exactly what you want to say, hehe.{/i}"
        hide daisy_daily_serious2
    menu:
        "Go Talk With Olivia":
            if v3_oliviatalk == True:
                jump v3_oliviatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone1
        "Go Talk With Vanessa":
            if v3_vanessatalk == True:
                jump v3_vanessatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone1
        "Go Back To Your Room":
            if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                jump v3_ambercall
            "{i}(I haven't spoken to everyone yet.){/i}"
            jump v3_talkeveryone1
label v3_daisytalk1b:

    mc "{i}She was really brave last night, sneaking in my room while I was sleeping...{/i}"
    mc "{i}Let's see how she will react to this...{/i}"
    mc "You guys put a good show for me last night."
    hide daisy_daily_serious1
    show daisy_daily_serious2 with dissolve
    ds "Huh?"
    mc "Does [vn2] know about you and Robin?"
    ds "Are you trying to blackmail me?"
    hide daisy_daily_serious2
    show daisy_daily_laugh1 with dissolve
    ds "Hahaha! Now, that's really funny."
    ds "Do you think that I give a damn about what others think of my sexuality?"
    mc "You don't?"
    hide daisy_daily_laugh1
    show daisy_daily_natural1 with dissolve
    ds "Of course not. I mean, if I {i}really{/i} cared about things like that, I wouldn't have Robin over while everyone is here, and I {i}definitely{/i} would've locked the door."
    mc "I guess..."
    ds "Look, [mc], I'm glad you enjoyed watching me and Robin having a little fun time."
    ds "Also, don't worry, I won't tell [vn1] that you are a perverted {i}freak.{/i}"
    mc "What?! I am not a freak!"
    hide daisy_daily_natural1
    show daisy_daily_smile1 with dissolve
    ds "Oh, so you're just a pervert? My bad."
    menu:
        "You Can't Talk To Me Like That!":
            jump v3_daisytalk1c
        "Don't Say Anything.":
            mc "..."


    hide daisy_daily_smile1
    if v3_daisytalk == True:
        $ v3_daisytalk = False
        menu:
            "Go Talk With Olivia":
                if v3_oliviatalk == True:
                    jump v3_oliviatalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone1
            "Go Talk With Vanessa":
                if v3_vanessatalk == True:
                    jump v3_vanessatalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone1
            "Go Back To Your Room":
                if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                    jump v3_ambercall
                "{i}(I haven't spoken to everyone yet.){/i}"
                jump v3_talkeveryone1
label v3_daisytalk1c:
    mc "You can't talk to me like that!"
    ds "Why is that?"
    mc "You need to learn to respect people, especially me!"
    ds "I was just joking. Don't make a big deal out of that."
    mc "Okay, fine. Anyway, I have other things to do."
    mc "I'll see you later."

    hide daisy_daily_smile1
    if v3_daisytalk == True:
        $ v3_daisytalk = False
        menu:
            "Go Talk With Olivia":
                if v3_oliviatalk == True:
                    jump v3_oliviatalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone1
            "Go Talk With Vanessa":
                if v3_vanessatalk == True:
                    jump v3_vanessatalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone1
            "Go Back To Your Room":
                if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                    jump v3_ambercall
                "{i}(I haven't spoken to everyone yet.){/i}"
                jump v3_talkeveryone1
label v3_oliviatalk:
    scene v3_olivia_afternoon1 with fade
    ol "Keep pushing guys, I got your back."
    ol "NoobMaster69, enemy on your left."
    ol "Moelsa and Lvaih protect him."
    scene v3_olivia_afternoon2 with fade
    ol "Nevermind, I've already got them."
    mc "You really are taking playing a video game seriously..."

    ol "One second, [mc]."
    scene v3_olivia_afternoon1 with hpunch
    ol "Hey! You fucking morons! Either play this fucking game right or I will hunt you down! I'll find you and I'll kill you! Do you understand?!"
    mc "{b}WOW!{/b}"
    ol "Phew! That was fun."
    scene v3_olivia_afternoon1blur
    show olivia_daily_smile1 with dissolve
    ol "Hello, [mc]."
    mc "Hi..."
    mc "Maybe I should come another time."
    ol "What? Don't be silly."
    mc "No, no. It's okay. I was just wanted to chat with you. It can wait."
    ol "No, it can't. We haven't seen each other for a long time."
    ol "I would love to catch up with you about what's been going on in your life."
    mc "Alright."
    mc "Actually, I want to talk to you about working at SID."
    menu:
        "Please Be Careful.":
            $ olivia_rlt += 1
            jump v3_oliviatalka
        "You Should Quit Your Job.":
            jump v3_oliviatalkb
label v3_oliviatalka:
    mc "You know, [eg1] had done some work with SID."
    hide olivia_daily_smile1
    show olivia_daily_natural1 with dissolve
    ol "Yes, I'm aware of that."
    mc "I don't want to make you worry or anything, but..."
    mc "{i}Please{/i}, be careful."
    ol "What do you mean?"
    mc "What I mean is, those kinds of institutions aren't always the safest place to work at."
    ol "Look, [mc], I know what kind of place SID is and I'm being careful about it."
    ol "The only danger I'm facing while working at the office is a computer virus or losing internet connection."
    ol "For me, SID is no different than any other work environment."
    mc "Are you sure about that?"
    mc "You haven't met anyone who looks suspicious? No one has ever forced you to do something dangerous?"
    hide olivia_daily_natural1
    show olivia_daily_blushing1 with dissolve
    ol "Well, there was that one incident..."
    mc "I KNEW IT!"
    mc "What did they do? Tell me!"
    ol "I was in the office kitchen and..."
    hide olivia_daily_blushing1
    show olivia_daily_sad1 with dissolve
    mc "Don't worry, Olivia, you can tell me."
    hide olivia_daily_sad1
    show olivia_daily_blushing1 with dissolve
    ol "Alright... here goes."
    ol "I was in the office kitchen, about to make some coffee."
    ol "I picked up my cup and I was looking for the coffee jar."
    ol "When suddenly..."
    mc "..."
    hide olivia_daily_blushing1
    show olivia_daily_sad1 with dissolve
    ol "I realized the coffee jar was empty!"
    ol "Those monsters finished all the coffee at the office."
    ol "It was so cruel!"
    mc "Yeah, then what?"
    mc "Wait..."
    hide olivia_daily_sad1
    show olivia_daily_laugh1 with dissolve
    ol "Hahaha!"
    mc "Very funny."
    hide olivia_daily_laugh1
    show olivia_daily_smile1 with dissolve
    ol "I really appreciate your concern, but there is nothing to worry about."
    mc "Are you sure?"
    ol "Positive."
    hide olivia_daily_smile1
    show olivia_daily_serious1 with dissolve
    ol "Also, you have no right to tell me what to do in with life."
    ol "You missed that chance when you left home and never so much as called."
    mc "I didn't mean to distance myself from you, Olivia. It's just that things were... difficult."
    hide olivia_daily_serious1
    show olivia_daily_angry1
    ol "How should I know that? I never received any calls or texts from you."
    menu:
        "You Are Right":
            $ olivia_rlt += 2
            jump v3_oliviatalk1a
        "That's Not The Point":
            $ olivia_rlt -= 1
            jump v3_oliviatalk1b

label v3_oliviatalkb:
    mc "I don't think it's a good idea to keep working at SID."
    mc "I think you should quit your job."
    hide olivia_daily_smile1
    show olivia_daily_serious1 with dissolve
    ol "Really? Why should I quit my job?"
    mc "Because SID is not exactly the safest place to work at."
    mc "[eg1] was working with them and you know what happened to him."
    ol "Look, [mc]. I know what kind of place SID is and I'm being careful about it."
    ol "The only danger I'm facing while working at the office is a computer virus or losing internet connection."
    ol "For me, SID is no different than any other work environment."
    mc "{i}You have no idea...{/i}"
    hide olivia_daily_serious1
    show olivia_daily_angry1
    ol "Also, you have absolutely no right to tell me what to do in with life."
    ol "After you left us to join the Police Academy, I was devastated."
    hide olivia_daily_angry1
    show olivia_daily_sad2 with dissolve
    ol "I didn't have any friends."
    ol "[vn1] was only focused on her work."
    hide olivia_daily_sad2
    show olivia_daily_angry1 with dissolve
    ol "Daisy didn't give damn about me and, by the way, she still doesn't!"
    ol "The only person who really cared about me was you and you haven't called me. Not even once."
    menu:
        "You Are Right":
            $ olivia_rlt +=2
            jump v3_oliviatalk1a
        "That's Not The Point":
            $ olivia_rlt -= 1
            jump v3_oliviatalk1b
label v3_oliviatalk1a:
    mc "You're right, Liv."
    mc "I was so focused on finding out what happened to [eg1] that I forgot about you."
    mc "I'm really sorry."
    hide olivia_daily_angry1
    show olivia_daily_sad2 with dissolve
    ol "It's alright. I'm sorry, too. I shouldn't have said that."
    ol "You were so young when we lost [eg1]."
    hide olivia_daily_sad2
    show olivia_daily_natural1 with dissolve
    ol "It's only normal for you to be affected more than us."
    mc "No, that's not an excuse."
    mc "We all lost him that day, not just me."
    mc "I promise you, I will make up for our lost time together."
    mc "I'll be always there for you."
    mc "I'll do my best for you, whenever you need it!"
    hide olivia_daily_natural1
    show olivia_daily_smile1
    ol "That means a lot to me, [mc]."
    ol "Thank you so, so much."
    ol "Also, don't worry about my work. I am always careful."
    mc "I trust you, Olivia, and I also trust that if you feel like something is off about that place, you'll tell me."
    ol "Of course, [mc]."
    ol "You are the only person in my life that I can really trust."
    mc "Thank you, Liv."
    hide olivia_daily_smile1
    if v3_oliviatalk == True:
        $ v3_oliviatalk = False
        menu:
            "Go Talk With Daisy":
                if v3_daisytalk == True:
                    jump v3_daisytalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone2
            "Go Talk With Vanessa":
                if v3_vanessatalk == True:
                    jump v3_vanessatalk
                    mc "{i}(I've already spoken to her.){/i}"
                    jump v3_talkeveryone2
            "Go Back To Your Room":
                if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                    jump v3_ambercall
                "{i}(I haven't spoken to everyone yet.){/i}"
                jump v3_talkeveryone2
label v3_oliviatalk1b:
    mc "That has nothing to with what we are talking about."
    mc "Listen to me, I'm asking you this because I real-"
    hide olivia_daily_angry1
    show olivia_daily_angry2 with hpunch
    ol "NO!"
    ol "You listen to me!"
    ol "You know nothing about me or what I've been through this whole time!"
    ol "You were gone, [mc]..."
    ol "I was all alone and had to work so hard to get to where I'm right now."
    ol "So, nobody... NOBODY in the world can tell me what to do."
    mc "I was just-"
    hide olivia_daily_angry2
    show olivia_daily_angry1 with dissolve
    ol "You should leave now."
    ol "I want to be alone."
    mc "..."
    mc "Okay."
    hide olivia_daily_angry1
    if v3_oliviatalk == True:
        $ v3_oliviatalk = False
        menu:
            "Go Talk With Daisy":
                if v3_daisytalk == True:
                    jump v3_daisytalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone2
            "Go Talk With Vanessa":
                if v3_vanessatalk == True:
                    jump v3_vanessatalk
                    mc "{i}(I've already spoken to her.){/i}"
                    jump v3_talkeveryone2
            "Go Back To Your Room":
                if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                    jump v3_ambercall
                "{i}(I haven't spoken to everyone yet.){/i}"
                jump v3_talkeveryone2
label v3_vanessatalk:
    scene v3_vanessa_afternoon3 with dissolve:
        xpos 0.7 ypos 1.0 xanchor 0.66 yanchor 0.93 zoom 1.1
        linear 4 xanchor 0.32
    mc "{i}As usual, she is at the pool after breakfast.{/i}"
    scene v3_vanessa_afternoon4 with fade
    mc "I see your habit hasn't changed."
    mc "Don't you worry about being late to the work, [vn1]."
    scene v3_vanessa_afternoon2 with fade
    vn "Hey, [mc]."
    vn "Why would I worry? I'm the leader of the team and their boss."
    vn "Plus, the scientists on my team are more than capable of doing their research without needing me to constantly observe them."
    mc "I see."
    scene v3_vanessa_afternoon1 with fade
    vn "Why don't you join me? The weather is great today."
    mc "I've got some things to do, maybe next time."
    vn "As you wish, honey."

    menu:
        "You Are In A Perfect Shape":
            $ vanessa_rlt += 2
            jump v3_vanessatalka
        "You Look Beautiful For A Woman At Your Age":
            $ vanessa_rlt -= 1
            jump v3_vanessatalkb
label v3_vanessatalka:

    mc "[vn1], I don't know how you manage to do it, but you are always in perfect shape."
    scene v3_vanessa_afternoon1blur
    show vanessa_bikini_smile2 with dissolve
    vn "You are so sweet, [mc]."
    vn "I really take care of my body and watch what I eat."
    mc "I must say your natural beauty helps a lot too, [vn1]."
    hide vanessa_bikini_smile2
    show vanessa_bikini_blushing2 with dissolve
    vn "Stop it, [mc], you're gonna make me blush."
    hide vanessa_bikini_blushing2
    show vanessa_bikini_natural1 with dissolve
    vn "I'm really glad you come to visit us, [mc]."
    mc "Yeah. Me too."
    vn "Speaking of which, is there any special reason you suddenly decided to come visit us?"
    vn "Please, don't get me wrong, I'm more than happy to have you here..."
    vn "I'm just curious, that's all."
    menu:
        "I Just Missed You guys":
            $ vanessa_rlt += 1
            jump v3_vanessatalk1a
        "Do I Need A Reason?":
            jump v3_vanessatalk1b
label v3_vanessatalkb:
    mc "I must say, you look really beautiful for a woman your age, [vn1]."
    scene v3_vanessa_afternoon1blur
    show vanessa_bikini_angry1 with dissolve
    vn "For a woman my {i}age{/i}?"
    vn "Thank you, I guess..."
    mc "..."
    mc "Sorry, I didn't mean it that way, I..."
    hide vanessa_bikini_angry1
    show vanessa_bikini_natural1 with dissolve
    vn "Don't worry about it, I know what you really meant."
    vn "By the way, I was meaning to ask you."
    vn "Is there any special reason you suddenly decided to come visit us?"
    vn "Please, don't get me wrong, I'm more than happy to have you here..."
    vn "I'm just curious, that's all."
    menu:
        "I Just Missed You guys":
            $ vanessa_rlt += 1
            jump v3_vanessatalk1a
        "Do I Need A Reason?":
            jump v3_vanessatalk1b
label v3_vanessatalk1a:
    mc "I just missed you guys so much."
    mc "I've been absent for a long time."
    mc "I thought, if I distanced myself from you and focused on finding [eg1], it would be easier."
    mc "I was wrong..."
    vn "Honey, I know it was really hard for you and I'm sure it still is..."
    vn "But you don't have to carry this burden on your shoulders anymore."
    hide vanessa_bikini_natural1
    show vanessa_bikini_sad2 with dissolve
    vn "It's been a really long time since we lost [eg4]."
    vn "Trust me, I miss him too, but we have to move on."
    mc "I know that you're right, [vn1], but, it's... it's just not that simple for me..."
    hide vanessa_bikini_sad2
    show vanessa_bikini_natural1 with dissolve
    vn "If that's the case, at least promise me this."
    vn "You will not do anything stupid or dangerous."
    vn "And never forget that, no matter what happens, I'm always here for you."
    vn "I know I really shouldn't say this, but Olivia was right."
    mc "About what?"
    hide vanessa_bikini_natural1
    show vanessa_bikini_smile2 with dissolve
    vn "You {i}are{/i} my favorite."
    mc "..."
    mc "I don't know what to say..."
    vn "You don't have to say anything."
    hide vanessa_bikini_smile2
    show vanessa_bikini_natural1 with dissolve
    vn "Just be careful, and never forget that I've got your back."
    mc "Thank you, [vn1]."
    hide vanessa_bikini_natural1
    if v3_vanessatalk == True:
        $ v3_vanessatalk = False
        menu:
            "Go Talk With Daisy":
                if v3_daisytalk == True:
                    jump v3_daisytalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone3
            "Go Talk With Olivia":
                if v3_oliviatalk == True:
                    jump v3_oliviatalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone3
            "Go Back To Your Room":
                if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                    jump v3_ambercall
                "{i}(I haven't spoken to everyone yet.){/i}"
                jump v3_talkeveryone3
label v3_vanessatalk1b:
    mc "Do I really need a reason?"
    vn "Of course not, sweetheart."
    vn "Listen..."
    vn "I know you're still obsessed with [eg4]'s case."
    vn "I know it was really hard for you, and I'm sure it still is..."
    vn "But you don't have to carry this burden on your shoulders anymore."
    vn "It's been a really long time since we lost [eg4]."
    vn "Trust me, I miss him too, but we have to move on."
    mc "I know that you're right, [vn1], but, it's... it's just not that simple for me..."
    hide vanessa_bikini_natural1
    show vanessa_bikini_angry1 with dissolve
    vn "If that's the case, at least promise me this."
    vn "You will not do anything stupid or dangerous."
    hide vanessa_bikini_angry1
    show vanessa_bikini_natural1 with dissolve
    vn "And never forget that, no matter what happens, I'm always here for you."
    vn "I know I really shouldn't say this, but Olivia was right."
    mc "About what?"
    hide vanessa_bikini_natural1
    show vanessa_bikini_smile2 with dissolve
    vn "You {i}are{/i} my favorite."
    mc "..."
    mc "I don't know what to say..."
    vn "You don't have to say anything."
    hide vanessa_bikini_smile2
    show vanessa_bikini_natural1 with dissolve
    vn "Just be careful, and never forget that I've got your back."
    mc "Thank you, [vn1]."
    hide vanessa_bikini_natural1
    if v3_vanessatalk == True:
        $ v3_vanessatalk = False
        menu:
            "Go Talk With Daisy":
                if v3_daisytalk == True:
                    jump v3_daisytalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone3
            "Go Talk With Olivia":
                if v3_oliviatalk == True:
                    jump v3_oliviatalk
                mc "{i}(I've already spoken to her.){/i}"
                jump v3_talkeveryone3
            "Go Back To Your Room":
                if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                    jump v3_ambercall
                "{i}(I haven't spoken to everyone yet.){/i}"
                jump v3_talkeveryone3
label v3_talkeveryone1:
    menu:

        "Go Talk With Olivia":
            if v3_oliviatalk == True:
                jump v3_oliviatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone1
        "Go Talk With Vanessa":
            if v3_vanessatalk == True:
                jump v3_vanessatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone1
        "Go Back To Your Room":
            if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                jump v3_ambercall
            "{i}(I haven't spoken to everyone yet.){/i}"
            jump v3_talkeveryone1

label v3_talkeveryone2:
    menu:
        "Go Talk With Daisy":
            if v3_daisytalk == True:
                jump v3_daisytalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone2

        "Go Talk With Vanessa":
            if v3_vanessatalk == True:
                jump v3_vanessatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone2
        "Go Back To Your Room":
            if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                jump v3_ambercall
            "{i}(I haven't spoken to everyone yet.){/i}"
            jump v3_talkeveryone2
label v3_talkeveryone3:
    menu:
        "Go Talk With Daisy":
            if v3_daisytalk == True:
                jump v3_daisytalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone3
        "Go Talk With Olivia":
            if v3_oliviatalk == True:
                jump v3_oliviatalk
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryone3
        "Go Back To Your Room":
            if v3_oliviatalk == False and v3_daisytalk == False and v3_vanessatalk == False:
                jump v3_ambercall
            "{i}(I haven't spoken to everyone yet.){/i}"
            jump v3_talkeveryone3

label v3_ambercall:
    mc"I should change my clothes and get ready."
    scene black with fade
    play sound "sounds/cellphone.ogg"
    scene v3_amber_phone2 with fade
    mc "My phone is ringing..."
    scene v3_amber_phone3
    mc "Oh! It's Amber."
    mc "I completely forgot about her."
    scene v3_amber_phone1 with fade
    am "Hey."
    mc "Hi, Amber."
    mc "I was going to call you, but-"
    am "Please, stop that."
    am "I'm not the kind of person who expects a call from a guy she just met."
    mc "That's really good to hear."
    am "I was wondering if you're free tonight maybe we could go out for dinner?"
    mc "That would be great, but I'm not in the city."
    am "Really?"
    mc "Yes, something came up and I had to leave town."
    am "Aww, that's too bad."
    am "I was hoping that we can have some fun tonight."
    am "Where are you exactly?"
    mc "I'm at my family's home."
    mc "You know what? It's not that far from the city, so if you want to come you're more than welcome."
    am "I don't know. I mean, I don't have any other plans, but I wouldn't want to disturb your family."
    mc "That's nonsense, you won't bother them at all."
    mc "Pack some clothes and hop on the bus."
    mc "You can spend the night here."
    am "You say spend the night, but..."
    am "Where am I gonna sleep?"
    mc "I've always liked sharing what I have, so you can sleep in my bed."
    am "I don't know if I can sleep next to you..."
    mc "Why not?"
    am "I don't think I could stop myself from tearing off your clothes and fucking your brains out."
    mc "That shouldn't be a problem, I'm not planning on wearing anything at all."
    am "Alright, I'm convinced."
    mc "I'll send you the address."
    am "Are you really sure about this?"
    mc "Yes, I'm sure."
    am "Okay, then. I'm gonna hang up now, so I can go home and get ready."
    mc "Okay, I'll see you soon."
    scene black
    mc "I should get ready, too."
    scene black with fade
    nr "At the SID, Haruka's Office."

label v3_haruka:
    stop music
    play music "sounds/background1.mp3"
    scene v3_office1 with fade
    mc "{i}She has a really nice office.{/i}"
    mc "{i}She's also quite beautiful, I can't believe I didn't notice it yesterday.{/i}"
    mc "Hello."
    scene v3_office1blur
    show haruka_daily_natural1 with dissolve
    hr "Welcome, [mc]."
    hr "I'm really glad that you decided to visit me."
    hr "Can I offer you something to drink? Coffee or maybe something stronger?"
    mc "Thanks, but I'm good."
    hr "As you wish."
    hr "Could you please give me a moment?"
    mc "Of course."
    hr "Thank you."
    hide haruka_daily_natural1
    scene v3_office2 with fade
    mc "{i}I can't stop looking at her breasts. They look so firm.{/i}"
    mc "{i}No, no, no! I learned my lesson last night. No matter how hot they are, secret agents are really dangerous.{/i}"
    mc "{i}I still can't believe that Samantha chick hit me with a flying kick. My chest still hurts.{/i}"
    scene v3_office1blur with fade
    show haruka_daily_natural1 with dissolve
    hr "Sorry about that."
    hr "Today has been busier than usual."
    hr "How can I help you?"
    mc "I want to talk to you about yesterday."
    hr "Did something happen?"
    hr "Wait!"
    hr "Let's go sit over there."
    mc "Alright."
    scene v3_office3 with fade
    hr "Please, go on."
    menu:
        "Before We Start":
            $haruka_rlt += 1
            jump v3_haruka1
        "About Last Night":
            jump v3_haruka2

label v3_haruka1:
    mc "Before we start, I must say you are really beautiful."
    scene v3_office3blur
    hide haruka_daily_natural1
    show haruka_daily_serious1 with dissolve
    mc "Ah, sorry. Please don't mistake, I'm not trying to hit on you or anything..."
    mc "I just felt the need to say it, that's all."
    hide haruka_daily_serious1
    show haruka_daily_smile1 with dissolve
    hr "Thank you, [mc]."
    hr "Now, please... tell me what happened."
    hide haruka_daily_smile1
    show haruka_daily_natural1 with dissolve
    mc "Something {i}weird{/i} happened last night."
    mc "I don't know how I can explain this..."
    hr "Let me guess: You had an emotional moment, probably get really angry, and suddenly felt something weird."
    mc "Yes! How did you know?"
    hide haruka_daily_natural1
    show haruka_daily_angry1 with dissolve
    hr "That's exactly what we expected."
    hr "According to Dr. Donovan, to awaken one's power, the subject has to feel extreme emotion."
    hr "What caused you to feel something like that, [mc]?"
    jump v3_haruka3
label v3_haruka2:
    scene v3_office3blur
    mc "Something weird happened last night."
    show haruka_daily_serious1 with dissolve
    hr "What do you mean?"
    mc "I don't know how I can explain this..."
    hr "Let me guess: You had an emotional moment, probably get really angry, and suddenly felt something weird."
    mc "Yes! How did you know?"
    hide haruka_daily_serious1
    show haruka_daily_natural1
    hr "That's exactly what we expected."
    hr "According to Dr. Donovan, to awaken one's power, the subject has to feel extreme emotion."
    hr "What caused you to feel something like that, [mc]?"

label v3_haruka3:
    mc "It doesn't matter."
    mc "All that really matters is I have some sort of superpower."
    mc "And it freaks me out!"
    hr "That's... completely understandable, [mc]. This must all come as quite a shock."
    hr "What kind of power do you have?"
    mc "I'm not sure I should share that with you..."
    hide haruka_daily_natural1
    show haruka_daily_angry1 with dissolve
    hr "Look, [mc], if you want my help, you need to be honest with me."
    mc "As much as I need your help, you also need me."
    mc "And I still have my doubts about you and your story."
    mc "The best thing we can do for now help each other."
    hr "Okay, but under one condition."
    hr "You will work for us."
    hr "You will quit your job as a police officer and move to this city."
    hide haruka_daily_angry1
    show haruka_daily_natural1 with dissolve
    hr "Should you accept, we are not only going to help you, we will also train you."
    hr "You will learn how to fight, how to read people and how to handle extreme situations."
    mc "And if I refuse?"
    hr "We will keep protecting you and your family, but we will not share any information with you."
    hr "If we feel that it's unsafe for you and your family to live normal life, we will take you and your family into custody, re-locate you, and give all of you new identities."
    mc "So, you're saying if I want my family to have a normal life, I must join SID."
    mc "Even if I join SID, there is still a chance that you take my family into custody and change their life."
    hide haruka_daily_natural1
    show haruka_daily_smile1 with dissolve
    hr "You are right, we do have that power."
    hr "In fact, I could have done so long before now if I so desired, and yet I'm giving you a chance."
    hr "As you said before; we need each other."
    mc "..."
    mc "Looks like I don't really have a choice."
    hr "Great."
    hide haruka_daily_smile1
    show haruka_daily_serious1 with dissolve
    hr "Before you leave, I want to ask you again."
    hr "Do you want to tell me about last night?"
    mc "Maybe someday."
    mc "You need to earn my trust first."
    mc "You've got all the resources and power over me."
    mc "I got nothing."
    mc "I don't really know who you are."
    hr "During your training sessions, we will have many opportunities to get to know each other."
    mc "I'm sure we will, but until then I'm keeping some things to myself."
    hr "Fair enough."
    hr "I'll see you tomorrow, then."
    mc "Okay."
    hide haruka_daily_serious1
    scene v3_office4 with fade
    al "OH!"
    al "Hi, [mc]"
    scene v3_office5 with fade
    mc "Excuse me."
    al "..."
    scene v3_office6 with fade
    al "Wait."
    al "I want-"
    scene v3_office7 with fade
    al "..."
label v3_home:
    stop music

    scene black with fade
    mc "{i}Haruka thinks she got strings on me, but that's not the case.{/i}"
    mc "{i}I will play nice for now and see what her true intentions are.{/i}"
    mc "{i}I must find something to leverage against SID to ensure my family's safety. I can't leave their fate in the hands of SID!{/i}"
    scene black with fade
    play music "sounds/background2.mp3"
    scene v3_amber_meet4 with fade
    show vanessa1 with dissolve
    vn "Hello, [mc]. Where did you go?"
    mc "Hey, just went out to get some fresh air."
    vn "Okay, honey."
    vn "I hope you didn't have any plans for tonight, because I'm going to take all of you to a nice restaurant."
    mc "Actually, I do have plans."
    mc "Remember the girl I told you about yesterday?"
    vn "Yes."
    mc "Well, she is coming by to visit, and she's staying the night."
    mc "I know that I should've asked you first, bu-"
    hide vanessa1
    show vanessa3 with dissolve
    vn "Don't be silly, [mc]. She is more than welcome. In fact, bring her to dinner tonight."
    vn "The more the merrier."
    mc "I don't know."
    vn "Why not?"
    mc "I'm kinda afraid that you might start to talk about relationship and marriage stuff..."
    hide vanessa3
    show vanessa2 with dissolve
    vn "I won't do such a thing. I know how to behave around young people."
    mc "Are you sure?"
    vn "Yes, [mc], I'm sure."
    mc "Okay, then."
    hide vanessa2
    show vanessa1 with dissolve
    vn "So, when should we expect to meet with her parents?"
    mc "What?!"
    vn "Hahaha! Just kidding..."
    vn "Her name was Amber, right?"
    mc "Yes."
    vn "I'll call the restaurant and change the reservation."
    mc "Thanks."
    mc "She should arrive at any moment. Please, tell Olivia and Daisy to not be weird."
    vn "No need to be nervous. I'm going to be cool. Olivia and Daisy are going to be cool..."
    vn "Everything is going to be cool."
    mc "{i}Please{/i} stop saying cool..."
    scene black with fade
    play sound "sounds/doorbell.ogg"
    mc "That must be Amber."
    scene v3_amber_meet1 with fade
    am "Hi, [mc]."
    mc "Hello Amber, please come in."
    am "Thanks."
    am "Wow, you guys have a really nice house."
    mc "Thank you."
    mc "Let me take your bag for you."
    scene v3_amber_meet2 with fade
    vn "Hello, welcome to our home."
    am "Thanks, you must be Olivia."
    vn "No, I'm Vanessa."
    am "Really? You look so young. I was certain you were Olivia. I'm sorry for the mix up."
    vn "Aren't you the sweetest?"
    vn "Please make your self comfortable."
    vn "Daisy and Olivia are in the living room."
    am "Great! I can't wait to meet with them."
    mc "I should take this bag to my room."
    mc "I'm gonna join you guys in a minute."
    scene v3_amber_meet3 with fade
    am "Hi."
    ol "Hello. You must be Amber."
    ol "I'm Olivia, it's so nice to meet you."
    am "Thanks! You too."
    am "And you are... Daisy, am I right?"
    ds "Yep."
    am "Nice to meet you, Daisy."
    scene v3_amber_meet3blur
    show daisy_daily_flirting2 with dissolve
    ds "Nice to meet {b}you{/b}."
    ds "Wow, you're {i}really{/i} beautiful, no wonder [mc] likes you a lot."
    show daisy_daily_flirting2 at right with dissolve:
        xpos 1750
    show olivia_daily_natural1 at left with dissolve

    ol "Daisy, please watch your mouth."
    show olivia_daily_natural1:
        ease .5 zoom 1.0
    show daisy_daily_flirting2 at right:
        ease .5 xpos 1750 zoom 1.1
    ds "Mind your own business."
    show daisy_daily_flirting2 at right:
        ease .5 xpos 1900 zoom 1.0
    show olivia_daily_natural1 at left with dissolve:
        ease .5
    show daily_amber_natural_eyes with dissolve
    am "It's okay, I appreciate the compliment."
    ds "And I'm appreciating the view..."
    hide olivia_daily_natural1
    show olivia_daily_serious2 at left with dissolve
    ol "That's enough, Daisy."
    ol "I'm sorry about her."
    show daily_amber_natural_eyes:
        ease .5 zoom 1.1
    am "No need to apologize."
    mc "I see you've finally met the girls."
    show daily_amber_natural_eyes:
        ease .5 zoom 1.0
    hide olivia_daily_serious2 with dissolve
    hide daisy_daily_flirting2 with dissolve

    mc "Olivia is the oldest, she is a Software Engineer."
    mc "Daisy is the youngest, she recently graduated from high school."
    mc "Olivia is the most mature and caring person in this house."
    mc "On the other hand, Daisy is..."
    hide daily_amber_natural_eyes

    show daily_amber_smile1_eyes with dissolve
    am "If I had to guess I would say cutest and the most unpredictable?"
    mc "I should've warned you about Daisy..."
    show daisy_daily_laugh1 at right with dissolve:
        xpos 1750
    ds "Too late! Hahaha."
    hide daisy_daily_laugh1 with dissolve
    mc "Anyway, [vn1] told me that you guys should get ready to head out to the restaurant."
    am "I'm sorry, what restaurant?"
    mc "Oh. Right, I forgot to tell you."
    mc "[vn1] wants to take us all out to dinner tonight."
    mc "If you don't want to go, we can make other plans."
    hide daily_amber_smile1_eyes
    show daily_amber_surprised2_eyes with dissolve
    am "Are you kidding me? I would love to."
    ds "Great."

    hide daily_amber_surprised2_eyes
    show daily_amber_smile1_eyes at left with dissolve:
        xpos 150
    show daisy_daily_smile2 at right with dissolve:
        xpos 1750
    ds "Hey, Amber, would you mind helping me to pick out a dress for tonight?"
    am "Sure, no problem."
    hide daisy_daily_smile2
    show daisy_daily_smile1 at right with dissolve:
        xpos 1750
    ds "Awesome, let's head up to my room. You can change in my room, too, if you'd like."
    am "Alright."
    hide daisy_daily_smile1 with dissolve
    hide daily_amber_smile1_eyes with dissolve
    mc "..."
    with hpunch
    mc "WAIT!"
    show daily_amber_natural1_eyes with dissolve
    am "What?"
    mc "Umm..."
    show daily_amber_natural1_eyes at left:
         xpos 150
    show daisy_daily_angry1 at right with dissolve:
        xpos 1750
    ds "Yes, [mc]. Is there a problem?"
    mc "Umm..."
    ol "Are you trying to meditate?"
    mc "Umm..."
    ds "The right word for that is 'Omm'."
    mc "What? No! I was gonna say that your bag is in my room, Amber, and you can change your clothes in my room where it's safe."
    hide daily_amber_natural1_eyes
    show daily_amber_smile1_eyes at left with dissolve:
        xpos 150
    am "Huh?"
    hide daisy_daily_angry1
    show daisy_daily_natural1 at right with dissolve:
        xpos 1750
    ds "Hehe."
    show daisy_daily_natural1 at right:
        ease .5 zoom 1.1 xpos 1750
    ds "Don't worry about him, he is just too excited for tonight."
    ds "Let's go."
    hide daisy_daily_natural1 with dissolve
    hide daily_amber_smile1_eyes with dissolve
    mc "{i}I have a bad feeling about this...{/i}"
    scene v3_amber_meet5 with fade
    show olivia_daily_serious1 with dissolve

    ol "What's wrong with you?"
    mc "Huh? Oh, nothing..."
    ol "If you say so..."
    hide olivia_daily_serious1
    show olivia_daily_sad2 with dissolve
    ol "I should get ready too, but I don't have a dress."
    mc "Really?"
    ol "I don't usually go out at night."
    mc "I'm sure you have something. I mean every woman has at least one or two dresses in their closet."
    hide olivia_daily_sad2
    show olivia_daily_natural1 with dissolve
    ol "Nope. Not this one."
    vn "Why am I not surprised?"
    show olivia_daily_natural1 at left:
        xpos 150
    ol "[vn1]!"
    show vanessa3 at right with dissolve:
        xpos 1750
    vn "Let's go to my room. I'm sure we can find something for you."
    ol "Really? Thank you so much."

    scene black with fade
    mc "Okay, I'm ready to go."
    mc "I better check in on Amber."
    mc "I don't want that pervert to freak her out."
    stop music
    scene black with fade
    play music "sounds/cafe.mp3"
    scene v3_daisy_amber1 with fade
    mc "..."
    ds "So, you're saying I should wear this black dress tonight?"
    am "Absolutely. You will look so cute and sexy in it."
    ds "Really? I don't know about this. I'm not sure that I have a sexy body."
    mc "{i}You crafty little bastard! Trying to get compliments from Amber.{/i}"
    am "Are you kidding me? You have a really sexy body, Daisy. You're incredibly beautiful."
    ds "Stop that, you're gonna make me blush."
    ds "Enough about me, what are you gonna wear tonight?"
    ds "Perhaps something to get you laid?"
    am "Haha. Well, I only brought one dress and it got me laid two days ago."
    ds "So, you and [mc] have already slept together?"
    am "I didn't say it was [mc]..."
    ds "You didn't have to, I can tell. When you're next to him, I can sense the vibe between you two."
    am "Is it really that obvious?"
    ds "Probably not, but I have a knack for things like that."
    scene black with fade
    mc "{i}She hasn't tried anything weird so far, so that's good.{/i}"
    mc "{i}I don't want to take any chances, so...{/i}."
    mc "Hey, girls. May I come in?"
    ds "Sure."
    scene v3_daisy_amber2 with fade
    mc "Wow! You both look gorgeous."
    am "Thank you."
label v3_amberdaisy:
    menu:
        "Look At Amber":
            if v3_amberdress == True:
                jump v3_amberdress
            mc "{i}(Let's look at her one more time.){/i}"
            jump v3_amberdaisy1


        "Look At Daisy":
            if v3_daisydress == True:
                jump v3_daisydress
            mc "{i}(Let's look at her one more time.){/i}"
            jump v3_amberdaisy2
        "Leave":
            mc "{i}(...){/i}"
            jump v3_home1

label v3_amberdress:
    if v3_amberdress == True:
        $v3_amberdress = False
        am "How do I look, [mc]?"
        scene v3_daisy_amber6 with fade
        mc "I see you are wearing that red dress again."
        mc "You look stunning, Amber."
        ds "Yes, she does."
        ds "It's just..."
        scene v3_daisy_amber3 with vpunch
        ds "Here let me fix it!"
        mc "WHAT THE-"
        am "..."
        ds "Okay, now you look perfect."
        am "Thanks..."
        scene black with fade
        ds "C'mon, give us another pose."
        mc "Daisy, stop that."
        am "I don't mind."
        scene v3_daisy_amber4 with fade
        am "How is it?"
        mc "Just... Wow!"
        am "Thanks."
        ds "How the hell did such a sexy woman end up with... you...?"
        mc "Well, for starters, any woman would be lucky to have me in their life."
        scene v3_daisy_amber6 with fade
        ds "And?"
        mc "And... that's it. We don't have all day for me to explain to you why am I the ultimate male."
        am "Hahaha."
        ds "Oh! Now, I get it. You are covering all your flaws by being funny."
        am "I think she got you, [mc]."
        ds "To be fair, he makes it too easy for me, and he is supposed to be the smartest one among us."
        am "Haha! I really like you, Daisy."
        ds "Hehe, thanks! I really like you, too."
        jump v3_amberdaisy
label v3_daisydress:
    if v3_daisydress == True:
        $v3_daisydress = False
    scene v3_daisy_amber5 with fade
    ds "What do you think?"
    mc "You've really grown so much."
    mc "Look how beautiful you've become."
    scene v3_daisy_amber7 with fade
    ds "How about now?"
    mc "I'm speechless."
    am "You look so cute and hot, Daisy."
    ds "Hold your horses, beautiful."
    ds "Your boyfriend is right here."
    ds "Unless, you don't mind sharing...?"
    scene v3_daisy_amber5 with fade
    am "Huh?!"
    mc "What?!"
    ds "HAHAHA! I love screwing with people."
    mc "Sorry about her, Amber."
    am "No, no. I think It was pretty funny."
    ds "Finally! Someone who shares my sense of humor."
    jump v3_amberdaisy
label v3_amberdaisy1:
    scene v3_daisy_amber4 with fade
    mc "..."
    jump v3_amberdaisy
label v3_amberdaisy2:
    scene v3_daisy_amber7 with fade
    mc "..."
    jump v3_amberdaisy

label v3_home1:
    scene black with fade
    mc "Looks like they are ready, too."
    scene v3_olivia_vanessa1 with fade
    mc "Hey, girls. Are you ready to go?"
    vn "Yes, honey. But first, we need you."
    mc "Umm, for what?"
    vn "Can you please tell Olivia that she looks really beautiful in that dress?"
    ol "Stop that, [vn1]."
    menu:
        "Maybe Another Time":
            mc "Maybe later,[vn1]. I'll wait for you guys downstairs."
            jump v3_home2
        "Let Me Look At you":
            mc "Sure, let me look at you."
    scene v3_olivia_vanessa2 with fade
    ol "I feel so uncomfortable in this."
    mc "Olivia, you look extremely beautiful in that dress."
    ol "You're just saying that."
    mc "No, I'm not. You're already really beautiful as you are, but with that dress... I just can't take my eyes off from you."
    scene v3_olivia_vanessa3
    ol "Really?"
    mc "Yes."
    ol "Thank you."
    scene v3_olivia_vanessa4 with fade
    vn "So, are you saying that she is the only one who looks beautiful in a dress?"
    mc "[vn1], are you kidding me? Your whole body is like sculpted by Michelangelo himself."
    mc "I don't think that any woman can pull off this dress."
    mc "At least they wouldn't look as good as you in it, that's for sure."
    scene v3_olivia_vanessa5 with fade
    vn "Thank you, sweetheart. You really know how to talk to a woman."
    mc "Well, you're the one who taught me to be a gentleman."
    vn "Enough of that, young man, before I start falling for you."
    vn "Go and wait for us in the living room."
    vn "I'll check on the girls and we'll be with you in a minute."
    mc "Okay."
    scene black with fade
label v3_home2:
    vn "Is everyone ready?"
    ol "Seems so."
    vn "Let's go, then."
    scene v3_amber_meet5 with fade
    show daisy_dress_natural1 with dissolve
    ds "Wait! Before we go I want to ask [mc] something."
    vn "What is it now?"
    ds "I just wanna play a little game."
    ds "[mc], which one of us is the hottest lady of tonight?"
    mc "Are you kidding me? I don't want to play such a childish game."
    hide daisy_dress_natural1
    show daisy_dress_serious1 with dissolve
    ds "Oh, c'mon! Don't be like that. All you have to do is pick one of us."
    show daisy_dress_serious1 at right with dissolve:
        xpos 1750
    show olivia_dress_natural1 at left with dissolve:
        xpos 150
    ol "Daisy, when will you grow up?"
    hide daisy_dress_serious1
    show daisy_dress_serious2 at right with dissolve:
        xpos 1750
    ds "Whenever I want to."
    show olivia_dress_natural1 at left:
        ease .5 zoom 1.1 xpos 150
    ol "I don't want to be part of this."
    show olivia_dress_natural1 at left:
        ease .5 zoom 1.0 xpos 150
    show daisy_dress_serious2 at right:
        ease .5 zoom 1.1 xpos 1750
    ds "Of course you don't, since you already know that he won't pick you I mean why would he?"
    show daisy_dress_serious2 at right:
        ease .5 zoom 1.0 xpos 1750
    hide olivia_dress_natural1
    show olivia_dress_angry1 at left:
        zoom 1.1 xpos 150
    ol "You little turd. Alright, I'm in."
    show olivia_dress_angry1 at left:
        ease .5 zoom 1.0 xpos 150
    show vanessa_dress_natural1 with dissolve
    vn "C'mon girls. I'm really hungry, let's go."
    show daisy_dress_serious2 at right:
        ease .5 zoom 1.1 xpos 1750
    ds "You can go wait outside, if you want. You don't have to force yourself to play games with much 'younger' people, [vn1]."
    show daisy_dress_serious2 at right:
        ease .5 zoom 1.0 xpos 1750
    vn "You really {i}are{/i} a little turd."
    ds "How about you, Amber. Are you in?"
    am "Sure, why not?"
    hide vanessa_dress_natural1 with dissolve
    hide olivia_dress_angry1 with dissolve
    hide daisy_dress_serious2 with dissolve
    show daisy_dress_smile1 with dissolve
    ds "Alright, [mc]. You will be the judge."
    ds "You have 3 beautiful young women and [vn1] in front of you."
    vn "What?!"
    hide daisy_dress_smile1
    ol "Just let it go, [vn1]."
    show daisy_dress_smile1 with dissolve:
        xpos 950 ypos 205
    show vanessa_dress_natural1 at left with dissolve:
        ypos 1120
    show olivia_dress_blushing2 at right with dissolve:
        ypos 1120
    show dress_amber_flirt2_eyes with dissolve:
        xpos 470 ypos 125
    mc "..."

    menu:
        "Daisy":
            $ daisy_rlt += 3
            jump v3_pickdaisy
        "Olivia":
            $ olivia_rlt += 3
            jump v3_pickolivia
        "Vanessa":
            $ vanessa_rlt += 3
            jump v3_pickvanessa
        "Amber":
            $ amber_rlt += 3
            jump v3_pickamber
label v3_pickdaisy:
    mc "I think I will say..."
    mc "Daisy."
    hide daisy_dress_smile1
    hide vanessa_dress_natural1
    hide olivia_dress_blushing2
    hide dress_amber_flirt2_eyes
    show daisy_dress_surprised2 with dissolve
    ds "YES!"
    ds "You really have great taste in women, [mc]."
    ol "Whatever..."
    vn "..."
    mc "Can we go now?"
    ds "Yep, let's go..."
    hide daisy_dress_surprised2
    jump v3_restourant
label v3_pickolivia:
    mc "I think I will say..."
    mc "Olivia."
    hide daisy_dress_smile1
    hide vanessa_dress_natural1
    hide olivia_dress_blushing2
    hide dress_amber_flirt2_eyes
    show daisy_dress_surprised1 with hpunch
    ds "WHAT?!"
    hide daisy_dress_surprised1
    show olivia_dress_blushing1 with dissolve
    ol "Really?! But... why?"
    mc "When I look at you, I'm astonished. You being my choice was inevitable."
    hide olivia_dress_blushing1
    show olivia_dress_flirting1 with dissolve
    ol "Oh my... Thank you, [mc]! I'm... I... I don't know what to say..."
    hide olivia_dress_flirting1
    show daisy_dress_angry1 at right with dissolve:
        xpos 1750
    ds "Maybe this game wasn't such a good idea."
    show olivia_dress_smile2 at left with dissolve:
        xpos 150
    ol "I disagree."
    ds "Let's just go..."
    hide daisy_dress_angry1
    hide olivia_dress_smile2
    jump v3_restourant
label v3_pickvanessa:
    mc "I think I will say..."
    mc "[vn1]."
    ds "Why her?"
    hide daisy_dress_smile1
    hide vanessa_dress_natural1
    hide olivia_dress_blushing2
    hide dress_amber_flirt2_eyes
    show vanessa_dress_natural1 with dissolve
    vn "Yes, [mc], why me?"
    mc "Well, why not? You are extremely beautiful, and incredibly hot in that dress..."
    mc "My words are not enough to describe your beauty, [vn1]."
    vn "I- I don't know what to say."
    vn "Thank you..."
    vn "If we are done with Daisy's little game, we should go now. Otherwise, we'll be late."
    hide vanessa_dress_natural1
    jump v3_restourant
label v3_pickamber:
    mc "I think I will say..."
    mc "Amber."
    hide daisy_dress_smile1
    hide vanessa_dress_natural1
    hide olivia_dress_blushing2
    hide dress_amber_flirt2_eyes
    show daisy_dress_natural1 with dissolve
    ds "Of course you will pick her."
    mc "What? No, it's not what you think."
    mc "She doesn't need anyone's approval to know how beautiful she is."
    mc "She is cute, funny, and really sexy."
    hide daisy_dress_natural1
    show daisy_dress_laugh1 with dissolve
    ds "And she's actually willing to have sex with you..."
    hide daisy_dress_laugh1
    show dress_amber_flirt2_eyes
    am "Yes, I {i}am{/i}."
    hide dress_amber_flirt2_eyes
    show dress_amber_blush2_eyes
    am "Oops, umm... did I say that out loud...?"
    mc "Yes..."
    vn "Maybe it's best we get going before anyone else says something... unexpected."
    mc "Good idea."
    hide dress_amber_blush2_eyes
    jump v3_restourant
label v3_restourant:
    stop music
    play music "sounds/background1.mp3"
    scene black with fade
    wtr "Welcome. Do you have a reservation?"
    wtr "Ah! Dr. Donovan. It's been a while..."
    vn "Yes, I know. I am always at work lately, but we are celebrating the return of [mc]."
    wtr "I see. Your table is ready. Shall I send the sommelier?"
    vn "Not necessary, we will have Cabernet Sauvignon. Let it breathe for at least 10 minutes before you bring it over."
    wtr "Great choice."
    mc "I assume you ordered red wine?"
    vn "Yes, honey. This place has the greatest Bordeaux Cabernet Sauvignon wine."
    scene black with fade
    scene v3_dinner1 with fade
    mc "Allow me."
    am "Thank you."
    scene black
    wtr "Are you ready to order?"
    mc "I'm sorry, but my menu has only one English word and that's... menu..."
    mc "Which one of these items is food?"
    am "Hahaha."
    scene v3_dinner7 with fade
    vn "I should probably take care of ordering the food."
    vn "I know what the girls and [mc] would prefer, but what would you like, Amber?"
    am "I'll let you decide for me."
    am "OH! I am allergic to shrimp. Anything else is fine."
    scene v3_dinner2 with fade
    vn "Okay, sweety."
    vn "I would like to order..."
    scene black with fade
    scene v3_dinner4 with fade
    mc "Wow, everything looks great!"
    am "Yes, and the wine is absolutely delicious."
    scene v3_dinner5 with fade
    vn "I'm glad you like it. Please, don't be shy. Dig in."
    scene black with fade
    scene v3_dinner19 with fade
    am "That's amazing, Vanessa. I've never eaten such a delicious meal in my life."
    mc "Just wait till you've tried [vn1]'s home cooking."
    scene v3_dinner5 with fade
    vn "Aww. You are so sweet, [mc]. I'm glad you enjoyed it, Amber."
    vn "So, Amber, tell me about yourself."
    am "Where should I start?"
    vn "Maybe you can start by telling us how you two met each other."
    am "Sure."
    scene v3_dinner4 with fade
    am "So, I moved out of my old place into the city not long ago after my boyfriend cheated on me with my best friend."
    ds "What a piece of shit."
    am "You have no idea..."
    am "Anyway, I was just leaving out to buy some new clothes."
    am "Then, suddenly, someone attacked me and tried to steal my purse."
    vn "Oh, god! That's terrible."
    scene v3_dinner4blur
    show dress_amber_sad2_eyes with dissolve
    am "I tried to fight back, but he was too strong for me."
    am "He took my bag and I collapsed on the ground."
    am "Suddenly a police officer started chasing him."
    am "His partner helped me up and tried her best to calm me down, but I was so scared."
    hide dress_amber_sad2_eyes
    show dress_amber_smile1_eyes with dissolve
    am "A few minutes later, the police officer came with my bag and the thief."
    am "He looked into my eyes and returned my bag to me."
    hide dress_amber_smile1_eyes
    show dress_amber_blush2_eyes with dissolve
    am "When our eyes met, I suddenly felt as light as the air, as though he had swept me off my feet."
    am "I did my best not to cry, but I couldn't hold it."
    am "That's when the police officer gave me a hug and held me tightly..."
    hide dress_amber_blush2_eyes
    show dress_amber_smile2_eyes
    am "His arms were so big and strong. I felt completely safe while he was holding me."
    am "He introduced himself to me."
    hide dress_amber_smile2_eyes
    show dress_amber_natural1_eyes
    am "Didn't even try hit on me. He was just doing his job."
    am "I waited for him to ask for my number, but he didn't."
    show dress_amber_natural1_eyes at right:
        xpos 1750
    show olivia_dress_smile1 at left with dissolve:
        xpos 150
    ol "What a gentleman."
    ol "So, what did you do?"
    show dress_amber_natural1_eyes at right:
        ease .5 zoom 1.1 xpos 1750
    am "What could I do? I asked him out, of course."
    am "There was no way I was going to let such a wonderful guy slip trough my hands."
    show dress_amber_natural1_eyes at right:
        ease .5 zoom 1.0 xpos 1750
    hide olivia_dress_smile1
    show vanessa_dress_natural1 at left with dissolve:
        xpos 150
    vn "Now, that's a smart girl."
    show olivia_dress_smile2 with dissolve
    ol "Such a lovely story."
    hide olivia_dress_smile2
    hide vanessa_dress_natural1
    hide dress_amber_natural1_eyes
    show daisy_dress_natural1 with dissolve
    ds "I'm really surprised, [mc]. Perhaps you {i}do{/i} have balls after all..."
    mc "You of all people would know that I have balls, Daisy."
    ds "{i}Oh, you fucking bastard.{/i}"
    hide daisy_dress_natural1
    show vanessa_dress_smile1 with dissolve
    vn "That's a wonderful story."
    vn "I'm really proud of you, [mc]."
    mc "Thanks."
    hide vanessa_dress_smile1
label v3_talkeveryonerst:
    scene black with fade
    menu:
        "Talk To Vanessa":
            if v3_vanessatalk2 == True:
                jump v3_vanessarst
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryonerst

        "Talk to Olivia":
            if v3_oliviatalk2 == True:
                jump v3_oliviarst
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryonerst
        "Talk to Daisy":
            if v3_daisytalk2 == True:
                jump v3_daisyrst
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryonerst
        "Talk to Amber":
            if v3_ambertalk1 == True:
                jump v3_amberrst
            mc "{i}(I've already spoken to her.){/i}"
            jump v3_talkeveryonerst
        "Continue":
            if v3_vanessatalk2 == False and v3_oliviatalk2 == False and v3_daisytalk2 == False and v3_ambertalk1 == False:
                jump v3_restaurant2
            mc "{i}(I haven't spoken to everyone yet.){/i}"
            jump v3_talkeveryonerst

label v3_vanessarst:
    if v3_vanessatalk2 == True:
        $ v3_vanessatalk2 = False
    scene v3_dinner7 with fade
    vn "It's been a while since we had dinner with the whole family together."
    vn "I'm really glad you decided to visit us, [mc]."
    mc "Yes, me too [vn1]. I wish [eg1] could be with us..."
    scene v3_dinner7blur
    show vanessa_dress_sad2 at left with dissolve:
        xpos 150
    vn "I know, honey. I've missed him, too."
    show olivia_dress_serious1 at right with dissolve:
        xpos 1750
    ol "I still remember that day..."
    ol "[vn1] told us the bad news. We were all devastated, but it seemed to affect you much more so than the rest of us, [mc]."
    ds "..."
    mc "Yes, but it was a long time ago. We have each other and a long happy life ahead of us."
    mc "We have to move on..."
    vn "{i}I wish I could believe you...{/i}"
    mc "Let's talk about something else."
    hide vanessa_dress_sad2
    hide olivia_dress_serious1
    menu:
        "How Is Everything At work?":
            jump v3_vanessarst1
        "Are You Able To Fill The Shoes Of [eg1]?":
            $ vanessa_rlt -= 1
            jump v3_vanessarst2
label v3_vanessarst1:
    mc "How is everything going at work?"
    show vanessa_dress_natural1 with dissolve
    vn "Everything is going great. My team works really hard every day to achieve our goals."
    mc "That's wonderful to hear."
    mc "You know, I've been working on [eg1]'s case and learned many things about his work."
    hide vanessa_dress_natural1
    show vanessa_dress_angry1 with dissolve
    vn "Really...? Like what?"
    mc "I know he did research for the government and the military."
    mc "I also know that you are now heading those projects."
    show vanessa_dress_angry1 at left with dissolve:
        xpos 150
    show daisy_dress_surprised1 at right with dissolve:
        xpos 1750
    ds "Are you serious?"
    ds "What kind of projects you are talking about?"
    ds "Laser guns, cloning people, flying soldiers...?"
    show olivia_dress_natural1 with dissolve
    ol "You watch too many movies, Daisy."
    ol "I'm sure her research is mostly on developing new biotech for the military or the government."
    mc "I don't think [vn1] will tell us anything..."
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.1 xpos 150
    vn "No, [mc], I won't, and I can't talk about those projects with anyone."
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.0 xpos 150
    mc "Not even with your family?"
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.1 xpos 150
    vn "Especially with my family."
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.0 xpos 150
    mc "{i}At least now I'm sure that you are still working on [eg1]'s classified projects...{/i}."
    mc "I completely understand, [vn1]."
    hide daisy_dress_surprised1
    show daisy_dress_smile1 at right with dissolve:
        xpos 1750
    ds "Just let me know when I will able to fly, okay?"
    vn "Sure, honey..."
    hide daisy_dress_smile1
    hide vanessa_dress_angry1
    hide olivia_dress_natural1
    jump v3_talkeveryonerst
label v3_vanessarst2:
    mc "So... are you able to fill the shoes of [eg1]?"
    show vanessa_dress_serious2 at left with dissolve:
        xpos 150

    vn "What?"
    show dress_amber_angry1_eyes at right with dissolve:
        xpos 1750
    am "That was a little rude, [mc]."
    hide dress_amber_angry1_eyes
    show olivia_dress_natural1 at right with dissolve:
        xpos 1750
    ol "Yes."
    ol "What kind of question is that?"
    ol "[vn1] is more than capable of working as a team leader for any science group."
    hide olivia_dress_natural1
    show daisy_dress_natural1 at right with dissolve:
        xpos 1750
    ds "Yes, she is, but is she really as good as [eg1]?"
    ds "I mean he was sort of like an Einstein of his generation, right?"
    show vanessa_dress_serious2 at left with dissolve:
        ease .5 zoom 1.1 xpos 150
    vn "Enough with this nonsense!"
    vn "Yes, [mc], I'm able to fill the shoes of [eg1] as the team's leader and the head scientist."
    hide daisy_dress_natural1 with dissolve
    hide vanessa_dress_serious2
    show vanessa_dress_serious2 with dissolve

    mc "I didn't mean to offend you. My words were poorly chosen."
    vn "You think so?"
    mc "I'm sorry."
    mc "I just wanted to know how everything's going at work."
    hide vanessa_dress_serious2
    hide daisy_dress_natural1
    show vanessa_dress_smile1 with fade
    vn "Okay, that's better."
    vn "Everything is going great. My team works really hard every day to achieve our goals."
    hide vanessa_dress_smile1
    mc "That's wonderful to hear."
    mc "You know, I've been working on [eg1]'s case and learned many things about his work."
    show vanessa_dress_angry1 with dissolve
    vn "Really...? Like what?"
    mc "I know he did research for the government and the military."
    mc "I also know that you are now heading those projects."
    show vanessa_dress_angry1 at left with dissolve:
        xpos 150
    show daisy_dress_surprised1 at right with dissolve:
        xpos 1750
    ds "Are you serious?"
    ds "What kind of projects you are talking about?"
    ds "Laser guns, cloning people, flying soldiers...?"
    show olivia_dress_natural1 with dissolve
    ol "You watch too many movies, Daisy."
    ol "I'm sure her research is mostly on developing new biotech for the military or the government."
    mc "I don't think [vn1] will tell us anything..."
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.1 xpos 150
    vn "No, [mc], I won't, and I can't talk about those projects with anyone."
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.0 xpos 150
    mc "Not even with your family?"
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.1 xpos 150
    vn "Especially with my family."
    show vanessa_dress_angry1 at left:
        ease .5 zoom 1.0 xpos 150
    mc "{i}At least now I'm sure that you are still working on [eg1]'s classified projects...{/i}."
    mc "I completely understand, [vn1]."
    hide daisy_dress_surprised1
    show daisy_dress_smile1 at right with dissolve:
        xpos 1750
    ds "Just let me know when I will able to fly, okay?"
    vn "Sure, honey..."
    hide daisy_dress_smile1
    hide vanessa_dress_angry1
    hide olivia_dress_natural1

    jump v3_talkeveryonerst

label v3_oliviarst:
    if v3_oliviatalk2 == True:
        $ v3_oliviatalk2 = False
        scene v3_dinner8 with fade
        menu:
            "Compliment Her":
                $ olivia_rlt += 1
            "Ask Her If She Liked The Food":
                jump v3_oliviarst1
        mc "I know I've already said this, but you look fantastic in that dress, Olivia."
        ol "Oh! Umm... thank you. Again."
        am "Yes, absolutely."
        am "You look so pretty it makes me kinda jealous."
        ol "Really?"
        scene v3_dinner8blur
        show vanessa_dress_natural1 with dissolve

        vn "See, honey? I told you. You're a real beauty."
        vn "I've never understood why you are trying so hard to hide yourself."
        mc "I don't think this is about hiding herself."
        mc "She is just happy with the way she lives her life."
        mc "Playing video games and having mostly online friends might sound weird for most people."
        mc "If you ask me, there is nothing wrong with that."
        hide vanessa_dress_natural1
        show olivia_dress_smile2 with dissolve
        ol "Thank you so much, [mc]."
        ol "He is right. I'm happy with how I live my life."
        hide olivia_dress_smile2
        show olivia_dress_natural1 with dissolve

        ol "For instance, I can't live like Daisy."
        ol "She is with her friends all the time, changes boyfriends like she changes clothes."
        show vanessa_dress_smile1 at left with dissolve:
            xpos 150
        vn "I agree with you. Even though I would like to see you become more socially active, I disapprove of the way Daisy lives, too."
        show daisy_dress_angry1 at right with dissolve:
            xpos 1750
        ds "How did this suddenly become about me?"
        ds "Going out and spending time with friends is not a bad thing."
        show vanessa_dress_smile1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "That's not the problem, Daisy."
        vn "The problem is these so-called 'friends' you are talking about."
        vn "They are a good for nothing bunch of idiots who have no future."
        vn "Except Robin, of course."
        show vanessa_dress_smile1 at left:
            ease .5 zoom 1.0 xpos 150
        show olivia_dress_natural1:
            ease .5 zoom 1.1
        ol "I still don't understand why a girl like Robin hangs out with you."
        mc "{i}I can think of a few reasons...{/i}."
        show olivia_dress_natural1:
            ease .5 zoom 1.0
        hide daisy_dress_angry1
        show daisy_dress_angry2 at right with dissolve:
            xpos 1900
        ds "Oh, shut up, Olivia!"
        ds "You know nothing about me or her."
        hide vanessa_dress_smile1
        show vanessa_dress_angry1 at left with dissolve:
            xpos 150
        vn "Don't talk to your sister like that."
        mc "Guys, let's just calm down and change the subject."
        mc "We have a guest with us."
        vn "You are right, honey."
        vn "Sorry about that, Amber."
        vn "Let's just enjoy each other's company."
        hide vanessa_dress_angry1
        hide daisy_dress_angry2
        hide olivia_dress_natural1
        jump v3_talkeveryonerst
label v3_oliviarst1:
    scene v3_dinner8 with fade

    mc "Did you like the food, Olivia?"
    ol "Oh yes! It was delicious."
    ol "Oh, and the wine is wonderful, too!"
    vn "I'm glad to hear that, sweetheart."
    vn "By the way, you look stunning in that dress."
    ol "Stop it, [vn1]."
    am "No, please don't stop, Vanessa."
    am "You look gorgeous, Olivia."
    ol "Oh! Umm... thank you!"
    vn "I've never understood why you are trying so hard to hide yourself."
    mc "I don't think this is about hiding herself."
    mc "She is just happy with the way she lives her life."
    mc "Playing video games and having mostly online friends might sound weird for most people."
    mc "If you ask me, there is nothing wrong with that."
    hide vanessa_dress_natural1
    scene v3_dinner8blur
    show olivia_dress_smile2 with dissolve
    ol "Thank you so much, [mc]."
    ol "He is right. I'm happy with how I live my life."
    hide olivia_dress_smile2
    show olivia_dress_natural1 with dissolve

    ol "For instance, I can't live like Daisy."
    ol "She is with her friends all the time, changes boyfriends like she changes clothes."
    show vanessa_dress_smile1 at left with dissolve:
        xpos 150
    vn "I agree with you. Even though I would like to see you become more socially active, I disapprove of the way Daisy lives, too."
    show daisy_dress_angry1 at right with dissolve:
        xpos 1750
    ds "How did this suddenly become about me?"
    ds "Going out and spending time with friends is not a bad thing."
    show vanessa_dress_smile1 at left:
        ease .5 zoom 1.1 xpos 150
    vn "That's not the problem, Daisy."
    vn "The problem is these so-called 'friends' you are talking about."
    vn "They are good for nothing bunch of idiots who have no future."
    vn "Except Robin, of course."
    show vanessa_dress_smile1 at left:
        ease .5 zoom 1.0 xpos 150
    show olivia_dress_natural1:
        ease .5 zoom 1.1
    ol "I still don't understand why a girl like Robin hangs out with you."
    mc "{i}I can think of a few reasons...{/i}."
    show olivia_dress_natural1:
        ease .5 zoom 1.0
    hide daisy_dress_angry1
    show daisy_dress_angry2 at right with dissolve:
        xpos 1900
    ds "Oh, shut up, Olivia!"
    ds "You know nothing about me or her."
    hide vanessa_dress_smile1
    show vanessa_dress_angry1 at left with dissolve:
        xpos 150
    vn "Don't talk to your sister like that."
    mc "Guys, let's just calm down and change the subject."
    mc "We have a guest with us."
    vn "You are right, honey."
    vn "Sorry about that, Amber."
    vn "Let's just enjoy each other's company."
    hide vanessa_dress_angry1
    hide daisy_dress_angry2
    hide olivia_dress_natural1
    jump v3_talkeveryonerst
label v3_daisyrst:
    if v3_daisytalk2 == True:
        $ v3_daisytalk2 = False
        scene v3_dinner3 with fade
        mc "{i}Daisy kept looking at Amber like food during the whole dinner.{/i}"
        mc "{i}This little devil won't dare to do anything weird, I hope...{/i}"
        scene v3_dinner9 with fade
        mc "Hey, Daisy."
        ds "..."
        mc "Daisy!"
        scene v3_dinner10 with fade
        ds "What?"
        mc "What's on your mind?"
        ds "What do you mean?"
        mc "You seem really focused on something... particular."
        mc "I was just wondering if maybe you wanted to talk about that."
        ds "Hmm... Let me think..."
        ds "Nope. I'm good."
        mc "I'm sure you are..."
        scene v3_dinner9 with fade
        ds "So, Amber. Tell me about yourself."
        ds "We heard the story of how you met [mc]."
        ds "But, I want to get to know you better."
        ds "Tell me your hobbies, what do you do for a living, {i}would you consider to let me dine on your tight hot body!{/i}"
        mc "What was that?"
        scene v3_dinner10 with fade
        ds "Huh?"
        mc "You mumbled something."
        ds "What are you talking about? Someone has clearly had too much wine tonight."
        mc "..."
        scene v3_dinner9 with fade
        ds "Where was I...? Right, you were going to tell me about yourself, Amber."
        scene v3_dinner9blur
        show dress_amber_natural1_eyes with dissolve
        am "There is not so much to tell actually."
        am "I'm working at a clothing store as a saleswoman."
        am "Living at my friend's house. For now, of course."
        am "I don't have that many hobbies. I enjoy reading books, and-"
        hide dress_amber_natural1_eyes
        scene v3_dinner9 with fade
        ds "{i}You are so hot. I want to eat you up so bad.{i}"
        am "When I was at college, I met this-"
        ds "{i}Well we haven't ordered dessert yet. I wonder if can I have her with some chocolate sauce and strawberries...{/i}"
        am "Oh and the funniest thing happened: there was this girl-"
        ds "{i}She has nice breasts. They are not as big as Robin's, but they look so firm and good.{i}"
        ds "{i}I wonder if she would let me bury my face between them. She seems like a nice person, I'm sure she would...{i}"
        am "Well, that's about everything about me."
        ds "Huh?"
        ds "Oh, right! What a great story."
        am "..."
        ds "By the way, I love your tattoos. I want to get a tattoo, but [vn1] won't let me..."
        am "Oh, thanks! Some people hate them, but I think they look good."
        scene v3_dinner11 with fade
        ds "Well, there are lots of girls without tattoos. If they don't like it, they can always look for someone else."
        scene v3_dinner12 with fade
        ds "Oops! I dropped my fork. Hehe, silly me."
        ds "Excuse me."
label v3_undertable:
    stop music
    play music "sounds/cafe.mp3"
    scene v3_dinner13 with fade
    ds "Look what we have here."
    ds "She has such smooth, beautiful, long legs."
    ds "I wonder how they feel."
    ds "Just a little touch. It's not a big deal."
    ds "I mean, I'm looking for my fork. I might accidentally bump her leg."
    scene v3_dinner19
    am "..."
    scene v3_dinner14 with fade
    ds "Her skin is so smooth!"
    ds "I hate you [mc]..."
    scene v3_dinner20 with fade
    am "Huh?!"
    mc "Is something wrong?"
    scene v3_dinner19 with fade
    am "No, everything's fine."
    scene v3_dinner13 with fade
    ds "That was close."
    ds "Totally worth it, though."
    ds "Okay. That's enough, Daisy. No need to push your luck."
    ds "Time to get back to your seat."
    ds "Any moment now..."
    ds "Any moment..."
    scene v3_dinner15 with fade
    ds "..."
    ds "Fuck it!"
    ds "This is so fucking exciting."
    ds "..."
    mc "{i}What's taking her so long?{/i}"
    mc "{i}Don't tell me...{/i}"
    scene v3_dinner16 with hpunch
    mc "Oh crap!"
    am "What?"
    ds "..."
    mc "DAISY!"
    scene v3_dinner17 with hpunch
    ds "Shit!"
    mc "What the fuck are you doing?!"
    ds "Ummm..."
    ds "Looking for my fork."
    scene v3_dinner16 with fade
    mc "Really? Seemed you were trying to reach {i}her{/i} fork."
    ds "What? Oh! Well..."
    vn "What's going on down there?"
    scene v3_dinner18 with fade
    ds "Look, I found my fork."
    ds "Stupid me how did I miss it? Hehe."
    mc "Yes, how indeed..."
    am "Is everything okay?"
    mc "Yes, everything is fine."
    mc "{i}I'll deal with you later, you little fucking devil!{/i}"
    stop music
    scene v3_dinner21 with vpunch

    mc "WOW!"
    vn "What's wrong honey."
    mc "{i}Look at the view...{/i}"
    ol "[mc]?"
    mc "..."
    scene v3_dinner7 with fade
    mc "What?"
    vn "Are you okay honey?"
    mc "Yeah, yeah. I'm fine."
    jump v3_talkeveryonerst
label v3_amberrst:
    if v3_ambertalk1 == True:
        $ v3_ambertalk1 = False
        scene v3_dinner6 with fade
        play music "sounds/background2.mp3"
        mc "So, what do you think about my family?"
        am "I loved them!"
        am "Especially Vanessa! She is a wonderful woman."
        mc "I'm glad to hear that."
        mc "I know you wanted to spend some alone time with me, but I'm sure we can spend some time together at home."
        mc "Maybe we can watch a movie together and drink wine."
        am "Sounds wonderful."
        scene v3_dinner6blur
        show vanessa_dress_natural1 at left with dissolve:
            xpos 150
        vn "Did you go to college, Amber?"
        show dress_amber_smile1_eyes at right with dissolve:
            xpos 1750
        am "Yes, I did."
        am "I graduated 2 years ago."
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "What did you major in?"
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.0 xpos 150
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.1 xpos 1750
        am "Chemical Engineering."
        mc "Really?"
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.0 xpos 1750
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "You didn't know?"
        mc "No."
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.0 xpos 150
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.1 xpos 1750
        am "That's fine. We only met two days ago."
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.0 xpos 1750
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "I don't understand. Why do you work at a clothing store?"
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.0 xpos 150
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.1 xpos 1750
        am "I would love to work as a chemical engineer, but I'm having trouble finding any job in the field."
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.0 xpos 1750
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "I'm sorry to hear that, honey."
        vn "Tell you what. I will make a few phone calls and see what we can do for you."
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.0 xpos 150
        show dress_amber_smile1_eyes at right:
            ease .5 zoom 1.1 xpos 1750
        am "You don't have to do that, Vanessa."
        am "You don't even know if I'm good at my job."
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.1 xpos 150
        vn "I'm not saying that I will give you a job just like that."
        vn "I'll only try to make things easier for you. If you want to get job, you'll have to earn it by yourself."
        show vanessa_dress_natural1 at left:
            ease .5 zoom 1.0 xpos 150
        hide dress_amber_smile1_eyes
        show dress_amber_smile2_eyes at right with dissolve:
            xpos 1750
        am "I don't know what to say."
        am "Thank you so much, Vanessa."
        vn "You are welcome, honey."
        hide dress_amber_smile2_eyes
        hide vanessa_dress_natural1
        jump v3_talkeveryonerst
label v3_restaurant2:
    stop music
    scene v3_dinner7 with fade
    mc "Thank you so much for dinner and everything, [vn1]."
    am "Yes, Vanessa. It was delightful."
    vn "You are welcome."
    vn "Let me get the check so we can leave."
    am "Our plan hasn't changed, right?"
    mc "Absolutely. We can watch a movie and relax in the living room after everyone falls asleep."
    scene black with fade
    nr "In front of Donovan house..."

label v3_daisymctalk:
    scene v3_mcdaisytalk1 with fade
    mc "Wait!"
    mc "We need to talk."
    ds "What?"
    menu:
        "GET YOUR SHIT TOGETHER!":
            $daisy_rlt -= 2
            jump v3_daisymctalka
        "Stop Acting Like That!":
            jump v3_daisymctalkb
        "Nevermind...":
            mc "You know what? Maybe another time..."
            jump v3_homenight
label v3_daisymctalka:
    scene v3_mcdaisytalk2 with fade
    mc "I've had enough of your bullshit!"
    ds "Excuse me?"
    with hpunch
    mc "Just shut your mouth and listen!"
    ds "..."
    mc "I don't care how you act around your friends, but..."
    mc "The things you've done around Amber are unacceptable."
    mc "Especially the thing you tried to pull under the table!"
    ds "Hey! I wasn't tr-"
    with hpunch
    mc "Don't interrupt!"
    mc "This is your last warning."
    mc "Now, if you ever try to do anything unacceptable around me or my guest again, you won't enjoy what's coming your way."
    mc "Never, EVER forget that!"
    ds "{i}I'm sorry.{/i}"
    mc "What was that? Can't hear you."
    ds "I said I'm sorry."
    mc "Good. Now, let's get back in and {i}don't{/i} disturb me and Amber."
    ds "Okay."
    scene black
    pause 2.0
    jump v3_homenight
label v3_daisymctalkb:
    scene v3_mcdaisytalk2 with fade
    mc "Look, Daisy."
    mc "I know I wasn't there for you when you needed me the most and I'm sure you had a hard time with dealing [eg1]'s absence."
    mc "But, none of that gives you to right to act that way."
    ds "You can't tell me how to-"
    with hpunch
    mc "Listen to me!"
    mc "I'm not like Olivia or [vn1]."
    mc "My patience has a limit. If you ever cross the line again, with me or with any of my guests..."
    ds "What? What are you gonna do if I cross the 'line'."
    mc "Trust me, Daisy. You have no idea what I'm capable of."
    ds "Is that a threat?!"
    mc "No. It's a sincere warning that you should take 'seriously'..."
    ds "..."
    mc "It's getting cold. Let's go inside."
    mc "I hope you won't force me to do something I may end up regretting..."
    scene black
    pause 2.0
    jump v3_homenight


label v3_homenight:
    play music "sounds/cafe.mp3"
    scene v3_amber_mc1 with fade
    mc "What do you want to watch?"
    am "Hm... I don't know. You pick."
    mc "Umm..."
    mc "How about a Tarantino movie?"
    am "Yes, sure! I love his movies."
    mc "Alright, then."
    mc "By the way, about Daisy..."
    am "What about her?"
    mc "I don't know what was up with the way she was acting."
    mc "Sometimes she can be a real pain in the ass."
    mc "I think something is seriously wrong with her."
    am "C'mon give her a break."
    am "She acted pretty weird around me, I admit, but it's understandable."
    mc "How come?"
    am "Well, she lost [eg4] when she was only a little child. You weren't there for her for most of her life."
    am "She just wants attention that's all."
    mc "Hm, I don't know. Maybe..."
    mc "How would you explain the way she was acting at dinner, then?"
    am "She accidentally touched my leg while looking for her fork, so what?"
    mc "No, it was-"
    mc "Nevermind."
    am "Forget about Daisy. Come here."
    am "I want to cuddle with you."
    mc "Okay."
    scene black with fade
    "20 minutes later..."
    scene v3_amber_mc2 with fade
    am "It's been a while since I've watched Kill Bill."
    mc "It's one of my favorite movies."
    am "I really like it, but it's not my favorite."
    am "My favorite movie is Forrest Gump."
    mc "Really? Mine too!"
    mc "Tom Hanks is the best actor in the world, don't you think?"
    am "YES! I love all of his movies."
    scene v3_amber_mc3 with fade
    am "Look, that's my favorite scene in this movie."
    mc "Ah, the 'wiggle your big toe' scene."
    am "Tarantino always focuses on the actor's feet in his movies. He has a major foot fetish."
    mc "Yeah..."
    stop music
    scene v3_amber_mc4 with fade
    mc "..."
    am "Huh?"
    scene v3_amber_mc5 with fade
    am "{i}Is he getting hard?{/i}"
    play music "sounds/sexscene1.mp3"
    am "Looks like Tarantino isn't the only one who has a foot fetish! Hehe."
    mc "What? Ohh!"
    mc "Well..."
    am "I was gonna wait until the movie ended, but it looks like our friend here can't wait anymore."
    mc "Sorry."
    scene v3_amber_mc6 with fade
    am "Oh, {i}don't{/i} be."
    am "I can't wait the see this fellow again."
    mc "We can't, someone might catch us."
    am "C'mon, it's gonna be fine."
    am "Everyone is sleeping."
    scene black with fade
    mc "I don't kno-"
    scene v3_amber_mc7 with fade
    mc "Mmmm."
    scene v3_amber_mc8 with fade
    am "Yes! Just relax and let me take care of everything."
    am "Just like that."
    am "Doesn't it feel so good?"
    mc "Yeah!"
    mc "Mmm."
    scene v3_amber_mc7 with fade
    mc "Your hands are so soft."
    mc "Go a little bit faster."
    am "I love jerking your hard cock."
    am "It feels so hot in my hand."
    mc "OH!"
    menu:
        "Footjob":
            am "{i}I wonder...{/i}"
        "Blowjob":
            jump v3_blowjob
    scene black with fade
    mc "Why did you st-"
    scene v3_amber_mc9 with fade
    mc "OHH!"
    am "You're really into the feet stuff, aren't you?"
    am "I've never done anything like this, but I'll make an exception just for you."
    mc "THANK YOU!"
    mc "OH GOD!"
    scene v3_amber_mc10 with fade
    am "Careful, they will hear you."
    mc "Sorry It just feels {i}so{/i} {b}good{/b}!"
    am "Don't be so loud or I'll stop!"
    mc "Please, don't stop."
    mc "I won't make any noise..."
    am "That's better."
    am "Do you remember our first night?"
    mc "Yes..."
    am "You were really cocky that night."
    am "Now, It's my turn!"
    am "Suck on my feet!"
    mc "Gladly!"
    scene v3_amber_mc11 with fade
    am "Mmm."
    am "YES! Just like that. Suck my toes."
    mc "Mhmhm."
    am "You like the feeling of my feet on your dick, don't you?"
    mc "Mmph, yes..."
    scene v3_amber_mc12 with fade
    am "You are not supposed to talk with your mouth full. Didn't your mother teach that?"
    mc "Sorry."
    scene black with fade
    scene v3_mcamber1
    mc "OH GOD, YESS!"
    am "Seriously, be quiet."
    mc "Sorry."
    mc "It feels so good. Are you sure you haven't done this before?"
    scene v3_mcamber2 with fade
    am "Nope. This a first for me. I guess I'm just natural."
    mc "Yes, you are! You're doing an amazing job."
    am "Thank you."
    mc "In fact, you are way too good. I think I'm gonna cum."
    scene v3_amber_mc23 with hpunch
    am "NO!"
    am "You are not allowed to cum yet!"

    am "Here. I will use only one foot."
    am "Try to hold back."
    scene v3_mcamber3 with fade
    mc "Mmm."
    mc "It's so hard!"
    mc "Your feet just feel AMAZING!"
    mc "Please, Amber. I can't hold it anymore."
    am "Fine."

    mc "OH GOD."
    scene v3_amber_mc13 with flash
    pause 0.5
    am "What the-"

    scene v3_amber_mc13 with flash
    pause 0.5
    mc "AHHH!"
    scene v3_amber_mc13 with flash
    pause 1.2

    mc "YESS."
    am "Haha. Wow. Look at all that hot cum."
    mc "Pant... Pant... Pant..."
    scene black with fade
    am "You were like a fucking fire hose!"
    mc "That was AMAZING."
    am "We are not done yet."
    mc "I think I'm done for the night."
    am "Oh, no, you're not!"
    am "Just sit back and relax. I will get you ready again in no time."
    mc "Okay."
    scene v3_mcamber4 with fade
    am "Mhmhm."
    mc "Wow."
    mc "You're {i}really{/i} eager tonight."
    am "Mhmhm. Yes. I. Am."
    scene black with fade
    am "See? Ready for round two."
    scene v3_amber_mc26 with fade
    am "I will give you the ride of your life, [mc]."
    scene v3_amber_mc27 with hpunch
    am "Ah! It's finally in me!"
    mc "AHH!"
    scene v3_mcamber5 with fade
    am "Mmm! AHH! AHH!"
    am "OH, YES. I fucking love your cock."
    mc "Slow down! You're gonna break the couch!"
    am "Shut up!"
    am "OH GOD, YES! I LOVE IT! I LOVE IT! I LOVE IT!"
    mc "Shit, Amber! You become a crazy slut during sex."
    am "Mmm. So what? Mmm! Ahh! I'm a crazy slut who loves to ride your fucking cock."
    am "I want to feel you deep inside of me."
    mc "You are incredible."
    mc "OH! AHHH!"
    mc "Yes! Take it... Take it ALL!"

    if amber_rlt >= 3:
        menu:
            "Cum Inside":
                jump v3_amber_climax1
            "Cum On Her Face":
                jump v3_amber_climax2
    elif amber_rlt < 3:
        menu:
            "Cum Inside (disabled)" :
                "Not enough points"
            "Cum On Her Face":
                jump v3_amber_climax2

label v3_amber_climax1:
    mc "I'm about to cum."
    am "Hang in there just a little longer. I'm almost there."
    am "Please, [mc]! Just a few more seconds AHHH-"
    am "Just a little longer."
    mc "AHH."
    mc "I'm trying, but you are so fucking HOT. I- I can't anymore."
    scene v3_amber_mc17 with fade
    am "OH GOD YES! I AM CUMMING AHH!"

    mc "OHHH!"
    scene v3_amber_mc16 with hpunch
    pause 0.5
    scene v3_amber_mc16 with flash
    pause 0.5
    scene v3_amber_mc16 with flash
    pause 0.5
    scene v3_amber_mc15 with fade
    am "That was FUCKING AMAZING!"
    mc "Pant... Yeah... Let- Let me just catch my-"
    mc "Pant... Breath."
    mc "..."
    am "Are you okay?"
    mc "No, I'm not okay, you freaking crazy slut!"
    am "Hahaha."
    scene black with fade
    am "I think I've just literally rocked your world!"
    mc "Damn right, you did!"
    am "Do you want to finish the movie?"
    mc "No. Let's just go to bed. I'm exhausted."
    am "Alright."
    stop music
    jump version_04
label v3_amber_climax2:
    mc "I'm about to cum."
    am "Hang in there just a little longer. I'm almost there."
    am "Please, [mc]! Just a few more seconds AHHH-"
    am "Just a little longer."
    mc "AHH."
    mc "I'm trying, but you are so fucking HOT. I- I can't anymore."
    scene v3_amber_mc17 with fade
    am "OH GOD YES! I AM CUMMING AHH!"

    mc "OHHH!"
    scene v3_amber_mc18 with hpunch
    pause 0.5
    scene v3_amber_mc19 with flash
    pause 0.5
    scene v3_amber_mc20 with flash
    pause 1.0
    am "That was FUCKING AMAZING!"
    mc "Pant... Yeah... Let- Let me just catch my-"
    mc "Pant... Breath."
    mc "..."
    am "Are you okay?"
    mc "No, I'm not okay, you freaking crazy slut!"
    am "Hahaha."
    scene black with fade
    am "I think I've just literally rocked your world!"
    mc "Damn right, you did!"
    am "Do you want to finish the movie?"
    mc "No. Let's just go to bed. I'm exhausted."
    am "Alright."
    stop music
    jump version_04
label v3_blowjob:
    scene black with fade
    "Why did you st-"
    scene v3_amber_mc14 with hpunch
    am "Mmmm."
    mc "OHH!"
    scene v3_mcamber4 with fade
    mc "GOD! I've missed feeling your beautiful lips on my dick."
    am "Mhmhm."
    mc "Yes, keep going!"
    mc "OHH!"
    scene v3_amber_mc26 with fade
    am "I will give you the ride of your life, [mc]."
    scene v3_amber_mc27 with hpunch
    am "Ah! It's finally in me!"
    mc "AHH!"
    scene v3_mcamber5 with fade
    am "Mmm! AHH! AHH!"
    am "OH, YES. I fucking love your cock."
    mc "Slow down! You're gonna break the couch!"
    am "Shut up!"
    am "OH GOD, YES! I LOVE IT! I LOVE IT! I LOVE IT!"
    mc "Shit, Amber! You become a crazy slut during sex."
    am "Mmm. So what? Mmm! Ahh! I'm a crazy slut who loves to ride your fucking cock."
    am "I want to feel you deep inside of me."
    mc "You are incredible."
    mc "OH! AHHH!"
    mc "Yes! Take it... Take it ALL!"

    if amber_rlt >= 3:
        menu:
            "Cum Inside":
                jump v3_amber_climax1
            "Cum On Her Face":
                jump v3_amber_climax2
    elif amber_rlt < 3:
        menu:
            "Cum Inside (disabled)" :
                "Not enough points"
            "Cum On Her Face":
                jump v3_amber_climax2


























label gameover:
    stop music
    scene black with fade
    nr "Version 0.4 is over."
    nr "{a=https://discord.gg/M5Rh2Yu}www.discord.gg{/a} Please visit our discord channel. You can access previews and news about our game."
    nr "{a=https://www.patreon.com/purplefellas}www.patreon.com/purplefellas{/a} You can support us from our patreon page and help us to make this game better with each update."
    nr "Please do not hesitate to share your ideas, comments and suggestions with us. Your feedback is really important to us."
    nr "Thank you so much for playing our game!"
    jump main
label badend:
    stop music
    scene gameover
    nr "You haven't seen the true ending yet!"
    nr "{a=https://discord.gg/M5Rh2Yu}www.discord.gg{/a} Please visit our discord channel. You can access previews and news about our game."
    nr "{a=https://www.patreon.com/purplefellas}www.patreon.com/purplefellas{/a} You can support us from our patreon page and help us to make this game better with each update."
    menu:
        "You can go back to breaking point of the game, start over or return to main menu."
        "Go Back To Breaking Point":
            jump breakingpoint
        "Start Over":
            jump start
        "Return Main Menu":
            jump main




    pause
label main:







    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.



    # This ends the game.
