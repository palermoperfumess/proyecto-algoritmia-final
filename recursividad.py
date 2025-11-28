# recursividad.py
from utilidades import comparar_fechas, parse_fecha_datetime
def buscar_reserva_en_fecha(reservas, fecha, i=0):
    """
    Devuelve la primera reserva activa en la fecha dada.
    Una reserva está activa si: entrada <= fecha < salida
    
    reservas: lista de diccionarios con claves 'entrada' y 'salida'
    fecha: string en formato 'dd/mm/aaaa', por ejemplo '02/10/2025'
    i: índice interno para la recursión (no hace falta pasar desde fuera)
    """
    if i >= len(reservas):
        return None

    reserva = reservas[i]
    
    # Verificar que existan las claves necesarias
    if 'entrada' not in reserva or 'salida' not in reserva:
        return buscar_reserva_en_fecha(reservas, fecha, i + 1)
    
    entrada = reserva['entrada']
    salida = reserva['salida']
    
    # Usamos comparar_fechas 
    try:
        if entrada and salida:
            # Verificar si la fecha está dentro del rango de la reserva
            if comparar_fechas(fecha, entrada) >= 0 and comparar_fechas(fecha, salida) < 0:
                return reserva
    except ValueError:
        # Si hay error en las fechas, continuar con la siguiente
        pass

    return buscar_reserva_en_fecha(reservas, fecha, i + 1)


def suma_recaudacion_recursiva(reservas, i=0):
    if i >= len(reservas):
        return 0

    reserva = reservas[i]
    
    # Verificar que existan las claves necesarias
    if 'precio_noche' not in reserva:
        return suma_recaudacion_recursiva(reservas, i + 1)
    
    precio_noche = reserva['precio_noche'] if reserva['precio_noche'] else 0
    
    # Calcular noches de la reserva
    noches = 0
    if 'entrada' in reserva and 'salida' in reserva:
        entrada = reserva['entrada']
        salida = reserva['salida']
        
        try:
            d_entrada = parse_fecha_datetime(entrada)
            d_salida = parse_fecha_datetime(salida)
            if d_entrada and d_salida:
                noches = (d_salida - d_entrada).days
        except:
            noches = 0
    
    total_reserva = precio_noche * noches
    return total_reserva + suma_recaudacion_recursiva(reservas, i + 1)


def contar_personas_recursivo(reservas, i=0):
    
    if i >= len(reservas):
        return 0

    reserva = reservas[i]
    
    # Verificar que exista la clave 'personas'
    if 'personas' not in reserva:
        return contar_personas_recursivo(reservas, i + 1)
    
    cant = reserva['personas'] if reserva['personas'] else 0
    return cant + contar_personas_recursivo(reservas, i + 1)


def contar_reservas_por_tipo(habitaciones, tipo_buscado, i=0):
    """
    Cuenta recursivamente cuántas reservas hay para un tipo específico de habitación.
    
    habitaciones: lista de diccionarios de habitaciones
    tipo_buscado: "Single", "Doble", o "Suite"
    i: índice interno para recursión
    """
    if i >= len(habitaciones):
        return 0
    
    hab = habitaciones[i]
    cantidad_actual = 0
    
    if 'tipo' in hab and hab['tipo'] == tipo_buscado:
        if 'reservas' in hab:
            cantidad_actual = len(hab['reservas'])
    
    return cantidad_actual + contar_reservas_por_tipo(habitaciones, tipo_buscado, i + 1)


def buscar_habitacion_recursiva(habitaciones, codigo, i=0):
    """
    Busca una habitación por código de forma recursiva.
    habitaciones: lista de habitaciones
    codigo: código a buscar (ej: "H001")
    i: índice interno
    """
    if i >= len(habitaciones):
        return None
    
    hab = habitaciones[i]
    
    if 'codigo' in hab:
        codigo_hab = hab['codigo'].upper()
        if codigo_hab == codigo.upper():
            return hab
    
    return buscar_habitacion_recursiva(habitaciones, codigo, i + 1)


