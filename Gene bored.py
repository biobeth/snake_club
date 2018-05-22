def bored_in_gene():
    ans = raw_input("are you bored?:")
    if ans =="Y" or ans == "y" or ans == "Yes" or ans == "YES" or ans == "yes":
        return "good, so am I"
    elif ans == "N" or ans == "n" or ans == "NO" or ans == "No" or ans == "no":
        return "are you even human"
    else:
        print "Invalid choice!"
        bored_in_gene()
