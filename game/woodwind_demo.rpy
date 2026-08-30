default woodwind.highlight = "#e1b25f"

default woodwind.poem = "Bought far back in the early aughts\nA woodwind sought as it ought to be\nBut alas, 'twas all for nought\n'Twas nicked onstage, right from me!"

default woodwind.poem_highlight = """{color=""" + woodwind.highlight + """}B{/color}ought far back in the early {color=""" + woodwind.highlight + """}a{/color}ughts
A woodwind {color=""" + woodwind.highlight + """}s{/color}ought as it {color=""" + woodwind.highlight + """}o{/color}ught to be
But alas, 'twas all for {color=""" + woodwind.highlight + """}n{/color}ought
'Twas nicked onstage, right from me!"""

# Kept separate from the poem + hints so we can continue to display it after
# the highlighted poem is revealed
default woodwind.puzzle_intro = "A double read, so to speak, for it rhymes in double time. 7 letters - lucky you!"

# Set to the poem to start with, then whatever all is revealed with hints - highlighted poem, further hints, etc.
default woodwind.puzzle_text = woodwind.poem 

default woodwind.redd_hint = "Woodwinds - flute, clarinet, bassoon, oboe, saxophone, bagpipe, ocarina"

default woodwind.input = ""

default woodwind.answer = "bassoon"
default woodwind.secret = "bagpipe"

default woodwind.asked_thanos = False
default woodwind.asked_redd = False
default woodwind.asked_willow = False

default woodwind.solved = False
default woodwind.secret_solved = False

init python:
    def check_woodwind():
        if woodwind.input.strip().casefold() == woodwind.answer:
            woodwind.solved = True
            renpy.jump( "woodwind_process_answer" )
        elif woodwind.input.strip().casefold() == woodwind.secret:
            woodwind.secret_solved = True
            renpy.jump( "woodwind_process_secret" )

    def woodwind_reinit():
        woodwind.puzzle_text = woodwind.poem 
        woodwind.input = ""

        woodwind.asked_thanos = False
        woodwind.asked_redd = False
        woodwind.asked_willow = False

        woodwind.solved = False
        woodwind.secret_solved = False

screen woodwind_name:
    frame:
        xpos 0.6
        ypos 0.25
        style "frame_fancy"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            label "Woodwind Name":
                text_size gui.text_size
            input:
                value VariableInputValue( variable = "woodwind.input" )
            textbutton "Check Answer":
                style "button_input"
                xalign 0.5
                action Function( check_woodwind )

label woodwind_start:
    $ woodwind_reinit()
    $ gui.custom.textbox_position = "centre"

    show reggie_m at my_moveinright
    
    reggie "I'd like to have a look, if I may.{p}\nIf I can't keep this lock box for research purposes..."
    reggie "{cps=20}\"[woodwind.puzzle_intro]{p}\n[woodwind.poem]\"{/cps}{p}\nIt's about an instrument - or a performance - or a shameless act of larceny -"

    show clay_m_r happy at my_moveinleft
    clay "It's a laugh is what it is. I'd almost let the bloke get away with it."
    hide clay_m_r happy with moveoutleft

    show trinity_m_r at my_moveinleft
    trinity "What do we even do with it? Ace, are you expecting a password? On that note, the Four of Hearts says hello."

    hide reggie_m with moveoutright
    show acespades at my_moveinright
    ace "I wasn't expecting Mr. Minski, if that answers it - or his particular tastes in mixology. Peculiar, but I must say delightful."

    show typewriter with vpunch
    tp "{cps=[cps]}Le ts cl i nng!{/cps}"

    hide acespades with moveoutright
    show thanos at my_moveinright
    thanos "Ah, the delights of translation, though rather more expected. \"Cheers\", he means. \"Raise a toast.\"{p}\nAfter this scavenger hunt is sorted, perhaps..."
    hide thanos with moveoutright

    show willow_m at my_moveinright
    willow "Mr. Minski, any hint of where to go with this one?"

    show typewriter with vpunch
    tp "{cps=[cps]}MUU SC H L{/cps}"

    trinity "I doubt he wants to take us all to muscle school."
    willow "And I suspect he's running short of ink."

    hide trinity_m_r with moveoutleft
    hide willow_m with moveoutright

    show reggie_m_r at my_moveinleft
    reggie "If I could just pop down to my workshop...just to see if that ink might be handy..."

    show tequila_m at my_moveinright
    tequila "We should all pop upstairs. To the music hall. Where else could he possibly be thinking?"

    hide reggie_m_r with moveoutleft
    show aurum_m_r at my_moveinleft
    aurum "That's as good a change of venue as any, right?{p}\nJust as long as I can take one for the road."

    hide tequila_m with moveoutright
    show acespades at my_moveinright

    ace "Much obliged, sir."

    hide acespades with moveoutright
    hide typewriter

    $ gui.custom.textbox_position = "left"

    scene bg instrumentroom with wave

    jump woodwind_menu

