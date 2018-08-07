#!/usr/bin/env python3

import os 
import dbm.gnu
import sys
import re

file = "cns.fq"

#open (or create) db
db = dbm.gnu.open("cns.db", "c")

print (str(sys.argv))

flag = "no"
nseq = 0
nqual = 0
iteration = 0
name = "fix me"
seq = ''

for i in open(file): 
	if (flag == "seq"): 
		nseq +=1
		if  i =="+\n": #marks end of sequence 
			flag = "qual" #ie quality score
			#print (i)
			#make the fasta
			f = open("cns.fa", 'a')
			f.write(name)
			f.write("\n")
			f.write(seq)
			f.write("\n")
			#make the database
			db[name] = seq
		else: 
			seq = seq + i[:-2] #add this line to seq record
	elif (flag == "qual"):  
		nqual +=1
		if (re.match("@", i) and (nseq -1 == nqual)): 
			flag = "seq" 
			name = i[0:-1]
			#print (i, "CHANGING IT AGAIN")
	elif (flag =="no"): 
		nseq += 1
		if i == "+\n":
			flag = "qual" 
			#print ("CHANGING IT FOLKS")
	iteration +=1

f.close()

print (db[sys.argv[1]])
