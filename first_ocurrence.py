def first(arr,x):
    low =0
    high = len(arr)-1
    while low <= high:
        mid = low+(high-low)//2
        
        if arr[mid] > x:
            high = mid -1
        elif arr[mid]<x:
            low = mid +1
        else:
            if mid==0 or arr[mid+1] !=arr[mid]:
                return mid
            else:
                low= mid+1
    return -1
    

arr= [1,2,2,2,2,2,3,3]
x=2
print(first(arr,x))