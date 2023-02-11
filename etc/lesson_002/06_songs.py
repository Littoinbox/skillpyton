#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

pocket_universe_songs = {
    'Solar Driftwood': '1:51',
    'Celsius': '5:59',
    'More': '6:39',
    'On Track': '5:33',
    'Monolith': '6:21',
    'To the Sea': '5:46',
    'Magnetic': '5:53',
    'Liquid Mountain': '2:58',
    'Pan Blue': '5:31',
    'Resistor': '7:13',
    'Beyond Mirrors': '5:49',
}


def song_time(with_seconds):
    minutes, seconds = with_seconds.split(':')
    return int(minutes) + round(int(seconds) / 60.0, 2)


pocket_universe_songs_fractions = {k: song_time(v) for k, v in pocket_universe_songs.items()}

pprint(pocket_universe_songs_fractions)
