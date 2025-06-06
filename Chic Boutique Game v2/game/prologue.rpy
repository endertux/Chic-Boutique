# play intro
label splashscreen:
    play sound "Chic_Boutique_Studio_Intro.mp3"
    $ renpy.movie_cutscene('intro.webm')
    return

###############################################################
######################### Dress Up ############################
###############################################################

# remember player choise connected to movie night
$ music = False

# dress up mini game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia

#These variables correspond to the images saved in "images/Minigame". If the variable is 0, the corresponding clothes will have 0 in their filename and so on.
#I set the default to 0, but you can set it to whatever you want.
#We need these variables if you want to keep the outfit you chose for the rest of the game, or if you want to do a reveal at the end of the minigame.
default bottom = 0
default shoe = 0
default top = 0

#saved outfit for the first outfit choosing scene. They are copies of bottom, shoe, and top where the current outfit is stored
default firstBottom = 0
default firstShoe = 0
default firstTop = 0

define mc = Character("[povname]")
define anon = Character("???")
default mc_line = ""

define Felix = Character("Felix", color = "#88b790" )
define Addie = Character("Addison", color = "#92b9d6" )
define Kalvin = Character("Kalvin", color = "#c17779")
define Riya = Character("Riya", color = "#470b1b")

define ra  = Character("RA Olivia", color = "#e6b076")
define Nadia = Character("Nadia", color = "#b5a7df")

#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen MC_Base:
    image "Assets/newMCSprite.png":
        xpos 300
        ypos 0

##############################################################################################################################
# Tops Define -- Tops Define -- Tops Define -- Tops Define -- Tops Define -- Tops Define -- Tops Define
##############################################################################################################################

# -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS
# (1T)-- Regular Top, first dressup
screen top0 zorder 4:
    image "Assets/Top_9.png":
        xpos 300
        ypos 0

# (2T)-- Regular Top, first dressup
screen top1 zorder 4:
    image "Assets/Top_2.png":
        xpos 300
        ypos 0

# (3T)-- Regular Top, first dressup
screen top2 zorder 3:
    image "Assets/Top_3.png":
        xpos 300
        ypos 0

# (4T)-- Regular Top, first dressup
screen top3 zorder 4:
    image "Assets/Top_5.png":
        xpos 300
        ypos 0

# (5T)-- Regular Top, first dressup
screen top4 zorder 4:
    image "Assets/Top_10.png":
        xpos 300
        ypos 0

# (6T)-- Regular Top, first dressup
screen top5 zorder 4:
    image "Assets/Top_11.png":
        xpos 300
        ypos 0

# -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS

# (1T)-- Addie Top 1, second dressup 
screen top6 zorder 2:
    image "Assets/Top_1.png":
        xpos 300
        ypos 0

# (2T)-- Riya Top 1, second dressup
screen top7 zorder 4:
    image "Assets/Top_4.png":
        xpos 300
        ypos 0

# (3T)-- Addie Top 1, second dressup
screen top8 zorder 4:
    image "Assets/Top_6.png":
        xpos 300
        ypos 0

# (4T)-- Riya Top 2, second dressup
screen top9 zorder 4:
    image "Assets/rTop_7.png":
        xpos 300
        ypos 0

# (5T)-- Addie Top 2, second dressup
screen top10 zorder 4:
    image "Assets/aTop_8.png":
        xpos 300
        ypos 0

# (6T)-- Felix Top 2, second dressup
screen top11 zorder 4:
    image "Assets/fTop_12.png":
        xpos 300
        ypos 0

##############################################################################################################################
# Pants Define -- Pants Define -- Pants Define -- Pants Define -- Pants Define -- Pants Define -- Pants Define -- Pants Define
##############################################################################################################################

# -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS
# (1B)-- Regular Bottom, first dressup
screen bottom0 zorder 3:
    image "Assets/Bottom_2.png":
        xpos 300
        ypos 0

# (2B)-- Regular Bottom, first dressup
screen bottom1 zorder 3:
    image "Assets/Bottom_5.png":
        xpos 300
        ypos 0

# (3B)-- Regular Bottom, first dressup
screen bottom2 zorder 3:
    image "Assets/Bottom_8.png":
        xpos 300
        ypos 0

# (4B)-- Regular Bottom, first dressup
screen bottom3 zorder 3:
    image "Assets/Bottom_9.png":
        xpos 300
        ypos 0

# (5B)-- Regular Bottom, first dressup
screen bottom4 zorder 3:
    image "Assets/Bottom_10.png":
        xpos 300
        ypos 0

# (6B)-- Regular Bottom, first dressup
screen bottom5 zorder 3:
    image "Assets/Bottom_13.png":
        xpos 300
        ypos 0

# -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS
# (1B)-- Addison Bottom 1, second dressup
screen bottom6 zorder 3:
    image "Assets/Bottom_1.png":
        xpos 300
        ypos 0

# (2B)-- Felix Bottom 1, first dressup
screen bottom7 zorder 3:
    image "Assets/Bottom_3.png":
        xpos 300
        ypos 0

# (3B)-- Riya Bottom 1, first dressup
screen bottom8 zorder 3:
    image "Assets/Bottom_4.png":
        xpos 300
        ypos 0

# (4B)-- Addison Bottom 2, second dressup
screen bottom9 zorder 3:
    image "Assets/aBottom_7.png":
        xpos 300
        ypos 0

# (5B)-- Riya Bottom 2, second dressup
screen bottom10 zorder 3:
    image "Assets/rBottom_11.png":
        xpos 300
        ypos 0

# (6B)-- Felix Bottom 2, second dressup
screen bottom11 zorder 3:
    image "Assets/fBottom_12.png":
        xpos 300
        ypos 0

##############################################################################################################################
# Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes -- Shoes
##############################################################################################################################

# -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS -- PROLOGUE OUTFITS
# (1S)-- Regular Shoe, first dressup
screen shoe0 zorder 1:
    image "Assets/Shoe_2.png":
        xpos 300
        ypos 0

# (2S)-- Regular Shoe, first dressup
screen shoe1 zorder 1:
    image "Assets/Shoe_3.png":
        xpos 300
        ypos 0

# (3S)-- Regular Shoe, first dressup
screen shoe2 zorder 1:
    image "Assets/Shoe_4.png":
        xpos 300
        ypos 0

