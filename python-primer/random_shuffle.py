import random

def random_shuffle(list):
    shuffled_list = []
    index_track = {}
    for k in range(0, len(list)):
        random_no = random.randrange(0, len(list)-1)
        list[k], list[random_no] = list[random_no], list[k]
    return list

print(random_shuffle([1,2,3,4,5,12,32,43,53,6,7,8]))
