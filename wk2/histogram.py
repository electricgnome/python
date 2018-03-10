from collections import Counter

content="Here here is is is is is a a a a a a a a a a a a a a a sentence with lots of letters that make up words. Let's see what is the most common letter used."
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

word_count(content)
top=dict(Counter(word_dic).most_common(3))
print (top)

char_count(content)
top_c=dict(Counter(char_dic).most_common(3))
print(top_c)
