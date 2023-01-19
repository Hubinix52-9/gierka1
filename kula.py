from turtle import Turtle
import random

ruch1=7

class kula(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Grafiki/ball.gif")
        self.color("red")
        self.penup()
        self.x_ruch=ruch1
        self.y_ruch=ruch1
        self.reset()



    def ruszaj(self):
        x_pr=self.xcor()+self.x_ruch
        y_pr=self.ycor()+self.y_ruch
        self.goto(x=x_pr, y=y_pr)

    def odbicie(self, odb_x, odb_y):
        if odb_x:
            self.x_ruch *=-1

        if odb_y:
            self.y_ruch *=-1

    def reset(self):
        self.goto(x=0,y=-220)
        self.y_ruch = abs(self.y_ruch)
