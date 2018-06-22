#!/usr/bin/python3
myFile = open("genes.gtf",'r')
myLines = myFile.readlines()

#solution 1: wow this is fucking slow 
#myGenes = []
#for x in myLines:
#    splitLine = x.split()
#    #check splitLine[9] against each value in list (slow and bad)
#    if splitLine[9] not in myGenes:
#        #print(splitLine[9])
#        myGenes.append(splitLine[9])
#print(len(myGenes))    

myGenes = {}
exonCount = 0
totalExonLen = 0
topExon = 0
topGene = ''
#solution 2: less stupid
for x in myLines:
    splitLine = x.split()
    #test if this key exists
    if splitLine[9] not in myGenes:
        myGenes[splitLine[9]] = 0
    if splitLine[2] == "exon":
        exonCount += 1
        totalExonLen += (int(splitLine[4])-int(splitLine[3]))
        myGenes[splitLine[9]] +=1
        if myGenes[splitLine[9]] > topExon:
            topExon = myGenes[splitLine[9]]
            topGene = splitLine[9]
        
print("Total number of genes = ",len(myGenes))
print("Total number of exons = ",exonCount)
print("Average exon length = ",(int(totalExonLen/exonCount)))
print("Gene with most exons is ",topGene," with ",topExon," exons")
