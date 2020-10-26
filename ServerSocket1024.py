# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
import threading
import time
import random
#tcp
def increase_loop():
    x=0
    global stop_threads
    while True:
        print(x)
        time.sleep(.5)
        x +=1
        if stop_threads:
            break
def decrease_loop():
    x=0
    global stop_threads
    while True:
        print(x)
        time.sleep(.5)
        x -=1
        if stop_threads:
            break
def random_loop():
    global stop_threads
    while True:
        print(random.randint(0,9))
        time.sleep(.5)
        if stop_threads:
            break

HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        thread2 = threading.Thread(target=random_loop)
        stop_threads = False
        thread2.start()
        #while True:
            #data = conn.recv(1024)
        while True:
            thread1 = threading.Thread(target=decrease_loop)
            thread = threading.Thread(target=increase_loop)
            thread2 = threading.Thread(target=random_loop)
            command = conn.recv(1024)            
            if repr(command) == "b'increase'":
                if thread2.is_alive():
                    stop_threads = True
                    thread2.join()
                stop_threads = False
                thread.start()
            if repr(command) == "b'decrease'":
                if thread2.is_alive():
                    stop_threads = True
                stop_threads = False
                thread1.start()
            if repr(command) == "b'random'":
                if thread2.is_alive():
                    stop_threads = True
                stop_threads = False
                thread2.start()
            if repr(command) == "b'stop'":
                #threading.Thread(target=increase_loop).join()
                stop_threads = True
                if thread.is_alive():
                    thread.join()
                if thread1.is_alive():
                    thread1.join()
                if thread2.is_alive():
                    thread2.join()
                
            #if not data:
             #   break
            #conn.sendall(data)
