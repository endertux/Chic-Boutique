###############################################################
######################### Text Sound ##########################
###############################################################

# code by Aquapaulo --> https://github.com/aquapaulo/renpy-typewriter-sounds

##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

#init python:
    #def type_sound(event, interact=True, **kwargs):
        #if not interact:
            #return

#if text's being written by character, spam typing sounds until the text ends
        #if event == "show":
            #renpy.sound.play(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v (from Aquapaulo)



        #elif event == "slow_done" or event == "end":
            #renpy.sound.stop()

###############################################################
######################### Dress Up ############################
###############################################################

# dress up mini game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia

#These variables correspond to the images saved in "images/Minigame". If the variable is 0, the corresponding clothes will have 0 in their filename and so on.
#I set the default to 0, but you can set it to whatever you want.
#We need these variables if you want to keep the outfit you chose for the rest of the game, or if you want to do a reveal at the end of the minigame.
default bottom = 0
default shoe = 0
default top = 0

define Ariadne = Character("[povname]")
define anon = Character("???")

define Felix = Character("Felix")
define Addie = Character("Addison")
define Kyle = Character("Kyle")

define ra = Character("RA")
define Nadia = Character("Nadia")


#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen Dana_Sprite:
    image "Dana_Imgs/Dana_Sprite.png":
        xpos 300
        ypos 0

# Tops Define
screen top0 zorder 2:
    image "Dana_Imgs/Dana_Top_1.png":
        xpos 300
        ypos 0

screen top1 zorder 2:
    image "Dana_Imgs/Dana_Top_2.png":
        xpos 300
        ypos 0

screen top2 zorder 2:
    image "Dana_Imgs/Dana_Top_3.png":
        xpos 300
        ypos 0

# Pants Define
screen bottom0 zorder 3:
    image "Dana_Imgs/Dana_Bottom_1.png":
        xpos 300
        ypos 0

screen bottom1 zorder 3:
    image "Dana_Imgs/Dana_Bottom_2.png":
        xpos 300
        ypos 0

screen bottom2 zorder 3:
    image "Dana_Imgs/Dana_Bottom_3.png":
        xpos 300
        ypos 0

# Shoes
screen shoe1 zorder 1:
    image "Dana_Imgs/Dana_Shoe_1.png":
        xpos 300
        ypos 0

screen shoe2 zorder 1:
    image "Dana_Imgs/Dana_Shoe_2.png":
        xpos 300
        ypos 0

screen shoe3 zorder 1:
    image "Dana_Imgs/Dana_Shoe_3.png":
        xpos 300
        ypos 0


#Dress up menu screen
#Start button
screen outfits:
    image "Minigame/bg.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.40) action [Show("outfits_ui"), Show("Dana_Sprite"), Show("top0"), Show("bottom0")]

#Minigame
screen outfits_ui:
    image "Minigame/bg.png"
    image "Minigame/ui_base.png" align(1.1, 1.0) size (1300, 1100) 

    imagebutton auto "Minigame/done_%s.png" align(0.70, 0.85) action Jump("instructions")

#Tops
    imagebutton auto "Dana_Imgs/Dana_Top_1_%s.png" align(0.50, 0.25) action [Show("top0"), Hide("top1"), Hide("top2"), SetVariable("top", 0)]
    imagebutton auto "Dana_Imgs/Dana_Top_2_%s.png" align(0.50, 0.45) action [Show("top1"), Hide("top0"), Hide("top2"), SetVariable("top", 1)]
    imagebutton auto "Dana_Imgs/Dana_Top_3_%s.png" align(0.50, 0.65) action [Show("top2"), Hide("top0"), Hide("top1"), SetVariable("top", 2)]

