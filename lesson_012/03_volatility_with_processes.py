# -*- coding: utf-8 -*-
import os
from multiprocessing import Process, Pipe


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
class Valatation(Process):

    def __init__(self, file_name, conn,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.conn = conn
        self.max = 0
        self.min = 0
        self.half_sum = 0
        self.volatility = 0


    def run(self):
        self.read_file(self.file_name)

    def read_file(self, full_file_path):
        with open(full_file_path, mode='r', encoding='utf8') as file:
            self.max = 0
            self.min = -1
            self.half_sum = 0
            self.volatility = 0
            self.name = ''
            for line in file:
                l = line.split(",")
                if l[1] == 'TRADETIME':
                    continue
                self.name = l[0]
                if float(l[2]) > self.max:
                    self.max = float(l[2])
                    self.calcVal()
                if float(l[2]) < self.min or self.min == -1:
                    self.min = float(l[2])
                    self.calcVal()
            self.conn.send([self.name, self.volatility])
            self.conn.close()

    def calcVal(self):
        try:
            self.half_sum = (self.min + self.max) / 2
            self.volatility = ((self.max - self.min) / self.half_sum) * 100
        except (ZeroDivisionError):
            self.half_sum = 0
            self.volatility = 0


def print_info(list):
    maxValue = sorted(list.items(), key=lambda x: x[1], reverse=True)[:3]
    non_zero_values = [v for k, v in list.items() if v != 0]
    minValue = sorted(non_zero_values)[:3]
    zeroVal = sorted([k for k, v in list.items() if v == 0])

    print("Максимальная волатильность:")
    for key, val in maxValue:
        print(" " * 3, key, " - ", val)
    print("Минимальная волатильность:")
    for value in minValue:
        key = [k for k, val in list.items() if val == value][0]
        print(" " * 3, key, " - ", value)
    print("Нулевая волатильность:")
    print(', '.join(zeroVal))

if __name__ == '__main__':
    path = 'trades'
    lists = {}
    process, pipes = [], []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            parent_conn, child_conn = Pipe()
            full_file_path = os.path.join(dirpath, file)
            print("Создаем процесс для файла ", full_file_path)
            process.append(Valatation(file_name=full_file_path, conn=child_conn))
            pipes.append(parent_conn)

    for proces in process:
        proces.start()
    for conn in pipes:
        name, valot = conn.recv()
        print(f"Из трубы {conn} приняли сообщение {name} с волотильностью {valot}")
        lists[name] = valot
    for proces in process:
        proces.join()

    print_info(lists)