def squares_sum_odd_sl(n):
    return sum(k**2 if k%2 != 0 else 0 for k in range(1,n))


print(squares_sum_odd_sl(10))
