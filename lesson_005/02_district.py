# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.soviet_street.house1.room1 as r1, district.soviet_street.house1.room2 as r2
import district.soviet_street.house2.room1 as r3, district.soviet_street.house2.room2 as r4
import district.central_street.house1.room1 as r5, district.central_street.house1.room1 as r6
import district.central_street.house2.room1 as r7, district.central_street.house2.room2 as r8

print("На районе живут:", ", ".join(r1.folks), ", ", ", ".join(r2.folks), ", ", ", ".join(r3.folks), ", ",
      ", ".join(r4.folks), ", ", ", ".join(r5.folks), ", ", ", ".join(r6.folks), ", ", ", ".join(r7.folks), ", ",
      ", ".join(r8.folks))
