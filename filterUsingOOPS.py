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
    obj = StartsWithStratedy()
    obj.setStartsWith('a')
    def setList(self, strList):
        self.strList = strList
    
    def filter(self):
        for string in self.strList:
            if self.obj.invoke(string):
                self.__returnArr.append(string)
        
        
    def getList(self):
        return self.__returnArr

def main():
    ExampleObject = ConsoleDisplayController()
    FilterObject = StringListFilterController()
    List1 = ["Car", "Apple", "airplane"]
    FilterObject.setList(List1)
    FilterObject.filter()
    ExampleObject.setContent(FilterObject.getList())
    ExampleObject.display()
    
main()
