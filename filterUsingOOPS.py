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
        
    

    
    
