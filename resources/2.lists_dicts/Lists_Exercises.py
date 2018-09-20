##This is a list of names, note that lists are defined by [] and can contain
##many types of variables including strings, integers and floats
Names = ['Bob', 'Jeff', 'Matt']
##Slicing is how we refer to taking a subsection of the lists.
print(Names[0:2]) ##Prints the first two entries 
##A list can be altered
Names[1] = 'Dick'
##A list can also be added to (Note that strings themselves are immutable in python)
Names.append('Pope')
##This does not copy the list, but rather instead makes 2 variables point to the same object
B = Names
##Note, the numbering of the list starts at 0
B[2] = 'Blackbird'
##This returns ['Bob', 'Dick','Blackbird', 'Pope'] as we altered B, which points
##to the same place as Names
print(Names)
##Using Len you can also assess how long a list is
len(Names) #4
##If the list contains integers or floats, adding them is easy using sum()
Num = [7,8,9]
print(sum(Num))


##Exercise:

Ex1 = ['Beth', 'John', 'Astra', 'Shannon', 'Tom']
##Q1: Assess the length of the list

##Q2: Replace the second entry in the list with your favourite colour

##Q3: Add a list entry, is the length of the list now divisible by two?

Ex2 = [7, 9, 12, 3]
##Q4: Add the elements of Ex2 together
