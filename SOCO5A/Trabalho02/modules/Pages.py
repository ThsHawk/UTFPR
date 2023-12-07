# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

class Pages():
    # ---------------------------
    # init
    # ---------------------------
    def __init__(self):
        self.address = 0
        self.payload = ""
        self.access = True
    
    # ---------------------------
    # getters and setters
    # ---------------------------
    def getAddress(self):
        return self.address
    
    def setAddress(self, adr):
        self.address = adr

    def getAccess(self):
        return self.access
    
    def setAccess(self, access):
        self.access = access