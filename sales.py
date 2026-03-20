from validation import get_valid_data_str
from validation import get_valid_data_int
# sales.py
# Este archivo maneja el registro de ventas

def register_sale():
    """
    Solicita al usuario los datos de una venta
    y devuelve un diccionario con la información.
    """
    #name validation
    i = True
    while i:
        name = input("Enter product name: ").strip()
        if not name.isalpha():
            print ("Symbols and Numbers are not allowed")
            continue
    i = False

    #price validation
    while True:
        try:
            # Request user data
            price = float(input("Enter product price: "))
            if price <=0:
                print ("ERROR: Enter a valid value")
                continue

            break

        except ValueError:
            print ("Enter a valid value")
            continue

    #quantity validation
    while True:
        try:
            # Request user data

            quantity = int (input("Enter product quantity: "))
            if quantity <=0:
                print ("ERROR: Enter a valid value")
                continue
            break
        except ValueError:
            print ("Enter a valid value")
            continue
        
    total = price * quantity

    sale = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total
    }

    return sale