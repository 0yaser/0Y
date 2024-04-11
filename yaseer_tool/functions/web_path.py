import os

from .. import COLOR, DATE, SESSION, TOOL_INFORMATION


def web_paths(host, path):
    paths = open(path, "r").read().splitlines()
    true_path = []
    for dir in paths:
        try:
            if "https://" in host:
                web = host + "/"
            elif "http://" in host:
                web = host + "/"
            else:
                web = "https://" + host + "/" + dir
            response = SESSION.get(web, timeout=4).status_code
            if response == 200:
                print(
                    f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE} >>> {COLOR.GREEN}{web} {COLOR.WHITE}| {COLOR.GREEN}{response}{COLOR.RESET}"
                )
                true_path.append(web)
            elif response == 404:
                print(
                    f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE} >>> {COLOR.RED}{web} {COLOR.WHITE}| {COLOR.RED}{response}{COLOR.RESET}"
                )
            else:
                print(
                    f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE} >>> {COLOR.YELLOW}{web} {COLOR.WHITE}| {COLOR.YELLOW}{response}{COLOR.RESET}"
                )
        except:
            break
    for i in true_path:

        if os.name == "posix":
            os.system("clear")

        elif os.name == "nt":
            os.system("cls")
        print(TOOL_INFORMATION)
        print(
            f"\r{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}] {COLOR.WHITE} >>> {COLOR.GREEN}{i} {COLOR.WHITE}| {COLOR.GREEN}200{COLOR.RESET}"
        )
