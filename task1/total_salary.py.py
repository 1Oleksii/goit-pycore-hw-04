def total_salary(path):
    try:
        print("Йду відкривати файл, бо без нього ніяк не вийде.")  # Відкриваю файл!
        with open(path, encoding='utf-8') as file:
            salaries = []  # Містечко для зарплат!
            
            for line in file:  # Читаю кожен рядок файлу, а ви й не уявляєте, скільки їх там!
                parts = line.strip().split(',')  # О, ось і дані розділені на частини! Потрібно їх ретельно розділити.
                
                if len(parts) == 2:  # Якщо рядок виглядає як зарплата, то працюємо далі.
                    try:
                        salary = int(parts[1])  # А ось і сама зарплата! Перевіряємо чи це число!
                        salaries.append(salary)  # Додаю зарплату в список.
                    except ValueError:
                        print(f"Помилка в рядку: {line.strip()} - некоректна зарплата")  # О, тут сталася помилка! Не число! Що робити?
                        
        if not salaries:  # Якщо зарплат не зібралося, що ж... Ні заробітку, ні радості.
            return 0, 0
        
        total = sum(salaries)  # Ось і підсумок! Сумуємо всі зарплати.
        average = total / len(salaries)  # Середня зарплата - все заради балансу.
        
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")  # Ось і результат! Виводжу!
        return total, average
    
    except FileNotFoundError:  # А якщо файлу немає, то кажу, що його нема!
        print("Файл не знайдено.")
        return None
    except Exception as e:  # О, тут щось сталося! Різнакі помилки – усе на увагу!
        print(f"Помилка: {e}")
        return None

# Приклад використання
path = "/Users/aleksej/projects/goit-pycore-hw-04/task1/salary_file.txt"  # Ось шлях до файлу!
total, average = total_salary(path)  # О, тепер все зібрано в одне! Виводимо результат!
