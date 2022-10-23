# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
num = int(input("Введите число: "))
list = []
def randomNum(): return random.randint(0,100)

for i in range(num, 2, -1):
    f = randomNum()
    if f == 0: break
    else: list.append(f"{f}x^{i}")

y = randomNum()
if y == 0 or y == 1: list.append(f"x")
else: list.append(f"{y}x")

z = randomNum()
if z == 0: list.append(" ")
else: list.append(f"{z}")
2
line = '+ '.join(list) + ' = 0'

with open('polinomOne.txt', 'w') as file:
    file.write(line + '/n')

print(line)

