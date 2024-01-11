logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import random
from day13_r import *

def choice():
    A = random.choice(data)
    B = random.choice(data)
    return A ,B
def main():
    your_score = 0
    attempts = 0
    while(attempts < 6):
        A ,B = choice()
        print(f"Compare A : {A['name']},a {A['description']},from {A['country']}")
        print(vs)
        print(f"Compare B : {B['name']},a {B['description']},from {B['country']}")
        choose = input("Who has more followers A or B ?")

