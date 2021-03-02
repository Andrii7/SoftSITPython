def multiple(num, length):
    lengthList = []
    for i in range(1,length + 1):
        lengthList.append(i * num)
    return lengthList
print(multiple(7,5))