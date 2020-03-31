# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:30:27 2020

@author: User1
"""
# Create the car class

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage


class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value


class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__EngineSize = 1

    def getEngineSize(self):
        return self.__EngineSize

    def setEngineSize(self, value):
        self.__EngineSize = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__EngineSize = 1

    def getEngineSize(self):
        return self.__EngineSize

    def setEngineSize(self, value):
        self.__EngineSize = value

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__EngineSize = 1
        self.__numberFuelCells = 1

    def getEngineSize(self):
        return self.__EngineSize

    def setEngineSize(self, value):
        self.__EngineSize = value
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value