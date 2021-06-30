class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.paliwo = 0
        #self.ilosc_miejsc = 0
        #self.liczba_przystankow = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        if self.paliwo < 5:
            print("Wcześniej zatankuj!")
        else:
            self.speed += 5
            self.paliwo -= self.odometer/10

    def brake(self):
        if self.speed <5:
            self.speed = 0
        else:
            self.speed -=5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time

    def zatankuj(self):
        if self.paliwo < 46:
            self.paliwo += 5
        else:
            print("Bak jest pełny")


class Autobus(Car):
    def __init__(self):
        super().__init__()
        self.ilosc_miejsc = 0
        self.liczba_przystankow = 0

    def wsiadaja(self):
        self.ilosc_miejsc += 3
        print("Liczba ludzi w autobusie {}.".format(self.ilosc_miejsc))

    def przystanek(self):
        self.liczba_przystankow += 1
        print("Liczba przystanków {}.".format(self.liczba_przystankow))


class Ciezarowy(Car):
    def __init__(self):
        super().__init__()
        self.pojemnosc = 0
        self.awaryjne = 0

    def zaladuj(self):
        self.pojemnosc += 5
        print("Załadowano:{}".format(self.pojemnosc))

    def wlacz_awaryjne(self):
        self.awaryjne = True
        print("Awaryjne: {}".format(self.awaryjne))


if __name__ == '__main__':

    my_car = Car()
    autobus= Autobus()
    ciezarowy=Ciezarowy()
    print("I'm a car!")
    while True:
        action = input("What should I do ? [A]ccelerate, "
                       "[B]rake, show [O]dometer, "
                       "show average [S]peed, [R]efuel or amount of [F]uel \n"
                       "[W]siadaja ludzie, [D]odaj przystanek, [Z]aładuj auto lub w[L]acz awaryjne?").upper()
        if action not in "ABOSRFWDZL" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} "
                  "kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} "
                  "kph".format(my_car.average_speed()))
        elif action == 'R':
            my_car.zatankuj()
        elif action == 'F':
            print("There are {} liters of fuel in the tank.".format(my_car.paliwo))
        elif action == 'W':
            autobus.wsiadaja()
        elif action == 'D':
            autobus.przystanek()
        elif action == 'Z':
            ciezarowy.zaladuj()
        elif action == 'L':
            ciezarowy.wlacz_awaryjne()
        my_car.step()
        my_car.say_state()
