class Utils:

    def __init__(self) -> None:
        pass

    def binarySerch(self, array, key):
        first = 0
        last = len(array)-1
        while first<=last:
            mid = (first + last)//2
            if array[mid] == key :
                return (True)
            else:
                if key < array[mid]:
                    last = mid - 1
                else:
                    first = mid + 1	
        return (False)