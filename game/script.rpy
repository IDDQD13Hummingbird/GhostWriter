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

transform plant_left:
    xalign 0.25
    yalign 0.825
transform plant_right:
    xalign 0.75
    yalign 0.825


transform plant_slightleft:
    xalign 0.40
    yalign 0.825
transform plant_slightright:
    xalign 0.55
    yalign 0.755

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
    linear 0.5 xalign 0.015
    pause 0.5

transform my_moveinright:
    xalign 1.5 yalign 1.0
    linear 0.5 xalign 0.985
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

# Cards!

default cards_found = 0 # To be set from card_images_found

default card_images_found = [ False, False, False, False, False ]

define card_images = [
"jack_diamonds.png",
"queen_spades.png",
"king_hearts.png",
"joker_clubs.png",
"the_fool.png"
]

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

# Variables!

    $ gui.custom.textbox_position = "centre"

    n "Another year, another masquerade ball at the Sexy Brutale casino mansion. A show grandly run by the Marquis Lucas Bondes, a gambler dealing in luxuries and rarities and his own form of full house theater."
    n "First editions and last manuscripts. Old masters and avant garde abstracts. Musical acts and magic shows, and an exclusive list of guests apt to bring their own surprises beyond what the Marquis had in store."
    n "Such as a dealer in arcane antiquities who found herself in possession of a battered old typewriter..."

    stop music fadeout 1.5

    scene bg casino with spiral
    show willow_m at my_moveinright
    willow "Lafcadio! I have something here that could use a second opinion."
    willow "It's a ghost needing spiritual guidance. More than I can give, it seems."

    hide willow_m with moveoutright
    play music "MainTheme.mp3" fadein 0.5

    show typewriter with moveintop
    show typewriter with vpunch

    n "With a metallic {i}thud{/i}, the typewriter plopped down on the worn inlaid table.\n\nIn it was jammed a piece of paper spelling \"H ELP\".\n\nSomehow, it almost looked sympathetic."

    show willow_m at my_moveinright #at right

    willow "I present Alexander Minski, \"The Thunderous\". A notorious Russian dealer in diamonds, and a mainstay on the Marquis' guest list.{p}\nOr rather he was before I was. His acquaintance is new to me."
    show thanos_r at my_moveinleft 
    thanos "\"The Cruel\", you mean. {p}\nThat is the true translation of his title, and also how I most unfortunately recall him. {p}\nBut go on."
    willow "Yes. {w}He died of a rare form of jaw cancer. Rare enough that he's mute, even after taking leave of his earthly body.{p}\nHe can only communicate by typing - as well as he can manage with this relic -"
    hide thanos_r with moveoutleft
    show reggie_m_r at my_moveinleft 
    reggie "{cps=20}Oh dear...{/cps} This typewriter. A Remington Standard 7. It's a classic...and it's rubbish! \n{p}Oh, you poor mistreated machine. I'll get you sorted in my workshop straight away!"
    willow "How straight away would that be?"
    reggie "Perhaps two hours - perhaps four - perhaps more. I'm afraid I can't say without a thorough disassembly."
    willow "Then I'm afraid that will all have to wait. Mr. Minski is in somewhat of a hurry."
    hide reggie_m_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "Of course he is. Never a whit of patience with that one."
    hide thanos_r with moveoutleft
    show aurum_m_r at my_moveinleft
    aurum "What's the hurry? Where's the chill? Relax, man. You'll always have a seat at the Marquis' tables."
    hide aurum_m_r with moveoutleft
    show willow_m thinking
    willow "He's looking for - something. He hasn't said what yet."
    show greyson_r at my_moveinleft
    greyson "A diamond?"
    show willow_m
    willow "Maybe that, maybe not. Something important, yes, in any case. We had a quick look around, but nothing seemed to ring a bell."
    greyson "And you didn't think to call me in? Did you expect I'd nick it all? I might skim a hair off the top, but -"
    willow "We were pressed for time, as I mentioned. And it seems we still are."
    greyson "Then what's the wait? Point me in a direction, and off I'll go. I might get into a bit of a pickle - or a jam. But I'll get out straight away, or rather Redd will -"
    hide willow_m with moveoutright
    show redd_m at my_moveinright
    redd "Only with the most necessary of force."
    hide redd_m with moveoutright
    show willow_m at my_moveinright
    willow "That's the rub. The direction. So far, this is all we have to go on."

    show typewriter with vpunch
    tp "F D LU CAS"

    show greyson_r at my_moveinleft
    greyson "Flaming Daft Lucas? Spot on."
    hide greyson_r with moveoutleft

    show redd_m_r at my_moveinleft
    redd "A game of anagrams, perhaps? Scald, laud, clad, calf - I'm not seeing much here to go on -"
    hide redd_m_r with moveoutleft

    show clay_m_r sober at my_moveinleft
    clay "Come on, bruv. Don't hurt yourself overthinking. It's just missing letters.{p}\n\"Feed Lucas\"? Right. Sorted.{p}\nThough we would have to find him to feed him..."
    willow "That does seem to be the implication, yes.{p}\nThe finding part, that is. Mr. Minski hasn't been forthcoming with a menu."
    hide clay_m_r sober with moveoutleft

    show reggie_m_r at my_moveinleft 
    reggie "Did he say why we're pressed for time? Is there something he needs the Marquis for? A limit to his ghostly vigor? Or is he simply apt to run out of ink?{p}\nI might have a spare ribbon handy -"
    willow "He said before noon. He didn't say why, no. Just some business about ''hiding behind seven locks''."
    hide reggie_m_r with moveoutleft
    show greyson_r at my_moveinleft
    greyson "I'd have all those cracked before elevenses, if not for that matter of needing direction."
    hide greyson_r with moveoutleft
    show thanos_r at my_moveinleft
    thanos "I wouldn't be so flagrantly confident. \"Behind seven seals\", he means, or at least some significant number thereof. The idioms strike once again."
    hide willow_m with moveoutright
    hide thanos_r with moveoutleft

    show trinity_m at my_moveinright
    trinity "So we've already begun with the party games? What a time to be fashionably late."
    show tequila_m_r at my_moveinleft
    tequila "You and me both in that sailboat. I just had to get these lyrics unstuck, and don't even think to get me started on this hairdo..."
    hide tequila_m_r with moveoutleft
    show redd_m_r at my_moveinleft
    redd "You're both right on time, I'd say. We're rather just getting sorted."
    trinity "Oh, so we're choosing teams? Or partners? What skills are we testing? I wonder what's to be won -"
    redd "The game is ghost whispering. The prize is - unspecified. Perhaps just a \"Jolly Good Show\" if we crack what it is that he's on about?"
    trinity "Fair enough, I suppose. It is a lark, if nothing else.{p}\nHow about it, Laffy? Fancy a game of Ghost Detective?"

    menu( screen="choice_h" ):
        "You won't leave me any real choice, will you?":
            hide redd_m_r with moveoutleft
            hide trinity_m with moveoutright
            jump adventure_start
        #if possible, implement a few gates allowing to skip puzzles player already completed. 
        #The maximum allowed amount of turns is going to come into play here.

