# sale records
from sales import register_sale
from summary import show_summary
from totals import calculate_totals

list= []
option = ""

while option != "4":

    print("\n===== SALES SYSTEM =====")
    print("1. Register sale")
    print("2. Show sales summary")
    print("3. Show totals")
    print("4. Exit")

    option = input("Select an option: ")

    if option == "1":
        valor=register_sale()
        list.append(valor)

    elif option == "2":
        show_summary(list)

    elif option == "3":
        calculate_totals(list)

    elif option == "4":
        print("Program finished")

    else:
        print("Invalid option")