# (4S)-- Regular Shoe, first dressup
screen shoe3 zorder 1:
    image "Assets/Shoe_9.png":
        xpos 300
        ypos 0

# (5S)-- Regular Shoe, first dressup
screen shoe4 zorder 1:
    image "Assets/Shoe_10.png":
        xpos 300
        ypos 0

# (10S)-- Regular Shoe, first dressup
screen shoe5 zorder 1:
    image "Assets/Shoe_12.png":
        xpos 300
        ypos 0

# # -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS -- CH1 OUTFITS
# (1S)-- Addison Shoe 1, second dressup
screen shoe6 zorder 1:
    image "Assets/Shoe_1.png":
        xpos 300
        ypos 0

# (2S)-- Felix Shoe 1, second dressup
screen shoe7 zorder 1:
    image "Assets/fShoe_5.png":
        xpos 300
        ypos 0

# (3S)-- Addison Shoe 2, second dressup
screen shoe8 zorder 1:
    image "Assets/aShoe_6.png":
        xpos 300
        ypos 0

# (4S)-- Riya Shoe 1, second dressup
screen shoe9 zorder 1:
    image "Assets/rShoe_7.png":
        xpos 300
        ypos 0

# (5S)-- Riya Shoe 2, second dressup
screen shoe10 zorder 1:
    image "Assets/rShoe_8.png":
        xpos 300
        ypos 0

# (11S)-- Felix Shoe 2, first dressup
screen shoe11 zorder 1:
    image "Assets/fShoe_11.png":
        xpos 300
        ypos 0

#Dress up menu screen
#Start button
screen outfits:
    image "Minigame/startmenu.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.45) action [Play("sound", "mouseclick.mp3"), Show("outfits_ui"), Show("MC_Base"), Show("top0"), Show("bottom0"), Show("shoe0")]
#Minigame

define gui.scrollbar_size = 24

init python:
    #an array of the items the player ownes, these are the unique names of the clothing items, just add an item to the list to give it to the player
    owned_outfits = ["top0", "top1", "top2", "top3", "top4", "top5", "bottom0", "bottom1", "bottom2", "bottom3", "bottom4", "bottom5", "shoe0", "shoe1", "shoe2", "shoe3", "shoe4", "shoe5"]


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
        ("Assets/Top_9_%s.png", "Assets/Top_9_%s.png",    "top",   "top0", 0, -20, 60),
        ("Assets/Bottom_2_%s.png", "Assets/Bottom_2_%s.png", "bottom", "bottom0", 0, -20, 40),
        ("Assets/Shoe_2_%s.png", "Assets/Shoe_2_%s.png",   "shoe",   "shoe0", 0, 0, 200),

        ("Assets/Top_2_%s.png", "Assets/Top_2_%s.png",    "top",   "top1", 1, -20, -40),
        ("Assets/Bottom_5_%s.png", "Assets/Bottom_5_%s.png", "bottom", "bottom1", 1, 0, 50),
        ("Assets/Shoe_3_%s.png", "Assets/Shoe_3_%s.png",   "shoe",   "shoe1", 1, 0, 200),

        ("Assets/Top_3_%s.png", "Assets/Top_3_%s.png",    "top",   "top2", 2, 0, 60),
        ("Assets/Bottom_8_%s.png", "Assets/Bottom_8_%s.png", "bottom", "bottom2", 2, 0, 50),
        ("Assets/Shoe_4_%s.png", "Assets/Shoe_4_%s.png",   "shoe",   "shoe2", 2, 0, 200),

        ("Assets/Top_5_%s.png", "Assets/Top_5_%s.png",    "top",   "top3", 3, 0, 60),
        ("Assets/Bottom_9_%s.png", "Assets/Bottom_9_%s.png", "bottom", "bottom3", 3, 0, 40),
        ("Assets/Shoe_9_%s.png", "Assets/Shoe_9_%s.png",   "shoe",   "shoe3", 3, 0, 100),


        #TEST OUTFITS, these are chapter one outfits that are here to show the scroll bar
        ("Assets/Top_10_%s.png", "Assets/Top_10_%s.png",    "top",   "top4", 4, -20, 30),
        ("Assets/Bottom_10_%s.png", "Assets/Bottom_10_%s.png", "bottom", "bottom4", 4, -20, 40),
        ("Assets/Shoe_10_%s.png", "Assets/Shoe_10_%s.png",   "shoe",   "shoe4", 4,   0, 100),

        ("Assets/Top_11_%s.png", "Assets/Top_11_%s.png",    "top",   "top5", 5, -20, 30),
        ("Assets/Bottom_13_%s.png", "Assets/Bottom_13_%s.png", "bottom", "bottom5", 5, -20, 40),
        ("Assets/Shoe_12_%s.png", "Assets/Shoe_12_%s.png",   "shoe",   "shoe5", 5, 0, 100),

        #("Assets/Top_6_%s.png", "Assets/Top_6_%s.png",    "top",   "top1", 1,     0, 40),
        #("Assets/Bottom_6_%s.png", "Assets/Bottom_6_%s.png", "bottom", "bottom1", 1, 0, 50),
        #("Assets/Shoe_1_%s.png", "Assets/Shoe_1_%s.png",   "shoe",   "shoe1", 1,   0, 100),

        #("Assets/Top_7_%s.png", "Assets/Top_7_%s.png",    "top",   "top2", 2,     10, 60),
        #("Assets/Bottom_7_%s.png", "Assets/Bottom_7_%s.png", "bottom", "bottom2", 2, 0, 50),
        #("Assets/Shoe_3_%s.png", "Assets/Shoe_3_%s.png",   "shoe",   "shoe2", 2,   0, 50),

        #("Assets/Top_8_%s.png", "Assets/Top_8_%s.png",    "top",   "top3", 3,     0, 60),
        #("Assets/Bottom_4_%s.png", "Assets/Bottom_4_%s.png", "bottom", "bottom3", 3, 0, 50),
        #("Assets/Shoe_4_%s.png", "Assets/Shoe_4_%s.png",   "shoe",   "shoe3", 3,   0, 100),
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
    imagebutton auto "Minigame/done_%s.png" align(0.02, 0.97) action [Play("sound", "dressup.mp3"), Jump("instructions")]
    
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
                                    action [tops, Show(showname), SetVariable(Type, setval), SetVariable("firstTop", setval)]
                                if Type == "bottom":
                                    action [bottoms, Show(showname), SetVariable(Type, setval), SetVariable("firstBottom", setval)]
                                if Type == "shoe":
                                    action [shoes, Show(showname), SetVariable(Type, setval), SetVariable("firstShoe", setval)]
                            #else if you don't own it (I.E. its not in its)
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

