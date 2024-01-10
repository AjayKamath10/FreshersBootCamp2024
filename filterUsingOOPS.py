class printer:
    def __init__(self, item):
        self.item = item
        
    def displayToScreen(self):
        for obj in self.item:
            print(obj.content())
        
class filterList:
    
    def __init__(self, itemList):
        self.resultList = []
        self.itemList = itemList
        
    def predicate(self, param):
        for item in self.itemList:
            if item.check(param):
                self.resultList.append(item)
        return self.resultList 
                
class stringFilter:
    def __init__(self,string):
        self.string = string
        
    def check(self,startChar):
        return self.string[0].lower() == startChar.lower()
        
    def content(self):
        return self.string
                
StringList = ["Carl", "Zeiss", "Ajay", "Air", "Car"]
StringList = [stringFilter(string) for string in StringList]

filterStringObj =  filterList(StringList)
PrintObj = printer(filterStringObj.predicate('a'))

PrintObj.displayToScreen()
        
    

    
    

'''
ALTERNATIVE:
class printer:
    def __init__(self, string):
        self.string = string
        
    def displayToScreen(self):
        print(self.string)
        
class filterList:
    resultList = []
    def __init__(self, stringList):
        self.stringList = stringList
        
    def predicate(self,className, methodName):
        for item in self.filterList:
            obj = className(item)
            if obj.methodName():
                resultList.append(item)
        return self.resultList 
                
class stringFilter:
    def __init__(self,string):
        self.string = string
        
    def checkStartsWith(self,startChar):
        return self.string[0].lower() == startChar.lower()
                
StringList = ["Carl", "Zeiss", "Ajay", "Air", "Car"]
filterStringObj =  filterList(StringList)

PrintObj = printer(filterStringObj.predicate(stringFilter, stringFilter.checkStartsWith('a')))
PrintObj.displayToScreen()
'''
    

    
    
