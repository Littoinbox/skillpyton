# -*- coding: utf-8 -*-
from random import randint

import datetime
import os
import time
import shutil


SRC = 'icons'
now = datetime.datetime.now()
BASE_DIR = os.path.dirname(__file__)

for dirpath, dirnames, filenames in os.walk(SRC):
    for file in filenames:
        path = os.path.join(BASE_DIR, dirpath, file)
        rand_time = now - datetime.timedelta(days=randint(1, 365))
        rand_time = rand_time.timestamp()
        print(path)
        try:
            os.utime(path=path, times=(rand_time, rand_time))
        except OSError as exc:
            print('Не получилось', exc)
