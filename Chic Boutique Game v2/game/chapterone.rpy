###############################################################
######################### Dress Up ############################
###############################################################

# Dress up mini-game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia

#saved outfit for the second outfit choosing scene. They are copies of bottom, shoe, and top where the current outfit is stored
default secondBottom = 0
default secondShoe = 0
default secondTop = 0



#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
screen MC_Base:
    image "Assets/newMCSprite.png":
        xpos 300
        ypos 0

# All the outfit declarations are in the prologue

#Dress up menu screen
#Start button
screen outfits2:
    image "Minigame/startmenu.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.55) action [Show("outfits_ui2"), Show("MC_Base"), Show("top0"), Show("bottom0"), Show("shoe0")]
#Minigame

define gui.scrollbar_size = 24

init python:
    #an array of the items the player ownes, these are the unique names of the clothing items, just add an item to the list to give it to the player
    owned_outfits2 = ["top6", "top7", "top8", "top9", "top10", "top11", "bottom6", "bottom7", "bottom8", "bottom9", "bottom10", "bottom11","shoe6", "shoe7", "shoe8", "shoe9", "shoe10", "shoe11"]


    #these attach the outfits to the love interests (I'm not sure why felix only has one for tops)
    FelixTops = ["top11"]
    RiyaTops = ["top7", "top9"]
    AddieTops = ["top6", "top8", "top10"]

    FelixBottoms = ["bottom7", "bottom11"]
    RiyaBottoms = ["bottom8", "bottom10"]
    AddieBottoms = ["bottom6", "bottom9"]

    FelixShoes = ["shoe7", "shoe11"]
    RiyaShoes = ["shoe9", "shoe10"]
    AddieShoes = ["shoe6", "shoe8"]


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
    outfit_buttons2 = [ #outfit buttons (path of normal clothing, path of lock clothing image, type (top, bottom, shoe), showname, item id number (saved clothing item number), offsetx, offsety)
        #prologue outfits
        ("Assets/Top_1_%s.png", "Assets/Top_1_%s.png",    "top",   "top6", 0, -40, 0),
        ("Assets/Bottom_1_%s.png", "Assets/Bottom_1_%s.png", "bottom", "bottom6", 0, -20, 40),
        ("Assets/Shoe_1_%s.png", "Assets/Shoe_1_%s.png",   "shoe",   "shoe6", 0, 0, 200),

        ("Assets/Top_4_%s.png", "Assets/Top_4_%s.png",    "top",   "top7", 1, -20, -40),
        ("Assets/Bottom_3_%s.png", "Assets/Bottom_3_%s.png", "bottom", "bottom7", 1, 0, 50),
        ("Assets/fShoe_5_%s.png", "Assets/fShoe_5_%s.png",   "shoe",   "shoe7", 1, 0, 200),

        ("Assets/Top_6_%s.png", "Assets/Top_6_%s.png",    "top",   "top8", 2, 0, 60),
        ("Assets/Bottom_4_%s.png", "Assets/Bottom_4_%s.png", "bottom", "bottom8", 2, 0, 50),
        ("Assets/aShoe_6_%s.png", "Assets/aShoe_6_%s.png",   "shoe",   "shoe8", 2, 0, 200),

        ("Assets/rTop_7_%s.png", "Assets/rTop_7_%s.png",    "top",   "top9", 3, 0, 60),
        ("Assets/aBottom_7_%s.png", "Assets/aBottom_7_%s.png", "bottom", "bottom9", 3, 0, 50),
        ("Assets/rShoe_7_%s.png", "Assets/rShoe_7_%s.png",   "shoe",   "shoe9", 3, 0, 200),


        #TEST OUTFITS, these are chapter one outfits that are here to show the scroll bar
        ("Assets/aTop_8_%s.png", "Assets/aTop_8_%s.png",    "top",   "top10", 4,     -20, 30),
        ("Assets/rBottom_11_%s.png", "Assets/rBottom_11_%s.png", "bottom", "bottom10", 4, -20, 40),
        ("Assets/rShoe_8_%s.png", "Assets/rShoe_8_%s.png",   "shoe",   "shoe10", 4,   0, 200),

        ("Assets/fTop_12_%s.png", "Assets/fTop_12_%s.png",    "top",   "top11", 5,     0, 40),
        ("Assets/fBottom_12_%s.png", "Assets/fBottom_12_%s.png", "bottom", "bottom11", 5, 0, 50),
        ("Assets/fShoe_11_%s.png", "Assets/fShoe_11_%s.png",   "shoe",   "shoe11", 5,   0, 100),

        #("Assets/Top_7_%s.png", "Assets/Top_7_%s.png",    "top",   "top2", 2,     10, 60),
        #("Assets/Bottom_7_%s.png", "Assets/Bottom_7_%s.png", "bottom", "bottom2", 2, 0, 50),
        #("Assets/Shoe_3_%s.png", "Assets/Shoe_3_%s.png",   "shoe",   "shoe2", 2,   0, 50),

        #("Assets/Top_8_%s.png", "Assets/Top_8_%s.png",    "top",   "top3", 3,     0, 60),
        #("Assets/Bottom_4_%s.png", "Assets/Bottom_4_%s.png", "bottom", "bottom3", 3, 0, 50),
        #("Assets/Shoe_4_%s.png", "Assets/Shoe_4_%s.png",   "shoe",   "shoe3", 3,   0, 100),
        #TEST OUTFITS, these are chapter one outfits that are here to show the scroll bar
    ]

    #figures out what the main love interest of an outfit is
    def getOutfitLoveInterest():
        #variables for the number of each lov interests items you have
        FelixCount = 0
        RiyaCount = 0
        AddieCount = 0
        #a variable for breaking ties
        default = "Felix"
        #loop through outfit buttons
        for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons2):
            #if button data is a top, check if felix, riya, or addie own it and add to their counts if they do
            if Type == "top" and top == setval:
                if showname in FelixTops:
                    FelixCount += 1
                    default = "Felix"
                if showname in RiyaTops:
                    RiyaCount += 1
                    default = "Riya"
                if showname in AddieTops:
                    AddieCount += 1
                    default = "Addie"
            #if button data is a bottom, check if felix, riya, or addie own it and add to their counts if they do
            if Type == "bottom" and bottom == setval:
                if showname in FelixBottoms:
                    FelixCount += 1
                if showname in RiyaBottoms:
                    RiyaCount += 1
                if showname in AddieBottoms:
                    AddieCount += 1
            #if button data is a shoe, check if felix, riya, or addie own it and add to their counts if they do
            if Type == "shoe" and shoe == setval:
                if showname in FelixShoes:
                    FelixCount += 1
                if showname in RiyaShoes:
                    RiyaCount += 1
                if showname in AddieShoes:
                    AddieCount += 1
        #dfebug log counts (use shift O to see this)
        print("FelixCount is", FelixCount, "   RiyaCount is", RiyaCount, "   AddieCount is", AddieCount)
        #check who had the majority of the items, breaking the tie with the default variable. the value returned is the label to jump to
        if FelixCount >= 2 or default == "Felix":
            return "felixMovie"
        if RiyaCount >= 2 or default == "Riya":
            return "riyaMovie"
        if AddieCount >= 2 or default == "Addie":
            return "addieMovie"



    #these three arrays automatically fill themselfs with Hide() functions for every item of their respective types. when you press a button it uses these to first hide all items of that type on the character before showing the specific one clicked
    tops2 = []
    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons2):
        if Type == "top":
            tops2.append(Hide(showname))
    bottoms2 = []
    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons2):
        if Type == "bottom":
            bottoms2.append(Hide(showname))
    shoes2 = []
    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons2):
        if Type == "shoe":
            shoes2.append(Hide(showname))

