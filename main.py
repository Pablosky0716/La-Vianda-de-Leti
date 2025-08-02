import json
from datetime import datetime, timedelta
from utils.json_handler import cargar_json, guardar_json
from utils.pedidos import registrar_pedido, ver_historial

CONFIG_PATH = "config.json"
MENU_PATH = "menu.json"
PEDIDOS_PATH = "pedidos.json"
PAGOS_PATH = "pagos.json"

def cargar_config():
    return cargar_json(CONFIG_PATH)

def mostrar_menu_principal():
    while True:
        print("\n🙋‍♀️ Hola! soy el Bot de La Vianda de Leti")
        print("\n🍽️ Bienvenidos al Menú Principal")
        print("1️⃣ Ver menú del día siguiente")
        print("2️⃣ Realizar pedido")
        print("3️⃣ Ver historial de pedidos")
        print("4️⃣ Salir")

        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "1":
            dia_siguiente = obtener_dia_siguiente()
            mostrar_menu(dia_siguiente)

        elif opcion == "2":
            nombre = input("Tu nombre: ")
            opcion_pedido = input("Elegí opción (comun_1, comun_2, especial): ").strip()
            registrar_pedido(nombre, opcion_pedido, menu_path=MENU_PATH, pedidos_path=PEDIDOS_PATH)

        elif opcion == "3":
            ver_historial(pedidos_path=PEDIDOS_PATH)

        elif opcion == "4":
            print("👋 ¡Gracias por usar La Vianda de Leti!")
            break

        else:
            print("❗ Opción inválida. Intentá de nuevo.")    

def obtener_dia_siguiente():
    dias = {
        0: "lunes",
        1: "martes",
        2: "miercoles",
        3: "jueves",
        4: "viernes",
        5: "sabado",
        6: "lunes"
    }
    mañana = datetime.now() + timedelta(days=1)
    return dias[mañana.weekday()]
    
#def obtener_dia_actual():
    #dias = {
        #0: "lunes",
        #1: "martes",
        #2: "miercoles",
        #3: "jueves",
        #4: "viernes",
        #5: "sabado",
        #6: "domingo"
    #}
    #hoy = datetime.now().weekday()
    #return dias[hoy]


def mostrar_menu(dia, path_menu=MENU_PATH):
    menu = cargar_json(path_menu)
    dia = dia.lower()
    
    if dia in menu and menu[dia]:
        print(f"🍽️ Menú para {dia.capitalize()}:")
        print(f"1️⃣ {menu[dia].get('comun_1', 'No disponible')}")
        print(f"2️⃣ {menu[dia].get('comun_2', 'No disponible')}")
        print(f"⭐ Especial: {menu[dia].get('especial', 'No disponible')}")
    else:
        print(f"No hay menú cargado para {dia.capitalize()}.")

def cargar_menu_dia(dia):
    dia = dia.lower()
    menu = cargar_json(MENU_PATH)

    if dia not in menu:
        menu[dia] = {}

    print(f"Cargando menú para {dia.capitalize()}:")
    comun_1 = input("Plato común 1: ")
    comun_2 = input("Plato común 2: ")
    especial = input("Plato especial: ")

    menu[dia]["comun_1"] = comun_1
    menu[dia]["comun_2"] = comun_2
    menu[dia]["especial"] = especial

    guardar_json(MENU_PATH, menu)
    print(f"✅ Menú para {dia.capitalize()} guardado correctamente.")
    

def main():
    registrar_pedido("Pablo", "especial", menu_path=MENU_PATH, pedidos_path=PEDIDOS_PATH)
    config = cargar_config()
    print("Bienvenido a La Vianda de Leti 🍽️")
    print(f"Configuración cargada: {config['nombre_proyecto']}")
    mostrar_menu_principal()
    
    #dia_siguiente = obtener_dia_siguiente()
    #mostrar_menu(dia_siguiente)
    
if __name__ == "__main__":
    main()



