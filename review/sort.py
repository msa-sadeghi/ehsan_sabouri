x = [1,17,5,12,19,80]

def bubble_sort(array):
    swapped = False
    # for i in range(len(array)-1, 0, -1):
    #     for j in range(i):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break           
            
    return array

print(bubble_sort(x))    