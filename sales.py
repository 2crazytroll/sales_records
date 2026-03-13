sales_list = []

def register_sale():
    
    #name validation
    val1=1
    while val1 ==1 :
        product_name = str(input("Enter product name: "))
        if not product_name.isalpha():
                print("ERROR: ")
                continue

        val1 +=2    

    #price validation
    product_price = float(input("Enter product price: "))

    #quantity validetion
    product_quantity = int(input("Enter quantity sold: "))



    sale = {
        "product": product_name,
        "price": product_price,
        "quantity": product_quantity
    }

    sales_list.append(sale)

    print("Sale registered successfully")


