def sc(apple):
    i = 0
    while i < len(apple):
        j = 0
        while j < len(apple[i]):
            if apple[i][j] == "B":
                return [i, j]
            j += 1
        i += 1    
    return 0
