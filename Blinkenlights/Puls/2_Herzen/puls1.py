from time import sleep

HOST = "localhost"
PORT = 4223
UID = "wVj"

NUM_LEDS = 10

red = []
green = []
blue = []

for i in range (1):
    red.append([0]*16)
    green.append([0]*16)
    blue.append([0]*16)

r_index = 0
g_index = 0
x = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
y7 = 0
y8 = 0
y9 = 0
y10 = 0
r = 0
g = 0
b = 0

puls = 60

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

def fOn():
    for i in range (1):
            ls.set_rgb_values((i+9)*10, NUM_LEDS, red[i], green[i], blue[i])

def setCord(fx,fanzahl,fy1,fy2,fy3,fy4,fy5,fy6,fy7,fy8,fy9,fy10):
    global x
    x=fx

    global anzahl
    anzahl = fanzahl
    
    global y1
    y1=fy1
    
    global y2
    y2=fy2
    
    global y3
    y3=fy3
    
    global y4
    y4=fy4
    
    global y5
    y5=fy5
    
    global y6
    y6=fy6

    global y7
    y7=fy7
    
    global y8
    y8=fy8
    
    global y9
    y9=fy9
    
    global y10
    y10=fy10
    
    fLight(x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,r,g,b)

def setColor(fr,fg,fb):
    global r
    r=fr
    global g
    g=fg    
    global b
    b=fb

def xLine(x):
     setCord(x,10,1,2,3,4,5,6,7,8,9,10)

def fClear():
    for i in range(1):
        setColor(0,0,0)
        xLine(i+1)

def fLight(x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,r,g,b):
   
    global r_index
    global g_index

    g_index=x

    Ys = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]

    for y in range (anzahl):
    
        if g_index % 2==0:
            r_index = Ys[y]-1
        else:
            r_index = 10-Ys[y]
        
        red[g_index-1][r_index] = r
        green[g_index-1][r_index] = g
        blue[g_index-1][r_index] = b

def putDot(y):
    setCord(1,1,y,0,0,0,0,0,0,0,0,0)

def showPuls(puls):
    if puls >= 128:
        putDot(9)
        puls -= 128
    if puls >= 64:
        putDot(8)
        puls -= 64
    if puls >= 32:
        putDot(7)
        puls -= 32
    if puls >= 16:
        putDot(6)
        puls -= 16
    if puls >= 8:
        putDot(5)
        puls -= 8
    if puls >= 4:
        putDot(4)
        puls -= 4
    if puls >= 2:
        putDot(3)
        puls -= 2
    if puls >= 1:
        putDot(2)

if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    fClear()
    sleep(1)

    setColor(255,255,255)

    putDot(1)
    putDot(10)

    while True:
        while puls != 0:
            setColor(2,255,55)
            showPuls(puls)   
            fOn()
            sleep(1)
            setColor(0,0,0)
            showPuls(puls)
            fOn()
##            puls messen
        setColor(255,2,55)
        xLine(1)  
        fOn()
        while puls == 0:
            sleep(0.001)
##            puls messen
        setColor(0,0,0)
        xLine(1)


    raw_input("Press key to exit\n")
    ipcon.disconnect()
