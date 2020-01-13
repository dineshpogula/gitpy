import random

x='Dinesh, Pogula'
years =4
age=27

def myFun():
    global y
    y = 'Pogula'
    print('My Name is '+(x+y))

myFun()

power = 2E2 #e or E after this based on count, will add post zeros to the number and e stands for value 10

c = -5j

#Multiline  String using  three double/single quotes

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print(c)
print('My Name is '+y)

print(random.randrange(1,12)) 


#Character of position in a string
print(x[2])

#Slicing
print(x[0:3])
print(x[-7:-1])
print(len(x)) # len() length of string
print(x.strip()) # strip() removy white space.
print(x.lower()) # returns lower case.
print(x.upper()) # returns upper case.
print(x.replace('Dinesh','DAC')) # replace string with another string.
print(x.split(",")) # split() method splits the string into sub string, if it finds #instance of the separator.
check = "Din" in x # check if the phrase "Din" in present in the following text.
notPresent = "zzz" not in x #check if the phrase "zzz" not present in the following text.
print(check)
print(notPresent)
# Combine string and numbers by using format() menthod!
txt ='My age is {0} from Detroit since {1}'
print(txt.format(age,years))
# \ escape character allows you to use double quotes, when you normally would not be allowed.
print('we are the so called \"Wall keepers\" from the nort side')



#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)


#if you have an objects that are made from a class with a __len__ function that returns 0 or False: 
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))

#//  operator

aa= 5
aa <<= 2
print (aa)



