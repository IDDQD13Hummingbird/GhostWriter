# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Characters!

define tp = Character("Typewriter Ghost", color="#819494") 

define l = Character("Lafcadio", color="#4480e4") 

define w = Character("Willow", color="#6e25c0")
define t = Character("Tequila", color="#3a8fd0")
define g = Character("Greyson", color="#308840")


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
        
        $ attempts = 5 # I can't figure out where to initialize the variable so that the program remembers and recognizes it.
        jump typewriter_default
        
    label typewriter_default:
    
            show typewriter at centre
            tp "{cps=25}Th e qu ee  da c es, and so shall you{/cps}"
            $ TYPEWRITER_MESSAGE = "Th e qu ee  da c es, and so shall you"
            jump typewriter_menu

    label typewriter_clarified:
        
            show typewriter at centre
            tp "{cps=25}Sw eed sh f emal e royalty. Four l ett ers. Four umb ers.{/cps}"
            $ TYPEWRITER_MESSAGE = "Th e qu ee  da c es, and so shall you\nSw eed sh f emal e royalty. Four l ett ers. Four umb ers."
            jump typewriter_menu

    label typewriter_menu:
            menu:
                "The typewriter says : [TYPEWRITER_MESSAGE]"
                "Clarify what the ghost meant.":
                    jump typewriter_ghost
                "Dancing? Queen? What is it on about? Tequila!":
                    jump typewriter_tequila
                "How am I supposed to give an answer on a padlock?...":
                    jump typewriter_grayson
                "Alright, I think I get it!":
                    jump typewriter_give_answer

               # Ask ghost to clarify
    label typewriter_ghost:
           show lafcadio happy at centre
           l "Clarify."
           hide Lafcadio
           jump typewriter_clarified
              

               #Ask Tequila about it
    label typewriter_tequila:
           show lafcadio happy at centre
           l "What is it referencing?"
           hide Lafcadio
           show tequila at left
           t "You are the dancing queen~{p}Young and sweet, only seventeen~"
           t "It's from ABBA, isn't it?"
           hide tequila
           jump typewriter_menu

               #Ask Greyson about it
    label typewriter_grayson:
           show lafcadio happy at centre
           l "I don't get what it's expecting from me."
           hide Lafcadio
           show grayson at right
           g "Hm... {w=.2}Actually!" 
           g "You know how they abstract All Cops Are Bastards down to 1312? \nI think that's what they were going for!"
           g "Numbers are letter's position in the alphabet, I mean. \nNot ACAB. Of course not."
           hide grayson
           jump typewriter_menu

    label typewriter_give_answer:
        "You see a padlock. You need to put in four numbers."
        $ padlock_1 = "0"
        $ padlock_2 = "0"
        $ padlock_3 = "0"
        $ padlock_4 = "0"

        $ padlock_final = "0000"
        $ padlock_correct = "1221"
        $ padlock_secret = "1312"
        
        $ attempts = 5 # I can't figure out where to initialize the variable so that the program remembers and recognizes it.

        menu:
            "Would you like to attempt the padlock? You have [attempts] attempts left."
            "Yes":
                jump padlock
            "On the second thought...":
                jump typewriter_menu

    label padlock:
            "Select the first number:"
            menu:
                "0":
                    $ padlock_1 = "0"
                "1":
                    $ padlock_1 = "1"
                "2":
                    $ padlock_1 = "2"
                "3":
                    $ padlock_1 = "3"
                "4":
                    $ padlock_1 = "4"
            
            "Select the second number:"
            menu:
                "0":
                    $ padlock_2 = "0"
                "1":        
                    $ padlock_2 = "1"
                "2":        
                    $ padlock_2 = "2"
                "3":        
                    $ padlock_2 = "3"
                "4":        
                    $ padlock_2 = "4"
                
            "Select the third number:"
            menu:
                "0":
                    $ padlock_3 = "0"
                "1":        
                    $ padlock_3 = "1"
                "2":        
                    $ padlock_3 = "2"
                "3":        
                    $ padlock_3 = "3"
                "4":        
                    $ padlock_3 = "4"
                
            "Select the fourth number:"
            menu:
                "0":
                    $ padlock_4 = "0"
                "1":        
                    $ padlock_4 = "1"
                "2":        
                    $ padlock_4 = "2"
                "3":        
                    $ padlock_4 = "3"
                "4":        
                    $ padlock_4 = "4"

            "Let's see..."
            $ padlock_final = padlock_1 + padlock_2 + padlock_3 + padlock_4
            "You dialed in [padlock_final]."
            $ attempts =- 1

            if padlock_final == padlock_correct:

               #Select 1221 as an answer
               "The lock opens!"
               jump end

            if padlock_final == padlock_secret:
               #Select 1312 as an answer
               "The lock remains closed.{p}However...!"
               show lafcadio happy at slightleft
               l "!"
               hide Lafcadio
               "A playing card fell out of the lock!"
               show grayson at slightright
               g "So it {i}was{/i} ACAB after all!"
               jump typewriter_give_answer
            else:
               #Select wrong answer
               "The padlock remains closed."
               l "Well that wasn't productive."
               #if attempts > 0:
               #     jump typewriter_give_answer
               jump typewriter_give_answer
    #Select 
    label end:
        "This concludes the tech demo."

    # This ends the game.

    return