def recorrido_basico(datos, fn):
    if isinstance(datos, dict):
        for clave in datos:
            valor = datos[clave]
            if isinstance(valor, (dict, list)):
                recorrido_basico(valor, fn)
            else:
                fn(valor)
    elif isinstance(datos, list):
        for elemento in datos:
            if isinstance(elemento, (dict, list)):
                recorrido_basico(elemento, fn)
            else:
                fn(elemento)
    else:
        fn(datos)


def validar_datos_recursivo(habitaciones):
    errores = []
    def validar_valor(valor):
        if valor is None or valor == "":
            errores.append("Valor vacío encontrado")
    
    recorrido_basico(habitaciones, validar_valor)
    
    return len(errores) == 0
def contar_reservas_totales_recursivo(habitaciones, i=0):
    """
    Cuenta el total de reservas en todas las habitaciones de forma recursiva.
    Alternativa a la función en estadisticas.py
    """
    if i >= len(habitaciones):
        return 0
    
    hab = habitaciones[i]
    cant_actual = 0
    
    if 'reservas' in hab:
        cant_actual = len(hab['reservas'])
    
    return cant_actual + contar_reservas_totales_recursivo(habitaciones, i + 1)


def buscar_reservas_por_usuario(habitaciones, nombre_usuario, i=0, resultado=None):
 
    if resultado is None:
        resultado = []
    
    if i >= len(habitaciones):
        return resultado
    
    hab = habitaciones[i]
    
    if 'reservas' in hab:
        for reserva in hab['reservas']:
            if 'usuario_nombre' in reserva:
                if reserva['usuario_nombre'].lower() == nombre_usuario.lower():
                    # Agregar código de habitación a la reserva para referencia
                    reserva_con_hab = reserva.copy()
                    if 'codigo' in hab:
                        reserva_con_hab['habitacion'] = hab['codigo']
                    resultado.append(reserva_con_hab)
    
    return buscar_reservas_por_usuario(habitaciones, nombre_usuario, i + 1, resultado)


# Ejemplos y pruebas (corren solo si ejecutás este archivo directamente)
if __name__ == '__main__':
    # Ejemplo con el formato real del proyecto
    reservas_ejemplo = [
        {
            'usuario_nombre': 'Ana Pérez',
            'entrada': '01/10/2025',
            'salida': '03/10/2025',
            'precio_noche': 60000,
            'personas': 2,
            'tipo': 'Single',
            'ambientes': 1,
            'pago': 'Efectivo'
        },
        {
            'usuario_nombre': 'Luis Gómez',
            'entrada': '05/10/2025',
            'salida': '08/10/2025',
            'precio_noche': 85000,
            'personas': 3,
            'tipo': 'Doble',
            'ambientes': 2,
            'pago': 'Tarjeta'
        },
    ]

    print('=== PRUEBAS DE FUNCIONES RECURSIVAS ===\n')
    
    print('1. Buscar reserva activa para 02/10/2025:')
    resultado = buscar_reserva_en_fecha(reservas_ejemplo, '02/10/2025')
    if resultado:
        print(f"   → Encontrada: {resultado['usuario_nombre']}, {resultado['entrada']} a {resultado['salida']}")
    else:
        print("   → No encontrada")
    
    print('\n2. Recaudación total (precio_noche * noches):')
    total = suma_recaudacion_recursiva(reservas_ejemplo)
    print(f"   → ${total:,.0f}")
    
    print('\n3. Total de personas en todas las reservas:')
    personas = contar_personas_recursivo(reservas_ejemplo)
    print(f"   → {personas} personas")
    
    print('\n4. Recorrido básico (mostrar todos los valores):')
    def mostrar(x):
        print(f'   → valor: {x}')
    
    datos_prueba = {'habitacion': 'H001', 'datos': [1, 2, {'precio': 60000}]}
    recorrido_basico(datos_prueba, mostrar)
    
    print('\n=== FIN DE PRUEBAS ===')