#define outfit button currently it uses the confirm outfit button art
screen ViewOutfitButton():
    imagebutton:
        auto "Minigame/clothes_%s.png"#image
        align (0.98, 0.02)#Allign to top right
        action [Play("sound", "mouseclick.mp3"),ShowMenu("ViewOutfitMenu")]#show view outfit screen on click

#design view outfit screen
screen ViewOutfitMenu():
    tag menu
    modal True
    image "Backgrounds/classroom bg.jpg"#background image
    add "Player":#show player in the middle
        xpos 0.5
        xanchor 0.5
        ypos 0.0
        yanchor 0.0
    #back button
    imagebutton:
        auto "Minigame/clothes_%s.png"#image
        align (0.98, 0.02)#align to top right
        action Return()#return to game

#This image can be used for the rest of the game, or just as a final reveal.
layeredimage Player:
    always:
        "Assets/newMCSprite.png"

    group shoe:
        attribute 1 default:
            Null()
    if shoe == 0: 
        "Assets/Shoe_2.png"
    if shoe == 1: 
        "Assets/Shoe_3.png"
    if shoe == 2: 
        "Assets/Shoe_4.png"
    if shoe == 3: 
        "Assets/Shoe_9.png"
    if shoe == 4: 
        "Assets/fShoe_10.png"
    if shoe == 5: 
        "Assets/Shoe_12.png"

    group top:
        attribute 8 default:
            Null()
    if top == 0:
        "Assets/Top_9.png"
    if top == 1:
        "Assets/Top_2.png"
    if top == 2:
        "Assets/Top_3.png"
    if top == 3:
        "Assets/Top_5.png"
    if top == 4:
        "Assets/Top_10.png"
    if top == 5:
        "Assets/Top_11.png"
   
    group bottom:
        attribute 4 default:
            Null()
    if bottom == 0:
        "Assets/Bottom_2.png"
    if bottom == 1:
        "Assets/Bottom_5.png"
    if bottom == 2:
        "Assets/Bottom_8.png"
    if bottom == 3:
        "Assets/Bottom_9.png"
    if bottom == 4:
        "Assets/Bottom_10.png"
    if bottom == 5:
        "Assets/Bottom_13.png"

# for looping sounds? 
#init:
#    renpy.music.register_channel("Addie", "sfx", True) # Register a looping "Addie" channel
        
###############################################################
#################### Gameplay: Prologue #######################
###############################################################
label start:
    $quick_menu = False
call screen outfits
label instructions:
    $quick_menu = True
    scene bg with dissolve

    hide screen outfits
    hide screen outfits_ui

    hide screen MC_Base

    #hide screen tops
    hide screen top0
    hide screen top1
    hide screen top2
    hide screen top3
    hide screen top4
    hide screen top5

    #hide sceen bottoms
    hide screen bottom0
    hide screen bottom1
    hide screen bottom2
    hide screen bottom3
    hide screen bottom4
    hide screen bottom5

    #hide screen shoes
    hide screen shoe0
    hide screen shoe1
    hide screen shoe2
    hide screen shoe3
    hide screen shoe4
    hide screen shoe5


    show screen ViewOutfitButton
    show Player:
        xpos 0.38
        ypos 0
    with dissolve

# Ask player for their custom name with clearer instructions
    label ask_name:

    $ povname = ""
    while not povname:
        $ povname = renpy.input(" What is your name? (Type and press Enter)").strip()
        if not povname:
            "Please enter a name before continuing."

    $ povname = povname.capitalize()

    "Nice to meet you, [povname]!"

    scene congratsnew
    with dissolve
    #play music "Test Theme  - Opening the Mail-001.mp3" fadein 1.0 volume 0.5
    play sound "Open_mail_theme.wav" volume 0.5 loop
    #"Congratulations, [povname]!"

    "After reviewing your application, we have decided to offer you admission to Slaycademy Institute of the Arts for the upcoming school year."

    "We believe that your application is a reflection of your effort and dedication to creative endeavors."

    "We believe that you can truly excel at Slaycademy and achieve greatness. Welcome to Slaycademy."

    show Player:
        xpos 0.01
        ypos 0.6
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
        ypos 0.6
    with dissolve
    
    #stop sound fadeout 0.5

    #play sound "Chic_Boutique_General_Theme.wav" volume 0.5 loop
    #play music "podcast-smooth-jazz-instrumental-music-225674.mp3" volume 0.5
    # https://pixabay.com/music/smooth-jazz-podcast-smooth-jazz-instrumental-music-225674/

    # Suprised Face
    "This doesn’t feel real…"

    "One of the most prestigious art schools in the world and I’m here!"

    "Not as a visitor but as a real student!"

    #INSERT OF SCHOOL MAP 
    #map should look confusing and unclear

    scene map temp 
    with fade 

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
    "Alright, one foot in front of the other…"

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
    #COMMON ROUTE CHOICE 1: [museum] [garden] [field] [music studio]
    show dim_bg
    menu:
        # Confused Face
        "…Which way first?"

        "Head over to the museum.":
            stop sound fadeout 0.5
            jump museum
        "Walk to the garden.":
            stop sound fadeout 0.5
            jump garden
        "Go over to the field.":
            stop sound fadeout 0.5
            jump field
        "Check out the music studio.":
            #$ music = True
            stop sound fadeout 0.5
            jump music

    label museum:
        ##play music "felixtheme.mp3" fadein 1.0 volume 0.5
        play sound "Felix_test_audio.wav" volume 0.5 loop
    #BG ART OF SCHOOL MUSEUM
        scene museum 4
        with fade
        show Player:
            xpos 0.01
            ypos 0.07
        with dissolve

        "Where am I!" 
        #🥲

        "I’m totally lost, but…"

        # Suprised Face
        "This place is beautiful so I’m not complaining!"

        "I can’t believe that a school has a building like this."

        "As expected from a top university…"

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
        scene museum 4
        show dim_bg
        show Player:
            xpos 0.01
            ypos 0.6
        with dissolve
        "Wow, these paintings are so cool! Which one should I look at?"
        call screen choice_menu 

