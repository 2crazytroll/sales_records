from sales import sales_list

def show_summary():

    if len(sales_list) == 0:
        print("No sales registered")
        return

    print("\n----- SALES SUMMARY -----")

    for sale in sales_list:
        print(
            "Product:", sale["product"],
            "| Price:", sale["price"],
            "| Quantity:", sale["quantity"]
        )