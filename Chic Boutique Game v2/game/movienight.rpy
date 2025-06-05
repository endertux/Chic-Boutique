#define nadia sprite:
image nadia normal = "bsf normal.png"
image nadia speak = "bsf speak.png"
image nadia sad = "bsf sad.png"
image nadia worried = "bsf worried.png"

###############################################################
############## Chapter 1: Movie Night - Felix #################
###############################################################
label felixMovie:
    show movie bg
    show Player:
        xpos 0.01
        ypos 0.6
    with fade
    mc "(I really hope this outfit isn’t too cozy…)"
    mc "(Since it’s a movie night, something comfy is just fine, right?)"
    mc "(Though Nadia did say on the way that there would be upperclassmen here…)"
    mc "(Maybe I should’ve dressed a little more professionally to leave a good impression.)"
    mc "(Agh, especially if upperclassmen from the fashion department will be here!)"
    mc "(I still have time to go change if I sprint to my dorm–)"
    mc "Hey, Nadia I think I’m gonna head back really quick, but I’ll be back in a sec."

    show nadia sad
    with dissolve
    Nadia "Wait, wait why!"
    Nadia "Your outfit is so cutieful!"

    show nadia normal
    mc "Really? I’m not sure if it would leave a good impression on fashion students though…"

    #Felix
    anon "No, no. I agree with Nadia. Totally cutieful."
    mc "!"
    #Felix sprite appears
    hide nadia normal

    show artguy normal
    with dissolve
    mc "Felix…"

    show nadia speak:
        xalign 0.2
        yalign 0.5
    show artguy normal:
        xalign 0.8
        yalign 0.5
    hide Player

    Nadia "Seeeee! Everyone agrees. You’re the most cutieful cutest cutie pie here."
    Nadia "So stop worrying!"
    Nadia "I’m gonna go get us some popcorn while you and your friend talk, okay?"
    #Nadia sprite hide
    hide nadia speak
    hide artguy normal

    show Player:
        xpos 0.01
        ypos 0.6
    with fade
    mc "(What’s with the grin on her face…)"
    mc "(She totally just left me here alone with Felix…)"
    mc "(And in this outfit!)"
    show artguy speak
    with dissolve
    Felix "What are you looking so worried for?"

    show dim_bg
    menu:
        "Be open with him":
            jump felixOpen
        
        "Keep your concerns to yourself":
            jump felixConcerns

label felixOpen:
    hide dim_bg

    show artguy normal
    mc "Ah just…wondering if my outfit is too informal…"
    show artguy speak
    Felix "You’re better dressed than I am, that’s for sure."
    show artguy normal
    mc "..."
    show artguy speak
    Felix "Relax, you look cute."
    show artguy normal
    mc "I don’t want to leave a bad first impression on the upperclassmen is all…"
    show artguy speak
    Felix "Well, as an upperclassman,"
    Felix "I’m telling you that you look cute."

    jump felixMovie2

label felixConcerns:
    hide dim_bg

    show artguy normal
    mc "Ah, it’s nothing really."
    show artguy speak
    Felix "You sure?"
    show artguy normal
    mc "Mhm. Just a little nervous, that’s all."
    show artguy speak
    Felix "Huh…I won’t push it, but I want you to be able to tell me if something’s wrong."

    jump felixMovie2

label felixMovie2:
    show artguy normal
    mc "Thanks. I’m glad that I have someone that I can count on."
    show artguy speak
    Felix "Hey, you lean on me, I lean on you."
    Felix "That’s how I hope my friends can see me."
    show artguy normal
    mc "Will there ever really be a time where you can lean on me? You seem like you have everything figured out…"
    show artguy normal
    Felix "That’s-"
    show artguy normal

    hide artguy normal
    anon "[povname]!"
    #Nadia sprite show
    show nadia speak
    with dissolve
    Nadia "Turns out, we got here kindaaaa late. Movie’s about to start!"
    Nadia "The beanbags near the front look real comfy and I wanna snag them before someone else does."
    
    show dim_bg
    menu:
        "Sit with Felix":
            jump felixSit

        "Go with Nadia":
            jump nadiaGo