label adventure_start:
    
    $ gui.custom.textbox_position = "centre"

    n "The typewriter creaked with great effort at the ghost's struggles with its assorted misalignments."

    show typewriter with vpunch
    tp "m l "
    show typewriter with vpunch
    tp "m l  th e"
    show typewriter with vpunch
    tp "m l  th e sp d er"

    show tequila_m at my_moveinright
    tequila "Mail the spider? What for? Cousin Zeke gave me a scare like that once. That is, until it turned out to be rubber."

    show clay_m_r happy at my_moveinleft
    clay "Pummel the spider? Ring the bell and I'm on it!"

    hide tequila_m with moveoutright
    show reggie_m at my_moveinright
    reggie "Put the gloves down, please - at least for now. It's not missing quite that many letters. That 'L' is double struck with a blank 'K'."

    hide clay_m_r happy with moveoutleft
    show willow_m_r at my_moveinleft
    willow "Milk the spider, maybe? I suppose I've heard of stranger possibilities."

    hide reggie_m with moveoutright
    show trinity_m at my_moveinright

    trinity "Brilliant! I know just where we need to go, then!"

    show willow_m_r disappointed

    willow "Do you now, yes?"

    trinity "There's a locked door I've never managed to get into, all the way in the back past the slot machines. And a certain husband of mine refuses to help."
    show willow_m_r
    willow "Because that would spoil your fun?"
    trinity "Because of the cobwebs, or so he says. As if a sculptor would be so fussed about a bit of dust. Perhaps it's just some private loo that's never cleaned. Or rather -"

    hide willow_m_r with moveoutleft

    show clay_m_r sober at my_moveinleft

    clay "It's staff only. End of story. I can only bend the rules so far."
    trinity "You are the rules, Mr. Head of Security."
    clay "I was. I'm retired. You'll have to try and pull one over on some other bloke."
    trinity "Or I could see if what I've overheard might be useful -"

    show typewriter with vpunch
    tp "Y ES\nA D HURRY"

    $ gui.custom.textbox_position = "left"

    jump keypad_start

#After receiving correct answer: (v1 - leaving here for now)
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

    jump tutorial_no

    
    label tutorial_no:
        play music "MainTheme.mp3" fadein 0.5
  
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
