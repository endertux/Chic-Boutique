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

define mc = Character("[povname]")
define anon = Character("???")

define Felix = Character("Felix", color = "#3f7d2d" )
define Addie = Character("Addison", color = "#32327c" )
define Kyle = Character("Kyle", color = "#b72417")

define ra = Character("RA", color = "#a84480")
define Nadia = Character("Nadia", color = "#9b33c6")

#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen Body_Base:
    image "Assets/Body.Base.png":
        xpos 300
        ypos 0

# Tops Define
screen top0 zorder 2:
    image "Assets/Top_1.png":
        xpos 300
        ypos 0

screen top1 zorder 2:
    image "Assets/Top_2.png":
        xpos 300
        ypos 0

screen top2 zorder 3:
    image "Assets/Top_3.png":
        xpos 300
        ypos 0

screen top3 zorder 4:
    image "Assets/Top_4.png":
        xpos 300
        ypos 0

# Pants Define
screen bottom0 zorder 3:
    image "Assets/Bottom_1.png":
        xpos 300
        ypos 0

screen bottom1 zorder 3:
    image "Assets/Bottom_2.png":
        xpos 300
        ypos 0

screen bottom2 zorder 3:
    image "Assets/Bottom_3.png":
        xpos 300
        ypos 0

screen bottom3 zorder 3:
    image "Assets/Bottom_4.png":
        xpos 300
        ypos 0

# Shoes
screen shoe0 zorder 1:
    image "Assets/Shoe_1.png":
        xpos 300
        ypos 0

screen shoe1 zorder 1:
    image "Assets/Shoe_2.png":
        xpos 300
        ypos 0

screen shoe2 zorder 1:
    image "Assets/Shoe_3.png":
        xpos 300
        ypos 0

screen shoe3 zorder 1:
    image "Assets/Shoe_4.png":
        xpos 300
        ypos 0

#Dress up menu screen
#Start button
screen outfits:
    image "Minigame/startmenu.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.55) action [Show("outfits_ui"), Show("Body_Base"), Show("top0"), Show("bottom0")]
#Minigame

define gui.scrollbar_size = 24

init python:
    #an array of the items the player ownes, these are the unique names of the clothing items, just add an item to the list to give it to the player
    owned_outfits = ["top0", "top1", "top2", "top3", "bottom0", "bottom1", "bottom2", "bottom3", "shoe0", "shoe1", "shoe2", "shoe3"]


    #adding new outfit options:
        #copy and paste one of the current outfits to the bottom of the list (all three items in the group of three: top, bottom, and shoe)
        #chenge the first string path name in each item to the regular image of the item as it should apear if the player owns it
        #change the second string path name in each item to the locked image of the item, as it should apear if the item is not owned (this image should be the same size as the other)
        #you don't need to change the third string, that just defigns the types of the items
        #change the fourth string to the unique name of the item i.e. top0, shue3
        #change the first of the three numbers to the clouthing item number. this is the number that tells the game what the player is wearing outside of the dress up screen i.e if the player is weearing top number 0, 1, or 2
        #the last two numbers are x and y offsets for the items, check that the items are aligned properly and adjust the offsets if needed
        #change the xsize INSIDE the viewport to the current number of clothing options times the x_spacing for the grid (for each item you add, add x_spaceing to the xsize, again only in the viewport)

    
    #an array of clothing buttons(outfits are organised in groups of three items, the order is top, bottom, shoe. this order is required for the code to work)
    outfit_buttons = [ #outfit buttons (path of normal clothing, path of lock clothing image, type (top, bottom, shoe), showname, item id number (saved clothing item number), offsetx, offsety)
        #prologue outfits
        ("Assets/Top_1_%s.png", "Assets/Top_1_%s.png",    "top",   "top0", 0,     0, 0),
        ("Assets/Bottom_1_%s.png", "Assets/Bottom_1_%s.png", "bottom", "bottom0", 0, -20, 40),
        ("Assets/Shoe_1_%s.png", "Assets/Shoe_1_%s.png",   "shoe",   "shoe0", 0,   0, 120),

        ("Assets/Top_2_%s.png", "Assets/Top_2_%s.png",    "top",   "top1", 1,     -50, -30),
        ("Assets/Bottom_2_%s.png", "Assets/Bottom_2_%s.png", "bottom", "bottom1", 1, 0, 50),
        ("Assets/Shoe_2_%s.png", "Assets/Shoe_2_%s.png",   "shoe",   "shoe1", 1,   0, 100),

        ("Assets/Top_3_%s.png", "Assets/Top_3_%s.png",    "top",   "top2", 2,     10, 60),
        ("Assets/Bottom_3_%s.png", "Assets/Bottom_3_%s.png", "bottom", "bottom2", 2, 0, 50),
        ("Assets/Shoe_3_%s.png", "Assets/Shoe_3_%s.png",   "shoe",   "shoe2", 2,   0, 50),

        ("Assets/Top_4_%s.png", "Assets/Top_4_%s.png",    "top",   "top3", 3,     0, 60),
        ("Assets/Bottom_4_%s.png", "Assets/Bottom_4_%s.png", "bottom", "bottom3", 3, 0, 50),
        ("Assets/Shoe_4_%s.png", "Assets/Shoe_4_%s.png",   "shoe",   "shoe3", 3,   0, 100),


        #TEST OUTFITS, these are chapter one outfits that are here to show the scroll bar
        ("Assets/Top_5_%s.png", "Assets/Top_5_%s.png",    "top",   "top0", 0,     -20, 30),
        ("Assets/Bottom_5_%s.png", "Assets/Bottom_5_%s.png", "bottom", "bottom0", 0, -20, 40),
        ("Assets/Shoe_5_%s.png", "Assets/Shoe_5_%s.png",   "shoe",   "shoe0", 0,   0, 120),

        ("Assets/Top_6_%s.png", "Assets/Top_6_%s.png",    "top",   "top1", 1,     0, 40),
        ("Assets/Bottom_6_%s.png", "Assets/Bottom_6_%s.png", "bottom", "bottom1", 1, 0, 50),
        ("Assets/Shoe_1_%s.png", "Assets/Shoe_1_%s.png",   "shoe",   "shoe1", 1,   0, 100),

        ("Assets/Top_7_%s.png", "Assets/Top_7_%s.png",    "top",   "top2", 2,     10, 60),
        ("Assets/Bottom_7_%s.png", "Assets/Bottom_7_%s.png", "bottom", "bottom2", 2, 0, 50),
        ("Assets/Shoe_3_%s.png", "Assets/Shoe_3_%s.png",   "shoe",   "shoe2", 2,   0, 50),

        ("Assets/Top_8_%s.png", "Assets/Top_8_%s.png",    "top",   "top3", 3,     0, 60),
        ("Assets/Bottom_4_%s.png", "Assets/Bottom_4_%s.png", "bottom", "bottom3", 3, 0, 50),
        ("Assets/Shoe_4_%s.png", "Assets/Shoe_4_%s.png",   "shoe",   "shoe3", 3,   0, 100),
        #TEST OUTFITS, these are chapter one outfits that are here to show the scroll bar
    ]

    #these three arrays automatically fill themselfs with Hide() functions for every item of their respective types. when you press a button it uses these to first hide all items of that type on the character before showing the specific one clicked
    tops = []
    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons):
        if Type == "top":
            tops.append(Hide(showname))
    bottoms = []
    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons):
        if Type == "bottom":
            bottoms.append(Hide(showname))
    shoes = []
    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons):
        if Type == "shoe":
            shoes.append(Hide(showname))

