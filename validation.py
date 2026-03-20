# validation.py
# Este archivo valida los datos del usuario

def get_valid_data_str():
    nikolas = True
    while nikolas:
        # Nombre (solo letras)
        name = input("Enter product name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Please enter the product name correctly (only letters).")
            continue

        # Precio (solo números)
        price_input = input("Enter product price: ").strip()
        if not price_input.replace(".", "", 1).isdigit():
            print("Please enter a valid price (numbers only).")
            continue
        price = float(price_input)

        # Cantidad (solo enteros)
        quantity_input = input("Enter quantity: ").strip()
        if not quantity_input.isdigit():
            print("Please enter a valid quantity (integer numbers only).")
            continue
        quantity = int(quantity_input)

        # Si todo está bien
        total = price * quantity

def get_valid_data_int(int):
    nikola = True
    while nikola:
        # Precio (solo números)
        if not int.replace(".", "", 1).isdigit():
            print("Please enter a valid price (numbers only).")
            continue
        price = float(price_input)

        # Cantidad (solo enteros)
        quantity_input = input("Enter quantity: ").strip()
        if not quantity_input.isdigit():
            print("Please enter a valid quantity (integer numbers only).")
            continue
        quantity = int(quantity_input)

        # Si todo está bien
        total = price * quantity
        return name, price, quantity, total