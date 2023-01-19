import turtle
import time
from odbijacz import *
from tablica import *
from ui import UI
from kula import *
from klocki import *
from pygame import mixer

screen=turtle.Screen()

screen.register_shape(name="Grafiki/odbijacz.gif")
screen.register_shape(name="Grafiki/ball.gif")
screen.register_shape(name="Grafiki/hp.gif")
screen.register_shape(name="Grafiki/punkty.gif")
screen.register_shape(name="Grafiki/fiol_klc.gif")
screen.register_shape(name="Grafiki/fiol_klc_u.gif")
screen.register_shape(name="Grafiki/czerw_klc.gif")
screen.register_shape(name="Grafiki/czerw_klc_u.gif")
screen.register_shape(name="Grafiki/braz_klc.gif")
screen.register_shape(name="Grafiki/braz_klc_u.gif")
screen.register_shape(name="Grafiki/szary_klc.gif")
screen.register_shape(name="Grafiki/szary_klc_u.gif")
screen.register_shape(name="Grafiki/nieb_klc.gif")
screen.register_shape(name="Grafiki/nieb_klc_u.gif")
screen.register_shape(name="Grafiki/pomar_klc.gif")
screen.register_shape(name="Grafiki/pomar_klc_u.gif")
screen.register_shape(name="Grafiki/ziel_klc.gif")
screen.register_shape(name="Grafiki/ziel_klc_u.gif")

screen.setup(width=1200, height=600)
print(screen.setup)
screen.bgcolor('black')
screen.title(titlestring="Arkanoid")
screen.tracer(0)
screen.bgpic("Grafiki/background.gif")

odb = obijacz()
klocki = klocki()
kula = kula()
mixer.init()
mixer.music.load("sound1.wav")
mixer.music.play()
muzyka=True
mnoznik=1

ui = UI()
ui.naglowek()
punkty = Tablica(zycia=5)
gra_wstrzymana = False
gra = True

def stop_muzyka():
    global muzyka
    if muzyka:
        muzyka=False
        mixer.music.pause()
    else:
        muzyka=True
        mixer.music.play()
def zatrzymanie_gry():
    global gra_wstrzymana
    if gra_wstrzymana==True:
        gra_wstrzymana = False
    elif gra_wstrzymana==False:
        gra_wstrzymana = True
def poprz_ekran():
    if screen.bgpic(picname=None)=="Grafiki/background.gif" :
        pass
    else :
        screen.bgpic("Grafiki/background.gif")
def nast_ekran():
    if  punkty1>150:
        if screen.bgpic(picname=None)=="Grafiki/background.gif" :
            screen.bgpic("Grafiki/background2.gif")
        else :
            pass
def szybsza_pilka():
    if kula.y_ruch>0:
        kula.y_ruch+=1
    else:
        kula.y_ruch-=1
def wolniejsza_pilka():
    if kula.y_ruch>0:
        kula.y_ruch-=1
    else:
        kula.y_ruch+=1
def zwiekszenie_mnoznika():
    global mnoznik
    mnoznik=2

screen.listen()
screen.onkey(key='q', fun=zwiekszenie_mnoznika)
screen.onkey(key="Up", fun=szybsza_pilka)
screen.onkey(key="Down", fun=wolniejsza_pilka)
screen.onkey(key="Left", fun=odb.ruch_lewo)
screen.onkey(key="Right", fun=odb.ruch_prawo)
screen.onkey(key='space', fun=zatrzymanie_gry)
screen.onkey(key="m", fun=stop_muzyka)
screen.onkey(key="a", fun=poprz_ekran)
screen.onkey(key="d", fun=nast_ekran)

def kolizja():

    global kula,punkty,gra,ui

    if kula.xcor()< -580 or kula.xcor()>570:
        kula.odbicie(odb_x=True, odb_y=False)

    if kula.ycor()>270:
        kula.odbicie(odb_x=False, odb_y=True)

    if kula.ycor()< -280:
        kula.reset()
        punkty.zmniejszanie_zyc()
        if punkty.zycia == 0:
            punkty.reset()
            gra = False
            ui.game_over(wygrana=False)
            return
        return

def kolizja_z_odbijaczem():
    global kula, odb
    dystans=kula.distance(odb)
    odbijacz_x = odb.xcor()
    kula_x = kula.xcor()

    if dystans < 110 and kula.ycor() < -250:

        if odbijacz_x>0:
            if kula_x > odbijacz_x:
                kula.odbicie(odb_x=True, odb_y=True)
                return
            else:
                kula.odbicie(odb_x=False, odb_y=True)
                return

        elif odbijacz_x<0:
            if kula_x < odbijacz_x:
                kula.odbicie(odb_x=True, odb_y=True)
                return
            else:
                kula.odbicie(odb_x=False, odb_y=True)
                return

        else:
            if kula_x > odbijacz_x:
                kula.odbicie(odb_x=True, odb_y=True)
            elif kula_x < odbijacz_x:
                kula.odbicie(odb_x=True, odb_y=True)
            else:
                kula.odbicie(odb_x=False, odb_y=True)

def kolizja_z_klockami():
    global kula, klocki, punkty
    for klocek in klocki.klocki:
         if kula.distance(klocek) < 40:
            for x in range(mnoznik):
                punkty.zwiekszanie_punktow()
            klocek.ile_zostalo -= 1
            klocek.zmiana_uszkodzenia()
            if kula.xcor() < klocek.lewy:
                kula.odbicie(odb_x=True, odb_y=False)
            elif kula.xcor() > klocek.prawy:
                kula.odbicie(odb_x=True, odb_y=False)
            elif kula.xcor() < klocek.dolny:
                kula.odbicie(odb_x=False, odb_y=True)
            elif kula.xcor() < klocek.gorny:
                kula.odbicie(odb_x=False, odb_y=True)
            if klocek.ile_zostalo == 0:
                klocek.clear()
                klocek.goto(x=5000, y=5000)
                klocki.klocki.remove(klocek)


while gra:
    if gra_wstrzymana==False:
        screen.update()
        time.sleep(0.01)
        kula.ruszaj()
        kolizja()
        kolizja_z_odbijaczem()
        kolizja_z_klockami()

        if len(klocki.klocki) == 0:
            ui.game_over(wygrana=True)
            break
    else:
        ui.zatrzymane()
turtle.mainloop()



