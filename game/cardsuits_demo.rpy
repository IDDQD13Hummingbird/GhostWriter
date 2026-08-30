default card.puzzle_text = ""

default card.suit.input = [ 0, 0, 0, 0 ] #Jack, Queen, King, Joker
default card.suit.answer = "1230" # Up the chapel
default card.suit.secret = "1210" # Down the basement

default card.suit.images = [ 
    "select_clubs.png",     #0
    "select_diamonds.png",  #1
    "select_spades.png",    #2
    "select_hearts.png",    #3
]

default card.wildcard.input = 0
default card.wildcard.answer = 2

default card.wildcard.images = [
    "knight_spades.png",
    "weapon_clubs.png",
    "the_fool.png"
]

default card.suit.zoom = 0.45
default card.display.zoom = 0.65
default card.suit.xysize = (200, 150)

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

    def wildcard_get_image( index ):
        return card.wildcard.images[ index ]

    def wildcard_get_combination_image():
        return wildcard_get_image( card.wildcard.input )

    def wildcard_set_combination_input( direction ):
        value = card.wildcard.input
        max = len( card.wildcard.images ) - 1

        if direction == "up":
            card.wildcard.input = 0 if value == max else value + 1

        elif direction == "down":
            card.wildcard.input = max if value == 0 else value - 1

    def check_suit_combination(): 
        combination = "".join( str(x) for x in card.suit.input )
        if combination == card.suit.answer and card.wildcard.input == card.wildcard.answer:
            renpy.jump( "card_process_choice_answer" )
        elif combination == card.suit.secret and card.wildcard.input == card.wildcard.answer:
            renpy.jump( "card_process_choice_secret" )
        else:
            renpy.jump( "card_process_choice_wrong")

screen card_suit_reference:
    grid 5 1:
        xalign 0.9
        yalign 0.1

        frame:
            xysize card.suit.xysize
            if card_images_found[0]:
                $ file_path = card_images[0]
                add [file_path]:
                    xalign 0.5
                    yalign 0.5
                    zoom card.display.zoom

        frame:
            xysize card.suit.xysize
            if card_images_found[1]:
                $ file_path = card_images[1]
                add [file_path]:
                    xalign 0.5
                    yalign 0.5
                    zoom card.display.zoom

        frame:
            xysize card.suit.xysize
            if card_images_found[2]:
                $ file_path = card_images[2]
                add [file_path]:
                    xalign 0.5
                    yalign 0.5
                    zoom card.display.zoom

        frame:
            xysize card.suit.xysize
            if card_images_found[3]:
                $ file_path = card_images[3]
                add [file_path]:
                    xalign 0.5
                    yalign 0.5
                    zoom card.display.zoom

        frame:
            xysize card.suit.xysize
            if card_images_found[4]:
                $ file_path = card_images[4]
                add [file_path]:
                    xalign 0.5
                    yalign 0.5
                    zoom card.display.zoom

