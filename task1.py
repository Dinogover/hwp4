# Вычислить число c заданной точностью d
from decimal import Decimal

num = input('Введите число: ')
d = input('Введите точноть: ')

numAfter = Decimal(num)
numAfter = numAfter.quantize(Decimal(d))
print(num)
print(numAfter)