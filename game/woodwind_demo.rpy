default woodwind_puzzle_text = [ 
"A double read, so to speak, for it rhymes in double time. 7 letters - lucky you!", 
"Bought far back in the early aughts\nA woodwind sought as it ought to be\nBut alas, 'twas all for nought\n'Twas nicked onstage, right from me!" 
]

label woodwind_start:

    show lafcadio at centre

    lafcadio "Let's have a look at this telegram."

    python:
        for line in woodwind_puzzle_text:
            renpy.say(lafcadio, "{cps=[cps]}[line]{/cps}")

    jump woodwind_menu

label woodwind_menu:

    python:
        woodwind_puzzle_text_all = '\n\n'.join( woodwind_puzzle_text )

    menu:
        "The telegram says: [woodwind_puzzle_text_all]"
        "Early aughts? That's just a tad before my time. Thanos, might it be closer to yours?":
            jump woodwind_thanos
        "Woodwind, eh? Redd, if you could - some examples would be instrumental to this cipher...":
            jump woodwind_redd
        "I think I've got it well enough to have a gander.":
            jump woodwind_give_answer
        "Select another puzzle":
            jump tutorial_no

label woodwind_thanos:
    show lafcadio happy at right
    lafcadio "Can you tell me more about the era it's referring to?"
    hide lafcadio
    show thanos at right
    thanos "Early aughts? That's a mere decade ago! Hardly the time of the Great War! Why, I ought to..."
    thanos "...double check my own calendar, it seems."
    hide thanos
    jump woodwind_menu

label woodwind_redd:
    show lafcadio happy at right
    lafcadio "I understand you're the piano man, but I'd bet you're more familiar than I am. Might you name a few possibilities?"
    hide lafcadio
    show redd at right
    redd "Flute, clarinet, oboe. Saxophone, bassoon. Bagpipe and ocarina - those too. And they all sound like an unfortunate goose, at least the ones I've ever thought to try my hand at."
    hide redd
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
