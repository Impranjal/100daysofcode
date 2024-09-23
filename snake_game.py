from turtle import Screen ,Turtle

screen = Screen()
screen.setup(width=500,height=800)
screen.bgcolor("black")

segment_pos = [(0,0),(-20,0),(-40,0)]
segment = []
for s in segment_pos:
    new_seg = Turtle('square')
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(s)
screen.exitonclick()