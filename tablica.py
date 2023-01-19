from turtle import Turtle

try:
    punkty1 = int(open('najwiekszy.txt', 'r').read())
except FileNotFoundError:
    punkty1 = open('najwiekszy.txt', 'w').write(str(0))
except ValueError:
    punkty1 = 0
czcionka = ('arial', 18, 'normal')

class Tablica(Turtle):
    def __init__(self, zycia):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.najwiekszy_wynik = punkty1
        self.goto(x=-580, y=260)
        self.zycia = zycia
        self.punkty = 0
        self.update_punkty()

    def update_punkty(self):
        self.clear()
        self.write(f"Punkty: {self.punkty} | Największy wynik: {self.najwiekszy_wynik} | Życia: "
                   f"{self.zycia} ", align='left', font=czcionka)

    def zwiekszanie_punktow(self):
        self.punkty += 1
        if self.punkty > self.najwiekszy_wynik:
            self.najwiekszy_wynik += 1
        self.update_punkty()

    def zmniejszanie_zyc(self):
        self.zycia -= 1
        self.update_punkty()

    def reset(self):
        self.clear()
        self.punkty = 0
        self.update_punkty()
        open('najwiekszy.txt', 'w').write(str(self.najwiekszy_wynik))