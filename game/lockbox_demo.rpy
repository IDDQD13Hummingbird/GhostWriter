default lockbox.puzzle_text_start = """KSG II{font=DejaVuSans.ttf}♫{/font} EEM YNA

Jump on C
Hop to G
Add one more 
Fall back two"""

default lockbox.cipher_answer = "1342"

default lockbox.cipher_vertical = """1 2 3 4
K I E Y
S I E N
G * M A

Cipher key - """ + lockbox.cipher_answer + """

Arrange the columns in that order"""

default lockbox.cipher_descrambled = """1 3 4 2
K E Y I
S E N I
G M A"""

default lockbox.typewriter_message = "A no tth r pas sww o d? I k ew i t! Wh t a snn a e - or a sn ee k -"

default lockbox.puzzle_text = lockbox.puzzle_text_start

default lockbox.cipher = ""

default lockbox.password.input = [ 0, 0, 0, 0, 0, 0 ]
default lockbox.password.answer = "163250" # ENIGMA
default lockbox.password.secret = "761048" # SNEAKY

default lockbox.password.images = [
    "Letter1.png", # A 0
    "Letter3.png", # E 1
    "Letter2.png", # G 2
    "Letter5.png", # I 3
    "Letter4.png", # K 4
    "Letter9.png", # M 5
    "Letter8.png", # N 6
    "Letter7.png", # S 7
    "Letter6.png" # Y 8
]

default lockbox.password.zoom = 0.45
default lockbox.password.xysize = (100, 100)

default lockbox.asked_tequila = False
default lockbox.asked_greyson_cipher = False
default lockbox.asked_greyson_descramble = False
default lockbox.asked_redd = False

default lockbox.cipher_solved = False
default lockbox.password_solved = False
default lockbox.password_secret_solved = False

init python:
    def check_cipher():
        if lockbox.cipher == lockbox.cipher_answer:
            lockbox.cipher_solved = True
            renpy.jump( "lockbox_process_cipher_answer" )

    def password_get_image( index ):
        return lockbox.password.images[ index ]

    def password_get_combination_image( index ):
        return password_get_image( lockbox.password.input[ index ] )

    def password_set_combination_input( index, direction ):
        value = lockbox.password.input[ index ]
        max = len( lockbox.password.images ) - 1

        if direction == "up":
            lockbox.password.input[ index ] = 0 if value == max else value + 1

        elif direction == "down":
            lockbox.password.input[ index ] = max if value == 0 else value - 1

        check_password_combination()

    def check_password_combination():
        combination = "".join( str(x) for x in lockbox.password.input )
        if combination == lockbox.password.answer and not lockbox.password_solved:
            lockbox.password_solved = True
            renpy.jump( "lockbox_process_password_answer" )
        if combination == lockbox.password.secret:
            lockbox.password_secret_solved = True
            renpy.jump( "lockbox_process_password_secret" )

    def lockbox_reinit():
        lockbox.puzzle_text = lockbox.puzzle_text_start

        lockbox.cipher = ""
        lockbox.password.input = [ 0, 0, 0, 0, 0, 0 ]

        lockbox.asked_tequila = False
        lockbox.asked_greyson_cipher = False
        lockbox.asked_greyson_descramble = False
        lockbox.asked_redd = False

        lockbox.cipher_solved = False
        lockbox.password_solved = False
        lockbox.password_secret_solved = False

screen lockbox_cipher:
    frame:
        xpos 0.6
        ypos 0.25
        style "frame_fancy"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            label "4-Digit Cipher Code":
                text_size gui.text_size
            input:
                value VariableInputValue( variable = "lockbox.cipher" )
            textbutton "Check Code":
                style "button_input"
                xalign 0.5
                action Function( check_cipher )

