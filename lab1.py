
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    
    if len(int_list) == 0:
        return None
    if int_list == None:
        raise ValueError
    max_value = int_list[0]   
    for i in int_list:
        if max_value < i:
            max_value = i
    return max_value


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    # Base Case
    if len(int_list) == 0:
        return None
    if int_list == None:
        raise ValueError
    # Base Case
    if len(int_list) == 1:
        return int_list
    # Base Case
    elif len(int_list) == 2:
        return [ int_list[1], int_list[0] ]
    else:
        # Interative
        temp = int_list[1:]
        return reverse_rec(temp) + [int_list[0]]



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
