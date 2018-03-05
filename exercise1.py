#  Exercise 1
name = input('What is your name?'.upper()).upper()
print (("Hello, " + name + "!").upper())
#  Exercise 2 count letteres in name
letters= len(name)
print (('your name has ' + str(len(name)) + ' letteres in it! Awesome!').upper())

#  Exercise 3: madlib
print ("Please fill in the blanks!")
print ("_____ had a little _____")
mary = input("First blank:")
lamb = input("Second blank:")
print ("{} had a little {}".format(mary, lamb))

#  Exercise 4: Day of week
week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

day = int(input("Day (0-6)?"))
print (week[day])

#  Exercise 5: Work or sleep?
day = int(input("Day (0-6)?"))

if day <5:
    print ("Go to work!")
else:
    print ("Sleep in")

#  Exercise 6: C to F converter
temp = int(input("Temp in C?"))

far = (temp * 1.8) +32

print (str(far) + "F")

#  Exercise 7/8: Tip calc.
bill = int(input ("Bill amount?"))
qc = {"good":0.20, "fair":0.15, "bad":0.10}
service = input ("Level of service?")
people =int(input("How many people?"))
tip = bill * qc[service]

total = bill + tip
split = total/people
print ("Tip amount $" + str(tip))
print ("Total amount $" + str(total))
print ("Amount per person $" + str(split))

#  Exercise 9: print 1 to 10
i =1
while (i < 11):
    print (i)
    i +=1


#  Exercise 10: How many coins?
coins = 0
choice = "yes"
print ("you have " + str(coins) + " coins.")

while (choice == "yes"):
    choice = input("Do you want another?")
    if choice == "yes":
        coins +=1
        print ("you have " + str(coins) + " coins.")
    else:
        print ("Bye!!")
