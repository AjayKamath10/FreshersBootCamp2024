from abc import ABC, abstractmethod
 
class DocumentPart(ABC):
    _name = ''
    _position = ''
    
    @abstractmethod
    def paint(self):
        pass
 
    @abstractmethod
    def save(self):
        pass
 
class Header(DocumentPart):
    def __init__(self, title =  "DefaultTitle"):
        self.title = title
    def paint(self):
        print("Painting Header titled", self.title)
 
    def save(self):
        print("Saving Header")
 
class Footer(DocumentPart):
    def __init__(self, text =  "DefaultText"):
        self.text = text
        
    def paint(self):
        print("Painting Footer having text", self.text)
 
    def save(self):
        print("Saving Footer")
 
class Hyperlink(DocumentPart):
    def __init__(self,url = "defaultURL.com", text = "defaultText"):
        self.url = url
        self.text = text
    
    def paint(self, ):
        print("Painting Hyperlink having url {} and text {}".format(self.url, self.text))
 
    def save(self):
        print("Saving Hyperlink")
 
class Paragraph(DocumentPart):
    def __init__(self, content = "defaultContent"):
        self.content = content
        
    def paint(self):
        print("Painting Paragraph having content", self.content)
 
    def save(self):
        print("Saving Paragraph")
 
class WordDocument:
    def __init__(self, documentParts=[]):
        self.documentParts = documentParts
        
    def addDocumentPart(self, documentPart):
        self.documentParts.append(documentPart)
 
    def openDocument(self):
        for part in self.documentParts:
            part.paint()
 
    def saveDocument(self):
        for part in self.documentParts:
            part.save()
 
# Example usage
headerObj = Header("Title1")
hyperlinkObj = Hyperlink("google.co.in", "search")
footerObj = Footer()
paragraphObj = Paragraph()

documentPartList = [headerObj, footerObj, hyperlinkObj, paragraphObj] 

wordDoc = WordDocument(documentPartList)
 
wordDoc.openDocument()
print()
wordDoc.saveDocument()
