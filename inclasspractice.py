"""for number in range (1, 20, 2):
    print(number)
number2 = list(range(1,10))
print(number2)
name = []
name = input("Enter your name: ")
index = 0
while name != "" and index < len(name):
    print(name[index])
    index += index
"""
"""
name =input("Enter your name: ")
for char in name:
    print(char)
"""
"""
sentence = input("Enter a sentence: ")
sentence = " " + sentence
for i in range (1, len(sentence)):
    if sentence[i-1]== "" and sentence [i] != "":
        print(sentence[i])
    i+=1
"""
"""
def greeting(name):
    print("blablabla", name)
    return
greeting("Lisa")
print("kimmo")
"""
"""
def greeting(times):
    for i in range (times):
        print("blablabla")

greeting(3)
greeting(7)
"""
"""
def grocery (items):
    print("Here is the shopping lsit: ")
    for i in items:
        print("-" + i)
    return
shopping_list = ["croissants", "banana", "bread"]
grocery(shopping_list)
"""
"""
def calculation (a, b):
    add = a+b
    return add
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
calculation(num1,num2)
add = calculation(num1,num2)
print(f" The calculation result is {add}")
"""
def draw_spruce():

