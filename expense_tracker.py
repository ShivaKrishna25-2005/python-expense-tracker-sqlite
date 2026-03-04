import sqlite3

class ExpenseTracker:

    def __init__(self):
        try:
            self.conn = sqlite3.connect("expenses.db")
            self.cursor = self.conn.cursor()
            self.create_table()
            print("Database connected successfully.")
        except sqlite3.Error as e:
            print("Connection error:", e)

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print("Table creation error:", e)

    # ➤ Add Expense
    def add_expense(self, amount, category, date):
        try:
            self.cursor.execute(
                "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
                (amount, category, date)
            )
            self.conn.commit()
            print("Expense added successfully!")
        except sqlite3.Error as e:
            print("Error adding expense:", e)

    # ➤ View All Expenses
    def view_expenses(self):
        try:
            self.cursor.execute("SELECT * FROM expenses")
            records = self.cursor.fetchall()

            if records:
                print("\nAll Expenses:")
                for row in records:
                    print(row)
            else:
                print("No expenses found.")
        except sqlite3.Error as e:
            print("Error fetching expenses:", e)

    # ➤ View Total Spent
    def view_total(self):
        try:
            self.cursor.execute("SELECT SUM(amount) FROM expenses")
            total = self.cursor.fetchone()[0]

            print("Total Spent:", total if total else 0)
        except sqlite3.Error as e:
            print("Error calculating total:", e)

    # ➤ Filter by Category
    def filter_by_category(self, category):
        try:
            self.cursor.execute(
                "SELECT * FROM expenses WHERE category = ?",
                (category,)
            )
            records = self.cursor.fetchall()

            if records:
                print(f"\nExpenses in category '{category}':")
                for row in records:
                    print(row)
            else:
                print("No expenses found in this category.")
        except sqlite3.Error as e:
            print("Error filtering expenses:", e)

    # ➤ Delete Expense
    def delete_expense(self, expense_id):
        try:
            self.cursor.execute(
                "DELETE FROM expenses WHERE id = ?",
                (expense_id,)
            )
            self.conn.commit()

            if self.cursor.rowcount == 0:
                print("Expense ID not found.")
            else:
                print("Expense deleted successfully!")
        except sqlite3.Error as e:
            print("Error deleting expense:", e)

    # ➤ Close connection safely
    def close(self):
        self.conn.close()
        print("Database connection closed.")


# 🟢 Menu System
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                date = input("Enter date (YYYY-MM-DD): ")
                tracker.add_expense(amount, category, date)

            elif choice == "2":
                tracker.view_expenses()

            elif choice == "3":
                tracker.view_total()

            elif choice == "4":
                category = input("Enter category: ")
                tracker.filter_by_category(category)

            elif choice == "5":
                expense_id = int(input("Enter expense ID to delete: "))
                tracker.delete_expense(expense_id)

            elif choice == "6":
                tracker.close()
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter correct data type.")


if __name__ == "__main__":
    main()