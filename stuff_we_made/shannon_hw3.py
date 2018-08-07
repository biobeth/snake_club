#!/usr/bin/python3

import math
import os.path


print ("What's the file?")
file = input()
if os.path.isfile(file): 
	print ("What are the atom numbers?")
	print ("first:")
	a1 = input()
	print ("second:")
	a2 = input()
else: 
	print ("there is no file here!")
	quit()


atoms = [a1, a2]
d = {}

#make a dictionary d of atom numbers and coordinates 
#ie d{atom_id: [x_coordinate, y_coord, z_coord]}

with open(file) as f: 
	for line in f: 
		if line[0:4] =='ATOM':
			line = line.split()
			d[line[1]] = line[6:9]


def find_distance(atoms, d): 
	atom1 = list(map(float, d[atoms[0]]))
	atom2 = list(map(float, d[atoms[1]]))
	return math.sqrt((atom1[0] - atom2[0])**2 + (atom1[1] - atom2[1])**2 + (atom1[2] - atom2[2])**2)

def output():
	print ("The distance is...", round(find_distance(atoms, d), 2), '!')

output()
