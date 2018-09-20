def score_summary (NAME,NUMBER1, NUMBER2, NUMBER3):
    print NAME,NUMBER1, NUMBER2, NUMBER3
    print "Max="
    print max(NUMBER1, NUMBER2, NUMBER3)
    print "Min="
    print min(NUMBER1, NUMBER2, NUMBER3)
    print "average="
    print (NUMBER1+NUMBER2+NUMBER3)/3
    
score_summary("BRUCE",22, 3, 9)
