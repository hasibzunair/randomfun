def factorial(x):
    if x <= 1:
        return x
    else:
        return x * factorial(x-1)


def arr_len(x):
    if x == []:
        return 0
    else:
        return 1 + arr_len(x[1:])

def arr_sum(x):
    if x == []:
        return 0
    else:
        return x[0] + arr_sum(x[1:])

def binary_search(array, value, min_idx=0, max_idx=None):
    
    if min_idx == max_idx:
        return None
    elif max_idx is None:
        max_idx = len(array)
    else:
        pass

    middle_idx = min_idx + (max_idx - min_idx) // 2

    if array[middle_idx] == value:
        return middle_idx
    elif array[middle_idx] < value:
        min_idx = middle_idx + 1
    else:
        max_idx = middle_idx
        
    return binary_search(array, value, min_idx, max_idx)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        smaller, bigger = [], []
        for ele in array[1:]:
            if ele <= pivot:
                smaller.append(ele)
            else:
                bigger.append(ele)
        return quicksort(smaller) + [pivot] + quicksort(bigger)


print(factorial(3))
print(arr_len([]))

print(arr_len([1, 2, 3]))
print(arr_sum([1, 2, 3, 4]))

print(binary_search(array=[1, 2, 4, 7, 8, 10, 11], value=99))

print(quicksort([1, 2, 33, 7, 5, 4]))