label goyascene:
    scene museum 4
    show dim_bg
    show goya:
        ypos 0.05
    with dissolve

        #INSERT OF AN ART PIECE 
        #im referencing this one you can just take the pic and put a pixel filter over bc its public domain now (refer to google doc)
        #"Virgin and Child with Canon van der Paele" Painting by Jan van Eyck

    "({i}Compared to the other one, this painting is so muted!{i})"

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

    #(Felix)
    anon "It’s just that I noticed you seemed lost in thought looking at this piece."

    scene museum 4
    show dim_bg
    hide artguy normal
    hide Player
    show goya
    with fade

    show artguy small:
        xpos 0.72
        ypos 0.25

    #(Felix) Interested Face
    anon "I feel the same way every time I see it."
    hide artguy small

    show Player:
        xpos 0.01
        ypos 0.33

    # Surprised Face
    mc "The world is so mind-bending… I feel like I’m getting sucked into the painting just by looking at it."
    hide Player

    show artguy small:
        xpos 0.72
        ypos 0.3

    #(Felix) Interested Face
    anon "I get what you mean! The artist actually painted this directly on his walls."
    anon "After slowly becoming deaf, he isolated himself in his house to paint these large frescos that are now considered 'The Black Paintings.'"
    anon "It's really quite tragic but it's a very beautiful painting."
    anon "I didn't mean to get dark, but sometimes I just get lost in the painting myself."

    hide goya
    hide art guy small
    scene museum 4
    with fade
    jump artguyscene

label madronescene:
    scene museum 4
    show dim_bg
    show madone painting
    with fade

    "The colors on this are so vibrant!"

    #(Felix)
    anon "It’s amazing, right?"

    # Confused Face
    mc "!"

    hide madone painting
    show Player:
        xpos 0.01
        ypos 0.6
    with dissolve

    show artguy normal
    with dissolve

    show artguy speak
    anon "Sorry! I didn’t mean to startle you."

    anon "It’s just that I noticed you seemed lost in thought looking at this piece."

    scene museum 4
    show dim_bg
    hide artguy normal
    hide Player
    show madone painting
    with fade

    show artguy small:
        xpos 0.72
        ypos 0.3

    anon "I feel the same way every time I see it."
    hide artguy

    show Player:
        xpos 0.01
        ypos 0.33

    mc "The colors are so bright… I feel like I’m getting sucked into the painting just by looking at it."
    hide Player

    show artguy small:
        xpos 0.72
        ypos 0.3

    anon "I get what you mean! The artist actually spent months meticulously making his own paints."
    anon "Back then, oil paints were made with eggs rather than oil, but then this guy came along and had the idea of using oil. So simple yet effective…"

    hide madone painting
    hide art guy small
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

    anon "Ah, I’m a fine arts major. I’m working on a project focusing on just the pieces we have at our campus museum."

    scene museum 4
    show Player:
        xpos 0.01
        ypos 0.6
    show artguy normal

    show artguy speak
            
    anon "I'm sure you're going to get this a ton, but what major are you?"
    anon "Wait, let me guess."
    anon "Are you fashion? I love your style."

    scene museum 4
    show Player:
        xpos 0.01
        ypos 0.6
    show artguy normal
    show dim_bg

menu:
    "Aww thank you. I am a fashion major!":
        $ mc_line = "Aww thank you. I am a fashion major!"
        jump artguychoice

    "Did you automatically assume that I'm in fashion?":
        $ mc_line = "Did you automatically assume that I'm in fashion?"
        jump felixsurprised


label artguychoice:
    scene museum 4
    show Player:
        xpos 0.01
        ypos 0.6
    show artguy normal

    jump felixtalking

label felixsurprised:
    scene museum 4
    show Player:
        xpos 0.01
        ypos 0.6
    show artguy speak

    mc "[mc_line]"

    anon "Ohh I'm sorry... Are you not?"

    mc "Just kidding, I'm just teasing you."

    anon "Oh really now?"

    mc "Yes haha, fashion is totally my thing."
    jump felixtalking2

label felixtalking:

    mc "[mc_line]"

label felixtalking2:
    show artguy speak

    anon "Fashion’s not an easy department to get into. You must be really good!"

    show artguy normal
    mc "I wouldn’t say all that. It’s just hard work."

    show artguy speak

    Felix "Oh—sorry, I just realized I never introduced myself. I’m Felix."

    mc "Haha, no worries. I’m [povname]."

    show artguy normal
    Felix "[povname], huh? That’s a nice name. Fits you."

    show artguy speak
    Felix "I don’t usually see fashion majors in this building. Thinking of switching majors?"

    show artguy normal
    show dim_bg

    menu:
        "More like just totally, utterly lost.":
            $ mc_line = "More like just totally, utterly lost."
            jump felixtalking3

        "I don't know where I'm going..":
            $ mc_line = "I don't know where I'm going.."
            jump felixtalking3
label felixtalking3:
    hide dim_bg
    show artguy speak
    mc "[mc_line]"

    Felix "I gotta say, the campus is nice, but navigating it… Not as great. Where are you headed? Maybe I can point you in the right direction."

    show artguy normal
    mc "I guess freshman dorms? I should check in before exploring around a bit more."

    show artguy speak
    Felix "No wonder why you were so lost! The dorms are always impossible to get to."
    Felix "Bad news is… it’s about a 25 minute walk."

    show artguy normal
    mc "25 minutes?!"

    show artguy speak
    Felix "But wait! The good news is that I can walk you there."

    show artguy normal
    mc "Are you sure? 25 minutes is a long ways away…"

    show artguy speak
    Felix "It’s no problem. Research can wait."

    show artguy normal
    mc "If you’re researching right now, you should focus!"
    mc "Plus if you walked me there, I have a feeling I’d tune out my surroundings and never get the hang of the campus layout. I’ll be fine on my own, just point me in the right direction."

    show artguy speak
    Felix "Alright, alright. Just don’t get too lost and end up back in front of this painting again."

    scene map temp
    Felix "There’s a clear path riiiight here. Here, I’ll highlight it for you so you can’t miss it."

    with dissolve
    scene black bg
    stop sound fadeout 0.5
    with fade
    jump path


