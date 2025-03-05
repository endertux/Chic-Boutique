###############################################################
######################### Dress Up ############################
###############################################################

# dress up mini game by dicortesia --> https://www.youtube.com/watch?v=oZU0CmyuZHE&ab_channel=dicortesia


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
screen outfits2:
    image "Minigame/bg.png"
    imagebutton auto "Minigame/start_%s.png" align(0.5, 0.40) action [Show("outfits_ui2"), Show("Dana_Sprite"), Show("top0"), Show("bottom0")]

#Minigame
screen outfits_ui2:
    image "Minigame/bg.png"
    image "Minigame/ui_base.png" align(1.1, 1.0) size (1300, 1100) 

    imagebutton auto "Minigame/done_%s.png" align(0.02, 0.05) action Jump("instructions2")

#Tops
    imagebutton auto "Dana_Imgs/Dana_Top_1_%s.png" align(0.50, 0.22) action [Show("top0"), Hide("top1"), Hide("top2"), SetVariable("top", 0)]
    imagebutton auto "Dana_Imgs/Dana_Top_2_%s.png" align(0.66, 0.33) action [Show("top1"), Hide("top0"), Hide("top2"), SetVariable("top", 1)]
    imagebutton auto "Dana_Imgs/Dana_Top_3_%s.png" align(0.78, 0.24) action [Show("top2"), Hide("top0"), Hide("top1"), SetVariable("top", 2)]

#Bottoms
    imagebutton auto "Dana_Imgs/Dana_Bottom_1_%s.png" align(0.51, 0.60) action [Show("bottom0"), Hide("bottom1"), Hide("bottom2"), SetVariable("bottom", 0)]
    imagebutton auto "Dana_Imgs/Dana_Bottom_2_%s.png" align(0.64, 0.60) action [Show("bottom1"), Hide("bottom0"), Hide("bottom2"), SetVariable("bottom", 1)]
    imagebutton auto "Dana_Imgs/Dana_Bottom_3_%s.png" align(0.79, 0.60) action [Show("bottom2"), Hide("bottom0"), Hide("bottom1"), SetVariable("bottom", 2)]

#Shoes
    imagebutton auto "Dana_Imgs/Dana_Shoe_1_%s.png" align(0.50, 0.90) action [Show("shoe1"), Hide("shoe2"), Hide("shoe3"),SetVariable("shoe", 0)]
    imagebutton auto "Dana_Imgs/Dana_Shoe_2_%s.png" align(0.64, 0.90) action [Show("shoe2"), Hide("shoe1"), Hide("shoe3"),SetVariable("shoe", 1)]
    imagebutton auto "Dana_Imgs/Dana_Shoe_3_%s.png" align(0.79, 0.88) action [Show("shoe3"), Hide("shoe1"), Hide("shoe2"),SetVariable("shoe", 2)]


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
#################### Gameplay: Chapter 1 ######################
###############################################################
#PROMPT DRESS UP CHOICE
label dress:

    Nadia "Just borrow something from my closet."

    Nadia "Something casual, nothing too fancy!"

    call screen outfits2

label instructions2:
    scene bg with dissolve

    hide screen outfits2
    hide screen outfits_ui2

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

    Nadia "Wow! Looking real good [povname]!"

    scene black bg
    "End of Prototype"

    # This ends the game.

    return