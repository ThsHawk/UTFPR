#Autor(es): Thales Alves, Rebecca Paulino
#Data: 19/06/2023

HEADER_ATTRIBUTES = 4
LINE_LENTH = 91
LINE_OFFSET = LINE_LENTH + 2
import sys

def openFile(fileName, op):
    if op == "r" or op == "r+":
        try:
            file = open(fileName, op, encoding='utf-8')
        except FileNotFoundError:
            print("file: \"" + fileName + "\" not found")
            exit()
        else:
            return file
    else:
        return open(fileName, op, encoding='utf-8')
    
def addEmptyCharLine(line):
    for i in range(len(line), LINE_LENTH):
        line = line + " "
    return line + "\n"

def addEmptyCharFile(fileName):
    file = open(fileName, "r+")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
        lines[i] = addEmptyCharLine(lines[i])
    file.seek(0, 0)
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()

def readRrn(fileName, rrn):
    file = open(fileName, "r")
    file.seek(rrn*(LINE_OFFSET), 0)
    line = file.read(LINE_LENTH)
    file.close()
    return line

def storageCompaction(fileName1, fileName2, array):
    file2 = openFile(fileName2, "w")
    file1 = openFile(fileName1, "r")
    file2.write(file1.readline(LINE_LENTH) + "\n")
    file1.close()
    for i in range(len(array)):
        file2.write(readRrn(fileName1, array[i][1]+1) + "\n")
    file2.close()

def genKey(line, tkn):
    print(line.encode())
    line = line.split(tkn)
    key = line[2] + line[3]
    key = key.strip()
    key = key.upper()
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

def sortAux(a):
    return a[0]

def main():
    keyList = genKeyList(sys.argv[1])
    #keyList.sort(key=sortAux)
    #storageCompaction(sys.argv[1], sys.argv[2], keyList)
    del keyList[:]

if len(sys.argv) == 5:
    if sys.argv[2] == "--": #facilitar minha vida
        addEmptyCharFile(sys.argv[1]) #usado somente para formatar os arquivos de entrada (Registros de tamanho fixo)
        exit()
    else:
        main()
else:
    print("invalid argument")
    exit()