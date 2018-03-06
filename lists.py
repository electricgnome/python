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
