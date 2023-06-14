class NodeTree:    
    
    def __init__(self, leaf):
        self.__keys = list()
        self.__refs = list()
        self.__isLeaf = leaf
        self.__count = 0

class Tree:    
    
    def __init__(self, degree):
        self.__degree = degree
        self.__root = None
    
    def search(self, key):
        if self.__root == None:
            return None
        else:
            self.searchNode(self.__root, key)
            
    def searchNode(self, node, key):
        print("")

    
    def insert(self, key):
        if self.__root == None:
            self.__root = NodeTree(True)
            self.__root.__isLeaf = True
            self.__root.insert(key)
        elif self.__root.__isLeaf == True:
            self.__root.insert(key)

    def printTree(self):
        self.printNode(self.__root)

    def printNode(self, node):
        if node.__isLeaf == True:
            print("leaf: " + node.__keys)
        else:
            for i in range(len(node.__refs)):
                node.printNode(node.__refs[i])
            print("leaf: " + node.__keys)
        