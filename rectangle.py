# Задание №1

# Пользователь вводит стороны прямоугольника, выведите его площадь и периметр. 
# На вход программе могут подаваться как целые числа, так и вещественные

print("Введите ширину и длину прямоугольника:")

def try_type(l):
    try:
        return float(l)
    except (ValueError, TypeError):
        print("Ошибка: Вы ввели некорректное число")
        exit()
            
def checkLen(d):
    if len(d) == 2:
        return d
    else:
        print("Ошибка: Неверное количество чисел")
        exit()


a, b = map(try_type, checkLen(input().split()))
square = a * b
perimeter = (a + b) * 2
print("Площадь прямоугольника равна: ", square)
print("Периметр прямоугольника равен: ", perimeter)