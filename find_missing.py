def find_missing(x, y): #Lets define a find_missing function that takes x and y as the arguments.
    length_x = len(x) #this variable stores the lenght of x
    length_y = len(y) #and then this variable stores the lenght of y
    if length_x == length_y: # this loop should return 0 for lists with the same entries
        return 0
    else: #otherwise we make another loop if the entries ain't the same.
        for j in y:
            if j  not in x:
                return j    #should return the missing number for lists with similar entries and a missing number