class Car:
    def __init__(self, plate, max_speed, current_speed=0, distance=0):
        self.plate=plate
        self.max_speed=max_speed
        self.current_speed=current_speed
        self.distance=distance
    def accelerate(self, speed_change):
            self.current_speed+=speed_change
            if self.current_speed <= 0:
                self.current_speed=0
                return
            elif self.current_speed < self.max_speed:
                return
            else:
                self.current_speed = self.max_speed
                return
    def drive(self, hours):
        self.distance + self.current_speed * hours
        return

car=Car("ABC-123", 142, 0, 0)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(car.current_speed)
car.accelerate(-200)
print(car.current_speed)


