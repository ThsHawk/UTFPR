#Autor(es): Thales Alves, Rebecca Paulino
#Data: 19/06/2023

HEADER_ATTRIBUTES = 4
LINE_LENTH = 91
LINE_OFFSET = LINE_LENTH + 2
import sys

SECND_INDEX = ["ano", "duracao", "titulo", "artista", "genero", "idioma"]

def openFile(fileName, op):
    if op == "r" or op == "r+":
        try:
            file = open(fileName, op)
        except FileNotFoundError:
            print("file: \"" + fileName + "\" not found")
            exit()
        else:
            return file
    else:
        return open(fileName, op)
    
def addEmptyCharLine(line):
    for i in range(len(line), LINE_LENTH):
        line = line + " "
    return line + "\n"

def addEmptyCharFile(fileName):
    file = openFile(fileName, "r+")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
        lines[i] = addEmptyCharLine(lines[i])
    file.seek(0, 0)
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()

def readRrn(fileName, rrn):
    file = openFile(fileName, "r")
    file.seek(rrn*(LINE_OFFSET), 0)
    line = file.read(LINE_LENTH)
    file.close()
    return line

def genKey(line, tkn):
    line = line.split(tkn)
    key = line[2] + line[3]
    key = key.split(" ")
    keyLine = ""
    for i in range(len(key)):
        keyLine = keyLine + key[i]
    key = keyLine.upper()
    return key

def genKeyList(fileName):
    aux = readHeader(fileName)
    regN = int(aux[2])
    del aux[:]
    keyList = []
    for i in range(1, regN + 1):
        tup = (genKey(readRrn(fileName, i), '|'), i-1)
        keyList.append(tup)
    return keyList

def genSecKeyList(fileName, array, index):
    secKeyList = []
    for i in range(len(array)):
        line = readRrn(fileName, array[i][1] + 1)
        line = line.split("|")
        tup = (line[index], array[i][0])
        secKeyList.append(tup)
    return secKeyList

def readHeader(fileName):
    file = openFile(fileName, "r")
    header = file.readline(LINE_LENTH)
    header = header.split(" ")
    headerData = []
    try:
        for i in range(HEADER_ATTRIBUTES):
            aux = header[i].split("=")
            headerData.append(aux[1])
        del header[:]
    except IndexError:
        print("invalid file: \'" + fileName + "\'")
        exit()
    del aux[:]
    return headerData

def searchSecndKey(Array, secKey):
    listIdx = []
    for i in range(len(Array)):
        if Array[i][0] == secKey:
            listIdx.append(i)
    return listIdx

def searchSecndKey(Array, secKey):
    listIdx = []
    for i in range(len(Array)):
        if Array[i][0] == secKey:
            listIdx.append(i)
    return listIdx if listIdx != [] else -1

def sortAux(a):
    return a[0]

def main():
    primaryKeyList = genKeyList(sys.argv[1])
    primaryKeyList.sort(key=sortAux)
    file = openFile(sys.argv[2], 'r')
    lines = file.readlines()
    if len(lines) == 2:
        lines[0] = lines[0].strip()
        lines[1] = lines[1].strip()
    else:
        print("invalid input file: \'" + sys.argv[2] + "\'")
        exit()
    try:
        secIndex = SECND_INDEX.index(lines[0])
    except ValueError:
        print("this script dont handle any field \'" + lines[0] + "\', try one of these instead: " + str(SECND_INDEX))
        exit()
    else:
        secondKeyList = genSecKeyList(sys.argv[1], primaryKeyList, secIndex)
    index = searchSecndKey(secondKeyList, lines[1])
    file = openFile(sys.argv[3], "w")
    if index != -1:
        for i in range(len(index)):
            file.write(readRrn(sys.argv[1], int(primaryKeyList[index[i]][1])+1))
    else:
        file.write("search for \'" + lines[1] + "\' on \'" + lines[0] + "\' in \'" + sys.argv[1] + "\' did not found any record")
    file.close()        

if sys.argv[2] == "--": #usado somente para formatar os arquivos de entrada (Registros de tamanho fixo)
    addEmptyCharFile(sys.argv[1]) 
    exit()
elif len(sys.argv) == 4:
    main()
else:
    print("invalid argument")
    exit()