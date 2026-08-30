default cocktail.highlight = "#5de173"

default cocktail.typewriter_message_start = "R ge rr's jol y, b l dyy trro l ley d\nB leww h s sta kk of tth tr ckks\nC ugg t ut f r a li r, tro uus rs al o n fi re\nWal kkd t hee pla k, n w he s s nk"
default cocktail.typewriter_message_deciphered = "Roger's jolly, bloody trolleyed\nBlew his stack off the tracks\nCaught out for a liar, trousers all on fire\nWalked the plank, now he's sank"
default cocktail.typewriter_message_highlight = "{color=" + cocktail.highlight + "}Roger's jolly{/color}, bloody trolleyed\nBlew his stack off the {color=" + cocktail.highlight + "}tracks{/color}\nCaught out for a liar, trousers all on {color=" + cocktail.highlight + "}fire{/color}\nWalked the plank, now he's {color=" + cocktail.highlight + "}sank{/color}"
default cocktail.typewriter_message = cocktail.typewriter_message_start

default cocktail.ingredient.input = [ 0, 0, 0, 0 ]
default cocktail.ingredient.answer = "1457" # Index order, not clued order - Grinmaw, Jolly Roger, railroad, fire
default cocktail.ingredient.secret = "0367" # FIRE!

default cocktail.mix1 = 1
default cocktail.mix2 = 1
default cocktail.mix3 = 1
default cocktail.mix4 = 1

default cocktail.ingredient.images = [ # Rearranged from their original numbering to spread the solution around
    "Label1.png", # ! Keep away from small children and Lucas Bondes
    "Label4.png", # Grinmaw
    "Label2.png", # Does your mother know you're here?
    "Label3.png", # Asbestos
    "Label5.png", # Poison is sexy
    "Label6.png", # RR
    "Label8.png", # Gas
    "Label7.png", # Fire
]

default cocktail.ingredient.zoom = 0.45
default cocktail.ingredient.xysize = (200, 150)

default cocktail.asked_mix_help = False

default cocktail.choice_answer_solved = False # True when the standard choice of ingredients is discovered
default cocktail.choice_secret_solved = False # True when the secret choice of ingredients is discovered
default cocktail.mix_solved = False

init python:
    def ingredient_get_image( index ):
        return cocktail.ingredient.images[ index ]

    def ingredient_get_combination_image( index ):
        return ingredient_get_image( cocktail.ingredient.input[ index ] )

    def ingredient_set_combination_input( index, direction ):
        value = cocktail.ingredient.input[ index ]
        max = len( cocktail.ingredient.images ) - 1

        if direction == "up":
            cocktail.ingredient.input[ index ] = 0 if value == max else value + 1

        elif direction == "down":
            cocktail.ingredient.input[ index ] = max if value == 0 else value - 1

        check_ingredient_combination()

    def check_ingredient_combination(): # Sort solution & input by image index to compare irrespective of order
        combination = "".join( str(x) for x in sorted( cocktail.ingredient.input ) )
        if combination == cocktail.ingredient.answer and not cocktail.choice_answer_solved:
            cocktail.choice_answer_solved = True
            renpy.jump( "cocktail_process_choice_answer" )
        if combination == cocktail.ingredient.secret:
            cocktail.choice_secret_solved = True
            renpy.jump( "cocktail_process_choice_secret" )

    def check_ingredient_mix():
        if cocktail.mix1 == 1 and cocktail.mix2 == 2 and cocktail.mix3 == 3 and cocktail.mix4 == 2:
            cocktail.mix_solved = True
            renpy.jump( "cocktail_process_mix_answer" )

    def cocktail_reinit():
        cocktail.typewriter_message = cocktail.typewriter_message_start

        cocktail.ingredient.input = [ 0, 0, 0, 0 ]
        cocktail.mix1 = 1
        cocktail.mix2 = 1
        cocktail.mix3 = 1
        cocktail.mix4 = 1

        cocktail.choice_answer_solved = False
        cocktail.choice_secret_solved = False
        cocktail.mix_solved = False

        cocktail.asked_mix_help = False

