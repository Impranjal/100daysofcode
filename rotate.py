
arr = [1,2,3,4,5]
k = int(input("enter the k"))
n = len(arr)

for i in range(n):
    t= arr[i]
    arr[i]=arr[(n-k+i)%n]
    print(arr)
        

