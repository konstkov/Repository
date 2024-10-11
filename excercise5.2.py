import itertools
numbers = []
for n in itertools.count():
    user_input = input("Please enter a number (or press Enter to stop the program): ")
    if user_input == "":
         break
    number=float(user_input)
    numbers.append(number)
    numbers.sort()
    numbers.reverse()
print(numbers[0:5])









