import base64
import datetime
import os

import colorama

color = colorama.Fore


def base64_(base64_hasH, file):

    for string_to_encode in open(file, "r").read().splitlines():
        date = datetime.datetime.now().time()
        encoded_string = base64.b64encode(string_to_encode.encode()).decode()
        if base64_hasH == encoded_string:
            if os.name == "posix":
                os.system("clear")

            elif os.name == "nt":
                os.system("cls")
            print(
                f"""{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

"""
            )
            print(
                f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.GREEN} {string_to_encode}"
            )
            break
        else:
            print(
                f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.RED} {encoded_string}"
            )