label garden:
    #play music "Addie Test Theme 1-002.mp3" fadein 1.0 volume 0.5
    

    #loop text 
    #play Addie "Addie_test_audio.wav"


    #BG ART OF SCHOOL GARDEN
    scene garden bg

    show Player:
        xpos 0.01
        ypos 0.35
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
    #should be kind of far away on the screen

    # Confused Face
    mc "{i}(Is she talking to me?){i}"

    play sound "Addie_test_audio.wav" volume 0.5 loop
    show baddie small:
        xpos 0.75
        ypos 0.35
    with dissolve

    anon "Yes, you! Cutie with the cute fit! You dropped your map!"

    # Surprised Face
    mc "Oh!"

    # RUNNING SOUND EFFECT
    scene garden bg
    with dissolve

    show Player:
        xpos 0.01
        ypos 0.6

    show baddie big
    with dissolve

    mc "Thank you so much! I didn’t even notice that I had dropped it."

    mc "{i}(Wow she’s so pretty… and her outfit is so put-together yet effortless.){/i}"

    show baddie tease
    anon "No probs."

    show baddie happy
    anon "You a freshman?"

    show dim_bg
    menu:
        "Did the map give it away?":
            $ mc_line = "Did the map give it away?"
            jump addiechoiceone
        "Maybe..":
            $ mc_line = "Maybe.."
            jump addiechoiceone

label addiechoiceone:
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie tease

    mc "[mc_line]"

    anon "The lost look in your eyes told me. Don’t worry about it, this school is huge. We’ve all been there."

    mc "{i}(Her gaze is making me a little nervous… It’s like I’m being studied.){/i}"

    show baddie happy
    anon "So where ya headin, babe?"

    mc "I was trying to get to the student dorms, before I lost my map."

    show baddie tease
    anon "Ooh! I lived there last year! So many memories…"

    show baddie happy
    anon "Hey, I don’t have anything going on right now if you want me to take you there?"

    show dim_bg
    menu:
        "No, you really don't have to.":
            $ mc_line = "No, you really don't have to."
            jump notrouble
        "Is it far?":
            $ mc_line = "Is it far?"
            jump notrouble

label notrouble:
    hide dim_bg
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie big

    mc "[mc_line]"
    mc "I don’t want to trouble you too much…"

    show baddie happy
    anon "No, it’s no trouble at all. I can’t leave a cute girl lost in the garden like this!"

    show Player:
        xpos 0.01
        ypos 0.6
    show baddie tease
    with dissolve

    anon "So, what’s your name?"

    mc "[povname]. And you’re…?"

    show baddie happy
    Addie "Addison. But my friends call me Addie!"

    show baddie big
    mc "Gotcha. It’s nice to meet someone so friendly right away. I was really concerned about making friends here, to be honest…"

    show baddie happy
    Addie "No, I get it. I’m not gonna lie, you’re gonna meet some people here that are a little pretentious. It {i}is{/i} Slaycademy, after all."

    show baddie tease
    Addie "..."

    show baddie happy
    Addie "But don’t worry! Most of the people here are really nice. And for a girl as cute as you, you’ll have no problem making friends!"

    show dim_bg
    menu:
        "Haha... thanks!":
            $ mc_line = "Haha... thanks!"
            jump ofcourse
        "You think so?":
            $ mc_line = "You think so?"
            jump ofcourse

label ofcourse:
    hide dim_bg
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie happy
    mc "[mc_line]"
    Addie "Of course!"

    show baddie tease
    Addie "So, what are you here for? Architecture? Film?"

    mc "{i}(Ah—I should’ve dressed a little nicer…){/i}"

    mc "I’m a fashion major!"

    show baddie big
    mc "I usually dress up a little more than this… I didn’t expect to meet anyone until the first day of classes."

    show baddie happy
    Addie "Hey, what are you talking about!? I can tell a fellow fashionista when I see one."

    scene garden bg
    show garden bg with vpunch
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie concerned
    Addie "Umm..."

    mc "What??"

    show baddie disgusted
    Addie "Alright... DON’T freak out, okay..."

    show dim_bg
    menu:
        "What is it?":
            $ mc_line = "What is it?"
            jump bee
        "Oh, don't tell me...":
            $ mc_line = "Oh, don't tell me..."
            jump bee

label bee:
    hide dim_bg
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie scared

    mc "[mc_line]"

    Addie "There—There’s a bee!"

    show dim_bg
    menu:
        "Freak out":
            $ mc_line = "AHHHH GET IT OFF!"
            jump freakout
        "Act calm":
            $ mc_line = "Ah... That's no big deal."
            jump actcalm

label freakout:
    hide dim_bg
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie scared

    mc "[mc_line]"
    mc "???"
    mc "Aren’t you going to help me!?"

    Addie "I'm sorry! I just—ah! This is something I just can't deal with!"

    mc "Oh my gosh! I can feel it crawling on me!"

    Addie "O-okay. Just—just give me one second, okay?"

    show baddie big
    Addie "Got it!"
    show baddie tease
    mc "Oh thank god..."
    mc "Thank you!"
    show baddie happy
    Addie "Of course, babe!"
    show baddie tease
    Addie "It was nothing, really."
    jump flower

label actcalm:
    hide dim_bg
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie concerned

    mc "[mc_line]"

    Addie "How were you so calm??"
    mc "They're harmless as long as you leave them alone!"

    show baddie scared
    Addie "Ugh, I’m just glad that it’s gone!"

    mc "No way... Are you... scared of bees?"

    show baddie concerned
    Addie "How could you not be!?"

    mc "Haha, I didn’t expect you to be so afraid of something so small."
    show baddie happy
    Addie "Well, at least it's been dealt with."

    show baddie tease
    mc "{i}(Oh, she's returned to normal.){/i}"

    label flower:
    hide dim_bg
    scene garden bg
    show Player:
        xpos 0.01
        ypos 0.6
    show baddie tease

    show baddie happy
    Addie "It probably just thought you were a flower! Easy mistake."

    show baddie concerned
    anon "Addison!"

    show baddie scared
    Addie "Shoot!"

    show baddie concerned
    anon "You told me you’d meet me at the quad 20 minutes ago!"

    show baddie happy
    Addie "Sorry babe, I gotta run."

    show baddie big
    Addie "Luckily it’s super easy to get to the dorms from here. Just follow this path to the end, ‘kay?"

    show baddie happy
    mc "Thank you so much! For everything. I’ll see you around then!"

    Addie "See ya!"
    hide baddie with fade

    mc "{i}(Wait a minute… Didn't she say she had nothing to do?){/i}"
    
    #FADE SCENE TO OUTSIDE ON PATH
    scene black bg
    with fade

    stop sound fadeout 1.0

    jump path

