# -*- coding: utf-8 -*-
import os.path
import zipfile

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
file_name = 'voyna-i-mir.txt.zip'


class Statistic_char:
    file = ''
    statistics = {}

    def __init__(self, file_name):
        self.file = file_name
    def __del__(self):
        os.remove(self.file)
    def extr(self):
        zip = zipfile.ZipFile(self.file)
        for file in zip.namelist():
            zip.extract(file)
            self.file = file

    def getStat(self):
        with open(self.file, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.statistics:
                            self.statistics[char] += 1
                        else:
                            self.statistics[char] = 1

    def sort_stat(self, sort='val_up'):
        # print(self.statistics.items())
        if len(self.statistics) > 0:
            if (sort == 'val_up'):
                self.statistics = dict(sorted(self.statistics.items(), key=lambda x: x[1]))
            elif (sort == 'val_down'):
                self.statistics = dict(sorted(self.statistics.items(), key=lambda x: x[1], reverse=True))
            elif (sort == 'key_up'):
                self.statistics = dict(sorted(self.statistics.items(), key=lambda x: x[0]))
            elif (sort == 'key_down'):
                self.statistics = dict(sorted(self.statistics.items(), key=lambda x: x[0], reverse=True))

    def print_stat(self, sort='val_up'):
        self.sort_stat(sort)
        print("+{0:-^9}+{1:-^9}+".format("", ""))
        for (char, static) in self.statistics.items():
            print("|{0:^9}|{1:^9}|".format(char, static))
        print("+{0:-^9}+{1:-^9}+".format("", ""))


# print(os.path.join(os.path.dirname(__file__),'python_snippets',  file_name))

new_file = Statistic_char(os.path.join(os.path.dirname(__file__), 'python_snippets', file_name))

new_file.extr()
new_file.getStat()
new_file.print_stat()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
