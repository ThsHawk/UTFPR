import sys

def main():
    argvLen = len(sys.argv)
    if argvLen < 2:
        print("ERR: Too few arguments!")
        exit()
    elif argvLen > 2:
        print("ERR: Too many arguments!")
        exit()
    else:
        try:
            file = open(sys.argv[1], "r")
        except FileNotFoundError:
            print("file \'" + sys.argv[1] + "\' not found")
            exit()
            
        lines = file.readlines()
        #lines[0] -- processos
        #lines[1] -- tempo
        #lines[2] -- chegada
        for i in range(len(lines)):
            lines[i] = lines[i][:len(lines[i])-1]
            lines[i] = lines[i].split("\t")
            lines[i].pop(0)
        print(lines)
            
        file.close()

main()