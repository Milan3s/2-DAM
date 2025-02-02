import csv

# Función para generar un ID único para cada registro.
def generar_id(contador):
    return f"film_{contador}"

# Función para convertir la cadena de actores separada por '-' a la estructura adecuada para Odoo.
def procesar_actores(actores_str):
    # Dividimos la cadena por el guion '-' para obtener cada actor.
    actores = actores_str.split('-')
    # Creamos una estructura que sigue el formato eval de Odoo.
    actores_refs = ", ".join([f"ref('{actor.strip()}')" for actor in actores])
    return f"[(6,0,[{actores_refs}])]"

# Función principal que transforma el CSV en el formato requerido por Odoo.
def transformar_csv_a_odoo(input_csv, output_xml):
    with open(input_csv, mode='r', newline='', encoding='utf-8') as archivo_csv:
        # Leemos el archivo CSV.
        lector_csv = csv.DictReader(archivo_csv)
        # Abrimos el archivo XML para escritura.
        with open(output_xml, mode='w', encoding='utf-8') as archivo_xml:
            # Añadimos cabecera del XML para asegurar que el archivo tiene el formato correcto.
            archivo_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            archivo_xml.write('<odoo>\n')
            archivo_xml.write('  <data>\n')
            
            contador = 1
            # Recorremos cada línea del archivo CSV.
            for linea in lector_csv:
                # Extraemos los valores del CSV usando las claves del DictReader.
                nombre = linea['name']
                director = linea['director']
                actores = procesar_actores(linea['actors'])
                release = linea['release']
                pais = linea['country']
                duracion = linea['duration']
                rating = linea['rating']
                archivo = linea['file']

                # Generamos el ID único para este registro.
                id_pelicula = generar_id(contador)

                # Escribimos el contenido en el archivo XML en el formato requerido por Odoo.
                archivo_xml.write(f'    <record id="{id_pelicula}" model="videoclub.peliculas">\n')
                archivo_xml.write(f'      <field name="name">{nombre}</field>\n')
                archivo_xml.write(f'      <field name="director" ref="{director}" />\n')
                archivo_xml.write(f'      <field name="actors" eval="{actores}" />\n')
                archivo_xml.write(f'      <field name="release">{release}</field>\n')
                archivo_xml.write(f'      <field name="country">{pais}</field>\n')
                archivo_xml.write(f'      <field name="duration">{duracion}</field>\n')
                archivo_xml.write(f'      <field name="rating">{rating}</field>\n')
                archivo_xml.write(f'      <field file="{archivo}" name="cover" type="base64" />\n')
                archivo_xml.write(f'    </record>\n\n')

                # Aumentamos el contador para el siguiente registro.
                contador += 1

            # Añadimos el cierre adecuado del archivo XML.
            archivo_xml.write('  </data>\n')
            archivo_xml.write('</odoo>\n')

# Función para probar el programa.
if __name__ == "__main__":
    # Archivo CSV de entrada.
    archivo_csv = 'peliculas.csv'
    # Archivo XML de salida.
    archivo_xml = 'peliculas_odoo.xml'

    try:
        # Llamamos a la función para transformar el CSV al formato Odoo.
        transformar_csv_a_odoo(archivo_csv, archivo_xml)
        print(f"Transformación completada. Los datos se guardaron en {archivo_xml}.")
    except FileNotFoundError:
        print("Error: El archivo CSV no fue encontrado.")
    except KeyError as e:
        print(f"Error: Falta la columna {e} en el CSV.")
    except Exception as e:
        print(f"Error inesperado: {e}")
