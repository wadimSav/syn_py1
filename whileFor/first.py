from helpers import *
# Задание №1

# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, 
# и выведите это количество.


N = check_int(input("Введите число: "))
count = 0

while N > 0:
    n = check_int(input("Введите целое число: "))
    if n == 0:
        count += 1
    N = N - 1
    
print(count)