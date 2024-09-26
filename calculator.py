"""Module for creating calaculator"""

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def divi(n1,n2):
    return n1/n2

calc_dic = {
    "+": add,
    "-": sub,
    "/": divi,
    "*": multi
}
def perform(num1,num2):
    print("Hi welcome to the pranjal calculator")
    for op in calc_dic:
        print(op)
    operation = input("enter the operation which you want to perform ")
    # num2 = int(input("enter the second number"))
    fn = calc_dic[operation]
    output = fn(num1,num2)
    print(f"{num1}{operation}{num2} is {output}")
    perifrom = input("If you want to perfrom operation type y else type n")
    while perifrom =="y":
        num = int(input("enter the number"))
        perform(output,num)

# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))  
# out = perform(num1,num2)
# print(out)
