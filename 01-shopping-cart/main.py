import os

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

SHOPPING_CAR = []


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
        print(f" {product["code"]} | {product["name"]}{" "*(20-len(product["name"]))} | {product["price"]}")


def add_product_to_shopping_car(code_product):
    for product in WAREHOUSE:
        if code_product == product["code"]:
            SHOPPING_CAR.append(product)
            print(f"✔ El Producto {product["code"]} fue agregado al carrito.")
            break



# show_menu()
# show_catalog()
os.system("clear")
add_product_to_shopping_car("A002")