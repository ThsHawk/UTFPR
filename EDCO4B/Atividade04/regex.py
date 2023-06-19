LINE_OFFSET = 92
LINE_LENTH = LINE_OFFSET - 1
import sys
import re

def openFile(fileName, op):
    if op == "r" or op == "r+":
        try:
            #file = open(fileName, op)
            file = open(fileName, op, encoding='utf-8')
        except FileNotFoundError:
            print("file: \"" + fileName + "\" not found")
            exit()
        else:
            return file
    else:
        return open(fileName, op)
    
if len(sys.argv) == 3:
    file = open(sys.argv[1], "r")
    print(sys.argv[2])
    text = file.read()
    file.close()
    if text == sys.argv[2]: print("ihu")

else:
    print("invalid argument")
    exit()