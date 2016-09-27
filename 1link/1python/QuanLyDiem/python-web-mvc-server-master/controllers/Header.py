class Head:

    def __init__(self):
        self.startResponse()
        self.initDocument()
        self.head({})
        
    def startResponse(self):
        print("Content-type: text/html\n\n")

    def initDocument(self):
        print("<!DOCTYPE><html>")

    def head(self,params):
        print("<head><title>Python webapp</title></head>")

    def closeDocument(self):
        print("</html>")
