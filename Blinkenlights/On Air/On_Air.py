from time import sleep

HOST = "localhost"
PORT = 4223
UID = "wVj"

NUM_LEDS = 10

red = []
green = []
blue = []

for i in range (20):
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

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

def fOn():
    for i in range (20):
            ls.set_rgb_values(i*10, NUM_LEDS, red[i], green[i], blue[i])
    sleep(0.001)
    

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

def yLine(y):
    for i in range (20):
        setCord(i+1,1,y,0,0,0,0,0,0,0,0,0)
               
def fClear():
    for i in range(20):
        setColor(0,0,0)
        xLine(i+1)

def fLight(x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,r,g,b):
   
    global r_index
    global g_index

    g_index=x

    Ys = [y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]

    for y in range (anzahl):
    
        if g_index % 2==1:
            r_index = Ys[y]-1
        else:
            r_index = 10-Ys[y]
        
        red[g_index-1][r_index] = r
        green[g_index-1][r_index] = g
        blue[g_index-1][r_index] = b

def fRed(color):
    if color%100 < 50:
        setColor(5*(color%50)+5,0,0)
    else:
        setColor(5*(50.0-(color%50+1))+5,0,0)

def fRing(position):
    position = (position%4) + 1
    if position == 1:
        setCord(1,2,2,9,0,0,0,0,0,0,0,0)
        setCord(4,2,1,10,0,0,0,0,0,0,0,0)
        setCord(5,2,2,9,0,0,0,0,0,0,0,0)
        setCord(8,2,1,10,0,0,0,0,0,0,0,0)
        setCord(9,2,2,9,0,0,0,0,0,0,0,0)
        setCord(12,2,1,10,0,0,0,0,0,0,0,0)
        setCord(13,2,2,9,0,0,0,0,0,0,0,0)
        setCord(16,2,1,10,0,0,0,0,0,0,0,0)
        setCord(17,2,2,9,0,0,0,0,0,0,0,0)
        setCord(20,2,1,10,0,0,0,0,0,0,0,0)

    if position == 2:
        setCord(4,2,2,9,0,0,0,0,0,0,0,0)
        setCord(5,2,1,10,0,0,0,0,0,0,0,0)
        setCord(8,2,2,9,0,0,0,0,0,0,0,0)
        setCord(9,2,1,10,0,0,0,0,0,0,0,0)
        setCord(12,2,2,9,0,0,0,0,0,0,0,0)
        setCord(13,2,1,10,0,0,0,0,0,0,0,0)
        setCord(16,2,2,9,0,0,0,0,0,0,0,0)
        setCord(17,2,1,10,0,0,0,0,0,0,0,0)
        setCord(20,2,2,9,0,0,0,0,0,0,0,0)
        setCord(1,2,1,10,0,0,0,0,0,0,0,0)

    if position == 3:
        setCord(3,2,2,9,0,0,0,0,0,0,0,0)
        setCord(6,2,1,10,0,0,0,0,0,0,0,0)
        setCord(7,2,2,9,0,0,0,0,0,0,0,0)
        setCord(10,2,1,10,0,0,0,0,0,0,0,0)
        setCord(11,2,2,9,0,0,0,0,0,0,0,0)
        setCord(14,2,1,10,0,0,0,0,0,0,0,0)
        setCord(15,2,2,9,0,0,0,0,0,0,0,0)
        setCord(18,2,1,10,0,0,0,0,0,0,0,0)
        setCord(19,2,2,9,0,0,0,0,0,0,0,0)
        setCord(2,2,1,10,0,0,0,0,0,0,0,0)

    if position == 4:
        setCord(6,2,2,9,0,0,0,0,0,0,0,0)
        setCord(7,2,1,10,0,0,0,0,0,0,0,0)
        setCord(10,2,2,9,0,0,0,0,0,0,0,0)
        setCord(11,2,1,10,0,0,0,0,0,0,0,0)
        setCord(14,2,2,9,0,0,0,0,0,0,0,0)
        setCord(15,2,1,10,0,0,0,0,0,0,0,0)
        setCord(18,2,2,9,0,0,0,0,0,0,0,0)
        setCord(19,2,1,10,0,0,0,0,0,0,0,0)
        setCord(2,2,2,9,0,0,0,0,0,0,0,0)
        setCord(3,2,1,10,0,0,0,0,0,0,0,0)

def onAir():
    setCord(1,2,4,6,0,0,0,0,0,0,0,0)
    setCord(2,2,5,7,0,0,0,0,0,0,0,0)
    setCord(3,4,4,5,6,7,0,0,0,0,0,0)
    setCord(5,4,4,5,6,7,0,0,0,0,0,0)
    setCord(7,3,4,5,6,0,0,0,0,0,0,0)
    setCord(8,2,5,7,0,0,0,0,0,0,0,0)
    setCord(9,3,4,5,6,0,0,0,0,0,0,0)
    setCord(12,4,4,5,6,7,0,0,0,0,0,0)
    setCord(13,1,5,0,0,0,0,0,0,0,0,0)
    setCord(14,1,6,0,0,0,0,0,0,0,0,0)
    setCord(15,4,4,5,6,7,0,0,0,0,0,0)
    setCord(17,2,6,5,0,0,0,0,0,0,0,0)
    setCord(18,2,4,7,0,0,0,0,0,0,0,0)
    setCord(19,2,4,7,0,0,0,0,0,0,0,0)
    setCord(20,2,6,5,0,0,0,0,0,0,0,0)


if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    sleep(1)
    fClear()

    counter = 0

    for i in range(20):
        setColor(10,10,10)
        xLine(i+1)

    while True:
        fRed(counter-75)
        fRing(4)
        fRed(counter-50)
        fRing(3)
        fRed(counter-25)
        fRing(2)
        fRed(counter)
        fRing(1)
        fRed(counter)
        onAir()
        fOn()
        counter += 1
                                                    
    raw_input("Press key to exit\n")
    ipcon.disconnect()
