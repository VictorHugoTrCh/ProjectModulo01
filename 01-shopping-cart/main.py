import os
from datetime import datetime

FILE_NAME = 'ventas.txt'

WAREHOUSE = [

    {
        "code":"A001",
        "name":"Pan",
        "price":1.5
    },
    
    {
        "code":"A002",
        "name":"Leche",
        "price":3.8
    }
]

# Código: A001 | Producto: Pan | Precio: S/1.50
# Código: B203 | Producto: Leche | Precio: S/3.80

SHOPPING_CART = []


def show_menu():
    print('''
    1. Ver catálogo
    2. Agregar producto al carrito
    3. Eliminar producto del carrito
    4. Vaciar carrito
    5. Mostrar carrito
    6. Finalizar compra
    7. Salir
    ''')

def show_catalog():
    print(f"Código  |  Producto  |  Precio")
    for product in WAREHOUSE:
        print(f" {product["code"]} | {product["name"]}{" "*(10-len(product["name"]))} | {product["price"]}")


def add_product_to_shopping_car(code_product):
    for product in WAREHOUSE:
        if code_product == product["code"]:
            SHOPPING_CART.append(product)
            print(f"✔ El Producto {product["code"]} fue agregado al carrito.")
            break


def remove_product_to_shopping_car(code_product):
    for i, product in enumerate(SHOPPING_CART):
        if code_product == product["code"]:
            SHOPPING_CART.pop(i)
            print(f"✔ El Producto {product["code"]} fue eliminado al carrito.")
            break


def clear_to_shopping_car():
    SHOPPING_CART.clear()
    print("El carrito ha sido limpiado")


def show_cart():
    if not SHOPPING_CART:
        print("El carrito es vacio")
        return
    else:
        print("\nPRODUCTOS EN EL CARRITO:")
        print("Cantidad | Código | Producto | Precio | Subtotal")
        total = 0
        for product in SHOPPING_CART:
            subtotal = product["price"] * product["quantity"]
            total += subtotal
            print(f"{product['quantity']} | {product['code']} | {product['name']}{' '*(10-len(product['name']))} | S/{product['price']:.2f} | S/{subtotal:.2f}")

def checkout():
    if not SHOPPING_CART:
        print("El carrito es vacio")
        return
    else:
        total = sum(item['price'] * item['quantity'] for item in SHOPPING_CART)
        registerd_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        add_order_to_file(registerd_at, SHOPPING_CART,total)
        print(f"✔ Compra finalizada. Total: S/{total:.2f}")
        clear_to_shopping_car()




show_menu()
# show_catalog()
# os.system("clear")
add_product_to_shopping_car("A002")
remove_product_to_shopping_car("A002")
clear_to_shopping_car()
show_cart()
checkout()


def add_order_to_file(registerd_at, list_products, total_price):
    complete_order = "=============================\n\n"
    complete_order += f"Fecha: {registerd_at}\n\n"
    
    for prod in list_products:
        complete_order += f"{prod['quantity']}  |  {prod['name']}  |  S/{prod['price']:.2f}  |  S/{prod['price'] * prod['quantity']:.2f}\n"



    complete_order += f"S/. {total_price}\n\n"
    complete_order += "=============================\n"


    with open(FILE_NAME,'a') as archivo:
        archivo.write(complete_order)


add_order_to_file(
    "20-04-2025 10:56:50",
    [{
        "quantity": 1,
        "code":"A001",
        "name":"Pan",
        "price":1.5
    },
    {
        "quantity": 1,
        "code":"A002",
        "name":"Leche",
        "price":2.5
    }],
    4.0
    )