# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')
    def by_cat_food(self):
        if self.house.money >= 50:
            self.house.food_cat += 50
            self.house.money -= 50
        else:
            cprint('{} нет денег коту на еду!'.format(self.name), color='red')

    def clean_after_cat(self):
        if self.house.clean > 0:
            cprint('{} убирал за котом'.format(self.name), color='green')
            self.fullness -= 20
            self.house.clean = 0
        else:
            cprint('{} хотел убирать за котом, но в доме чисто'.format(self.name), color='green')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def take_cat(self, cat):
        self.fullness -= 10
        cat.house = self.house
        self.house.hase_cat = True
        cprint('{} Подобрал кота'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif not self.house.hase_cat:
            self.take_cat(cat)
        elif self.house.food_cat <= 10:
            self.by_cat_food()
        elif self.house.clean > 50:
            self.clean_after_cat()
        elif not self.house.hase_cat:
            self.take_cat(cat)
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.clean = 0
        self.food_cat = 0
        self.hase_cat = False

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, чистота в доме {}, еды для кота {}'.format(
            self.food, self.money,self.clean, self.food_cat,
        )

class Cat():

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None


    def play(self):
        self.house.clean += 10
        self.fullness -= 10
        cprint("Кот поиграл")
    def sleep(self):
        self.fullness -= 10
        cprint("Кот поспал")
    def eat(self):
        if self.house.food_cat > 0:
            self.fullness += 50
            self.house.food_cat -= 10
            cprint("Кот поел")
        else:
            self.fullness -= 10
            cprint("В доме нет еды для кота!")
    def action(self):
        i = randint(1, 3)
        if self.fullness == 0:
            cprint("Кот умер")
        elif self.fullness < 20:
            self.eat()
        elif i == 1:
            self.play()
        else:
            self.sleep()

    def __str__(self):
        return "Кот сытость {} ".format(self.fullness)



citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

cat = Cat('Васька')
my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    cat.action()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(cat)
    print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
