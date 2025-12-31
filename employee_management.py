# Employee Management System - Step 1
import csv

employees = []
def load_employees():
    try:
        with open("employees.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "age": int(row["age"]),
                    "department": row["department"],
                    "salary": float(row["salary"])
                })
    except FileNotFoundError:
        pass
def save_employees():
    with open("employees.csv", "w", newline="") as file:
        fieldnames = ["id", "name", "age", "department", "salary"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for emp in employees:
            writer.writerow(emp)


def add_employee():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "department": dept,
        "salary": salary
    }

    employees.append(employee)
    print("Employee added successfully")


def view_employees():
    if not employees:
        print("No employees found")
        return

    print("\nEmployee List:")
    for emp in employees:
        print(emp)


def search_employee():
    if not employees:
        print("No employees available to search")
        return

    search_id = int(input("Enter Employee ID to search: "))
    for emp in employees:
        if emp["id"] == search_id:
            print("\nEmployee Found:")
            print(emp)
            return

    print("Employee not found")


def update_employee():
    if not employees:
        print("No employees available to update")
        return

    update_id = int(input("Enter Employee ID to update: "))

    for emp in employees:
        if emp["id"] == update_id:
            print("Employee found. Enter new details:")

            emp["name"] = input("Enter New Name: ")
            emp["age"] = int(input("Enter New Age: "))
            emp["department"] = input("Enter New Department: ")
            emp["salary"] = float(input("Enter New Salary: "))

            print("Employee updated successfully")
            return
    print("Employee not found")
    

    
        
    
def delete_employee():
    if not employees:
        print("No employees available to delete")
        return

    delete_id = int(input("Enter Employee ID to delete: "))

    for emp in employees:
        if emp["id"] == delete_id:
            employees.remove(emp)
            print("Employee deleted successfully")
            return

    print("Employee not found")

load_employees()


# MENU MUST BE LAST
while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        save_employees()
        print(" Data saved. Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
