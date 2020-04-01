from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar
from csv import writer

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    def create_current_stock(self):
        for i in range(6):
           self.electric_cars.append(ElectricCar())
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(10):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())

    def stock_count(self):
        print('petrol cars in stock ' + str(len(self.petrol_cars)))
        print('electric cars in stock ' + str(len(self.electric_cars)))
        print('diesel cars in stock ' + str(len(self.diesel_cars)))
        print('hybrid cars in stock ' + str(len(self.hybrid_cars)))

    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print('Not enough cars in stock')
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1

    def process_rental(self):
        # Display the welcome message to users
            print('WELCOME TO THE DBS CAR RENTAL SYSTEM')
        # Receive input from customers
            answer = input('Would you like to rent a car? Yes/No')
        if answer == 'Yes':
            answer = input('Enter car type: Petrol/Diesel/Electric/Hybrid')
            answer = int(input('how many would you like?'))
        if answer == 'Petrol':
            self.rent(self.petrol_cars, amount)
        elif answer == 'Diesel':
            self.rent(self.diesel_cars, amount)
        elif answer == 'Electric':
            self.rent(self.electric_cars, amount)
        elif answer == 'Hybrid':
            self.rent(self.hybrid_cars, amount)
        else:
            print('Order not recognised. Please try again.')
            self.stock_count()
  
    def save_cvs(self, new_res):
        csv_file = open(r"C:/Users/Desktop/DBS_Rental.csv", "a+")
           	vehicle_ID= new_res.get_vehicle_ID()
            colour = new_res.get_colour()
            model = new_res.get_model()
            mileage = new_res.get_mileage()
            Engine_Size = new_res.get_engine_size()
            Number_Fuel_Cells = new_res.get_number_fuel_cells()
            reservations_file.write("\n{},{},{},{},{},{},{}".format(vehicle_ID, colour, model, mileage,  engine_size, number_fuel_cells))

dealership = Dealership()
dealership.create_current_stock()
proceed = 'Yes'
while proceed == 'Yes':
    dealership.process_rental()
    proceed = input('Continue? Yes/No')
