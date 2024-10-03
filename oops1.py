class employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay =pay
        self.email = first + '.' +last +'@company.com'

    def full_name(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*1.04)
            
    @classmethod
    def set_raise_amt(cls,amount):
        pass   

emp1= employee("pranjal","singh",4000)
print(emp1.full_name())