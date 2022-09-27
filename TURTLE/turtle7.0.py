import turtle
screen=turtle.getscreen()
t=turtle.Turtle()
screen.bgcolor('black')
t.speed(0)
rainbow=['yellow','blue','red','purple','green','violet','lime','magenta','orange','white','pink']
for x in range(6):
    for i in range(len(rainbow)):
        t.color(rainbow[i])
        t.right(15)
        t.forward(70+10*i)
        t.right(90)
        t.forward(70 + 10 * i)
        t.right(90)
        t.forward(70 + 10 * i)
        t.right(90)
        t.forward(70 + 10 * i)
        t.right(90)




turtle.mainloop()
