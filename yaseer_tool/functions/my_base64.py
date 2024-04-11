import base64
import os

from consts import TOOL_INFORMATION, failed, sucsess


def base64_(base64_hasH, file):

    for string_to_encode in open(file, "r").read().splitlines():

        encoded_string = base64.b64encode(string_to_encode.encode()).decode()
        if base64_hasH == encoded_string:
            if os.name == "posix":
                os.system("clear")

            elif os.name == "nt":
                os.system("cls")  #! unreachable
            print(TOOL_INFORMATION)
            print(sucsess(string_to_encode))
            break
        else:
            print(failed(encoded_string))
