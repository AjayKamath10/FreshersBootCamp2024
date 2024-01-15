from abc import ABC, abstractmethod

class Car:
    def __init__(self,engineObj, transmissionObj):
        self.engine = engineObj
        self.transmission = transmissionObj
        
    def getDetails(self):
        return [self.engine, self.transmission.get]
        
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
        return self.transmissionName
    
class InterfaceEngine(ABC):
    @abstractmethod
    def setEngine(self, engineName):
        pass

class Engine:
    def __init__(self, FuelPumpObj, StartupMotorObj):
        self.fuelPump = FuelPumpObj
        self.startUpMotor = StartupMotorObj
        
    def setEngine(self, engineName):
        self.engineName = engineName
        
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
        

def main():
    startUpMotor1 = StartUpMotor()
    startUpMotor1.setStartUpMotor("SUP1")
    fuelPump1 = FuelPump()
    fuelPump1.setFuelPump("FP1")
    
    engine1 = Engine(startUpMotor1, fuelPump1)
    engine1.setEngine("E1")
    
    transmission1 = Transmission()
    transmission1.setTransmission("T1")
    
    car1 = Car(engine1, transmission1)
    
    
    
    
