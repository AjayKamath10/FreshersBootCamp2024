from abc import ABC, abstractmethod

class Car:
    def __init__(self,engineObj, transmissionObj):
        self.engine = engineObj
        self.transmission = transmissionObj
        
    def getDetails(self):
        return "Engine: {}, Transmission: {}".format(self.engine.getEngine(), self.transmission)
        
class InterfaceTransmission(ABC):
    @abstractmethod
    def setTransmission(self,transmissionName):
        pass
    
    @abstractmethod
    def getTransmission(self):
        pass
        
class Transmission(InterfaceTransmission):
    def setTransmission(self,transmissionName):
        self.transmission = transmissionName
    
    def getTransmission(self):
        return self.transmission
    
class InterfaceEngine(ABC):
    @abstractmethod
    def setEngine(self, engineName):
        pass
    
    @abstractmethod
    def getEngine(self):
        pass

class Engine(InterfaceEngine):
    def __init__(self, FuelPumpObj, StartupMotorObj):
        self.fuelPump = FuelPumpObj
        self.startUpMotor = StartupMotorObj
        
    def setEngine(self, engineName):
        self.engineName = engineName
        
    def getEngine(self):
        return self.fuelPump
        
class InterfaceFuelPump(ABC):
    @abstractmethod
    def setFuelPump(self,fuelPumpName):
        pass
    
    @abstractmethod
    def getFuelPump(self):
        pass

class FuelPump(InterfaceFuelPump):
    def setFuelPump(self,fuelPumpName):
        self.fuelPump = fuelPumpName
    
    def getFuelPump(self):
        return self.fuelPump
        
        
class InterfaceStartUpMotor(ABC):
    @abstractmethod
    def setStartUpMotor(self,startUpMotorName):
        pass
    
    @abstractmethod
    def getStartUpMotor(self):
        pass

class StartUpMotor(InterfaceStartUpMotor):
    def setStartUpMotor(self,startUpMotorName):
        self.startUpMotorName = startUpMotorName
    
    def getStartUpMotor(self):
        return self.startUpMotorName
        
class Log:
    def writeLog(self,string):
        print(string)

class DiContainer:
    @staticmethod
    def createEngine():
        return Engine(FuelPump(), StartUpMotor())
        
    @staticmethod
    def createTransmission():
        return Transmission()
        
    @staticmethod
    def createCar():
        Engine1 = DiContainer.createEngine()
        Transmission1 = DiContainer.createTransmission()
        return Car(Engine1, Transmission1)
    
        
def main():
    
    log1 = Log()
    carObj = DiContainer.createCar()
    log1.writeLog(carObj.getDetails())
    
main()
    