label field:

    #define audio.Gymbro = "Gymbro_test_theme_3.mp3"
    #play music Gymbro fadein 1.0 volume 0.5
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
    "AHH-"

    #SHAKE SCREEN EFFECT
    #CraSH NOISE
    show field with hpunch

    # cry face
    mc "Ow!!!"

    #maybe put some sort of screen movement here to indicate that she stood back up after falling

    #KYLE SPRITE
    play sound "Gymbro_test_audio.wav" loop volume 0.5
    show gymbro normal:
        xpos 0.32
        ypos 0.15
    with dissolve

    # yelling face
    #(Kyle)
    anon "Bruh, you’re blocking the field!!!"

    # confused face
    "({i}What the hell, he bumped into me! No apology?{i})"

    # determined face
    mc "If you saw me then you didn’t have to run right into me!"

    # neutral face
    #(Kyle)
    anon "Yah, you’re right, dude! That was on me."

    mc "{i}(What’s with this guy!?){i}"

    #(Kyle)
    anon "So, you here to lift or what?"

    show dim_bg
    menu:
        "No, I don't lift.":
            $ mc_line = "No, I don't lift."
            jump confused

        "Umm. I got lost here.":
            $ mc_line = "Umm. I got lost here."
            jump confused

    label confused:
    hide dim_bg
    mc "[mc_line]"

    #(Kyle)
    anon "That’s a shame, man. We could really use more students in the sports department."

    show dim_bg
    menu:
        "Do you even go here?":
            $ mc_line = "Do you even go here?"
            jump confused3

        "I'm guessing that you're a sports major..":
            $ mc_line = "I'm guessing that you're a sports major.."
            jump confused3

    label confused3:
    hide dim_bg
    mc "[mc_line]"

    anon "Yeah, bro. Can’t you tell I lift? This is art, not athletics."

    mc "I just didn’t know that Slaycademy had a sports department."

    anon "Haha, they don’t!"

    # confused face
    mc "What? Then how are you-"

    anon "Look, man. Rome wasn’t built in a day, alright?"

    anon "You know what they say!"

    # cry face
    mc "No… I don’t…"

    "({i}Please! Someone… Anyone! Get me out of this conversation!){i}"

    Kalvin "Anyways, the name is Kalvin."

    Kalvin "I’ll be attempting a 350 squat today. It’ll be hard, but I think with an audience I’ll be hyped enough to do it."

    Kalvin "Maybe I should practice right now! Tell me how my form is, here-"

    # sweat drop face
    show dim_bg
    menu:
        "Actually, I really should be going.":
            $ mc_line = "Actually, I really should be going." 
            jump kalvintalk

        "Ew stop! I'm leaving now.":
            $ mc_line = "Ew stop! I'm leaving now."
            jump kalvintalk

    label kalvintalk:

    hide dim_bg
     
    mc "[mc_line]"

    Kalvin "Aw man, that’s a shame! We were really vibing!"

    "({i}Were we?{i})"

    # neutral face
    mc "Would you mind pointing me in the direction of the freshman dorms?"

    # cry face
    "({i}Please respond normally!{i})"

    #(Kyle)
    Kalvin "Down near the tennis courts over there, follow the dirt path."

    # sigh face
    "({i}Oh, thank god…{i})"

    #(Kyle)
    Kalvin "Haha, that reminds me of a movie I watched. Follow the yellow brick road!"

    #(Kyle)
    Kalvin "The movie’s super underground. Sorry for the obscure reference!"

    # flat face
    mc "..."

    mc "Yeah… Thanks for the directions."

    #(Kyle)
    Kalvin "No prob, bro. I gotta lock in getting my gains. Good luck finding the cafeteria or wherever you wanted to go!"

    hide gymbro
    with dissolve

    # sweat drop face
    "({i}Did this guy really give me the right directions?{i})"

    scene black bg
    stop sound fadeout 0.5
    with fade

    jump path

