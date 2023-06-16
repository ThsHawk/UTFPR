from BTree import *
import sys

if __name__ == '__main__':

    if len(sys.argv) == 3:
        try:
            file = open(sys.argv[1], "r")
        except FileNotFoundError:
            print("file \'" + sys.argv[1] + "\' not found")
            exit()

        try:
            degree = int(sys.argv[2])
        except ValueError:
            print("unsuported arguments")
            exit()
        tree = Tree(abs(degree))
        line = ""
        exeption = True
        while exeption:
            line = file.readline().split(",")
            try:
                line[1] = line[1].split()
                if line[0] == "i":
                    tree.insert(key=line[1])
                elif line[0] == "s":
                    tree.search(key=line[1])
                else:
                    print("ih")
            except IndexError:
                exeption = False
        file.close()
        tree.printTree()