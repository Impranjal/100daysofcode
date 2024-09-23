from turtle import Turtle ,Screen
import random
tim = Turtle()
sc = Screen()
sc.listen()
def move_forward():
    steps = random.randint(100)
    return steps

tim.listen(move_forward())