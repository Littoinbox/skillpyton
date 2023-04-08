# -*- coding: utf-8 -*-
import random

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.clean = 0
        self.count_fur = 0
        self.food_cat = 10

    def __str__(self):
        return 'Состояние дома: количество денег {} , количесто еды {} чистота в доме {}, количество шуб {}, еды у кота {}'.format(
            self.money, self.food,
            self.clean, self.count_fur, self.food_cat)


class Human:
    def __init__(self, name, house):
        self.name = name
        self.happy = 100
        self.fullness = 30
        self.house = house

    def __str__(self):
        return self.name + ' состояние: Уровень счастья {}, Уровень сытости {}'.format(self.happy, self.fullness)

    def eat(self):
        if self.house.food >= 30:
            food = 30
        else:
            food = self.house.food
        if food == 0:
            self.fullness -= 10
            print("Еды дома нет!")
            return False
        else:
            self.fullness += food
            self.house.food -= food
            print(self.name + " поел!")
            return True

    def pet_cat(self):
        self.happy += 10
        print(self.name + " Гладил кота")

    def act(self):
        if self.house.clean > 90:
            self.happy -= 5
        if self.fullness < 10:
            print(self.name + " умер!")
            return False
        if self.happy < 10:
            print(self.name + " умер!")
            return False
        return True


class Husband(Human):
    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            if self.fullness < 30:
                self.eat()
            elif self.happy < 20:
                self.gaming()
            elif self.house.money <30:
                self.work()
            else:
                i = random.randint(0, 3)
                if i == 1:
                    self.work()
                elif i == 2:
                    self.pet_cat()
                else:
                    self.gaming()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        print(self.name + " порабоал!")

    def gaming(self):
        self.fullness -= 10
        self.happy += 20
        print(self.name + " поиграл в WoT!")


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if super().act():
            if self.fullness < 30:
                self.eat()
            elif self.house.food < 40:
                self.shopping()
            elif self.happy < 30:
                self.buy_fur_coat()
            elif self.house.food_cat <= 10:
                self.shop_cat_food()
            else:
                i = random.randint(0, 3)
                if i == 0:
                    self.clean_house()
                elif i == 1:
                    self.shopping()
                elif i == 2:
                    self.pet_cat()
                else:
                    self.buy_fur_coat()

    def shop_cat_food(self):
        if self.house.money >= 30:
            get_money = 30
        else:
            get_money = self.house.money
        if get_money == 0:
            print("В доме нет денег купить еду коту")
        else:
            self.house.money -= get_money
            self.house.food_cat += get_money
            print(self.name + " Купила корм коту!")

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 50:
            money = 50
        elif self.house.money < 50:
            money = self.house.money
        else:
            print(self.name + " Дома нет денег!")
            return None
        self.house.money -= money
        self.house.food += money
        print(self.name + " Купила еды!")

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 350:
            self.house.money -= 350
            self.happy += 60
            self.house.count_fur += 1
            print(self.name + " Купила шубу!")
        else:
            print(self.name + " Нехватает денег на шубу!")

    def clean_house(self):
        self.fullness -= 10
        if self.house.clean == 0:
            print(self.name + " В доме чисто!")
        else:
            if self.house.clean >= 100:
                self.house.clean -= 100
            else:
                self.house.clean = 0
            print(self.name + " прибралась в доме!")

    def eat(self):
        if not super().eat():
            self.fullness += 10
            self.shopping()


# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)

# for day in range(365):
#    cprint('================== День {} =================='.format(day), color='red')
#    serge.act()
#    masha.act()
#    cprint(serge, color='cyan')
#    cprint(masha, color='cyan')
#    cprint(home, color='cyan')
#    home.clean += 5


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return self.name + " Состояние голод {}".format(self.fullness)

    def act(self):
        if self.fullness == 0:
            print("Кот умер!")
            return False
        if self.fullness <= 10:
            self.eat()
        else:
            i = random.randint(0, 1)
            if (i == 0):
                self.sleep()
            else:
                self.soil()

    def eat(self):
        if self.house.food_cat >= 10:
            food = 10
        else:
            food = self.house.food_cat

        if food == 0:
            self.fullness-=10
            print("У кота нет еды")
        else:
            self.house.food_cat -= food
            self.fullness += food * 2

    def sleep(self):
        self.fullness -= 10
        print('Кот поспал!')

    def soil(self):
        self.house.clean += 5
        self.fullness -= 10
        print('Кот драл обои!')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness == 0:
            print(self.name + " умер!")
            return True
        if self.fullness <= 10:
            self.eat()
            return True
        i = random.randint(0, 1)
        if i == 0:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            get_food = 10
        else:
            get_food = self.house.food

        if get_food == 0:
            self.fullness -= 10
            print(self.name + " Дома нет еды")
        else:
            self.fullness += get_food
            self.house.food -= get_food
            print(self.name + " Поел!")

    def sleep(self):
        self.fullness -= 10
        print(self.name + " Поспал")


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)
#
for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
