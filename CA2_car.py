# Copy in Darren's starter code and expand on this code

# Create the car class

# The following ID system will be used to distinguish between the 4 categories of cars on offer:

# pc = Petrol Car
# dc = Diesel Car
# hc = Hybrid Car
# ec = Electric Car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.vehicle_ID = ''
        self.__colour = ''
        self.__model = ''
        self.__mileage = 0

    def __str__(self):
        return "Vehicle_ID: {}\n Colour: {}\n Model: {}\n Milage: {}\n".format(self.vehicle_ID, self.colour, self.model, self.milage)
    
    def get_Vehicle_ID(self):
        return self.vehicle_ID
    
    def getColour(self):
        return self.__colour

    def getModel(self):
        return self.__model

    def getMileage(self):
        return self.__mileage

    def set_Vehicle_ID(self, vehicle_ID):
        self.__vehicle_ID = vehicle_ID
        
    def setColour(self, colour):
        self.__colour = colour

    def setModel(self, model):
        self.__model = model

    def setMileage(self, mileage):
        self.__mileage = mileage


class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumber_Fuel_Cells(self):
        return self.__numberFuelCells

    def setNumber_Fuel_Cells(self, value):
        self.__numberFuelCells = value


class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__EngineSize = 1

    def getEngine_Size(self):
        return self.__EngineSize
    
    def setEngine_Size(self, value):
        self.__EngineSize = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__EngineSize = 1

    def getEngine_Size(self):
        return self.__EngineSize

    def setEngine_Size(self, value):
        self.__EngineSize = value

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__EngineSize = 1
        self.__numberFuelCells = 1

    def getEngine_Size(self):
        return self.__EngineSize

    def setEngine_Size(self, value):
        self.__EngineSize = value
        
    def getNumber_Fuel_Cells(self):
        return self.__numberFuelCells

    def setNumber_Fuel_Cells(self, value):
        self.__numberFuelCells = value

