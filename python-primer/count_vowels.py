def count_vowels(str):
    vowels = 'aeiou'
    count = 0
    for i in range(len(str)):
        if str[i] in vowels:
            count += 1
    return count


print(count_vowels('count the vowels in this'))
