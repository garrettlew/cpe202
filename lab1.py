
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
    if int_list == None:
        raise ValueError
    # Base Case list is empty or has 1 element
    if len(int_list) <= 1:
        return int_list
    # Base Case Swap
    elif len(int_list) == 2:
        return [ int_list[1], int_list[0] ]
    else:
    # Recursive Step
        return reverse_rec( int_list[1:] ) + [int_list[0]]



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """

    # Base case
    if int_list == None:
        raise ValueError
    # Base Case where target not found
    if high < low or target not in int_list:
        return None
    # Base Case where target is at the middle index
    mid = high + low // 2

    if int_list[mid] == target:
        return mid

    # Recursive Step
    if target in int_list[low:mid]:    # If target on bottom half of list
        bin_search(target, low, mid-1, int_list)
    else:    # Target on top half of list
        bin_search(target, mid+1, high, int_list)







