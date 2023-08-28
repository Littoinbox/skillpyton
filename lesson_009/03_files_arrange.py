# -*- coding: utf-8 -*-

import os
import time
import datetime
import shutil
import zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class dirSorter:
    inputDir = ""
    outputDir = ""

    def __init__(self, inputDir='icons', outputDir='icons_by_year'):
        self.inputDir = os.path.join(os.path.dirname(__file__), inputDir)
        self.outputDir = os.path.join(os.path.dirname(__file__), outputDir)
        self.createrDir(self.outputDir)

    def createrDir(self, name):
        if os.path.exists(name):
            return True
        else:
            try:
                os.makedirs(name)
                return True
            except OSError as e:
                print(f"Возникла ошибка: {e}")
                return False

    def copyFiles(self):
        for dirpath, dirnames, filenames in os.walk(self.inputDir):
            if len(filenames) > 0:
                for fileName in filenames:
                    filemap = os.path.join(dirpath, fileName)
                    date = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(dirpath, fileName)))
                    if self.checkDir(date):
                        try:
                            shutil.copy2(os.path.join(dirpath, fileName),
                                         os.path.join(self.outputDir, date.strftime("%Y"), date.strftime("%m")))
                        except shutil.Error as err:
                            print(f"Не удалось скопировать файл {filemap}: ошибка {err}")

    def checkDir(self, date):
        if self.createrDir(os.path.join(self.outputDir, date.strftime("%Y")) and
                           self.createrDir(os.path.join(self.outputDir, date.strftime("%Y"), date.strftime("%m")))):
            return True
        else:
            return False


class zipSorter(dirSorter):

    def copyFiles(self):
        zip = zipfile.ZipFile(self.inputDir)
        for file in zip.namelist():
            file_info = zip.getinfo(file)
            date = datetime.datetime(*file_info.date_time)
            file_name = os.path.basename(file_info.filename)
            new_file = os.path.join(self.outputDir, date.strftime("%Y"), date.strftime("%m"))
            if file_info.is_dir():
                continue
            if self.checkDir(date):
                zip.extract(file_info.filename, new_file)


sortet = dirSorter(inputDir='icons', outputDir='icons_by_year')
# sortet.scanFiles()

zipSort = zipSorter(inputDir='icons.zip', outputDir='icons_by_year2')
zipSort.copyFiles()
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
