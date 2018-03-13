#Exercise 1: 1-4
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print("Elizabeth: {}".format(phonebook_dict['Elizabeth']))
phonebook_dict["Kareem"]='938-489-1234'
del phonebook_dict['Alice']
phonebook_dict.update({'Bob':'968-345-2345'})
print(phonebook_dict)

# Exercise 2: Nested dictionaries

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

ramit_email= ramit['email']
print (ramit_email)
print (ramit['interests'][0])
print (ramit['friends'][0].get('email', {}))

print (ramit['interests'][1])

#Exercise 3: Letter Summary
char_dic=dict()
def char_count(content):
    content=content.replace(' ','')
    for c in range(len(content)):
        if content.lower()[c] in char_dic:
            char_dic[content.lower()[c]]+=1
        elif content.lower()[c] :
            char_dic[content.lower()[c]]= 1
    return char_dic


#Exercise 4: Word Summary
word_dic=dict()
def word_count(content):
    content=content.lower()
    words=content.split()

    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic

#Bonus: Print top 3 words/letters
word_count(content)
top=dict(Counter(word_dic).most_common(3))
print (top)

char_count(content)
top_c=dict(Counter(char_dic).most_common(3))
print(top_c)
