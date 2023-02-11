# -*- coding: utf-8 -*-

from random import choice
from pprint import pprint

bank = 'йцукенгшщзхфывапролдячсмитьб123456789'

phrase = 'в бане веник дороже денег'
phrase = phrase.split()

MESSAGE_LEN = 32


def rndmsg(n):
    return ''.join([choice(bank) for _ in range(n)])


word_0 = phrase[0]
word_1 = phrase[1]
word_2 = ''.join([c + choice(bank) for c in phrase[2]])
word_3 = phrase[3][::-1]
word_4 = phrase[4][::-1]
print(word_0, word_1, word_2, word_3, word_4)

starts = [3, 9, 5, 7, 16]

print(f"""
ключ к расшифровке:
  первое слово - {starts[0]+1}-я буква
  второе слово - буквы с {starts[1]+1} по {starts[1] + len(phrase[1])}, включительно
  третье слово - буквы с {starts[2]+1} по {starts[2] + len(word_2)}, включительно, через одну
  четвертое слово - буквы с {starts[3]+1} по {starts[3] + len(word_3)}, включительно, в обратном порядке
  пятое слово - буквы с {starts[4]+1} по {starts[4] + len(word_4)}, включительно, в обратном порядке
""")

secret_message = [
    rndmsg(starts[0]) + word_0 + rndmsg(MESSAGE_LEN - starts[0] - len(word_0)),
    rndmsg(starts[1]) + word_1 + rndmsg(MESSAGE_LEN - starts[1] - len(word_1)),
    rndmsg(starts[2]) + word_2 + rndmsg(MESSAGE_LEN - starts[2] - len(word_2)),
    rndmsg(starts[3]) + word_3 + rndmsg(MESSAGE_LEN - starts[3] - len(word_3)),
    rndmsg(starts[4]) + word_4 + rndmsg(MESSAGE_LEN - starts[4] - len(word_4)),
]

# secret_message = [
# 'квевтфпп6щ3стмзалтнмаршгб5длгуча',
# 'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
# 'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
# 'ьд5фму3ежородт9г686буиимыкучшсал',
# 'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
# ]

mess_0, mess_1, mess_2, mess_3, mess_4 = secret_message

print(len(mess_0), mess_0[3])
print(len(mess_1), mess_1[9:13])
print(len(mess_2), mess_2[5:15], mess_2[5:15:2])
print(len(mess_3), mess_3[7:13], mess_3[12:6:-1], mess_3[7:13][::-1])
print(len(mess_3), mess_3[-25:-19], mess_3[-20:-26:-1])
print(len(mess_4), mess_4[16:21], mess_4[20:15:-1], mess_4[16:21][::-1])
print(len(mess_4), mess_4[-16:-11], mess_4[-12:-17:-1])

print()
print("[\n\t'" + "',\n\t'".join(secret_message) + "',\n]")
