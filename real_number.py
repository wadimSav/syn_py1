# Задание №2

# Дано пятизначное целое число. Напишите алгоритм, который возведёт количество десятков в степень 
# количества единиц. Затем умножит это число на количество сотен. И делит получившееся число на 
# разность количества десятков тысяч и количества тысяч

# Например, есть число 46275

# Необходимо возвести 7 (десятки) в степень 5 (единицы), умножить получившееся число на 2 (сотни), 
# и разделить на разность между 4 (десятки тысяч) и 6 (тысячи) то есть (4-6)

# В результате необходимо получить вещественное число. В нашем примере это будет: -16807.0

n = 46275

res = [int(digit) for digit in str(n)]

a = res[3] ** res[4]
b = a * res[2]
c = b / (res[0] - res[1])

print(c)