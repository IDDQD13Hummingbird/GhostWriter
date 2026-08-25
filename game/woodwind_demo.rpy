default woodwind.puzzle_text = """A double read, so to speak, for it rhymes in double time. 7 letters - lucky you!{p}
Bought far back in the early aughts\nA woodwind sought as it ought to be\nBut alas, 'twas all for nought\n'Twas nicked onstage, right from me!""" 

default woodwind.asked_thanos = False
default woodwind.asked_redd = False

label woodwind_start:

    show lafcadio at centre

    lafcadio "Let's have a look at this telegram.\n{p}{cps=[cps]}[woodwind.puzzle_text]{/cps}"

    jump woodwind_menu

label woodwind_menu:

    menu:
        "[woodwind.puzzle_text]"
        "Early aughts? That's just a tad before my time. Thanos, might it be closer to yours?":
            jump woodwind_thanos
        "Woodwind, eh? Redd, if you could - some examples would be instrumental to this cipher...":
            jump woodwind_redd
        "I think I've got it well enough to have a gander.":
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
    redd "Of course - I can orchestrate that sort of help. Flute, clarinet, oboe. Saxophone, bassoon. Bagpipe and ocarina - those too. And they all sound like an unfortunate goose, at least the ones I've ever tried my hand at."
    if not woodwind.asked_redd:
        $ woodwind.puzzle_text += "\n\nWoodwinds - flute, clarinet, oboe, saxophone, bassoon, bagpipe, ocarina"
        $ woodwind.asked_redd = True
    hide redd with moveoutright
    hide lafcadio with moveoutleft
    $ gui.custom.textbox_position = "left"
    jump woodwind_menu

label woodwind_give_answer:
    $ answer = renpy.input( "What is the instrument in question?", length=10 ).strip()
    if answer.casefold() == "bassoon":
        "Correct!"
        jump woodwind_exit
    else:
        "Not quite...care to give it another go?"
        jump woodwind_menu

label woodwind_exit:
    jump woodwind_menu
