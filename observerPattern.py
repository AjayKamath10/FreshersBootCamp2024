import time
class Thread():
    def __init__(self):
        self.state = "created"
        self.priority = 10
        self.culture = "defaultCulture"
    
    def start(self):
        self.state = "running"
        
    def abort(self):
        self.state = "aborted"
        
    def sleep(self, sleepInterval):
        self.state = "sleeping"
        time.sleep(sleepInterval)
        
    def wait(self):
        self.state = 'waiting'
        
    def suspended(self):
        self.state = 'suspended'
        
    def setPriority(self, newPriority):
        self.priority = newPriority
        
    def setCulture(self, newCulture):
        self.culture = newCulture
        
    def getState(self):
        return self.state
        
def main():
    Thread1 = Thread()
    print("Thread state: ", Thread1.getState())
    
    Thread1.wait()
    print("Thread state: ", Thread1.getState())
    
    Thread1.abort()
    print("Thread state: ", Thread1.getState())
    
    Thread1.start()
    print("Thread state: ", Thread1.getState())
    
main()
    
        
