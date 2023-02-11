# -*- coding: utf-8 -*-
from functools import reduce


class Producer:

    def __init__(self):
        self.listeners = []

    def subscribe(self, listener_callback):
        self.listeners.append(listener_callback)

    def message(self, msg):
        for callback in self.listeners:
            try:
                callback(msg)
            except Exception as exc:
                print('Листенер не справился', exc)


class Listener:

    def __init__(self, name):
        self.name = name

    def process(self, msg):
        print(self.name, 'Я получил сообщение', msg)


tv_station = Producer()

tv = Listener('телевизор')
tv_station.subscribe(tv.process)

fm = Listener('радио')
tv_station.subscribe(fm.process)

tv_station.message('Кино Самогонщики')


res = reduce(lambda a, b: a * b, map(lambda x: x ** 2, [1, 2, 3, 4]))
print(res)
