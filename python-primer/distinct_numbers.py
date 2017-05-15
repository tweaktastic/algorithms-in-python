def distinct_number(seq):
    seq_dict = {}
    result = True
    for num in seq:
        try:
            value = seq_dict[num]
            result = False
            break;
        except Exception as e:
            seq_dict[num] = 1
            continue
    return result


if __name__ == '__main__':
    seq = str(input("Enter sequence")).split(' ')
    print(distinct_number(seq))
