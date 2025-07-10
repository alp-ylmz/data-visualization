import turtle
import math
import time

class TurkBayragi:
    def __init__(self, en=600):
        self.en = en
        self.boy = en * 2 / 3  # Bayrak oranı: en / boy = 2 / 3
        self.kalem = turtle.Turtle()
        self.kalem.hideturtle()
        self.kalem.speed(0)
        self.ekran = turtle.Screen()
        self.ekran.bgcolor("red")
        self.ekran.title("Profesyonel Türk Bayrağı")

    def daire(self, x, y, r, renk):
        self.kalem.penup()
        self.kalem.goto(x, y - r)
        self.kalem.setheading(0)
        self.kalem.pendown()
        self.kalem.color(renk)
        self.kalem.begin_fill()
        self.kalem.circle(r)
        self.kalem.end_fill()
        time.sleep(0.5)

    def yildiz(self, x, y, r, renk):
        self.kalem.penup()
        self.kalem.goto(x, y)
        self.kalem.setheading(-90)
        self.kalem.forward(r)
        self.kalem.setheading(0)
        self.kalem.pendown()
        self.kalem.begin_fill()
        self.kalem.color(renk)
        for _ in range(5):
            self.kalem.forward(2 * r * math.sin(math.radians(36)))
            self.kalem.right(144)
        self.kalem.end_fill()
        time.sleep(0.5)

    def ciz(self):
        # Bayrak merkezini (0,0) kabul ediyoruz
        # TSE’ye göre oranlar (sadeleştirilmiş)
        G = self.en  # En
        A = G * 1.5   # Boy

        # Ay (hilal) oranları
        D = G * 0.5      # Büyük daire çapı
        d = G * 0.4      # Küçük daire çapı
        x1 = -G * 0.25   # Büyük daire merkezi
        x2 = -G * 0.15   # Küçük daire merkezi

        # Yıldız oranları
        y_r = G * 0.15   # Yıldızın çevrelendiği dairenin yarıçapı
        y_x = G * 0.05   # Yıldızın merkezi

        # Hilal (2 daire ile yapılır)
        self.daire(x1, 0, D / 2, "white")
        self.daire(x2, 0, d / 2, "red")

        # Yıldız
        self.yildiz(y_x, 0, y_r, "white")

        self.ekran.exitonclick()

# Çalıştır
if __name__ == "__main__":
    bayrak = TurkBayragi(en=600)
    bayrak.ciz()
