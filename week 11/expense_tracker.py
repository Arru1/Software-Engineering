class Expense:
    def __init__(self, description: str, amount: float):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: ${self.amount:.2f}"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description: str, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.expenses.append(Expense(description, amount))

    def total_expense(self) -> float:
        return sum(exp.amount for exp in self.expenses)

    def list_expenses(self):
        return [str(exp) for exp in self.expenses]



if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 3.5)
    tracker.add_expense("Lunch", 12.0)
    print("Expenses:")
    for e in tracker.list_expenses():
        print(" -", e)
    print(f"Total: ${tracker.total_expense():.2f}")
