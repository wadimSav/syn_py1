from helpers import *
# Задание №2

# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число).
# x ≤ 2e9 (2 миллиарда)

X = 0
count = 0
while X < 1:
    X = check_int(input("Введите натуральное число: "))

num = X

while num > 0:
    if num == X or num == 1 or X % num == 0:
        count += 1
    num = num - 1
    
print(count)