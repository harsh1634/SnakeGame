from turtle import Turtle,Screen
from food import Food
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        with open("highscore.txt") as data:
            self.highscore=int(data.read())
        self.goto(0,270)
        self.pendown()
        self.hideturtle()
        self.updateScore()
        file = open("highscore.txt", mode='w')
        file.write("0")
        file.close()

    def updateScore(self):
        self.clear()
        self.write(f"Score : {self.score}   HIGHSCORE : {self.highscore}", align="center", font=("Arial", 21, "normal"))

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align="center", font=("Times new roman", 21, "normal"))
    def reset(self):
        with open("highscore.txt",mode="w") as file:
            if self.score>self.highscore:
                file.write(f"{self.score}")
                self.highscore=self.score

        self.score=0
        self.updateScore()


    def Score_in(self):
        self.score += 1







