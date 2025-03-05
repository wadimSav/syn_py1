# Задание №2

# Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? 
# Гласными называют буквы «a», «e», «i», «o», «u».

# Для решения задачи создайте переменную и в неё положите слово с помощью input()

# А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - 
# Выведите False

vowels = 0
consonants = 0

def find_duplicate_chars(input_string):
    char_count = {}
    duplicates = []
    duplicate_count = []

    for char in input_string:
        if char.isalpha():
            if char in 'aeiou':
                global vowels
                vowels += 1
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            else:
                global consonants
                consonants += 1
                    
    for char in 'aeiou':
        if char not in input_string:
            duplicates.append(char)
            duplicate_count.append(False)

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
            duplicate_count.append(count)
                    
    return [duplicates, duplicate_count]

word = input("Введите строку: ").lower()
result = find_duplicate_chars(word)

if result:
    for index, value in zip(result[0], result[1]): 
        print(f"Повторяющиеся символы в строке '{index}': {value}")
    print(f"Гласных всего => {vowels}")
    print(f"Соласных всего => {consonants}")
else:
    print("Нет повторяющихся символов в строке.")