import hashlib
import os

from .consts import COLOR, DATE, TOOL_INFORMATION


def md5(md5_hasH, file):

    for i in open(file, "r").read().splitlines():

        text = i
        md5_hash = hashlib.md5()
        md5_hash.update(text.encode())
        md5_hex = md5_hash.hexdigest()
        md5_hex = md5_hex[:32]
        if md5_hasH == md5_hex:
            if os.name == "posix":
                os.system("clear")

            elif os.name == "nt":
                os.system("cls")  #! unreachable
            print(TOOL_INFORMATION)
            print(f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}]{COLOR.GREEN} {i}")
            break
        else:
            print(
                f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}]{COLOR.RED} {md5_hex}"
            )
