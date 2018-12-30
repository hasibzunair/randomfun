def bst(array, value):
    # returns the index of the element that is searched

    min_idx = 0
    max_idx = len(array)

    while min_idx < max_idx:
        middle_idx = (min_idx + max_idx) // 2

        if array[middle_idx] == value:
            return middle_idx
        elif array[middle_idx] < value:
            min_idx = middle_idx + 1
        else:
            max_idx = middle_idx

    return None

print(bst([4,5,6,7,8], value=0))
print(bst([4,5,6,7,8], value=8))
