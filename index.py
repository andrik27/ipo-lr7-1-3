import json 

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def input_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['да', 'нет']:
            return response
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

def input_string(prompt):
    while True:
        response = input(prompt).strip()
        if response.isalpha():
            return response
        else:
            print("Пожалуйста, введите корректное название.")

with open("fish.json", 'r', encoding='utf-8') as file:
    data = json.load(file) 

start = True
count = 0

def menu():
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)

def all_records():
    global count
    print(" Все записи: ".center(60,'~'))
    for fish in data:
        print(f"""
        Номер записи: {fish['id']}, 
        Общее название рыбы: {fish['name']},                       
        Латинское (научное) название рыбы: {fish["latin_name"]}, 
        Рыба пресноводная или нет: {fish['is_salt_water_fish']},    
        Количество подвидов рыбы: {fish['sub_type_count']} 
        """)
    count += 1

def index():
    global count
    id = input_int("Введите номер рыбы (цифрой): ")
        
    find = False
    for fish in data:
        if id == fish['id']:
            print("\n Выбранная запись: ".center(60,' '))
            print(f"""
            Номер записи: {fish['id']},
            Общее название: {fish['name']},
            Латинское (научное) название рыбы: {fish['latin_name']}, 
            Рыба пресноводная или нет: {fish['is_salt_water_fish']},    
            Количество подвидов рыбы: {fish['sub_type_count']} 
            """) 
            find = True
            count += 1
            break
    if not find:
        print("\n"," Запись не найдена ".center(60, "~"))

def new():
    global count
    if data:
        id = max(int(fish['id']) for fish in data) + 1 
    else: 
        id = 1

    new_name = input_string("Введите общее название рыбы: ")  
    new_latin_name = input_string("Введите латинское название рыбы: ")

    while True:
        num = input_int("Введите, является ли пресноводной (1 - да / 2 - нет): ")
        if num == 1 or num == 2:
            new_salt_water_fish = True if num == 1 else False 
            break 
        else:
            print("Введите 1, если рыба пресноводная. Если нет, введите 2.")

    new_sub_type_count = input_float("Введите количество подвидов рыбы (числом): ")

    new_fish = {
        'id': id,
        'name': new_name,
        'latin_name': new_latin_name,
        'is_salt_water_fish': new_salt_water_fish, 
        'sub_type_count': new_sub_type_count
    }

    data.append(new_fish)
    with open("fish.json", 'w', encoding='utf-8') as out_file:
        json.dump(data, out_file)
    print("Рыба успешно добавлена.")
    count += 1

def del_id():
    global count
    id = input_int("Введите номер записи для удаления: ")

    find = False  
    for fish in data:
        if id == fish['id']:
            data.remove(fish) # Удаление 
            find = True  
            break

    if not find:
        print("Запись не найдена.")
    else:
        with open("fish.json", 'w', encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print("Запись успешно удалена.".center(60, '=')) 
    count += 1

def exit_program():
    global start
    print(f"Программа завершена. Количество операций: {count}")
    start = False
        
def main():
    while start:
        menu()
        num = input_int("Введите номер действия: ")
        if num == 1:
            all_records()
        elif num == 2:
            index()
        elif num == 3:
            new()
        elif num == 4:
            del_id()
        elif num == 5:
            exit_program()
        else:
            print("Такого номера нет.")

main()