label felixSit:
    hide dim_bg
    show nadia normal
    mc "I think I wanted to catch up with Felix a little bit. Mind if I come sit a little later?"
    show nadia speak
    Nadia "Hey, more beanbag space for me! I’m not complaining!"
    Nadia "Have fun…alone together…"
    hide nadia normal
    with dissolve
    mc "There’s that grin again!"
    #Nadia sprite hide
    show artguy speak
    Felix "Should we sit near the back? It’s a quieter and a little less crowded."
    show artguy normal
    mc "Sure, but I’m starved."
    show artguy speak
    Felix "You can go grab seats and I’ll bring some snacks over."
    show black bg
    with fade
    #Scene change maybe cg of them sitting next to each other w popcorn idk
    hide black bg
    show movie bg
    show artguy normal
    with dissolve
    mc "Do you know what they’re showing?"
    show artguy speak
    Felix "I think it’s some comedy film? The coordinators wanted to keep the mood light."
    show artguy normal
    mc "Well, I guess we’re about to see."

    show black bg
    with fade
    jump credits


label nadiaGo:
    hide dim_bg

    mc "Ooh, I was eyeing those when I walked in too."
    hide nadia normal
    show artguy speak
    with fade
    Felix "We can catch up later. Go grab those seats with your friend. I think everyone wants dibs on ‘em."
    show artguy normal
    mc "It was nice to run into you again, Felix."
    hide artguy normal
    with dissolve

    show nadia speak
    Nadia "I think your friend wanted to talk to you a little longer. You should’ve gone with him! I wouldn’t mind having to mingle with new people."
    show nadia normal
    mc "No, no don’t worry about it. I’m sure that I’ll get another chance to chat with him."
    show nadia speak
    Nadia "Alrightie, if you say so."
    Nadia "C’mon, movie’s starting! I heard it’s one of those comedy heist kinda movies."

    show black bg
    with fade
    jump credits

###############################################################
############## Chapter 1: Movie Night - Addie #################
###############################################################
label addieMovie:
    show movie bg
    show Player:
        xpos 0.01
        ypos 0.6
    with fade

    show baddie happy
    with dissolve
    Addie "Omg [povname] you made it!!"
    show baddie big
    mc "Oh hey Addie!"
    show baddie happy
    Addie "So were you able to find the dorms ok?"
    show baddie big
    mc "Yeah! Well…"
    show baddie tease
    Addie "Well?"
    show baddie big
    mc "..."
    show baddie concerned
    Addie "Wait, you didn’t walk all the way there, did you?"
    show baddie big
    mc "Um, yeah."
    show baddie happy
    Addie "HAHAHA! I’m so sorry, I should’ve told you about the buses!"
    Addie "Aww now you’re getting all red."
    Addie "Don’t worry, everyone has to do that at least once, or you’re not getting the full Slaycademy experience!"
    show baddie big
    mc "Ha, so I was told."
    show baddie happy
    Addie "So how are you settling in?"
    show baddie big
    mc "Good! I came with my roommate, she’s really nice."
    show baddie happy
    Addie "That’s great!"
    show baddie happy
    mc "Although I don’t know where she went off to…"
    show baddie tease
    mc "...Addie?"
    show baddie happy
    Addie "Oh sorry! I was just thinking this lighting is so good. With the sunset and the pink clouds…"
    show baddie big
    mc "Yeah you’re right, it is beautiful."
    show baddie tease
    Addie "Would you mind taking a picture of me? Pretty please?"
    show baddie big
    mc "Oh of course!"
    show baddie happy
    Addie "Period, thanks girlie!"
    show black bg
    with fade

    hide black bg
    show movie bg
    with fade

    mc "(Wow, when it comes to posing, she’s a pro.)"
    mc "(Well I shouldn’t be surprised.)"
    show baddie happy
    with dissolve
    Addie "Ugh, these came out so great, you know the best angles!"
    Addie "Do you want a picture? You should show off that fit!"
    
    show dim_bg
    menu:
        "Oh, no that's ok!":
            jump addieSelfie1

        "Yeah, sure!":
            jump addieSure
label addieSelfie1:
    hide dim_bg

    Addie "Aww ok. Well how about a selfie together?"
    mc "Well… I guess I can do that."

    jump addieSelfie2

