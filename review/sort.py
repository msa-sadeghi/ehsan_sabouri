# x = [1,17,5,12,19,80]

# def bubble_sort(array):
#     swapped = False
#     # for i in range(len(array)-1, 0, -1):
#     #     for j in range(i):
#     for i in range(len(array)):
#         for j in range(len(array) - i - 1):
#             if array[j] > array [j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#         else:
#             break           
            
#     return array

# print(bubble_sort(x))    

# x = [1,17,5,12,19,80]
# def selection_sort(array):
#     for i in range(len(array) - 1):
#         min_idx = i
#         for idx in range(i+1, len(array)):
#             if array[idx] < array[min_idx]:
#                 min_idx = idx
#         array[i], array[min_idx] = array[min_idx], array[i]
#     return array

# print(selection_sort(x))

# x = [1,17,5,12,19,80]

# def insertion_sort(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         j = i - 1
#         while array[j] > key and j >= 0 :
#             array[j+1] = array[j]
#             j -= 1
#         array[j+1] = key
#     return array

# print(insertion_sort(x))
# import random

# numbers = [random.randint(1,100) for _ in range(100)]
# print(numbers)
# x = 10
# numbers.sort()
# n = 11
# while len(numbers)//2:
#     mid = numbers[len(numbers)//2]
#     if n < mid:
#         numbers = numbers[:len(numbers)//2]
#     elif n>mid:
#         numbers = numbers[len(numbers)//2:]
#     else:
#         print("found")
#         break
    

# import random
# random.seed(12)
# numbers = [random.randint(1,100) for _ in range(10)]
# print(numbers)
# numbers.reverse()
# print(numbers)

# animals = [
#     "Tiger",	"Lion",	"Elephant",
# "Aardvark",	"Antelope",	"Alpine Goat",
# "Bearded Dragon",	"Royal Bengal Tiger",	"Flying Squirrel",
# "Eagle",	"Eel",	"Asiatic" ,"Lion",
# "Beaver",	"Emperor", "Penguin",	"Baboon"
# ]

# def my_function(names):
#     c = 0
#     for n in names:
#         if n[0].lower() == "a":
#             c += 1
#             print(n)
#     return c
# print(my_function(animals))



# def f1():
#     count = 0
#     while True:
#         n = int(input("enter a number:> "))
#         if n <= 0:
#             break
#         count += 1
#     return count
        
# print(f1())
        
        
# def f2(number):
#     return number[::-1]
# print(f2("15"))
# print(f2("sara"))


def is_prime_number(num):
    if num <= 1:
        return False
    res = True
    for x in range(2, num):
        if num % x == 0:
            res = False
            break
    return res

for i in range(100):
    print(f"{i} => {is_prime_number(i)}")
