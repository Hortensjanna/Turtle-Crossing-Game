from turtle import Turtle

FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-230, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", False, align="center", font=FONT)

    def track_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align='center', font=FONT)
