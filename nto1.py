def func(n):
    if n==0:
        return
    print(n)
    return func(n-1)
 

n =6
print(func(n))