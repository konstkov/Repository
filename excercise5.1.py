import random
rolls=[]
n=int(input("How many times do you want to roll the dice?"))
for i in range(n):
    each_roll = random.randint(1, 6)
    rolls.append(each_roll)
total=sum(rolls)
print(f"The sum of all the rolls equals to {total}")

