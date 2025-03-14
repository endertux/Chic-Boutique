###############################################################
######################### Dress Up ############################
###############################################################

# dress up mini game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia


#This is where we create a separate screen for each article of clothing, as well as the character base. Make sure they're all aligned!
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
    image "Minigame/bg.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.40) action [Show("outfits_ui2"), Show("Body_Base"), Show("underwear1"), Show("underwear2")]

#Minigame
screen outfits_ui2:
    image "Backgrounds/temp dorm.png" 
    image "Minigame/ui_base.png" align(1.1, 1.0) size (1300, 1100) 

    imagebutton auto "Minigame/done_%s.png" align(0.02, 0.95) action Jump("instructions2") 

# Tops
    imagebutton auto "Assets/Top_5_%s.png" align(0.50, 0.28) action [Show("top5"), Hide("underwear2"), Hide("top6"), Hide("top7"), Hide("top8"), SetVariable("top", 5)]
    imagebutton auto "Assets/Top_6_%s.png" align(0.64, 0.28) action [Show("top6"), Hide("underwear2"), Hide("top5"), Hide("top7"), Hide("top8"), SetVariable("top", 6)]
    imagebutton auto "Assets/Top_7_%s.png" align(0.78, 0.28) action [Show("top7"), Hide("underwear2"), Hide("top5"), Hide("top6"), Hide("top8"), SetVariable("top", 7)]
    imagebutton auto "Assets/Top_8_%s.png" align(0.923, 0.28) action [Show("top8"), Hide("underwear2"), Hide("top5"), Hide("top6"), Hide("top7"), SetVariable("top", 8)]

# Bottoms
    imagebutton auto "Assets/Bottom_5_%s.png" align(0.51, 0.56) action [Show("bottom5"), Hide("underwear1"), Hide("bottom6"), Hide("bottom7"), Hide("bottom8"), SetVariable("bottom", 5)]
    imagebutton auto "Assets/Bottom_6_%s.png" align(0.645, 0.55) action [Show("bottom6"), Hide("underwear1"), Hide("bottom5"), Hide("bottom7"), Hide("bottom8"), SetVariable("bottom", 6)]
    imagebutton auto "Assets/Bottom_7_%s.png" align(0.78, 0.46) action [Show("bottom7"), Hide("underwear1"), Hide("bottom5"), Hide("bottom6"), Hide("bottom8"), SetVariable("bottom", 7)]
    imagebutton auto "Assets/Bottom_4_%s.png" align(0.935, 0.55) action [Show("bottom8"), Hide("underwear1"), Hide("bottom5"), Hide("bottom6"), Hide("bottom7"), SetVariable("bottom", 8)]

# Shoes (Placed underneath bottoms)
    imagebutton auto "Assets/Shoe_5_%s.png" align(0.51, 0.85) action [Show("shoe5"), Hide("shoe6"), Hide("shoe7"), Hide("shoe8"), SetVariable("shoe", 5)]
    imagebutton auto "Assets/Shoe_1_%s.png" align(0.635, 0.87) action [Show("shoe6"), Hide("shoe5"), Hide("shoe7"), Hide("shoe8"), SetVariable("shoe", 6)]
    imagebutton auto "Assets/Shoe_3_%s.png" align(0.77, 0.83) action [Show("shoe7"), Hide("shoe5"), Hide("shoe6"), Hide("sho8"), SetVariable("shoe", 7)]
    imagebutton auto "Assets/Shoe_4_%s.png" align(0.93, 0.86) action [Show("shoe8"), Hide("shoe5"), Hide("shoe6"), Hide("shoe7"), SetVariable("shoe", 8)]



#This image can be used for the rest of the game, or just as a final reveal.
layeredimage Player:
    always:
        "Assets/Body.Base.png"

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

###############################################################
#################### Gameplay: Chapter 1 ######################
###############################################################
#PROMPT DRESS UP CHOICE
label dress:

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

    scene bg
    show Player:
        xpos 0.38
        ypos 0
    with dissolve
    Nadia "Perfect! That works just fine!"

    scene black bg
    "End of Prototype"

    # This ends the game.

    return