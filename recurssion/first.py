def rev(lis:list):
    n = len(lis)
    for i in range(0,n):
        k = lis[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i]=k
    return lis

if __name__ == "__main__":
    lis = [1,2,3,4,5]
    print(rev(list)) 