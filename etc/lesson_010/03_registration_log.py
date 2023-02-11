# -*- coding: utf-8 -*-
from termcolor import cprint


class LostPedalError(Exception):
    pass


def check_name(name):
    if not name.isalpha():
        raise LostPedalError('LostPedalError')


def check_age(age):
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


def run(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:
            try:
                line = line[:-1]
                name, email, age = line.split(' ')
                check_name(name=name)
                check_age(age=age)
                cprint(f'{name}, {email}, {age}', color='yellow')
            except Exception as exc:
                cprint(f'In line {line} exception {exc}', color='red')


if __name__ == '__main__':
    run(file_name='../registrations.txt')
