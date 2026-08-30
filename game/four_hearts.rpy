define swave = ImageDissolve("imagedissovle wave.png", 1.0, 124)

#we do a little trolling
image butterfly animated:
    "butterfly1"
    pause .05
    "butterfly2"
    pause .025
    "butterfly3"
    pause .025
    "butterfly4"
    pause .025
    "butterfly5"
    pause .05
    "butterfly4"
    pause .025
    "butterfly3"
    pause .025
    "butterfly2"
    pause .025
    repeat

image butterfly_r animated:
    "butterfly_r3"
    pause .025
    "butterfly_r2"
    pause .025
    "butterfly_r1"
    pause .05
    "butterfly_r2"
    pause .025
    "butterfly_r3"
    pause .025
    "butterfly_r4"
    pause .025
    "butterfly_r5"
    pause .05
    "butterfly_r4"
    pause .025
    repeat

image abutterfly animated:
    "abutterfly2"
    pause .025
    "abutterfly1"
    pause .05
    "abutterfly2"
    pause .025
    "abutterfly3"
    pause .025
    "abutterfly4"
    pause .025
    "abutterfly5"
    pause .05
    "abutterfly4"
    pause .025
    "abutterfly3"
    pause .025
    repeat

image abutterfly_r animated:
    "abutterfly_r4"
    pause .025
    "abutterfly_r3"
    pause .025
    "abutterfly_r2"
    pause .025
    "abutterfly_r1"
    pause .05
    "abutterfly_r2"
    pause .025
    "abutterfly_r3"
    pause .025
    "abutterfly_r4"
    pause .025
    "abutterfly_r5"
    pause .05
    repeat


image bbutterfly animated:
    "bbutterfly3"
    pause .025
    "bbutterfly4"
    pause .025
    "bbutterfly5"
    pause .07
    "bbutterfly4"
    pause .025
    "bbutterfly3"
    pause .025
    "bbutterfly2"
    pause .025
    "bbutterfly1"
    pause .07
    "bbutterfly2"
    pause .025
    repeat

image bbutterfly_r animated:
    "bbutterfly_r5"
    pause .07
    "bbutterfly_r4"
    pause .025
    "bbutterfly_r3"
    pause .025
    "bbutterfly_r2"
    pause .025
    "bbutterfly_r1"
    pause .07
    "bbutterfly_r2"
    pause .025
    "bbutterfly_r3"
    pause .025
    "bbutterfly_r4"
    pause .025
    repeat

default four_hearts.puzzle_text = "La fée verte - that is all.\n\nAb s ntt? A b s in? A n thee?"

default four_hearts.answer = "absinthe"
default four_hearts.secret = "trinity"

default four_hearts.asked_willow = False
default four_hearts.asked_tequila = False

default four_hearts.solved = False
default four_hearts.secret_solved = False 

default four_hearts.input = ""

init python:
    def check_four_hearts_answer():
        if four_hearts.input.strip().casefold() == four_hearts.answer:
            four_hearts.solved = True
            renpy.jump( "four_hearts_process_answer" )
        elif four_hearts.input.strip().casefold() == four_hearts.secret:
            four_hearts.secret_solved = True
            renpy.jump( "four_hearts_process_secret" )

screen four_hearts_name:
    frame:
        xpos 0.6
        ypos 0.25
        style "frame_fancy"
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            label "La Fée Verte":
                text_size gui.text_size
            input:
                value VariableInputValue( variable = "four_hearts.input" )
            textbutton "Check Answer":
                style "button_input"
                xalign 0.5
                action Function( check_four_hearts_answer )

