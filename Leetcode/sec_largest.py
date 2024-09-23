def sec(a):
    n = len(a)
    out = []
    sec_lar = -11
    lar = -1
    sm = 100000
    sec_sm = 99999
    for i in range(n):
        if lar < a[i]:
            sec_lar = lar
            lar = a[i]
        if a[i] > sec_lar and a[i] <lar:
            sec_lar = a[i]
    out.append(sec_lar)
    for i in range(n):
        if sm > a[i]:
            sec_sm = sm
            sm = a[i]
            print(f"sm is {sm}and sec sm is {sec_sm}")
        if sec_sm > a[i] & a[i]>sm:
            sec_sm = a[i]
            print(f"sec sm is {sec_sm}")
    out.append(sec_sm)   
    return out

a = [1,9,5,6,7]
print(sec(a))