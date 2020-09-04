from src.database import add_reminder, list_reminders
from src.deadlined_reminders import DateReminder
from src.external_reminders import EveningReminder


def handle_input():
    choice = input("Choice: ")
    if choice == "4":
        return False

    if choice == "1":
        list_reminders()

    elif choice in {'2', '3'}:
        print()
        reminder = input("What would you like to be reminded about?: ")
        date = input('When is that due?')
        reminder_class = DateReminder if choice == '2' else EveningReminder

        add_reminder(reminder, date, reminder_class)
        list_reminders()
    else:
        print("Invalid menu option")

    return True


def print_menu():
    print()
    print('|--------------|')
    print('|  Pluralsight |')
    print('|   Reminders  |')
    print('|     App      |')
    print('|--------------|')
    print('* * * * * * * * *')
    print('Please select an option:')
    print()
    print('1) List reminders')
    print('2) Add a reminder')
    print('3) Add an evening reminder')
    print('4) Exit')


def main():
    print_menu()
    while handle_input():
        print_menu()


if __name__ == '__main__':
    main()
