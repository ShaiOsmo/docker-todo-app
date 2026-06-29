import json
import os
from datetime import date, datetime

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, "data", "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        tasks = json.load(file)

    return tasks


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def get_valid_date():
    while True:

        due_date = input("תאריך יעד (YYYY-MM-DD): ")

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return due_date

        except ValueError:
            print("\n❌ פורמט תאריך לא תקין.")
            print("יש להקליד בפורמט הבא:")
            print("2026-07-29\n")

def show_tasks():
    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nאין משימות.")
        return

    print("=" * 100)
    print(f'{"ID":>3} | {"סטטוס":^3} | {"שם המשימה":<25} | {"עדיפות":<12} | {"סוג":<12} | {"תאריך יעד"}')
    print("=" * 100)

    for task in tasks:

        status = "✅" if task["done"] else "❌"

        # עדיפות
        if task["priority"] == 1:
            priority = "🟢 נמוכה"
        elif task["priority"] == 2:
            priority = "🟡 בינונית"
        else:
            priority = "🔴 גבוהה"

        # סוג המשימה
        recurring_type = task.get("recurring", "none")

        if recurring_type == "daily":
            recurring = "🔁 יומית"

        elif recurring_type == "weekly":
            recurring = "📅 שבועית"

        elif recurring_type == "monthly":
            recurring = "🗓 חודשית"

        else:
            recurring = "   חד-פעמית"
        print(
            f'{task["id"]:<5} '
            f'{status:<8} '
            f'{task["task"]:<25} '
            f'{priority:<12} '
            f'{recurring:<15} '
            f'{task["due_date"]:<15}'
        )
    print("=" * 110)

def add_task():

    tasks = load_tasks()

    task_name = input("\nשם המשימה: ")
    description = input("תיאור: ")

    while True:

        print("\nבחר עדיפות:")
        print("1. נמוכה")
        print("2. בינונית")
        print("3. גבוהה")

        try:

            priority = int(input("בחירה: "))

            if priority in [1, 2, 3]:
                break

            print("❌ יש לבחור מספר בין 1 ל-3.")

        except ValueError:

            print("❌ יש להכניס מספר בלבד.")


    while True:

        print("\nסוג המשימה:")
        print("1. חד פעמית")
        print("2. יומית")
        print("3. שבועית")
        print("4. חודשית")

        recurring_choice = input("בחירה: ")

        recurring_types = {
            "1": "none",
            "2": "daily",
            "3": "weekly",
            "4": "monthly"
        }
        due_date = get_valid_date()
        if recurring_choice in recurring_types:
            recurring = recurring_types[recurring_choice]
            break

        print("❌ בחירה לא חוקית.")

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "task": task_name,
        "description": description,
        "priority": priority,
        "created_at": str(date.today()),
        "due_date": due_date,
        "recurring": recurring,
        "done": False
    }

    tasks.append(new_task)

    save_tasks(tasks)

    print("\n✅ המשימה נוספה בהצלחה!")


def complete_task():

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nאין משימות.")
        return

    show_tasks()

    try:
        task_id = int(input("\nהכנס את מספר המשימה שהושלמה: "))

    except ValueError:
        print("❌ יש להכניס מספר.")
        return

    for task in tasks:

        if task["id"] == task_id:

            if task["done"]:
                print("\n⚠ המשימה כבר הושלמה.")
                return

            task["done"] = True

            save_tasks(tasks)

            print("\n✅ המשימה סומנה כהושלמה!")

            return

    print("\n❌ לא נמצאה משימה עם המספר הזה.")


def delete_task():

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nאין משימות.")
        return

    show_tasks()

    try:
        task_id = int(input("\nהכנס את מספר המשימה למחיקה: "))

    except ValueError:
        print("❌ יש להכניס מספר.")
        return

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            print("\n✅ המשימה נמחקה!")

            return

    print("\n❌ לא נמצאה משימה עם המספר הזה.")

def edit_task():

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nאין משימות.")
        return

    show_tasks()

    try:
        task_id = int(input("\nהכנס את מספר המשימה לעריכה: "))

    except ValueError:
        print("❌ יש להכניס מספר.")
        return

    for task in tasks:

        if task["id"] == task_id:

            print("\nלחץ ENTER כדי להשאיר את הערך הקיים.\n")

            new_name = input(f'שם ({task["task"]}): ')
            if new_name != "":
                task["task"] = new_name

            new_description = input(f'תיאור ({task["description"]}): ')
            if new_description != "":
                task["description"] = new_description

            while True:

                print(f'\nעדיפות נוכחית: {task["priority"]}')
                print("1. נמוכה")
                print("2. בינונית")
                print("3. גבוהה")
                print("ENTER - ללא שינוי")

                priority_input = input("בחירה: ")

                if priority_input == "":
                    break

                try:
                    priority = int(priority_input)

                    if priority in [1, 2, 3]:
                        task["priority"] = priority
                        break

                    print("❌ יש לבחור בין 1 ל-3.")

                except ValueError:
                    print("❌ יש להכניס מספר.")

            new_due_date = input(f'תאריך יעד ({task["due_date"]}): ')
            if new_due_date != "":
                task["due_date"] = new_due_date

            save_tasks(tasks)

            print("\n✅ המשימה עודכנה!")

            return

    print("\n❌ לא נמצאה משימה.")
def show_statistics():

    tasks = load_tasks()

    total = len(tasks)

    completed = 0
    open_tasks = 0

    low = 0
    medium = 0
    high = 0

    for task in tasks:

        if task["done"]:
            completed += 1
        else:
            open_tasks += 1

        if task["priority"] == 1:
            low += 1

        elif task["priority"] == 2:
            medium += 1

        else:
            high += 1

    if total == 0:
        percentage = 0
    else:
        percentage = round(completed / total * 100, 1)

    print("\n==============================")
    print("        DASHBOARD")
    print("==============================")
    print(f"📋 סך הכל משימות: {total}")
    print(f"✅ הושלמו: {completed}")
    print(f"⏳ פתוחות: {open_tasks}")
    print(f"🔴 עדיפות גבוהה: {high}")
    print(f"🟡 עדיפות בינונית: {medium}")
    print(f"🟢 עדיפות נמוכה: {low}")
    print(f"📈 אחוז השלמה: {percentage}%")



def main():

    while True:

        print("\n==============================")
        print("        TO DO LIST")
        print("==============================")
        print("1. הצג משימות")
        print("2. הוסף משימה")
        print("3. סמן משימה כהושלמה")
        print("4. מחק משימה")
        print("5. ערוך משימה")
        print("6. סטטיסטיקות")
        print("7. יציאה")

        choice = input("\nבחר אפשרות: ")

        if choice == "1":
            show_tasks()

        elif choice == "2":
            add_task()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            edit_task()

        elif choice == "6":
            show_statistics()

        elif choice == "7":
            print("\n👋 להתראות!")
            break

        else:
            print("\n❌ בחירה לא חוקית.")


if __name__ == "__main__":
    main()