###############################################################
######################### Dress Up ############################
###############################################################

# Dress up mini-game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia

# This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen Body_Base:
    image "Assets/Body.Base.png":
        xpos 300
        ypos 0

screen underwear1:
    image "Assets/Underwear_1.PNG":
        xpos 300
        ypos 0

screen underwear2:
    image "Assets/Underwear_2.PNG":
        xpos 300
        ypos 0

# Tops Define
screen top5 zorder 3:
    image "Assets/Top_5.png":
        xpos 300
        ypos 0

screen top6 zorder 3:
    image "Assets/Top_6.png":
        xpos 300
        ypos 0

screen top7 zorder 3:
    image "Assets/Top_7.png":
        xpos 300
        ypos 0

screen top8 zorder 3:
    image "Assets/Top_8.png":
        xpos 300
        ypos 0

# Pants Define
screen bottom5 zorder 2:
    image "Assets/Bottom_5.png":
        xpos 300
        ypos 0

screen bottom6 zorder 2:
    image "Assets/Bottom_6.png":
        xpos 300
        ypos 0

screen bottom7 zorder 2:
    image "Assets/Bottom_7.png":
        xpos 300
        ypos 0

screen bottom8 zorder 2:
    image "Assets/Bottom_4.png":
        xpos 300
        ypos 0

# Shoes
screen shoe5 zorder 1:
    image "Assets/Shoe_5.PNG":
        xpos 300
        ypos 0

screen shoe6 zorder 1:
    image "Assets/Shoe_1.png":
        xpos 300
        ypos 0

screen shoe7 zorder 1:
    image "Assets/Shoe_3.png":
        xpos 300
        ypos 0

screen shoe8 zorder 1:
    image "Assets/Shoe_4.png":
        xpos 300
        ypos 0

#Dress up menu screen
#Start button
screen outfits2:
    image "Minigame/startmenu.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.55) action [Show("outfits_ui"), Show("Body_Base"), Show("top0"), Show("bottom0")]
#Minigame


init python:

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
        #chapter one outfits
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

screen outfits_ui2:
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

# This image can be used for the rest of the game, or just as a final reveal.
layeredimage Player:
    always:
        "Assets/Body.Base.png"

    group top:
        attribute 0 default:
            Null()
    if top == 5:
        "Assets/Top_5.png"
    if top == 6:
        "Assets/Top_6.png"
    if top == 7:
        "Assets/Top_7.png"
    if top == 8:
        "Assets/Top_8.png"

    group bottom:
        attribute 0 default:
            Null()
    if bottom == 5:
        "Assets/Bottom_5.png"
    if bottom == 6:
        "Assets/Bottom_6.png"
    if bottom == 7:
        "Assets/Bottom_7.png"
    if bottom == 3:
        "Assets/Bottom_4.png"

    group shoe:
        attribute 0 default:
            Null()
    if shoe == 5: 
        "Assets/Shoe_5.png"
    if shoe == 6: 
        "Assets/Shoe_1.png"
    if shoe == 7: 
        "Assets/Shoe_3.png"
    if shoe == 8: 
        "Assets/Shoe_4.png"

###############################################################
#################### Gameplay: Chapter 1 ######################
###############################################################

# PROMPT DRESS UP CHOICE
label dress:

    show bsf speak
    Nadia "Just borrow something from my closet."

    Nadia "Something casual, nothing too fancy!"

    call screen outfits2

label instructions2:
    hide screen outfits2
    hide screen outfits_ui2
    hide screen Body_Base
    hide screen top5
    hide screen top6
    hide screen top7
    hide screen top8
    hide screen bottom5
    hide screen bottom6
    hide screen bottom7
    hide screen bottom8
    hide screen shoe5
    hide screen shoe6
    hide screen shoe7
    hide screen shoe8
    hide underwear1
    hide underwear2

    scene bg
    show Player:
        xpos 0.38
        ypos 0
    with dissolve

label end_scene:
    hide screen outfits2
    hide screen outfits_ui2
    hide screen Body_Base
    hide screen top5
    hide screen top6
    hide screen top7
    hide screen top8
    hide screen bottom5
    hide screen bottom6
    hide screen bottom7
    hide screen bottom8
    hide screen shoe5
    hide screen shoe6
    hide screen shoe7
    hide screen shoe8
    scene temp dorm
    with fade 

    show bsf speak
    Nadia "Oh my gosh, you look better in those clothes than me!"

    Nadia "Okay, let's get going now."

    show black bg
    with fade

    "End Prototype"
    return
