numbers=[]
integer=int(input("Please enter an integer number"))
for number in range(1, integer + 1):
    number /=1
    if integer % number == 0:
        numbers.append(number)
if integer == 1:
    print("This is not a prime number")
elif len(numbers)==2:
    print("This is a prime number")
else:
    print("This is not a prime number")


