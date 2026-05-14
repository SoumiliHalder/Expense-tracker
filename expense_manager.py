import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Amount",
                "Category",
                "Description"
            ])


def read_expenses():

    initialize_file()

    expenses = []

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            expenses.append(row)

    return expenses


def add_expense(amount, category, description):

    initialize_file()

    current_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            current_date,
            amount,
            category,
            description
        ])


def delete_expense(values):

    expenses = read_expenses()

    updated_expenses = []

    for expense in expenses:

        if not (
            expense["Date"] == str(values[0])
            and expense["Amount"] == str(values[1])
            and expense["Category"] == str(values[2])
            and expense["Description"] == str(values[3])
        ):

            updated_expenses.append(expense)

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = [
            "Date",
            "Amount",
            "Category",
            "Description"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(updated_expenses)


def total_spending():

    expenses = read_expenses()

    total = 0

    for expense in expenses:

        try:

            total += float(expense["Amount"])

        except:

            pass

    return total


def get_category_data():

    expenses = read_expenses()

    categories = {}

    for expense in expenses:

        try:

            category = expense["Category"]

            amount = float(expense["Amount"])

            categories[category] = (
                categories.get(category, 0)
                + amount
            )

        except:

            pass

    return categories


def monthly_report():

    expenses = read_expenses()

    monthly_total = {}

    for expense in expenses:

        try:

            month = expense["Date"][:7]

            amount = float(expense["Amount"])

            monthly_total[month] = (
                monthly_total.get(month, 0)
                + amount
            )

        except:

            pass

    return monthly_total