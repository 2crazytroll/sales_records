def show_summary(list):

    if  list == "":
        print("No sales registered")
        return

    print("\n----- SALES SUMMARY -----")

    for sale in list:
        print(
            f"Product: { sale["name"]}\n"
            f"Price: {sale["price"]}\n"
            f"Quantity: {sale["quantity"]}\n"
        )