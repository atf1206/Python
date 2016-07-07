import itertools

def permutation_average(n):
    my_array = []
    my_perms = []
    average = 0.0
    
    for i in str(n):
        my_array.append(int(i))
        
    my_perms = list(itertools.permutations(my_array))
    my_array = []
    for i in my_perms:
        my_array.append(make_string(i))
        
    average = 1.0 * sum(my_array) / len(my_array)

    return int(round(average))
   
def make_string(string):
    my_string = ""
    for j in string:
        my_string += str(j)
    return int(my_string)
