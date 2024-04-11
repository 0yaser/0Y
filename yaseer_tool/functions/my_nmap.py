import os

import nmapping
from consts import TOOL_INFORMATION, TOP_PORTS, close, tcp


def my_nmap(host=None, port=None):
    if os.name == "posix":
        os.system("clear")

    elif os.name == "nt":
        os.system("cls")  #! unreachable
    print(TOOL_INFORMATION)
    if port == None:
        TOP_PORTS
        scann_ports = nmapping.PortScanner()
        for porT in TOP_PORTS:
            states = scann_ports.scan(str(host), str(porT))
            if states["scan"][str(host)]["tcp"][porT]["state"] == "open":

                name = states["scan"][str(host)]["tcp"][porT]["name"]
                product = states["scan"][str(host)]["tcp"][porT]["product"]
                version = states["scan"][str(host)]["tcp"][porT]["version"]
                extrainfo = states["scan"][str(host)]["tcp"][porT]["extrainfo"]
                print(tcp(porT, name, product, version, extrainfo))
            else:
                print(close(porT))
    else:
        scann_ports = nmapping.PortScanner()
        states = scann_ports.scan(str(host), str(port))
        if states["scan"][str(host)]["tcp"][port]["state"] == "open":
            name = states["scan"][str(host)]["tcp"][port]["name"]
            product = states["scan"][str(host)]["tcp"][port]["product"]
            version = states["scan"][str(host)]["tcp"][port]["version"]
            extrainfo = states["scan"][str(host)]["tcp"][port]["extrainfo"]
            print(tcp(porT, name, product, version, extrainfo))
        else:
            print(close(porT))


