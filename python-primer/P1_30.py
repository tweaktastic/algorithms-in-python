def divide_times(n):
    if(n < 2):
        return "Enter valid number"
    else:
        k = n
        times = 0
        while k >= 2:
            times += 1
            k = k//2
        return times
