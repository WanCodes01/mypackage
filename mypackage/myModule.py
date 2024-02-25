def top_n (items, n):
    """ Return the top n items in an array, in desceding order.

    Args:
        items (array): list or array-like object
        n (int): the number of items to return
    Return:
        array: top n items in desceding order
    Egs:
        >>> top_n([7,2, 11, 18, 4, 9], 3)
        [18, 11, 9]
    """
    for i in range(n): # keep sorting until we have the top n items 
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: # if this item is bigger than the next one
                items[j], items[j+1] = items[j+1], items[j] # swap the two numbers 
    
    #get the last two items
    top_n = items[-n:]
    
    #return in desceding order
    return top_n[::-1]