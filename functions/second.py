import collections
pets = {}
command = ''

# Вспомогательные методы
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

def get_pet(id):
    if id in pets.keys():
        pet = pets[id]
        name = list(pet.keys())[0]
        pet_data = {
            'pet': pet,
            'name': name,
            'nearList': list(pet[name].values()),
            'nearListKeys': list(pet[name].keys())
        }
        return pet_data
    else:
        return False
    
def get_list():
    for key in pets:
        for k in pets[key]:
            print((
                f"Это {list(pets[key][k].values())[0]} по кличке '{list(pets[key].keys())[0]}'. "
                f"Его возраст {list(pets[key][k].values())[1]} {pluralize(list(pets[key][k].values())[1])}. "
                f"{list(pets[key][k].keys())[2]}: {list(pets[key][k].values())[2]}"))
    global command
    command = ''

# основные методы
def create():
    name = input("Введите имя питомца: ")

    if name:
        if not pets:
            key = 1
        else:
            key = collections.deque(pets)[0] + 1
        
        pets[key] = {}
        pets[key][name] = {}
        pets[key][name]["Вид питомца"] = input("Введите вид питомца: ")
        pets[key][name]["Возраст питомца"] = int(input("Введите возраст питомца: "))
        pets[key][name]["Имя владельца"] = input("Введите имя владельца: ")
    global command
    command = ''

def read(id):
    pet = get_pet(id)
    if pet:
        print(f"Это {pet['nearList'][0]} по кличке '{pet['name']}'. Его возраст {pet['nearList'][1]} {pluralize(pet['nearList'][1])}. {pet['nearListKeys'][2]}: {pet['nearList'][2]}")
    else:
        print("Питомец с таким ID не найден в БД!")
    global command
    command = ''

def update(id):
    if id in pets.keys():
        name = list(pets[id].keys())[0]
        pets[id][name]["Возраст питомца"] = int(input("Введите возраст питомца: "))
        pets[id][name]["Имя владельца"] = input("Введите имя владельца: ")
    
        print(f"Питомец по кличке '{name}' успешно изменен! "
              f"Его возраст {list(pets[id][name].values())[1]} {pluralize(list(pets[id][name].values())[1])}. "
              f"{list(pets[id][name].keys())[2]}: {list(pets[id][name].values())[2]}")
    else:
        print("Питомец с таким ID не найден в БД!")
    # print(pets)
    global command
    command = ''
    
def delete(id):
    if id in pets.keys():
        pet = pets[id]
        name = list(pet.keys())[0]
        del pets[id]
        print(f"Питомец по кличке '{name}' успешно удален!")
    else:
        print("Питомец с таким ID не найден в БД!")
    global command
    command = ''


while command != 'stop':
    if command == 'create':
        create()
    elif command == 'update':
        id = int(input("Введите идентификатор питомца: "))
        update(id)
    elif command == 'read':
        id = int(input("Введите идентификатор питомца: "))
        read(id)
    elif command == 'delete':
        id = int(input("Введите идентификатор питомца: "))
        delete(id)
    elif command == 'list':
        get_list()
    else:
        command = input("Введите команду: ")
        