label four_hearts_start:
    $ flag_quiz = True
    $ gui.custom.textbox_position = "centre"

    play music "OminousTheme.mp3" fadein 1.5
    scene bg stage with swave
    show plant1 at plant_right with swave
    show plant2s at plant_left with swave
    show plant2 at plant_slightright with swave
    show plant1s at plant_slightleft with swave
            
    show bbutterfly animated:
        parallel:
            linear 5.9 xalign 1.0
            linear 5.7 xalign 0.0
            repeat
        parallel:
            linear 4.2 yalign 0.0
            linear 5.9 yalign 1.0
            repeat
            
    show bbutterfly_r animated:
        parallel:
            linear 6.2 xalign 0.0
            linear 5.0 xalign 1.0
            repeat
        parallel:
            linear 5.9 yalign 1.0
            linear 4.2 yalign 0.0
            repeat

    show butterfly animated:
        parallel:
            linear 6.0 xalign 0.0
            linear 6.0 xalign 1.0
            repeat
        parallel:
            linear 5.5 yalign 1.0
            linear 4.0 yalign 0.0
            repeat


    show butterfly_r animated:
        parallel:
            linear 6.0 xalign 1.0
            linear 6.0 xalign 0.0
            repeat
        parallel:
            linear 4.0 yalign 0.0
            linear 5.5 yalign 1.0
            repeat

            
    show abutterfly animated:
        parallel:
            linear 6.0 xalign 1.0
            linear 6.2 xalign 0.0
            repeat
        parallel:
            linear 5.5 yalign 1.0
            linear 4.2 yalign 0.0
            repeat
            
    show abutterfly_r animated:
        parallel:
            linear 6.2 xalign 0.0
            linear 6.0 xalign 1.0
            repeat
        parallel:
            linear 4.0 yalign 0.0
            linear 5.1 yalign 1.0
            repeat


    show fourhearts upset at my_moveinright
    four "...ugh."
    
    show fourhearts
    four "{cps=20}Finally{/cps}. {i}Somebody{/i} saw fit to show up."
    
    four "What even took you so long? You had {i}Trinity{/i} with you, for God's sake."
    show trinity_m_r at my_moveinleft
    trinity "Good to see my reputation precedes me as usual."
    hide trinity_m_r with moveoutleft
    show clay_m_r sober at my_moveinleft
    clay "Excuse me... Were you expecting us?"
    show fourhearts upset
    four "You first. Were you expecting me? Or not?"
    clay "I've got no expectations at this point. Aside from more tosh from this barmy old contraption -"

    show typewriter with vpunch
    tp "{cps=[cps]}I c an hee r y u, yo kn ww{/cps}"

    four "I'm that bloody well out of the loop, am I? I suppose I should have expected no less."
    hide clay_m_r sober with moveoutleft
    show trinity_m_r at my_moveinleft
    trinity "Then what are you in here for, anyhow? Hiding out to give us a laugh?"
    four "To pop you a quiz, apparently. And play nanny to the {i}world's deadliest spider{/i}, or so it says on its terrarium. I had better be in for one monumental bonus."
    trinity "What do we get if we win?"
    four "That's for me to know until it becomes relevant.{p}\n\"La fée verte\" - that's the quiz. And that's all I'm permitted to say."

    show typewriter with vpunch
    tp "{cps=[cps]}Ab s ntt{/cps}"

    four "Absent? Yes, the Marquis most certainly is. And downright impossible, but that goes without saying."

    tp "{cps=[cps]}A b s in{/cps}"

    hide trinity_m_r with moveoutleft
    show clay_m_r sober at my_moveinleft

    clay "Abstain? Damn right I do when I'm on the job!"

    hide clay_m_r sober with moveoutleft

    tp "{cps=[cps]}A n thee{/cps}"

    show tequila_m_r at my_moveinleft
    tequila "Oh, say can you see - no, I don't reckon it's my national anthem -"

    hide fourhearts with moveoutright 
    hide tequila_m_r with moveoutleft

    $ gui.custom.textbox_position = "left"

    jump four_hearts_menu

label four_hearts_menu:
    #n "You have [turns] turns left."
    if turns == 20:
        tp "W e do 't hav e much t me. Hurry."
    if turns == 15:
        n "The typewriter seems rather restless."
    if turns == 10:
        n "The typewriter is clacking worryingly..."
    if turns == 5:
        tp " T'S TOO LAT E. W E'R E DOOM ED. RU ."
        n "...should you worry?"
    if turns < 1:
        jump gameover
    menu:
        "[four_hearts.puzzle_text]"
        "That's French - that much is clear. Anyone care to translate?":
            $ turns -= 1
            jump four_hearts_willow
        "Does this verdant spirit sound familiar?" if four_hearts.asked_willow:
            $ turns -= 1
            jump four_hearts_tequila
        "I may have enough of a clue -":
            $ turns -= 1
            jump four_hearts_give_answer

