# exerciese 1: Hello
def hello(name="Igor"):
    print ("Hello {}!".format(name))
    return

name=input("Whats your name:")

if __name__=="__main__":
    hello(name)

# exercise 2: y=x+1

import matplotlib.pyplot as plot
def f(x):
    return x+1
xs=list(range(-3,4))
ys=[]
for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()

#exercise 3: square of X
def f(x):
    return x*x
xs=list(range(-100,100))
ys=[]
for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()

#exercise 4: odd or even
def f(x):
    if x % 2:
        return 1
    else:
        return -1

xs=list(range(-5,5))
ys=[]
for x in xs:
    ys.append(f(x))

plot.bar(xs,ys)
plot.show()

#exercise 5/6: Sine
from numpy import arange
import math
def f(x):
    return x+1
xs=arange(-5,6,0.1)
ys=[]
for x in xs:
    ys.append(math.sin(x))

plot.plot(xs,ys)
plot.show()


#exercise 7: Degree conversion

def f(x):
    return ((x*1.8)+32)
xs=list(range(-40,100))
ys=[]
for x in xs:
    ys.append(f(x))

plot.plot(xs,ys)
plot.show()


#exercise 8/9: Play again
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

again=yes_no("Do you want to play again?")
print (again)
