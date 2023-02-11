# -*- coding: utf-8 -*-
import csv
import os
import random

SOURCE_FILE = '/home/wad/futures_forts_trades_201902201726.csv'
TARGET_PATH = '/home/wad/skillbox/src/python_base_source/lesson_012/trades'


def gel_lines(filename):
    headers = None
    with open(filename, 'r') as ff:
        reader = csv.reader(ff)
        for line in reader:
            if headers is None:
                headers = line
                continue
            yield dict(zip(headers, line))


def jit_value(val, percent=5):
    val = float(val)
    val += val * random.randint(-percent, percent) / 100
    return f'{val:.4f}'


count, out_files = 0, {}

for line in gel_lines(SOURCE_FILE):
    # {'\ufeff"TRADENO"': '2218118027', 'TRADETIMESYS': '2019-01-24 19:05:00',
    # 'TRADEDATE': '2019-01-24', 'TRADETIME': '19:05:00', 'BOARDID': 'RFUD',
    # 'SECID': 'BRG9', 'PRICE': '60.97', 'QUANTITY': '1', 'TRADETIME_GRP': '1905',
    # 'SYSTIME': '2019-01-25 00:02:09', 'PERIOD': 'N', 'SESSIONID': '5712', 'VALUE': '60.97'}
    # print(line)
    secid = line['SECID']
    if secid not in out_files:
        file_name = os.path.join(TARGET_PATH, f'TICKER_{secid}.csv')
        out_file = open(file_name, 'w')
        cvs_writer = csv.writer(out_file)
        cvs_writer.writerow(['SECID', 'TRADETIME', 'PRICE', 'QUANTITY'])
        out_files[secid] = dict(cvs_writer=cvs_writer, out_file=out_file)
        print(f'new file {file_name}')
    else:
        cvs_writer = out_files[secid]['cvs_writer']
    cvs_writer.writerow([
        line['SECID'],
        line['TRADETIME'],
        jit_value(line['PRICE']),
        line['QUANTITY'],
    ])
    count += 1

for _, desc in out_files.items():
    desc['out_file'].close()

print(f'Proceeded {count} lines')
