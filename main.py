listText =[]
def write_Name():
    text = input("Enter your name =>")
    for i in range(len(text)):
        listText.append(text[i])
    return listText
print("List =",write_Name())

def write_File():
    inputFile = open("name.txt","w")
    for i in range(len(listText)):
        inputFile.write(str(listText[i]))    
    inputFile.close()
write_File()

def write_Name2():
    inputFile = open("name.txt",'a')
    inputFile.write("\neren")
    inputFile.close()
write_Name2()

def read_File():
    outFile = open("name.txt","r")
    print(outFile.readline())
    outFile.close()
read_File()

def read_File2():
    line =""
    fileName = open("name.txt","r")
    line = fileName.read()
    for line in fileName:
        line += line 
    return line
print(read_File2())

def split_File():
    allName = []
    outFile = open("name.txt","r")
    allLine = outFile.read()
    for i in allLine.split():
        if i != "\n":
            allName.append(i)
    return(allName)
print(split_File())

def ord_Name():
    outFile = open("name.txt","r")
    line = outFile.read()
    sumName = 0
    for i in line:
        if i != "\n":
            sumName = int(sumName) + ord(i)
    return sumName
print("Sum =",ord_Name())

    
    
    
    