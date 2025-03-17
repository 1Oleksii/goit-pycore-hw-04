def parse_input(user_input):
    # Роблю магію з рядком — обрізаю зайві пробіли!
    user_input = user_input.strip()
    if not user_input:  # Якщо нічого не ввели — так і скажу!
        return None, []
    # Розбираю команду на слова, перше слово — це команда, решта — аргументи.
    cmd, *args = user_input.split()
    cmd = cmd.lower()  # Перетворюю команду на нижній регістр, бо я поважаю порядок!
    return cmd, args

# Тут зберігаю контакти, наче у власному телефончику 📱
contacts = {}

def add_contact(args):
    # Перевіряю, чи правильно ввели дані (а то люблять вводити все підряд!)
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    name, phone = args
    # Додаю контакт до словника! Тепер він тут навічно! 😈
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args):
    # Перевіряю, чи все правильно написали, бо я люблю порядок!
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new_phone]"
    name, phone = args
    # Оновлюю номер, якщо контакт є, а якщо нема — сварюся! 😡
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    return f"Contact {name} not found."

def show_phone(args):
    # Перевіряю, чи запросили телефон для конкретного друга!
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
    name = args[0]
    # Якщо контакт є — радісно показую! 🎉 Якщо нема — розчарування 😢
    return contacts.get(name, f"Contact {name} not found.")

def show_all():
    # Якщо контактів нема — кажу, що у вас порожнеча, як у холодильнику після свята! 🥶
    if not contacts:
        return "Empty contact list."
    # Виводжу всі контакти, бо ділитися інформацією — це моє покликання!
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def show_help():
    # Виводжу список команд, щоб ніхто не загубився у цьому лабіринті можливостей! 🤓 
    # У завданні цього не було, але я вирішив трохи покращити — ну, щоб було веселіше! 😜
    return (
        "Available commands:\n"
        "  add [name] [phone] - Add a new contact\n"
        "  change [name] [new_phone] - Update an existing contact\n"
        "  phone [name] - Show phone number for the contact\n"
        "  all - Show all contacts\n"
        "  help - Show this help message\n"
        "  close, exit - Exit the program"
    )

def main():
    print("Welcome to the assistant bot! 😊")  # Привітання, бо я ввічливий бот!
    while True:
        user_input = input("Enter a command: ").strip()  # Чекаю команду від користувача
        command, args = parse_input(user_input)

        if command is None:
            print("Invalid command. Please enter a valid command.")  # Ну як так можна? 😡
            continue

        if command in ["close", "exit"]:
            print("Good bye! 👋")  # До зустрічі, я буду сумувати! 😢
            break
        elif command == "hello":
            print("How can I help you? Час зробити ваш день кращим! 🚀")  # Піднімаю настрій!
        elif command == "add":
            print(add_contact(args))  # Додаю контакт, щоб не забути важливих людей!
        elif command == "change":
            print(change_contact(args))  # Міняю номер, бо друзі люблять змінювати сімки!
        elif command == "phone":
            print(show_phone(args))  # Даю номер, але тільки якщо він є!
        elif command == "all":
            print(show_all())  # Ділюся всіма контактами, наче телефонна книга!
        elif command == "help":
            print(show_help())  # Пояснюю, що тут і як працює!
        else:
            print("Invalid command. Type 'help' to see the available commands.")  # Хмм, що це було? 🤔

if __name__ == "__main__":
    main()  # Запускаю головний цикл програми, бо хто ж іще це зробить?! 💪
