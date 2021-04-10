from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fwd():
    tim.forward(10)

def move_bkw():
    tim.back(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_screen():
    tim.clear()


screen.listen()
screen.onkeypress(fun=move_fwd, key='Up')
screen.onkeypress(fun=move_bkw, key='Down')
screen.onkeypress(fun=turn_right, key='Right')
screen.onkeypress(fun=turn_left, key='Left')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
