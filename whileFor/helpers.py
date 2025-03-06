def check_int(a):
    try:
        return int(a)
    except (ValueError, TypeError):
        print("Ошибка: Вы ввели некорректное число")
        exit()
