#!/usr/bin/python3
from math import *

pdbFile = input("Please enter pdb filename:")
atom1 = input("Atom 1:")
atom2 = input("Atom 2:")

myFile=open(pdbFile,'r')
myLines=myFile.readlines()

myAtoms = {}

#function for calculating distance between two atoms
def atomCalc(var1, var2):
    x1 = myAtoms[var1][0]
    x2 = myAtoms[var2][0]
    y1 = myAtoms[var1][1]
    y2 = myAtoms[var2][1]
    z1 = myAtoms[var1][2]
    z2 = myAtoms[var2][2]
    myDistance = sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    print('{:2.2f}'.format(myDistance))

#if line starts with ATOM/HETATM then store as atom numbers with linked co-ordinates 
for line in myLines:
    splitLine = line.split()
    if splitLine[0] == "ATOM" or splitLine[0] == "HETATM":
        myAtoms[splitLine[1]] = [float(splitLine[6]),float(splitLine[7]),float(splitLine[8])]

atomCalc(atom1,atom2)


