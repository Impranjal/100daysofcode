def mergesort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left_half = mergesort(arr[:mid])
    right_half =mergesort(arr[mid:])
    return merge(left_half,right_half)

def merge(left,right):
    i=j=0
    res =[]
    while i < len(left) and j <len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i +=1
        else:
            res.append(right[j])
            j+=1
    while i < len(left):
        res.append(left[i])
        i+=1
    while j <  len(right):
        res.append(right[j])
        j +=1
    return res

arr = [32,24,12,28,2]
print(mergesort(arr))
