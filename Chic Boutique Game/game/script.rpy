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
default socks = 0
default top = 0

define e = Character("Player")
define x = Character("???")

define a = Character("ART GUY")
define b = Character("BADDIE")
define g = Character("GYM BRO")

define ra = Character("RA")
define bsf = Character("BSF")


#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen Dana_Sprite:
    image "Dana_Imgs/Dana_Sprite.png":
        xpos 300
        ypos 0

screen top0 zorder 2:
    image "Dana_Imgs/Dana_Top_1.png":
        xpos 300
        ypos 0

screen top1 zorder 2:
    image "Dana_Imgs/Dana_Top_2.png":
        xpos 300
        ypos 0

screen bottom0 zorder 1:
    image "Dana_Imgs/Dana_Bottom_1.png":
        xpos 300
        ypos 0

screen bottom1 zorder 1:
    image "Dana_Imgs/Dana_Bottom_2.png":
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
    image "Minigame/ui_base.png" align(1.0, 0.0)

    imagebutton auto "Minigame/done_%s.png" align(0.80, 0.75) action Jump("instructions")

#Tops
    imagebutton auto "Dana_Imgs/Dana_Top_1_%s.png" align(0.655, 0.25) action [Show("top0"), Hide("top1"), SetVariable("top", 0)]
    imagebutton auto "Dana_Imgs/Dana_Top_2_%s.png" align(0.655, 0.45) action [Show("top1"), Hide("top0"), SetVariable("top", 1)]

#Bottoms
    imagebutton auto "Dana_Imgs/Dana_Bottom_1_%s.png" align(0.755, 0.25) action [Show("bottom0"), Hide("bottom1"),SetVariable("bottom", 0)]
    imagebutton auto "Dana_Imgs/Dana_Bottom_2_%s.png" align(0.755, 0.45) action [Show("bottom1"), Hide("bottom0"), SetVariable("bottom", 1)]


#This image can be used for the rest of the game, or just as a final reveal.
layeredimage Dana_N:
    always:
        "Dana_Imgs/Dana_Sprite.png"

    group top:
        attribute 0 default:
            "Dana_Imgs/Dana_Top_1.png"
    if top == 1:
        "Dana_Imgs/Dana_Top_2.png"

    group bottom:
        attribute 0 default:
            "Dana_Imgs/Dana_Bottom_1.png"
    if bottom == 1:
        "Dana_Imgs/Dana_Bottom_2.png"

###############################################################
######################### Gameplay ############################
###############################################################
label start:

    # display lines of dialogue.

    scene accept letter
    with fade

    ### PROLOGUE ###

    #Letter (on screen, not text box):
    #[animation, you got mail!]
    "Testing gege lol !!Congratulations! On behalf of the staff here at Slaycademy Institute of the Arts, we are pleased to inform you of your acceptance into the Fashion major."
    #*CG of a desk with a ripped envelope.

    "Your application stood out amongst the thousands that our committee considered, and we expect to see great things from you."
    
    #scene bg room
    with fade
    
    "This journey is sure to be full of great opportunities for you, but first, let’s customize your character."

    "The fashion scene at Slaycademy is unparalleled, so get ready to unleash your inner fashionista and create a character as stylish as you are!"
    #*MC is in her room wearing pajamas, clicks on the closet to get dressed

    #[The camera pans over the character creation menu, showcasing the options available.]

    jump dress

label dress:
    scene bg
    "Now you can customize every aspect of your character’s appearance."

    "Experiment with an array of hairstyles, eye colors, facial features, and so much more. Mix and match until you find the perfect combinations that reflect you and your style."
    #[As players make their selections, the avatar on the screen transforms accordingly, showcasing the chosen features.]

    call screen outfits

    label instructions:
        scene bg with dissolve

        hide screen outfits
        hide screen outfits_ui

        hide screen Dana_Sprite

        hide screen top0
        hide screen top1

        hide screen bottom0
        hide screen bottom1

        show Dana_N:
            xpos 0.38
            ypos 0
        
        "Once you’re satisfied with your creation, it’s time to step onto the runway and show the world your style!"

        jump story

