def add(a, b):
    return a + b
#i'mjust beggining to learn to code

b = 99
a = 3
aPb = add(a, b)

print(a, " + ", b, " = ", aPb)


import math

print(math.pi)
print(math.e)

print(math.sqrt(2.0))

print(math.sin(math.radians(90)))   # sin of 90 degrees

#turtles

import turtle            # allows us to use the turtles library

wn = turtle.Screen()     # creates a graphics window
alex = turtle.Turtle()   # create a turtle named alex

alex.forward(150)        # tell alex to move forward by 150 units
alex.left(90)            # turn by 90 degrees
alex.forward(75)         # complete the second side of a rectangle
wn.exitonclick()
