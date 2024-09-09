quantity_username=[]
quantity_password=[]
username="python"
password="rules"
while True:
    user_username=input("Enter your username: ")
    user_password=input("Enter your password: ")
    quantity_username.append(user_username)
    quantity_password.append(user_password)
    if user_username==username and user_password==password:
        print("Welcome!")
        break
    elif len(quantity_username)>=5 or len(quantity_password)>=5:
        print("Access denied")
        break
    else:
        print("Please try again ")
