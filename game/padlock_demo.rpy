default padlock_puzzle_text = [
"Th e qu ee  da c es, and so shall you",
"Sw eed sh f emal e royalty. Four l ett ers. Four umb ers."
]

default padlock_typewriter_message = ""
default padlock_attempts = 5

label padlock_start:
    show typewriter at centre
    tp "{cps=[cps]}[padlock_puzzle_text[0]]{/cps}"
    $ padlock_typewriter_message = padlock_puzzle_text[0]
    jump padlock_menu

label padlock_clarified:
    show typewriter at centre
    tp "{cps=[cps]}[padlock_puzzle_text[1]]{/cps}"

    python:
        padlock_typewriter_message = '\n\n'.join( padlock_puzzle_text )

    jump padlock_menu

label padlock_menu:
    menu: 
        "The typewriter says: [padlock_typewriter_message]"
        "Ghost, would you kindly elaborate? Even a man of the cloth can be in need of some spiritual clarity.":
            jump padlock_ghost
        "Dancing? Queen? Seems rather more of a musical concept than a newfangled variety of poker. Tequila, if you would -":
            jump padlock_tequila
        "A padlock? How? I might as well be speaking to a slot machine. Greyson, your thoughts on cracking this code?":
            jump padlock_greyson
        "Let's give this a go, shall we?":
            jump padlock_give_answer
        "All done for now - the rest is in progress!":
            jump end

label padlock_ghost:
    show lafcadio happy at centre
    lafcadio "If you'd be so kind as to clarify."
    hide Lafcadio
    jump padlock_clarified

label padlock_tequila:
    show lafcadio happy at centre
    lafcadio "What is it referencing?"
    hide Lafcadio
    show tequila at right
    tequila "You are the dancing queen~{p}Young and sweet, only seventeen~"
    tequila "Doesn't ring a bell, then, I reckon? Sounds like I should bring some disco to this stage. It's Dancing Queen by ABBA. One heck of a hit, and it still is. One heck of a thing to get unstuck from your head, too, but we'll worry ourselves with that later."
    hide tequila
    jump padlock_menu

label padlock_greyson:
    show lafcadio happy at centre
    lafcadio "I don't get what it's expecting from me."
    hide Lafcadio
    show greyson at right
    greyson "Hm... {w=.2}Actually!" 
    greyson "You know how they abstract All Cops Are Bastards down to 1312? \nI think that's what they were going for!"
    greyson "Numbers as the position of letters in the alphabet, I mean. \nNot ACAB. Of course not."
    hide greyson
    jump padlock_menu

label padlock_give_answer:
    "This padlock takes four numbers."
    $ padlock = [0, 0, 0, 0]

    $ padlock_final = "0000"
    $ padlock_correct = "1221"
    $ padlock_secret = "1312"

    $ padlock_attempt_noun = "attempts" if padlock_attempts > 1 else "attempt"

    menu:
        "Would you like to try the padlock? You have [padlock_attempts] [padlock_attempt_noun] left."
        "Yes":
            jump padlock_give_answer_entry
        "On second thought...":
            jump padlock_menu

label padlock_give_answer_entry:

    "Select the first number:"
    menu:
        "0":
            $ padlock[0] = "0"
        "1":
            $ padlock[0] = "1"
        "2":
            $ padlock[0] = "2"
        "3":
            $ padlock[0] = "3"
        "4":
            $ padlock[0] = "4"

    "Select the second number:"
    menu:
        "0":
            $ padlock[1] = "0"
        "1":
            $ padlock[1] = "1"
        "2":
            $ padlock[1] = "2"
        "3":
            $ padlock[1] = "3"
        "4":
            $ padlock[1] = "4"

    "Select the third number:"
    menu:
        "0":
            $ padlock[2] = "0"
        "1":
            $ padlock[2] = "1"
        "2":
            $ padlock[2] = "2"
        "3":
            $ padlock[2] = "3"
        "4":
            $ padlock[2] = "4"

    "Select the fourth number:"
    menu:
        "0":
            $ padlock[3] = "0"
        "1":
            $ padlock[3] = "1"
        "2":
            $ padlock[3] = "2"
        "3":
            $ padlock[3] = "3"
        "4":
            $ padlock[3] = "4"

    "Now, let's see what we have..."
    $ padlock_final = padlock[0] + padlock[1] + padlock[2] + padlock[3]
    "You dialed in [padlock_final]."

    $ padlock_attempts -= 1

    if padlock_final == padlock_correct:
        #Select 1221 as an answer
        "The lock opens!"
        jump end

    if padlock_final == padlock_secret:
        #Select 1312 as an answer
        "The lock remains closed.{p}However...!"
        show lafcadio happy at slightleft
        lafcadio "!"
        hide Lafcadio
        "A playing card fell out of the lock!"
        show greyson at slightright
        greyson "So it {i}was{/i} ACAB after all!"
        jump padlock_give_answer
    else:
        #Select wrong answer
        "The padlock remains closed."
        lafcadio "Well, that wasn't productive."
        if padlock_attempts > 0:
            jump padlock_give_answer
        else:
            lafcadio "I'd better give this one a rest for now."
            jump end