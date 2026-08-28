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
    

    $ found_card1 = False
    $ found_card2 = False
    $ found_card3 = False
    $ found_card4 = False

    n "This is a fangame dedicated to {b}The Sexy Brutale{/b}.\nAll featured characters are the property of {b}Tequila Works{/b} and {b}Cavalier Game Studios{/b}."

    scene bg room with spiral

    play music "SlowTheme.mp3" fadein 2.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "lafcadio happy.png" to the images
    # directory.

# Variables!

    $ gui.custom.textbox_position = "centre"

    n "Another year, another masquerade ball at the Sexy Brutale casino mansion. A show grandly run by the Marquis Lucas Bondes, a gambler dealing in luxuries and rarities and his own form of full house theater."
    n "First editions and last manuscripts. Old masters and avant garde abstracts. Musical acts and magic shows, and an exclusive list of guests apt to bring their own surprises beyond what the Marquis had in store."
    n "Such as a dealer in arcane antiquities who found herself in possession of a battered old typewriter..."

    stop music fadeout 1.5

    scene bg casino with spiral

    show willow_m at my_moveinright
    willow "Lafcadio! I have something here that could use a second look."
    willow "It's a ghost needing spiritual guidance. More than I can give, it seems."

    hide willow_m with moveoutright
    play music "MainTheme.mp3" fadein 0.5

    show typewriter with moveintop
    show typewriter with vpunch

    n "With a metallic {i}thud{/i}, the typewriter plopped down on the worn inlaid table.\n\nIn it was jammed a piece of paper spelling \"H ELP\".\n\nSomehow, it almost looked sympathetic."

    show willow_m at my_moveinright #at right

    willow "I present Alexander Minski, \"The Thunderous\". A notorious Russian dealer in diamonds, and a mainstay on the Marquis' guest list. Or he was, in his long past distant time."
    show thanos_r at my_moveinleft 
    thanos "\"The Cruel\", you mean. {p}\nThat is the true translation of his title, and also how I most unfortunately recall him. {p}\nBut go on."
    willow "Yes. {w}He died of a rare form of jaw cancer. Rare enough that he's mute, even after taking leave of his earthly body.{p}\nHe can only communicate by typing - as well as he can manage with this relic -"
    hide thanos_r with moveoutleft
    show reggie_m_r at my_moveinleft 
    reggie "{cps=20}Oh dear...{/cps} This typewriter. It's a classic...and it's rubbish! \n{p}Oh, you poor mistreated machine. I'll get you sorted in my workshop straight away!"
    willow "How straight away would that be?"
    reggie "Perhaps two hours - perhaps four - perhaps more. I'm afraid I can't say without a thorough disassembly."
    willow "Then I'm afraid that will all have to wait. Mr. Minski is in somewhat of a hurry."
    hide reggie_m_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "Of course he is. Never a whit of patience."
    hide thanos_r with moveoutleft
    show aurum_r at my_moveinleft
    aurum "What's the hurry? Where's the chill? Relax, old chap. You'll always have a seat at the Marquis' tables."
    hide aurum_r with moveoutleft
    show willow_m thinking
    willow "He insisted we find something..."
    show greyson_r at my_moveinleft
    greyson "A diamond?"
    show willow_m
    willow "Maybe that, maybe not. Something important, yes, in any case. We had a look around, but came up empty."
    greyson "And you didn't think to ring me in? Did you expect I'd nick it all? I might skim a touch off the top, but -"
    willow "We were pressed for time, as I mentioned. And it seems we still are."
    greyson "Then what's the wait? Point me in a direction, and off I'll go. I might get into a bit of a pickle - or a jam - but I'll get out straight away, or rather Redd will -"
    show willow_m thinking
    willow "That's the rub. The direction. So far, this is all we have to go on."
    show willow_m

    show typewriter with vpunch
    tp "F D LUCAS"

    greyson "Flaming Daft Lucas? Spot on."
    hide greyson_r with moveoutleft

    show redd_m_r at my_moveinleft
    redd "A game of anagrams, perhaps? Scald, laud, clad, calf - I'm not seeing much here to go on -"
    hide redd_m_r with moveoutleft

    show clay_m_r sober at my_moveinleft
    clay "Come on, bruv. Don't hurt yourself thinking. It's just missing letters.{p}\n\"Feed Lucas\", innit? Right. Sorted.{p}\nThough we would have to find him to feed him..."
    willow "That does seem to be the implication, yes.{p}\nThe finding part, that is. Mr. Minski hasn't been forthcoming with a menu."
    hide clay_m_r sober with moveoutleft

    show reggie_m_r at my_moveinleft 
    reggie "Did he say why we're pressed for time? Is there an event he needs this for? A limit to his ghostly vigor? Or is he more so apt to run out of ink?{p}\nI might have a spare ribbon handy -"
    willow "He said the limit is noon. He didn't say why, no. Just some business about ''hiding behind seven locks''."
    hide reggie_m_r with moveoutleft
    show greyson_r at my_moveinleft
    greyson "I'd have those cracked before second breakfast, if not for that matter of needing direction."
    hide greyson_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "I wouldn't be so flagrantly confident. \"Behind seven seals\", he means. Yet again with the Russian idioms as always."
    hide willow_m with moveoutright
    hide thanos_r with moveoutleft

    show trinity_m at my_moveinright
    trinity "So we've already begun with the party games? What a time to be fashionably late."
    show redd_m_r at my_moveinleft
    redd "We're rather just getting sorted."
    trinity "Oh, so we're choosing teams? Or partners? What skills are we testing? I wonder what's to be won -"
    redd "The game is ghost whispering. The prize is - unspecified. Perhaps just a \"Good Show\" if we crack what it is that he's on about?"
    trinity "Fair enough, I suppose. It is a lark, if nothing else.{p}\nHow about it, Laffy? \nFancy a game of Ghost Detective?"

    #"Rydain" "That's where I left off for now. More to come!"

    menu:
        "You won't leave me any real choice, will you?":
            jump adventure_start
        "DEBUG : Test the final puzzle":
            hide redd_m_r with moveoutleft
            hide trinity_m with moveoutright
            jump cardsuit_start
            
        #if possible, implement a few gates allowing to skip puzzles player already completed. 
        #The maximum allowed amount of turns is going to come into play here.

