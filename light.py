#!/usr/bin/env python
import sw

def start():
    print('''
*******************************************************************************
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 '  .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(  ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `  `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((

███████╗███╗   ██╗     ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ███████╗██╗
██╔════╝████╗  ██║    ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║
█████╗  ██╔██╗ ██║    ██║  ███╗██║   ██║███████║██████╔╝██║  ██║█████╗  ██║
██╔══╝  ██║╚██╗██║    ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██╔══╝  ╚═╝
███████╗██║ ╚████║    ╚██████╔╝╚a██████╔╝██║  ██║██║  ██║██████╔╝███████╗██╗
╚══════╝╚═╝  ╚═══╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝                                                                         
*******************************************************************************
''')
    print("Your lightsaber flickers to life as you use it's glow to illuminate your surroundings. It's gentle hum gives your")
    print("a sense of false security, but your chances now, are better, nevertheless.")
    print("")
    print("\"Hellooo?\", you shout half-heartedly. You didn't think anyone could live in these conditions but somehow you had")
    print("the feeling that you were wrong. A low mourning howl reverberated the jungle just as you were about to switch off")
    print("your lightsaber and thinking twice, you decide to leave it on, just in case.")
    print("")
    option()

def option():
    user_input=input(f"Type (p) Proceed towards the bushes. ")

    if user_input.upper() == "P":
        sw.start()  
    elif user_input.upper() != "P":
        print("Invalid option, please try again")
        option()