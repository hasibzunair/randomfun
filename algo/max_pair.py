import random
import sys
'''
Finding maximum pairwise product in an array of numbers
'''
random.seed(1)

a = [7, 1, 2, 8, 1, 3]
big_list = random.sample(range(0, 10000000), 1000)

def max_pairprod_1(arr):
    '''
    Running time O(n^2)
    '''
    n = len(arr)
    max_prod = -sys.float_info.max

    for i in range(0, n):
        for j in range(i +1, n):
            prod = arr[i] * arr[j]
            if prod > max_prod:
                max_prod = prod
    return max_prod


def max_pairprod_2(arr):
    '''
    Running time O(n)
    '''
    pos_1 = -sys.float_info.max
    pos_2 = -sys.float_info.max
    
    for i in range(0, len(arr)):
        if arr[i] > pos_1:
            tmp = pos_1
            pos_1 = arr[i]
            if tmp > pos_2:
                pos_2 = tmp
        elif arr[i] > pos_2:
            pos_2 = arr[i]

    return pos_1 * pos_2

#print(max_pairprod_1(ary=a))
#print(max_pairprod_1(ary=rnd_lst))

print(max_pairprod_2(arr=a))
print(max_pairprod_2(arr=big_list))