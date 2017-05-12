def sqares_sum_odd(n):
    sum = 0
    numbers = range(1,n)
    for i in numbers:
        sum += i if i%2 != 0 else 0
    print(sum)

sqares_sum_odd(10)
