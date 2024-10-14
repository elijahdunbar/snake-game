from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.color("white")
    self.ht()
    self.goto(0, 270)
    self.score = 0
    self.high_score = 0
    self.refresh_score()

  def refresh_score(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def add_point(self):
    self.score += 1
    self.refresh_score()

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.refresh_score()

  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write("GAME OVER", align=ALIGNMENT, font=FONT)

