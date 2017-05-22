def p_norm(v, p=2):
    result = 0
    for a in v:
        result += a ** p
    result = result ** (1/p)
    return result


if __name__ == '__main__':
    print(p_norm([4,3]))
