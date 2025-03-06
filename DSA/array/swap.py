arr_pos =[]
arr_n =[]
temp =[]
a=[1, 2, -4, -5]
for i in range(len(a)):
    if a[i] >= 0:
        arr_pos.append(a[i])
    else:
        arr_n.append(a[i])
print(arr_pos)