# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

from modules.Pages import Pages
from modules.FileAccess import FileAccess

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class Queue():
    # ---------------------------
    # initialize
    # ---------------------------
    def __init__(self):
        self.fifo = []
        self.len = int(input("Lenth of queue: "))
        self.refreshRate = input("Refresh rate: ")
        self.pagefault = 0
        self.pointer = 0
        self.accessCount = 0

    # ---------------------------
    # finalize
    # ---------------------------
    def __del__(self):
        print("Total page fault: " + str(self.pagefault))

    # ---------------------------
    # access page routine
    # ---------------------------
    def access(self, page):
        result = None
        for i in range(len(self.fifo)):
            self.refreshCounter()
            if self.fifo[i].getAddress() == page:
                self.fifo[i].setAccess(True)
                result = self.fifo[i]
                break
        if not result: self.pageIn(page)
        self.printState()
    
    # ---------------------------
    # insert page routine
    # ---------------------------
    def pageIn(self, page):
        self.pagefault += 1
        print("Err: Page fault.")
        if len(self.fifo) >= self.len: self.pageOut()

        newPage = Pages()
        newPage.setAddress(page)
        self.fifo.insert(self.pointer, newPage)
        self.pointer += 1
        if self.pointer == self.len: self.pointer = 0

    # ---------------------------
    # pop page routine
    # ---------------------------
    def pageOut(self):
        while 1:
            state = self.fifo[self.pointer].getAccess()
            if state:
                self.fifo[self.pointer].setAccess(False)
                self.pointer += 1
                if self.pointer == self.len: self.pointer = 0
            else:
                self.fifo.pop(self.pointer)
                break

    # ---------------------------
    # refresh bit routine
    # ---------------------------
    def refreshCounter(self):
        self.accessCount += 1
        if self.accessCount == int(self.refreshRate):
            for i in range(len(self.fifo)):
                self.fifo[i].setAccess(False)
    
    # ---------------------------
    # view page status
    # ---------------------------
    def printState(self):
        stateList = []
        for i in range(len(self.fifo)):
            adr = self.fifo[i].getAddress()
            bit = self.fifo[i].getAccess()
            state = (adr, bit)
            stateList.append(state)
        print(stateList)

    