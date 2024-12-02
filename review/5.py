# import random
# numbers = []

# for i in range(10):
#     x = random.randint(1, 1000)
#     numbers.append(x)
    
# print(numbers)
# print(min(numbers))
# print(max(numbers))

# students = ["sara", "abtin", "maryam", "amirhossein", "mohammadali"]

# def func1(names):
#     count = 0
#     for n in names:
#         if len(n) > 5:
#             count += 1
#     return count
# print(func1(students))
        

# import random
# numbers = []

# for i in range(10):
#     x = random.randint(1, 1000)
#     numbers.append(x)
    
# print(numbers)
# even_numbers = []
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
        
# print(even_numbers)
    
    
# def func2(number):
#     res = True
#     for i in range(2, number):
#         if number % i == 0:
#             res = False
#     return res

# output = []
# for x in range(1, 101):
#     if func2(x) == True:
#         output.append(x)
        
# print(len(output))
    
# list1 = ["a" ,"b", "c"]
# list2 = [1 ,2, 3]
# list3 = list1 + list2
# list1.extend(list2)
# print(list3)
# print(list1)

# mylist = ["abcd" ,"b" ,"ab"]
# print(sorted(mylist, key=lambda x:len(x)))
# print(sorted(mylist))


# try:
#     print()
# except KeyError:
#     print()
    
# else:print("bbb")
# finally:print("dddd")
from colorama import Fore, Back, Style
print(f"{Fore.RED} {Back.GREEN} Hello")
# try:
#     x = int(input("enter a number:> "))
#     print(x)
# except ValueError:
#     print("")
    
# w = open("ff", "r")

# x = [1,2,3,4]
# try:
#     x.index(30)
# except ValueError:
#     print("adasd")


x = {}

key = input("enter a key: ")
value = input("enter a value: ")
try:
    x[key] += value
except KeyError:
    print("Error")
print(x)
