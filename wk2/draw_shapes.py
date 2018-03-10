from turtle import*
import shapes

menu=""" You can draw:
    a triangle,
    a square,
    a pentagon,
    a hexagon,
    an octagon,
    a star,
    or a circle
    to quit type 'exit'"""

def yes_no(answer):
    yes=(['yes','y','ye',''])
    no=(['no','n'])
    while True:
        choice= input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print ("Please respond with 'yes' or 'no'")

def sizef(numb):
    while True:
        try:
            choice=int(input(numb))
            return choice
        except ValueError:
            print ("please use a number between 1 and 50")

def colorf(colorin):
    while True:
        try:
            color=input(colorin)
            fillcolor(color)
            return color
        except:
            print("We don't have that color, please try another")


if __name__=="__main__":

    print(menu)

    while True:
        try:
            shape = input("what would you like to draw:")
            if shape =="exit":
                print("Good bye!")
                break
            else:
                shapes.shapeIndex[shape]
                size = sizef("What size[1-50]:")
                fill = yes_no("FillY [Y/n]:")
                if fill:
                    color = colorf("What color:")
                    shapes.shapeIndex[shape](size, color, fill)

            shapes.shapeIndex[shape](size, color, fill)

        except KeyError:
            print("Please try again")