label woodwind_menu:
    $ check_turns()

    menu:
        "[woodwind.puzzle_intro]\n\n[woodwind.puzzle_text]"
        "This verse seems rather oddly repetitive.":
            $ turns -= 1
            jump woodwind_thanos
        "What's the deal with all these oughts? Perhaps there's a clue in the calligraphy?" if woodwind.asked_thanos:
            $ turns -= 1
            jump woodwind_willow
        "Woodwind, eh? Redd, if you could - some examples would be instrumental -" if not woodwind.solved and not woodwind.secret_solved:
            $ turns -= 1
            jump woodwind_redd
        "I think I've got it well enough to have a gander." if not woodwind.solved:
            $ turns -= 1
            jump woodwind_give_answer
        "There might be more around here worth poking at -" if woodwind.solved and not woodwind.secret_solved:
            $ turns -= 1
            jump woodwind_give_answer

label woodwind_thanos:
    $ gui.custom.textbox_position = "centre"
   
    show thanos_r at my_moveinleft
    thanos "Aught... ought... there's indeed quite a lot.{p}\nHa! It seems that I am a poet as well."
    show greyson at my_moveinright
    greyson "So you've cracked it, then. At least halfway."
    thanos "I've only read it halfway. Hold your horses, now, will you? Or your tongue, even better. Or better yet, go put your nosy hands to work.{p}\n{cps=20}Wherever did those cabinet keys run off to?{/cps}"
    greyson "Permission to infiltrate, straight from the architect himself. That one's going on my business cards."
    hide greyson with moveoutright
    hide thanos_r with moveoutleft

    if not woodwind.asked_thanos:
        $ woodwind.puzzle_text += "\n\nQuite a lot of oughts and aughts"
        $ woodwind.asked_thanos = True

    $ gui.custom.textbox_position = "left"
    jump woodwind_menu

label woodwind_willow:
    show willow_m at my_moveinright

    willow "It's subtle, yes? Those \"ought\" words all start with a letter penned twice over.{p}\nThere are five such letters, and the answer takes seven. But in order, they begin to spell something. Which might be close enough, if we can double some -"

    if not woodwind.asked_willow:
        $ woodwind.puzzle_text = woodwind.poem_highlight + "\n\nNote the first letter of each \"ought\""
        if woodwind.asked_redd:
            $ woodwind.puzzle_text += "\n\n" + woodwind.redd_hint
        $ woodwind.asked_willow = True

    hide willow_m with moveoutright
    jump woodwind_menu

label woodwind_redd:
    $ gui.custom.textbox_position = "centre"
    show redd_m at my_moveinright
    redd "Off the top of my head - or rather from a good look around -\n{p}Flute, clarinet, bassoon, oboe, saxophone.{p}\nOcarina and bagpipe - those too.\n\nAnd they all sound like an unfortunate goose, at least the ones I've ever tried my hand at. Piano doesn't translate to the wind bit."
    show thanos_r at my_moveinleft
    thanos "A bagpipe? In here? That doesn't seem so acoustically wise."
    hide redd_m with moveoutright
    show aurum_m at my_moveinright
    aurum "That doesn't seem so wise at all, with that stained glass mural just put in behind the stage. One banger of a note and -"
    hide aurum_m with moveoutright
    show greyson at my_moveinright
    greyson "But that is just like the Marquis, isn't it? Quite fitting, really, for such a windbag."
    thanos "As if you're one to speak of the excessive flapping of gums."
    greyson "What can I say?{p}\nIt takes one to know one, old chap."
    if not woodwind.asked_redd:
        $ woodwind.puzzle_text += "\n\n" + woodwind.redd_hint
        $ woodwind.asked_redd = True
    hide thanos_r with moveoutleft
    hide greyson with moveoutright
    $ gui.custom.textbox_position = "left"
    jump woodwind_menu

label woodwind_give_answer:
    show screen woodwind_name
    menu( screen="choice_h" ):
        "[woodwind.puzzle_text]"
        "Back to Clues":
            hide screen woodwind_name
            jump woodwind_menu

