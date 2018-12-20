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



#lst = [1, 5, 6, 12, 13,2,77,56,33,23,43]
#idx = binary_search(lst, 2)
#print(idx)

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


#lst1 = [1, 2, 3, 3, 3]
#print(lst1, '->', maj_elem_dac(lst=lst1)[0])

#lst2 = [1, 2, 3, 3]
#print(lst2, '->', maj_elem_dac(lst=lst2)[0])


'''Finding majority elements with divide and conquer algo
'''

def maj_elem_dac(lst):
    n = len(lst)
    # split list in two sub lists
    left = lst[:n // 2]
    right = lst[n // 2:]

    # run majority elem check on two sub lists
    l_maj = maj_elem(left)
    r_maj = maj_elem(right)
    
    #case 1
    if l_maj[0] == -1 and r_maj[0] == -1:
        return -1
    
    #case 2
    elif l_maj[0] == -1 and r_maj[0] == -1:
        # no. of occurencae in right list
        cnt = r_maj[1]
        if r_maj[0] in l_maj[2]:
            cnt += l_maj[2][r_maj[0]]
        if cnt > n // 2:
            return r_maj[0]

    #case 3 --> same as 2
    elif r_maj[0] == -1 and l_maj[0] > -1:
        cnt = l_maj[1]
        if l_maj[0] in r_maj[2]:
            cnt += r_maj[2][l_maj[0]]
        if cnt > n // 2:
            return l_maj[0]

    #case 4
    else:
        c1, c2 = l_maj[1], r_maj[1]

        if l_maj[0] in r_maj[2]:
            c1 = l_maj[1] + r_maj[2][l_maj[0]]
        if r_maj[0] in l_maj[2]:
            c2 = r_maj[1] + l_maj[2][r_maj[0]]

        m = max(c1, c2)
        if m > n // 2:
            return m
    
    return -1

lst2 = [1, 2, 4, 4, 4, 5]
print(lst2, '->', maj_elem_dac(lst=lst2))

lst3 = [4, 2, 4, 4, 4, 5]
print(lst3, '->', maj_elem_dac(lst=lst3))
print(lst3[::-1], '->', maj_elem_dac(lst=lst3[::-1]))


