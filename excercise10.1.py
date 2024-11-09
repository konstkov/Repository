class Elevator:
    def __init__(self, floor=0):
        self.floor = floor
    def go_to_floor(self,times):
        for i in range(times):
            elevator1.floor_up()
        else:
            for i in range(times):
                elevator1.floor_down()
        return
    def floor_up(self):
        self.floor = elevator1.floor + 1
        print(f"You are on the floor n. {self.floor}")
    def floor_down(self):
        self.floor = elevator1.floor - 1
        print(f"You are on the floor n. {self.floor}")
user_input=input("Which floor would you like to go to? (Please enter a positive integer.)")
floor_number=int(user_input)
elevator1=Elevator()
elevator1.go_to_floor(floor_number)