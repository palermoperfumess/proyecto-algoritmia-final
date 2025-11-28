import json
import os
from typing import List, Dict
from config import FILE_HABITACIONES, FILE_USUARIOS

def crear_habitaciones() -> List[Dict]:
    """Crea la lista base de habitaciones si no existe el archivo."""
    habs = []
    for i in range(1, 26):
        codigo = "H" + ("00" + str(i))[-3:]
        if i <= 10:
            tipo = "Single"; ambientes = 1; capacidad = 1; precio = 60_000
        elif i <= 20:
            tipo = "Doble"; ambientes = 2; capacidad = 2; precio = 85_000
        else:
            tipo = "Suite"; ambientes = 3; capacidad = 4; precio = 140_000
        
        # Estructura de diccionario lista para JSON
        habs.append({
            "id": i, 
            "codigo": codigo, 
            "tipo": tipo, 
            "ambientes": ambientes,
            "capacidad": capacidad, 
            "precio": precio, 
            "reservas": []
        })
    return habs


def crear_usuarios_base() -> List[Dict]:
    """Crea usuarios por defecto."""
    return [
        {"id": 1, "nombre": "Ana Pérez", "dni": "30123456"},
        {"id": 2, "nombre": "Luis Gómez", "dni": "28999888"}
    ]


# ======================
# GUARDAR / CARGAR JSON
# ======================

def guardar_datos(habitaciones: List[Dict], usuarios: List[Dict]) -> None:
    try:
        # Guardar usuarios
        with open(FILE_USUARIOS, "w", encoding="utf-8") as f:
            # indent=4 hace que el JSON sea legible para humanos
            json.dump(usuarios, f, indent=4, ensure_ascii=False)

        # Guardar habitaciones (incluye las reservas anidadas automáticamente)
        with open(FILE_HABITACIONES, "w", encoding="utf-8") as f:
            json.dump(habitaciones, f, indent=4, ensure_ascii=False)

        print("\n[Datos guardados exitosamente en JSON.]")

    except Exception as e:
        print(f"[Error crítico al guardar JSON]: {e}")


def cargar_datos():
    habitaciones = []
    usuarios = []
    
    # Intentar cargar usuarios
    if os.path.exists(FILE_USUARIOS):
        try:
            with open(FILE_USUARIOS, "r", encoding="utf-8") as f:
                usuarios = json.load(f)
        except Exception as e:
            print(f"Error leyendo {FILE_USUARIOS}: {e}")
            usuarios = []
    
    # Intentar cargar habitaciones
    if os.path.exists(FILE_HABITACIONES):
        try:
            with open(FILE_HABITACIONES, "r", encoding="utf-8") as f:
                habitaciones = json.load(f)
        except Exception as e:
            print(f"Error leyendo {FILE_HABITACIONES}: {e}")
            habitaciones = []

    # Si no había datos o falló la carga, creamos los base
    if not usuarios:
        print("[No se encontraron usuarios. Creando base...]")
        usuarios = crear_usuarios_base()
        # Forzamos un guardado inicial
        guardar_datos(habitaciones if habitaciones else crear_habitaciones(), usuarios)
        
    if not habitaciones:
        print("[No se encontraron habitaciones. Creando base...]")
        habitaciones = crear_habitaciones()
        guardar_datos(habitaciones, usuarios)

    print("[Datos cargados exitosamente desde JSON.]")
    return habitaciones, usuarios