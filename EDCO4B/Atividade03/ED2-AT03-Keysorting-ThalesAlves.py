#Autor(es): Thales Alves, Rebecca Paulino
#Data: 08/06/2023

LINE_OFFSET = 131
LINE_LENTH = LINE_OFFSET - 1
import sys

class SortAlgorithms:

    def __init__(self) -> None:
        pass

    def quickSort (self, array, begin, end):
        if begin < end:
            pivo = self.Particion(array, begin, end)
            self.quickSort(array, begin, pivo - 1)
            self.quickSort(array, pivo + 1, end)
        
    def Particion (self, array, begin, end):
        left = begin + 1
        right = end
        pivoValue = array[begin][0]
        while left <= right:
            while(array[left][0] <= pivoValue and (left <= end)):
                left += 1
            while (array[right][0] > pivoValue and (right >= begin)):
                right -= 1
            if left < right:
                array[left], array[right] = array[right], array[left]
        array[right], array[begin] = array[begin], array[right]
        return right

    def maxHeapify(self, array, len, size):
        left = 2*len + 1
        right = 2*len + 2
        max = len
        
        if (left <= (size - 1)) and (array[left][0] > array[len][0]):
            max = left
        if (right <= (size - 1)) and (array[right][0] > array[max][0]):
            max = right
        
        if len != max:
            array[len], array[max] = array[max], array[len]
            self.maxHeapify(array, max, size - 1)
            
    def buildMaxHeap(self, array, size):
        for index in range(size//2 -1, -1, -1):
            self.maxHeapify(array, index, size)
                
    def heapSort(self, array, size):
        self.buildMaxHeap(array, size)
        for index in range(len(array) -1, 0, -1):
            array[0], array[index] = array[index], array[0]
            size = size -1
            self.maxHeapify(array, 0, size)

    def mergeSort(self, v):
        cmp = 0    
        if len(v) > 1:
            vMiddle = len(v) // 2
            leftHalf = v[:vMiddle]
            rightHalf = v[vMiddle:]
            self.mergeSort(leftHalf)
            self.mergeSort(rightHalf)
            #merge
            i=j=k = 0
            while (i < len(leftHalf)) and (j < len(rightHalf)):
                cmp = cmp + 1
                if leftHalf[i][0] < rightHalf[j][0]:
                    v[k] = leftHalf[i]
                    i = i + 1
                else:
                    v[k] = rightHalf[j]
                    j = j + 1
                k = k + 1
            if i == len(leftHalf):
                v[k:] = rightHalf[j:]
            else:
                v[k:] = leftHalf[i:]
        return cmp

    def insertionSort(self, v, vLen):
        cmp = 0
        for i in range(1, vLen):
            aux = v[i]
            j = i - 1
            while (j >= 0) and (aux[0] < v[j][0]):
                cmp = cmp + 1
                v[j+1] = v[j]
                j = j - 1
            v[j+1] = aux
        return cmp

def openFile(fileName, op):
    if op == "r" or op == "r+":
        try:
            file = open(fileName, op)
        except FileNotFoundError:
            print("file: \"" + fileName + "\" not found")
            exit()
        else:
            return file
    else:
        return open(fileName, op)
    
def addEmptyCharLine(line):
    for i in range(len(line), LINE_LENTH):
        line = line + " "
    return line + "\n"

def addEmptyCharFile(fileName):
    file = openFile(fileName, "r")
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = lines[i][:len(lines[i])-1]
        lines[i] = addEmptyCharLine(lines[i])
    file = openFile(fileName, "w")
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()

def readRrn(fileName, rrn):
    file = openFile(fileName, "r")
    file.seek(rrn*LINE_OFFSET, 0)
    line = file.readline(LINE_LENTH)
    file.close()
    return line

def storageCompaction(fileName1, fileName2, array):
    file2 = openFile(fileName2, "w")
    file1 = openFile(fileName1, "r")
    file2.write(file1.readline(LINE_LENTH) + "\n")
    file1.close()
    for i in range(len(array)):
        file2.write(readRrn(fileName1, array[i][1]+1) + "\n")
    file2.close()

def getKey(line, tkn):
    line = line.split(tkn)
    key = line[0]
    del line[:]
    return key

def genKeyList(fileName):
    aux = readHeader(fileName)
    regN = int(aux[2])
    del aux[:]
    keyList = []
    for i in range(1, regN + 1):
        tup = (getKey(readRrn(fileName, i), '|'), i-1)
        keyList.append(tup)
    return keyList

def readHeader(fileName):
    file = openFile(fileName, "r")
    header = file.readline(LINE_LENTH)
    header = header.split(" ")
    headerData = []
    try:
        for i in range(5):
            aux = header[i].split("=")
            headerData.append(aux[1])
        del header[:]
    except IndexError:
        print("invalid file: \'" + fileName + "\'")
        exit()
    del aux[:]
    return headerData

def sortAux(a):
    return a[0]

def sortKeyList(array, method, order):
    sort = SortAlgorithms()
    if method == "Q":
        sort.quickSort(array, 0, len(array)-1)
    elif method == "H":
        sort.heapSort(array, len(array))
    elif method == "M":
        sort.mergeSort(array)
    elif method == "I":
        sort.insertionSort(array, len(array))
    else:
        print("invalid sort \'" + method + "\' method")
        exit()

    if order == "C":
        return array
    elif order == "D":
        array.sort(reverse=True, key=sortAux)
    else:
        print("invalid sort \'" + order + "\' order")
        exit()
    return array

def main():
    keyList = genKeyList(sys.argv[1])
    header = readHeader(sys.argv[1])
    try:
        keyList = sortKeyList(keyList, header[3], header[4])
    except IndexError:
        print("invalid file: \'" + sys.argv[1] + "\'")
    storageCompaction(sys.argv[1], sys.argv[2], keyList)
    del keyList[:]


if len(sys.argv) == 3:
    if sys.argv[2] == "--": #facilitar minha vida
        addEmptyCharFile(sys.argv[1]) #usado somente para formatar os arquivos de entrada (Registros de tamanho fixo)
        exit()
    else:
        main()
else:
    print("invalid argument")
    exit()