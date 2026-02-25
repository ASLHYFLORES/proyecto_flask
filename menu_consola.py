from logica import Inventario

def menu():
    inv = Inventario()
    while True:
        print("\n--- 🎂 MENÚ REPOSTERÍA (CONSOLA) ---")
        print("1. Mostrar Todo")
        print("2. Añadir Postre")
        print("3. Eliminar por ID")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            inv.cargar_desde_db()
            for p in inv.productos_dict.values():
                print(f"[{p.id}] {p.nombre} - ${p.precio} (Stock: {p.stock})")
        elif opcion == "2":
            n = input("Nombre: ")
            c = input("Categoría: ")
            s = int(input("Stock: "))
            p = float(input("Precio: "))
            inv.añadir(n, c, s, p)
        elif opcion == "3":
            id_p = int(input("ID a eliminar: "))
            inv.eliminar(id_p)
        elif opcion == "4":
            break

if __name__ == "__main__":
    menu()