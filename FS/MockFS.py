# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
from threading import Thread
from time import sleep
import random
from PseudoPressureSensor import PseudoPressureSensor


def main():
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
            sensor = PseudoPressureSensor(15, 510)
            measure(conn, sensor)
            # r = Thread(target=measure, args=[conn, sensor])
            # r.daemon = True
            # r.start()
            
            stop_threads = False
            while True:
                if stop_threads==True:
                    break

def measure(socket, sensor):
    """
    Socket is the socket used to send data
    Transmit new pressure measurement / warning every second.
    """
    measurement = sensor.measure()
    info = [measurement, warning(measurement, 50, 460)]

    # Pickle converts objects into a format that can be sent via websocket.
    socket.sendall(str(info[0]).encode('utf-8'))
    socket.sendall(str(info[1]).encode('utf-8'))
    sleep(1)

def warning(measurement, min, max):
    """
    Generate warning if measurement outside min and max range is detected.
    """
    if (measurement < min or measurement > max):
        return True

    else:
        return False

main()