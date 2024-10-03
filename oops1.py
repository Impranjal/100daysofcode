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
        cls.rasie_amt = amount
    #static method - 
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() ==6:
            return False
        return True

emp1= employee("pranjal","singh",4000)
print(emp1.full_name())
import datetime
my_date = datetime.date(2016,7,10)

print(employee.is_workday(my_date))