screen card_suit_interactive:
    modal True
    grid 5 3:
        xalign 0.9
        yalign 0.3
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

        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( card.suit.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( wildcard_set_combination_input, "up" )

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(0): 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(1): 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(2): 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add suit_get_combination_image(3): 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add wildcard_get_combination_image(): 
                xalign 0.5
                yalign 0.5
                zoom card.display.zoom

        frame:
            xysize card.suit.xysize
            add "card_jack.png": 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add "card_queen.png": 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add "card_king.png": 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize
            add "card_jester.png": 
                xalign 0.5
                yalign 0.5

        frame:
            xysize card.suit.xysize

    textbutton "I am ready.":
        style "button_input"
        xalign 0.71
        yalign 0.65
        action Function( check_suit_combination )

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

label cardsuit_start:
    $ flag_card = true
    $ gui.custom.textbox_position = "centre"

    stop music fadeout 3.0

    scene bg tequilastage with spiral

    play music "MainTrack.ogg" fadein 5.0

    show kingclubs at my_moveinright

    king "Here we are."

    $ text = "Get it wrong, and it locks for an hour. Or worse.{p}\nThe Marquis did mention a new measure of extra security."

    if cards_found == 5:
        king "Do be careful to match the exact combination. [text]"
    else:
        show greyson_r at my_moveinleft
        greyson "Is that all? Can't we just brute force it? Or does this daft device charge per attempt?"
        king "That would be very much at your own risk, sir. [text]"
        hide greyson_r with moveoutleft

    show thanos_r at my_moveinleft
    thanos "That measure is news to me. I'm almost afraid to even ask."
    hide thanos_r with moveoutleft

    show reggie_m_r at my_moveinleft
    reggie "A spiral slide down to the basement? If only I had my druthers..."
    hide reggie_m_r with moveoutleft

    if cards_found < 5:
        show willow_m_r at my_moveinleft
        willow "If only we had a better idea of this combination. Let's review what we do know so far..."

        $card.puzzle_text = "Each suit is only used once\n\nSuit colors are mixed - combination will not have both red together then both black, or vice versa"

        if not card_images_found[0]:
            $card.puzzle_text += "\n\nJack is not Clubs"
        hide willow_m_r with moveoutleft

        show twodiamonds_r at my_moveinleft
        two "There is one thing - could be nothing - but it's something. The Marquis was humming a song the other day.{p}\nSomething about a diamond, and a spade.{p}\nIf the first then goes before the other..."
        hide twodiamonds_r with moveoutleft
        $card.puzzle_text += "\n\nDiamonds perhaps followed by Spades?"

        if not card_images_found[4]:
            king "What manner of a fool would come up with this whole scheme, anyhow?"
            $card.puzzle_text += "\n\nFoolish business, all told"

    hide kingclubs with moveoutright
    
    $ gui.custom.textbox_position = "left"

    show screen card_suit_interactive
    show screen card_suit_reference
    if len( card.puzzle_text ):
        "[card.puzzle_text]"
    pause

label cardsuit_start_v1:
    $ gui.custom.textbox_position = "centre"

    stop music fadeout 3.0

    scene bg tequilastage with spiral

    two "Summoning us with the toot on the horn?"
    king "Very well. You found it. The final puzzle."

    play music "MainTrack.ogg" fadein 5.0

    show kingclubs at my_moveinright
    king "You wish to see the Marquis, correct?\nHe warned us we might be due for a divine intervention, and it seems he was actually right."
    show twodiamonds_r at my_moveinleft
    two "We'll take you to the last door behind which lie all the answers.\nIt is, however, up to you to present us with the right key."
    two "Four statues : Jack, Queen, King and Joker. Four suits to match their ranks. Name them, and we'll set up the order."
    hide twodiamonds_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "The statues? You don't mean... It's time for the Phoenix Elevator?"
    king "It might as well be. We weren't thouroughly instructed."
    king "I hope you've gathered a good idea what shape holds the Marquis's heart, for that the king has been concealed from us as much as he has stayed hidden from you."
    hide thanos_r with moveoutleft
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
    king "I've been told I should warn you - you'll only get one shot.\nWhatever you are doing, I sincerely wish you to succeed."
    
    #show screen card_suit_answer
    show screen card_suit_interactive
    pause

label card_process_choice_answer:
    hide screen card_suit_reference
    hide screen card_suit_interactive
    show kingclubs at my_moveinright
    king "A jolly good show! Off we go, then."
    king "Let's see where the Marquis was hiding!"
    hide background

    n "NORMAL ENDING"

    jump end

label card_process_choice_secret:
    hide screen card_suit_reference
    hide screen card_suit_interactive
    show kingclubs at my_moveinright
    #king "The true secret is where this branch actually leads."
    king "That certainly broke the rules of how this lock operates. I'm fascinated - and somewhat worried - that it worked at all."
    king "...how did you figure this out?"
    king "On a second thought, I don't need to know. You all seemed in a hurry."
    king "Wherever this door is going to take you... good luck."
    hide background

    n "SECRET ENDING"

    jump end

label card_process_choice_wrong:
    hide screen card_suit_reference
    hide screen card_suit_interactive
    show kingclubs upset at my_moveinright
    king "That... didn't sound right. {b}Uh-oh."
    jump gameover
    #king "I regret to inform you that...{p}\nYou get nothing! You lose! Good day, sir!"

    jump end