label story:
    scene slaycad bg
    with fade
    #After character customization: 
    #*Insert CG of the giant school facade with chill music
    #[MC looks distressed/ in awe of the size of the school.]

    #play music
    play music "podcast-smooth-jazz-instrumental-music-225674.mp3" volume 0.5
        # https://pixabay.com/music/smooth-jazz-podcast-smooth-jazz-instrumental-music-225674/

    #Main Entrance

    "Slaycademy, one of the world’s most prestigious art schools dedicated to excellency. Only the best and brightest young artists and designers are chosen to attend."

    "Here, your talents will be nurtured by the expert staff and endless amenities available to you."

    "Every year, Slaycademy hosts its own special showcase honoring designs by the best students. Be prepared to work hard, and you will be rewarded."

    "Do you have what it takes to succeed? Good luck!"

    scene courtyard bg
    with fade

    e "Oh my gosh, this school is so big! How am I ever going to get around this place?"

    e "They gave me this map, but it doesn’t make much sense…"

    #*screen opens to a CG of a large map with random shapes*
    menu:
        e "Maybe I should go ask someone for directions, but where do I go?"
        
        "Forward":
            jump art

        "Left":
            jump baddie

        "Right":
            jump gymBro

label art:
    scene art build bg
    with fade

    #show ARTGUY netural
    e "(I walk to what seems to be a spread-out building with painted murals all around me.)"
    
    "As MC wanders the area, they bump into someone by accident."

    e "Oh gosh! I'm so sorry, are you alright?"

    show artguy normal
    with dissolve

    a "Oh don’t worry about it, I'm alright! Are you looking for something?"

    e "Actually, yeah… I’m a little lost. The map they gave me is so confusing!"

    a "Yeah I remember going through that when I first came here, where are you trying to go?"

    e "I’m looking for the dorms."

    a "Oh you're not far off! The dorms are actually right over here."

    "he points to where the dorms are on the map."

    e "Umm… That would actually be helpful if I knew where we are right now."

    a "*chuckles* I can just take you there…"
    
    a "I know you’re going to hear this a hundred times.. But what's your major?"

    e "Actually, you're the first to ask, I'm a Fashion major."

    a "Wow! That’s so awesome, I heard that one is really hard to get into."
    
    a "I’m in Fine Arts."

    e "Oh that sounds cool! Do you enjoy studying fine arts?"
    
    a "It changes the way I see everything; the colors of the sky, the shapes of the buildings, the expression of the people around me… It’s a beautiful thing."

    e "..."

    a "*laughs* But seriously, I really love what I do."

    "ART GUY starts walking to the dorms. *Later they arrive."

    scene dorms outside bg
    with fade

    show artguy normal
    with dissolve

    a "Oh, looks like we’re here."

    e "Thank you so much!"

    a "Of course! Good luck on your first week!"
    
    jump dorms01

label baddie:
    scene tinted bg
    with fade

    e "(I walk to what seems to be a large building with big tinted windows…)"

    e "(There are large mahogany doors with columns on either side.)"

    show baddie normal
    with dissolve

    b "Hi babe, are you looking for classes too?"

    e "I’m looking for the dorms, but I’m having trouble finding it on this map…"

    b "Oh! Let me see…"

    "Baddie’s manicured hand points the way as her smile remains warm yet slightly teasing."

    b "Ah you’re almost there, Just head down that path over there and take a right at the next building."

    e "Oh thank you! It was right there all along."
    
    b "Of course babes! This campus is like a maze. Let me know if you need anything else."

    "As the MC is about to leave, BADDIE stops them."

    b "Also I really like your outfit, you look so good!"

    e "Oh my gosh thank you!"

    b "Yeah of course, hope you find the dorms ok!"

    jump dorms01

label gymBro:
    scene gym bg
    with fade

    e "(I walk to what seems to be a small building near a large field…)"

    x "(Outfit piece) at the gym, that’s an interesting choice."

    e "What? Oh! I'm not here for the gym. I’m actually looking for the dorms"

    show gymbro normal
    with dissolve

    g "Lol, You’re in the opposite direction, have you tried looking around?"
    # *Gym sprite is smirking/snickering*

    e "Wha-?"

    g "Hahah….I’m just messing with you, the dorms are over there to your left."

    e "Thanks…"

    scene dorms outside bg
    with fade

    e "(What is with that guy? He just got on my nerves! But I guess I'm here.)"

    jump dorms01
    

label dorms01:
    scene office bg
    with fade

    "MC arrives and walks into the lobby."

    show ra normal
    with dissolve
    
    "The RA is at the counter, reading, and looks up from her book."

    menu:
        ra "Hello! How can I help you?"

        "give a polite response":
            jump raInteraction01

        "give a bitter response":
            jump raInteraction02

