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