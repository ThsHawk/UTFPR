from NodeTree import *

class Tree:    
    
    def __init__(self, degree):
        self.__degree = degree
        self.__root = NodeTree(True)
    
    def search(self, key):
        if self.__root == None:
            return None
        else:
            self.searchNode(self.__root, key)
            
    def searchNode(self, node, key):
        print("")
    
    def insert(self, key):
        if self.__root.isLeaf():
            self.__root.getKeys().append(key)
        else:
            print("wtf")

    def printTree(self):
        if self.__root.isLeaf():
            print("leaf: " + str(self.__root.getKeys()))
        else:
            for i in range(len(self.__root.getRefs())):
                self.__root.printNode(self.__root.getRefs[i])
            print("node: " + self.__root.getKeys())