label raInteraction01:
    e "Hi! I'm new here and I’m looking for my room."

    ra "Alright! I’m *RA by the way, I'm going to be your RA for this year."

    ra "So first things first, what is your name?"

    "*Insert game prompt to enter their name"

    ra "Alright, MC… MC… Oh MC! Here you are!"

    ra "These are your room keys, and your dorm number is 407."

    e "Ok, thank you so much!"

    "MC begins to walk away"

    ra "Wait, I forgot to mention. There's going to be a *insert event name*."
        
    ra "It’s part of our Welcome Week activities for freshmen. Don’t miss out!"

    e "Ooh sounds fun! I'll look into it, thanks!"

    "She turned to walk away again."

    ra "Umm… the elevator is just to your right *MC."

    e "Ahaha… right, got it!"

    ra "Of course! And don’t hesitate to reach out if you have any questions!"

    ra "Or if you encounter any problems during your time here, just come talk to me."

    jump dorms02



label raInteraction02:
    e "Uh.. yeah. Can’t you see I’m new here?"

    ra "I can definitely see that.."

    ra "I’m an RA for this building, I’m checking people in."

    ra "Can I get your name?"

    "*Insert game prompt to enter their name"

    e "MC."

    ra "Oh! Wow, it looks like I'm your RA."
    
    ra "I’m *RA. Here’s your key and your dorm number is 407."

    ra "I’m sure I’ll see you around."

    ra "And, the elevator is to your right."

    ra "Try not to miss it."

    e "(Wow, she seems assertive.)"

    jump dorms02

label dorms02:
    scene dorm hallway bg
    with fade

    "MC walks to the elevator and enters the fourth floor."

    "The elevator opens up to a long hallway with adjacent hallways veering off to places unseen."

    "Tall mahogany doors are widely spread out on each side, with each door having an ornate plaque carrying the room numbers."

    e "Alright, lets see...403…404…"

    "MC is then interrupted by a loud thud, almost sounding like multiple heavy objects were dropped."

    "MC walks to the sound, from around the corner and sees someone sitting on the floor."

    "*Insert CG of BSF character on the ground with multiple large luggages around her."

    x "Aww geez, maybe I brought a little too much stuff with me…"

    "MC approaches the student sitting on the floor."

    e "Are you ok? Do you need some help?"

    show bsf normal
    with dissolve

    x "Uh yeah, that would actually be great!"

    "MC begins helping her pick up her stuff."

    e "Is it your first year too?"

    x "Yeah! I’m so excited, I’ve always wanted to go here. This school is so pretty, don’t you think?"

    e "Yeah totally!"

    "They both finished picking up the clumsy students luggage."

    "As MC gets up, they noticed the room number on the door."

    e "This is room 407!"

    x "Oh, yeah. Wait, are you in this room too?"

    e "Yes!"

    bsf "Oh my gosh! You’re my roommate! My name is *BSF!"

    e "I’m *MC."

    scene fade
    scene mc dorm empty bg

    "The room is spacious, with two four-poster beds and desks at the far end, and a couch with a tv in the center."

    "There are two huge floor-to-to ceiling windows between the beds. As they walk inside, there is a small kitchen with a stove, oven, and fridge, and another window is behind it."

    e "Wow! I thought the dorms would be fancy, but I wasn’t expecting all this!"

    show bsf normal

    bsf "I mean we’re at one of the best art schools in the world, considering how much we’re paying I'd hope it’d be this nice!"

    e "Haha yeah."

    e "(Maybe now’s not the time to mention that I’m here on a scholarship…)"

    "They start unpacking."

    bsf "So what’s your major?"

    e "I’m a Fashion Major!"

    bsf "You’re kidding, me too! Well, Slaycademy is known for having a really good fashion department, so I guess I shouldn’t be surprised!"

    bsf "So, what classes do you have?"

    e "Pretty much the basic classes right now, like *class and *class."

    bsf "Oh I’m taking *class too! Does it happen to be the Monday class at 9 am?"

    e "Yup! I’m kind of worried I won’t be able to find it though. This campus is so huge…"

    bsf "Oh I think I know where it is actually! I’ve been here a few times for parties so I know my way around a little."

    bsf "Do you want me to show you?"

    e "Could you? That would be great!"

    bsf "Of course! It’ll be a good opportunity for you to explore the campus."
    
    bsf "C'mon let's go!"


    # This ends the game.

    return