_init_.py 

Welcome.py
import os
from admin import admin_mode
from user import user_mode

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    print("*" * 55)
    print("" + " " * 15 + "WELCOME TO OUR INFIRMARY" + " " * 15 + "")
    print("*" * 55)

def main_menu():
    while True:
        clear_screen()
        display_welcome()
        print("\n1. Admin Mode")
        print("2. User Mode")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            admin_mode()
        elif choice == "2":
            user_mode()
        elif choice == "3":
            print("\n👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid input. Please enter 1, 2, or 3.")
            input("Press Enter to try again...")

if _name_ == "_main_":
    main_menu()

admin.py
def admin_mode():
    def patient_management():
        def display_menu():
            print("Press 1. Add new patient")
            print("      2. Edit patient information")
            print("      3. Display all patients")
            print("      4. Delete a patient")
            print("      5. Exit")

        def add_patient():
            with open("patients.txt", "a") as file:
                name = input("Enter name: ")
                dob = input("Enter date of birth (DDMMYYYY): ")
                age = input("Enter age: ")
                gender = input("Enter gender: ")
                condition = input("Enter condition: ")
                file.write(f"{name},{dob},{age},{gender},{condition}\n")
                print(" Patient added.")

        def edit_patient():
            with open("patients.txt", "r") as file:
                patients = file.readlines()
            for i, p in enumerate(patients):
                print(f"{i+1}. {p.strip()}")
            i = int(input("Enter index to edit: ")) - 1
            new = [
                input("New name: "),
                input("New DOB: "),
                input("New age: "),
                input("New gender: "),
                input("New condition: ")
            ]
            patients[i] = ",".join(new) + "\n"
            with open("patients.txt", "w") as file:
                file.writelines(patients)
            print("✅ Patient updated.")

        def display_patients():
            print("Patient Information:")
            print("-" * 30)
            with open("patients.txt", "r") as file:
                for line in file:
                    name, dob, age, gender, condition = line.strip().split(",")
                    print(f"Name: {name}, DOB: {dob}, Age: {age}, Gender: {gender}, Condition: {condition}")
            print("-" * 30)

        def delete_patient():
            with open("patients.txt", "r") as file:
                patients = file.readlines()
            for i, p in enumerate(patients):
                print(f"{i+1}. {p.strip()}")
            i = int(input("Enter index to delete: ")) - 1
            deleted = patients.pop(i)
            with open("patients.txt", "w") as file:
                file.writelines(patients)
            print(f"🗑 Deleted: {deleted.strip()}")

        while True:
            display_menu()
            ch = input("Enter your choice: ")
            if ch == "1": add_patient()
            elif ch == "2": edit_patient()
            elif ch == "3": display_patients()
            elif ch == "4": delete_patient()
            elif ch == "5": break
            else: print("❌ Invalid choice.")
            print("*" * 40)

    def doctor_management():
        def display_menu():
            print("Press 1. Add new doctor")
            print("      2. Display all doctors")
            print("      3. Exit")

        def add_doctor():
            with open("doctors.txt", "a") as file:
                name = input("Doctor name: ")
                age = input("Age: ")
                spl = input("Specialization: ")
                file.write(f"{name},{age},{spl}\n")
                print("✅ Doctor added.")

        def display_doctors():
            print("Doctor Information:")
            print("-" * 30)
            with open("doctors.txt", "r") as file:
                for line in file:
                    name, age, spl = line.strip().split(",")
                    print(f"Name: {name}, Age: {age}, Specialisation: {spl}")
            print("-" * 30)

        while True:
            display_menu()
            ch = input("Enter your choice: ")
            if ch == "1": add_doctor()
            elif ch == "2": display_doctors()
            elif ch == "3": break
            else: print("❌ Invalid choice.")

    def medicines_records():
        def display_menu():
            print("1. Add new medicine")
            print("2. Edit medicine")
            print("3. Display all")
            print("4. Update price")
            print("5. Update stocks")
            print("6. Exit")

        def add_medicine():
            with open("medicines.txt", "a") as file:
                name = input("Name: ")
                price = input("Price: ")
                stocks = input("Stocks: ")
                file.write(f"{name},{price},{stocks}\n")
                print("✅ Medicine added.")

        def edit_medicine():
            with open("medicines.txt", "r") as file:
                meds = file.readlines()
            for i, med in enumerate(meds):
                print(f"{i+1}. {med.strip()}")
            i = int(input("Index to edit: ")) - 1
            name = input("New name: ")
            price = input("New price: ")
            stock = input("New stock: ")
            meds[i] = f"{name},{price},{stock}\n"
            with open("medicines.txt", "w") as file:
                file.writelines(meds)
            print("✅ Updated.")

        def display_all():
            print("Medicine Information:")
            print("-" * 30)
            with open("medicines.txt", "r") as file:
                for line in file:
                    name, price, stocks = line.strip().split(",")
                    print(f"Name: {name}, Price: {price}, Stocks: {stocks}")
            print("-" * 30)

        def update_price():
            name = input("Medicine name: ")
            new_price = input("New price: ")
            updated = False
            with open("medicines.txt", "r") as file:
                meds = file.readlines()
            with open("medicines.txt", "w") as file:
                for line in meds:
                    med = line.strip().split(",")
                    if med[0] == name:
                        file.write(f"{med[0]},{new_price},{med[2]}\n")
                        updated = True
                    else:
                        file.write(line)
            print("✅ Price updated." if updated else "❌ Not found.")

        def update_stocks():
            name = input("Medicine name: ")
            new_stock = input("New stocks: ")
            updated = False
            with open("medicines.txt", "r") as file:
                meds = file.readlines()
            with open("medicines.txt", "w") as file:
                for line in meds:
                    med = line.strip().split(",")
                    if med[0] == name:
                        file.write(f"{med[0]},{med[1]},{new_stock}\n")
                        updated = True
                    else:
                        file.write(line)
            print("✅ Stocks updated." if updated else "❌ Not found.")

        while True:
            display_menu()
            ch = input("Enter your choice: ")
            if ch == "1": add_medicine()
            elif ch == "2": edit_medicine()
            elif ch == "3": display_all()
            elif ch == "4": update_price()
            elif ch == "5": update_stocks()
            elif ch == "6": break
            else: print("❌ Invalid choice.")

    while True:
        print("*" * 40)
        print("Press 1 to manage patients")
        print("      2 to manage doctors")
        print("      3 to manage medicines")
        print("      4 to exit")
        ch = input("Enter your choice: ")
        if ch == "1": patient_management()
        elif ch == "2": doctor_management()
        elif ch == "3": medicines_records()
        elif ch == "4": break
        else: print("❌ Invalid input.")

