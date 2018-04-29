def count(i):
    print(i)

    if i <= 0:
        return
    else:
        count(i-1)



count(20)