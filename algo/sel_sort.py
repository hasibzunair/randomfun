'''
Selection sort
    - sort inplace
    - O(n2)
'''

def selection_sort(arr):

    # iterate over array
    for i in range(len(arr) - 1):
        # set idx to 
        min_ele_idx = i+1
        for j in range(i+2, len(arr)):
            if arr[j] < arr[min_ele_idx]:
                min_ele_idx = j
        if arr[min_ele_idx] < arr[i]:
            # swap
            arr[min_ele_idx], arr[i] = arr[i], arr[min_ele_idx]
                          
    return arr

x = [4, 5, 1, 3]
print(selection_sort(x))