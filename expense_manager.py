from datetime import datetime
from utils import validate_amount, validate_category
from constants import CATEGORIES


def add_expense(expenses):
    title = input("Enter title: ")
    amount = validate_amount(input("Enter amount: "))
    if amount is None:
        return

    print("Categories:", CATEGORIES)
    category = input("Enter category: ")

    if not validate_category(category, CATEGORIES):
        return

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    print("✅ Expense added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses.")
        return

    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['title']} - ₹{e['amount']} - {e['category']} - {e['date']}")


def delete_expense(expenses):
    view_expenses(expenses)
    try:
        i = int(input("Enter index to delete: ")) - 1
        removed = expenses.pop(i)
        print("Deleted:", removed["title"])
    except:
        print("❌ Invalid index")


def total_spending(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"💰 Total Spending: ₹{total}")