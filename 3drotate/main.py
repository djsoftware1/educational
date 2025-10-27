# Simple educational example using Python Turtle to show cos/sin for beginners or young learners
# dj2025

# 🐢 Let's use Python Turtle to show how sin() and cos() can move things!
# We'll spin a triangle around its center using some simple math.

import turtle
import math

# 📐 Create a window and turtle
t = turtle.Turtle()
t.speed(0)  # 0 = fastest!
turtle.bgcolor("black")
t.color("cyan")

# 🎨 Define triangle points
triangle = [
    (0, 50),   # Top point
    (-40, -30),# Bottom-left
    (40, -30)  # Bottom-right
]

# 🔁 Draw many frames to show rotation
angle = 0
while angle < 360:
    t.clear()
    t.penup()

    # 🌀 Rotate each point using sin and cos
    rotated = []
    for (x, y) in triangle:
        # Convert angle to radians for math.sin/math.cos
        # (In the degrees system, there are 360 degrees around a circle. The radians system is a differerent way of specifying angles in which there are 2 x pi radians around a circle.)
        rad = math.radians(angle)
        new_x = x * math.cos(rad) - y * math.sin(rad)
        new_y = x * math.sin(rad) + y * math.cos(rad)
        rotated.append((new_x, new_y))

    # 🖊 Draw the rotated triangle
    t.goto(rotated[0])
    t.pendown()
    for point in rotated[1:] + [rotated[0]]:
        t.goto(point)
    t.penup()

    # 🔄 Increase the angle (spin!)
    angle += 5

# 📚 Keep window open
turtle.done()
