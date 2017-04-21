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
            ls.set_rgb_values((i)*10, NUM_LEDS, red[i], green[i], blue[i])
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

def putDot(x,y):
    setCord(x,1,y,0,0,0,0,0,0,0,0,0)

def deleteDot(x,y):
    saveR = r
    saveG = g
    saveB = b
    setColor(10-10.0*g/(r+g),10.0*g/(r+g),0)
    putDot(x,y)
    setColor(saveR,saveG,saveB)

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

def symTripple(x,anzahl,y2,y3,y4,y5,y6,y7,y8,y9):
    for i in range (3):
        setCord(x+i*7,anzahl,y2,y3,y4,y5,y6,y7,y8,y9,0,0)
        setCord(7*(i+1)-x,anzahl,y2,y3,y4,y5,y6,y7,y8,y9,0,0)
                
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
    fOn()

if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    fClear()
    sleep(1)
    
    setColor(255,255,255)
    
    yLine(1)
    yLine(10)

    fOn()
    
    setColor(10,255,25)
    
    for i in range(255):

        setColor(i,255-i,0)

        deleteDot(3,6)
        putDot(20,5)
        deleteDot(2,6)
        putDot(19,5)
        deleteDot(1,6)
        putDot(18,5)
        deleteDot(20,5)
        putDot(17,5)
        deleteDot(19,5)
        putDot(16,5)
        deleteDot(18,5)
        putDot(15,5)
        deleteDot(17,5)
        putDot(14,5)
        deleteDot(16,5)
        putDot(13,6)
        deleteDot(15,5)
        putDot(13,7)
        deleteDot(14,5)
        putDot(12,8)
        deleteDot(13,6)
        putDot(12,9)
        deleteDot(13,7)
        putDot(11,7)
        deleteDot(12,9)
        putDot(11,6)
        deleteDot(12,8)
        putDot(10,5)
        deleteDot(11,7)
        putDot(10,4)
        deleteDot(11,6)
        putDot(9,3)
        deleteDot(10,5)
        putDot(9,2)
        deleteDot(10,4)
        putDot(8,4)
        deleteDot(9,2)
        putDot(8,5)
        deleteDot(9,3)
        putDot(7,6)
        deleteDot(8,4)
        putDot(6,6)
        deleteDot(8,5)
        putDot(5,6)
        deleteDot(7,6)
        putDot(4,6)
        deleteDot(6,6)
        putDot(3,6)
        deleteDot(5,6)
        putDot(2,6)
        deleteDot(4,6)
        putDot(1,6)

        
    fClear()
    setColor(255,0,0)
    yLine(6)
    yLine(5)

    
    
    raw_input("Press key to exit\n")
    ipcon.disconnect()
