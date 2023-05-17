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

def genKeyList(fileName):
    regN = getRegN(fileName)
    for i in range(1, regN):
        line = readRrn(filename, i)
        line = line.split("|")
        line[0] = line[0].split(" ")
        print(line[0])
        str = ""
        for j in range(len(line[0])):
            str = str + line[0][j]
        line = str.upper() + line[4]


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
    genKeyList(sys.argv[1])


if len(sys.argv) == 5:
    main()
else:
    print("invalid argument")
    exit()

