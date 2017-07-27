import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)

    brad.forward(100) #go forward 100px
    brad.right(90) # go right 90px

    brad.forward(100)
    brad.right(90)

    brad.forward(100) #go forward 100px
    brad.right(90) # go right 90px

    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    triangle = turtle.Turtle()
    triangle.shape('turtle')
    triangle.color('green')
    triangle.forward(100)
    triangle.right(90)
    triangle.home()
    triangle.position()

    window.exitonclick()

draw_square()