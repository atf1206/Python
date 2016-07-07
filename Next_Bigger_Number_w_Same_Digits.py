import itertools

def next_bigger(n):
    my_array = []
    digits_array = []
    new_array = []
    answer = 0
    
    for i in str(n): #array of the digits in n
        my_array.append(int(i))

    i = len(my_array)-1
    
    while i > 0:
        digits_array.insert(0, my_array[i])
        digits_array.sort(reverse = True)
        if my_array[i-1] < digits_array[0]:
            print my_array
            print digits_array
            n = 10
            least_higher_digit = 0
            for d in range(len(digits_array)):
                if digits_array[d] > my_array[i-1] and digits_array[d] < n:
                    n = digits_array[d]
                    least_higher_digit = d
            new_array.append(digits_array[least_higher_digit])
            digits_array[least_higher_digit] = my_array[i-1]
            digits_array.sort()
            for j in digits_array:
                new_array.append(j)
            
            k = i-2
            while k >=0:
                new_array.insert(0, my_array[k])
                k -= 1
            print new_array
            answer = make_string(new_array)
            return answer
        i -= 1
    return -1
    
def make_string(string):
    my_string = ""
    for j in string:
        my_string += str(j)
    return int(my_string)
