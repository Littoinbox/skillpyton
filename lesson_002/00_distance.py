#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

# Не забываем удалять тудушки!
moscow_to_london = math.sqrt(((sites['Moscow'][0]-sites['London'][0])**2) + ((sites['Moscow'][1] - sites['London'][1])**2))
moscow_to_paris = math.sqrt(((sites['Moscow'][0]-sites['Paris'][0])**2) + ((sites['Moscow'][1] - sites['Paris'][1])**2))
london_to_paris = math.sqrt(((sites['London'][0]-sites['Paris'][0])**2) + ((sites['London'][1] - sites['Paris'][1])**2))

distances = {
    'Moscow': {'London': moscow_to_london,
               "Paris": moscow_to_paris
               },

    'London': {'Moscow': moscow_to_london,
               'Paris': london_to_paris
               },
    'Paris': {
            'Moscow':moscow_to_paris,
            'London':london_to_paris
    }
}



print(distances)

# зачет!



