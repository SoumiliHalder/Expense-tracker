import matplotlib.pyplot as plt

from expense_manager import get_category_data


def show_pie_chart():

    categories = get_category_data()

    if len(categories) == 0:

        return False

    plt.figure(figsize=(7, 7))

    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense Distribution")

    plt.show()

    return True


def show_bar_chart():

    categories = get_category_data()

    if len(categories) == 0:

        return False

    plt.figure(figsize=(8, 5))

    plt.bar(
        list(categories.keys()),
        list(categories.values())
    )

    plt.xlabel("Categories")

    plt.ylabel("Amount")

    plt.title("Category-wise Expenses")

    plt.show()

    return True