#Bottoms
    imagebutton auto "Dana_Imgs/Dana_Bottom_1_%s.png" align(0.69, 0.25) action [Show("bottom0"), Hide("bottom1"), Hide("bottom2"), SetVariable("bottom", 0)]
    imagebutton auto "Dana_Imgs/Dana_Bottom_2_%s.png" align(0.69, 0.45) action [Show("bottom1"), Hide("bottom0"), Hide("bottom2"), SetVariable("bottom", 1)]
    imagebutton auto "Dana_Imgs/Dana_Bottom_3_%s.png" align(0.69, 0.65) action [Show("bottom2"), Hide("bottom0"), Hide("bottom1"), SetVariable("bottom", 2)]

#Shoes
    imagebutton auto "Dana_Imgs/Dana_Shoe_1_%s.png" align(0.90, 0.25) action [Show("shoe1"), Hide("shoe2"), Hide("shoe3"),SetVariable("shoe", 0)]
    imagebutton auto "Dana_Imgs/Dana_Shoe_2_%s.png" align(0.90, 0.45) action [Show("shoe2"), Hide("shoe1"), Hide("shoe3"),SetVariable("shoe", 1)]
    imagebutton auto "Dana_Imgs/Dana_Shoe_3_%s.png" align(0.90, 0.70) action [Show("shoe3"), Hide("shoe1"), Hide("shoe2"),SetVariable("shoe", 2)]


#This image can be used for the rest of the game, or just as a final reveal.
layeredimage Player:
    always:
        "Dana_Imgs/Dana_Sprite.png"

    group top:
        attribute 0 default:
            Null()
    if top == 0:
        "Dana_Imgs/Dana_Top_1.png"
    if top == 1:
        "Dana_Imgs/Dana_Top_2.png"
    if top == 2:
        "Dana_Imgs/Dana_Top_3.png"

    group bottom:
        attribute 0 default:
            Null()
    if bottom == 0:
        "Dana_Imgs/Dana_Bottom_1.png"
    if bottom == 1:
        "Dana_Imgs/Dana_Bottom_2.png"
    if bottom == 2:
        "Dana_Imgs/Dana_Bottom_3.png"
    
    group shoe:
        attribute 0 default:
            Null()
    if shoe == 0: 
        "Dana_Imgs/Dana_Shoe_1.png"
    if shoe == 1: 
        "Dana_Imgs/Dana_Shoe_2.png"
    if shoe == 2: 
        "Dana_Imgs/Dana_Shoe_3.png"
        
###############################################################
#################### Gameplay: Prologue #######################
###############################################################
label start:
    #LETTER CG
    scene black bg
    with fade

    #[allow player to input their name]
    #[if player does not input a name; default name: Ariadne]

    # Ask player for their custom name
    $ povname = renpy.input("What is your name? After you are done, press enter!", default="Ariadne").strip()

    call screen outfits

label instructions:
    scene bg with dissolve

    hide screen outfits
    hide screen outfits_ui

    hide screen Dana_Sprite
    hide screen top0
    hide screen top1
    hide screen top2
    hide screen bottom0
    hide screen bottom1
    hide screen bottom2
    hide screen shoe1
    hide screen shoe2
    hide screen shoe3

    show Player:
        xpos 0.38
        ypos 0

    "slay"

    # Ensure the first letter is capitalized
    $ povname = povname.capitalize()

    scene congratsnew
    with dissolve
    #"Congratulations, [povname]!"

    "After reviewing your application, we have decided to offer you admission to Slaycademy Institute of the Arts for the upcoming school year."

    "We believe that your application is a reflection of your effort and dedication to creative endeavors."

    "We believe that you can truly excel at Slaycademy and achieve greatness. Welcome to Slaycademy."

    show Player:
        xpos 0.01
        ypos 0.6
    "I made it? All my hard work was worth it!"

    "All of the people I’ll meet and the opportunities I’ll come across…"

    "I have to make the most of this."

    "I will make the most of this."

    hide Player

    #BLACK SCREEN WITH WHITE TEXT ACROSS
    scene black bg
    with fade

    "A summer passes and the Fall season begins…"

    #BLACK SCREEN WITH WHITE TEXT ACROSS 

    "A new adventure begins…"

    #CG OF SLAYCADEMY ENTraNCE 
    #IF POSSIBLE, do a pan up reveal
    scene school
    with fade

    show Player:
        xpos 0.01
        ypos 0.6
    
    #play music
    play music "podcast-smooth-jazz-instrumental-music-225674.mp3" volume 0.5
    # https://pixabay.com/music/smooth-jazz-podcast-smooth-jazz-instrumental-music-225674/

    "This doesn’t feel real…"

    "One of the most prestigious art schools in the world and I’m here"

    "Not as a visitor but as a real student."

    #INSERT OF SCHOOL MAP 
    #map should look confusing and unclear

    "Orientation materials are never any help when you can’t read maps!" 
    #😞

    "And an online orientation? At least include a tour!"

    "If I had to figure this out right before classes I’d be totally screwed"

    "…"

    "…"

    "Hah…"

    #FADE INSERT AWAY
    scene black bg
    with dissolve
    show Player:
        xpos 0.01
        ypos 0.6

    "WHY AM I SO NERVOUS"

    "One foot in front of the other…"

    #FADE INSERT AWAY
    #scene 
    #with dissolve
    #show Player:
    #    xpos 0.01
    #    ypos 0.6

    "I have to at least go into the school if I want to attend…"

    #"…Which way first?"

    #COMMON ROUTE CHOICE 1: [museum] [garden] [field]
    menu:
        "…Which way first?"

        "Museum":
            jump museum
        "Garden":
            jump garden
        "Field":
            jump field


