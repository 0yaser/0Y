import datetime
import os

import paramiko

from .. import COLOR, TOOL_INFORMATION, ssh_login_data

date = datetime.datetime.now().time()


def ssh_login(hostname, port, username, password, status):
    print(TOOL_INFORMATION)
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
                print(TOOL_INFORMATION)
                print(ssh_login_data(user, password, hostname, port))
                break
            except:
                print(
                    f"{COLOR.WHITE}[{COLOR.BLUE}{date}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}Bad Login{COLOR.WHITE}]  {COLOR.YELLOW}{user}{COLOR.WHITE}:{COLOR.YELLOW}{password}"
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
                print(TOOL_INFORMATION)
                print(ssh_login_data(username, pas, hostname, port))
                break
            except:
                print(
                    f"{COLOR.WHITE}[{COLOR.BLUE}{date}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}Bad Login{COLOR.WHITE}]  {COLOR.YELLOW}{username}{COLOR.WHITE}:{COLOR.YELLOW}{pas}"
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
                print(TOOL_INFORMATION)
                print(ssh_login_data(username, pas, hostname, port))
                break
            except:
                print(
                    f"{COLOR.WHITE}[{COLOR.BLUE}{date}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}Bad Login{COLOR.WHITE}]  {COLOR.YELLOW}{username2}{COLOR.WHITE}:{COLOR.YELLOW}{pas}"
                )
                client.close()
        num = num + 1