screen outfits_ui:
    image "Backgrounds/classroom bg.jpg"
    image "Minigame/ui_base.png" align(1.1, 1.0) size (1300, 1100)
    imagebutton auto "Minigame/done_%s.png" align(0.02, 0.95) action Jump("instructions")
    
    fixed:
        #align the outfit window on screen
        align(0.905, 0.45)
        #the x size of the entire outfit window
        xsize 1000
        #the y size of the entire outfit window
        ysize 900
        vbox:
            viewport id "outfit_viewport":
                mousewheel True
                draggable True
                fixed:
                    #x start of clothing item grid (shift all items horizontally)
                    $ x_start = 40
                    #y start of clothing item grid (shift all items vertically)
                    $ y_start = 25
                    #x spacing of clothing item grid (the horizontal seperation between outfits)
                    $ x_spacing = 250
                    #y spacing of clothing item grid (the vertical seperation between outfits)
                    $ y_spacing = 250

                    #x size of the clothing item grid (number of outfit options * x_spacing) this is the interier size of the scrolling space
                    xsize 2000
                    #y size of the clothing item grid (not really necesary, just use outfit offsets in the outfit_buttons array) this is the interier size of the scrolling space
                    ysize 900

                    #loop through clothing buttons
                    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons):
                        imagebutton:
                            #if you own an item (I.E. its in owned_outfits)
                            if showname in owned_outfits:
                                #set inage to the normal clothing image
                                auto imagepath
                                #set the items position on the grid
                                pos (x_start + Xoffset + (i // 3) * x_spacing, y_start + Yoffset + (i % 3) * y_spacing)

                                #set up action to set clothing when pressed. for each option it hides all items of that type and then shows the specific one you clicked
                                if Type == "top":
                                    action [tops, Show(showname), SetVariable(Type, setval)]
                                if Type == "bottom":
                                    action [bottoms, Show(showname), SetVariable(Type, setval)]
                                if Type == "shoe":
                                    action [shoes, Show(showname), SetVariable(Type, setval)]
                            #else if you don't own it (I.E. its not in owned_outfits)
                            else:
                                #set the items position on the grid
                                pos (x_start + Xoffset + (i // 3) * x_spacing, y_start + Yoffset + (i % 3) * y_spacing)
                                #set inage to the locked clothing image
                                auto imagepathmissing
            #create the scrollbar (its at the bottom of a vbox to it is stacked under the outfit window, to place it above, move it to the top of the vbox)
            bar value XScrollValue("outfit_viewport") style "outfit_scrollbar"#set up scrollbar and style it (it's at the bottom of a vbox so its under the clothing buttons)

#define the scrollbar style (art assets, size)     
style outfit_scrollbar:#scrollbar style
    ysize 80  # Height of your scrollbar (in pixels)
    base_bar Frame("gui/scrollbar/horizontal_idle_bar.png", 10, 10, 10, 10)  # background art (track)
    thumb "gui/scrollbar/horizontal_idle_thumb_large.png"  # thumb art (draggable part)
    thumb_offset 45  #offset of thumb collider
    


#This image can be used for the rest of the game, or just as a final reveal.
layeredimage Player:
    always:
        "Assets/Body.Base.png"

    group shoe:
        attribute 0 default:
            Null()
    if shoe == 0: 
        "Assets/Shoe_1.png"
    if shoe == 1: 
        "Assets/Shoe_2.png"
    if shoe == 2: 
        "Assets/Shoe_3.png"
    if shoe == 3: 
        "Assets/Shoe_4.png"

    group top:
        attribute 0 default:
            Null()
    if top == 0:
        "Assets/Top_1.png"
    if top == 1:
        "Assets/Top_2.png"
    if top == 2:
        "Assets/Top_3.png"
    if top == 3:
        "Assets/Top_4.png"

    group bottom:
        attribute 0 default:
            Null()
    if bottom == 0:
        "Assets/Bottom_1.png"
    if bottom == 1:
        "Assets/Bottom_2.png"
    if bottom == 2:
        "Assets/Bottom_3.png"
    if bottom == 3:
        "Assets/Bottom_4.png"
        
###############################################################
#################### Gameplay: Prologue #######################
###############################################################
label start:
call screen outfits
label instructions:
    scene bg with dissolve

    hide screen outfits
    hide screen outfits_ui

    hide screen Body_Base
    hide screen top0
    hide screen top1
    hide screen top2
    hide screen top3
    hide screen top4
    hide screen bottom0
    hide screen bottom1
    hide screen bottom2
    hide screen bottom3
    hide screen bottom4
    hide screen shoe0
    hide screen shoe1
    hide screen shoe2
    hide screen shoe3
    hide screen shoe4

    show Player:
        xpos 0.38
        ypos 0
    with dissolve

    # Ask player for their custom name
    $ povname = renpy.input("Before you make your grand debut, what is your name?", default="").strip()

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
        ypos 0.1
    with dissolve
    
    # Neutral/Happy Face
    "I made it? All my hard work was worth it!"

    "All of the people I’ll meet and the opportunities I’ll come across…"

    # Determined Face
    "I have to make the most of this."

    "I {i}will{/i} make the most of this."

    hide Player

    #BLACK SCREEN WITH WHITE TEXT ACROSS
    scene black bg
    with fade

    "A summer passes and the fall season begins…"

    #BLACK SCREEN WITH WHITE TEXT ACROSS 

    "A new chapter begins…"

    #CG OF SLAYCADEMY ENTraNCE 
    #IF POSSIBLE, do a pan up reveal
    scene school
    with fade

    show Player:
        xpos 0.01
        ypos 0.07 
    with dissolve
    
    #play music
    play music "podcast-smooth-jazz-instrumental-music-225674.mp3" volume 0.5
    # https://pixabay.com/music/smooth-jazz-podcast-smooth-jazz-instrumental-music-225674/

    # Suprised Face
    "This doesn’t feel real…"

    "One of the most prestigious art schools in the world and I’m here!"

    "Not as a visitor but as a real student!"

    #INSERT OF SCHOOL MAP 
    #map should look confusing and unclear

    scene map temp 
    with fade 
    
    show Player:
        xpos 0.01
        ypos 0.07 
    with dissolve

    "Orientation materials are never any help when you can’t read maps!" 
    #😞 Sigh Face

    "And an {i}online{/i} orientation? At least include a tour!"

    "If I had to figure this out right before classes, I’d be totally screwed!"

    "…"

    "Hah…"

    #FADE INSERT AWAY
    scene black bg
    with dissolve
    show Player:
        xpos 0.01
        ypos 0.6
    with dissolve

    # Cry Face
    "WHY AM I SO NERVOUS?!"

    # Determined Face
    "Aright, one foot in front of the other…"

    scene map temp 
    with fade 
    #FADE INSERT AWAY
    #scene 
    #with dissolve
    #show Player:
    #    xpos 0.01
    #    ypos 0.6

    "I have to at least go into the school if I want to attend…"

    #"…Which way first?"

    #COMMON ROUTE CHOICE 1: [museum] [garden] [field]
    show dim_bg
    menu:
        # Confused Face
        "…Which way first?"

        "Museum":
            jump museum
        "Garden":
            jump garden
        "Field":
            jump field


    label museum:
    #BG ART OF SCHOOL MUSEUM
        scene museum 4
        with fade
        show Player:
            xpos 0.01
            ypos 0.07
        with dissolve

        mc "Where am I!" 
        #🥲

        mc "I’m totally lost, but…"

        # Suprised Face
        mc "This place is beautiful so I’m not complaining!"

        mc "I can’t believe that a school has a building like this."

        mc "As expected from a top university…"

    screen choice_menu():
        modal True #prevents clicks outside buttons

        hbox:
            align (0.5, 0.5)  # Center the menu
            spacing 50

        # first choice: "Painting on the left": 
            imagebutton: 
                idle "ArtGuy/goya_redone.png" 
                hover "ArtGuy/goya_redone.png" 
                action Jump("goyascene")
                xalign 0.5
                yalign 0.5

        # second choice: painting on the left
            imagebutton:
                idle "ArtGuy/madrone_redone.png" 
                hover "ArtGuy/madrone_redone.png" 
                action Jump("madronescene")  
                xalign 0.5
                yalign 0.5

    # menu call in script 
    label paintings : 
        scene black bg
        show Player:
            xpos 0.01
            ypos 0.07
        mc "Wow, these paintings are so cool! Which one should I look at?"
        call screen choice_menu 

    label goyascene :
        scene black bg
        show goya 
        with fade 

        #INSERT OF AN ART PIECE 
        #im referencing this one you can just take the pic and put a pixel filter over bc its public domain now (refer to google doc)
        #"Virgin and Child with Canon van der Paele" Painting by Jan van Eyck

        "Wow, compared to the other one, this painting is so muted!"

        #(Felix)
        anon "It’s haunting, right?"

        # Confused Face
        "!"

        hide goya 
        #FELIX SPRITE
        show Player:
            xpos 0.01
            ypos 0.6
        with dissolve

        show artguy normal

        with dissolve

        show artguy speak
        #(Felix) Neutral Face
        anon "Sorry! I didn’t mean to startle you."
        # MC nerutal face

        #(Felix)
        anon "It’s just that I noticed you seemed lost in thought looking at this piece."

        scene black bg
        hide artguy normal
        hide Player
        show goya
        with fade

        show artguy speak:
            xpos 0.72
            ypos 0.1

        #(Felix) Intrested Face
        anon "I feel the same way every time I see it."
        hide artguy

        show Player:
            xpos 0.01
            ypos 0.07

        # Suprised Face
        mc "The world is so mind-bending… I feel like I’m getting sucked into the painting just by looking at it."
        hide Player

        show artguy speak:
            xpos 0.72
            ypos 0.1

        #(Felix) Intrested Face
        anon "I get what you mean! The artist actually painted this directly on his walls."

        #(Felix)
        anon "After slowly becoming deaf, he isolated himself in his house to paint these large frescos that are now considered 'The Black Paintings.'"
        anon "It's really quite tragic but it's a very beautiful painting."
        anon "I didn't mean to get dark, but sometimes I just get lost in the painting myself."

        hide goya
        hide art guy speak
        scene museum 4
        with fade
        jump artguyscene

    label madronescene :
        #INSERT OF AN ART PIECE 
        #im referencing this one you can just take the pic and put a pixel filter over bc its public domain now (refer to google doc)
        #"Virgin and Child with Canon van der Paele" Painting by Jan van Eyck
        scene black bg
        show madone painting
        with fade

        "The colors on this are so vibrant!"

        #(Felix)
        anon "It’s amazing, right?"

        # Confused Face
        "!"

        hide madone painting
        #FELIX SPRITE
        show Player:
            xpos 0.01
            ypos 0.6
        with dissolve

        show artguy normal

        with dissolve

        show artguy speak
        #(Felix) Neutral Face
        anon "Sorry! I didn’t mean to startle you."
        # MC nerutal face

        #(Felix)
        anon "It’s just that I noticed you seemed lost in thought looking at this piece."

        scene black bg
        hide artguy normal
        hide Player
        show madone painting
        with fade

        show artguy speak:
            xpos 0.72
            ypos 0.1

        #(Felix) Intrested Face
        anon "I feel the same way every time I see it."
        hide artguy

        show Player:
            xpos 0.01
            ypos 0.07

        # Suprised Face
        mc "The colors are so bright… I feel like I’m getting sucked into the painting just by looking at it."
        hide Player

        show artguy speak:
            xpos 0.72
            ypos 0.1

        #(Felix) Intrested Face
        anon "I get what you mean! The artist actually spent months meticulously making his own paints."

        #(Felix)
        anon "Back then, oil paints were made with eggs rather than oil, but then this guy came along and had the idea of using oil. So simple yet effective…"

        hide madone painting
        hide art guy speak
        scene museum 4
        with fade
        jump artguyscene
        

    label artguyscene:
        scene museum 4
        show Player:
            xpos 0.01
            ypos 0.6

        show artguy normal
        with dissolve

        mc "You seem to know a lot about this painting! I just thought it looked cool."
        #😅 Nervous Sweat Drop Face

        #(Felix) Shy Face - Looking down, slight turned away & blush
        anon "Ah, I’m a fine arts major. I’m working on a project focusing on just the pieces we have at our campus museum."

    scene museum 4
    show Player:
        xpos 0.01
        ypos 0.6
    show artguy normal
    
    # Surprised Face
    #mc "The fabric looks so real that I can tell exactly what they are. I can practically feel the soft velvety texture in my hands…"

    show artguy speak
    
    #(Felix) Neutral Face
    #anon "It’s so intentional too! He built up thin layers of paint to make it more vibrant and textured. This artist is actually credited for coming up with the technique."

    #FADE INSERT AWAY

    #(Felix)
    #anon "From your fabric comment, I’m guessing you’re here for fashion?"

    anon "I'm sure you're going to get this a ton, but what major are you?"
    anon "Wait, let me guess."
    anon "Are you fashion? I love your style."

    show artguy normal

    # Neutral/Happy Face
    mc "Aww omg thank you! I am. I'm [povname], by the way. It’s my first day on campus."

    show artguy speak

    # Neutral Face
    Felix "Felix. Fashion’s not an easy department to get into. You must be really good!"

    show artguy normal

    mc "I wouldn’t say all that. It’s just hard work."

    show artguy speak

    # Sly/Smerking Face
    Felix "I don’t usually see fashion majors in this building. Thinking of switching majors?" 
    #this is just said playfully hes not actually asking so maybe put a playful expression

    show artguy normal
    
    # Sweat Drop Face
    mc "More like just totally, utterly lost."

    show artguy speak

    # Neutral Face
    Felix "I gotta say, the campus is nice, but navigating it… Not as great. Where are you headed? Maybe I can point you in the right direction."

    show artguy normal
   
    # Neutral Face
    mc "I guess freshman dorms? I should check in before exploring around a bit more."

    show artguy speak

    # Suprised Face (little bit, eyebrow raise)
    Felix "No wonder why you were so lost! The dorms are always impossible to get to."

    # Neutral Face 
    Felix "Bad news is… it’s about a 25 minute walk."

    show artguy normal

    # Cry Face
    mc "25 minutes?!"

    show artguy speak

    Felix "But wait! The good news is that I can walk you there."

    show artguy normal

    # Neutral Face
    mc "Are you sure? 25 minutes is a long ways away…"

    show artguy speak

    Felix "It’s no problem. Research can wait."

    show artguy normal

    # Determined Face
    mc "If you’re researching right now, you should focus!"

    # Sweat Drop Face
    mc "Plus if you walked me there, I have a feeling I’d tune out my surroundings and never get the hang of the campus layout. I’ll be fine on my own, just point me in the right direction."

    show artguy speak
    
    Felix "Alright, alright. Just don’t get too lost and end up back in front of this painting again."

    #INSERT OF SCHOOL MAP
    #map should look confusing and unclear still
    scene map temp

    Felix "There’s a clear path riiiight here. Here, I’ll highlight it for you so you can’t miss it."

    with dissolve

    #INSERT OF SCHOOL MAP
    #map should now have a highlighted path on it
    scene black bg
    with fade
    #FADE SCENE TO OUTSIDE ON PATH
    jump path


label garden:
    #BG ART OF SCHOOL GARDEN
    scene garden temp

    show Player:
        xpos 0.01
        ypos 0.07
    with dissolve

    # Surprised Face
    "Ah! I’ve seen this place on the school website before!"

    "And now I’m really here in real life! It’s so pretty!"

    "Seems like a nice place to study… Maybe I should mark it on the map for later."

    # Confused Face
    "…"

    "Wait…where did my map go?"
    #😞 Cry Face

    #(Addie)
    anon "Hey, you there!"

    "?"
    #ADDIE SPRITE
    show Player:
        xpos 0.01
        ypos 0.07
    with dissolve
    #should be kind of far away on the screen

    # Confused Face
    "Is she talking to me?"

    show baddie normal:
        xpos 0.75
        ypos 0.3
    with dissolve

    anon "Yes, you! Cutie with the cute fit! You dropped your map!"

    # Suprised Face
    mc "Oh!"

    #RUNNING SOUND EFFECT
    #ADDIE SPRITE APPEARS CLOSER

    scene garden temp
    with dissolve

    show Player:
        xpos 0.01
        ypos 0.6

    show baddie normal
    with dissolve

    mc "Thank you so much! I didn’t even notice that I had dropped it."
    #😞 Cry Face

    # Suprised Face
    "Wow she’s so pretty… and her outfit is so put-together yet effortless."

    #(Addie)
    anon "No probs."

    #(Addie)
    anon "You a freshman?"

    menu: 
        #Neutral face
        "Did the map give it away?":
            jump addiechoiceone
        "How'd you know?":
            jump addiechoiceone

    label addiechoiceone : 
        scene garden temp

        show Player:
            xpos 0.01
            ypos 0.6

        show baddie normal

        #(Addie)
        anon "The lost look in your eyes told me. Don’t worry about it, this school is huge. We’ve all been there."

        # Sweat Drop Face
        "Her gaze is making me a little nervous… It’s like I’m being studied."

        #(Addie)
        anon "So where ya headin, babe?"

        mc "I was trying to get to the student dorms, before I lost my map."

        #(Addie) Excited Talking Face
        anon "Ooh! I lived there last year! So many memories…"

        #(Addie) Eager Face
        anon "Hey, I don’t have anything going on right now if you want me to take you there?"

        menu: 
            "No, you really don't have to.":
                jump notrouble 
            "Is it far?":
                jump notrouble

       
    # Surprised Face
    label notrouble : 
        scene garden temp
        show Player:
            xpos 0.01
            ypos 0.6

        show baddie normal
        mc "I don’t want to trouble you too much…"

        #(Addie) Winking Face
        anon "No, it’s no trouble at all. I can’t leave a cute girl lost in the garden like this!"

    #WALKING SOUND EFFECT THROUGHOUT SCENE
    #since they’re outside make it sound like they’re on a track; sound shouldn’t be too loud so it doesn’t distract from dialogue
    show Player:
        xpos 0.01
        ypos 0.6

    show baddie normal
    with dissolve

    #(Addie) Neutral Face
    anon "So, what’s your name?"


    # Neutral Face
    mc "[povname]. And you’re…?"

    #(Addie) Winking Face
    Addie "Addison. But my friends call me Addie!"
    #😉

    # Sweat Drop Face
    mc "Gotcha. It’s nice to meet someone so friendly right away. I was really concerned about making friends here, to be honest…"

    # Neutral Face
    Addie "No, I get it. I’m not gonna lie, you’re gonna meet some people here that are a little pretentious. It {i}is{/i} Slaycademy, after all."

    # MC Confused Face

    # Notice Face
    Addie "?"

    # Excited Talking Face
    Addie "But don’t worry! Most of the people here are really nice. And for a girl as cute as you, you’ll have no problem making friends!"

    menu : 
        "Haha... thanks!": 
            jump ofcourse
        "You think so?": 
            jump ofcourse

    label ofcourse : 
        scene garden temp
        show Player:
            xpos 0.01
            ypos 0.6

        show baddie normal
        Addie "Of course!"

    # Neutral Face
    Addie "So, what are you here for? Architecture? Film?"

    # Cry Face
    "Ah-"

    "I should’ve dressed a little nicer…"

    # Sweat Drop Face
    mc "I’m a fashion major!"
    
    mc "I usually dress up a little more than this… I didn’t expect to meet anyone until the first day of classes."

    Addie "Hey, what are you talking about!? I can tell a fellow fashionista when I see one."

    scene garden temp

    #ADDIE WINKS
    #SUDDENLY HER EYES WIDEN AS SHE STARES JUST ABOVE YOUR HEAD

    show garden temp with vpunch

    show Player:
        xpos 0.01
        ypos 0.6

    # Surprised Face
    Addie "Umm..."

    # Confused Face
    mc "What??"

    show baddie normal

    Addie "Alright... DON’T freak out, okay..."

    menu: 
        "What is it?":
            jump bee
        "Oh, don't tell me..":
            jump bee

    label bee : 
        scene garden temp
        show Player:
            xpos 0.01
            ypos 0.6

        show baddie normal

        # Surprised Face
        Addie "There-"
        Addie "There’s a bee!"

    mc "AHHHH GET IT OFF!!!"
    # Put choice here
    menu: 
        "Freak out": 
            jump freakout 
        "Act calm": 
            jump actcalm

    label freakout : 
        scene garden temp
        show Player:
            xpos 0.01
            ypos 0.6

        show baddie normal
        mc "AHHHH GET IT OFF!"
        # mc in distress 
        # addie in distress 
        mc "???"
        mc "Aren't you going to help me?"
        Addie "I'm sorry! I just- ah!"
        Addie "This is something I just can't deal with!"
        # mc cry face
        mc "Please..."
        mc "I can feel it crawling on me..."
    
        Addie "O-okay."
        Addie "Just-just give me one second, okay?"
        #hide Addie sprite
        #show Addie sprite with notebook in hand
        #woosh sfx and vfx
        #Addie sigh face
        Addie "Got it!"
        #mc sigh face
        mc "Thank you!"
        Addie "Of course, babe!"
        Addie "It was nothing, really."

    
    label actcalm : 
        scene garden temp
        show Player:
            xpos 0.01
            ypos 0.6

        show baddie normal
        mc "Ah..."
        mc "That's no big deal."
        
        #Addie sprite backing up
        #show through visual/audio guides a bee to a flower
        #Addie cry or shocked face

        Addie "How were you so calm??"
        mc "They're harmless as long as you leave them alone!"

        #Addie distressed face
        Addie "Ugh, I'm just glad that it's gone!"
        mc "No way..."
        mc "Are you...scared of bees?"

        #Addie embarrassed face 
        Addie "How could you not be!?"

        #mc closed eye smiling
        mc "Haha, I didn't expect you to be so afraid of something so small."
        Addie "Well, at least it's been dealt with."

    #addie hair flip sprite would require a new pose which idk if artists are willing to do
    #good substitute could just be addie wink face (or honestly just her neutral face)

    "Oh, she's returned to normal."

    # wink face
    Addie "It probably just thought you were a flower! Easy mistake."

    #(Student)
    anon "Addison!"

    # surprised face
    Addie "Shoot!" 
    #😨

    #(Student)
    anon "You told me you’d meet me at the quad 20 minutes ago!"

    # wink face
    Addie "Sorry babe, I gotta run."

    # neutral face
    Addie "Luckily it’s super easy to get to the dorms from here. Just follow this path to the end, ‘kay?"

    # neutral happy face
    mc "Thank you so much! For everything. I’ll see you around then!"
      
    show baddie normal at Move((0.33, 0), (0.8, 0), 2.0)
    pause 1.3
    show baddie normal at Alpha(1.0, 0.0, 1.0)

    Addie "See ya!"

    #RUNNING SOUND
    #ADDIE SPRITE HIDE

    # sweat drop face
    "Wait a minute… Didn't she say she had nothing to do?"

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
    with dissolve

    # neutral face
    "Well, this is a place I probably won’t be seeing much of…"

    "I didn’t even think that an art school would need a place like this."

    "Maybe that’s just the kind of crazy budget that they h-"

    # surprised face
    mc "AHH-"

    #SHAKE SCREEN EFFECT
    #CraSH NOISE
    show field with hpunch

    # cry face
    mc "Ow…"

    #maybe put some sort of screen movement here to indicate that she stood back up after falling

    #KYLE SPRITE

    show gymbro normal
    with dissolve 

    # yelling face
    #(Kyle)
    anon "You’re blocking the field, bro!!!!!"

    # confused face
    "No apology?"

    # determined face
    mc "If you saw me then you didn’t have to barrel right into me!"

    # neutral face
    #(Kyle)
    anon "Yah, you’re right, dude. My bad!"

    "What’s with this guy!?"

    #(Kyle)
    anon "So, you here to play?"

    # confused face
    mc "Huh?"

    # neutral face
    mc "Oh! No, no I was just wandering around and got a little lost."

    #(Kyle)
    anon "That’s a shame, man. We could really use more students in the sports department."

    mc "Are you a sports major?"

    #(Kyle)
    anon "Yeah, bro. Can’t you tell I lift??"

    mc "I just didn’t know that Slaycademy had a sports department."

    anon "Haha, they don’t!"

    # confused face
    mc "What? Then how are you-"


    #(Kyle)
    anon "Look, man. Rome wasn’t built in a day, alright?"

    #(Kyle)
    anon "You know what they say!"

    # cry face
    "No… I don’t…"

    "Please! Someone… Anyone! Get me out of this conversation!"

    "Ah… We’re the only ones on the field…"

    #(Kyle)
    anon "Anyways, I’m gonna be attempting a 350 squat today. It’ll be hard, but I think with an audience I’ll be hyped enough to do it."

    #(Kyle)
    anon "Maybe I should practice right now! Tell me how my form is, here-"

    # sweat drop face
    mc "Actually, I really gotta get going."

    #(Kyle)
    anon "Aw man, that’s a shame! We were really vibing!"

    "Were we?"

    # neutral face
    mc "Would you mind pointing me in the direction of the freshman dorms?"

    # cry face
    "Please respond normally!"

    #(Kyle)
    anon "Down near the tennis courts over there, follow the dirt path."

    # sigh face
    "Oh, thank god…"

    #(Kyle)
    anon "Haha, that reminds me of a movie I watched. Follow the yellow brick road!"

    #(Kyle)
    anon "The movie’s super underground. Sorry for the obscure reference!"

    # flat face
    "..."

    mc "Yeah… Thanks for the directions."

    #(Kyle)
    anon "No prob, bro. Gotta get back to running my laps. Good luck finding the cafeteria or wherever you wanted to go!"

    hide gymbro
    with dissolve

    # sweat drop face
    mc "Did this guy really give me the right directions??"

    scene black bg
    with fade

    jump path

label path:
    #FADE TO SCENE OUTSIDE ON PATH

    #atp all choice options should have converged into the same main story where player is on the path outside

    #BG ART OF PATH
    scene temp path
    with fade

    show Player:
        xpos 0.01
        ypos 0.07
    with dissolve

    # neutral happy face
    "It’s great that I was able to get directions from someone."
    
    # sweat drop face
    "I don’t think I would’ve made it here on my own."
    #😓

    # surprised face
    "But this path looks like it goes on forever…"

    #FADE BLACK SCREEN WITH WHITE TEXT ACROSS

    scene black bg
    with fade

    "A while later…"

    #FADE BRIGHT WHITE SCREEN
    #think it would be funny here to make it a scene where shes like i didnt think i would make it 😭 and the bright light is literally like her being like i see the light

    show temp path
    #show white bg
    with fade

    show Player:
        xpos 0.01
        ypos 0.6
    with dissolve

    # distressed face
    mc "Did-"

    mc "Did I really make it?"

    # determined face (if artists draw it vaguely enough, it can serve as upset face)
    "Who had the bright idea of building this school on a bunch of hills?!"
    #tbh this is straight out of my experience at korea university bc korea is super mountainous but its like they did no landscaping at all they just plopped the school right on the hills…walked to the dorms ONCE and was so winded and with my iron deficiency i was seeing stars

    # distressed face
    "I need to sit down…"

    #BG ART OF DORMS FRONT DESK
    scene temp lounge
    with dissolve

    show Player:
        xpos 0.01
        ypos 0.07 
    with dissolve

    mc "Hah…"
    #😓

    #SOUND AND SCREEN EFFECT TO INDICATE THAT PLAYER IS NOW SITTING

    # determined face (can serve as upset)
    "Big ass school and no way to get up here besides that dirt path-"

    "Judging by how long that took me, I’ll need to wake up before classes like an hour early-"

    # distressed face
    "If I want my outfit to be even a little decent, it’ll need to be earlier."

    "Should I drop out?"

    "Should I do it?"

    # concerned face
    ra "Um…"

    "?"
    show Player:
        xpos 0.01
        ypos 0.6

    #ra SPRITE
    show ra normal:
        xpos 0.70
        ypos 0.4

    with dissolve   
    # concerned face
    ra "Are you a student here?" 

    #  happy neutral face
    mc "Ah-yes!"

    scene temp lounge
    with dissolve

    show Player:
        xpos 0.01
        ypos 0.6  

    show ra normal
    with dissolve

    # distressed face
    mc "I’m sorry, I should’ve checked in before using the lounge!"

    # neutral face
    ra "No worries! …Did you really walk all that way?"

    mc "...Yes."

    ra "You know we have a shuttle system, right?"

    # surprised face
    mc "Wait, WHAT?!"

    # cry face
    mc "You mean I didn’t have to walk all that way?!"

    ra "Haha don’t worry, you’re not the only one who’s made that mistake. It’s kind of an unofficial freshman tradition."

    ra "Please, take a seat! You must be winded. I’ll get you checked in."

    ra "Could you give me your name and ID number for check-in?"

    # neutral happy face
    mc "Yes, it’s [povname] and my ID number is 14399333."

    ra "Wonderful! You’re all checked in."

    #INSERT OF ACCESS CARD

    ra "This will give you access to the dorm building and all amenities. The number in the corner is the PIN for your room’s lock."

    #FADE INSERT AWAY

    ra "You’ll be on the second floor in room 143. Your roommate checked in early this morning, so she should be here already."

    mc "Thank you!"

    ra "Oh! And the elevator is in maintenance this week. The stairs are right next to it."

    # cry face
    mc "Thanks…"
    #😭

    #BG ART OF DORM HALL
    scene temp hallway
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    # happy neutral face
    "Even the hallways feel fancy."

    "I wonder what the room w-"

    # surprised face
    mc "Ah!"

    #(Nadia)
    anon "AH-"
    show temp hallway with hpunch

    #CraSH EFFECT

    scene zoe cg

    #CG NADIA ON FLOOR

    #(Nadia)
    anon "Ow ow ow ow ow"

    # distressed face
    mc "Are you alright?!"

    #(Nadia)
    anon "Oh my god! I’m so sorry! I totally wasn’t looking where I was going…"


    mc "Don’t worry about it! Are you hurt? Do you need help getting up?"

    #(Nadia)
    anon "No, I’m good, I’m good."

    scene temp hallway
    with fade

    show Player:
        xpos 0.01
        ypos 0.6  

    show bsf normal
    with dissolve

    #(Nadia)
    show bsf sad
    anon "I lost a piece of jewelry that’s important to me earlier and the RA just called and told me that someone turned it in."

    #(Nadia)
    show bsf speak
    anon "I guess thinking about it now… it’s not like it was gonna go anywhere."

    #(Nadia)
    show bsf sad
    anon "But I was so desperate to get it back!"

    show Player:
        xpos 0.01
        ypos 0.6

    # neutral happy face
    show bsf normal
    mc "I’m guessing you’re a resident of this dorm?"

    show bsf speak
    Nadia "Yup! Name’s Nadia."

    show bsf normal
    mc "[povname]. You should probably go get that jewelry. Seems like it means a lot to you."

    show bsf speak
    Nadia "Ah! The jewelry! I almost forgot…"

    # sweat drop face
    show bsf normal
    "..."

    show bsf speak
    Nadia "I’m sure we’ll see each other around a lot. Let’s hang out sometime!"

    # neutral happy face
    show bsf normal
    mc "Sounds good! It’ll be nice to have a friend in the dorms."

    show bsf speak
    Nadia "Oh, for sure. I gotta run but maybe I’ll see you at movie night!"


    show bsf normal at Move((0.35, 0), (0.7  , 0), 2.0)
    pause 1.2
    show bsf normal at Alpha(1.0, 0.0, 1.0)

    # confused face
    mc "Movie n-"

    # sweat drop face
    "She left…"

    # neutral happy face
    "Well, I’m bound to see her again sometime soon."

    #BG ART DORM ROOM
    scene temp dorm
    with fade

    show Player:
        xpos 0.01
        ypos 0.07 
    with dissolve 

    # distressed face
    "!"

    "So many boxes…"

    # neutral happy face
    "So, the dorm is nice too."

    "It’s so much bigger than I thought it would be! Let’s see…"

    "I could set up a mannequin here… sewing machine in this corner…"

    #DOOR BEEPING SOUND EFFECT

    # surprised face
    "?"

    #NADIA SPRITE
    show bsf normal

    show Player:
        xpos 0.01
        ypos 0.6  
    with dissolve

    show bsf speak
    Nadia "You’re…"

    show bsf normal
    mc "From earlier…"

    show bsf worried
    Nadia "HAHAHAHAHA"

    show bsf sad
    Nadia "Did we really end up as roommates!?"

    # happy face
    show bsf normal
    mc "What are the chances!?"

    show bsf speak
    Nadia "Well it’s a good thing we got introductions out of the way."

    show bsf normal
    mc "Yup, we’re practically old friends!"

    Nadia "..."

    Nadia "..."

    # confused face
    mc "Nadia…?"

    #DOOM SOUND EFFECT
    show bsf worried
    Nadia "I MADE SUCH A BAD FIRST IMPRESSION."

    # neutral happy face
    mc "Oh, come on stop worrying about that. You’re the one who ended up on the floor!"

    # surprised face
    show bsf sad
    mc "Ah, but I was curious about what you meant by movie night."

    show bsf speak
    Nadia "No one told you about movie night?"

    # confused face
    show bsf sad
    mc "Not at all..."

    show bsf speak
    Nadia "Oh, it’s just a little social event they’re holding for new students in the lounge tomorrow."

    Nadia "They’re having upperclassmen come in too so that we can meet people who have a bit more experience than us."

    Nadia "You have to come! It’ll be fun and you’ll make a ton of friends."

    # cry face
    show bsf normal
    mc "I wish I knew about this earlier! I would’ve planned an outfit but now I gotta unpack first."

    show bsf speak
    Nadia "There are wayyyy too many boxes. How many clothes do you have?"

    # sweat drop face
    show bsf normal
    mc "A lot… The thrifting addiction is real…"
    
    show bsf speak
    Nadia "I get it. I had to leave tons of boxes at my parents'."

    Nadia "Hmm… Well you don’t really wanna unpack now, do you?"

    # sweat drop face
    show bsf normal
    mc "No, but what choice do I have?"
    #😭
    
    jump dress
    with fade

return
    