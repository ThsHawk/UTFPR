class PrimaryKeyList:

    __dataFileName = None
    __primaryKeyList = list()
    __LINE_OFFSET = 169
    __LINE_LENTH = 168

    def __init__(self) -> None:
        pass
    
    def getRegN(self):
        regN = self.readRrn(self.__dataFileName, 0)
        regN = regN.split(" ")
        regN = regN[0].split("=")
        regN = regN[1]
        return regN

    def getTOP(self):
        top = self.readRrn(self.__dataFileName, 0)
        top = top.split(" ")
        top = top[1].split("=")
        top = top[1]
        return top

    def genKey(self, line, tkn):
        line = line.split(tkn)
        line[0] = line[0].split(" ")
        key = ""
        for j in range(len(line[0])):
            key = key + line[0][j]
        key = key.upper() + line[4]
        return key

    def genKeyList(self):
        regN = int(self.getRegN(self.__dataFileName))
        keyList = []
        for i in range(1, regN + 1):
            tup = (self.genKey(self.readRrn(self.__dataFileName, i), '|'), i-1)
            keyList.append(tup)
        return keyList

    def readRrn(self, rrn):
        file = self.openFile(self.__dataFileName)
        file.seek(rrn*LINE_OFFSET, 0)
        line = file.readline(LINE_LENTH)
        file.close()
        return line

    def readOps(self):
        file = self.openFile(self.__dataFileName)
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            lines[i] = lines[i].split(", ")
            tmp = lines[i][1].split("\n")
            lines[i][1] = tmp[0]
        return lines

    def searchRecord(self, array, key): #peguei da net pq eu tbm sou filho de Deus (mas modifiquei pra ser tupla)
        first = 0
        last = len(array)-1
        found = False
        while( first<=last and not found):
            mid = (first + last)//2
            if array[mid][0] == key :
                return (True, array[mid][1], mid)
            else:
                if key < array[mid][0]:
                    last = mid - 1
                else:
                    first = mid + 1	
        return (False, -1, -1)

    def header(self, regN, top):
        headerLine = "REG.N=" + str(regN) + " TOP=" + str(top)
        headerLine = addEmptyCharLine(headerLine)
        return headerLine

    def delRecord(self, array, key):
        searchResult = self.searchRecord(array, key)
        if searchResult[0]:
            file = self.openFile(self.__dataFileName)
            regN = int(self.getRegN(self.__dataFileName))-1
            top = self.getTOP(self.__dataFileName)
            file.close()
            file = open(self.__dataFileName, "r+")
            file.seek(0, 0)
            file.write(self.header(regN, searchResult[1]))
            file.seek((searchResult[1]+1)*LINE_OFFSET, 0)
            file.write("*" + top + "|")
            file.close()
            array.pop(searchResult[2])
        else:
            print("Record \"" + key + "\" not found")

    def insertRecord(self, array, line):
        searchResult = self.searchRecord(array, self.genKey(line, ","))
        if searchResult[0]:
            print("Record already exists")
        else:
            top = int(self.getTOP(self.__dataFileName))
            regN = int(self.getRegN(self.__dataFileName))
            file = open(self.__dataFileName, "r+")
            if top != -1:
                file.seek((top+1)*LINE_OFFSET, 0)
                newTop = file.readline(LINE_LENTH)
                newTop = newTop.split("|")
                newTop = newTop[0][1:]
                file.seek(0, 0)
                file.write(self.header(regN+1, newTop))
                file.seek((int(top)+1)*LINE_OFFSET, 0)
                tup = (self.genKey(line, ","), top)
            else:
                file.seek(0, 0)
                file.write(self.header(regN+1, top))
                file.seek((regN+1)*LINE_OFFSET)
                tup = (self.genKey(line, ","), regN)
            file.write(self.newRecord(line))
            file.close()
            array.append(tup)
            array.sort()

    def openFile(self):
        try:
            file = open(self.__dataFileName,"r")
        except FileNotFoundError:
            print("file: \"" + self.__dataFileName + "\" not found")
            exit()
        else:
            return file

    def setFile(fileName):
        self.__dataFileName = fileName