# Draw a Koch snowflake
from turtle import *

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            left(t)
    else:
        forward(a)

# Choose colours and size
color("sky blue", "white")
bgcolor("black")
size = 500
order = 6

# Ensure snowflake is centred
penup()
backward(size/1.732)
left(30)
pendown()

# Make it fast
tracer(100)
hideturtle()

begin_fill()

# Three Koch curves
for i in range(3):
    koch(size, order)
    right(120)

end_fill()

# Make the last parts appear
update()