from turtle import*
import random

setup()
title("night sky")
clear()
width(3)
pencolor("yellow")
bgcolor("black")

def crcl():

    fillcolor("silver")
    begin_fill()
    circle(50)
    end_fill()

def star():

    fillcolor("yellow")
    begin_fill()

    for i in range(5):
        forward(20)
        right(144)
    end_fill()
speed(100)
ht()
up()

setposition(-300,100)
down()
crcl()
for i in range(50):
    x=random.randint(-500,500)
    y=random.randint(-400,400)
    up()
    setposition(x,y)
    down()
    star()

input("Press Enter to continue...")
