# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:22:21 2020

@author: User1
"""
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar

# This method will be used to intialise data for the car rental system

def initialise_data():
    initial_vehicles = {}

# pc = Petrol Car
# dc = Diesel Car
# hc = Hybrid Car
# ec = Electric Car

# Sample data for the petrol cars
    pc1 = PetrolCar("Black", "Audi Saloon", 107550, 1.8)
    pc2 = PetrolCar("Red", "Audi Saloon", 134550, 1.8)
    pc3 = PetrolCar("Blue", "Audi Saloon", 846352, 1.8)
    pc4 = PetrolCar("Grey", "Audi Saloon", 237634, 1.8)
    pc5 = PetrolCar("Black", "BMW M140i", 123462, 3.0)
    pc6 = PetrolCar("White", "BMW M140i", 123725, 3.0)
    pc7 = PetrolCar("Grey", "BMW M140i", 237162, 3.0)
    pc8 = PetrolCar("Black", "Volkswagon Golf", 47000, 1.4)
    pc9 = PetrolCar("Black", "Volkswagon Golf", 32000, 1.4)
    pc10 = PetrolCar("White", "Volkswagon Golf", 52000, 1.4)
    pc11 = PetrolCar("Grey", "Volkswagon Golf", 82000, 1.4)
    pc12 = PetrolCar("Blue", "Volkswagon Golf", 13000, 1.4)
    pc13 = PetrolCar("White", "Skodia Fabia", 60000, 1.2)
    pc14 = PetrolCar("White", "Skodia Fabia", 69000, 1.2)
    pc15 = PetrolCar("Grey", "Skodia Fabia", 17000, 1.2)
    pc16 = PetrolCar("White", "Skodia Fabia", 51000, 1.2)
    pc17 = PetrolCar("White", "Ford Focus", 8000, 1.4)
    pc18 = PetrolCar("Blue", "Ford Focus", 12000, 1.4)
    pc19 = PetrolCar("Red", "Ford Focus", 300, 1.4)
    pc20 = PetrolCar("Red", "Ford Focus", 1900, 1.4)

# Sample data for the diesel cars

    dc1 = DieselCar("Grey", "Citroen C5", 107550, 1.6)
    dc2 = DieselCar("White", "Citroen C5", 9550, 1.6)
    dc3 = DieselCar("Grey", "Skodia Octavia", 8850, 1.6)
    dc4 = DieselCar("Blue", "Skodia Octavia", 82430, 1.6)
    dc5 = DieselCar("Blue", "Hyundai i30", 430, 1.4)
    dc6 = DieselCar("Black", "Hyundai i30", 4720, 1.4)
    dc7 = DieselCar("Red", "Hyundai i30", 24000, 1.4)
    dc8 = DieselCar("White", "Hyundai i30", 51000, 1.4)
    dc9 = DieselCar("Black", "Volkswagon Passat", 32000, 1.9)
    dc10 = DieselCar("Grey", "Volkswagon Passat", 52000, 1.9)

# Sample data for the hybrid cars

    hc1 = HybridCar("Grey", "Toyota Prius", 107550, 1.2, "113 Kw")
    hc2 = HybridCar("Black", "Toyota Prius", 9550, 1.2, "113 Kw")
    hc3 = HybridCar("Red", "Toyota Prius", 8850, 1.2, "113 Kw")
    hc4 = HybridCar("Blue", "Toyota Prius", 82430, 1.2, "113 Kw")
    
# Sample data for the electric cars

    ec1 = ElectricCar("Grey", "Nissan Leaf", 6000, "200 kw")
    ec2 = ElectricCar("Red", "Nissan Leaf", 2000, "200 kw")
    ec3 = ElectricCar("Black", "Nissan Leaf", 12000, "200 kw")
    ec4 = ElectricCar("White", "Nissan Leaf", 7000, "200 kw")
    ec5 = ElectricCar("Blue", "Nissan Leaf", 17000, "200 kw")
    ec6 = ElectricCar("Blue", "Nissan Leaf", 23000, "200 kw")
