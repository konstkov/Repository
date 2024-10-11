def gas():
    print(f"{gallons} gallons equals approximately {float(gallons * 3.785):.3f} liters.")
    return
while True:
    gallons=int(input("Please provide volume of gasoline in gallons (or enter a negative value to stop the program):"))
    if gallons<0:
        print("Bye Bye!")
        break
    gas()