label addieSure:
    hide dim_bg

    Addie "Yes! Ok here, stand this way."
    show baddie big
    mc "What do I do?"
    show baddie happy
    Addie "Just turn your body a little to the side, put your hand on your hip, yeah! Like that!"
    Addie "And tilt your head just a little bit," 
    Addie "Yes! Omg so cute!"
    Addie "Ok I took a bunch. Look, you ate that UP!"
    show baddie big
    mc "Aww haha thanks!"
    mc "I’m not the best at posing, I usually leave that to the models.I’m not the best at posing, I usually leave that to the models."
    show baddie happy
    Addie "Oh the coach never plays, huh?"
    show baddie big
    mc "Yeah, something like that."
    show baddie big
    Addie "Well don’t count yourself out, I think you could totally be a model!"
    show baddie happy
    mc "Aww, thanks Addie!"
    show baddie big
    Addie "Of course babe! See you’re totally serving face in these pics. Hey, do you wanna take a selfie together!"
    show baddie happy
    mc "Sure!"
    show baddie big

    jump addieSelfie2
    
label addieSelfie2:
    hide dim_bg

    show baddie happy
    Addie "Yay! I knew you’d be down. Say cheese!"
    show baddie tease
    mc "(Oh, we’re kind of close… is it normal to put your arm around someone’s waist this soon?)"
    show baddie happy
    Addie "Oh slayyy these look so good! What do you think?"
    show baddie tease
    mc "Ha! I look like I’m about to sneeze!"
    show baddie happy
    Addie "What do you mean, you look cute! Here, I’ll send it to you. What’s your Winstagram?"
    show baddie big
    mc "Oh, it’s Fashionista2468."
    show baddie happy
    Addie "Ok slay."
    Addie "Wait your Winsta is so cute, I love all your designs!"
    show baddie big
    mc "Oh thanks!"
    show baddie happy
    Addie "This one is totally giving Betsey Johnson Fall 2005."
    show baddie big
    mc "Yes, that’s what I was going for! You have a good eye!"
    show baddie happy
    Addie "Well you know, I am in fashion marketing, I know a thing or two haha."
    hide baddie happy
    anon "Oh there you are Addie, we were looking for you."
    show baddie happy
    Addie "Oh! Ah–well, [povname] looks like I gotta run"
    Addie "But I’m so glad you made it [povname]! Sorry I have to leave you, but enjoy the movie! This one is one of my favorites!"
    Addie "See you around!"

    show black bg
    with fade
    jump credits

###############################################################
############## Chapter 1: Movie Night - Riya ##################
###############################################################

# If player NEVER met Riya
label riyaMovie_A:
    show movie bg
    show Player:
        xpos 0.01
        ypos 0.6
    with fade

    #riya looking away
    mc "(I love her style. The ‘70s punk-rock spikes and chains, a gratuitous amount of piercings—it’s classic Vivienne Westwood. She looks like she was ripped straight out of one of those old punk zines, like Maximum Rocknroll.)"
    mc "(I kind of want to ask her where she got her jewelry. Plus, there’s something about her…)"
    mc "(Her jet-black hair and the sound of her voice… She seems a little familiar. Maybe I met her at orientation?)"
    mc "(I should ask her.)"
    menu:
        "Hey, I love your jewelry. Where’d you get it?":
            anon "Oh, thank you. They’re mostly from Carnage in Bloom, they’re a popular punk jeweler. I love your style, I feel like you’d like some of their pieces."
            jump riya_isThatYou


        "Hey, have we met somewhere?":
            anon "Have we met? Not that I know of. Unless you’ve come to one of my shows? I’m the lead singer of—"
            jump riya_isThatYou

