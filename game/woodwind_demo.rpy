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

default woodwind.redd_hint = "Woodwinds - flute, clarinet, oboe, saxophone, bassoon, bagpipe, ocarina"

default woodwind.input = ""

default woodwind.answer = "bassoon"
default woodwind.secret = "windbag"

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
    thanos "Ah, the delights of linguistics, though rather more expected through this barrier. \"Cheers\", he means. \"Raise a toast.\"{p}\nAfter this scavenger hunt is sorted, perhaps..."
    hide thanos with moveoutright

    show willow_m at my_moveinright
    willow "Mr. Minski, where should we go with this one?"

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

    menu:
        "[woodwind.puzzle_intro]\n\n[woodwind.puzzle_text]"
        "This verse seems rather oddly repetitive.":
            jump woodwind_thanos
        "What's the deal with all these oughts? Perhaps there's a clue in the calligraphy?" if woodwind.asked_thanos:
            jump woodwind_willow
        "Woodwind, eh? Redd, if you could - some examples would be instrumental -" if not woodwind.solved and not woodwind.secret_solved:
            jump woodwind_redd
        "I think I've got it well enough to have a gander." if not woodwind.solved:
            jump woodwind_give_answer
        "There might be more around here worth poking at -" if woodwind.solved and not woodwind.secret_solved:
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
    redd "Off the top of my head - or rather from a good look around -\n{p}Flute, clarinet, oboe. Saxophone, bassoon.{p}\nOcarina and bagpipe - those too. And they all sound like an unfortunate goose, at least the ones I've ever tried my hand at."
    show thanos_r at my_moveinleft
    thanos "A bagpipe? In here? That doesn't seem so acoustically wise."
    hide redd_m with moveoutright
    show aurum_m at my_moveinright
    aurum "That doesn't seem so wise at all, with that stained glass mural just built. One banger of a note and -"
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
    show thanos_r at my_moveinleft
    thanos "Why that choice of instrument in particular? That display cabinet doesn't conceal any secret that I'm privy to. Though perhaps it did - past tense being the operative here. And here we are, in the here and now, on the hunt for wild geese."
    redd "If that's what we're after, I can give it a good honk and declare victory."
    thanos "With the utmost caution, I trust."
    hide redd_m with moveoutright 
    hide thanos_r with moveoutleft
    "To be continued when we sort the solution..."
    $ gui.custom.textbox_position = "left"
    jump cardsuit_start

label woodwind_process_secret:
    hide screen woodwind_name
    "Indeed, the Marquis is a windbag, and considers such to be a point of pride.{p}
    \n\nA card was tucked under the tartan bag of the Great Highland bagpipe." 
    jump woodwind_menu

label woodwind_exit:
    jump woodwind_menu
