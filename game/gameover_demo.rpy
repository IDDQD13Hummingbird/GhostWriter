

label gameover:

    $ flag_died = True
    stop music fadeout 5.0

    scene bg room with fire

    $ gui.custom.textbox_position = "centre"

    n "It ended before you even realized what happened."
    n "The only sound left - mourning chapel bell striking noon - filled your head with it's grave weight."
    n "So that's it... \nYou must've ran out of time."
    show bg burned_room with fade

    n "{cps=2}...{/cps}{w}!"

    n "You sense an unknown force putting you back in place, right where you came from."
    jump start
