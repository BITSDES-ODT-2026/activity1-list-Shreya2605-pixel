# LEDs code using list inside a list
from machine import Pin
import time
V = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
R = Pin(19, Pin.OUT)
Y = Pin(4, Pin.OUT)
B = Pin(5, Pin.OUT)
G = Pin(21, Pin.OUT)
while True:
    for i in V:
        R.value(i[0])
        time.sleep(0.3)
        Y.value(i[1])
        time.sleep(0.3)
        B.value(i[2])
        time.sleep(0.3)
        G.value(i[3])
        time.sleep(0.3)
