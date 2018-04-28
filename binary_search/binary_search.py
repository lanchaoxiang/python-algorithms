def find(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:

        mid = (low + high) // 2 #mid向下取整
        print(mid)  #展示寻找过程
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

#生成一个1-99 步长为2的列表
mylist = list(range(1, 100, 2))
print('结果：', find(mylist, 3))
