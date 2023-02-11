# -*- coding: utf-8 -*-

from itertools import combinations, permutations
from random import choice, randint

operations = ['+', '-', '*', '/', '%', '//']

with open('../../solutions/lesson_010/calc.txt', 'w') as ff:
    for i in range(10000):
        op1, op2 = str(randint(1, 999)), str(randint(1, 999))
        operation = choice(operations)
        line = [op1, operation, op2]
        if randint(1, 30) == 1:
            if randint(1, 2) == 1:
                line = list(permutations(line))
            else:
                line = list(combinations(line, randint(0, 2)))
            print(line)
            if line:
                line = choice(line)
                print(line)
        line = ' '.join(line)
        ff.write(f'{line}\n')
