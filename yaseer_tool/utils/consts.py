from datetime import datetime

import colorama
import requests

SESSION = requests.session()
DATE = datetime.now().time()
COLOR = colorama.Fore


def thePath(path):
    return f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}]{COLOR.GREEN} {path}"


def tcp(port, name, product, version, extrainfo):
    return f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.GREEN}OPEN{COLOR.WHITE}]  >>{COLOR.YELLOW} TCP{COLOR.WHITE} | {COLOR.GREEN}{port} {COLOR.WHITE}/ {COLOR.YELLOW} {name} | {product} | {version} | {extrainfo}"


def close(port):
    return (
        f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}CLOSE{COLOR.WHITE}] >>{COLOR.RED} {port} ",
    )


def login_data(
    user,
    password,
    hostname,
    port,
) -> str:
    return f"""

        {COLOR.RED} 
                                    
        {COLOR.WHITE}            username :{COLOR.GREEN} {user} 
        {COLOR.WHITE}            password :{COLOR.GREEN} {password}
        {COLOR.WHITE}            host     :{COLOR.CYAN} {hostname}
        {COLOR.WHITE}            port     :{COLOR.YELLOW} {port}

                      """


def prompt(
    param,
    prompt,
    password=None,
):
    return f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE}[{COLOR.RED}{prompt}{COLOR.WHITE}]  {COLOR.YELLOW}{param}{COLOR.WHITE}:{COLOR.YELLOW}{password}"


def sucsess(param):
    return f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}]{COLOR.GREEN} {param}"


def failed(param):
    return f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}]{COLOR.RED} {param}"


OPTIONS = f"""                                                
        Options:
        {COLOR.YELLOW}
            ________________________________________SSH CHECKER______________________________________________
            -t  , --type \t\t {COLOR.WHITE}Specify the service             |{COLOR.YELLOW} --type ssh 
            -ps , --pas  \t\t {COLOR.WHITE}Password                        |{COLOR.YELLOW} --pas password
            -ho , --host \t\t {COLOR.WHITE}Host IP                         |{COLOR.YELLOW} --host 192.168.0.0
            -u  , --user \t\t {COLOR.WHITE}Username                        |{COLOR.YELLOW} --user username
            -p  , --port \t\t {COLOR.WHITE}Port                            |{COLOR.YELLOW} --port 22
            -pf , --pfile\t\t {COLOR.WHITE}Password file                   |{COLOR.YELLOW} --pfile password.txt
            -uf , --ufile\t\t {COLOR.WHITE}Username file                   |{COLOR.YELLOW} --ufile username.txt
            
            
            ________________________________________FTP CHECKER______________________________________________
            -t  , --type \t\t {COLOR.WHITE}Specify the service             |{COLOR.YELLOW} --type ftp 
            -ps , --pas  \t\t {COLOR.WHITE}Password                        |{COLOR.YELLOW} --pas password
            -ho , --host \t\t {COLOR.WHITE}Host IP                         |{COLOR.YELLOW} --host 192.168.0.0
            -u  , --user \t\t {COLOR.WHITE}Username                        |{COLOR.YELLOW} --user username
            -p  , --port \t\t {COLOR.WHITE}Port                            |{COLOR.YELLOW} --port 21
            -pf , --pfile\t\t {COLOR.WHITE}Password file                   |{COLOR.YELLOW} --pfile password.txt
            -uf , --ufile\t\t {COLOR.WHITE}Username file                   |{COLOR.YELLOW} --ufile username.txt


            ________________________________________CHECK DIR THE SITE________________________________________
            -ho , --host  \t\t {COLOR.WHITE}Host IP                         |{COLOR.YELLOW} --host 192.168.0.0
            -fp , --fipath \t\t {COLOR.WHITE}File path                       |{COLOR.YELLOW} --fipath dir.txt 

            
            ________________________________________DECRYPT MD5________________________________________________
            -fh , --fhash \t\t {COLOR.WHITE}Hash file                       |{COLOR.YELLOW} --fhash password.txt
            -th , --thash \t\t {COLOR.WHITE}Hash type                       |{COLOR.YELLOW} --thash MD5
            -hs , --hash \t\t {COLOR.WHITE}The hash                        |{COLOR.YELLOW} --hash 25d55ad283aa400af464c76d713c07ad
            
            
            ________________________________________DECODE BASE64______________________________________________
            -fh , --fhash \t\t {COLOR.WHITE}Hash file                       |{COLOR.YELLOW} --fhash password.txt
            -th , --thash \t\t {COLOR.WHITE}Hash type                       |{COLOR.YELLOW} --thash BASE64
            -sh , --hash \t\t {COLOR.WHITE}The hash                        |{COLOR.YELLOW} --hash MTIzNDU2Nzg=
            

            ________________________________________WIFI CHECKER_______________________________________________
            -t   , --type \t\t {COLOR.WHITE}Specify the service             |{COLOR.YELLOW} --type checkfi
            -ho  , --host  \t\t {COLOR.WHITE}Wifi name (SSID)                |{COLOR.YELLOW} --host SSID
            -pfi , --passfi \t\t {COLOR.WHITE}Password file                   |{COLOR.YELLOW} --passfi password.txt    


            ________________________________________GET WIFI___________________________________________________
            -t  , --type \t\t {COLOR.WHITE}Specify the service             |{COLOR.YELLOW} --type getfi
                                                                                                                                                                                                                                                    
                                                                                                
                                                                                                
            ________________________________________DOS ATTACK_________________________________________________
            -do  , --dos \t\t {COLOR.WHITE}Enable DoS attack               |{COLOR.YELLOW} --dos true            
            -ho  , --host \t\t {COLOR.WHITE}Host IP & domain                |{COLOR.YELLOW} --host google.com     
            -p   , --port \t\t {COLOR.WHITE}Port                            |{COLOR.YELLOW} --port 22             
                                                                                                
                                                                                                
            ________________________________________POWERSHELL REVERSE_________________________________________
            -po  , --pshell \t\t {COLOR.WHITE}Enable PowerShell reverse       |{COLOR.YELLOW} --pshell true         
            -lho , --lhost\t\t {COLOR.WHITE}Local host                      |{COLOR.YELLOW} --lhost 192.168.1.1
            -n   , --name\t\t {COLOR.WHITE}Name file                       |{COLOR.YELLOW} --name shell.ps1

            ________________________________________SCAN PORTS_________________________________________________
            -ho , --host  \t\t {COLOR.WHITE}Host IP                         |{COLOR.YELLOW} --host 192.168.0.0    
            -t  , --type \t\t {COLOR.WHITE}Specify the service             |{COLOR.YELLOW} --type scan
        """

TOOL_INFORMATION = f"""
        {COLOR.YELLOW}
                                ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                                ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
        {COLOR.BLUE} 0Y Tool{COLOR.YELLOW}                 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
                                ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
        {COLOR.GREEN} By : 0xYaser {COLOR.YELLOW}           ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 
                                ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░           
        {COLOR.WHITE} version [0.1] {COLOR.YELLOW}          ░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░ 

        {COLOR.RED}   
        """

TOP_PORTS = [
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
