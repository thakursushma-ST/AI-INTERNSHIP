from expense_manager import *
from file_handler import load_expenses, save_expenses


def menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Save Data")
    print("6. Exit")


def main():
    expenses = load_expenses()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            total_spending(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Saved!")
        elif choice == "6":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()