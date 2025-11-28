
from persistencia import cargar_datos
from menus import ejecutar_menu_principal


def main():
    habitaciones, usuarios = cargar_datos()
    ejecutar_menu_principal(habitaciones, usuarios)


if __name__ == "__main__":
    main()

def main():
    habitaciones, usuarios = cargar_datos()
    
   
    print(f"DEBUG: Se cargaron {len(habitaciones)} habitaciones y {len(usuarios)} usuarios.")
   
    
    ejecutar_menu_principal(habitaciones, usuarios)
