from turtle import Turtle, Screen 
from paddle import Paddle

#Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create two paddles from class
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#Keyboard function
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

#Game loop
game_is_on = True 

while game_is_on:
    screen.update()


screen.exitonclick()