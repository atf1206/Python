def longest_palindrome (s):
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0
        
    longest = 1
    slice = ""
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            slice = s[i:j+1]
            if slice == slice[::-1]:
                if (j - i) + 1 > longest:
                    longest = (j - i) + 1
    return longest
