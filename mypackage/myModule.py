def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    """
    
    # We add the body of the function just below the docstring:
    
    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than the next item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!
                
    # Get last n items
    top_n = items[-n:]
    
    # Return in descending order
    return top_n[::-1]