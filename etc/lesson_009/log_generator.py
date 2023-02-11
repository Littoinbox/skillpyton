import datetime
import os
from pprint import pprint
from random import randint, choice


cdate = datetime.datetime.now()
with open('events.txt', 'w') as ff:
    for _ in range(10000):
        cdate = cdate + datetime.timedelta(seconds=randint(1, 45))
        nok = 'OK' if randint(1, 2) % 2 else 'NOK'
        ff.write(f'[{cdate}] {nok}\n')


# [2018-04-11 03:13:57] ОК
# [2018-04-11 03:14:04] OK
# [2018-04-11 03:14:04] NOK
# [2018-04-11 03:14:09] OK
