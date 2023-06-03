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

    def __init__(self, fileName):
        self.file = fileName

    def create_stat(self):
        with open(os.path.join(os.path.dirname(__file__), self.file), 'r') as file:
            last_date = datetime.datetime.now()
            for line in file:
                l = line.split("] ")
                date = datetime.datetime.strptime(l[0].replace('[', ''), '%Y-%m-%d %H:%M:%S.%f')
                if date.minute == last_date.minute:
                    if date.hour == last_date.hour:
                        if date.date() == last_date.date:
                            if l[1].replace("\n") != "NOK":
                                if date.format('%Y-%m-%d %H:%M') in self.statistic:
                                    self.statistic[date.format('%Y-%m-%d %H:%M')] += 1
                                else:
                                    self.statistic[date.format('%Y-%m-%d %H:%M')] = 1



newEvent = EventsRestruckt('events.txt')
newEvent.create_stat()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
