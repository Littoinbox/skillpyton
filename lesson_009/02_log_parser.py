# -*- coding: utf-8 -*-
import datetime
import os.path


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class EventsRestruckt:
    file = ''
    outFile = ""
    statistic = {}
    group = ""

    def __init__(self, inputFile, outFile, group='minute'):
        self.file = inputFile
        self.outFile = outFile
        self.setGroup(group)

    def setGroup(self, group):
        if group == 'month':
            self.group = '%Y-%m'
        elif group == 'minute':
            self.group = '%Y-%m-%d %H:%M'
        elif group == 'year':
            self.group = '%Y'
        elif group == 'hours':
            self.group = '%Y-%m-%d %H'
        elif group == 'days':
            self.group = '%Y-%m-%d'

    def create_stat(self):
        with open(os.path.join(os.path.dirname(__file__), self.file), 'r') as file:
            for line in file:
                l = line.split("] ")
                date = datetime.datetime.strptime(l[0].replace('[', ''), '%Y-%m-%d %H:%M:%S.%f')
                if l[1].replace("\n", "") == "NOK":
                    if date.strftime(self.group) in self.statistic:
                        self.statistic[date.strftime(self.group)] += 1
                    else:
                        self.statistic[date.strftime(self.group)] = 1

    def writeStat(self):
        if len(self.outFile) > 0 and len(self.statistic) > 0:
            file = open(os.path.join(os.path.dirname(__file__), self.outFile), 'w')
            for key in self.statistic:
                file.write(str(key) + " " + str(self.statistic[key]) + "\r")


newEvent = EventsRestruckt('events.txt', 'newEvent.txt')
newEvent.create_stat()
newEvent.writeStat()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
