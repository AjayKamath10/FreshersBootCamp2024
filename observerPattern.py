import time
from abc import ABC, abstractmethod

class Thread():
    def __init__(self):
        self.state = "created"
        self.priority = 10
        self.culture = "defaultCulture"
        self.observerList = []
    
    def __notify(self):
        for observer in self.observerList:
            observer.update(self.getState())
        
    def start(self):
        self.state = "running"
        self.__notify()
        
    def abort(self):
        self.state = "aborted"
        self.__notify()
        
    def sleep(self, sleepInterval):
        self.state = "sleeping"
        time.sleep(sleepInterval)
        self.__notify()
        
    def wait(self):
        self.state = 'waiting'
        self.__notify()
        
    def suspend(self):
        self.state = 'suspended'
        self.__notify()
        
    def setPriority(self, newPriority):
        self.priority = newPriority
        
    def setCulture(self, newCulture):
        self.culture = newCulture
        
    def getState(self):
        return self.state
        
    def subscribe(self, observerObj):
        log = Log()
        self.observerList.append(observerObj)
        log.write("Added a subscriber")
        
    def unsubscribe(self, observerObj):
        log = Log()
        self.observerList.remove(observerObj)
        log.write("Removed a subscriber")
        
        
class IObserver(ABC):
    
    @abstractmethod
    def update(self, stateString):
        pass
        
class DashboardObserver(IObserver):
    
    def update(self,stateString):
        
        log = Log()
        log.write("Dashboard notified about state change: Thread is "+ stateString)
    

class Log():
    def write(self, string):
        print(string)
def main():
    log = Log()
    Thread1 = Thread()

    
    
    Dashboard = DashboardObserver()
    Thread1.subscribe(Dashboard)
    Thread1.start()
    Thread1.abort()
    
    
main()
    
        
