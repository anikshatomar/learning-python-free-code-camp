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
