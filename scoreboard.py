from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.ht()
    self.goto(0, 270)
    self.score = 0
    self.refresh_score()


  def refresh_score(self):
    self.color("white")
    self.clear()
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def add_point(self):
    self.score += 1
    self.refresh_score()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

