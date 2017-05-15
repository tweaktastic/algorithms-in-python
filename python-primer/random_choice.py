import random

def random_choice(seq):
    try:
        return seq[random.randrange(len(seq))]
    except IndexError:
        raise()

if __name__ == '__main__':
    print(random_choice([4,5,6,7,8,10,23,44,55,43,563,23,124,24,32,4543]))
