def sport():
    print "What sport would you like to know about?"
    print "1: Cricket"
    print "2: Ice Hockey"
    print "3: Rugby"
    print "4: Tennis"
    print "5: Football"
    sport = input("Please choose a number!:")
    if sport == 1:
        print "Cricket is not as good as Ice Hockey but is still pretty cool"
        print "And Knox is much better at it"
    elif sport == 2:
        print "ALL HAIL THE BEST SPORT IN THE WORLD"
        print "PRAISE GRETZKY"
    elif sport == 3:
        print "Meh but 20-8 and 27-23"
    elif sport == 4:
        print "I know literally nothing about Tennis... Federer?"
    elif sport == 5:
        print "George enjoys football quite a bit, but Harry thinks it's overrated"
    else:
        print "Invalid choice!!!!"
        sport()
