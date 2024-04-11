import os

import paramiko
from .consts import TOOL_INFORMATION, login_data, prompt


def ssh_login(hostname, port, username, password, status):
    print(TOOL_INFORMATION)
    if port == None:
        port = 22
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    num = 0

    if status == "1,0":
        for user in open(username, "r").read().splitlines():

            try:
                client.connect(hostname, port=port, username=user, password=password)
                # stdout = client.exec_command("whoami")  #! not accessed
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")
                print(TOOL_INFORMATION)
                print(login_data(user, password, hostname, port))
                break
            except:
                print(prompt(param=user, password=password, prompt="BAD LOGIN"))

                client.close()

    elif status == "0,1":
        for pas in open(password, "r").read().splitlines():
            try:
                client.connect(hostname, port=port, username=username, password=pas)
                # stdout = client.exec_command("whoami")  #! not accessed
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")
                print(TOOL_INFORMATION)
                print(login_data(username, pas, hostname, port))
                break
            except:
                print(prompt(param=username, password=pas, prompt="BAD LOGIN"))
                client.close()

    elif status == "1,1":
        for pas in open(password, "r").read().splitlines():
            try:
                username2 = open(username, "r").read().splitlines()[num]
                client.connect(hostname, port=port, username=username2, password=pas)
                # stdout = client.exec_command("whoami")  #! not accessed
                if os.name == "posix":
                    os.system("clear")

                elif os.name == "nt":
                    os.system("cls")
                print(TOOL_INFORMATION)
                print(login_data(username, pas, hostname, port))
                break
            except:
                print(prompt(param=username2, password=pas, prompt="BAD LOGIN"))
                client.close()
        num = num + 1
