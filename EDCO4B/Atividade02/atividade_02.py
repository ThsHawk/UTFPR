#Autor(es): Thales Alves, Rebecca Paulino
#Data: 15/05/2023

import sys

def tmpFile(lines):
    print(lines)

def main():
    try:
        file = open(sys.argv[1],"r")
    except FileNotFoundError:
        print("file: \"" + sys.argv[1] + "\" not found")
    else:
        lines = file.readlines()
        file.close()
        tmpFile(lines)

if len(sys.argv) == 5:
    main()
else:
    print("invalid argument")

