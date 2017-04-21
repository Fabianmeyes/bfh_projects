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

puls = 100

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

def fYellow():
    setColor(222,255,0)

def fOrange():
    setColor(255,155,0)

def fGreen():
    setColor(0,255,0)

def fBlue():
    setColor(0,0,255)

def fCyan():
    setColor(0,255,255)

def fRed():
    setColor(255,0,0)

def outerRing(position):
    fBlue()
    if position == 1:
        setCord(1,3,1,5,9,0,0,0,0,0,0,0)
        setCord(4,1,10,0,0,0,0,0,0,0,0,0)
        setCord(5,1,1,0,0,0,0,0,0,0,0,0)
        setCord(8,1,10,0,0,0,0,0,0,0,0,0)
        setCord(9,1,1,0,0,0,0,0,0,0,0,0)
        setCord(12,1,10,0,0,0,0,0,0,0,0,0)
        setCord(13,1,1,0,0,0,0,0,0,0,0,0)
        setCord(16,1,10,0,0,0,0,0,0,0,0,0)
        setCord(17,1,1,0,0,0,0,0,0,0,0,0)
        setCord(20,3,2,6,10,0,0,0,0,0,0,0)

    if position == 2:
        setCord(1,2,4,8,0,0,0,0,0,0,0,0)
        setCord(2,1,1,0,0,0,0,0,0,0,0,0)
        setCord(3,1,10,0,0,0,0,0,0,0,0,0)
        setCord(6,1,1,0,0,0,0,0,0,0,0,0)
        setCord(7,1,10,0,0,0,0,0,0,0,0,0)
        setCord(10,1,1,0,0,0,0,0,0,0,0,0)
        setCord(11,1,10,0,0,0,0,0,0,0,0,0)
        setCord(14,1,1,0,0,0,0,0,0,0,0,0)
        setCord(15,1,10,0,0,0,0,0,0,0,0,0)
        setCord(18,1,1,0,0,0,0,0,0,0,0,0)
        setCord(19,1,10,0,0,0,0,0,0,0,0,0)
        setCord(20,2,3,7,0,0,0,0,0,0,0,0)

    if position == 4:
        setCord(20,3,1,5,9,0,0,0,0,0,0,0)
        setCord(17,1,10,0,0,0,0,0,0,0,0,0)
        setCord(16,1,1,0,0,0,0,0,0,0,0,0)
        setCord(13,1,10,0,0,0,0,0,0,0,0,0)
        setCord(12,1,1,0,0,0,0,0,0,0,0,0)
        setCord(9,1,10,0,0,0,0,0,0,0,0,0)
        setCord(8,1,1,0,0,0,0,0,0,0,0,0)
        setCord(5,1,10,0,0,0,0,0,0,0,0,0)
        setCord(4,1,1,0,0,0,0,0,0,0,0,0)
        setCord(1,3,2,6,10,0,0,0,0,0,0,0)

    if position == 3:
        setCord(20,2,4,8,0,0,0,0,0,0,0,0)
        setCord(19,1,1,0,0,0,0,0,0,0,0,0)
        setCord(18,1,10,0,0,0,0,0,0,0,0,0)
        setCord(15,1,1,0,0,0,0,0,0,0,0,0)
        setCord(14,1,10,0,0,0,0,0,0,0,0,0)
        setCord(11,1,1,0,0,0,0,0,0,0,0,0)
        setCord(10,1,10,0,0,0,0,0,0,0,0,0)
        setCord(7,1,1,0,0,0,0,0,0,0,0,0)
        setCord(6,1,10,0,0,0,0,0,0,0,0,0)
        setCord(3,1,1,0,0,0,0,0,0,0,0,0)
        setCord(2,1,10,0,0,0,0,0,0,0,0,0)
        setCord(1,2,3,7,0,0,0,0,0,0,0,0)

def innerRing(position):
    fOrange()
    if position == 1:
        setCord(2,3,2,5,8,0,0,0,0,0,0,0)
        setCord(4,1,9,0,0,0,0,0,0,0,0,0)
        setCord(5,1,2,0,0,0,0,0,0,0,0,0)
        setCord(7,1,9,0,0,0,0,0,0,0,0,0)
        setCord(8,1,2,0,0,0,0,0,0,0,0,0)
        setCord(10,1,9,0,0,0,0,0,0,0,0,0)
        setCord(11,1,2,0,0,0,0,0,0,0,0,0)
        setCord(13,1,9,0,0,0,0,0,0,0,0,0)
        setCord(14,1,2,0,0,0,0,0,0,0,0,0)
        setCord(16,1,9,0,0,0,0,0,0,0,0,0)
        setCord(17,1,2,0,0,0,0,0,0,0,0,0)
        setCord(19,3,3,6,9,0,0,0,0,0,0,0)

    if position == 2:
        setCord(19,3,2,5,8,0,0,0,0,0,0,0)
        setCord(17,1,9,0,0,0,0,0,0,0,0,0)
        setCord(16,1,2,0,0,0,0,0,0,0,0,0)
        setCord(14,1,9,0,0,0,0,0,0,0,0,0)
        setCord(13,1,2,0,0,0,0,0,0,0,0,0)
        setCord(11,1,9,0,0,0,0,0,0,0,0,0)
        setCord(10,1,2,0,0,0,0,0,0,0,0,0)
        setCord(8,1,9,0,0,0,0,0,0,0,0,0)
        setCord(7,1,2,0,0,0,0,0,0,0,0,0)
        setCord(5,1,9,0,0,0,0,0,0,0,0,0)
        setCord(4,1,2,0,0,0,0,0,0,0,0,0)
        setCord(2,3,3,6,9,0,0,0,0,0,0,0)

    if position == 3:
        setCord(2,2,4,7,0,0,0,0,0,0,0,0)
        setCord(3,2,2,9,0,0,0,0,0,0,0,0)
        setCord(6,2,2,9,0,0,0,0,0,0,0,0)
        setCord(9,2,2,9,0,0,0,0,0,0,0,0)
        setCord(12,2,2,9,0,0,0,0,0,0,0,0)
        setCord(15,2,2,9,0,0,0,0,0,0,0,0)
        setCord(18,2,2,9,0,0,0,0,0,0,0,0)
        setCord(19,2,4,7,0,0,0,0,0,0,0,0)

