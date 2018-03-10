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



#Exercise 4: JSON file plot