label riya_isThatYou:
    anon "Hey, wait a second. [povname], is that you!?"
    mc "(Maybe we do know each other…?)"
    Riya "What the hell are you doing here!? It’s me, Riya!"
    mc "Riya!? Oh my god, it’s been so long!"
    mc "(No wonder why she looked familiar! Riya and I were friends in middle school, and she always talked about wanting to start a band. She would practice guitar in front of me for hours, and god, she was so bad! It’s making me laugh just thinking about it.)"
    mc "(Riya goes in for a hug and squeezes me tight. When she pulls away and holds me by the shoulders, I feel like we’re back in middle school again.)"
    mc "I just got accepted into Slaycademy! I just met my roommate and she told me about this movie night. What are you doing here?"
    Riya "Figures you’d end up here, you always used to talk my ear off about fashion. I started last year, Music major. I started a band in high school, and now we play shows around here. You’ve gotta come see us sometime!"
    mc "Wow, that’s so cool. I’d love to!"

    jump riyaMovie_Join

    
    show black bg
    with fade
    jump credits

# if player DID pick music studio
label riyaMovie_B:
    show movie bg
    show Player:
        xpos 0.01
        ypos 0.6
    with fade

    mc "Hey, Riya!"
    Riya "Oh, hey, Ruffles."
    mc "(Ruffles? That’s kind of cute…)"
    Riya "Sorry, do you not like it anymore? I used to call you that in middle school, remember? Because of all the frilly, ruffly designs you’d sketch and show me in class."
    mc "(Oh, right. In homeroom, I’d subject Riya to reviewing all of my amateurish fashion sketches. She always liked the punk-inspired ones the most.)"
    mc "Oh yeah! Remember when our homeroom teacher caught us talking about them, and he pinned my sketchbook pages to the board for a whole month? He thought they were too cute not to show off…"
    Riya "They were really cute! I remember this mermaid skirt you designed with a criminal amount of belts and spikes. That was the craziest thing I’ve ever seen."
    mc "Wow, I totally forgot about that one! I did have some crazy ideas back then."

    jump riyaMovie_Join

label riyaMovie_Join:
    Riya "Hey, so, what are you doing this weekend? My favorite band is playing here on Saturday and my guitarist, James, just bailed on me ‘cause he has a date. I’ve got a free ticket if you’d like to come."
    menu:
        "Is it Velvet Panic? I wanted to go so bad!":
            Riya "No way, you listen to them too? You’re going to love seeing them live."

            jump riyaMovie_PickUp

        "I might be too busy. Some of my classes already assigned design homework…":
            Riya "Hey, no worries. You know, the concert might be a good inspiration for your designs. Velvet Panic’s style is pretty out there."
            mc "Maybe you’re right… I could use some inspiration."

            jump riyaMovie_PickUp

label riyaMovie_PickUp:
    Riya "Should I pick you up at 7 on Saturday then?"
    mc "Yeah, that sounds great!"
    Riya "Great, then it’s a date. Throw on something grimy and grunge, okay?"
    mc "(A date!? Wait, no, she probably doesn’t mean a date date. But maybe…?)"
    Riya "Oh, hey, my bandmates just got here. I need to update them on some gigs we’ve got next week. But I’ll see you on Saturday, yeah?"
    mc "Oh, sure! See you then, Riya."
    Riya "See you, Ruffles."


    show black bg
    with fade
    jump credits

label credits: 
    scene black with fade 
    show text "{color=#f5188a}Credits{/color}" at truecenter with dissolve
    pause 2

    show text "{color=#f5188a}{i}Producers{/i}{/color} {color=#ffffff}\n Ruby Hirsch\n Jennie Le\n Helwa Halloum{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}{i}Programming{/i}{/color} {color=#ffffff}\n Aidan Sterling\n Helwa Halloum\n Ruby Hirsch\n Jennie Le{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}{i}UX/UI{/i}{/color} {color=#ffffff}\n Jennie Le\n Ruby Hirsch{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}{i}Art{/i}{/color} {color=#ffffff}\n Stephanie Lipe\n Jennie Le\n Helwa Halloum\n Ruby Hirsch \nJasper Siem \nHalle Fouche \nAlona Rees-Ramirez{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}{i}Narrative Design{/i}{/color} {color=#ffffff}\n Stephanie Lipe\n Noel Kim\n Hailey Phipps{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}{i}Editor{/i}{/color} {color=#ffffff}\n Hailey Phipps{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}{i}Music{/i}{/color} {color=#ffffff}\n Ishan Gupta{/color}" at truecenter with dissolve
    pause 3

    show text "{color=#f5188a}Thank you for playing!{/color}" at truecenter with dissolve
    pause 3

    return

