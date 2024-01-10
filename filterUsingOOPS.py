class ConsoleDisplayController:
    __content = '' 
    
    def setContent(self, array):
        self.__content = array
        
    def display(self):
        for item in self.__content:
            print(item)
        
class StartsWithStratedy:
    __startsWith = ''
    
    def setStartsWith(self, key):
        self.__startsWith = key
        
    def invoke(self, item):
        return item[0].lower() == self.__startsWith.lower()

class StringListFilterController:
    __returnArr = []
    def setList(self, strList):
        self.strList = strList
    
    def filter(self):
        
        obj = StartsWithStratedy()
        obj.setStartsWith('a')
        for string in self.strList:
            if obj.invoke(string):
                self.__returnArr.append(string)
        
        
    def getList(self):
        return self.__returnArr


ExampleObject = ConsoleDisplayController()
FilterObject = StringListFilterController()
List1 = ["Car", "Apple", "airplane"]
FilterObject.setList(List1)
FilterObject.filter()
ExampleObject.setContent(FilterObject.getList())
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
    

    
    
