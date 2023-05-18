#Autor(es): Thales Alves, Rebecca Paulino
#Data: 15/05/2023

LINE_OFFSET = 169
LINE_LENTH = 168
import sys

def addEmptyCharLine(line):
    for j in range(len(line), 168):
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
    line = key.upper() + line[4]
    return line

def genKeyList(fileName):
    regN = int(getRegN(fileName))
    keyList = []
    for i in range(1, regN + 1):
        line = (genKey(readRrn(fileName, i), '|'), i-1)
        keyList.append(line)
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

def delRecord(fileName, array, key):
    searchResult = searchRecord(array, key)
    if searchResult[0]:
        file = openFile(fileName)
        regN = int(getRegN(fileName))-1
        top = getTOP(fileName)
        file.close()
        defRecord = "REG.N=" + str(regN) + " TOP=" + str(searchResult[1])
        defRecord = addEmptyCharLine(defRecord)
        file = open(fileName, "r+")
        file.seek(0, 0)
        file.write(defRecord)
        file.seek((searchResult[1]+1)*LINE_OFFSET, 0)
        file.write("*" + top + "|")
        file.close()
        array.pop(searchResult[2])
    else:
        print("Record not found")

def insertRecord(fileName, array, line):
    searchResult = searchRecord(array, genKey(line, ","))
    if searchResult[0]:
        print("Record already exists")
    else:
        top = int(getTOP(fileName))
        if top != -1:
            file = open(fileName, "r+")
            file.seek((top+1)*LINE_OFFSET, 0)
            string = file.readline()
            string = string.split("|")
            string = string[0][1:]
            newTOP = int(string)
            print(newTOP)
            print(line)



def main():
    keyList = genKeyList(sys.argv[1])
    keyList.sort()
    opsList = readOps(sys.argv[2])
    insertRecord(sys.argv[1], keyList, opsList[0][1])
    #delRecord(sys.argv[1], keyList, "HALO32007")


if len(sys.argv) == 5:
    if sys.argv[2] == "--": #facilitar minha vida
        addEmptyCharFile(sys.argv[1])
        exit()
    else:
        main()
else:
    print("invalid argument")
    exit()

