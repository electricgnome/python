# file_handle = open('hello.txt', 'w')
# file_handle.write('Hello World\n')
# file_handle.close()

# file_handle = open('hello.txt', 'r')
# contents = file_handle.read()
# file_handle.close()
# print(contents)
#
# file_handle = open('hello.txt', 'r')
# line1 = file_handle.readline()
# file_handle.close()
# print(line1)


# file_handle = open('hello.txt', 'r')
# while True:
#   char = file_handle.read(1)
#   if not char:
#     break
#   else:
#     print(char)
# file_handle.close()


# import pickle
# data = {'name': 'Paul'}
# with open('data.pickle', 'wb') as fh:
#   pickle.dump(data, fh)


import json
data = {
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
with open('data.json', 'w') as fh:
  json.dump(data, fh)
with open('data.json', 'r') as fh:
  data = json.load(fh)
  print(data)
