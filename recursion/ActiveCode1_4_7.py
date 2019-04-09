import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.color('red')
        myTurtle.forward(lineLen)
        myTurtle.right(33)
        drawSpiral(myTurtle, lineLen-10)


drawSpiral(myTurtle, 100)
myWin.exitonclick()
