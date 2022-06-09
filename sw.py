#!/usr/bin/env python
#import subprocess
# https://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=Taking%20Aim
# https://ascii.co.uk/art
import light
import pistol

def start():
    print('''
*******************************************************************************
    .-.__        .-.  ___   .      .        +       .           .       .
    |_|  '--.-.-(   \/\;;\_ .-._______.-.       .           .       .
    (_)___     \ \ .-\ \;;\(   \       \ \\                                 .
     |    '---._\_((Q)) \;;\\ .-\      __(_)    .       .          .    
     ,           __'-' / .--.((Q))---'    \,
     |     ___.-:    \|  |   \'-'_          \\       .          .       .
     ,  .-'      \ .-.\   \   \ \ '--.__    '\\
     |  |____.----((Q))\   \__|--\_      \    '         oo
     '  (_)        '-'  \_  :  \-' '--.___\\
         |                \  \  \       \(_)
         ,                 \  \  \         \,
 ~~~~~~~~|~~~~~~~~~~~~~~~~~~\~~\~~\~~~~~~~~~\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         ,                   \  \  \   )`'-.,'\,)`'-.,)`'-.,)`'-.,,)`'-.,)`'-.
         |                    \  \__|          '
         '  )`'-.,)`'-.,)`'-.,)\_:. \\)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,
                                 \ \ \\
                                  \ \ \\
                                   \_\_|
)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)`'-.,)                                   
*******************************************************************************
''')
    print("You have just crash landed into the swampy marshlands of this tropical planet.  Your X-Wing is quickly sinking")
    print("into the thick bog and clammering out of the cockpit, you gently wade towards the shore intently aware that")
    print("someone is watching..")
    print("")
    print("You make it ashore, a bit injured from the crash landing but nothing you haven't experienced before. A huge")
    print("shadow rustles past some bushes overhead and instinctively you pull out your...")
    option()

def option():
    user = input(f"Type (a) lightsaber or (b) laser pistol: ")

    if user.upper() == "A":
        light.start()
        #subprocess.call("light.py", shell=True)
    elif user.upper() == "B":
        pistol.start()
    elif user.upper != "A" or user.upper != "B":
        print("Invalid option, please try again")
        option()

if __name__ == '__main__':       
    start()