label museum:
    #BG ART OF SCHOOL MUSEUM
    scene museum
    with fade
    show Player:
        xpos 0.01
        ypos 0.6

    "Where am I!" 
    #🥲

    "I’m totally lost but…"

    "This place is beautiful so I’m not complaining!"

    "I can’t believe that a school has a building like this"

    "As expected from a top university…"

    #INSERT OF AN ART PIECE 
    #im referencing this one you can just take the pic and put a pixel filter over bc its public domain now (refer to google doc)
    #"Virgin and Child with Canon van der Paele" Painting by Jan van Eyck
    show madone painting
    with fade

    "The colors on this are so vibrant!"

    #(Felix)
    anon "It’s amazing, right?"

    "!"

    hide madone painting
    #FELIX SPRITE
    show artguy normal
    with dissolve

    #(Felix)
    anon "Sorry! I didn’t mean to startle you."

    #(Felix)
    anon "It’s just that I noticed you seemed lost in thought looking at this piece."

    scene museum
    hide artguy normal
    hide Player
    show madone painting
    with fade

    show artguy normal:
        xpos -0.04
        ypos 0.6

    #(Felix)
    anon "I feel the same way every time I see it."
    hide artguy

    show Player:
        xpos 0.01
        ypos 0.6

    Ariadne "The colors are so bright…I feel like I’m getting sucked into the painting just by looking at it."
    hide Player

    show artguy normal:
        xpos -0.04
        ypos 0.6

    #(Felix)
    anon "I get what you mean! The artist actually spent months meticulously making his own paints."

    #(Felix)
    anon "Back then, oil paints were made with eggs rather than oil, but then this guy came along and had the idea of using oil. So simple yet effective…"

    hide madone painting
    hide art guy normal
    scene museum
    with fade

    scene museum

    show Player:
        xpos 0.01
        ypos 0.6
    Ariadne "You seem to know a lot about this painting! I just thought it looked cool."
    #😅
    
    show artguy normal

    #(Felix)
    anon "Ah, I’m a fine arts major. I’m working on a project focusing on just the pieces we have at our campus museum."

    Ariadne "The fabric looks so real that I can tell exactly what they are. I can practically feel the soft velvety texture in my hands…"

    #(Felix)
    anon "It’s so intentional too! He built up thin layers of paint to make it more vibrant and textured. This artist is actually credited for coming up with the technique."

    #FADE INSERT AWAY

    #(Felix)
    anon "From your fabric comment, I’m guessing you’re here for fashion?"

    Ariadne "Haha, so obvious right? I’m [povname]. It’s my first day on campus."

    Felix "Felix. Fashion’s not an easy department to get into. You must be really good."

    Ariadne "I wouldn’t say all that. It’s just hard work."

    Felix "I don’t usually see fashion majors in this building. Thinking of switching majors?" 
    #this is just said playfully hes not actually asking so maybe put a playful expression

    Ariadne "More like just totally, utterly lost."

    Felix "I gotta say, the campus is nice but navigating it…not as great. Where are you headed? Maybe I can point you in the right direction."

    Ariadne "I guess freshman dorms? I should check in before exploring around a bit more."

    Felix "No wonder why you were so lost! The dorms are always impossible to get to."

    Felix "Bad news is…it’s about a 25 minute walk."

    Ariadne "25 minutes?!"

    Felix "But wait! The good news is that I can walk you there."

    Ariadne "Are you sure? 25 minutes is a long ways away…"

    Felix "It’s no problem. Research can wait."

    Ariadne "If you’re researching right now, you should focus!"

    Ariadne "Plus if you walked me there I have a feeling I’d tune out my surroundings and never get the hang of the campus layout. I’ll be fine on my own, just point me in the right direction."

    Felix "Alright, alright just don’t get too lost and end up back in front of this painting again."

    #INSERT OF SCHOOL MAP
    #map should look confusing and unclear still

    Felix "There’s a clear path riiiight here. Here, I’ll highlight it for you so you can’t miss it."

    #INSERT OF SCHOOL MAP
    #map should now have a highlighted path on it
    scene black bg
    with fade
    #FADE SCENE TO OUTSIDE ON PATH
    jump path


