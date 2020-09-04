import csv

from src.deadlined_reminders import DateReminder


def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()


def add_reminder(text: str, date: str):
    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        reminder = DateReminder(text, date)
        writer.writerow(reminder)
