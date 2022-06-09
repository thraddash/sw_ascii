#!/usr/bin/env python
import sw

def start():
    print('''
*******************************************************************************
            |^\                      _________________/\_
            |~~~|--------------~~~~~~~~~~~~~~~~,xx.~~~~~~~~\\
            |___|-------++++==|___|~~~~~|_____(x@x),;'//  ||
                            |~~~||    |~~~~~~~~~~~ //   ||
                                ~\(_(=)~~ ,-~-\       \  __/
                                   ~~~~~\[  \ ]\       \/
                                        `:  |'()       \\
                                         ~~~~\ \       \\
                                              \ \       \\
                                               \ \       \\
                                                \ \       \\
                                                 \ \       ||
                                                  | \       ||
                                                  |  \_  ___||
                                                  \____( )-=~/

████████╗ █████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗      █████╗ ██╗███╗   ███╗
╚══██╔══╝██╔══██╗██║ ██╔╝██║████╗  ██║██╔════╝     ██╔══██╗██║████╗ ████║
   ██║   ███████║█████╔╝ ██║██╔██╗ ██║██║  ███╗    ███████║██║██╔████╔██║
   ██║   ██╔══██║██╔═██╗ ██║██║╚██╗██║██║   ██║    ██╔══██║██║██║╚██╔╝██║
   ██║   ██║  ██║██║  ██╗██║██║ ╚████║╚██████╔╝    ██║  ██║██║██║ ╚═╝ ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝                                                                         
*******************************************************************************
''')
    print("You quickly snap off a couple of shots in the general direction, punching scorched holes in the vegetation.")
    print("You stop and hold your breath to listen. Nothing. In the strange silence, you hear your own heartbeat pounding.")
    print("You realize that whatever was stalking you is now long gone.")
    print("")
    option()

def option():
    print("Type (a) You go back and try to salvage as much as you can from the ship.")
    user_input=input(f"Type (b) You decide to inspect the damage done to the vegetation. ")

    if user_input.upper() == "A":
        sw.start()
    elif user_input.upper() == "B":
        sw.start()  
    elif user_input.upper() != "A" or user_input.upper() !="B":
        print("Invalid option, please try again")
        option()