label garden:
    #BG ART OF SCHOOL GARDEN
    scene background

    show Player:
        xpos 0.01
        ypos 0.6

    "Ah! I’ve seen this place on the school website before!"

    "And now I’m really here in real life!"

    "Seems like a nice place to study…maybe I should mark it on the map for later."

    "…"

    "Where did my map go…"
    #😞

    #(Addie)
    anon "Hey, cutie!"

    "?"

    #ADDIE SPRITE
    #should be kind of far away on the screen

    "Is she talking to me?"

    anon "Yes, you! Cutie with the dark hair! You dropped your map!"
    #erm i need mc description here…i'll add after u guys make the design

    Ariadne "Oh!"

    #RUNNING SOUND EFFECT
    #ADDIE SPRITE APPEARS CLOSER
    show baddie normal
    with dissolve

    Ariadne "Thank you so much! I didn’t even notice that I had dropped it."
    #😞

    #(Addie)
    anon "No probs."

    #(Addie)
    anon "You a freshman?"

    Ariadne "Did the map give it away?"

    #(Addie)
    anon "The lost look in your eyes did. This school is huge…we’ve all been there."

    #(Addie)
    anon "Where you heading, kid?"
    #addie is a second year 😭 kinda wanna make it a running joke that she always calls mc kid despite only being a year older than her; she just wanna give unnie vibes


    Ariadne "If I can figure this map out, the student dorms."

    #(Addie)
    anon "Ooh! I lived there last year! I don’t have anything going on right now if you want me to take you there?"

    Ariadne "Is it far? I don’t want to trouble you too much…"

    #(Addie)
    anon "No, no it’s fine. You’ve already caught my attention so I wanna get to know you."

    scene black bg
    with fade

    #WALKING SOUND EFFECT THROUGHOUT SCENE
    #since they’re outside make it sound like they’re on a track; sound shouldn’t be too loud so it doesn’t distract from dialogue

    show baddie normal
    #(Addie)
    anon "So, what’s your name?"

    show Player:
        xpos 0.01
        ypos 0.6

    Ariadne "[povname]. You’re…?"

    #(Addie)
    Addie "Addie. It’s easy to remember because it rhymes with baddie!"
    #😉

    Ariadne "It’s nice to meet someone so friendly right away. I was really concerned about making friends here to be honest…"

    Addie "With a face like that? C’mon you’ll have no problem making friends."

    "Her gaze is making me a little nervous…it’s like I’m being studied"
    #😓

    Addie "So, what are you here for? Architecture? Film?"

    "Ah-"

    "I should’ve dressed a little nicer…"

    Ariadne "I’m a fashion major. I usually dress up a little more than this…I didn’t expect to meet anyone until the first day of classes…"

    Addie "Hey, the sweats are a good indicator too! I can never get mine to look that stylish."

    Ariadne "The trick is to look at the seam on the side here. And the cuffs on the bottom are a minor change but they make a big difference!"

    Addie "You totally need to give me more tips. I wanna up my wardrobe game this year."

    Ariadne "Really? …Your outfit already looks great though?"

    Addie "Thanks, cutie. But what you don’t see is that I literally wear this outfit alllll the time. I gotta change things up."

    scene building

    #WALKING SOUND EFFECT STOPS

    #ADDIE SPRITE DROPS TO HER KNEES
    show building with vpunch

    show Player:
        xpos 0.01
        ypos 0.6

    "?!"

    Ariadne "Are you okay?!"

    #Maybe we could have a music change here? Something comedic sounding

    show baddie normal

    Addie "Pleaseee tell me you’ll help me out! Be my little fashionista!"

    Ariadne "Ahh- please stand up!"

    Addie "Say yes!"

    Addie "Please please please please please please please pl-" 
    #number 1 flirting technique she’s such a pro….

    Ariadne "Yes, yes I’ll help you!"

    Ariadne "Please stand up. You’ll get dirt all over your clothes…"

    #ADDIE SPRITE BACK TO NORMAL
    #WALKING SOUND EFFECT STARTS AGAIN

    Addie "Phew! I thought I was gonna have to start crying."

    "This girl is kind of…"
    #😅

    Ariadne "You didn’t need to beg y’know. I was hoping to find a model for my projects anyways."

    Addie "Me, me! I volunteer! Plus I’m in fashion marketing and merchandising so we’ll be in the same buildings all the time."

    Addie "It’s like a match made in heaven! You can teach me the rules of fashion and I can be your muse."

    Ariadne "Muse? I didn’t say all th-"

    #(Student)
    anon "Addison!"

    Addie "Shoot!" 
    #😨

    #(Student)
    anon "You told me you’d meet me at the quad 20 minutes ago!"

    Addie "Sorry, cutie! I gotta run."

    Addie "Luckily it’s super easy to get to the dorms from here. Just follow this path to the end, ‘kay?"

    Ariadne "Thanks! I’ll see you around then."

    Addie "See ya!"

    #RUNNING SOUND
    #ADDIE SPRITE GONE

    "I thought she said she had nothing to do…?"

    #FADE SCENE TO OUTSIDE ON PATH
    scene black bg
    with fade

    jump path

