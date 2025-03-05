q1 = "australopithecus"
q2 = "homo habilis"
q3 = "homo erectus"
q4 = "homo sapiens"
q5 = "homo sapiens sapiens"
correctanswer = 0;


print("Введите свое имя")
name = input()
print("Первый вопрос:")
print("1 этап эволюции называется:")

a1 = input().lower()
if a1 == q1:
    print("Правильно")
    correctanswer += 1
else:
    print("Неправильный ответ.")
    
print("Второй вопрос: 2 этап эволюции называется:")
a2 = input().lower()
if a2 == q2:
    print("Правильно")
    correctanswer += 1
else:
    print("Неправильный ответ.")
    
print("Третий вопрос вопрос: 3 этап эволюции называется:")
a3 = input().lower()
if a3 == q3:
    print("Правильно")
    correctanswer += 1
else:
    print("Неправильный ответ.")
   
print("Четвертый вопрос вопрос: 4 этап эволюции называется:")
a4 = input().lower()
if a4 == q4:
    print("Правильно")
    correctanswer += 1
else:
    print("Неправильный ответ.")
    
print("Пятый вопрос вопрос: 5 этап эволюции называется:")
a5 = input().lower()
if a5 == q5:
    print("Правильно")
    correctanswer += 1
else:
    print("Неправильный ответ.")
    
    
print("Правильный порядок выглядит вот так: ")
print(q1,q2,q3,q4,q5, sep=" => ")
print("Твои ответы:")
print(a1,a2,a3,a4,a5, sep=" => ")
print("Ты ответил на ", correctanswer, "из 5 вопросов правильно")
print("Ответы для пользователя ", name.upper()," записаны")