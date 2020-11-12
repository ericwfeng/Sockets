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
#def random_loop():
 #   global stop_threads
  #  while True:
   #     data = random.randint(0,9)
    #    print(data)
     #   s.send(str(data).encode('utf-8'))
      #  time.sleep(1)
       # if stop_threads:
        #    break

HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        #while True:
            #data = conn.recv(1024)
        stop_threads = False
        while True:
            if stop_threads==True:
                break
            data = random.randint(15,510)
            print(data)
            conn.send(str(data).encode('utf-8'))
            time.sleep(1)
            #command = conn.recv(1024)     
            #if not command:
             #   break
            #if repr(command) == "b'stop'":
                #threading.Thread(target=increase_loop).join()
             #   stop_threads = True
                
            #if not data:
             #   break
            #conn.sendall(data)