label woodwind_process_answer:
    $ gui.custom.textbox_position = "centre"
    hide screen woodwind_name
    show redd_m at my_moveinright
    redd "Bassoon - of course - a double read denotes a double reed. Took me a moment to catch that, sad to say."
    show reggie_m_r at my_moveinleft
    reggie "I don't see any buttons nearby, or switches - though perhaps the display mount is pressure sensitive -"
    hide reggie_m_r with moveoutleft

    show thanos_r at my_moveinleft
    thanos "A switch for what, though? This room doesn't hide any secrets.\n\nUnless it did - past tense being the operative here. And here we are, in the here and now, on the hunt for wild geese."
    redd "If that's what we're after, I can give it a good honk and declare victory."
    thanos "With the utmost caution, I trust."
    redd "Actually - Tequila, if you would - you're the one with the most lung power."
    hide redd_m with moveoutright 

    show tequila_m at my_moveinright

    tequila "You know, I played recorder way back when. I had a solo at the spring recital and all that. Oh, what the heck. Let's take this thing out for a toot.\n\nDon't expect I'll be any good at it, but at least I won't get hollered at for making noise inside."

    hide thanos_r with moveoutleft
    hide tequila_m with moveoutright

    "SQUEEEEEEEEEEEAK!"

    show kingclubs_r at my_moveinleft
    king "You rang? Or rather produced whatever fractured note that was."

    show twodiamonds at my_moveinright
    two "You could have just knocked. Did you not get the memo?"

    hide kingclubs_r with moveoutleft
    show reggie_m_r at my_moveinleft
    reggie "There's a memo? Somehow we all managed to miss it."
    two "It's right here in your hands. Now, where's my torch...\n\nOh dear...it fell down the bell. The full way, too. That will require some disassembly..."

    hide reggie_m_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "Not by any means whatsoever. That instrument dates to the 19th century, bespoke for the director of the Paris Conservatory.\n\nIt stays in one piece, end of story."
    two "Then that poses somewhat of a problem."

    hide thanos_r with moveoutleft
    show redd_m_r at my_moveinleft
    redd "Let me guess. That memo had some key information?"
    two "You could say that. Quite literally."

    hide redd_m_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "Please tell me that was key information you were privy to. At least partially."
    two "It's a card game, or the start of it. A set of rules for a winning hand."

    hide thanos_r with moveoutleft
    show clay_m_r happy at my_moveinleft

    clay "Not 52 Pickup? Thank hell. Then we'd really be bloody well in it."

    hide clay_m_r happy with moveoutleft
    show kingclubs_r upset at my_moveinleft

    king "It was meant to be a game, rather. It's now a - situation."

    hide twodiamonds with moveoutright
    show willow_m at my_moveinright
    show willow_m thinking

    willow "Maybe it's been a situation. And that's why Mr. Minski's been so insistent."

    show willow_m
    
    show typewriter with vpunch
    tp "{cps=[cps]}Y U G OT T AT ST RA GGHT{/cps}"
   
    willow "What exactly is this game for, anyhow?"
    show kingclubs_r
    king "For the staff door. The new one. That none of us know how to open. Only our part of the combination."
    show kingclubs_r upset
    king "Or we {i}did{/i}, before the Marquis changed it..."
    pause

    # Compute total number of cards found for subsequent dialogue.

    $cards_found = 0

    python:
        for flag in card_images_found:
            if flag:
                cards_found += 1 

    $arrangement = "Each suit is only used once. He also likes to mix up the colors. You won't see both red then both black, or vice versa."

    show kingclubs_r
    if cards_found > 0: # At least 1
        $old_combination = ""
        if card_images_found[0]:
            $old_combination = "That Jack of Diamonds wasn't in the old combination."
        else:
            $which = "any of these" if cards_found > 1 else "this one"
            $old_combination = "I don't recall " + which + " in the old combination."
        willow "So that's what's been scattered about, yes?"
        king "Perhaps. Hopefully. [old_combination] And the Marquis is in the habit of changing it entirely."
        willow "A rare bit of foresight come back to haunt him. I'll take it in the spirit he intended."
        if cards_found == 4 and not card_images_found[4]: # Jack, Queen, King, Joker
            willow "Do you suppose these might lay it all out for us?"
            king "Almost. There is a wild card.{p}\nI can't recall who'd know which one it isn't -"
        elif cards_found == 5: # The full hand!
            willow "Please tell me we managed to find them all."
            king "Five all told, so it seems so. Shall we move on, then?"
            pause
            $ gui.custom.textbox_position = "left"
            jump cardsuit_start
        willow "Is there anything else you have for us to go on?"
        king "The Marquis is most aesthetically particular. [arrangement]"
    else:
        willow "Do you know of any guidelines we could go on?"
        king "The Marquis always changes it entirely. The Jack won't be Clubs, then."
        willow "I suppose that's a semblance of a start."
        king "He's also most aesthetically particular. [arrangement]"

    hide willow_m with moveoutright
    show greyson at my_moveinright 

    greyson "Seems we'd best start with a look, then."
    king "Of course. Right this way, all."

    hide greyson with moveoutright
    hide kingclubs_r with moveoutleft

    $ gui.custom.textbox_position = "left"
    jump cardsuit_start

label woodwind_process_secret:
    hide screen woodwind_name
    "Indeed, the Marquis is a windbag, and considers such to be a point of pride."

    $ card_index = 4
    $ card_images_found[ card_index ] = True
    $ card_image = card_images[ card_index ]

    show expression [card_image] as card at screen_centre with spiral
    pause

    "A card was tucked under the tartan bag of the Great Highland bagpipe." 
    
    hide card

    jump woodwind_menu

label woodwind_exit:
    jump woodwind_menu
