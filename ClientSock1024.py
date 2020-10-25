# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 19:57:25 2020

@author: ericw
"""

import socket

HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello World')
    while True:
        command = input()
        s.send(command.encode('utf-8'))
    #s.send(command.encode('utf-8'))
    #data = s.recv(1024)
#print('Recieved', repr(data))