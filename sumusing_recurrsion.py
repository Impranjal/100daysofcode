def sum_using_recursion(n):
    if n <10:
        return n
    return n%10 + sum_using_recursion(n//10)

n =253
print(sum_using_recursion(n))