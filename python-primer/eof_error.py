def eof_error():
    entered_data = []
    while(True):
        try:
            data = input()
            entered_data.append(data)
        except EOFError:
            break;
            
    for i in range(len(entered_data)-1, -1, -1):
        print(entered_data[i])
    return

eof_error()
