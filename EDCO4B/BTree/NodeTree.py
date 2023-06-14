class NodeTree:    
    
    def __init__(self, leaf = False):
        self.__father = None
        self.__keys = list()
        self.__refs = list()
        self.__isLeaf = leaf
        self.__count = 0

    def isLeaf(self):
        return(self.__isLeaf)

    def getKeys(self):
        return(self.__keys)

    def getCount(self):
        return(self.__count)

    def getRefs(self):
        return(self.__refs)
    
    def getFather(self):
        return self.__father