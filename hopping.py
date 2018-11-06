def reset_fun(arr_len):
    '''
    return go_to_next function with 
    updated last_index value
    '''
    last_index = arr_len-1
    def go_to_next(idx):
        '''
        this recursive function takes 
        in a current index and recursively
        calls itself to go to next and 
        next-to-next index.
        
        '''
        global count

        if idx > last_index:
            return

        if idx == last_index:
            count += 1
            return

        if idx < last_index:
            go_to_next(idx+1)
            go_to_next(idx+2)

        return 
    return go_to_next 
    
    
    for arr_len in range(3,16):
        count=0 # reset global variable
        go_to_next = reset_fun(arr_len)
        go_to_next(0)
        print("N=", arr_len, "P=", count)
