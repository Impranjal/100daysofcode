import logging as logger
from student_details import *
class Scm:
    def __init__(self):
        print(f"Welcome to the Jaihind College Student Portal")
    def accept_details(self):
        logger.debug("The details of the submitted  to login into the system")
        self.user_name = input('Username of the student\t')
        self.pass_word = input("Password of the student\t")
    def authenticate(self,attempts):
        self.sucess_log = False
        while attempts > 0:
            if self.user_name in student_data:
                if student_data[self.user_name]['pass_word'] == self.pass_word:
                    sucess_log = True
                    print(f"Welcome {student_data[self.user_name]['name']}")
                    exit()
                else:
                    attempts -=1
                    print(f"Your password did not match try again, you have {attempts} left")
                    self.pass_word = input("Retry ! Password of the student\t")
                    
            else:
                print("You entered wrong Username")
                self.accept_details()   
        if self.sucess_log != True:
            print("Sorry we couldn't log you at this moment")
    def display_details(self,sucess_log):
        if self.sucess_log == True:
            for student in 
    def handle_request(self):
        self.accept_details()
        self.authenticate(attempts=3)

if __name__ =="__main__":
    scm = Scm()
    call = scm.handle_request()
    






        

