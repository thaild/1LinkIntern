from Controller import MasterController

class Index(MasterController):

    def __init__(self):
        self.view = ""
        self.action = ""
        
    def Init(self):
        requestTest = self.setHeader("ciao")
        #requestTest = open("views/Index.html").read()
        #requestTest = "Inside init method"
        return requestTest
    