def write(number,x,y):
    if number == 1:
        setCord(x,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)
        setCord(x+1,1,y+3,0,0,0,0,0,0,0,0,0)
        setCord(x+2,1,y+2,0,0,0,0,0,0,0,0,0)

    if number == 2:
        setCord(x,4,y,y+2,y+3,y+4,0,0,0,0,0,0)
        setCord(x+1,3,y,y+2,y+4,0,0,0,0,0,0,0)
        setCord(x+2,4,y,y+1,y+2,y+4,0,0,0,0,0,0)

    if number == 3:
        setCord(x,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)
        setCord(x+1,3,y,y+2,y+4,0,0,0,0,0,0,0)
        setCord(x+2,2,y,y+4,0,0,0,0,0,0,0,0)
        
    if number == 4:
        setCord(x,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)
        setCord(x+1,1,y+2,0,0,0,0,0,0,0,0,0)
        setCord(x+2,3,y+2,y+3,y+4,0,0,0,0,0,0,0)
        
    if number == 5:
        setCord(x+2,4,y,y+2,y+3,y+4,0,0,0,0,0,0)
        setCord(x+1,3,y,y+2,y+4,0,0,0,0,0,0,0)
        setCord(x,4,y,y+1,y+2,y+4,0,0,0,0,0,0)
        
    if number == 6:
        setCord(x+2,5,y,y+2,y+3,y+4,y+1,0,0,0,0,0)
        setCord(x+1,3,y,y+2,y+4,0,0,0,0,0,0,0)
        setCord(x,4,y,y+1,y+2,y+4,0,0,0,0,0,0)

    if number == 7:
        setCord(x,2,y+3,y+4,0,0,0,0,0,0,0,0)
        setCord(x+1,2,y+2,y+4,0,0,0,0,0,0,0,0)
        setCord(x+2,3,y,y+1,y+4,0,0,0,0,0,0,0)

    if number == 8:
        setCord(x,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)
        setCord(x+1,3,y,y+2,y+4,0,0,0,0,0,0,0)
        setCord(x+2,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)

    if number == 9:
        setCord(x+2,4,y,y+2,y+3,y+4,0,0,0,0,0,0)
        setCord(x+1,3,y,y+2,y+4,0,0,0,0,0,0,0)
        setCord(x,5,y,y+1,y+2,y+4,y+3,0,0,0,0,0)

    if number == 0:
        setCord(x,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)
        setCord(x+1,2,y,y+4,0,0,0,0,0,0,0,0)
        setCord(x+2,5,y,y+1,y+2,y+3,y+4,0,0,0,0,0)    
    

def writeNumber(number):
    if number > 9999:
        number = 9999

    counter = 0
    while number >= 1000:
        number -= 1000
        counter += 1      
    write(counter,15,3)
    
    counter = 0
    while number >= 100:
        number -= 100
        counter += 1      
    write(counter,11,3)
    
    counter = 0    
    while number >= 10:
        number -= 10
        counter += 1
    write(counter,7,3)
    
    counter = 0    
    while number >= 1:
        number -= 1
        counter += 1
    write(counter,3,3)
        
        

if __name__ == "__main__":
    ipcon = IPConnection()
    ls = BrickletLEDStrip(UID, ipcon)

    ipcon.connect(HOST, PORT)

    fClear()
    sleep(1)

    while True:
        while puls != 0:
            for i in range (12):
                fGreen()
                xLine(2)
                xLine(19)
                yLine(2)
                yLine(9)
                fYellow()
                xLine(1)
                xLine(20)
                yLine(1)
                yLine(10)
                outerRing(((i+1)%4)+1)
                innerRing(((i+1)%3)+1)
                fOn()

            setColor(0,0,0)
            writeNumber(puls)

##          puls messen
                    
            fCyan()
            writeNumber(puls)        
            fOn()

        while puls <= 0:

            setColor(0,0,0)
            writeNumber(puls)
            
            fRed()
            writeNumber(000)
            fOn()
            setColor(0,0,0)
            writeNumber(000)

            sleep(5)
            
##          puls messen            
                              
    raw_input("Press key to exit\n")
    ipcon.disconnect()
