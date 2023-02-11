# -*- coding: utf-8 -*-


class DecorMixin:

    def __init__(self, obj):
        self.obj = obj

    def cost(self):
        return self.obj.cost()

    def recept(self):
        return self.obj.recept()


class Coffee(DecorMixin):

    def __init__(self, obj=None):
        super(Coffee, self).__init__(obj=obj)
        self._cost = 5

    def cost(self):
        return self._cost

    def recept(self):
        return 'Кофе'


class Latte(DecorMixin):

    def cost(self):
        return self.obj.cost() + .75


class Syrop(DecorMixin):

    def recept(self):
        return self.obj.recept() + ' и сироп'


cup = Coffee()
cup = Latte(cup)
cup = Syrop(cup)

print(cup.cost())
print(cup.recept())
