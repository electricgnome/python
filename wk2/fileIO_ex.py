#Exercise 1: prompt for file name, and prints contents

fname=input("Read file:")

with open(fname, 'r') as file_handle:
  contents = file_handle.read()

print(contents)

#Exercise 2: prompt user for file name and contents and saves to file
fname=input("file:")
acontents=input("start typing:")

with open(fname, 'a') as file_handle:
  file_handle.write(acontents)

print(acontents)


#Exercise 3: print word/letter histogram of a file
from collections import Counter

char_dic=dict()
word_dic=dict()
def char_count(content):
    content=content.replace(' ','')
    for c in range(len(content)):
        if content.lower()[c] in char_dic:
            char_dic[content.lower()[c]]+=1
        elif content.lower()[c] :
            char_dic[content.lower()[c]]= 1
    return char_dic

def word_count(content):
    content=content.lower()
    words=content.split()

    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic

fname=input("Read file:")

with open(fname, 'r') as file_handle:
  content = file_handle.read()



word_count(content)
top=dict(Counter(word_dic).most_common(3))
print (word_dic)
# print (top)

char_count(content)
top_c=dict(Counter(char_dic).most_common(3))
print (char_dic)
# print(top_c)

#Exercise 4: JSON file plot

import json
import matplotlib.pyplot as plot

data={"data":[[1,1],[2,3],[5,8],[9,-10],[-5,20],[9,8]]}
# data={"data":[[1,1],[2,2],[3,3],[4,4]]}
with open('data.json','w') as fh:
    json.dump(data,fh)

with open('data.json', 'r') as fh:
    jsdata=json.load(fh)
    print (json.dumps(jsdata))
    plot.plot(jsdata['data'])
    plot.show()
