def odd_one_out(arr):
    res=0
    for i in arr:
       res= res ^i
        
    return res

arr = [1,2,3,2,3,4,4,4,1]
print(odd_one_out(arr))
