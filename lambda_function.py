"""lambda arguments :expression"""

# pow = lambda a,b :a**b
# print(pow(2,3))

# avg = lambda L:sum(L)/len(L)
# list1 = [1,2,3,4]
# print(avg(list1))

my_list=[1,2,3,4]

my_list = map(lambda list1: list1**2,my_list )
print(my_list)