class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.car_weight=2

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def incremental_odometer(self, miles):
        self.odometer_reading += miles

    def weight(self, tons):
        self.car_weight = tons
        print("The weight of the car is update to " + str(tons))


from class3 import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print("\t" + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Importing an Entire Module
import class3
my_beetle = class3.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = class3.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())