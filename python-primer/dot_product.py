def dot_product(l1, l2):
    l2 = [i*j for (i,j) in zip(l1,l2)]
    return l2


print(dot_product([1,2],[3,4]))
