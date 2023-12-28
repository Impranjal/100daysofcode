def second_largest(s):
    l = list()
    for i in s:
        l.append(i)
    maxi = get_max(l)
    for i in l:
        if i == maxi:
            l.remove(i)
    sec = get_max(l)
    return sec
def get_max(k):
    maxi = 0
    for i in range(len(k)):
        if k[i] > maxi:
            k[i] = maxi
    return maxi

s = int(input())
print(second_largest(s))