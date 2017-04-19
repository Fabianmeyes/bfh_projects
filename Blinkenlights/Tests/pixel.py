#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "xgE" # Change XYZ to the UID of your LED Strip Bricklet

NUM_LEDS = 10
r = [0]*16
g = [0]*16
b = [0]*16
r_index = NUM_LEDS-1
g_index = 0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip


# Use frame rendered callback to move the active LED every frame
def cb_frame_rendered(length, ls, red, green, blue):
    global r_index
    global g_index
    
    r = [0]*16
    g = [0]*16
    b = [0]*16
        
    if r_index == NUM_LEDS-1:
        r_index = 0
        g_index += NUM_LEDS
    else:
        r_index += 1

    if g_index==200:
        g_index=0
        ls.set_rgb_values(190, NUM_LEDS, [0]*16, [0]*16, [0]*16) 
        
    r = [red]*16
    g = [green]*16
    b = [blue]*16
    
    if g_index==200:
        r_index=NUM_LEDS-1
        
    if g_index > 0:
        ls.set_rgb_values(g_index-NUM_LEDS, NUM_LEDS, [0]*16, [0]*16, [0]*16)       

    # Set new data for next render cycle
    ls.set_rgb_values(g_index, NUM_LEDS, r, g, b)
  

    
if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ls = BrickletLEDStrip(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set frame duration to 50ms (20 frames per second)
    ls.set_frame_duration(10)

    # Register frame rendered callback to function cb_frame_rendered

    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         lambda x: cb_frame_rendered(x, ls, 0, 0, 255))


    # Set initial rgb values to get started
    ls.set_rgb_values(0, NUM_LEDS, r, g, b)

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
