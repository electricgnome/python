#exercise 1: 1 to 10
for i in range(1,11):
    print (i)

#exercise 2: n to m
n= int(input("initial number:"))
m= int(input("final number:"))

for i in range(n,m+1):
    print (i)

#exercise 3: odd numbers
for i in range(1,11):
    if i %2:
        print (i)

#exercise 4: print square
for i in range(0,5):
    print("*" * 5)

#exercise 5: N square
n = int(input("How big of a square?"))
for i in range(n):
    print("*"*n)

#exercise 6: print a box
n= int(input("height:"))
m= int(input("width:"))

for i in range(n):


#exercise 7: triangle
x=0
for i in range(7):
    x=+ i+i
    print ("*"*x)
