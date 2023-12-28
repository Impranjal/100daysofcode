# def gret(name):
#     print(f"Hi {name} how are you doing")
#     print("How's weather")
# nam = 'pranjal'
# gret(nam)

#fucntion with multiple input

# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is in like {location}")

# greet_with(location='goa',name='aman')

#exercise
# import math
# test_h = int(input())
# test_w = int(input())
# cov = 5 

# def print_calc(test_h,test_w):
#     area = test_h * test_w
#     cans = area/5
    
#     return math.ceil(cans)

# print(print_calc(test_h,test_w))

#Prime number 

def prime_no(num):
    c =0
    if num == 1:
        print("not prime")
    else:
        for i in range(2,num):
            if num %i == 0:
                c +=1
        
        if c == 0:
            print("prime")
        else:
            print("not prime")
        
            
            
num = int(input())
prime_no(num)