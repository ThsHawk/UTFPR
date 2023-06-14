from NodeTree import *
from Utils import *

class Tree:    
    
    def __init__(self, degree):
        self.__degree = degree
        self.__root = NodeTree(True)
    
    def getRoot(self):
        return self.__root

    def search(self, node, key):
        if node.isLeaf():
            if key in node.getKeys():
                print(":)")
            
        else:
            first = 0
            last = len(node.getKeys())-1
            while first < last:
                mid = (first + last)//2
                if key < node.getKeys()[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            refs = node.getRefs()
            self.search(refs[mid])
            
    def searchNode(self, node, key):
        print("")
    
    def insert(self, node, key):
        if node.isLeaf():
            if not(key in node.getKeys()):
                node.getKeys().append(key)
                node.getKeys().sort()
            else:
                print("already exists")
        else:
            refIndex = Utils.binarySearch(node.getKeys(), key)
            self.insert(node.getKeys()[refIndex], key)
        if len(node.getKeys()) == self.__degree:
            self.splitNode(node)

    def split(self, node):
        mid = self.__degree // 2
        father = node.getFather()
        rightNode = NodeTree(True)
        leftNode = NodeTree(True)
        if father == None:
            father = NodeTree()
            father.__keys.append(node.getKeys()[mid])
            

    def printTree(self, node = None):
        if self.__root.isLeaf():
            print("leaf: " + str(self.__root.getKeys()))
        else:
            refs = self.__root.getRefs()
            for i in range(len(refs)):
                self.printTree(refs[i])
            print("node: " + self.__root.getKeys())
