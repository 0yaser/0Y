import argparse
import os

from functions.check import check
from functions.consts import COLOR, DATE, OPTIONS, TOOL_INFORMATION
from functions.dos import dos
from functions.ftp_login import ftp_login
from functions.md5 import md5
from functions.my_base64 import base64_
from functions.my_nmap import my_nmap
from functions.powershell import powershell
from functions.ssh_login import ssh_login
from functions.web_path import web_path
from pywifi import PyWiFi


def argparser():
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
            my_nmap(host=args.host, port=args.port)
        else:
            my_nmap(host=args.host)

    elif str(args.type).upper() == "GETFI":
        if os.name == "posix":
            os.system("clear")

        elif os.name == "nt":
            os.system("cls")
        print(TOOL_INFORMATION)
        wifi = PyWiFi()
        INF = wifi.interfaces()[0]
        INF.scan()
        Rscan = INF.scan_results()
        num_net = 0
        for network in Rscan:
            num_net = num_net + 1
            print(
                f"""
{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}{num_net}{COLOR.WHITE}] >>> {COLOR.GREEN} {network.ssid} {COLOR.RESET}
             
             """
            )

    elif str(args.type).upper() == "CHECKFI":
        check(args.host, args.passfi)

    elif args.fipath:
        web_path(args.host, args.fipath)
    else:
        if os.name == "posix":
            os.system("clear")

        elif os.name == "nt":
            os.system("cls")
        print(TOOL_INFORMATION)
        print(OPTIONS)


if __name__ == "__main__":
    argparser()
