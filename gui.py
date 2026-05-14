import tkinter as tk
from tkinter import ttk, messagebox

from expense_manager import (
    initialize_file,
    read_expenses,
    add_expense,
    delete_expense,
    total_spending,
    monthly_report
)

from charts import (
    show_pie_chart,
    show_bar_chart
)


def run_app():

    root = tk.Tk()

    root.title("Expense Tracker")

    root.geometry("1100x700")

    root.configure(bg="#f0f4f7")


    def show_expenses():

        for item in expense_table.get_children():

            expense_table.delete(item)

        expenses = read_expenses()

        for expense in expenses:

            expense_table.insert(
                "",
                tk.END,
                values=(
                    expense["Date"],
                    expense["Amount"],
                    expense["Category"],
                    expense["Description"]
                )
            )


    def add_expense_gui():

        amount = amount_entry.get()

        category = category_entry.get()

        description = description_entry.get()

        if amount == "" or category == "":

            messagebox.showerror(
                "Error",
                "Amount and Category are required"
            )

            return

        try:

            amount = float(amount)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Invalid Amount"
            )

            return

        add_expense(
            amount,
            category,
            description
        )

        amount_entry.delete(0, tk.END)

        category_entry.set("")

        description_entry.delete(0, tk.END)

        show_expenses()

        messagebox.showinfo(
            "Success",
            "Expense Added Successfully!"
        )


    def search_expense():

        keyword = search_entry.get().lower()

        for item in expense_table.get_children():

            expense_table.delete(item)

        expenses = read_expenses()

        for expense in expenses:

            if (
                keyword in expense["Category"].lower()
                or keyword in expense["Description"].lower()
            ):

                expense_table.insert(
                    "",
                    tk.END,
                    values=(
                        expense["Date"],
                        expense["Amount"],
                        expense["Category"],
                        expense["Description"]
                    )
                )


    def delete_expense_gui():

        selected_item = expense_table.selection()

        if not selected_item:

            messagebox.showwarning(
                "Warning",
                "Select an expense first"
            )

            return

        values = expense_table.item(
            selected_item
        )["values"]

        delete_expense(values)

        show_expenses()

        messagebox.showinfo(
            "Success",
            "Expense Deleted"
        )


    def edit_expense():

        selected_item = expense_table.selection()

        if not selected_item:

            messagebox.showwarning(
                "Warning",
                "Select an expense first"
            )

            return

        values = expense_table.item(
            selected_item
        )["values"]

        amount_entry.delete(0, tk.END)
        amount_entry.insert(0, values[1])

        category_entry.set(values[2])

        description_entry.delete(0, tk.END)
        description_entry.insert(0, values[3])

        delete_expense(values)

        show_expenses()


    def show_total():

        total = total_spending()

        messagebox.showinfo(
            "Total Spending",
            f"Total Spending = ₹{total}"
        )


    def show_monthly_report():

        report_data = monthly_report()

        report = ""

        for month, total in report_data.items():

            report += f"{month} : ₹{total}\n"

        if report == "":

            report = "No data found"

        messagebox.showinfo(
            "Monthly Report",
            report
        )


    def pie_chart_gui():

        success = show_pie_chart()

        if not success:

            messagebox.showwarning(
                "Warning",
                "No data found"
            )


    def bar_chart_gui():

        success = show_bar_chart()

        if not success:

            messagebox.showwarning(
                "Warning",
                "No data found"
            )


    title_label = tk.Label(
        root,
        text="Expense Tracker Dashboard",
        font=("Arial", 24, "bold"),
        bg="#f0f4f7",
        fg="#1f2937"
    )

    title_label.pack(pady=20)


    input_frame = tk.Frame(
        root,
        bg="#ffffff",
        bd=2,
        relief=tk.GROOVE
    )

    input_frame.pack(
        padx=20,
        pady=10,
        fill="x"
    )


    tk.Label(
        input_frame,
        text="Amount",
        bg="#ffffff",
        font=("Arial", 12)
    ).grid(row=0, column=0, padx=10, pady=10)

    amount_entry = tk.Entry(
        input_frame,
        font=("Arial", 12)
    )

    amount_entry.grid(row=0, column=1, padx=10)


    tk.Label(
        input_frame,
        text="Category",
        bg="#ffffff",
        font=("Arial", 12)
    ).grid(row=0, column=2, padx=10)

    category_entry = ttk.Combobox(
        input_frame,
        values=[
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Entertainment",
            "Health",
            "Education",
            "Other"
        ],
        state="readonly",
        font=("Arial", 12)
    )

    category_entry.grid(row=0, column=3, padx=10)


    tk.Label(
        input_frame,
        text="Description",
        bg="#ffffff",
        font=("Arial", 12)
    ).grid(row=0, column=4, padx=10)

    description_entry = tk.Entry(
        input_frame,
        font=("Arial", 12),
        width=25
    )

    description_entry.grid(row=0, column=5, padx=10)


    search_frame = tk.Frame(
        root,
        bg="#f0f4f7"
    )

    search_frame.pack(pady=10)


    tk.Label(
        search_frame,
        text="Search:",
        bg="#f0f4f7",
        font=("Arial", 12)
    ).pack(side=tk.LEFT, padx=5)


    search_entry = tk.Entry(
        search_frame,
        font=("Arial", 12),
        width=30
    )

    search_entry.pack(side=tk.LEFT, padx=5)


    button_frame = tk.Frame(
        root,
        bg="#f0f4f7"
    )

    button_frame.pack(pady=15)


    buttons = [

        ("Add Expense", add_expense_gui),

        ("Edit Expense", edit_expense),

        ("Delete Expense", delete_expense_gui),

        ("Search", search_expense),

        ("Show All", show_expenses),

        ("Total Spending", show_total),

        ("Monthly Report", show_monthly_report),

        ("Pie Chart", pie_chart_gui),

        ("Bar Chart", bar_chart_gui)

    ]


    for text, command in buttons:

        tk.Button(
            button_frame,
            text=text,
            command=command,
            font=("Arial", 10, "bold"),
            bg="#2563eb",
            fg="white",
            padx=12,
            pady=8
        ).pack(side=tk.LEFT, padx=5)


    table_frame = tk.Frame(root)

    table_frame.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )


    columns = (
        "Date",
        "Amount",
        "Category",
        "Description"
    )


    expense_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )


    for col in columns:

        expense_table.heading(
            col,
            text=col
        )

        expense_table.column(
            col,
            width=250
        )


    expense_table.pack(
        fill="both",
        expand=True
    )


    initialize_file()

    show_expenses()

    root.mainloop()