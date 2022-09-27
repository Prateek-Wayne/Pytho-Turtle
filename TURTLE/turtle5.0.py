import turtle
screen=turtle.getscreen()
point=turtle.Turtle()
# point.pen(pensize=5,pencolor='lime',fillcolor='red')
# point.begin_fill()
#
# point.circle(100)
# point.end_fill()
# turtle.mainloop()
# CLONNING
rainbow=['yellow','blue','red','purple','green','violet','lime','pink']
i=0
point.speed(0)
for i in range(7) :
    point.hideturtle()
    point.begin_fill()
    point.circle(60+(i*10))
    point.fillcolor(rainbow[i])
    point.end_fill()
    point.begin_fill()
    point.circle(-(60 + (i * 10)))
    point.pencolor(rainbow[i])
    point.end_fill()
point.penup(0,-130)
turtle.mainloop()