label music:
    #play music "Riya Band Practice Theme Test 1.mp3" fadein 1.0 volume 0.5

    play sound "Riya_test_audio.wav" loop volume 0.5
    scene music studio bg
    with fade

    # MUSIC STUDIO SCENE - RIYA INTRODUCTION

    show Player:
        xpos 0.01
        ypos 0.6
    with dissolve

    mc "Whoa…"

    # awe, wide eyes
    mc "I didn’t know this school had a recording studio."

    mc "There’s a band playing right now. It looks like they’re in the middle of a set."

    mc "They’re playing an upbeat rock song. The electric guitar is cutting through the air like a knife, the drums are sending the tempo crashing toward me, the bass is washing over me like waves. And the singer…"

    show riya talking:
        xpos 0.45
        xanchor 0.5
        ypos 1.0
        yanchor 1.0
    
    with dissolve

    # CG of Riya singing into the mic
    # (CG asset should be shown here if available)
    # show cg riya_singing with dissolve

    # Riya CG description for artist reference:
    # Main details: Riya singing into a microphone, playing guitar. This CG can be moved to a later scene (concert date?) if needed.

    "{i}(She’s so cool! She’s clearly the leader of the band. Everyone is looking to her for cues.{i})"

    "{i}(Her voice is clear and controlled. I feel like she’s sharing a piece of her soul with me with every note.{i})"

    "{i}(Her clear tone, and that jet-black hair… She looks a little familiar. Maybe I met her at orientation?{i})"

    "{i}(Oh, they finished. Everyone’s cheering and putting up their instruments. Maybe I should leave before they see me.{i})"

    play music "Riya Tender Moment Test Theme 1.mp3" fadein 1.0 volume 0.5

    anon "Last one to the car is paying for drinks tonight!"

    "({i}The guitarist runs past me, followed by the other two band members.{i})"

    mc "Hey, watch it! They nearly knocked me over."

    show riya judging

    anon "You idiots! I’m going to kill you all if you don’t come back here for your instruments!"

    show riya talking

    anon "Ugh. Hey Mike, thanks for helping us out today. Sorry I forced you to work with these dumbasses."

    "({i}Aha… She’s not as elegant in person as when she’s singing.{i})"

    show riya judging

    anon "Hey, show’s not for free, you know. This is a private practice. How are we supposed to focus on our music when we’ve got fangirls like you barging in every five minutes?"

    "({i}Jeez, I just got lost. But her guttermouth, and those bad manners… I definitely know her from somewhere.{i})"

    show dim_bg
    menu:
        "Sorry, I’m lost. If you just point me in the right direction, I’ll get out of your hair.":
            $ mc_line = "Sorry, I’m lost. If you just point me in the right direction, I’ll get out of your hair." 
            jump riyamemory

        "Fine, I'll just leave then.":
            $ mc_line = "Fine, I'll just leave then."
            jump riyamemory

    label riyamemory:
    hide dim_bg

    mc "[mc_line]"

    show riya smiling

    anon "Oh my god...[povname]!?"

    "({i}Does she know me…?{i})"

    show riya talking

    anon "What the hell are you doing here!? It’s me, Riya!"

    mc "Riya!? Oh my god, it’s been so long!"

    show riya smiling

    "({i}No wonder why she looked familiar! Riya and I were friends in middle school, and she always talked about wanting to start a band. She would practice guitar in front of me for hours, and god, she was so bad! It’s making me laugh just thinking about it.{i})"

    # Hug visual cue could be added here

    show riya normal

    "({i}Riya goes in for a hug and squeezes me tight. When she pulls away and holds me by the shoulders, I feel like we’re back in middle school again.{i})"

    mc "I just got accepted into Slaycademy! I was trying to find the dorms, but I got lost. What are you doing here?"

    show riya smiling

    Riya "Of course you got lost already. I started last year, Music major. I drag my bandmates with me everywhere, and we play shows around here. You’ve gotta come see us sometime!"

    show riya normal

    mc "Wow, that’s so cool. I’d love to! But would you mind helping me find my dorm first? I have no idea where to go."

    show riya talking

    Riya "Don’t worry, I’ve got you. Lemme see your map."

    show dim_bg
    menu:
        "Lean in.":
            jump lean_in
        "Back away a little.":
            jump back_away

label lean_in:
    hide dim_bg
    "({i}So close… She smells like cherries and cigarettes. Her hand is touching mine…{i})"

    show riya smiling

    Riya "See this right here? You made a right instead of a left. Just go straight back and you’ll find it. Even you can’t screw that up."
    jump music_continue

label back_away:
    hide dim_bg
    "({i}I instinctively shift a bit back as she reaches for my map.{i})"
    show riya talking
    Riya "Here, look. You made a right when you should’ve gone left. Just double back and go straight. Even you can’t mess that up."
    jump music_continue

label music_continue:
    "({i}When she moves away, I let out a breath. I didn’t realize I was holding it this whole time.{i})"

    mc "What? Oh, right. Sorry. It’s been a long day."

    show riya talking

    Riya "Oh—my bad, it was a joke. You doing okay?"

    show riya normal

    "({i}Of course it was a joke. Why am I acting so weird? It’s just Riya. It’s just, things feel different for some reason.{i})"

    show riya judging

    mc "Yeah, thanks. Hey, I’ll catch you later, okay? I’m running late for something."

    show riya talking

    Riya "Oh, uh, okay. Hope to see you soon?"

    scene black bg
    stop sound fadeout 1.0
    with fade

    jump path


