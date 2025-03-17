import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama - даю нашому тексту кольору, щоб було веселіше
init(autoreset=True)

def print_directory_structure(directory, indent="", is_root=True):
    # Перевіряю, чи існує ця директорія і чи вона справжня, а не просто віртуальна
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + f"Помилка: '{directory}' не є директорією або не існує.")
        return
    
    dirs = []  # Сюди складатиму наші каталоги
    files = []  # А ось тут будуть файли
    
    # Перше, що я роблю - збираю всі файли та папки, щоб мати чітке уявлення
    for item in sorted(directory.iterdir()):
        if item.is_dir():
            dirs.append(item)  # Папки йдуть в один список
        else:
            files.append(item)  # Файли - в інший список
    
    # Виводжу першу папку без відступів, бо вона найголовніша
    if is_root:
        print(Fore.GREEN + f"📦{directory.name}")
    
    # Тепер виводжу всі папки, додаючи відступи для кожної
    for item in dirs:
        print(indent + " ┣ 📂" + item.name)
        # Рекурсивно продовжую працювати з цією папкою, занурюючись глибше
        print_directory_structure(item, indent + " ┃ ", is_root=False)
    
    # Ось і файли! Виводжу їх теж з правильними відступами та лініями
    for idx, item in enumerate(files):
        prefix = " ┗ 📜" if idx == len(files) - 1 else " ┣ 📜"  # Ось тут перевіряю, чи останній файл
        print(indent + prefix + item.name)

def main():
    # Вказую шлях до директорії, яку я хочу вивести (це моя точка входу)
    directory_path = Path("/Users/aleksej/projects/goit-pycore-hw-04/task3/test_directory/picture")
    
    # Викликаю функцію, щоб побудувати структуру директорії (крок до мети!)
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()  # І ось я запускаю всю цю красу!
