import NodeTree
class BTree:
    
    __degree = 0
    __root = None
    
    def __init__(self) -> None:
        pass
    
    def search(self, key):
        if self.__root == None:
            return None
        else:
            self.searchNode(self.__root, key)
            
    def searchNode(self, node, key):
        print("")

    
    def insert(self, key):
        if self.__root == None:
            self.__root = NodeTree()
            self.__root.__isLeaf = True
            self.__root.insert(key)
        elif self.__root.__isLeaf == True:
            self.__root.insert(key)
        