#exercise 8:Multiply vectors
list1=[1,3,5]
list2=[2,4,6]
result=[]
for i in range(len(list1)):
    result.append(list1[i] * list2[i])

print (result)

#exercise 9: Matrix addition

list3=[[1,2,3],[4,5,6]]
list4=[[7,8,9],[10,11,12]]
sum_result=[]
for i in range(len(list3)):
    row=[]
    for j in range(len(list3[i])):
        row.append(list3[i][j]+list4[i][j])
    sum_result.append(row)
print (sum_result)
