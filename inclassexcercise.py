"""
born_year=int(input("Enter your born year: "))
age = 2024 - born_year
if age >=18:
    print("You are welcome!")
if age < 18:
    print("You are not eligible")
if age == 0:
    print("Are you sure you are not an idiot?")
print("thank you")
"""
from itertools import count

"""
born_year=int(input("Enter your born year: "))
age = 2024 - born_year
if age >=18:
    print("You are welcome!")
elif 0 < age < 18:
    print("You are not eligible")
else:
    print("Virhe")
"""
"""
letter=input("Enter a letter: ")
if letter == "a, e, i, o, u":
    print("Letter is a vowel")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes y is a consonant")
else:
    print("Letter is a consonant")
"""
"""
emotion=input("Enter your emotion: ")
happy_count=emotion.count(":-)")
sad_count=emotion.count(":-(")
if happy_count == 0 and sad_count == 0:
    print("none")
elif happy_count == sad_count:
    print("unsure")
elif happy_count > sad_count:
    print("happy")
else:
    print("sad")

i = 1
while i < 11:
    print(i)
    i += 1
  
greeting =int(input("How many times do you want to greet?"))
first_greeting=0
while first_greeting < greeting:
    print("good morning!")
    first_greeting += 1
   """
"""

"""
"""
import random
dice1=dice2=roll_times=0
while(dice1!=3 or dice2!=3):
    dice1=random.randint(1,3)
    dice2=random.randint(1,3)
    roll_times+=1
print(f"The two dices were rolled {roll_times} times.")
"""
"""
command=input("Enter a command: ")
while command != "STOP":
    if command == "BREAK":
        break
    print("The program is running " + command)
    command=input("Enter a command: ")
else:
    print("Goodbye")
print("The program stops now")

"""
"""
num = 10
while num < 100:
    print("Current number is ", num)
    num += 10
    if num == 50:
        continue
    print("Current number: ", num)
"""
""" 
first_num=1
while first_num<=5:
    second_num=1
    while second_num<=5:
        print(f"{first_num}, times {second_num} is {first_num*second_num}")
        second_num += 1
    first_num += 1
 """
"""
import random
number=random.randint(1,100)
number_guess=0
while number_guess != number:
    number_guess = int(input("Enter a number: "))
    if number_guess < number:
        print("Your number is too low")
    elif number_guess > number:
        print("Your number is too high")
    else:
        print("Your number is correct")
  """

while True:
    number=int(input("Enter a number: "))
    if number<=0:
        break
    factorial = 1
    new_num=1
    while new_num<=number:
        factorial*=new_num
        new_num+=1
    print(f"The factorial of {number} is {factorial}")






