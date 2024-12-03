import json 

with open("fish.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 

count = 0 
open = True

def menu():
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)


def all():
    global count
    for fish in data:
            print(f"""
            Номер записи: {fish['id']}, 
            Общее название: {fish['name']},                       
            Латинское название: {fish['latin_name']}, 
            Пресноводная: {fish['is_salt_water_fish']},    
            Кол-во подвидов: {fish['sub_type_count']} 
            """)
    count += 1

def index():
    global count
    id = int(input("Введите номер рыбы: "))
    find = False    
    for fish in data:
        if id == fish['id']:
            print(f"""
            Номер записи: {fish['id']}, 
            Общее название: {fish['name']},                       
            Латинское название: {fish['latin_name']}, 
            Пресноводная: {fish['is_salt_water_fish']},    
            Кол-во подвидов: {fish['sub_type_count']} 
            """)
            find = True  
            break  
    count += 1
    if not find:
        print("Запись не найдена.")


def new():
    global count
    id = int(input("Введите номер рыбы: "))    
    exists = False
    for fish in data:
        if fish['id'] == id:
            exists = True
            break
        
    if exists:
        print("Такой номер уже существует.")
    else:
        name = input("Введите название: ")  
        latin_name = input("Введите латинское название: ")  
        is_salt_water_fish = input("Введите, пресноводная ли рыба (да/нет): ")  
        sub_type_count = float(input("Введите кол-во подвидов: "))  

        new_fish = {
            'id': id,
            'name': name,
            'latin_name': latin_name,
            'is_salt_water_fish': True if is_salt_water_fish.lower() == 'да' else False, 
            'sub_type_count': sub_type_count
        }

        data.append(new_fish) 
        with open("fish.json", 'w', encoding='utf-8') as out_file: 
            json.dump(data, out_file)
        print("Машина успешно добавлена.")
    count += 1

def del_id():
    global count
    id = int(input("Введите номер рыбы: "))
    find = False  

    for fish in data:
        if id == fish['id']:
            data.remove(fish)  
            find = True  
            break 

    if not find:
        print("Запись не найдена.")
    else:
        with open("fish.json", 'w', encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print("Запись успешно удалена.")
    count += 1

def exit():
    global count
    global open
    print(f"""Программа завершена.
            Кол-во операций: {count}""")
    open = False
        
def main():
    while open:
        menu()

        num = int(input("Введите номер действия: "))

        if num == 1:
            all()
        elif num == 2:
            index()
        elif num == 3:
            new()
        elif num == 4:
            del_id()
        elif num == 5:
            exit()
        else:
             print("Такого номера нет.")

main()
