# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:57:25 2020

@author: ericw
"""

import socket
import pickle
from time import sleep
from threading import Thread
from PseudoValve import PseudoValve

def main():
    HOST = '127.0.0.1'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        valve = PseudoValve()

        r = Thread(target=recieve, args=[s, valve])
        r.daemon = True
        r.start()


        # prevents socket from closing
        while True:
            pass

def recieve(s, valve):
    """
    recieves data from the server
    s is the socket used to receieve data.
    """
    while True:
        if valve.state == 'off':
            msg = 'False'
        else:
            msg = 'True'
        s.sendall(msg.encode('utf-8'))

        msg = s.recv(4096)
        data = pickle.loads(msg)

        message = data[0]
        pressure = data[1]
        flag = data[2]

        print(message, end="")
        """ print(message, end="")
        print(pressure)
        print(flag) """

        if flag:
            valve.flip()

main()