def Fileopen():
    file_to_open = open("child.txt", "r")
    file_to_open = file_to_open.readlines()
    for index in range(len(file_to_open)):
        print file_to_open[index][0:-1] + " -Tutor"
        if file_to_open[index][0:-1] == "Kara" or file_to_open[index][0:-1] == "Harry":
            print file_to_open[index][0:-1] + " -Supervisor"
        
    
    
Fileopen()
