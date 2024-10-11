import random
sides=int(input("Enter a number of sides"))
def roll(sides):
    return random.randint(1, sides)
def main():
    result = 0
    while result != sides:
        result = roll(sides)
        print(result)
main()