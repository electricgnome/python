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


menu()
