import random
import sys

bet=int(input("Place your bet. Choose the number of the car (between 1 and 10):"))

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
        if winner.plate == f"ABC-{bet}":
            print("Congratulations! You won € 10000000!")
        else:
            print("Sorry, you lost € 10000000!")
        sys.exit()

    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-5, 10))
            car.drive(1)

            if car.distance >= self.distance:
                self.race_finished()

        self.hours += 1
        if self.hours % 10 == 0:
            self.print_status()

    def print_status(self):
        print(f"\nAfter {self.hours} hours of racing:")
        print("License plate | Max speed | Current speed | Distance")
        for car in self.car_list:
            print(f"   {car.plate}       {car.max_speed} km/h       {car.current_speed} km/h      {car.distance} km")

Grand_Demolition_Derby = Race("Grand Demolition Derby", 8000)

for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    Grand_Demolition_Derby.car_list.append(car)

while True:
    Grand_Demolition_Derby.hour_passes()