label field:
    #BG ART OF SCHOOL FOOTBALL FIELD
    scene field
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    "Well, this is a place I probably won’t be seeing much of…"

    "I didn’t even think that an art school would need a place like this."

    "Maybe that’s just the kind of crazy budget that they h-"

    Ariadne "AHH-"

    #SHAKE SCREEN EFFECT
    #CraSH NOISE
    show field with hpunch

    Ariadne "Ow…"

    #maybe put some sort of screen movement here to indicate that she stood back up after falling

    #KYLE SPRITE

    show gymbro normal

    #(Kyle)
    anon "You’re blocking the field, bro!!!!!"

    "No apology?"

    Ariadne "If you saw me then you didn’t have to barrel right into me!"

    #(Kyle)
    anon "Yah, you’re right, dude. My bad!"

    "What’s with this guy!"

    #(Kyle)
    anon "So, you here to play?"

    Ariadne "Huh?"

    Ariadne "Oh! No, no I was just wandering around and got a little lost."

    #(Kyle)
    anon "That’s a shame, man. We could really use more students in the sports department."

    Ariadne "Are you a sports major?"

    #(Kyle)
    anon "Yeah, bro. Can’t you tell I lift??"

    Ariadne "I just didn’t know that Slaycademy had a sports department."

    anon "Haha, they don’t!"

    Ariadne "What? Then how are you-"


    #(Kyle)
    anon "Look, man. Rome wasn’t built in a day, alright?"

    #(Kyle)
    anon "You know what they say!"

    "No…I don’t…"

    "Please! Someone…anyone! Get me out of this conversation!!"

    "Ah…we’re the only ones on the field…"
    #😔

    #(Kyle)
    anon "Anyways, I’m gonna be attempting a 350 squat today. It’ll be hard but I think with an audience I’ll be hyped enough to do it."

    #(Kyle)
    anon "Maybe I should practice right now! Tell me how my form is, here-"

    Ariadne "Actually, I really gotta get going."

    #(Kyle)
    anon "Aw man, that’s a shame! We were really vibing!"

    "Were we?"

    Ariadne "Would you mind pointing me in the direction of the freshman dorms?"


    "Please respond normally!"

    #(Kyle)
    anon "Down near the tennis courts over there, follow the dirt path."

    "Oh, thank god…"

    #(Kyle)
    anon "Haha, that reminds me of a movie I watched. Follow the yellow brick road!"

    #(Kyle)
    anon "The movie’s super underground. Sorry for the obscure reference!"

    "..."

    Ariadne "Yeah…thanks for the directions."

    #(Kyle)
    anon "No prob, bro. Gotta get back to running my laps. Good luck finding the cafeteria or wherever you wanted to go!"

    hide gymbro
    with dissolve

    Ariadne "Did this guy really give me the right directions??"

    scene black bg
    with fade

    jump path

