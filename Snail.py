def snail(array):
    output_array = []
    left, right, up, down = 0, 0, 0, 0
    height, width = len(array), len(array[0])
    flag = True
    position = 0
    
    while flag == True:
        
        if (left + right) > (width-1) or (up + down) > (height-1):
            flag = False
        
        position = left
        while position < (width - right):
            output_array.append(array[up][position])
            position += 1
        up += 1
    
        if (left + right) > (width-1) or (up + down) > (height-1):
            flag = False
            
        position = up
        while position < (height - down):
            output_array.append(array[position][(width-1)-right])
            position += 1
        right += 1     

        if (left + right) > (width-1) or (up + down) > (height-1):
            flag = False
            
        position = (width-1) - right
        while position >= left:
            output_array.append(array[(height-1) - down][position])
            position -= 1
        down += 1    

        if (left + right) > (width-1) or (up + down) > (height-1):
            flag = False
            
        position = (height-1) - down
        while position > up-1:
            output_array.append(array[position][left])
            print "position = ",
            print position

            position -= 1
        left += 1
    
    return output_array
