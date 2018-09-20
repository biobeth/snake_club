##An introduction and explanation to variables, objects and types in Python
##An object is what we call any value saved in a programming language, for
##example, if you wanted to store your name "Bob", you can assign the object
##NAME as "Bob" using NAME = "Bob"
##To visualise an object, the simplest method is a function called print()
##Note that the two brackets () mean this is a FUNCTION, and the function
##takes ARGUMENTS within the brackets, for example running the code below
##will print out 'Bob'

NAME = 'Bob'
print(NAME)

##Any thing wrapped in two quote marks e.g. "" or '' is what is called a STRING
##In Python, a string is a TYPE (in other languages they can be known as a
##multitude of names). To check the type of any object, use type()

print(type(NAME))

##Remember, anything wrapped in quote marks is a string, including numbers!

Number = '7'
print(type(Number))

##If a number is not in quote marks, it is an INTEGER

print(type(7))

##If it has a decimal place it is a FLOAT (remember that integers and floats
##are different!!

print(type(7.1))

##We can do anything we like to numbers as well!

print(7*9+4)
