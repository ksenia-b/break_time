import turtle

def draw_square(some_turtle):
        for i in range(1,5):
            some_turtle.forward(100)
            some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the Turtle
    brad = turtle.Turtle()
    brad.speed(2)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)


    #Create the turtle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    window.exitonclick()

draw_art()