screen cocktail_ingredient_interactive:
    grid 4 3:
        xalign 0.75
        yalign 0.2
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( ingredient_set_combination_input, 0, "up" )
            
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( ingredient_set_combination_input, 1, "up" )

        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( ingredient_set_combination_input, 2, "up" )
  
        imagebutton:
            auto "arrow_up_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.85
            action Function( ingredient_set_combination_input, 3, "up" )

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_combination_image(0): 
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_combination_image(1): 
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_combination_image(2): 
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_combination_image(3): 
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( ingredient_set_combination_input, 0, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( ingredient_set_combination_input, 1, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( ingredient_set_combination_input, 2, "down" )

        imagebutton:
            auto "arrow_down_%s.png"
            at button_zoom( cocktail.ingredient.zoom )
            xalign 0.5 
            yalign 0.15
            action Function( ingredient_set_combination_input, 3, "down" )

screen cocktail_ingredient_answer( grid_xalign, grid_yalign, grid_x, grid_y, answer ):
    python:
        index1 = int( answer[0] )
        index2 = int( answer[1] )
        index3 = int( answer[2] )
        index4 = int( answer[3] )

    grid grid_x grid_y:
        xalign grid_xalign
        yalign grid_yalign

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index1):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index2):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index3):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index4):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

screen cocktail_mix_interactive:

    default ordered_answer = "4571"

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
            value VariableValue( variable = "cocktail.mix1", step = 1, range = 3, action = Function( check_ingredient_mix ) )         

        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "cocktail.mix2", step = 1, range = 3, action = Function( check_ingredient_mix ) )

        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "cocktail.mix3", step = 1, range = 3, action = Function( check_ingredient_mix ) )

        vbar:
            ysize 200
            xalign 0.5
            range 3
            value VariableValue( variable = "cocktail.mix4", step = 1, range = 3, action = Function( check_ingredient_mix ) )

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index1):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index2):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index3):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

        frame:
            xysize cocktail.ingredient.xysize
            add ingredient_get_image(index4):
                zoom cocktail.ingredient.zoom
                xalign 0.5
                yalign 0.5

label cocktail_start:
    $ cocktail_reinit()
    $ flag_bar = True
    $ gui.custom.textbox_position = "centre"

    play music "SlowTheme.mp3" fadein 2.0

    scene bg bar with wave

    show acespades_r at my_moveinleft
    ace "At your service."

    show willow_m at my_moveinright
    willow "Best in the Brutale business, yes? Of course you are. He speaks of you fondly just now."

    show acespades_r upset
    ace "He being - the typewriter?"

    willow "That is so, yes. It's quite the story. Quite the - adventure - to converse with."

    show typewriter with vpunch
    tp "{cps=[cps]}I cn h earr y o, yuu kn w! D onn' ma e m wa sst my in k!{/cps}"

    ace "Might I be familiar with this - shall we say - tempest in a typewriter?"

    willow "Alexander Minski, a Russian diamond magnate. Seems that you gave him a shot to remember - or more so a good few all at once."

    show acespades_r
    ace "Right - yes - that's some history. Top secret, too, sad to say."
    hide willow_m with moveoutright

    show aurum_m at my_moveinright
    aurum "You mean to say you can't mix it for an audience?"

    ace "I'm afraid I can't mix it at all. Just once, when I forget to make a note of things - unless our guest here might have some idea -"

    hide aurum_m with moveoutright

    show typewriter with vpunch
    tp "{cps=[cps]}I t w as bot tm sh llf! Th t's h gh pr i see!{/cps}"

    ace "Bottom - shelf? Oh - right - it would be. Now what all do I have in there?"

    show clay_m sober at my_moveinright
    clay "You don't have a note of that, either?"

    ace "Of course not. I have to keep some secrets in trade."
    hide acespades_r with moveoutleft
    
    show acespades_r at my_moveinleft
    ace "Even if they're from myself, at times, when I dust something off from the back. Have a look?"

    hide clay_m sober with moveoutright
    show aurum_m at my_moveinright

    aurum "\"For industrial use only.\"{p}\n\"Caustic - do not handle without gloves and full face shield.\"{p}\n\"Hard hats required at all times.\""
    hide aurum_m with moveoutright

    show clay_m sober at my_moveinright
    clay "I'd try my luck with that. Line 'em up, knock 'em back, right? Knock myself out - I've had worse.{p}\nBut not right now. We've got work to do."

    show typewriter with vpunch
    tp "{cps=[cps]}It k n oc edd me o t! Tw c e o vv r! F ur sho s d wn fo t e co nnt!{p}\n[cocktail.typewriter_message]{/cps}"

    show acespades_r upset
    ace "Strong and incomprehensible in absurd and equal measures. Right.{p}\nMay I ask how Mr. Minski is to drink it?"

    hide clay_m sober with moveoutright
    show willow_m at my_moveinright
    willow "I'll cross that spiritual bridge when we get there."
    hide willow_m with moveoutright

    hide acespades_r
    hide typewriter
    $ gui.custom.textbox_position = "left"
    jump cocktail_menu

