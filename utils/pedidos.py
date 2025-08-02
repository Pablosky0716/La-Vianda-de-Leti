from datetime import datetime
from utils.json_handler import cargar_json, guardar_json

def registrar_pedido(nombre, opcion, dia=None, menu_path="menu.json", pedidos_path="pedidos.json"):
    if dia is None:
        dia = datetime.now().strftime("%Y-%m-%d")

    pedidos = cargar_json(pedidos_path)
    menu = cargar_json(menu_path)
    
    # Calcular el día siguiente (nombre del día)
    dia_semana = datetime.now().weekday()
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    nombre_dia = dias[dia_semana + 1 if dia_semana < 6 else 0]  # si es sábado, va a lunes

    # Validar que el menú y la opción existan
    if nombre_dia not in menu or opcion not in menu[nombre_dia]:
        print("❌ No se puede registrar el pedido. Menú u opción inválida.")
        return

    plato = menu[nombre_dia][opcion]

    if dia not in pedidos:
        pedidos[dia] = {}

    pedidos[dia][nombre] = {
        "opcion": opcion,
        "plato": plato,
        "pagado": False
    }

    guardar_json(pedidos_path, pedidos)
    print(f"✅ Pedido registrado para {nombre}: {plato} ({opcion})")

def ver_historial(pedidos_path="pedidos.json"):
    pedidos = cargar_json(pedidos_path)

    if not pedidos:
        print("📭 No hay pedidos registrados.")
        return

    for fecha, clientes in pedidos.items():
        print(f"\n📅 {fecha}:")
        for cliente, datos in clientes.items():
            estado = "Pagado ✅" if datos["pagado"] else "Pendiente 💸"
            print(f"- {cliente}: {datos['plato']} ({datos['opcion']}) → {estado}")
