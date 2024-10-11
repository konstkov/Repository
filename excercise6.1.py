import random
def roll():
    return random.randint(1, 6)
def main():
    result = 0
    while result != 6:
        result = roll()
        print(result)
main()








