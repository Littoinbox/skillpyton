# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def randomExeption():
    errorNumber = random.randint(1, 6)
    if errorNumber == 1:
        return IamGodError("Исключение бога")
    if errorNumber == 2:
        return DrunkError("Исключение пьяни")
    if errorNumber == 3:
        return CarCrashError("Исключение Автоавирии")
    if errorNumber == 4:
        return GluttonyError("Исключение чревоугодья")
    if errorNumber == 5:
        return DepressionError("Исключение депрессии")
    if errorNumber == 6:
        return SuicideError("Исключение суицида")


def one_day():
    i = random.randint(1, 13)
    if i == 13:
        raise randomExeption()
    else:
        return random.randint(1, 7)


karmaSumma = 0
day = 0
while karmaSumma <= ENLIGHTENMENT_CARMA_LEVEL:
    try:
        day += 1
        karmaSumma += one_day()
    except  IamGodError as err:
        print(f"Произошла ошибка {type(err)}, Текст ощибки {err}")
    except  DrunkError as err:
        print(f"Произошла ошибка {type(err)}, Текст ощибки {err}")
    except  CarCrashError as err:
        print(f"Произошла ошибка {type(err)}, Текст ощибки {err}")
    except  GluttonyError as err:
        print(f"Произошла ошибка {type(err)}, Текст ощибки {err}")
    except  DepressionError as err:
        print(f"Произошла ошибка {type(err)}, Текст ощибки {err}")
    except  SuicideError as err:
        print(f"Произошла ошибка {type(err)}, Текст ошибки {err}")
    finally:
        print(f"Прошел {day} день, карма равна {karmaSumma}")
# https://goo.gl/JnsDqu
