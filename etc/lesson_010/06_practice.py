# -*- coding: utf-8 -*-

# Есть файл calc.txt с записями операций - текстовый калькулятор. Записи вида
#
# 100 + 34
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделенные пробелами.
#
# Нужно вычислить все операции и найти их сумму.

# TODO здесь ваш код


class ApocalypticNumberError(Exception):
    pass


def proceed_line(line):
    global total
    op1, operand, op2 = line.split()
    op1, op2 = int(op1), int(op2)
    if op1 == 666 or op2 == 666:
        raise ApocalypticNumberError()
    if operand == '+':
        total += op1 + op2
    elif operand == '-':
        total += op1 - op2
    elif operand == '*':
        total += op1 * op2
    elif operand == '/':
        total += op1 / op2
    elif operand == '%':
        total += op1 % op2
    elif operand == '//':
        total += op1 // op2


total = 0
with open('../../solutions/lesson_010/calc.txt', 'r') as ff:
    for i, line in enumerate(ff):
        line = line[:-1]
        # print(line)
        try:
            proceed_line(line)
        except ValueError as exc:
            print(f'Ошибка {exc} в строке №{i} "{line}"')
        except ApocalypticNumberError:
            print('Чур меня!')
print(total)
