from turtle import Turtle

FONT = ('Arial', 50, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0 
        self.r_score = 0
        self.penup()
        self.update_score()

    #Add right score
    def r_get_score(self):
        self.r_score += 1
        self.update_score()

    #Add left score
    def l_get_score(self):
        self.l_score += 1
        self.update_score()

    #Update score
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=FONT)
