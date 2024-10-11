def sum_of_integers(integers):
    return sum(integers)
def main():
    integers = []
    while True:
        user_input = input("Enter a number (or press enter to quit): ")
        if user_input == "":
            break
        integers.append(int(user_input))
    total_sum = sum_of_integers(integers)
    print(f"The sum of the integers is: {total_sum}")
main()