label path:
    #FADE TO SCENE OUTSIDE ON PATH

    #atp all choice options should have converged into the same main story where player is on the path outside

    #BG ART OF PATH
    scene building
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    "It’s great that I was able to get directions from someone. I don’t think I would’ve made it here on my own."
    #😓

    "But this path looks like it goes on forever…"

    "Hah…"

    "They better tell me about a campus shuttle or something later."

    #FADE BLACK SCREEN WITH WHITE TEXT ACROSS

    scene black bg
    with fade

    "A while later…"

    #FADE BRIGHT WHITE SCREEN
    #think it would be funny here to make it a scene where shes like i didnt think i would make it 😭 and the bright light is literally like her being like i see the light

    show white bg
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    Ariadne "Did-"

    Ariadne "Did I really make it?"

    "Who had the bright idea of building this school on a bunch of hills?!"
    #tbh this is straight out of my experience at korea university bc korea is super mountainous but its like they did no landscaping at all they just plopped the school right on the hills…walked to the dorms ONCE and was so winded and with my iron deficiency i was seeing stars

    "I need to sit down…"

    #BG ART OF DORMS FRONT DESK
    show building
    with dissolve

    show Player:
        xpos 0.01
        ypos 0.6

    Ariadne "Hah…"
    #😓

    #SOUND AND SCREEN EFFECT TO INDICATE THAT PLAYER IS NOW SITTING

    "Big ass school and no way to get up here besides that dirt path-"

    "Judging by how long that took me, I’ll need to wake up before classes like an hour early-"
    "If I want my outfit to be even a little decent, it’ll need to be earlier"

    "Should I drop out?"

    "Should I do it?"

    ra "Um…"

    "?"

    #ra SPRITE
    show ra normal
    with dissolve

    ra "Are you a student here?"

    show Player:
        xpos 0.01
        ypos 0.6

    Ariadne "Ah-yes! I’m sorry, I should’ve checked in before using the lounge!"

    ra "Please, feel free to have a seat! I’ll get you checked in. New students usually get winded after that hike."

    ra "But don’t worry, it gets easier!"

    Ariadne "I hope so…"

    "I really don’t think that’s something that I can do every day!"

    ra "Could you give me your name and ID number for check in?"

    Ariadne "Yes, it’s [povname] and my ID number is 14399333."

    ra "Wonderful! You’re all checked in."

    #INSERT OF ACCESS CARD

    ra "This will give you access to the dorm building and all amenities. The number in the corner is the PIN for your room’s lock."

    #FADE INSERT AWAY

    ra "You’ll be on the second floor in room 143. Your roommate checked in early this morning, so she should be here already."

    Ariadne "Thank you!"

    ra "Oh! And the elevator is in maintenance this week. The stairs are right next to it."

    Ariadne "Thanks…"
    #😭

    #BG ART OF DORM HALL
    scene dorm hallway
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    "Clearly the school budget didn’t make it to the housing department."

    "Hopefully the room will be better-"

    Ariadne "Ah!"

    #(Nadia)
    anon "AH-"
    show dorm hallway with hpunch

    #CraSH EFFECT

    scene zoe cg

    #CG NADIA ON FLOOR

    #(Nadia)
    anon "Ow ow ow ow ow"

    Ariadne "Are you alright?!"

    #(Nadia)
    anon "Oh my god! I’m so sorry! I totally wasn’t looking where I was going…"


    Ariadne "Don’t worry about it! Are you hurt? Do you need help getting up?"

    #(Nadia)
    anon "No, I’m good, I’m good."

    scene dorm hallway
    with fade

    show bsf normal

    #(Nadia)
    anon "I lost a piece of jewelry that’s important to me earlier and the ra just called and told me that someone turned it in."

    #(Nadia)
    anon "I guess thinking about it now…it’s not like it was gonna go anywhere."

    #(Nadia)
    anon "But I was so desperate to get it back!"

    show Player:
        xpos 0.01
        ypos 0.6

    Ariadne "I’m guessing you’re a resident of this dorm?"

    Nadia "Yup! Name’s Nadia."

    Ariadne "[povname]. You should probably go get that jewelry. Seems like it means a lot to you."

    Nadia "Ah! The jewelry! I almost forgot…"

    "..."

    Nadia "I’m sure we’ll see each other around a lot. Let’s hang out sometime!"

    Ariadne "Sounds good! It’ll be nice to have a friend in the dorms."

    Nadia "Oh, for sure. I gotta run but maybe I’ll see you at movie night!"

    hide bsf normal
    with dissolve

    Ariadne "Movie n-"

    "She left…"

    "Well, I’m bound to see her again sometime soon."

    #BG ART DORM ROOM
    scene room
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    "!"

    "So many boxes…"

    "Thankfully the dorm seems a lot nicer than the halls."

    "It’s so much bigger than I thought it would be! Let’s see…"

    "I could set up a mannequin here…sewing machine in this corner…"

    #DOOR BEEPING SOUND EFFECT

    "?"

    #NADIA SPRITE
    show bsf normal

    Nadia "You’re…"

    Ariadne "From earlier…"

    Nadia "HAHAHAHAHA"

    Nadia "Did we really end up as roommates!"

    Ariadne "What are the chances!"

    Nadia "Well it’s a good thing we got introductions out of the way."

    Ariadne "Yup, we’re practically old friends!"

    Nadia "..."

    Nadia "..."

    Ariadne "Nadia…?"

    #DOOM SOUND EFFECT
    Nadia "I MADE SUCH A BAD FIRST IMPRESSION."

    Ariadne "Oh, come on stop worrying about that. You’re the one who ended up on the floor!"

    Ariadne "Ah, but I was curious about what you meant by movie night."

    Nadia "No one told you about movie night?"

    Ariadne "Haven’t heard of it."

    Nadia "Oh, it’s just a little social event they’re holding for new students in the lounge tomorrow."

    Nadia "They’re having upperclassmen come in too so that we can meet people who have a bit more experience than us."

    Nadia "You have to come! It’ll be fun and you’ll make a ton of friends."

    Ariadne "I wish I knew about this earlier! I would’ve planned an outfit but now I gotta unpack first."

    Nadia "There are wayyyy too many boxes. How much clothes do you have?"

    Ariadne "A lot…the thrifting addiction is real…"

    Nadia "I get it. I had to leave tonsils of boxes at my parent’s."

    Nadia "Hmm…well you don’t really wanna unpack now, do you?"

    Ariadne "No, but what choice do I have?"
    #😭

    jump dress
    with fade