from random import randrange

number = ""


def create_number():
    number = ""
    while (len(number) < 4):
        i = str(randrange(0, 9))
        if (len(number) == 0 and i == "0"):
            continue
        if i in number:
            continue
        else:
            number += i
    return number


def validate_input(str):
    for i in range(len(str)):
        if (i == 0 and str[i] == "0"):
            return False
        if (str[i].count(str)>1):
            return False
    return True


def check_input(str):
    bulls = 0
    cows = 0
    for i in range(len(str)):
        if (str[i] == number[i]):
            bulls += 1
        elif (str[i] in number):
            cows += 1
    return {'bulls': bulls, 'cows': cows}
