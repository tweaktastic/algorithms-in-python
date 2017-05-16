def out_of_bounds(list):
    max_limit = len(list)
    try:
       list[max_limit+5] = 22
    except IndexError:
       print('Don’t try buffer overflow attacks in Python!')
    return


out_of_bounds([1,2])
