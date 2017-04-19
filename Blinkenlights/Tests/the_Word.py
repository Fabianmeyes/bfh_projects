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

puls = 60

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_led_strip import BrickletLEDStrip

def fOn():
    for i in range (20):
            ls.set_rgb_values((i)*10, NUM_LEDS, red[i], green[i], blue[i])

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
    
    sleep(0.001)

def symDot(x,y):
    setCord(x,1,y,0,0,0,0,0,0,0,0,0)
    setCord(21-x,1,y,0,0,0,0,0,0,0,0,0)

def wingDot(x,y):
    setColor(250,0,0)
    symDot(x,y)
    setColor(250,50,0)
    symDot(x,y-1)
    if x % 2 == 1:
        setColor(250,50,0)
        symDot(x,y-1)
        if y >= 3:
            setColor(250,100,0)
            symDot(x,y-2)
            if y >= 4:
                setColor(250,150,0)
                symDot(x,y-3)
        
def deleteWing(x):

    setColor(0,0,0)
    xLine(x)
    xLine(21-x)
    
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
        ls.set_rgb_values(10*i, NUM_LEDS, [0]*16, [0]*16, [0]*16)

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

if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    fClear()
    sleep(1)

    ls.set_frame_duration(1)
  
    ls.register_callback(ls.CALLBACK_FRAME_RENDERED,
                         lambda w: fLight(x,anzahl,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,r,g,b))
    
    wingDot(9,8)
    wingDot(9,5)
    wingDot(10,9)
    wingDot(10,4)
    setColor(250,50,100)
    symDot(10,7)
    setColor(250,0,100)
    symDot(10,6)
    setColor(250,0,50)
    symDot(10,5)

    for i in range(8):
        wingDot(i+1,7)
    fOn()

    while True:
        deleteWing(1)
        deleteWing(2)
        wingDot(1,8)
        wingDot(2,8)
        fOn()
        sleep(0.3)
        
        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        wingDot(1,9)
        wingDot(2,9)
        wingDot(3,8)
        wingDot(4,8)
        fOn()

        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        deleteWing(5)
        deleteWing(6)
        wingDot(1,10)
        wingDot(2,10)
        wingDot(3,9)
        wingDot(4,9)
        wingDot(5,8)
        wingDot(6,8)
        fOn()

        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        deleteWing(5)
        deleteWing(6)
        wingDot(1,9)
        wingDot(2,9)
        wingDot(3,8)
        wingDot(4,8)
        wingDot(5,7)
        wingDot(6,7)
        fOn()
        sleep(0.2)

        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        wingDot(1,8)
        wingDot(2,8)
        wingDot(3,7)
        wingDot(4,7)
        fOn()
        sleep(0.4)

        deleteWing(1)
        deleteWing(2)
        wingDot(1,7)
        wingDot(2,7)
        fOn()
        sleep(0.45)

        deleteWing(1)
        deleteWing(2)
        wingDot(1,6)
        wingDot(2,6)
        fOn()
        sleep(0.25)
        
        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        wingDot(1,5)
        wingDot(2,5)
        wingDot(3,6)
        wingDot(4,6)
        fOn()
        sleep(0.1)

        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        deleteWing(5)
        deleteWing(6)
        wingDot(1,4)
        wingDot(2,4)
        wingDot(3,5)
        wingDot(4,5)
        wingDot(5,6)
        wingDot(6,6)
        fOn()

        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        deleteWing(5)
        deleteWing(6)
        wingDot(1,5)
        wingDot(2,5)
        wingDot(3,6)
        wingDot(4,6)
        wingDot(5,7)
        wingDot(6,7)
        fOn()
        sleep(0.2)
        
        deleteWing(1)
        deleteWing(2)
        deleteWing(3)
        deleteWing(4)
        wingDot(1,6)
        wingDot(2,6)
        wingDot(3,7)
        wingDot(4,7)
        fOn()
        sleep(0.45)

        deleteWing(1)
        deleteWing(2)
        wingDot(1,7)
        wingDot(2,7)
        fOn()
        sleep(0.45)
        
    raw_input("Press key to exit\n")
    ipcon.disconnect()
