from turtle import*

setup()
title("Turtle Test")
clear()
width(3)

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
    fillcolor(clr)
    if fl == True:
        begin_fill()
        for i in range(3):
            forward(100)
            left(120)
        end_fill()
        shapesize(sz,sz,)


# square
def square(sz, clr, fl):
    fillcolor(clr)
    for i in range(4):
        forward(100)
        right(90)

# pentagon
def pentagon(sz, clr, fl):
    fillcolor(clr)
    for i in range(sz, clr, fl):
        forward(100)
        left(72)

# hexagon
def hexagon(sz, clr, fl):
    fillcolor(clr)
    for i in range(6):
        forward(100)
        left(60)

# octagon
def octagon(sz, clr, fl):
    fillcolor(clr)
    for i in range(8):
        forward(100)
        left(45)

# star
def star(sz, clr, fl):
    fillcolor(clr)
    for i in range(5):
        forward(100)
        right(144)


#cirlce
def crcl(sz, clr, fl):
    fillcolor(clr)
    circle(100)



shapeIndex={'triangle':triangle,'square':square,'pentagon':pentagon,'hexagon':hexagon,'octagon':octagon,'star':star,'circle':crcl}
