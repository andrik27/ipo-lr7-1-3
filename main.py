import json # Подключение библиотеки

with open("fish.json", 'r', encoding='utf-8') as file:  
    data = json.load(file) # Считываем из файла

count = 0 # Для подсчёта выполненных операций

while True:
    print("""
       1: Вывести все записи 
       2: Вывести запись по полю 
       3: Добавить запись 
       4: Удалить запись по полю 
       5: Выйти из программы
    """)

    while True:
        numb = input("Введите номер действия: ")
        if numb.isdigit():
            numb = int(numb)
            break
        else: 
            print("Введите число!(цифрой)")


    if numb == 1: # Выводим все записи

        print(" Все записи: ".center(60,'~'))
        for fish in data:
            print(f"""
            Номер записи: {fish['id']}, 
            Общее название рыбы: {fish['name']},                       
            Латинское (научное) название рыбы:{fish["latin_name"]}, 
            Рыба пресноводная или нет: {fish['is_salt_water_fish']},    
            Количество подвидов рыбы: {fish['sub_type_count']} 
            """)

        count += 1

    elif numb == 2: # Выводим определенную запись

        while True:
            id = input("Введите номер записи: ")
            if id.isdigit():
                id = int(id)
                break
            else: 
                print("Введите номер рыбы (цифрой)")
        
        find = False
        for fish in data:
            if id == fish['id']:
                print("")
                print(f"""
                Номер записи: {fish['id']},
                Общее название: {fish['name']},
                Латинское (научное) название рыбы: {fish['latin_name']}, 
                Рыба пресноводная или нет: {fish['is_salt_water_fish']},    
                Количество подвидов рыбы: {fish['sub_type_count']} 
                """)
                find = True
                break

        count += 1

        if not find: 
            print(" Запись не найдена ".center(60, "~"))


    elif numb == 3: # Добавление новой записи

        while True:
            id = input("Введите номер рыбы: ")
            if id.isdigit():
                id = int(id)
                break
            else: 
                print("Введите номер рыбы (цифрой)")

        find = False
        for fish in data:
            if fish['id'] == id:
                find = True
                break
        
        if find: 
            print("Такой номер уже существует.")
        else:
            new_name = input("Введите общее название рыбы: ")  
            new_latin_name = input("Введите латинское название рыбы: ")  

            while True:
                numb = input("Введите, является ли пресноводной (1 - да / 2 - нет): ")
                if numb.isdigit():
                    numb = int(numb)
                    if numb == 1:
                        new_salt_water_fish = 'да'
                        break
                    elif numb == 2:
                        new_salt_water_fish = 'нет'
                        break

                else :
                    print("Вы должны ввести число (1 - является пресноводной, 2 - не является)")
                
            while True:
                new_sub_type_count = input("Введите количество подвидов рыбы(числом): ")
                if new_sub_type_count.isdigit():
                    new_sub_type_count = int(new_sub_type_count)
                    break
                else: 
                    print("Введите количество видов рыбы числом")
           

            new_fish = {
                'id': id,
                'name': new_name,
                'latin_name': new_latin_name,
                'is_salt_water_fish': True if new_salt_water_fish.lower() == 'да' else False, 
                'sub_type_count': new_sub_type_count
            }

            data.append(new_fish) 
            with open("fish.json", 'w', encoding = 'utf-8') as out_file: 
                json.dump(data, out_file)
            print("Рыба успешно добавлена.")

        count += 1
    elif numb == 4: # Удаляем запись
            id = int(input("Введите номер записи для удаления: "))
            find = False  

            for fish in data:
                if id == fish['id']:
                    data.remove(fish) # Удаление 
                    find = True  
                    break 

            if not find:
                print("Запись не найдена.")
            else:
                with open("fish.json", 'w', encoding = 'utf-8') as out_file:
                    json.dump(data, out_file)
                print("Запись успешно удалена.")

            count += 1

    elif numb == 5: # Завершаем программу
        print(f"""Программа завершена.
        Кол-во операций: {count}""") 
        break


    else:
        print("Число должно быть от 1 до 5")
