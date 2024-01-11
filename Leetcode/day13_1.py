def swap(a,b):
    t = a
    a=b
    b=t
    return a,b
def main(a):
    n = len(a)
    l= 0
    while l<n:
        small = min(a)
        # print(small)
        a[l],small=swap(a[l],small)
        
        l+=1
    return a
a = [2,1,3,5]
print(main(a))

    

