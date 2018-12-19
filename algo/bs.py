
def linear_search(lst, item): 
    # running time: O(n)
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1

'''Binary search
    -  Take midpoint of array and comp to search key
    -  If search key is equal to midpoint, end
    -  Else
        * search key < midpoint
            - Yes, repeat 1 with sub-array that ends at index pos midpoint - 1
            - No, repeat 1 with sub-array that ends at index pos midpoint + 1
'''        

def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        midpoint = (first+last) // 2

        if lst[midpoint] == item:
            found = True
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    if found:
        return midpoint
    else:
        return -1

'''Finding majority element in a list of length n
    - occurences > n/2
''' 
def maj_elem(lst):
    cnt = {}

    for elem in lst:
        if elem not in cnt:
            # add counter value for an elem
            cnt[elem] = 1
        else:
            # increment counter
            cnt[elem] += 1

    for elem, c in cnt.items():
        # no. of occurences > n/2
        if c > (len(lst) // 2):
            return (elem, c, cnt)
    return (-1, -1, cnt)


lst1 = [1, 2, 3, 3, 3]
print(lst1, '->', maj_elem(lst=lst1)[0])

lst2 = [1, 2, 3, 3]
print(lst2, '->', maj_elem(lst=lst2)[0])

#lst = [1, 5, 6, 12, 13,2,77,56,33,23,43]
#idx = binary_search(lst, 2)
#print(idx)