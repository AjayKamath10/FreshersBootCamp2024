class ConsoleDisplayController:
    __content = '' 
    
    def setContent(self, message):
        self.__content = message
        
    def display(self):
        print(self.__content)
        
class StartsWithStratedy:
    __startsWith = ''
    
    def setStartsWith(self, key):
        self.__startsWith = key
        
    def invoke(self, item):
        return item[0].lower() == self.__startsWith.lower()

class StringListFilterController:
    
    def filter(self,strList):
        __returnArr = []
        obj = StartsWithStratedy()
        obj.setStartsWith('a')
        for string in strList:
            
            if obj.invoke(string):
                __returnArr.append(string)
        return __returnArr


ExampleObject = ConsoleDisplayController()
FilterObject = StringListFilterController()

for item in FilterObject.filter(["Car", "Apple", "airplane"]):
    ExampleObject.setContent(item)
    ExampleObject.display()

'''ALTERNATIVE : 
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
    

    
    
