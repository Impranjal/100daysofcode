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

# emp1= employee("pranjal","singh",4000)
# print(emp1.full_name())
# import datetime
# my_date = datetime.date(2016,7,10)

# print(employee.is_workday(my_date))

class Deveolper(employee):
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang =prog_lang
    
class Manager(employee):
    def __init__(self,first,last,pay,employee_list):
        super().__init__(first,last,pay)
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list
    def add_emp(self,emp):
        if emp not in self.employee_list:
            self.employee_list.append(emp)
    def remove_emp(self,emp):
        if emp  in self.employee_list:
            self.employee_list.remove(emp)
    def print_emp(self):
        for emp in self.employee_list:
            print(f'----> {emp}')
        

mang = Manager('akash','hemanth',9000,['raghul'])
mang.add_emp('saad')
print(mang.print_emp())
