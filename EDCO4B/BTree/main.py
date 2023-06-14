class NodeTree:    
    
    def __init__(self, leaf):
        self.__keys = list()
        self.__refs = list()
        self.__isLeaf = leaf
        self.__count = 0

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
        if self.__root.__isLeaf == True:
            self.__root.__keys.append(key)
        else:
            print("wtf")

    def printTree(self):
        if self.__root.__isLeaf == True:
            print("leaf: " + self.__root.__keys)
        else:
            for i in range(len(self.__root.__refs)):
                self.__root.printNode(self.__root.__refs[i])
            print("node: " + self.__root.__keys)

tree = Tree(3)
tree.printTree()
tree.insert(1)
tree.printTree()
