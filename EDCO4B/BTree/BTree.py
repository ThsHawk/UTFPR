class BTree:
    
    
    def __init__(self):
        
        __degree = 0
        __root = None
    
    def search(self, key):
        if this.__root == None:
            return None
        else:
            searchNode(this.__root, key)
            
    def searchNode(self, node, key):
        first = 0
        last = len(node.__keys)-1
        found = False
        while first<=last:
            mid = (first + last)//2
            if array[mid][0] == key :
                return (True, array[mid][1], mid)
            else:
                if key < array[mid][0]:
                    last = mid - 1
                else:
                    first = mid + 1	
        return (False, -1, -1)
    
    def insert(self, key):
        if this.__root == None:
            this.__root = KnotTree()
            this.__root.insert(key)
        else:
            this.__root