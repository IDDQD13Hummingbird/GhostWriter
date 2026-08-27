default woodwind.puzzle_text = """A double read, so to speak, for it rhymes in double time. 7 letters - lucky you!{p}
Bought far back in the early aughts\nA woodwind sought as it ought to be\nBut alas, 'twas all for nought\n'Twas nicked onstage, right from me!""" 

default woodwind.input = ""

default woodwind.answer = "bassoon"
default woodwind.secret = "windbag"

default woodwind.asked_thanos = False
default woodwind.asked_redd = False

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

    show lafcadio at centre

    lafcadio "Let's have a look at this telegram.\n{p}{cps=[cps]}[woodwind.puzzle_text]{/cps}"

    jump woodwind_menu

label woodwind_menu:

    menu:
        "[woodwind.puzzle_text]"
        "Early aughts? That's just a tad before my time. Thanos, might it be closer to yours?":
            jump woodwind_thanos
        "Woodwind, eh? Redd, if you could - some examples would be instrumental to this cipher -" if not woodwind.solved and not woodwind.secret_solved:
            jump woodwind_redd
        "I think I've got it well enough to have a gander." if not woodwind.solved:
            jump woodwind_give_answer
        "There might be more around here worth poking at -" if woodwind.solved and not woodwind.secret_solved:
            jump woodwind_give_answer
        "Select another puzzle":
            jump tutorial_no

label woodwind_thanos:
    $ gui.custom.textbox_position = "centre"
    show lafcadio happy at my_moveinleft
    lafcadio "Can you tell me more about the era it's referring to?"
    show thanos at my_moveinright
    thanos "Early aughts? That's a mere decade ago! Hardly the time of the Great War! Why, I ought to{cps=20}...{/cps}"
    thanos "{cps=20}...{/cps}double check my own calendar, it seems."
    if not woodwind.asked_thanos:
        $ woodwind.puzzle_text += "\n\nThanos has strong feelings about aughts."
        $ woodwind.asked_thanos = True
    hide thanos with moveoutright
    hide lafcadio with moveoutleft
    $ gui.custom.textbox_position = "left"
    jump woodwind_menu

label woodwind_redd:
    $ gui.custom.textbox_position = "centre"
    show lafcadio happy at my_moveinleft
    lafcadio "I understand you're the piano man, but I'd bet you're more familiar than I am. Might you name a few possibilities?"
    show redd at my_moveinright
    redd "I can orchestrate a thing or few. Flute, clarinet, oboe. Saxophone, bassoon. Bagpipe and ocarina - those too. And they all sound like an unfortunate goose, at least the ones I've ever tried my hand at."
    if not woodwind.asked_redd:
        $ woodwind.puzzle_text += "\n\nWoodwinds - flute, clarinet, oboe, saxophone, bassoon, bagpipe, ocarina"
        $ woodwind.asked_redd = True
    hide redd with moveoutright
    hide lafcadio with moveoutleft
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
    show redd at my_moveinright
    redd "Bassoon - of course - a double read denotes a double reed. Took me a moment to catch that, sad to say."
    show thanos at my_moveinleft
    thanos "Why that choice of instrument in particular? That display cabinet doesn't conceal any secret that I'm privy to. Though perhaps it did - past tense being the operative here. And here we are, in the here and now, on the hunt for wild geese."
    redd "If that's what we're after, I can give it a good honk and declare victory."
    thanos "With the utmost caution, I trust."
    hide redd 
    hide thanos 
    "To be continued when we sort the solution..."
    $ gui.custom.textbox_position = "left"
    jump woodwind_menu

label woodwind_process_secret:
    hide screen woodwind_name
    "Indeed, the Marquis is a windbag. This needs a proper clue, of course."
    jump woodwind_menu       

label woodwind_exit:
    jump woodwind_menu
