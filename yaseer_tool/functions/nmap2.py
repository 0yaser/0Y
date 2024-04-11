import os
from ftplib import FTP  # I dont know why you add this when it is not accessed

import nmap

from .. import COLOR, DATE, TOOL_INFORMATION


def nmaP(host=None, port=None):
    if os.name == "posix":
        os.system("clear")

    elif os.name == "nt":
        os.system("cls")  # not accessed
    print(TOOL_INFORMATION)
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
            states = scann_ports.scan(str(host), str(porT))
            if states["scan"][str(host)]["tcp"][porT]["state"] == "open":

                name = states["scan"][str(host)]["tcp"][porT]["name"]
                product = states["scan"][str(host)]["tcp"][porT]["product"]
                version = states["scan"][str(host)]["tcp"][porT]["version"]
                extrainfo = states["scan"][str(host)]["tcp"][porT]["extrainfo"]
                print(
                    f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.GREEN}OPEN{COLOR.WHITE}]  >>{COLOR.YELLOW} TCP{COLOR.WHITE} | {COLOR.GREEN}{porT} {COLOR.WHITE}/ {COLOR.YELLOW} {name} | {product} | {version} | {extrainfo}"
                )
            else:
                print(
                    f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}CLOSE{COLOR.WHITE}] >>{COLOR.RED} {porT} ",
                    end="",
                )
    else:
        scann_ports = nmap.PortScanner()
        states = scann_ports.scan(str(host), str(port))
        if states["scan"][str(host)]["tcp"][port]["state"] == "open":
            name = states["scan"][str(host)]["tcp"][port]["name"]
            product = states["scan"][str(host)]["tcp"][port]["product"]
            version = states["scan"][str(host)]["tcp"][port]["version"]
            extrainfo = states["scan"][str(host)]["tcp"][port]["extrainfo"]
            print(
                f"\n{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.GREEN}OPEN{COLOR.WHITE}] >>{COLOR.YELLOW} TCP{COLOR.WHITE} | {COLOR.GREEN}{port} {COLOR.WHITE}/ {COLOR.YELLOW} {name} | {product} | {version} | {extrainfo}"
            )
        else:
            print(
                f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}CLOSE{COLOR.WHITE}] >>{COLOR.RED} {porT} ",
                end="",
            )
