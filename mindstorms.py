import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()

    brad.forward(100) #go forward 100px
    brad.right(90) # go right 90px

    brad.forward(100)
    brad.right(90)

    brad.forward(100) #go forward 100px
    brad.right(90) # go right 90px

    brad.forward(100)
    brad.right(90)


    window.exitonclick()

draw_square()