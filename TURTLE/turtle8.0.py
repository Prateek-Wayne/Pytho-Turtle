import turtle
screen=turtle.getscreen()
t= turtle.Turtle()
t.speed(0)
def pattern(n):
    for i in range(n):
        t.forward(75+i*10)
        t.right(90)
        t.forward(75+i*10)
        t.right(90)
        t.forward(75+i*10)
        t.right(90)
        t.forward(75+i*10)
        t.right(90)
def circle(radius,loop):
    for i in range(loop):
        t.circle(radius+i*10)


circle(40,7)
pattern(7)
circle(40,7)
pattern(7)
turtle.mainloop()