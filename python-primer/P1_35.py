def birthday_paradox(n):
    b_list = {}
    same_bdays = 0
    import random
    import datetime
    for n in range(5,101,5):
        b_list = {}
        same_bdays = 0
        for i in range(n):
            year = random.randrange(1900,2015)
            month = random.randrange(1,13)
            day = random.randrange(1,29)
            bday = datetime.datetime(year=year, day=day, month=month)
            if b_list.get(bday, None) is 0:
                b_list[bday] += 1
                same_bdays   += 1
            else:
                b_list[bday]  = 0
        print(same_bdays)
    return True


birthday_paradox(100)
