default keypad.typewriter_message = "o be pre c sse{p}Do he ' s, c rro s he ' s"

default keypad.keypad_xsize = 400
default keypad.keypad_ysize = 600

default keypad.keypad_zoom = 3.0


transform door_center:
    xalign 0.5
    yalign 0.70

default keypad.asked_reggie = False
default keypad.asked_trinity = False
default keypad.asked_willow = False

default keypad.combination = ""
default keypad.answer = "80456"
default keypad.secret = "802"

init python:

    def process_keypad_input( input ):

        keypad.combination += input

        if len( keypad.combination ) >= 5:
            renpy.jump( "keypad_process_answer" )

        match keypad.combination:
            case keypad.answer:
                renpy.jump( "keypad_process_answer" )
            case keypad.secret:
                renpy.jump( "keypad_process_answer" )
            case _:
                return

image numpad_0:
    "images/numpad_0.png"
    zoom keypad.keypad_zoom

image numpad_pressed_0:
    "images/numpadpressed_0.png"
    zoom keypad.keypad_zoom

image numpad_1:
    "images/numpad_1.png"
    zoom keypad.keypad_zoom

image numpad_pressed_1:
    "images/numpadpressed_1.png"
    zoom keypad.keypad_zoom

image numpad_2:
    "images/numpad_2.png"
    zoom keypad.keypad_zoom

image numpad_pressed_2:
    "images/numpadpressed_2.png"
    zoom keypad.keypad_zoom

image numpad_3:
    "images/numpad_3.png"
    zoom keypad.keypad_zoom

image numpad_pressed_3:
    "images/numpadpressed_3.png"
    zoom keypad.keypad_zoom

image numpad_4:
    "images/numpad_4.png"
    zoom keypad.keypad_zoom

image numpad_pressed_4:
    "images/numpadpressed_4.png"
    zoom keypad.keypad_zoom

image numpad_5:
    "images/numpad_5.png"
    zoom keypad.keypad_zoom

image numpad_pressed_5:
    "images/numpadpressed_5.png"
    zoom keypad.keypad_zoom

image numpad_6:
    "images/numpad_6.png"
    zoom keypad.keypad_zoom

image numpad_pressed_6:
    "images/numpadpressed_6.png"
    zoom keypad.keypad_zoom

image numpad_7:
    "images/numpad_7.png"
    zoom keypad.keypad_zoom

image numpad_pressed_7:
    "images/numpadpressed_7.png"
    zoom keypad.keypad_zoom

image numpad_8:
    "images/numpad_8.png"
    zoom keypad.keypad_zoom

image numpad_pressed_8:
    "images/numpadpressed_8.png"
    zoom keypad.keypad_zoom

image numpad_9:
    "images/numpad_9.png"
    zoom keypad.keypad_zoom

image numpad_pressed_9:
    "images/numpadpressed_9.png"
    zoom keypad.keypad_zoom

screen keypad():
    frame:
        xalign 0.455 yalign 0.5
        xsize keypad.keypad_xsize
        ysize keypad.keypad_ysize
        add "images/numpad_bg.png":
            zoom keypad.keypad_zoom
        add "numpad_1"
        add "numpad_2"
        add "numpad_3"
        add "numpad_4"
        add "numpad_5"
        add "numpad_6"
        add "numpad_7"
        add "numpad_8"
        add "numpad_9"
        add "numpad_0"

