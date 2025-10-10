import unittest
from expense_tracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense("Book", 15.99)
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].description, "Book")
        self.assertEqual(self.tracker.expenses[0].amount, 15.99)

    def test_total_expense(self):
        self.tracker.add_expense("Pen", 1.5)
        self.tracker.add_expense("Notebook", 3.0)
        self.assertAlmostEqual(self.tracker.total_expense(), 4.5)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense("Invalid", -10)


if __name__ == "__main__":
    unittest.main()
