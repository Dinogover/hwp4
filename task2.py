# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input('Введите число: '))
count = 2
list = []
while True: 
    if num % count == 0:
        list.append(count)
        num /= count 
        count = 2
    elif num == 1: break 
    else: count += 1
print("Число простое" if len(list) == 1 else (list))
