#Extend the previously written Car class by adding two subclasses:
# ElectricCar and GasolineCar. Electric cars have the capacity of the battery
# in kilowatt-hours as their property. Gasoline cars have the volume of
# the tank in liters as their property. Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration
# number, maximum speed and battery capacity as its parameter. It calls
# the initializer of the base class to set the first two properties and then
# sets its capacity. Write a main program where you create one electric car
# (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out
# the values of their kilometer counters.

import random
import sys

electric_speed=int(input("Enter the speed of the electric car (ABC-15): (between 1 and 180 km/h):"))
gasoline_speed=int(input("Enter the speed of the gasoline car (ACD-123): (between 1 and 165 km/h):"))


class Car:
    def __init__(self, plate, max_speed, current_speed=0, distance=0):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        self.car_list = []
        self.hours = 0

    def race_finished(self):
        winner = max(self.car_list, key=lambda car: car.distance)
        self.print_status()
        print(f"And the winner is: {winner.plate}!!!!!!!!!!!!!!!!!!!!!!")
        sys.exit()

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-5, 10))
            car.drive(1)


        self.hours += 1
        if self.hours ==3:
            self.race_finished()

    def print_status(self):
        print(f"\nAfter {self.hours} hours of racing:")
        print("License plate | Distance")
        for car in self.car_list:
            print(f"   {car.plate}          {car.distance} km")

class ElectricCar(Car):
    def __init__(self, plate, max_speed, battery, current_speed=0, distance=0):
        super().__init__(plate, max_speed, electric_speed )


class GasolineCar(Car):
    def __init__(self, plate, max_speed, tank, current_speed=0, distance=0):
        super().__init__(plate, max_speed, gasoline_speed)

Grand_Demolition_Derby = Race("Grand Demolition Derby", 8000)


Grand_Demolition_Derby.car_list.append(ElectricCar("ABC-15", 180, "52.5 kWh"))
Grand_Demolition_Derby.car_list.append(GasolineCar("ACD-123", 165, "32.3 l"))



while True:
    Grand_Demolition_Derby.hour_passes()