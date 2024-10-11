integers=[]
integers_even=[]
def function(fun1, fun2):
    while True:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        if number % 2 == 0:
            integers_even.append(number) and integers.append(number)
        elif number % 2 != 0:
            integers.append(number)
        elif user_input == "":
            return
function(integers, integers_even)
print(integers)
print(integers_even)