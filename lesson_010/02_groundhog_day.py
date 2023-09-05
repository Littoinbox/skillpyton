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
    def returnError(self):
        return "Исключение бога"


class DrunkError(Exception):
    def returnError(self):
        return "Исключение пьяни"


class CarCrashError(Exception):
    def returnError(self):
        return "Исключение Автоаварии"


class GluttonyError(Exception):
    def returnError(self):
        return "Исключение чревоугодья"


class DepressionError(Exception):
    def returnError(self):
        return "Исключение депрессии"


class SuicideError(Exception):
    def returnError(self):
        return "Исключение суицидв"


def randomExeption():
    errorNumber = random.randint(1, 6)
    if errorNumber == 1:
        return IamGodError()
    if errorNumber == 2:
        return DrunkError()
    if errorNumber == 3:
        return CarCrashError()
    if errorNumber == 4:
        return GluttonyError()
    if errorNumber == 5:
        return DepressionError()
    if errorNumber == 6:
        return SuicideError()


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
        print(f"Произошла ошибка {err.__class__.__name__}, Текст ощибки {err.returnError()}")
    except  DrunkError as err:
        print(f"Произошла ошибка {err.__class__.__name__}, Текст ощибки {err.returnError()}")
    except  CarCrashError as err:
        print(f"Произошла ошибка {err.__class__.__name__}, Текст ощибки {err.returnError()}")
    except  GluttonyError as err:
        print(f"Произошла ошибка {err.__class__.__name__}, Текст ощибки {err.returnError()}")
    except  DepressionError as err:
        print(f"Произошла ошибка {err.__class__.__name__}, Текст ощибки {err.returnError()}")
    except  SuicideError as err:
        print(f"Произошла ошибка {err.__class__.__name__}, Текст ошибки {err.returnError()}")
    finally:
        print(f"Прошел {day} день, карма равна {karmaSumma}")
# https://goo.gl/JnsDqu
