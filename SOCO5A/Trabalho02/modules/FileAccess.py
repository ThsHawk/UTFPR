# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class FileAccess():
    # ---------------------------
    # main
    # ---------------------------
    def __init__(self):
        self.path = input("Input file path: ")
        self.mode = input("Input file mode: ")
        self.fileDescriptor = self.openFile()
    
    def setPath(self, path):
        self.path = path
    
    def setMode(self, mode):
        self.mode = mode

    def openFile(self):
        try:
            return open(self.path, self.mode)
        except FileNotFoundError:
            print("Err: File \'" + self.path + "\' not found.")
            return -1
    
    def closeFile(self):
        self.fileDescriptor.close()

    def getChar(self):
        char = self.fileDescriptor.read(1)
        return char
