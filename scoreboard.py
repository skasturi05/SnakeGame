from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg="Score= " + str(self.score) + "High score = " + str(self.high_score), move=False, align="center",
                   font=("Verdana", 12, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="G A M E O V E R", move=False, align="center", font=("Verdana", 12, "normal"))