def admin_mode():
    print("✅ Admin mode is now active.")
    input("Press Enter to exit admin mode...")

user.py
def user_mode():
    def login():
        name = input("Enter your name: ")
        dob = input("Enter your password (DD/MM/YYYY): ")
        login_successful = False
        with open("patients.txt", "r") as file:
            for line in file:
                details = line.strip().split(",")
                if details[0] == name and details[1] == dob:
                    print("✅ Login successful!")
                    login_successful = True
                    break
        if not login_successful:
            print("❌ Invalid credentials.")
        return name, dob, login_successful

    def signup():
        with open("patients.txt", "a") as file:
            name = input("Enter your name: ")
            dob = input("Enter your DOB (DDMMYYYY): ")
            age = input("Enter age: ")
            gender = input("Enter gender (M/F/O): ")
            condition = input("Enter condition: ")
            file.write(f"{name},{dob},{age},{gender},{condition}\n")
            print("✅ Account created successfully.")

    def show_user_profile(name, dob):
        with open("patients.txt", "r") as file:
            for line in file:
                details = line.strip().split(",")
                if details[0] == name and details[1] == dob:
                    print("\n👤 User Profile:")
                    print("Name:", details[0])
                    print("Date of Birth:", details[1])
                    print("Age:", details[2])
                    print("Gender:", details[3])
                    print("Condition:", details[4])
                    return
        print("❌ Profile not found.")

    def bill():
        def display_medicines():
            print("\n📦 Available Medicines:")
            with open("medicines.txt", "r") as file:
                print("-" * 40)
                for line in file:
                    name, price, stocks = line.strip().split(",")
                    print(f"Name: {name}, Price: {price}, Stocks: {stocks}")
                print("-" * 40)

        def generate_bill(items):
            total = sum(item[2] for item in items)
            print("\n🧾 Bill Summary:")
            print("-" * 40)
            print("Name\tQty\tPrice")
            for item in items:
                print(f"{item[0]}\t{item[1]}\t{item[2]}")
            print("Total Amount:", total)
            print("-" * 40)

        items = []
        while True:
            display_medicines()
            name = input("Enter medicine name (or 'done'): ").capitalize()
            if name.lower() == "done":
                break
            try:
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("❌ Invalid quantity.")
                continue

            found = False
            with open("medicines.txt", "r") as file:
                for line in file:
                    med_name, price, stocks = line.strip().split(",")
                    if med_name == name:
                        if qty <= int(stocks):
                            items.append((med_name, qty, float(price) * qty))
                            print(f"✅ {med_name} added to bill.")
                            found = True
                        else:
                            print("⚠ Insufficient stock.")
                        break
            if not found:
                print("❌ Medicine not found.")
            cont = input("Add more? (yes/no): ")
            if cont.lower() != "yes":
                break

        if items:
            generate_bill(items)
        else:
            print("🛒 No items in the bill.")

    # Start user mode interaction
    while True:
        print("\n1. Log in")
        print("2. Sign up")
        print("3. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            name, dob, success = login()
            if success:
                while True:
                    print("\nWhat would you like to do?")
                    print("1. Show Profile")
                    print("2. Order Medicines")
                    print("3. Logout")
                    ch2 = input("Enter your choice: ")
                    if ch2 == "1":
                        show_user_profile(name, dob)
                    elif ch2 == "2":
                        bill()
                    elif ch2 == "3":
                        print("🚪 Logging out...")
                        break
                    else:
                        print("❌ Invalid option.")
        elif ch == "2":
            signup()
        elif ch == "3":
            print("👋 Exiting user mode.")
            break
        else:
            print("❌ Invalid input.")

def user_mode():
    print("✅ User mode is now active.")
    input("Press Enter to exit user mode...")
