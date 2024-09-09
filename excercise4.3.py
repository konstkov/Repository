numbers = []
while True:
    user_input = input("Please enter a number (or press Enter to stop the program): ")
    if user_input == "":
          break
    number = float(user_input)
    numbers.append(number)
if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")



