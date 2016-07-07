def short_form(s):
    my_string = s[1:]
    final = s[0]
    for i in range(1,len(s)-1):
        if s[i] not in "aeiouAEIOU":
            final += s[i]
    final += s[-1]
    return final
