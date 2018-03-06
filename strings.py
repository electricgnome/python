
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

msg= "learned"
#alpha = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

alpha = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
alphalist =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k=13


key=1

for key, value in alpha.items():
    msg1= msg.replace(alpha[key], alpha[(key+k) % 25])
