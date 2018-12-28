'''
Find greatest common divisor that divides a/b without remainder
    e.g: 6/9 = 3

    6/3 = 2
    9/3 = 3

'''


def naive_gcd(a, b):
    # time comp O(n)

    gcd = 0
    if a < b:
        n = a
    else:
        n = a
    for d in range(1, n+1):
        if not a % d and not b % d:
            gcd = d
        
    return gcd


def eucl_gcd(a, b):
    '''
    Euclidean Algo
        - computer remainder of the division a/b
        - store reminder as 'a'
        - Compute gcd(a, b)
        - Repeat process in recursive manner until b=0

    ** better time complexity
    '''
    if not b:
        return a
    else:
        return eucl_gcd(b, a % b)


def eucl_gcd_dynamic(a, b):
    '''
    Since Python is "notoriously bad" at recursion,
    this is an implementation of a dynamic version of this algorithm.
    
    **
    (One problem of recursion via Python is the limited stack size,
    and the other one is that tail recursion optimization not implemented.) **    
    '''    
    while b:
       #print(b)
       tmp = b 
       b = a % b 
       a = tmp 
    return a


print('In: 1/1,', 'Out:', naive_gcd(1, 1))
print('In: 1/2,', 'Out:', naive_gcd(1, 2))
print('In: 3/9,', 'Out:', naive_gcd(3, 9))
print('In: 12/24,', 'Out:', naive_gcd(12, 24))
print('In: 12/26,', 'Out:', naive_gcd(12, 26))
print('In: 26/12,', 'Out:', naive_gcd(26, 12))

print('In: 13/17,', 'Out:', eucl_gcd_dynamic(13, 17))