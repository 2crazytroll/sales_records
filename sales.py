ventas = []

def registrar_venta():

    producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad vendida: "))

    venta = {
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad
    }

    ventas.append(venta)

    print("Venta registrada correctamente")
    
