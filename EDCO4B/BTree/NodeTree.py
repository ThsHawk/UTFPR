import Utils
class NodeTree:    
    
    __keys = list()
    __refs = list()
    __isLeaf = False
    __count = 0  

    def insert(self, key):
        if not Utils.binarySearch(self.__keys, key):
            self.__keys.append(key)
            self.__keys.sort()
            self.__count += 1
        else:
            print("already exists")