label cocktail_menu:
    $ check_turns()
    pause
    
    menu:
        "[cocktail.typewriter_message]"
        "I'm rather at a loss here. Clay, you look as if this might ring a bell -" if not cocktail.choice_answer_solved:
            $ turns -= 1
            jump cocktail_clay
        "The ingredients are sorted - now for the mix." if cocktail.choice_answer_solved and not cocktail.mix_solved:
            $ turns -= 1
            jump cocktail_give_mix_answer
        "I'm perplexed about these proportions. The hot stuff calls for a heavy pour -" if cocktail.choice_answer_solved and not cocktail.mix_solved:
            $ turns -= 1
            jump cocktail_mix_help
        "Let's gin this up, now, shall we?" if not cocktail.choice_answer_solved:
            $ turns -= 1
            jump cocktail_give_choice_answer
        "A second round, perhaps? Mr. Minski seems suspiciously fond of that hot stuff -" if cocktail.choice_answer_solved and not cocktail.choice_secret_solved:
            $ turns -= 1
            jump cocktail_give_choice_answer

label cocktail_clay:
    $ gui.custom.textbox_position = "centre"
    show clay_m happy at my_moveinright
    clay "It's a song some git kept banging on about. Over and over till I almost had to bang on him myself.{p}\n\"Roger's Jolly, bloody trolleyed{p}Blew his stack off the tracks{p}Caught out for a liar, trousers all on fire{p}Walked the plank, now he's sank\"{p}\nAnd that's bloody stuck in my head now."
    show acespades_r at my_moveinleft
    ace "Right - that one - but of course. Spells it out line by line, does it not?"
    clay "Jolly Roger. What a mate. Still cheeky, even after that misadventure into the sea."
    $ cocktail.typewriter_message = cocktail.typewriter_message_deciphered
    hide clay_m happy with moveoutright
    hide acespades_r with moveoutleft
    $ gui.custom.textbox_position = "left"
    jump cocktail_menu

label cocktail_mix_help:
    $ gui.custom.textbox_position = "centre"
    show clay_m happy at my_moveinright
    clay "Don't ask me. What I get, I get, and it's all good. I'm the last one to be faffing about with a beaker."
    show aurum_m_r at my_moveinleft
    aurum "I'm one to put the fun in formulation - but I doubt we need to be exact. Just close enough according to some measure."

    clay "Don't be stingy with that hot stuff. Got that. The song rather does make a show of that bit."

    aurum "At the end of the longest line, nonetheless. So if that one's the most -"

    clay "And Jolly Roger's the least -"

    aurum "And the other two are in the middle -"
    if not cocktail.asked_mix_help:
        $ cocktail.typewriter_message = cocktail.typewriter_message_highlight

    hide clay_m happy with moveoutright
    hide aurum_m_r with moveoutleft
    $ gui.custom.textbox_position = "left"
    $ cocktail.asked_mix_help = True
    jump cocktail_menu

label cocktail_give_choice_answer:
    show screen cocktail_ingredient_interactive

    menu( screen="choice_h" ):
        "[cocktail.typewriter_message]"
        "Back to Clues":
            hide screen cocktail_ingredient_interactive
            jump cocktail_menu

