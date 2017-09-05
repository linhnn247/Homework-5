from turtle import *
import random
#1
def drawstar(x,y,sz):
    penup()
    goto(x,y)
    pendown()
    left(36)
    for i in range(5):
        forward(sz)
        left(144)
    right(36)

#2 Hàm random.randint(a,b) là đưa ra 1 số nguyên bất kỳ nhỏ hơn b và >= a
hideturtle()
speed( 0 )
colormode(255)

for i in range ( 100 ):
    import random
    clr1 = random.randint(1, 255)
    clr2 = random.randint(1, 255)
    clr3 = random.randint(1, 255)
    color(clr1, clr2, clr3)
    x = random.randint(- 300 , 300 )
    y = random.randint(- 300 , 300 )
    length = random.randint( 3 , 10 )
    drawstar(x , y , length)


mainloop()

#