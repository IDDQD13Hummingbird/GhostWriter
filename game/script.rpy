# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters!

define tp = Character("Typewriter Ghost", window_background=Frame( "gui/custom/TypewriterGhost_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/TypewriterGhost_namebox.png", gui.namebox_borders ) ) 
define ace = Character("Ace of Spades", window_background=Frame( "gui/custom/Tequila_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Tequila_namebox.png", gui.namebox_borders ), what_justify = True )
define king = Character("King of Clubs", window_background=Frame( "gui/custom/Tequila_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Tequila_namebox.png", gui.namebox_borders ), what_justify = True )
define four = Character("Four of Hearts", window_background=Frame( "gui/custom/Tequila_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Tequila_namebox.png", gui.namebox_borders ), what_justify = True )
define two = Character("Two of Diamonds", window_background=Frame( "gui/custom/Tequila_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Tequila_namebox.png", gui.namebox_borders ), what_justify = True )
#I love the little guys, so all of them have an "upset" skin now

define aurum = Character("Aurum", window_background=Frame( "gui/custom/Aurum_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Aurum_namebox.png", gui.namebox_borders ), what_justify = True )
define clay = Character("Clay", window_background=Frame( "gui/custom/Clay_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Clay_namebox.png", gui.namebox_borders ), what_justify = True )
define greyson = Character("Greyson", window_background=Frame( "gui/custom/Greyson_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Greyson_namebox.png", gui.namebox_borders ), what_justify = True )
define lafcadio = Character("Lafcadio", window_background=Frame( "gui/custom/Lafcadio_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Lafcadio_namebox.png", gui.namebox_borders ), what_justify = True )
define redd = Character("Redd", window_background=Frame( "gui/custom/Redd_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Redd_namebox.png", gui.namebox_borders ), what_justify = True )
define reggie = Character("Reggie", window_background=Frame( "gui/custom/Reggie_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Reggie_namebox.png", gui.namebox_borders ), what_justify = True )
define tequila = Character("Tequila", window_background=Frame( "gui/custom/Tequila_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Tequila_namebox.png", gui.namebox_borders ), what_justify = True )
define thanos = Character("Thanos", window_background=Frame( "gui/custom/Thanos_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Thanos_namebox.png", gui.namebox_borders ), what_justify = True )
define trinity = Character("Trinity", window_background=Frame( "gui/custom/Trinity_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Trinity_namebox.png", gui.namebox_borders ), what_justify = True )
define willow = Character("Willow", window_background=Frame( "gui/custom/Willow_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), namebox_background=Frame( "gui/custom/Willow_namebox.png", gui.namebox_borders ), what_justify = True )

define n = Character( None, window_background=Frame( "gui/custom/Tequila_frame.png", gui.custom.frame_xcorner, gui.custom.frame_ycorner ), what_justify = True, what_size=33 )


define spiral = ImageDissolve("imagedissovle spiral.png", 0.5, 64)

define wave = ImageDissolve("imagedissovle wave.png", 1.0, 64)

# Variables!

default cps = 25

transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0


transform left:
    xalign 0.15
    yalign 1.0
transform right:
    xalign 0.85
    yalign 1.0

transform centre:
    xalign 0.5
    yalign 1.0

transform my_moveinleft:
    xalign -0.5 yalign 1.0
    linear 0.5 xalign 0.05
    pause 0.5

transform my_moveinright:
    xalign 1.5 yalign 1.0
    linear 0.5 xalign 0.95
    pause 0.5

transform my_moveoutleft:
    xalign 0.05 yalign 0.0
    linear 0.5 xalign 0.0
    pause 0.5
    
 
transform my_moveoutright:
    xalign 0.95 yalign 0.0
    linear 3.0 xalign 1.0
    pause 0.5
    
transform screen_centre:
    xalign 0.5
    yalign 0.5

# Inline zoom imagebutton upon declaration with at button_zoom( whatever )

transform button_zoom( amount ):
    zoom amount
    
# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ turns = 25

    scene bg room with spiral

    play music "SlowTheme.mp3" fadein 2.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "lafcadio happy.png" to the images
    # directory.

    #"Do you need a demo/tutorial?"

    
# Variables!

    # menu:

    #     "Yes":
    #         jump tutorial_yes
    #     "No":
    #         jump tutorial_no

    # label tutorial_yes:

    #     show lafcadio happy at slightleft

    #     # These display lines of dialogue.

    #     lafcadio "You've created a new Ren'Py game."

    #     lafcadio "Once you add a story, pictures, and music, you can release it to the world!"

    #     lafcadio "Do you like visual novels with choices?"

    #     menu:

    #         "Yes, I do.":
    #             jump choice1_yes

    #         "No, I don't.":
    #             jump choice1_no

    #     label choice1_yes:

    #         $ menu_flag = True

    #         "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

    #         jump choice1_done

    #     label choice1_no:

    #         $ menu_flag = False

    #         "Games without menus are called kinetic novels, and there are dozens of them available to play."

    #         jump choice1_done

    #     label choice1_done:

    #         # ... the game continues here.


    #     lafcadio "For example, we might want to have text that is {b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, or {u}underlined{/u}."
        
    #     lafcadio "The size tag changes the size of text. It can make text {size=+10}bigger{/size} or {size=-10}smaller{/size}, or set it to a {size=30}fixed size{/size}."
 
    #     lafcadio "The cps text tag {cps=25}makes text type itself out slowly{/cps}, even if slow text is off."

    #     lafcadio "The cps tag can also be relative to the default speed, {cps=*2}doubling{/cps} or {cps=*0.5}halving{/cps} it."

    #     lafcadio "The k tag changes kerning. It can space the letters of a word {k=-.5}closer together{/k} or {k=.5}farther apart{/k}."

    #     lafcadio "The p tag breaks a paragraph,{p}and waits for the player to click."

    #     lafcadio "If it is given a number as an argument,{p=1.5}it waits that many seconds."
 
    #     lafcadio "The w tag also waits for a click,{w} except it doesn't break lines,{w=.5} the way p does."

    #     lafcadio "To break a line without pausing,\none can write \\n. \\' and \\\" include quotes in the text."
    
    #     $ variable = "{i}variable value{/i}"

    #     lafcadio "For example, this displays the [variable]."
 
    #     lafcadio "When the variable name is followed by !q, special characters are quoted. This displays the raw [variable!q], including the italics tags."
 
    #     $ translatable = _("translatable text")

    #     lafcadio "When the variable name is followed by !t, it is translated to [variable!t]. It could be something else in a different language."
 
    #     lafcadio "Finally, certain characters are special. [[, {{, and \\ need to be doubled if included in text. The %% character should be doubled if used in dialogue."
 
    $ gui.custom.textbox_position = "centre"

    #     hide lafcadio
    #    lafcadio "Tutorial done."
    n "And so, it was time for another annual masquerade at the premises of The Sexy Brutale casino mansion."
    n "With it's impressive rooms filled with exquisite oddities, gracious music and mysteriously dressed guests, it was hard to hold back anticipation for what surprises Marquis would prepare for them this year."
    n "And when antique dealer rushed into the room with a half-beaten typewriter, it was evident that Marquis didn't forget to deliver."

    stop music fadeout 1.5

    scene bg casino with spiral

    show willow_m at my_moveinright #at right
    willow "Lafcadio! May I have you?"
    willow "Certain troubled ghost requires your spiritual guidance."

    hide willow_m with moveoutright
    play music "MainTheme.mp3" fadein 0.5

    show typewriter with moveintop
    show typewriter with vpunch
    

    n "With a loud {i}thud{/i}, the archaic machine plopped onto the table. \nIn it was jammed a single piece of paper, \nspelling \"H ELP\".\n\nSomething about it almost felt sympathetic."

    show willow_m at my_moveinright #at right

    willow "To your attention, Alexander Minski \"The Thunderous\", a former attende that goes the long way back with the mansion."
    show thanos_r at my_moveinleft #at left
    thanos "You mean, \"The Cruel\". {p}That was the official adaptation of his title. {p}But go on."
    willow "Yes. So. {w}He has succumbed to a terrible jaw and mouth cancer, and is therefore, unfortunately, mute.{p}The only way for him to communicate right now is through the analog means."
    hide thanos_r with moveoutleft
    show reggie_m_r at my_moveinleft #at left
    reggie "{cps=20}Oh dear... This typewriter... it's garbage! \n{size=-10}{cps=*0.5}Oh, poor machine..!{/cps}{/size}{/cps}"
    hide reggie_m_r with moveoutleft
    show willow_m thinking
    willow "...me and the ghost couldn't locate anything better in the time we were given."
    show greyson_r at my_moveinleft
    greyson "Come again? There's a time limit?"
    show willow_m
    willow "I couldn't piece out {i}exactly{/i} why, but mr. Minski assured me that we - and by that he means {i}all{/i} of us - only have until noon to resolve the issue."
    greyson "If I dare ask, {i}what{/i} does your ghost expect us to do?"
    show typewriter with vpunch
    tp "F D LUCAS"
    hide greyson_r with moveoutleft
    show clay_m_r sober at my_moveinleft
    clay "Uh-h... Feed?... Lucas?"
    willow "I believe he implies we must find him. And, from what I've gathered, it will be no easy feat. Lucas is ''hiding behind seven locks''."
    hide clay_m_r sober with moveoutleft
    show greyson_r at my_moveinleft
    greyson "...!"
    hide greyson_r with moveoutleft 
    show thanos_r at  my_moveinleft
    thanos "No, {i}not{/i} literally. \nIt's a Russian idiom, to the effect of ''behind seven seals''. \nMore familiar with that one?"
    #thanos"...achem. Which is to say, Willow's interpretation is right - he must be well hidden."
    show willow_m thinking
    willow "...we might get lost in translations, it seems."
    #show willow at slide_right
    hide willow_m with moveoutright
    hide thanos_r with moveoutleft
    show trinity_m at my_moveinright #at right
    trinity "O-oh! All of this sounds mighty important! {p}What'cha say, Laffy? {p=1}Wanna play Ghost Detectives?"

    menu:
        "You're not gonna leave me any choice, are you?":
            jump adventure_start
        #if possible, implement a few gates allowing to skip puzzles player already completed. 
        #The maximum allowed amount of turns is going to come into play here.

label adventure_start:
    hide trinity_m with moveoutright
    $ gui.custom.textbox_position = "centre"
    n "The machine strained as its ghost struggled against the groaning architecture and countless mechanical mishaps."
    show typewriter with vpunch
    tp "m l "
    show typewriter with vpunch
    tp "m l  th e"
    show typewriter with vpunch
    tp "m l  th e sp d er"

    show willow_m_r at my_moveinleft

    willow "I think it says 'milk the spider'? \nEducated guess."

    show trinity at my_moveinright

    trinity "O-oh! I know exactly where we need to go, then!"

    show willow_m_r disappointed

    willow "Do you now?"

    trinity "Sooo... There is one suspiciously well-guarded room at the back of casino Clay never lets me into because of all the cowwebs-"    

    hide willow_m_r with moveoutleft

    show clay_m_r sober at my_moveinleft

    clay "Well, first of all, it's Staff Only, and I'm no longer head of security to let you break rules like you used to-"
    trinity "{size=-10}aw.{/size}"
    clay "And secondly, I can't let you wander around the Butterfly House on your own because half of all mansion's venomous critters are kept there."
    show clay_m_r happy
    clay "Surely you know that much if you pieced together the clue, ay, smartass?"
    trinity "Teehee. {p}So that means I get to visit the cool butterfly room this one time, right? {p}Right, mr. very important ghost?"
    show typewriter with vpunch
    tp "Y ES\nA D HURRY"
    hide clay with moveoutleft
    show willow_m_r disappointed at my_moveinleft 
    willow "I take that settles it, then."
    jump keypad_start

label adventure_after_keypad:

    play music "OminousTheme.mp3" fadein 1.5
    n "Wow, that was an adventure!"
    $ turns_taken = 25-turns
    n "You managed in [turns_taken] turns, too. \nGood job!"
    n "Rydain, I need to sleep, please take from here-"

#Inside of the spider room : play OminousTheme, bg foyer, show FourHearts upset
#Do a woodwind-esque puzzle where the player is asked to say a code word to proceed. I was planning to implement a "green fairy" (absinthe) as an answer. Note that Four Hearts really wants to get out of the spider room and won't make it more difficult that it's required to be. Ghost may repeatedly misstype it while trying to give an answer/hint
#Player receives a password/item they present to the Ace of Spades. The rest of the minigame follows.
#Post minigame, transition into your box puzzle.
#Post box puzzle, transition into woodwind. If Dani/I get the sprites for it on time, it might be worth the hustle to implement it as "click on the right instrument" (partially reusing the numpad's implementation)
#If we want to be evil, throw in padlock with ABBA as a final tiny insult of a puzzle.
#The last bit, I'll have to code in myself.
#Good luck! I'll be back in 12-16 hours, probably.


    jump tutorial_no

    
    label tutorial_no:
        play music "MainTheme.mp3" fadein 0.5
        "{size=55}THIS IS A TECH DEMO PUZZLE. \nDO NOT INCLUDE IN THE FINAL GAME.{/size}"
        n "Harpy : My offer is we start with the keypad puzzle, because Trinity and Reggie are already here, and maybe then move onto drink mixing with Clay and Aurum. We could throw in a painting room/aquarium puzzle somewhere in-between, if we write one. Then we can somehow lead it to woodwind puzzle, maybe with a joke that Redd had to carry Thanos up the stairs first. A different version of Padlock (that needs to be set up before entering the final area) can be used for the elevator puzzle at the end."

        menu:
            "Padlock Code":
                jump padlock_start

            "Woodwind Poem":
                jump woodwind_start

            "Keypad Code":
                jump keypad_start

            "Cocktail Break":
                jump cocktail_start

            "Lockbox":
                jump lockbox_start

    #Select 
    label end:
        "This concludes the tech demo."

    # This ends the game.

    return