label four_hearts_willow:
    show willow_m at my_moveinright
    willow "That one's easy. \"The Green Fairy.\" Like the spirit - that is, the drink - or like a certain someone here of my acquaintance, yes?"
    hide willow_m with moveoutright
    show trinity_m at my_moveinright
    trinity "As I said, my reputation precedes me."
    hide trinity_m with moveoutright
    if not four_hearts.asked_willow:
        $ four_hearts.puzzle_text += "\n\n\"The Green Fairy\" - a name for an alcoholic drink, or a guest with a winged mask"
        $ four_hearts.asked_willow = True
        $ turns -= 1
    jump four_hearts_menu

label four_hearts_tequila:
    show tequila_m at my_moveinright
    tequila "I had it once. That was way more than plenty. It went right to my head and knocked me down flat. Even the name of it almost sets me to spinning.{p}\n{b}Ab{/b}solutely {b}sin{/b}ful, that stuff."
    hide tequila_m with moveoutright
    if not four_hearts.asked_tequila:
        $ four_hearts.puzzle_text += "\n\n{b}Ab{/b}solutely {b}Sin{/b}ful, says Tequila"
        $ four_hearts.asked_tequila = True
        $ turns -= 1
    jump four_hearts_menu

label four_hearts_give_answer:
    show screen four_hearts_name
    menu( screen="choice_h" ):
        "[four_hearts.puzzle_text]"
        "Back to Clues":
            hide screen four_hearts_name
            jump four_hearts_menu

label four_hearts_process_answer:
    $ gui.custom.textbox_position = "centre"
    hide screen four_hearts_name
    show fourhearts at my_moveinright
    four "Congratulations."
    show trinity_m_r at my_moveinleft
    trinity "...appreciated?"
    four "To me, since I get to leave. To where, I don't know.{p}\nTo tender my resignation, if that bonus isn't forthcoming."
    trinity "And the prize? Or whatever it is we're meant to win."
    four "My begrudging respect, or a speck thereof. And this token of appreciation, literally."
    hide trinity_m_r with moveoutleft
    show aurum_m_r at my_moveinleft
    aurum "Redeemable for one house specialty. From the back bar - lucky us."

    show typewriter with vpunch
    tp "{cps=[cps]}Lu kyy me! I mu sst we t m yy whi s le str ighh t aw y{/cps}"

    aurum "Oil your sprockets, so to speak... er... type? If that is what it takes - however that even works -"

    tp "{cps=[cps]}As k A cee. Wh t he g nne d u p. Un f or ge t a bbl !{/cps}"

    hide aurum_m_r with moveoutleft

    four "Then that's that. I played my part. I can't say it's been a pleasure.{p}\nSay hello to the Ace of Spades for me, will you? Au revoir."
    hide four with moveoutright

    $ gui.custom.textbox_position = "left"

    jump cocktail_start

label four_hearts_process_secret:

    $ gui.custom.textbox_position = "centre"
    hide screen four_hearts_name

    $ card_index = 1
    $ card_images_found[ card_index ] = True
    $ card_image = card_images[ card_index ]

    show expression [card_image] as card at screen_centre with spiral
    pause
    hide card

    show fourhearts upset at my_moveinright
    four "Here you are. A secret card. I suppose you've properly earned this."
    
    show trinity_m_r at my_moveinleft
    trinity "Don't sound too thrilled at my victory."
    four "You guessed your name. How victorious was that?"
    trinity "My name was the answer. I declare that a win."
    four "Only if you insist, madam."

    hide fourhearts upset with moveoutright
    hide trinity_m_r with moveoutleft

    $ gui.custom.textbox_position = "left"
    
    jump four_hearts_menu

