from turtle import Turtle

ruch = 80

class obijacz(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape("Grafiki/odbijacz.gif")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)
    def ruch_lewo(self):
        self.backward(ruch)

    def ruch_prawo(self):
        self.forward(ruch)