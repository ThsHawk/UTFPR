from BTree import *
import sys

if __name__ == '__main__':
    tree = Tree(int(sys.argv[1]))
    for i in range(int(sys.argv[2])):
        tree.insert(key=i)
    tree.printTree()
    tree.search(key=8)