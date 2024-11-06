#Extend the program by adding an accelerate method
# into the new class. The method should receive the change
# of speed (km/h) as a parameter. If the change is negative,
# the car reduces speed. The method must change the value of
# the speed property of the object. The speed of the car must
# stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased
# by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car.
# Finally, use the emergency brake by forcing
# a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

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

car=Car("ABC-123", 142, 0, 0)


car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(car.current_speed)
car.accelerate(-200)
print(car.current_speed)

