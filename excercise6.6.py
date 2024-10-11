import math
def pizza():
    unit_price_1=price_1 / surface_area_1
    unit_price_2= price_2 / surface_area_2
    if unit_price_1>unit_price_2:
        print("The unit price of the second pizza is cheaper")
    elif unit_price_1==unit_price_2:
        print("The unit prices of both pizzas are equal")
    else:
        print("The unit price of the first pizza is cheaper")
    return
diameter_1 = float(input("Please enter the diameter of the first pizza(in cm):"))
diameter_2 = float(input("Please enter the diameter of the second pizza(in cm):"))
price_1 = float(input("Please enter the price of the first pizza(in euros):"))
price_2 = float(input("Please enter the price of the second pizza(in euros):"))
surface_area_1 = (math.pi*(diameter_1)**2)/10000
surface_area_2 = (math.pi*(diameter_2)**2)/10000
pizza()
