from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(open("high_score.txt", "r").read())
        self.penup()
        self.color("white")
        self.pencolor("white")
        self.setposition(x=0, y=270)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.clear()
        with open("high_score.txt", "r") as reader:
            self.write(f"You score: {self.score} High score: {reader.read()}", move=False, align=ALIGNMENT, font=FONT)

    def get_point(self):
        self.score += 1

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.show_score()