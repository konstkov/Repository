import random
print("License plate: Max. speed: Current speed: Distance:")
class Car:
    def __init__(self, plate, max_speed=random.randint(100,200), current_speed=0, distance=0):
        self.plate=plate
        self.max_speed=max_speed
        self.current_speed=current_speed
        self.distance=distance
    def accelerate(self, speed_change):
            self.current_speed+=speed_change
            while self.current_speed >=0 :
                if self.current_speed < self.max_speed:
                    return
                else:
                    self.current_speed = self.max_speed
                    return
    def drive(self, hours):
        self.distance=self.distance + self.current_speed * hours
        return
car_list=[]
for i in range(10):
    car = Car(f"ABC-{i+1}",random.randint(100,200), 0, 0)
    car_list.append(car)
    for n in car_list:
        while car.distance <= 10000:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    print(f"   {car.plate}        {car.max_speed} km/h      {car.current_speed} km/h     {car.distance} km")

