
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

#Exercise 6: print a box
x=int(input("width:"))
y=int(input("hieght:"))

for i in range(y):
    if i==0 or i ==(y-1):
        print ("X"* x)
    else:
        print ("X" +" "*(x-2) +"X")


#exercise 7: print triangle
def triangle(i, t=0):
    if i==0:
        return 0
    else:
        print(' '*(i+1)+ '*'*(t*2+1))
        return triangle(i-1,t+1)

x=int(input("triangle height:"))
triangle(x)
#######
x=int(input("triangle height:"))
t=0
for i in range(x):
    print (' '*(x+1)+'*'*(t*2+1))
    x=x-1
    t=t+1

#exercise 9: mult table
x=11
for x in range(1,x):
    for i in range(x,11):
        print (str(x) +"X" +str(i) +"=" +str(x*i))
    print ("...")
    x+=1
    i+=1

#exercise 10: print banner

text= input("Banner text:")
for i in range(0,3):
    if i==0 or i == 2:
        print("*"*(len(text)+2))
    else:
        print ("*"+text+"*")


#exercise 11: triangle numbs
for i in range(1,100):
    print ((i*(i+1))//2)

#exercise 12: number factors

x=int(input("give me a number:"))
li=[]
for i in range(1,x):
    if x%i == False:
        li.append(i)
li.append(x)
print ("The factors of "+ str(x)+" are: "+ str(li))
