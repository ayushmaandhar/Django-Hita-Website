# this python program reads Agreement1.txt and creates a new file new.txt where $$$1 is replaced with my name


f = open("sprofile/all_txt/Agreement1.txt", "r")
newf = open("sprofile/all_txt/new.txt", "w")
i = 3
for line in f:
    variable = "$$$" + str(i)
    
    if(variable) not in line:
        newf.write(line)
        print(line)

    elif(variable) in line:
        newline = line.replace(variable, "AYUSH")
        print(newline)
        newf.write(newline)


newf.close()
f.close()       