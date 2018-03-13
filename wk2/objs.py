#exercise 1: Person class
class Person:
    def __init__(self,name,email,phone,friends=[],greet_count=0, unique_counts=0, unique={}):

        self.name=name
        self.email=email
        self.phone=phone
        self.friends=friends
        self.greet_count=greet_count
        self.unique=unique
        self.unique_counts=unique_counts

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name,self.name))
        self.greet_count+=1
        if other_person in self.unique:
            self.unique[other_person] += 1
        else:
            self.unique[other_person] = 1
            self.unique_counts+=1

    def print_contact_info(self):
        print (self.name+"'s" + '\nphone: '+ self.phone + '\nemail: '+ self.email)
        # print("testing")

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)



sonny=Person('Sonny', 's@dcc.com', '832-505-6060')
jordan=Person('Jordan','j@dcc.com','832-200-2020')

sonny.greet(jordan)

jordan.greet(sonny)

print ('name: '+ sonny.name + '\nphone: '+ sonny.phone + '\nemail: '+ sonny.email)

print ('name: '+ jordan.name + '\nphone: '+ jordan.phone + '\nemail: '+ jordan.email)


#exercise 2: own class

class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def print_info(self):
        print(self.year +' '+ self.make +' ' + self.model)

leaf=Vehicle('Nissan', 'Leaf', '2015')
