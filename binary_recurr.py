def binary_recur(arr,low,high,x):
    if low > high :
        return -1
    mid = low + (high-low)//2
    if arr[mid] ==x:
        return mid
    elif arr[mid] > x:
        return binary_recur(arr,low,mid-1,x)
    else:
        return binary_recur(arr,mid+1,high,x)
    
arr = [1,2,3,4,5,6]
x=3
low= 0
high = len(arr) -1
print(binary_recur(arr,low,high,x))