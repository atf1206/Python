def number_of_routes(m, n):
    counter = 1
    i = m + n
    while i > 0:
        counter *= i
        i -= 1
    i = m
    while i > 0:
        counter /= i
        i -= 1
    i = n
    while i > 0:
        counter /= i
        i -= 1
    return counter
