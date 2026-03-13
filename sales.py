sales_list = []

def register_sale():

    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter quantity sold: "))

    sale = {
        "product": product_name,
        "price": product_price,
        "quantity": product_quantity
    }

    sales_list.append(sale)

    print("Sale registered successfully")
    
