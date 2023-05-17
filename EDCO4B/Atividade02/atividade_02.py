#Autor(es): Thales Alves, Rebecca Paulino
#Data: 15/05/2023

LINE_OFFSET = 170
LINE_LENTH = 168
import sys

def getRegN(fileName):
    regN = readRrn(fileName, 0)
    regN = regN.split(" ")
    regN = regN[0].split("=")
    regN = regN[1]
    return regN

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
    for i in range(1, regN):
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

def main():
    keyList = genKeyList(sys.argv[1])
    print(keyList)


if len(sys.argv) == 5:
    main()
else:
    print("invalid argument")
    exit()

