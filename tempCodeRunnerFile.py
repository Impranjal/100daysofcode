def odd_one_out(arr):
    count_all = []
    for i in arr:
        count_all.append(arr.count(i))
    for i in count_all:
        if i % 2 !=0:
            return i
        
    return -1

arr = [1,2,3,2,3,4,4,4,1]

