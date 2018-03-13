#phonebook
import json

# with open('phonebook.json', 'r') as fh:
#   data = json.load(fh)

print(""" ======================
    1. Look up an entry
    2. Add an entry
    3. Delete an entry
    4. List all entries
    5. Exit
    """)
	1. Look up an entry
	2. Add an entry
	3. Delete an entry
	4. List all entries
	5. Exit
	""")


def menu():
    with open('phonebook.json', 'r') as fh:
      data = json.load(fh)

    while True:
        try:
            choice = int(input("(1-5)>>"))
        except ValueError:
            print("please use a number between 1 and 5.")
            continue


        if 1 <= choice <=5:
            if choice == 1:
                with open('phonebook.json', 'r') as fh:
                  data = json.load(fh)
                  name=input("Look up name:").lower()
                  print(data[name])

            elif choice == 2:
                print("New Entry")
                name=input("Name:").lower()
                phone=input("Phone:")
                data[name]=phone


                with open('phonebook.json', 'w') as fh:
                  json.dump(data, fh)

            elif choice == 3:
                with open('phonebook.json', 'r') as fh:
                  data = json.load(fh)
                  name=input("Entry to delete:")
                  del data[name]


            elif choice == 4:
                with open('phonebook.json', 'r') as fh:
                  data = json.load(fh)
                  print(data)

            elif choice == 5:
                print ("Good bye!")
                return False

        else:
            print("please use a number between 1 and 5.")
	with open('phonebook.json', 'r') as fh:
	  data = json.load(fh)

	while True:
		try:
			choice = int(input("(1-5)>>"))
		except ValueError:
			print("please use a number between 1 and 5.")
			continue


		if 1 <= choice <=5:
			if choice == 1:
				# with open('phonebook.json', 'r') as fh:
				#   data = json.load(fh)
				name=input("Look up name:").lower()
				try:
					print('phone: '+data[name][0]['phone'])
					print('emai: '+data[name][0]['email'])
					print('url: '+data[name][0]['url'])
				except KeyError:
					print("No such entry, please try again")


			elif choice == 2:
				print("New Entry")
				name=input("Name:").lower()
				phone=input("Phone:")
				email=input("Email:")
				url=input("Website:")
				data[name]=[{'phone':phone,'email':email,'url':url}]


				# with open('phonebook.json', 'w') as fh:
				#   json.dump(data, fh)

			elif choice == 3:
				# with open('phonebook.json', 'r') as fh:
				#   data = json.load(fh)
				name=input("Entry to delete:")
				try:
					del data[name]
				except KeyError:
					print("No such entry, please try again!")


			elif choice == 4:
				# with open('phonebook.json', 'r') as fh:
				#   data = json.load(fh)
				  print('\n'*20)
				  for key, value in data.items():
					  print('name: '+key)
					  print('Phone: '+data[key][0]['phone'])
					  print('email: '+data[key][0]['email'])
					  print('url: '+data[key][0]['url'])
					  print('========================')

			elif choice == 5:
				with open('phonebook.json', 'w') as fh:
				  json.dump(data, fh)
				print ("Good bye!")
				return False

		else:
			print("please use a number between 1 and 5.")


menu()
