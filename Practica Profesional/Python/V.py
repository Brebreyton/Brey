
import os

def leer_factura(ruta_carpeta):
    resultados = {}  # Diccionario para almacenar las claves de cada archivo

    try:
        # Listar todos los archivos en la carpeta
        archivos = os.listdir(ruta_carpeta)

        for nombre_archivo in archivos:
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

            if os.path.isfile(ruta_completa):  # Verificar que es un archivo
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as archivo:
                        contenido = archivo.readlines()

                    for linea in contenido:
                        if "Clave Electrónica de Verificación" in linea:
                            clave_verificacion = linea.split(":")[-1].strip()
                            resultados[nombre_archivo] = clave_verificacion
                            break  # Sale del bucle si encuentra la clave
                    else:
                        resultados[nombre_archivo] = "Clave Electrónica de Verificación no encontrada."
                except Exception as e:
                    resultados[nombre_archivo] = f"Ocurrió un error al leer el archivo: {e}"

    except FileNotFoundError:
        return "No encontrada."

    return resultados


ruta_carpeta = r'C:\\Users\\practicante5\\Desktop\\Facturas'  # Cambia por la ruta
resultados = leer_factura(ruta_carpeta)

# Mostrar resultados
for archivo, clave in resultados.items():
    with open ("Claves.txt", 'a', )as archivo:
        archivo.write(f'Clave Electrónica: {clave}\n\n')
    #print(f"Clave Electrónica: {clave}")







































