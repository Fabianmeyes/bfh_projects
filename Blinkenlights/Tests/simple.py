#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "wVj" # Change XYZ to the UID of your LED Strip Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected
    while 1==1:
        # Set first 10 LEDs to green
        ls.set_frame_duration(1)
        for i in range (13):
            r = [200, 0, 0, 200, 11*i, 11*i, 100, 11, 111, 111, 111, 11, 100, 123, 234, 255]
            g = [0, 190, 0, 255, 255, 255, 255, 11*i, 255, 255, 255, 200, 10, 20, 11, 11]
            b = [0, 0, 100, 150, 11, 77, 11*i, 11*i, 50, 55, 66, 255, 11, 234, 123, 11]
            ls.set_rgb_values(16*i, 16, r, g, b)

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
