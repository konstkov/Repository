def numbers(list):
    for i in range(2,len(list)+1,2):
        list_even.append(i)
    print(f"And this is what your list would like if we left all the odd numbers out:\n {list_even}")
    return
list = []
list_even=[]
string_len = int(input("Please enter the desired length of your list:"))
while True:
    user_input=int(input("Please enter any positive number:"))
    list.append(user_input)
    if string_len == len(list):
        break
print(f"This is what your original list looks like:\n {list}")
numbers(list)