# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import socket
from threading import Thread
from time import sleep
import pickle
from PseudoPressureSensor import PseudoPressureSensor
from flag import flag


def main():
    HOST = '127.0.0.1'
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                #data = conn.recv(1024)
                sensor = PseudoPressureSensor(15, 510)
                t = Thread(target=transmit, args=[conn, sensor])
                t.daemon = True
                t.start()
                sleep(1)
                stop_threads = False
                if stop_threads==True:
                    break

def transmit(conn, sensor):
    """
    Transmit new pressure measurement / warning every second.
    conn is the client socket
    """
    #sleep(1)
    command_sent = False
    while not command_sent:
        measurement = sensor.measure()

        msg = "Waiting for command from ground station.\n"
        
        val = conn.recv(1024).decode('utf-8')

        if val == 'True':
            command_sent = True

        if (command_sent):
            msg = "Command Sent!\n"
            print(msg)
        info = [msg, measurement, warning(measurement, 50, 460)]

        # Pickle converts objects into a format that can be sent via websocket.
        packet = pickle.dumps(info)
        conn.sendall(packet)

def warning(measurement, min, max):
    """
    Generate warning if measurement outside min and max range is detected.
    """
    setflag = flag()
    if (measurement < min):
        setflag.giveWarning = True
        setflag.abortFlight = False
        setflag.actuatePressureRelease = False
        return setflag
    if(measurement > max):
        setflag.giveWarning = True
        setflag.abortFlight = False
        setflag.actuatePressureRelease = True
        return setflag
    else:
        setflag.giveWarning = False
        setflag.abortFlight = False
        setflag.actuatePressureRelease = False
        return setflag
main()
