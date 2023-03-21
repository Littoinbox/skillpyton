# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.name = "Вода"

    def __add__(self, other):
        if other.name == "Воздух":
            return Storm()
        elif other.name == "Огонь":
            return Par()
        elif other.name == "Земля":
            return Dirt()
        else:
            return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Earth:
    def __init__(self):
        self.name = "Земля"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Storm:
    def __init__(self):
        self.name = "Шторм"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Par:
    def __init__(self):
        self.name = "Пар"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Dirt:
    def __init__(self):
        self.name = "Грязь"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Lightning:
    def __init__(self):
        self.name = "Молния"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Dust:
    def __init__(self):
        self.name = "Пыль"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


# Lava
class Lava:
    def __init__(self):
        self.name = "Лава"

    def __add__(self, other):
        return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Air:
    def __init__(self):
        self.name = "Воздух"

    def __add__(self, other):
        if other.name == "Огонь":
            return Lightning()
        elif other.name == "Земля":
            return Dust()
        else:
            return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


class Fire:
    def __init__(self):
        self.name = "Огонь"

    def __add__(self, other):
        if other.name == "Земля":
            return Lava()
        else:
            return None

    def __str__(self):
        return "Элемент " + self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False


elemets = [Water(), Air(), Earth(), Fire()]

play = 1

while play:
    print("есть элементы: ")
    i = 1
    for element in elemets:
        print(str(i) + ' ' + str(element))
        i += 1

    a1 = -1
    while (0 > a1) or (a1 > len(elemets)):
        print("Выберите первый элемет ")
        a1 = int(input()) - 1
        if 0 > a1 > len(elemets):
            print("Выбран не правильный элемент")
    a2 = -1

    while (0 > a2) or (a2 > len(elemets)):
        print("Выберите второй элемет ")
        a2 = int(input()) - 1
        if 0 > a2 > len(elemets):
            print("Выбран не правильный 2 элемент")
    new_element = elemets[a1] + elemets[a2]
    if new_element is None:
        print("Ничего не получеилось!")
        continue
    else:
        print(str(elemets[a1]) + " + " + str(elemets[a2]) + " = " + str(new_element))
    in_arr = False
    for element in elemets:
        if element == new_element:
            in_arr = True
            break
    if not (in_arr):
        elemets.append(elemets[a1] + elemets[a2])

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
