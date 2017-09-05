from turtle import *
from random import *
#1
speed(-1)
def drawsquare(lgt,clr):
    color(clr)
    for i in range(4):
        forward(lgt)
        left(90)

drawsquare(100,'red')
#2
for i in range (30):
    drawsquare(i * 5 , 'red' )
    left( 17 )
    penup()
    forward(i * 2 )
    pendown()

mainloop()