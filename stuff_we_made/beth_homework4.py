#!/usr/bin/python3
import dbm

with dbm.open('seqDB','c') as db:
    with open('cns.fq') as fp:
        myHeader = ''
        mySeq = ''
        myQual = ''
        flag = 0
        for line in fp:
            # 2: lines contain quality scores
            if flag == 2:
                #continue adding lines until the quality score line is the same as the sequence line
                if (len(myQual)+1) < len(mySeq) :
                    myQual += line[:-1]
                    #when finished, store record and reset variables
                else:
                    db[myHeader]=mySeq
                    mySeq = ''
                    myQual = ''
                    flag = 0
                    # 1: lines contain sequence
            elif flag == 1:
                #if line is a separator (single '+'), then subsequent lines will be quality score lines. set flag to 2
                if line == '+\n':
                    flag = 2
                    #else store sequence line
                else:
                    mySeq += line[:-1]
                    #0 : header line. expect next lines to be sequence.
            else:
                myHeader = line[1:-1]
                flag = 1
    print(db.get(b'CLK').decode('utf-8'))
            
