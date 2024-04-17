#DAVID LUBWAMA
#101416908
#Lab Professor: Reza

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []  # List to store employee data
        self.items = []      # List to store item data

    # Main menu function to display options
    def main_menu(self):
        print("-" * 30)
        print("|  1. Create Employee        |")
        print("|  2. Create Item            |")
        print("|  3. Make Purchase          |")
        print("|  4. All Employee Summary   |")
        print("|  5. Exit                   |")
        print("-" * 30)

    # Function to create employee
    def create_employee(self):
        while True:
            # Input for Employee ID
            while True:
                try:
                    employee_id = int(input("Enter employee ID (numeric): "))
                    if any(employee_id == emp[0] for emp in self.employees):
                        print("This Employee ID already exists. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Employee ID must be numeric.")

            # Input for Employee Name
            employee_name = input("Enter employee name: ").strip()
            if not employee_name:
                print("Employee name cannot be empty.")
                continue

            # Input for Employee Type
            while True:
                employee_type = input("Enter employee type ('hourly' or 'manager'): ").lower()
                if employee_type in ['hourly', 'manager']:
                    break
                else:
                    print("Invalid employee type. Type must be 'hourly' or 'manager'.")

            # Input for Years Worked
            while True:
                try:
                    years_worked = int(input("Enter years worked: "))
                    break
                except ValueError:
                    print("Invalid input. Years worked must be numeric.")

            # Employee Discount Number
            while True:
                try:
                    employee_discount_number = int(input("Enter employee discount number (numeric): "))
                    if any(employee_discount_number == emp[6] for emp in self.employees):
                        print("This Employee Discount Number already exists. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Employee Discount Number must be numeric.")

            # Append employee data to the list
            self.employees.append([employee_id, employee_name, employee_type, years_worked, 0, 0, employee_discount_number])

            # Check if the user wants to add another employee
            add_another = input("Do you want to add another employee? (YES/NO): ").strip().lower()
            if add_another == 'no':
                break

    # Function to create item
    def create_item(self):
        while True:
            # Input for Item Number
            while True:
                try:
                    item_number = int(input("Enter item number (numeric): "))
                    if any(item_number == item[0] for item in self.items):
                        print("This Item Number already exists. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Item Number must be numeric.")

            # Input for Item Name
            item_name = input("Enter item name: ").strip()
            if not item_name:
                print("Item name cannot be empty.")
                continue

            # Input for Item Cost
            while True:
                try:
                    item_cost = float(input("Enter item cost: "))
                    break
                except ValueError:
                    print("Invalid input. Item Cost must be numeric.")

            # Append item data to the list
            self.items.append([item_number, item_name, item_cost])

            # Check if the user wants to add another item
            add_another = input("Do you want to add another item? (YES/NO): ").strip().lower()
            if add_another == 'no':
                break

    # Function to make a purchase
    def make_purchase(self):
        # Display item list
        print("Item Number, Item Name, Item Cost")
        for item in self.items:
            print(f"{item[0]}, {item[1]}, ${item[2]:.2f}")

        while True:
            try:
                item_number = int(input("Enter item number for purchase: "))
                item = next((itm for itm in self.items if itm[0] == item_number), None)
                if not item:
                    print("Item not found. Please try again.")
                    continue

                employee_discount_number = int(input("Enter your employee discount number: "))
                employee = next((emp for emp in self.employees if emp[6] == employee_discount_number), None)
                if not employee:
                    print("Employee discount number not found. Please try again.")
                    continue

                discount_percentage = min(employee[3] * 2, 30)  # Years Worked * 2, max 30%
                if employee[2].lower() == 'manager':
                    discount_percentage += 10  # Additional discount for managers
                discount_amount = item[2] * discount_percentage / 100
                final_price = item[2] - discount_amount

                # Update employee's purchase details
                employee[4] += final_price
                employee[5] += discount_amount

                print(f"Purchase successful. Final price: {final_price:.2f}")

                another_purchase = input("Another purchase? (YES/NO): ").strip().lower()
                if another_purchase == 'no':
                    break
            except ValueError:
                print("Invalid input. Please enter numeric values for item numbers and discount numbers.")

    # Function to display all employee summary
    def all_employee_summary(self):
        print("All Employee Summary:")
        for emp in self.employees:
            print(f"Employee ID: {emp[0]}, Name: {emp[1]}, Role: {emp[2]}, Years Worked: {emp[3]}")
            print(f"Total Purchased: {emp[4]:.2f}, Total Discounts: {emp[5]:.2f}, Discount Number: {emp[6]}")
            print("-" * 20)

    # Function to run the program
    def run_program(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.create_employee()
            elif choice == "2":
                self.create_item()
            elif choice == "3":
                self.make_purchase()
            elif choice == "4":
                self.all_employee_summary()
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice, please enter a number between 1-5.")

if __name__ == "__main__":
    emp_sys = EmployeeManagementSystem()
    emp_sys.run_program()
