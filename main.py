 # sale records
from sales import register_sale
from summary import show_summary
from totals import calculate_totals

option = ""

while option != "4":

    print("\n===== SALES SYSTEM =====")
    print("1. Register sale")
    print("2. Show sales summary")
    print("3. Show totals")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":
        register_sale()

    elif option == "2":
        show_summary()

    elif option == "3":
        calculate_totals()

    elif option == "4":
        print("Program finished")

    else:
        print("Invalid option")