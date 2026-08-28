# To adress the elephant in the room : I feel incredibly understimulated by coding, and this feels like a physical torture.
# Insofar, this puzzle is a reskin of card selection.
# Anyhow, 

default card.suit.input = [ 0, 0, 0, 0 ] #Jack, Queen, King, Joker
default card.suit.answer = "1230" # Up the chapel
default card.suit.secret = "1210" # Down the basement

default card.suit1 = 2
default card.suit2 = 2
default card.suit3 = 2
default card.suit4 = 2

default card.suit.images = [ 
    "select_clubs.png",     #0
    "select_diamonds.png",  #1
    "select_spades.png",    #2
    "select_hearts.png",    #3
]

default card.suit.zoom = 0.45
default card.suit.xysize = (200, 150)
#default card.suit_solved = False - you only get one shot

init python:
    def suit_get_image( index ):
        return card.suit.images[ index ]

    def suit_get_combination_image( index ):
        return suit_get_image( card.suit.input[ index ] )

    def suit_set_combination_input( index, direction ):
        value = card.suit.input[ index ]
        max = len( card.suit.images ) - 1

        if direction == "up":
            card.suit.input[ index ] = 0 if value == max else value + 1

        elif direction == "down":
            card.suit.input[ index ] = max if value == 0 else value - 1

        check_suit_combination()

    def check_suit_combination(): # Sort solution & input by image index to compare irrespective of order
        combination = "".join( str(x) for x in sorted( card.suit.input ) )
        if combination == card.suit.answer and not card.choice_answer_solved:
            card.choice_answer_solved = True
            renpy.jump( "card_process_choice_answer" )
        if combination == card.suit.secret:
            card.choice_secret_solved = True
            renpy.jump( "card_process_choice_secret" )

screen card_suit_interactive:
    grid 4 3:
        xalign 0.5
        yalign 0.2
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( suit_set_combination_input, 0, "up" )
            
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( suit_set_combination_input, 1, "up" )

        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( suit_set_combination_input, 2, "up" )
  
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( suit_set_combination_input, 3, "up" )

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(0): 
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(1): 
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(2): 
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(3): 
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( suit_set_combination_input, 0, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( suit_set_combination_input, 1, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( suit_set_combination_input, 2, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( suit_set_combination_input, 3, "down" )

screen card_suit_answer( grid_xalign, grid_yalign, grid_x, grid_y, answer ):
    python:
        index1 = int( answer[0] )
        index2 = int( answer[1] )
        index3 = int( answer[2] )
        index4 = int( answer[3] )

    grid grid_x grid_y:
        xalign grid_xalign
        yalign grid_yalign

        frame:
            xysize card.suit.xysize
            add suit_get_image(index1):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_image(index2):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_image(index3):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_image(index4):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

screen card_suit_interactive:

    default ordered_answer = "2222"

    python:
        index1 = int( ordered_answer[0] )
        index2 = int( ordered_answer[1] )
        index3 = int( ordered_answer[2] )
        index4 = int( ordered_answer[3] )

    grid 4 2:
        xalign 0.75
        yalign 0.2
        xspacing 50
        yspacing 25
        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "card.suit1", step = 1, range = 3, action = Function( check_suit_suit ) )         

        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "card.suit2", step = 1, range = 3, action = Function( check_suit_suit ) )

        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "card.suit3", step = 1, range = 3, action = Function( check_suit_suit ) )

        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "card.suit4", step = 1, range = 3, action = Function( check_suit_suit ) )

        frame:
            xysize card.suit.xysize
            add suit_get_image(index1):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_image(index2):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_image(index3):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_image(index4):
                zoom card.suit.zoom
                xalign 0.5
                yalign 0.5


label cardsuit_start:
    $ gui.custom.textbox_position = "centre"

    play music "MainTrack.ogg" fadein 5.0

    scene bg tequilastage with spiral

    king "Very well. You found it. The final puzzle."

    show kingclubs at my_moveinright
    king "You wish to see the Marquis, correct?\nHe warned us we might be due for a divine intervention, and it seems he was actually right."
    show twodiamonds_r at my_moveinleft
    two "We'll take you to the last door behind which lie all the answers.\nIt is, however, up to you to present us with the right key."
    two "Four statues : Jack, Queen, King and Joker. Four suits to match their ranks. Name them, and we'll set up the order."
    king "I hope you've gathered a good idea what shape holds the Marquis's heart, for that the king has been concealed from us as much as he has stayed hidden from you."
    hide twodiamonds_r with moveoutleft
    show tequila_m_r at my_moveinleft
    tequila "Hold on... this sounds familiar."
    tequila "Marquis was always a fan of a good Sting. This is \"Shape of My Heart\", isn't it?"
    tequila "He may lay the Jack of Diamonds, he may play the Queen of Spades... That's good for at least half the clue, isn't it?\nBut I'm not sure what that has to do with the Jester - let alone with the concealed king in his hand." 
    hide kingclubs with moveoutright
    show willow_m thinking at my_moveinright
    willow "...I'm afraid Mr. Minski has no clue as of how to solve this one."
    if found_card1 or found_card2 or found_card3 or found_card4:
        show willow_m
        willow "Perhaps, this is where the cards become useful?" 
    if found_card1 and not found_card2:
        willow "Jack of Diamonds... Just as Tequila said. It really is in the song, isn't it?" 
    if found_card2 and not found_card1:
        willow "Queen of Spades... Just as Tequila said. It really is in the song, isn't it?"
    if found_card1 and found_card2:
        willow "Jack of Diamonds and Queen of Spades... Just as Tequila said. It really is in the song, isn't it?" 
    if found_card3 and not found_card4:
        tequila "The Fool, which might as well be our runaway \"King\", or, rather the Jester..." 
    if found_card4 and not found_card3:
        tequila "The Jester and the weapon of war that he holds..." 
    if found_card3 and found_card4:
        tequila "The Fool, which might as well be our runaway \"King\" - and the Jester with the exact same staff for it's suit." 
    hide willow_m with moveoutright
    hide tequila_m_r with moveoutleft
    show kingclubs at my_moveinright
    king "You'll only get one shot.\nI sincerely wish you to succeed."
    
    show screen card_suit_interactive


    jump end