label cocktail_process_choice_answer:
    hide screen cocktail_ingredient_interactive
    show willow_m at my_moveinright with moveoutright
    willow "Let's see if this smells familiar, yes?"

    show expression ingredient_get_image(4) as ingredient_label at screen_centre
    willow "Licorice, coriander, juniper, salamander. Maybe not exactly, no, but there's something in that sharp whiff of smoke."
    hide ingredient_label
    
    show expression ingredient_get_image(5) as ingredient_label at screen_centre
    willow "Lavender and rosemary. A sweet scent, surprisingly strong."
    hide ingredient_label
     
    show expression ingredient_get_image(7) as ingredient_label at screen_centre
    willow "Oof. My nose. Seems this one is just straight fire."
    hide ingredient_label
   
    show expression ingredient_get_image(1) as ingredient_label at screen_centre
    willow "Rum. As if this would be anything else. It's so dark I can just about chew it."
    hide ingredient_label

    hide willow_m with moveoutright

    show typewriter with vpunch
    tp "{cps=[cps]}Th tt' i ! T at's itt! Nw don tt y u d re bee s ti ggy wi h tat hoo t s ttuf!{/cps}"
    hide typewriter

    $ conditional_message = "Mr. Minski seems pleased - or close enough."
    if not cocktail.choice_secret_solved:
        $ conditional_message += "{p}\nThough I suspect something more might be concocted..." 
    "[conditional_message]"
    $ cocktail.typewriter_message = cocktail.typewriter_message_deciphered
    jump cocktail_menu

label cocktail_process_choice_secret:
    hide screen cocktail_ingredient_interactive
    show screen cocktail_ingredient_answer( grid_xalign = 0.5, grid_yalign = 0.5, grid_x = 2, grid_y = 2, answer = cocktail.ingredient.secret )
    show acespades at my_moveinright
    ace "Doubling down on that hot stuff with a hat tip to fire safety. Well done.\n{p}Have a card."
    hide screen cocktail_ingredient_answer

    $ card_index = 2
    $ card_images_found[ card_index ] = True
    $ card_image = card_images[ card_index ]
    show expression [card_image] as card at screen_centre with spiral
    pause
    hide acespades
    hide card
    jump cocktail_menu

label cocktail_give_mix_answer:
    show screen cocktail_mix_interactive
    menu( screen="choice_h" ):
        "[cocktail.typewriter_message]"
        "Back to Clues":
            hide screen cocktail_mix_interactive
            jump cocktail_menu

label cocktail_process_mix_answer:
    hide screen cocktail_mix_interactive
    $ gui.custom.textbox_position = "centre"
    pause 5.0
    show acespades at my_moveinright
    ace "Just a shake - and a stir - and a garnish of ghost pepper - and here we are -"
    show typewriter with vpunch
    tp "{cps=[cps]}Sp t onn!{/tps}"

    ace "Very good. Though this leaves just one question."
    show clay_m_r happy at my_moveinleft
    clay "The logistics of drinking that?"
    ace "The logistics of payment. Would Mr. Minski care to start a tab?"
    hide clay_m_r happy with moveoutleft

    show aurum_m_r at my_moveinleft
    aurum "Mr. Minski's on a rather tight schedule - swinging by more so than settling in. He'd like to settle with this."

    ace "A token of the Marquis' appreciation. But of course. This one in particular was taken in trade for a party favor.{p}\nWhich I was told to trade back for some purpose, and should be securely locked up in here -"

    hide acespades with moveoutright
    hide aurum_m_r with moveoutleft

    show greyson_r at my_moveinleft
    greyson "Need a hand back there, mate? Or a lockpick?"

    show acespades at my_moveinright
    ace "I need a good head for riddles, it seems. You do, rather, if you're meant to open this."
    hide acespades with moveoutright

    show redd_m at my_moveinright
    redd "There is the nuclear option. Twist it right open like a jam jar. And end up with a crumpled mess of tin foil, and mincemeat made of what's in there."
    hide redd_m with moveoutright

    show tequila_m at my_moveinright
    tequila "Are you two getting up to some tomfoolery? For once I need to witness this myself."
    greyson "Nothing of questionable safety, sad to say. Though to some of us, that comes as a relief."
    hide greyson_r with moveoutleft

    show redd_m_r at my_moveinleft
    redd "Some of us need to stay sensible.{p}\nThough not so much as to spoil {i}all{/i} the fun..."

    hide redd_m_r with moveoutleft
    hide tequila_m with moveoutright
    hide typewriter

    $ gui.custom.textbox_position = "left"

    jump lockbox_start