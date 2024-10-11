#Write a program that asks the user to enter names
# until he/she enters an empty string.
# After each name is read the program either prints out
# New name or Existing name depending on whether the name
# was entered for the first time. Finally, the program lists out
# the input names one by one, one below another in any order.
# Use the set data structure to store the names.
names=set()
while True:
    user_input=input("Please enter a name:")
    if user_input in names:
        print("Existing name")
    elif user_input =='':
        break
    else:
        print("New name")
    names.add(user_input)
for i in names:
    print(i)

