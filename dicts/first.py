pets = {}

name = input("Введите имя питомца: ")

if name:
    pets[name] = {}
    pets[name]["Вид питомца"] = input("Введите вид питомца: ")
    pets[name]["Возраст питомца"] = int(input("Введите возраст питомца: "))
    pets[name]["Имя владельца"] = input("Введите имя владельца: ")
    
def pluralize(num):
    words = ['год', 'года', 'лет']
    a1 = [1,21,31] # год
    a2 = [2,3,4,22,23,24,32,33,34] # года
    a3 = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30] # лет
    if num in a1:
        return words[0]
    elif num in a2:
        return words[1]
    else:
        return words[2]

nearList = list(pets[name].values())
nearListKeys = list(pets[name].keys())
    
print(f"Это {nearList[0]} по кличке '{list(pets.keys())[0]}'. Его возраст {nearList[1]} {pluralize(nearList[1])}. {nearListKeys[2]}: {nearList[2]}")