screen outfits_ui2:
    image "Backgrounds/temp dorm.png"
    image "Minigame/ui_base.png" align(1.1, 1.0) size (1300, 1100)
    imagebutton auto "Minigame/done_%s.png" align(0.02, 0.95) action [Play("sound", "dressup.mp3"), Jump("instructions2")]
    on "show" action [Show("MC_Base")]

    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons2):
        if Type == "top" and top == setval:
            on "show" action [tops2, Show(showname)]
        if Type == "bottom" and bottom == setval:
            on "show" action [bottoms2, Show(showname)]
        if Type == "shoe" and shoe == setval:
            on "show" action [shoes2, Show(showname)]
    #on "show" action [tops2,Show(showname)]

    #on "hide" action Hide("MC_Base")

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
                    #y size of the clothing item grid (not really necesary, just use outfit offsets in the outfit_buttons2 array) this is the interier size of the scrolling space
                    ysize 900

                    #loop through clothing buttons
                    for i, (imagepath, imagepathmissing, Type, showname, setval, Xoffset, Yoffset) in enumerate(outfit_buttons2):
                        imagebutton:
                            #if you own an item (I.E. its in owned_outfits)
                            if showname in owned_outfits2:
                                #set inage to the normal clothing image
                                auto imagepath
                                #set the items position on the grid
                                pos (x_start + Xoffset + (i // 3) * x_spacing, y_start + Yoffset + (i % 3) * y_spacing)

                                #set up action to set clothing when pressed. for each option it hides all items of that type and then shows the specific one you clicked
                                if Type == "top":
                                    action [tops2, Show(showname), SetVariable(Type, setval), SetVariable("secondTop", setval)]
                                if Type == "bottom":
                                    action [bottoms2, Show(showname), SetVariable(Type, setval), SetVariable("secondBottom", setval)]
                                if Type == "shoe":
                                    action [shoes2, Show(showname), SetVariable(Type, setval), SetVariable("secondShoe", setval)]
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
layeredimage Player2:
    always:
        "Assets/newMCSprite.png"

    group shoe:
        attribute 0 default:
            Null()
    if shoe == 0:
        "Assets/Shoe_1.png"
    if shoe == 1:
        "Assets/fShoe_5.png"
    if shoe == 2:
        "Assets/aShoe_6.png"
    if shoe == 3:
        "Assets/rShoe_7.png"
    if shoe == 4:
        "Assets/rShoe_8.png"
    if shoe == 5: 
        "Assets/fShoe_11.png"

    group top:
        attribute 0 default:
            Null()
    if top == 0:
        "Assets/Top_1.png"
    if top == 1:
        "Assets/Top_4.png"
    if top == 2:
        "Assets/Top_6.png"
    if top == 3:
        "Assets/rTop_7.png"
    if top == 4:
        "Assets/aTop_8.png"
    if top == 5:
        "Assets/fTop_12.png"

    group bottom:
        attribute 0 default:
            Null()
    if bottom == 0:
        "Assets/Bottom_1.png"
    if bottom == 1:
        "Assets/Bottom_3.png"
    if bottom == 2:
        "Assets/Bottom_4.png"
    if bottom == 3:
        "Assets/aBottom_7.png"
    if bottom == 4:
        "Assets/rBottom_11.png"
    if bottom == 5:
        "Assets/fBottom_12.png"

###############################################################
#################### Gameplay: Chapter 1 ######################
###############################################################

# PROMPT DRESS UP CHOICE
label dress:
    #### test 

# hide screen tops 
    hide screen top0
    hide screen top1
    hide screen top2
    hide screen top3
    hide screen top4
    hide screen top5

    hide screen top6
    hide screen top7
    hide screen top8
    hide screen top9
    hide screen top10
    hide screen top11

    # hide screen bottoms
    hide screen bottom0
    hide screen bottom1
    hide screen bottom2
    hide screen bottom3
    hide screen bottom4
    hide screen bottom5

    hide screen bottom6
    hide screen bottom7
    hide screen bottom8
    hide screen bottom9
    hide screen bottom10
    hide screen bottom11

    #hide screen shoes
    hide screen shoe0
    hide screen shoe1
    hide screen shoe2
    hide screen shoe3
    hide screen shoe4
    hide screen shoe5

    hide screen shoe6
    hide screen shoe7
    hide screen shoe8
    hide screen shoe9
    hide screen shoe10
    hide screen shoe11

    #### test 

    #hide screen top0
    #hide screen top1
    #hide screen top2
    #hide screen top3
    #hide screen top4
    #hide screen top5

    # hide screen bottoms
    # hide screen bottom0
    # hide screen bottom1
    # hide screen bottom2
    # hide screen bottom3
    # hide screen bottom4
    # hide screen bottom5

    #hide screen shoes
    # hide screen shoe0
    # hide screen shoe1
    # hide screen shoe2
    # hide screen shoe3
    # hide screen shoe4
    # hide screen shoe5

    hide Player
    show bsf speak
    Nadia "Just borrow something from my closet."

    Nadia "Something casual, nothing too fancy!"
    call screen outfits_ui2

label instructions2:
    $quick_menu = True
    #instantly set scene so fade below works (without this the fade would start from the bedroom)
    scene bg
    with None

    hide screen outfits2
    hide screen outfits_ui2

    hide screen MC_Base

    # hide screen tops 
    hide screen top0
    hide screen top1
    hide screen top2
    hide screen top3
    hide screen top4
    hide screen top5

    hide screen top6
    hide screen top7
    hide screen top8
    hide screen top9
    hide screen top10
    hide screen top11

    # hide screen bottoms
    hide screen bottom0
    hide screen bottom1
    hide screen bottom2
    hide screen bottom3
    hide screen bottom4
    hide screen bottom5

    hide screen bottom6
    hide screen bottom7
    hide screen bottom8
    hide screen bottom9
    hide screen bottom10
    hide screen bottom11

    #hide screen shoes
    hide screen shoe0
    hide screen shoe1
    hide screen shoe2
    hide screen shoe3
    hide screen shoe4
    hide screen shoe5

    hide screen shoe6
    hide screen shoe7
    hide screen shoe8
    hide screen shoe9
    hide screen shoe10
    hide screen shoe11

    show screen ViewOutfitButton
    show Player2:
        xpos 0.38
        ypos 0
    #fade out outfit screen and in the results screen
    with fade

    #pause for 2 seconds because no input to pause like in prologue
    pause 2

label end_scene:
    hide screen outfits2
    hide screen outfits_ui2

    hide screen MC_Base

    # hide screen tops 
    hide screen top0
    hide screen top1
    hide screen top2
    hide screen top3
    hide screen top4
    hide screen top5

    hide screen top6
    hide screen top7
    hide screen top8
    hide screen top9
    hide screen top10
    hide screen top11


    # hide screen bottoms
    hide screen bottom0
    hide screen bottom1
    hide screen bottom2
    hide screen bottom3
    hide screen bottom4
    hide screen bottom5

    hide screen bottom6
    hide screen bottom7
    hide screen bottom8
    hide screen bottom9
    hide screen bottom10
    hide screen bottom11

    #hide screen shoes
    hide screen shoe0
    hide screen shoe1
    hide screen shoe2
    hide screen shoe3
    hide screen shoe4
    hide screen shoe5

    hide screen bottom6
    hide screen bottom7
    hide screen bottom8
    hide screen bottom9
    hide screen bottom10
    hide screen bottom11


    scene temp dorm

    #show Player2:
        #xpos 0.01
        #ypos 0.1
    with fade 

    show bsf speak
    hide Player2
    Nadia "Oh my gosh, you look better in those clothes than me!"


#Test Code: this resets the current outfit to the first one choosen
    # $top = firstTop
    # $bottom = firstBottom
    # $shoe = firstShoe
#Test Code



    Nadia "Okay, let's get going now."

    #jump to the label of the love interest the outfit is primarily made of
    jump expression getOutfitLoveInterest()
    hide bsf normal
    show black bg
    with fade
