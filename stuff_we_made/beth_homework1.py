#!/usr/bin/python3
import sys

myString =input("FEED ME WORDS\n")
myCodons = ["TAG", "TAA", "TGA"]

#convert input to uppercase
if myString.isalpha():
    myString = myString.upper()
else:
    sys.exit([print('ERROR: Input contains non-alpha characters')])

#Check for start codons in sequence    
for x in myCodons[:]:
    if x in myString:
        print(x,' is in ',myString)

#Count occurences of G/C/T/A/other and print
gCount = 0
cCount = 0
tCount = 0
aCount = 0
zCount = 0
for z in myString:
    if z =='G':
        gCount += 1
    elif z == 'T':
        tCount += 1
    elif z == 'C':
        cCount += 1
    elif z == 'A':
        aCount += 1
    else:
        zCount += 1
gPer = (gCount/len(myString))*100
cPer = (cCount/len(myString))*100
tPer = (tCount/len(myString))*100
aPer = (aCount/len(myString))*100
zPer = (zCount/len(myString))*100
print('A = {:3.2f}%\nG = {:3.2f}%\nT = {:3.2f}%\nC = {:3.2f}%\nOther characters = {:3.2f}%\n'.format(aPer,gPer,tPer,cPer,zPer))

#Modify string and return
newString = myString + 'AAA'
print (newString,end='\n')

