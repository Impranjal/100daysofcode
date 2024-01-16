def sec(a):
    n = len(a)
    out = []
    sec_lar = -11
    lar = -1
    for i in range(n):
        if lar < a[i]:
            sec_lar = lar
            print(f"sec_lar is {sec_lar}")
            lar = a[i]
            print(f"lar is {lar}")

        if a[i] > sec_lar and a[i] <lar:
            sec_lar = a[i]
    out.append(sec_lar)
    return out

a = [1,9,5,6,7]
print(sec(a))