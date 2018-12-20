
def binary_search(array, val):
    arr = array
    min_idx = 0
    max_idx = len(array)

    while min_idx < max_idx:
        middle_idx = (min_idx + max_idx) // 2

        if array[middle_idx] == val:
            return middle_idx
        elif array[middle_idx] < val:
            min_idx = middle_idx + 1
        else:
            max_idx = middle_idx

    return None


def recursive_binary_search(array, value, start_idx=None, end_idx=None):
    
    len_ary = len(array)
    
    if start_idx is None:
        start_idx = 0
    if end_idx is None:
        end_idx = len(array) - 1
    
    if not len_ary or start_idx >= end_idx:
        return None
    
    middle_idx = (start_idx + end_idx) // 2
    if array[middle_idx] == value:
        return middle_idx

    elif array[middle_idx] > value:
        return recursive_binary_search(array, 
                                       value, 
                                       start_idx=start_idx,
                                       end_idx=middle_idx)
    else:
        return recursive_binary_search(array,
                                       value,
                                       start_idx=middle_idx + 1,
                                       end_idx=len_ary)
    return None


print(binary_search([1,2,4,7,10,11], val=10))
print(recursive_binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=4))