label adventure_start:
    hide redd_m_r with moveoutleft
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
    scene bg foyer with wave
    show fourhearts upset at my_moveinright
    four "...ugh."
    show fourhearts
    four "{cps=20}{i}Finally{/i}{/cps}. {i}Somebody{/i} showed up."
    four "What even took you so long? You had {i}Trinity{/i} with you, for God's sake."
    show clay_m_r sober at my_moveinleft
    clay "Excuse me... Were you expecting us?"
    show fourhearts upset
    four "Oh, so you're telling me not informing guests of the arrangement is part of the attraction?"
    four "And what about me, then? Was I expected to spend the whole day in this greenhouse, locked up with the {i}world's deadliest spider{/i}, waiting until you'll figure out where to go?"
    four "I swear to God, I am {i}resigning{/i}. The Marquis is {i}truly{/i} impossible."
    hide clay_m_r sober with moveoutleft
    show trinity_m_r at my_moveinleft
    trinity "Oh, cheer up. We're here {i}now{/i}. At least entertain us one last time before you leave this circus for good."
    show fourhearts
    four "Alright, I suppose... I was put here to give you directions as to where go next. Didn't think I'd be the first in line, though."
    four "You need to say the correct password. The only clue I'm allowed to give you is \"la fée verte\"."
    trinity "Huh. Was entering the room not enough?"
    show fourhearts upset
    four "For Lucas? Apparently not."

    "Harpy" "More to come!"

# So- This is where the type-in-the-word puzzle is to be implemented.
#Say Absinthe to go further, 
#Say Trinity (I mean, doesn't she look like a green fairy), and get a card.


# Somebody speaking French could give a hint on the translation.
# Somebody smart could 'spelling bee' the absinthe if the player fails +3 times 

# In Russian, the drink is called "Absent".
# Feel free to use it as an immediate hint.


#After receiving correct answer:
label adventure_after_spider_room:
    four "Absinthe is the correct answer — which means you've proven you deserve your next directions, and I deserve to get the hell out of here."
    n "Four of Hearts produced a copper tumbler out of the glass tray. A peculiar item appeared chill to the touch."
    tp "A Moscow Mul e! Lucas, that dog!"
    tp "    ow e xac ly wha  h e wan s from us."
    four "I played my part now. Can't say it's been a pleasure."
    four "Say hi to Ace of Spades for me, will you? \nAu revoir."

    aurum "Ace of Spades? we gotta head to What's Your Poison, then."
    Willow "Good thing Lucas can't talk to ghosts — at least there will be no challenges getting into the bar."
   

    stop music fadeout 0.5

    n "Wow, that was an adventure!"
    $ turns_taken = 25-turns
    n "You managed in [turns_taken] turns, too. \nGood job!"

#Inside of the spider room : play OminousTheme, bg foyer, show FourHearts upset
#Do a woodwind-esque puzzle where the player is asked to say a code word to proceed. I was planning to implement a "green fairy" (absinthe) as an answer. Note that Four Hearts really wants to get out of the spider room and won't make it more difficult that it's required to be. Ghost may repeatedly misstype it while trying to give an answer/hint
#Player receives a password/item they present to the Ace of Spades. The rest of the minigame follows.





#Post minigame, transition into your box puzzle.

#Post box puzzle, transition into woodwind.

    clay "What now, a poem?\nSomebody oughta tell Lucas it's far too high-brow to jump straight into fine arts after heavy drinking."
    tequila "Oh, Lucas, what a tease."
    greyson "Figured out something?"
    tequila "He's luring me right onto my stage."
    tequila "Boys, I'm calling dibs on breaking glass if the solution calls for it."



# If Dani/I get the sprites for it on time, it might be worth the hustle to implement it as "click on the right instrument" (partially reusing the numpad's implementation)
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
            "Card Suit":
                jump cardsuit_start

    #Select 
    label end:
        n "This concludes the game. Thank you for playing!"
        n "{b}Developer team!{/b}\nProgrammer and writer : Rydain\nArtist and game designer : TheNorthernHarpy\nBackground artist : NostalgicTree\nMusic : fionnectomy"
        
        n "...Would you like to find out how the story ended?\nPlay our source material, {b}The Sexy Brutale!{/b}"

    # This ends the game.

    return
