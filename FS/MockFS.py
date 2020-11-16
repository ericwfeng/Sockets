# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
from threading import Thread
from time import sleep
import random
import pickle
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

            t = Thread(target=transmit, args=[conn, sensor])
            t.daemon = True
            t.start()
            
            stop_threads = False
            while True:
                if stop_threads==True:
                    break

def transmit(conn, sensor):
    """
    Transmit new pressure measurement / warning every second.
    conn is the client socket
    """
    command_sent = False
    while not command_sent:
        measurement = sensor.measure()

        msg = "Waiting for command from ground station.\n"
        
        val = conn.recv(1024).decode('utf-8')

        if val == 'True':
            command_sent = True

        if (command_sent):
            msg = "Command Sent!\n"

        info = [msg, measurement, warning(measurement, 50, 460)]

        # Pickle converts objects into a format that can be sent via websocket.
        packet = pickle.dumps(info)
        conn.sendall(packet)
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