import turtle
screen=turtle.getscreen()
screen.bgcolor('pink')
point=turtle.Turtle()
rainbow=['yellow','blue','red','purple','green','violet','lime','magenta']
point.speed(0)
for i in range(len(rainbow)):
    point.pencolor(rainbow[i])
    point.circle((50+i*5))

    point.pencolor(rainbow[i])
    point.circle(-(50 + i * 5))

point.penup()
point.home()
# point.forward(85)
point.right(90)
# point.forward(42.5)
point.pendown()
for i in range(len(rainbow)):
    point.pencolor(rainbow[i])
    point.circle((50 + i * 5))
point.penup()
point.home()
# point.back(85)
point.right(90)
# point.forward(42.5)
point.pendown()
for i in range(len(rainbow)):
    point.pencolor(rainbow[i])
    point.circle(-(50 + i * 5))
point.hideturtle()
point.pensize(2)
point.pencolor('red')
point.penup()
point.home()
point.goto(0,-170)
point.pendown()
point.circle(170)

turtle.mainloop()