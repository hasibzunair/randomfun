'''
Fibonacci F(n) computers as sum of two numbers...
'''
def fibo_rec(n):
    # O(2^n) ->> Terrible!
    if n <= 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_dynamic(n):
    f, f_minus_1 = 0, 1
    for i in range(n):
        f_minus_1, f = f, f + f_minus_1
    return f


print(fibo_rec(3))
print(fibo_rec(10))

print(fibo_dynamic(3))
print(fibo_dynamic(10))

