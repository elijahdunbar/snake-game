import random
from turtle import Turtle


class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("yellow")
    self.speed("fastest")
    self.refresh()


  def refresh(self):
    rand_x = random.randint(-265, 265)
    rand_y = random.randint(-265, 265)
    self.goto(rand_x, rand_y)