screen keypad_interactive:
    frame:
        xalign 0.5 yalign 0.1
        text '[keypad.combination]':
            xalign 0.5
            size 55
            color "#f1e8c7"
            outlines [ (absolute(2), "#604d32", absolute(0), absolute(0)) ]
    frame:
        xalign 0.455 yalign 0.5
        xsize keypad.keypad_xsize
        ysize keypad.keypad_ysize
        add "images/numpad_bg.png":
            zoom keypad.keypad_zoom
        imagebutton:
            idle "numpad_0"
            hover "numpad_pressed_0"
            focus_mask True
            keysym str(0)
            action Function( process_keypad_input, "0" )
        imagebutton:
            idle "numpad_1"
            hover "numpad_pressed_1"
            focus_mask True
            keysym str(1)
            action Function( process_keypad_input, "1" )
        imagebutton:
            idle "numpad_2"
            hover "numpad_pressed_2"
            focus_mask True
            keysym str(2)
            action Function( process_keypad_input, "2" )
        imagebutton:
            idle "numpad_3"
            hover "numpad_pressed_3"
            focus_mask True
            keysym str(3)
            action Function( process_keypad_input, "3" )
        imagebutton:
            idle "numpad_4"
            hover "numpad_pressed_4"
            focus_mask True
            keysym str(4)
            action Function( process_keypad_input, "4" )
        imagebutton:
            idle "numpad_5"
            hover "numpad_pressed_5"
            focus_mask True
            keysym str(5)
            action Function( process_keypad_input, "5" )
        imagebutton:
            idle "numpad_6"
            hover "numpad_pressed_6"
            focus_mask True
            keysym str(6)
            action Function( process_keypad_input, "6" )
        imagebutton:
            idle "numpad_7"
            hover "numpad_pressed_7"
            focus_mask True
            keysym str(7)
            action Function( process_keypad_input, "7" )
        imagebutton:
            idle "numpad_8"
            hover "numpad_pressed_8"
            focus_mask True
            keysym str(8)
            action Function( process_keypad_input, "8" )
        imagebutton:
            idle "numpad_9"
            hover "numpad_pressed_9"
            focus_mask True
            keysym str(9)
            action Function( process_keypad_input, "9" )

label keypad_start:
    scene bg hallway with spiral
    show numpad_icon at door_center with spiral

    show typewriter at my_moveinright
    tp "{cps=[cps]}[keypad.typewriter_message]{/cps}"

    hide typewriter with moveoutright

    jump keypad_menu

label keypad_menu:
    menu:
        "[keypad.typewriter_message]"
        "Reggie, any thoughts on the gaps in this garble?":
            jump keypad_reggie
        "Trinity, you mentioned overhearing something useful?":
            jump keypad_trinity
        "If only Mr. Minski saw fit to haunt an adding machine. Willow, might you translate?" if keypad.asked_reggie and keypad.asked_trinity:
            jump keypad_willow
        "I suppose it's time to push these buttons.":
            jump keypad_give_answer

label keypad_reggie:
    show reggie_m at my_moveinright
    reggie "The paper has faint impressions of I's and T's. And that's it for missing letters and a coincidentally fitting conclusion."
    if not keypad.asked_reggie:
        $ keypad.typewriter_message += "\n\nThis note is missing I's and T's."
        $ keypad.asked_reggie = True
        $ turns -= 1
    hide reggie_m with moveoutright
    jump keypad_menu

label keypad_trinity:
    show trinity_m at my_moveinright
    trinity "Just enough to have half a clue. Two, rather, though they might very well add up to bugger all.{p}\nThe first is 4, 5, 6.{p}\nThe second is 8 and 0."
    if not keypad.asked_trinity:
        $ keypad.typewriter_message += "\n\nParts of the combination - \n  *  4, 5, 6\n  *  8, 0"
        $ keypad.asked_trinity = True
        $ turns -= 1
    hide trinity_m with moveoutright
    jump keypad_menu

label keypad_willow:
    show willow_m at my_moveinright
    willow "If I can read between these lines - dot an i, or cross a T. Just the same as you'd write with a pen, yes?{p}\nFirst a stroke down -"
    if not keypad.asked_willow:
        $ keypad.typewriter_message += "\n\nTo key in the combination, dot an i or cross a T as you'd write with a pen."
        $ keypad.asked_willow = True  
        $ turns -= 1  
    hide willow_m with moveoutright
    jump keypad_menu

label keypad_process_answer:
    $ turns -= 1
    if keypad.combination == keypad.answer:
        "You crossed the T and opened the lock. Congratulations!"
        hide screen keypad_interactive
        jump four_hearts_start
    elif keypad.combination == keypad.secret:
        "A stroke and a dash - that's an i! A secret drawer slides open, revealing a card."
        jump keypad_give_answer
    elif len( keypad.combination ):
        "Not quite...let's be sure to get our clues all in order..."
        jump keypad_give_answer
    else:
        jump keypad_give_answer

label keypad_give_answer:
    $ keypad.combination = ""
    show screen keypad_interactive
    menu( screen="choice_h" ):
        "Start Over":
            jump keypad_give_answer
        "Back to Clues":
            hide screen keypad 
            hide screen keypad_interactive with moveoutbottom
            jump keypad_menu