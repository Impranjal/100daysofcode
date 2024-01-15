def contains_duplicate(arr):
    max = -1
    if len(arr) < 2:
        return [-1]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if max < arr[j]:
                max = arr[j]
                print(max)
        t = arr[i]
        arr[i] = max
        max = -1
    
    return arr

arr =  [17,18,5,4,6,1]
print(contains_duplicate(arr))
