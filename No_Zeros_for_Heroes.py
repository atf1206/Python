def no_boring_zeros(n):
    if n == 0:
        return n
    
    while True:
        if n % 10 == 0:
            n /= 10
        else:
            return n
