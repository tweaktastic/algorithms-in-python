def minmax(data):
    min = max = data[0]
    for i in data:
        if i < min:
            min = data[i]
        elif i > max:
            max = data[i]
    return min, max


print(minmax([1,2,3,4,5,6,7,8,10
        ]))
