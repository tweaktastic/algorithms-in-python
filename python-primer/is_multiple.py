def is_multiple(n, m):
    return (n % m == 0)


if __name__ == '__main__':
    numbers = input("Please enter 2 numbers \n").split(' ')
    print(is_multiple(int(numbers[0]), int(numbers[1])))
