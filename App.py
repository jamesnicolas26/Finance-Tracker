import tkinter as tk
from tkinter import ttk
import pandas as pd


class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.income_label = tk.Label(self.frame, text="Income")
        self.income_label.grid(row=0, column=0, padx=5, pady=5)
        self.income_entry = tk.Entry(self.frame)
        self.income_entry.grid(row=0, column=1, padx=5, pady=5)

        self.expense_label = tk.Label(self.frame, text="Expense")
        self.expense_label.grid(row=1, column=0, padx=5, pady=5)
        self.expense_entry = tk.Entry(self.frame)
        self.expense_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add", command=self.add_transaction)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.frame, columns=("Type", "Amount"), show='headings')
        self.tree.heading("Type", text="Type")
        self.tree.heading("Amount", text="Amount")
        self.tree.grid(row=3, column=0, columnspan=2)

        self.balance_label = tk.Label(self.frame, text="Balance: $0")
        self.balance_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.transactions = []

    def add_transaction(self):
        income = self.income_entry.get()
        expense = self.expense_entry.get()

        if income:
            self.transactions.append(('Income', float(income)))
            self.tree.insert("", "end", values=("Income", income))
            self.income_entry.delete(0, tk.END)
        if expense:
            self.transactions.append(('Expense', float(expense)))
            self.tree.insert("", "end", values=("Expense", expense))
            self.expense_entry.delete(0, tk.END)

        self.update_balance()

    def update_balance(self):
        balance = sum(amount if type_ == 'Income' else -amount for type_, amount in self.transactions)
        self.balance_label.config(text=f"Balance: ${balance:.2f}")


# Create the main window
root = tk.Tk()
app = FinanceTracker(root)
root.mainloop()
