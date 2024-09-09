import random
random.randint(1,10)
while True:
    guess=input("Try to guess the number between 1 and 10: ")
    value=int(guess)
    if value<random.randint(1,10):
        print("the actual number is lower, try again!")
    elif value < random.randint(1,10):
        print("the actual number is higher, try again!")
    else:
        print("that's correct")
        break
