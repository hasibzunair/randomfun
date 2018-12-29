'''
Given an integer array and a number 'k', output al pairs that sum up to k.
'''

def all_pairs_sum_k(nums, k):
    # remove dups
    nums_set = set(nums)
    # convert back to list
    nums = list(nums_set)

    res = []

    for num in nums:
        complement = k-num
        #print(complement)
        nums_set.remove(num)
        print(nums_set)

        if complement in nums_set:
            #print(num, complement)
            res.append((num, complement))

    return res

# case 1
nums = [1, 3, 3, 4, 2, 5, 46, 6, 7, 4]
k = 5
#print(all_pairs_sum_k(nums, k))

# case 2
nums = [1, 3, 4, 2]
k = 2
print(all_pairs_sum_k(nums, k))