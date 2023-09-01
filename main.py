from turtle import Turtle, Screen 
from paddle import Paddle
from ball import Ball 
import time 
from score import Score

#Create a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create two paddles from class
r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))

#Create ball & score object
ball = Ball()
score = Score()

#Keyboard function
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

#Game loop
game_is_on = True 

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        #Ball need to bounce
        ball.bounce()

    #Detect collision with the paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    #Detect when right paddles miss the ball:
    if ball.xcor() > 380:
         ball.reset_position()
         score.l_get_score()

    #Detect when left paddles miss the ball:
    if ball.xcor() < -380:
         ball.reset_position()
         score.r_get_score()

screen.exitonclick()