from NodeTree import *

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
    
    def search(self, node=None, key=None):
        if node == None: node = self.__root
        if node.isLeaf():
            if key in node.getKeys():
                print("key \'" + str(key) + "\'is in tree")
            else:
                print("key \'" + str(key) + "\'is not in tree")
        else:
            refIndex = self.refSearch(node.getKeys(), key)
            refs = node.getRefs()
            self.search(refs[refIndex], key)
    
    def insert(self, node = None, key = None):
        if node == None: node = self.__root
        if node.isLeaf():
            if key not in node.getKeys() and key != None:
                node.getKeys().append(key)
                node.getKeys().sort()
            else:
                print("key \'" + str(key) + "\'already exists")
        else:
            refIndex = self.refSearch(node.getKeys(), key)
            self.insert(node.getRefs()[refIndex], key)
        if len(node.getKeys()) == self.__degree:
            self.split(node)

    def split(self, node):
        mid = self.__degree // 2
        father = node.getFather()
        leaf = True if node.getRefs() == [] else False
        rightNode = NodeTree(leaf)
        rightNode.getKeys().extend(node.getKeys()[mid+1:])
        rightNode.getRefs().extend(node.getRefs()[mid+1:])
        leftNode = NodeTree(leaf)
        leftNode.getKeys().extend(node.getKeys()[:mid])
        leftNode.getRefs().extend(node.getRefs()[:mid+1])
        if father == None:
            father = NodeTree()
            father.getKeys().append(node.getKeys()[mid])
            father.getRefs().append(leftNode)
            father.getRefs().append(rightNode)
            self.__root = father
        else:
            refIndex = self.refSearch(father.getKeys(), node.getKeys()[mid])
            father.getRefs().pop(refIndex)
            father.getRefs().insert(refIndex, leftNode)
            father.getRefs().insert(refIndex+1, rightNode)
            father.getKeys().append(node.getKeys()[mid])
            father.getKeys().sort()
        rightNode.setFather(father)
        leftNode.setFather(father)

    def printTree(self, node = None, iterator = 0):
        if node == None: node = self.__root
        if node.isLeaf():
            print("leaf[" + str(iterator) + "]: " + str(node.getKeys()))
        else:
            refs = node.getRefs()
            for i in range(len(refs)):
                self.printTree(refs[i], i)
            print("node[" + str(iterator) + "]: " + str(node.getKeys()))
