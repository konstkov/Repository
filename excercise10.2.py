# Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers
# of the bottom and top floors and the number of elevators
# in the building. When a building is created, the building creates
# the required number of elevators. The list of elevators is stored
# as a property of the building. Write a method called run_elevator
# that accepts the number of the elevator and the destination floor
# as its parameters. In the main program, write the statements for
# creating a new building and running the elevators of the building.
import sys
class Elevator:
    def __init__(self, number, floor=0):
        self.floor = floor
        self.number = number
    def floor_up(self):
        self.floor = elevator1.floor + 1
        print(f"The elevator n. {target_elevator} is on the floor n. {self.floor}")
    def floor_down(self):
        self.floor = elevator1.floor - 1
        print(f"The elevator n. {target_elevator} is on the floor n. {self.floor}")
class Building:
    def __init__(self, floors, elevators):
        self.floors = floors
        elevators_list=[]
        for i in range (elevators):
            elevators = Elevator(f"Elevator-{i + 1}", 0)
            elevators_list.append(elevators)
    def run_elevator(self, target_elevator, destination_floor):
        for i in range(destination_floor):
            elevator1.floor_up()
        else:
            for i in range(destination_floor):
                elevator1.floor_down()
        return

def game_over():
    print("Index out of range")
    sys.exit()

floors=int(input("Please enter the desired number of floors in the building"))
elevators=int(input("Please enter the desired number of elevators in the building"))

target_elevator=int(input("Please enter the index number of the elevator you would like to use"))
if target_elevator>elevators:
    game_over()
destination_floor = int(input("Which floor would you like to go to? (Please enter a positive integer.)"))
if destination_floor>floors:
    game_over()

building=Building(floors, elevators)
elevator1=Elevator(target_elevator)
building.run_elevator(target_elevator,destination_floor)












