import turtle
screen=turtle.getscreen()
point=turtle.Turtle()
screen.bgcolor('black')
point.speed(10)
rainbow=['yellow','blue','red','purple','green','violet','lime','magenta','orange','white','pink']
for i in range(5):
    for x in range(len(rainbow)):
        point.pencolor(rainbow[x])
        point.left(20)
        point.forward(100 + (i * 10))
        point.left(90)
        point.forward(100 + (i * 10))
        point.left(90)
        point.forward(100 + (i * 10))
        point.left(90)
        point.forward(100 + (i * 10))





turtle.mainloop()