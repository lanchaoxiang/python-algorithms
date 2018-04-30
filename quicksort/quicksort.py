import random
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        bigger = [i for i in arr[1:] if i >pivot]
        return quick_sort(less)+[pivot]+quick_sort(bigger)

list = list(range(10))
random.shuffle(list)
print(list)
print(quick_sort(list))

