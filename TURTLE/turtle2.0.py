import turtle
screen=turtle.getscreen()
poiint=turtle.Turtle()
poiint.hideturtle()
color=('red', 'yellow')
poiint.speed(5)
poiint.begin_fill()
poiint.fillcolor('red')
while True:
    poiint.forward(200)
    poiint.left(170)
    if abs(poiint.pos()) < 1:
        break
poiint.end_fill()
# poiint.done()
turtle.mainloop()
