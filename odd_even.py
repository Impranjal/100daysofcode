def odd_even(l1:list):
    odd = []
    even = []
    for i in l1:
        if i % 2== 0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even


l1 = [1,3,4,5,6,8,2,7]
print(odd_even(l1))