label path:
    #play music "RAtheme.mp3" fadein 1.0 volume 0.5 
    play sound "Chic_Boutique_General_Theme.wav" volume 0.5 loop
    #FADE TO SCENE OUTSIDE ON PATH

    #atp all choice options should have converged into the same main story where player is on the path outside

    #BG ART OF PATH
    scene transition path
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

    show transition path
    #show white bg
    with fade

    show Player:
        xpos 0.01
        ypos 0.6
    with dissolve

    # distressed face
    "Did-"

    "Did I really make it?"

    # determined face (if artists draw it vaguely enough, it can serve as upset face)
    "Who had the bright idea of building this school on a bunch of hills?!"
    #tbh this is straight out of my experience at korea university bc korea is super mountainous but its like they did no landscaping at all they just plopped the school right on the hills…walked to the dorms ONCE and was so winded and with my iron deficiency i was seeing stars

    # distressed face
    "I need to sit down…"

    #BG ART OF DORMS FRONT DESK
    scene lounge
    with dissolve

    show Player:
        xpos 0.01
        ypos 0.07 
    with dissolve

    "Hah…"
    #😓

    #SOUND AND SCREEN EFFECT TO INDICATE THAT PLAYER IS NOW SITTING

    # determined face (can serve as upset)
    "Big ass school and no way to get up here besides that dirt path-"

    "Judging by how long that took me, I’ll need to wake up before classes like an hour early-"

    # distressed face
    "If I want my outfit to be even a little decent, it’ll need to be earlier."

    "Should I drop out?"

    "Should I do it?"
    show dim_bg

    menu:
        "Stay In":
            hide dim_bg
            "(I guess I could keep going...)"

        "Drop Out":
            stop sound fadeout 0.5
            jump credits


    # concerned face
    hide dim_bg
    anon "Um…"
    stop sound fadeout 0.5
    play sound "RA_test_theme.wav" volume 0.5 loop

    "?"
    show Player with fade:
        xpos 0.01
        ypos 0.6

    #ra SPRITE
    show ra normal with dissolve:
        xpos 0.38
        ypos 0.20

    # distressed face
    anon "Hello, are you a student here?"

    mc "Oh I’m sorry, I should’ve checked in before using the lounge!"

    # neutral face
    anon "No worries! …Did you really walk all that way?"

    show dim_bg
    menu:
        "Yeah, I couldn’t find the main entrance. I think I took the long way around...":
            $ mc_line = "Yeah, I couldn’t find the main entrance. I think I took the long way around..."
            jump rameet

        "Why? Is there another way?":
            $ mc_line = "Why? Is there another way?"
            jump rameet

    label rameet:
    hide dim_bg
    mc "[mc_line]"

    anon "You know we have a shuttle system, right?"

    # surprised face
    mc "Wait, WHAT?!"

    # cry face
    mc "You mean I didn’t have to walk all that way?!"

    anon "Haha don’t worry, you’re not the only one who’s made that mistake. It’s kind of an unofficial freshman tradition."

    anon "This campus is a maze if you don’t have someone to guide you."

    anon "Please, take a seat! You must be winded. I’ll get you checked in."

    ra "I’m Olivia, the RA for this building. Just doing my rounds and saw someone who looked a little lost."

    ra "Could you give me your ID number for check-in?"

    # neutral happy face
    show dim_bg
    menu:
        "My ID number is 14399333.":
            $ mc_line = "My ID number is 14399333."
            jump idcard2

        "Uhhh.. I actually don't know my number.":
            $ mc_line = "Uhhh.. I actually don't know my number."
            jump lostid

    label lostid:
    
    hide dim_bg

    mc  "[mc_line]"

    ra "That's fine! Just tell me your name and your major."

    jump major

    label idcard2:

    hide dim_bg
    
    mc "[mc_line]"

    ra "Okay nice! Can you tell me your name and your major?"

    #INSERT OF ACCESS CARD
    label major:
        
    mc  "My name is [povname] and my major is Fashion."

    ra "Wonderful! You’re all checked in."

    ra "This will give you access to the dorm building and all amenities. The number in the corner is the PIN for your room’s lock."

    #FADE INSERT AWAY

    ra "You’ll be on the second floor in room 143. Your roommate checked in early this morning, so she should be here already."

    mc "Thank you!"

    ra "Oh! And the elevator is in maintenance this week. The stairs are right next to it."

    # cry face
    mc "Thanks…"
    #😭
    stop sound fadeout 0.5


    #BG ART OF DORM HALL
    play sound "Chic_Boutique_General_Theme.wav" volume 0.5 loop
    scene temp hallway
    with fade

    show Player:
        xpos 0.01
        ypos 0.6

    # happy neutral face
    "Even the hallways feel fancy."

    "I wonder what the room w-"

    stop sound fadeout 0.5

    # surprised face
    mc "Ah!"

    #(Nadia)
    anon "AH-"
    show temp hallway with hpunch

    #CraSH EFFECT

    play sound "Nadia_test_theme.wav" volume 0.5 loop

    scene zoe cg

    #CG NADIA ON FLOOR

    #(Nadia)
    anon "Ow ow ow ow ow."

    # distressed face
    show dim_bg
    menu:
        "Are you alright?!":
            $ mc_line = "Are you alright?!"
            jump bestiemeet

        "Hey! Watch where you're going!":
            $ mc_line = "Hey! Watch where you're going!"
            jump bestiemeet

    label bestiemeet: 
    hide dim_bg
    mc "[mc_line]"
    #(Nadia)
    anon "Oh my god! I’m so sorry! I totally wasn’t looking where I was going…"

    anon "Did you get hurt?"

    mc "That was also my bad... Are you hurt? Do you need help getting up?"

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
    anon "Sorry... it's just that I lost a piece of jewelry that’s important to me earlier and the RA just called and told me that someone turned it in."

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
    mc "You should probably go get that jewelry. Seems like it means a lot to you."

    show bsf speak
    Nadia "Ah! The jewelry! I almost forgot…"

    show dim_bg
    menu:
        "You were just talking about it 2 seconds ago...":
            $ mc_line = "You were just talking about it 2 seconds ago...."
            jump forgetten

        "Did you just forget?":
            $ mc_line = "Did you just forget?"
            jump forgetten

    label forgetten:
    hide dim_bg
    mc "[mc_line]"

    show bsf speak
    Nadia "Ahhh sorry I gotta run! I’m sure we’ll see each other around a lot. Let’s hang out sometime!"

    # neutral happy face
    show bsf normal
    mc "Sounds good! It’ll be nice to have a friend in the dorms."

    show bsf speak
    Nadia "Oh, for sure. Maybe I’ll see you at movie night!"
    
    hide bsf with fade
    
    # confused face
    mc "Movie n-"

    # sweat drop face
    "She left…"
    stop sound fadeout 0.5
    
    play sound "Chic_Boutique_General_Theme.wav" volume 0.5 loop
    # neutral happy face

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

    stop music fadeout 3.5
    play sound "doorbell.mp3" volume 2.0

    "I could set up a mannequin here… sewing machine in this corner…"

    #DOOR BEEPING SOUND EFFECT

    # surprised face
    "? (What was that?)"
    


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
    
    #play music "Nadia_Test_Theme_1.mp3" fadein 1.0 volume 0.5 
    stop sound fadeout 0.5
    play sound "Nadia_test_theme.wav" volume 0.5 loop
    Nadia "HAHAHAHAHA"

    show dim_bg
    menu:
        "Did we end up as roomates?":
            $ mc_line = "Did we end up as roomates?"
            jump bestiemeet2

        "You're the jewerly girl!":
            $ mc_line = "You're the jewerly girl!"
            jump bestiemeet2

    label bestiemeet2:
    hide dim_bg
    mc "[mc_line]"

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

    show dim_bg
    menu:
        "No, I gotta unpack first.":
            $ mc_line = "No, I gotta unpack first."
            jump bestiemeet3

        "Seems fun! I'm down to go." :
            $ mc_line = "Seems fun! I'm down to go."
            jump bestiemeet3

    label bestiemeet3:
    hide dim_bg
    mc "[mc_line]"
    show bsf speak
    Nadia "I can also help you unpack!"

    Nadia "There are wayyyy too many boxes. How many clothes do you have?"

    # sweat drop face
    show bsf normal
    mc "A lot… The thrifting addiction is real…"
    
    show bsf speak
    Nadia "I get it. I had to leave tons of boxes at my parents."

    Nadia "Hmm… Well you don’t really wanna unpack now, do you?"

    # sweat drop face
    show bsf normal
    mc "No, but what choice do I have?"
    
    show bsf speak
    $quick_menu = False
    #😭
    jump dress
    with fade
    stop sound fadeout 0.5

return
    