cabin_class=input("Enter the cabin class of the cruise ship")
if cabin_class == " LUX":
    print("It's an upper-deck cabin with a balcony.")
elif cabin_class == " A":
    print("above the car deck, equipped with a window.")
elif cabin_class == " B" and " C":
    print("windowless cabin above the car deck.")
else:
    print("Invalid cabin class")