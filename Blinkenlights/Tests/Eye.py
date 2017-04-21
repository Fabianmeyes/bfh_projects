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
rrrr = 0.0
gggg = 0.0
bbbb = 0.0
indicatorR = 0
indicatorG = 0
indicatorB = 0

global speed
speed = 1000

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

def fOn():
    for i in range (20):
            ls.set_rgb_values((i)*10, NUM_LEDS, red[i], green[i], blue[i])
    sleep(1.0/speed)

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
    saveR = r
    saveG = g
    saveB = b
    setColor(0,0,0)
    for i in range(20):
        setColor(0,0,0)
        xLine(i+1)
    setColor(saveR,saveG,saveB)

def symCord(x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10):
    setCord(x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10)
    setCord(21-x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10)
    

def symDiCord(x,y1,y2):
    symCord(x,2,y1,y2,0,0,0,0,0,0,0,0)

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

def fLook(x):
    setColor(0,0,0)
    
    setCord(x,2,5,6,0,0,0,0,0,0,0,0)
    setCord(x+1,2,5,6,0,0,0,0,0,0,0,0)
    
    setColor(rrrr,gggg,bbbb)
    
    setCord(x-1,2,5,6,0,0,0,0,0,0,0,0)
    setCord(x,2,4,7,0,0,0,0,0,0,0,0)
    setCord(x+1,2,4,7,0,0,0,0,0,0,0,0)
    setCord(x+2,2,5,6,0,0,0,0,0,0,0,0)

def fEye(x):
    setColor(255,255,255)
        
    symDiCord(3,5,6)
    symCord(4,4,4,5,6,7,0,0,0,0,0,0)
    symCord(5,4,4,5,6,7,0,0,0,0,0,0)
    symCord(6,6,4,5,6,7,3,8,0,0,0,0)
    symCord(7,6,4,5,6,7,3,8,0,0,0,0)
    symCord(8,6,4,5,6,7,3,8,0,0,0,0)
    symCord(9,8,4,5,6,7,3,8,2,9,0,0)
    symCord(10,8,4,5,6,7,3,8,2,9,0,0)
    symDiCord(2,5,6)
    symDiCord(3,4,7)
    symDiCord(5,3,8)
    symDiCord(8,2,9)

    fLook(x)

    setColor(bbbb,gggg,rrrr)
        
    symDiCord(1,5,6)
    symDiCord(2,4,7)
    symDiCord(3,3,8)
    symDiCord(4,3,8)
    symDiCord(5,2,9)
    symDiCord(6,2,9)
    symDiCord(7,2,9)
    symDiCord(8,1,10)
    symDiCord(9,1,10)
    symDiCord(10,1,10)
    
    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(1,4,7)
    symDiCord(2,3,8)
    symDiCord(4,2,9)
    symDiCord(7,1,10)

        
def fBlink(x):

    for i in range (25):
        fEye(x)
        fOn()
        
    setColor(bbbb,gggg,rrrr)

    yLine(9)
    yLine(2)

    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(4,2,9)
    setColor(0,0,0)
    symDiCord(3,2,9)
    symDiCord(2,2,9)
    symDiCord(1,2,9)
    fOn()

    setColor(bbbb,gggg,rrrr)

    yLine(8)
    yLine(3)

    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(2,3,8)
    setColor(0,0,0)
    symDiCord(1,3,8)
    fOn()

    for i in range(5):
        setColor(bbbb,gggg,rrrr)
        
        yLine(7)
        yLine(4)

        setColor(bbbb/10,gggg/10,rrrr/10)

        symDiCord(1,4,7)
        fOn()

        setColor(bbbb,gggg,rrrr)

        yLine(6)
        yLine(5)
        fOn()

    fEye(x)
    
    setColor(bbbb,gggg,rrrr)

    yLine(9)
    yLine(2)

    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(4,2,9)
    setColor(0,0,0)
    symDiCord(3,2,9)
    symDiCord(2,2,9)
    symDiCord(1,2,9)

    setColor(bbbb,gggg,rrrr)

    yLine(8)
    yLine(3)
    
    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(2,3,8)
    setColor(0,0,0)
    symDiCord(1,3,8)

    setColor(bbbb,gggg,rrrr)

    yLine(7)
    yLine(4)

    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(1,4,7)
    fOn()

    fEye(x)

    setColor(bbbb,gggg,rrrr)
    
    yLine(9)
    yLine(2)
    
    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(4,2,9)
    setColor(0,0,0)
    symDiCord(3,2,9)
    symDiCord(2,2,9)
    symDiCord(1,2,9)

    setColor(bbbb,gggg,rrrr)

    yLine(8)
    yLine(3)

    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(2,3,8)
    setColor(0,0,0)
    symDiCord(1,3,8)
    fOn()

    fEye(x)
    
    setColor(bbbb,gggg,rrrr)

    yLine(9)
    yLine(2)
    
    setColor(bbbb/10,gggg/10,rrrr/10)

    symDiCord(4,2,9)
    setColor(0,0,0)
    symDiCord(3,2,9)
    symDiCord(2,2,9)
    symDiCord(1,2,9)
    fOn()

    for i in range (25):
        fEye(x)
        fOn()

def fTime():
    
    global rrrr
    global gggg
    global bbbb
    global indicatorR
    global indicatorG
    global indicatorB

    if indicatorR%510 < 255:
        rrrr += 1
    else:
        rrrr -= 1
    indicatorR += 1

    if rrrr == 255:
        if indicatorG%510 < 255:
            gggg += 1
        else:
            gggg -= 1
        indicatorG += 1
        
        if gggg == 255:
            if indicatorB%510 < 255:
                bbbb += 1
            else:
                bbbb -= 1
            indicatorB += 1        
    
if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    fClear()
    sleep(1)

    ls.set_frame_duration(1000.0/speed)
  
    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                     lambda w: fTime())

    while True:
        for i in range(3,18):
            
            fEye(i)
            fOn()
            
            if i == 10:
                fBlink(i)
                
        for i in range (25):
            fEye(17)
            fOn()

        for i in range(3,18):

            fEye(20-i)

            fOn()

        for i in range (25):
            fEye(3)
            fOn()
      
    raw_input("Press key to exit\n")
    ipcon.disconnect()
