from NodeTree import *
from Utils import *

class Tree:    
    
    def __init__(self, degree):
        self.__degree = degree
        self.__root = NodeTree(True)
    
    def getRoot(self):
        return self.__root

    def refSearch(self, array, key):
        first = 0
        last = len(array)-1
        while first <= last:
            mid = (first + last)//2
            if key < array[mid]:
                last = mid - 1
            else:
                first = mid + 1	
        return first
    
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
            if key not in node.getKeys():
                node.getKeys().append(key)
                node.getKeys().sort()
            else:
                print("already exists")
        else:
            refIndex = self.refSearch(node.getKeys(), key)
            self.insert(node.getRefs()[refIndex], key)
        if len(node.getKeys()) == self.__degree:
            self.split(node)

    def split(self, node):
        mid = self.__degree // 2
        father = node.getFather()
        rightNode = NodeTree(True)
        leftNode = NodeTree(True)
        if father == None:
            father = NodeTree()
            father.getKeys().append(node.getKeys()[mid])
            rightNode.getKeys().extend(node.getKeys()[mid+1:])
            leftNode.getKeys().extend(node.getKeys()[:mid])
            father.getRefs().append(leftNode)
            father.getRefs().append(rightNode)
            self.__root = father
            

            

    def printTree(self, node = None):
        if node == None: node = self.__root
        if node.isLeaf():
            print("leaf: " + str(node.getKeys()))
        else:
            refs = node.getRefs()
            for i in range(len(refs)):
                self.printTree(refs[i])
            print("node: " + str(node.getKeys()))
