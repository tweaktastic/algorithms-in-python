def factors(n):
    k = 1
    temp = []
    while k*k < n:
        if n % k == 0:
            yield k
            temp.append(n//k)
        k += 1
    if k * k == n:
        yield k

    for n in reversed(temp):
        yield n


if __name__ == '__main__':
    a = list(factors(100))
    print(a)
