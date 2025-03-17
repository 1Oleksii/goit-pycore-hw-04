def get_cats_info(path):
    cats_info = []  # Створюю порожній список для зберігання котячих даних, бо ж котики не можуть самі себе заносити в базу!

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяю рядок на елементи, ніби котиків на частини, щоб вони стали розбірливіше
                cat_data = line.strip().split(',')  

                # Перевіряю, чи всі частинки на місці — якщо котик без хвоста, то не візьму
                if len(cat_data) == 3:
                    # Створюю словник з котячими даними, ідентифікую котика на основі його ID, імені та віку
                    cat_dict = {
                        'id': cat_data[0],  # ID котика — це його паспорт!
                        'name': cat_data[1],  # ім'я котика — його гордість!
                        'age': cat_data[2]  # Вік котика — не завжди можна вгадати!
                    }
                    # Додаю цей словник до списку, бо котики повинні бути разом
                    cats_info.append(cat_dict)  
                else:
                    print(f"Невірний формат рядка: {line}")  # Якщо щось пішло не так, кричу про це, як котик, що зіпсував килим!

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")  # Якщо файлу немає, тоді котик точно не прийде

    except Exception as e:
        print(f"Сталася помилка: {e}")  # Ой, сталося щось незрозуміле, таке інколи трапляється з котиками!

    return cats_info  # Повертаю список з котами, бо вони це заслужили!

# Якщо це головний файл, то запускаю все і дивлюсь на результат
if __name__ == "__main__":
    cats_info = get_cats_info("/Users/aleksej/projects/goit-pycore-hw-04/task2/cats_file.txt")  # Нагадую, що потрібно передати шлях до файлу
    print(cats_info)  # Показую котиків у всій красі
