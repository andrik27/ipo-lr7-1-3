import json

def input_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Пожалуйста, введите целое число от {min_value} до {max_value}.")
            else:
                return value
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

with open("fish.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

count = 0

while True:
    print("""
       1: Вывести все записи
       2: Вывести запись по полю
       3: Добавить запись
       4: Удалить запись по полю
       5: Выйти из программы
    """)

    number = input_int("Введите номер действия: ", 1, 5)

    if number == 1:
        for fish in data:
            print(f"""
            Номер записи: {fish['id']},
            Общее название: {fish['name']},
            Латинское название: {fish['latin_name']},
            Пресноводная: {fish['is_salt_water_fish']},
            Кол-во подвидов: {fish['sub_type_count']}
            """)
        count += 1

    elif number == 2:
        id = input_int("Введите номер рыбы: ")
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

    elif number == 3:
        id = input_int("Введите номер рыбы: ")

        exists = any(fish['id'] == id for fish in data)
        
        if exists:
            print("Такой номер уже существует.")
        else:
            name = input("Введите название: ").strip()
            latin_name = input("Введите латинское название: ").strip()
            is_salt_water_fish = input_yes_no("Введите, пресноводная ли рыба (да/нет): ")
            sub_type_count = input_float("Введите кол-во подвидов: ")

            new_fish = {
                'id': id,
                'name': name,
                'latin_name': latin_name,
                'is_salt_water_fish': is_salt_water_fish == 'да',
                'sub_type_count': sub_type_count
            }

            data.append(new_fish)
            with open("fish.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись успешно добавлена.")
        count += 1

    elif number == 4:
        id = input_int("Введите номер рыбы: ")
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

    elif number == 5:
        print(f"Программа завершена. Кол-во операций: {count}")
        break
    else:
        print("Такого номера нет.")
