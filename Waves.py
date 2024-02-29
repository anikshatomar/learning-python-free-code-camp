print("Hello World")
# Drawing a shape
print(" |\     ")
print(" | \    ")
print(" |  \   ")
print(" |___\  ")
# Variable and data type
character_name = "Kajal"
character_age = "22"
is_male = 'false'
print("My name is" + character_name + ",")
print("I am " + character_age + "years old.")

character_name = "Aniksha"
character_age = "21"
print("I really liked my name" + character_name + ",")
print("But didn't like being" + character_age + ".")
# note- "__" is called string , true & false value is known as Boolean value
# Working with strings:-
# if we want to print one quotation: use (\")
print("Turtle\"Academy")
# if we want to change a line : use (\n)
print("Turtle\nAcademy")
# if we want to print simple backslash : use (\)
print("Turtle\Academy")
# if we want to create a string variable & (concatenation) means add more string in it:
phrase = "Turtle Academy"
print(phrase + " is vey excellent")
# convert your phrase or string in upper case and lower case:
phrase = "Turtle Academy"
print(phrase.upper())
print(phrase.lower())
# if we want to check that a string is entirely uppercase or lowercase:
phrase = "Turtle Academy"
print(phrase.isupper())
print(phrase.islower())
# now we try something different to check out these strings :firstly change in upper case and then use to check it is upper or not
phrase = "Turtle Academy"
print(phrase.upper().isupper())
print(phrase.lower().islower())
# we also figure out the length of this string: figure out how many characters were
phrase = "Turtle Academy"
print(len(phrase))
# if we wanted to figure out what the first character in the string or another one :
phrase = "Turtle Academy"
print(phrase[0])
print(phrase[7])
# Index Function: it'll tell us where a specific character or string is located inside of our string
phrase = "Turtle Academy"
print(phrase.index("e"))
# replace :
phrase = "Turtle Academy"
print(phrase.replace("Turtle", "Tortoise"))

# WORKING WITH NUMBERS:
# we can print any number on the screen:
print(8)
print(9.235)
print(-654)
# adding,subtracting,multiplication,division:
print(2 + 4.53)
print(6 - 4)
print(19 * 2)
print(8 / 2)
print(2 + 3 * 5)
print(2 * (3 + 5))
# modulus operation:
# when we have spit out the remainder, by dividing one from another ;
# this sign is known as mod (%)
print(9 % 2)
# we can also store these numbers inside of variables container:
my_num = 25
print(my_num)
# if we want to convert any number into a string :
my_num = 25
print(str(my_num) + " is my lucky number ")
# more operators used in functions:
# abs(it makes number negative to positive but if number is positive then it shows same :
my_num = -2
print(abs(my_num))
# pow(it helps to calculate the power of number):for ex- 9*9*9=729
print(pow(9, 3))
# max & min(it helps to find out the largest & smallest item among all:
print(max(5, 8, 2, 7, 9, 4, 0))
print(min(8, 3, 5, 1, 9, 4, 0))
# round(it used to round a number to a specified number :
print(round(3.5))
print(round(6.4))

from math import *

# floor(this function is used to round down a number to the nearest integer that is less than or equal to the
# original number:
print(floor(4.1))
print(floor(3.6))
# ceil(it is used to round a number up to the nearest integer that is greatest than or equal to the original number:
print(ceil(5.4))
print(ceil(9.5))

# sqrt(it stands for square root):
print(sqrt(81))
print(sqrt(49))

# GETTING  INPUT FROM USERS:
# name = input("Enter your name")
# age = input("Enter your age")
# print("Hello " + name + "! You are " + age )

# BUILDING A BASIC CALCULATOR:
# int(it helps in adding numbers but doesn't help to add decimal number):

# num1 = input("Enter a number: ")
# num2 = input("Enter another number : ")
# result = int(num1) + int(num2)

# print(result)

# float(it also helps in adding numbers and it also helps to add decimal numbers also):
# num1 = input("Enter a number: ")
# num2 = input("Enter another number : ")
# result = float(num1) + float(num2)

# print(result)
# MAD LIBS GAME:
# color = input("Enter your color: ")
# plural_noun = input("Enter a plural noun: ")
# name = input("Enter a name: ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I LOVE YOU " + name)

# LISTS:You can change them after they're created.lists are defined using square brackets '[]'
# make a list of classmates:
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
print(classmates)
# we make this list easy to find out the peoples with the help of numbers:
# if we use negative number , the list starts from the end side:
# if we use colon(:) it provide further names
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
print(classmates[1])
print(classmates[-2])
print(classmates[3:])
print(classmates[1:4])
# LIST FUNCTIONS:
# extend(it helps to add two lists together)
roll_numbers = [5, 3, 43, 6, 2]
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.extend(roll_numbers)
print(classmates)
# append(it is used to add a single element tpo the end of a list):
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.append("manisha")
print(classmates)
# insert(it is used to insert an element at a specified position in a list)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.insert(2, "punit")
print(classmates)
# remove(it helps to remove a specific element from the list or anywhere)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.remove("ankit")
print(classmates)
# clear()(you can use the clear()method to remove all items from a list)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.clear()
print(classmates)
# pop()(it is used to remove and return the last item from a list)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.pop()
print(classmates)
# index()(it is used to find the index of the first occurrence of a specified value in a list)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]

print(classmates.index("ritik"))
# count()(it is used to count the number of occurrences of a specified element in a list)
classmates = ["harsh", "tanu", "harsh", "ritik", "ankit", "harsh", "sanjana"]

print(classmates.count("harsh"))
# sort()(it is used to sort the elements of a list in ascending order)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.sort()
print(classmates)
# reverse()(it is used to reversethe order of elements in a list.)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]
classmates.reverse()
print(classmates)
# copy()(it creates a new object with the same contents as the original object,but any changes made to the copied object won't affect the original one, and vice versa)
classmates = ["tanu", "harsh", "ritik", "ankit", "sanjana"]

classmates2 = classmates.copy()

print(classmates2)

# TUPLES: (means once they're created, you can't change them. You can't add, remove, or change elements).
#Tuples are defined using parentheses ()
coordinates = (3, 7)
print(coordinates[0])