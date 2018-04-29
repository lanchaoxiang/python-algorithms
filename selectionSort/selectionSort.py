import random


# 找出列表中的最小值
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selsort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# 生成一个乱序列表
list = list(range(10))
random.shuffle(list)
print('排序前：', list)
print('排序后：', selsort(list))
