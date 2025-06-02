###############################################################
############## Chapter 1: Movie Night - Felix #################
###############################################################
label felixMovie:
    show movie bg
    with fade

    show Player:
        xpos 0.01
        ypos 0.6
    mc "(I really hope this outfit isn’t too cozy…)"
    mc "(Since it’s a movie night, something comfy is just fine, right?)"
    mc "(Though Nadia did say on the way that there would be upperclassmen here…)"
    mc "(Maybe I should’ve dressed a little more professionally to leave a good impression.)"
    mc "(Agh, especially if upperclassmen from the fashion department will be here!)"
    mc "(I still have time to go change if I sprint to my dorm–)"
    mc "Hey, Nadia I think I’m gonna head back really quick, but I’ll be back in a sec."

    show bsf sad
    Nadia "Wait, wait why!"
    Nadia "Your outfit is so cutieful!"

    show bsf normal
    mc "Really? I’m not sure if it would leave a good impression on fashion students though…"
    hide bsf normal
    with dissolve

    #Felix
    anon "No, no. I agree with Nadia. Totally cutieful."
    mc "!"
    #Felix sprite appears
    show artguy normal
    with dissolve
    mc "Felix…"

    show artguy normal:
        xpos .5
        ypos 1.0
    show bsf speak:
        xpos 1.0
        ypos 0.5
    Nadia "Seeeee! Everyone agrees. You’re the most cutieful cutest cutie pie here."
    Nadia "So stop worrying!"
    Nadia "I’m gonna go get us some popcorn while you and your friend talk, okay?"
    #Nadia sprite hide
    mc "(What’s with the grin on her face…)"
    mc "(She totally just left me here alone with Felix…)"
    mc "(And in this outfit!)"
    Felix "What are you looking so worried for?"
    menu:
        "Be open with him":
            jump felixOpen
        
        "Keep your concerns to yourself":
            jump felixConcerns

label felixOpen:
    mc "Ah just…wondering if my outfit is too informal…"
    Felix "You’re better dressed than I am, that’s for sure."
    mc "..."
    Felix "Relax, you look cute."
    mc "I don’t want to leave a bad first impression on the upperclassmen is all…"
    Felix "Well, as an upperclassman,"
    Felix "I’m telling you that you look cute."

    jump felixMovie2

label felixConcerns:
    mc "Ah, it’s nothing really."
    Felix "You sure?"
    mc "Mhm. Just a little nervous, that’s all."
    Felix "Huh…I won’t push it, but I want you to be able to tell me if something’s wrong."

    jump felixMovie2

label felixMovie2:
    mc "Thanks. I’m glad that I have someone that I can count on."
    Felix "Hey, you lean on me, I lean on you."
    Felix "That’s how I hope my friends can see me."
    mc "Will there ever really be a time where you can lean on me? You seem like you have everything figured out…"
    Felix "That’s-"
    anon "[povname]!"
    #Nadia sprite show
    Nadia "Turns out, we got here kindaaaa late. Movie’s about to start!"
    Nadia "The beanbags near the front look real comfy and I wanna snag them before someone else does."
    menu:
        "Sit with Felix":
            jump felixSit

        "Go with Nadia":
            jump nadiaGo

label felixSit:
    mc "I think I wanted to catch up with Felix a little bit. Mind if I come sit a little later?"
    Nadia "Hey, more beanbag space for me! I’m not complaining!"
    Nadia "Have fun…alone together…"
    mc "There’s that grin again!"
    #Nadia sprite hide
    Felix "Should we sit near the back? It’s a quieter and a little less crowded."
    mc "Sure, but I’m starved."
    Felix "You can go grab seats and I’ll bring some snacks over."
    #Scene change maybe cg of them sitting next to each other w popcorn idk
    mc "Do you know what they’re showing?"
    Felix "I think it’s some comedy film? The coordinators wanted to keep the mood light."
    mc "Well, I guess we’re about to see."

    centered "{color=#ffffff}Thank You For Playing{/color}"
    return


