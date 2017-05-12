def square_sums(n):
    items = range(1,n)
    sum = 0
    for i in items:
        sum +=i**2
    return sum

print(square_sums(20))
