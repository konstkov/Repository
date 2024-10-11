#Write a program that asks the user for a number of a month and
# then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months,
# December being the first month of winter.
user_input=int(input("Enter a number of a month to find out the corresponding season"))
seasons=("Spring","Summer","Autumn","Winter")
if user_input in (12, 1, 2):
    print(f"The season is {seasons[3]}")
elif user_input in (3, 4, 5):
    print(f"The season is {seasons[0]}")
elif user_input in (6, 7, 8):
    print(f"The season is {seasons[1]}")
elif user_input in (9, 10, 11):
    print(f"The season is {seasons[2]}")
else:
    print(f"The month doesn't exist")

