# -*- coding: utf-8 -*-
import os


# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

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
