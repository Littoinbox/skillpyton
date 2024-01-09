# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.n = n
        self.data = get_prime_numbers(self.n)
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if (self.i <= len(self.data)):
            #map(is_lucky_number, self.data[self.i - 1])
            #map(is_palindrom_number, self.data[self.i - 1])
            return self.data[self.i - 1]
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
for number in prime_number_iterator:
   print(number)


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            yield number
            prime_numbers.append(number)

for number in prime_numbers_generator(n=10000):
    print(number)


def is_lucky_number(num):
    number_str = str(num)
    if len(number_str) % 2 == 1:
        middle_index = len(number_str) // 2
        first_half = number_str[:middle_index]
        second_half = number_str[middle_index + 1:]
    else:
        middle_index = len(number_str) // 2
        first_half = number_str[:middle_index]
        second_half = number_str[middle_index:]
    first_half_sum = sum(int(digit) for digit in first_half)
    second_half_sum = sum(int(digit) for digit in second_half)
    if first_half_sum == second_half_sum:
        print('Lucky number true')
        return True
    else:
        return False


def is_palindrom_number(num):
    number_str = str(num)
    if len(number_str) % 2 == 1:
        middle_index = len(number_str) // 2
        first_half = number_str[:middle_index]
        second_half = "".join(reversed(number_str[middle_index + 1:]))
    else:
        middle_index = len(number_str) // 2
        first_half = number_str[:middle_index]
        second_half = "".join(reversed(number_str[middle_index:]))
    if (first_half == second_half):
        print("Palindron number true")
        return True
    else:
        return False

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
