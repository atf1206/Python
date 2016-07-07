def sum_pairs(ints, s):
    i = 1
    best_i, best_j = 0, 0
    my_set = set([])
    
    while i < len(ints) :
        my_set.add(ints[i-1])
        if (s - ints[i]) in my_set:
            return [s - ints[i], ints[i]]

        i += 1
    return None
