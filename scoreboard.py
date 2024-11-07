from turtle import Turtle

from Tools.demo.spreadsheet import center


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score =int(file.read())
        self.hideturtle()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset_scoreboard(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score=0
        self.update_score()


    def increase_score(self):
        self.score+=1
        self.update_score()




