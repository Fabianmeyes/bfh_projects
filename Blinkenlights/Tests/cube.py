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
    sleep(0.05)

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

def fCube (x,y):
    setCord(x,6,y+3,y+4,y+5,y+6,y+7,y+8,0,0,0,0)
    setCord(x+1,3,y+2,y+7,y+8,0,0,0,0,0,0,0)
    setCord(x+2,3,y+1,y+6,y+8,0,0,0,0,0,0,0)
    setCord(x+3,7,y,y+1,y+2,y+3,y+4,y+5,y+8,0,0,0)
    setCord(x+4,3,y,y+5,y+8,0,0,0,0,0,0,0)
    setCord(x+5,3,y,y+5,y+8,0,0,0,0,0,0,0)
    setCord(x+6,3,y,y+5,y+7,0,0,0,0,0,0,0)
    setCord(x+7,3,y,y+5,y+6,0,0,0,0,0,0,0)
    setCord(x+8,6,y,y+1,y+2,y+3,y+4,y+5,0,0,0,0)

if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    fClear()
    sleep(1)

    counter = 0

    while True:
        for i in range(24):
            setColor(counter%256,(10*counter)%256,(i*counter)%256)
            if i < 12:
                fCube(i+1,1)
                fOn()
                setColor(0,0,0)
                fCube(i+1,1)
            else:
                fCube(24-i,2)
                fOn()
                setColor(0,0,0)
                fCube(24-i,2)
            counter += 1
                              
    raw_input("Press key to exit\n")
    ipcon.disconnect()
