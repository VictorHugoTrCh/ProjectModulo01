import os
from datetime import datetime
from typing import List, Dict, Any

FILE_NAME = 'ventas.txt'

WAREHOUSE  = [

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

SHOPPING_CART  = []


def show_menu() -> None:
    print('''

    Bienvenido a la tienda virtual 🛍️
    ¿Qué deseas hacer?

    1. Ver catálogo
    2. Agregar producto al carrito
    3. Eliminar producto del carrito
    4. Vaciar carrito
    5. Mostrar carrito
    6. Finalizar compra
    7. Salir
    ''')

def show_catalog() -> None:
    try:
        print(f"Código | Producto   | Precio")
        for product in WAREHOUSE:
            print(f"{product["code"]:<6} | {product["name"]:<10} | {product["price"]:<6}")
    except Exception as e:
        print("Error al mostrar catálogo: {e}")

def add_product_to_shopping_cart(code_product: str,quantity_product: int) -> None:

    try:
        quantity = int(quantity_product)
        if quantity <= 0:
            print("La Cantidad debe ser un número positivo")
            return
    except ValueError:
        print("La cantidad debe ser un número válido")
        return

    try:
        for product in WAREHOUSE:
            if code_product == product["code"]:

                for cart_item in SHOPPING_CART:
                    if cart_item["code"] == code_product:
                        cart_item["quantity"] += quantity
                        print(f"✔ Se agregó otra unidad de {product['name']} al carrito.")
                        return
                
                cart_item = product.copy()
                cart_item["quantity"] = quantity
                SHOPPING_CART.append(cart_item)
                return print(f"✔ El Producto {product["code"]} fue agregado al carrito.")
        print(f"El código {code_product} no existe en el catálogo.")
    except Exception as e:
        print("Error al agregar producto: {e}")


def remove_product_to_shopping_cart(code_product: str) -> None:
    try:
        for i, product in enumerate(SHOPPING_CART):
            if code_product == product["code"]:
                SHOPPING_CART.pop(i)
                print(f"✔ El Producto {product["code"]} fue eliminado al carrito.")
                return
        print(f"El producto con código {code_product} no está en el carrito.")
    except Exception as e:
        print("Error al eliminar producto {e}")


def clear_cart() -> None:
    try:
        SHOPPING_CART.clear()
        print("El carrito ha sido limpiado")
    except Exception as e:
        print("Error al vaciar el carrito {e}")


def show_cart() -> str:
    try:
        if not SHOPPING_CART:
            return print("El carrito es vacio")
            
        else:
            print("\nPRODUCTOS EN EL CARRITO:")
            print("Cantidad | Código | Producto | Precio | Subtotal")
            total = 0
            for product in SHOPPING_CART:
                subtotal = product["price"] * product["quantity"]
                total += subtotal
                print(f"{product['quantity']} | {product['code']} | {product['name']}{' '*(10-len(product['name']))} | S/{product['price']:.2f} | S/{subtotal:.2f}")
            print(f"\nTotal: S/.{total:.2f}")
    except Exception as e:
        print("Error al mostrar el carrito {e}")

def checkout() -> None:
    try:
        if not SHOPPING_CART:
            print("El carrito es vacio")
            return
        else:
            total = sum(item['price'] * item['quantity'] for item in SHOPPING_CART)
            registerd_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            add_order_to_file(registerd_at, SHOPPING_CART,total)
            print(f"Compra finalizada. Total: S/{total:.2f}")
            clear_cart()
    except Exception as e:
        print("Error al finalizar la compra: {e}")




show_menu()
# show_catalog()
# os.system("clear")
# add_product_to_shopping_cart("A002")
remove_product_to_shopping_cart("A002")
clear_cart()
show_cart()
checkout()


def main():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            show_menu()
            option = input("Elige una opcion: ")

            if option == "1":
                show_catalog()
            elif option == "2":
                code = input("Ingrese el código del producto: ")
                quantity = input("Ingrese la cantidad del producto: ")
                add_product_to_shopping_cart(code,quantity)
            elif option == "3":
                code = input("Ingrese el código del producto a eliminar: ")
                remove_product_to_shopping_cart(code)
            elif option == "4":
                clear_cart()
            elif option == "5":
                show_cart()
            elif option == "6":
                checkout()
            elif option == "7":
                print("Hasta pronto 👋")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para confirmar...")
        
        except Exception as e:
            print("Error inesperado:  {e}")
            input("\nPresione Enter para confirmar...")







def add_order_to_file(registerd_at : datetime, list_products : List[Dict[str,Any]], total_price : float) -> None:
    try:
        complete_order = "=============================\n\n"
        complete_order += f"Fecha y hora: {registerd_at}\n\n"
        
        for prod in list_products:
            complete_order += f"{prod['quantity']}  |  {prod['name']}  |  S/{prod['price']:.2f}  |  S/{prod['price'] * prod['quantity']:.2f}\n"



        complete_order += f"\nTotal S/. {total_price:.2f}\n\n"
        complete_order += "=============================\n"
    except Exception as e:
        print("Error al guardar la orden")


    with open(FILE_NAME,'a') as archivo:
        archivo.write(complete_order)


# add_order_to_file(
#     "20-04-2025 10:56:50",
#     [{
#         "quantity": 1,
#         "code":"A001",
#         "name":"Pan",
#         "price":1.5
#     },
#     {
#         "quantity": 1,
#         "code":"A002",
#         "name":"Leche",
#         "price":2.5
#     }],
#     4.0
#     )

if __name__ == "__main__":
    main()