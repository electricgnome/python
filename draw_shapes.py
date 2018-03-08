from turtle import*
import shapes

menu=""" You can draw:
    a triangle,
    a square,
    a pentagon,
    a hexagon,
    an octagon,
    a star,
    or a circle"""

# setup()
# title("Turtle Test")
# clear()
# pencolor('green')
# width(3)


if __name__=="__main__":

    print(menu)

    while True:
        try:

            shape = input("what would you like to draw:")
            size = input("What size:")
            color = input("What color:")
            fill = input("Fill Y/n:")
            shapes.shapeIndex[shape](size, color, fill)
        except KeyError:
            print("Please try again")
