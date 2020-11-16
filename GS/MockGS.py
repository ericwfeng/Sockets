# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:57:25 2020

@author: ericw
"""

import socket
from threading import Thread

def main():
    HOST = '127.0.0.1'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        r = Thread(target=recieve, args=[s])
        t = Thread(target=transmit, args=[s])

        r.daemon = True

        t.start()
        r.start()

        # prevents socket from closing
        while True:
            pass
            
def transmit(s):
    """transmits data to server
    s is the socket used to send data.
    """
    # while True:

def recieve(s):
    """recieves data from the server
    s is the socket used to receieve data.
    """
    while True:
        recv_data = s.recv(1024).decode('utf-8')
        # data = pickle.loads(s)
        print(recv_data)

main()