from turtle import*

setup()
title("Turtle Test")
clear()
width(3)
pencolor("green")
# exercise 0: run slide code
# down()
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
#
# # move into position
# up()
# forward(50)
# left(90)
# forward(50)
# left(90)
# down()
# # draw the square
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# for i in range(5):
#     forward(100)
#     right(144)
# mainloop()

# equal triangle
def triangle(sz, clr, fl):

    if fl == True:
        fillcolor(clr)
        begin_fill()

    for i in range(3):
        forward(sz*10)
        left(120)

    end_fill()
    ht()




# square
def square(sz, clr, fl):
    if fl == True:
        fillcolor(clr)
        begin_fill()

    for i in range(4):
        forward(100)
        right(90)
    end_fill()
    ht()
# pentagon
def pentagon(sz, clr, fl):
    if fl == True:
        fillcolor(clr)
        begin_fill()

    for i in range(5):
        forward(100)
        left(72)
    end_fill()
    ht()
# hexagon
def hexagon(sz, clr, fl):
    if fl == True:
        fillcolor(clr)
        begin_fill()

    for i in range(6):
        forward(100)
        left(60)
    end_fill()
    ht()
# octagon
def octagon(sz, clr, fl):
    if fl == True:
        fillcolor(clr)
        begin_fill()

    for i in range(8):
        forward(100)
        left(45)
    end_fill()
    ht()
# star
def star(sz, clr, fl):
    if fl == True:
        fillcolor(clr)
        begin_fill()

    for i in range(5):
        forward(100)
        right(144)
    end_fill()
    ht()

#cirlce
def crcl(sz, clr, fl):
    if fl == True:
        fillcolor(clr)
        begin_fill()

    fillcolor(clr)
    circle(100)
    end_fill()
    ht()


shapeIndex={'triangle':triangle,'square':square,'pentagon':pentagon,'hexagon':hexagon,'octagon':octagon,'star':star,'circle':crcl}
