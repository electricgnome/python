# while True:
#   try:
#     x = int(input("Please enter a number: "))
#     break
#   except ValueError:
#     print("Oops!  That was not a valid number.  Try again...")
# def f(x):
#   return 2 * x + 1
# f(4)
# def g(x):
#   return x + 1
# for x in range(-3, 5):
#   print("f({x})={y} \t g({x})={z}".format(
#           x=x, y=f(x), z=g(x)
#        ))
#
# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# f_output = []
# g_output = []
# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))
# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close() # start a new plot


#Local vs Global vars

# words = ['hello','world!']
# def hello_world():
#     print (words)
#
#
# if __name__=="__main__":
#     hello_world()


students = dict(best='Mittens', worst='Jason')

print(students['best'])
students['best'] = 'Lassie'
print(students['best'])
students['favorite_foods'] = ['pizza', 'chicken']
# print(students['favorite_foods'][1])
del students['favorite_foods']
# print(students['favorite_foods'])

contact = {
  'name': 'Paul',
  'favorite_foods': {
    'fast': 'burgers',
    'italian': 'pizza'
  }
}
print(contact['favorite_foods']['italian'])

print(contact.get('name'))
print(contact['address'])
print(contact.get('address'))
print(contact.get('Address', '<default address>'))
for key, value in students.items():
