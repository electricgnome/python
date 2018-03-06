
numbs =[1,2,50,22,12,3,4,5,6,7,8,9, -1,-2,-3,-4,-5,-6,-7,]
#Exercise 1: sum of numbers
for number in numbs:
    numbsSum +=number
print (numbsSum)

#Exercise 2: largest number
numbs.sort()
print ("largest number in the list is:" + str(max(numbs)))

#Exercise  3: Smallest number
print ("smallest number in the list is:" + str(min(numbs)))

#Exercise 4: Even numbers
for number in range(len(numbs)):
    if numbs[number]%2 ==0:
        print (numbs[number])

#Exercise 5,6: positive numbers new list
numbs2 = []
for number in range(len(numbs)):
    if numbs[number] >0:
        numbs2.append(numbs[number])

print (numbs2)

#Exercise 7: Multiply list


#exercise 8:Multiply vectors
list1=[1,3,5]
list2=[2,4,6]
result=[]
for i in range(len(list1)):
    result.append(list1[i] * list2[i])

print (result)

#exercise 9/10: Matrix addition

list3=[[1,2,3,7,8,9],[4,5,6,1,2,3]]
list4=[[7,8,9,4,5,6],[1,2,5,10,11,12]]
sum_result=[]
for i in range(len(list3)):
    row=[]
    for j in range(len(list3[i])):
        row.append(list3[i][j]+list4[i][j])
    sum_result.append(row)
print (sum_result)

#exercise 11: De-dup
list5= [1,2,3,4,5,6,7,8,9,0,0,9,8,7,6,5,4,3,2,1, "some", "words","here", "some", "words", "here"]
list5 = set(list5)
list6 = list(list5)
print (list6)

#exercise: bonus

import numpy as np
x = [[1,2],[4,5]]
y = [[7,8],[10,11]]

mx=np.matrix(x)
my=np.matrix(y)
mx*my
