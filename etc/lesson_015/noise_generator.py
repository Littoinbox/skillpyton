from random import choice
import random
import json
import pprint

bank = 'йцукенгшщзхфывапролдячсмитьб012345678901234567890123456789'


def rndmsg(n):
    return ''.join([choice(bank) for _ in range(n)])


date1 = '010119'
date2 = '010219'
date3 = '010319'
date4 = '010419'

city1 = 'берлин'
city2 = 'лондон'
city3 = 'москва'
city4 = 'токио'

keyd = 'jbd'
keyc = 'jbc'
keye = 'jbe'

MESSAGE_LEN = 700

len_of_period = [209, 222, 170, 100, 200]
cities_and_dates = [(city1, 1.13, date1), (city2, 1.26, date2), (city3, 0.015747, date3), (city4, 0.009259, date4)]


def encryption(date, city, money, intervals):
    secret_message = [
        rndmsg(intervals[0]) + keyd + date + rndmsg(intervals[1]) + keyc + city + keyc
        + rndmsg(intervals[2]) + keye + money + keye + rndmsg(
            MESSAGE_LEN - intervals[0] - intervals[1]
            - intervals[2] - len(date) - len(city) - len(money) - len(keyd) * 5,
        ),
    ]
    return secret_message


exchange_rates = [1.26, 1.13, 0.009259, 0.015747]
secret_data = {}
msg_number = 0
for town, ex_r, months in cities_and_dates:
    for days in range(int(months), int(months) + 90001, 10000):
        expenses = str(random.randint(10000, 90000) / ex_r)
        day = '0' + str(days) if len(str(days)) == 5 else str(days)
        period = [random.choice(len_of_period), random.choice(len_of_period), random.choice(len_of_period)]
        msg_number += 1
        print(day, town)
        secret_data['message' + str(msg_number)] = encryption(day, town, expenses, period)[0]

with open('Bond.json', 'w') as write_file:
    json.dump(secret_data, write_file)
