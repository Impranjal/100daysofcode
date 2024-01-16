def mat(arr):
    sp = -1
    max =0
    for i in arr:
        for j in range(len(i)):
            if i[j] ==0:
                sp = j
                print(sp)
                i[j] = 0
        # if sp != -1:
        #     arr[i][sp] =0

    return arr

arr = [[1,1,1],[1,0,1],[1,1,1]]
print(mat(arr))
