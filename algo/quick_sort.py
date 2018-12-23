
'''
    Quick sort
        - O(n log n)
'''

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller, bigger = [], []
        for elem in arr[1:]:
            if elem <= pivot:
                smaller.append(elem)
            else:
                bigger.append(elem)
        return quicksort(smaller) + [pivot] + quicksort(bigger)


print(quicksort([12, 5, 1, 2]))