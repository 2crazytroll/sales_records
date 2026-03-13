from sales import sales_list

def calculate_totals():

    total_money = 0
    total_units = 0

    for sale in sales_list:
        total_money += sale["price"] * sale["quantity"]
        total_units += sale["quantity"]

    print("\n----- TOTALS -----")
    print("Total units sold:", total_units)
    print("Total revenue:", total_money)