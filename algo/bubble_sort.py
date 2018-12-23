def bubble(arr):
    length = len(arr)
    # go over array
    for i in range(length):
        for j in range(1, length):
            # check if next elem less than previous
            if arr[j] < arr[j-1]:
                # swap if true
                arr[j-1], arr[j] = arr[j], arr[j-1]
        
    return arr

x = [5, 4, 3, 6, 1]
print(bubble(x))
