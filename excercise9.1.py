# Write a Car class that has the following properties:
# registration number, maximum speed, current speed and
# travelled distance. Add a class initializer that sets
# the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be
# automatically set to zero. Write a main program where
# you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.

class Car:
    def __init__(self, plate, max_speed, current_speed=0, distance=0):
        self.plate=plate
        self.max_speed=max_speed
        self.current_speed=current_speed
        self.distance=distance
car=Car("ABC-123", "142 km/h")
print(car.plate, car.max_speed, car.current_speed, car.distance)





