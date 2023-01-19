from turtle import Turtle
import random
import time

czcionka = ("Courier", 52, "normal")
kolory = ['red','green','blue','purple','yellow','pink']


class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(kolory))
        self.naglowek()

    def naglowek(self):
        self.color('white')
        self.clear()
        self.goto(x=0, y=-120)
        self.write('Breakout', align='center', font=czcionka)
        self.goto(x=-580, y=-150)
        self.write('Naciśnij spacje, aby wznowić lub zatrzymać grę ',
                   align='left', font=('Calibri', 14, 'normal'))
        self.goto(x=-580, y=-180)
        self.write('Naciśnij m, aby ponownie włączyć lub zatrzymać muzyke',
                   align='left', font=('Calibri', 14, 'normal'))
        self.goto(x=-580, y=-210)
        self.write('Naciśnij d, aby zmienić tło na następne jeżeli masz przynajmniej 150 punktów najwyszego wyniku, lub a, aby cofnąć do poprzedniego',
                   align='left', font=('Calibri', 14, 'normal'))
        self.goto(x=-580, y=-240)
        self.write('Naciśnij strzałkę w górę aby zwiększyć szybkość piłki bądź, w strzałkę w dół, aby ją zmniejszyć',
                   align='left', font=('Calibri', 14, 'normal'))
        self.goto(x=-580, y=-270)
        self.write('Naciśnij q aby zwiększyć mnożnik na x2',
                   align='left', font=('Calibri', 14, 'normal'))

    def zmiana_koloru(self):
        self.clear()
        self.color(random.choice(kolory))
        self.naglowek()

    def zatrzymane(self):
        self.clear()
        self.zmiana_koloru()
        time.sleep(0.5)

    def game_over(self, wygrana):
        self.clear()
        self.goto(x=0, y=-240)
        if wygrana == True:
            self.write('Ukończyłeś grę!!', align='center', font=czcionka)
        else:
            self.write("Przegrałeś", align='center', font=czcionka)
