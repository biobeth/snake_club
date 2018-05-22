def on_many_lines(word):
    for char in word:
        print char


def prefixes():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        print letter + suffix
        if prefixes == "O" or "Q":
            print letter + "u" + suffix
prefixes()
            
    
        
