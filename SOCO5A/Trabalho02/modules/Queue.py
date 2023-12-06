# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

from modules.Pages import Pages
from modules.FileAccess import FileAccess
from icecream import ic

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class Queue():
    # ---------------------------
    # main
    # ---------------------------
    def __init__(self):
        self.fifo = []
        self.len = int(input("Lenth of queue: "))
        self.refreshRate = input("Refresh rate: ")
        self.pagefault = 0
        self.pointer = 0

    def access(self, page):
        for i in range(len(self.fifo)):
            if self.fifo[i].getAddress() == page:
                self.fifo[i].setAccess(True)
                return self.fifo[i]
        self.pagefault += 1
        self.pageIn(page)
    
    def pageIn(self, page):
        if len(self.fifo) >= self.len:
            self.pageOut()

        newPage = Pages()
        newPage.setAddress(page)
        self.fifo.insert(self.pointer, newPage)
        self.pointer += 1
        ic(self.fifo)
        ic(self.pagefault)

    def pageOut(self):
        pass

    