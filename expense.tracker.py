# Daily Expense Tracker
# This program allows the user to add, view, and manage daily expenses.

# Welcome message
print("Welcome to the Daily Expense Tracker!")

# Display the menu options
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

# This list will store all expenses entered by the user
expenselst = []

# Main program loop
while True:
    choice = input("Enter your choice (1-5): ")  # Ask the user for menu choice

    # Option 1: Add a new expense
    if choice == "1":
        exp = float(input("Enter the expense amount: "))  # Get expense as a number
        expenselst.append(exp)  # Add to the list
        print('Expense added successfully!')

    # Option 2: View all expenses
    elif choice == "2":
        if expenselst == []:  # If list is empty
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenselst)):
                print(f"{i + 1}. {expenselst[i]}")  # Show expense number and amount

    # Option 3: Calculate total and average
    elif choice == "3":
        if expenselst == []:
            print("No expenses recorded yet.")
        else:
            total = 0
            for exp in expenselst:
                total += exp  # Add up expenses
            average = total / len(expenselst)  # Calculate average
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")

    # Option 4: Clear all expenses
    elif choice == "4":
        expenselst.clear()  # Remove all items from list
        print("All expenses cleared.")

    # Option 5: Exit the program
    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break  # End the loop, stop program

    # Invalid option handling
    else:
        print("Invalid choice. Please try again.")
