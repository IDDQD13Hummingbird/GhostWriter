# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters!

define tp = Character("Typewriter Ghost", color="#819494") 

define l = Character("Lafcadio", color="#4480e4") 

define w = Character("Willow", color="#6e25c0")
define t = Character("Tequila", color="#3a8fd0")
define g = Character("Greyson", color="#308840")
define redd = Character("Redd", color="#B063F8")
define reggie = Character("Reggie", color="#C86509")
define thanos = Character("Thanos", color="#3038d4")

# Variables!

default cps = 25

transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0


transform left:
    xalign 0.15
    yalign 1.0
transform right:
    xalign 0.85
    yalign 1.0

transform centre:
    xalign 0.5
    yalign 1.0

# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "lafcadio happy.png" to the images
    # directory.

    "Do you need a demo/tutorial?"

    
# Variables!
    $ TYPEWRITER_MESSAGE = "Th e qu ee  da c es, and so shall you"

    menu:

        "Yes":
            jump tutorial_yes
        "No":
            jump tutorial_no

    label tutorial_yes:

        show lafcadio happy at slightleft

        # These display lines of dialogue.

        l "You've created a new Ren'Py game."

        l "Once you add a story, pictures, and music, you can release it to the world!"

        l "Do you like visual novels with choices?"

        menu:

            "Yes, I do.":
                jump choice1_yes

            "No, I don't.":
                jump choice1_no

        label choice1_yes:

            $ menu_flag = True

            "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

            jump choice1_done

        label choice1_no:

            $ menu_flag = False

            "Games without menus are called kinetic novels, and there are dozens of them available to play."

            jump choice1_done

        label choice1_done:

            # ... the game continues here.


        l "For example, we might want to have text that is {b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, or {u}underlined{/u}."
        
        l "The size tag changes the size of text. It can make text {size=+10}bigger{/size} or {size=-10}smaller{/size}, or set it to a {size=30}fixed size{/size}."
 
        l "The cps text tag {cps=25}makes text type itself out slowly{/cps}, even if slow text is off."

        l "The cps tag can also be relative to the default speed, {cps=*2}doubling{/cps} or {cps=*0.5}halving{/cps} it."

        l "The k tag changes kerning. It can space the letters of a word {k=-.5}closer together{/k} or {k=.5}farther apart{/k}."

        l "The p tag breaks a paragraph,{p}and waits for the player to click."

        l "If it is given a number as an argument,{p=1.5}it waits that many seconds."
 
        l "The w tag also waits for a click,{w} except it doesn't break lines,{w=.5} the way p does."

        l "To break a line without pausing,\none can write \\n. \\' and \\\" include quotes in the text."
    
        $ variable = "{i}variable value{/i}"

        l "For example, this displays the [variable]."
 
        l "When the variable name is followed by !q, special characters are quoted. This displays the raw [variable!q], including the italics tags."
 
        $ translatable = _("translatable text")

        l "When the variable name is followed by !t, it is translated to [variable!t]. It could be something else in a different language."
 
        l "Finally, certain characters are special. [[, {{, and \\ need to be doubled if included in text. The %% character should be doubled if used in dialogue."
 
 

        hide lafcadio
        l "Tutorial done."
        jump tutorial_no

    
    label tutorial_no:
        "{size=55}THIS IS A TECH DEMO PUZZLE. \nDO NOT INCLUDE IN THE FINAL GAME.{/size}"

        menu:
            "Padlock Puzzle":
                jump padlock_start

            "Woodwind Poem":
                jump woodwind_start

    #Select 
    label end:
        "This concludes the tech demo."

    # This ends the game.

    return
