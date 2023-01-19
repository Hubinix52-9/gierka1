from turtle import Turtle
import random
kolory=["Grafiki/fiol_klc.gif","Grafiki/czerw_klc.gif","Grafiki/braz_klc.gif",
        "Grafiki/szary_klc.gif","Grafiki/nieb_klc.gif","Grafiki/pomar_klc.gif",
        "Grafiki/ziel_klc.gif"]
kolory2=["Grafiki/fiol_klc_u.gif","Grafiki/czerw_klc_u.gif","Grafiki/braz_klc_u.gif",
        "Grafiki/szary_klc_u.gif","Grafiki/nieb_klc.gif_u","Grafiki/pomar_klc_u.gif",
        "Grafiki/ziel_klc.gif"]
trudnosc = [2,2,2,2,3,3,3,4,4,5]
class Klocek(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.shape(random.choice(kolory))
        self.goto(x=x_cor, y=y_cor)
        self.ile_zostalo = random.choice(trudnosc)
        self.sprawdz = self.shape(name=None)
        self.jak_ciezko=self.ile_zostalo
        self.lewy = self.xcor() - 30
        self.prawy = self.xcor() + 30
        self.gorny = self.ycor() + 15
        self.dolny = self.ycor() - 15
        self.zmiana_uszkodzenia()

    def zmiana_uszkodzenia(self):
        if self.jak_ciezko > self.ile_zostalo:
            if self.sprawdz == "Grafiki/fiol_klc.gif":
                self.shape("Grafiki/fiol_klc_u.gif")
            if self.sprawdz == "Grafiki/czerw_klc.gif":
                self.shape("Grafiki/czerw_klc_u.gif")
            if self.sprawdz == "Grafiki/szary_klc.gif":
                self.shape("Grafiki/szary_klc_u.gif")
            if self.sprawdz == "Grafiki/braz_klc.gif":
                self.shape("Grafiki/braz_klc_u.gif")
            if self.sprawdz == "Grafiki/nieb_klc.gif":
                self.shape("Grafiki/nieb_klc_u.gif")
            if self.sprawdz == "Grafiki/pomar_klc.gif":
                self.shape("Grafiki/pomar_klc_u.gif")
            if self.sprawdz == "Grafiki/ziel_klc.gif":
                self.shape("Grafiki/ziel_klc_u.gif")


class klocki:
    def __init__(self):
        self.y_start = 0
        self.y_koniec = 240
        self.klocki = []
        self.tworz_wszystko()

    def tworz(self, y_cor):
        for i in range(-570, 570, 63):
            klocek = Klocek(i, y_cor)
            self.klocki.append(klocek)

    def tworz_wszystko(self):
        for i in range(self.y_start, self.y_koniec, 32):
            self.tworz(i)