label nadiaGo:
    mc "Ooh, I was eyeing those when I walked in too."
    Felix "We can catch up later. Go grab those seats with your friend. I think everyone wants dibs on ‘em."
    mc "It was nice to run into you again, Felix."
    Nadia "I think your friend wanted to talk to you a little longer. You should’ve gone with him! I wouldn’t mind having to mingle with new people."
    mc "No, no don’t worry about it. I’m sure that I’ll get another chance to chat with him."
    Nadia "Alrightie, if you say so."
    Nadia "C’mon, movie’s starting! I heard it’s one of those comedy heist kinda movies."

    centered "{color=#ffffff}Thank You For Playing{/color}"
    return

###############################################################
############## Chapter 1: Movie Night - Addie #################
###############################################################
label addieMovie:
    Addie "Omg [povname] you made it!!"
    mc "Oh hey Addie!"
    Addie "So were you able to find the dorms ok?"
    mc "Yeah! Well…"
    Addie "Well?"
    mc "..."
    Addie "Wait, you didn’t walk all the way there, did you?"
    mc "Um, yeah."
    Addie "HAHAHA! I’m so sorry, I should’ve told you about the buses!"
    Addie "Aww now you’re getting all red."
    Addie "Don’t worry, everyone has to do that at least once, or you’re not getting the full Slaycademy experience!"
    mc "Ha, so I was told."
    Addie "So how are you settling in?"
    mc "Good! I came with my roommate, she’s really nice."
    Addie "That’s great!"
    mc "Although I don’t know where she went off to…"
    mc "...Addie?"
    Addie "Oh sorry! I was just thinking this lighting is so good. With the sunset and the pink clouds…"
    mc "Yeah you’re right, it is beautiful."
    Addie "Would you mind taking a picture of me? Pretty please?"
    mc "Oh of course!"
    Addie "Period, thanks girlie!"
    mc "(Wow, when it comes to posing, she’s a pro.)"
    mc "(Well I shouldn’t be surprised.)"
    Addie "Ugh, these came out so great, you know the best angles!"
    Addie "Do you want a picture? You should show off that fit!"
    menu:
        "Oh, no that's ok!":
            jump addieSelfie1

        "Yeah, sure!":
            jump addieSure
label addieSelfie1:
    Addie "Aww ok. Well how about a selfie together?"
    mc "Well… I guess I can do that."

    jump addieSelfie2

label addieSure:
    Addie "Yes! Ok here, stand this way."
    mc "What do I do?"
    Addie "Just turn your body a little to the side, put your hand on your hip, yeah! Like that!"
    Addie "And tilt your head just a little bit," 
    Addie "Yes! Omg so cute!"
    Addie "Ok I took a bunch. Look, you ate that UP!"
    mc "Aww haha thanks!"
    mc "I’m not the best at posing, I usually leave that to the models.I’m not the best at posing, I usually leave that to the models."
    Addie "Oh the coach never plays, huh?"
    mc "Yeah, something like that."
    Addie "Well don’t count yourself out, I think you could totally be a model!"
    mc "Aww, thanks Addie!"
    Addie "Of course babe! See you’re totally serving face in these pics. Hey, do you wanna take a selfie together!"
    mc "Sure!"

    jump addieSelfie2
    
label addieSelfie2:
    Addie "Yay! I knew you’d be down. Say cheese!"
    mc "(Oh, we’re kind of close… is it normal to put your arm around someone’s waist this soon?)"
    Addie "Oh slayyy these look so good! What do you think?"
    mc "Ha! I look like I’m about to sneeze!"
    Addie "What do you mean, you look cute! Here, I’ll send it to you. What’s your Winstagram?"
    mc "Oh, it’s Fashionista2468."
    Addie "Ok slay."
    Addie "Wait your Winsta is so cute, I love all your designs!"
    mc "Oh thanks!"
    Addie "This one is totally giving Betsey Johnson Fall 2005."
    mc "Yes, that’s what I was going for! You have a good eye!"
    Addie "Well you know, I am in fashion marketing, I know a thing or two haha."
    anon "Oh there you are Addie, we were looking for you."
    Addie "Oh! Ah–well, [povname] looks like I gotta run"
    Addie "But I’m so glad you made it [povname]! Sorry I have to leave you, but enjoy the movie! This one is one of my favorites!"
    Addie "See you around!"

    centered "{color=#ffffff}Thank You For Playing{/color}"
    return

###############################################################
############## Chapter 1: Movie Night - Riya ##################
###############################################################
label riyaMovie:
    "text Riya"

    centered "{color=#ffffff}Thank You For Playing{/color}"
    return

