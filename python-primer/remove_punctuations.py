def remove_punctuations(str):
    return ''.join([str[i] if (ord(str[i]) >=65 or ord(str[i]) == 32)\
            else '' for i in range(len(str)) ])

print(remove_punctuations('Let\'s just check if it removes puncutation marks or not!'))
