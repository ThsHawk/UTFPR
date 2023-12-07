# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

from modules.Queue import Queue
from modules.FileAccess import FileAccess
from modules.Pages import Pages

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class Options():
    # ---------------------------
    # initialize
    # ---------------------------
    def __init__(self):
        self.file = FileAccess()
        self.file.openFile()
        self.fifo = Queue()

    # ---------------------------
    # finalize
    # ---------------------------
    def __del__(self):
        self.file.closeFile()
    
    # ---------------------------
    # print menu
    # ---------------------------
    def menu(self):
        print("-- Second Chance Simulator --")
        print("01 - Automatic run")
        print("02 - Paused run")
        print("03 - Exit\n")
        
        opt = input("Select an option (default = 1): ")
        if not opt: opt = "1"
        print("\n")
        
        match opt:
            case "1":
                self.auto()
            case "2":
                self.paused()
            case "3":
                return 0
            case _:
                print("Err: invalid option.")
        return 1
    
    # ---------------------------
    # automatic run option
    # ---------------------------
    def auto(self):
        while 1:
            page = self.file.getChar()
            if page == "": break
            self.fifo.access(int(page))


    # ---------------------------
    # manual run option
    # ---------------------------
    def paused(self):
        while 1:
            page = self.file.getChar()
            if page == "": break
            self.fifo.access(int(page))
            input("Press any to continue..")