screen lockbox_password:
    grid 6 3:
        xalign 0.75
        yalign 0.2
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( password_set_combination_input, 0, "up" )
            
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( password_set_combination_input, 1, "up" )

        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( password_set_combination_input, 2, "up" )
  
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( password_set_combination_input, 3, "up" )

        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( password_set_combination_input, 4, "up" )
  
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( password_set_combination_input, 5, "up" )

        frame:
            xysize lockbox.password.xysize
            add password_get_combination_image(0): 
                zoom lockbox.password.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize lockbox.password.xysize
            add password_get_combination_image(1): 
                zoom lockbox.password.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize lockbox.password.xysize
            add password_get_combination_image(2): 
                zoom lockbox.password.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize lockbox.password.xysize
            add password_get_combination_image(3): 
                zoom lockbox.password.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize lockbox.password.xysize
            add password_get_combination_image(4): 
                zoom lockbox.password.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize lockbox.password.xysize
            add password_get_combination_image(5): 
                zoom lockbox.password.zoom
                xalign 0.5
                yalign 0.5

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( password_set_combination_input, 0, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( password_set_combination_input, 1, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( password_set_combination_input, 2, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( password_set_combination_input, 3, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( password_set_combination_input, 4, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( lockbox.password.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( password_set_combination_input, 5, "down" )

label lockbox_start:
    $ lockbox_reinit()
    $ flag_cipher = True
    $ gui.custom.textbox_position = "centre"
    show greyson_r at my_moveinleft
    greyson "Now, let's see what we have!"
    "[lockbox.puzzle_text]"
    show tequila_m at my_moveinright
    tequila "Six letters from all that, somehow. And I don't see any C in these dials."
    greyson "You wouldn't. It's a transposition cipher. Rather classic - or extremely antiquated - but anyhow. All the letters we need are up at the top."
    tequila "And I reckon you know how to order them?"
    greyson "I will when we know the code. One number for each three-letter phrase, so some permutation of 1,2,3,4. Not in that same order, though - that would be just too trivial."
    tequila "What sort of lock isn't too trivial for you?"
    greyson "This right here, I suppose - I was never brilliant at bashing through these in my head. If I was sat with pen and paper, I could take a good crack at it. But why hog all the fun around here, eh?"

    hide greyson_r with moveoutleft
    hide tequila_m with moveoutright

    $ lockbox.puzzle_text += "\n\nNeeds a 4-digit code made of 1,2,3,4"

    $ gui.custom.textbox_position = "left"
    jump lockbox_menu

label lockbox_menu:
    $ check_turns()

    menu:
        "[lockbox.puzzle_text]"
        "Let's settle this 4-digit cipher code" if not lockbox.cipher_solved and not lockbox.password_solved:
            $ turns -= 1
            jump lockbox_cipher_give_answer
        "The cipher contains a music note. Might that be of significance?" if not lockbox.cipher_solved and not lockbox.password_solved:
            $ turns -= 1
            jump lockbox_tequila
        "1,5,6,4 - I could use some locksmith's eyes here" if lockbox.asked_tequila and not lockbox.cipher_solved and not lockbox.password_solved:
            $ turns -= 1
            jump lockbox_greyson_cipher
        "I'm rather scrambled trying to descramble this" if lockbox.cipher_solved and not lockbox.password_solved and not lockbox.asked_greyson_descramble:
            $ turns -= 1
            jump lockbox_greyson_descramble
        "Shall we crack this mystery box open, then?" if not lockbox.password_solved:
            $ turns -= 1
            jump lockbox_password_give_answer
        "This letter set has some possibilities -" if lockbox.password_solved and not lockbox.password_secret_solved:
            $ turns -= 1
            jump lockbox_password_give_answer
        "Redd, does that give you enough to go on?" if lockbox.password_solved and not lockbox.password_secret_solved:
            $ turns -= 1
            jump lockbox_redd
        "Time's short - let's rather move onto that riddle -" if lockbox.password_solved and not lockbox.password_secret_solved:
            jump woodwind_start

label lockbox_tequila:
    $ gui.custom.textbox_position = "centre"

    show tequila_m at my_moveinright
    tequila "Mr. Redd - a duet, if you would."
    tequila "Jump on C, hop to G. Sounds like a piece of a chord progression."

    show redd_m_r at my_moveinleft
    redd "And a subtler hint at the rest. If we {i}add{/i} one - go up to A - then {i}fall{/i} back two down the scale -"
    tequila "Then we have C, G, A, F, and our numbers are chord notation."
    redd "We started with C, so we should be in that key. Therefore, C is 1."
    tequila "So C, G, A, F gives us 1, 5, 6, 4.{p}\n...{p}\nAnd of course it couldn't be all nice and literal."
    hide tequila_m with moveoutright
    hide redd_m_r with moveoutleft
 
    if not lockbox.asked_tequila:
        $ lockbox.puzzle_text += "\n\nThe verse is a chord progression - 1,5,6,4"
    $ lockbox.asked_tequila = "True"
    $ gui.custom.textbox_position = "left"
    jump lockbox_menu

label lockbox_greyson_cipher:
    show greyson at my_moveinright
    greyson "Ah, there's the fun, relatively speaking. We need to number those numbers. If we start with 1, what's the next largest? The 2 goes in that position. And so on to 4.{p}\nSo, to start - 1 * * 2 -"
    if not lockbox.asked_greyson_cipher:
        $ lockbox.puzzle_text += " - to be numbered from smallest to largest. To start, looks like 1 * * 2"
    $ lockbox.asked_greyson_cipher = True
    hide greyson
    jump lockbox_menu

label lockbox_greyson_descramble:
    show greyson at my_moveinright
    greyson "Of course - let's set these all in order -"
    $ lockbox.puzzle_text = lockbox.cipher_descrambled
    $ lockbox.asked_greyson_descramble = True
    hide greyson 
    jump lockbox_menu

label lockbox_redd:
    show redd_m at my_moveinright
    redd "That is about right, then, isn't it? 'What a snake, or a sneak'. We just need one more letter, and the clues seem to already be in order -"
    $ lockbox.puzzle_text = "As per Mr. Minski - \"What a snake, or a sneak\".\n\nNow to just add one more letter - "
    hide redd_m with moveoutright
    jump lockbox_menu

label lockbox_cipher_give_answer:
    show screen lockbox_cipher
    menu( screen="choice_h" ):
        "[lockbox.puzzle_text]"
        "Back to Clues":
            hide screen lockbox_cipher
            jump lockbox_menu
   
label lockbox_process_cipher_answer:
    hide screen lockbox_cipher
    $ lockbox.puzzle_text = lockbox.cipher_vertical
    show greyson at my_moveinright
    greyson "[lockbox.cipher_answer] - shall we give that a go? First, write each phrase out vertically -{p}\nThen rearrange accordingly -"
    "[lockbox.puzzle_text]"
    hide screen lockbox_cipher
    hide greyson
    jump lockbox_menu

label lockbox_password_give_answer:
    show screen lockbox_password
    menu( screen="choice_h" ):
        "[lockbox.puzzle_text]"
        "Back to Clues":
            hide screen lockbox_password
            jump lockbox_menu

label lockbox_process_password_answer:
    $ gui.custom.textbox_position = "centre"
    hide screen lockbox_password
    show greyson_r at my_moveinleft
    greyson "Ha! Not much of an enigma now, is it?"
    show tequila_m at my_moveinright
    tequila "The password isn't, at least. We've yet to see what all it's been hiding."

    if lockbox.password_secret_solved:
        greyson "There's a note, for one - another riddle, from the looks of it. Now what's to be done with that?"
        hide greyson_r with moveoutleft
        hide tequila_m with moveoutright
        jump woodwind_start

    greyson "There's a note, for one - another riddle, from the looks of it. Though this compartment seems a bit shallow."
    tequila "Do you reckon there's another way in?"
    hide tequila_m with moveoutright
    show redd_m at my_moveinright
    redd "There is with an anagram, I'd wager. Gamine, making, genies - this could keep me tied up for a while -"
    hide greyson_r
    hide tequila 
    show willow_m_r at my_moveinleft
    willow "Mr. Minski, please tell me you have some sense of direction."

    show typewriter with vpunch
    tp "{cps=[cps]}[lockbox.typewriter_message]{/cps}"
    $ lockbox.puzzle_text = lockbox.typewriter_message
    hide willow_m_r
    hide redd_m
    hide typewriter
    $ gui.custom.textbox_position = "left"
    jump lockbox_menu

label lockbox_process_password_secret:
    hide screen lockbox_password

    "Sneaky sneaky. Well done! The secret compartment contains a card for your collection."
    
    $ card_index = 3
    $ card_images_found[ card_index ] = True
    $ card_image = card_images[ card_index ]

    show expression [card_image] as card at screen_centre with spiral
    pause

    if lockbox.password_solved:
        "Now on to the riddle at hand..."
        hide card
        jump woodwind_start

    menu( screen="choice_h" ):
        "Though there's still more to be found here..."
        "Back to Clues":
            hide card
            jump lockbox_menu
