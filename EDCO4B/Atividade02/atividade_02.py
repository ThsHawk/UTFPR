#Autor(es): Thales Alves, Rebecca Paulino
#Data: 15/05/2023

LINE_OFFSET = 169
LINE_LENTH = 168
import sys

def addEmptyCharLine(line):
    for i in range(len(line), LINE_LENTH):
        line = line + " "
    return line + "\n"

def addEmptyCharFile(fileName): #usado somente para formatar os arquivos de entrada (Registros de tamanho fixo)
    file = openFile(fileName)
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = lines[i][:len(lines[i])-1]
        lines[i] = addEmptyCharLine(lines[i])
    file = open(fileName, "w")
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()

def getRegN(fileName):
    regN = readRrn(fileName, 0)
    regN = regN.split(" ")
    regN = regN[0].split("=")
    regN = regN[1]
    return regN

def getTOP(fileName):
    top = readRrn(fileName, 0)
    top = top.split(" ")
    top = top[1].split("=")
    top = top[1]
    return top

def genKey(line, tkn):
    line = line.split(tkn)
    line[0] = line[0].split(" ")
    key = ""
    for j in range(len(line[0])):
        key = key + line[0][j]
    key = key.upper() + line[4]
    return key

def genKeyList(fileName):
    regN = int(getRegN(fileName))
    keyList = []
    for i in range(1, regN + 1):
        tup = (genKey(readRrn(fileName, i), '|'), i-1)
        keyList.append(tup)
    return keyList

def readRrn(fileName, rrn):
    file = openFile(fileName)
    file.seek(rrn*LINE_OFFSET, 0)
    line = file.readline(LINE_LENTH)
    file.close()
    return line

def openFile(fileName):
    try:
        file = open(fileName,"r")
    except FileNotFoundError:
        print("file: \"" + fileName + "\" not found")
        exit()
    else:
        return file
    
def readOps(fileName):
    file = openFile(fileName)
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = lines[i].split(", ")
        tmp = lines[i][1].split("\n")
        lines[i][1] = tmp[0]
    return lines

def searchRecord(array, key): #peguei da net pq eu tbm sou filho de Deus (mas modifiquei pra ser tupla)
	first = 0
	last = len(array)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if array[mid][0] == key :
			return (True, array[mid][1], mid)
		else:
			if key < array[mid][0]:
				last = mid - 1
			else:
				first = mid + 1	
	return (False, -1, -1)

def header(regN, top):
    headerLine = "REG.N=" + str(regN) + " TOP=" + str(top)
    headerLine = addEmptyCharLine(headerLine)
    return headerLine

def delRecord(fileName, array, key):
    searchResult = searchRecord(array, key)
    if searchResult[0]:
        file = openFile(fileName)
        regN = int(getRegN(fileName))-1
        top = getTOP(fileName)
        file.close()
        file = open(fileName, "r+")
        file.seek(0, 0)
        file.write(header(regN, searchResult[1]))
        file.seek((searchResult[1]+1)*LINE_OFFSET, 0)
        file.write("*" + top + "|")
        file.close()
        array.pop(searchResult[2])
    else:
        print("Record \"" + key + "\" not found")

def insertRecord(fileName, array, line):
    searchResult = searchRecord(array, genKey(line, ","))
    if searchResult[0]:
        print("Record already exists")
    else:
        top = int(getTOP(fileName))
        regN = int(getRegN(fileName))
        file = open(fileName, "r+")
        if top != -1:
            file.seek((top+1)*LINE_OFFSET, 0)
            newTop = file.readline(LINE_LENTH)
            newTop = newTop.split("|")
            newTop = newTop[0][1:]
            file.seek(0, 0)
            file.write(header(regN+1, newTop))
            file.seek((int(top)+1)*LINE_OFFSET, 0)
            tup = (genKey(line, ","), top)
        else:
            file.seek(0, 0)
            file.write(header(regN+1, top))
            file.seek((regN+1)*LINE_OFFSET)
            tup = (genKey(line, ","), regN)
        file.write(newRecord(line))
        file.close()
        array.append(tup)
        array.sort()

def newRecord(line):
    line = line.split(",")
    newLine = ""
    for i in range(len(line)):
        newLine = newLine + line[i]
        if i == 8:
            newLine = newLine.split("\n")
            newLine = addEmptyCharLine(newLine[0])
            return newLine
        else:
            newLine = newLine + "|"
    print("Record must have 9 fields")
    exit()

def storageCompaction(fileName1, fileName2, array):
    file = open(fileName2, "w")
    regN = getRegN(fileName1)
    file.write(header(regN, -1))
    for i in range(len(array)):
        file.write(readRrn(fileName1, array[i][1]+1) + "\n")
    file.close()
    
def main():
    keyList = genKeyList(sys.argv[1])
    keyList.sort()
    opsList = readOps(sys.argv[2])
    for i in range(len(opsList)):
        if opsList[i][0] == "i":
            insertRecord(sys.argv[1], keyList, opsList[i][1])
        elif opsList[i][0] == "d":
            delRecord(sys.argv[1], keyList, opsList[i][1])
        else:
            print("Invalid option")
    print(keyList)
    storageCompaction(sys.argv[1], sys.argv[3], keyList)

if len(sys.argv) == 5:
    if sys.argv[2] == "--": #facilitar minha vida
        addEmptyCharFile(sys.argv[1])
        exit()
    else:
        main()
else:
    print("invalid argument")
    exit()

