
def calculate_totals(list):

    total_money = 0
    total_units = 0
    for sale in list:
        total_money += sale["total"] 
        total_units += sale["quantity"]

    print("\n----- TOTALS -----\n"
          "Total units sold:", total_units)
    print("Total revenue:", total_money)

    