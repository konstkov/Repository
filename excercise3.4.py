year=int(input("Please write a year"))
if year % 4 == 0:
        print("It's a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("It's a leap year")
else:
        print("It's not a leap year")
