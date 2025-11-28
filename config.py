import json

FILE_HABITACIONES = 'habitaciones.json'
FILE_USUARIOS = 'usuarios.json'
FILE_FECHAS = 'fechas.json'

try:
    archivo = open(FILE_FECHAS, 'r', encoding='utf-8')
    contenido = archivo.read()
    archivo.close()
    datos = json.loads(contenido)
    FECHA_HOY = datos["fecha_sistema"]
except:
    FECHA_HOY = "03/10/2025"