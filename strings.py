
string="This is a string of words"
print (string.upper())
print (string.title())
print(string[::-1])

#exercise 4: Leetspeak

l337 = {"A":"4","E":"3","G":"6","I":"1","O":"0","S":"5","T":"7"}

lorem ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam semper purus nec semper suscipit. Ut cursus cursus nisl vel tincidunt. Maecenas cursus placerat purus ac ultrices. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam eget viverra mi. Fusce sodales vel ex eget ullamcorper. Maecenas eget sem ex. Mauris ullamcorper, tortor ornare hendrerit feugiat, enim enim auctor velit, eget gravida lacus nisl vitae quam. Nulla quam diam, maximus interdum tortor et, ornare laoreet mi. Donec ullamcorper, arcu non tempus dignissim, mi enim luctus ipsum, quis tincidunt tortor ante id nunc. Maecenas vehicula ligula ullamcorper, cursus felis sed, imperdiet magna. Vestibulum pulvinar nulla ut neque molestie sodales. Quisque nibh felis, congue et nisl sit amet, varius mollis arcu."

lorem=lorem.upper()

for key, value in l337.items():
    lorem=lorem.replace(key, value)

#exercise 5: long-long vowels

vowels={'ee':'eeeee','oo':'ooooo'}

words = "good cheese stuff"

for key, value in vowels.items():
    words =words.replace(key, value)

#exercise 6: Caesar C
from pycipher import Caesar

code= Caesar(key=13).encipher('you must unlearn what you have learned')
uncode = Caesar(key=13).decipher(code)
#############

# use ord() and chr()
